"""S4 pilot: can simple retrieval signals tell answerable from unanswerable questions?

For each pilot question, records the top retrieval score from each method and measures how
well it separates answerable from unanswerable questions (AUROC: 1.0 = perfect, 0.5 = chance).
This tests the assumption behind S4 before it is built: that a low retrieval score is a
usable signal for escalating instead of answering.

If eval/results/model_signal.csv exists (python -m eval.model_signal), the LLM's sufficiency score is
compared too. Each AUROC has a bootstrap 95% interval, because the unanswerable group is small.

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


def bootstrap_auc(y, scores, n=2000, seed=0):
    """95% percentile interval for the AUROC, resampling questions with replacement (fixed seed)."""
    rng = np.random.default_rng(seed)
    aucs = []
    for _ in range(n):
        i = rng.integers(0, len(y), len(y))
        if 0 < y[i].sum() < len(i):  # a resample needs both classes
            aucs.append(roc_auc_score(y[i], scores[i]))
    return np.percentile(aucs, 2.5), np.percentile(aucs, 97.5)


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

    cols = ["bm25_stem_top", "bm25_stem_gap", "dense_top", "dense_gap"]
    model_path = cfg["results_dir"] / "model_signal.csv"
    if model_path.exists():
        with open(model_path, encoding="utf-8") as f:
            model = {r["qid"]: r["model_score"] for r in csv.DictReader(f)}
        for r in rows:
            r["model_score"] = int(model[r["qid"]]) if model.get(r["qid"], "") != "" else ""
        cols.append("model_score")
        rows = [r for r in rows if r["model_score"] != ""]  # compare all signals on the same questions

    y = [1 if r["answerable"] == "yes" else 0 for r in rows]
    out = cfg["results_dir"]
    with open(out / "confidence_pilot.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    lines = ["# S4 pilot: escalation signals", "",
             f"{sum(y)} answerable and {len(y) - sum(y)} unanswerable questions. "
             "AUROC = chance that a random answerable question scores higher than a random unanswerable one.", "",
             "| Signal | AUROC | Bootstrap 95% CI | Mean (answerable) | Mean (unanswerable) |", "|---|---|---|---|---|"]
    for c in cols:
        vals = np.array([r[c] for r in rows], dtype=float)
        auc = roc_auc_score(y, vals)
        lo, hi = bootstrap_auc(np.array(y), vals)
        lines.append(f"| {c} | {auc:.2f} | {lo:.2f}-{hi:.2f} | {vals[np.array(y) == 1].mean():.3f} | "
                     f"{vals[np.array(y) == 0].mean():.3f} |")
    lines += ["", f"Only {len(y) - sum(y)} unanswerable questions: indicative only; the wide intervals show the uncertainty."]
    (out / "confidence_pilot.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    for r in sorted(rows, key=lambda r: r["dense_top"]):
        print(f"{r['qid']:>4} {r['answerable']:>3}  dense={r['dense_top']:.3f}  bm25={r['bm25_stem_top']:.2f}  {r['question'][:60]}")


if __name__ == "__main__":
    main()
