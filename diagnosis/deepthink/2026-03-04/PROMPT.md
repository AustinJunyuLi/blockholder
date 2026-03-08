# Theory Repair Request — EVT Model (Round 4)

**Date:** 2026-03-04
**Commit:** 4c63de2 (theory-fixes branch, post-Anonymous Accumulation implementation)
**Files uploaded:** 9 consolidated files covering full manuscript + Python codebase + verification data
**Round focus:** Repairing Lemma 2, Proposition 5, and secondary theory gaps identified by independent audit

## How to Read the Uploaded Files

| File | Contents | Size |
|------|----------|------|
| 00_PROJECT_OVERVIEW.md | Project identity, architecture, model concepts | 3 KB |
| 01_MANUSCRIPT.md | Full LaTeX manuscript (`draft_v3.tex`, 1462 lines) | 135 KB |
| 02_PYTHON_MODEL.md | Core model (`numerical/model.py`) — posteriors, prices, payoffs, welfare | 26 KB |
| 03_PYTHON_INFRASTRUCTURE.md | `params.py` (calibration) + `solver.py` (fixed-point) | 17 KB |
| 04_NUMERICAL_VERIFICATION.md | **Independent verification data** — kappa sweeps proving the issues are real | 5 KB |
| 05_GPT_PRO_AUDIT.md | **External audit** that identified the issues (full text) | 17 KB |
| 06_PREVIOUS_ROUNDS.md | Summary of Rounds 1–3.5 and what was fixed | 3 KB |
| 07_KEY_DATA.md | CSV outputs: baseline series, prices, disclosure, welfare | 8 KB |
| 08_SUPPORTING.md | Makefile, `export_data.py`, `bibliography.bib` | 26 KB |

Each file contains concatenated source with `## path/to/file` headers.
**Read files 04 and 05 first** — they contain the issues this round must fix and the evidence proving them real.

---

## Ground Rules

**ON INTELLECTUAL HONESTY:**

I am a serious academic researcher. I need your **honest, independent judgment** — not agreement, not flattery, not validation.

1. **Do NOT open with compliments.** Go straight to substance.
2. **Challenge my analysis if you disagree.** If the issues below are not actually problems, explain why. If there are additional problems I missed, flag them.
3. **Distinguish confidence levels.** "I am confident that X" vs "I suspect Y" vs "Z is speculative."
4. **Prioritize correctness over my feelings.** This is a job market paper targeting a top-5 journal.

**ON VERBOSITY AND DETAIL:**

1. **Do NOT abbreviate.** Complete proofs with every algebraic step.
2. **Do NOT provide proof sketches.** Camera-ready LaTeX.
3. **Show ALL algebra.** Every derivative, every substitution.
4. **Your response should be VERY LONG.** The cost of verbosity is zero. The cost of a proof gap is a desk reject.

---

## Context: What Happened in Rounds 1–3.5

- **Rounds 1–2:** Identified and fixed 7 theoretical proof gaps (T1–T7). Recalibrated parameters.
- **Round 3:** Diagnosed the "front-running pathology" — Public Voice was off-path because the blockholder paid the fully inflated post-disclosure price. Proposed the **Anonymous Accumulation** fix: the blockholder trades at `P_trade(X)` before disclosure `D` is revealed.
- **Round 3.5:** Provided exhaustive theoretical rewrite incorporating Anonymous Accumulation. All proofs rewritten with the two-price structure (`P_trade(X)` and `P_post(X,D)`).

**The Anonymous Accumulation fix is fully implemented** in both the manuscript (`draft_v3.tex`) and the Python code. Public Voice is now on-path with ω_P ≈ 23–36% across κ values. The cutoff k_D is at ≈1.5 (reasonable, ~0.7σ above μ).

---

## What This Round Addresses

An independent external theory audit (by a separate AI model reviewing `draft_v3.tex` in its entirety) identified **two critical failures** and **four secondary issues** in the current manuscript. I have independently verified all claims against both the manuscript text and numerical output. **Every issue below is confirmed valid.**

---

## P0 — CRITICAL: Lemma 2 Right-Endpoint Argument Is Mathematically Wrong

