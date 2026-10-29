# Project Journal Submission 4 (Covering week 7)

Student name: Muhammad Faizal Haris bin Aidi
Student ID: H00459013
Student email address: mba2022@hw.ac.uk
Date of submission: 30 October 2026

## Title of dissertation and brief description
**A Grounded University Support Assistant: Retrieval-Augmented Generation with Confidence-Based Escalation**
This project builds and evaluates a university support chatbot that answers student questions only from official university documents using retrieval-augmented generation (RAG), cites its sources, and escalates to staff when its confidence is low. Four systems (an FAQ-matching baseline, a plain LLM, RAG, and RAG with escalation) will be compared on a purpose-built test set of about 200 questions. The artefact is a locally run Python web application, and the evaluation covers correctness, hallucination, citation accuracy and escalation quality.
No change to the title since Journal 1.

## Communicating with supervisor
**Teams (online), 26 October 2026**
- Supervisor confirmed she had signed the ethics form and that it would go to the committee, and asked me to start the project work so I would not be delayed.
- Explained that most of the previous weeks went into the ethics application and the D1 draft in Overleaf.
**Meeting 4: Week 7, Tuesday 27 October 2026, in person**
- Gave an update since Week 5: ethics submitted, project records organised, and the first pilot built.
- Demonstrated the pilot: document search with page-level citations compared with the FAQ baseline on four example questions, and the first pilot numbers.
- Asked whether accuracy matters: my supervisor said that for this project the analysis matters more than the accuracy, as long as the experiments are done properly and every choice is justified and explained.
- Asked about the LLM API: any provider is fine, and costs can be claimed later with receipts.
- My supervisor gave a lot of feedback on the current D1 draft and asked me to share the Overleaf link again so she can read it properly.
**Teams (online), 29 October 2026**
- Shared the Overleaf link again, asked for her views on the current draft, and told her I am starting the next sections this week.

## References consulted
- The five official documents loaded into the pilot: the L&T briefing paper on the coursework submission policy, the Mitigating Circumstances Procedure (V1, Sept 2026), the HAPS information for undergraduates, the 2026/27 international fee structure, and the HWUM fees and payment guide. Downloaded from the HWU website.
- Robertson and Zaragoza (2009) on BM25, used to understand the keyword search method in the pilot (citation details to verify).
- Supervisor's past-year example dissertation, used as a guide to structure, requirement tables and the risk table.
- Claude (AI assistant): used to write the pilot code, the pilot questions and the evaluation script, and to organise my project records. I reviewed and ran all of it and can explain each part.

## Tools explored/used
- Python with PyMuPDF (PDF text extraction), rank_bm25 (BM25 search), scikit-learn (TF-IDF and similarity), PyYAML (settings) and pytest (unit tests): all installed and used in the pilot.
- VS Code: used to run the pilot and the demo on my laptop.
- GitHub: pilot code, results, journal, meeting notes and D1 LaTeX files committed this week.
- https://github.com/sutin1215/grounded-university-support-assistant
- Notion: task board and weekly update pages updated.
- Failed attempts: the coursework submission policy PDF and the July 2025 fees and payment guide could not be downloaded, so I used the L&T briefing paper on coursework submission and the current Malaysia fees and payment guide instead.

## Other work carried out
- Built the pilot: ingestion of 5 official PDFs into 45 page-tagged passages, BM25 and TF-IDF search, the FAQ-matching baseline (S1) with 12 FAQs, and a demo.
- Wrote 26 pilot questions (20 answerable, 6 not answerable from the documents) with gold answers and exact quotes, and a script that finds the page of each quote in the PDF.
- First results: BM25 finds the correct page in the top 5 for 90% of answerable questions (first place 60%), TF-IDF 85% (45%). The FAQ baseline answers 40% of answerable questions correctly and escalates 5 of the 6 unanswerable ones.
- Observed failure cases: the FAQ baseline gives confident wrong answers when FAQs sound alike, keyword search misses different wording ("extension" vs "extensions"), and search always returns passages even when the documents cannot answer, which motivates confidence-based escalation.
- Organised all project records in GitHub and Notion, and moved the D1 LaTeX project into the repository as the main copy.

## Plan the next 2 to 3 weeks
**Week 7 (rest of week)**
- Draft the Background Research and Methodology sections of D1.
**Week 8 (2 to 6 Nov)**
- Add word-stem matching and embedding search; choose an LLM API and run the plain LLM (S2) vs RAG (S3) pilot.
- Write the Feasibility section, Gantt chart, risk table and PLES; set measurable success criteria; send the full D1 draft to my supervisor by 6 November.
**Week 9 (9 to 13 Nov)**
- Apply my supervisor's feedback to D1 and prepare the D2 storyboard and script.

## Overall reflection
This week I recovered the pilot that had slipped from Weeks 5 and 6. The pilot already shows the main problem the project addresses: simple approaches either miss answers worded differently or give confident wrong answers, and search alone cannot tell when the documents do not contain the answer. My supervisor's point that analysis matters more than accuracy changes how I will write the evaluation: the focus will be on explaining why each system succeeds or fails, with justified experiment choices, not only on the highest score.
Compared with the plan in Journal 3, the ethics submission and the pilot are done, but the plain LLM vs RAG comparison and the Background Research section are still behind. I also need to follow up on my supervisor's feedback on the current D1 draft before writing too much more.
Direction: ethics submitted; pilot on track; D1 draft by 6 November is tight but achievable.

## Additional section, if needed
None this time.
