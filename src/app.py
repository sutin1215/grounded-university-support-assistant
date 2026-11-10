"""Web interface for the support assistant, "AskWatt" (F6, working prototype for the D1 Design section).

Two views:
  Student  ask a question; get an answer whose citations link to the exact page of the official
           document, or a referral to Student Services with a reference number.
  Staff    see the referred questions and mark them as resolved.
Any of S1-S3 can be chosen in the sidebar for demonstrations; S3 is the default. In Semester 2,
S4's confidence check will replace S3's built-in decline. Styling lives in src/static/style.css.

Usage:  streamlit run src/app.py
"""
import csv
import html
import json
import re
import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # so "src" imports work under streamlit

from src.config import ROOT, load_config  # noqa: E402
from src.escalations import EscalationLog  # noqa: E402
from src.systems import build_systems  # noqa: E402

SYSTEMS = {"S3": "S3: documents with citations", "S1": "S1: FAQ matching", "S2": "S2: language model only"}
EXAMPLES = ["What is the penalty if I submit my coursework late?",
            "How many times can I resit a course I failed?",
            "Can I get a refund if I withdraw from my programme in Week 3?"]
LOG = EscalationLog(ROOT / "data" / "escalations.jsonl")
STYLE = Path(__file__).with_name("static") / "style.css"


@st.cache_resource(show_spinner="Loading the documents...")
def get_system(name):
    """Build one system once per server (loading the embedding model takes a few seconds)."""
    return build_systems(load_config(), (name,))[name]


