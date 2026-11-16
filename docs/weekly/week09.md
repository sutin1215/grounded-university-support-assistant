# Weekly management update - Week 9 (9 - 15 Nov 2026)

## Done this week
- 10 Nov: compared D1 against the past samples for length and depth, then simplified Background and Methodology. Each table now sits in its own section, the chatbot comparison is cut to 5 systems, and the MoSCoW table is back in Section 3.3. The interface was redesigned and named AskWatt.
- 10 Nov: fixed the dense-miss count; completed five references; filled in the form emails; fixed `.env.example` and the demo comments.
- 11 Nov: ethics application approved. Pilot re-run and extended to 32 questions (24 answerable, 8 unanswerable, including paraphrases and near-misses):
  - Hybrid search: hit@5 0.92, MRR 0.78.
  - Correct on 24 answerable: S1 8, S2 8, S3 24. Unanswerable declined: S1 6/8, S2 2/8, S3 8/8.
  - Judge vs reference labels: 90/96, kappa 0.91.
  - S4 signals: dense top score AUROC 0.85; model signal 1.00 (8 negatives only).
  - Pilot cost US$0.37; the full evaluation is projected at about US$5.80.
- 11 Nov: all 96 reference labels reviewed and confirmed by me. Risk heat map and signal plot added. D1 compiled locally (MiKTeX). Layout fixed so tables and figures stay in their sections.
- 12 Nov: D1 review pass:
  - New evaluation design table (Table 5) and metric definitions.
  - Clearer technology table (Chosen / Evidence / Alternatives rejected).
  - GenAI statement, neutral RQ1, SC3 fallback, Gantt updated to Week 9.
- 13 Nov: meeting 6 (in person). Report judged good; small fixes requested; survey moves to Semester 2.
## Blockers
- None. The prototype could not be shown in the meeting, so screenshots will be shared instead.
## Next week
- Send the AskWatt screenshots; apply any further comments.
- D2: slides, demo clip, narration and editing.
- Final D1 checks (page limit, references, Overleaf build); make the GitHub repository private before submitting.
- Submit D1 and D2 (aim 24 Nov).
## Questions for supervisor
- Are the screenshots enough, or would you like a short meeting to see the prototype running?
## Evidence (commits, files, links)
- d1/main.tex (D1 v8, then the meeting 6 fixes), eval/results/, src/app.py, docs/meetings/2026-11-13_week9_meeting6.md, docs/journal/journal_06_week_9.md
