# P1-01: Freeze the immutable evidence manifest

Status: ready-for-agent
Blocked by: `.scratch/v4-consolidation/issues/08-land-tag-and-retire-theory-worktree.md`

## What to build

Create one machine-readable manifest at `research/empirics_v4/e1_evidence_manifest_2026-09-01.json`. It fixes the pre-E1 state before any adopted filing-delay rerun.

## Acceptance

- [ ] Record the canonical branch and commit, environment and package versions, legal-calendar version, parser/code versions, and SHA-256 for every raw input, registered rule, current Fact 1 file, viewed estimate, audit record, and generated manuscript input that E1 could read or supersede
- [ ] Record each current result label, including old Fact 1 as unpublishable, provisional E1 numbers as read-only and unadopted, H1/H2/dose/stake/placebo/BID12 as viewed, and matched BID12 as `NOT ESTIMATED`
- [ ] Record the frozen `research/model_v4` and `sections_v3` tree hashes and the hash-stamped BID12 rules; do not modify any listed artifact
- [ ] Sort paths and keys so the manifest is deterministic; validate it with the standard-library JSON parser and write its SHA-256 to an adjacent `.sha256` file
- [ ] Commit the manifest before P1-02. Later corrections create a new dated manifest and preserve this file
- [ ] No parser, estimator, table, figure, or manuscript rerun occurs in this ticket

## Comments
