# 10 — E2 · Pre-specified empirical design

**Lane:** empirics (`v4`, this machine)

**Routing:** per ADR-0005 — Opus writer (design judgement); Sonnet for the data manifest and the file inventory; a separate Opus verifier checks the spec against the literature cards and against what is actually on disk.

**What to build:** The whole design written down before any estimation, under `research/empirics_v4/`. The timing split as the headline (run-up from trigger to filing versus the filing-day jump, by liquidity, before and after February 2024); the bindingness dose; stake at filing; the bounded null; the run-up path; the matched difference-in-differences on the twelve-month bid hazard against never-13D controls — sample, three-to-one matching on size, illiquidity, two-digit industry and quarter, outcome coding, confound list, power and minimum detectable effect, placebos on at least 500 dates, pre-trends; and bidder entry by liquidity. Plus a data manifest mapping every variable to a file on disk, a pull to be requested, or "not obtainable".

**Blocked by:** 05 (T1) — **soft: placeholder allowed.** The handoff at `research/model_v4/HANDOFF_sign.md` supplies only the slope sign for the post-2024 prediction. Write the spec with a marked placeholder and do not wait.

**Status:** done (2026-08-20) — awaiting Austin's approval before any estimation

- [x] Every referee-checklist item addressed (SPEC.md §12; power/MDE §§3.6, 5, 8.6; placebos 568 dates §8.7; pre-trends §8.8; parser validation cites the 11-check suite + hand audits)
- [x] Data manifest complete — 32 rows, each DISK / PULL / NONE; verifier executed every DISK row against the files (100% pass)
- [x] Supportive vs against written for every estimate (§10 + inline decision rules) before any estimate exists
- [x] Slope sign marked placeholder, dated 2026-08-20 (HANDOFF_sign.md absent from origin/v4-theory); BOTH branches specified so H2 is falsifiable either way
- [x] Opus verifier (did not write it) checked against cards + disk + arithmetic + the SEC release; open items in §13, none resolved by assumption
- [x] Session log entry and commit on `v4`

## Comments

- 2026-08-20 (Fable): Opus writer + Sonnet inventory + Opus verifier. One
  retry round: verifier found the §2.1 counts were filed-date-based under a
  trigger-date label (w 0.269→0.230) and the stake MDE used an inconsistent N;
  writer reproduced the counts independently, fixed both, recomputed all
  downstream MDEs; re-verify closed with "nothing new" (verifier conceded its
  own stake-SE and day-count arithmetic on re-check). SEC dates verified
  against the release itself: adopted 2023-10-10, effective 2024-02-05, XML
  mandate 2024-12-18; proposal 2022-02-10.
- Headline design: H1 (partition: run-up carries the liquidity slope, the
  filing-day jump does not) is sign-free — not hostage to the theory lane.
- Pre-registered power finding: the matched DiD's best MDE (4.4 pp) exceeds
  the 3 pp bounded-null rung — that leg can only rule out large effects.
- NEXT (ticket 11) is blocked on Austin approving this spec.
