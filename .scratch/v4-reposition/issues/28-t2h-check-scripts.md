# 28 — T2h · Check scripts: every NUMERICAL CHECK REQUEST, executed and committed

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** Opus writes each script; a DIFFERENT Opus agent
re-runs each one (the D-series discipline). All runs `.venv/bin/python`.

**Premise:** `numerical_v4/` built (ticket 25). The check requests are in the
NUMERICAL CHECK REQUEST sections of `threads/thread1_turn1_answer.md` (D1, P1,
L1, L3, L4, T1) and `threads/thread1_turn2_answer.md` (refined D1/L1/L2
requests — the turn-2 versions supersede turn-1 where they differ). Pattern:
`quality_reports/fixes/d7_takeover_game_check.py` + JSON.

**What to build:** one `quality_reports/fixes/t2_<id>_check.py` + `.json` per
result:

- [ ] D1: history enumeration — partition exclusivity/exhaustion, clock
      equivalence, timing-split residual < 1e-12
- [ ] L1: direct summation vs Ω·M_F + (1−Ω)·M_P at every node + the Ω∈{0,1}
      degenerations
- [ ] L2: frozen-policy κ sweep — ranges of flagged posteriors/P^F/entry/M_F
      < 1e-10, finite-difference derivatives < 1e-8
- [ ] L3: chord — enumerated ∂_κE[h] vs A′_κ·C_h residual < 1e-10; quadratic
      small-π̄ scaling
- [ ] L4: Ω(τ)↑, π̄(τ)↓, 𝒮_P(τ)↓ under tightening; sign violations reported as
      failed hypotheses, never smoothed
- [ ] T1: W·C product identities to 1e-10 both margins; the old-framework
      regression benchmark (reproduce directions ≈1.06/1.19/1.14/0.38)
- [ ] P1: 30-seed multistart existence on the grid ±20% perturbations
- [ ] Raw JSON committed next to each script; labels moved to NUMERICAL in the
      card ledger with log lines, only on passing output
- [ ] Session log lines; commits on `v4-theory`

**Blocked by:** 25 (implementation); each script also needs its result's proof
landed so the request is final (21–23, 26).

**Status:** ready-for-agent

## Comments
