# Gemini Deep Think Round 2: Theory Repair + Recalibration

**Date:** 2026-03-03
**Model:** Gemini 2.5 Pro (Deep Think mode)
**Objective:** Fix remaining theoretical proof gaps AND propose parameter recalibration for the paper "Liquidity, Activism Disclosure, and Takeover Premia"

---

## Context

This is a single-author academic finance theory paper modeling a blockholder who chooses among four actions (Exit, Hold, Quiet Voice, Public Voice) based on a private signal, in a market with noise traders, a Bayesian market maker, and a potential acquirer. The paper's main result is that expected minority takeover gains are **nonmonotone** (hump-shaped) in market liquidity κ.

**What has been done so far:**
- Two rounds of GPT Pro review produced 14 deliverables (D1-D14) of prose revisions, all completed
- A comprehensive `fix.md` implementation plan was executed, producing `draft_v3.tex`
- The Python numerical code (`numerical/model.py`, `params.py`, `solver.py`, `export_data.py`) has been fully audited against `draft_v3.tex` — **all equations match exactly**
- The code is correct; the calibration produces degenerate economics
- A panel discussion (Claude + GPT-5.2) identified the key theoretical issues below

**Current model architecture (draft_v3.tex):**
- Bidder observes (X, D) directly (not price); arrival rate λ_B
- Bid probability: p(X,D) = λ_B · [1 - Λ(T/s_ξ)] where T = V̂(X,D) + m̄(X,D) + K - (S̄ + π·Δ_S) and Λ is the logistic CDF
- Feed-forward pricing: P*(X,D) = δ[V̂(X,D) + p(X,D)·m̄(X,D)] — no price fixed point
- Noise distribution: p₀ = 1 - 2κ/3, p₁ = κ/3 (fixes the parity flaw at κ→1)
- Synergy facilitation term Δ_S allows activism to increase bid probability through the channel (S̄ + π·Δ_S)
- Net deterrence condition (A5): Δ̃ + m̃ - m₀ > Δ_S ensures engagement still deters bids on net

---

## PART A: THEORETICAL PROOF GAPS

I have identified 7 issues of varying severity. Please address each one with a complete, rigorous fix.

### Issue T1: QA Domination Proof is Circular (CRITICAL)

**Location:** Lemma 1 (lem:qa-domination), Appendix B.1, lines 897-914

**Current proof:** Claims that under QA = (+1, 0), the blockholder triggers D=1, and therefore "the expected standalone value V̂(X,1), market price P*(X,1), and unconditional bid probability p(X,1) are identical for both QA and Public Voice P ≡ (+1, 1)."

**Problem:** This assumes the market's beliefs are unchanged when QA is played. But if QA were on-path with positive probability, then observing D=1 would NOT imply a=1 with certainty. The posterior π(X,1) would need to be updated to reflect the mixture of P and QA actions, changing V̂(X,1) and p(X,1). The proof treats off-equilibrium beliefs as identical to on-equilibrium beliefs — this is the circularity.

**What I need:** Either:
(a) A rigorous proof that handles off-path beliefs explicitly (e.g., using the D1 criterion, or proving QA is dominated for ALL belief specifications on D=1), or
(b) An honest restriction of the action space with economic justification (e.g., "buying shares without engaging is economically irrational because the cost of capital is sunk and engagement has positive NPV on 2 shares"), stated as an assumption

### Issue T2: B_{q,a} Definition Inconsistency (CRITICAL)

**Location:** Proof of Proposition 1 (cutoff structure), lines 939-957

**Current text:** Defines B_{q,a} ≡ δh · E_z[1-p(X,D)] at line 941, then claims "U(q,a|s) = A_{q,a} + B_{q,a}·v̂(s) - a·C(s)" at line 945.

**Problem:** Look at the actual payoff expression at line 936:
```
U(q,a|s) = E_z[-q·P*(X,D) + δh(p(X,D)·(V̂(X,D) + m^R(a)) + (1-p(X,D))·(v̂(s) + aΔ̃))] - a·C(s)
```