@st.cache_data
def load_sources():
    """Map each PDF file name to its title, version and official URL from data/doc_sources.csv."""
    by_file = {}
    with open(ROOT / "data" / "doc_sources.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = row["url"].rstrip("/").split("/")[-1]
            if name not in by_file or row["use_in_kb"] == "yes":  # prefer the current version
                by_file[name] = row
    return by_file


@st.cache_data
def kb_documents():
    """File names of the documents that were ingested into the knowledge base."""
    with open(load_config()["chunks_path"], encoding="utf-8") as f:
        return sorted({json.loads(line)["doc"] for line in f if line.strip()})


def answer_html(text):
    """Turn the model's plain-text answer into safe HTML: paragraphs, bullet lists, bold and [n] markers."""
    text = html.escape(text.strip())
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    parts = []
    for block in re.split(r"\n\s*\n", text):
        lines = [ln for ln in block.split("\n") if ln.strip()]
        if lines and all(re.match(r"\s*[-*•]\s+", ln) for ln in lines):
            items = "".join("<li>" + re.sub(r"^\s*[-*•]\s+", "", ln) + "</li>" for ln in lines)
            parts.append(f"<ul>{items}</ul>")
        elif lines:
            parts.append("<p>" + "<br>".join(lines) + "</p>")
    return re.sub(r"\[(\d+)\]", r'<span class="cite">\1</span>', "".join(parts))


def group_citations(citations):
    """Merge citations that point to the same document page, e.g. [1] and [3] both on page 1."""
    groups = {}
    for c in citations:
        groups.setdefault((c["doc"], c["page"]), []).append(c["n"])
    return [{"doc": doc, "page": page, "ns": ns} for (doc, page), ns in groups.items()]


def source_html(g, sources):
    """One cited page: a page tab, the document title and version, and a link to that page."""
    marks = "".join(f'<span class="cite">{n}</span>' for n in g["ns"])
    src = sources.get(g["doc"])
    title = html.escape(src["title"] if src else g["doc"])
    version = "" if not src or "(" in src["title"] else f' <span class="version">({html.escape(src["version_or_date"])})</span>'
    link = (f'<br><a href="{html.escape(src["url"])}#page={g["page"]}" target="_blank">Open page {g["page"]}</a>'
            if src else "")
    return (f'<div class="source"><div class="tab">{g["page"]}<small>page</small></div>'
            f'<div class="doc">{marks} {title}{version}{link}</div></div>')


def show_answer(out, sources):
    """Render one answer sheet, or the referral notice when the system declined."""
    if out.get("escalation"):
        e = out["escalation"]
        st.markdown(
            f'<div class="sheet refer"><h3>Passed to {html.escape(e["office"])}</h3>'
            "<p>The official documents don't answer this question, so instead of guessing, it has been "
            "passed to a member of staff who will follow it up. Only the question was saved, nothing about you.</p>"
            f'<div class="ticket">Reference <span>{e["id"]}</span></div></div>', unsafe_allow_html=True)
        return
    body = f'<div class="sheet"><div class="answer">{answer_html(out["answer"])}</div>'
    if out["citations"]:
        rows = "".join(source_html(g, sources) for g in group_citations(out["citations"]))
        body += f'<div class="sources"><h4>Where this comes from</h4>{rows}</div>'
    elif out["system"] == "S2":
        body += '<p class="meta">No sources: this system answers from the language model alone.</p>'
    if out.get("latency_s"):
        body += f'<p class="meta">Answered by {out["system"]} in {out["latency_s"]:.1f} seconds</p>'
    st.markdown(body + "</div>", unsafe_allow_html=True)


def ask(question, system_name):
    out = get_system(system_name).answer(question)
    if out["abstained"]:
        out["escalation"] = LOG.add(question, system_name)
    return out


def masthead(tagline):
    st.markdown(f'<div class="masthead"><h1 class="wordmark">AskWatt</h1><p class="tagline">{tagline}</p></div>',
                unsafe_allow_html=True)


def student_view(system_name):
    masthead("Ask about fees, deadlines and university rules. Every answer shows the page of the "
             "official Heriot-Watt or HWUM document it comes from.")
    st.markdown('<p class="notice">A student project prototype. Please don\'t type personal details such as '
                "your student ID, health or money matters: questions are sent to Google's Gemini service "
                "to write the answer.</p>", unsafe_allow_html=True)

    history = st.session_state.setdefault("history", [])
    sources = load_sources()
    if not history and "pending" not in st.session_state:
        st.markdown('<p class="try">Try asking</p>', unsafe_allow_html=True)
        for q in EXAMPLES:
            st.button(q, on_click=st.session_state.__setitem__, args=("pending", q))

    for item in history:
        st.markdown(f'<p class="asked">{html.escape(item["question"])}</p>', unsafe_allow_html=True)
        show_answer(item["out"], sources)

    question = st.chat_input("Ask a question about fees, deadlines or assessment rules")
    question = question or st.session_state.pop("pending", None)
    if question:
        st.markdown(f'<p class="asked">{html.escape(question)}</p>', unsafe_allow_html=True)
        with st.spinner("Searching the official documents..."):
            out = ask(question, system_name)
        show_answer(out, sources)
        history.append({"question": question, "out": out})


def staff_view():
    masthead("Questions the assistant passed to Student Services. Reply to the student through the "
             "usual channels, then mark the question as resolved. In this prototype, referral is simulated.")
    entries = LOG.all()
    waiting = sum(e["status"] == "open" for e in entries)
    noun = "question" if waiting == 1 else "questions"
    st.markdown(f'<p class="waiting"><b>{waiting}</b> {noun} waiting for a reply</p>', unsafe_allow_html=True)
    if not entries:
        st.write("Nothing has been passed to staff yet.")
        return
    rows = "".join(
        f'<tr><td>{e["id"]}</td><td>{e["time"][:16].replace("T", " ")}</td>'
        f'<td class="q">{html.escape(e["question"])}</td>'
        f'<td><span class="pill {e["status"]}">{e["status"]}</span></td></tr>' for e in entries)
    st.markdown('<table class="queue"><tr><th>Reference</th><th>Received (UTC)</th><th>Question</th>'
                f'<th>Status</th></tr>{rows}</table>', unsafe_allow_html=True)
    open_ids = [e["id"] for e in entries if e["status"] == "open"]
    if open_ids:
        st.write("")
        with st.form("resolve"):
            esc_id = st.selectbox("Question to resolve", open_ids)
            note = st.text_input("Note (optional)", placeholder="For example: replied by email, add to the FAQ")
            if st.form_submit_button("Mark as resolved"):
                LOG.resolve(esc_id, note)
                st.rerun()


def main():
    st.set_page_config(page_title="AskWatt: student support assistant", page_icon="📄", layout="centered")
    st.markdown(f"<style>{STYLE.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    with st.sidebar:
        view = st.radio("View", ["Student", "Staff"], horizontal=True)
        system_name = st.selectbox("Answering system (for demos)", list(SYSTEMS), format_func=SYSTEMS.get)
        sources = load_sources()
        docs = "".join(f"<li>{html.escape(sources[d]['title'] if d in sources else d)}</li>"
                       for d in kb_documents())
        st.markdown(f'<p><b>Documents it can read</b></p><ul class="kb">{docs}</ul>', unsafe_allow_html=True)
    if view == "Student":
        student_view(system_name)
    else:
        staff_view()


main()
