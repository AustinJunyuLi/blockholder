# Adversarial Math Review — D7: Tender-Game Microfoundation of the Premium Wedge

**Date:** 2026-06-11
**Reviewer:** independent re-derivation + numerical falsification (no repo files edited)
**Files reviewed:**
`quality_reports/fixes/D7_takeover_game_spec.md`, `quality_reports/fixes/D7_takeover_game_microfound.tex`,
`numerical/takeover_game.py`, `quality_reports/fixes/d7_takeover_game_check.py` / `.json`,
`draft_v2.tex` (abstract l.84, §Tender-game micro-foundation l.286–290, eq:bid-prob l.319–322, eq:pricing l.349–355, A5a l.678–698, App `app:bg` l.2464–2674, splice at l.2680).

---

## Verdict: **SOUND-WITH-ISSUES**

The headline outputs survive independent verification **under one unstated domain restriction (α < τ_c)**: the closed form λ = 1 − q(1−γ)ψ, the threat-point values d(a) in both regimes, the wedge mapping m₁−m₀ = (1−θ)λρΔ_eng, Theorem d7:A3's iff boundary, the comparative statics of Remark d7:compstat, and the existence of λ_crit > 0 in Proposition d7:afs are all correct, and `takeover_game.py` implements the TeX formulas with no drift (verified to 1e-14). However: (i) the supporting equilibrium lemmas (d7:floor, d7:entry, d7:bloc) are **false as stated** — the raider has a profitable "top-up" deviation in the pivotal blocking region, confirmed by best-response simulation — so Proposition d7:lambda is currently *unproven as written* even though its conclusion is correct (the deviating raids hold the bloc exactly at its reservation, so d(a) is unchanged); (ii) the λ formula is wrong on the unhandled subdomain α ≥ τ_c (true λ = 1 there); (iii) one standalone clause of Proposition d7:afs ("P′(π) > 0 whenever Δ̃ > 0") is false at general λ — I found counterexamples satisfying A5a; and (iv) the ρ² fold re-asserted by Remark d7:fold rests on an economically unidentified second Bernoulli draw inherited from Lemma bg-tree.

**Issue counts: 1 CRITICAL · 3 MAJOR · 6 MINOR.** All are repairable without changing any headline formula or numerical result.

---

## (a) The tender subgame equilibrium

### What checks out

**Float free-riding.** An atomistic float member is never pivotal; with a *conditional* offer, failure pays y(a) under either action, so her decision is pinned by the success-conditional comparison: tender (b̂) vs. retain a diluted share (Z(a)−φ). Tender iff b̂ ≥ Z(a)−φ, with the Grossman–Hart selection resolving indifference toward tendering. Correct, and the equilibrium concept (SPE + GH indifference-tendering selection, Bagnoli–Lipman finite foundation cited, Holmström–Nalebuff mixed equilibria explicitly *not* selected) is stated once and used consistently. The "all-or-none is without loss" claim for the bloc is also correct: at a uniform price, tendered and retained shares have identical per-share values at the floor, and at any b̂ > Z−φ tendering all is weakly dominant.

**Raider payoff identity at the floor.** With tendered mass m ≥ τ_c at b̂* = Z−φ: margin (Z − b̂*) = φ on m acquired shares plus dilution φ on (1−m) retained shares = φ·1, independent of m and of (a, S_F). Verified; this is what makes entry depend only on {c_F ≤ φ} *at the floor*.

### What fails — the top-up deviation (CRITICAL, D7-1)

Lemma d7:floor claims the floor b̂* = Z(a)−φ is the offer "in **every** subgame-perfect tendering outcome … in which the raid succeeds with positive probability," and Lemma d7:bloc(ii) claims that off the acquiescence set {S_F ≥ φ + (1−γ)a δ_e} "the raid fails." Both are false in the pivotal regime. Re-derivation:

In the **blocking region** S_F < φ + (1−γ)a δ_e, equivalently y(a) > Z(a)−φ, consider the uniform conditional offer b̂ = y(a):

