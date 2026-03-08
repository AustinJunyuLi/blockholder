# Comprehensive Status Report: Post-Round 2 Patch

## Summary

Round 2 (Gemini Deep Think) produced 7 theoretical proof fixes (T1-T7) and a recalibration proposal. ALL have been applied to draft_v3.tex and params.py. The pipeline runs cleanly, producing 14 CSVs and 13 PDF figures.

**Result: 5 of 8 calibration targets now pass. 3 remain failing — all related to the disclosure channel (D=1 branch).**

---

## Section 1: What Is Working (5/8 Targets PASS)

### 1.1 Interior Hump in Δ^min (PASS)
- **Peak location:** κ = 0.438 (target range: [0.25, 0.70])
- **Δ^min range:** [0.00737, 0.00793] across κ ∈ [0.15, 0.85]
- **Amplitude:** (0.00793 - 0.00737) / 0.00793 = 7.1% (target: >5%)
- **Economic interpretation:** The Jensen's inequality mechanism works exactly as T4 predicted. At κ→0, extreme belief dispersion minimizes E[f(π)]; at interior κ, noise pooling concentrates π, raising the concave function value.

### 1.2 Hold Region Restored (PASS)
- **Hold width at κ=0.50:** k0 - k1 = 1.231 - 0.776 = 0.454
- **Condition:** C₀ = 0.25 > δΔ̃ = 0.95 × 0.225 = 0.214 ✓
- **Economic interpretation:** Raising C₀ from 0.12 to 0.25 pushed the base engagement cost above the expected improvement, restoring a signal range where the blockholder rationally prefers passivity.

### 1.3 State-Level Bid Variation (PASS)
- **D=0 bid rates:** 16.0% (X=-2), 10.7% (X=-1), 1.83% (X=0), 1.09% (X=1)
- **Variation ratio:** 16.0% / 1.09% = 14.6x
- **Economic interpretation:** S̄ = 1.10 places the raw bid threshold T_raw in the sensitive left tail of the logistic CDF. Variation in V̂(X,D) across states produces dramatic bid probability differences. This is exactly the mechanism that drives the hump.

### 1.4 Net Deterrence A5 (PASS)
- **LHS:** Δ̃ + m̃ - m₀ = 0.225 + 0.28 - 0.10 = 0.405
- **RHS:** Δ_S = 0.30
- **Margin:** 0.405 - 0.30 = 0.105 > 0 ✓

### 1.5 Solver Convergence (PASS)
- 36 κ grid points, all converge (0 failures)
- Maximum residual: within tolerance
- Cutoffs vary smoothly with κ

---

## Section 2: What Is Failing (3/8 Targets FAIL)

### 2.1 kD Is Extreme (FAIL)
- **Value at κ=0.50:** kD = 4.942
- **In standard deviations:** (4.942 - 1.0) / 0.707 = 5.6σ above μ
- **Target:** kD < μ + 3σ = 3.12
- **Consequence:** Pr(s > kD) ≈ Φ(-5.6) ≈ 10⁻⁸, so ω_P ≈ 0

### 2.2 Disclosure Effect Is Zero (FAIL)
- **act_disclosure vs act_no_disclosure at κ=0.50:** 0.002132 vs 0.002132
- **Difference:** ~5×10⁻⁷ (effectively 0%)
- **Target:** >1% disclosure effect
- **Consequence:** Proposition 6 (disclosure attenuation) has no numerical support. The two curves in Figure 6 are visually identical.

### 2.3 D=1 Prices and Bid Rates Are Degenerate (FAIL)
- **D=1 prices:** P(X,1) = 3.015 for ALL X ∈ {0,1,2} (off-path, set by π=1)
- **D=1 bid rates:** λ_B × expit(-T/s_ξ) = 0.20 × expit(-5.03) ≈ 8.3×10⁻⁸
- **D=0 price range:** 0.626 to 1.284
- **D=1/D=0 price ratio:** 3.015 / 0.983 (avg D=0) ≈ 3.07x
- **Target:** D=1/D=0 ratio < 1.5x

