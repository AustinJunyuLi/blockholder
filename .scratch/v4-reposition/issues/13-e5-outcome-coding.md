# 13 — E5 · Outcome coding: bids within twelve months

**Lane:** empirics (`v4`, this machine)

**Routing:** per ADR-0005 — Sonnet for the filing pulls and the coding pass (mechanical); Opus adjudicates ambiguous cases and designs the audit; a separate agent re-does the audit sample blind.

**What to build:** For every initial 13D in the parsed universe, whether a bid arrived within twelve months — coded from tender-offer filings, merger proxies and current reports pulled through the existing pipeline and the EDGAR tools. Plus a thirty-filing hand audit against the coded outcome. This is the long pole for the control-outcome leg, so the coding rule and the twelve-month clock definition are written down before the pass starts. Output under `empirics/` and `research/empirics_v4/`.

**Blocked by:** 09 (E1).

**Status:** stale (2026-09-01) — targets the E5 twelve-month bid outcome coding of the August empirical record, deleted 2026-09-01 (history: 9b98089; record preserved in draft_v3_onlineappendix.tex §app:honesty). Do not execute.

- [ ] Outcome coded for every initial 13D by a committed script; the form types used and the twelve-month clock definition written down before coding
- [ ] Thirty-filing hand audit with the disagreement rate reported; the coding rule fixed wherever the audit found it wrong, then re-run
- [ ] The audit sample re-done blind by an agent who did not code the outcome
- [ ] Ambiguous cases listed as ambiguous rather than forced into a category
- [ ] Session log entry and commit on `v4`

## Comments
