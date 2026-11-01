"""Gemini client used by S2, S3, S4 and the LLM judge.

- Reads GEMINI_API_KEY from .env (never committed).
- Caches every response in data/cache/llm_cache.jsonl, keyed by model, settings and prompt,
  so a rerun gives exactly the same answers at no cost (reproducibility, NF2).
- Records tokens, latency and estimated cost for every call (NF4, NF5).
- Retries with back-off on rate limits and temporary errors, and paces requests.
"""
import hashlib
import json
import os
import time
from dataclasses import asdict, dataclass

from dotenv import load_dotenv

from src.config import ROOT


@dataclass
class LLMResult:
    text: str
    model: str
    input_tokens: int
    output_tokens: int       # visible answer tokens + thinking tokens (both are billed)
    latency_s: float         # wall-clock time of the original (uncached) call
    cost_usd: float
    cached: bool


class GeminiClient:
    def __init__(self, cfg, model: str | None = None):
        from google import genai  # imported here so modules that do not call the LLM stay light
        from google.genai import types

        load_dotenv(ROOT / ".env")
        key = os.environ.get("GEMINI_API_KEY", "").strip()
        if not key:
            raise SystemExit("GEMINI_API_KEY missing: add it to .env in the repository root.")
        llm = cfg["llm"]
        self.model = model or llm["model"]
        self.temperature = llm["temperature"]
        self.max_tokens = llm["max_output_tokens"]
        self.price_in = llm["price_input_per_m"] / 1e6
        self.price_out = llm["price_output_per_m"] / 1e6
        self.min_interval = 60.0 / llm["requests_per_minute"]
        self.types = types
        self.client = genai.Client(api_key=key)
        self.cache_path = cfg["cache_path"]
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self.cache = {}
        if self.cache_path.exists():
            with open(self.cache_path, encoding="utf-8") as f:
                for line in f:
                    rec = json.loads(line)
                    self.cache[rec["key"]] = rec["result"]
        self._last_call = 0.0

    def _key(self, system: str, prompt: str) -> str:
        raw = json.dumps([self.model, self.temperature, self.max_tokens, system, prompt])
        return hashlib.sha256(raw.encode()).hexdigest()

    def generate(self, prompt: str, system: str = "") -> LLMResult:
        key = self._key(system, prompt)
        if key in self.cache:
            return LLMResult(**{**self.cache[key], "cached": True})
        config = self.types.GenerateContentConfig(
            temperature=self.temperature, max_output_tokens=self.max_tokens,
            system_instruction=system or None)
        for attempt in range(6):
            wait = self.min_interval - (time.monotonic() - self._last_call)
            if wait > 0:
                time.sleep(wait)
            self._last_call = time.monotonic()
            try:
                start = time.perf_counter()
                resp = self.client.models.generate_content(model=self.model, contents=prompt, config=config)
                latency = time.perf_counter() - start
                break
            except Exception as e:  # rate limit (429) or overload (503): back off and retry
                msg = str(e)
                if attempt == 5 or not any(c in msg for c in ("429", "503", "500", "UNAVAILABLE", "RESOURCE_EXHAUSTED")):
                    raise
                time.sleep(min(60, 5 * 2 ** attempt))
        usage = resp.usage_metadata
        tin = usage.prompt_token_count or 0
        tout = (usage.candidates_token_count or 0) + (getattr(usage, "thoughts_token_count", 0) or 0)
        result = LLMResult(text=(resp.text or "").strip(), model=self.model, input_tokens=tin,
                           output_tokens=tout, latency_s=round(latency, 3),
                           cost_usd=tin * self.price_in + tout * self.price_out, cached=False)
        record = asdict(result)
        record.pop("cached")
        self.cache[key] = record
        with open(self.cache_path, "a", encoding="utf-8") as f:
            f.write(json.dumps({"key": key, "result": record}) + "\n")
        return result
