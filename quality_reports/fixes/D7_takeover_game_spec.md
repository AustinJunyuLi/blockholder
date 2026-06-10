# D7 Spec — The Disagreement-Node Tender Game (pinning λ)

**Date:** 2026-06-10 · **Workstream:** Theorem A (nine-month milestone plan)
**Target:** derive the appropriability coefficient λ of Condition BG (`cond:bg`, draft l.2469–72) from a complete tender-game equilibrium, closing the gap stated at draft l.2440–41 and D4 header ("five earlier attempts ... did NOT close").

## Why this attempt closes where the five earlier ones did not

The earlier attempts failed the circularity test: asserting λ>0 as a lemma relabels the assumption. D7 instead **solves the complete tender game at the disagreement node** so that λ is an *equilibrium output* with primitive arguments. The structural residue moves down one altitude level: from a condition on an endogenous bargaining object (the threat point d(1)−d(0)) to conditions on the disagreement-node *environment*:

- `q ∈ [0,1]` — probability a fringe raider is viable at the disagreement node (entry cost c_F ~ H, dilution cap φ: q = H(φ̄·φ-margin));
- `γ ∈ [0,1]` — **portability** of the activist's improvement under a fringe acquirer (γ=1: improvement survives a change of control — complements; γ=0: the raider's plan supersedes it — substitutes);
- `α, τ` — bloc stake and control threshold; **pivotality** = {1−α < τ} (the float alone cannot deliver control);
- `φ ≥ 0` — charter-permitted dilution of non-tendering shareholders (Grossman–Hart exclusion device);
- `S_F ~ G` — fringe synergy distribution.

λ>0 then holds on an **open set of primitives** and fails on a **characterized, economically meaningful boundary** — not by assumption.

## The game (one stage-game, solved exactly)

Setting: bargaining with the incumbent bidder has broken down (the disagreement node of App B). Firm's per-share standalone value: `w + a·Δ_eng` (a ∈ {0,1} = engagement success state; ρ-folds applied at the end exactly as Lemma `lem:bg-tree`).

Players: fringe raider (cost c_F ~ H, synergy S_F ~ G, both drawn at the node); bloc (stake α, strategic); atomistic float (measure 1−α).

Timing:
1. Raider observes (c_F, S_F), chooses enter / stay out; if enter, posts a uniform unrestricted tender offer b̂ for control threshold τ.
2. Float members tender atomistically (free-ride: tender iff b̂ ≥ post-raid value of a retained share). Bloc tenders strategically (iff b̂ ≥ its blocking payoff when pivotal).
3. If raider obtains ≥ τ: control transfers; post-raid per-share value `w + γ·a·Δ_eng + S_F`, non-tendered shares worth that minus dilution φ. Else status quo `w + a·Δ_eng`.

Equilibrium (GH logic):
- Float free-rider floor: b̂* = w + γaΔ_eng + S_F − φ (raider nets exactly φ per acquired share; standard GH selection: indifferent float tenders).
- **Non-pivotal regime** (1−α ≥ τ): raid succeeds iff entry pays: c_F ≤ (1−α)φ (per-share dilution on the float covers cost — define q accordingly). Bloc takes the post-raid value either way.
- **Pivotal regime** (1−α < τ): raid additionally requires the bloc's shares: bloc tenders iff b̂* ≥ w + aΔ_eng ⇔ S_F − φ ≥ (1−γ)aΔ_eng. Raising b̂ above the float floor is strictly unprofitable on float shares, so the raid happens iff the floor already clears the bloc's blocking value.

Threat point (bloc per-share continuation at the node):
- Non-pivotal: d(a) = w + q·[γaΔ_eng + E(S_F − φ | raid)] + (1−q)·aΔ_eng
- Pivotal: d(a) = w + aΔ_eng + q·E[(S_F − φ − (1−γ)aΔ_eng)⁺]

## Main results (to prove in D7.tex)

**Lemma D7.1 (free-rider floor & raid sets).** Equilibrium offer b̂* and the raid sets above; existence/uniqueness of the tendering equilibrium under the GH selection.

**Proposition D7.2 (λ derived).** d(1) − d(0) = λ·Δ_eng with

- non-pivotal: **λ = 1 − q(1−γ)**
- pivotal: **λ = 1 − q(1−γ)·ψ**, ψ = (1/((1−γ)Δ_eng)) ∫₀^{(1−γ)Δ_eng} P(S_F − φ ≥ t) dt ∈ [0,1]

(unified: λ = 1 − q(1−γ)ψ with ψ=1 when non-pivotal). λ ∈ [0,1] always — Condition BG's *form* is derived, not assumed.

**Theorem D7.3 (A3 from primitives).** λ > 0 — hence m̃ > m0 given θ<1, ρΔ_eng>0 — **iff NOT** [q = 1 and γ = 0 and (non-pivotal or P(S_F − φ ≥ Δ_eng) = 1)]. In words: A3 fails only when a fringe raid is (i) certain, (ii) fully supersedes the activist's improvement, and (iii) cannot be blocked (or blocking protects nothing). Comparative statics: λ ↓ q, λ ↑ γ, λ jumps up at pivotality (α crossing 1−τ); φ raises q but thins the pivotal tail (signed per-regime).

**Proposition D7.4 (AFS sign-reversal / measured premia).** With the wedge m1−m0 = (1−θ)λρΔ_eng and the body's price channel (activism premium in P, Prop 3) + deterrence (∂p/∂π<0), the *measured* premium (offer over a price that already capitalizes activism) falls with activism whenever λ < λ_crit(price-channel strength) — the model rationalizes AFS (JFE 2022)'s −13.7% as the low-portability/strong-fringe region while m1 ≥ m0 holds throughout. Formal statement on measured premium M(π) ≡ (P+m̄)/P − 1 decreasing in π iff m̄/P elasticity condition; numerical illustration in d7 check.

## Folding back into App B

Condition BG → **Lemma (derived)**; Theorem `thm:bg-A3` → unconditional given game primitives; wedge formula m1−m0 = (1−θ)λρΔ_eng with λ = 1−q(1−γ)ψ; reconciliations R1–R3 reinterpreted (the one-parameter family now indexed by observable-ish primitives); Remark `rem:bg-threat-honest` honesty language updated (heuristic → solved game), keeping an honest-residue paragraph: what the game still abstracts from (no bidder competition dynamics, exogenous φ and τ, one-shot fringe).

## Verification plan (d7_takeover_game_check.py)

1. Monte-Carlo the game (draws of c_F, S_F) vs closed forms for d(a), λ, both regimes — equality to MC error.
2. ψ ∈ [0,1], λ ∈ [0,1] across a primitive grid; boundary cases (q∈{0,1}, γ∈{0,1}, pivotal flip).
3. Theorem D7.3 iff-condition: enumerate primitive grid, check λ>0 classification matches.
4. Calibration consistency: exhibit primitives with (1−θ)λρΔ_eng = 0.20 and m0 = 0.10 (θ=0.5, ρ=0.9, γ=0.6, q=0.5, ψ=0.8 ⇒ λ=0.84, Δ_eng≈0.529); attainability of body baseline.
5. Prop D7.4: measured-premium reversal region nonempty under baseline-adjacent calibration.

JSON output to quality_reports/fixes/d7_takeover_game_check.json.
