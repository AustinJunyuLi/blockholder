# CIK→CUSIP→PERMNO link rebuild + never-13D control universe — realised

**Date:** 2026-08-30 · **Executes:** SPEC §11 row 11 (link) and row 23 (control
universe); closes §13 item 3 (BLOCKING for the DiD leg) · **Code:**
`empirics/link_cik_cusip.py`, `empirics/build_control_universe.py` (both
committed) · **Route:** free route only (EDGAR + CRSP-on-disk), no WRDS.

---

## 0. Provenance (multi-agent session; read before citing)

This ticket ran during the 2026-08-30 environment migration. Sequence, from
git history and process inspection:

1. ~09:25 local — first implementation of both scripts written in this
   working tree (uncommitted), fetch phase started (~2,950 submissions
   documents cached).
2. 10:01 — commit `362f038` ("E2 execution tooling") harvested the
   uncommitted Mac-side work products, including both scripts.
3. 11:16–11:40 — the E4 lane rewrote `empirics/link_cik_cusip.py` after its
   first run scored the validation gate at **0.7301** (660/904). Diagnosis:
   identity-vintage mismatch, not linkage error — the cover-page CUSIP is the
   issuer's identity *on the filing date*, while CRSP `HdrCUSIP`/ticker on
   the last row is *current-only*. Committed as `906128b`; gate then PASSED.
