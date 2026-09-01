# 01: Preserve v4-side intentional dirty work

**What to build:** The canonical branch carries the two empirical integration reports and the Grok workflow as committed history, so nothing on the v4 side is lost when branches move.

**Blocked by:** None (backup push done by orchestrator).

**Status:** resolved

- [x] Commit `research/empirics_v4/2026-08-31_gpt_pro_integration_angle_review.md` + `2026-08-31_theory_empirics_december_integration.md` in one commit (research records)
- [x] Commit `.grok/` in a second commit (local tooling adopted)
- [x] `.scratch/v4-consolidation/` and `.scratch/position-1-delivery/` specs, authorities, and tickets committed (third commit)
- [x] `git status` on v4 clean except `empirics/data` symlink and declared local deps

## Comments

Resolved 2026-09-01. Reports commit: `5070955827cd70fcdf2366674bd802fe85468b42`; Grok commit: `44e0cbfaa383262af5cf7dd3abb29811a1359c6d`. Ticket-writing validation: governing-handoff SHA-256 `b0f99d485900b029f9d4aa41a1668ff958b37f00add1c4b6ababd470065b781c`; Position 1 issue count `9`.