- float: y(a) > Z(a)−φ ⟹ strictly tenders;
- bloc: indifferent (y(a) either way) ⟹ tenders under the stated selection;
- tendered mass = 1 ≥ τ_c ⟹ success.

The raider acquires the full register at y(a), each share worth Z(a), no minority left to dilute:

> payoff = Z(a) − y(a) − c_F = **S_F − (1−γ)a δ_e − c_F**,

which is **strictly positive** on the nonempty positive-measure set
{ (1−γ)a δ_e + c_F < S_F < φ + (1−γ)a δ_e } ∩ {c_F < φ}
(nonempty whenever H puts mass below φ and G puts mass on that interval). The proof's "one-line computation" asserting this deviation is "dominated by not entering whenever the floor fails the bloc" is wrong: it implicitly compares the top-up payoff to the floor payoff φ − c_F (true: S_F − (1−γ)aδ_e < φ in the blocking region), but the relevant comparison is to **zero**, since the floor offer *fails* there.

**Numerical confirmation** (4×10⁶ draws, pivotal, a=1, q=0.5, γ=0.6, φ=0.12, μ_S=0.6, δ_e=0.5):

| object | claimed eq. | best-response eq. |
|---|---|---|
| raid probability | 0.2933 (= q·Ḡ) | 0.3248 |
| raider's mean gain on the extra (top-up) raid set | — | +0.0012 > 0 |
| bloc value d(1) | 1.67609 | 1.67609 (= closed form 1.67599 ± MC) |
| raid prob. at a=0 vs a=1 | state-blind | 0.4530 vs 0.3248 — **not** state-blind |

**Why Proposition d7:lambda survives anyway.** In every top-up raid the bloc is paid exactly its reservation y(a), contributing zero to d(a) − y(a). Hence

d(a) = y(a) + P(c_F ≤ φ)·E[(S_F − φ − (1−γ)a δ_e)⁺]

holds **exactly** in the corrected equilibrium — the standard outside-option principle: marginal raids extract the bloc's full surplus. So eq. (d7-dP), λ, Corollary d7:BG, and Theorem d7:A3 are all *correct*, but currently rest on false lemmas (unproven as stated). The narration around Lemma d7:entry ("the raider's profit … is always φ − c_F"; "State-blindness of entry is the economically important part") is also false in the corrected equilibrium: entry/raid probability is state-dependent through top-ups (and engagement *deters* top-up raids); what is state-blind is the **bloc-surplus-relevant raid margin** (the floor raids), which is the correct economic statement to keep.

### Second failure — bloc-alone control (MAJOR, D7-2)

The stated primitives allow α ≥ τ_c (e.g., α = 0.6, τ_c = 0.5, which the TeX classifies "pivotal" since 1−α < τ_c). There the bloc **alone** delivers control, and the raider's cheapest successful coalition is the bloc-only lowball b̂ = y(a): on the acquiescence set the float refuses (y < Z−φ), the bloc tenders (selection), mass α ≥ τ_c succeeds, raider payoff α(Z−y(a)) + (1−α)φ = φ + α(Z−y(a)−φ) ≥ φ, strictly preferred to the floor. The bloc then receives y(a) in *every* raid ⟹ d(a) = y(a) ⟹ **true λ = 1**, while the formula gives 1 − q(1−γ)ψ (= 0.8607 at the test point). Theorem d7:A3's failure boundary is also wrong on this subdomain (cells with q=1, γ=0, 1−α ≥ τ_c, α ≥ τ_c are classified λ=0 but truly have λ=1). The proof of Lemma d7:floor contains the garbled clause "impossible since α<1≤τ_c+(1−α) would require α≥τ_c", i.e., it silently invokes α ≤ τ_c, which is **never stated**. Fix: add the primitive assumption **α < τ_c** ("the bloc alone cannot deliver control") — economically innocuous (baseline α=0.30, τ_c=0.75 satisfies it) and it restores every statement outside the blocking-region issue above.