### What Lemma 2 Currently Claims (lines 1268–1269 of `draft_v3.tex`)

> "As κ→1, noise trading converges to a perfect uniform distribution... Order flow X=q+z becomes completely uninformative about the blockholder's underlying trade q. The Bayesian posteriors π(X,0) perfectly converge to the unconditional prior ω_Q/(ω_E+ω_H+ω_Q) across all nondisclosed states."

It then concludes: voice regions collapse (ω_Q+ω_P→0), Δ_act(κ)→0, and Δ_min(κ)→m₀·P(bid).

### Why This Is Wrong (Three Independent Proofs)

**Proof 1: Direct contradiction with Proposition 2.**
Proposition 2 (line 407) gives: π(1,0) = ω_Q/(ω_H+ω_Q). This expression does NOT contain κ. Appendix B.8 (line 1164) explicitly confirms ∂π(1,0)/∂κ = 0. Therefore π(1,0) CANNOT converge to the unconditional prior ω_Q/(ω_E+ω_H+ω_Q) unless ω_E→0, which is not proven and not generally true.

At κ=1: p₀=p₁=1/3. Substituting into the posterior formulas:
- π(-1,0) = ω_Q·(1/3) / [(ω_H+ω_Q)·(1/3) + ω_E·(1/3)] = ω_Q/(ω_E+ω_H+ω_Q) ✓
- π(0,0) = ω_Q·(1/3) / [(ω_H+ω_Q)·(1/3) + ω_E·(1/3)] = ω_Q/(ω_E+ω_H+ω_Q) ✓
- π(1,0) = ω_Q/(ω_H+ω_Q) ✗ (Does NOT equal ω_Q/(ω_E+ω_H+ω_Q))

So π(-1,0) and π(0,0) DO converge to the unconditional D=0 prior at κ=1, but π(1,0) does NOT. The claim "across all nondisclosed states" is false.

**Proof 2: Bounded support precludes "completely uninformative."**
With z ∈ {-1, 0, +1} and q ∈ {-1, 0, +1}, even at κ=1 (uniform noise), extreme order flows remain revealing: X=2 ⇒ q=+1, X=-2 ⇒ q=-1. Within D=0 states, X=1 mechanically reveals q=0 (since Exit has q=-1 and can only produce X ∈ {-2,-1,0}). This is structural, not parametric — bounded discrete support cannot become "completely uninformative."

**Proof 3: Numerical falsification.**
I computed the equilibrium at high κ values under the current (post-Anonymous-Accumulation) model:

| κ | ω_Q | ω_P | ω_Q+ω_P | π(1,0) | π(-1,0) | Uncond prior | Δ_act |
|---|-----|-----|---------|--------|---------|-------------|-------|
| 0.50 | 0.142 | 0.227 | 0.369 | 0.295 | 0.086 | 0.184 | 0.00190 |
| 0.85 | 0.081 | 0.286 | 0.367 | 0.236 | 0.089 | 0.114 | 0.00125 |
| 0.95 | 0.069 | 0.299 | 0.368 | 0.215 | 0.090 | 0.098 | 0.00081 |
| 0.99 | 0.000 | 0.362 | 0.362 | 0.000 | 0.000 | 0.000 | 0.00020 |

Key observations:
1. **Voice does NOT collapse.** Total voice (ω_Q+ω_P) stays at ~36% across all κ.
2. **Voice SHIFTS from Quiet to Public.** At high κ, noise camouflages the buy order, making Public Voice cheaper relative to Quiet Voice.
3. **π(1,0) ≠ unconditional prior** at any κ where ω_Q > 0 and ω_E > 0.
4. **Δ_act shrinks but does NOT reach zero.** At κ=0.99, Δ_act = 0.00020 (driven by D=1 disclosed component).
5. At κ≥0.63, Quiet Voice collapses (k₀ = k_D), producing a two-cutoff equilibrium (Exit/Hold/Public). In this regime, π(X,0) = 0 trivially (no quiet engagement exists), but ω_P ≈ 36%.

### What the Correct Right-Endpoint Behavior Is

