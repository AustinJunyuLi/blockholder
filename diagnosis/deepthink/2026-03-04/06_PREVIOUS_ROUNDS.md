# Previous Rounds Summary (Rounds 1–3.5)

## Round 1 (2026-03-03)
**Focus:** Initial codebase review and theoretical audit.
**Outcome:** Identified 7 theoretical proof gaps (T1–T7).

## Round 2 (2026-03-03)
**Focus:** Fix T1–T7 + recalibration.
**Fixes applied:**
- T1: Noise distribution parity bug fixed (p₀ = 1 − 2κ/3, p₁ = κ/3)
- T2: Bidder entry rule clarified (bidder observes (X,D) directly)
- T3: Feed-forward pricing (eliminated premium-on-premium recursion)
- T4: Lambda_B introduced as explicit Poisson arrival rate
- T5: Net deterrence assumption A5 formalized
- T6a/T6b: Premium wedge and synergy facilitation clarified
- T7: Engagement cost specification tightened

**Recalibration:** C₀: 0.12→0.25, S̄: 1.44→1.10, Δ_S: 0.35→0.30, λ_B: 0.05→0.20

**Results after Round 2:**
- ✓ Interior hump restored (peak at κ = 0.438)
- ✓ Hold region restored (width 0.454)
- ✓ State-level bid variation (14.6x)
- ✓ A5 (net deterrence) holds
- ✓ Solver convergence (36/36 grid points)
- ✗ k_D extreme (4.942, 5.6σ above μ)
- ✗ Disclosure effect zero (baseline ≈ no-disclosure)
- ✗ D=1 prices degenerate

## Round 3 (2026-03-03)
**Focus:** Structural diagnosis of disclosure channel failure.
**Root cause:** Public Voice was off-path because the blockholder paid the fully inflated
post-disclosure price P_post(X,1) to buy the second share. Under A5, this price was so high
that buying was only rational at extreme signal values (k_D ≈ 5.6σ).

**Structural fix proposed: Anonymous Accumulation (Delayed Disclosure)**
- The blockholder trades at P_trade(X) = Σ_d Pr(D=d|X) · P_post(X,d) BEFORE disclosure
- Post-disclosure secondary market updates to P_post(X,D)
- Bidder acts on (X,D) as before
- Single-crossing preserved because P_trade(X) is s-independent

## Round 3.5 (2026-03-03)
**Focus:** Exhaustive theoretical rewrite incorporating Anonymous Accumulation.
**Delivered:** Complete camera-ready LaTeX for all model sections, definitions, propositions,
and appendix proofs under the new two-price structure (P_trade and P_post).

**Key confirmations:**
- Single-crossing survives (P_trade absorbed into s-independent constants)
- Existence via Brouwer's fixed-point theorem preserved
- Feed-forward pricing eliminates recursive loops
- A5 preservation proven (not just claimed)

## Current State (Post-Implementation)
All Round 3/3.5 changes have been implemented in both manuscript (draft_v3.tex) and
Python code (model.py, solver.py). Public Voice is now on-path:
- k_D ≈ 1.53 at κ = 0.50 (reasonable, ~0.7σ above μ)
- ω_P ≈ 23% at κ = 0.50 (substantial probability)
- Disclosure effect is now meaningful (D=1 branch carries real weight)

## What Round 4 Addresses
Round 4 fixes issues in Lemma 2 (right-endpoint behavior) and Proposition 5
(nonmonotonicity proof) that were NOT addressed in Rounds 1–3.5. These issues
were identified by a separate independent audit (GPT Pro, file 05) and verified
numerically (file 04).
