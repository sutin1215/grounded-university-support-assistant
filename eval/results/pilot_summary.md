# Pilot results (2026-11-11)

- Documents: 5 (Fee-International.pdf, Fees-and-payment-guide-Malaysia.pdf, hapsug.pdf, ltbp-submission-coursework.pdf, mc-procedure.pdf)
- Chunks: 45 (about 220 words, 40 overlap)
- Questions: 32 (24 answerable, 8 unanswerable)
- Skipped (source document not downloaded): none

## Retrieval (answerable questions, top 5)

| Method | Hit@1 | Hit@5 | Doc hit@5 | MRR |
|---|---|---|---|---|
| bm25 | 0.58 | 0.88 | 0.96 | 0.68 |
| bm25_stem | 0.58 | 0.92 | 0.96 | 0.72 |
| tfidf | 0.46 | 0.83 | 0.96 | 0.61 |
| dense | 0.62 | 0.83 | 1.00 | 0.72 |
| hybrid | 0.71 | 0.92 | 1.00 | 0.78 |

## S1 FAQ baseline (threshold 0.35)

- answerable correct: 0.33
- answerable wrongly escalated: 0.21
- unanswerable correctly escalated: 0.75

Small pilot set: treat these as indicative only, not final results.
