# Data inventory — empirics lane (ticket 10, E2 input)

Compiled 2026-08-20 from `/Users/austinli/Projects/blockholder_v4` (branch `v4`).
Facts only, gathered by direct inspection (`head`, `wc -l`, `awk` min/max scans,
`python3 -c` for a date-format check). No design opinions.

`empirics/data` is a symlink to `/Users/austinli/Projects/blockholder/empirics/data`
(the pre-v4 checkout) — gitignored, not present in this repo's git history.

---

## 1. `empirics/data/` (gitignored, on-disk raw/derived assets)

| File | Size | Format | Columns / fields | Rows | Date coverage | Notes / gaps |
|---|---|---|---|---|---|---|
| `crsp_daily.csv` | 1.21 GB | CSV, header row | `PERMNO,HdrCUSIP,CUSIP,PrimaryExch,USIncFlg,IssuerType,SecurityType,SecuritySubType,ShareType,Ticker,PERMCO,DlyCalDt,DlyPrc,DlyCap,DlyRet,DlyVol` | 11,884,715 data rows | `DlyCalDt` 2021-01-04 → 2025-12-31 | 14,092 unique PERMNOs. No gap found in the date-range scan itself; row-level daily coverage per PERMNO not checked (would require a per-security calendar diff). |
| `wrds_evtstudy.csv` | 4.25 MB | CSV, header row | `Model,cusip,uid,evtdate,date,evttime,ret,abret` | 49,116 data rows | `evtdate` 2022-01-04 → 2025-12-15; `date` (daily obs within event windows) 2021-12-20 → 2025-12-30 | 47,883/49,116 rows have a non-empty `evtdate` (the rest look like header/placeholder rows per the sample: first two data rows have empty `evtdate`/`date`/`ret`/`abret`). This is the WRDS Event Study tool's per-day panel output (one row per event × relative day). |
| `wrds_evtstudy_edate.csv` | 179 KB | CSV, header row | `Model,cusip,evtdate,cret,car,bhar,nrets,nrets_est` | 2,285 data rows | `evtdate` 2022-01-04 → 2025-12-15 | Per-event summary (CAR/BHAR over a fixed window; `nrets`/`nrets_est` = 21-day event / 220-day estimation window per column values). 1,749 distinct CUSIPs. This is the per-event collapse of `wrds_evtstudy.csv`. |
| `fact2_events_upload.txt` | 74 KB | Plain text, 2 whitespace-separated fields, no header | `<CUSIP8> <DD-MON-YYYY>` (e.g. `00739D10 04-JAN-2022`) | 3,518 lines | 2022-01-04 → 2026-01-01 (parsed with `datetime.strptime(%d-%b-%Y)`) | 2,625 distinct CUSIPs. This is the upload list fed to the WRDS Event Study web tool; 3,518 requested events → 2,285 matched in `wrds_evtstudy_edate.csv` (~65% match rate). Max date 2026-01-01 is beyond the 13D universe below (2025-12-31), i.e. one row past the parsed-filing window. |
| `fact2_parsed.jsonl` | 4.87 MB | JSON Lines | keys per record: `form, company, cik, date_filed, edgar_path, quarter, accession, filed, subject_cik, filer_cik, event, pct_of_class, has_xml, cusip, subject_name, filer_name, accepted, accepted_after_4pm` | 9,234 lines | `date_filed` 2022-01-03 → 2025-12-31 | Full-universe parsed SC 13D originals, 2022Q1–2025Q4. `has_xml` is `false` for all sampled rows (README/feasibility doc flags this as a known parser gap for the post-2024-12-18 structured-XML era — see §4/§5 quotes below). |
| `form_2022_QTR1.idx` … `form_2025_QTR4.idx` (16 files) | 36–58 MB each (~770 MB total) | EDGAR quarterly master index, fixed-width header + delimited body | Header: `Form Type / Company Name / CIK / Date Filed / File Name`; body rows are the master index of every EDGAR filing that quarter (all form types, not just 13D/13G) | e.g. `form_2022_QTR1.idx`: 356,530 data rows; `form_2025_QTR4.idx`: 275,897 data rows (row counts vary per quarter, not individually totalled here) | Per-file `Date Filed` range matches its named quarter exactly (spot-checked QTR1 2022: 2022-01-03 → 2022-03-31; QTR4 2025: 2025-10-01 → 2025-12-31) | Covers all 4 quarters of 2022, 2023, 2024, 2025 — no missing quarters in the 2022Q1–2025Q4 span. These are raw EDGAR master indexes (all form types); `fact2_parsed.jsonl` above is the SC 13D/13G-filtered extraction from these 16 files. |

