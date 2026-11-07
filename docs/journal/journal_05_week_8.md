# Project Journal Submission 5 (Covering week 8)

Student name: Muhammad Faizal Haris bin Aidi
Student ID: H00459013
Student email address: mba2022@hw.ac.uk
Date of submission: 7 November 2026

## Title of dissertation and brief description
**A Grounded University Support Assistant: Retrieval-Augmented Generation with Confidence-Based Escalation**
This project builds and evaluates a university support chatbot that answers student questions only from official Heriot-Watt and HWUM documents using retrieval-augmented generation (RAG), cites the document and page, and escalates to staff when its confidence is low. Four systems (an FAQ-matching baseline, a plain LLM, RAG, and RAG with escalation) will be compared on a test set of about 200 questions, with a web interface for students and staff. The evaluation covers correctness, hallucination, citation accuracy, escalation quality, latency and cost.
No change to the title since Journal 1.

## Communicating with supervisor
**Meeting 5: Week 8, Tuesday 3 November 2026, in person**
- Went through the D1 draft (Sections 1 to 3). My supervisor asked for a restructure:
- Introduction: start with a problem statement specific to HWUM, renumber the sections, and look at how past samples are structured.
- Objectives: start each with "To...", keep them general without numbers, and give one bullet per system in the objective about the four systems.
- Add a Scope section after the objectives, with limitations: HWU students only, and no sensitive topics such as financial hardship or mental health.
- Background: clearer numbering, more papers, and a comparison table of existing chatbots with two to four points each and how my project differs.
- Methodology: add the development method (agile), a development plan, and a Design section with a use case diagram and a simple user interface that is already built, which she stressed was important.
- She also mentioned a survey; I was not sure whether she meant one in Semester 1, so I asked on Teams.
- The next meeting will be on Friday 13 November instead of Tuesday.
**Teams (online), 3 November 2026**
- Sent my supervisor the restructured D1 outline based on her feedback and asked her to confirm it matches what she had in mind. She has seen the message; no reply yet at the time of writing.

## References consulted
- Literature for the rewritten Introduction and Background (found via the Internet: ACL Anthology, arXiv, PMLR, NeurIPS and publisher or university repository pages), including: Trienes et al. 2025 (Marcel, EMNLP demos); Chen et al. 2024 (RGB, AAAI); Gao et al. 2023 (ALCE) and Liu et al. 2023 (verifiability), both EMNLP; Neupane et al. 2024 (BarkPlug); Chen et al. 2024 (admissions chatbot, Educational Technology & Society); Nguyen and Quan 2025 (URAG); Pathiyan Cherumanal et al. 2024 (Walert, CHIIR); Khasanova and Suh 2025 (Electronics); Kuhail et al. 2023 and Okonkwo and Ade-Ibijola 2021 and Labadze et al. 2023 (chatbot reviews); Rajpurkar et al. 2018 (SQuAD 2.0); Kamath et al. 2020 (selective QA); Kadavath et al. 2022; Feng et al. 2024 (abstention); Farquhar et al. 2024 (semantic entropy, Nature); Asai et al. 2024 (Self-RAG); Yan et al. 2024 (CRAG); Mozannar and Sontag 2020 (learning to defer); Huang et al. 2025 (hallucination survey); Fan et al. 2024 (RAG survey); Liu et al. 2024 (Lost in the Middle); Thakur et al. 2021 (BEIR); Xiao et al. 2024 (BGE embeddings); Saad-Falcon et al. 2024 (ARES); Cohen 1960 (kappa); Dror et al. 2018 (significance testing); Brooke 1996 (SUS).
- Project management and PLES: the 2020 Scrum Guide, the BCS Code of Conduct (2022), Malaysia's Personal Data Protection Act 2010 (amended 2024) and Copyright Act 1987, and the Gemini API pricing page.
- Twelve past HWU dissertations and D1 reports from the project files, compared section by section with the D1 marking rubric to plan the structure, length and referencing (most use about 35 to 50 references).
- Claude (AI assistant): used to search for papers and check every reference's details against its source, to compare the past samples with the rubric, to draft and edit parts of the D1 report (which I reviewed and revised), to write the web interface code, and to draft these records. I reviewed all of it and can explain each part. Details are in the D1 Generative AI Summary.

