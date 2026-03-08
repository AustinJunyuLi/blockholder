# Theory Audit History

## Context
This paper has undergone rigorous multi-model theory auditing across 4 rounds (GPT Pro × Gemini Deep Think × Claude). Six mathematical issues were identified and fixed. The theory in draft_v3.tex is the corrected version.

## GPT Pro Round 2 Meeting Notes (2026-03-04)

# Meeting Notes: GPT Pro Theory Audit — Round 2

**Date:** 2026-03-04
**Reviewer:** GPT Pro (OpenAI)
**Project:** Liquidity, Activism Disclosure, and Takeover Premia
**Commit reviewed:** 4c63de2

---

## Executive Summary

GPT Pro independently confirms Claude's D5 gap is real and provides 5 camera-ready LaTeX patches. The core verdict: **D3, D4, D6 are resolved; D1 and D2 are partially resolved (overclaim what's analytically provable); D5 introduces a new problem that GPT Pro fixes with a belief-free lower-bound proof.** The recommended strategy is to stop trying to prove general-equilibrium endpoint limits analytically and instead use an honest "analytic decomposition + numerical verification" hybrid for Proposition 5.

## Findings by Category

### Correctness Issues

1. **D5 Gap Confirmed Real** — Gemini's Lemma 1 proof compares `G = 2δ E_z[p(X,1)(m̃−m₀) + (1−p(X,1))Δ̃]` to `C(k₀) = δ E_z[p(X,0)(m̃−m₀) + (1−p(X,0))Δ̃]` and claims "2× > 1×". But inner expectations differ: different `X` distributions (`X=1+z` vs `X=z`) and different bid probabilities (`p(·,1) < p(·,0)` under A5). The step is invalid.
   - **Severity:** Critical
   - **Action required:** Replace with belief-free lower-bound proof (Patch 1). Two versions offered: Version 1 (weaker statement, no new assumptions) or Version 2 (adds A8 for "for all s ≥ k₀").

