# D2 video script, version 2 (18 Nov 2026)

Target 4:40, limit 5:00. About 680 spoken words: 4:30 at 150 words a minute, 4:40 at 145. If a run-through goes over 4:50, cut the judge sentence in Part 4 first, then the tool sentence about LangChain. Format agreed on 18 Nov: voice-over only, 5 Canva slides plus the AskWatt clip, the Canva Gantt page and the risk heat map, recorded part by part in Clipchamp. Every number matches D1 v13.

## Coverage check

| What is asked for | Source | Part |
|---|---|---|
| Overview | Dr Rosalind's email | 1 |
| Problem statement | Dr Rosalind's email | 1 |
| Objectives and scope | Dr Rosalind's email | 2 |
| System diagram, explained quickly and precisely | Dr Rosalind's email | 3 |
| Method and tool choice, justified against alternatives | Rubric | 3 |
| Preparation work: what's done and why it matters | Rubric | 4 |
| Feasibility evidence: pilot data, prototype, calculations | Rubric | 4 |
| Plan with dependencies and contingencies | Rubric | 5 |
| Quantified risks, each with mitigation and fallback | Rubric | 5 |
| Success criteria: concrete, measurable, justified | Rubric | 6 |
| Professional, legal, ethical and social issues | Rubric | 6 |
| Within 5:00, clear audio, readable visuals | Rubric and email | All |

## What goes on screen

| Asset | Content | Used in |
|---|---|---|
| Slide 1 | Title "AskWatt: a grounded support assistant for HWUM students", name, supervisor; the problem in three short lines with the numbers 23 sources, 6 outdated, plain chatbot 8/24 | Part 1, Part 7 |
| Slide 2 | Objectives O1 to O5 as five short lines; scope in and out as two columns | Part 2 |
| Slide 3 | D1 Figure 1 (architecture), with three tool choices underneath: Gemini Flash vs local model, hybrid search vs one method, plain Python vs LangChain | Part 3 |
| AskWatt clip | About 40 s: the late-penalty example with S3, the library question passed to staff, the staff view, then S2 on the late-penalty question | Part 4 |
| Slide 4 | Pilot numbers: S1/S2/S3 on 24 answerable and 8 unanswerable questions; judge 90/96; cost US$0.37, projected about US$6 (RM26) against RM100 | Part 4 |
| Canva Gantt | Page 2 of "AskWatt project timeline" (Semester 2 plan) | Part 5 |
| Heat map | D1 Figure 7 (risk heat map) | Part 5 |
| Slide 5 | Success targets on the left; PLES points on the right | Part 6 |

Slide text 24 pt or larger, dark on light, HW colours. Never show the `.env` file, the API key or an email address.

---

## Part 1 (0:00–0:30): Overview and problem
**Show:** Slide 1

> "Hi, I'm Faizal. This is AskWatt, my honours project: a support assistant for Heriot-Watt Malaysia students that answers only from official documents, shows its sources, and passes the question to staff when it isn't sure.
> It's needed because answers on fees, deadlines and penalties are spread across 23 official sources, six of them outdated copies still online. And general chatbots guess: in my pilot, a plain language model was fully accurate on only 8 of 24 questions."

## Part 2 (0:30–1:00): Objectives and scope
**Show:** Slide 2

> "The objectives are: to study existing work; to build a knowledge base and a labelled test set; to build and compare four systems, from a simple FAQ bot and a plain language model to a document-based system with citations, and the same system with a confidence check; and to test the app with students.
> The scope is fees, deadlines, mitigating circumstances, assessment and regulations, from public documents in English. It does not involve personal cases, personal data or live deployment."

## Part 3 (1:00–1:45): System diagram and tool choices
**Show:** Slide 3. Point at each box as you say it.

