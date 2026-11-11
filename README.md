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
# put GEMINI_API_KEY=... in a .env file in this folder (not committed)
python -m src.ingest              # PDFs -> page-tagged passages (data/processed/)
python -m eval.locate_gold        # find the page of each gold answer quote
python -m eval.run_pilot          # retrieval comparison (5 methods) + S1 baseline
python -m eval.run_systems        # S1, S2, S3 answers for all pilot questions (cached)
python -m eval.judge              # LLM judge labels
python -m eval.score_systems      # results table: eval/results/pilot_systems_summary.md
python -m eval.model_signal       # S4 pilot: LLM "are these passages enough?" score (cached)
python -m eval.confidence_pilot   # S4 pilot: retrieval and model signals (AUROC with bootstrap CI)
python -m eval.label_evidence     # evidence for checking the reference labels (no LLM)
python -m eval.plot_signals       # D1 figure: d1/images/signal_plot.tex
python -m eval.cost_projection    # cost projection for the Semester 2 evaluation
python -m src.demo                # demo: S1 vs search with citations
python -m src.systems S3 "How many times can I resit a course?"
python -m pytest -q
streamlit run src/app.py          # web interface prototype (student and staff views)
```

Gemini responses are cached in `data/cache/llm_cache.jsonl`, so rerunning gives identical results without new API calls.