---

## (b) Re-derivation of λ = 1 − q(1−γ)ψ

**Non-pivotal.** d(a) = (1−q)(w + aδ_e) + q(w + γaδ_e + E[S_F] − φ). Differencing:
d(1) − d(0) = (1−q)δ_e + qγδ_e = δ_e[1 − q(1−γ)]. ✓ (λ = 1 − q(1−γ), ψ ≡ 1.)

**Pivotal.** d(a) = y(a) + q·E[(X − ca)⁺] with X ≡ S_F − φ, c ≡ (1−γ)δ_e:
d(1) − d(0) = δ_e + q( E[(X−c)⁺] − E[X⁺] ) = δ_e − q∫₀ᶜ P(X ≥ t) dt,
using the layer-cake identity E[X⁺] − E[(X−c)⁺] = ∫₀ᶜ P(X > t)dt (valid for E|X| < ∞; P(X≥t) = P(X>t) a.e. by atomlessness). Substituting P(X ≥ t) = Ḡ(φ+t) and ∫₀ᶜ Ḡ(φ+t)dt = c·ψ with c = (1−γ)δ_e gives
d(1) − d(0) = δ_e[1 − q(1−γ)ψ]. ✓ Algebra verified line-by-line; the Fubini step is sound. (Caveat: **E[S_F] < ∞** is needed both here and for eq:d7-dNP, but the standing assumption on G states only atomlessness — D7-6.)

