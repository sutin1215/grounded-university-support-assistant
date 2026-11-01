"""Run S1, S2 and S3 on every pilot question and save their answers.

Output: eval/results/pilot_answers.jsonl (one line per question and system), including the
answer, citations, retrieved passages, tokens, latency and cost. LLM calls are cached, so
rerunning this script reproduces the same answers without new API calls.

Usage:  python -m eval.run_systems
"""
import json
import sys

from eval.run_pilot import load_questions
from src.config import load_config
from src.systems import build_systems


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    cfg = load_config()
    questions = load_questions(cfg)
    systems = build_systems(cfg, ("S1", "S2", "S3"))
    out_path = cfg["results_dir"] / "pilot_answers.jsonl"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for i, q in enumerate(questions, start=1):
        for name, system in systems.items():
            out = system.answer(q["question"])
            rows.append({"qid": q["qid"], "question": q["question"], "answerable": q["answerable"],
                         "gold_answer": q["gold_answer"], "gold_doc": q["gold_doc"],
                         "gold_page": q["gold_page"], **out})
        print(f"[{i}/{len(questions)}] {q['qid']} done", flush=True)
    with open(out_path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Saved {len(rows)} answers to {out_path}")


if __name__ == "__main__":
    main()
