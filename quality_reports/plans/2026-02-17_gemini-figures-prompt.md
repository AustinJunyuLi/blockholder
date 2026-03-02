# Gemini Deep Think Prompt: Numerical Code + Figure-Referenced Prose

## INSTRUCTIONS FOR GEMINI

You previously reviewed the paper "Liquidity, Activism Disclosure, and Takeover Premia" and provided D1-D14 surgical revisions. Those text revisions have now been implemented into `draft_v2.tex` (attached as PDF). The notation streamlining (D13) is complete: `m(a)` is now `m^{R}(a)`, `m(X,D)` is now `\bar{m}(X,D)`, etc.

The prose from D10, D11, and D12 describes numerical patterns (sensitivity sweeps over rho, sigma_xi, delta; noisy rumor precision flattening; welfare decomposition) but the corresponding **figures do not yet exist** and the prose does **not yet reference them by figure label**. Your task is to write the complete code for these figures and the surgical LaTeX edits to connect them to the prose.

You are given:
1. **draft_v2.pdf** -- the current compiled paper (45 pages)
2. **Figures diagnosis** -- a gap analysis identifying exactly what is missing (included below)
3. **All numerical code** (5 Python files, attached):
   - `numerical/params.py` (172 lines) -- ModelParams dataclass, Action enum, Cutoffs/MinorityGains tuples
   - `numerical/model.py` (714 lines) -- Core economic functions: posteriors, prices, payoffs, minority gains
   - `numerical/solver.py` (472 lines) -- Equilibrium solver, kappa sweeps
   - `numerical/figures.py` (884 lines) -- All current figure-generating functions
   - `numerical/accel.py` (1062 lines) -- Numba-accelerated solver (optional performance layer; the pure-Python solver.py is the reference implementation)

---

## WHAT YOU MUST PRODUCE

### Part 1: New Python Code (5 deliverables)

