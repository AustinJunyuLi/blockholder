# CLAUDE.md

This file provides guidance to Claude Code and other agents when working with code in this repository.

## Project Overview

Academic research project: **"Liquidity, Activism Disclosure, and Takeover Premia"** — an economic theory model studying blockholder behavior (exit, voice, corporate control). Three layers: numerical computation (Python, `numerical/`), visualization (Python/matplotlib, `pyfig/`), and manuscript/presentation (LaTeX/Beamer). Build entry point is the Makefile; compile commands live in the verify-blockholder skill.

## Host environment (RHEL10 build host — not universal)

- `biber` requires `libxcrypt-compat` (RHEL10): `sudo dnf install libxcrypt-compat` if citation resolution fails with a `libcrypt.so.1` error.
- TeX Gyre fonts are exposed to fontconfig via `~/.config/fontconfig/fonts.conf`.

## Architecture gotchas

- Import order is one-way: `params.py` → `model.py` → `solver.py` → `export_data.py` (`accel.py` is an optional Numba mirror of `solver.py`, not on the critical path).
- `numerical/` code convention: pure functions with full type hints; every function takes `params: ModelParams` as first argument and returns immutable NamedTuples.
- `takeover_game.py`'s microfounded premium wedge (`params_with_endogenous_wedge`) is **opt-in**; the exogenous `(m0, m1)` wedge remains the default everywhere else.
- CSV interface contract: `numerical_output/data/*.csv` is the stable boundary between the model and the figure layer. Changing the model requires updating both `export_data.py` and the matching function in `pyfig/figures.py` together — they drift silently otherwise. Column names match paper notation.
- `pyfig/figures.py` house rule: no in-figure titles (LaTeX captions / slide titles carry them); multi-panel figures use `(a)/(b)` panel labels.
- `pres/presentation.tex` uses the Beamer Metropolis theme with no local `.sty` file — it ships with TeX Live, don't go hunting for a missing style file.
- Two separate bibliographies: `bibliography.bib` (manuscript) and `pres/slides.bib` (deck). `pres/slides.bib` is a real file, not a symlink — an older setup symlinked it to the manuscript bibliography; do not recreate that symlink. Verify a bibkey exists in the right file before citing; a wrong/invented key fails the compile gates.
- `draft_v2.tex`'s abstract is capped at 150 words — nothing enforces this at compile time, so re-count after any abstract edit.
- Figures are written as vector PDF with embedded fonts (`pdf.fonttype = 42`) and matplotlib `mathtext` (Computer Modern) to match manuscript typography.
- Derivation records in `quality_reports/fixes/`: each lands as `DN_*.tex` (spliced into `draft_v2.tex` via `\input` for D7/D8) plus a paired `dN_*_check.py` verification script emitting JSON. Never weaken the honesty labels (proved / conditional / numerically-verified) in these files or the draft.
- Empirics layer (`empirics/`): stdlib-only EDGAR pipeline. See `empirics/README.md` for the fetch/parse/facts workflow.

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

## Working Notes

- The active visualization pipeline is Python/matplotlib (`pyfig/`); the earlier R/ggplot2 layer (`R/`) was removed in favour of an end-to-end Python pipeline.
- The `figures/` directory (if present) holds archived PDFs superseded by `numerical_output/*.pdf`.
- Solver may produce NA rows at extreme `kappa` values (edge-case non-convergence) — this is expected and the figure functions drop NA rows gracefully.
- No formal test suite.

## Verification

Before any commit or completion claim, run the **verify-blockholder** skill (data / figures / both LaTeX compiles / D7 / D8 gates). Don't restate its gates here — it's the single source of truth for what "done" means.