The v̂(s)-dependent part is indeed δh·E_z[(1-p(X,D))·v̂(s)], consistent with B_{q,a} = δh·E_z[1-p(X,D)].

But wait — V̂(X,D) = E[v|X,D] + Δ̃·π(X,D) also contains E[v|X,D], which is NOT v̂(s) but rather a weighted average of action-conditional means. The term δh·p(X,D)·V̂(X,D) contributes to A_{q,a} (the s-independent part), which is fine.

**The real inconsistency** is at line 957, where the proof claims B_P - B_Q = 2δ - δ = δ > 0. This would require B_{q,a} = δh·E_z[1-p(X,D)] where:
- For Q: h=1, so B_Q = δ·E_z[1-p(X,0)] ≈ δ·(1 - small number) ≈ δ
- For P: h=2, so B_P = 2δ·E_z[1-p(X,1)] ≈ 2δ·(1 - small number) ≈ 2δ

But Q and P have DIFFERENT disclosure states (D=0 vs D=1), so p(X,0) ≠ p(X,1) in general. The claim B_P - B_Q = δ only holds approximately when bid probabilities are small. With λ_B = 0.05 this is empirically true but the proof states it as exact ("structurally guaranteed").

**What I need:** Fix the proof to either:
(a) State the exact expression B_P - B_Q = 2δ·E_z[1-p(X,1)] - δ·E_z[1-p(X,0)] and show this is positive under A5 or reasonable conditions, or
(b) Reformulate the affine decomposition more carefully, noting that single-crossing of U_P - U_Q follows from a different argument (e.g., the engagement cost cancels and the remaining terms are increasing in s because of the h=2 ownership multiplier)

### Issue T3: Left Endpoint Proof Relies on Calibration (MAJOR)

**Location:** Lemma 2 (lem:endpoints), Appendix B.9, lines 1237-1248

**Current proof:** For κ↓0, claims "Under baseline calibrations, this benefit strictly exceeds the cost C(μ) at the prior mean, meaning the blockholder strictly prefers Quiet Voice to Hold for a given range of signals. Thus, the Quiet Voice region does not collapse (ω_Q > 0)."

**Problem:** A proof cannot invoke "baseline calibrations." This makes the lemma parameter-dependent rather than general. The lemma statement says "Under the Standing Assumptions" but the proof requires specific parameter values.

Moreover, the proof doesn't properly handle the fixed-point aspect: as κ→0, the equilibrium cutoffs themselves change, which changes ω_Q, which changes the posteriors, which changes the bid probabilities. The proof needs to show that the FIXED POINT of the cutoff mapping maintains ω_Q > 0, not just that the benefit exceeds cost at a particular point.

**What I need:** Either:
(a) Add a parametric sufficient condition (e.g., "Assume C₀ < δ·min(Δ̃, m̃ - m₀)") that guarantees ω_Q > 0 as κ→0 as a theorem, or
(b) Weaken the lemma to say "Under the Standing Assumptions and a parameter restriction ensuring engagement remains profitable at zero liquidity..." and state the restriction explicitly

### Issue T4: Nonmonotonicity Proof Assumes Its Conclusion (MAJOR)

**Location:** Proposition 4 (prop:nonmonotone), lines 552-559, Appendix B.10, lines 1253-1257

**Current statement:** "Assume the deterrence effect at κ→0 is sufficiently strong relative to an intermediate liquidity level κ̃ ∈ (0,1), such that Δ^min(κ̃) > lim_{κ↓0} Δ^min(κ). Then there exists an interior maximizer κ† ∈ (0,1)."

**Problem:** The proposition literally assumes what it wants to prove. The hypothesis "Δ^min(κ̃) > lim_{κ↓0} Δ^min(κ)" is just saying "the function is higher at some interior point than at the left endpoint" — which IS the nonmonotonicity. The Weierstrass argument then trivially gives an interior maximum.

A referee will immediately see this as vacuous. The real work is in establishing the hypothesis from primitives, which the proof doesn't do.

