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
