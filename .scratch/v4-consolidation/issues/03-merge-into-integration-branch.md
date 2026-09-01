# 03: Merge v4-theory into codex/v4-integration

**What to build:** One branch containing both full histories, with the frozen theory trees byte-identical to `v4-theory` and no textual conflicts.

**Blocked by:** 01, 02.

**Status:** ready-for-agent

- [ ] `codex/v4-integration` created from `v4` tip and checked out in the `blockholder_v4` worktree
- [ ] `git merge --no-ff v4-theory` — normal merge, no squash; conflict-free (preview was clean; new files don't overlap)
- [ ] `git rev-parse 'HEAD:research/model_v4'` equals `v4-theory`'s; same for `sections_v3`
- [ ] `git log --oneline` shows both lineages; merge commit message records both parent tips
- [ ] `research/empirics_v4/bid12_coding_rules.md` blob unchanged vs pre-merge `v4`

## Comments
