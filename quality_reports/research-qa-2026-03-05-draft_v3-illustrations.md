# Research QA: Illustrations Parity (Critic -> Fixer -> Re-check)
Target: `draft_v3.tex` illustrations vs `evt_codebase/numerical_output/*` (figures, tables, and the surrounding narrative)
Date: 2026-03-05

## Round 1 Critic: Issues Found

### Critical
1. Captions referenced visual elements missing from the PDFs.
   - Decomposition caption referenced a dashed vertical line at \(\kappa^\dagger\) but `fig_decomposition.pdf` had no such line.
   - Cutoffs-vs-\(\kappa\) caption referenced a horizontal \(\mu\) line but `fig_cutoffs_kappa.pdf` had no such line.
   - Prices caption referenced posterior labels \(\pi(X,D)\) above bars and a legend distinguishing \(P_{post}\) vs \(P_{trade}\), but `fig_prices.pdf` lacked both.

2. Caption/object mismatch: noisy rumor precision.
   - Caption discussed the “activism premium” channel, but `fig_noisy_rumor_precision.pdf` plots \(\Delta^{\min}(\kappa)\).

3. Caption/object mismatch: welfare.
   - Caption suggested total surplus inherited the hump. Numerically, \(W_{tot}\) is increasing on the plotted grid while \(W_{min}=\Delta^{\min}\) is hump-shaped.

### Major
4. Sensitivity narrative and captions did not match the qualitative patterns shown in the plotted sweeps.
5. Premium-wedge sweep was not centered on the baseline wedge, undermining “robustness around baseline” language.
6. No-disclosure text referenced \(D=1\) despite the ND regime having no disclosure state.

### Minor
7. Some prose was stronger than what was numerically verified (especially “uniform/robust” hump claims across sweeps).
8. One paragraph used overly literal language about pre-filing belief levels at high \(\kappa\).

## Round 1 Fixer: Changes Implemented

### Code
- Updated `evt_codebase/numerical/figures.py`:
  - Added vertical \(\kappa^\dagger\) reference line to `fig_decomposition.pdf`.
  - Added horizontal \(\mu\) reference line to `fig_cutoffs_kappa.pdf`.
  - Added explicit legend labels and \(\pi(X,D)\) annotations to `fig_prices.pdf`.

- Updated `evt_codebase/numerical/solver.py`:
  - Made the \(k_D\) condition robust to region collapse by comparing PUBLIC against `max(HOLD, QUIET)`.

- Updated `evt_codebase/numerical/export_data.py`:
  - Recentered and retuned sensitivity grids to be both (i) around the baseline calibration and (ii) visually informative for curvature:
    - `C0`: {0.24, 0.25, 0.35, 0.40}
    - wedge \((m_1-m_0)\): {0.35, 0.40, 0.45}
    - `rho`: {0.88, 0.90, 0.92}
    - `s_xi`: {0.10, 0.12, 0.15}
    - `delta`: {0.93, 0.95, 0.97}

### Paper
- Updated `draft_v3.tex`:
  - Fixed captions to match plotted objects (noisy rumor, welfare, prices, reference lines).
  - Updated the sensitivity parameter sets to match the exported sweeps.
  - Softened statements that were stronger than what the figures/CSVs support.
  - Fixed the no-disclosure paragraph so it does not reference \(D=1\).
  - Tightened the endpoint lemma/proof to avoid claiming an “uninformative” limit under bounded noise.

### Verification
- `cd evt_codebase && make clean && make all` succeeds and regenerates all CSVs, tables, and PDFs.
- `pdflatex draft_v3.tex` succeeds and picks up the regenerated `numerical_output/*` artifacts.

## Round 2 Critic: Re-check (Current State)

- No remaining illustration mismatches found between LaTeX captions and the generated PDFs/tables.
- Remaining risks are mainly rhetorical (how strong you want to phrase general-equilibrium claims beyond what is explicitly plotted).
