# Full Numerical Codebase Request — Liquidity, Activism Disclosure, and Takeover Premia (Round 3)

**Commit:** 4c63de2 (2026-03-04)
**Files in package:** 26 files, 76 KB

---

## What I Need From You

I need you to deliver **two things**:

1. **A complete, runnable Python codebase** (as a zip file or clearly delimited complete files) that implements the numerical exercise for my paper. The codebase must go end-to-end: from model parameters to equilibrium computation to data export to publication-quality figures. Everything must match the corrected theory in `draft_v3.tex`.

2. **A detailed, copy-pasteable rewrite guide** for all numerical-discussion sections of `draft_v3.tex`. Wherever the paper discusses numerical results, calibration, comparative statics, or figure descriptions, provide the exact LaTeX replacements to ensure the text accurately describes what the code produces.

---

## The Paper

`draft_v3.tex` is included in the zip. This is the **authoritative theory reference**. The proofs have been rigorously audited and corrected across a 3-model triangulation (GPT Pro × Gemini Deep Think × Claude). The theory is correct. Your code must faithfully implement it.

### Key equations you must implement:

**Noise distribution** (z ∈ {-1, 0, +1}):
- P(z=0) = 1 − 2κ/3, P(z=±1) = κ/3
- Order flow: X = q + z ∈ {-2, -1, 0, 1, 2}

**Posteriors** (Proposition 2, lines ~1048-1083 in draft_v3.tex):
- π(X, 1) = 1 for all X (disclosed = engaged)
- π(1, 0) = ω_Q/(ω_H + ω_Q) — κ-invariant
- π(-1, 0) = ω_Q·(κ/3) / [(ω_H+ω_Q)·(κ/3) + ω_E·(1−2κ/3)]
- π(0, 0) = ω_Q·(1−2κ/3) / [(ω_H+ω_Q)·(1−2κ/3) + ω_E·(κ/3)]
- π(-2, 0) = 0

**Pricing** (feed-forward, Section 3.4):
- V̂(X,D) = E[v|X,D] + Δ̃·π(X,D)
- P_post(X,D) = δ·[p(X,D)·b(X,D) + (1−p(X,D))·V̂(X,D)]
- P_trade(X) = Σ_d P(D=d|X)·P_post(X,d) — weighted average, NO recursion

**Bid probability** (eq:bid-prob):
- p(X,D) = λ_B · [1 − Λ((V̂(X,D) + m̄(X,D) + K − (S̄ + π(X,D)·ΔS)) / s_ξ)]
- Net deterrence: ∂p/∂π < 0 under A5 (Δ̃ + m̃ − m₀ > ΔS)

**Payoffs** (affine in signal, eq:U-affine):
- U(q,a|s) = A_{q,a} + B_{q,a}·v̂(s) − a·C(s)
- C(s) = C₀·exp(−χ·(s−μ)/σ_s) — engagement cost, decreasing in s

**Indifference conditions** (three cutoffs k1, k0, kD):
- k1: U_Exit(k1) = U_Hold(k1)
- k0: U_Hold(k0) = U_Quiet(k0)
- kD: U_Quiet(kD) = U_Public(kD)

**Minority gains decomposition** (Proposition 5):
- Δ^min(κ) = Δ^base(κ) + Δ^act(κ)
- Δ^base(κ) = m₀ · P(bid)
- Δ^act(κ) = (m̃−m₀) · E[π(X,D) · 1{bid}]

**Welfare** (Section 7):
- W_min: minority shareholder welfare
- W_bid: bidder welfare
- W_tot: total welfare

**Information regimes** (Section 8 — Extensions):
- Baseline: D = 1{q=+1}
- No disclosure: market sees only X
- Noisy rumor: market sees (X, D, R) where R has hit/false-alarm rates (η₁, η₀)

### Baseline calibration:
μ=1.0, σ_v=0.50, σ_ε=0.50, κ=0.50, C₀=0.25, χ=0.50, ρ=0.90, Δ=0.25,
m₀=0.10, m₁=0.30, S̄=1.10, Δ_S=0.30, K=0.15, s_ξ=0.15, λ_B=0.20, δ=0.95

Derived: Δ̃ = ρΔ = 0.225, m̃ = m₀ + ρ(m₁−m₀) = 0.28, β = σ_v²/(σ_v²+σ_ε²) = 0.5

---

## Legacy Reference Code

The zip includes a **legacy Python codebase** (`numerical/` directory) from a previous version of the paper. Use it as **structural reference only** — it shows the architecture pattern (params → model → solver → export), the CSV schema contract, and the calibration values. Do NOT assume the legacy code is correct; implement from the theory in `draft_v3.tex`.

### Architecture to follow:

```
numerical/
├── __init__.py          # Public API
├── params.py            # ModelParams dataclass, Action enum, tolerances
├── model.py             # Core economics: posteriors, prices, payoffs, welfare, regimes
├── solver.py            # Equilibrium solver: damped fixed-point iteration + Brent
├── export_data.py       # Parameter sweeps → 13 CSVs + 2 LaTeX tables
├── theme.py             # [NEW] Publication theme: Paul Tol palette, save_figure()
└── figures.py           # [NEW] All 13 figures: seaborn + matplotlib
```

### CSV interface contract (stable — figures.py reads these):

