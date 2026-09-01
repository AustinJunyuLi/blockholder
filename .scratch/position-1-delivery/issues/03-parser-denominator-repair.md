# P1-03: Repair the E1 parser and denominator

Status: ready-for-agent
Blocked by: P1-02

## What to build

Implement the smallest protocol-conforming parser repair and produce a deterministic one-row-per-accession reconciliation file, one-row-per-campaign analysis file, and an unresolved-case queue.

## Acceptance

- [ ] Enumerate every initial 13D accession in the fixed 2023Q2-Q3 and 2024Q3-Q4 EDGAR windows before applying any parser result
- [ ] Apply the registered amendment, issuer, reporting-group, campaign-collapse, trigger-source, accepted-timestamp, effective-public-date, and legal-calendar rules exactly; preserve raw source pointers and source/parser hashes
- [ ] Reconcile every enumerated accession to `resolved`, `ineligible`, or `unresolved` with a predeclared reason. No row disappears because its delay is negative, long, missing, or inconvenient
- [ ] Manually recover every residual historical case whose filing contains a usable trigger date; retain the remaining queue for audit and bounds
- [ ] Reach at least 95 percent resolved trigger classification among eligible campaigns separately in each historical regime; report the accession-level rate as a sensitivity
- [ ] Hold the absolute pre/post unresolved eligible-campaign share gap to at most 3 percentage points. Any larger gap is a failed gate, not permission to narrow the sample
- [ ] Add one focused runnable check covering unit identity, deduplication, accepted timestamp, status exhaustiveness, no delay screen, and regime-level gate arithmetic; all existing relevant fixtures still pass
- [ ] Commit code, reconciliation output, unresolved queue, hashes, exact command, and gate verdict. Stop with `NO-GO` if either binding gate fails

## Comments
