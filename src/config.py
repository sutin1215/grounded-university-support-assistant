"""Load the YAML config and resolve paths relative to the repository root."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PATH_KEYS = ("raw_dir", "chunks_path", "faq_path", "questions_path", "results_dir", "cache_path")


def load_config(name: str = "pilot.yaml") -> dict:
    with open(ROOT / "configs" / name, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    for key in PATH_KEYS:
        if key in cfg:
            cfg[key] = ROOT / cfg[key]
    return cfg
