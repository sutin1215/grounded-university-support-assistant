# D2 video script: Preparation and Feasibility (target 4:40, limit 5:00)

Draft 1, 16 Nov 2026. About 650 spoken words: about 4:20 at a normal 150 words a minute, 4:50 at a slow 135. If a run-through goes over 4:50, cut the AUROC sentence in Part 4 first. Every number below matches D1 v8.

## What the markers look for (D2 guide), and where each part covers it
| Rubric point | Where in the video |
|---|---|
| Preparation work: what's done and why it matters | Part 2 |
| Method and tool choice, justified against alternatives | Part 3 |
| Feasibility evidence: pilot data, prototype, calculations | Part 4 |
| Plan, dependencies, contingencies; risks quantified with mitigations and fallbacks | Part 5 |
| Success criteria: concrete, measurable, justified | Part 6 |
| Professional, legal, ethical and social issues | Part 7 |
| Professionalism: structured, under 5:00, clear audio, readable visuals | All parts, plus the checklist at the end |

## Visuals to prepare (the guide suggests 5 slides or fewer, plus clips)
- **Slide 1:** title, your name, supervisor, and one line on the problem
- **Slide 2:** preparation timeline (Weeks 1 to 9), one line per item
- **Slide 3:** tool choices, a simplified Table 2 (Chosen / Why / Rejected), next to the architecture diagram (Fig. 1)
- **Clip:** AskWatt screen recording, about 40 seconds (see Part 4)
- **Slide 4:** pilot numbers, a simplified Table 7: 24 answerable and 8 unanswerable questions, S1/S2/S3
- **Figures from D1:** Semester 2 Gantt (Fig. 6) and risk heat map (Fig. 7)
- **Slide 5:** success targets on the left, ethics and legal points on the right

Slide text at least 24 pt, dark on light. Never show the `.env` file, the API key, or your email.

---

## Part 1 (0:00–0:25): Title and problem
**Show:** Slide 1

> "Hi, I'm Faizal, and this is my honours project: a grounded support assistant for students at Heriot-Watt Malaysia.
> Students often need quick answers about fees, deadlines, late submission and mitigating circumstances. The official answers exist, but they are spread across many PDFs and web pages. And general chatbots answer these questions confidently, and often incorrectly."

## Part 2 (0:25–1:05): Preparation work
**Show:** Slide 2 (timeline)

> "This semester, I audited 27 sources and kept the 23 official ones, then split five key PDFs into 45 passages, each tagged with its page.
> I built five search methods and three of my four systems: an FAQ bot, a plain language model, and one that answers only from the documents, with citations.
> I tested them on 32 pilot questions, built a working app called AskWatt, and my usability study has ethics approval."

## Part 3 (1:05–1:45): Method and tool choices
**Show:** Slide 3 (tool table and architecture diagram)

> "Each tool was picked against four tests: low cost, it can be run on a laptop, tests can be repeated exactly, and evidence that it works.
> For the language model, I chose Gemini Flash, at about a third of a US cent per question. A local model would be free, but too slow on a laptop.
> For search, I combine keyword search with meaning-based search, because in the pilot each one missed passages the other found. And plain Python, not LangChain, keeps every setting visible."

## Part 4 (1:45–2:50): Feasibility evidence and demo
**Show:** AskWatt clip, then Slide 4

Record the clip beforehand: the late-penalty example question with S3, then "What time does the library close on Saturdays?", then the staff view, then S2 on the late-penalty question. All of these are cached, so they cost nothing.

> "Here is AskWatt. The answer comes only from the official documents, and each blue number links to the exact page of the PDF.
> When the documents don't cover a question, it doesn't guess: it passes it to Student Services with a ticket number, and staff see it in their own view.
> The plain model, on the same late-work question, says 3% per day. The official document says 30%."

**Switch to Slide 4.**

> "In the pilot, the document-based system was fully accurate on all 24 answerable questions and declined all 8 it couldn't answer. The plain model managed only 8, and made up answers to 6 it should have declined. The whole pilot cost 37 US cents.
> These pilot questions follow the documents' wording, so the full score is a ceiling. The final test set is harder, and that's where the confidence check matters: one search score already split the two groups with an AUROC of 0.85."

## Part 5 (2:50–3:35): Plan and risks
**Show:** Semester 2 Gantt, then the heat map

> "Semester 2 has five stages, each needing the one before: write 200 test questions, 60 for tuning and 140 used once; build the confidence check; run the final tests; the usability study in Weeks 6 to 8; then write up, with Weeks 9 and 10 as a buffer.
> The two biggest risks score 12 out of 25. Writing the questions may take longer, so I start straight after the exams, and the fallback is 150 questions with the same mix. Workload from other courses is covered by weekly sprints and the buffer, and the fallback is to drop an optional feature and shorten the study."

## Part 6 (3:35–4:10): Success targets
**Show:** Slide 5, left side

> "Success is measurable. The document-based system should be fully accurate on at least 80% of answerable questions, 20 points ahead of the plain model, with paired tests. At least 85% of its citations should support the answer. The confidence check should halve the false answers while sending no more than a fifth of answerable questions to staff. And the app should answer within 10 seconds, cost under 100 ringgit, and score at least 68 on the usability scale."

## Part 7 (4:10–4:40): Professional, legal, ethical and social
**Show:** Slide 5, right side

> "Ethically and legally, the app collects no personal data: only the question text is kept when something is passed to staff, in line with the PDPA and UK GDPR. Documents are cited by page, not copied. The usability study has ethics approval and informed consent, I follow the BCS Code of Conduct, and I declare my use of AI tools. The aim is to support staff, not replace them."

## Part 8 (4:40–4:55): Close
**Show:** Slide 1 again, or the AskWatt home screen

> "So the documents, the search, the answers, a working app and the budget are all in place. Semester 2 is about the harder test set, the confidence check, and a fair, measured comparison. Thank you for watching."

---

## Words to practise (prominent R sounds that have no easy swap)
Heriot-Watt, Faizal (fine) / Haris (if you add it), grounded, PDFs, prototype is avoided (say "app"), Student Services, ringgit, PDPA (fine), GDPR, ceiling (fine), "three", "approved", "risks", "around".

Swaps already used: "search" for retrieval, "fully accurate" for correct, "false answers" for wrong answers, "targets" for criteria, "app" for prototype, "made up" for hallucinated.

## Recording checklist
1. Run AskWatt and record the clip on its own first (OBS or Xbox Game Bar), with the browser zoomed to 125% so the text is readable.
2. Record the narration over the slides in one take per part. Short parts are easy to redo.
3. Edit in Clipchamp: put the parts together, trim the pauses, and normalise the audio.
4. Check the length is under 5:00 (aim for 4:40), the text is readable at 1080p, and no key or email is visible.
5. Export as MP4 (H.264), under 100 MB.
