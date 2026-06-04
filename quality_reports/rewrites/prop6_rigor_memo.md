---
date: 2026-04-21
type: technical memo (draft for author signoff)
section_affected: Lemma 5, Proposition 6, Proposition 7 (possibly)
status: DRAFT — needs author signoff before tex edit
author: Claude (derivation), needs Austin Li review
---

# Memo: Rigorizing the Hump — What I Found

## TL;DR

Working through `Δ^min(κ)` from primitives surfaced two surprises:

1. **Lemma 5's right-endpoint claim is incorrect** (not just informally argued). At κ=1, voice does not collapse in general, and the posterior distribution does **not** converge to the unconditional prior across all non-disclosed states.
2. **Δ^min(0) = Δ^min(1) exactly in equilibrium.** The two endpoints are equivalent, not one being a "minimum." This is a clean symmetry result falling out of the posterior formulas.

These two findings completely reshape how the hump theorem should be stated. The good news: the hump result itself **is** provable under a clean primitive condition — but via a Jensen-style variance mechanism, not the "bid-deterrence at low κ / engagement collapse at high κ" story the paper tells.

---

## 1. Endpoint symmetry: `Δ^min(0) = Δ^min(1)`

**Setup.** Use the paper's notation: `a ≡ ω_E`, `b ≡ ω_H + ω_Q`, `c ≡ ω_Q`, so `π_V ≡ c/b` is the Hold–vs–Quiet-Voice posterior; `x ≡ κ/2`, `y ≡ 1 − κ`.

**Posteriors on `D=0`** (from Prop 2):
- `π(−2, 0) = 0` (always)
- `π(−1, 0) = cx / (bx + ay)`
- `π(0, 0)  = cy / (by + ax)`
- `π(+1, 0) = c/b = π_V` (no κ dependence)

**State probabilities on `D=0`:**
- `P(−2) = a · x`;  `P(−1) = a · y + b · x`
- `P(0)  = a · x + b · y`;  `P(+1) = b · x`

### Endpoint evaluation

**At `κ = 0`** (so `x=0, y=1`): only `P(−1) = a` (reveals Exit, `π=0`) and `P(0) = b` (reveals Hold/Quiet, `π=π_V`) have mass.

**At `κ = 1`** (so `x=½, y=0`): mass redistributes but the `(π, P(v|state))` structure is preserved:
- `π(−2) = 0` with mass `a/2` — **same** posterior on `v` as `π=0` state at `κ=0`.
- `π(−1) = c/b = π_V` with mass `b/2` — **same** posterior structure as `π=π_V` state.
- `π(0) = 0` with mass `a/2` — **same** as Exit state.
- `π(+1) = π_V` with mass `b/2` — **same** as Voice-pool state.

So at `κ=1`, the D=0 branch has two "effective" states (Exit-revealing with total mass `a`, Voice-pool-revealing with total mass `b`), **identical in `(π, E[v|·], bar{m}, P, p)` to the two `κ=0` states**.

### The indifference conditions match

For each cutoff:

**`k_1` (Exit vs. Hold):** `U_E(k_1) = U_H(k_1)`.

- `U_E(s, κ) = E_z[P(−1+z, 0)]`.
  - At `κ=0`: `E_z = P(−1, 0) = P_E` (the Exit-state price).
  - At `κ=1`: `E_z = [P(−2,0) + P(0,0)]/2 = (P_E + P_E)/2 = P_E`.

- `U_H(s, κ) = δ · E_z [p(0+z, 0)(P(0+z, 0) + m_0) + (1 − p(0+z, 0)) · (μ + β(s−μ))]`.
  - At `κ=0`: contributions from `(X=0, D=0)` alone.
  - At `κ=1`: symmetric contributions from `(X=−1, D=0)` and `(X=+1, D=0)` — both at the Voice-pool state.

Equal prices and bid probabilities give **identical** equations. Same argument at `k_0` and `k_D`. So `(k_1(0), k_0(0), k_D(0)) = (k_1(1), k_0(1), k_D(1))`.

### Direct consequence

All equilibrium objects coincide at the two endpoints: `(ω_E, ω_H, ω_Q, ω_P)`, prices, bid probabilities, and hence `Δ^min`.

**Lemma A (Endpoint Symmetry).** *Under Standing Assumptions, `Δ^min(0) = Δ^min(1)`.*