---

## Section 3: Root Cause Analysis

### 3.1 The Core Problem: Public Voice Is Economically Irrational

The fundamental issue is that **under the current model structure + A5 (net deterrence), Public Voice is never an attractive action for the blockholder at any reasonable signal level.**

**Why kD is so high:**

When the blockholder chooses Public Voice (q=+1), she:
1. Pays market price P(X,1) to buy a second share
2. Pays engagement cost C(s)
3. Triggers disclosure D=1, which sets π(X,1) = 1

With π = 1, the expected standalone value is:
  V̂(X,1) = E[v|X,1] + Δ̃ = μ_P + 0.225

The bid threshold becomes:
  T_raw = V̂ + m̃ + K - (S̄ + Δ_S) = (μ_P + 0.225) + 0.28 + 0.15 - (1.10 + 0.30)

At baseline μ_P ≈ μ + βσ_s × λ_U(αD) ≈ 1.50 (for very high kD):
  T_raw ≈ 1.725 + 0.28 + 0.15 - 1.40 = 0.755

With s_ξ = 0.15:
  T_scaled = 0.755/0.15 = 5.03
  p_bid_cond = expit(-5.03) ≈ 0.0065%
  p_bid_uncond = 0.20 × 0.0065% ≈ 0.0013%

**The bid probability under full disclosure is essentially zero.** The market perfectly prices engagement (Δ̃ = 0.225) plus the premium wedge (m̃ - m₀ = 0.18), making the target so expensive that no bidder finds it profitable. Under A5, the price run-up from engagement strictly exceeds the synergy gain Δ_S.

**Meanwhile, the blockholder must pay P(X,1) ≈ 3.015 per share.** The expected terminal value of 2 shares is approximately:
  2 × (v_post + Δ̃) ≈ 2 × (μ + 0.225) ≈ 2.45

She's paying 3.015 for something worth ~2.45 in expectation — a guaranteed loss of ~0.57, plus C(s). This is only rational at extreme signal values where v_post >> μ.

### 3.2 Mathematical Summary

The issue is structural, not parametric:

1. **A5 requires:** Δ̃ + m̃ - m₀ > Δ_S  (net deterrence)
2. **This implies:** ∂p/∂π < 0  (engagement deters bids)
3. **At D=1:** π = 1 (maximal engagement inference)
4. **Therefore:** p(X,1) is minimized among all states
5. **The price P(X,1)** capitalizes full Δ̃ + expected premium
6. **The blockholder pays P(X,1)** to buy the second share
7. **Net result:** Public Voice generates a trading loss, engagement cost, AND minimal takeover benefit

### 3.3 Why No Calibration Can Fix This

The three failing targets all trace to ω_P ≈ 0 (no Public Voice). This is not a matter of finding the right (S̄, s_ξ, λ_B, C₀) — the economics make Public Voice structurally unattractive under A5.

To make kD reasonable (say, kD = μ + 1.5σ), the payoff to Public Voice must match Quiet Voice at that signal level. But:
- Public Voice has an additional trading cost (-P(X,1)) that Quiet Voice avoids
- Public Voice triggers full price capitalization of engagement
- Under A5, this capitalization strictly eliminates the takeover benefit

**We ran a systematic recalibration sweep** (recalibrate.py) across 640 parameter combinations of (λ_B, C₀, S̄, s_ξ, Δ_S). No configuration achieved all three disclosure targets simultaneously with the other five. The "triple win" (hump + hold + disclosure) was empty.

---

## Section 4: What the Theory Proofs Claim vs. What the Numerics Show

### Proposition 4 (Nonmonotonicity): NUMERICALLY CONFIRMED ✓
The Jensen's inequality proof is validated: the interior hump exists at κ = 0.438.

