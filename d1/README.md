# D1 (Research Report) - main copy

This folder is the **main copy** of the D1 LaTeX project (no Overleaf GitHub sync).
It is the HWU template (`hwu_template/`, `acm_format/`, do not edit those) plus our `main.tex` and `references.bib`.

## Workflow (never edit both places at once)
1. **Claude edits here** and pushes to GitHub, then says which files changed (usually `main.tex`, `references.bib`, new `images/`).
2. **You upload those files to Overleaf** (drag and drop, replace) and check the PDF there.
3. **If you edit in Overleaf**, download the source zip (Menu > Download > Source) and unzip it over this folder before asking Claude to work on D1, so both copies match again.

## Build locally (optional)
`./build.sh` compiles to `build/main.pdf` (needs a TeX Live install). Overleaf compiles without any setup.

## Rules from the template
- Write only in `main.tex` and `references.bib`; images in `images/`, code snippets in `code/`.
- D1 main body: 14 pages maximum. Template must not be modified.