**What I need:**
(a) A sufficient condition stated in terms of model primitives (λ_B, S̄, Δ̃, m₀, m̃, C₀, etc.) that guarantees the hypothesis, with a proof that the condition holds. For example: "When λ_B is small enough that bid probabilities are bounded away from zero at intermediate κ, but the takeover channel is strong enough that Δ^min varies meaningfully..." — make this precise.
(b) Alternatively, state the proposition as: "Δ^min(κ) is nonmonotone if and only if [specific primitive condition]" and prove both directions.

### Issue T5: Hold Region Collapse Not Formally Characterized (MODERATE)

**Location:** Line 357, line 603

**Current text:** Line 357 says "When engagement costs are constant (i.e., χ=0), the Hold region may collapse." Line 603 says "The Hold region collapses (k₀=k₁)" under baseline calibration.

**Problem:** The collapse condition is δ[p·(m̃-m₀) + (1-p)·Δ̃] > C₀ for ALL non-exit signals. Under the current calibration (C₀=0.12, δ·Δ̃ ≈ 0.208), engagement is always profitable regardless of bid probability, making Hold always dominated. This is NOT just a χ=0 issue — it happens because C₀ is too low relative to δΔ̃.

**What I need:** Add a Remark after Proposition 1 that characterizes when Hold collapses:
- State the condition: Hold collapses iff C₀ < δ·Δ̃ (approximate, since bid premium also contributes)
- Note this is parameter-dependent, not structural
- Reference the C₀ sensitivity figure showing Hold reappears at higher C₀
- Confirm this does not affect the paper's main results (nonmonotonicity, disclosure effects work with or without Hold)

### Issue T6: Assumption A6 Never Formally Stated (MODERATE)

**Location:** Table at line 885, referenced at lines 314, 509, 513, 968

**Current text:** A6 is listed as "Contraction (uniqueness)" in the assumptions table but never given a formal mathematical statement. Line 968 says "Assumption (A6) states that T is a contraction on a suitable nonempty compact subset Θ ⊂ R³."

**Problem:** This is circular: the assumption says "assume the mapping is a contraction" without specifying what conditions on primitives make it so. A referee will ask: "Under what parameter configurations does A6 hold? Can you verify it?"

**What I need:**
(a) Either provide sufficient conditions on primitives (e.g., bounds on derivatives of bid probability, engagement costs, etc.) that imply contraction, or
(b) Honestly state: "We verify A6 numerically following [citation]. In all calibrations considered, the spectral radius of DT is bounded strictly below 1." This is actually what the paper does at line 1231 — but it should be stated explicitly as A6's content, not as a separate subsection.

### Issue T7: Disclosure Attenuation is Partial Equilibrium Only (MINOR)

**Location:** Proposition 5 (prop:disclosure-attenuation), lines 580-589

**Current text:** "Hold the blockholder's strategy constant: fix the cutoffs (k₁, k₀, k_D)."

**Problem:** This is explicitly a partial-equilibrium result. In GE, changing κ also changes the cutoffs. The paper acknowledges this but doesn't verify whether the PE intuition survives in GE. Under the current calibration, the GE disclosure effect is **exactly zero** (baseline = no-disclosure in Figure 6), contradicting the proposition's spirit.

**What I need:** Add a sentence noting that the GE disclosure effect is parameter-dependent and may vanish when Public Voice usage is negligible (ω_P ≈ 0), with a cross-reference to Figure 6 showing conditions under which it's meaningful.

---

## PART B: CALIBRATION FAILURE

The Python code is verified correct. The problem is purely parametric. Here is the precise diagnosis.

