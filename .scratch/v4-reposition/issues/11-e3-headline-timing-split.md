# 11 — E3 · Headline: timing split, bindingness dose, bounded null

**Lane:** empirics (`v4`, this machine)

**Routing:** per ADR-0005 — Opus for the estimation calls and the result note; Sonnet for data assembly and tables; a separate verifier re-runs the committed script from the manifest.

**What to build:** The December number, secured before the long pole starts. Run-up from the trigger date to the filing date versus the filing-day jump, split by liquidity, before and after the February 2024 acceleration; the bindingness dose split (filers whose pre-rule delay ran past five business days against those already fast); and the bounded null computed from the SEC's own tables. One committed script, its outputs under `research/empirics_v4/` and `numerical_output/empirics/`, and a plain-language note saying whether the result is supportive, against, or a bounded null.

**Blocked by:** 09 (E1), 10 (E2).

**Status:** ready-for-agent

- [ ] Estimates, standard errors and the pre-specified robustness table all produced by a committed script, none by hand
- [ ] The bounded null computed from a named SEC table with the arithmetic shown, presented as a ceiling and not as an estimate
- [ ] A verifier who did not write the script re-runs it from the manifest and matches every number
- [ ] Plain-language result note carrying the ESTIMATED label with standard errors and the design; a null reported as a null, with no reframing
- [ ] Session log entry and commit on `v4`

## Comments
