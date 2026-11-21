"""Blind hand-labelling check of the LLM judge on a random sample of pilot answers.

The reference labels were drafted with AI help, so agreement between them and the
Gemini judge does not show that the judge matches a human. This script draws a random
sample of answerable-question answers (equal numbers per system), hides which system
wrote each answer and what the judge and reference labels said, and lets me label them
by hand. It then reports Cohen's kappa of the judge (and of the reference labels)
against my blind labels.

Labels: CORRECT (matches the gold answer), PARTIAL (right but incomplete),
WRONG (contradicts the gold answer, or declines/escalates although the question is answerable).

Steps:
  1. python -m eval.blind_check make    -> eval/labels/blind_check_sheet.csv (fill my_label)
  2. python -m eval.blind_check score   -> eval/results/blind_check.md
Usage: python -m eval.blind_check make|score
"""
import csv
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANSWERS = ROOT / "eval/results/pilot_answers.jsonl"
QUESTIONS = ROOT / "eval/pilot_questions.csv"
JUDGE = ROOT / "eval/results/pilot_judgements.csv"
REFERENCE = ROOT / "eval/labels/pilot_manual_labels.csv"
SHEET = ROOT / "eval/labels/blind_check_sheet.csv"
REPORT = ROOT / "eval/results/blind_check.md"

SEED = 2026          # fixed so the same sample is rebuilt when scoring
PER_SYSTEM = 10      # 10 answers each from S1, S2 and S3 = 30
LABELS = {"CORRECT", "PARTIAL", "WRONG"}


def sample():
    """Return the fixed random sample as a list of answer dicts, in shuffled order."""
    answers = [json.loads(l) for l in open(ANSWERS, encoding="utf-8")]
    rng = random.Random(SEED)
    picked = []
    for system in ("S1", "S2", "S3"):
        pool = [a for a in answers if a["system"] == system and a["answerable"] == "yes"]
        picked += rng.sample(pool, PER_SYSTEM)
    rng.shuffle(picked)
    return picked


def make():
    """Write the blind sheet: no system name, no judge or reference label."""
    quotes = {r["qid"]: r["gold_quote"] for r in csv.DictReader(open(QUESTIONS, encoding="utf-8"))}
    with open(SHEET, "w", encoding="utf-8-sig", newline="") as f:  # BOM so Excel shows symbols correctly
        w = csv.writer(f)
        w.writerow(["item", "question", "gold_answer", "gold_quote", "answer", "my_label", "my_note"])
        for i, a in enumerate(sample(), 1):
            w.writerow([i, a["question"], a["gold_answer"], quotes.get(a["qid"], ""), a["answer"], "", ""])
    print(f"Wrote {SHEET} ({PER_SYSTEM * 3} items). Fill my_label with CORRECT, PARTIAL or WRONG.")


def kappa_line(name, pairs):
    from sklearn.metrics import cohen_kappa_score
    agree = sum(a == b for a, b in pairs)
    k = cohen_kappa_score([a for a, _ in pairs], [b for _, b in pairs])
    return f"- {name}: {agree}/{len(pairs)} agree ({agree / len(pairs):.0%}), Cohen's kappa {k:.2f}"


def score():
    """Compare my blind labels with the judge and with the reference labels."""
    mine = list(csv.DictReader(open(SHEET, encoding="utf-8-sig")))
    if len(mine) != PER_SYSTEM * 3:
        sys.exit(f"Expected {PER_SYSTEM * 3} rows in {SHEET}, found {len(mine)}: rebuild it with 'make'.")
    bad = [r["item"] for r in mine if r["my_label"].strip().upper() not in LABELS]
    if bad:
        sys.exit(f"Items without a valid label (CORRECT/PARTIAL/WRONG): {', '.join(bad)}")
    judge = {(r["qid"], r["system"]): r["judge_label"] for r in csv.DictReader(open(JUDGE, encoding="utf-8"))}
    ref = {(r["qid"], r["system"]): r["label"].replace("ESCALATED", "WRONG")
           for r in csv.DictReader(open(REFERENCE, encoding="utf-8"))}
    rows = []
    for r, a in zip(mine, sample()):
        key = (a["qid"], a["system"])
        rows.append((key, r["my_label"].strip().upper(), judge[key], ref[key]))

    lines = ["# Blind hand-label check of the LLM judge", "",
             f"- Sample: {len(rows)} answers to answerable pilot questions, {PER_SYSTEM} each from S1, S2, S3 "
             f"(random, seed {SEED}), labelled by hand without seeing the system, judge or reference label.", "",
             kappa_line("Judge vs my blind labels", [(m, j) for _, m, j, _ in rows]),
             kappa_line("Reference labels vs my blind labels", [(m, r) for _, m, _, r in rows])]
    for system in ("S1", "S2", "S3"):
        sub = [(m, j) for k, m, j, _ in rows if k[1] == system]
        lines.append(f"- {system}: judge agrees with me on {sum(a == b for a, b in sub)}/{len(sub)}")
    diffs = [f"{k[0]}/{k[1]} (me {m}, judge {j}, reference {r})" for k, m, j, r in rows if m != j or m != r]
    lines += ["", "Disagreements: " + ("; ".join(diffs) if diffs else "none"), "",
              "Small sample: indicative only."]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    {"make": make, "score": score}.get(sys.argv[1] if len(sys.argv) > 1 else "", lambda: sys.exit(__doc__))()
