"""Check that the Gemini API key in .env works.

Makes one tiny request and prints the model, response time and token counts.
If the default model name is not available, it lists the models your key can use.

Usage:  python tools/check_gemini.py
"""
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai

ROOT = Path(__file__).resolve().parents[1]
MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.6-flash")


def main():
    load_dotenv(ROOT / ".env")
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key:
        sys.exit("No GEMINI_API_KEY found in .env (it must be in the repo's top folder).")
    print(f"Key found ({len(key)} characters). Testing model: {MODEL}")
    client = genai.Client(api_key=key)
    try:
        start = time.perf_counter()
        resp = client.models.generate_content(model=MODEL, contents="Reply with exactly: OK")
        secs = time.perf_counter() - start
    except Exception as e:  # show the reason, then list what the key can use
        print(f"\nRequest failed: {e}\n")
        print("Models available to this key:")
        for m in client.models.list():
            if "generateContent" in (getattr(m, "supported_actions", None) or []):
                print("  ", m.name)
        sys.exit(1)
    usage = resp.usage_metadata
    print(f"Reply: {resp.text.strip()!r}")
    print(f"Time: {secs:.2f} s")
    print(f"Tokens: {usage.prompt_token_count} in, {usage.candidates_token_count} out")
    print("\nThe key works.")


if __name__ == "__main__":
    main()