### Proposition 5 (Disclosure Attenuation): NUMERICALLY UNSUPPORTED ✗
The proposition states that disclosure "attenuates" the inference channel. But with ω_P ≈ 0, the disclosed branch carries negligible probability weight, so:
- The baseline model ≈ the no-disclosure counterfactual
- There is nothing for disclosure to attenuate

The proposition is mathematically correct (holds "in principle"), but economically vacuous under any calibration satisfying A5.

### Remark 2 (GE caveat for Proposition 5): PRESCIENT
The remark notes that disclosure attenuation "robustly survives full general equilibrium feedback provided the baseline parameterization supports a non-negligible incidence of Public Voice (ω_P >> 0)." Under the current calibration, ω_P ≈ 0, so the proviso is violated.

### Hold Collapse Remark: RESOLVED ✓
With C₀ = 0.25, the Hold region is restored (width 0.454).

---

## Section 5: Options for Resolution

The disclosure channel failure appears to require a structural change, not just parameter tuning. Possible directions include:

**Option A: Accept the limitation.** Document that A5 implies ω_P ≈ 0 under realistic calibrations. Reframe the paper around the hump result (Proposition 4) and downweight Proposition 5.

**Option B: Weaken or restructure A5.** Allow some parameter configurations where ∂p/∂π is not uniformly negative — perhaps making the deterrence effect state-dependent rather than global.

**Option C: Decouple the D=1 price problem.** Change the model so that disclosure does not fully reveal engagement to the market maker at the time of pricing, or so that the blockholder does not pay the fully-inflated D=1 price.

**Option D: Modify the bidder's entry rule.** Perhaps the bidder's surplus should not fully capitalize the engagement improvement, or the synergy facilitation should dominate the deterrence effect on the disclosed branch.

**Option E: Partial or noisy disclosure.** Instead of D=1 perfectly revealing a=1, introduce noise into the disclosure signal, reducing the extreme price inflation on the disclosed branch.

**We explicitly do NOT recommend any specific option.** We seek Gemini's independent structural assessment.

---

## Section 6: Exact Numerical Data

### Cutoffs at κ = 0.50
| Cutoff | Value | Standard deviations from μ |
|--------|-------|---------------------------|
| k1     | 0.776 | -0.32σ                    |
| k0     | 1.231 | +0.33σ                    |
| kD     | 4.942 | +5.57σ                    |

### Action Probabilities at κ = 0.50 (approximate)
| Action | ω | Signal range |
|--------|---|-------------|
| Exit   | ~28% | s < 0.776 |
| Hold   | ~32% | 0.776 ≤ s < 1.231 |
| Quiet Voice | ~40% | 1.231 ≤ s < 4.942 |
| Public Voice | ~10⁻⁸ | s ≥ 4.942 |

### Parameters (Table C.3 in draft_v3.tex)
| Parameter | Symbol | Value |
|-----------|--------|-------|
| Prior mean | μ | 1.00 |
| Fundamental vol | σ_v | 0.50 |
| Signal noise | σ_ε | 0.50 |
| Base cost | C₀ | 0.25 |
| Cost sensitivity | χ | 0.50 |
| Success prob | ρ | 0.90 |
| Value improvement | Δ | 0.25 |
| Base premium | m₀ | 0.10 |
| Activism premium | m₁ | 0.30 |
| Baseline synergy | S̄ | 1.10 |
| Synergy improvement | Δ_S | 0.30 |
| Bidding cost | K | 0.15 |
| Synergy scale | s_ξ | 0.15 |
| Bidder arrival | λ_B | 0.20 |
| Discount factor | δ | 0.95 |

### Derived Quantities
| Quantity | Value |
|----------|-------|
| σ_s | 0.707 |
| β | 0.50 |
| Δ̃ = ρΔ | 0.225 |
| m̃ = m₀ + ρ(m₁-m₀) | 0.28 |
| A5 margin: Δ̃+m̃-m₀-Δ_S | 0.105 |
| Hold condition: C₀ - δΔ̃ | 0.036 > 0 |
