"""S4 pilot: can simple retrieval signals tell answerable from unanswerable questions?

For each pilot question, records the top retrieval score from each method and measures how
well it separates answerable from unanswerable questions (AUROC: 1.0 = perfect, 0.5 = chance).
This tests the assumption behind S4 before it is built: that a low retrieval score is a
usable signal for escalating instead of answering.

Output: eval/results/confidence_pilot.csv and eval/results/confidence_pilot.md

Usage:  python -m eval.confidence_pilot
"""
import csv
import sys

import numpy as np
from sklearn.metrics import roc_auc_score

from eval.run_pilot import load_questions
from src.config import load_config
from src.retrieve import DenseRetriever, StemmedBM25Retriever, load_chunks


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    cfg = load_config()
    chunks = load_chunks(cfg)
    questions = load_questions(cfg)
    signals = {"bm25_stem_top": StemmedBM25Retriever(chunks, cfg), "dense_top": DenseRetriever(chunks, cfg)}
    rows = []
    for q in questions:
        row = {"qid": q["qid"], "answerable": q["answerable"], "question": q["question"]}
        for name, r in signals.items():
            s = np.sort(np.asarray(r.scores(q["question"])))[::-1]
            row[name] = round(float(s[0]), 4)
            row[name.replace("_top", "_gap")] = round(float(s[0] - s[1]), 4)  # margin over the runner-up
        rows.append(row)

    y = [1 if r["answerable"] == "yes" else 0 for r in rows]
    cols = ["bm25_stem_top", "bm25_stem_gap", "dense_top", "dense_gap"]
    out = cfg["results_dir"]
    with open(out / "confidence_pilot.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    lines = ["# S4 pilot: retrieval scores as an escalation signal", "",
             f"{sum(y)} answerable and {len(y) - sum(y)} unanswerable questions. "
             "AUROC = chance that a random answerable question scores higher than a random unanswerable one.", "",
             "| Signal | AUROC | Mean (answerable) | Mean (unanswerable) |", "|---|---|---|---|"]
    for c in cols:
        vals = np.array([r[c] for r in rows])
        auc = roc_auc_score(y, vals)
        lines.append(f"| {c} | {auc:.2f} | {vals[np.array(y) == 1].mean():.3f} | {vals[np.array(y) == 0].mean():.3f} |")
    lines += ["", "Only 6 unanswerable questions: indicative only."]
    (out / "confidence_pilot.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    for r in sorted(rows, key=lambda r: r["dense_top"]):
        print(f"{r['qid']:>4} {r['answerable']:>3}  dense={r['dense_top']:.3f}  bm25={r['bm25_stem_top']:.2f}  {r['question'][:60]}")


if __name__ == "__main__":
    main()
