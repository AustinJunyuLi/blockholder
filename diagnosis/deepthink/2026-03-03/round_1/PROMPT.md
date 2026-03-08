# Numerical Code Overhaul Request — Exit-Voice-Takeover Model (Round 1)

**Commit:** 4c63de2 (branch: theory-fixes)
**Date:** 2026-03-03
**Files uploaded:** Up to 10 raw source files

## IMPORTANT: Verbosity and Thoroughness Requirements

**I need you to operate at MAXIMUM VERBOSITY and MAXIMUM THOROUGHNESS.** This is a critical juncture: the theory paper (`draft_v3.tex`) has been completely rewritten with fundamental mathematical changes, but the numerical Python code still implements the OLD formulations. Every function, every line, every formula must be audited and updated.

Do not summarize. Do not skip. Do not say "similar changes apply to..." — spell out every single change explicitly. Show me the exact old code and the exact new code for every modification. I need a complete, copy-pasteable transformation of every affected file.

Push your limits. Use your full context window. This is the most important task.

---

## How to Read the Uploaded Files

| File | Role |
|------|------|
| `draft_v3.tex` | **THE AUTHORITATIVE SPEC** — the rewritten theory paper with all 22 fixes applied |
| `draft_v3.pdf` | Compiled PDF for visual cross-reference (equations, tables, figures) |
| `fix.md` | The 22-fix changelog that drove the theory rewrite (context for what changed and why) |
| `params.py` | Model parameters dataclass — **OUTDATED calibration, missing Δ_S** |
| `model.py` | Core economic functions — **OUTDATED bid probability (Normal→Logistic), missing V̂ in threshold** |
| `solver.py` | Equilibrium solver — calls model functions, may need signature updates |
| `export_data.py` | CSV export + LaTeX tables — references `sigma_xi` in sweep names |
| `accel.py` | Numba JIT accelerator — **COMPLETELY OUT OF SYNC**, currently disabled |
| `bibliography.bib` | BibTeX bibliography |

You may also receive the `Makefile` (build pipeline: Python→CSV→R→PDF).

**The authoritative source of truth is `draft_v3.tex`.** All Python code must be brought into exact alignment with the equations in that paper. The PDF is provided so you can visually inspect equations, tables (especially Table C.3 calibration), and notation.

---

## Context: What Changed and Why

The paper underwent a fundamental mathematical restructuring. Here are the 6 core changes:

### Change 1: Feed-Forward Pricing (Replaces Recursive Fixed-Point)
- **Old:** Bidder surplus depended on market price P(X,D), and price depended on bid probability → circular fixed point requiring Assumption A7 (δ/σ_ξ < 1/φ(0))
- **New:** Bidder anchors to standalone fundamental value V̂(X,D) = E[v|X,D] + Δ̃·π(X,D), NOT to market price P(X,D). The pricing equation becomes a pure feed-forward formula. A7 is eliminated entirely.

### Change 2: Logistic Synergy Distribution (Replaces Normal)
- **Old:** ξ ~ N(0, σ_ξ²), bid probability used Φ (Normal CDF)
- **New:** ξ ~ Logistic(0, s_ξ), bid probability uses Λ (Logistic CDF)
- The parameter `sigma_xi` is replaced by `s_xi` everywhere

### Change 3: Synergy Facilitation Parameter Δ_S
- **Old:** Bidder surplus = S̄ + ξ - b(X,D) - K
- **New:** Bidder surplus = (S̄ + π(X,D)·Δ_S) + ξ - b(X,D) - K
- Activism fundamentally facilitates the sale by increasing expected synergy by Δ_S

### Change 4: Corrected Noise Distribution
- **Old:** P(z=0) = 1-κ, P(z=±1) = κ/2
- **New:** P(z=0) = 1-2κ/3, P(z=±1) = κ/3
- **This was already applied to `model.py` but NOT to `accel.py`**

### Change 5: Updated Calibration Parameters
- **Old:** S̄=0.60, σ_ξ=0.30
- **New:** S̄=1.44, Δ_S=0.35, s_ξ=0.15
- See Table C.3 in the paper (line ~1310 of draft_v3.tex) for full calibration

### Change 6: Net Deterrence Assumption (A5)
- **New A5:** Δ̃ + m̃ - m₀ > Δ_S (replaces old δ/σ_ξ < 1/φ(0))

