# Week 4 reading list (8 Oct 2026)

**How these were checked.** Titles, authors, venues and abstracts for 1-4 and 6-8 were checked on arXiv, ACL Anthology, NeurIPS or the publisher page. Entries 5, 9 and 10 (and the optional ones) have metadata checked through another paper's reference list, so open them and read the abstract before citing. Bibliography entries are in `references_week4.bib`.

## The list (suggested reading order)

| # | Paper | Why it matters | Use it in |
|---|---|---|---|
| 1 | Trienes et al. 2025, *Marcel: A Lightweight and Open-Source Conversational Agent for University Student Support* (arXiv:2507.13937) | **Closest related work.** University RAG chatbot, abstains when the knowledge base lacks the answer, evaluated on answerable and unanswerable questions | Background, gap, evaluation design |
| 2 | Lewis et al. 2020, *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (NeurIPS 33) | Origin of RAG: combines a language model with retrieved passages | Background, justify S3 |
| 3 | Wen et al. 2025, *Know Your Limits: A Survey of Abstention in LLMs* (TACL 13) | Framework for abstention: the query, the model and human values; methods, benchmarks, metrics | Justify S4 and escalation metrics |
| 4 | Peng et al. 2025, *Unanswerability Evaluation for Retrieval Augmented Generation* (ACL 2025) | About evaluating unanswerable questions in RAG. **Read the abstract first**, I only confirmed the title and venue | Test set design, escalation metrics |
| 5 | Gao et al. 2023, *RAG for Large Language Models: A Survey* (arXiv:2312.10997) | Maps RAG designs (naive, advanced, modular) and evaluation | Background, RQ2 design choices |
| 6 | Ji et al. 2023, *Survey of Hallucination in Natural Language Generation* (ACM Computing Surveys 55(12)) | Defines and surveys hallucination, including in generative QA | Define hallucination (H2) |
| 7 | Es et al. 2024, *RAGAs* (EACL 2024 demos) | Reference-free metrics for retrieval and generation quality | Metrics, optional cross-check |
| 8 | Zheng et al. 2023, *Judging LLM-as-a-Judge* (NeurIPS 36 Datasets and Benchmarks) | Shows the strengths and biases of LLM judges and reports agreement with humans | Justify calibrating the judge against humans |
| 9 | Cormack et al. 2009, *Reciprocal Rank Fusion* (SIGIR 2009) | The method for combining dense and keyword rankings (R3 hybrid) | Methodology |
| 10 | Nguyen et al. 2021, *NEU-chatbot* (Computers and Education: AI 2) | Earlier intent-based admissions chatbot, as described in Marcel's related work | Background for the S1 baseline |

Optional: Odede and Frommholz 2024 (*JayBot*, CHIIR), a user study of live chat vs a RAG chatbot as described by Marcel, useful for the usability study design. Also Reimers and Gurevych 2019 (Sentence-BERT) and Robertson and Zaragoza 2009 (BM25) for the tools you plan to use.

Found but not verified (authors unconfirmed): a 2024 Ulster University paper on a RAG-based university chatbot (Conversations 2024 workshop), and an eLearning 2024 proceedings paper on a RAG student-support chatbot.

## What the related work means for your project
- **The gap is narrower than "nobody has built this".** University RAG chatbots with abstention already exist. Frame your contribution as a **controlled comparison of four systems** and a **measurable escalation mechanism** (confidence signals, threshold, risk-coverage curve) on an HWUM test set.
- **Gap evidence to cite:** Marcel leaves the abstain decision to the generation prompt and says other approaches deserve investigation. Marcel also evaluates only the system components, not students using it over time.
- Marcel's test set is small (95 questions, 19 unanswerable). Yours is larger, but your unanswerable group is also small, so report confidence intervals.

## Suggested reading plan (about 5 hours)
1. Marcel: whole paper (1 hr).
2. Lewis: abstract, introduction, method overview (30 min).
3. Wen: abstract, framework section, metrics section (45 min).
4. Peng: abstract and introduction (20 min).
5. Gao, Ji, Es, Zheng: abstract, conclusion and the sections you need (about 20 min each).
6. Cormack and Nguyen: abstract only for now.

## Note template (one per paper, in Notion)
- **Citation key:**
- **Problem:**
- **Method:**
- **Key result:**
- **Relevance to my project:**
- **Limitation or gap:**
- **Where I will cite it (D1 section):**

## Added 5 Nov 2026 (Introduction)

- Okonkwo and Ade-Ibijola 2021, *Chatbots Applications in Education: A Systematic Review*, Computers and Education: AI 2, 100033, doi:10.1016/j.caeai.2021.100033. Checked on the University of Johannesburg repository and DOAJ (53 studies reviewed; benefits and challenges of educational chatbots).
- Labadze, Grigolia and Machaidze 2023, *Role of AI Chatbots in Education: Systematic Literature Review*, International Journal of Educational Technology in Higher Education 20, doi:10.1186/s41239-023-00426-1. Title, authors, year and DOI checked (DOAJ record and the journal PDF link). **Article number 56 is from memory: check it on the journal page before submission.** A correction notice was published in 2024 (doi:10.1186/s41239-024-00461-6).

## Added 5 Nov 2026 (Background rewrite)

How these were checked: authors, title, venue, pages and DOI were read from the ACL Anthology, arXiv, PMLR, mlanthology, NeurIPS, a university repository (Oxford ORA, Lingnan, Zayed) or another library record, as noted. Key findings were read from the abstract or the paper page. **Read at least the abstract of each before the final submission**, and open the full paper for the ones used in the comparison table.

