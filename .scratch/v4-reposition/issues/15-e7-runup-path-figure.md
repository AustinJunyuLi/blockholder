# 15 — E7 · Run-up path figure

**Lane:** empirics (`v4`, this machine)

**Routing:** per ADR-0005 — Sonnet (mechanical figure work in the existing house style); a separate agent re-runs the script and checks the drawn values against the underlying table.

**What to build:** The daily price path of the target from the trigger date to the filing date, split by liquidity and by before/after February 2024, drawn in the project's existing figure style. Cheap, and can run any time after the parser fixes. Output under `numerical_output/empirics/`.

**Blocked by:** 09 (E1).

**Status:** stale (2026-09-01) — targets the E7 run-up path figure of the August empirical record, deleted 2026-09-01 (history: 9b98089; record preserved in draft_v3_onlineappendix.tex §app:honesty). Do not execute.

- [ ] Figure produced by a committed script from data on disk, vector output in the existing house style
- [ ] The number of filings behind each line shown in the figure or its note
- [ ] A verifier who did not draw it re-runs the script and confirms the plotted values against the underlying table
- [ ] Session log entry and commit on `v4`

## Comments