**Edge cases** (all consistent with the TeX's claims, conditional on α < τ_c):

| corner | formula | sense check |
|---|---|---|
| q = 0 | λ = 1 | no fringe ⟹ bloc keeps full improvement ✓ |
| q = 1, γ = 0, ψ = 1 | λ = 0 | raid certain, superseding, unblockable ✓ (exactly F1∧F2∧F3) |
| γ = 1 (or δ_e = 0) | λ = 1 | c = 0 ⟹ ψ-term annihilated; improvement portable ✓ (TeX's convention handles ψ's 0/0 correctly) |
| ψ = 0 (Ḡ(φ⁺) = 0) | λ = 1 | no fringe ever clears the bloc's reservation ⟹ all raids blocked ⟹ d(a) = y(a) ✓ |
| ψ = 1 (Ḡ ≡ 1 on the interval) | λ = 1 − q(1−γ) | blocking never binds ⟹ collapses to non-pivotal ✓ |
| pivotal vs non-pivotal | λ_piv − λ_nonpiv = q(1−γ)(1−ψ) ≥ 0 | "pivotality protects the threat point" ✓ (jump at q=0.8, γ=0.3 re-derived by hand: 0.21266, matches JSON 0.21262) |

**Comparative statics (Remark d7:compstat).** (i) ∂λ/∂q = −(1−γ)ψ ≤ 0 ✓ (ψ is q-free). (ii) (1−γ)ψ = (1/δ_e)∫₀^{(1−γ)δ_e} Ḡ(φ+t)dt, so ∂λ/∂γ = q·Ḡ(φ+(1−γ)δ_e) ≥ 0 ✓ (Leibniz; continuity of Ḡ from atomlessness). (iv) ∂λ/∂φ = −(1−γ)ψH′(φ) + (q/δ_e)[Ḡ(φ) − Ḡ(φ+(1−γ)δ_e)] ✓ — genuinely two-edged as claimed; but the promised numerical verification of both φ-directions is **absent from the check script** (D7-8).

**Theorem d7:A3 boundary.** q(1−γ)ψ = 1 with each factor in [0,1] ⟺ each equals 1. Given γ=0 pivotal: ψ=1 ⟺ Ḡ(φ+t)=1 a.e. on (0, δ_e) ⟺ (monotonicity + continuity from atomlessness) P(S_F ≥ φ+δ_e) = 1. ✓ The iff is correct as stated — on the α < τ_c domain (see D7-2).

**Fold (Remark d7:fold) — and the ρ² question (MAJOR, D7-4).** The within-appendix step is exact: with a ∈ {0,1} binary, d(a) is trivially affine in a; taking E over B₁ ~ Bern(ρ) gives expected shift ρλ(Δ_eng)Δ_eng = λ·D̃_eng, with the honest flag that λ(·) is evaluated at the realized Δ_eng. ✓ The problem is the *composition with the body*: m̃−m₀ = ρ²(1−θ)λΔ_eng requires Lemma bg-tree's two **independent** draws — B₁ ("engagement success … realizing the improvement") and B₂ ("premium-state arrival"). But the body (draft l.282–284) defines m̃ = m₀ + ρ(m₁−m₀) with ρ explicitly the probability that *engagement succeeds* — the same event that realizes the improvement. Under the body's single-event reading, m₁ is the premium conditional on campaign success, in which event the disagreement-node improvement is Δ_eng with certainty, giving m₁−m₀ = (1−θ)λΔ_eng and m̃−m₀ = ρ(1−θ)λΔ_eng — a **single ρ**. The two-draw reading also sits oddly with the standalone branch, where Δ̃ = ρΔ folds only once. "Premium-state arrival" is never given economic content independent of campaign success. This is inherited from Appendix B (D4), but Remark d7:fold *re-asserts* it ("No approximation is involved … preserving m̃−m₀ = ρ²(1−θ)λΔ_eng"), so it is in D7's scope. Quantitative consequence: under single-ρ, the calibration cell solves 0.20 = (1−θ)λ(Δ)Δ (no ρ), shifting Δ_eng ≈ 0.516 → ≈ 0.46; signs and architecture unchanged. Fix: either give B₂ independent content and align the body's description of m̃, or adopt the single-ρ fold and recalibrate.

---

## (c) Code vs TeX (`numerical/takeover_game.py`)

**No sign or normalization drift.** Verified by independent recomputation:

- `pivotal` ⟺ 1−α < τ_c ✓ (matches TeX definition; baseline 0.70 < 0.75 pivotal ✓).
- `survival` = Ḡ for S_F = s_min + Exp(μ_S) ✓.
- `psi` decomposes ∫_φ^{φ+c} Ḡ(u)du into the Ḡ≡1 segment [φ, min(φ+c, s_min)] plus the exponential tail from max(φ, s_min); checked against numerical quadrature at five (γ, δ_e, φ, μ_S, s_min) points incl. s_min > 0: max |Δ| ≈ 2×10⁻¹⁴ ✓. Edge conventions (c ≤ 0 → ψ=1, harmless because multiplied by zero) match the TeX ✓.
- `appropriability` = 1 − q(1−γ)ψ ✓; `wedge(rho)` = (1−θ)λρΔ_eng ✓ = eq:bg-identify's m₁−m₀.
- `params_with_endogenous_wedge`: m₁ = m₀ + wedge(base.ρ); then `ModelParams.m_tilde` = m₀ + ρ(m₁−m₀) reproduces m̃−m₀ = ρ²(1−θ)λΔ_eng = 0.1800000000 exactly ✓ — consistent with the TeX's ρ² fold (and therefore carrying D7-4's conceptual issue, not introducing a new one).
- `calibrate_delta_eng`'s monotonicity claim: d/dΔ[λ(Δ)Δ] = 1 − q(1−γ)Ḡ(φ+(1−γ)Δ) > 0 — verified analytically and on a 400-point grid ✓.
- Baseline reproduces the JSON: λ = 0.8614452514, Δ_eng = 0.5159288344, wedge = 0.20 ✓.

**One gap (MINOR, D7-10):** no guard or documentation for the α < τ_c domain restriction. `TenderGameParams(alpha=0.6, tau_c=0.5)` silently returns λ = 0.8614 where the true game value is 1.0 (see D7-2).

---

## (d) Proposition d7:afs — the measured-premium reversal

