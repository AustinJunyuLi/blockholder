# Map — p1-existence-route

**Effort.** Determine whether the correspondence-based existence route can replace A3 and A6 in
P1's hypothesis set, so that existence stops depending on the two assumptions the implemented
calibration measurably violates. Opened 2026-08-29 on Austin's ruling (grilling Q1: option C is
the December baseline — conditional theorems framed as benchmark implications — and this
exploration runs in parallel as its possible upgrade). This is exploration, not a proof campaign:
the first child ticket ends in a GO / NO-GO / GO-WITH-CHANGES assessment and, on GO, proposed
child tickets for the campaign.

## Notes

- The prize: P1 as an implemented-model existence theorem. Today P1 is PROVED as a conditional;
  at the implemented calibration A3 fails (two loci; the weakly-increasing-selection set can be
  empty, so the single-valued outer map is undefined there) and A6's continuity clause fails
  (measured 𝒯₂ jumps at interior n(s) cell edges; card §5 notes, stamp 2026-08-28 `59c0dfc`).
- Already on file, the raw material:
  - `research/model_v4/proofs/P1_proof.md` Step 18 — the t-constrained game + Kakutani + t↓0
    route. The paper transcription's own scope note: it removes only transversality, not joint
    continuity or the bracket; card §9 item 4(a) says it "removes h.6's continuity half" and the
    repair is "identified, not executed".
  - The k-indexed concentration family — constructible; its 0/0 corner unresolved (card §5 A6
    note).
  - The implementation's `OFF_PATH_EPS` = 1e-14 IS the fixed-t constrained game (card §5 A6
    note) — the standard repair already shipped numerically, switch relocated ~1e-9.
  - The A6 panel records (`threads/2026-08-27_A6_panel_{substantiate,defuse}.md`) — the locus,
    the non-vanishing deviation weight, the chamber-interior Θ⁺ caveat, the continuum-face lemma
    (single-pass, not gate-checked).
  - The A5 two-continuities split (card §5 A5 note, 2026-08-28): belief-summaries continuity is
    a theorem; composed cutoff-continuity is not — the correspondence route must not smuggle it
    back in.
  - GPT Pro's re-review (threads/2026-08-28_gpt_rereview.md, P1 section): names this route "most
    plausibly the already identified correspondence-based route"; its numerical-check request
    sets the bar an implemented-model theorem would face.
- Label discipline: everything in this effort is CONJECTURE-grade until a proof passes the
  two-pass gate. No card writes from this effort; findings live here and in ticket answers.

## Decisions so far

- 2026-08-29 — effort opened; ticket 01 (route exploration) dispatched to a single Opus agent,
  scope-boxed to the assessment (no proof writing).
- 2026-08-29 — ticket 01 resolved **GO-WITH-CHANGES**: route buys A6's continuity half (measured),
  cannot buy A3 (`𝒮(k) = ∅` at a located fixed point, 8/8 family × `t` variants); locus (i)
  family-dependence flagged for verification — `.scratch/p1-existence-route/issues/01-route-exploration.md`.

## Fog

- Does Kakutani apply at all with the argmax treated as a correspondence — are the best-response
  values convex in cutoff space at the jump edges (upper hemicontinuity is expected; convexity
  of values is the classical failure point)?
- What exactly does the t↓0 limit lose: does a fixed point of the limit correspondence survive
  as an equilibrium of the unconstrained game, or only as an ε-equilibrium?
- Can the same move absorb A3's failure (empty selection set) or only A6's (discontinuity) —
  and if only A6's, what is the weakest replacement for A3?
- Does the route deliver at the boundary κ ∈ {0,1} under the extension reading, or does the
  constrained game need its own boundary treatment?
- If the route lands, which downstream results consume P1's conclusion in a way that notices
  the changed hypothesis set (A8 addendum, H-ord restatement)?