For each deliverable, provide the **complete function** that can be inserted into `figures.py` (or `model.py` where noted). Follow the existing code patterns exactly:
- Same signature style: `(base_params: ModelParams, save_path: Optional[str] = None)`
- Same plotting style: `fig, ax = plt.subplots(figsize=(5.5, 3.8))`, seaborn muted palette
- Same sweep pattern: `np.linspace(0.25, 0.85, 21)` for kappa grid
- Same error handling: try/except with `np.nan` fallback
- Use `SENSITIVITY_STYLES` from figures.py for multi-curve plots
- All text uses LaTeX math rendering (matplotlib's `$...$`)

**F1. `plot_sensitivity_rho(base_params, save_path)`**
- Sweep `rho` in {0.5, 0.7, 0.9} (baseline is 0.9)
- For each rho, sweep kappa and compute Delta^min via `solve_valid()` + `compute_minority_gains()`
- Use `base_params.replace(kappa=..., rho=rho)` to vary parameters
- Y-axis: Expected Minority Takeover Gains
- The theory predicts: lowering rho flattens the hump but preserves the qualitative shape. The peak compresses vertically.

**F2. `plot_sensitivity_sigma_xi(base_params, save_path)`**
- Sweep `sigma_xi` in {0.25, 0.40, 0.60} (baseline is 0.40)
- Use `base_params.replace(kappa=..., sigma_xi=sigma_xi)`
- The theory predicts: higher sigma_xi shifts the entire curve upward (more bid incidence) while preserving the hump shape. Also note that higher sigma_xi relaxes Assumption (A5).

**F3. `plot_sensitivity_delta(base_params, save_path)`**
- Sweep `delta` in {0.85, 0.90, 0.95} (baseline is 0.95)
- Use `base_params.replace(kappa=..., delta=delta)`
- The theory predicts: lower delta shifts the curve downward and slightly leftward (engagement harder to sustain at high kappa).

**F4. `plot_noisy_rumor_precision(base_params, save_path)`**
- This is more complex. The model already has `compute_posteriors_noisy_rumor()` and `compute_premium_wedges_noisy_rumor()` in model.py that compute posteriors for a given (kappa, rho1, rho0) at fixed cutoffs.
- Sweep three rumor precision levels: uninformative (eta_1 = eta_0 = 0.5), moderate (eta_1=0.75, eta_0=0.25), precise (eta_1=0.95, eta_0=0.05).
- For each precision level, sweep kappa and compute Delta^min.
- **Key implementation detail**: The noisy rumor changes the information environment but NOT the equilibrium cutoffs (it is a partial-equilibrium exercise holding the blockholder's strategy fixed at baseline). So:
  1. Solve baseline equilibrium at each kappa to get (k1, k0, kD)
  2. Compute action probabilities from those cutoffs
  3. Compute noisy-rumor posteriors using `compute_posteriors_noisy_rumor()`
  4. Compute minority gains by iterating over (action, z, R) states with the noisy-rumor posteriors and the rumor-augmented prices
- You may need to write a helper function `compute_minority_gains_noisy_rumor(k1, k0, kD, params, eta_1, eta_0)` in model.py. This parallels `compute_minority_gains()` but uses the (X, D, R) state space instead of (X, D), marginalizing over the rumor signal R.
- The theory predicts: as rumor precision increases (eta_1 - eta_0 grows), the Delta^min(kappa) curve flattens, confirming that any mechanism shifting engagement from inferred to observable attenuates liquidity sensitivity.

**F5. `plot_welfare(base_params, save_path)` + `compute_welfare(k1, k0, kD, params)` in model.py**
- This requires computing three welfare components:
  - W_min = Delta^min (already computed by `compute_minority_gains()`)
  - W_bid = E[max(Pi_B, 0)] (bidder expected surplus)
  - W_B = E[U(q*, a* | s)] (blockholder expected utility)
- **Bidder surplus** (`compute_bidder_surplus`): For each (X, D) state, the bidder's expected surplus is the truncated normal expectation: integrate max(xi - threshold, 0) * phi(xi/sigma_xi) over xi, weighted by state probabilities.
- **Blockholder surplus**: Use the already-computed `compute_expected_payoff()` function in model.py (line 306), which gives U(q,a|s). Integrate this over the signal distribution s using the equilibrium strategy (Exit if s<k1, Hold if k1<s<k0, Quiet if k0<s<kD, Public if s>kD).
- Plot W_min(kappa), W_bid(kappa), and W_total(kappa) on the same axes.
- Mark kappa^dagger (peak of W_min) and kappa* (peak of W_total) with vertical dashed lines.
- The theory predicts: W_total(kappa) is also hump-shaped, but kappa* > kappa^dagger because bidders prefer higher liquidity (lowers acquisition cost). The gap between kappa* and kappa^dagger illustrates the tension between minority protection and allocative efficiency.

### Part 2: Updated `generate_all_figures()` Orchestrator

Provide the updated orchestrator function that calls all 5 new figure functions (Figures 9-13) inside the `if include_sensitivity:` block, following the existing pattern.

### Part 3: Surgical LaTeX Prose Edits (5 deliverables)

For each edit, provide the **exact old text** to search for and the **exact new text** to replace it with, so that my assistant can perform mechanical find-and-replace. Use the ACTUAL citation keys from bibliography.bib (NOT short keys). Use the new notation (m^{R}(a), \bar{m}(X,D), etc.).

**CRITICAL FORMATTING RULES:**
- NEVER use em dashes (---). Use commas, semicolons, colons, or parentheses instead.
- Use `\textup{}` for upright text in math mode (not `\mathrm{}`).
- Use `\E[...]` for expectations (custom macro already defined).
- Use `\1{...}` for indicator functions (custom macro already defined).
- Use `\PP(...)` for probabilities (custom macro already defined).
- Cross-references: `Figure~\ref{fig:label}`, `Proposition~\ref{prop:label}`, `Section~\ref{sec:label}`

**L1. Add figure references in D10 sensitivity text** (around lines 639-645 of draft_v2.tex)
- Insert `Figure~\ref{fig:sensitivity-rho}` reference in the rho paragraph
- Insert `Figure~\ref{fig:sensitivity-sigma-xi}` reference in the sigma_xi paragraph
- Insert `Figure~\ref{fig:sensitivity-delta}` reference in the delta paragraph
- Each insertion should be a single sentence or clause woven into the existing text.

**L2. Add figure reference in D11 noisy rumors text** (around line 778)
- Insert `Figure~\ref{fig:noisy-rumor-precision}` reference in the numerical analysis paragraph
- The existing text says "Numerical analysis of this regime reveals that as the rumor becomes more precise..."

**L3. Add figure reference in D12 welfare text** (around lines 810-812)
- Insert `Figure~\ref{fig:welfare}` reference where the text discusses W(kappa) being hump-shaped and kappa* differing from kappa^dagger

**L4. Add 5 new figure float blocks in Appendix C**
- These go after the last existing figure float (fig:sensitivity-wedge, currently at line ~1327)
- Each block follows this template:
```latex
\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/FILENAME.pdf}
\caption{CAPTION TEXT.}
\label{fig:LABEL}
\end{figure}
```
- Write substantive captions (2-3 sentences) that describe what the figure shows and its economic interpretation.

**L5. (If needed) Any other prose adjustments** to ensure the discussion of numerical results accurately matches what the figures will show, given the theoretical predictions.

---

## OUTPUT FORMAT

Structure your response as follows. Use fenced code blocks for all code and LaTeX.

```
=== F1: plot_sensitivity_rho ===
[Complete Python function]

=== F2: plot_sensitivity_sigma_xi ===
[Complete Python function]

=== F3: plot_sensitivity_delta ===
[Complete Python function]

=== F4: plot_noisy_rumor_precision ===
[Complete Python function for figures.py]
[Complete helper function for model.py, if needed]

=== F5: plot_welfare + compute_welfare ===
[Complete compute_welfare/compute_bidder_surplus functions for model.py]
[Complete plot_welfare function for figures.py]

=== F6: Updated generate_all_figures() ===
[The FULL updated function, not a diff]

=== L1: D10 figure references ===
OLD: [exact text to find]
NEW: [exact replacement text]
(repeat for each edit in D10)

=== L2: D11 figure reference ===
OLD: [exact text to find]
NEW: [exact replacement text]

=== L3: D12 figure reference ===
OLD: [exact text to find]
NEW: [exact replacement text]

=== L4: Appendix figure floats ===
[Complete LaTeX for all 5 new figure floats]

=== L5: Additional prose adjustments ===
OLD: [exact text]
NEW: [exact replacement text]
(if any)
```

---

## FIGURES DIAGNOSIS (from code review)

### Existing Figures (complete, no changes needed)
1. fig:timeline -- TikZ inline
2. fig:cutoff-structure -- plot_cutoff_structure()
3. fig:nonmonotone -- plot_nonmonotonicity()
4. fig:decomposition -- plot_decomposition()
5. fig:prices -- plot_prices()
6. fig:cutoffs-kappa -- plot_cutoffs_vs_kappa()
7. fig:disclosure -- plot_disclosure_attenuation()
8. fig:sensitivity-C0 -- plot_sensitivity_C0()
9. fig:sensitivity-wedge -- plot_sensitivity_premium_wedge()

### New Figures Required
| Figure | Output File | Complexity | Key Dependency |
|---|---|---|---|
| Sensitivity rho | fig_sensitivity_rho.pdf | Low | params.replace(rho=...) |
| Sensitivity sigma_xi | fig_sensitivity_sigma_xi.pdf | Low | params.replace(sigma_xi=...) |
| Sensitivity delta | fig_sensitivity_delta.pdf | Low | params.replace(delta=...) |
| Noisy rumor precision | fig_noisy_rumor_precision.pdf | Medium | compute_posteriors_noisy_rumor() exists; need minority gains under rumor regime |
| Welfare decomposition | fig_welfare.pdf | High | Need new compute_welfare() + compute_bidder_surplus() |

### Key Existing Functions to Build On
- `solve_valid(params, prev_cutoffs)` -- returns (Cutoffs, residual) or (None, inf)
- `compute_minority_gains(k1, k0, kD, params)` -- returns MinorityGains(total, base, activism)
- `compute_posteriors_noisy_rumor(omega_E, omega_H, omega_Q, omega_P, kappa, rho1, rho0)` -- returns dict keyed by (X, D, R)
- `compute_expected_payoff(action, s, k1, k0, kD, params)` -- returns expected payoff for a given action and signal
- `bid_probability(P, m_XD, params)` -- returns Phi-based bid probability
- `SENSITIVITY_STYLES` -- list of dicts with linestyle/color/marker for multi-curve plots

### ModelParams Fields (for parameter sweeps)
```python
rho: float = 0.9       # Engagement success probability
sigma_xi: float = 0.40 # Synergy shock volatility
delta: float = 0.95    # Discount factor
kappa: float = 0.5     # Noise trading intensity (swept on x-axis)
C0: float = 0.12       # Engagement cost
m0: float = 0.10       # Base premium
m1: float = 0.30       # Premium with engagement
# Derived: m_tilde = m0 + rho*(m1-m0), Delta_tilde = rho*Delta
# Method: params.replace(kappa=0.3, rho=0.7) returns a new ModelParams
```