### Current Parameters (Table C.3 in draft_v3.tex)

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Prior mean | μ | 1.00 |
| Fundamental vol | σ_v | 0.50 |
| Signal noise | σ_ε | 0.50 |
| Base engagement cost | C₀ | 0.12 |
| Cost sensitivity | χ | 0.50 |
| Success probability | ρ | 0.90 |
| Value improvement | Δ | 0.25 |
| Base premium | m₀ | 0.10 |
| Activism premium | m₁ | 0.30 |
| Baseline synergy | S̄ | 1.44 |
| Synergy improvement | Δ_S | 0.35 |
| Bidding cost | K | 0.15 |
| Synergy scale | s_ξ | 0.15 |
| Bidder arrival | λ_B | 0.05 |
| Discount factor | δ | 0.95 |

Derived quantities: Δ̃ = ρ·Δ = 0.225, m̃ = ρ·m₁ + (1-ρ)·m₀ = 0.28, σ_s = √(σ_v² + σ_ε²) ≈ 0.707, β = σ_v²/σ_s² = 0.50

### Symptom 1: No Interior Hump in Δ^min

**What happens:** Δ^min peaks at the left boundary κ=0.15 (the lowest value in our grid), NOT at an interior point. The entire range is [0.0068, 0.0076], a variation of ~0.7% of μ.

**Root cause:** The bid probability threshold is:
```
T_raw = V̂(X,D) + m̄(X,D) + K - (S̄ + π·Δ_S)
```
With S̄ = 1.44 and V̂ ≈ 1.0-1.2 (near μ=1), T_raw is often NEGATIVE, meaning bids are unconditionally likely (>50% conditional probability before λ_B scaling). After λ_B=0.05, we get p ≈ 0.02-0.05 uniformly across states — there's essentially no STATE-LEVEL VARIATION in bid probability, which eliminates the mechanism that creates the hump.

The hump requires: (a) bid probability varying meaningfully across (X,D) states, and (b) the activism component Δ^act varying with κ through the inference channel. When S̄ is so large that bids are nearly certain pre-scaling, the λ_B parameter just uniformly scales everything down, destroying the variation.

### Symptom 2: Hold Region Collapsed

**What happens:** k₀ = k₁ everywhere. The Hold region has zero width.

**Root cause:** The Hold-to-Quiet Voice indifference requires:
```
δ·E_z[p(X,0)·(m̃ - m₀) + (1-p(X,0))·Δ̃] = C(k₀)
```
The LHS ≈ δ·[0.04·0.18 + 0.96·0.225] ≈ 0.95·0.223 ≈ 0.212
The RHS at the prior mean: C(μ) = C₀ - χ·(μ-μ)·C₀/σ_s = C₀ = 0.12

Since 0.212 > 0.12, engagement dominates holding for ALL signals above the exit cutoff. The fundamental improvement Δ̃=0.225 alone (even ignoring the premium wedge) exceeds C₀/δ = 0.126.

**Fix needed:** Either raise C₀ to ~0.21+ or lower δΔ̃ below C₀.

### Symptom 3: Disclosure Completely Inert

**What happens:** k_D ≈ 5.24, which is >6σ above μ=1 (σ_s ≈ 0.707). This means ω_P ≈ 0 and the baseline vs. no-disclosure lines in Figure 6 are identical.

**Root cause:** The Quiet-to-Public indifference requires the signal to be high enough that buying a second share at the (high) market price is worthwhile. The price for D=1 states is approximately:
```
P*(X,1) ≈ δ·[V̂(X,1) + p(X,1)·m̃] ≈ 0.95·[1.2 + 0.04·0.28] ≈ 1.15
```
Buying this share costs P* but gives 2× the terminal value instead of 1×. The net benefit of going from h=1 to h=2 must exceed the purchase cost. With the current parameters, this benefit is too small relative to the price, pushing k_D into the extreme tail.

### Symptom 4: Extreme D=1 vs D=0 Price Spread

**What happens:** D=1 prices (~3.17) are roughly 2.4× the D=0 prices (~1.35). This is economically implausible — disclosure of a 5% blockholder shouldn't triple the stock price.

**Root cause:** When k_D is extreme, the conditional mean μ_P = E[v|s ≥ k_D] is very high (since only extreme tail signals trigger Public Voice). This makes V̂(X,1) extremely large, driving up D=1 prices.