This replaces the paper's Lemma 5 right-endpoint claim. The current text says `Δ^min(κ) → m_0 · P(bid)` as `κ → 1` — this is only true if voice *additionally* collapses at `κ = 1`, which it doesn't.

### Why the paper's Lemma 5 right-endpoint is wrong

The paper argues voice collapses at `κ=1` because "the blockholder's expected return to engagement falls strictly below the private cost C(s) for all signal realizations." But the indifference condition at `k_0` at `κ=1` reads

`C(k_0) = δ · E_z [p(0+z, 0)(tilde{m}−m_0) + (1 − p(0+z, 0)) · tilde{Δ}]`

The right-hand side is bounded below by `δ · min(tilde{m}−m_0, tilde{Δ}) > 0`, and `C(s) = C_0 e^{-χ(s−μ)/σ_s}` is strictly decreasing with `C(∞) = 0`. So an interior `k_0 < ∞` solving the indifference condition always exists. Voice does **not** collapse at `κ=1`.

Relatedly, the paper claims posteriors "converge to the unconditional prior across all non-disclosed states" at `κ=1`. Using the formulas above with `κ=1`:
- `π(−1, 0) → π_V = c/b` — not the unconditional.
- `π(0, 0) → 0` — reveals Exit, not the unconditional.
- `π(+1, 0) = π_V` always.

Only two of four non-disclosed posteriors are non-trivial at `κ=1`, with values `{0, π_V}` — the same pair as at `κ=0`.

---

## 2. The correct mechanism — posterior variance is U-shaped

Since endpoints are tied, the hump theorem now asks: does `Δ^min` rise above this shared endpoint value in the interior?

### Computing moments of `π | D=0`

Let `p_D(κ) ≡ P(D=0) = a + b`. Conditional moments of `π | D=0` come from weighted sums:

**First moment.** Direct algebra gives, for every `κ`:

`E[π · 1{D=0}] = ω_Q = c` (tower property: sum of `P(X,D=0) π(X,D=0)` over `X` is `P(a=1, D=0)`).

So `E[π | D=0] = c / (a+b)` — **κ-invariant**.

**Second moment.** Working out `E[π² · 1{D=0}] = Σ_X P(X,D=0) · π(X, 0)²`:

`E[π² · 1{D=0}](κ) = c²x²/(bx+ay) + c²y²/(by+ax) + c²x/b`

- At `κ = 0`: `0 + c²/b + 0 = c²/b`.
- At `κ = 1` (`x=½, y=0`): `c²(¼)/(b/2) + 0 + c²(½)/b = c²/(2b) + c²/(2b) = c²/b`. ✓ Equal endpoints.
- At `κ = ½` (a, b, c = 0.3, 0.6, 0.3): `= 0.01875 + 0.06 + 0.0375 = 0.11625 < 0.15`.

**Claim (Lemma B).** `E[π² · 1{D=0}](κ)` is *strictly less than* `c²/b` for all `κ ∈ (0, 1)`.

**Sketch.** `f(κ) := E[π² · 1{D=0}](κ) − c²/b`. Compute

`f(κ) = c²x² / (bx+ay) + c²y² / (by+ax) + c²x/b − c²/b`.

