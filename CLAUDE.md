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
cd presentation && xelatex slides_v2.tex && biber slides_v2 && xelatex slides_v2.tex
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
- **`presentation/slides_v2.tex`**: Beamer slides with UCL institutional theme (`beamerthemeucl.sty`)
- **`bibliography.bib`**: Manuscript bibliography; `presentation/slides.bib`: separate presentation bibliography

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