## 2. `empirics/output/` (committed, small derived summaries)

| File | Size | Format | Columns | Rows | Date coverage | Notes |
|---|---|---|---|---|---|---|
| `fact1_filings.csv` | 62 KB | CSV, header row | `form,company,cik,date_filed,edgar_path,window,accession,filed,subject_cik,filer_cik,event,pct_of_class,has_xml,delay_bdays,delay_cdays` | 300 data rows | Two sampled windows: pre = 2023Q2–Q3 (10-calendar-day-rule era), post = 2024Q3–Q4 (5-business-day-rule era); exact per-row `date_filed` not separately scanned beyond the window labels | Per-filing detail behind `fact1_summary.csv`; 150 sampled per window (seeded random draw per `facts.py`). |
| `fact1_summary.csv` | 301 B | CSV, header row | `window,count,mean,median,p90,share_within_5bd,share_within_10bd,parse_rate` | 2 data rows (one per window) | n/a (summary stats, not dated) | pre-window: n=98, mean 9.63 bdays, median 7.0, p90 23.0, share≤5bd 35.7%, share≤10bd 80.6%, parse_rate 0.68. post-window: n=90, mean 6.4, median 5.0, p90 11.1, share≤5bd 75.6%, share≤10bd 88.9%, parse_rate 0.64. |
| `fact1_delay.pdf` | 13.9 KB | PDF figure | — | — | — | Histogram of `delay_bdays` by window (Fact 1 figure). |

## 3. Other data-bearing files in the repo

A repo-wide grep for `*.csv`, `*.parquet`, `*.jsonl`, `*.tsv` (excluding `numerical_output/`,
`empirics/data/`, `empirics/output/`, `.venv/`, `node_modules/`, `.git/`) found **no
other data files** in the repository.

The model layer (excluded from the table above but part of the same paper's
pipeline): `pyfig/figures.py` documents 13 named figure functions (`fig01_cutoff_structure`
… `fig15_wedge_primitives`, 15 slots but 13 currently wired per `ALL_FIGURES`) reading
from CSVs the CLAUDE.md build contract says land in `numerical_output/data/` (16 CSVs
as of 2026-06, per project docs). As of this inventory, `numerical_output/data/` does
**not exist on disk** — only 14 previously-rendered PDF figures and 2 `.tex` tables sit
in `numerical_output/`. The 16 model CSVs are not currently generated; they are produced
on demand by `make data` (`.venv/bin/python -m numerical.export_data --output-dir
numerical_output`), not fetched/scraped like the empirics-lane data above.

## 4. Pipeline stages: what can be produced on demand

From `empirics/README.md`, `empirics/edgar_fetch.py`, `empirics/facts.py`, `empirics/parse_13d.py`:

- **`empirics/edgar_fetch.py`** — `download_form_index(year, quarter)` fetches (and
  caches locally) one quarterly EDGAR `form.idx` master index from
  `https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{q}/form.idx`, throttled to
  ~4 req/s with a declared `User-Agent` (`"blockholder-research
  austin.junyu.li@gmail.com"`). `list_filings(idx_path, form_types=...)` parses an
  already-downloaded index into SC 13D/13G (+ EDGAR's post-2024Q3 "SCHEDULE 13D/13G"
  rename aliases) rows: form, company, cik, date_filed, edgar_path. `fetch_filing_text(edgar_path)`
  fetches one filing's master `.txt` submission (truncated to 400 KB by default). Callable
  directly (`python -m empirics.edgar_fetch --quarters 2023Q2 2023Q3 2024Q3 2024Q4`) to
  re-fetch/refresh any quarter's index on demand.
- **`empirics/parse_13d.py`** — given fetched filing text, extracts accession number,
  filed-as-of date, subject/filer CIKs (regex on header blocks), event date (either the
  structured `<dateOfEvent>` XML tag for post-Dec-2024 filings, or a cover-page label
  regex for any era), and a best-effort `pct_of_class`.
