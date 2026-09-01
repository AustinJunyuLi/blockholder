# 06: Untracked/local cleanup via Trash + final manifest

**What to build:** ~674 MB of proven residue in the Trash (recoverable), with a before/after manifest committed under `.scratch/v4-consolidation/`.

**Blocked by:** 03 and 07. Theory work must be merged first, and final verification must run before cleanup so regenerated caches and LaTeX intermediates appear in the final manifest. The orchestrator has already captured Q6–Q13 from the 2026-08-29 tmp handoff.

**Status:** ready-for-agent

Targets (Trash via `osascript`/`trash`, explicit paths only, no recursive globs at worktree roots; never follow `empirics/data`):
- [ ] `blockholder_v4_theory/v2/` (byte-identical duplicates of git-recoverable blobs)
- [ ] `blockholder_v4_theory/standalone_v3.pdf`
- [ ] `blockholder_v4_theory/.playwright-mcp/`
- [ ] `blockholder_v4/deliverables/conversion/` (233 MB ignored intermediates)
- [ ] `blockholder_v4/.claude/.cc-writes/` only if it is still empty, unreferenced, and has no live owner; after removal, perform a repository write/status cycle and verify it remains absent. If it reappears, retain it as tool-managed and record that classification
- [ ] `__pycache__` ×7, `.DS_Store` ×8, and LaTeX intermediates ×16, using only the explicit paths in `cleanup_inventory.md`; retain the four ignored A6 probe logs because they are executed evidence
- [ ] Before trashing `/private/tmp/blockholder-consolidation-handoff.3DjoUp/`, prove that its handoff and `.scratch/v4-consolidation/governing-handoff.md` are byte-identical, that both filesystem SHA-256 values equal `b0f99d485900b029f9d4aa41a1668ff958b37f00add1c4b6ababd470065b781c`, and that `git show HEAD:.scratch/v4-consolidation/governing-handoff.md | shasum -a 256` returns the same content hash; record the commands and output in the manifest
- [ ] `/private/tmp` blockholder residue: the 11 explicit superseded handoff paths in `cleanup_inventory.md`; `blockholder-report-qa.e2okWM/` only after `lsof +D` and a process check both show no live browser holds it. If still live, retain it and record the blocker rather than forcing deletion
- [ ] Before/after manifest committed at `.scratch/v4-consolidation/cleanup-manifest.md`. For every candidate record exact path; tracked, ignored, or untracked state; size; modification time; last Git commit when tracked; reference checks; replacement; classification; action; recovery route; after-state; and retained blocker. Also record counts, total reclaimed size, browser-check time, handoff comparison evidence, and `.cc-writes` durability result
- [ ] `blockholder_v4_theory/.venv/` left alone (dies with worktree retirement, ticket 08)
- [ ] `blockholder_gpt_pro_packet.yIHcac/` retained unless a separate evidence check proves it is fully superseded; it is not one of the 11 handoff targets

## Comments
