"""Render the diagram and long-table sources in docs/figures/*.tex to PNG images for the D1 report.

The report itself only inserts images (like the template example), so it compiles quickly on Overleaf.
Edit a source here (or redraw it in draw.io / Canva), then rerun this script and re-upload the PNG.
Needs a LaTeX install with pgf/tikz, pgfgantt and the libertine fonts, plus pdftoppm (poppler).

Usage: python tools/render_figures.py [name ...]   (no names = all figures)
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs" / "figures"
OUT = ROOT / "d1" / "images"

# Same class, size and fonts as the report (acmart 12pt), so text in the figures matches the report.
WRAPPER = r"""\documentclass[class=acmart,12pt,nonacm,acmlarge,border=0pt]{standalone}
\usepackage{tikz}
\usepackage{pgfgantt}
\usetikzlibrary{arrows.meta,positioning,fit,backgrounds,shapes.geometric}
\usepackage{array}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\begin{document}
\input{%s}
\end{document}
"""


def render(name):
    """Compile one figure to PDF, then convert it to a 300 dpi PNG in d1/images."""
    src = SRC / f"{name}.tex"
    with tempfile.TemporaryDirectory() as tmp:
        tex = Path(tmp) / "fig.tex"
        tex.write_text(WRAPPER % src.as_posix(), encoding="utf-8")
        # the report's own acmart.cls lives in d1/acm_format
        env = dict(os.environ, TEXINPUTS=f".{os.pathsep}{(ROOT / 'd1' / 'acm_format').as_posix()}//{os.pathsep}")
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "fig.tex"],
                       cwd=tmp, env=env, check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["pdftoppm", "-r", "300", "-png", "-singlefile", "fig.pdf", str(OUT / name)],
                       cwd=tmp, check=True)
    print("wrote", (OUT / f"{name}.png").relative_to(ROOT))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    names = sys.argv[1:] or sorted(p.stem for p in SRC.glob("*.tex"))
    for n in names:
        render(n)
