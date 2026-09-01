# Independent verification — E1 clean-environment reproduction

**Verifier:** fresh session, clean clone at `/tmp/e1_repro_20260901`; did not write any of the
code under test.
**Date:** 2026-09-01 · **Branch:** `v4` · **Commit under test:** `1f23867` ("Document how the
G3 audit ran"; `git log --oneline -1` confirmed, `git status` clean at clone time).
**Route:** cached-source reproduction. The from-network alternative (re-fetch from EDGAR) was
not taken: the registered spec fixes the local cache as the input of record and a network
re-fetch would test the cache, not the estimate.
**Environment:** fresh `python3 -m venv` in the clone; Python 3.12.13 (same interpreter version
as the live `.venv`); pinned from the live environment's `pip freeze`:
numpy 2.5.2, pandas 3.0.5, matplotlib 3.11.1 (numpy/pandas are the top-level imports in
`empirics/*.py`; matplotlib is required at run time by `_plot_cdf` via `pyfig.style`).
**Inputs copied** (from the live `empirics/data` symlink target, read-only):
`form_2023_QTR2.idx`, `form_2023_QTR3.idx`, `form_2024_QTR3.idx`, `form_2024_QTR4.idx`, and
`filings/` (6,397 files, 836M, incl. `_failures.json`). In the clone `empirics/data` is a real
directory (the symlink is gitignored, not tracked), so no write-through to the live cache was
possible.

## Commands

```bash
git clone /Users/austinli/Projects/blockholder_v4 /tmp/e1_repro_20260901
cd /tmp/e1_repro_20260901
mkdir -p empirics/data && cp <four .idx files> empirics/data/
cp -R /Users/austinli/Projects/blockholder/empirics/data/filings empirics/data/filings
python3 -m venv .venv && .venv/bin/pip install numpy==2.5.2 pandas==3.0.5 matplotlib==3.11.1
PYTHONPATH=. .venv/bin/python -m empirics.e1 run
cmp empirics/output/e1_delays.csv \
    /Users/austinli/Projects/blockholder_v4/empirics/output/e1_delays.csv
.venv/bin/python /tmp/diff_e1_json.py   # recursive JSON diff, G3_parser_validation masked
PYTHONPATH=. .venv/bin/python empirics/test_e1.py
PYTHONPATH=. .venv/bin/python empirics/test_parse_13d.py
```

## Results

- **`e1_delays.csv`: BIT-IDENTICAL** (`cmp` clean; 1,138 lines = header + 1,137 data rows).
- **`e1_estimate.json`: masked diff clean.** Recursive field-by-field diff with
  `gates.G3_parser_validation` masked reports zero differences. G3 state is exactly the
  expected one: committed `"PASS"` (audit scored) vs clean-rerun `"NOT RUN"` with note
  "run audit-sample, hand-code, commit, then audit-report" — the audit was not re-scored in
  this verification, per the ticket. All other fields match the committed authority exactly:
  enumerated 616 pre / 521 post; campaigns 450/432; eligible 461/435; resolved 450/432;
  unresolved 11/3; share ≤5 business days 0.3889 → 0.6713; difference +0.2824
  (0.2824074074074074); bootstrap CI [0.21795, 0.34753], n_boot 2000, seed 20260901;
  worst-case bound [0.26320, 0.29395]; medians 6 → 5 (pre median bound [6, 7]); G2 gap
  0.016965 (threshold 0.1); G1 PASS, G2 PASS; `headline_suppressed` false;
  `causal_claim` false; `label` "descriptive"; `spec` path unchanged.
- **Tests:** `test_e1.py` — 13/13 checks passed (exit 0). `test_parse_13d.py` — 11/11 checks
  passed (exit 0).
- **No-disappearing-rows check** on the regenerated CSV: 1,137 data rows; `status` ∈
  {resolved 1,123, unresolved 14}; every row carries a non-null `status` and `reason`
  (resolved→`ok` 1,123; unresolved→`no_trigger_date` 14); window × status: pre 605/11,
  post 518/3 (sums to the enumerated 616/521 in the JSON).

## Verdict

**REPRODUCED.** The clean-clone rerun from the cached inputs is bit-identical for
`e1_delays.csv` and field-identical for `e1_estimate.json` outside the G3 block, whose
`NOT RUN` state is the expected consequence of not re-scoring the hand-coding audit. Both
test suites pass and every enumerated row carries a status and reason.

Clone left in place for inspection at `/tmp/e1_repro_20260901` (its `git status` shows only
the two regenerated outputs as modified: `e1_estimate.json` via the G3 block and the binary
`e1_cdf.pdf`, which was not part of the diff contract).