---

## Your Task: Complete Code Audit and Rewrite

### Part 1: Parameter Updates (`params.py`)

Go through `params.py` line by line and produce the complete updated file. Specific changes needed:

1. **Rename `sigma_xi` → `s_xi`** and change default from 0.30 → 0.15
2. **Add `Delta_S: float = 0.35`** (synergy facilitation parameter)
3. **Change `S_bar` default** from 0.60 → 1.44
4. **Update all docstrings** to reference Logistic distribution instead of Normal
5. **Update equation references** in docstrings (section numbers may have changed)
6. **Remove any `from scipy.stats import norm`** if it's only used for σ_ξ-related computations (check if it's used for signal distribution too — signal s is still Normal)
7. **Add a derived property for the net deterrence condition** (optional but useful for validation)

Show me the COMPLETE updated `params.py` file.

### Part 2: Core Model Rewrite (`model.py`)

This is the most critical file. Go through EVERY function and produce the complete updated version.

#### 2.1: `bid_probability()` (line 259-269) — CRITICAL REWRITE

**Current code (WRONG):**
```python
def bid_probability(m_XD: float, params: ModelParams) -> float:
    T = (m_XD + params.K - params.S_bar) / params.sigma_xi
    return float(norm.sf(T))
```

**What the paper says (Equation 8, line 256 of draft_v3.tex):**
```
p̃(X,D) = 1 - Λ( (V̂(X,D) + m̄(X,D) + K - (S̄ + π(X,D)·Δ_S)) / s_ξ )
```

where:
- V̂(X,D) = E[v|X,D] + Δ̃·π(X,D) is the standalone fundamental value
- m̄(X,D) = m₀ + (m̃ - m₀)·π(X,D) is the expected premium wedge
- Λ(·) is the standard logistic CDF: Λ(x) = 1/(1+exp(-x))
- So 1 - Λ(x) = 1/(1+exp(x)) = Λ(-x)

**Issues to fix:**
1. Function signature must accept `V_hat_XD`, `m_XD`, and `pi_XD` (or the full threshold components)
2. Replace `norm.sf(T)` with logistic survival: `1 / (1 + exp(T / s_xi))`
   - Note: `norm.sf(T)` = 1 - Φ(T), but we need 1 - Λ(T/s_ξ) where T is the RAW threshold (not yet divided by s_ξ)
   - Actually, the paper defines T(X,D) = (V̂ + m̄ + K - (S̄ + π·Δ_S)) / s_ξ, then p̃ = 1 - Λ(T)
   - So: `T = (V_hat_XD + m_XD + K - (S_bar + pi_XD * Delta_S)) / s_xi`
   - And: `p_tilde = 1 / (1 + exp(T))` (since 1 - Λ(T) = 1/(1+e^T) for standard logistic)
3. Add `Delta_S` synergy facilitation term: `S_bar + pi_XD * Delta_S`
4. Include V̂(X,D) in the threshold (currently missing entirely!)

**IMPORTANT SUBTLETY:** The standard logistic CDF is Λ(x) = 1/(1+e^{-x}), so:
- 1 - Λ(x) = e^{-x}/(1+e^{-x}) = 1/(1+e^x)
- Therefore `p_tilde = 1 / (1 + exp(T))` where T = threshold/s_xi

Produce the complete new `bid_probability()` function with updated signature, formula, and docstring.

#### 2.2: `compute_bidder_surplus_state()` (line 516-530) — CRITICAL REWRITE

**Current code (WRONG):**
```python
def compute_bidder_surplus_state(m_XD: float, params: ModelParams) -> float:
    T = m_XD + params.K - params.S_bar
    z = T / params.sigma_xi
    return params.sigma_xi * norm.pdf(z) - T * (1 - norm.cdf(z))
```

This uses the Normal truncated expectation formula E[max(ξ-T, 0)] for ξ ~ N(0, σ²).

**What it should be:** E[max(ξ - T, 0)] for ξ ~ Logistic(0, s_ξ).

For ξ ~ Logistic(0, s_ξ) with CDF Λ(x/s_ξ) and PDF λ(x/s_ξ)/s_ξ:

E[max(ξ - T, 0)] = ∫_T^∞ (x - T) · f(x) dx = s_ξ · ln(1 + exp(-T/s_ξ))