## Tools explored/used
- Gemini API (gemini-3.6-flash, paid tier): used for the plain LLM (S2), RAG (S3) and the LLM judge in the pilot; all responses are cached so reruns cost nothing.
- sentence-transformers with the bge-small embedding model: used for dense and hybrid search.
- Streamlit: new this week; used to build the working interface prototype (student view with citations and escalation, staff view of escalated questions).
- LaTeX with TikZ and pgfgantt: used for the architecture and use case diagrams and the Gantt charts in D1.
- GitHub: https://github.com/sutin1215/grounded-university-support-assistant (D1 draft, interface code and records committed).
- Notion: task board updated.
- Failed attempts: PlantUML was tried for the use case diagram, but its automatic layout was hard to read, so the diagram was redrawn in TikZ. My laptop's virtual environment is still missing sentence-transformers, so the dense, hybrid and S3 runs were done in a separate environment; installing from requirements.txt will fix this.

## Other work carried out
- Completed the S1 to S3 pilot on 26 questions (1 November): hybrid search was best (correct page in the top 5 for 95% of answerable questions, MRR 0.79); correct on 20 answerable questions: S1 8, S2 6, S3 20; unanswerable questions declined: S1 5 of 6, S2 1 of 6, S3 6 of 6; about US$0.0035 per S3 question with a median of 2.6 seconds. The LLM judge agreed with the reference labels on 72 of 78 answers (kappa 0.89), but those labels were drafted with AI assistance and I still need to check them by hand.
- Tested retrieval scores as an escalation signal for S4: the top dense score separated answerable from unanswerable questions well (AUROC 0.88), but one near-miss question about a late-payment charge scored higher than six answerable ones.
- Analysed the past samples and the rubric before rewriting, then restructured the whole D1: a shorter Introduction with an HWUM problem statement, objectives and scope; a rewritten Background with a literature review in four parts, a comparison table of eight existing chatbots and a technology review table; a Methodology with the agile approach, development plan, requirements, design (architecture, use case diagram and interface) and evaluation plan; Feasibility; Conclusions; and appendices (Gantt charts, risk register, PLES, requirements, GenAI summary, ethics forms). The main body is 14 pages with 51 references.
- Built the interface prototype on top of S3: answers show page citations with a link to the exact PDF page, unanswerable questions are logged with a reference number, and staff can mark them as resolved.

## Plan the next 2 to 3 weeks
**Week 9 (9 to 15 Nov)**
- Read the full draft carefully, check the 78 draft labels and the remaining reference details, and finish the GenAI statement and acknowledgements.
- Send the full D1 draft to my supervisor by Wednesday 11 November; meeting 6 on Friday 13 November.
- Start the D2 storyboard and script.
**Week 10 (16 to 22 Nov)**
- Apply my supervisor's feedback; check D1 against the rubric and page limit; record the D2 video.
**Week 11 (23 to 26 Nov)**
- Submit D1 and D2 early (aim 24 November, deadline 26 November), alongside the Data Mining D2 (25 November) and the AI class test (27 November).

## Overall reflection
My plan was to send the full D1 draft by 6 November, but meeting 5 showed that the structure did not match what my supervisor expected, so I restructured the report first and moved the draft date to 11 November, before our next meeting on 13 November. At first I was not sure that a working interface and a use case diagram belonged in a D1 proposal, but the past samples, including one by her own student, include a design section with these, and building the prototype early also showed that the whole pipeline already works end to end.
The main challenge was the 14-page limit: my first rewritten Introduction was too long, so I compared the past samples before writing more and kept each section to a page budget, moving the full requirements table to an appendix. The pilot is encouraging but small and written close to the documents' wording, so I have described all numbers as indicative, and the next step that matters most is checking the AI-drafted labels myself.
Direction: on track to send the full D1 draft by 11 November and submit D1 and D2 by 24 November.

## Additional section, if needed
None this time.
