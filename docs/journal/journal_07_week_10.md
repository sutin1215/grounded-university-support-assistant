# Project Journal Submission 7 (Covering week 10)

Student name: Muhammad Faizal Haris bin Aidi
Student ID: H00459013
Student email address: mba2022@hw.ac.uk
Date of submission: 20 November 2026

## Title of dissertation and brief description
**A Grounded University Support Assistant: Retrieval-Augmented Generation with Confidence-Based Escalation**
This project builds and evaluates a university support chatbot that answers student questions only from official Heriot-Watt and HWUM documents using retrieval-augmented generation (RAG), cites the document and page, and escalates to staff when its confidence is low. Four systems (an FAQ-matching baseline, a plain LLM, RAG, and RAG with escalation) will be compared on a test set of about 200 questions, with a web interface for students and staff. The evaluation covers correctness, hallucination, citation accuracy, escalation quality, latency and cost.
No change to the title since Journal 1.

## Communicating with supervisor
**No meeting this week (Week 10)**
- My supervisor sent a pre-submission checklist by email this week. I applied all of it to D1 on 18 November (details under Other work carried out).
- 19 November (Teams): I sent her the AskWatt prototype screenshots and the D2 slides. I asked for her feedback on both and said I would then send all my journals for her to sign. There was no reply by the time of writing, so I went ahead with the video using the checklist and the D2 rubric. Any comments that arrive before 24 November will still be applied.

## References consulted
- The D2 guide and marking rubric (Canvas): five-minute limit, what each part should cover, readable slide text, and no requirement to show my face on camera.
- My supervisor's pre-submission checklist, used as a final list for D1.
- The past samples in the project files, compared again for how appendices are ordered and what they contain.
- The official Heriot-Watt coursework submission policy PDF on hw.ac.uk, opened in the demo. I checked that it matches the copy in my knowledge base, so the demo shows the real source.
- Claude (AI assistant): used to apply the checklist edits to D1 (which I reviewed), to draft the D2 script with me, to fill my chosen Canva template, to record the scripted AskWatt demo and to edit the video and subtitles from my own narration, and to draft these records. I wrote the final wording, recorded all the narration myself and checked the finished video. This use is declared in the D1 Generative AI Summary.

## Tools explored/used
- Canva: D2 slides, built from a ready-made template that I picked, with only my own screenshots, Gantt chart and risk heat map. The Gantt charts from D1 were redrawn in Canva for the slides (the report keeps its own LaTeX versions).
- Streamlit (AskWatt): demo run from cached answers only, so recording it made no new API calls and cost nothing.
- Playwright: a scripted browser run of the demo, so the clip is smooth and can be repeated exactly.
- ffmpeg: cutting long pauses, cleaning and levelling the audio, adding the slides and burning in subtitles.
- faster-whisper (speech-to-text): timing the subtitles to my narration and checking that what I said matches the script.
- Notion (progress board, now screenshotted in an appendix) and GitHub: https://github.com/sutin1215/grounded-university-support-assistant
- Failed attempts: my first slides were built as HTML pages, but they looked machine-made, so I dropped them. An AI-generated Canva deck added an invented campus photo and crest; I rejected it, because a made-up image of the university would be misleading, and used a plain template with my own material instead. In the first test edit, the audio went silent halfway through because of a mistake in how the cuts were made; this was fixed before the full edit.

## Other work carried out
- 16 November (after Journal 6): restyled AskWatt in the Heriot-Watt brand colours and fonts from the official brand guidelines (no logo, and a notice saying it is a student prototype). Retook the screenshots and redid D1 Figure 3. Dropped the plan for a second person to write questions, so the test set will be written and labelled by me alone. Final D1 check of numbers, references, spelling and layout.
- 18 November: applied the supervisor's checklist to D1. I added a motivation paragraph, tightened the scope wording, did a language pass on the abstract, introduction and conclusion, and used my full name.
- 18 November: added three appendices: progress tracking (Notion screenshots); pilot study materials (the sources, all 32 questions with their labels, the prompts and the cost breakdown); and interface screenshots. I also put the appendices in order and filled in the Journal 1 date. The main body still ends on page 14.
- 18 to 19 November: wrote the D2 script (version 2) to follow the rubric, at about 4:40. Built the 11-slide deck in Canva.
- 20 November: added my full name, student ID and the full project title to the first slide and the opening line.
- 20 November: recorded the narration in 12 parts. A speech-to-text check against the script caught two wrong numbers I had said (37 sources instead of 27, and 30 points instead of 20), so I re-recorded those parts.
- 20 November: recorded the AskWatt demo. It shows a cited answer, then "Open page" opening the official policy PDF at the 30% late-penalty line; an unanswerable question passed to Student Services with a ticket number, and the staff view; and the plain model giving a wrong 3% penalty for the same question.
- 20 November: finished the D2 video. It is 4 minutes 38 seconds (under the 5-minute limit), with subtitles, and narrated in my own voice. It is saved outside the repository with the recordings.

## Plan the next 2 to 3 weeks
**Week 11 (23 to 29 Nov)**
- Send all seven journals to my supervisor for her signature, and apply any late comments on the slides or prototype.
- Update the D1 Generative AI Summary to cover the video editing, subtitles and scripted demo recording, then recompile and check the page count.
- Make the GitHub repository private and give my supervisor access, then submit D1 and D2 on Canvas (aim 24 November, deadline 26 November).
- Other courses: Data Mining D2 (25 November) and the AI class test (27 November).
**Week 12 (30 Nov to 6 Dec)**
- Mini-viva (30 November): prepare to explain the design choices, the pilot results and the Semester 2 plan.
- Computer Networks class test 2 (1 December), then revision for the exams (7 to 18 December).
**Semester 2, Weeks 1 to 3**
- Write and label the 200 test questions, starting straight after the exams.

## Overall reflection
This week went to plan: D1 is in its final form and the D2 video is finished four days before my target date. The most useful thing was checking my own narration against the script with speech-to-text. I would not have noticed that I said "37 sources" instead of 27 just by listening, and a wrong number in the video would contradict the report.
The main lesson was about presentation. My first two slide designs were technically fine but did not look like my own work, and one included an invented picture of the university, which I could not have defended. Starting from a simple template with only real screenshots and my own charts gave a cleaner result in less time. I also extended the demo to open the official PDF at the cited page, because that shows the main idea of the project (every answer can be checked against its source) better than any slide.
The challenge was not hearing back from my supervisor on the slides and prototype. I used her checklist and the rubric so the work was not held up, and I will still apply any comments before submitting.
Direction: on track to submit D1 and D2 on 24 November.

## Additional section, if needed
None this time.
