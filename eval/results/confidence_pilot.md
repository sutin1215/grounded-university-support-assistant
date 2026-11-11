# S4 pilot: escalation signals

24 answerable and 8 unanswerable questions. AUROC = chance that a random answerable question scores higher than a random unanswerable one.

| Signal | AUROC | Bootstrap 95% CI | Mean (answerable) | Mean (unanswerable) |
|---|---|---|---|---|
| bm25_stem_top | 0.71 | 0.52-0.88 | 8.917 | 5.928 |
| bm25_stem_gap | 0.58 | 0.36-0.78 | 2.578 | 1.070 |
| dense_top | 0.85 | 0.69-0.97 | 0.710 | 0.632 |
| dense_gap | 0.55 | 0.31-0.79 | 0.030 | 0.022 |
| model_score | 1.00 | 1.00-1.00 | 98.750 | 0.000 |

Only 8 unanswerable questions: indicative only; the wide intervals show the uncertainty.
