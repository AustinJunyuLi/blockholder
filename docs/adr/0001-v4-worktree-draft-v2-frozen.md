---
status: accepted
date: 2026-08-19
---
# Work in a separate v4 worktree; draft_v2.tex is frozen

The original checkout had 29 untracked paths and three tmp_* dirs; the supervisor has read draft_v2. We work in `~/Projects/blockholder_v4` (git worktree, branch `v4` off `proposal`), never edit `draft_v2.tex`, and write the new draft as `draft_v3.tex`. This keeps the milestone record intact and gives every agent a clean tree.
