"""Fill gold_page in eval/pilot_questions.csv by finding each gold_quote in its PDF.

Each answerable question stores a short exact phrase (gold_quote) from the source.
This script finds which page(s) of gold_doc contain it, so retrieval can be scored
against the real document instead of a page number typed by hand. Questions whose
quote cannot be found are listed so they can be checked manually.

Usage:  python -m eval.locate_gold
"""
import csv
import re

from src.config import load_config
from src.ingest import pdf_pages


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower()).strip()


def main():
    cfg = load_config()
    path = cfg["questions_path"]
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    cache, missing = {}, []
    for r in rows:
        if r["answerable"] != "yes":
            continue
        pdf = cfg["raw_dir"] / r["gold_doc"]
        if not pdf.exists():
            missing.append((r["qid"], f"document not found: {r['gold_doc']}"))
            continue
        if pdf not in cache:
            cache[pdf] = [(n, norm(t)) for n, t in pdf_pages(pdf)]
        quote = norm(r["gold_quote"])
        pages = [str(n) for n, t in cache[pdf] if quote in t]
        r["gold_page"] = ";".join(pages)
        if not pages:
            missing.append((r["qid"], f"quote not found: {r['gold_quote']!r}"))
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"Updated {path}")
    for qid, why in missing:
        print(f"  CHECK {qid}: {why}")


if __name__ == "__main__":
    main()
