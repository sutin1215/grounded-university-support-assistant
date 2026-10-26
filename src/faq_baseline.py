"""S1: FAQ-matching baseline.

Matches the student's question to the closest question in a hand-written FAQ
(data/faq.csv) using TF-IDF cosine similarity, and returns that FAQ's answer.
If the best match is below a similarity threshold it escalates instead.
This mirrors the intent-matching chatbots described in the related work.

Usage (demo):  python -m src.faq_baseline "How late can I submit coursework?"
"""
import csv
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from src.config import load_config
from src.retrieve import tokenize

ESCALATE = "ESCALATE"


class FAQBaseline:
    def __init__(self, faq_rows, min_similarity: float):
        self.rows = faq_rows
        self.min_similarity = min_similarity
        self.vec = TfidfVectorizer(tokenizer=tokenize, lowercase=False, ngram_range=(1, 2),
                                   sublinear_tf=True, token_pattern=None)
        self.matrix = self.vec.fit_transform(r["question"] for r in faq_rows)

    def answer(self, question: str) -> dict:
        sims = linear_kernel(self.vec.transform([question]), self.matrix).ravel()
        best = int(sims.argmax())
        if sims[best] < self.min_similarity:
            return {"faq_id": ESCALATE, "similarity": float(sims[best]),
                    "answer": "I can't answer that reliably. Please contact the relevant university office."}
        row = self.rows[best]
        return {"faq_id": row["faq_id"], "similarity": float(sims[best]),
                "answer": row["answer"], "source": row["source"]}


def load_faq(cfg):
    with open(cfg["faq_path"], encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    cfg = load_config()
    bot = FAQBaseline(load_faq(cfg), cfg["faq_baseline"]["min_similarity"])
    q = " ".join(sys.argv[1:]) or "How late can I hand in my coursework?"
    print(q)
    print(bot.answer(q))


if __name__ == "__main__":
    main()
