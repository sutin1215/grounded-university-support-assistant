# Project Journal Submission 2 (Covering week 4-5)

Student name: Muhammad Faizal Haris bin Aidi
Student ID: H00459013
Student email address: mba2022@hw.ac.uk
Date of submission: 27 October 2026

## Title of dissertation and brief description
**A Grounded University Support Assistant: Retrieval-Augmented Generation with Confidence-Based Escalation**
This project builds and evaluates a university support chatbot that answers student questions only from official university documents using retrieval-augmented generation (RAG), cites its sources, and escalates to staff when its confidence is low. Four systems (an FAQ-matching baseline, a plain LLM, RAG, and RAG with escalation) will be compared on a purpose-built test set of about 200 questions. The artefact is a locally run Python web application, and the evaluation covers correctness, hallucination, citation accuracy and escalation quality.
No change to the title since Journal 1.

## Communicating with supervisor
**Week 4: Microsoft Teams (online), 8 October 2026**
- Shared a more detailed and thought-through version of my project idea and asked for my supervisor's opinion on it.
- Told my supervisor I would not book a consultation that week, and agreed that weekly sessions start on Tuesday 13 October (fixed slot: Tuesdays 11:30).
- Updated her on my plan for the week: reading papers on existing university support chatbots, compiling a list of university documents available online, and starting the proposal in LaTeX.
- Asked if I could send updates on Teams that week to get her opinion on a few things.
**Meeting 3: Week 5, Tuesday 13 October 2026, in person**
- Discussed the official documents I had collected. My supervisor confirmed it is fine to use them for the project because they are publicly available online.
- Walked my supervisor through the flow of the application: ingest documents, retrieve relevant passages, answer with citations, and escalate to staff when confidence is low.
- Received a past-year example report to use as a guide for D1.
- Shared the link to my Overleaf project so she can follow the D1 draft.

## References consulted
- Trienes et al. (2025), Marcel: a conversational agent for university student support (arXiv). Closest related work; abstention is left to the generation prompt, which motivates my measured escalation component.
- Lewis et al. (2020), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (NeurIPS). The original RAG method, used to justify the RAG systems S3 and S4.
- Wen et al. (2025), Know Your Limits: a survey of abstention in LLMs (TACL). Framework and metrics for when a model should not answer.
- Peng et al. (2025), Unanswerability Evaluation for RAG (ACL). Taxonomy of unanswerable questions, used to design the unanswerable part of my test set.
- Zheng et al. (2023), Judging LLM-as-a-Judge (NeurIPS). Strengths and biases of LLM judges; supports calibrating the judge against human scores.
- Also identified (abstracts and metadata checked, full reading still to do): Gao et al. (2023) RAG survey; Ji et al. (2023) hallucination survey; Es et al. (2024) RAGAs; Cormack et al. (2009) reciprocal rank fusion; Nguyen et al. (2021) NEU-chatbot; Odede and Frommholz (2024) JayBot.
- How found: web and Google Scholar searches, arXiv, ACL Anthology and publisher pages. Claude (AI assistant) was used to help search, check the metadata and write first summaries of the five priority papers; I recorded this in my literature review log.
- 27 candidate sources from the HWU and HWUM websites (fee pages and guides, coursework submission policy, mitigating circumstances procedure, assessment and progression rules, academic regulations), found by searching the university website. Four third-party or other-university pages were found and excluded.

## Tools explored/used
- GitHub: repository updated with the official document source list and the Week 4 reading list (commits on 8 October).
- https://github.com/sutin1215/grounded-university-support-assistant
- Overleaf / LaTeX: HWU template set up for D1; the Introduction and the section skeleton are drafted and compile. Link shared with my supervisor.
- Notion: task board used to track the Week 4 and Week 5 tasks.
- Claude (AI assistant): used for the literature search, paper summaries, the source list and drafting the Introduction, which I then reviewed and edited.
- Pilot tools (Python, rank_bm25, scikit-learn, PyMuPDF) were planned for Week 5 but not yet set up in this period.
- No failed attempts to report.

## Other work carried out
- Built a reading list of 10 papers with notes on why each matters, and a literature review log with summaries of the five priority papers.
- Compiled the official document source list (27 entries: 23 official, 4 excluded), with version, scope, intended use and permission notes. Older versions are kept on purpose to test how the system handles outdated information.
- Drafted the D1 Introduction in Overleaf: motivation, aim, eight objectives (O1 to O8) and four research questions (RQ1 to RQ4), plus the skeleton for the remaining D1 sections.
- Outlined the ethics application (participants, recruitment, consent, data handling and use of a hosted LLM).
- Prepared for and attended the Week 5 meeting.

## Plan the next 2 to 3 weeks
**Week 6 (19 to 23 Oct)**
- Complete the ethics form with the information sheet, consent form, sample questionnaire and recruitment advertisement, and send it to my supervisor.
- Start the pilot: download a few official documents and set up ingestion and retrieval.
**Week 7 (26 to 30 Oct)**
- Submit the ethics application (deadline 30 October).
- Pilot: FAQ baseline (S1), retrieval demo and 20 to 30 pilot questions with gold answers.
**Week 8 (2 to 6 Nov)**
- Pilot comparison of plain LLM (S2) vs RAG (S3) with first numbers.
- Draft the Background Research and Methodology sections and send a full D1 draft to my supervisor by 6 November.

## Overall reflection
Week 4 went to plan: the reading list, the official document source list, the D1 Introduction and the ethics outline were all completed, and my supervisor confirmed in Week 5 that the public documents can be used, which removes the main risk I flagged in Journal 1.
Week 5 did not go to plan. The pilot (document ingestion, the FAQ baseline and 20 to 30 pilot questions) and the start of the ethics form were planned for this week but were not started. Most of my time that week went into another course assignment, which needed far more study and work than I had planned for. As a result the pilot is now about two weeks behind, so I have moved it into Week 7 and will keep the ethics work on its own track so the ethics deadline is not affected.
Direction: behind on the pilot, on track for the ethics deadline (30 Oct) and for D1/D2 (26 Nov) if the pilot is completed in Week 7.

## Additional section, if needed
None this time.