### What I Need from You: Recalibration Proposal

Find parameter values (S̄, s_ξ, C₀, λ_B, Δ_S, and possibly Δ, m₁, K) that satisfy ALL of the following simultaneously:

1. **Interior hump:** Δ^min(κ) peaks at some κ† ∈ [0.25, 0.70], not at the boundary
2. **Hump amplitude:** Peak Δ^min at least 5% above the endpoints
3. **Realistic bid rates:** Unconditional bid probability ∈ [2%, 8%] — but with meaningful STATE-LEVEL VARIATION (p(X,D) should differ across states by at least a factor of 2)
4. **Non-collapsed Hold (desirable but not required):** k₀ > k₁ + 0.01 for at least some κ values. If Hold collapse is unavoidable, explain why.
5. **Non-inert disclosure:** ω_P > 0.01, k_D < μ + 3σ_s, baseline vs no-disclosure curves visually distinct
6. **Reasonable price spread:** D=1 prices at most 1.5× the D=0 prices
7. **Net deterrence (A5) holds:** Δ̃ + m̃ - m₀ > Δ_S with comfortable margin

**Approach hint:** The core problem is that S̄ = 1.44 makes the bid threshold T_raw negative. Try S̄ ∈ [0.50, 0.80] so that T_raw is positive and bid probability is genuinely state-dependent. Then adjust s_ξ to control dispersion, and λ_B to hit the 2-8% unconditional target. C₀ may need to be higher (~0.20) to restore Hold.

**Key formulas for your analysis:**

Bid probability:
```
T(X,D) = [V̂(X,D) + m̄(X,D) + K - (S̄ + π(X,D)·Δ_S)] / s_ξ
p(X,D) = λ_B · [1 - Λ(T)]  = λ_B · expit(-T)
```

Hold-Quiet indifference (sets k₀):
```
δ · E_z[p(X,0)·(m̃-m₀) + (1-p(X,0))·Δ̃] = C(k₀) = C₀ · [1 - χ·(k₀-μ)/σ_s]
```

For Hold to exist, we need the LHS < C₀ at s = k₁ (the exit cutoff), i.e.:
```
δ · [p_avg·(m̃-m₀) + (1-p_avg)·Δ̃] < C₀
```

Approximate: when p is small, LHS ≈ δ·Δ̃ = 0.214. So need C₀ > 0.214 for Hold to exist with current Δ̃.

---

## PART C: CONSISTENCY REQUIREMENTS

Whatever fixes you propose must satisfy:

1. **All six Assumptions (A1)-(A6) must hold** under the proposed parameters
2. **The bid probability formula, pricing formula, and payoff formulas must NOT change** — only parameters and proof text
3. **Proposition 4 (nonmonotonicity) must be provable** — if your sufficient condition requires specific parameter ranges, state them
4. **The noise distribution p₀ = 1-2κ/3, p₁ = κ/3 must NOT change**
5. **Notation must be consistent** with the existing paper (V̂, Δ̃, m̃, etc.)

---

## DELIVERABLES

Please provide:

**D1. Fixed proofs** for Issues T1-T7 (complete LaTeX-ready text for each)

**D2. Recalibration table** — a complete replacement for Table C.3 with new parameter values, including a brief justification for each change

**D3. Verification** — for each proposed parameter, compute:
- T_raw at the (X=0, D=0) state at κ=0.50 (should be positive)
- Conditional bid probability p̃ = expit(-T/s_ξ) at the most and least favorable states
- The LHS of the Hold-Quiet indifference at s = μ
- Whether A5 holds: compute Δ̃ + m̃ - m₀ - Δ_S

**D4. Sufficient conditions** for Proposition 4 (nonmonotonicity) stated in terms of primitives, with proof

**D5. Economic narrative** — 2-3 paragraphs explaining why the new calibration is economically reasonable (cite empirical literature if relevant: bid rates from SDC, premium estimates from Schwert 2000 or Betton et al. 2008, activism frequency from Brav et al. 2008)
