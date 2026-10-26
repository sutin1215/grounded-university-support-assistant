# Meeting 4: Week 7, Tuesday 27 October 2026, 11:30 - Dr Rosalind Deena Kumari (AGENDA, notes to add after)

## 1. Progress since last meeting
- Ethics: signed by supervisor and submitted on 26 Oct.
- Pilot built (26 Oct): 5 official PDFs ingested (45 chunks with document + page), BM25 and TF-IDF retrieval, S1 FAQ baseline (12 FAQs), 26 pilot questions (20 answerable, 6 unanswerable) with gold answers.
- First numbers: BM25 finds the right page in the top 5 for 90% of answerable questions (top 1: 60%); TF-IDF 85% (45%). S1 answers 40% of answerable questions correctly and escalates 5 of 6 unanswerable ones.
- Records organised: journals 2 (Weeks 4-5) and 3 (Week 6), meeting notes, weekly updates, ethics and D1 folders in GitHub; Notion up to date.

## 2. Observations
- S1 gives confident wrong answers when FAQs sound alike (e.g. late-payment charge answered with the fee due date): the failure RAG + escalation targets.
- Retrieval misses wording mismatches (e.g. "ask my lecturer for an extension" vs "No individual extensions"): motivates adding dense (embedding) retrieval and hybrid fusion.

## 3. Plan
- Week 8: dense + hybrid retrieval; LLM API for S2 (plain LLM) vs S3 (RAG); Background Research + Methodology; full D1 draft by 6 Nov.

## 4. Questions
1. Which LLM provider/API is acceptable (no personal data sent)?
2. Is a typed name OK as a consent signature? How long should signed consent forms be kept?
3. Feedback on the D1 structure in Overleaf.

## Notes (after the meeting)
-
