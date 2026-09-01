# empirics/

Stdlib-only EDGAR access, no new dependencies. Raw downloads live in `empirics/data/`
(gitignored, regenerable); derived summaries are committed under `empirics/output/`.

## E1 — filing delay around the Feb-2024 acceleration

Did the realised delay between the trigger event and the Schedule 13D filing fall after the SEC
cut the initial deadline from 10 calendar days to 5 business days, effective 2024-02-05
(release 33-11253)?

The registered specification is `research/empirics_v4/e1_spec.md`. Read it before changing
anything here. `empirics/output/e1_estimate.json` is the single result authority.

```bash
PYTHONPATH=. .venv/bin/python -m empirics.e1 run           # enumerate, parse, estimate, gate
PYTHONPATH=. .venv/bin/python -m empirics.e1 audit-sample  # 60 blind cases for G3
PYTHONPATH=. .venv/bin/python -m empirics.e1 audit-report  # score them after hand-coding
PYTHONPATH=. .venv/bin/python empirics/test_e1.py
```

The population is 1,137 unique accessions, 616 pre and 521 post. All sources are cached locally,
so `run` needs no network. `form.idx` is filer-indexed, so one joint filing appears once per
reporting person under the same accession; enumeration collapses on accession first.

Outputs: `output/e1_delays.csv` (one row per accession, every row carrying a status and reason),
`output/e1_estimate.json`, `output/e1_cdf.pdf`.

## Modules

- `edgar_fetch.py` — quarterly `form.idx` enumeration and a throttled fetcher with a declared
  User-Agent. Both EDGAR spellings, `SC 13D` and `SCHEDULE 13D`, resolve to the same form.
- `parse_13d.py` — trigger date from the structured XML tag or the cover-page label, filed date,
  CIKs, percent of class. Cover pages write dates with HTML entities inside them, so the parser
  decodes entities before matching.
- `e1.py` — the E1 runner.
- `facts.py` — the superseded v0 Fact 1 sampler, kept so its numbers stay reproducible. Its
  0-to-60-day screen is legacy and the E1 spec forbids that kind of exclusion; do not copy it.
