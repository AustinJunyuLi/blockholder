# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Academic research project: **"Liquidity, Activism Disclosure, and Takeover Premia"** — an economic theory model studying blockholder behavior (exit, voice, corporate control). The codebase has three layers: numerical computation (Python), visualization (Python/matplotlib), and manuscript/presentation (LaTeX/Beamer).

## Build Pipeline

The pipeline flows (Python end-to-end): **Python → CSV → matplotlib → PDF figures → LaTeX manuscript**.

Set up the environment once with `make venv` (creates `.venv/` from `requirements.txt`).

```bash
# Full pipeline (data export + figure generation)
make all

# Step 1 only: Python model → 16 CSV files in numerical_output/data/
make data

# Step 2 only: matplotlib → 15 PDF figures in numerical_output/
#              + 4 slide-only variants in pres/figures/
make figures

# Remove all generated CSVs and PDFs
make clean

# Full rebuild
make clean && make all
```

**Individual commands** (when Make isn't needed):
```bash
# Python data export
.venv/bin/python -m numerical.export_data --output-dir numerical_output

# Python figure rendering (manuscript + slide-only variants)
.venv/bin/python -m pyfig.render_all --data-dir numerical_output/data --output-dir numerical_output
.venv/bin/python -m pyfig.slide_figures --data-dir numerical_output/data --output-dir pres/figures

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
- **`takeover_game.py`**: Disagreement-node tender game (Appendix D7) — derives the appropriability coefficient `lambda = 1 - q(1-gamma)psi` and the microfounded premium wedge; `params_with_endogenous_wedge` maps game primitives into `ModelParams` (opt-in; exogenous `(m0, m1)` remains the default)
- **`model.py`**: Core economic functions — posteriors, prices, payoffs, welfare, information regimes. Sections of the paper are cited in comments
- **`solver.py`**: Equilibrium solver using damped fixed-point iteration with `scipy.optimize.brentq`. Multi-start search with collapsed-hold fallback
- **`export_data.py`**: Sweeps parameter grids and writes 13 CSV files — this is the interface contract between the model and the figure layer (`pyfig/`)
- **`accel.py`**: Optional Numba JIT layer. Performance optimization only; `solver.py` is the reference implementation

**Conventions**: Pure functions throughout, full type hints, all functions take `params: ModelParams` argument, immutable return types (NamedTuples).

### Python visualization (`pyfig/`)

- **`pyfig/style.py`**: Shared matplotlib house style, Paul Tol colourblind-friendly palette, and helpers (`apply_style`, `new_ax`, `legend_outside`, `save_fig`). Editorial-minimal, with Computer-Modern math typography matching the manuscript
- **`pyfig/figures.py`**: One function per figure (`fig01_*` … `fig15_*`; fig14 = GE channel decomposition, fig15 = microfounded wedge), each taking `(data_dir, output_dir)`; `ALL_FIGURES` lists them in render order. House rule: no in-figure titles (LaTeX captions and slide titles carry them); multi-panel figures use `(a)/(b)` panel labels
- **`pyfig/render_all.py`**: Master orchestrator (`python -m pyfig.render_all`) that applies the style and calls all 15 manuscript figures
- **`pyfig/slide_figures.py`**: Four slide-only variants written to `pres/figures/` (`fig_disclosure_slopes`, `fig_sensitivity_panel1/2`, `fig_noisy_rumor`), used by the Beamer deck and the PPTX build

**Color palette** (Paul Tol muted, used consistently across all figures):
- Exit: `#cc6677` (rose), Hold: `#ddcc77` (sand), Quiet Voice: `#88ccee` (cyan), Public Voice: `#44aa99` (teal)
- Sensitivity: `#4477aa`, `#ee6677`, `#228833`, `#ccbb44`

### CSV interface contract

The CSV files in `numerical_output/data/` (16 as of 2026-06: the original 13 plus `ge_decomposition.csv`, `ge_cellmap.csv`, `wedge_primitives.csv`) are the stable boundary between the model and the figure layer. Column names match paper notation. When modifying the model, update both the export logic and the corresponding figure function in `pyfig/figures.py`.

### Empirics layer (`empirics/`)

Stdlib-only EDGAR pipeline for the de-risk data leg: `edgar_fetch.py` (quarterly form.idx enumeration, throttled fetcher), `parse_13d.py` (event/filed dates, CIKs), `facts.py` (Fact 1: 13D disclosure-delay compression around the 2024-02-05 five-business-day rule). Raw data in `empirics/data/` is gitignored; summaries committed in `empirics/output/`. See `empirics/README.md`.

### Derivation records (`quality_reports/fixes/`)

D-series pattern: each derivation lands as `DN_*.tex` (spliced into `draft_v2.tex` via `\input` for D7/D8) plus a paired `dN_*_check.py` verification script with JSON output. D7 = tender-game microfoundation of the premium wedge; D8 = GE cutoff-shift region theorem + counterexample.

### LaTeX

- **`draft_v2.tex`**: Main manuscript (XeLaTeX + biblatex/biber). References figures from `numerical_output/`. Abstract is capped at 150 words
- **`pres/presentation.tex`**: Beamer slides, Metropolis theme with paper-palette accents (no local `.sty` files; theme ships with TeX Live). Pulls shared figures from `numerical_output/` via `\graphicspath`
- **`pres/make_pptx.py`**: Business-format PPTX twin of the Beamer deck (navy/charcoal consulting style); rasterizes the same PDFs into `pres/pptx_assets/`
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

## Python Dependencies

`numpy`, `scipy`, `pandas`, `matplotlib` (pinned in `requirements.txt`; install via `make venv`). Figures are written as vector PDF with embedded fonts (`pdf.fonttype = 42`) and matplotlib `mathtext` (Computer Modern) for math labels.

## Working Notes

- The active visualization pipeline is Python/matplotlib (`pyfig/`); the earlier R/ggplot2 layer (`R/`) was removed in favour of an end-to-end Python pipeline
- The `figures/` directory (if present) holds archived PDFs superseded by `numerical_output/*.pdf`
- Solver may produce NA rows at extreme `kappa` values (edge-case non-convergence) — this is expected and the figure functions drop NA rows gracefully
- No formal test suite; verification is via `make clean && make all` + visual inspection of output PDFs and CSV row counts
