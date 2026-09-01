# Handoff: consolidate the v4 worktrees and deep-clean the local project

Created: 2026-08-31

## Objective

Consolidate the theory and empirical lanes into one active branch and worktree while preserving both Git histories, the frozen theory record, registered empirical evidence, and current uncommitted work.

The user also wants a deep local cleanup. Remove proven temporary, stale, duplicate, or superseded material, including old handoffs and stale tests. Treat cleanup as an evidence-based deletion task. Inventory first, classify every candidate, use recoverable deletion where possible, and keep ambiguous research evidence until the user rules on it.

The research destination is GPT Pro's Position 1:

- Keep the theory record frozen.
- Make `draft_v3` a theory-led paper about the disclosure rule as a public-market information partition.
- Make corrected filing timing, E1, the sole December empirical headline if it clears its protocol, denominator, audit, artifact, and reproduction gates.
- Keep H1, H2, dose, stake, placebo, and BID12 fixed as viewed and move them to the honesty appendix.
- Do not claim a causal return or control-outcome effect.

Repository consolidation prepares this work. It does not itself complete E1 or the integrated manuscript.

## Read first

Use paths relative to `<HOME>/Projects/blockholder_v4` unless another worktree is named.

1. `research/empirics_v4/2026-08-31_gpt_pro_integration_angle_review.md`
   - Decision: lines 14-41
   - E1: lines 475-523
   - E2: lines 525-564
   - Immediate decision: lines 818-822
2. `docs/adr/0007-one-theorem-two-round-model-two-lanes.md`
   - Line 9 already says `v4-theory` will merge into `v4` at the `draft_v3` ticket.
3. Theory authority in `<HOME>/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md`.
4. Empirical authority in `research/empirics_v4/SPEC.md` and `research/empirics_v4/decisions_2026-08-31.md`.
5. Root `CONTEXT.md`, `CLAUDE.md`, and `AGENTS.md` in both worktrees. The theory versions contain lane-specific rules that become false after consolidation.
6. `research/empirics_v4/data_inventory.md` before changing the empirical data location.

Do not repeat the material in these files in a new planning document. Point to them.

## Verified live state

The directories are already worktrees of one repository, not separate repositories.

- Common Git directory: `<HOME>/Projects/blockholder/.git`
- Remote: the same origin repository for both worktrees
- Canonical candidate: `<HOME>/Projects/blockholder_v4`, branch `v4`, head `8e200ec`
- Theory lane: `<HOME>/Projects/blockholder_v4_theory`, branch `v4-theory`, head `adf97c6`
- Merge base: `5b34a404`
- Divergence at inspection: 47 commits unique to `v4`, 100 unique to `v4-theory`
- `v4` was 37 commits ahead of `origin/v4`; `v4-theory` matched `origin/v4-theory`
- A read-only merge preview of the committed tips produced no textual conflicts.
- Only `CONTEXT.md` and ADR-0007 changed on both branches since the merge base; their tip contents agree.
- Use a normal merge. Do not squash. Theory and audit records cite exact commits.

No files, branches, refs, worktrees, or external systems were changed during the prior session.

## Dirty work that must be preserved

Re-run `git status --short --branch` in all worktrees before acting. The following was live at handoff creation.

### `v4`

Tracked files were clean. Untracked material included:

- `.grok/`
- `research/empirics_v4/2026-08-31_gpt_pro_integration_angle_review.md`
- `research/empirics_v4/2026-08-31_theory_empirics_december_integration.md`

The two reports are intentional research records. Classify `.grok/` as local tooling unless current use proves otherwise.

### `v4-theory`

Tracked changes included:

- `draft_v3.tex`, a large live rewrite
- `draft_v3_trace.md`
- `quality_reports/session_logs/2026-08-30_draft_v3_team_review_brief.md`
- Both PDFs under singular `deliverable/`
- Four deleted legacy binaries under plural `deliverables/`

Untracked material included:

- `teach/`, active user learning state. Preserve it.
- `quality_reports/session_logs/2026-08-30_draft_v3_prose_rewrite_onepager.md`
- `research/model_v4/legal_regime_portability.md`
- `research/txt_extracts/gpt_pro`
- `standalone_v3.pdf`
- `.playwright-mcp/`
- `v2/`, containing the same four binaries deleted from `deliverables/`

