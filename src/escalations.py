"""File-based log of escalated questions, read by the staff view of the web interface (F3, F6).

Each line of the log is one escalation stored as JSON. Only the question text is kept, never
student details (NF1). In this prototype escalation is simulated: nothing is sent to a real inbox.

Usage:  log = EscalationLog(ROOT / "data" / "escalations.jsonl"); log.add("question", "S3")
"""
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path


class EscalationLog:
    def __init__(self, path):
        self.path = Path(path)

    def add(self, question: str, system: str, office: str = "Student Services") -> dict:
        """Record a question the assistant could not answer and return the new entry."""
        entry = {"id": uuid.uuid4().hex[:8].upper(),
                 "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 "question": question.strip(), "system": system, "office": office,
                 "status": "open", "note": ""}
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        return entry

    def all(self) -> list:
        """All escalations, newest first."""
        if not self.path.exists():
            return []
        with open(self.path, encoding="utf-8") as f:
            entries = [json.loads(line) for line in f if line.strip()]
        return sorted(entries, key=lambda e: e["time"], reverse=True)

    def resolve(self, esc_id: str, note: str = "") -> bool:
        """Mark one escalation as resolved, with an optional staff note. Returns False if not found."""
        entries, found = self.all(), False
        for e in entries:
            if e["id"] == esc_id:
                e["status"], e["note"], found = "resolved", note.strip(), True
        if found:
            with open(self.path, "w", encoding="utf-8") as f:
                f.writelines(json.dumps(e) + "\n" for e in reversed(entries))
        return found
