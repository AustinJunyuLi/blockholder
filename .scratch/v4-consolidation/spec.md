# Spec: v4 consolidation and deep clean

Status: ready-for-agent
Date: 2026-09-01
Authority: `.scratch/v4-consolidation/governing-handoff.md`, a byte-identical committed copy of the temporary source, SHA-256 `b0f99d485900b029f9d4aa41a1668ff958b37f00add1c4b6ababd470065b781c`. Grill rounds 1/1b were ratified by Austin on 2026-09-01 ("all recommended, go ahead").
Supporting inventories:
- `governing-handoff.md`: durable governing handoff; read it because this spec does not repeat it
- `authority_digest.md`: the authority map and root-document rewrite checklist
- `cleanup_inventory.md`: the exact cleanup targets, protections, and recovery route

## Problem Statement

The paper lives in two worktrees of one repository — `v4` (empirical lane, canonical) and `v4-theory` (theory lane, frozen theory record) — with live uncommitted work on both sides, stale lane-split instructions, and ~674 MB of proven local residue. The author wants one active branch and worktree, both histories preserved, the frozen theory record and registered empirical evidence byte-intact, and an evidence-based deep clean.

## Solution

Preserve all intentional dirty work in split commits; merge `v4-theory` into a staging branch `codex/v4-integration` off `v4` with a normal (no-squash) merge; rewrite the root instruction docs and add a superseding ADR in the same landing; clean tracked residue in dedicated commits and untracked residue via Trash; run every verification gate; fast-forward `v4`, push, tag, and retire the theory worktree.

## Campaign end state

Executing tickets 01–08 produces one clean, verified repository on branch `v4`, in the `blockholder_v4` worktree. It preserves both Git histories, the frozen theory trees, the hash-stamped empirical rules, the live manuscript, the teaching workspace, and the viewed-result record. The separate `blockholder_v4_theory` worktree is retired, while `origin/v4-theory` and an annotated retirement tag remain as provenance.

This campaign prepares GPT Pro Position 1; it does not complete it. It does not create the E1 protocol, rerun the filing-delay exercise, clear E1's denominator/audit/reproduction gates, or rewrite `draft_v3` into the legal-clock paper. Those are a follow-on campaign. Its first action is the immutable evidence manifest and E1 protocol required by `research/empirics_v4/2026-08-31_gpt_pro_integration_angle_review.md:680-682,820-822`.

## Ratified decisions (grill rounds 1 + 1b, all Austin-approved)