This is the **softplus function** applied to -T/s_ξ, scaled by s_ξ.

**Updated formula:**
```python
T_raw = V_hat_XD + m_XD + K - (S_bar + pi_XD * Delta_S)
return s_xi * log(1 + exp(-T_raw / s_xi))
```

Note the function signature must also change to accept the same arguments as `bid_probability()`.

Verify this derivation! The integral of (x-T)·f(x) from T to ∞ for logistic is a standard result. Double-check it.

#### 2.3: `compute_price_direct()` (line 272-287)

**Current code:**
```python
def compute_price_direct(E_v_XD, pi_XD, p_bid, m_XD, params):
    V_hat = E_v_XD + params.Delta_tilde * pi_XD
    return params.delta * (V_hat + p_bid * m_XD)
```

**Paper equation (Eq 10, line 443):**
```
P*(X,D) = δ · (V̂(X,D) + p(X,D) · m̄(X,D))
```

This looks correct IF `p_bid` is the unconditional probability (λ_B · p̃) and `m_XD = m̄(X,D)`. **Verify that the calling code passes the right values.** The formula itself appears aligned.

#### 2.4: `compute_equilibrium_prices()` (line 290-334)

Check every line. In particular:
- Line 328: `p_bid = params.lambda_B * bid_probability(m_XD, params)` — the call to `bid_probability` must be updated for the new signature
- The function must now pass `V_hat_XD`, `pi_XD` to `bid_probability()`
- V̂(X,D) is computed on line 286 inside `compute_price_direct` but also needed BEFORE calling `bid_probability`

#### 2.5: `compute_expected_payoff()` (line 337-439)

Go through ALL FOUR action branches (EXIT, HOLD, QUIET, PUBLIC) line by line:

- **EXIT (line 383-391):** Payoff is just +P(X,0). Verify this matches the paper. The EXIT branch doesn't involve takeover terminal values, so it should be fine.

- **HOLD (line 393-405):**
  - Line 399: `p_bid = params.lambda_B * bid_probability(m_XD, params)` — needs updated call
  - Line 403: `expected_terminal = p_bid * (V_hat_XD + params.m0) + (1 - p_bid) * v_post` — verify against paper
  - Paper says: if bid, per-share payoff = V̂(X,D) + m^R(a=0) = V̂(X,D) + m₀ ✓
  - If no bid, per-share payoff = v + 0·Δ̃ = v ✓ (since a=0 for HOLD)

- **QUIET (line 407-419):**
  - Line 414: needs updated `bid_probability` call
  - Line 417: `expected_terminal = p_bid * (V_hat_XD + params.m_tilde) + (1 - p_bid) * (v_post + params.Delta_tilde)`
  - Paper says: if bid, payoff = V̂(X,D) + m^R(a=1) = V̂(X,D) + m̃... BUT WAIT — for Quiet Voice, a=1 is the ACTION but the REALIZED premium depends on whether engagement succeeded (ρ probability). Actually no — m̃ = m₀ + ρ(m₁-m₀) IS the expected premium conditional on a=1. And the paper defines m^R(a) as the realized premium...
  - **IMPORTANT:** The paper says (line 263): m^R(a) = m₀ + a·(m̃ - m₀). So for a=1: m^R(1) = m̃. This matches.
  - But verify: is the takeover payout V̂(X,D) + m^R(a) or V̂(X,D) + m̃? They're the same for a=1.
  - If no bid: payoff = v + Δ̃ (since a=1) ✓

- **PUBLIC (line 421-436):**
  - Line 428: `m_XD = params.m_tilde` — for D=1, π(X,1) = 1, so m̄ = m̃ ✓
  - Line 429: needs updated `bid_probability` call
  - Line 434: `expected_terminal = p_bid * 2 * (V_hat_XD + params.m_tilde) + (1 - p_bid) * 2 * (v_post + params.Delta_tilde)` — h=2 shares, each worth V̂+m̃ if bid ✓
  - Line 433: `trading_cf = -P` — buying 1 share at market price ✓

**For each branch, show the exact updated code.**

#### 2.6: `compute_minority_gains()` (line 445-500+)

- Updates needed for `bid_probability` call signature
- Show complete updated function

#### 2.7: `compute_welfare()` (line 533-595)

