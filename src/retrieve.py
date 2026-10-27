"""Retrieval over the chunk store: BM25 (lexical) and TF-IDF cosine.

Dense (sentence-transformers) retrieval and hybrid fusion are added after the pilot.

Usage (demo):  python -m src.retrieve "What is the penalty for late coursework?"
"""
import json
import re
import sys

from rank_bm25 import BM25Okapi
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from src.config import load_config

STOP = set("""a an the of to in on for and or is are be by with at from as it this that
what how do does can i my me when where which who will if any there their your""".split())


def tokenize(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in STOP]


def load_chunks(cfg) -> list[dict]:
    with open(cfg["chunks_path"], encoding="utf-8") as f:
        return [json.loads(line) for line in f]


class BM25Retriever:
    name = "bm25"

    def __init__(self, chunks):
        self.chunks = chunks
        self.bm25 = BM25Okapi([tokenize(c["text"]) for c in chunks])

    def search(self, query: str, k: int = 5):
        scores = self.bm25.get_scores(tokenize(query))
        top = sorted(range(len(scores)), key=lambda i: -scores[i])[:k]
        return [dict(self.chunks[i], score=float(scores[i])) for i in top]


class TfidfRetriever:
    name = "tfidf"

    def __init__(self, chunks):
        self.chunks = chunks
        self.vec = TfidfVectorizer(tokenizer=tokenize, lowercase=False, ngram_range=(1, 2),
                                   sublinear_tf=True, token_pattern=None)
        self.matrix = self.vec.fit_transform(c["text"] for c in chunks)

    def search(self, query: str, k: int = 5):
        scores = linear_kernel(self.vec.transform([query]), self.matrix).ravel()
        top = scores.argsort()[::-1][:k]
        return [dict(self.chunks[i], score=float(scores[i])) for i in top]


def build(name: str, chunks):
    return {"bm25": BM25Retriever, "tfidf": TfidfRetriever}[name](chunks)


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # safe on Windows consoles
    cfg = load_config()
    query = " ".join(sys.argv[1:]) or "What is the penalty for late submission of coursework?"
    chunks = load_chunks(cfg)
    retriever = BM25Retriever(chunks)
    print(f"Query: {query}\n")
    for rank, hit in enumerate(retriever.search(query, cfg["retrieval"]["top_k"]), start=1):
        print(f"[{rank}] {hit['doc']}, page {hit['page']}  (score {hit['score']:.2f})")
        print("    " + hit["text"][:300].replace("\n", " ") + " ...\n")


if __name__ == "__main__":
    main()
