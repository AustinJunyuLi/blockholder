# Project Overview

## Identity
**Title:** "Liquidity, Activism Disclosure, and Takeover Premia: A Theory of Exit, Voice, and Corporate Control"
**Author:** Austin Li
**Type:** Academic economics theory paper (job market paper candidate)
**Stage:** Pre-submission; theory complete, proofs revised, calibration partially working

## Architecture

```
numerical/params.py   → ModelParams dataclass, Action enum, Cutoffs, tolerances
numerical/model.py    → Core economic functions (posteriors, prices, payoffs, welfare)
numerical/solver.py   → Equilibrium solver (damped fixed-point iteration)
numerical/export_data.py → Parameter sweeps → 14 CSV files
R/*.R                 → ggplot2 figure generation from CSVs
draft_v3.tex          → Full manuscript (~1448 lines)
```

Pipeline: `Python → CSV → R → PDF figures → LaTeX manuscript`

## Git State

**Commit:** 4c63de2
**Branch:** main
**Recent history:**
```
4c63de2 refactor: move presentation from presentation/ to pres/, delete legacy
4742d6c feat(pres): add 7 theory backup slides and restructure presentation
42c61f9 Initial commit: Exit-Voice-Takeover model codebase
```

**Uncommitted changes:** All current work (draft_v3.tex, params.py, model.py, solver.py, export_data.py, all CSVs, all figures). This is intentional — we are iterating on theory+calibration before committing.

## Directory Tree (key files only)

```
draft_v3.tex                    # Main manuscript
bibliography.bib                # References
numerical/
  params.py                     # Parameter definitions (ModelParams dataclass)
  model.py                      # Core economic model (~648 lines)
  solver.py                     # Equilibrium solver (~238 lines)
  export_data.py                # CSV export (~284 lines)
numerical_output/
  data/                         # 14 CSV files (current output)
    baseline_series.csv         # Δ^min vs κ (the main result)
    prices.csv                  # Equilibrium prices at baseline κ=0.50
    disclosure_attenuation.csv  # Disclosure vs no-disclosure comparison
    sensitivity_*.csv           # Parameter sensitivity sweeps
    welfare.csv                 # Welfare decomposition
  *.pdf                         # 13 PDF figures
R/
  theme_evtmodel.R              # Shared theme + Paul Tol palette
  plot_fig01_*.R ... plot_fig13_*.R  # One script per figure
  render_all.R                  # Master orchestrator
diagnosis/
  deepthink/2026-03-03/
    round_1/                    # First Gemini review (identified issues)
    round_2/                    # Second Gemini review prompt
  fix2.md                       # Round 2 reply (applied)
```

## Model Summary

A blockholder observes private signal s about firm value v and chooses among:
- **Exit** (q=-1, a=0): sell stake
- **Hold** (q=0, a=0): passive retention
- **Quiet Voice** (q=0, a=1): engage below disclosure threshold
- **Public Voice** (q=+1, a=1): buy, engage, trigger disclosure (D=1)

Market maker prices from discrete order flow X=q+z and disclosure D.
Bidder conditions entry on (X,D) and private synergy shock ξ.
Equilibrium cutoffs (k1, k0, kD) solved via fixed-point iteration.

The central result: expected minority takeover gains Δ^min(κ) are nonmonotone (hump-shaped) in noise-trading intensity κ.
