# 02: Preserve v4-theory intentional dirty work in split commits

**What to build:** Every piece of live theory-lane work (manuscript rewrite, refreshed PDFs, deliverables move, teaching workspace, provenance extract, narrowed legal note) is committed on `v4-theory` so the merge carries it, split per handoff line 188.

**Blocked by:** None.

**Status:** resolved

- [x] Commit A (manuscript sources): `draft_v3.tex`, `draft_v3_trace.md`, `quality_reports/session_logs/2026-08-30_draft_v3_team_review_brief.md`, untracked `quality_reports/session_logs/2026-08-30_draft_v3_prose_rewrite_onepager.md`
- [x] Commit B (generated deliverables): `deliverable/draft_v3.pdf`, `deliverable/draft_v3_onlineappendix.pdf`
- [x] Commit C (deliverables move): the four `deliverables/` deletions — binaries proven byte-identical in git history; `deliverable/` is canonical
- [x] Commit D (teaching workspace): `teach/`
- [x] Commit E (legal note): header narrowed to what was verified (US/UK checked; DE/FR/NL/IT rows unchecked; IT claim unsourced; cites card stamp 2026-08-28/59c0dfc, now 2026-08-30/65b8db3 — mark non-authoritative), moved to `research/notes/legal_regime_portability.md`, committed
- [x] Commit F (provenance): `research/txt_extracts/gpt_pro`
- [x] Frozen trees untouched: `git rev-parse 'v4-theory:research/model_v4'` = `107c4c71…`, `'v4-theory:sections_v3'` = `16b8b3c6…` after all commits
- [x] Every file created after the 2026-09-01 inventory is accounted for. The unrelated Amp research report was relocated outside the repository with its exact SHA-256 preserved
- [x] Leftover untracked on v4-theory: only ticket-06 cleanup targets

## Comments

Resolved 2026-09-01. Commits: `532d3df` manuscript sources, `6ea4908` refreshed PDFs, `e050236` duplicate deliverables, `cfdb88a` teaching workspace, `e4866e9` legal note, and `80ce7ae` GPT Pro provenance. Frozen tree hashes remain `107c4c7172875fed949eccf15f4f9d25dde8dae4` and `16b8b3c6155ce94fd697abd482b779f9ae0662b9`. The unrelated report is now `/Users/austinli/Documents/Codex/2026-09-01/claude-subscription-amp-research.md`, SHA-256 `8f8fd5a97846b21c1979020033e40a44128fc2eaf5d5730aeed6c48b2e85a555`.
