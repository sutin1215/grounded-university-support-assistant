"""The systems compared in the project, behind one interface: answer(question) -> dict.

  S1  FAQ baseline (no LLM)                      src/faq_baseline.py
  S2  Plain LLM: Gemini answers from its own knowledge
  S3  RAG: retrieve passages, Gemini answers only from them with [n] citations
  S4  (Week 8+) S3 plus a confidence check that escalates instead of answering

Prompts live in configs/prompts.yaml.

Usage (demo):  python -m src.systems S3 "How many times can I resit a course?"
"""
import re
import sys

import yaml

from src.config import ROOT, load_config
from src.faq_baseline import ESCALATE, FAQBaseline, load_faq
from src.llm import GeminiClient
from src.retrieve import build, load_chunks

NOT_FOUND = "NOT_FOUND"


def load_prompts() -> dict:
    with open(ROOT / "configs" / "prompts.yaml", encoding="utf-8") as f:
        p = yaml.safe_load(f)
    role = p["role"]
    for key in ("s2_system", "s3_system"):
        p[key] = p[key].replace("{role}", role)
    return p


class S1FAQ:
    name = "S1"

    def __init__(self, cfg):
        self.bot = FAQBaseline(load_faq(cfg), cfg["faq_baseline"]["min_similarity"])

    def answer(self, question):
        out = self.bot.answer(question)
        return {"system": self.name, "answer": out["answer"], "abstained": out["faq_id"] == ESCALATE,
                "faq_id": out["faq_id"], "confidence": out["similarity"], "citations": [],
                "input_tokens": 0, "output_tokens": 0, "latency_s": 0.0, "cost_usd": 0.0}


class S2PlainLLM:
    name = "S2"

    def __init__(self, cfg, llm, prompts):
        self.llm, self.prompts = llm, prompts

    def answer(self, question):
        r = self.llm.generate(question, system=self.prompts["s2_system"])
        return {"system": self.name, "answer": r.text, "abstained": None, "citations": [],
                "input_tokens": r.input_tokens, "output_tokens": r.output_tokens,
                "latency_s": r.latency_s, "cost_usd": r.cost_usd}


class S3RAG:
    name = "S3"

    def __init__(self, cfg, llm, prompts, chunks):
        self.llm, self.prompts = llm, prompts
        self.k = cfg["retrieval"]["top_k"]
        self.retriever = build(cfg["retrieval"]["s3_method"], chunks, cfg)

    @staticmethod
    def format_passages(hits):
        return "\n\n".join(f"[{i}] ({h['doc']}, page {h['page']})\n{' '.join(h['text'].split())}"
                           for i, h in enumerate(hits, start=1))

    def answer(self, question):
        hits = self.retriever.search(question, self.k)
        prompt = self.prompts["s3_user"].format(passages=self.format_passages(hits), question=question)
        r = self.llm.generate(prompt, system=self.prompts["s3_system"])
        abstained = r.text.strip().upper().startswith(NOT_FOUND)
        cited = sorted({int(n) for n in re.findall(r"\[(\d+)\]", r.text) if 1 <= int(n) <= len(hits)})
        return {"system": self.name,
                "answer": " ".join(self.prompts["abstain_message"].split()) if abstained else r.text,
                "abstained": abstained,
                "citations": [{"n": n, "doc": hits[n - 1]["doc"], "page": hits[n - 1]["page"]} for n in cited],
                "retrieved": [{"doc": h["doc"], "page": h["page"], "score": round(h["score"], 5)} for h in hits],
                "input_tokens": r.input_tokens, "output_tokens": r.output_tokens,
                "latency_s": r.latency_s, "cost_usd": r.cost_usd}


def build_systems(cfg, names=("S1", "S2", "S3")):
    prompts = load_prompts()
    llm = GeminiClient(cfg) if {"S2", "S3"} & set(names) else None
    chunks = load_chunks(cfg) if "S3" in names else None
    makers = {"S1": lambda: S1FAQ(cfg), "S2": lambda: S2PlainLLM(cfg, llm, prompts),
              "S3": lambda: S3RAG(cfg, llm, prompts, chunks)}
    return {n: makers[n]() for n in names}


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    name, question = sys.argv[1], " ".join(sys.argv[2:])
    system = build_systems(load_config(), (name,))[name]
    out = system.answer(question)
    print(f"{name}: {out['answer']}")
    for c in out["citations"]:
        print(f"  [{c['n']}] {c['doc']}, page {c['page']}")


if __name__ == "__main__":
    main()