- Line 571: `surplus = params.lambda_B * compute_bidder_surplus_state(m_XD, params)` — needs updated signature
- Show complete updated function

#### 2.8: `compute_bidder_surplus_state()` as discussed in 2.2

#### 2.9: ALL remaining functions

Go through EVERY OTHER function in model.py. For each one, state:
- Whether it needs changes (and what)
- OR confirm it is unchanged and why

Include: `noise_probs`, `engagement_cost`, `v_hat`, `compute_action_probabilities`, `compute_conditional_means`, `compute_posteriors`, `compute_E_v_given_XD`, and any other functions I may have missed.

#### 2.10: Import changes

- Remove `from scipy.stats import norm` IF it's only used for bid probability / bidder surplus (NOT for signal distribution)
- Actually, `norm` is still needed for the signal distribution (s ~ N(μ, σ_s)), so it stays
- But add `from scipy.special import expit` if you want to use `expit` for the logistic CDF (optional — can also use `1/(1+exp(-x))`)
- Or just compute logistic CDF inline

### Part 3: Solver Updates (`solver.py`)

Go through `solver.py` function by function. The solver structure (damped fixed-point iteration) should be largely unchanged since it operates on cutoffs, but:

1. Any calls to `model.bid_probability()` must be updated for new signature
2. Any references to `sigma_xi` must become `s_xi`
3. Check `_compute_residuals()` — this evaluates payoff differences and may call model functions
4. Check convergence criteria — are they still appropriate?
5. Check the multi-start search and collapsed-hold fallback

Show ALL changes needed.

### Part 4: Export Data Updates (`export_data.py`)

1. Any references to `sigma_xi` in sweep grids or CSV column names → `s_xi`
2. Any calls to model functions with updated signatures
3. Check CSV column names — do any reference `sigma_xi`? If so, update to `s_xi`
4. Check the LaTeX table generators (`generate_table_example`, `generate_table_disclosure_extensions`) for references to old parameters
5. Check sensitivity sweep ranges — are the sweep ranges for `s_xi` appropriate given the new default of 0.15?

Show ALL changes needed, with exact old → new code.

### Part 5: Accelerator Rewrite (`accel.py`)

`accel.py` is currently DISABLED (`HAS_NUMBA = False` in solver.py) but is completely out of sync. It still uses:
- Old noise probabilities: `p0 = 1.0 - kappa`, `p1 = kappa / 2.0`
- Old bid probability formula with P inside: `T = (m_XD + K - S_bar + P) / sigma_xi`
- Old iterative fixed-point pricing (the recursive approach that was eliminated)
- Normal CDF for bid probability