**Differentiation. ✓** M = m̄/P ⟹ M′ = [(m̃−m₀)P − m̄P′]/P², giving the sign display (and the implied elasticity reading: M′ < 0 ⟺ dln m̄/dπ < dln P/dπ — "price capitalizes activism faster than the wedge"). Note M ≡ m̄/P equals (P+m̄)/P − 1, matching the prose "offer over price, net of one." ✓

**Implicit differentiation. ✓** With F(P,π) = δ[p(P+m̄) + (1−p)(E[v|X,D]+Δ̃π)] − P:
F_P = δp + δp_P(P+m̄−E[v]−Δ̃π) − 1, F_π = δ[p(m̃−m₀) + (1−p)Δ̃ + p_π(P+m̄−E[v]−Δ̃π)],
and P′ = −F_π/F_P reproduces the TeX display exactly. ✓

**λ→0 limit. ✓** m̃−m₀ = ρ²(1−θ)λΔ_eng → 0 and p_π = −φ(·)(m̃−m₀)/σ_ξ → 0 (π enters p only through m̄ — correct), so P′ → δ(1−p)Δ̃ / [1−δp−δp_P(P+m₀−E[v]−Δ̃π)] > 0 given the denominator is positive and p < 1. Then M′ → −m₀P′/P² < 0 (this needs **m₀ > 0**, used but not hypothesized — D7-6/minor), and since π ranges over the compact [0,1] and all objects are jointly continuous in (π, λ) under the contraction, sup_π M′(π; λ) < 0 for λ below some λ_crit > 0. **The existence claim and its proof are sound** (the "compact interior subsets" hedging is unnecessary — [0,1] is compact — but harmless).

**Is m₁ ≥ m₀ needed?** It is *implied* (wedge = (1−θ)λρΔ_eng ≥ 0 for λ ∈ [0,1]) rather than assumed, and it is not needed for the reversal — that is precisely the proposition's point ("M′ < 0 even though m₁ ≥ m₀ throughout"). It is used only for the sign p_π ≤ 0 in the composition remark. Consistent. ✓

**Two defects:**

1. **(MAJOR, D7-3)** The standalone clause "Then P′(π) > 0 whenever Δ̃ > 0" is asserted at *general* λ but proved only in the λ→0 limit — and it is **false** in general. The numerator sign is sgn[p(m̃−m₀) + (1−p)Δ̃ − (φ(t)/σ_ξ)(m̃−m₀)g] with g = P+m̄−E[v]−Δ̃π = [m̄−(1−δ)V̂]/(1−δp) > 0 typically; when Δ̃ is small relative to the wedge, the deterrence term wins. Grid search over (δ, σ_ξ, wedge, m₀, S̄−K, Δ̃) with **A5a verified at every grid point** found violations, e.g. δ=0.95, σ_ξ=0.25, m̃−m₀=0.2, m₀=0.1, S̄−K=1.1, Δ̃=0.005: min dP/dπ ≈ −0.02 (P falls with activism evidence because higher m̄ deters bids on a positive-surplus deal branch). Fix: restrict the clause to the λ→0 limit (as proved), or add the explicit condition p(m̃−m₀)+(1−p)Δ̃ > φ(t)(m̃−m₀)g/σ_ξ. The headline λ_crit result is unaffected (it needs only the limit).
2. **(MINOR, D7-5)** The proof justifies denominator positivity "by Assumption (A5), which bounds δ|p_P| away from the feedback singularity, and δp<1". The literal clauses δ|p_P| < 1 and δp < 1 do **not** imply 1 − δp − δp_P·g > 0 when g < 0 (the |g| factor is unbounded by them). The correct citation is the body's **A5a** (draft l.678–688), whose contraction bound δ[p + |P+m̄−V̂|φ(0)/σ_ξ] < 1 yields the denominator ≥ 1 − |Ψ′| > 0 directly — and the proof's later "uniform contraction" phrase shows A5a is what is meant. Worth also cross-referencing Remark rem:A5margins (draft l.695–698), which concedes the baseline does *not* satisfy the conservative sufficient form of A5a, so the numerical λ_crit = 0.07 rests on observed convergence rather than the maintained bound.

