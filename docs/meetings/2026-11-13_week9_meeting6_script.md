# Meeting 6 script: Fri 13 Nov 2026, 4pm (about 30 min) - full D1 draft, prototype, diagrams, D2

Have open before the call:
- D1 PDF (v8), zoomed to page width
- AskWatt running: `.venv\Scripts\python.exe -m streamlit run src/app.py`
- This script and something to write notes on

Page numbers below are from the v8 PDF. If the Overleaf build differs, go by the table and figure numbers instead.

## 0-2 min: Opening
> "Thank you for making time today, Dr. I'd like to go through the full D1 draft with you, show the working prototype and the diagrams, and check a few things before I start on D2, the video."

## 2-5 min: Changes since meeting 5
Show page 1, then scroll slowly.
> "I followed your points from last time. The Introduction now opens with a problem statement about HWUM. The objectives start with 'To', with one bullet per system, and there's a new Scope and Limitations section that leaves out sensitive topics like financial hardship and mental health."

> "In Background, there's a comparison table of five existing student chatbots, and each one shows the gap for this project. In Methodology, I added the agile approach, the development plan, and a Design section with a use case diagram and the interface I've built."

> "There's also some new work: the ethics application was approved this month, and I extended the pilot from 26 to 32 questions, adding paraphrased and near-miss questions."

## 5-14 min: Walk through the draft

### Section 2: Background (pages 2 to 6)
**Table 1, page 4: existing chatbots.**
> "Five systems: Walert, BarkPlug, Chen et al., URAG and Marcel. Most of them focus on admissions, and few test questions they can't answer. That's the gap this project fills."

**Table 2, page 5: technology choices.**
> "Each part of the system is chosen against four tests: low cost, it can be run on a laptop, every setting is visible so tests can be repeated, and evidence that it works. The table shows what I chose, the evidence for it, and why I didn't pick the alternatives. For example, for the LLM I chose Gemini 3.6 Flash, because a local model would be too slow on a laptop."

**Page 6: the gaps and the four questions.**
> "That leads to three gaps and four questions. The fourth, on usability, is the study that ethics approved."

Ask:
1. "Is Table 2 clear enough on why each tool was chosen, or would you like more depth?"
2. "Are the three gaps and four questions convincing?"

### Section 3: Methodology (pages 6 to 11)
**Table 3, page 6: the plan.**
> "Five stages. Semester 2 starts with writing the 200 test questions, then the experiments, then the final test run once, then analysis and writing up."

**Table 4, page 7: MoSCoW table.**
> "Each item is linked to an objective. The must-haves are the core needed to answer the first three questions."

**Figure 1, page 8: architecture.**
> "The top half is offline: documents split into passages with the document and page kept. The bottom half is what happens for each question: search, the answer with citations, and the confidence check in S4, which hands the question to staff if the evidence is weak."

**Figure 2, page 9: use case diagram.**
> "Three users: the student, the Student Services staff, and the maintainer, which is me."

**Table 5, page 10: evaluation design.** (new since the last version)
> "This is new. For each question it shows the test, what's measured and the statistics. For example, for escalation, I measure how well each signal separates the questions it can answer from the ones it can't, and how many wrong answers S4 avoids against S3."

**Success targets, page 11.**
> "These are the targets. One thing to point out: S3 made no wrong answers in the pilot, so if it also makes very few in the final test, I'll judge S4 on a curve of accuracy against coverage instead of a simple ratio."

Ask:
3. "Does the evaluation design in Table 5 look sound to you?"
4. "Are the success targets sensible, especially SC3, the one for escalation?"

### Section 4: Feasibility (pages 11 to 14)
**Tables 6 and 7, Figure 4, pages 12 to 13.**
> "On 32 pilot questions, hybrid search did best. S3 got all 24 answerable questions fully correct and declined all 8 it couldn't answer. S2 was fully correct on only 8, and answered 6 it should have declined, which shows the made-up answer problem."

> "I'm being honest that S3's full score is a ceiling effect, since the pilot questions follow the documents' wording closely. The final test set adds harder questions where S3 should fail, and that's where S4 matters."

> "Figure 4 shows the signals for S4. The top dense search score works fairly well. The model signal, one extra Gemini call, separated the two groups fully, but only on 8 negative questions, so that's weak evidence for now."

> "The whole pilot cost 37 cents in US dollars, and the full plan comes to about 6 US dollars, well within budget."

Ask:
5. "Is this enough feasibility evidence, or should I add anything?"

### Appendices (pages 19 onwards)
Scroll: Gantt charts (pages 19 to 20), heat map and table of risks (pages 20 to 21), the PLES section, the Generative AI summary.
> "Two Gantt charts, one for each semester, with a buffer in Weeks 9 and 10. Each of the ten risks has a likelihood, an impact, a way to avoid it and a backup plan. The GenAI summary sets out how I used AI tools."

Ask:
6. "Are the Gantt charts and the risk table detailed enough?"

## 14-20 min: Live demo of AskWatt
Share the browser.
1. Click one of the example questions under "Try asking".
   > "It answers only from the official documents. The yellow numbers are citations, and each source shows the page, with a link that opens that exact page of the PDF."
2. Type a question the documents don't cover, e.g. "What is the Wi-Fi password in the library?"
   > "When the documents don't have the answer, it doesn't guess. It passes the question to Student Services and gives the student a ticket number."
3. In the sidebar, switch the view to staff.
   > "This is the staff view. The question is waiting here, and staff can mark it as done."
4. Optional: switch the system to S2 and ask the first question again.
   > "This is S2, the plain model, on the same question, with no sources."

Ask:
7. "Does the interface look right for a prototype, or is there anything you'd change before the video?"

## 20-25 min: Two plans and the survey
> "I added two plans to the draft, and I'd like to check them with you."

8. > "First, could we ask Student Services, through you, which topics students ask about most? I'd use that to decide how many test questions cover each topic."
9. > "Second, to check the questions aren't too close to the documents' wording, I'd like a second person, maybe a coursemate, to write about 20 of the questions in their own words without seeing the documents. Is that fine, and does it need any extra ethics cover?"
10. > "Last time you mentioned a survey. I've planned the usability study for Semester 2, Weeks 6 to 8, once S4 is built, and that's what ethics approved. Is that the timing you had in mind, or did you want a survey this semester?"

## 25-28 min: D2 video
> "Next I'm starting on D2, the five-minute video. I plan to show what I've prepared, why I chose each tool, the pilot numbers, a demo of the prototype, the plan and the main risks, and the ethics side."

11. > "Is there anything you'd like to see in the video, or anything to leave out?"
12. > "Would you like to see a script or a draft before I submit it?"

## 28-30 min: Wrap up
> "So to confirm: I'll apply your comments to D1, start on the D2 video, and I'm aiming to submit both on the 24th, two days before the deadline. Thank you, Dr."

## Notes (write during the meeting)
- Draft overall:
- Table 2 (technology choices):
- Gaps and questions:
- Table 5 (evaluation design) and success targets:
- Feasibility evidence:
- Gantt, risks, appendices:
- AskWatt prototype:
- Student Services topics:
- Second-person question check / ethics:
- Survey timing:
- D2 video:
- Next meeting:
- Anything else:

Words to practise (R-heavy, no easy swap): Heriot-Watt, draft, Student Services, prototype, Gantt chart, BarkPlug, URAG, Marcel, near-miss, ratio, curve, interface.
Swaps already used: "search" for retrieval, "targets" for success criteria, "must-haves" for requirements, "made-up answers" for hallucination, "numbers" for results.
