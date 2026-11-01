"""LLM judge: label every pilot answer as CORRECT / PARTIAL / WRONG (answerable questions)
or DECLINED / ANSWERED (unanswerable questions), using the gold answer as reference.

The judge's labels are compared with manual labels (eval/labels/pilot_manual_labels.csv)
before they are trusted, because LLM judges have known biases (Zheng et al. 2023).

Output: eval/results/pilot_judgements.csv
Usage:  python -m eval.judge
"""
import csv
import json
import re
import sys

import yaml

from src.config import ROOT, load_config
from src.llm import GeminiClient

ANSWERABLE_LABELS = {"CORRECT", "PARTIAL", "WRONG"}
UNANSWERABLE_LABELS = {"DECLINED", "ANSWERED"}


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    cfg = load_config()
    prompts = yaml.safe_load(open(ROOT / "configs" / "prompts.yaml", encoding="utf-8"))
    judge = GeminiClient(cfg, model=cfg["judge"]["model"])
    rows = [json.loads(l) for l in open(cfg["results_dir"] / "pilot_answers.jsonl", encoding="utf-8")]
    out = []
    for r in rows:
        prompt = prompts["judge_user"].format(
            question=r["question"], answerable="yes" if r["answerable"] == "yes" else "no",
            gold=r["gold_answer"], answer=r["answer"])
        res = judge.generate(prompt, system=prompts["judge_system"])
        m = re.search(r"LABEL:\s*([A-Z]+)", res.text)
        label = m.group(1) if m else "UNPARSED"
        valid = ANSWERABLE_LABELS if r["answerable"] == "yes" else UNANSWERABLE_LABELS
        if label not in valid:
            label = "UNPARSED"
        reason = re.search(r"REASON:\s*(.+)", res.text)
        out.append({"qid": r["qid"], "system": r["system"], "judge_label": label,
                    "judge_reason": reason.group(1).strip() if reason else res.text[:200]})
        print(f"{r['qid']} {r['system']}: {label}", flush=True)
    path = cfg["results_dir"] / "pilot_judgements.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    print(f"Saved {len(out)} judgements to {path}")


if __name__ == "__main__":
    main()
