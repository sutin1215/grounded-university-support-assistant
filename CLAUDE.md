# CLAUDE.md

Guide for Claude Code sessions in this repository. Read it before changing anything.

## What this project is

Final-year (honours) project at Heriot-Watt University Malaysia (HWUM), supervised by Dr Rosalind Deena Kumari.
Title: *A Grounded University Support Assistant: Retrieval-Augmented Generation with Confidence-Based Escalation.*

A Python chatbot that answers student questions only from official HWU/HWUM documents, cites document and page,
and escalates to staff when it is not confident. The research contribution is a **controlled comparison of four
systems** plus a **measurable escalation mechanism**, not just a working chatbot. The supervisor has said that
**analysis matters more than accuracy**: every experiment must be run properly and every choice justified and explained.

| System | What it does | Code |
|---|---|---|
| S1 | FAQ baseline: TF-IDF match against `data/faq.csv`, escalates below `faq_baseline.min_similarity` | `src/faq_baseline.py`, `S1FAQ` |
| S2 | Plain LLM (Gemini) answering from its own knowledge | `S2PlainLLM` in `src/systems.py` |
| S3 | RAG: top-k hybrid retrieval, Gemini answers only from numbered passages with `[n]` citations, or `NOT_FOUND` | `S3RAG` in `src/systems.py` |
| S4 | S3 plus a confidence check that escalates (Week 8+, **not built yet**) | pilot only: `eval/confidence_pilot.py` |

Research questions: RQ1 is RAG vs FAQ vs plain LLM. RQ2 asks which retrieval choices matter (chunking, k, lexical, dense or hybrid).
RQ3 asks whether escalation reduces wrong answers and at what cost in wrongly escalated answerable questions. RQ4 is an optional
usability study and depends on ethics approval. The planned experiments are E1 to E4 (one per RQ). Requirements are F1 to F9 and
NF1 to NF6, with success criteria SC1 to SC5. All of these are defined in `d1/main.tex`, Section 3, which is the source of truth.

## Layout

- `src/`: `config.py` (loads `configs/pilot.yaml`, resolves paths from repo root), `ingest.py` (PDF to page-tagged
  chunks), `retrieve.py` (bm25, bm25_stem, tfidf, dense, hybrid RRF), `llm.py` (Gemini client with cache, cost and
  retry), `systems.py` (S1 to S3 behind `answer(question) -> dict`), `faq_baseline.py`, `demo.py` (supervisor demo),
  `app.py` (Streamlit web interface "AskWatt": student and staff views; style in `static/style.css`, fonts in `static/fonts`), `escalations.py` (escalation log, `data/escalations.jsonl`, gitignored)
- `eval/`: pilot harness. `pilot_questions.csv` (32 questions: Q01-Q20 answerable, U01-U06 unanswerable, plus P01-P04
  paraphrased and N01-N02 near-miss added 11 Nov; each answerable one has gold answer, doc, quote and page),
  `labels/pilot_manual_labels.csv`, `results/` (generated tables, committed)
- `configs/`: `pilot.yaml` (all settings) and `prompts.yaml` (all prompts, reported verbatim in the dissertation)
- `data/`: `doc_sources.csv` (27 sources with version, scope and staleness-test flags), `faq.csv` (12 FAQs),
  `cache/llm_cache.jsonl` (committed). `raw/` (PDFs) and `processed/` are gitignored
- `tests/test_pilot.py`: unit tests, no PDFs or API key needed
- `d1/`: D1 research report in LaTeX, the **main copy** (see D1 below)
- `docs/`: `journal/` (Markdown source to .docx), `meetings/`, `weekly/`, `reading_list.md`
- `ethics/`: ethics application documents (submitted 26 Oct 2026)
- `tools/`: `build_journal.py` (journal .md to .docx), `check_gemini.py` (tests the API key)

## Commands

Use the project venv: `.venv/Scripts/python.exe` (Windows). Run modules from the repo root with `-m`.

```bash
.venv/Scripts/python.exe -m pytest -q                  # unit tests (fast, offline)
.venv/Scripts/python.exe -m src.ingest                 # PDFs in data/raw -> data/processed/chunks.jsonl
.venv/Scripts/python.exe -m eval.locate_gold           # rewrites gold_page in pilot_questions.csv
.venv/Scripts/python.exe -m eval.run_pilot             # retrieval comparison + S1
.venv/Scripts/python.exe -m eval.run_systems           # S1-S3 answers (LLM, cached)
.venv/Scripts/python.exe -m eval.judge                 # LLM judge labels
.venv/Scripts/python.exe -m eval.score_systems         # eval/results/pilot_systems_summary.md
.venv/Scripts/python.exe -m streamlit run src/app.py   # web interface prototype (cached questions cost nothing)
.venv/Scripts/python.exe -m eval.model_signal          # S4 model signal: LLM "are these passages enough?" (paid, cached)
.venv/Scripts/python.exe -m eval.confidence_pilot      # S4 signal pilot (AUROC + bootstrap CI; includes the model signal)
.venv/Scripts/python.exe -m eval.label_evidence        # evidence file for checking the reference labels (no LLM)
.venv/Scripts/python.exe -m eval.plot_signals          # d1/images/signal_plot.tex from confidence_pilot.csv
.venv/Scripts/python.exe -m eval.cost_projection       # Semester 2 cost projection from measured pilot costs
.venv/Scripts/python.exe -m src.systems S3 "question"  # one answer
.venv/Scripts/python.exe tools/build_journal.py docs/journal/journal_NN_week_X.md
```

