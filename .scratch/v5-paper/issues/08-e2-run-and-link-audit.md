# 08 · Run E2 and audit the price link (E2-G2)

**Lane:** empirics. **Routing:** Grok in batch 1; the audit by a fresh Grok subagent that did not run E2.
**Blocked by:** 06, and the orchestrator's dated E2 direction note in `empirics/spec.md`.
**Blocks:** 10, 11.

**What to do.** `... run e2` writes `e2_estimate.json`, `e2_campaigns.csv`, `e2_runup_jump.pdf`;
gates E2-G1, E2-G3, E2-G4 evaluated in the run. The audit agent draws sixty matched campaigns
(seed 5, stratified by year), compares the CRSP issuer name with the filing's subject name, writes
`empirics/output/e2_audit.csv`, and records E2-G2.

**Acceptance.**
- [ ] Result file with all four gates evaluated; a NO-GO suppresses every E2 number.
- [ ] The direction note's date precedes the run (evidence: git log shown by the orchestrator).

**Status:** open; Grok batch 1 (`.scratch/v5-paper/grok/batch-1.md`)

## Comments
