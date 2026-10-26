# Meeting 4 script: Tue 27 Oct 2026, 11:30 (about 30 min)

Have open before you walk in (VS Code, repo folder):
1. Terminal, already run once: `python -m src.demo`
2. `eval/results/pilot_summary.md`
3. `data/doc_sources.csv`
4. Notion task board, and Overleaf (D1)
5. Something to write notes on

## 0-2 min: Opening
> "Thank you for signing the ethics form, Dr. Since our last face-to-face meeting was in Week 5, I'd like to give you a quick update on what's been done, show you the first pilot, then go through my plan up to D1 and ask a few questions. Is that okay?"

## 2-6 min: Update since Week 5
> "First, the ethics application. It's signed and submitted as of yesterday. No work with participants will start until it's approved."

> "Second, I'll be honest about Week 5: I fell behind on the pilot, because another course assignment took up most of my time that week. Week 6 was study week, so I used it to finish the ethics form. I've now caught up on the pilot this week."

> "Third, I've organised all my project records. The GitHub repo now has the journal entries, the meeting notes, a weekly update for each week, the ethics documents and the D1 LaTeX files. Notion has every task with its status."

Show: Notion board (Weeks 3-7 done or in progress), then GitHub `docs/` folder for 5 seconds.

## 6-16 min: Pilot demo
> "Next, the pilot. I loaded five official documents: the coursework submission briefing paper, the mitigating circumstances procedure, the assessment and progression guide, the international fee structure and the fees and payment guide. The system splits them into passages, and every passage keeps its document name and page, so each answer can cite its source."

Show `data/doc_sources.csv`:
> "This is my full source list: 27 official sources, with version, scope and notes. I kept some older versions on purpose to test how the system handles outdated information."

Run `python -m src.demo` and talk through each question:
1. Self-certify:
> "For this one both work. The FAQ baseline gives the right answer, and the search finds the exact page of the MC procedure."
2. Extension:
> "Here both miss. The question says 'extension' and the policy says 'extensions', so plain keyword matching fails. That's why my next step is word-stem matching plus embedding-based search, which matches meaning, not just words."
3. Late fee charge:
> "This is the key one. The FAQ baseline gives a confident but wrong answer: it was asked about a late payment charge and answered with the due date. That's exactly the problem my escalation component is meant to catch."
4. Library hours:
> "This isn't in the documents at all, but the search still returns passages. So the system can't just answer from whatever it finds. It needs a confidence check to decide when to hand over to staff. That's S4."

Open `eval/results/pilot_summary.md`:
> "These are the first numbers, on 26 test questions, 20 answerable and 6 not answerable. BM25 keyword search finds the correct page in the top 5 for 90% of questions and puts it first 60% of the time. TF-IDF gets 85%. The FAQ baseline answers only 40% correctly. It's a small set, so I'm treating these as early signals, not final outcomes."

Optional: offer to type one of her own questions: `python -m src.demo "her question"`.

## 16-21 min: Plan to D1
> "My plan from now until D1:
> - This week: add embedding search, choose an LLM API so I can compare a plain LLM against the document-grounded version, and draft the Background Research and Methodology.
> - Next week: the Feasibility section with these pilot numbers and tool comparison tables, plus the Gantt chart, risk table and professional and ethical issues. I'd like to send you the full D1 draft by Friday 6 November.
> - Week 9: apply your feedback and plan the D2 video.
> - Week 10: final checks and record D2.
> - Then submit by 24 November, before the 26 November deadline."

## 21-28 min: Questions (ask the first four even if time is short)
1. LLM API:
> "For comparing the plain LLM and the grounded version, I need a hosted LLM API. Only public university documents and test questions are sent, no personal data. Is any provider fine, or does the university have one you'd suggest? Is there any budget, or should I keep it to free or low-cost options?"
2. D1 draft timing:
> "If I send the full D1 draft on Friday 6 November, will that give you enough time to comment before the 26th? Would you like any section earlier, like the Background Research?"
3. Scope check:
> "Based on the pilot, I think the four-system comparison and a test set of about 200 questions is still realistic. Do you agree, or should I narrow the scope?"
4. D1 example:
> "You mentioned you'd look for more sample D1 reports. That would help a lot with the level of detail you expect, especially for the Feasibility section."
5. Feedback on the current D1:
> "The Introduction is in Overleaf. Could you look at it, especially the objectives and the four research questions, and tell me if anything should change?"
6. Journal:
> "For the project journal, should I submit an entry each week on Canvas, or just keep them up to date and submit them together?"
7. Ethics follow-up:
> "If the ethics committee asks for changes, should I just update and resubmit, or check with you first? And is a typed name okay as the signature on the consent form?"
8. Second marker:
> "Do you know yet who my second marker is, or whether there's anything specific I should prepare for them?"

## 28-30 min: Wrap up
> "So, to confirm: this week I'll add embedding search, set up the LLM comparison and draft the Background Research and Methodology. I'll share progress next Tuesday. Is there anything else you'd like me to focus on?"
> "Thank you, Dr. See you next week."

## Notes during the meeting (write down)
- LLM provider decision:
- D1 draft deadline agreed:
- Scope decision:
- Journal submission:
- Feedback on the Introduction:
- Anything else she asks for:

After the meeting: send these notes to Claude, who updates the meeting notes, journal 4 (Week 7), Notion and the D1 plan.
