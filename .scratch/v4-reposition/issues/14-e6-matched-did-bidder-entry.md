# 14 — E6 · Matched DiD on bid hazard, and bidder entry by liquidity

**Lane:** empirics (`v4`, this machine)

**Routing:** per ADR-0005 — Opus for the estimation and the result note; Sonnet for matching and table assembly; a separate verifier re-runs from the manifest.

**What to build:** The matched difference-in-differences on the twelve-month bid hazard against never-13D controls, run exactly as pre-specified — three-to-one matching, placebos, pre-trends, the power statement — plus bidder entry by liquidity on the same outcome coding. The estimate is reported next to the bounded null; where the design is underpowered, that goes in the number, not in a footnote.

**Blocked by:** 13 (E5); design from 10 (E2).

**Status:** stale (2026-09-01) — targets the E6 matched-DiD bid-hazard and bidder-entry-by-liquidity estimators of the August empirical record, deleted 2026-09-01 (history: 9b98089; record preserved in draft_v3_onlineappendix.tex §app:honesty). Do not execute.

- [ ] Estimate, standard errors, matching diagnostics, placebos and pre-trends all produced by a committed script following the pre-specified design; every departure from the spec named and justified in writing
- [ ] Bidder entry by liquidity estimated on the same outcome coding
- [ ] Result reported against the bounded null and the pre-specified minimum detectable effect; an underpowered result labelled underpowered
- [ ] A verifier who did not write the script re-runs it from the manifest and matches
- [ ] Plain-language result note carrying the ESTIMATED label; no spin
- [ ] Session log entry and commit on `v4`

## Comments
