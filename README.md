# A Grounded University Support Assistant: Retrieval-Augmented Generation with Confidence-Based Escalation

A Python chatbot for answering student questions from official university documents with source citation and confidence-based escalation to staff.

## Start here

- Notion project management (tasks, deadlines): https://app.notion.com/p/6f58a0a5b3c549b98d6a51e9b8e36ae7
- Overleaf D1 draft: shared with the supervisor (backup exports in `d1/`)
- Journal and meeting notes: `docs/`
- Ethics documents: `ethics/`

## Structure

- `configs/`: experiment settings
- `data/`: source list and test set
- `src/`: ingestion, retrieval, generation, escalation, web UI
- `eval/`: evaluation harness
- `tests/`: unit tests
- `docs/`: journal, meeting notes, weekly updates, reading list
- `ethics/`: ethics application documents
- `d1/`: D1 report LaTeX (main copy, upload changed files to Overleaf)
- `tools/`: helper scripts (journal builder)

## Run the pilot

```bash
pip install -r requirements.txt
# put the official PDFs listed in data/doc_sources.csv into data/raw/ (not committed)
python -m src.ingest          # PDFs -> data/processed/chunks.jsonl
python -m eval.locate_gold    # find the page of each gold answer
python -m eval.run_pilot      # retrieval (BM25 vs TF-IDF) + S1 FAQ baseline -> eval/results/
python -m src.retrieve "What is the penalty for late coursework?"   # demo with citations
python -m pytest -q
```
