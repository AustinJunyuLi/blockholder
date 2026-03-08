# Codebase Review Request — EVT Model (Round 3)

**Commit:** 4c63de2 (2026-03-03)
**Files uploaded:** 9 consolidated files covering the full codebase + manuscript
**Round focus:** Structural consultation on the disclosure channel failure

## How to Read the Uploaded Files

| File | Contents | Lines |
|------|----------|-------|
| 00_PROJECT_OVERVIEW.md | Project identity, architecture, git state, model summary | 76 |
| 01_MANUSCRIPT.md | Full LaTeX manuscript (`draft_v3.tex`, 1448 lines) | 1451 |
| 02_PYTHON_MODEL.md | Core model (`numerical/model.py`) — posteriors, prices, payoffs, welfare | 651 |
| 03_PYTHON_INFRASTRUCTURE.md | `params.py` (calibration) + `solver.py` (fixed-point) + `export_data.py` (CSV export) | 707 |
| 04_NUMERICAL_OUTPUT.md | Key CSV outputs: baseline series, prices, disclosure attenuation, cutoffs, params | 133 |
| 05_ROUND2_REPLY.md | Your Round 2 response (`fix2.md`) — all 7 theoretical fixes + recalibration | 189 |
| 06_STATUS_REPORT.md | **Comprehensive status report** — what works, what fails, root cause analysis | 205 |
| 07_ROUND2_PROMPT_SUMMARY.md | Summary of what was asked and delivered in Round 2 | 37 |
| 08_SUPPORTING.md | Recalibration sweep script summary + Makefile | 64 |

Each file contains concatenated source with `## path/to/file` headers.

---

## Previous Round Feedback

Your Round 2 analysis identified 7 theoretical issues (T1-T7) and proposed a recalibration. **All 7 fixes have been applied to the manuscript.** The recalibration (C₀: 0.12→0.25, S̄: 1.44→1.10, Δ_S: 0.35→0.30, λ_B: 0.05→0.20) has been applied to `params.py`. The full pipeline runs cleanly, producing 14 CSVs and 13 PDF figures.

### What Improved After Round 2

1. **Interior hump restored:** Peak at κ = 0.438, amplitude 7.1% (target: >5%)
2. **Hold region restored:** Width 0.454 (target: >0.01)
3. **State-level bid variation:** 14.6x across D=0 states (target: >5x)
4. **A5 (net deterrence) holds:** Margin 0.105 (target: >0)
5. **Solver convergence:** 36/36 grid points, 0 failures

### What Did NOT Improve After Round 2

6. **kD is extreme:** 4.942 (5.6σ above μ) — target: < μ + 3σ = 3.12
7. **Disclosure effect is zero:** Baseline vs no-disclosure differ by ~5×10⁻⁷ — target: >1%
8. **D=1 prices are degenerate:** P(X,1) = 3.015 for all X; D=1/D=0 ratio = 3.07x — target: <1.5x

**Result: 5 of 8 calibration targets pass. 3 remain failing — all related to the disclosure channel (D=1 branch).**

---

## The Core Problem

The three failures all trace to one root cause: **Public Voice (q=+1, a=1, D=1) is essentially off-path.** The probability of Public Voice is ω_P ≈ 10⁻⁸ at κ = 0.50.

### Why Public Voice Is Off-Path

When the blockholder chooses Public Voice, she:
1. Pays market price P(X,1) to buy a second share
2. Pays engagement cost C(s)
3. Triggers disclosure D=1, which sets π(X,1) = 1 (maximal engagement inference)

With π = 1, the market maker fully capitalizes engagement into the price:
- V̂(X,1) = E[v|X,1] + Δ̃ = μ_P + 0.225
- P(X,1) ≈ δ[V̂ + p_bid × m̃] ≈ 3.015

Meanwhile, the bid threshold under full disclosure:
- T_raw = V̂ + m̃ + K − (S̄ + Δ_S) = (μ_P + 0.225) + 0.28 + 0.15 − 1.40 = 0.755
- T_scaled = 0.755 / 0.15 = 5.03
- p_bid = expit(−5.03) ≈ 0.0065%
- p_bid_uncond = 0.20 × 0.0065% ≈ 0.0013%

**The bid probability under full disclosure is essentially zero.** Under A5, the price run-up from engagement strictly exceeds the synergy gain Δ_S, making the target so expensive that no bidder finds it profitable.

**The blockholder's problem is worse:** She pays P(X,1) ≈ 3.015 per share for something worth ~2.45 in expectation — a guaranteed loss of ~0.57, plus C(s). This is only rational at extreme signal values where v_post >> μ, hence kD ≈ 5.6σ above μ.

### Mathematical Summary

The chain of implications:
1. A5 requires: Δ̃ + m̃ − m₀ > Δ_S (net deterrence)
2. This implies: ∂p/∂π < 0 (engagement deters bids)
3. At D=1: π = 1 (maximal engagement inference)
4. Therefore: bid probability under D=1 is minimized
5. The price P(X,1) capitalizes full Δ̃ + expected premium
6. The blockholder pays this inflated P(X,1) to buy the second share
7. Net result: Public Voice generates a trading loss, engagement cost, AND minimal takeover benefit