1. **Q1** Staging branch `codex/v4-integration`; normal merge, no squash; ff `v4` + push all after gates. `v4` backup-pushed to origin pre-work (done: `0384f8d..8e200ec`).
2. **Q2** `teach/` committed in its own commit.
3. **Q3** `deliverables/` deletion committed pre-merge (both branches track it — an uncommitted move would be silently reverted by the merge); singular `deliverable/` is canonical; untracked `v2/` duplicate trashed (blobs proven byte-identical to git history).
4. **Q4** `legal_regime_portability.md`: header narrowed to what was actually verified, relocated out of the frozen tree to `research/notes/`, committed as non-authoritative.
5. **Q5** `research/txt_extracts/gpt_pro` (30 K file, cited by 4 records as Austin's 2026-08-22 drop) committed as provenance.
6. **Q6** Data move deferred. `empirics/data` symlink and `~/Projects/blockholder` main checkout untouched. Two SHA-256-verified off-repo copies exist (SPEC.md:1448); `data_inventory.md` is stale on this and may be annotated, not rewritten.
7. **Q7** Evidence-conservative stance: all tracked `quality_reports/` (fixes, handoffs, session logs), `t2_*`/`dN_*` checks, audit records, `.scratch/` files KEPT. Deletions limited to caches, intermediates, duplicates, stale tmp handoffs. Untracked → Trash; tracked → dedicated commits.
8. **Q8** Scope ends at verified consolidation. E1 protocol / December critical path = follow-on spec, not here. Theory worktree retired after gates; branch `v4-theory` kept on origin + annotated tag.
9. **Q9** `HANDOFF.md`: migrate the live "confirm UCL WRDS access" to-do into the empirical docs that cite it, then delete in tracked-cleanup commit.
10. **Q10** `.grok/` committed.
11. **Q11** `standalone_v3.pdf` trashed (no refs; source + canonical PDF tracked).
12. **Q12** Tracked broken symlink `quality_reports/session_logs/2026-02-24_description.md` deleted in tracked-cleanup commit.
13. **Q13** `/private/tmp` residue trashed after (a) Q6–Q13 capture into `carried-open-decisions.md` (done) and (b) confirming no live browser holds the 150 MB Chrome profile `blockholder-report-qa.e2okWM/`.
14. **Q14** `v4/deliverables/conversion/` (233 MB, ignored) trashed; 24 stale `ready-for-agent` `.scratch/` tickets get a `Status:` refresh (edit, no deletion).

## Implementation Decisions

- **Never-touch list (byte-frozen):** `research/model_v4/` (tree `107c4c71…` at `v4-theory`), `sections_v3/` (tree `16b8b3c6…`), `research/empirics_v4/bid12_coding_rules.md` (whole-file hash-stamped in `bid12_run_meta.json`; any touch — whitespace included — voids the 0-of-30 blind audit). Frozen trees exist only on `v4-theory`, so the merge adds them wholesale; their tree hashes must be identical on the integrated branch.
- **Merge-winner rule:** `CLAUDE.md`/`AGENTS.md` are unchanged on `v4` since merge base and rewritten on `v4-theory`, so the raw merge installs theory-lane docs ("do no empirics work here") on the canonical branch. The unified-docs rewrite lands immediately after the merge commit, before anything else runs on the branch.
- Preview facts (unmodified tips): merge-tree clean, preview tree `cd59bd8e404ae4ecb6c02fcf6c20d42613d73ba5`. Preservation commits change both tips, so the final merge is NOT expected to reproduce that OID; the binding gates are the frozen-tree hashes and a conflict-free merge.
- Consolidation ADR `docs/adr/0009-*` records one active branch/worktree, supersedes ADR-0007's two-lane split, and retires the "two-lane split unchanged" clause in ADR-0008:31-33. ADR-0007 stays as history.
- A separate Position 1 ADR `docs/adr/0010-*` supersedes ADR-0006. It records the legal-clock paper, E1 as the only authorised December headline, the viewed appendix exercises, and the prohibition on causal claims.
- `CONTEXT.md` is byte-identical across worktrees and carries no lane rule. Correct only the stale `Timing split` glossary entry so it describes the registered overlapping return-window contrast, not the model's latent flagged/pooled states or the new headline.
- One commit per concern; never combine preservation, merge, doc rewrite, and deletion (handoff line 188).
- Execution per ADR-0005: fresh agents per ticket; the orchestrator owns Git sequencing and destructive steps.

Ticket graph: 01 and 02 may run in parallel; 03 waits for both; 04 waits for 03; 05 waits for 04; 07 waits for 04 and 05; 06 runs after 07 so it removes build-generated residue and writes a genuinely final cleanup manifest; 08 waits for 06 and 07.

## Testing Decisions

Gates are the handoff's "Verification and completion criteria" (lines 190–208), executed on the integrated branch and recorded in `.scratch/v4-consolidation/verification-log.md` plus ticket `## Comments`:
smoke (`.venv/bin/python -m numerical_v4.smoke`), committed `t2_*` checks, `make clean && make all`, draft_v3 XeLaTeX→Biber→XeLaTeX×2 zero errors/undefined, online appendix compile with xr resolution, empirics commands exactly as recorded in `empirics/README.md`/SPEC (no invented runners, no reruns of viewed specifications), frozen-tree hash equality, dirty-state accounting, cleanup manifest exhaustive, `git status --short` clean modulo declared items.

## Out of Scope

Executing the E1 protocol and evidence manifest in `.scratch/position-1-delivery/spec.md`, E2, any figure regeneration, the 14 carried-open research decisions (see `carried-open-decisions.md`), data relocation, and any edit to frozen or hash-stamped material.

## Further Notes

Loss-risk ranking pre-work (now mitigated by backup push + preservation tickets): 37 unpushed `v4` commits (pushed), then untracked `teach/`, `gpt_pro`, legal note, research records, `.grok/`.
