# Checkpoint: D1 final pass (paused 11 Nov 2026)

Resume from here. Read `CLAUDE.md` first. The student's full brief for this pass is summarised below.

## Brief (from the student, 11 Nov 2026)
Final pass on D1 before submission (Sem 1 Week 11). Aim for the top band in both rubrics:
Proposal & Research (15) and Preparation & Feasibility (10). Hard rules: keep the HWU template;
main body (Introduction to Conclusions) at most 14 pages (13 now), so additions must be paid for with cuts;
never invent numbers or references; describe every method accurately, including AI-assisted steps;
**leave the Declaration's GenAI box as it is**; in Appendix B (GenAI summary) only correct facts and report
what changed; **do not commit or push**, and give a suggested commit message at the end.

## Decisions taken (11 Nov)
- Ethics: write "approved in November 2026" (no reference number).
- Usability study E4/F8: raise from Could to **Should**. E4 runs in Semester 2, around Weeks 6-8, once S4 is in the interface.
- LaTeX: there is no TeX on the laptop. **The student compiles in Overleaf** and sends the PDF for the final checks.
- Labels: Claude builds an evidence file (gold answer, exact source quote, deterministic number/date checks,
  reasoning, flags for uncertain cases). **The student reviews and confirms each label**, then kappa and Table 6
  are recomputed and can be called the student's labels.

## Step 1 assessment (already given to the student)
Estimated bands now: Proposal & Research about A- (11-12/15); Preparation & Feasibility about A- (7.5-8/10).
Top weaknesses: unverified AI-drafted labels and the kappa built on them; thin S4 evidence (6 negatives);
S3 ceiling effect (20/20 on document-worded questions); SC1 too easy; inconsistent numbers (audit counts,
topic lists, E2 cost); stale ethics wording. Handbook 6.3 and the rubric files are not on the laptop (probably in
the claude.ai project); marking used the A-band descriptors the student quoted. Past samples analysed (in Downloads):
Chia (strongest feasibility: benchmarks + API cost comparison), Nur Damia, Tan Alan, Izzat, Tan Shwu En.
No extra diagram proposed beyond the two requested; Gemini justification goes in the technology table instead.

## Status at end of 11 Nov session
All edits in the brief are made in `d1/main.tex`, `d1/references.bib`, `d1/images/` and the eval scripts.
Paid run done (62 calls, US$0.13 including the model signal). Nothing committed.

Waiting on the student:
1. Labels: DONE 11 Nov. All 96 reviewed and confirmed by the student; the 6 disputed S2 labels were decided by
   them and matched the drafts, so Table 6 and kappa (0.91) did not change. D1 4.2 and Appendix B updated.
2. Compile: DONE 11 Nov on the laptop with MiKTeX (installed with the student's approval). Build:
   `cd d1`, then pdflatex -include-directory=acm_format -output-directory=build main.tex, bibtex in build/ (copy
   references.bib and ACM-Reference-Format.bst there), then pdflatex twice. Result: 38 pages, main body pages 1-14
   (ends about 60% down page 14), 0 errors, no undefined references; the only overfull boxes are 6 in the template's
   title page and declaration (not editable). All 25 number checks against eval/results pass. PDF:
   d1/build/D1_final_2026-11-11.pdf (gitignored).
3. Holm's correction is named without a citation (Holm 1979 could not be verified in Crossref here).
4. SUS >= 68 is justified against BarkPlug's 67.75 only; the Lewis 2018 "68 is average" source could not be read.
5. The GenAI box in the Declaration (left for last by choice).
