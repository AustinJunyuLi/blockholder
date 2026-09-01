# Authority digest for consolidation

Date: 2026-09-01. This is the compact execution digest. The cited files remain the authorities.

## Campaign boundary

Tickets 01–08 consolidate and verify the repository. They do not deliver GPT Pro Position 1. Position 1 starts afterward with the immutable evidence manifest and registered E1 protocol, then proceeds only if E1 clears its fixed gates.

## Baselines to preserve

- Pre-preservation `v4`: `8e200ec92b11ba40d45cdc9a7e92307846a945fb`; pushed to `origin/v4` before ticketing.
- Pre-preservation `v4-theory`: `adf97c6130c83bcf72b16694f18fd8f9878a776d`; matched `origin/v4-theory`.
- Merge base: `5b34a4048c2b05feb45a0f3d9b8b25e6d9c36d78`.
- Frozen `research/model_v4` tree: `107c4c7172875fed949eccf15f4f9d25dde8dae4`.
- Frozen `sections_v3` tree: `16b8b3c6155ce94fd697abd482b779f9ae0662b9`.
- BID12 coding-rules Git blob: `f237d7662ff5a604c173529993b8a01ea62ab791`.
- BID12 coding-rules SHA-256: `e95c4f9f87d4224597f91b659251fd3b7f8d81ca748843ef7cc4a2c9255de0c6`, matching `empirics/output/bid12_run_meta.json`.

Preservation commits change branch tips, so compare protected tree and file hashes rather than expecting the earlier merge-preview tree ID.

## Authority map after consolidation

| Area | Authority | Treatment |
|---|---|---|
| Frozen theory | `research/model_v4/MODEL_CARD.md`, `research/model_v4/`, `sections_v3/` | Byte-preserve. Reopen only for a genuine logical error under the recorded freeze process. |
| Editable theory implementation | `numerical_v4/`, root `draft_v3*`, `deliverable/` | Build and edit in later campaigns without rewriting the frozen record. |
| Registered empirics | `research/empirics_v4/SPEC.md`, `decisions_2026-08-31.md`, `bid12_coding_rules.md`, `empirics/`, committed outputs and audits | Preserve estimands, viewed labels, gates, and hashes. No specification search. |
| Position 1 decision | `2026-08-31_gpt_pro_integration_angle_review.md:14-41,345-416,475-523,655-684,818-822` | Theory-led legal-clock paper; E1 is the only authorised December headline, conditional on its gates. |
| Provenance | `quality_reports/`, `.scratch/`, `docs/adr/`, `draft_v3_trace.md` | Retain evidence. Refresh stale statuses, not history. |
| Active learning state | `teach/` | Preserve in its own commit; exclude from manuscript builds. |

## Root-document rewrite checklist

The raw merge selects the theory-side `CLAUDE.md` and `AGENTS.md`. Rewrite them immediately after the merge. Remove or correct these nine stale statements while preserving the freeze and honesty rules:

1. `v4-theory/CLAUDE.md:9-10` says live work is only the theory lane.
2. `v4-theory/CLAUDE.md:12` names a surviving `v4-theory` lane.
3. `v4-theory/CLAUDE.md:14-16` identifies this checkout as the theory worktree and forbids empirical work.
4. `v4-theory/CLAUDE.md:26` treats empirics as an import from another lane and again forbids it locally.
5. `v4-theory/CLAUDE.md:77-79` says `.scratch/` remains split by branch and points to another worktree.
6. `v4-theory/AGENTS.md:9` says empirical work happens elsewhere.
7. `v4/CLAUDE.md:141` hard-codes the checkout as branch `v4`; instructions should describe the canonical repository, not a temporary checkout state.
8. `v4/CLAUDE.md:142-143` names `framework_v4.*` and the old reposition tracker as current targets; Position 1 and `draft_v3` supersede that description.
9. `v4/CLAUDE.md:144-145` carries only the empirical-lane orchestration rule; reconcile it with ADR-0008's theory safeguards and make one combined Git-ownership rule.

Also correct the incomplete layer/build lists and remove the RHEL-only host note from the unified macOS instructions. `CONTEXT.md` is byte-identical across the two branches and contains no lane rule; edit it only if a glossary term must change. Preserve ADR-0007 as history and supersede its two-lane operating rule in ADR-0009.

## Stale handoff and live to-do

Root `HANDOFF.md` still points to `jmp-upgrade-2026-05` and quotes superseded Fact 1 numbers. Before deleting it, move the unresolved UCL WRDS-access to-do into `research/empirical_feasibility.md` and `research/empirics_v4/data_inventory.md`, which currently cite that handoff. Annotate `data_inventory.md:123`: `SPEC.md:1448` records two SHA-256-verified off-repo CRSP copies, so the older no-backup sentence is stale.

## Position 1 follow-on

The next campaign's critical path is fixed by the GPT Pro review: evidence manifest, E1 protocol, unique-accession denominator and parser recovery, manual audit, immutable E1 artifact, independent reproduction, main table and CDF, manuscript reorganisation, appendix honesty ledger, and final theory/empirical QA. H1, H2, dose, stake, placebo, and BID12 remain viewed appendix evidence. They do not become headline tests.