**Student support chatbots (Table 1)**
- Trienes et al. 2025, *Marcel*. Now cited as EMNLP 2025 System Demonstrations, pp. 181-195, doi:10.18653/v1/2025.emnlp-demos.13 (ACL Anthology). 95 test questions (19 unanswerable), 9-week deployment with 92 users, abstention left to the prompt.
- Pathiyan Cherumanal et al. 2024, *Walert*, CHIIR '24 (arXiv:2401.07216). Authors and venue checked; **pages and DOI not found, add them from the ACM Digital Library**.
- Neupane et al. 2024, *From Questions to Insightful Answers: Building an Informed Chatbot for University Resources* (BarkPlug), arXiv:2405.08120. RAGAS 0.96, SUS 67.75 from 50 students (checked in the paper).
- Chen, Zou, Xie, Lou and Pang 2024, *Facilitating University Admission Using a Chatbot Based on LLMs with RAG*, Educational Technology & Society 27(4), 454-470, doi:10.30191/ETS.202410_27(4).TP02 (Lingnan repository).
- Nguyen and Quan 2025, *URAG*, arXiv:2501.16276 (arXiv HTML).
- Khasanova Zafar kizi and Suh 2025, *Design and Performance Evaluation of LLM-Based RAG Pipelines for Chatbot Services in International Student Admissions*, Electronics 14(15), 3095, doi:10.3390/electronics14153095 (MDPI page). Prompt tells the model to infer from loosely related context; unanswerable questions not evaluated.
- Kuhail et al. 2023, *Interacting with Educational Chatbots: A Systematic Review*, Education and Information Technologies 28(1), 973-1018, doi:10.1007/s10639-022-11177-3 (36 papers reviewed).

**Hallucination and citation**
- Huang et al. 2025, *A Survey on Hallucination in LLMs*, ACM TOIS, doi:10.1145/3703155 (arXiv record). **Volume, issue and article number not confirmed: add them from the ACM page.**
- Chen, Lin, Han and Sun 2024, *Benchmarking LLMs in RAG* (RGB), AAAI 38(16), 17754-17762, doi:10.1609/aaai.v38i16.29728.
- Liu, Zhang and Liang 2023, *Evaluating Verifiability in Generative Search Engines*, Findings of EMNLP 2023, 7001-7025.
- Gao, Yen, Yu and Chen 2023, *Enabling LLMs to Generate Text with Citations* (ALCE), EMNLP 2023, 6465-6488.

**Abstention, confidence and escalation**
- Rajpurkar, Jia and Liang 2018, *Know What You Don't Know* (SQuAD 2.0), ACL 2018, 784-789.
- Kamath, Jia and Liang 2020, *Selective Question Answering under Domain Shift*, ACL 2020, 5684-5696 (56% vs 48% answered at 80% accuracy).
- Kadavath et al. 2022, *Language Models (Mostly) Know What They Know*, arXiv:2207.05221.
- Feng et al. 2024, *Don't Hallucinate, Abstain*, ACL 2024, 14664-14690.
- Farquhar, Kossen, Kuhn and Gal 2024, *Detecting Hallucinations in LLMs Using Semantic Entropy*, Nature 630(8017), 625-630 (Oxford ORA).
- Asai et al. 2024, *Self-RAG*, ICLR 2024 (mlanthology).
- Yan, Gu, Zhu and Ling 2024, *Corrective RAG* (CRAG), arXiv:2401.15884.
- Mozannar and Sontag 2020, *Consistent Estimators for Learning to Defer to an Expert*, ICML 2020, PMLR 119, 7076-7087.

**Retrieval and evaluation**
- Fan et al. 2024, *A Survey on RAG Meeting LLMs*, KDD 2024, 6491-6501.
- Liu et al. 2024, *Lost in the Middle*, TACL 12, 157-173.
- Thakur et al. 2021, *BEIR*, NeurIPS 2021 Datasets and Benchmarks track.
- Xiao et al. 2024, *C-Pack* (BGE embeddings), SIGIR '24, doi:10.1145/3626772.3657878. Pages not confirmed.
- Saad-Falcon et al. 2024, *ARES*, NAACL 2024, 338-354.
- Cohen 1960, *A Coefficient of Agreement for Nominal Scales*, Educational and Psychological Measurement 20(1), 37-46.

**Technology review**
- Grattafiori et al. 2024, *The Llama 3 Herd of Models*, arXiv:2407.21783.
- Abid et al. 2019, *Gradio*, arXiv:1906.02569.
- Google, Gemini API pricing page (accessed 1 Nov 2026, as recorded in `configs/pilot.yaml`) and the Streamlit chat app tutorial (accessed 5 Nov 2026).

## Added 7 Nov 2026 (Methodology, Feasibility, appendices)

- Schwaber and Sutherland 2020, *The Scrum Guide* (scrumguides.org PDF). Cited for the Scrum-inspired development approach.
- Brooke 1996, *SUS: A "Quick and Dirty" Usability Scale*, in Jordan et al. (eds), *Usability Evaluation in Industry*,
  Taylor & Francis, 189-194. Title and year checked (UCL constructDB record); **editors, publisher and pages are from
  memory, check them in a library record**.
- Dror, Baumer, Shlomov and Reichart 2018, *The Hitchhiker's Guide to Testing Statistical Significance in NLP*, ACL 2018,
  1383-1392, doi:10.18653/v1/P18-1128 (ACL Anthology).
- BCS Code of Conduct, version 8, approved 8 June 2022 (bcs.org PDF). Four sections: public interest, professional
  competence and integrity, duty to relevant authority, duty to the profession.
- Personal Data Protection Act 2010 (Act 709), Malaysia, amended by the Personal Data Protection (Amendment) Act 2024
  (in force in phases from 1 Jan to 1 Jun 2025; checked in a Data Protection Report summary).
- Copyright Act 1987 (Act 332), Malaysia (WIPO Lex record).
