# Re-fetch and re-parse of the full 13D universe — realised counts and recomputed MDEs

**Date:** 2026-08-30 · **Executes:** SPEC §2.2 (mandatory re-parse) and SPEC §13 item 2 (BLOCKING — now closable)
**Script:** `empirics/reparse_fact2.py` (committed, resumable, `--link-file` ready) · **Data:** `empirics/data/fact2_parsed.jsonl` (rewritten), old file archived as `empirics/data/fact2_parsed_oldparser_2026-08-20.jsonl`
**Outputs:** `empirics/output/reparse_funnel.csv`, `reparse_quarterly_parse_rates.csv`, `reparse_counts.json`
**Nothing here is an estimate.** These are counts and power arithmetic on realised counts, exactly the pre-specification inputs §0 allows.

---

## 0. The finding that reorganises everything: the old file double-counted the universe

EDGAR's quarterly `form.idx` lists every 13D **twice** — once under the filer's CIK
directory and once under the subject's (same accession number, same submission text).
The old pipeline never deduplicated. The archived old file has **9,234 rows but only
4,639 unique accessions** (9,190 rows sit in duplicate pairs; 44 filings are listed once).
Every SPEC §2.1 count, the §2.2 prediction, and the §3.6/§8.6 power tables were computed
on that file and are therefore inflated by a factor of ~2 in their levels (ratios like
`w` are roughly unaffected).

The re-parse enumerates **9,234 idx rows → 4,639 unique initial 13D filings**
(2022Q1–2025Q4, `SC 13D`/`SCHEDULE 13D`, amendments excluded). External consistency:
SEC Release 33-11253 Table 2 puts initial 13Ds at ~1,430/year over 2011–2021;
4,639 over four years (~1,160/year) is in range, whereas 9,234 (~2,300/year) was not.

**Consequence for the SPEC's power story:** the realised N is roughly half of what §2.2
predicted, and every MDE below moves accordingly. The post share `w` moved the other way
(up), because the parser fixes recover mostly post-era filings. Net: MDEs worsen by
roughly √2 relative to the printed post-re-parse projections.

## 1. Headline realised counts (trigger-date split, §2.5 assignment)

| | Pre (TD < 2024-02-05) | Post (TD ≥ 2024-02-05) | Total | w |
|---|---|---|---|---|
| Trigger date parsed | 1,945 | 1,765 | 3,710 | 0.476 |
| …and CUSIP (carry-forward) | 1,615 | 1,626 | 3,241 | 0.502 |
| **CRSP-matched sample (funnel step 3)** | **755** | **710** | **1,465** | **0.485** |
| **Estimation sample (funnel step 4, deduped)** | **569** | **543** | **1,112** | **0.488** |

**Realised vs the §2.2 prediction** (pre ~3,000 stable, post ~1,950, N ≈ 4,950, w ≈ 0.394):
realised N is **1,465** (CRSP-matched) — far below 4,950 — and w is **0.485**, above 0.394.
The prediction was written on the double-counted base. Like-for-like (unique filings,
old parser → new parser), the pre leg with trigger+CUSIP went **1,509 → 1,615** (+7%;
the "pre leg is stable" prediction holds in direction) and the post leg went
**451 → 1,626** (3.6×; the 2025 XML fix plus the cover-page fixes).

## 2. The §2.3 attrition funnel (realised; canonical = provisional carry-forward CUSIP link)

| Step | n | pre | post | dropped | notes |
|---|---|---|---|---|---|
| 0. Enumerated initial 13Ds | 4,639 | — | — | — | 9,234 idx rows; 4,595 duplicate subject/filer index rows dropped |
| 1. Trigger date parsed | 3,710 | 1,945 | 1,765 | 929 | 80.0% overall parse rate |
| 2. 0 ≤ (FD−TD) ≤ 90 cal. days | 3,356 | 1,683 | 1,673 | 354 | 2 negative-gap, 352 over 90d; **119 of the 153 stale 2014–2021 triggers drop here** (the 34 survivors are legitimate Oct–Dec 2021 triggers filed in early 2022) |
| 3. Subject links to CRSP PERMNO (common + US + ≥60 valid obs in [TD−126, TD−6]) | 1,465 | 755 | 710 | 1,891 | no_cusip 415 · cusip_not_in_crsp 1,235 · insufficient_obs 241 |
| 4. One obs per (firm, trigger), 365-day keep-first | 1,112 | 569 | 543 | 353 | 139 exact (firm, TD) duplicates; **214 flagged-second** within 365 days |

