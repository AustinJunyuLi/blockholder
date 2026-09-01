# Registered specification: the two empirical exercises

Registered by the commit that adds this file. Any later change to a measurement rule or a gate
is a dated amendment appended inside the relevant section, never an edit of the text above it.
A failed gate suppresses the exercise from the paper. It never licenses editing this file.

Both exercises are descriptive. They identify no effect, use no control group, and make no
causal claim. The paper says so where each appears.

## Shared population

- Universe: every initial Schedule 13D filing (form types `SC 13D` and `SCHEDULE 13D`; no
  amendments, no 13G) in the EDGAR quarterly form indexes for 2021 Q1 through 2025 Q4. EDGAR
  renamed the label to `SCHEDULE 13D` during 2025; both spellings are kept.
- Source texts: the local filing cache under `empirics/data/filings/`, which uses two file-naming
  schemes (accession with and without hyphens). The loader reads both. A filing absent from the
  cache is fetched once from EDGAR with the throttled fetcher and cached. The count of filings
  that could not be obtained is reported in the result file as `coverage.missing_text`.
- Unit: the campaign, one (subject CIK, trigger date) pair. Filings by several reporting persons
  on the same subject and trigger collapse to the accession with the earliest EDGAR acceptance.
- Trigger date: the date of the event which requires filing, read from the structured XML
  element when present and from the cover page otherwise, with the existing parser.
- Filing date: EDGAR's `date_filed` for the accession.
- Acceptance time: the header `ACCEPTANCE-DATETIME`, New York time.
- Period: pre if the trigger date is before 2024-02-05, post otherwise. The paper reports by
  calendar year as well; the pre and post cut is one comparison inside the yearly table.
- Campaigns with an unreadable trigger date are excluded and counted in `coverage.no_trigger`.

## The clock paragraph (not an exercise)

One paragraph of the paper documents that the filing clock moved. For every campaign, the delay
is the count of federal business days from the trigger date to the filing date, using the
holiday list in `empirics/facts.py`. The paper reports, by year and by period, the share of
campaigns filed within five business days and the median delay. These numbers live in the E1
result file under the key `clock`. No gate, no headline, no standard error beyond a bootstrap
interval on the two shares.

## E1: stake at filing

Object: the blockholder's stake on the filing date, B^F, measured as the percent of class on the
cover page (the maximum across reporting persons in a joint filing, in percent, on (0, 100]).

Reported: by year and by period, the mean, median, and the 25th and 75th percentiles of B^F;
the post-minus-pre difference in the mean and in the median with a campaign-level bootstrap
interval (2,000 draws, seed 5). The paper states the model's fixed-policy prediction for the
window cut next to the numbers and draws no causal conclusion from the comparison.

Gates:

- E1-G1 parse coverage. At least 90 percent of campaigns carry a stake value on (0, 100].
- E1-G2 blind audit. Sixty campaigns drawn at random, stratified by year and parser route, are
  hand-read by a worker who did not write the parser. At most three material errors, where a
  material error is a stake reading off by more than 0.5 percentage points or a wrong trigger
  date.
- E1-G3 differential coverage. The gap between the pre and post shares of campaigns with a
  readable stake is at most 10 percentage points.

Result file: `empirics/output/e1_estimate.json`. Campaign table: `empirics/output/e1_campaigns.csv`.
Figure: `empirics/output/e1_stake.pdf` (distribution of B^F by period).

## E2: run-up versus jump by pre-trigger liquidity

Objects: the run-up R and the jump J of the subject firm's price around the filing.

- Price link. The subject's CUSIP is read from the cover page (`issuerCUSIP` in the structured
  XML, the "CUSIP No." line otherwise). The campaign is matched to `empirics/data/crsp_daily.csv`
  on the first eight CUSIP characters against `CUSIP` and `HdrCUSIP`, with the SEC CIK-to-ticker
  map against `Ticker` as the fallback when the CUSIP has no match. A match must hold on every
  needed trading day. Run-up and jump are built from raw CRSP returns only; no derived event-study
  file is used.
- Market adjustment. The equal-weighted mean of `DlyRet` across all securities in the file on
  that day, computed from the file itself. A market-adjusted return is the security's return
  minus that mean.
- Reaction day. The filing date if the acceptance time is before 16:00 New York time, otherwise
  the next trading day.
- Run-up R: the cumulative market-adjusted return from the close of the last trading day before
  the trigger date to the close of the last trading day before the reaction day.
- Jump J: the market-adjusted return on the reaction day.
- Campaigns whose reaction day is on or before the trigger date have no pre-filing window and
  are excluded from E2, counted in `coverage.no_window`.
- Pre-trigger liquidity: the Amihud illiquidity ratio, the mean of |DlyRet| divided by dollar
  volume (|DlyPrc| times DlyVol) over trading days t-130 to t-11 relative to the trigger date,
  requiring at least 60 days with positive volume. Terciles are cut on the full E2 sample.
  Higher Amihud is lower liquidity.

Reported: by liquidity tercile and by period, the mean and median of R, J, and the run-up share
R/(R+J) on campaigns with R+J > 0, with campaign-level bootstrap intervals (2,000 draws, seed
5); and the same by year. The model's direction for the run-up share in κ enters this section by
a dated note once the v5 calibration grid has produced it, before the run. The paper reports the
direction the grid gives and the pattern the data show. It draws no causal conclusion.

Gates:

- E2-G1 link coverage. At least 80 percent of E1-eligible campaigns match a CRSP security with
  valid prices on every needed day.
- E2-G2 link audit. Sixty matched campaigns drawn at random, stratified by year, are checked by
  a worker who did not write the link, comparing the CRSP issuer name against the subject
  company name in the filing. At most three wrong matches.
- E2-G3 cell size. At least 100 campaigns in every tercile-by-period cell.
- E2-G4 differential coverage. The gap between the pre and post link-coverage shares is at most
  10 percentage points.

Result file: `empirics/output/e2_estimate.json`. Campaign table: `empirics/output/e2_campaigns.csv`.
Figure: `empirics/output/e2_runup_jump.pdf` (run-up share by tercile and period).

**Amendment, 2026-09-01, before any run.** Three changes to the E2 rules above. First, the
reported object is not a per-campaign share on campaigns with R + J > 0, which would condition on
the outcome. The paper reports, by cell, the mean and median of R and of J and the ratio of cell
means, mean R over (mean R plus mean J), with campaign-level bootstrap intervals on all three.
Second, gate E2-G1 counts coverage among campaigns whose subject CIK has a ticker in the SEC
company-tickers file, the listing proxy: at least 80 percent of those must link to CRSP with
valid prices on every needed day, and the share of all campaigns with such a ticker is reported
as `coverage.listed_share`. Third, campaigns with fewer than 60 valid pre-trigger days are
excluded from the liquidity split and counted in `coverage.no_liquidity`.

## Runner and tests

`empirics/fingerprints.py` builds the campaign table once and runs `e1` and `e2` from it.
`empirics/test_fingerprints.py` holds the gate checks and the number guard: it renders every
manuscript number from the two result files and asserts that each rendered string appears in
`paper.tex`. A gate failure writes `"status": "NO-GO"` into the result file and suppresses
every reported number for that exercise.
