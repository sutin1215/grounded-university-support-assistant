"""Web interface for the support assistant (F6, working prototype for the D1 Design section).

Two views:
  Student  ask a question; get an answer with citations to the official document and page,
           or a message that the question has been passed to Student Services.
  Staff    see the escalated questions and mark them as resolved.
Any of S1-S3 can be chosen in the sidebar, so the systems can be compared side by side in demos.
S3 is the default. S4 will replace S3's built-in decline with a confidence check (Semester 2).

Usage:  streamlit run src/app.py
"""
import csv
import json
import re
import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # so "src" imports work under streamlit

from src.config import ROOT, load_config  # noqa: E402
from src.escalations import EscalationLog  # noqa: E402
from src.systems import build_systems  # noqa: E402

SYSTEMS = {"S3": "S3 RAG with citations (default)", "S1": "S1 FAQ baseline", "S2": "S2 Plain LLM"}
EXAMPLES = ["What is the penalty if I submit my coursework late?",
            "How many times can I resit a course I failed?",
            "Can I get a refund if I withdraw from my programme in Week 3?"]
LOG = EscalationLog(ROOT / "data" / "escalations.jsonl")


@st.cache_resource(show_spinner="Loading the knowledge base...")
def get_system(name):
    """Build one system once per server (loading the embedding model takes a few seconds)."""
    return build_systems(load_config(), (name,))[name]


@st.cache_data
def load_sources():
    """Map each PDF file name to its title and official URL from data/doc_sources.csv."""
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


def group_citations(citations):
    """Merge citations that point to the same document page, e.g. [1] and [3] both on page 1."""
    groups = {}
    for c in citations:
        groups.setdefault((c["doc"], c["page"]), []).append(c["n"])
    return [{"doc": doc, "page": page, "ns": ns} for (doc, page), ns in groups.items()]


def cite_line(g, sources):
    """One cited page as Markdown: numbers, document title, version, page and a link to that page."""
    nums = "".join(f"[{n}]" for n in g["ns"])
    src = sources.get(g["doc"])
    if not src:
        return f"**{nums}** {g['doc']}, page {g['page']}"
    title = src["title"]
    if "(" not in title:  # add the version unless the title already carries it
        title += f" ({src['version_or_date']})"
    return f"**{nums}** {title}, page {g['page']} · [open page {g['page']}]({src['url']}#page={g['page']})"


def show_answer(out, sources):
    """Render one answer: the text, then its sources, or an escalation notice."""
    if out.get("escalation"):
        st.warning(out["answer"])
        e = out["escalation"]
        st.info(f"**Passed to {e['office']}** · reference {e['id']}. "
                "A member of staff will follow this up. Nothing about you was stored, only the question.")
        return
    st.markdown(re.sub(r"\[(\d+)\]", r"<sup>[\1]</sup>", out["answer"]), unsafe_allow_html=True)
    if out["citations"]:
        st.markdown("**Sources**")
        for g in group_citations(out["citations"]):
            st.markdown(cite_line(g, sources))
    elif out["system"] == "S2":
        st.caption("No sources: S2 answers from the model's own knowledge.")
    if out.get("latency_s"):
        st.caption(f"{out['system']} · answered in {out['latency_s']:.1f} s")


def ask(question, system_name):
    out = get_system(system_name).answer(question)
    if out["abstained"]:
        out["escalation"] = LOG.add(question, system_name)
    return out


def student_view(system_name):
    st.title("Student Support Assistant")
    st.caption("Answers come only from official Heriot-Watt and HWUM documents, with the page they come from. "
               "If the documents do not cover your question, it is passed to Student Services.")
    st.info("This is a student project prototype. Please do not type personal details such as your student ID, "
            "health or financial situation. Questions are sent to Google's Gemini API to write the answer.", icon="ℹ️")

    history = st.session_state.setdefault("history", [])
    sources = load_sources()
    if not history:
        st.markdown("**Try asking:**")
        for col, q in zip(st.columns(len(EXAMPLES)), EXAMPLES):
            if col.button(q, use_container_width=True):
                st.session_state["pending"] = q

    for item in history:
        with st.chat_message("user"):
            st.write(item["question"])
        with st.chat_message("assistant"):
            show_answer(item["out"], sources)

    question = st.chat_input("Ask about fees, deadlines, mitigating circumstances or assessment rules")
    question = question or st.session_state.pop("pending", None)
    if question:
        with st.chat_message("user"):
            st.write(question)
        with st.chat_message("assistant"):
            with st.spinner("Searching the official documents..."):
                out = ask(question, system_name)
            show_answer(out, sources)
        history.append({"question": question, "out": out})


def staff_view():
    st.title("Escalated questions")
    st.caption("Questions the assistant could not answer from the documents. Staff reply to the student "
               "through the usual channels; in this prototype escalation is simulated.")
    entries = LOG.all()
    open_n = sum(e["status"] == "open" for e in entries)
    st.metric("Open", open_n, help="Escalations waiting for a member of staff")
    if not entries:
        st.write("No escalated questions yet.")
        return
    st.dataframe([{"Reference": e["id"], "Received (UTC)": e["time"].replace("T", " ")[:16],
                   "Question": e["question"], "System": e["system"], "Status": e["status"]} for e in entries],
                 hide_index=True, use_container_width=True)
    open_ids = [e["id"] for e in entries if e["status"] == "open"]
    if open_ids:
        with st.form("resolve"):
            esc_id = st.selectbox("Mark as resolved", open_ids)
            note = st.text_input("Note (optional)", placeholder="e.g. replied by email; add to the FAQ")
            if st.form_submit_button("Resolve"):
                LOG.resolve(esc_id, note)
                st.rerun()


def main():
    st.set_page_config(page_title="Student Support Assistant", page_icon="🎓", layout="centered")
    with st.sidebar:
        view = st.radio("View", ["Student", "Staff"], horizontal=True)
        system_name = st.selectbox("System", list(SYSTEMS), format_func=SYSTEMS.get)
        st.divider()
        st.markdown("**Documents in the knowledge base**")
        sources = load_sources()
        for doc in kb_documents():
            st.caption(sources[doc]["title"] if doc in sources else doc)
    if view == "Student":
        student_view(system_name)
    else:
        staff_view()


main()
