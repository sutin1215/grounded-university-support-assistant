"""Load the YAML config and resolve paths relative to the repository root."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_config(name: str = "pilot.yaml") -> dict:
    with open(ROOT / "configs" / name, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    for key in ("raw_dir", "chunks_path", "faq_path", "questions_path", "results_dir"):
        cfg[key] = ROOT / cfg[key]
    return cfg
