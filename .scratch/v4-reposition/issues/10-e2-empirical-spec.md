# 10 — E2 · Pre-specified empirical design

**Lane:** empirics (`v4`, this machine)

**Routing:** per ADR-0005 — Opus writer (design judgement); Sonnet for the data manifest and the file inventory; a separate Opus verifier checks the spec against the literature cards and against what is actually on disk.

**What to build:** The whole design written down before any estimation, under `research/empirics_v4/`. The timing split as the headline (run-up from trigger to filing versus the filing-day jump, by liquidity, before and after February 2024); the bindingness dose; stake at filing; the bounded null; the run-up path; the matched difference-in-differences on the twelve-month bid hazard against never-13D controls — sample, three-to-one matching on size, illiquidity, two-digit industry and quarter, outcome coding, confound list, power and minimum detectable effect, placebos on at least 500 dates, pre-trends; and bidder entry by liquidity. Plus a data manifest mapping every variable to a file on disk, a pull to be requested, or "not obtainable".

**Blocked by:** 05 (T1) — **soft: placeholder allowed.** The handoff at `research/model_v4/HANDOFF_sign.md` supplies only the slope sign for the post-2024 prediction. Write the spec with a marked placeholder and do not wait.

**Status:** ready-for-agent

- [ ] Every referee-checklist item addressed: control group or bounded null, confound list, power and minimum detectable effect, placebos, pre-trends, parser validation
- [ ] Data manifest complete — each variable maps to a file on disk, a flagged pull, or "not obtainable"
- [ ] What would count as supportive and what as against, written down before any estimate exists
- [ ] The slope sign either taken from the handoff file with its date, or clearly marked as a placeholder
- [ ] A verifier who did not write the spec checks it against the cards and against the data on disk; open items listed rather than resolved by assumption
- [ ] Session log entry and commit on `v4`

## Comments