The `deliverables/` to `v2/` change is an uncommitted move, not proof that either side is junk. Decide and commit it explicitly.

The legal-portability note sits inside the frozen theory directory and cites an older card stamp. Keep it non-authoritative and move it outside the frozen tree, or verify and adopt it through a separate author decision.

## Authority boundaries after consolidation

Keep existing paths. Do not create a new monorepo hierarchy or move the frozen theory tree.

| Area | Paths | Rule |
|---|---|---|
| Frozen theory authority | `research/model_v4/`, `sections_v3/` | Preserve byte-for-byte. `MODEL_CARD.md` is the theory source of truth. `threads/` and re-derivations are evidence, not temporary files. |
| Editable theory implementation | `numerical_v4/`, relevant `quality_reports/fixes/t2_*` checks | Keep the smoke gate and executed evidence. |
| Empirical authority and code | `research/empirics_v4/`, `empirics/`, committed `empirics/output/` artifacts | Preserve registered rules, audit records, result labels, hashes, and decision notes. |
| Paper integration | Root `draft_v3*`, singular `deliverable/` | Editable after branch consolidation. The current manuscript still uses an old filing-delay figure. |
| Historical v2 record | `draft_v2*`, `numerical/`, `pyfig/`, `pres/`, chosen legacy-output location | Frozen reference unless a cleanup decision explicitly relocates binaries. |
| Teaching | `teach/` | Active user state. Keep separate from manuscript builds. |
| Shared provenance | `quality_reports/`, `.scratch/`, `CONTEXT.md`, `docs/adr/` | Classify by authority and references before deleting anything. |

## Deep-clean protocol

The user explicitly wants stale local material gone. Do not interpret age, a name such as `handoff`, or a test filename as sufficient evidence of staleness.

### 1. Inventory before deletion

Create a cleanup manifest outside the repository or under the consolidation issue directory. For every candidate, record:

- exact path
- tracked, ignored, or untracked status
- size
- last modification and last Git commit when tracked
- references from builds, instructions, specs, ADRs, traces, and scripts
- replacement or superseding artifact, if any
- classification: keep, relocate, archive, delete, or author decision
- recovery method

Use `rg` or `git grep` for references. Do not follow the empirical data symlink while scanning for deletion targets.

### 2. Likely local cleanup candidates

These still require a target-specific check:

- `.playwright-mcp/`
- ignored LaTeX intermediates
- Python caches, `.DS_Store`, editor state, and local browser captures
- generated root `standalone_v3.pdf` if its source and reproducible replacement are confirmed
- stale temporary handoffs under the task's own temporary directories
- obsolete generated PDFs that have a verified source and canonical replacement
- abandoned test outputs that no active command, spec, report, or result manifest consumes

### 3. Ambiguous candidates that require proof or an author decision

- Root `HANDOFF.md`, which is stale but tracked. Replace or supersede it before removal.
- Old files under `quality_reports/handoffs/` and `quality_reports/session_logs/`.
- `.scratch/` issue files.
- `research/txt_extracts/gpt_pro` and other source extracts.
- `research/model_v4/legal_regime_portability.md`.
- `.grok/`.
- `deliverables/`, `deliverable/`, and `v2/` binaries.
- Old test scripts under `quality_reports/fixes/`.

An executed check, proof audit, blind-audit record, result gate, or registered test remains evidence even when it is old. In particular, do not delete `t2_*`, `dN_*`, BID12 audit materials, frozen proof records, or empirical gate artifacts merely to reduce file count.

### 4. Deletion rules

- Use explicit paths. Do not use broad globs or recursive deletion against a worktree root.
- Prefer Trash for untracked local material.
- Delete tracked stale files in a dedicated commit so Git provides recovery.
- Keep a before-and-after manifest with counts and sizes.
- Stop and ask when a tracked candidate has no clear replacement or when deletion would change an authority record.

## Data dependency

`<HOME>/Projects/blockholder_v4/empirics/data` is an ignored symlink to `<HOME>/Projects/blockholder/empirics/data`. At inspection it resolved to about 5.9 GB.

