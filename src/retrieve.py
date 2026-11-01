"""Retrieval over the chunk store.

Methods (compared in the retrieval pilot, RQ2):
  bm25       BM25 keyword search on exact words
  bm25_stem  BM25 on stemmed words, so "extensions" also matches "extension"
  tfidf      TF-IDF cosine similarity
  dense      embedding search with a sentence-embedding model (matches meaning)
  hybrid     reciprocal rank fusion (RRF) of bm25_stem and dense

Every result keeps its document, page and score, so answers can cite their source.

Usage (demo):  python -m src.retrieve "What is the penalty for late coursework?"
               python -m src.retrieve --method dense "Can I ask for an extension?"
"""
import hashlib
import json
import re
import sys
from functools import lru_cache

import numpy as np
from nltk.stem import PorterStemmer
from rank_bm25 import BM25Okapi
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from src.config import ROOT, load_config

STOP = set("""a an the of to in on for and or is are be by with at from as it this that
what how do does can i my me when where which who will if any there their your""".split())
_stemmer = PorterStemmer()


def tokenize(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in STOP]


@lru_cache(maxsize=50000)
def _stem(word: str) -> str:
    return _stemmer.stem(word)


def tokenize_stem(text: str) -> list[str]:
    return [_stem(t) for t in tokenize(text)]


def load_chunks(cfg) -> list[dict]:
    with open(cfg["chunks_path"], encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def _top(scores, chunks, k):
    order = np.argsort(-np.asarray(scores), kind="stable")[:k]
    return [dict(chunks[i], score=float(scores[i])) for i in order]


class BM25Retriever:
    name = "bm25"
    tokenizer = staticmethod(tokenize)

    def __init__(self, chunks, cfg=None):
        self.chunks = chunks
        self.bm25 = BM25Okapi([self.tokenizer(c["text"]) for c in chunks])

    def scores(self, query: str):
        return self.bm25.get_scores(self.tokenizer(query))

    def search(self, query: str, k: int = 5):
        return _top(self.scores(query), self.chunks, k)


class StemmedBM25Retriever(BM25Retriever):
    name = "bm25_stem"
    tokenizer = staticmethod(tokenize_stem)


class TfidfRetriever:
    name = "tfidf"

    def __init__(self, chunks, cfg=None):
        self.chunks = chunks
        self.vec = TfidfVectorizer(tokenizer=tokenize, lowercase=False, ngram_range=(1, 2),
                                   sublinear_tf=True, token_pattern=None)
        self.matrix = self.vec.fit_transform(c["text"] for c in chunks)

    def scores(self, query: str):
        return linear_kernel(self.vec.transform([query]), self.matrix).ravel()

    def search(self, query: str, k: int = 5):
        return _top(self.scores(query), self.chunks, k)


class DenseRetriever:
    """Cosine similarity between sentence embeddings of the query and each passage.

    Passage embeddings are cached in data/processed/, keyed by the chunk texts and model,
    so they are only recomputed when the knowledge base or model changes.
    """
    name = "dense"
    # BGE models expect this instruction in front of short search queries.
    QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

    def __init__(self, chunks, cfg):
        from sentence_transformers import SentenceTransformer  # heavy import, only when used
        self.chunks = chunks
        model_name = cfg["retrieval"]["dense_model"]
        self.model = SentenceTransformer(model_name)
        key = hashlib.sha1((model_name + "".join(c["text"] for c in chunks)).encode()).hexdigest()[:12]
        cache = ROOT / "data" / "processed" / f"embeddings_{key}.npy"
        if cache.exists():
            self.matrix = np.load(cache)
        else:
            self.matrix = self.model.encode([c["text"] for c in chunks], normalize_embeddings=True,
                                            batch_size=32, show_progress_bar=False)
            cache.parent.mkdir(parents=True, exist_ok=True)
            np.save(cache, self.matrix)

    def scores(self, query: str):
        q = self.model.encode([self.QUERY_PREFIX + query], normalize_embeddings=True)[0]
        return self.matrix @ q

    def search(self, query: str, k: int = 5):
        return _top(self.scores(query), self.chunks, k)


class HybridRetriever:
    """Reciprocal rank fusion: score(d) = sum over methods of 1 / (rrf_k + rank of d)."""
    name = "hybrid"

    def __init__(self, chunks, cfg, parts=None):
        self.chunks = chunks
        self.rrf_k = cfg["retrieval"]["rrf_k"]
        self.parts = parts or [StemmedBM25Retriever(chunks, cfg), DenseRetriever(chunks, cfg)]

    def scores(self, query: str):
        fused = np.zeros(len(self.chunks))
        for part in self.parts:
            order = np.argsort(-np.asarray(part.scores(query)), kind="stable")
            ranks = np.empty(len(order), dtype=int)
            ranks[order] = np.arange(1, len(order) + 1)
            fused += 1.0 / (self.rrf_k + ranks)
        return fused

    def search(self, query: str, k: int = 5):
        return _top(self.scores(query), self.chunks, k)


RETRIEVERS = {"bm25": BM25Retriever, "bm25_stem": StemmedBM25Retriever, "tfidf": TfidfRetriever,
              "dense": DenseRetriever, "hybrid": HybridRetriever}


def build(name: str, chunks, cfg=None):
    cfg = cfg or load_config()
    return RETRIEVERS[name](chunks, cfg)


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # safe on Windows consoles
    args = sys.argv[1:]
    method = "bm25"
    if len(args) >= 2 and args[0] == "--method":
        method, args = args[1], args[2:]
    cfg = load_config()
    query = " ".join(args) or "What is the penalty for late submission of coursework?"
    retriever = build(method, load_chunks(cfg), cfg)
    print(f"Method: {method}\nQuery: {query}\n")
    for rank, hit in enumerate(retriever.search(query, cfg["retrieval"]["top_k"]), start=1):
        print(f"[{rank}] {hit['doc']}, page {hit['page']}  (score {hit['score']:.3f})")
        print("    " + hit["text"][:300].replace("\n", " ") + " ...\n")


if __name__ == "__main__":
    main()
