# Project Journal Submission 6 (Covering week 9)

Student name: Muhammad Faizal Haris bin Aidi
Student ID: H00459013
Student email address: mba2022@hw.ac.uk
Date of submission: 16 November 2026

## Title of dissertation and brief description
**A Grounded University Support Assistant: Retrieval-Augmented Generation with Confidence-Based Escalation**
This project builds and evaluates a university support chatbot that answers student questions only from official Heriot-Watt and HWUM documents using retrieval-augmented generation (RAG), cites the document and page, and escalates to staff when its confidence is low. Four systems (an FAQ-matching baseline, a plain LLM, RAG, and RAG with escalation) will be compared on a test set of about 200 questions, with a web interface for students and staff. The evaluation covers correctness, hallucination, citation accuracy, escalation quality, latency and cost.
No change to the title since Journal 1.

## Communicating with supervisor
**Meeting 6: Week 9, Friday 13 November 2026, in person**
- Went through the full D1 draft. My supervisor said the report is good and asked for small changes:
- Reword the scope as "This project does not involve ..." instead of "Out of scope are ...".
- Improve the Conclusions a little, following the past samples.
- Mention the Notion board and GitHub repository in the main report, and refer to every appendix from the relevant section.
- The survey does not need to run this semester. It should run in Semester 2, once the final system is done, and the report will be updated then. This matches my planned usability study.
- There was not enough time to show the prototype, so she asked me to share screenshots of it.

## References consulted
- Past samples from the project files (Nur Damia Zulfa D1 2025, Chia Zheng Rong D1 2025, Mackinnon and others), compared for section length and depth, and later for how the Conclusions are written.
- The D2 guide and marking rubric in the course information (Canvas), used to plan the video script.
- The Gemini API pricing and terms pages, rechecked for the technology table. I also tried to compare prices with other providers, but could not access their official pricing pages, so no prices for them were added.
- Claude (AI assistant): used to compare my draft with the past samples, to suggest and make edits to D1 (which I reviewed), to rerun and extend the pilot, to redesign the interface, to take the prototype screenshots, to draft the D2 script and to draft these records. I reviewed all of it, and I decided the reference labels myself. Details are in the D1 Generative AI Summary.

## Tools explored/used
- Gemini API (gemini-3.6-flash): pilot extended to 32 questions, plus a new model signal for S4. All responses are cached.
- Streamlit with custom CSS and open-licence fonts (Atkinson Hyperlegible, Literata): used to redesign the interface as AskWatt.
- Playwright: used to take consistent screenshots of the prototype for the report and my supervisor.
- MiKTeX: installed so D1 compiles on my laptop as well as in Overleaf.
- GitHub: https://github.com/sutin1215/grounded-university-support-assistant
- Notion: task board and weekly pages.
- Failed attempts: keeping every table inside its own section at first left large blank gaps on some pages, so I shortened the text around the tables. Competitor pricing pages could not be reached, so that comparison was left out rather than using unchecked numbers.

## Other work carried out
- Simplified Background and Methodology after comparing them with the past samples. Put each comparison table in its own section, cut the chatbot comparison to five systems and moved the MoSCoW table back into the Methodology.
- Extended the pilot to 32 questions, adding four paraphrased and two near-miss questions. Results: hybrid search found the right passage in the top five for 22 of 24 answerable questions (MRR 0.78); fully correct answers: S1 8, S2 8, S3 24 of 24; unanswerable questions declined: S1 6, S2 2, S3 8 of 8. The top dense score separated answerable from unanswerable questions with an AUROC of 0.85. I reviewed all 96 reference labels myself and decided the six disputed ones. The LLM judge agreed on 90 of 96 (kappa 0.91). The pilot cost US$0.37, and the full evaluation is projected at about US$5.80.
- Final pass on D1:
  - A new evaluation design table, and a clearer technology table showing the option chosen, the evidence for it and the alternatives rejected.
  - A risk heat map and a signal plot.
  - The GenAI statement.
  - The main body is now 14 pages, within the limit.
- 16 November (after the meeting): applied my supervisor's feedback (scope wording, a fuller four-paragraph Conclusions, and pointers to Notion, GitHub and every appendix in the main text). Fixed a small interface bug, took a full set of AskWatt screenshots for my supervisor, and drafted the D2 video script.

## Plan the next 2 to 3 weeks
**Week 10 (16 to 22 Nov)**
- Send the AskWatt screenshots to my supervisor and apply any comments.
- D2: make the slides, record the demo clip and narration, then edit to under 5 minutes.
- Final D1 checks: page limit, references, Overleaf build.
**Week 11 (23 to 26 Nov)**
- Make the GitHub repository private, then submit D1 and D2 (aim 24 November, deadline 26 November), alongside the Data Mining D2 (25 November) and the AI class test (27 November).
**Semester 2, Weeks 1 to 3**
- Write and label the 200 test questions, starting straight after the December exams.

## Overall reflection
This week went to plan: the full D1 draft was ready before meeting 6, and my supervisor was happy with it, asking only for small changes. Comparing my draft with the past samples early was useful. My Methodology was longer and deeper than theirs, so simplifying it made the report easier to read and freed space for the evaluation design table, which I think makes the plan much clearer.
The main challenge was the 14-page limit together with keeping each table in its own section, which needed several rounds of small layout fixes. I also learned to be careful with honesty in the pilot: some answers were cut off by the token limit, and I now report which system they came from, rather than letting S3's perfect score hide it.
I did not show the prototype in the meeting, which was a missed chance. Next time I will show the demo first, since it takes the least explaining.
Direction: on track to submit D1 and D2 by 24 November.

## Additional section, if needed
None this time.
