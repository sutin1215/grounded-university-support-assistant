# Handover note (for a new Claude chat)

Last updated: Thu 5 Nov 2026 (Week 8). Read this together with `CLAUDE.md` (repo rules, layout, commands).
A new chat should read both before doing anything.

## 1. Who, what, when

- Student: Muhammad Faizal Haris bin Aidi ("Maouf"), H00459013, BSc (Hons) Computing Science, HWU Malaysia.
- Supervisor: Dr Rosalind Deena Kumari. **Next meeting: Fri 13 Nov 2026** (moved from the usual Tuesday 11:30).
- Project: *A Grounded University Support Assistant: Retrieval-Augmented Generation with Confidence-Based Escalation* (F20PA).
- Deadlines: **D1 report + D2 5-minute video, Thu 26 Nov 2026, 15:30**. Aim to submit Tue 24 Nov.
  Clashes: Data Mining D2 (Wed 25 Nov), AI class test (Fri 27 Nov).
- Plan to the next meeting: full restructured D1 draft to the supervisor by **Wed 11 Nov**.
  - Thu–Fri 5–6 Nov: this note, then Introduction.
  - Sat–Sun 7–8: Background.
  - Mon 9: Methodology and Design.
  - Tue 10: Feasibility and appendices.
  - Wed 11: send the PDF.
  - After that: D2 script and storyboard, then recording. Minimise R sounds in the script and flag R-heavy names
    (Heriot-Watt) for practice.

## 2. Where everything lives

- **Laptop repo (main copy):** `C:\Users\faiza\Projects\University\grounded-university-support-assistant`, branch `main`.
  GitHub `ffaizalharis/grounded-university-support-assistant` is **public** (to be made private at the end).
