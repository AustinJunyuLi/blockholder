# E1: realised filing delay around the Feb-2024 acceleration

Registered 2026-09-01. This file is the specification. Committing it before any run is the
registration. Git commit order is the evidence; there are no hash chains, sidecars, or
manifests.

## Question

Did the realised delay between the trigger event and the Schedule 13D filing fall after the
Feb-2024 acceleration moved the window margin from 10 calendar days to 5 business days?

## Claim boundary

E1 is descriptive. It is a before-and-after comparison with no control group. It does not
identify an effect on liquidity, returns, activism, bidder entry, takeover premia, or control
outcomes. It does not test L2 or T1. Prose may not promote it.

## Population

Every `SC 13D` original listed in the EDGAR quarterly form indexes for:

- pre: 2023Q2 and 2023Q3, 616 filings
- post: 2024Q3 and 2024Q4, 521 filings
- total: 1,137 filings

Form-type match takes both EDGAR spellings, `SC 13D` and `SCHEDULE 13D`, and excludes both
amendment spellings. The full universe, not a sample.

**Amendment, 2026-09-01, before any run.** The registering commit gave the post window as 904
filings. That count came from a grep for `SC 13D` alone and missed the `SCHEDULE 13D` spelling
EDGAR adopted during 2024Q3: 18 filings in Q3 and 114 in Q4. The correct post count is 1,036 and
the correct total is 2,259. No outcome had been parsed, so this corrects an enumeration error and
not a result. The original count is preserved in this note and in commit 28ad200.

**Second amendment, 2026-09-01, after a diagnostic run and before any reported result.** The
counts above were index-row counts. `form.idx` is filer-indexed: one joint filing appears once
per reporting person, under each person's CIK, every row pointing at the same accession. A
first run enumerated 2,259 rows and then collapsed 1,633 resolved rows into 680
subject-trigger campaigns, a ratio that exposed the duplication rather than any property of
group filings. Counting unique accessions gives 616 pre and 521 post, 1,137 in total, which
matches the independently recorded denominator from the discarded lane. The enumeration now
collapses on accession before parsing. This corrects how the population is counted, not what
counts as a population, and no estimate or gate verdict from the diagnostic run is carried
forward.

## Unit

One row per `(subject_cik, trigger_date)`. Where a reporting group files simultaneously on the
same subject and trigger, keep the earliest accession by acceptance timestamp, breaking ties on
accession string. Accession-level estimates are reported as a sensitivity.

## Measurement

- Trigger date: "Date of Event Which Requires Filing". Structured XML tag first, cover-page
  regex second.
- Filing date: the EDGAR `ACCEPTANCE-DATETIME`. Acceptance after 17:30 America/New_York rolls
  the effective date to the next business day.
- Delay: federal business days from trigger date to effective filing date, computed with
  `numpy.busday_count` against the federal holiday list generated in `empirics/facts.py`.

## Status

Every enumerated accession receives exactly one status: `resolved`, `ineligible`, or
`unresolved`, each with a reason code. No row disappears because its delay is negative, long,
missing, or inconvenient.

There is no outcome screen. No filing is dropped for an implausible delay. Extremes stay
visible and are reported separately as a data-quality item.

## Estimands

- Primary: the share of filings with delay of 5 business days or fewer, pre and post, and the
  post-minus-pre difference.
- Co-primary: the median delay in business days, pre and post.
- Secondary: the empirical CDF of delay in each period.

## Inference

Cluster bootstrap on `subject_cik`, 2,000 draws, seed 20260901, percentile confidence intervals
at 95 percent.

## Bounds

Report worst-case lower and upper bounds on the primary share and on the post-minus-pre
difference, assigning every unresolved eligible filing to the extreme that most hurts the claim
and then to the extreme that most helps it. Report the bounds beside the complete-case
estimates, never instead of them.

## Gates

Three gates, all binding. A failure writes a `NO-GO` note and suppresses the headline. A
failure does not license editing this file.

**G1, worst-case bound.** The worst-case lower bound on the post-minus-pre difference in the
primary share is above zero.

This gate has a known feasibility threshold, derived before registration from the June 2026
sample (resolved shares 0.357 pre and 0.756 post; parse rates 0.68 pre and 0.64 post):

```
worst-case post lower = 0.756 x 0.64        = 0.484
worst-case pre  upper = 0.357 x 0.68 + 0.32 = 0.563
worst-case difference                       = -0.079
```

Solving `0.756r - [0.357r + (1-r)] > 0` for a common resolved rate r gives **r > 71.5 percent**.
G1 therefore cannot pass below roughly 72 percent coverage in each period. Raising coverage to
at least 75 percent is a prerequisite of the run, not an adjustment made after seeing a result.
Parser improvement and manual recovery are measurement work; they change no rule in this file.

If the bound still fails to clear zero at achieved coverage, the paper reports the bounded range
as the result and claims no decline. That is a finding about what this data supports.

**G2, differential coverage.** The absolute gap between the pre and post unresolved shares is at
most 10 percentage points.

This is the live hazard. Structured XML became mandatory on 2024-12-18, inside the post window,
so post filings parse more easily than pre filings by construction. Differential coverage alone
would manufacture the primary result. G2 catches it.

**G3, parser validation.** Hand-code 60 filings, stratified by period and parse route, before
seeing the parser's answer for those cases. At most 3 material date errors, and no directional
pattern of errors by period. Parser validation is on the referee checklist.

The blind is enforced by commit order. The audit sample carries case IDs and source excerpts and
no parser output. Coding is committed before the comparison runs.

**Third amendment, 2026-09-01, before the audit sample was drawn.** Fifteen cases per
period-by-route stratum cannot yield 60: the pre-xml stratum is empty, because structured XML did
not exist before 2024-12-18, so the non-empty strata are pre-text, post-text, and post-xml. The
allocation is 20 cases per non-empty stratum, 60 in total. A material error is any disagreement
between the hand-coded and the parsed trigger date; there is no de minimis tolerance. The error
threshold and the blind are unchanged. This corrects an infeasible allocation, not the gate.

**Fourth amendment, 2026-09-01, recording how the executed audit ran.** Two records, no rule
changes. First, the 20 xml-route excerpts in the audit sample read LABEL NOT FOUND, because the
excerpt window targets the cover-page label that xml submissions do not carry; those cases were
hand-coded from the `dateOfEvent` element in the cached source document, the text a human coder
would read. No parser output was consulted for any case, and the coding commit preceded the
scoring run. Second, a post-audit scan found 10 of 521 post filings (0 of 616 pre) whose document
body declares a non-zero amendment number although the index lists them as SC 13D originals. The
population stays as registered: it is defined by the index form type, these rows can only depress
the post-period share, and removing them after seeing results would help the claim. They are
noted here as a data-quality item for the manuscript's missingness and data-quality discussion.

## Outputs

`empirics/output/e1_delays.csv`, `e1_estimate.json`, `e1_cdf.pdf`. The JSON is the single result
authority and records per-period enumerated, resolved, ineligible and unresolved counts, all
three gate verdicts, complete-case estimates, worst-case bounds, confidence intervals, the seed,
and `causal_claim: false`.