---

## (e) Check-script adequacy (`d7_takeover_game_check.py`)

| TeX claim | tested? | note |
|---|---|---|
| d(a) closed forms, both regimes | partially | check 1 Monte-Carlos the **claimed policy** (`enter = c_F ≤ φ`; pivotal raid iff acquiescence), *not* the game: there is no best-response verification over offers, so it **cannot detect D7-1** (the top-up deviation) or D7-2. It verifies algebra, not equilibrium. |
| Lemma d7:floor (offer optimality/uniqueness) | **no** | exactly where the error sits |
| Lemma d7:entry (raid prob = q; state-blindness) | **no** | false in the corrected equilibrium |
| ψ, λ ∈ [0,1]; λ↓q, λ↑γ; pivotal ≥ non-pivotal; jump | yes | exponential family only; fine since the general-G claims are proved analytically (and re-verified here) |
| Theorem d7:A3 iff (48 cells incl. s_min trick for F3) | yes | but `pivotal` is a free boolean — (α, τ_c) never exercised, so the α < τ_c restriction is invisible |
| Calibration (wedge 0.20, m̃−m₀ 0.18, λ 0.8614) | yes | reproduced this session, exact |
| Prop d7:afs reversal, λ_crit > 0 | yes | one calibration cell; grid step 0.01 → λ_crit = 0.07 |
| "P′(π) > 0 whenever Δ̃ > 0" | **no** | false at general λ (D7-3) |
| Remark d7:compstat(iv): φ two-edged "verify both directions numerically" | **no** | promised in the TeX, absent from the script (D7-8) |
| ρ² fold composition | trivially | only multiplies by ρ; cannot adjudicate D7-4 |

Reproduction: the script runs clean (`ALL CHECKS PASS`, all five checks, values match the committed JSON). Minor spec drift: the spec's calibration sketch (ψ=0.8, λ=0.84, Δ_eng≈0.529) differs from the delivered joint solve (ψ≈0.693, λ≈0.8614, Δ_eng≈0.516) — planning-document noise, not an error.

## (f) Hidden assumptions

1. **α < τ_c** — load-bearing and unstated; without it λ's closed form and Theorem d7:A3's boundary are wrong (D7-2). The garbled clause in Lemma d7:floor's proof is the fossil of this assumption.
2. **E[S_F] < ∞** — used in eq:d7-dNP and the layer-cake step (acknowledged parenthetically inside the proof, absent from the standing assumption "atomless on its support") (D7-6).
3. **m₀ > 0** — needed for strict negativity of the limiting M′ in Prop d7:afs; a body calibration fact, not a stated hypothesis.
4. **Offer space**: uniform, conditional, unrestricted, single round — declared as institutional ✓; but the ledger's discussion of the discriminatory-offer alternative has a **sign error** (D7-7): with discriminatory take-it-or-leave-it offers the raider pays the pivotal bloc exactly y(a) in every successful raid, so d(a) = y(a) and λ = **1** (its maximum), not "lower… toward its non-pivotal value." The conclusion that equal treatment is conservative for A3's failure region survives — equal treatment yields the *smallest* λ — but for the opposite reason than the text gives.
5. Bloc indifference resolved toward tendering (G-measure-zero event) — stated ✓. Engagement state a observable at the node — stated ✓. Tie-break at c_F = φ — measure zero under continuous H, harmless.
6. The "fold" requires λ evaluated at the realized Δ_eng (state-dependence of λ honestly flagged in Remark d7:fold ✓), and the **independence of B₂ from B₁** in Lemma bg-tree — the economically unidentified assumption behind ρ² (D7-4).

---

## Issue table