- **`empirics/facts.py`** (Fact 1) — orchestrates: sample SC 13D originals from a named
  quarter-window pair, fetch + parse each, compute business-day delay (event → filed)
  against a US-federal-holiday calendar, and write `fact1_filings.csv` /
  `fact1_summary.csv` / `fact1_delay.pdf`. Runnable as `.venv/bin/python -m
  empirics.facts --per-window 150` (flag controls sample size per window; README notes
  the full-universe run is `--per-window 100000`).
- **WRDS/CRSP pulls (`wrds_evtstudy*.csv`, `crsp_daily.csv`)**: no code for these is
  committed in this repo. Column layout and filenames indicate they were produced by (a)
  a direct WRDS CRSP daily-stock-file query (`crsp_daily.csv`: PERMNO/CUSIP/PERMCO/price/
  cap/return/volume schema is CRSP's standard daily stock file), and (b) the WRDS Event
  Study web tool, fed by `fact2_events_upload.txt` (a CUSIP+date list), producing
  `wrds_evtstudy.csv` (per-day panel) and `wrds_evtstudy_edate.csv` (per-event CAR/BHAR
  summary). These cannot be regenerated by any script in this repo — the empirical
  feasibility doc (quoted below) states the CIK→CUSIP link script and event-study harness
  that built these were never committed.

## 5. Quotes from `research/empirical_feasibility.md`

On what's obtainable free vs. gated (§"Legend", Test i table, and elsewhere):

> "Legend: **[FREE]** = EDGAR / open data / in-repo; **[GATED]** = WRDS-CRSP-Compustat/SDC/Activist Insight/Bloomberg — WRDS demonstrably worked from this machine on 2026-06-11 (the CRSP pull), but HANDOFF.md still lists "confirm UCL WRDS access" as an open author to-do, so treat standing access as **UNCONFIRMED**."

On the CRSP/WRDS snapshot already in hand:

> "`crsp_daily.csv` — **1.2 GB CRSP daily, 2021-01-04 → 2025-12-31, 11.88M rows, 14,092 unique PERMNOs**, columns incl. price, cap, return, volume, share-type flags. Sufficient for market-model CARs, Amihud illiquidity, size controls — no Compustat needed for a first pass."

> "`wrds_evtstudy_edate.csv` — WRDS Event-Study-tool output: market-model CARs (21-day window, 220 estimation days) for **2,285 events** (from 3,518 uploaded CUSIP-date pairs → 65% match), 2022-01-04 → 2025-12-15."

On critical gaps in the uncommitted Fact-2 assets:

> "**Critical gaps:** (i) no code for any of this is committed (no CIK→CUSIP link script, no event-study harness) — reproducibility must be rebuilt; (ii) **the parser fails silently on the entire structured-data era**: event-parse rate is 66–68% for 2022–2024 but **0% for 2025**, and `has_xml=True` for zero of 9,234 rows, including post-2024-12-18 filings where the XML tag should exist."

On post-rule sample size as currently usable:

> "Post-rule (filed ≥ 2024-02-05) rows in `fact2_parsed.jsonl`: 4,176; with parsed event date: **1,235**; with event date *and* CUSIP: **1,048** — all concentrated in Feb–Dec 2024 because of the 2025 parse failure. Pre-rule: 5,058 / 2,849 with event+CUSIP. So the DiD's post leg is currently ~10.5 months, not the nominal ~2 years; fixing the 2025 parser roughly doubles the usable post window."

On the binding constraint for takeover-premium measurement:

> "The standard premium (offer price ÷ unaffected price − 1, 1-day or 4-week reference) is an **SDC/Bloomberg field — gated**, and it is the one variable with no complete free substitute."

> "**Verdict:** premia are measurable for a few-hundred-deal subsample at days-to-weeks cost without SDC; the binding constraint is labor (outcome matching + offer-price extraction), not access."

On cross-country data (Test ii):

> "**Notices [FREE] but heterogeneous:** UK RNS + Takeover Panel table; BaFin, AMF, Consob, CNMV, AFM, FINMA registers; SEDAR+ (CA); ASIC (AU); EDINET (JP) ... Each register is a bespoke scrape/parse job; none has an EDGAR-grade bulk API."

> "**Premia [GATED]:** SDC/Bloomberg premia-over-unaffected for non-US deals have no free substitute at scale."

> "**Recommendation:** in the minimal package, demote (ii) to a calibration/motivation exhibit ... rather than a regression leg; upgrade only if a RA or coauthor owns it."

On book-to-market/sector/governance controls:

> "Book-to-market, sector | Compustat / CRSP | [GATED]; minimal version: log-cap + 2-digit SIC from CRSP header or EDGAR"

> "B/M, sector, governance controls | Compustat [GATED — only if WRDS confirmed] | 1 d if access"

On access fragility:

> "WRDS worked on 2026-06-11 but standing UCL access is unconfirmed (HANDOFF.md open to-do). Mitigation already in place: the full study window's CRSP data is on disk (gitignored — back it up off-repo; it does not survive a machine change). All EDGAR-side assets regenerate in ~1 h."

On reproducibility debt (uncommitted Fact-2 code):

> "**Reproducibility debt.** The Fact-2 execution code (CIK→CUSIP link, evtstudy upload builder, regression) is not committed; rebuild and commit it when the empirical section is written, or the package cannot be defended."

---

## Capabilities: what can be produced on demand

- Re-fetch/refresh any EDGAR quarterly `form.idx` (2022Q1–2025Q4 already cached; any
  other quarter is one throttled fetch away) via `empirics.edgar_fetch`.
- Re-run the SC 13D/13G filtering + parsing (`list_filings` + `parse_filing`) over any
  cached or freshly-fetched index, at any sample size (`--per-window`), producing fresh
  `fact1_filings.csv` / `fact1_summary.csv` / `fact1_delay.pdf`.
- Extend Fact 1 from the current 300-filing sample to the full 2022–2025 universe (flag
  change per README: `--per-window 100000`), pending the known 2025 XML-parser fix noted
  in §5 above.
- Compute Amihud illiquidity, size (log market cap), and other CRSP-derived controls
  directly from the on-disk `crsp_daily.csv` snapshot — no additional fetch needed.
- Ken French daily factor library (market-model robustness) — free, not yet pulled into
  this repo.
- EDGAR full-text search / submissions API queries for post-13D outcome events (SC TO-T,
  SC 14D-9, DEFM14A, 8-K Item 1.01/2.01) to build a deal-outcome / offer-price premium
  subsample — free, stdlib-fetchable with the existing throttled fetcher, but not yet
  built (estimated 1–3 weeks per the feasibility doc).
- Hand-collection of offer prices from SC TO-T / 8-K / DEFM14A filings for a premium
  subsample, cross-referenced against the on-disk CRSP snapshot for a pre-rumor
  "unaffected" price.

**Cannot be regenerated from this repo's code as-is:** the WRDS CRSP daily pull
(`crsp_daily.csv`) and the WRDS Event Study tool outputs (`wrds_evtstudy.csv`,
`wrds_evtstudy_edate.csv`) — no committed script performs the CIK→CUSIP linking or the
WRDS query/upload steps; those assets exist only as the raw files already on disk from a
2026-06-11 run.

## Known constraints

(See quoted passages in §5 above for full text; summary pointers only.)

- WRDS/CRSP/Compustat/SDC/Activist Insight/Bloomberg access is gated and, per the
  feasibility doc, **unconfirmed as standing access** — it "worked" once (2026-06-11)
  but is not guaranteed to work again.
- Takeover-premium data (offer price ÷ unaffected price) has no free bulk substitute;
  SDC/Bloomberg is gated.
- Cross-country disclosure-threshold notices are free but require bespoke per-jurisdiction
  scraping (no EDGAR-grade bulk API exists for UK/EU/CA/AU/JP registers).
- Compustat-sourced book-to-market/sector/governance controls are gated; CRSP-only
  fallbacks (log market cap, 2-digit SIC) are free.
- The 2025 XML-parsing failure in `empirics/parse_13d.py` (0% event-date yield for 2025
  filings, `has_xml=False` for all 9,234 parsed rows) currently truncates the usable
  post-rule DiD window to ~10.5 months instead of the nominal ~2 years.
- The code that produced `crsp_daily.csv`, `wrds_evtstudy.csv`, and
  `wrds_evtstudy_edate.csv` is not committed to this repository.
