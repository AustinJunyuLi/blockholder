# 08: Land v4, tag provenance, and retire the theory worktree

**What to build:** `v4` and `origin/v4` point to the verified combined history; the final theory tip remains on `origin/v4-theory` and under an annotated retirement tag; only the canonical `blockholder_v4` worktree remains active for this project.

**Blocked by:** 06 and 07.

**Status:** ready-for-agent

- [ ] Re-run dirty-state accounting in both worktrees. Any new or unclassified file blocks retirement. In particular, preserve or relocate `.scratch/claude-subscription-amp-research.md` with its owning task; never delete or silently absorb it
- [ ] Confirm ticket 06's cleanup manifest is exhaustive, the Chrome QA profile is either safely trashed or explicitly retained because a live process still owns it, and `empirics/data` still resolves to `/Users/austinli/Projects/blockholder/empirics/data`
- [ ] Confirm `codex/v4-integration` contains both histories, ticket 07 is PASS, the frozen hashes still match, and no later commit touched the BID12 rulebook or viewed-result artifacts
- [ ] Fast-forward local `v4` to `codex/v4-integration` with `--ff-only`; no squash, rebase, force update, or history rewrite
- [ ] Push the preserved final `v4-theory` branch, then create and push an annotated `v4-theory-retired-YYYY-MM-DD` tag at that exact tip. Keep `origin/v4-theory`; retirement removes the worktree, not its history
- [ ] Push `v4`, verify `git rev-parse v4`, `origin/v4`, and the remote-advertised `refs/heads/v4` are identical, and record the final SHA
- [ ] Move the redundant theory `.venv/` to Trash only after the canonical `.venv` passes ticket 07. Remove `/Users/austinli/Projects/blockholder_v4_theory` with normal `git worktree remove`, without `--force`, then verify `git worktree list` and prune only stale administrative entries
- [ ] Delete local `codex/v4-integration` with safe `git branch -d` only after it equals `v4`; leave no remote staging branch unless one already existed and is documented
- [ ] Write `.scratch/v4-consolidation/completion.md`: final SHAs, tag, surviving worktrees, retained local dependencies, cleanup totals, verification-log link, and the explicit statement that Position 1 remains the next campaign
- [ ] Mark tickets 01–08 done, commit the completion record and final ticket comments on `v4`, push once more, and verify a clean status modulo declared ignored dependencies
- [ ] Record the next action exactly: create the immutable evidence manifest and register E1 before any adopted filing-delay rerun. Do not begin E1 or manuscript rewriting inside this ticket

## Comments
