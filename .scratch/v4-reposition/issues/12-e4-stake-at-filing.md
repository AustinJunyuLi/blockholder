# 12 — E4 · Stake at filing

**Lane:** empirics (`v4`, this machine)

**Routing:** per ADR-0005 — Sonnet for extraction and tabulation (mechanical); Opus reads the result against the model's prediction; a separate verifier re-runs the script.

**What to build:** The distribution of the percent of class printed on the 13D — the empirical counterpart of the two-round model's stake-at-filing object — before and after the February 2024 acceleration and split by liquidity. Reads the theory lane's prediction from `research/model_v4/HANDOFF_sign.md` if it has landed, and reports the number either way. Output under `research/empirics_v4/`.

**Blocked by:** 09 (E1) — the percent-of-class field is only trustworthy after the parser fix. Reads 05 (T1)'s prediction if it exists; soft, does not wait.

**Status:** ready-for-agent

- [ ] Distribution plus the before/after and liquidity splits produced by a committed script
- [ ] Filings whose percent of class could not be parsed counted and reported, never silently dropped
- [ ] Compared against the theory prediction if the handoff has landed; otherwise reported as a standalone fact and labelled as such
- [ ] A verifier who did not write the script re-runs it and matches
- [ ] Session log entry and commit on `v4`

## Comments