Order matters: ingest, then locate_gold, then run_pilot or run_systems, then judge, then score_systems;
model_signal before confidence_pilot, then plot_signals; label_evidence after judge.

## Rules

- **Never read, print or commit `.env`** (holds `GEMINI_API_KEY`). Never commit `data/raw/` PDFs or
  `ethics/Ethics_Application_submitted_*.pdf`. **The GitHub repo is public.**
- **Do not delete or rewrite `data/cache/llm_cache.jsonl`.** It makes reruns free and reproducible (NF2). Cache keys
  include model, temperature, max tokens, system prompt and user prompt, so changing any prompt or setting means new
  paid API calls. Say so before running anything that will miss the cache.
- **Fair comparison:** S2 and S3 share the same `role` prompt. Change prompts only in `configs/prompts.yaml`, and keep
  systems identical except for the factor being tested. Put settings in config, not hard-coded (F4).
- **No personal data to the LLM** (NF1). Only public documents and test questions.
- **Tuning only on the dev split.** The final test split (planned: about 60 dev and 140 test out of 200 questions) is used once.
- Pilot numbers are 32 questions: always call them indicative, not final results.
- New systems implement the same `answer()` dict shape (`system`, `answer`, `abstained`, `citations`, tokens,
  latency, cost) so `eval/` scripts work unchanged. Add unit tests in `tests/` with fakes (see `FakeLLM` and `FakeRetriever`).
- Code style: module docstring with purpose and `Usage:` line, short plain-English comments, small functions, no
  frameworks beyond `requirements.txt`. Call `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` in CLI
  entry points (Windows console).
- **Commits:** the student commits. Claude gives the exact commands and commits or pushes only when the student
  explicitly says to ("do it"). When committing for them, commit as the student (the laptop's git config
  already has their name and email; never write the email into a repo file) with **no Claude Co-Authored-By
  trailer**. Never push without being asked.
- Commit messages: short imperative summary of what changed and why (see `git log`).
- Records (journal, meetings) keep true dates; nothing is back-dated.

## D1 report (`d1/`)

- Edit only `d1/main.tex`, `d1/references.bib`, `d1/images/`, `d1/code/`. **Never edit `hwu_template/` or `acm_format/`.**
- Main body maximum 14 pages. ACM style, British spelling, plain clear English.
- Overleaf is not synced. After editing, list the changed files so the student can upload them. If they edited in
  Overleaf, they must unzip the Overleaf source here first.
- Numbers in the report must match `eval/results/*.md`. Check them when results change.
- Only cite entries that are verified (see `docs/reading_list.md` notes). Never invent references.
- The report's writing and analysis are the student's own work. Claude may suggest, check and edit, but GenAI use
  must be declared (D1 "Generative AI Summary" appendix and the journal "References consulted" section).

## Status (update as work moves on)

As of 11 Nov 2026 (Week 9), D1 final pass (ethics approved in November 2026):
- Pilot re-run end to end and extended to 32 questions (24 answerable, 8 unanswerable). Retrieval on 24:
  hybrid hit@1 0.71, hit@5 0.92, MRR 0.78. Correct on 24 answerable: S1 8, S2 8, S3 24; unanswerable declined:
  S1 6/8, S2 2/8, S3 8/8. Judge vs reference labels: 90/96, kappa 0.91. S4 signals (AUROC, bootstrap 95% CI):
  dense top 0.85 [0.69, 0.97], BM25 top 0.71, model signal 1.00 (8 negatives only). Pilot cost US$0.37 (192 calls);
  projection US$5.77 (`eval/results/cost_projection.md`). 5 of 64 LLM answers truncated by the 1,024-token cap
  (thinking tokens count): raise it before the Semester 2 evaluation (this invalidates the cache, so rerun costs apply).
- D1 edited for the final pass (see `docs/checkpoint_d1_final_pass.md`); the student compiles in Overleaf.
- Labels: all 96 reviewed and confirmed by the student on 11 Nov (6 disputed ones decided by them).
- D1 compiled locally on 11 Nov (MiKTeX; build steps in `docs/checkpoint_d1_final_pass.md`): main body 14 pages.
- Next: student reads the PDF, uploads the d1 files to Overleaf; GenAI box last; D1 deadline 26 Nov.
  Then: 200-question test set, S4, E1 to E3, E4 usability study in Semester 2 Weeks 6-8.
- Supervisor meetings: usually Tuesdays 11:30 (meeting 6 moved to Fri 13 Nov). Notes go in `docs/meetings/`, weekly journal in `docs/journal/`.

## Work in progress

- **D1 final pass: read `docs/checkpoint_d1_final_pass.md` before continuing it.**

## Known issues

- **GenAI declaration box is deliberately left for last** (student's choice): the statement in
  `hwu_template/declaration.tex` is still template text. Do not edit it unless asked. Appendix B facts were
  corrected on 11 Nov.
- The GitHub repo is public and contains the D1 draft and the student ID: make it private before submission
  (plagiarism checkers can match the report against it).
