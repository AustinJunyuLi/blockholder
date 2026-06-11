# empirics/ — the de-risk data leg (nine-month milestone, Workstream C)

Stdlib-only EDGAR access; no new Python dependencies. Raw downloads live in
`empirics/data/` (gitignored, regenerable); small derived summaries are
committed under `empirics/output/`.

## Fact 1 — 13D disclosure-delay compression

The SEC cut the Schedule 13D initial-filing deadline from 10 calendar days to
**5 business days**, compliance date **2024-02-05** (release 33-11253);
structured machine-readable XML became mandatory for filings from
**2024-12-18**.

```bash
# download quarterly indexes + sample/parse/summarize (throttled ~4 req/s)
.venv/bin/python -m empirics.facts --per-window 150
```

Outputs: `output/fact1_filings.csv` (per-filing), `output/fact1_summary.csv`
(per-window stats incl. share within 5 business days), `output/fact1_delay.pdf`.

Modules: `edgar_fetch.py` (quarterly `form.idx` enumeration + throttled
fetcher with declared User-Agent), `parse_13d.py` (event date via structured
XML tag or cover-page label regex; filed date; CIKs; percent-of-class).

## Fact 2 — 13D announcement event study (WRDS)

Design note: `quality_reports/plans/2026-06-10_fact2-event-study-design.md`.
UCL WRDS access confirmed 2026-06-11 (CRSP *annual* daily file + Event Study
by WRDS); executed via the WRDS web tools under the author's login.

```bash
# 1. enumerate + parse ALL SC 13D originals 2022Q1-2025Q4 (~9.2k filings,
#    throttled; resume-safe via data/fact2_parsed.jsonl)
.venv/bin/python -m empirics.fact2_events
#    -> output/fact2_filings.csv + data/fact2_events_upload.txt

# 2. WRDS "U.S. Daily Event Study: Upload your own events":
#    identifier=CUSIP, dates=DD-MMM-YYYY, Market Model,
#    estimation=220, min obs=100, gap=20, window [-10,+10];
#    select all event-time + event-date variables; csv output.
#    Save main output as data/wrds_evtstudy.csv (schema:
#    Model,cusip,uid,evtdate,date,evttime,ret,abret; uid="<permno>-<date>").

# 3. CRSP annual Daily Stock File, 2021-01-01..2025-12-31, by PERMNO list
#    (upload .txt, one per line; permnos from step 2's matched uids):
#    vars permno,dlycaldt,dlyret,dlyvol,dlyprc,dlycap,cusip,sharetype,
#    securitytype,securitysubtype,usincflg,issuertype,primaryexch,ticker.
#    Save as data/crsp_daily.csv[.gz].

# 4. CARs, Amihud, run-up, size + regressions (two-way clustered SEs)
.venv/bin/python -m empirics.fact2_analysis
#    -> output/fact2_summary.csv, fact2_regressions.csv, fact2_car.pdf
```

Notes: EDGAR renamed the form type to `SCHEDULE 13D` from Dec 2024
(`edgar_fetch.list_filings` is boundary-aware, not fixed-width, for this
reason); filings accepted after 16:00 ET shift to the next business day;
the new-era structured cover pages defeat the *event-date* regex (delay
stats for 2025 are sparse) but CUSIP parsing is unaffected (~80-90%).

### Fact 2 results (full run, 2026-06-11)

Universe: 9,234 original 13Ds parsed (86% CUSIP coverage) -> 3,518 unique
(CUSIP8, trade-date) events -> 2,280 matched by WRDS (misses are mostly
foreign G/M/U-prefix CINS) -> **1,513 events** after US-common-stock and
|CAR|<1 filters (843 pre / 670 post; WRDS query 11385426; the CRSP covariate
panel is the full 2021-2025 universe, chunk-filtered locally by PERMNO).

- Mean CAR[-1,+1] **doubles** post-acceleration: 0.85% -> 1.71%
  (beta_Post = +0.9pp level spec, t=1.12; +1.7pp with controls, t=0.87 --
  right sign, not significant under firm x month two-way clustering).
- CAR[-10,+1]: 4.6% -> 12.6% (t=1.55 level spec).
- Strong liquidity cross-section: dCAR/dln(Amihud) = **-1.4pp (t=-3.7)**
  in every spec and both windows -- filing surprises concentrate in liquid
  names, the model's camouflage margin.
- Post x ln(Amihud) interaction: precise null (+0.17pp, t=0.48) -- the
  differential-compression prediction (delta<0) is not supported.

## Caveats (v0)

- Fact 1 samples ~150 originals per window (seeded), not the universe; the
  full-universe run is a flag change (`--per-window 100000`).
- Cover-page date parsing is regex-based; the summary reports the parse rate
  per window. Amendments (`SC 13D/A`) are excluded by exact-form matching.
- EDGAR fair access: ~4 requests/second with a declared contact User-Agent.