| CSV | Key columns | Description |
|-----|------------|-------------|
| baseline_params.csv | param, value | 20 model parameters + derived quantities |
| baseline_cutoffs.csv | k1, k0, kD, mu, sigma_s | Single equilibrium at baseline |
| cutoff_regions.csv | region, xmin, xmax | Region bounds for number-line figure |
| baseline_series.csv | kappa, k1, k0, kD, delta_min, base, act | 35-point κ sweep |
| prices.csv | X, D, P_post, P_trade, pi, p_bid, m_XD, on_path | 7 (X,D) states |
| disclosure_attenuation.csv | kappa, act_disclosure, act_no_disclosure | Activism gains comparison |
| sensitivity_C0.csv | kappa, C0, delta_min | 21κ × 4 C0 values |
| sensitivity_wedge.csv | kappa, wedge, delta_min | 21κ × 3 wedge values |
| sensitivity_rho.csv | kappa, rho, delta_min | 21κ × 3 ρ values |
| sensitivity_sigma_xi.csv | kappa, s_xi, delta_min | 21κ × 3 s_ξ values |
| sensitivity_delta.csv | kappa, delta, delta_min | 21κ × 3 δ values |
| noisy_rumor.csv | kappa, eta_1, eta_0, label, delta_min | 21κ × 3 rumor regimes |
| welfare.csv | kappa, W_min, W_bid, W_tot | 21 κ values |

### 13 Figures to produce:

| # | Output filename | Data source | What it shows |
|---|----------------|-------------|---------------|
| 1 | fig_cutoff_structure.pdf | cutoff_regions.csv, baseline_cutoffs.csv | Number-line: colored bands for Exit/Hold/Quiet/Public, k1/k0/kD markers |
| 2 | fig_nonmonotone.pdf | baseline_series.csv | Δ^min vs κ with peak marker κ† |
| 3 | fig_decomposition.pdf | baseline_series.csv | Base + activism components (stacked or overlaid), showing opposing forces |
| 4 | fig_prices.pdf | prices.csv | Two-panel: P(X,D=0) and P(X,D=1) bar charts by order flow X |
| 5 | fig_cutoffs_kappa.pdf | baseline_series.csv | Three lines (k1, k0, kD) vs κ |
| 6 | fig_disclosure.pdf | disclosure_attenuation.csv | Activism gains: disclosure vs no-disclosure regime |
| 7 | fig_sensitivity_C0.pdf | sensitivity_C0.csv | Family of Δ^min(κ) curves for different C0 |
| 8 | fig_sensitivity_wedge.pdf | sensitivity_wedge.csv | Family for different premium wedge values |
| 9 | fig_sensitivity_rho.pdf | sensitivity_rho.csv | Family for different ρ |
| 10 | fig_sensitivity_sigma_xi.pdf | sensitivity_sigma_xi.csv | Family for different s_ξ |
| 11 | fig_sensitivity_delta.pdf | sensitivity_delta.csv | Family for different δ |
| 12 | fig_noisy_rumor_precision.pdf | noisy_rumor.csv | Three rumor regimes comparison |
| 13 | fig_welfare.pdf | welfare.csv | W_min, W_bid, W_tot with optimal markers |

### Figure quality:
- **Publication-ready for JF/RFS/JFE** — clean, minimal, no chartjunk
- **seaborn + matplotlib** — seaborn for statistical plots, matplotlib for custom layouts
- **Paul Tol muted palette** (colorblind-safe):
  - Actions: Exit=#cc6677, Hold=#ddcc77, Quiet=#88ccee, Public=#44aa99
  - Sensitivity: #4477aa, #ee6677, #228833, #ccbb44
- **LaTeX math labels** ($\kappa$, $\Delta^{\min}$, $k_D$, etc.)
- **PDF vector output**, 6×4 inches single panel, 10×4 two-panel
- **Handle NA values** gracefully (non-convergent equilibria at extreme κ)

---

## Deliverable 1: Complete Python Codebase

Return **every file** listed above as complete, runnable Python. The codebase must work end-to-end:

```bash
pip install -r requirements.txt
make clean && make all
# → produces: 13 CSVs + 2 LaTeX tables + 13 PDF figures
```

**Do NOT abbreviate.** Do NOT say "similar to above" or "rest unchanged." Every function, every import, every line. If a file is 800 lines, return all 800 lines. The cost of a gap is orders of magnitude higher than the cost of verbosity.

---

## Deliverable 2: Paper Rewrite Guide for Numerical Sections

After writing the code and verifying the outputs, provide a **detailed, section-by-section rewrite guide** for all parts of `draft_v3.tex` that discuss numerical results. For each section:

1. Quote the current text (with line numbers)
2. Provide the exact LaTeX replacement
3. Explain what changed and why (e.g., "the hump peak shifted from κ=0.24 to κ=0.26 because...")

Sections to cover:
- **Section 5** (Numerical Comparative Statics): All figure descriptions, calibration discussion, reported numerical values
- **Section 7** (Welfare): Welfare results discussion
- **Section 8** (Extensions): Disclosure regime comparisons, noisy rumor results
- **Appendix tables**: Any values in table_example.tex or table_disclosure_extensions.tex
- **Any in-text numerical claims**: κ† value, hump height, cutoff values, etc.

If the corrected code produces results identical to the legacy code, say so explicitly: "No text changes needed — legacy code was correct."

---

_Internal: snapshot_sha=4c63de2, round=3, date=2026-03-04_
