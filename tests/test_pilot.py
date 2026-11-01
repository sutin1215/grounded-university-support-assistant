"""Unit tests for chunking, retrieval and the FAQ baseline (no PDFs needed)."""
from src.faq_baseline import ESCALATE, FAQBaseline
from src.ingest import chunk_words, clean
from src.retrieve import BM25Retriever, TfidfRetriever, tokenize

CHUNKS = [
    {"chunk_id": "a", "doc": "policy.pdf", "page": 1,
     "text": "A standard 30% deduction applies to coursework submitted late up to five working days."},
    {"chunk_id": "b", "doc": "fees.pdf", "page": 2,
     "text": "Semester fees are payable in advance before the start of the semester."},
    {"chunk_id": "c", "doc": "haps.pdf", "page": 3,
     "text": "One re-assessment opportunity is permitted for each course."},
]


def test_clean_joins_hyphenated_words():
    assert clean("assess-\nment  policy") == "assessment policy"


def test_chunk_overlap_covers_all_words():
    words = [str(i) for i in range(50)]
    chunks = list(chunk_words(words, size=20, overlap=5))
    assert chunks[0].split()[0] == "0"
    assert chunks[-1].split()[-1] == "49"
    assert chunks[1].split()[0] == "15"


def test_tokenize_drops_stopwords():
    assert tokenize("What is the late penalty?") == ["late", "penalty"]


def test_retrievers_find_the_right_chunk():
    for cls in (BM25Retriever, TfidfRetriever):
        top = cls(CHUNKS).search("penalty for late coursework", k=1)[0]
        assert top["doc"] == "policy.pdf", cls.__name__


def test_faq_baseline_answers_and_escalates():
    faq = [{"faq_id": "F1", "question": "When are semester fees due?", "answer": "In advance.", "source": "fees.pdf"},
           {"faq_id": "F2", "question": "How many resits are allowed?", "answer": "One.", "source": "haps.pdf"}]
    bot = FAQBaseline(faq, min_similarity=0.3)
    assert bot.answer("when are my semester fees due")["faq_id"] == "F1"
    assert bot.answer("Where is the campus gym?")["faq_id"] == ESCALATE


def test_stemmed_tokenizer_matches_plural():
    from src.retrieve import tokenize_stem
    assert tokenize_stem("extensions") == tokenize_stem("extension")


def test_stemmed_bm25_finds_plural_wording():
    from src.retrieve import StemmedBM25Retriever
    chunks = CHUNKS + [{"chunk_id": "d", "doc": "ltbp.pdf", "page": 1, "text": "No individual extensions are permitted."}]
    top = StemmedBM25Retriever(chunks).search("Can I get an extension?", k=1)[0]
    assert top["doc"] == "ltbp.pdf"


def test_hybrid_rrf_rewards_agreement():
    from src.retrieve import HybridRetriever

    class Fixed:
        def __init__(self, scores):
            self._s = scores

        def scores(self, q):
            return self._s

    cfg = {"retrieval": {"rrf_k": 60}}
    # chunk "b" is ranked 1st by one part and 2nd by the other; "a" and "c" are each last once
    h = HybridRetriever(CHUNKS, cfg, parts=[Fixed([1, 3, 2]), Fixed([2, 3, 1])])
    assert h.search("x", k=1)[0]["chunk_id"] == "b"


def test_s3_citation_parsing_and_abstain():
    from src.systems import S3RAG

    class FakeLLM:
        def __init__(self, text):
            self.text = text

        def generate(self, prompt, system=""):
            from src.llm import LLMResult
            return LLMResult(self.text, "fake", 10, 5, 0.1, 0.0, False)

    class FakeRetriever:
        def search(self, q, k):
            return [dict(c, score=1.0) for c in CHUNKS[:2]]

    prompts = {"s3_user": "{passages}\n{question}", "s3_system": "", "abstain_message": "Please contact staff."}
    s3 = S3RAG.__new__(S3RAG)
    s3.llm, s3.prompts, s3.k, s3.retriever = FakeLLM("Late work loses 30% [1]. See [9]."), prompts, 2, FakeRetriever()
    out = s3.answer("late penalty?")
    assert [c["doc"] for c in out["citations"]] == ["policy.pdf"] and out["abstained"] is False
    s3.llm = FakeLLM("NOT_FOUND")
    out = s3.answer("library hours?")
    assert out["abstained"] is True and out["answer"] == "Please contact staff."
