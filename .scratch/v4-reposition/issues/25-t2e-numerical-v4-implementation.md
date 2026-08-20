# 25 — T2e · Two-round numerical implementation (`numerical_v4/`)

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** Opus designs and builds; **Fable reviews the
design before the build proceeds** (a named Fable checkpoint); Sonnet for
plumbing. This is the long pole for every NUMERICAL label.

**Premise:** the card `research/model_v4/MODEL_CARD.md` defines the model; the
NUMERICAL CHECK REQUEST sections of `threads/thread1_turn1_answer.md` and
`thread1_turn2_answer.md` define what the implementation must compute. House
style = the existing `numerical/` package (pure functions, type hints,
dataclass params, NamedTuples, its tolerance constants). The worktree may need
`make venv` first.

**What to build:**

- [ ] `research/model_v4/impl_design.md`: discretisation of s (quadrature vs
      analytic), simplest card-conformant plan menu (Exit / Hold / Voice family
      with strictly increasing terminal target — coordinate with ticket 24's
      A7′ condition), calendar d = 0..H, pooled-history enumeration with the
      count stated (coarse Γ, 2–3 marks), inner pricing fixed points per
      history, flagged prices on an s-grid, the frozen-policy κ-sweep mode
      (required by L2's check) vs equilibrium mode, outer solver reusing
      `solver.py`'s damped-iteration + brentq architecture, reuse map
      (verbatim / adapted / new), check-script interface mirroring
      `quality_reports/fixes/d7_*` JSON shape, and named risks where
      discretisation could betray a theorem (esp. injective A7 vs discrete s)
- [ ] **STOP for Fable design review** — build continues only after
- [ ] `numerical_v4/` package built to the reviewed design; deterministic;
      runs with `.venv/bin/python`
- [ ] A smoke run: one equilibrium solved at baseline, one frozen-policy κ
      sweep, outputs eyeballed against card signs
- [ ] Session log lines; commits on `v4-theory`

**Blocked by:** none (design can start now; coordinate the plan menu with 24).

**Status:** ready-for-agent

## Comments
