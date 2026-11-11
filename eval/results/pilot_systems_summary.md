# S1-S3 pilot results

24 answerable and 8 unanswerable questions; 5 official documents; LLM gemini-3.6-flash (temperature 0.0); S3 retrieves the top 5 passages with hybrid search. Reference labels are in eval/labels/pilot_manual_labels.csv (status in its labelled_by column); see the agreement section for the LLM judge.

| System | Correct | Partial | Wrong | Escalated (answerable) | Declined (unanswerable) | Answered (unanswerable) |
|---|---|---|---|---|---|---|
| S1 | 8/24 | 1/24 | 10/24 | 5/24 | 6/8 | 2/8 |
| S2 | 8/24 | 6/24 | 7/24 | 3/24 | 2/8 | 6/8 |
| S3 | 24/24 | 0/24 | 0/24 | 0/24 | 8/8 | 0/8 |

## Paraphrased and near-miss questions (N01, N02, P01, P02, P03, P04)

| System | N01 | N02 | P01 | P02 | P03 | P04 |
|---|---|---|---|---|---|---|
| S1 | DECLINED | ANSWERED | WRONG | WRONG | PARTIAL | ESCALATED |
| S2 | DECLINED | ANSWERED | PARTIAL | CORRECT | CORRECT | ESCALATED |
| S3 | DECLINED | DECLINED | CORRECT | CORRECT | CORRECT | CORRECT |

## Citations (S3)

- Answered answerable questions: 24
- With at least one citation: 24/24
- Citing the gold document and page: 20/24

## Cost and latency per question

| System | Median latency (s) | Mean input tokens | Mean output tokens | Cost per question (US$) |
|---|---|---|---|---|
| S1 | 0.00 | 0 | 0 | 0.00000 |
| S2 | 3.81 | 59 | 697 | 0.00266 |
| S3 | 3.12 | 1743 | 556 | 0.00339 |

Total pilot generation cost at paid-tier prices: US$0.1936. Projected for 200 questions x 2 LLM systems: US$1.21 (S4 adds roughly one S3-sized call per question).

## LLM judge vs manual labels

- Items compared: 96
- Exact agreement: 90/96 (94%)
- Cohen's kappa: 0.91 (threshold for using the judge: 0.60)
- Disagreements: Q03/S2 (manual WRONG, judge PARTIAL), Q05/S2 (manual PARTIAL, judge CORRECT), Q08/S2 (manual WRONG, judge PARTIAL), Q10/S2 (manual CORRECT, judge PARTIAL), Q18/S2 (manual PARTIAL, judge WRONG), Q19/S2 (manual PARTIAL, judge CORRECT)

Pilot set only (32 questions): indicative, not final results.
