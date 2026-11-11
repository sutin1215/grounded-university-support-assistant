"""Project the API cost of the Semester 2 evaluation from the costs measured in the pilot.

Measured per call (eval/results): S2 and S3 answers (pilot_answers.jsonl), judge calls (the cache records
whose keys are not in the answers or signal files), and S4 model-signal calls (from the cache via
eval/model_signal.py). The plan sizes below follow D1 Section 3.5: 200 questions (60 development, 140 test);
E2 runs on the development set only and its retrieval metrics (hit@k, MRR) need no LLM call.

Output: eval/results/cost_projection.md
Usage:  python -m eval.cost_projection
"""
import json
import statistics
import sys

from src.config import load_config

PLAN = {"questions": 200, "dev": 60, "e2_configs": 12, "rm_per_usd": 4.50}


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    cfg = load_config()
    answers = [json.loads(l) for l in open(cfg["results_dir"] / "pilot_answers.jsonl", encoding="utf-8")]
    per = {s: statistics.mean(a["cost_usd"] for a in answers if a["system"] == s) for s in ("S2", "S3")}
    cache = [json.loads(l)["result"] for l in open(cfg["cache_path"], encoding="utf-8")]
    # Judge and signal calls are identified by their output: the judge replies with "LABEL:", the signal with a number.
    judge = [r["cost_usd"] for r in cache if r["text"].lstrip().upper().startswith("LABEL:")]
    signal = [r["cost_usd"] for r in cache if r["text"].strip().isdigit()]
    per["judge"], per["signal"] = statistics.mean(judge), statistics.mean(signal)
    q, dev, n_cfg = PLAN["questions"], PLAN["dev"], PLAN["e2_configs"]
    items = [
        ("E1: S2 and S3 answer all questions", q * (per["S2"] + per["S3"])),
        (f"E2: {n_cfg} retrieval configurations answered by S3 on the {dev} development questions", n_cfg * dev * per["S3"]),
        ("E3: one model-signal call per question for S4", q * per["signal"]),
        ("Judge: every LLM answer above (S1 answers judged too)", (3 * q + n_cfg * dev + q) * per["judge"]),
    ]
    total = sum(c for _, c in items)
    lines = ["# Cost projection for the Semester 2 evaluation", "",
             f"Measured mean cost per call (US$): S2 {per['S2']:.5f}, S3 {per['S3']:.5f}, judge {per['judge']:.5f} "
             f"({len(judge)} calls), model signal {per['signal']:.5f} ({len(signal)} calls).", "",
             "| Item | US$ |", "|---|---|"]
    lines += [f"| {name} | {c:.2f} |" for name, c in items]
    lines += [f"| **Total** | **{total:.2f}** (RM{total * PLAN['rm_per_usd']:.0f} at RM{PLAN['rm_per_usd']:.2f} per US$) |", "",
              "Retrieval-only metrics in E2 need no LLM calls. Reruns are free because every response is cached."]
    out = cfg["results_dir"] / "cost_projection.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
