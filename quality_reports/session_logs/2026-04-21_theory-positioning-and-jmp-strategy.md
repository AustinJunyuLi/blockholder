---
date: 2026-04-21
session_type: theory-review + positioning
status: IN_PROGRESS
---

# Session: Theory Positioning and JMP Strategy — draft_v2.tex

## Goal

Evaluate the theoretical position of `draft_v2.tex` ("Liquidity, Activism Disclosure, and Takeover Premia") in the literature. The user intends this to be an ambitious JMP. Primary focus: theory only (code + presentation out of scope).

Deliverables:
1. Critical appraisal of the current draft's theory (completed earlier this session)
2. Literature survey to position the contribution
3. Identification of direct competitors and novelty claims
4. Proposal of alternative model architectures if a stronger setup exists
5. Final ranked JMP strategy

## Key Context

Target paper architecture (draft_v2):
- Static game, blockholder with signal `s` on fundamental `v`
- Four actions: Exit `(-1,0)`, Hold `(0,0)`, Quiet Voice `(0,1)`, Public Voice `(+1,1)`
- Stake-triggered disclosure: `D = 1 ⟺ q = +1`
- Discrete order flow `X = q + z` à la EGJ 2015
- Bayesian market maker; bidder with synergy shock `ξ`
- Headline: minority takeover gains `Δ^min(κ)` are hump-shaped in noise-trading intensity `κ`
- Secondary: disclosure threshold attenuates liquidity sensitivity (partial equilibrium)

## Phase 1 Findings (draft critique, completed)

Five agents reviewed model setup / equilibrium / core results / welfare-extensions / proofs.

Top theoretical issues:
- **Prop 6 (nonmonotonicity) literally assumes the conclusion** — line 554 states "Assume... Δ^min(κ̃) > lim Δ^min(κ)" before invoking Weierstrass. Proof skeleton only.
- **Prop 8 (GE disclosure tradeoff)** self-admittedly "heuristic" in footnote (line 785).
- **Equilibrium uniqueness** is numerical-only (A6 contraction assumed, not derived).
- **Engagement cost `C(s)` decreasing** (A2) load-bearing, runs counter to Maug/classical intuition.
- **Bidder bargaining protocol** for `m_0, m_1` is a primitive, not micro-founded.

Secondary: restricted action set (excludes `(+1,0)` silent buy); silent exit margin `k_1`; accounting (not causal) price decomposition; thin welfare section.

## Phase 2: Lit Survey (in progress)

Five agents deployed:
- `classical-papers`: Maug 1998, Kahn-Winton 1998, EFZ 2013 → **completed**
- `modern-activism`: Back 2018, Corum-Levit 2019, Burkart-Lee 2022 → running
- `edmans-survey`: Edmans 2014 (file dated 2024 but content is 2014) → **completed**
- `web-direct-competitors`: liquidity-takeover-theory web search → running
- `jmp-bar-and-alternatives`: recent JMPs + alt architectures → running

### Key findings so far

**Strong positioning news**:
- None of the three classical papers (Maug, Kahn-Winton, EFZ) generates a humped liquidity → takeover-premium result
- Maug has a hump but in **IPO price** (Prop 7), not in governance/premia
- Kahn-Winton has non-monotonicity in **ownership**, not in liquidity
- Edmans 2014 survey **explicitly flags three gaps** the target paper plausibly fills:
  1. Integrated voice-exit architecture (not separate) — Levit 2013 is rare precedent
  2. Endogenous disclosure threshold (`k_D`) — "theory models do not predict a discontinuity at 5%" (p.25)
  3. Non-monotone liquidity effect on governance outcomes

**Remaining risks**:
- Back et al 2018 (JF): continuous-time Kyle activism with liquidity → need to verify no hump on similar margin
- Corum-Levit 2019 (JFE): corporate control activism
- Burkart-Lee 2022 (RFS): activism AND takeovers jointly — directly overlapping scope
- 2023-2026 recent work unknown

## Decisions (tentative)

- **Keep** the integrated four-action architecture as core contribution
- **Keep** endogenous disclosure cutoff `k_D` as second contribution
- **Restate** hump in terms of observable outcome (likely: cross-sectional liquidity-premium slope) to avoid "assumes the conclusion" trap
- **Open question**: is the bidder problem salvageable with Nash-bargaining micro-foundation?

## Next Steps

1. Wait for remaining 3 agents (modern-activism, web-direct-competitors, jmp-bar-alternatives)
2. Synthesize full positioning: what's genuinely novel, what's at risk
3. Invoke `research-ideation` skill to generate 3-5 alternative architectures
4. Rank alternatives against current draft on (a) theoretical cleanness, (b) empirical sharpness, (c) JMP ambition
5. Final recommendation to author

## Open Questions

- Does Back et al 2018 already have a humped liquidity result on a related margin?
- Does Burkart-Lee 2022 cover disclosure-mediated takeover premia?
- What's the realistic JMP bar for a theory-heavy JMP at UCL / LSE / LBS?
- Should the hump result be relabeled "numerical with analytical endpoints" or fully proved via primitive conditions?

## Blockers

None so far.
