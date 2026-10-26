"""Pilot evaluation: retrieval quality (BM25 vs TF-IDF) and the S1 FAQ baseline.

Reads eval/pilot_questions.csv and writes:
  eval/results/pilot_per_question.csv  (one row per question and method)
  eval/results/pilot_summary.md        (headline numbers)

Retrieval hit = a retrieved chunk comes from the gold document and gold page.
Doc hit       = a retrieved chunk comes from the gold document (any page).
S1 is correct on an answerable question if it returns the expected FAQ entry,
and on an unanswerable question if it escalates.

Usage:  python -m eval.run_pilot
"""
import csv
from datetime import date

from src.config import load_config
from src.faq_baseline import ESCALATE, FAQBaseline, load_faq
from src.retrieve import build, load_chunks


def load_questions(cfg):
    with open(cfg["questions_path"], encoding="utf-8") as f:
        return list(csv.DictReader(f))


def gold_pages(q) -> set[int]:
    return {int(p) for p in q["gold_page"].split(";") if p.strip()}


def first_hit_rank(hits, doc, pages):
    for rank, h in enumerate(hits, start=1):
        if h["doc"] == doc and h["page"] in pages:
            return rank
    return None


def main():
    cfg = load_config()
    k = cfg["retrieval"]["top_k"]
    chunks = load_chunks(cfg)
    all_questions = load_questions(cfg)
    have = {c["doc"] for c in chunks}
    # Skip answerable questions whose source document is not in data/raw yet.
    questions = [q for q in all_questions if q["answerable"] == "no" or q["gold_doc"] in have]
    skipped = [q["qid"] for q in all_questions if q not in questions]
    answerable = [q for q in questions if q["answerable"] == "yes"]
    unanswerable = [q for q in questions if q["answerable"] == "no"]
    rows, summary = [], {}

    for method in cfg["retrieval"]["methods"]:
        retriever = build(method, chunks)
        h1 = hk = dk = rr = 0.0
        for q in answerable:
            hits = retriever.search(q["question"], k)
            rank = first_hit_rank(hits, q["gold_doc"], gold_pages(q))
            doc_hit = any(h["doc"] == q["gold_doc"] for h in hits)
            h1 += rank == 1
            hk += rank is not None
            dk += doc_hit
            rr += 1 / rank if rank else 0
            rows.append({"qid": q["qid"], "method": method, "rank_of_gold": rank or "",
                         "doc_hit_at_k": int(doc_hit),
                         "top1": f"{hits[0]['doc']} p{hits[0]['page']}"})
        n = len(answerable)
        summary[method] = {"hit@1": h1 / n, f"hit@{k}": hk / n, f"doc_hit@{k}": dk / n, "MRR": rr / n}

    faq = FAQBaseline(load_faq(cfg), cfg["faq_baseline"]["min_similarity"])
    correct_ans = escalated_ans = correct_unans = 0
    for q in questions:
        out = faq.answer(q["question"])
        if q["answerable"] == "yes":
            correct_ans += out["faq_id"] == q["expected_faq_id"]
            escalated_ans += out["faq_id"] == ESCALATE
        else:
            correct_unans += out["faq_id"] == ESCALATE
        rows.append({"qid": q["qid"], "method": "S1_faq", "rank_of_gold": "",
                     "doc_hit_at_k": "", "top1": f"{out['faq_id']} (sim {out['similarity']:.2f})"})
    s1 = {
        "answerable correct": correct_ans / len(answerable),
        "answerable wrongly escalated": escalated_ans / len(answerable),
        "unanswerable correctly escalated": correct_unans / len(unanswerable) if unanswerable else float("nan"),
    }

    out_dir = cfg["results_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "pilot_per_question.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    docs = sorted({c["doc"] for c in chunks})
    lines = [f"# Pilot results ({date.today().isoformat()})", "",
             f"- Documents: {len(docs)} ({', '.join(docs)})",
             f"- Chunks: {len(chunks)} (about {cfg['chunking']['words_per_chunk']} words, "
             f"{cfg['chunking']['overlap_words']} overlap)",
             f"- Questions: {len(questions)} ({len(answerable)} answerable, {len(unanswerable)} unanswerable)",
             f"- Skipped (source document not downloaded): {', '.join(skipped) or 'none'}",
             "", f"## Retrieval (answerable questions, top {k})", "",
             "| Method | Hit@1 | Hit@%d | Doc hit@%d | MRR |" % (k, k), "|---|---|---|---|---|"]
    for m, s in summary.items():
        lines.append(f"| {m} | {s['hit@1']:.2f} | {s[f'hit@{k}']:.2f} | {s[f'doc_hit@{k}']:.2f} | {s['MRR']:.2f} |")
    lines += ["", f"## S1 FAQ baseline (threshold {cfg['faq_baseline']['min_similarity']})", ""]
    lines += [f"- {name}: {v:.2f}" for name, v in s1.items()]
    lines += ["", "Small pilot set: treat these as indicative only, not final results."]
    (out_dir / "pilot_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