**Every row of step 3 is provisional**: the match uses CUSIP values carried forward from
the old file (3,998 of 4,639 filings carry one; 641 get null). The rebuilt link landed
mid-run — see §7. Conventions used (stated, not in the SPEC's wording): the observation
window [TD−126, TD−6] is read as **calendar days**; a "valid" day has DlyRet, nonzero
DlyPrc and positive DlyVol all present; the common-stock screen is `ShareType == 'NS'`
(the snapshot's dominant equity code) with `USIncFlg == 'Y'`.

**Step-3 attrition decomposition** (of the 1,235 `cusip_not_in_crsp`): 462 CUSIP8s are
absent from the CRSP snapshot entirely; 773 are present but fail eligibility —
per-filing classification: **406 foreign-incorporated common (NS,N), 86 ADRs, 74
beneficial-interest/REIT-like (SB), 13 units (UG)**, 194 mixed-history. The 74 SB cases
are the only judgement-call bucket (REITs are 13D targets but are not "common stock" by
the ShareType code). Reported, not changed.

## 3. Per-quarter trigger-date parse rates (the referee's first number)

| Quarter | n | parsed | rate | old parser (deduped) |
|---|---|---|---|---|
| 2022Q1 | 319 | 216 | 0.677 | 0.621 |
| 2022Q2 | 266 | 202 | 0.759 | 0.711 |
| 2022Q3 | 324 | 257 | 0.793 | 0.744 |
| 2022Q4 | 255 | 175 | 0.686 | 0.651 |
| 2023Q1 | 295 | 208 | 0.705 | 0.634 |
| 2023Q2 | 310 | 213 | 0.687 | 0.635 |
| 2023Q3 | 306 | 214 | 0.699 | 0.660 |
| 2023Q4 | 349 | 259 | 0.742 | 0.719 |
| 2024Q1 | 313 | 241 | 0.770 | 0.693 |
| 2024Q2 | 266 | 215 | 0.808 | 0.714 |
| **2024Q3** | 241 | 171 | **0.710** | 0.598 |
| **2024Q4** | 280 | 224 | **0.800** | 0.554 |
| **2025Q1** | 269 | 269 | **1.000** | 0.000 |
| **2025Q2** | 273 | 273 | **1.000** | 0.000 |
| **2025Q3** | 278 | 278 | **1.000** | 0.000 |
| **2025Q4** | 295 | 295 | **1.000** | 0.000 |

**The §2.2 prediction "the 2025 failure is fixed" is confirmed: 0% → 100%** (all 1,115
2025 filings parse via `<dateOfEvent>`). 2024Q3/Q4 rise from 57% (deduped old) to 76%.
Note, however: the pre-XML cover-page path still leaves a **~20–30% unparsed residual**
in every 2022–2024 quarter — the SPEC's "its triggers are all pre-2024 and already
parse" assumption is only ~70–80% true. This is a parser-coverage fact, reported for
the record; no design change is implied.

## 4. The §2.1 tables, rebuilt on unique filings

*Split on filing date (reference only):*

| | Filed pre 2024-02-05 | Filed on/after | Total |
|---|---|---|---|
| Initial 13Ds parsed | 2,545 | 2,094 | 4,639 |
| …with a parsed trigger date | 1,834 | 1,876 | 3,710 |
| …with trigger date **and** CUSIP | 1,523 | 1,718 | 3,241 |
| …with a parsed percent-of-class | 2,252 | 2,026 | 4,278 |

*Split on trigger date — the design's split:*

| | TD < 2024-02-05 | TD ≥ 2024-02-05 | Total |
|---|---|---|---|
| …with a parsed trigger date | 1,945 | 1,765 | 3,710 |
| …with trigger date **and** CUSIP | 1,615 | 1,626 | 3,241 |

Unique subject CIKs (filed-date split): **1,617 pre / 1,430 post / 2,735 total (312 in
both)** — unchanged from the SPEC (dedup-invariant). Unique filer CIKs: **3,503** —
confirmed. Trigger-year distribution: **835 / 879 / 819 / 1,024** in 2022/2023/2024/2025
(old parser, deduped: 779 / 815 / 605 / **0**), plus **153 stale 2014–2021 triggers**
(old: 273 idx rows ≈ 138 unique). **111 filings straddle** (TD < 2024-02-05 ≤ FD;
old-parser unique: 92); 10 of them survive into the estimation sample and are excluded
from the main sample at estimation time per §2.5 — the funnel itself is §2.3-only.

## 5. Accepted timestamps: route and verification

The master `.txt` carries `<ACCEPTANCE-DATETIME>` in its SGML header in **both eras**
(verified on 2022 and 2025 samples), so no submissions-API calls were needed:
**4,639/4,639 recovered, 0 API fallbacks** (the API route with per-CIK caching is
implemented in the script as a fallback). Verification against the old file: **20/20
exact string agreement** on a random sample of overlapping rows. Sanity: the
after-4pm share is 67.4% filed pre-rule vs 67.5% filed post-rule — no era break in the
timestamp itself (the 5:30→10:00 pm cut-off move matters for the FD* derivation at
estimation time, not for the parse).

## 6. The §4 dose-filer recount — SPEC §13 item 8's suspicion is confirmed

Old-parser claim: 2,004 of ~2,016 pre-period filer CIKs with ≥ 2 pre-period filings,
covering 5,046 of 5,058 filings. **That was a double-listing artefact** — every filer
with one real filing appeared to have two. Realised, on unique filings:

| Window | Filings | Filer CIKs | Filers with ≥ 2 | Filings they cover |
|---|---|---|---|---|
| §4 dose window 2022-01-01 → 2023-10-09 | 2,098 | 1,710 | **189 (11.1%)** | **577 (27.5%)** |
| Old claim's basis: filed < 2024-02-05 | 2,545 | 2,016 | **241 (12.0%)** | **770 (30.3%)** |

The repeat-filer restriction no longer "costs almost nothing" — it retains ~28% of
pre-period filings. The §4 stratum-imputation fallback for single-filing filers becomes
load-bearing for most of the sample. **Reported, not changed** — the dose construction
itself is untouched.

## 7. The rebuilt CIK→CUSIP link landed mid-run — status

`empirics/output/cik_cusip_link.csv` (2,735 subject CIKs) currently matches **978 CIKs
(35.8%)**, covering 1,672 of 4,639 filings; match routes: ticker_unique 971,
name_fallback 7, ambiguous_ticker 10, unmatched 892, unmatched_name 855. Where both
sources carry a CUSIP (1,509 filings), CUSIP8 agreement with the carry-forward values is
**71.0%** — the disagreements are dominated by issuer-CUSIP changes over time (the
carry-forward value is the filing-era cover-page CUSIP; the link maps to the CRSP header
CUSIP; `cik_cusip_link_disagreements.csv` shows e.g. 72303P107 → 72303P50). Because the
CRSP join here uses both the daily `CUSIP` and `HdrCUSIP` columns, filing-era CUSIPs are
usable directly. Union coverage of the two sources is 4,161 of 4,639 filings (89.7%).

The canonical outputs above use the task-specified **provisional carry-forward** route.
For comparison, the funnel regenerated with `--link-file` (rebuilt link only) gives:
step 3 = **1,064** (518 pre / 546 post; drops: no_cusip 2,135, insufficient_obs 157),
step 4 = **807** (395 / 412). Which source becomes canonical — carry-forward,
rebuilt-only, or union — is an orchestrator decision; the script regenerates any of them
in ~1 minute from cache.

## 8. MDE arithmetic on realised counts (σ stays an assumption, per instructions)

σ(JUMP) = 0.12, σ(RUNUP) = 0.15 remain **assumptions** (no card prints a 13D window-CAR
SD); GS base rates p_T = 0.181 / p_C = 0.072 stay until BID12 exists. 2.802 = z₀.₉₇₅ +
z₀.₈₀ throughout.

### 8.1 SPEC §3.6 — timing-split slope MDE

Formula: SE(δ̂) = σ / √(N·w(1−w)), MDE = 2.802·SE.

**Headline — CRSP-matched sample** (N = 1,465, w = 710/1,465 = 0.4846):
w(1−w) = 0.24978; √(1,465 × 0.24978) = √365.93 = **19.129**.

| Series | σ | SE | MDE | MDE ×1.1–×1.9 clustering |
|---|---|---|---|---|
| JUMP | 0.12 | 0.12/19.129 = 0.63 pp | 2.802 × 0.627 = **1.76 pp** | 1.93 – 3.34 pp |
| RUNUP | 0.15 | 0.15/19.129 = 0.78 pp | 2.802 × 0.784 = **2.20 pp** | 2.42 – 4.17 pp |

**Variant — estimation sample** (N = 1,112, w = 0.4883, √ = 16.669): JUMP SE 0.72 pp,
MDE **2.02 pp** (2.22–3.83); RUNUP SE 0.90 pp, MDE **2.52 pp** (2.77–4.79).

> **Honest reading, restated on realised counts:** the design can detect a liquidity
> slope of roughly **1.9–4.2 pp per sd of illiquidity** (CRSP-matched; **2.2–4.8 pp** on
> the estimation sample), against the printed post-re-parse range of **1.1–2.3 pp**.
> Against Zeng's 2.8% mean trigger-to-filing run-up, the realised range is ~70%–170% of
> the level (printed: 40–80%). The "not powered to find a small partition effect"
> conclusion stands and strengthens.

### 8.2 SPEC §8.6 — matched-DiD MDE

Formula: SE = √(0.1705 · (1/n_pre + 1/n_post)), MDE = 2.802·SE, ×1.31 clustering;
0.1705 = 0.181×0.819 + 0.072×0.928/3.

| Sample | n_pre | n_post | 1/n_pre + 1/n_post | SE | MDE | ×1.31 | % of 18.1% base |
|---|---|---|---|---|---|---|---|
| **S1 (estimation sample)** | 569 | 543 | 0.0035991 | 2.48 pp | **6.94 pp** | **9.09 pp** | 50% |
| S1 variant (CRSP-matched) | 755 | 710 | 0.0027330 | 2.16 pp | 6.05 pp | 7.92 pp | 44% |
| **S2 (20% of S1, SEC Table 2)** | 114 | 109 | 0.0179462 | 5.53 pp | **15.50 pp** | **20.30 pp** | 112% |

Realised vs printed (S1 after re-parse: 3.37 pp / 4.4 pp clustered; S2: 7.53 / 9.9):
both roughly double. **The realised S1 MDE (9.1 pp) is now 3× the §6 headline bound
(3 pp)**, and S2's MDE (20.3 pp) exceeds the loosest 20 pp rung — on realised counts the
S2 leg is arithmetically vacuous. S1 still rules out the loose rung (20 pp ≫ 9.1 pp),
so the leg is not vacuous, but the §8.6 "read this next to §6" tension is now the
dominant feature of the DiD leg.

### 8.3 SPEC §5 usable-N note (stake at filing)

Trigger-and-stake parsed: 3,619 (1,864 pre / 1,755 post). The §5 MDE used N ≈ 4,950 and
a BBJJ-scale winsorised sd of 8 pp. Realised: N = 1,465 (CRSP-matched), √ = 19.129, and
the **realised winsorised sd of STK is 23.86 pp** (raw sd 23.86; p1 = 0.38, p99 = 100 —
the all-filer universe carries 50–100% insider/SPV stakes, unlike BBJJ's activist-HF
sample; median 12.14%, mean 22.72%). So SE(γ̂) = 23.86/19.129 = 1.25 pp, **MDE(γ) = 3.50
pp, ×1.3 filer clustering = 4.54 pp** (estimation-sample variant: 4.01 / 5.21 pp) —
against the printed 0.65/0.85 pp. The §5 hazard conclusion is unchanged in kind (4.54 pp
is still ~38× the 0.12 pp days–stake-gradient prediction), but the stake regression is
no longer the best-powered estimate in the package — JUMP's MDE (1.76 pp) is smaller.
Cleaning counts per §5: STK ≤ 0: 28 rows; 0–5% tail: 269 of 4,278 parsed (6.3%); > 100:
0 (parser guard).

## 9. Every SPEC number these realised counts supersede

1. **§2.1 filed-date table** → §4 above (all four rows; levels roughly halve).
2. **§2.1 trigger-date table** → §4 above (3,586/1,052 → 1,945/1,765; 3,000/897 → 1,615/1,626).
3. **§2.1 unique-CIK counts** → confirmed unchanged (2,735 subjects, 312 both, 3,503 filers).
4. **§2.1 trigger-year row** → 835/879/819/**1,024**; stale 273 → **153**; straddle 183 → **111**.
5. **§2.2 prediction** → §1: realised 755/710, N = 1,465, w = 0.485 (predicted 3,000/1,950, 4,950, 0.394 — written on the double-counted base; like-for-like the re-parse grows the post leg 3.6×).
6. **§3.6 table + honest-reading range** → §8.1: JUMP 1.76 pp, RUNUP 2.20 pp (CRSP-matched); honest range 1.1–2.3 pp → **1.9–4.2 pp** (2.2–4.8 pp estimation sample).
7. **§4 repeat-filer counts** → §6: 189 of 1,710 filers covering 577 of 2,098 filings (dose window). The "costs almost nothing" sentence does not survive.
8. **§5 usable-N note and MDE(γ)** → §8.3: 0.65/0.85 pp → **3.50/4.54 pp** on realised N and realised winsorised sd.
9. **§8.1 sample sizes** → S1 = 569/543 (estimation) or 755/710 (CRSP-matched); S2 = 114/109.
10. **§8.6 table** → §8.2: S1 6.94/9.09 pp, S2 15.50/20.30 pp.
11. **§12 power-summary row** → all MDE figures therein superseded per 6, 8, 10.
12. **§13 item 2** → closed by this run. **§13 item 8** → confirmed (§6). **§13 item 3** → still open: the rebuilt link covers 36% of subject CIKs (§7).

## 10. Anomalies and design-change candidates (reported, NOT implemented)

1. **Double-listing** (§0) — the old file's counts were ~2× the unique-filing truth. Any
   other output built from the old `fact2_parsed.jsonl` without accession dedup inherits
   this (Fact-1 sampled filings, not counts, so its distribution statistics are
   unaffected in expectation but its per-window n's double-count any duplicated draws).
2. **The "132 renamed filings silently dropped" did not apply to the fact2 universe.**
   The old file already carries both spellings (2,382 `SCHEDULE 13D` rows; 2024Q3/Q4
   unique counts identical old vs new: 521 = 521). The rename bug bit the `facts.py`
   explicit-`("SC 13D",)` sampling path. The re-parse's real gains are the trigger-date
   (2025: 0% → 100%) and percent-of-class (67.1% → 92.2%) fixes.
3. **Pre-XML parse residual** — ~20–30% of 2022–2024 cover pages still do not yield a
   trigger date (§3). If the estimation sample needs them, a targeted second-pass parser
   is a new ticket, not a silent edit.
4. **CRSP-match attrition is the binding sample constraint** (56% of in-band filings
   drop at step 3 under the provisional link): 415 no-CUSIP (recoverable when the
   rebuilt link matures), 462 CUSIP absent from the snapshot, 773 present-but-ineligible
   (incl. 74 REIT-like SB — the only judgement bucket), 241 insufficient observations.
5. **Rebuilt link vs carry-forward disagreement: 29%** where both exist (§7) — mostly
   CUSIP changes over time; needs a ruling on which source (or union) is canonical
   before the DiD control universe (§11 row 23) is built.
6. **Harness reported the download "aborted" at ~900/4,614**; the process in fact ran to
   completion (4,639 files, 0 failures, empty `_failures.json` written at completion,
   10:44). Cache verified: zero empty files; the three sub-2 KB files are legitimate
   one-document filings. Provenance note only.
7. **2 negative-gap filings** (TD one day after FD — cover-page date noise) drop at the
   90-day band as registered.

## 11. Reproduction

```bash
# parser gate first: 11/11 must pass
.venv/bin/python -m empirics.test_parse_13d
# full pipeline (fetch is the slow stage; cached and resumable)
.venv/bin/python -m empirics.reparse_fact2 --stage fetch      # ~75 min at ~1.4 req/s
.venv/bin/python -m empirics.reparse_fact2 --stage finalize   # archive + write jsonl
.venv/bin/python -m empirics.reparse_fact2 --stage analyze    # funnel + counts + MDEs
# regenerate against the rebuilt CIK->CUSIP link when it matures:
.venv/bin/python -m empirics.reparse_fact2 --stage analyze --link-file empirics/output/cik_cusip_link.csv
```

The SEC fair-access lock (`/tmp/sec_edgar_bulk.lock`) was held for the entire download
phase and released after; the throttle never exceeded the existing ~4 req/s fetcher
(realised ~1.4 req/s including latency). Nothing was committed; `empirics/data/` is the
gitignored symlink, so the canonical JSONL, the archive, and the 4,639 cached texts live
outside git by design.