2. **D1 Unproved ω_Q → 0 Claim** — Gemini's Lemma 2 rewrite correctly removes the false "uninformative posterior" claim but replaces it with "ω_Q → 0 as κ → 1", which is an **equilibrium correspondence** claim requiring comparative statics on the cutoff mapping. Not proved. Numerical data even shows ω_Q can be nonmonotone (hits 0 at κ=0.63, becomes positive again at κ=0.70).
   - **Severity:** Critical
   - **Action required:** Rewrite Lemma 2 as purely Bayesian/pricing endpoint lemma (what's provable from bounded-noise algebra alone). See Patch 2.

3. **D2 Monotonicity Overclaim** — `Δ^base(κ)` increasing and `Δ^act(κ)` decreasing are stated as if analytically proved. They are general-equilibrium outcomes depending on endogenous cutoffs (k₁(κ), k₀(κ), k_D(κ)). Cannot be signed from primitives without a monotone comparative static theorem for the fixed point.
   - **Severity:** Major
   - **Action required:** Label as numerical comparative statics, not analytic. See Patch 2.

4. **D6 Narrative Error** — Formula `P(D=1|X)` is correct, but the sentence "interior order flows X ∈ {−1, 0, 1} mix across disclosure states" is wrong for X = −1 (since D = 1 requires q = +1, which needs z = X − 1 = −2, impossible). The mixing states are X ∈ {0, 1} only.
   - **Severity:** Minor
   - **Action required:** Fix sentence to say X ∈ {0, 1} mix across disclosure states.

5. **κ = 0 Full Support Claim** — Line 321 says "noise has full support on {−1, 0, 1}, hence every X ∈ {−2, …, 2} occurs with positive probability." At κ = 0, P(z = ±1) = 0, so X = ±2 never happens.
   - **Severity:** Minor
   - **Action required:** Add "for any κ > 0" qualifier.

### Methodology Concerns

1. **Analytic vs Numerical Labeling** — Any claim about general-equilibrium objects (Δ^base, Δ^act, ω_Q behavior) presented as a theorem/lemma without proof will trigger desk reject. Must explicitly separate what is provable (Bayesian algebra, within-regime posterior monotonicity) from what is computed (GE comparative statics).
   - **Severity:** Critical
   - **Action required:** Implement Patch 2's approach throughout.

2. **Equilibrium Refinement Formalization** — D1 criterion mentioned in Lemma 1 proof but not formally defined. Need one-paragraph formal definition or switch to "Cho–Kreps intuitive criterion" with explicit statement of what it rules out.
   - **Severity:** Major
   - **Action required:** Add formal definition of refinement used.

### Design Observations

1. **A7 (λ_B ≤ 1/2) is economically defensible** — Interpreted as annualized hazard, most firm-year bid rates are far below 50%. GPT Pro recommends adding one sentence: "trivially satisfied in U.S. M&A data (annual bid incidences are single-digit percentages)."

2. **Hybrid analytic + numerical is standard** — Explicitly cited Edmans–Goldstein–Jiang as precedent for PBE + equilibrium refinements with numerical fixed-point computations. Standard approach when closed forms are impossible.

3. **Version 1 vs Version 2 for Lemma 1** — Version 1 (no new assumption, honest "for sufficiently high s") is recommended as the cleanest patch. Version 2 (add A8) available if stronger claim needed.

## Camera-Ready Patches Provided

| Patch | Target | Lines in draft_v3.tex | What it does |
|-------|--------|----------------------|--------------|
| 1 | Lemma 1 statement + proof | 333–336 (statement), 905–922 (proof) | Belief-free lower-bound proof; no p(X,1) vs p(X,0) comparison |
| 2 | Lemma 2 + Prop 5 + narrative | 552–568 (main text), 1258–1297 (proofs) | Removes unproved ω_Q→0; labels monotonicities as numerical |
| 3 | Premium interpretation | Line 231 | b = V̂ + m^R(a) language |
| 4 | A7 assumption + Prop 1 proof | After line 898 (assumption table), 973–974 (proof) | Formalizes λ_B ≤ 1/2 |
| 5 | P(D=1\|X) formula + B.11 | After line ~1012, 1219–1231 | Explicit Bayes formula; fixes "by definition" |

## Validated (No Issues Found)

- **Proposition 2 posteriors**: Correctly computed given the discrete support. π(1,0) = ω_Q/(ω_H+ω_Q) is κ-invariant — GPT Pro re-derived this independently.
- **Feed-forward pricing identities**: Algebraically consistent, no math error.
- **Conditional expectations E[v|X,D]**: Standard mixture logic, correctly set up.
- **Bidder entry model**: Derivative and sign logic correct conditional on modeling choice.
- **D3 (premium fix)**: Correctly matches b(X,D,a) = V̂(X,D) + m^R(a).
- **D4 (A7 fix)**: Properly closes the single-crossing gap in Prop 1 proof.
- **D6 (Bayes formula)**: Formula itself is correct; only narrative sentence needs fixing.
- **Existence proof (Brouwer)**: Acceptable if you explicitly prove continuity of cutoff mapping and justify bounding box.

## Open Questions

1. **Version 1 vs Version 2 for Lemma 1?** Version 1 (no A8, weaker statement) is cleaner but means lemma says "for sufficiently high s" rather than "for all s ≥ k₀". Version 2 adds A8 (C(k₀) < 2δ min{α,β}) for the stronger claim. User must decide.
2. **Equilibrium refinement formalization:** Keep D1 or switch to Cho–Kreps intuitive criterion? Need one-paragraph definition either way.
3. **Existence/uniqueness:** Brouwer + compact rectangle approach is fine but needs explicit continuity proof and bounding box justification. Currently somewhat hand-wavy.

## Action Items Summary

| # | Item | Severity | Effort | Priority | Owner |
|---|------|----------|--------|----------|-------|
| 1 | Apply Patch 1: Lemma 1 belief-free proof | Critical | Medium | P0 | TBD |
| 2 | Apply Patch 2: Lemma 2 + Prop 5 honest hedging | Critical | Medium | P0 | TBD |
| 3 | Apply Patch 3: Premium interpretation | Minor | Low | P0 | TBD |
| 4 | Apply Patch 4: A7 assumption + Prop 1 proof | Major | Low | P0 | TBD |
| 5 | Apply Patch 5: P(D=1\|X) formula + B.11 | Minor | Low | P0 | TBD |
| 6 | Fix D6 narrative (X=-1 not a mixing state) | Minor | Low | P1 | TBD |
| 7 | Fix κ=0 full support claim (line 321) | Minor | Low | P1 | TBD |
| 8 | Add A7 economic justification sentence | Minor | Low | P1 | TBD |
| 9 | Formalize equilibrium refinement (D1 or Cho-Kreps) | Major | Medium | P1 | TBD |
| 10 | Decide: Version 1 vs Version 2 for Lemma 1 | Critical | Low | P0 | User |

---
_Raw reply saved to: `round_2_reply.md`_
_Generated by Claude from GPT Pro feedback_
