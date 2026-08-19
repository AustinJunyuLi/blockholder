# 16 — E8 · Draft-ready empirics section

**Lane:** empirics (`v4`, this machine)

**Routing:** per ADR-0005 — Opus writer (paper prose); Sonnet for LaTeX tables and figure inclusion; a separate Opus checker reads the section against the result notes.

**What to build:** The empirical section written as a standalone file under `sections_v3/` for inclusion in draft_v3, with its tables and figures: the design, the headline timing split, the bindingness dose, stake at filing, the bounded null, the run-up path, the matched DiD and bidder entry by liquidity.

**Blocked by:** 11 (E3), 12 (E4), 14 (E6), 15 (E7).

**Status:** ready-for-agent

- [ ] Section compiles on its own with xelatex, no undefined references
- [ ] Every number in the text and in the tables traceable to a committed script's output
- [ ] Every empirical claim carries the ESTIMATED label with its standard error and design; the bounded null presented as a ceiling, not an estimate
- [ ] A checker who did not write the section reads it against the result notes and reports every difference
- [ ] Session log entry and commit on `v4`

## Comments