As κ→1 in the current model:
- **Quiet Voice collapses** (ω_Q→0) because the stealth advantage of quiet engagement disappears when noise already camouflages Public Voice trades.
- **Public Voice survives and grows** (ω_P→~36%) because anonymous accumulation at P_trade(X) remains profitable.
- **The inferred component of Δ_act vanishes** (because ω_Q=0 means no quiet engagement to infer on D=0 branch).
- **The disclosed component of Δ_act stays positive but small** (because at D=1, π=1, and net deterrence A5 drives bid probability very low).
- **Δ_act → small positive constant** (NOT zero).
- **Δ_min → Δ_base + small_Δ_act** (NOT m₀·P(bid)).

### Why This Matters

The standard microstructure intuition (per GPT Pro's observation) is that more noise INCREASES informed trading rents (better camouflage), not decreases them. The paper's current narrative — "stripped of ability to extract adverse-selection rents" at high κ — runs against this logic. In fact, the numerics confirm that higher κ makes Public Voice MORE attractive (ω_P increases monotonically), which is consistent with the standard Kyle intuition.

---

## P0b — CRITICAL: Proposition 5 Nonmonotonicity Proof Fails

### Current Proof Structure (Appendix B, lines 1272–1281)

1. Uses Lemma 2 for right-endpoint: Δ_min(1) = m₀·P(bid).
2. Uses Jensen's inequality: f(π) = p̃(π)·(m₀ + π(m̃−m₀)) is concave, so maximal dispersion of π at κ→0 minimizes E[f(π)].
3. Concludes: both endpoints are depressed, interior must be higher.

### Why It Fails

**Problem 1:** Lemma 2's right-endpoint claim is wrong (established above). Δ_min does NOT converge to m₀·P(bid).

**Problem 2:** Even if Lemma 2 were correct, the Jensen argument is not rigorous because:
- The distribution of π(X,D) is ENDOGENOUS — cutoffs change with κ, which changes the ω's, which changes the π's.
- Changes in κ cannot be cleanly modeled as a mean-preserving spread in π because the mean itself shifts (the ω weights change).
- The function f(π) is evaluated at endogenous posterior values, not at exogenous points.

### What the Numerics Show

The hump IS real:
- Δ_min peaks at κ ≈ 0.24 with value ≈ 0.00864
- Δ_min at κ→0 is ≈ 0.00810 (left endpoint)
- Δ_min at κ→1 is ≈ 0.00778 (right endpoint)
- Amplitude: ~10% above endpoints

The mechanism: Δ_base (bid probability × m₀) is monotonically INCREASING in κ. Δ_act (activism-driven premium) is monotonically DECREASING. The hump in Δ_min is the sum of these opposing forces.

### What Is Needed

A correct proof (or honest acknowledgment that the result is numerically established with analytical support but not a closed-form theorem). Two viable routes:

**Route A: Correct analytical proof.** Establish correct endpoint behavior (both left and right), then show the interior must be higher. The key challenge is characterizing the right endpoint without the false "voice collapse" claim.

**Route B: Numerically verified theorem.** State the result as analytically motivated and numerically verified, following the precedent of Edmans-Goldstein-Jiang (2015) for uniqueness verification. The Jensen/concavity intuition can be preserved as economic motivation, but the formal proof should not rely on the false endpoint convergence.

---

## P1 — IMPORTANT: Premium Interpretation Inconsistency

### The Problem

Line 231 of `draft_v3.tex`:
> "I interpret m₀ and m₁ as per-share takeover premia above the market price (so the consummated offer satisfies b=P+m)."

But line 247–251:
> "The bidder anchors their takeover offer to the target's expected standalone fundamental value... b(X,D) = V̂(X,D) + m̄(X,D)."

These are inconsistent:
- b = P + m implies premium over TRADING PRICE (creates a fixed-point / recursion — the exact pathology that Anonymous Accumulation was designed to avoid).
- b = V̂ + m̄ implies premium over FUNDAMENTAL VALUE (the actual feed-forward structure).

The model uses the second interpretation. The first interpretation is a holdover from pre-Anonymous-Accumulation text.

### Fix Required

Change line 231 to interpret m₀ and m₁ as premia over the estimated standalone fundamental value, not the market price. Ensure ALL text referencing the premium interpretation is consistent with the feed-forward b = V̂ + m̄ structure.

---

## P2 — IMPORTANT: λ_B < 1/2 Must Be a Formal Assumption

### The Problem

Line 973 of `draft_v3.tex`:
> "Because the unconditional bid probability is structurally bounded by the bidder arrival rate (p(X,D) ≤ λ_B), and empirical calibrations ensure λ_B < 0.5, we are mathematically guaranteed that 2p(X,1) < 1."

This is used to establish the single-crossing property for the Quiet-vs-Public Voice boundary (B_P − B_Q > 0). It is a necessary condition for the monotone cutoff equilibrium structure (Proposition 1).

### Why This Is a Problem

"Empirical calibrations ensure" is not a formal theoretical assumption. A referee can legitimately ask: what happens when λ_B ≥ 0.5? The single-crossing argument breaks down. This is a knife-edge condition hidden inside a proof.

### Fix Required

Either:
**(A)** Add a formal assumption: (A7) λ_B < 1/2. Interpret: the unconditional probability of a bidder arriving is below 50%, which is empirically uncontroversial.
**(B)** Provide a more general sufficient condition that does not require λ_B < 1/2, using the structure of the model.

---

## P3 — MODERATE: Tighten Lemma 1 (QA Domination)

### The Problem

Lemma 1 claims that Quiet Accumulation (q=+1, a=0) — buying without engaging — is strictly dominated. The proof sketch is intuitive but not fully rigorous: it needs to establish that **for any type s that would ever choose q=+1, engagement is strictly optimal on h=2 shares.**

### Fix Required

Provide a rigorous proof. The cleanest approach:
- At any s where Public Voice is chosen (s ≥ k_D), the blockholder's gross engagement benefit on h=2 shares is 2δΔ̃, while the cost is C(s).
- Since k_D ≥ k₀ (the threshold where engagement on h=1 shares is profitable), and 2δΔ̃ > δΔ̃ (benefit doubles with stake), the net engagement benefit at s = k_D is strictly positive.
- For s > k_D, C(s) < C(k_D) (cost decreasing), so the result holds a fortiori.

Alternatively, add a simple sufficient condition: C₀ < 2δΔ̃, which ensures engagement is always profitable on 2 shares at any signal where buying is contemplated.

---

## P4 — MINOR: Rigor Leaks

### P4a: Appendix B.11 "by definition" language

Line 1221: "By definition, Δ_min(κ) = E[m̄(X,D) · 1{bid}]."

This is NOT "by definition." The definition is Δ_min = E[m^R(a) · 1{bid}] (line 536). Getting to the m̄(X,D) form requires an iterated expectations step: E[m^R(a)|X,D] = m̄(X,D), plus conditional independence of bid event and a given (X,D). This is a mathematical step, not a definition.

### P4b: Missing explicit P(D=d|X) formulas

The anonymous execution price P_trade(X) = Σ_d P(D=d|X) · P_post(X,d) uses conditional disclosure probabilities P(D=d|X). These should be given explicit formulas (or at least a line showing the Bayes calculation), especially for X ∈ {0, 1} where both D values are possible.

---

## Deliverables

### D1: Corrected Lemma 2

Provide a **complete replacement** for Lemma 2 and its proof (lines 552–556, 1255–1270). The new lemma must:
- Correctly characterize the left endpoint (κ→0): engagement survives, order flow is revealing, bid deterrence is maximal. This part of the existing proof is approximately correct.
- Correctly characterize the right endpoint (κ→1): Quiet Voice collapses but Public Voice survives. Δ_act → small positive constant (not zero). State exactly what happens to each posterior.
- NOT claim "order flow becomes completely uninformative" or "posteriors converge to the unconditional prior across all states."
- Be consistent with Proposition 2 (especially π(1,0) κ-invariance).

### D2: Corrected Proposition 5

Provide a **complete replacement** for Proposition 5 and its proof (lines 558–561, 1272–1281). Options:

**(A)** A correct analytical proof of nonmonotonicity that does not rely on the false right-endpoint voice collapse. One possible approach: show that Δ_base is monotonically increasing (more noise → more bids) and Δ_act is monotonically decreasing (more noise → quieter voice shrinks → less inference premium), and their sum has an interior maximum.

**(B)** A "numerically verified, analytically motivated" statement following the Edmans-Goldstein-Jiang (2015) precedent. State the analytical forces (opposing monotone components), cite Jensen/concavity as intuition, and verify the hump numerically.

### D3: Fixed Premium Interpretation

Provide replacement text for line 231 and any other lines where the premium is described as "above the market price." All premium language must be consistent with b = V̂ + m̄.

### D4: λ_B < 1/2 Formalization

Either add a new assumption (A7) or provide a general sufficient condition. Include the assumption statement, its placement in the assumption list, and any proof modifications needed.

### D5: Tightened Lemma 1

Provide the complete rigorous proof of QA domination.

### D6: Minor Fixes

Fix B.11 wording and add explicit P(D=d|X) formulas.

### D7: Updated Economic Narrative

The discussion paragraphs after Proposition 5 (lines 566–568) currently say "posteriors converge to the unconditional prior across all states, and prices flatten" at high κ. This must be rewritten to reflect the correct economics: Quiet Voice collapses but Public Voice survives; the inference channel on D=0 weakens but the D=1 branch carries non-negligible weight.

---

## Numerical Reference Data

For verification of your proposed fixes, the current model produces:

### Equilibrium at κ = 0.50
- Cutoffs: k₁ = 0.615, k₀ = 1.237, k_D = 1.529
- Probs: ω_E = 0.293, ω_H = 0.338, ω_Q = 0.142, ω_P = 0.227
- Gains: Δ_min = 0.00807, Δ_base = 0.00736, Δ_act = 0.00071

### Equilibrium at κ = 0.99
- Cutoffs: k₁ = 0.647, k₀ = 1.250, k_D = 1.250 (Quiet Voice collapsed)
- Probs: ω_E = 0.309, ω_H = 0.329, ω_Q = 0.000, ω_P = 0.362
- Gains: Δ_min = 0.00778, Δ_base = 0.00758, Δ_act = 0.00020

### Hump shape
- Peak Δ_min ≈ 0.00864 at κ ≈ 0.24
- Left limit (κ→0): Δ_min ≈ 0.00810
- Right limit (κ→1): Δ_min ≈ 0.00778
- Δ_base monotonically increasing: 0.00545 → 0.00758
- Δ_act monotonically decreasing: 0.00265 → 0.00020

---

## Output Format

For EACH deliverable, provide:

```latex
%% DELIVERABLE [Dn]: [Title]
%% REPLACES: lines [start]--[end] of draft_v3.tex
%% STATUS: [REWRITTEN / NEW]

[Complete LaTeX text, camera-ready, with full derivations]
```

After all deliverables, confirm:

1. [ ] Lemma 2 is consistent with Proposition 2 (π(1,0) κ-invariance respected)
2. [ ] Proposition 5 proof does not rely on "voice collapse" at κ→1
3. [ ] Premium interpretation is consistent throughout (b = V̂ + m̄, not b = P + m)
4. [ ] λ_B < 1/2 is formally assumed, not a calibration fact
5. [ ] Lemma 1 proof is complete (not a sketch)
6. [ ] No "by definition" claims that are actually theorems
7. [ ] Economic narrative matches the corrected theory

---

## What NOT to Change

- The information structure, noise specification, and action space are FINAL.
- The Anonymous Accumulation / Delayed Disclosure pricing structure is FINAL.
- Propositions 1–4 (cutoff structure, posteriors, price decomposition, existence) are correct and should NOT be modified (except for the λ_B < 1/2 formalization in Proposition 1's proof).
- The extensions (No Disclosure, Noisy Rumor) are correct.
- The numerical code is correct and should NOT be modified.

---

_Internal: branch=theory-fixes, round=4, date=2026-03-04_
