# 05: Tracked cleanup in dedicated commits

**What to build:** Stale tracked material removed or refreshed with git as the recovery path, nothing evidence-bearing touched.

**Blocked by:** 04 (HANDOFF.md deletion needs the to-do migrated first).

**Status:** ready-for-agent

- [ ] Delete root `HANDOFF.md` (superseded by CONTEXT.md + ADR-0009; to-do migrated in 04)
- [ ] Delete broken symlink `quality_reports/session_logs/2026-02-24_description.md` (dangling Linux path; real file adjacent)
- [ ] Reconcile every nonterminal or missing `Status:` in `.scratch/v4-reposition/issues/` against the current authority record. Use `resolved` only when the named deliverable and its required evidence exist; use `wontfix` when Position 1, a superseding ADR, or the frozen record bars or supersedes the work; use `ready-for-human` only for a live author judgement or review; use `ready-for-agent` only for authorised work with complete inputs and acceptance criteria. Do not bulk-assign one status and do not delete tickets
- [ ] Nothing else tracked deleted; `quality_reports/` fixes/handoffs/session_logs, `t2_*`, `dN_*`, BID12 materials, `.scratch/` files all intact
- [ ] Separate commits: deletions vs status refresh

## Comments
