#!/usr/bin/env bash
# Compile D1 locally. Overleaf finds acmart.cls in acm_format/ automatically; plain TeX Live needs the search path.
cd "$(dirname "$0")"
export TEXINPUTS=.:./acm_format//: BSTINPUTS=.:./acm_format//:
latexmk -pdf -interaction=nonstopmode -outdir=build main.tex && echo "PDF: d1/build/main.pdf"