**Options:**
1. Full rewrite to match new theory
2. Delete entirely (since it's disabled and solver.py is the reference implementation)

I lean toward option 2 (delete) but want your recommendation based on codebase analysis. If you recommend keeping it, provide the COMPLETE rewritten file.

### Part 6: R Visualization Updates (`05_R_VISUALIZATION.md`)

Check ALL 13 R figure scripts for:
1. **CSV column name changes**: If `sigma_xi` → `s_xi` in exports, R scripts reading those columns must update
2. **Axis labels**: Any labels referencing σ_ξ should become s_ξ
3. **Parameter references in plot titles or annotations**
4. **Sensitivity plots**: `plot_fig11_sensitivity_sigma_xi.R` — this entire script may need renaming and updating

For each R script, state whether changes are needed and show the exact modifications.

### Part 7: Calibration Verification

After all code changes, verify the calibration table matches. The paper's Table C.3 (line 1296 of draft_v3.tex) states:

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Prior mean | μ | 1.00 |
| Fundamental volatility | σ_v | 0.50 |
| Signal noise | σ_ε | 0.50 |
| Base engagement cost | C₀ | 0.12 |
| Cost sensitivity | χ | 0.50 |
| Success probability | ρ | 0.90 |
| Value improvement | Δ | 0.25 |
| Base premium | m₀ | 0.10 |
| Activism premium | m₁ | 0.30 |
| **Baseline synergy** | **S̄** | **1.44** |
| **Synergy improvement** | **Δ_S** | **0.35** |
| **Bidding cost** | **K** | **0.15** |
| **Synergy scale (Logistic)** | **s_ξ** | **0.15** |
| **Bidder arrival rate** | **λ_B** | **0.05** |
| Discount factor | δ | 0.95 |
| Noise intensity | κ | 0.50 |

**Bold entries are new or changed.**

The paper also states (line 1296 caption): "Cutoffs: k₁ = k₀ ≈ 0.82 and k_D ≈ 2.26"

**After your code changes, can you verify (by hand calculation or reasoning) that these cutoff values are plausible given the new calibration?** The old code with old parameters produced different cutoffs. The new parameters should produce the stated cutoffs.

### Part 8: Assumption Verification

Verify that Assumption (A5) holds with the baseline calibration:
- Δ̃ + m̃ - m₀ > Δ_S
- Δ̃ = ρ·Δ = 0.9 × 0.25 = 0.225
- m̃ = m₀ + ρ·(m₁ - m₀) = 0.10 + 0.9 × 0.20 = 0.28
- LHS = 0.225 + 0.28 - 0.10 = 0.405
- RHS = Δ_S = 0.35
- 0.405 > 0.35 ✓

### Part 9: Build Pipeline Test Plan

After all changes, the pipeline should run:
```bash
make clean && make all
```

Which executes:
1. `python -m numerical.export_data --output-dir numerical_output` → 13 CSVs
2. `Rscript R/render_all.R --data-dir numerical_output/data --output-dir numerical_output` → 13 PDFs

Describe a test plan:
1. What should I check in the CSV outputs? (column names, value ranges, no NAs except at extreme κ)
2. What should I check in the PDF figures? (axes, labels, curve shapes, non-degenerate ranges)
3. Any sanity checks on specific values? (e.g., at κ=0.5, bid probability should be ≈?)

---

## Deliverables Summary

I need you to produce, in this exact order:

1. **Complete updated `params.py`** — full file, copy-pasteable
2. **Complete updated `model.py`** — full file, copy-pasteable, every function audited
3. **Complete updated `solver.py`** — full file if changes needed, or a precise diff
4. **Complete updated `export_data.py`** — full file if changes needed, or a precise diff
5. **Decision + action on `accel.py`** — delete or complete rewrite
6. **R script changes** — exact diffs for each affected file
7. **Calibration verification** — hand-check that baseline params produce plausible equilibrium
8. **Test plan** — what to verify after running `make clean && make all`

For each file, show the COMPLETE updated version. Do not show partial snippets. Do not say "rest unchanged." Show every line.

**Reminder: MAXIMUM VERBOSITY. Every function. Every line. No shortcuts.**

---

## Mathematical Reference Card

For quick reference, here are the key formulas from draft_v3.tex that the code must implement:

### Noise Distribution (Definition 1)
```
P(z = 0) = 1 - 2κ/3
P(z = +1) = P(z = -1) = κ/3
```

### Bid Probability (Equation 8)
```
T(X,D) = (V̂(X,D) + m̄(X,D) + K - (S̄ + π(X,D)·Δ_S)) / s_ξ

p̃(X,D) = 1 - Λ(T(X,D)) = 1 / (1 + exp(T(X,D)))

p(X,D) = λ_B · p̃(X,D)
```

### Standalone Fundamental Value
```
V̂(X,D) = E[v|X,D] + Δ̃ · π(X,D)
```

### Expected Premium Wedge
```
m̄(X,D) = m₀ + (m̃ - m₀) · π(X,D)
```

### Pricing (Equation 10)
```
P*(X,D) = δ · (V̂(X,D) + p(X,D) · m̄(X,D))
```

### Bidder Expected Surplus (for ξ ~ Logistic(0, s_ξ))
```
E[max(ξ - T_raw, 0)] = s_ξ · ln(1 + exp(-T_raw / s_ξ))

where T_raw = V̂(X,D) + m̄(X,D) + K - (S̄ + π(X,D)·Δ_S)
```

### Terminal Payoff per Share
```
Y = 𝟙{bid} · (V̂(X,D) + m^R(a)) + (1 - 𝟙{bid}) · (v + a·Δ̃)

where m^R(a) = m₀ + a·(m̃ - m₀)
```

### Bid Deterrence Derivative (Equation in §4.8)
```
∂p̃/∂π = -Λ'(T) · (Δ̃ + (m̃ - m₀) - Δ_S) / s_ξ < 0    (under A5)
```

---

_Internal: snapshot_sha=4c63de2, round=1, date=2026-03-03_