- **Cloud clone** (Claude's workspace): `/home/claude/grounded-university-support-assistant`. Has `.env` and `data/raw/`
  (gitignored). Before use, run `git fetch origin && git reset --hard origin/main`.
- **D1 LaTeX:** `d1/main.tex` and `d1/references.bib`. Overleaf is not synced: after edits, tell the student which
  files changed so he can upload them. Local build: `cd d1 && TEXINPUTS=.:./acm_format//: latexmk -pdf main.tex`
  (or run `d1/build.sh`).
- **Notion:** weekly pages (Weeks 3–7 filled in and marked Done) and a task board. Gate 1 is still in Backlog
  (suggested: "Keep scope").
- **claude.ai project "Honours Project(FYP)":** past samples, templates, ethics documents, blueprint, deadlines.

## 3. Working rules agreed with the student

- **Commits:** the student commits. Claude gives the exact commands. Claude commits only if he explicitly says
  "do it". When committing for him, use `git -c user.name=ffaizalharis -c user.email=faizalharis1215@gmail.com`
  with no Claude trailer.
- Records (journal, meetings) keep **true dates**. Pacing what is shown to the supervisor each week is his choice,
  but nothing is back-dated.
- Never print or commit `.env` (Gemini key). The key should be regenerated at the end of the project.
- Report numbers must match `eval/results/*.md`. Only cite verified references.
- GenAI use is declared honestly (D1 appendix and the journal).
- Style: casual chat. For documents: British spelling, plain English, targeted edits rather than full rewrites.
  Timelines in chronological order.

## 4. Status

- **Code:** ingestion (5 PDFs, 45 chunks), 5 retrievers, S1 FAQ, S2 plain Gemini, S3 RAG with [n] citations and
  NOT_FOUND, LLM judge, S4 confidence-signal pilot. 9 unit tests pass. Model `gemini-3.6-flash`, temperature 0,
  paid tier (US$0.75 in / US$3.75 out per 1M tokens). All calls are cached in `data/cache/llm_cache.jsonl`.
- **Pilot results (26 questions, indicative only):**
  - Retrieval: hybrid is best (hit@1 0.70, hit@5 0.95, MRR 0.79). bm25_stem 0.60/0.95/0.74, bm25 0.60/0.90/0.69,
    dense 0.60/0.85/0.71, tfidf 0.45/0.85/0.61.
  - Correct out of 20 answerable: S1 8 (8 wrong, 4 escalated); S2 6 (5 partial, 7 wrong, 2 escalated); S3 20.
  - Declined out of 6 unanswerable: S1 5, S2 1, S3 6.
  - S3 citations: 20/20 cited, 17/20 on the gold page.
  - Median latency S2 3.75 s, S3 2.64 s. Cost per question S2 US$0.00257, S3 US$0.00345. Pilot total US$0.16.
    About US$1.20 projected for 200 questions.
  - Judge vs labels: kappa 0.89. **Caveat:** the "manual" labels were drafted by Claude and are not yet checked by
    the student, so this is AI vs AI. Do not call them human labels until he reviews them.
  - S4 signal: dense top score AUROC 0.88, bm25_stem 0.73. U03 (late-payment charge) is a near-miss that the
    scores cannot catch.
  - Lesson learned: the Q14 fee gold answer was wrong from PDF text extraction. Rendering the page showed
    RM24,200 per semester. Tables need visual checks.
- **Ethics:** application submitted 26 Oct 2026. Approval still pending.
- **D1:** Sections 1–3 drafted in the *old* structure (shown to the supervisor at meeting 5). Feasibility,
  conclusions and appendices are not written yet. Restructure is in progress (section 6).

## 5. Meeting 5 feedback (Tue 3 Nov), from the student's notes

1. Add a **Problem Statement** at the start. Make it specific to HWU/HWUM. Restructure and renumber.
2. **Objectives:** start with a verb ("To …"), keep them general, and include **no numbers** (so missing a target
   does not fail an objective). Give the systems objective one bullet per system (S1–S4).
3. Add **Scope** after the objectives: what is in and what is out. Limitations include HWU students only and no
   sensitive topics (financial hardship, mental health and so on).
4. **Background:** clearer structure and numbering, more papers, and a **comparison table of existing chatbots**
   (2–4 points each) with a final note on how this project differs.
5. **Methodology:** state the development method (agile), the development plan, and a new **Design** section with
   a simple UI already built (she stressed this), plus a use case diagram.
6. She mentioned a survey. The student thinks it does not belong in Semester 1. The samples agree (see section 7).
   We asked her to confirm.

The proposed structure and two questions (survey timing, OK to build a working UI prototype) were sent to her on
Teams on 3 Nov. She had seen the message by 5 Nov but had not replied.

## 6. Agreed D1 structure (main body max 14 pages)

1. **Introduction**
   - 1.1 Project Overview
   - 1.2 Problem Statement (HWUM)
   - 1.3 Aim and Objectives
   - 1.4 Research Questions
   - 1.5 Scope and Limitations
   - 1.6 Organisation
2. **Background Research**
   - 2.1 Literature Review: 2.1.1 RAG and retrieval, 2.1.2 hallucination, 2.1.3 abstention and escalation,
     2.1.4 evaluating RAG
   - 2.2 Existing Student Support Chatbots: overview, comparison table, how this project differs
   - 2.3 Technology Review: LLM, retrieval methods, UI framework, with the chosen option highlighted
   - 2.4 Summary and Research Gap (G1–G3)
3. **Methodology**
   - 3.1 Development Methodology (Scrum-inspired agile, one-week sprints, Notion, GitHub, Tuesday reviews; do not
     claim full Scrum)
   - 3.2 Development Plan (stages linked to the Gantt chart)
   - 3.3 Knowledge Base and the Four Systems
   - 3.4 Requirements (MoSCoW)
   - 3.5 Design: 3.5.1 architecture, 3.5.2 use case diagram (Student, Student Services staff, Maintainer),
     3.5.3 user interface (working prototype screenshots: answer with citations, escalation screen, staff view)
   - 3.6 Evaluation Plan (usability study in Semester 2 after ethics approval; forms in the appendix)
   - 3.7 Success Criteria
4. **Feasibility**: document sources, retrieval pilot, S1–S3 pilot, cost and latency, S4 signal, prototype,
   conclusion.
5. **Conclusions**
- **Appendices**: Gantt (Semester 1 done, Semester 2 plan), risk table (likelihood, impact, avoidance, contingency),
  PLES, GenAI summary, information sheet and consent form, questionnaire, detailed pilot tables, prompts.

Open questions for the supervisor: is three-level numbering in Nur Damia's style what she meant; is the survey a
plan with the forms in the appendix or something to run now; OK to build a working UI prototype.

## 7. What the past samples show (12 read, Introduction to Feasibility only)

- **Nur Damia D1 (Rosalind, 2025)** is effectively the supervisor's house style: Overview, Problem Statement,
  Objective (3 verb bullets), Scope. Then literature review plus component comparison tables (chosen option
  highlighted) and a software review. Requirements (MoSCoW), Architecture & Design (block diagram, flow, use case
  diagram). Feasibility with UI screenshots. Numbering goes three levels deep. No participants.
- **Izzat Hanis (Rosalind, final 2025):** Application Scope names Waterfall, a Constraints table, then a Design
  chapter (approach, architecture, interface mockups).
- **Tan Shwu En (RAG museum chatbot)** is the closest topic: numbered "To …" objectives, a Scope (in/out), existing
  chatbots compared in prose only, tool comparison tables, and a usability study with 5 HWUM students in Semester 2.
- Mufliha: Problem Statement, gaps then RQs, Feasibility with prototype mockup and success metrics, Notion for
  project management.
- McCaskell: a literature comparison table and an Agile project plan.
- Mackinnon: an "Iterative Agile Development" section.
- Hamish: a phased development plan. Chia: a 3-stage implementation plan plus API cost/latency feasibility.
- Tuma: iterative weekly cycles.
- **No sample ran a survey or study in Semester 1.** Every participant study ran in Semester 2, with forms in the
  appendix.

## 8. Next steps (in order)

1. Introduction rewrite (in progress 5 Nov).
2. Background: comparison table, about 30–35 verified references, technology review.
3. Methodology: development methodology, plan, Design (architecture diagram, use case diagram, UI prototype built
   with a simple web framework connected to S3).
4. Feasibility, Conclusions, appendices, GenAI summary, abstract.
5. Records: meeting 5 notes (`docs/meetings/2026-11-03_week8_meeting5.md`), Notion Week 8, journal 5.
6. Student to do: check the 78 draft labels, decide Gate 1, upload d1 files to Overleaf, get the section guidance
   docx from Canvas.

## Update, 5 Nov 2026 (afternoon)

- Introduction shortened to about 1.6 pages. The research questions moved to the end of Background (2.4).
- Background rewritten (about 4.6 pages): 2.1 Literature Review (2.1.1 to 2.1.4), 2.2 Existing Student Support Chatbots with
  a comparison table of 8 systems plus this project, 2.3 Technology Review table, 2.4 gaps G1 to G3 and RQ1 to RQ4.
- References: 45, all cited, numeric ACM. Verification notes in `docs/reading_list.md` ("Added 5 Nov 2026 (Background
  rewrite)"). Still to check: Walert pages and DOI, Huang TOIS volume and article number, C-Pack pages, Labadze article number.
- Feasibility 4.3 renamed from "Tools and Technology Choices" to "Prototype", because tools are now compared in 2.3.
- Page budget: Background ends on page 7, so Methodology plus Design and Feasibility must fit in about 7 pages.

## Update, 7 Nov 2026 (Saturday)

- **Full D1 draft done**: main body exactly 14 pages (Conclusions end on page 14 with about six lines spare), 51 references.
  - Methodology: 3.1 approach (Scrum-inspired one-week sprints, waterfall rejected), 3.2 development plan (5-stage
    table), 3.3 knowledge base and systems (systems table removed to save space), 3.4 requirements (summary in text,
    full MoSCoW table moved to Appendix B to fit the page limit), 3.5 design (TikZ architecture and use case diagrams in
    `d1/images/*.tex`, UI screenshots), 3.6 evaluation plan, 3.7 success criteria with reasons.
  - Feasibility: document audit, retrieval and S1-S3 pilot tables, S4 signal, cost projection (about US$14, RM62).
  - Appendices: Gantt (pgfgantt, both semesters), risk register (L x I scores), PLES, requirements, GenAI summary,
    ethics forms included as PDFs (`d1/images/appendix_*.pdf`, converted from `ethics/*.docx`).
- **UI prototype**: `src/app.py` (Streamlit; student and staff views; S1-S3 selectable) and `src/escalations.py`
  (tested). Run `streamlit run src/app.py`. Screenshots use cached pilot questions, so no API cost.
- Open points for the student: confirm the GenAI summary is accurate; fill the GenAI statement in the declaration
  (it lives in `hwu_template/declaration.tex`, which the rules say not to edit, so he decides how); acknowledgements
  text; the forms still show `[YOUR HW EMAIL]` placeholders; check Brooke 1996 details; review the 78 draft labels.
