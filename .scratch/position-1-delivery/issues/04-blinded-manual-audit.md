# P1-04: Complete the 100-case blinded audit

Status: ready-for-agent
Blocked by: P1-03

## What to build

Run the registered 100-case audit against sealed automated parses, stratified by regime and parser route, with an independent second reader.

## Acceptance

- [ ] Draw the sample from the registered seed and reconciliation population; save a manifest with case IDs and strata before coding
- [ ] Keep automated trigger dates, accepted timestamps, delays, classifications, and aggregate E1 results hidden from the primary auditor until the audit key is sealed
- [ ] Save source excerpts, independent coded trigger and acceptance fields, material-error flags, and signed coder identities in separate audit and key files
- [ ] Permit at most two audited cases with any material date error
- [ ] Test and report error direction by regime under the registered rule; any directional pattern by regime fails the gate
- [ ] A second reader adjudicates every disagreement before the key is opened; preserve original readings and the full adjudication trail
- [ ] Publish a result note with counts, errors, direction check, disagreements, adjudications, hashes, and `PASS` or `NO-GO`; never edit the parser after unblinding without versioning it and repeating the affected gate

## Comments
