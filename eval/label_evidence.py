"""Evidence for checking the reference labels of the pilot answers, one row per question and system.

For every answer in eval/results/pilot_answers.jsonl this records deterministic checks that do not use
an LLM, so the labels are not checked with the same model as the LLM judge:
  - key facts: every number in the gold answer (digits or number words, with %, RM and "days" kept),
    and whether each one appears in the answer
  - declined: whether the system abstained or the answer says it cannot answer or refers to staff
  - gold page cited (S3): whether a citation points to the gold document and page
  - quote check: the exact gold quote, and whether it is on the gold page of the source PDF
Rows where the checks and the current label disagree are flagged, and the reviewer's reasoning (the note
in the labels file) and the LLM judge's label are shown next to each label.

Output: eval/labels/pilot_label_evidence.csv
Usage:  python -m eval.label_evidence
"""
import csv
import json
import re
import sys

from src.config import ROOT, load_config
from src.ingest import pdf_pages

WORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
         "eight": "8", "nine": "9", "ten": "10"}
DECLINE = re.compile(r"can't find|cannot find|could not find|do not know|don't know|not able to answer|"
                     r"can't answer|cannot answer|contact the relevant|not (?:contain|include|mention|specify)|"
                     r"no information|isn't (?:specified|mentioned)|not specified|escalat", re.I)


def norm(text: str) -> str:
    text = text.lower().replace(",", "")
    for w, d in WORDS.items():
        text = re.sub(rf"\b{w}\b", d, text)
    return re.sub(r"\s+", " ", text)


def numbers(text: str) -> list[str]:
    """Numbers in the gold answer, e.g. '30', '5', '24200', '0' from '0F'."""
    return sorted(set(re.findall(r"\d+(?:\.\d+)?", norm(text))), key=lambda s: (len(s), s))


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    cfg = load_config()
    answers = [json.loads(l) for l in open(cfg["results_dir"] / "pilot_answers.jsonl", encoding="utf-8")]
    with open(cfg["questions_path"], encoding="utf-8") as f:
        questions = {q["qid"]: q for q in csv.DictReader(f)}
    labels_path = ROOT / "eval" / "labels" / "pilot_manual_labels.csv"
    with open(labels_path, encoding="utf-8") as f:
        labels = {(r["qid"], r["system"]): r for r in csv.DictReader(f)}
    judge_path = cfg["results_dir"] / "pilot_judgements.csv"
    with open(judge_path, encoding="utf-8") as f:
        judge = {(r["qid"], r["system"]): r["judge_label"] for r in csv.DictReader(f)}
    pages = {}
    rows = []
    for a in answers:
        q = questions[a["qid"]]
        quote_on_page = ""
        if q["answerable"] == "yes":
            pdf = cfg["raw_dir"] / q["gold_doc"]
            if pdf not in pages:
                pages[pdf] = {n: norm(t) for n, t in pdf_pages(pdf)}
            gold_pages = [int(p) for p in q["gold_page"].split(";") if p]
            quote_on_page = "yes" if any(norm(q["gold_quote"]) in pages[pdf].get(p, "") for p in gold_pages) else "NO"
        facts = numbers(q["gold_answer"]) if q["answerable"] == "yes" else []
        ans = norm(a["answer"])
        found = [n for n in facts if re.search(rf"(?<![\d.]){re.escape(n)}(?![\d])", ans)]
        declined = bool(a.get("abstained")) or bool(DECLINE.search(a["answer"]))
        cited_gold = ""
        if a["system"] == "S3" and q["answerable"] == "yes" and not a.get("abstained"):
            gp = {int(p) for p in q["gold_page"].split(";") if p}
            cited_gold = "yes" if any(c["doc"] == q["gold_doc"] and c["page"] in gp for c in a["citations"]) else "no"
        label = labels.get((a["qid"], a["system"]), {}).get("label", "")
        note = labels.get((a["qid"], a["system"]), {}).get("note", "")
        judged = judge.get((a["qid"], a["system"]), "")
        agrees = judged == label.replace("ESCALATED", "WRONG")
        flag = []
        if q["answerable"] == "yes":
            if label == "CORRECT" and len(found) < len(facts):
                flag.append("correct but a gold number is missing")
            if label in ("WRONG", "PARTIAL") and facts and len(found) == len(facts) and not declined:
                flag.append("all gold numbers present")
            if label == "CORRECT" and declined:
                flag.append("correct but looks declined")
            if label == "ESCALATED" and not declined:
                flag.append("escalated but no decline found")
        else:
            if label == "DECLINED" and not declined:
                flag.append("declined but no decline found")
            if label == "ANSWERED" and declined:
                flag.append("answered but decline wording found")
        rows.append({"qid": a["qid"], "system": a["system"], "answerable": q["answerable"],
                     "question": q["question"], "gold_answer": q["gold_answer"], "gold_doc": q["gold_doc"],
                     "gold_page": q["gold_page"], "gold_quote": q["gold_quote"], "quote_on_gold_page": quote_on_page,
                     "gold_numbers": " ".join(facts), "numbers_found": " ".join(found),
                     "declined": "yes" if declined else "no", "s3_cites_gold_page": cited_gold,
                     "answer": " ".join(a["answer"].split()), "current_label": label, "reason": note,
                     "judge_label": judged, "flag": "; ".join(flag),
                     "needs_review": "yes" if note.startswith("REVIEW") or " REVIEW:" in note or not agrees else ""})
    out = ROOT / "eval" / "labels" / "pilot_label_evidence.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"Saved {len(rows)} rows to {out}; flagged {sum(bool(r['flag']) for r in rows)}; "
          f"missing labels {sum(not r['current_label'] for r in rows)}; "
          f"quotes not on gold page {sum(r['quote_on_gold_page'] == 'NO' for r in rows)}; "
          f"for review {sum(r['needs_review'] == 'yes' for r in rows)}")


if __name__ == "__main__":
    main()