| ID | Severity | Location | Description | Suggested fix |
|---|---|---|---|---|
| D7-1 | **CRITICAL** | `D7_takeover_game_microfound.tex:105-116` (Lemma d7:floor), `:139-157` (Lemma d7:bloc, esp. the "one-line computation" at l.156), `:122-135` (Lemma d7:entry); spec `.md:32`; consequently Prop d7:lambda `:161-201` unproven as stated | In the pivotal blocking region the raider's optimal offer is the top-up b̂ = y(a), not the floor: it succeeds (selection makes the indifferent bloc tender; the float strictly tenders) and is strictly profitable on {(1−γ)aδ_e + c_F < S_F < φ+(1−γ)aδ_e}, a positive-measure set. Verified by BR simulation (+3.1pp raid mass, +0.0012 mean profit). Hence: floor-offer uniqueness false; "raid fails off the acquiescence set" false; raid probability ≠ q·Ḡ; raider profit not always φ−c_F; entry not state-blind (0.453 vs 0.325 across a). Proposition d7:lambda's conclusion is nevertheless **correct**: top-up raids pay the bloc exactly y(a), so d(a) and λ are unchanged. | Restate the lemmas with the corrected raid set (floor raids on the acquiescence set ∪ reservation-price top-up raids on the blocking set where S_F − (1−γ)aδ_e ≥ c_F); re-prove Prop d7:lambda via the outside-option principle (marginal raids contribute zero bloc surplus, so d(a) is as displayed); replace "state-blind entry" with "the bloc-surplus-relevant raid margin is state-blind." No downstream formula changes. |
| D7-2 | **MAJOR** | same file `:73` (Notation), `:115` (garbled clause "α<1≤τ_c+(1−α)"), `:161-181`, `:223-242`; `numerical/takeover_game.py:69-71` | Assumption **α < τ_c** (bloc alone cannot deliver control) is used but never stated. On α ≥ τ_c the raider lowballs the bloc-alone coalition at y(a) (payoff φ + α(Z−y−φ) ≥ φ on acquiescence), the bloc is held at reservation in every raid, and the true λ = 1, not 1−q(1−γ)ψ (0.8607 at test point); Theorem d7:A3's failure cells with α ≥ τ_c are misclassified. | State α < τ_c as a primitive in the Environment/Notation paragraph; repair the garbled clause in Lemma d7:floor's proof. Baseline (0.30, 0.75) satisfies it. |
| D7-3 | **MAJOR** | same file `:264` (Prop d7:afs clause "Then P′(π)>0 whenever Δ̃>0"), proof `:276-282` | Clause false at general λ and unproven (proof covers only λ→0). Counterexamples with **A5a verified pointwise** exist (e.g., δ=0.95, σ_ξ=0.25, m̃−m₀=0.2, m₀=0.1, S̄−K=1.1, Δ̃=0.005: dP/dπ < 0): the deterrence term p_π·g = −(φ(t)/σ_ξ)(m̃−m₀)g dominates (1−p)Δ̃ when Δ̃ is small relative to the wedge and the deal branch carries positive surplus g. | Restrict the clause to the λ→0 limit (all the λ_crit proof needs), or state the explicit sufficient condition p(m̃−m₀)+(1−p)Δ̃ > φ(t)(m̃−m₀)(P+m̄−E[v]−Δ̃π)/σ_ξ. |
| D7-4 | **MAJOR** | same file `:216-219` (Remark d7:fold, "composes exactly … preserving m̃−m₀=ρ²(1−θ)λΔ_eng"); `draft_v2.tex:2559-2565` (eq:bg-identify), `:2581-2594` (Lemma bg-tree) vs body `:282-284` | The ρ² fold needs two independent Bernoullis, but the body defines the m̃-fold ρ as the *campaign-success* probability — the same event that realizes the improvement at the node; "premium-state arrival" B₂ has no independent economic content, and the standalone branch folds only once (Δ̃=ρΔ). Single-event reading gives m̃−m₀ = ρ(1−θ)λΔ_eng (single ρ) and shifts the calibration (Δ_eng ≈ 0.46 vs 0.516); sign architecture unchanged. Inherited from App B but re-asserted by D7. | Either give B₂ independent content (improvement-survival-to-the-node risk distinct from campaign success) and align the body's description of m̃, or drop to the single-ρ fold and recalibrate Δ_eng. |
| D7-5 | MINOR | same file `:277` (proof of Prop d7:afs, IFT parenthetical) | Denominator positivity attributed to "A5, which bounds δ\|p_P\|" — insufficient without the \|P+m̄−V̂\| factor. The body's A5a (`draft_v2.tex:678-688`) is the bound that delivers it (and "uniform contraction" later in the proof shows it is intended). | Cite Assumption A5a explicitly; cross-reference rem:A5margins' baseline caveat for the numerical λ_crit. |
| D7-6 | MINOR | same file `:73` (Notation) | G assumed atomless only; **E[S_F] < ∞** is needed (E[S_F] in eq:d7-dNP; E\|X\|<∞ in the layer-cake step, acknowledged only inside the proof). Also m₀ > 0 used in Prop d7:afs without hypothesis. | Add "with finite mean" to the assumption on G; add m₀>0 to Prop d7:afs's hypotheses. |
| D7-7 | MINOR | same file `:299` (ledger, institutional-primitives paragraph) | Discriminatory-offers discussion has the comparative backwards: discrimination holds the pivotal bloc at y(a) in every raid ⟹ λ = 1 (maximal), not "lowers λ toward its non-pivotal value." The raid set does enlarge and the bloc's *level* drops, but the engagement *shift* rises. "Equal treatment is conservative for A3's failure region" remains true (equal treatment minimizes λ) — for the opposite reason. | Rewrite the parenthetical: discrimination kills the bloc's option-value level but maximizes the threat-point shift; equal treatment is conservative because it yields the smallest λ. |
| D7-8 | MINOR | same file `:250` (Remark d7:compstat(iv)); `d7_takeover_game_check.py` | TeX promises "verify both directions numerically" for the φ comparative static; no φ-sweep exists in the check script. | Add a check exhibiting ∂λ/∂φ < 0 and > 0 cells (e.g., vary H′(φ) via c_max). |
| D7-9 | MINOR | `d7_takeover_game_check.py:97-129` (`mc_game`) | "Monte-Carlo of the game" simulates the claimed equilibrium policy, not the game: no raider best-response check over the offer space, so checks 1–3 cannot detect D7-1/D7-2 by construction. | Add a BR verification: for each draw, compare the floor payoff against the top-up y(a) and bloc-only coalitions, and confirm the implemented policy is optimal (it is not, pivotal blocking region). |
| D7-10 | MINOR | `numerical/takeover_game.py:69-71, 99-102` | No guard/doc for α < τ_c; α ≥ τ_c silently returns the pivotal-formula λ (wrong; true value 1.0 — verified for α=0.6, τ_c=0.5). | `assert alpha < tau_c` (or document the domain) in `TenderGameParams`. |

---

## What was independently verified as correct

- λ = 1 − q(1−γ)ψ and both d(a) closed forms (re-derived; MC-confirmed including under the *corrected* equilibrium), conditional on α < τ_c.
- Theorem d7:A3's iff boundary, including the measure-theoretic step (a.e. + monotone + atomless ⟹ P(S_F ≥ φ+Δ_eng)=1) — on the α < τ_c domain.
- All comparative statics of Remark d7:compstat, including the pivotality jump (hand value 0.21266 vs JSON 0.21262).
- Corollary d7:BG's exact recovery of Condition BG's form, with the honest w′ = d(0) relabeling and the λ=0 caveat.
- `takeover_game.py` ⇄ TeX: exact agreement (ψ to 1e-14 vs quadrature; wedge mapping reproduces m₁=0.30, m̃−m₀=0.18; calibration map strictly increasing as documented).
- Prop d7:afs: the sign display, the IFT formula for P′, the λ→0 limit, and the existence of λ_crit > 0; the check script's λ_crit ≈ 0.07 reproduced.
- Check script reruns clean and matches the committed JSON exactly.
