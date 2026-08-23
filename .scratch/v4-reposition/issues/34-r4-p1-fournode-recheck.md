# 34 — R4 · P1's four unresolved nodes: the 30-seed re-run

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** Sonnet writer, effort medium — this parametrizes the existing
`t2_p1_check.py` machinery, no new model objects. Deterministic; no separate re-runner.
Orchestrator commits.

**Premise:** Audit finding 5. The sweep gave the four failing nodes `N_SEEDS_SWEEP = 5` attempts
where the design asked 30 (`impl_design.md` :25, :138, :320). Their status is **unresolved** —
cutoff residual ~1e-11 but payoff residual 3.1e-4…1.5e-3 after 5 seeds — neither existence nor
nonexistence. The four nodes:

| κ | τ | T |
|---|---|---|
| 0.15 | 0.05 | 5 |
| 0.15 | 0.075 | 1 |
| 0.85 | 0.05 | 5 |
| 0.85 | 0.075 | 1 |

**What to build:**

- [ ] `quality_reports/fixes/t2_p1_fournode_recheck.py` → `.json`, house style. Exactly these
      four nodes; seeds 0..29, **no early stop** — run all 30, keep the best per node.
- [ ] Per node report: best cutoff residual $\lVert k-\mathcal T(k)\rVert_\infty$; best (and
      distribution of) **maximum profitable plan deviation**; the achieving seed; wall time.
      Equilibrium criterion as in the parent check: cutoff residual < 1e-10 AND deviation
      magnitude < 1e-9.
- [ ] A3/A6 spot diagnostics at each node, using whatever proxies the parent check already
      computes (single-crossing / ordering diagnostics; self-map and continuity probes) — if the
      hypotheses' checkable proxies fail at a node, say so: conditional P1 would not even apply
      there, which is a different finding from solver failure.
- [ ] Verdict per node, honest: **RESOLVED-EXISTS** (a seed meets both criteria → the node gets
      NUMERICAL existence evidence), or **STILL UNRESOLVED after 30 seeds** (remains UNCHECKED —
      not "no equilibrium"), or **HYPOTHESIS-PROXY-FAILS** (name the proxy).
- [ ] Commit script + JSON; one-line outcome note in the session log. **Card edits wait** — if
      nodes resolve, ticket 35's close-out folds it into the P1 row's numerical sentence in the
      same touch (spec SHOULD-9).

**Do NOT:** rerun the full sweep; change tolerances; write to the card in this ticket.

**Stopping condition:** JSON on file with a per-node verdict; pushed. Expected cost: 4 nodes ×
30 cold solves ≈ under an hour on the batch's timings.
