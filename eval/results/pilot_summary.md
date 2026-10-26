# Pilot results (2026-10-26)

- Documents: 3 (Fee-International.pdf, hapsug.pdf, mc-procedure.pdf)
- Chunks: 27 (about 220 words, 40 overlap)
- Questions: 18 (12 answerable, 6 unanswerable)
- Skipped (source document not downloaded): Q01, Q02, Q03, Q04, Q05, Q18, Q19, Q20

## Retrieval (answerable questions, top 5)

| Method | Hit@1 | Hit@5 | Doc hit@5 | MRR |
|---|---|---|---|---|
| bm25 | 0.83 | 1.00 | 1.00 | 0.87 |
| tfidf | 0.67 | 0.92 | 1.00 | 0.76 |

## S1 FAQ baseline (threshold 0.35)

- answerable correct: 0.50
- answerable wrongly escalated: 0.17
- unanswerable correctly escalated: 0.83

Small pilot set: treat these as indicative only, not final results.
