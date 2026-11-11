"""S4 pilot: the model signal. Asks the LLM whether S3's retrieved passages are enough to answer.

For each pilot question, retrieves the same top-k passages as S3 (hybrid search), shows them to the
LLM with the signal prompt in configs/prompts.yaml, and records its 0-100 sufficiency score. The model
is told not to answer the question. eval/confidence_pilot.py then compares this score with the
retrieval signals (AUROC). Calls are cached like all other LLM calls.

Output: eval/results/model_signal.csv
Usage:  python -m eval.model_signal
"""
import csv
import re
import sys

from eval.run_pilot import load_questions
from src.config import load_config
from src.llm import GeminiClient
from src.retrieve import build, load_chunks
from src.systems import S3RAG, load_prompts


def parse_score(text: str):
    """The first whole number in the reply, if it is between 0 and 100; otherwise None."""
    m = re.search(r"\d+", text)
    return int(m.group()) if m and 0 <= int(m.group()) <= 100 else None


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    cfg = load_config()
    prompts = load_prompts()
    llm = GeminiClient(cfg)
    retriever = build(cfg["retrieval"]["s3_method"], load_chunks(cfg), cfg)
    k = cfg["retrieval"]["top_k"]
    rows, cost = [], 0.0
    for q in load_questions(cfg):
        hits = retriever.search(q["question"], k)
        prompt = prompts["signal_user"].format(passages=S3RAG.format_passages(hits), question=q["question"])
        r = llm.generate(prompt, system=prompts["signal_system"])
        cost += r.cost_usd
        score = parse_score(r.text)
        rows.append({"qid": q["qid"], "answerable": q["answerable"],
                     "model_score": "" if score is None else score, "reply": r.text[:80]})
        print(f"{q['qid']:>4} {q['answerable']:>3}  model={score}", flush=True)
    path = cfg["results_dir"] / "model_signal.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    unparsed = sum(r["model_score"] == "" for r in rows)
    print(f"Saved {len(rows)} scores to {path} ({unparsed} unparsed); cost US${cost:.4f}")


if __name__ == "__main__":
    main()
