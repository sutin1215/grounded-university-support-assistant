# S4 pilot: retrieval scores as an escalation signal

20 answerable and 6 unanswerable questions. AUROC = chance that a random answerable question scores higher than a random unanswerable one.

| Signal | AUROC | Mean (answerable) | Mean (unanswerable) |
|---|---|---|---|
| bm25_stem_top | 0.73 | 8.622 | 5.667 |
| bm25_stem_gap | 0.56 | 2.209 | 1.265 |
| dense_top | 0.88 | 0.715 | 0.618 |
| dense_gap | 0.45 | 0.027 | 0.025 |

Only 6 unanswerable questions: indicative only.
