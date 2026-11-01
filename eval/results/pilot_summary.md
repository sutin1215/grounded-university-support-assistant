# Pilot results (2026-11-01)

- Documents: 5 (Fee-International.pdf, Fees-and-payment-guide-Malaysia.pdf, hapsug.pdf, ltbp-submission-coursework.pdf, mc-procedure.pdf)
- Chunks: 45 (about 220 words, 40 overlap)
- Questions: 26 (20 answerable, 6 unanswerable)
- Skipped (source document not downloaded): none

## Retrieval (answerable questions, top 5)

| Method | Hit@1 | Hit@5 | Doc hit@5 | MRR |
|---|---|---|---|---|
| bm25 | 0.60 | 0.90 | 0.95 | 0.69 |
| bm25_stem | 0.60 | 0.95 | 0.95 | 0.74 |
| tfidf | 0.45 | 0.85 | 0.95 | 0.61 |
| dense | 0.60 | 0.85 | 1.00 | 0.71 |
| hybrid | 0.70 | 0.95 | 1.00 | 0.79 |

## S1 FAQ baseline (threshold 0.35)

- answerable correct: 0.40
- answerable wrongly escalated: 0.20
- unanswerable correctly escalated: 0.83

Small pilot set: treat these as indicative only, not final results.
