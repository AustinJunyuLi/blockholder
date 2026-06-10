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

## Fact 2 — event study (WRDS-gated)

Design note: `quality_reports/plans/2026-06-10_fact2-event-study-design.md`.
Execution requires CRSP daily returns (author: confirm UCL WRDS access);
Bloomberg fallback per the terminal checklist in `lit/bloomberg_checklist.md`.

## Caveats (v0)

- Fact 1 samples ~150 originals per window (seeded), not the universe; the
  full-universe run is a flag change (`--per-window 100000`).
- Cover-page date parsing is regex-based; the summary reports the parse rate
  per window. Amendments (`SC 13D/A`) are excluded by exact-form matching.
- EDGAR fair access: ~4 requests/second with a declared contact User-Agent.
