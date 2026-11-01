# S1-S3 pilot results

20 answerable and 6 unanswerable questions; 5 official documents; LLM gemini-3.6-flash (temperature 0.0); S3 retrieves the top 5 passages with hybrid search. Labels are manual; see the agreement section for the LLM judge.

| System | Correct | Partial | Wrong | Escalated (answerable) | Declined (unanswerable) | Answered (unanswerable) |
|---|---|---|---|---|---|---|
| S1 | 8/20 | 0/20 | 8/20 | 4/20 | 5/6 | 1/6 |
| S2 | 6/20 | 5/20 | 7/20 | 2/20 | 1/6 | 5/6 |
| S3 | 20/20 | 0/20 | 0/20 | 0/20 | 6/6 | 0/6 |

## Citations (S3)

- Answered answerable questions: 20
- With at least one citation: 20/20
- Citing the gold document and page: 17/20

## Cost and latency per question

| System | Median latency (s) | Mean input tokens | Mean output tokens | Cost per question (US$) |
|---|---|---|---|---|
| S1 | 0.00 | 0 | 0 | 0.00000 |
| S2 | 3.75 | 59 | 673 | 0.00257 |
| S3 | 2.64 | 1823 | 555 | 0.00345 |

Total pilot generation cost at paid-tier prices: US$0.1564. Projected for 200 questions x 2 LLM systems: US$1.20 (S4 adds roughly one S3-sized call per question).

## LLM judge vs manual labels

- Items compared: 78
- Exact agreement: 72/78 (92%)
- Cohen's kappa: 0.89 (threshold for using the judge: 0.60)
- Disagreements: Q03/S2 (manual WRONG, judge PARTIAL), Q05/S2 (manual PARTIAL, judge CORRECT), Q08/S2 (manual WRONG, judge PARTIAL), Q10/S2 (manual CORRECT, judge PARTIAL), Q18/S2 (manual PARTIAL, judge WRONG), Q19/S2 (manual PARTIAL, judge CORRECT)

Pilot set only (26 questions): indicative, not final results.
