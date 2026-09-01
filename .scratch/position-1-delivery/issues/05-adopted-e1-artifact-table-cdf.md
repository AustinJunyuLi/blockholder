# P1-05: Build the adopted E1 artifact, table, and CDF

Status: ready-for-agent
Blocked by: P1-04

## What to build

Create one deterministic E1 result builder and new `e1_*` outputs under `empirics/output/`. Leave every `fact1_*` file unchanged.

## Acceptance

- [ ] The builder reads only manifest and protocol inputs and emits a hashed `e1_estimate.json` as the single result authority
- [ ] The artifact records enumerated, eligible, resolved, ineligible, and unresolved counts by regime; coverage and unresolved-gap gates; audit verdict; complete-case estimates; worst-case bounds; confidence intervals; MDEs; and every input, code, and protocol hash. A companion output manifest records the artifact, table, CDF data, and rendered CDF hashes
- [ ] Generate a manuscript-ready summary table plus its data file, and an empirical CDF plus its plotted data, from `e1_estimate.json` in the same run
- [ ] Use campaign-level observations, accepted timestamps, effective public dates, and the registered business-day calendar. Keep acceptance and public-arrival results distinct, show accession-level estimates only as a sensitivity, and apply no delay screen or result-dependent exclusion
- [ ] Label historical estimates `VIEWED DESCRIPTIVE`; label any prospective extension under its registered power verdict; state `causal_claim: false`
- [ ] Preserve old Fact 1 and provisional values as prior records. The new artifact receives a new name, timestamp, and hash
- [ ] One clean rerun of the builder reproduces every output locally. If coverage, unresolved-gap, audit, discretionary-choice, or consistency gates fail, write a `NO-GO` artifact and do not create a headline claim

## Comments
