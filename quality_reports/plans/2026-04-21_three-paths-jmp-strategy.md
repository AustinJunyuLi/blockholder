---
date: 2026-04-21
type: plan
status: Path A selected — others retained for future revisit
author: session with Claude
---

# Three JMP Strategy Paths — draft_v2.tex

Three credible paths for positioning "Liquidity, Activism Disclosure, and Takeover Premia" as a JMP. Derived from full literature survey (Edmans 2014, Maug 1998, Kahn-Winton 1998, Back et al 2018, Corum-Levit 2019, Burkart-Lee 2022, Ordóñez-Calafi-Bernhardt 2022, Cetemen et al 2022 WP, EGJ 2015, Kyle-Vila 1991, Bris 2002), deep-read against known theoretical weaknesses of the current draft, and calibrated against recent JMP placements (2023-2026 FTG prize pool).

**Selected:** Path A. **Retained for revisit:** Paths B and C.

---

## Shared premise (all three paths)

The positioning is defensible — none of the surveyed competitors produce the specific combination:
- Discrete four-action blockholder menu `{Exit, Hold, Quiet Voice, Public Voice}`
- Stake-triggered disclosure `D = 1 ⟺ q = +1`
- Humped minority takeover gains `Δ^min(κ)` in noise-trading intensity
- Endogenous bidder entry with synergy shock

Three senior-author papers explicitly invite this contribution (Edmans 2014 survey pp.25, 45; Burkart-Lee 2022 conclusion; Back et al. 2018 §7).

The *execution* has rigor gaps that determine placement tier, not the *position*.

---

## Path A — Tighten the current draft in place

**Timeline:** 6-8 months
**Outcome tier:** Top-20 to top-25 JMP
**Ambition level:** Moderate — defensible first-paper

### Work items (in priority order)

1. **Prop 6 (nonmonotonicity) — derive primitive-level sufficient conditions.** Current statement (line 554) literally assumes the conclusion: "Assume Δ^min(κ̃) > lim Δ^min(κ)…" This is the single biggest theoretical gap. Two sub-options:
   - (A1) Find conditions on `(C_0, χ, Δ, ρ, m_0, m_1, \bar S, K, σ_ξ, σ_v, σ_ε)` under which the boundary-dominance holds. Likely requires a calibration-based inequality like `C_0 < some function of other primitives`.
   - (A2) If analytical conditions are not derivable, honestly reframe as **Theorem (Endpoint Behavior) + Proposition (Hump under stated conditions on primitives, verified numerically in baseline)**. Numerical hump with analytical endpoints is acceptable at top-15 IF the analytical skeleton is tight.

2. **Prop 8 (GE disclosure tradeoff) — apply IFT to three-cutoff fixed point `T(k_1, k_0, k_D)`.** The author's own footnote (line 785) calls it a "heuristic." This must become a theorem. Implicit function theorem on the coupled cutoff equations, sign each Jacobian component, state sufficient conditions for transparency-effect-dominates vs deterrence-effect-dominates.

3. **Bidder bargaining — micro-found `m_0, m_1` from primitives.** Currently these are parameters. Replace with Nash bargaining between blockholder and bidder over synergy surplus `(S + ξ)`. With outside options from failed takeover, this delivers closed-form `m_0(primitives), m_1(primitives)`. Kills the "these are parameters" referee handle.

4. **Action set — show dominance of excluded actions.** `(+1, 0)` silent buy and `(−1, 1)` engaged exit currently excluded by fiat. Add a lemma: under A1-A7, these actions are strictly dominated. Removes another handle.

5. **A2 defense (engagement cost `C(s)` decreasing in `s`).** This reverses classical Maug/Kahn-Winton intuition. Either:
   - Defend in a new paragraph of §2.4 with a clear activism-as-catalyst story, or
   - Show main result survives if `C(s)` is flat; relegate monotone-decreasing to an extension.

6. **Welfare section — write a real planner problem.** Currently a paragraph of verbal logic. Needs: explicit social welfare function, FOC for `κ*`, characterization of sign `κ* − κ†`.

7. **Lit review updates.**
   - Cite **Ordóñez-Calafi & Bernhardt (2022, JFQA)** — the most direct competitor on disclosure-policy design you're not currently citing.
   - Cite **Cetemen-Cisternas-Kolb-Viswanathan (2022 WP)** — live faculty work in the same space.
   - Quote **Edmans (2014) p.25, p.45** and **Burkart-Lee (2022) conclusion** and **Back et al. (2018) §7** as explicit invitations.
   - Fix **EGJ 2015 citation** — it's AER 105(12), not RFS.

### What you keep

- Four-action menu architecture (core novelty)
- Stake-triggered disclosure as equilibrium trigger
- Discrete order flow + Bayesian market maker
- Static one-shot structure
- Partial equilibrium disclosure attenuation (Prop 7) — the one theorem that actually works

### Risks

- Even with all tightening, a static model with ~6 propositions places top-15 to top-25, not top-5 to top-10 (ref: Yu 2024 "General Theory of Holdouts" won FTG First Prize and placed Colorado)
- If primitive-level Prop 6 conditions prove intractable, the honest reframing as "numerical with analytical endpoints" caps the ambition at top-25

---

## Path B — Extend to continuous-time Back-CDF architecture

**Timeline:** 10-12 months
**Outcome tier:** Top-10 to top-15 JMP
**Ambition level:** Significant — directly answers Back et al. 2018 §7

### Core idea

