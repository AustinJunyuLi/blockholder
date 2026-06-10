---
date: 2026-06-10
type: positioning-memo
status: DRAFT (author finalizes after full reads of C–L and J–S)
branch: jmp-upgrade-2026-05
title: "Positioning vs the three structural-activism competitors"
---

# Positioning Memo — feeds the intro rewrite and the milestone talk

## The one-paragraph claim

The structural activism literature has estimated *who* activists are (Johnson–Swem: reputation dynamics), *what* activism is worth (Albuquerque–Fos–Schroth: value-creation decomposition), and *how* activism interacts with managerial discipline in the control market (Celentano–Levine: activism + M&A equilibrium, R&R RFS). None of the three models the margin this paper is built on: **the trading-and-disclosure environment** — market liquidity, order-flow inference, and the stake-disclosure rule — through which activism information reaches prices and bidders. This paper supplies that margin with two theorems the prior drafts only assumed: the takeover-premium wedge is **derived from a complete free-rider tender game** (appropriability λ = 1 − q(1−γ)ψ from fringe intensity, improvement portability, and bloc pivotality), and the liquidity hump in minority takeover gains is **a theorem on a certified region with a genuine counterexample at its boundary** (GE cutoff-shift dominance holds on κ ∈ [0.35, 0.825] at the baseline; fails by construction at high bidder heterogeneity).

## Against each competitor

**Celentano–Levine (2025, R&R RFS).** Closest in nouns; farthest in mechanism. They quantify activism's disciplinary complementarity/substitution with M&A; no microstructure, no disclosure design, premia not microfounded. Our deterrence channel (∂p/∂π < 0) speaks directly to their crowding-out result, and our comparative statics run in state variables (κ, disclosure threshold) absent from their model. *Posture: complementary quantification; we own the liquidity/disclosure margin.* (Author: validate after full read — esp. whether any inference/trading appears and how premia are set.)

**Johnson–Swem (JFE 2021).** They own the 13D-window ↔ σ²T framing and reputation dynamics; accumulation is a reduced-form cost draw — exactly the object our microstructure opens up. We deliberately do *not* anchor the paper on the 2024 acceleration (their lever): it appears as a de-risk data fact (Fact 1: delay compression, `empirics/output/fact1_*`) and a testable implication, not identification. *Posture: cite-and-defer on the acceleration; our action-triggered disclosure margin is complementary to their fixed-T.*

**Albuquerque–Fos–Schroth (JFE 2022).** Their −13.7% premium effect is the paper's biggest apparent threat and is now its best exhibit: Proposition d7:afs shows the *measured* premium (offer over a price that already capitalizes activism) falls in activism evidence whenever appropriability is low — m₁ ≥ m₀ throughout. The model predicts *where* their estimate should attenuate or flip: portable improvements (financial acquirers, redeployable assets), pivotal blocs, cold fringe markets. Their scalar engagement cost leaves the cost-*distribution* as the white space our 9–24mo structural leg targets. *Posture: their estimate is a quantity our model explains and sharpens, not a contradiction.*

## What is genuinely new (for the talk's contribution slide)

1. **Theorem A (D7):** Condition BG's appropriability coefficient λ — flagged in the draft as derivable "only by a complete tender-game equilibrium" — is now derived: λ = 1 − q(1−γ)ψ, with A3 failing exactly on the characterized boundary (certain, superseding, unblockable fringe raids). Five prior in-house attempts were honestly relabeled; this one closes because λ is an equilibrium *output*.
2. **Theorem B (D8):** the GE cutoff-shift channel is bounded by an inversion-free, contraction-modulus bound computable from one solve; the hump is a theorem on the certified region [0.35, 0.825] (loose bound; [0.30, 0.85] exact) and *provably not* a global theorem (certified troughs at σ_ξ = 0.60 with channel A single-peaked) — with the economic boundary (entry insensitivity to premia) itself testable.
3. **AFS reconciliation (Prop d7:afs)** as above.
4. **De-risk facts:** Fact 1 (13D delay compression, EDGAR) + Fact 2 design (WRDS-gated).

## Risks / honesty lines for the talk

- Region theorem is calibration-certified (computable hypothesis, checked to numerical precision), not calibration-free; say so on the slide — the counterexample shows a calibration-free version is impossible.
- λ's tender game takes the institution (equal-treatment offers, GH selection, charter φ, τ_c) as given; the open items (bidder competition, dynamic fringe) are stated in D7's ledger.
- Celentano–Levine scope cells marked ◑ in `lit/competitor_scope_tables.md` await the full read; do not present those as verified.