### Systematic Recalibration Attempt

We ran a systematic parameter sweep (`recalibrate.py`) across 640 combinations of (λ_B, C₀, S̄, s_ξ, Δ_S). **Zero configurations achieved the "triple win"** (hump + hold + disclosure effect > 1%) simultaneously. The disclosure effect is structurally zero across all tested parameters when A5 holds.

---

## What the Theory Proofs Claim vs. What the Numerics Show

| Proposition | Claim | Numerical Status |
|-------------|-------|-----------------|
| Prop 4 (Nonmonotonicity) | Δ^min is hump-shaped in κ | **CONFIRMED** ✓ — peak at κ=0.438, Jensen's mechanism works |
| Prop 5 (Disclosure attenuation) | Disclosure attenuates the inference channel | **UNSUPPORTED** ✗ — with ω_P ≈ 0, baseline ≈ no-disclosure counterfactual |
| Remark 2 (GE caveat) | Attenuation survives GE "provided ω_P >> 0" | **PRESCIENT** — the proviso is violated |
| Hold collapse remark | Hold region can collapse | **RESOLVED** ✓ — restored with C₀ = 0.25 |

Proposition 5 is mathematically correct (holds "in principle") but economically vacuous under any calibration satisfying A5. There is nothing for disclosure to attenuate when the disclosed branch carries negligible probability weight.

---

## Exact Numerical Data

### Cutoffs at κ = 0.50
| Cutoff | Value | Standard deviations from μ |
|--------|-------|---------------------------|
| k1     | 0.776 | −0.32σ                    |
| k0     | 1.231 | +0.33σ                    |
| kD     | 4.942 | +5.57σ                    |

### Action Probabilities at κ = 0.50
| Action | ω | Signal range |
|--------|---|-------------|
| Exit   | ~28% | s < 0.776 |
| Hold   | ~32% | 0.776 ≤ s < 1.231 |
| Quiet Voice | ~40% | 1.231 ≤ s < 4.942 |
| Public Voice | ~10⁻⁸ | s ≥ 4.942 |

### Current Parameters (Table C.3)
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
| β (signal precision) | 0.50 |
| Δ̃ = ρΔ | 0.225 |
| m̃ = m₀ + ρ(m₁−m₀) | 0.28 |
| A5 margin: Δ̃+m̃−m₀−Δ_S | 0.105 |
| Hold condition: C₀ − δΔ̃ | 0.036 > 0 |

---

## Your Task

This is Round 3 of our iterative review. Rounds 1 and 2 successfully identified and fixed 7 theoretical proof gaps and restored the hump + hold region. **The remaining problem is structural, not parametric.**

We seek your **independent structural assessment** of the disclosure channel failure. We have deliberately avoided recommending any specific solution — we want your unbiased analysis of what can and should be done.

## Deliverables

### D1: Structural Diagnosis

Provide your independent analysis of why the disclosure channel fails. Do you agree with our root cause analysis (A5 ⇒ full price capitalization ⇒ Public Voice off-path)? Or is there a different or deeper structural explanation?

Specifically address:
- Is there a way to make Public Voice economically rational under A5, or does A5 fundamentally preclude it?
- Is the problem in the pricing mechanism, the bid entry rule, the disclosure structure, or the assumption set?
- What is the minimal structural change that would restore the disclosure channel while preserving the other 5 working results?

### D2: Proposed Fix

If you identify a structural change, provide:
1. **Exact mathematical specification** — new equations, modified assumptions, changed functional forms
2. **Exact LaTeX replacement text** for the manuscript — specify which lines/environments to modify in `draft_v3.tex`
3. **Exact Python implementation** — specify changes to `model.py`, `params.py`, `solver.py`, and/or `export_data.py`
4. **Economic narrative** — why does your proposed change make economic sense? What real-world phenomenon does it capture?

### D3: Verification Calculations

Show analytically that your proposed fix would produce:
- kD within μ ± 3σ (target: kD < 3.12)
- Non-trivial ω_P (target: >0.1%)
- Measurable disclosure effect (target: >1%)
- D=1/D=0 price ratio < 1.5x

Show that it preserves:
- Interior hump in Δ^min
- Hold region (C₀ > δΔ̃)
- A5 net deterrence (or explain why A5 should be modified)

### D4: Sensitivity Assessment

How robust is your proposed fix? Under what parameter ranges does it succeed? Are there new knife-edge conditions or fragilities introduced?

### D5: Alternative Approaches

If there are multiple possible structural changes, rank them by:
- Economic plausibility (does it match real-world institutional features?)
- Implementation complexity (how many equations/files change?)
- Robustness (how sensitive is the fix to parameter values?)
- Theoretical elegance (does it simplify or complicate the model?)

---

_Internal: snapshot_sha=4c63de2, round=3, date=2026-03-03_