Do not remove `<HOME>/Projects/blockholder` or follow this symlink during cleanup until the data has a stable external location and the empirical lane has been repointed and checked. Removing the theory worktree does not require moving this data.

## Recommended sequence

1. Run `/grill-with-docs` in `<HOME>/Projects/blockholder_v4`.
   - Confirm `v4` as the canonical branch.
   - Settle `teach/`, `deliverable/` versus `v2/`, the legal note, source extracts, data location, and cleanup authority.
   - Record decisions in `CONTEXT.md` or a superseding ADR only when the skill calls for them.
2. Turn the decisions into a compact `/to-spec` artifact, then `/to-tickets` because this work spans preservation, integration, cleanup, and verification.
3. Preserve intentional dirty work before merging.
   - Commit manuscript sources and trace separately from generated PDFs.
   - Commit the teaching workspace separately if adopted.
   - Commit or deliberately exclude research notes and extracts.
   - Commit the two empirical integration reports.
   - Remove only verified local residue.
4. Create `codex/v4-integration` from `v4`.
5. Merge `v4-theory` into it without squashing.
6. Add a superseding consolidation ADR. Retain ADR-0007 as history.
7. Replace the theory-only root instructions with one authority table for the combined branch. Update or replace stale root `HANDOFF.md`.
8. Perform tracked deep cleanup in separate, reviewable commits after the combined tree exists.
9. Run all verification gates.
10. Retire the theory worktree only after backup and verification. Preserve the theory branch or an annotated tag as provenance.
11. Begin the research critical path. Write the E1 protocol and complete evidence manifest before any adopted filing-delay rerun.

Do not combine preservation, merge, directory moves, and deletion in one commit.

## Verification and completion criteria

Record exact commands and outputs in the implementation tickets. Minimum gates:

- Both pre-merge dirty states are accounted for.
- Both branch histories are present in the integrated branch.
- Full tree hashes for `v4-theory:research/model_v4` and `v4-theory:sections_v3` match the integrated branch.
- `.venv/bin/python -m numerical_v4.smoke` passes.
- The applicable committed `quality_reports/fixes/t2_*` checks pass.
- `make clean && make all` passes for the legacy numerical and figure pipeline.
- Main `draft_v3` runs XeLaTeX, Biber, then two XeLaTeX passes with no errors or undefined references.
- The online appendix compiles after the main draft and resolves its external references.
- Empirical verification uses the commands recorded in `empirics/README.md`, `SPEC.md`, and the relevant gate artifacts. Do not invent a generic runner or rerun viewed specifications to search for a result.
- Unified `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, and the new ADR describe one active branch with protected theory and empirical areas.
- The cleanup manifest accounts for every deletion, relocation, and retained ambiguous item.
- `git status --short` shows only declared local dependencies or intentional untracked files.
- No worktree is removed until its unique work and external data dependencies are safe.

The consolidation is complete only when the combined branch builds and the frozen authority trees match. The deep clean is complete only when the deletion manifest is exhaustive and every removed tracked file remains recoverable from Git.

## Suggested skills

The next agent should call the Skill tool for these skills in this order:

1. `/grill-with-docs` to settle the remaining author decisions and record them.
2. `/domain-modeling` when unifying `CONTEXT.md` terms or writing the superseding ADR.
3. `/codebase-design` to define the smallest authority seams without moving directories.
4. `/to-spec` and `/to-tickets` for the multi-session preservation, merge, cleanup, and verification work.
5. `/implement` for each ticket.
6. `/ponytail` during cleanup. Delete proven residue and avoid new structure.
7. `/writing-for-agents` when rewriting `AGENTS.md`, `CLAUDE.md`, or their pointed documents.
8. `/code-review` after each implementation ticket and again over the integrated branch.
9. `/resolving-merge-conflicts` only if an actual merge or rebase conflict exists.
10. `/handoff` at the next real phase boundary if work moves to a new session or directory.

## First action for the next agent

Stay read-only at first. Read the authorities above, rerun the live Git and filesystem inventory, and start `/grill-with-docs`. The first deliverable is a decision and cleanup inventory, not a merge commit and not a deletion.