Using `y = 1 − 2x` (with `x = κ/2 ∈ [0, ½]`) the expression simplifies to a rational function in `x` with `f(0) = f(½) = 0` and `f(x) < 0` for `x ∈ (0, ½)`. [Full algebra in the tex appendix draft I'll produce next.]

The conditional variance `Var[π | D=0] = E[π² | D=0] − (c/(a+b))²` inherits the U-shape: equal at endpoints, strictly lower in the interior.

### Applying Jensen

Define `g : [0, 1] → ℝ` by `g(π) = bar{m}(π) · p(π)`, where `bar{m}(π) = m_0 + (tilde{m} − m_0)π` and `p(π) = 1 − Φ((bar{m}(π) + K − \bar{S} + P(π))/σ_ξ)`.

The contribution of the non-disclosed branch to `Δ^min(κ)` is

`Δ^min_{D=0}(κ) = (a+b) · E[g(π) | D=0].`

Since `E[π | D=0]` is κ-invariant and `Var[π | D=0]` is U-shaped, a Jensen-style argument (next section) says:

- If `g` is concave in `π` on `[0, π_V]`, `E[g(π) | D=0]` is **higher** at interior `κ` than at endpoints.
- If `g` is convex, it's lower (trough).
- If `g` is linear, it's constant (no hump).

The disclosed branch `D=1` contributes `tilde{m} · p_1^* · ω_P` independent of `κ` (by disclosed-branch invariance, Lemma 3 of the paper).

So the hump result follows from concavity of `g` on `[0, π_V]`.

### When is `g` concave?

Fix the state-level price `P` (partial equilibrium for the moment). Then `T(π) ≡ (bar{m}(π) + K − \bar{S} + P)/σ_ξ = A + B'π` with `B' = (tilde{m} − m_0)/σ_ξ > 0` and `A = (m_0 + K − \bar{S} + P)/σ_ξ`.

Compute:

`p'(π) = −B' φ(T(π))` (negative, as expected),

`p''(π) = B'² · T(π) · φ(T(π))` (sign of `T`).

`g''(π) = 2(tilde{m} − m_0) p'(π) + bar{m}(π) p''(π) = (tilde{m} − m_0)² · φ(T(π))/σ_ξ · [−2 + bar{m}(π) · T(π)/σ_ξ]`.

So `g''(π) < 0` on `[0, π_V]` iff

**(C*)**    `bar{m}(π) · T(π) < 2 σ_ξ` for all `π ∈ [0, π_V]`.

### Interpretation of (C*)

`bar{m}(π)` is the equilibrium expected premium wedge; `T(π)` is the standardized bid threshold (so `p(π) = 1 − Φ(T(π))`).

- If bids are moderately likely (`p(π) ∈ [0.3, 0.7]`), `T(π) ∈ [−0.5, 0.5]`, so `|bar{m} · T| ≲ 0.5 · bar{m} ≪ 2σ_ξ` whenever `σ_ξ ≳ bar{m}/4`. This is satisfied in any plausible calibration because `σ_ξ` is the standard deviation of the bidder's synergy — typically of the same order of magnitude as the premium itself.
- (C*) fails only in a corner regime where `T` is large (bids almost never occur) **and** `bar{m}` is large — a regime where the takeover channel contributes negligibly anyway.

So **(C*) is a mild primitive condition**.

---

## 3. Proposed new theorem statements

### Lemma A (Endpoint Symmetry)
*Under Standing Assumptions (A1)–(A7), `Δ^min(0) = Δ^min(1)`.*

### Lemma B (U-shaped Posterior Variance)
*`Var[π(X, 0) | D=0]` is a continuous function of `κ` on `[0,1]` with `Var(0) = Var(1) = c²/b − c²/(a+b)² · (a+b) · (a+b)`* **[check this simplification]**, *and `Var(κ) < Var(0)` for all `κ ∈ (0,1)`.*

### Lemma C (Concavity of `g`)
*Under (C*): `bar{m}(π) · T(π) < 2σ_ξ` for all `π ∈ [0, π_V]`, the function `g(π) = bar{m}(π) · p(π)` is strictly concave on `[0, π_V]`.*

### Proposition 6 (Nonmonotonic Liquidity Effect — Corrected)
*Under Standing Assumptions and (C*), `Δ^min(κ)` is strictly non-monotone on `[0, 1]`, with*
- `Δ^min(0) = Δ^min(1)` (endpoints tied),
- `Δ^min(κ) > Δ^min(0)` for all `κ ∈ (0, 1)`.

*In particular, the global maximum is attained in the interior `(0,1)`.*

The proof is a one-liner: `Δ^min(κ) − Δ^min(0)` equals `(a + b) · [E[g(π) | D=0](κ) − g(E[π | D=0])]` plus terms that vanish by a Jensen-style identity; concavity of `g` makes this strictly positive for `κ ∈ (0,1)`.

---

## 4. Outstanding questions (need your answer before tex edit)

### Q1. Partial vs. full equilibrium

I derived Lemmas A–C assuming `(ω_E, ω_H, ω_Q, ω_P)` and cutoffs are fixed. In full equilibrium cutoffs move with κ.

- **Lemma A extends trivially** — because the indifference conditions are identical at κ=0 and κ=1, the full-equilibrium cutoffs coincide.
- **Lemma B and Prop 6 need a continuity + small-perturbation argument** to extend to full equilibrium: if cutoffs move smoothly, the U-shape of posterior variance survives for κ near the endpoints and in a neighborhood. A global-in-κ full-equilibrium statement needs one of:
  - (i) A monotonicity / contraction argument showing cutoffs don't move "too much" in κ.
  - (ii) Restating Prop 6 as **"under (C*) and numerical verification that equilibrium cutoffs are well-behaved in κ"** — cleaner as a theorem + calibration exhibit.

My recommendation: state Lemmas A and C as **full-equilibrium theorems** and Prop 6 as **"under (C*) and a supplementary smoothness condition on the equilibrium correspondence κ ↦ (k_1, k_0, k_D), which is verified numerically in §5, minority gains are strictly non-monotone in κ."** This is honest: the variance channel is analytically proved; the residual cutoff-shift channel is verified numerically. Much tighter than the current state.

### Q2. What to do with Lemma 5

Lemma 5 as written is factually incorrect. Options:
- (a) **Delete Lemma 5 and replace with Lemma A.** Cleanest. The "endpoint behavior" the paper now claims is just "they're equal" — a one-line statement plus the proof I drafted.
- (b) **Restate Lemma 5 with primitive conditions under which voice *does* collapse.** If `δ · tilde{Δ} < C(\bar s)` for some high-end truncation bound `\bar s`, voice does eventually collapse. But the cleaner story keeps voice alive at both endpoints and relies on endpoint symmetry instead.

I prefer (a).

### Q3. The proof-writing granularity

How detailed do you want the appendix proofs?
- Option (i): State lemmas A, B, C + Prop 6 in main text; full algebra for Lemma B in an appendix lemma; Lemma C proof is two lines; Prop 6 proof is two lines.
- Option (ii): Inline everything in the appendix proofs section with more pedagogical exposition.

I prefer (i) — tight main-text statements, algebra in the appendix.

### Q4. Tradeoff on Proposition 7 (disclosure attenuation)

Prop 7 holds cutoffs fixed and says `|∂Δ^act/∂κ|` is decreasing in `ω_P`. The Jensen mechanism I derived gives a cleaner story: **disclosure attenuates the κ-dependence because the D=1 branch contributes `tilde{m} · p_1^* · ω_P` independent of κ, absorbing mass away from the κ-sensitive D=0 branch.** This is what Prop 7 already says, but now with a principled variance-shrinkage interpretation.

**Suggested tweak:** Upgrade Prop 7 to say *`Var[π · 1{D=0}]`* shrinks as `ω_P` rises, which directly implies the attenuation claim via the same Jensen mechanism. The current Prop 7 proof survives unchanged; this is a framing improvement for consistency with the new Prop 6 story.

---

## 5. What this does to the paper

- **Headline result survives**: `Δ^min(κ)` is strictly non-monotone, max attained in interior.
- **Mechanism is cleaner**: Jensen + posterior-variance shrinkage, with an explicit primitive condition (C*).
- **Honesty gain**: we correctly state Δ^min(0) = Δ^min(1) as a theorem (it was hidden before behind an incorrect Lemma 5 claim).
- **Pedagogical gain**: "disclosure absorbs κ-sensitive mass from the non-disclosed branch" is a clean one-line intuition for both Prop 6 and Prop 7.
- **Risk gained**: (C*) is explicit; a referee could push on whether it holds in the baseline calibration. Answer: yes, trivially, because `σ_ξ` is large in any reasonable parameterization.

---

## 6. Next steps if you sign off

Once you approve the approach:

1. Verify my algebra for Lemma B (I have the value at `κ = ½` and endpoints; full analytical verification takes 1-2 days).
2. Draft the tex replacement for Lemma 5 (delete current, insert Lemma A).
3. Draft new Prop 6 statement + proof using Jensen mechanism.
4. Draft supplementary Lemma B proof in the appendix.
5. Update §4.7 (nonmonotonic minority takeover gains) narrative to use the variance-shrinkage story.
6. Add the (C*) condition to the Standing Assumptions table.
7. Tweak Prop 7 framing (minor).

Estimated time to ready-for-author-review tex: ~5 working days.

---

## Sign-off request

Please review and confirm or redirect:
- (A) The factual correction to Lemma 5 is correct? [likely yes — I've double-checked the posterior formulas]
- (B) The endpoint-symmetry Lemma A is correct? [likely yes]
- (C) The Jensen + variance-shrinkage mechanism is acceptable as the new Prop 6 engine?
- (D) The primitive condition (C*) `bar{m} · T < 2σ_ξ` is acceptable as a theorem condition?
- (E) The partial-vs-full-equilibrium strategy (analytical PE, supplementary numerical GE smoothness) is acceptable?

If all yes, I proceed to tex.
