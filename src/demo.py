"""Pilot demo for supervisor meetings: retrieval with citations vs the S1 FAQ baseline.

Shows, for a few student questions, what each approach returns:
  - S1 FAQ baseline: the matched FAQ answer (or ESCALATE), with its similarity score
  - Retrieval (BM25): the top passages from the official documents, with document and page

Usage:
  python -m src.demo                      # runs the prepared demo questions
  python -m src.demo "your own question"  # try any question
"""
import sys

from src.config import load_config
from src.faq_baseline import FAQBaseline, load_faq
from src.retrieve import BM25Retriever, load_chunks

DEMO_QUESTIONS = [
    "Can I self-certify if I was sick for a few days?",          # both work
    "Can I ask my lecturer for an extension on an assignment?",  # FAQ helps, retrieval misses wording
    "What is the charge if I pay my fees after the deadline?",   # not in documents: FAQ answers wrongly
    "What time does the library close on Saturdays?",            # not in documents: should escalate
]


def show(question, faq, retriever, k=3):
    print("=" * 80)
    print(f"QUESTION: {question}\n")
    out = faq.answer(question)
    print(f"S1 FAQ baseline -> {out['faq_id']} (similarity {out['similarity']:.2f})")
    print(f"  {out['answer']}\n")
    print(f"Retrieval (BM25), top {k} passages with citations:")
    for rank, hit in enumerate(retriever.search(question, k), start=1):
        snippet = " ".join(hit["text"].split())[:220]
        print(f"  [{rank}] {hit['doc']}, page {hit['page']} (score {hit['score']:.2f})")
        print(f"      {snippet} ...")
    print()


def main():
    cfg = load_config()
    faq = FAQBaseline(load_faq(cfg), cfg["faq_baseline"]["min_similarity"])
    retriever = BM25Retriever(load_chunks(cfg))
    questions = [" ".join(sys.argv[1:])] if len(sys.argv) > 1 else DEMO_QUESTIONS
    for q in questions:
        show(q, faq, retriever)


if __name__ == "__main__":
    main()
