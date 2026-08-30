"""Fixture tests for the CRSP↔EDGAR link (empirics/link_cik_cusip.py).

Synthetic only — no network, no CRSP load, no shared output files.

The reason this file exists: on 2026-08-30 a missing CRSP ticker reached
``norm_ticker`` as a float NaN, normalised to the string ``"NAN"``, and matched
the real NYSE ticker NAN — the Nuveen New York Quality Municipal Income Fund.
Every delisted no-ticker PERMNO was therefore mapped to that one fund's CIK,
1,607 of them, through the ``ticker_delisted`` route. The bug was silent: the
map reported a *higher* link rate because of it, and the survivorship warning
the build already printed said the delisted PERMNOs were fine.

Run:
    .venv/bin/python -m empirics.test_link_cik_cusip
"""

from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from empirics.link_cik_cusip import build_reverse_map, norm_ticker

PASS, FAIL = "PASS", "FAIL"
_results = []


def check(label: str, cond: bool, detail: str = "") -> None:
    _results.append((label, bool(cond), detail))
    print(f"  [{PASS if cond else FAIL}] {label}"
          + (f" — {detail}" if detail and not cond else ""))


def test_norm_ticker() -> None:
    print("\n== norm_ticker on missing values ==")
    check("float NaN -> empty string (the 2026-08-30 bug)",
          norm_ticker(float("nan")) == "", repr(norm_ticker(float("nan"))))
    check("numpy NaN -> empty string", norm_ticker(np.nan) == "")
    check("pandas NA -> empty string", norm_ticker(pd.NA) == "")
    check("None -> empty string", norm_ticker(None) == "")
    check("empty string -> empty string", norm_ticker("") == "")
    check("a real ticker still normalises", norm_ticker("brk.b") == "BRKB",
          norm_ticker("brk.b"))
    check("the literal ticker 'NAN' is still a ticker — the guard keys on the "
          "missing value, not on the letters",
          norm_ticker("nan") == "NAN", norm_ticker("nan"))


def _permnos(rows: list) -> pd.DataFrame:
    """(permno, ticker, still_listed) triples -> the columns the map needs."""
    return pd.DataFrame([{
        "permno": p, "permco": 1, "hdrcusip": "00000010", "cusip": "00000010",
        "ticker": t, "primary_exch": "N", "first_date": "2021-01-04",
        "last_date": "2025-12-31", "still_listed": listed,
    } for p, t, listed in rows])


def _tickers(pairs: list) -> pd.DataFrame:
    return pd.DataFrame([{"cik": c, "norm_ticker": t} for t, c in pairs])


def test_reverse_map_missing_ticker() -> None:
    print("\n== reverse map: a missing ticker maps to nothing ==")
    # NAN is a real ticker in the EDGAR table, exactly as in production
    tickers = _tickers([("NAN", "1074769"), ("AAPL", "320193"),
                        ("XRAY", "818479")])
    permnos = _permnos([
        (10001, np.nan, False),      # delisted, ticker blanked by CRSP
        (10002, np.nan, True),       # listed but no ticker
        (10003, "AAPL", True),       # ordinary live match
        (10004, "XRAY", False),      # delisted, ticker survives, not reused
        (10005, "NAN", True),        # the genuine Nuveen ticker
    ])
    m = build_reverse_map(permnos, tickers).set_index("permno")

    check("delisted with no ticker -> unlinked, route no_edgar_ticker",
          m.loc[10001, "cik"] == "" and m.loc[10001, "map_route"] == "no_edgar_ticker",
          f"{m.loc[10001, 'cik']!r}/{m.loc[10001, 'map_route']}")
    check("listed with no ticker -> unlinked too",
          m.loc[10002, "cik"] == "", f"{m.loc[10002, 'cik']!r}")
    check("no PERMNO is handed the Nuveen CIK by accident",
          set(m.loc[[10001, 10002], "cik"]) == {""},
          str(list(m.loc[[10001, 10002], 'cik'])))
    check("ordinary live ticker still links", m.loc[10003, "cik"] == "320193")
    check("delisted with a surviving unique ticker links via ticker_delisted",
          m.loc[10004, "cik"] == "818479"
          and m.loc[10004, "map_route"] == "ticker_delisted",
          f"{m.loc[10004, 'cik']}/{m.loc[10004, 'map_route']}")
    check("the firm that genuinely trades as NAN keeps its CIK",
          m.loc[10005, "cik"] == "1074769")


def test_reverse_map_reuse_guard() -> None:
    print("\n== reverse map: the delisted-ticker-reuse guard still holds ==")
    tickers = _tickers([("ZZZ", "999999")])
    permnos = _permnos([(20001, "ZZZ", False), (20002, "ZZZ", True)])
    m = build_reverse_map(permnos, tickers).set_index("permno")
    check("a delisted PERMNO whose ticker a live security now uses is not "
          "mapped", m.loc[20001, "map_route"] == "delisted_ticker_reused",
          m.loc[20001, "map_route"])
    check("the live claimant of that ticker is mapped",
          m.loc[20002, "cik"] == "999999")


def test_reverse_map_ambiguity() -> None:
    print("\n== reverse map: ambiguous tickers stay unmapped ==")
    tickers = _tickers([("DUP", "111"), ("DUP", "222")])
    m = build_reverse_map(_permnos([(30001, "DUP", True)]),
                          tickers).set_index("permno")
    check("two CIKs on one ticker -> ambiguous_ticker, no CIK",
          m.loc[30001, "cik"] == ""
          and m.loc[30001, "map_route"] == "ambiguous_ticker",
          f"{m.loc[30001, 'cik']!r}/{m.loc[30001, 'map_route']}")
    check("both candidate CIKs are recorded for the record",
          set(m.loc[30001, "ambiguous_ciks"].split(";")) == {"111", "222"},
          m.loc[30001, "ambiguous_ciks"])


def test_no_mass_collision() -> None:
    print("\n== reverse map: no CIK absorbs a crowd of PERMNOs ==")
    tickers = _tickers([("NAN", "1074769")] +
                       [(f"T{i:03d}", str(400000 + i)) for i in range(50)])
    rows = [(40000 + i, np.nan, False) for i in range(200)]
    rows += [(50000 + i, f"T{i:03d}", True) for i in range(50)]
    m = build_reverse_map(_permnos(rows), tickers)
    linked = m[m["cik"] != ""]
    worst = linked["cik"].value_counts().max() if len(linked) else 0
    check("200 delisted no-ticker PERMNOs link to nothing",
          len(linked) == 50, f"{len(linked)} linked")
    check("no CIK is shared by more than one PERMNO here", worst == 1,
          f"worst collision {worst}")


def main() -> int:
    test_norm_ticker()
    test_reverse_map_missing_ticker()
    test_reverse_map_reuse_guard()
    test_reverse_map_ambiguity()
    test_no_mass_collision()
    n_fail = sum(1 for _, ok, _ in _results if not ok)
    print(f"\n{len(_results) - n_fail}/{len(_results)} checks passed"
          + (f", {n_fail} FAILED" if n_fail else ""))
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
