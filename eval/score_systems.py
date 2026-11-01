"""Score the S1-S3 pilot answers and write the summary used in the D1 Feasibility section.

Inputs:
  eval/results/pilot_answers.jsonl        answers from eval/run_systems.py
  eval/labels/pilot_manual_labels.csv     manual labels (primary)
  eval/results/pilot_judgements.csv       LLM-judge labels (checked against manual labels)

Manual labels:
  answerable questions:   CORRECT, PARTIAL, WRONG, ESCALATED (declined although answerable)
  unanswerable questions: DECLINED, ANSWERED

Output: eval/results/pilot_systems_summary.md
Usage:  python -m eval.score_systems
"""
import csv
import json
import statistics
import sys
from collections import Counter

from sklearn.metrics import cohen_kappa_score

from src.config import ROOT, load_config


def read_csv(path):
    with open(path, encoding="utf-8") as f:
        return {(r["qid"], r["system"]): r for r in csv.DictReader(f)}


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    cfg = load_config()
    res = cfg["results_dir"]
    answers = [json.loads(l) for l in open(res / "pilot_answers.jsonl", encoding="utf-8")]
    manual = read_csv(ROOT / "eval" / "labels" / "pilot_manual_labels.csv")
    judge = read_csv(res / "pilot_judgements.csv") if (res / "pilot_judgements.csv").exists() else {}
    systems = sorted({a["system"] for a in answers})
    n_ans = len({a["qid"] for a in answers if a["answerable"] == "yes"})
    n_un = len({a["qid"] for a in answers if a["answerable"] == "no"})

    lines = [f"# S1-S3 pilot results", "",
             f"{n_ans} answerable and {n_un} unanswerable questions; 5 official documents; "
             f"LLM {cfg['llm']['model']} (temperature {cfg['llm']['temperature']}); "
             f"S3 retrieves the top {cfg['retrieval']['top_k']} passages with {cfg['retrieval']['s3_method']} search. "
             "Labels are manual; see the agreement section for the LLM judge.", "",
             "| System | Correct | Partial | Wrong | Escalated (answerable) | Declined (unanswerable) | Answered (unanswerable) |",
             "|---|---|---|---|---|---|---|"]
    per_system = {}
    for s in systems:
        rows = [a for a in answers if a["system"] == s]
        lab = Counter(manual[(a["qid"], s)]["label"] for a in rows)
        per_system[s] = lab
        lines.append(f"| {s} | {lab['CORRECT']}/{n_ans} | {lab['PARTIAL']}/{n_ans} | {lab['WRONG']}/{n_ans} | "
                     f"{lab['ESCALATED']}/{n_ans} | {lab['DECLINED']}/{n_un} | {lab['ANSWERED']}/{n_un} |")

    # Citations (S3): does an answered, answerable question cite the gold document and page?
    s3 = [a for a in answers if a["system"] == "S3" and a["answerable"] == "yes" and not a["abstained"]]
    supported = 0
    for a in s3:
        pages = {int(p) for p in a["gold_page"].split(";") if p}
        supported += any(c["doc"] == a["gold_doc"] and c["page"] in pages for c in a["citations"])
    with_cit = sum(bool(a["citations"]) for a in s3)
    lines += ["", "## Citations (S3)", "",
              f"- Answered answerable questions: {len(s3)}",
              f"- With at least one citation: {with_cit}/{len(s3)}",
              f"- Citing the gold document and page: {supported}/{len(s3)}"]

    # Cost and latency (uncached latency is stored even for cached reruns)
    lines += ["", "## Cost and latency per question", "",
              "| System | Median latency (s) | Mean input tokens | Mean output tokens | Cost per question (US$) |",
              "|---|---|---|---|---|"]
    for s in systems:
        rows = [a for a in answers if a["system"] == s]
        lat = [a["latency_s"] for a in rows]
        cost = statistics.mean(a["cost_usd"] for a in rows)
        lines.append(f"| {s} | {statistics.median(lat):.2f} | {statistics.mean(a['input_tokens'] for a in rows):.0f} | "
                     f"{statistics.mean(a['output_tokens'] for a in rows):.0f} | {cost:.5f} |")
    llm_cost = sum(a["cost_usd"] for a in answers)
    lines += ["", f"Total pilot generation cost at paid-tier prices: US${llm_cost:.4f}. "
              f"Projected for 200 questions x 2 LLM systems: US${llm_cost / (n_ans + n_un) * 200:.2f} "
              "(S4 adds roughly one S3-sized call per question)."]

    # Judge agreement
    if judge:
        pairs = [(m["label"].replace("ESCALATED", "WRONG"), judge[k]["judge_label"])
                 for k, m in manual.items() if k in judge and judge[k]["judge_label"] != "UNPARSED"]
        agree = sum(a == b for a, b in pairs)
        kappa = cohen_kappa_score([a for a, _ in pairs], [b for _, b in pairs])
        lines += ["", "## LLM judge vs manual labels", "",
                  f"- Items compared: {len(pairs)}", f"- Exact agreement: {agree}/{len(pairs)} ({agree / len(pairs):.0%})",
                  f"- Cohen's kappa: {kappa:.2f} (threshold for using the judge: 0.60)"]
        disagreements = [k for k, m in manual.items() if k in judge and
                         m["label"].replace("ESCALATED", "WRONG") != judge[k]["judge_label"]]
        if disagreements:
            lines.append("- Disagreements: " + ", ".join(f"{q}/{s} (manual {manual[(q, s)]['label']}, "
                                                           f"judge {judge[(q, s)]['judge_label']})" for q, s in disagreements))
    lines += ["", "Pilot set only (26 questions): indicative, not final results."]
    (res / "pilot_systems_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
