# 07: Verify the integrated repository

**What to build:** A reproducible verification record showing that the combined branch builds, both authority trees and the BID12 rulebook remain byte-identical, existing checks pass, and no viewed empirical result was rerun or changed.

**Blocked by:** 04 and 05.

**Status:** ready-for-agent

- [ ] Create `.scratch/v4-consolidation/verification-log.md` with the integrated commit, both merge parents, environment versions, every command, exit status, elapsed time, and any retained warning
- [ ] Confirm `research/model_v4` tree = `107c4c7172875fed949eccf15f4f9d25dde8dae4`, `sections_v3` tree = `16b8b3c6155ce94fd697abd482b779f9ae0662b9`, and `research/empirics_v4/bid12_coding_rules.md` SHA-256 = `e95c4f9f87d4224597f91b659251fd3b7f8d81ca748843ef7cc4a2c9255de0c6`
- [ ] Run `.venv/bin/python -m numerical_v4.smoke`
- [ ] Enumerate and run every committed `quality_reports/fixes/t2_*.py` with `.venv/bin/python`; record one row per script and retain all existing truth labels, including failures or unresolved nodes that the check defines as expected
- [ ] Run `make clean && make all`; record generated-file counts and stop on any unexplained tracked diff
- [ ] Compile `draft_v3.tex` with XeLaTeX, Biber, then XeLaTeX twice; compile `draft_v3_onlineappendix.tex` twice after the main draft; record page counts and prove zero TeX errors, undefined references, or undefined citations
- [ ] Run the nine committed empirical self-check modules individually: `empirics.test_parse_13d`, `empirics.test_link_cik_cusip`, `empirics.test_recover_delisted_controls`, `empirics.test_bid12`, `empirics.test_bid12_audit_sample`, `empirics.test_bid12_control_lookup`, `empirics.test_estimate_bidder_entry`, `empirics.test_estimate_did`, and `empirics.test_estimate_did_diagnostics`
- [ ] Do not run `empirics.facts`, `reparse_fact2`, BID12 estimation, or any other viewed specification merely as a smoke test. Verify existing result hashes and recorded gates instead
- [ ] Compare `git status --short` and tracked file hashes before and after verification. Account for every generated file; no frozen tree, registered rulebook, viewed-result artifact, or empirical output changes
- [ ] Independent reviewer checks the verification log against the handoff's lines 190–208 and records PASS or exact blockers in `## Comments`

## Comments
