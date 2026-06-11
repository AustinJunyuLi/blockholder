# COMPILE.md — Build the three deliverables locally

Instructions for Claude Code. The sources are already final (abstract ≤150
words, Metropolis Beamer theme, consulting-style PPTX, polished figures).
Your job is only to **regenerate figures with local fonts, compile, verify,
and collect the outputs**. Do not edit content unless a check below fails.

## Deliverables

| # | Artifact | Built from | Final location |
|---|----------|-----------|----------------|
| 1 | `draft_v2.pdf` | `draft_v2.tex` (XeLaTeX + biber) | repo root → `deliverables/` |
| 2 | `presentation.pdf` | `pres/presentation.tex` (XeLaTeX + biber, Metropolis) | `pres/` → `deliverables/` |
| 3 | `blockholder_seminar_40min.pptx` | `pres/make_pptx.py` (python-pptx) | `pres/` → `deliverables/` |

## Step 0 — Preflight

```bash
cd <repo root>
which xelatex biber pdftocairo || echo "MISSING TOOL"
ls .venv/bin/python || make venv
.venv/bin/python -c "import pptx" || .venv/bin/pip install python-pptx
kpsewhich beamerthememetropolis.sty   # must resolve (ships with TeX Live)
```

- `biber` missing → `tlmgr install biber` (or comes with MacTeX).
- `pdftocairo` missing → `brew install poppler`.
- Metropolis warns if Fira Sans is absent and falls back to the default
  sans — that is fine. Optional: `tlmgr install fira`.

## Step 1 — Regenerate figures with local fonts

The committed figure PDFs were rendered on Linux with Latin Modern. Re-render
locally so the text font matches the manuscript exactly (CSV data already
exists; no solver run needed):

```bash
.venv/bin/python -m pyfig.render_all   --data-dir numerical_output/data --output-dir numerical_output
.venv/bin/python -m pyfig.slide_figures --data-dir numerical_output/data --output-dir pres/figures
.venv/bin/python -m empirics.facts --replot          # Fact 1, no network
.venv/bin/python -m empirics.fact2_analysis          # Fact 2, local data, ~10–60 s
```

Expected: 15 PDFs in `numerical_output/`, 4 in `pres/figures/`,
`fact1_delay.pdf` + `fact2_car.pdf` in `empirics/output/`. All figures have
**no in-figure titles** (house rule; captions/slide titles carry them).
`empirics/output/fact2_regressions.csv` may change only in float noise
(~1e-13); if coefficients change materially, stop and report.

## Step 2 — Manuscript

Stale aux files from earlier builds can break biblatex after version changes,
so clean first:

```bash
rm -f draft_v2.aux draft_v2.bbl draft_v2.bcf draft_v2.blg draft_v2.run.xml draft_v2.toc draft_v2.out
xelatex -interaction=nonstopmode draft_v2.tex
biber draft_v2
xelatex -interaction=nonstopmode draft_v2.tex
xelatex -interaction=nonstopmode draft_v2.tex
```

## Step 3 — Beamer deck

```bash
cd pres
rm -f presentation.aux presentation.bbl presentation.bcf presentation.blg \
      presentation.nav presentation.snm presentation.toc presentation.out presentation.run.xml
xelatex -interaction=nonstopmode presentation.tex
biber presentation
xelatex -interaction=nonstopmode presentation.tex
xelatex -interaction=nonstopmode presentation.tex
cd ..
```

Known-good noise: a handful (~8) of small `Overfull \vbox` warnings,
including one on the title page — verified cosmetically harmless. Do not
restyle frames to chase them.

## Step 4 — PPTX deck

Must run **after** Steps 1–3 so it rasterizes the fresh figure PDFs:

```bash
.venv/bin/python pres/make_pptx.py
```

Expected output: `wrote pres/blockholder_seminar_40min.pptx: 36 numbered slides`.

## Step 5 — Verify

```bash
# Abstract word count (must be ≤ 150; currently 148)
python3 - <<'EOF'
import re
tex = open("draft_v2.tex").read()
body = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S).group(1)
body = re.sub(r"\$[^$]*\$", "MATH", body.replace("\\noindent", " "))
body = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", body)
print("abstract words:", len(re.findall(r"[A-Za-z0-9'\-]+", body)))
EOF

# No missing figures / citations
grep -i "file not found\|undefined references" draft_v2.log pres/presentation.log || echo "logs clean"
grep -c "LaTeX Warning: Citation" draft_v2.log pres/presentation.log   # expect 0 after biber

# Page counts (sanity ranges)
pdfinfo draft_v2.pdf | grep Pages            # ≈ 86–90
pdfinfo pres/presentation.pdf | grep Pages   # ≈ 54–58
```

Visual spot-checks (render pages to PNG and look at them):
- `draft_v2.pdf` p.1: abstract is one paragraph, ~148 words.
- Figures appendix: no figure has an in-graphic title; nothing clipped.
- `presentation.pdf` p.1: Metropolis title page (no UCL banner anywhere).
- Evidence slides: in the Fact 1 histogram the "5 business days" label sits
  left of the dashed line, clear of the legend; the Fact 2 CAR figure has a
  full y-label ("Cumulative abnormal return (%)") and no title.
- PPTX: open it; title slide has a navy left bar; content slides have a
  hairline under the headline and a footer line; slide ~7 is
  "Three literatures, one missing piece".

## Step 6 — Collect deliverables

```bash
mkdir -p deliverables
cp draft_v2.pdf pres/presentation.pdf pres/blockholder_seminar_40min.pptx deliverables/
ls -la deliverables/
```

## Notes / guardrails

- Do **not** run `make clean` (it deletes the CSVs; regenerating them runs
  the full solver unnecessarily).
- Do not re-add in-figure titles or touch `pyfig/style.py` rcParams.
- The UCL theme files were deliberately deleted; if anything references
  `beamerthemeucl`, that is a bug to fix by removing the reference, not by
  restoring the theme.
- `empirics.facts` without `--replot` re-fetches ~300 EDGAR filings — never
  needed for compilation.
