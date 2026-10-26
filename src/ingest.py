"""Ingestion: turn the official PDFs in data/raw into page-aware text chunks.

Each chunk keeps its source file and page number so that answers can cite
"document, page". Output: one JSON object per line in data/processed/chunks.jsonl.

Usage:  python -m src.ingest
"""
import json
import re
from pathlib import Path

import pymupdf

from src.config import load_config


def clean(text: str) -> str:
    text = text.replace("­", "")              # soft hyphens
    text = re.sub(r"-\n(\w)", r"\1", text)          # words split across lines
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n\n", text)
    return text.strip()


def pdf_pages(path: Path):
    with pymupdf.open(path) as doc:
        for i, page in enumerate(doc, start=1):
            yield i, clean(page.get_text())


def chunk_words(words, size, overlap):
    step = max(1, size - overlap)
    for start in range(0, max(1, len(words)), step):
        piece = words[start:start + size]
        if piece:
            yield " ".join(piece)
        if start + size >= len(words):
            break


def build_chunks(cfg) -> list[dict]:
    size = cfg["chunking"]["words_per_chunk"]
    overlap = cfg["chunking"]["overlap_words"]
    chunks = []
    pdfs = sorted(cfg["raw_dir"].glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found in {cfg['raw_dir']}")
    for pdf in pdfs:
        for page_no, text in pdf_pages(pdf):
            words = text.split()
            if len(words) < 15:                     # skip near-empty pages (covers, blank pages)
                continue
            for n, piece in enumerate(chunk_words(words, size, overlap)):
                chunks.append({
                    "chunk_id": f"{pdf.stem}-p{page_no}-c{n}",
                    "doc": pdf.name,
                    "page": page_no,
                    "text": piece,
                })
    return chunks


def main():
    cfg = load_config()
    chunks = build_chunks(cfg)
    out = cfg["chunks_path"]
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    docs = sorted({c["doc"] for c in chunks})
    print(f"Wrote {len(chunks)} chunks from {len(docs)} documents to {out}")
    for d in docs:
        print(f"  {d}: {sum(c['doc'] == d for c in chunks)} chunks")


if __name__ == "__main__":
    main()
