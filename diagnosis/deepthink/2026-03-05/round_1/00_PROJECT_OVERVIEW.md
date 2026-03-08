# Project Overview

## CLAUDE.md

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Academic research project: **"Liquidity, Activism Disclosure, and Takeover Premia"** — an economic theory model studying blockholder behavior (exit, voice, corporate control). The codebase has three layers: numerical computation (Python), visualization (R/ggplot2), and manuscript/presentation (LaTeX/Beamer).

## Build Pipeline

The pipeline flows: **Python → CSV → R → PDF figures → LaTeX manuscript**.

```bash
# Full pipeline (data export + figure generation)
make all

# Step 1 only: Python model → 13 CSV files in numerical_output/data/
make data

# Step 2 only: R/ggplot2 → 13 PDF figures in numerical_output/
make figures

# Remove all generated CSVs and PDFs
make clean

# Full rebuild
make clean && make all
```

**Individual commands** (when Make isn't needed):
```bash
# Python data export
python -m numerical.export_data --output-dir numerical_output

# R figure rendering
Rscript R/render_all.R --data-dir numerical_output/data --output-dir numerical_output

# Compile manuscript
xelatex draft_v2.tex && biber draft_v2 && xelatex draft_v2.tex

# Compile presentation
cd pres && xelatex presentation.tex && biber presentation && xelatex presentation.tex
```

## Architecture

### Python numerical package (`numerical/`)

All modules import from `params.py` (the foundational module). Dependencies flow one way:

```
params.py → model.py → solver.py → export_data.py
                                  ↗
              accel.py (optional Numba JIT)
```

- **`params.py`**: `ModelParams` dataclass (baseline calibration), `Action` enum (EXIT/HOLD/QUIET/PUBLIC), `Cutoffs` and `MinorityGains` named tuples, tolerance constants
- **`model.py`**: Core economic functions — posteriors, prices, payoffs, welfare, information regimes. Sections of the paper are cited in comments
- **`solver.py`**: Equilibrium solver using damped fixed-point iteration with `scipy.optimize.brentq`. Multi-start search with collapsed-hold fallback
- **`export_data.py`**: Sweeps parameter grids and writes 13 CSV files — this is the interface contract between Python and R
- **`accel.py`**: Optional Numba JIT layer. Performance optimization only; `solver.py` is the reference implementation

**Conventions**: Pure functions throughout, full type hints, all functions take `params: ModelParams` argument, immutable return types (NamedTuples).

### R visualization (`R/`)

- **`theme_evtmodel.R`**: Shared theme, Paul Tol colourblind-friendly palette, and `plot_sensitivity()` helper. Must be sourced before any figure script
- **`plot_fig01_*.R` through `plot_fig13_*.R`**: One script per figure, each exports a function named `plot_figXX(data_dir, output_dir)`
- **`render_all.R`**: Master orchestrator that sources and calls all 13 figure scripts in sequence

**Color palette** (Paul Tol muted, used consistently across all figures):
- Exit: `#cc6677` (rose), Hold: `#ddcc77` (sand), Quiet Voice: `#88ccee` (cyan), Public Voice: `#44aa99` (teal)
- Sensitivity: `#4477aa`, `#ee6677`, `#228833`, `#ccbb44`

### CSV interface contract

The 13 CSV files in `numerical_output/data/` are the stable boundary between Python and R. Column names match paper notation. When modifying the model, update both the export logic and the corresponding R figure script.

### LaTeX

- **`draft_v2.tex`**: Main manuscript (XeLaTeX + biblatex/biber). References figures from `numerical_output/`
- **`pres/presentation.tex`**: Beamer slides with UCL institutional theme (`beamerthemeucl.sty`)
- **`bibliography.bib`**: Manuscript bibliography; `pres/slides.bib`: separate presentation bibliography

## Key Model Concepts

The blockholder chooses among four actions based on a private signal `s`:
- **Exit** (sell stake) when `s < k1`
- **Hold** (passive) when `k1 ≤ s < k0`
- **Quiet Voice** (engage below disclosure threshold) when `k0 ≤ s < kD`
- **Public Voice** (buy, engage, trigger disclosure) when `s ≥ kD`

Equilibrium cutoffs `(k1, k0, kD)` are solved via fixed-point iteration. The parameter `kappa` (noise trading intensity, 0 to 1) is the primary comparative statics variable.

## Numerical Tolerances

Defined in `params.py` — do not change without understanding downstream effects:
- `TOL_CONVERGE = 1e-6`: fixed-point convergence
- `TOL_RESIDUAL = 5e-3`: equilibrium quality gate
- `TOL_REGION = 1e-4`: cutoff collapse detection
- `TOL_PROB = 1e-10`: near-zero probability threshold

## R Dependencies

`ggplot2`, `dplyr`, `readr`, `latex2exp`, `scales`, `here`. All figures use `cairo_pdf()` device for font embedding.

## Working Notes

- The `figures/` directory contains archived matplotlib PDFs from before the R migration — these are superseded by `numerical_output/*.pdf`
- `figures_matplotlib.py` is archived legacy code; the active visualization pipeline is R-only
- Solver may produce NA rows at extreme `kappa` values (edge-case non-convergence) — this is expected and handled gracefully by R scripts
- No formal test suite; verification is via `make clean && make all` + visual inspection of output PDFs and CSV row counts


## Git History (last 20 commits)

```
4c63de2 refactor: move presentation from presentation/ to pres/, delete legacy
4742d6c feat(pres): add 7 theory backup slides and restructure presentation
42c61f9 Initial commit: Exit-Voice-Takeover model codebase
```


## Project Files

```
/home/austinli/Dropbox/Projects/Blockholder/directory/bibliography.bib
/home/austinli/Dropbox/Projects/Blockholder/directory/CLAUDE.md
/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.aux
/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.bcf
/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.log
/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.out
/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.run.xml
/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/Makefile
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical/export_data.py
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical/figures.py
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical/__init__.py
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical/model.py
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/baseline_cutoffs.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/baseline_params.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/baseline_series.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/cutoff_regions.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/disclosure_attenuation.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/noisy_rumor.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/prices.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/sensitivity_C0.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/sensitivity_delta.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/sensitivity_rho.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/sensitivity_sigma_xi.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/sensitivity_wedge.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/data/welfare.csv
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_cutoffs_kappa.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_cutoff_structure.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_decomposition.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_disclosure.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_noisy_rumor_precision.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_nonmonotone.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_prices.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_sensitivity_C0.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_sensitivity_delta.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_sensitivity_rho.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_sensitivity_sigma_xi.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_sensitivity_wedge.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/fig_welfare.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/table_disclosure_extensions.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical_output/table_example.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical/params.py
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical/solver.py
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/numerical/theme.py
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/README.md
/home/austinli/Dropbox/Projects/Blockholder/directory/evt_codebase/requirements.txt
/home/austinli/Dropbox/Projects/Blockholder/directory/figures/fig_cutoffs_kappa.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/figures/fig_cutoff_structure.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/figures/fig_decomposition.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/figures/fig_disclosure.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/figures/fig_nonmonotone.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/figures/fig_prices.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/figures/fig_sensitivity_C0.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/figures/fig_sensitivity_wedge.pdf
/home/austinli/Dropbox/Projects/Blockholder/directory/figures/table_disclosure_extensions.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/figures/table_example.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/.gitignore
/home/austinli/Dropbox/Projects/Blockholder/directory/Makefile
/home/austinli/Dropbox/Projects/Blockholder/directory/.playwright-mcp/console-2026-03-02T12-38-30-242Z.log
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/paper_review_draft_v3.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/plans/2026-02-08_numerical-polish-design.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/plans/2026-02-09_presentation-redesign.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/plans/2026-02-09_prose-polish-design.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/plans/2026-02-13_notation-consistency-fixes-design.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/plans/2026-02-13_notation-consistency-fixes-plan.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/plans/2026-02-17_figures-report.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/plans/2026-02-17_gemini-d1-d14-implementation.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/plans/2026-02-17_gemini-figures-prompt.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/plans/2026-03-02_backup-slides-design.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/plans/2026-03-02_backup-slides-plan.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/rewrites/abstract_conclusion_rewrite.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/rewrites/equilibrium_rewrite.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/rewrites/intro_rewrite.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/rewrites/litreview_rewrite.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/rewrites/model_rewrite.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/rewrites/numerical_compstatics_extensions_rewrite.tex
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/session_logs/2026-02-24_matplotlib-to-ggplot2.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/session_logs/2026-03-03_deepthink-round3-package.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/session_logs/2026-03-03_fixmd_review.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/session_logs/2026-03-04_theory-repair-round4.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/surgical_revision_prompt.md
/home/austinli/Dropbox/Projects/Blockholder/directory/quality_reports/surgical_revision_prompt_v2.md
/home/austinli/Dropbox/Projects/Blockholder/directory/.vscode/settings.json
```

Note: The `numerical/` directory (active Python package), `R/` directory (active visualization scripts), and `numerical_output/` directory (generated figures and data) are excluded from the listing above because they reside under paths not excluded by the filter. The active R scripts are at `R/` and active Python modules are at `numerical/`. Key active files not shown above due to filter behavior include:

- `numerical/params.py`, `numerical/model.py`, `numerical/solver.py`, `numerical/export_data.py`, `numerical/accel.py`
- `R/theme_evtmodel.R`, `R/render_all.R`, `R/plot_fig01_*.R` through `R/plot_fig13_*.R`
- `numerical_output/data/*.csv` (13 CSV files)
- `numerical_output/*.pdf` (13 PDF figures)
- `draft_v3.tex` (active manuscript, 1462 lines)


## Makefile

```makefile
# ============================================================================
# Makefile for Exit-Voice-Takeover model figures
#
# Pipeline: Python (model) → CSV data → R/ggplot2 → PDF figures
#
# Usage:
#   make all       -- run full pipeline (data + figures)
#   make data      -- export model computations to CSV
#   make figures   -- generate ggplot2 figures from CSV
#   make clean     -- remove generated CSVs and PDFs
# ============================================================================

DATA_DIR    := numerical_output/data
OUTPUT_DIR  := numerical_output

# CSV files produced by Python export
CSVS := $(DATA_DIR)/baseline_params.csv \
        $(DATA_DIR)/baseline_cutoffs.csv \
        $(DATA_DIR)/cutoff_regions.csv \
        $(DATA_DIR)/baseline_series.csv \
        $(DATA_DIR)/prices.csv \
        $(DATA_DIR)/disclosure_attenuation.csv \
        $(DATA_DIR)/sensitivity_C0.csv \
        $(DATA_DIR)/sensitivity_wedge.csv \
        $(DATA_DIR)/sensitivity_rho.csv \
        $(DATA_DIR)/sensitivity_sigma_xi.csv \
        $(DATA_DIR)/sensitivity_delta.csv \
        $(DATA_DIR)/noisy_rumor.csv \
        $(DATA_DIR)/welfare.csv

# PDF figures produced by R
PDFS := $(OUTPUT_DIR)/fig_cutoff_structure.pdf \
        $(OUTPUT_DIR)/fig_nonmonotone.pdf \
        $(OUTPUT_DIR)/fig_decomposition.pdf \
        $(OUTPUT_DIR)/fig_prices.pdf \
        $(OUTPUT_DIR)/fig_cutoffs_kappa.pdf \
        $(OUTPUT_DIR)/fig_disclosure.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_C0.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_wedge.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_rho.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_sigma_xi.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_delta.pdf \
        $(OUTPUT_DIR)/fig_noisy_rumor_precision.pdf \
        $(OUTPUT_DIR)/fig_welfare.pdf

.PHONY: all data figures clean

all: data figures

# Step 1: Python computation → CSV
data: $(CSVS)

$(CSVS) &: numerical/export_data.py numerical/model.py numerical/solver.py numerical/params.py
	python -m numerical.export_data --output-dir $(OUTPUT_DIR)

# Step 2: R/ggplot2 visualization → PDF
figures: $(PDFS)

# Step 2: Python/matplotlib visualization → PDF
$(PDFS) &: $(CSVS) numerical/figures.py numerical/theme.py
	python -m numerical.figures --data-dir $(DATA_DIR) --output-dir $(OUTPUT_DIR)

clean:
	rm -f $(CSVS)
	rm -f $(PDFS)
	rm -f $(OUTPUT_DIR)/table_example.tex $(OUTPUT_DIR)/table_disclosure_extensions.tex
```
