# 23 — T2c · P1 proof: cutoff PBE existence

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** one Opus writer agent.

**Premise:** card `research/model_v4/MODEL_CARD.md` §§2–5; turn-1 P1 statement
in `threads/thread1_turn1_answer.md`; the D1 repairs in
`threads/thread1_turn2_audit.md` — especially: B^F/Q^F are continuum-valued,
so A5's uniqueness must be consumed as a *measurably selected family* of fixed
points over the flagged-tuple continuum. Architecture to adapt (describe,
never `\ref`): draft_v2's `prop:existence` Brouwer argument (grep draft_v2.tex).

**What to build:** `research/model_v4/proofs/P1_proof.md`, answer template,
card notation binding. Proof route: inner prices for fixed cutoffs (finite
pooled histories + measurable selection on the flagged continuum) → sequential
optimality of the flagged component (be honest if this needs its own
hypothesis) → A3 single crossing gives a well-defined weakly ordered
best-response 𝒯(k;ϑ) → continuity + A6 self-map on the compact ordered
polytope Θ → Brouwer → assemble beliefs/prices/off-path limits → A8 gives both
cells on path.

- [ ] The measurable-selection reading of A5 consumed explicitly at the inner
      layer
- [ ] Sequential optimality of the flagged-round component stated and proved,
      or the weakest hypothesis making it so named
- [ ] Where A6 is assuming rather than deriving, said plainly
- [ ] Uniqueness explicitly NOT claimed
- [ ] Session log line; commit on `v4-theory` (label stays CONJECTURE)

**Blocked by:** none.

**Status:** ready-for-agent

## Comments