Embed the four-action intuition in the Back, Collin-Dufresne, Fos, Li & Ljungqvist (2018, Econometrica) continuous-time Kyle model. Add:
- A bidder-arrival process (e.g., Poisson with intensity `λ` tied to price) with synergy shock `ξ`
- An *endogenous* disclosure threshold — blockholder crosses `θ_D` when cumulative stake `X_t` hits a level
- "Quiet Voice" ↔ "pre-disclosure costly effort"; "Public Voice" ↔ "post-disclosure costly effort"

### Why it's attractive

- Back et al. (2018) §7 *explicitly flags* endogenizing disclosure horizon as future work
- Their non-monotone liquidity-efficiency relation is *already proved* in closed form — you extend to takeover premia
- The "hump" can be proved rigorously because the underlying Kyle-Back machinery is tight
- Reuses most of your microstructure intuition

### What you would give up

- Loss of the discrete four-action clarity (trade becomes `dX_t` continuous)
- Need to solve HJB equations with a takeover stopping time — technically harder
- Your stake-triggered disclosure rule `D=1 ⟺ q=+1` becomes a cumulative-stake hitting time `τ = inf{t : X_t ≥ θ_D}`

### New skills required

- Stochastic optimal control (HJB equations, free-boundary problems)
- Some comfort with Malliavin calculus or PDE methods for dynamic Kyle models
- Longer engagement with the Back-CDF-Fos-Li-Ljungqvist technical machinery

### Risks

- 10-12 months is a real commitment; if you're already writing job market materials this is a setback
- Continuous-time models with discrete disclosure events (jumps) can have subtle existence issues
- You may get scooped in the interim — the Cetemen-Cisternas-Kolb-Viswanathan team is clearly working in this space

---

## Path C — Frontier: Dynamic Kyle + BHK auction + endogenous disclosure

**Timeline:** 14+ months
**Outcome tier:** Top-5 to top-10 IF executed (big if)
**Ambition level:** Maximum — framework-level contribution

### Core idea

The subsumption move. Combine:
- Dynamic Kyle-Back stake-building (Path B machinery)
- Bulow-Huang-Klemperer (1999) / Burkart (1995) toehold auction for the takeover stage
- Endogenous disclosure triggering at a threshold

Current draft becomes a special case. Hump on premium arises from overbidding / winner's-curse mechanics that are already known to generate non-monotonicities in the auction literature.

### Why it's attractive

- Framework-level contribution (the kind that gets top-5 placements — Chen 2023, Pernoud 2023)
- BHK / Burkart toehold overbidding gives you a *proven* non-monotonicity on premia from the auction side
- Endogenous disclosure arrives naturally as part of the stopping-time problem in the pre-auction stake-acquisition phase
- Unifies three literatures (microstructure / activism / takeovers) — Yu 2024 "General Theory of Holdouts" won FTG First Prize for a similar unification move

### What you need to solve

- Two-stage game: (i) Kyle-Back dynamic trading + disclosure; (ii) auction with heterogeneous toeholds
- Backwards induction on the auction stage, then solve the stake-building / disclosure problem given the auction continuation value
- Multiple bidders (at least 2 for BHK machinery to bite) — adds a dimension
- Equilibrium existence at the interface of stochastic control + auction theory

### Risks

- 14+ months is a doctoral-extension-level commitment
- Even FTG First Prize 2024 (Yu) placed Colorado, not Stanford — ambition is necessary but not sufficient
- If any piece doesn't cleanly compose, you have a hybrid model with worse properties than either pure piece
- The Cetemen et al. team is 4 senior authors working on this space — a PhD student competing alone is at a disadvantage

---

## Decision matrix (as of 2026-04-21)

| Criterion | Path A | Path B | Path C |
|---|---|---|---|
| Timeline | 6-8 mo | 10-12 mo | 14+ mo |
| Target placement tier | Top-20/25 | Top-10/15 | Top-5/10 |
| Risk of not finishing | Low | Medium | High |
| Builds on current draft | Fully | Mostly | Partially |
| Requires new technical toolkit | No | Yes (stochastic control) | Yes (stochastic control + auction theory) |
| Preemption risk | Low | Medium (Cetemen et al.) | Medium (Cetemen et al., Burkart-Lee-Voss) |
| FTG-prize-plausible | No | Maybe | Yes |

## Selection & revisit criteria

**Current decision (2026-04-21):** Path A. Finalize tightened draft, target fall 2026 JMP interviews.

**Revisit Path B if:**
- Prop 6 primitive-level sufficient conditions prove intractable
- Time horizon extends past spring 2027
- You want a 2-paper JMP portfolio (Path A as short paper + Path B as main paper)
- Cetemen-Cisternas-Kolb-Viswanathan paper publishes without disclosure + bidder entry (confirms the lane is still open)

**Revisit Path C if:**
- You take a pre-doc year
- Path B delivers a complete first draft by early 2027 and you want to push higher
- You pair up with a co-author who has stochastic-control + auction-theory chops

---

## Notes for revisit

- The three-paper invitation (Edmans 2014, Burkart-Lee 2022, Back et al. 2018) gives you durable positioning; it doesn't expire soon
- Ordóñez-Calafi-Bernhardt (2022 JFQA) is the biggest surprise — closest competitor on disclosure-policy design that's not currently cited
- If another PhD student scoops Path B before you get there, Path A's static simplicity becomes a virtue (complementary, not redundant)
- Full session log at `quality_reports/session_logs/2026-04-21_theory-positioning-and-jmp-strategy.md`
