# P1-02: Register the E1 protocol

Status: ready-for-agent
Blocked by: P1-01

## What to build

Write `research/empirics_v4/e1_protocol_2026-09-01.md` and its machine-readable twin `research/empirics_v4/e1_protocol_2026-09-01.json`. Commit both before processing an adopted outcome.

## Acceptance

- [ ] Fix the primary unit as one subject-trigger campaign. Reconcile every unique initial Schedule 13D accession, exclude amendments, use accession as the immutable source key, collapse simultaneous reporting-group filings under the predeclared hierarchy, and report accession-level estimates only as a sensitivity
- [ ] Fix the historical populations to all eligible initial filings in 2023Q2-Q3 and 2024Q3-Q4, and the prospective population to all eligible initial filings accepted from 1 September through 20 November 2026
- [ ] Fix the same-subject, same-trigger, same-group deduplication hierarchy and deterministic tie-breaks before parsing
- [ ] Define filing acceptance from the EDGAR accepted timestamp, effective public arrival from the registered EDGAR cut-off rule, trigger date from the contemporaneous source hierarchy, and both delays from a versioned federal-business-day calendar. Keep acceptance and public arrival separate in every artifact and manuscript sentence
- [ ] Keep every enumerated accession in a reconciled status of `resolved`, `ineligible`, or `unresolved`; specify reason codes and the eligible denominator
- [ ] Use no 0-to-60-day, 0-to-90-day, or other outcome-based delay screen in the primary sample. Extreme or impossible delays remain visible for source adjudication and data-quality reporting
- [ ] Predeclare worst-case lower and upper bounds for the within-five-business-days share, its post-minus-pre difference, and the median using all unresolved eligible campaigns; report complete-case estimates and the accession-level sensitivity beside the bounds
- [ ] Fix the primary within-five-business-days share, co-primary business-day median, secondary CDF and quantiles, inference, audit seed and strata, parser gates, prospective power gate, all acceptance tests, and the 25 September kill rule
- [ ] Label historical E1 as viewed descriptive evidence and prospective 2026 evidence as persistence confirmation only if its blind power gate passes. State explicitly that neither supports a causal claim
- [ ] Validate Markdown and JSON agreement with one small runnable check, record both hashes, and commit. Stop before the adopted parser run

## Comments
