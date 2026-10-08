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