> "Here's the system. Offline, the official PDFs are split into passages, each tagged with its document and page. For each question, hybrid search, keyword plus meaning-based, picks the five best passages. Gemini answers only from those, with a citation number on each sentence, or says the answer isn't there. In the final system, a confidence check sits after the search and sends weak cases to Student Services.
> Tools were chosen for cost, laptop use and repeatable tests. Gemini Flash costs a third of a US cent per question; a local model was too slow. Hybrid search, because each method found passages the other missed. And plain Python, not LangChain, so every prompt stays visible."

## Part 4 (1:45–2:45): Preparation and feasibility
**Show:** AskWatt clip, then Slide 4

Record the clip first, with cached questions only (they cost nothing): the late-penalty example with S3, then "What time does the library close on Saturdays?", then the staff view, then S2 on the late-penalty question.

> "So far I've audited 27 sources, built three of the four systems, run a 32-question pilot, and built this app. The usability study already has ethics approval.
> Each answer comes only from the documents, and each blue number links to the exact PDF page. When the documents don't cover a question, it doesn't guess: it passes it to Student Services with a ticket number, and staff see it in their own view. The plain model, on the same question, says 3% per day. The document says 30%."

**Switch to Slide 4.**

> "In the pilot, the document-based system was fully accurate on all 24 answerable questions and declined all 8 it couldn't answer. An AI judge agreed with my labels on 90 of 96. The pilot cost 37 US cents; the full plan, about 6 dollars, well within budget. These questions follow the documents closely, so the final test set is tougher."

## Part 5 (2:45–3:35): Plan and risks
**Show:** Canva Gantt (Semester 2), then the heat map

> "Next semester is one chain: test set, search tests, confidence check, one final test run, then analysis. The 140 test questions come first, in Weeks 1 to 3. The usability study needs the confidence check in the app, so it runs in Weeks 6 to 8, and Weeks 9 and 10 are a buffer."

**Switch to the heat map.**

> "The two biggest risks score 12 out of 25. If writing the questions takes longer, I start straight after the exams, and the fallback is 150 questions. For workload from other courses: weekly sprints and the buffer, and the fallback is dropping one optional feature. All ten risks have a fallback in the report."

## Part 6 (3:35–4:30): Success targets and PLES
**Show:** Slide 5, left side, then right side

> "Success is measurable. The document-based system should be fully accurate on at least 80% of answerable questions, 20 points ahead of the plain model, with a paired test. At least 85% of citations should support the answer. The confidence check should halve false answers while sending at most a fifth of answerable questions to staff, because a wrong fee answer costs a student more than a short wait. And answers should take under 10 seconds, with a usability score of at least 68."

**Switch to the right side.**

> "No personal data is collected, in line with the PDPA and UK GDPR; documents are cited by page, not copied; the study has ethics approval and consent; and I follow the BCS Code and declare my AI use. The aim is to support staff, not replace them."

## Part 7 (4:30–4:40): Close
**Show:** Slide 1 again

> "So the documents, search, answers, app and budget are in place. Semester 2 is about the tougher test set, the confidence check and a fair comparison. Thank you for watching."

---

## Words to practise (prominent R sounds with no easy swap)
Heriot-Watt, Faizal (fine), university, Student Services, PDFs, citation, ringgit, PDPA, GDPR, ceiling (fine), "three", "risks", "first", "after", "chain" (fine).

Swaps already used: "fully accurate" for correct, "made up" for hallucinated, "app" for prototype, "search" for retrieval, "tougher" for harder, "targets" for criteria, "false answers" for wrong answers, "study" for research.

## Recording checklist
1. Run AskWatt with cached questions and record the clip on its own first (Clipchamp screen recording), with the browser zoomed to 125% so the text is readable.
2. Present the Canva slides full screen and record each part separately, with the narration.
3. In Clipchamp: put the parts in order, drop the clip into Part 4, trim pauses, and normalise the audio.
4. Check that it's under 5:00 (aim for 4:40), the text is readable at 1080p, and no key or email is visible.
5. Export as MP4 (1080p, H.264), under 100 MB.
