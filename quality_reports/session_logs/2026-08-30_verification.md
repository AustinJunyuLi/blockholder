# Session log — 2026-08-30 (verification lane) — E6 estimates independently re-run

**Lane:** empirics verification (ticket 11 checkbox: "a verifier who did not write the
script re-runs it from the manifest and matches every number"). Fresh session; none of the
scripts under test were written here. Full record:
`quality_reports/verification/2026-08-30_estimates_verify.md`. Nothing committed by this
session; committed outputs were preserved to `/tmp/verify_preserve/` before re-running and
restored afterwards (working tree left byte-identical to `v4` HEAD for all six files).

## What was done

1. Read `estimate_h1.py`, `estimate_h2.py`, `estimate_dose.py`, `estimate_stake.py`,
   `estimate_placebo_h1h2.py` against SPEC §2.3/§2.5/§2.6/§3.1–§3.5/§3.7/§4/§5/§6.
2. Re-ran all five with `.venv/bin/python` (CRSP load ~15 s; wild bootstrap 9,999 draws
   per regression; total wall ~4 min). Diffed against the preserved committed outputs.
3. Independent recomputation, own code only: (a) H1 main-sample N from
   `reparse_funnel.csv` + the script's exclusion rules re-applied to `h1_sample.csv`;
   (b) realised σ(RUNUP)/σ(JUMP)/σ(RUNUP5) from `h1_sample.csv`; (c) from-scratch OLS +
   Cameron–Gelbach–Miller two-way covariance reproducing H1's β2/SE and H2's δ/SE to 15
   significant digits; (d) Janover tail claim checked against raw CRSP rows (PERMNO 24072,
   $4.00 → $37.70 on 2025-04-07 — real).
4. Re-grepped `research/txt_extracts/sec_release_33_11253.txt` for every §6 figure
   (Table 3 ladder, 97%/3% prose, Table 2's 20%, 29%, 59%, $49m/$42m/$36m incl. the
   line-wrapped $26m, the p. 211 disclaimer, the 2,370 sample, absence of "$810 million").

## Result

**Overall verdict: MATCH.** All five re-run outputs identical to the committed ones except
the `generated_at` timing field; `h1_sample.csv` bit-identical; input hash in
`h1_estimate.json` matches the current `fact2_parsed.jsonl`; the §0-rule-1 JUMP-window
disclosure is present in `2026-08-30_link-coder-h1h2.md` §4 with both estimates.

Findings (all minor; none changes a verdict):

- Three full-frame-vs-estimation-sample labelling imprecisions in the commit messages /
  session logs: filer-type distribution 591/436/66 is the 1,093-row frame (main sample:
  523/394/62); "103 same-day filers" is the frame count (95 in the main sample);
  σ(JUMP) = 0.38 is the frame value (main sample 0.395, which is what `h2_estimate.json`
  itself carries). Plus one typo: "N = 979 (444 pre / 532 post)" — the corrected run is
  446/533.
- Script-vs-SPEC deviations (full list with file:line in the verification report): LIQ
  standardised on the full frame rather than the estimation sample (β2 moves +0.58 →
  +0.48 pp, MDE 4.38 pp — immaterial); dose regression adds LIQ to the registered
  controls; placebo runs full-funnel (disclosed); 90-day band inside the dose construction
  (disclosed); firm-only clustering row registered but not emitted; CUSIP tie-break
  unregistered; BIND_j built but never estimated.
- Pending, not claimed by any commit: §3.7's quarterly LIQ-slope pre-trend F-test; the 13G
  descriptive placebo (flagged in the placebo record's `not_run`).
- Record-keeping gap: only `h1_estimate.json` carries an input hash; the four downstream
  JSONs carry seeds only, and `crsp_daily.csv` is identified by basename alone.