4. The control-universe script was updated in this tree to the same
   history-based identity (ticker spans for the join, CUSIP history for the
   CUSIP routes) and accession-deduplication of the EDGAR idx rows (the
   re-parse report §0 found EDGAR lists every 13D twice — under the filer's
   and the subject's directory).

Everything below reports the **committed** code's outputs.

## 1. Method (row 11)

- **Subjects:** `fact2_parsed.jsonl` read at run time (sha256
  `cc0e3f9d4c264ca4…`, the re-parsed deduplicated file): **2,735 unique
  subject CIKs**, 2022Q1–2025Q4. 31 CIKs carry ≥1 filing whose EDGAR header
  names the same entity as SUBJECT COMPANY and FILED BY (header degeneracy —
  parsed faithfully, flagged, never patched).
- **EDGAR side:** company-submissions API `CIK{10d}.json` per subject CIK
  (throttled 4 req/s via `empirics.edgar_fetch.fetch`, cached under
  `empirics/data/submissions/`, all bulk pulls under the host lock
  `/tmp/sec_edgar_bulk.lock`). The JSON carries `tickers`/`exchanges`/`sic`/
  `name` but **no CUSIP** — the join key to CRSP is the ticker.
  `company_tickers.json` (10,391 rows) provides the reverse direction and the
  name fallback.
- **CRSP side:** one pass over the 1.2 GB snapshot builds last-observed
  identity **plus full history**: 18,654 (PERMNO, ticker) spans and 16,692
  (PERMNO, CUSIP) spans. The common-US filter (`EQTY`/`NS`/`USIncFlg=Y`) is
  evaluated over the PERMNO's **observed life** ("ever" flags): CRSP blanks
  ShareType/SecurityType on delisting, so a last-row test drops every
  security that left before the pull date — precisely the acquired firms a
  takeover study must keep (SPEC §2.3 filter 3). Pool: **5,443** PERMNOs
  (vs 3,827 under a last-row test; 1,607 delisted-before-pull retained).
- **Join:** normalised ticker (uppercase, non-alphanumerics stripped)
  against the PERMNO's whole ticker history; candidate must have been listed
  at the CIK's first in-window 13D; ties broken on the ticker's own date
  span; collisions surviving both filters are reported in
  `ambiguous_permnos`, never silently picked. No-ticker CIKs try a
  normalised-name fallback via `company_tickers.json` titles.

## 2. Link results (committed outputs)

`empirics/output/cik_cusip_link.csv` — 2,735 rows:

| match_route | n |
|---|---|
| ticker_unique | 1,006 |
| ticker_span | 5 |
| name_fallback | 7 |
| name_fallback_span | 1 |
| ambiguous_ticker | 12 |
| unmatched | 850 |
| unmatched_name | 854 |

**Matched: 1,019/2,735 = 37.3%.** The unmatched mass is dominated by
delisted/renamed targets whose current EDGAR record carries no usable ticker
— of the 1,505 CIKs that carry a reusable cover-page CUSIP but no ticker
match, **437** have that CUSIP's 8-prefix present among the header-less
(delisted) PERMNOs in the snapshot: they are in the file, just unreachable by
ticker. (They are still excluded from the control pool — route E3 below.)

**Validation vs the reusable cover-page CUSIPs** (2,446 CIKs carry one; the
old values are never a join key, only an independent check):

| rule | agreement | n |
|---|---|---|
| **GATE: cover CUSIP ∈ PERMNO's observed CUSIP history** | **0.9522** | 941 |
| date-consistent (CUSIP carried on the filing date) | 0.9160 | 941 |
| header-only (last-row HdrCUSIP) | 0.7216 | 941 |
| any cover CUSIP across the CIK's filings | 0.9702 | 941 |

Gate ≥ 0.95 → **PASS**. The header-only gap (0.7216) is CRSP identity drift,
not linkage error — this was the E4 repair. The 45 residual disagreements
(`cik_cusip_link_disagreements.csv`) carry mechanical reasons:
cusip_absent_from_crsp_window 15, same_issuer_different_issue 14,
cusip_owned_by_other_permno 12, non_equity_cusip_line 2,
leading_zero_shift_parse_artifact 1, subject_filer_header_collapse 1.

**Reverse map** (`permno_cik_map.csv`, what the BID12 coder needs):
**5,212/5,443 = 95.8%** of common-US PERMNOs mapped to a CIK — routes:
ticker 3,605, ticker_delisted 1,607, no_edgar_ticker 228, ambiguous_ticker 3.
A delisted PERMNO is mapped only when no still-listed security claims the
ticker (reassignment guard). Spot-check vs the submissions API: **300/300 =
100%**. Caveat printed by the build: the 228 unmapped are all delisted —
they cannot be BID12-extracted and would drop from the control pool,
suppressing control-side bid rates; visible, not silent.

## 3. Control universe (row 23) — realised

`empirics/output/never13d_control_universe.csv` — **3,600 PERMNOs**
(2,480 still listed, 1,120 delisted before the pull date), with PERMCO,
HdrCUSIP, CUSIP, ticker, exchange, listed span, and the ever-flags attached.
Funnel and per-component detail: `never13d_control_summary.csv`,
`never13d_exclusion_detail.csv`.

| step | n |
|---|---|
| CRSP snapshot PERMNOs | 14,092 |
| candidate pool (ever EQTY/NS/US, observed life) | 5,443 |
| **excluded (union E1–E6)** | **1,843** |
| **never-13D universe** | **3,600** |

Exclusion funnel (marginal adds, conservative union — a PERMNO leaves the
pool if ANY route ties it to an in-window 13D subject):

| component | PERMNOs | +new |
|---|---|---|
| E1 link, matched 2022–2025 subjects | 1,014 | 1,014 |
| E2 link, ambiguous collisions (all candidates) | 36 | 27 |
| E3 reusable cover CUSIPs vs CUSIP history | 1,322 | 417 |
| E4 2021 gap (below) | 552 | 340 |
| E5 amendment sample (below) | 102 | 27 |
| E6 reverse map ∩ subject CIKs | 1,246 | 18 |

**The 2021 gap mattered.** The on-disk idx files start 2022Q1 but the SPEC
window starts 2021-01-01. Downloaded the four 2021 quarterly form.idx via
the existing `download_form_index`: 3,101 idx rows → **1,557 unique initial
13Ds** (accession-deduped — EDGAR's double-listing confirmed in the 2021
files too; 1,557 is in line with the SEC's ~1,430/year 2011–2021 benchmark
cited in the re-parse report). Texts fetched (cached under
`empirics/data/filings/`); subject CIK parsed for **1,557/1,557**; cover
CUSIP for 804 (51.6%). 1,041 unique subject CIKs; ticker-link matched 383
(36.8% — statistically indistinguishable from the 2022–2025 rate, a good
consistency check). E4 excludes 552 pool PERMNOs, **340 of which no other
route catches** — skipping the 2021 leg would have left ~9% of the universe
contaminated.

**Amendment contamination (the material caveat).** 21,987 unique in-window
`SC 13D/A` filings (2021–2025, accession-deduped). Per the ticket, no bulk
fetch; a seeded random 200-filing sample (seed 20260830) was fetched and
parsed: 188 subjects parsed (94%). **53/188 = 28.2% name a subject with no
in-window original** (original filed pre-2021). Of those 53 orphan subjects,
**28 (52.8%) link to candidate-pool PERMNOs** (23 ticker, 15 cover-CUSIP,
union 28) — and were excluded (E5). Extrapolating the sample rate to the
~21,787 unsampled amendments gives an **upper-bound residual of ~3,200 pool
PERMNOs (~90% of the universe)**; the true figure is lower because orphan
subjects file multiple amendments (the sample shows ~0.94 unique subjects
per filing, but repeat amenders across years are invisible to a 200-draw).
**Recommendation for the matching ticket:** if control purity on this margin
matters, bulk-fetching all 21,987 amendment texts is ~90 minutes at the
4 req/s throttle on this cache pattern — cheap insurance, and the machinery
(`list_amendments` + `parse_filings` + the exclusion assembly) is already in
`build_control_universe.py`.

**vs the SPEC's "~11,000 candidates":** the SPEC's arithmetic was
14,092 − ~2,735 on the whole snapshot. Applying the documented common-stock
filter first (§8.2: US, share type common) leaves 5,443 candidates; the
universe is 3,600. Against the realised treated sample (re-parse funnel:
1,465 CRSP-matched / 1,112 estimation), 3:1 matching needs ~3,300–4,400
controls — **3,600 is adequate but tight** once exact SIC-2 × quarter cells
bind; the matching ticket should report cell-level shortfalls rather than
assume slack.

## 4. Caveats

- The CRSP snapshot's header is current-only: delisted PERMNOs keep
  HdrCUSIP/PERMCO but lose Ticker/ShareType/SecurityType. All identity work
  here is therefore history-based; anything last-row is reported only for
  comparison.
- The 37.3% CIK→PERMNO match rate is a *ticker-route* rate on a
  survivorship-truncated header, not a measure of target coverage: reusable
  cover-page CUSIPs reach further (route E3), and the DiD attrition funnel
  (re-parse report §2) is the authoritative treated-side count.
- The amendment-contamination residual (§3) is an estimate from a seeded
  200-filing sample, not a census; the unsampled remainder is the residual,
  and its upper bound is large enough to matter for control purity.
- `matched` CIK→PERMNO links are class-blind where a firm has two share
  classes (12 ambiguous collisions preserved, excluded from controls on both
  legs).
- 228 delisted pool PERMNOs carry no CIK in the reverse map (ticker
  reassignment guard); they cannot be BID12-extracted — visible in
  `permno_cik_map.csv` as `no_edgar_ticker`, not silently dropped.
