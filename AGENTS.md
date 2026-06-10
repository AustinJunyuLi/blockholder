# AGENTS.md

This file provides guidance to Codex and other coding agents working in this repository. (Kept in sync with CLAUDE.md — that file is the canonical, more detailed version.)

## Project Overview

Academic research project: **"Liquidity, Activism Disclosure, and Takeover Premia"** — an economic theory model of blockholder behavior (exit, voice, corporate control). Layers: numerical computation (Python, `numerical/`), visualization (Python/matplotlib, `pyfig/`), empirics (`empirics/`, EDGAR 13D/G), and manuscript/presentation (XeLaTeX/Beamer).

## Build Pipeline (Python end-to-end)

```bash
make venv      # create .venv from requirements.txt (once)
make all       # data (16 CSVs in numerical_output/data/) + figures (15 PDFs)
make data      # numerical/export_data.py only
make figures   # pyfig/render_all.py only
make clean
```

Manuscript: `xelatex draft_v2.tex && biber draft_v2 && xelatex draft_v2.tex` (×2).
Presentation: same in `pres/` (bibliography: `pres/slides.bib`, a real file — do not recreate the old symlink).

## Architecture

- `numerical/params.py` → `model.py` → `solver.py` → `export_data.py`; `accel.py` optional Numba mirror; `takeover_game.py` = Appendix-D7 tender game (microfounded premium wedge; opt-in via `params_with_endogenous_wedge`).
- `pyfig/style.py` (Paul Tol muted palette, CM mathtext) + `figures.py` (`fig01`–`fig15`, `ALL_FIGURES`) + `render_all.py`.
- `empirics/` — stdlib-only EDGAR pipeline (throttled, declared User-Agent); raw data gitignored under `empirics/data/`; summaries committed under `empirics/output/`.
- `quality_reports/fixes/` — D-series derivation records (`DN_*.tex`, some `\input` into the draft) + paired `dN_*_check.py` verification scripts with JSON artifacts. Never weaken the honesty labels (proved vs conditional vs numerically-verified) in these files or the draft.

## Conventions

- Pure functions, full type hints, `params: ModelParams` argument, NamedTuple returns.
- Tolerances in `params.py` (`TOL_CONVERGE=1e-6`, `TOL_RESIDUAL=5e-3`, `TOL_REGION=1e-4`, `TOL_PROB=1e-10`) — do not change casually.
- Solver NA rows at extreme `kappa` are expected; figure functions drop NAs.
- No formal test suite; verification = `make clean && make all` + the `dN_*_check.py` scripts + compile gates (0 errors, 0 undefined refs).

## Known environment notes (this host)

- `biber` requires `libxcrypt-compat` (RHEL10): `sudo dnf install libxcrypt-compat` if citation resolution fails with a `libcrypt.so.1` error.
- TeX Gyre fonts are exposed to fontconfig via `~/.config/fontconfig/fonts.conf`.
