"""Checks for the E1 filing-delay runner.

Run:
    PYTHONPATH=. .venv/bin/python empirics/test_e1.py
"""

from __future__ import annotations

import datetime as dt
import os

import numpy as np
import pandas as pd

from empirics import e1

CHECKS = []


def check(fn):
    CHECKS.append(fn)
    return fn


@check
def check_acceptance_before_cutoff_stays_same_day():
    accepted = dt.datetime(2023, 5, 26, 16, 2, 45)      # Friday, before 17:30
    assert e1.effective_filing_date(accepted) == dt.date(2023, 5, 26)


@check
def check_acceptance_after_cutoff_rolls_forward():
    accepted = dt.datetime(2023, 5, 26, 18, 0, 0)       # Friday evening
    # Monday 29 May 2023 is Memorial Day, so the next session is Tuesday.
    assert e1.effective_filing_date(accepted) == dt.date(2023, 5, 30)


@check
def check_weekend_acceptance_rolls_to_monday():
    accepted = dt.datetime(2023, 7, 8, 9, 0, 0)         # Saturday morning
    assert e1.effective_filing_date(accepted) == dt.date(2023, 7, 10)


@check
def check_federal_holiday_is_not_a_business_day():
    assert not e1.is_business_day(dt.date(2023, 6, 19))   # Juneteenth
    assert e1.is_business_day(dt.date(2023, 6, 20))


@check
def check_business_delay_skips_holidays():
    # 2023-06-16 (Fri) to 2023-06-21 (Wed): Mon 19th is Juneteenth.
    assert e1.business_delay(dt.date(2023, 6, 16), dt.date(2023, 6, 21)) == 2


@check
def check_acceptance_datetime_parsed_from_header():
    text = "<ACCEPTANCE-DATETIME>20230725101815\nACCESSION NUMBER: x"
    assert e1.parse_acceptance(text) == dt.datetime(2023, 7, 25, 10, 18, 15)


@check
def check_missing_acceptance_returns_none():
    assert e1.parse_acceptance("no header here") is None


@check
def check_bounds_put_unresolved_at_both_extremes():
    delays = np.array([1.0, 2.0, 9.0, 10.0])   # 2 of 4 within five days
    b = e1.bounds_for_period(delays, n_unresolved=4)
    assert b["n_eligible"] == 8
    assert b["share_complete_case"] == 0.5
    assert b["share_lower"] == 0.25          # all unresolved are misses
    assert b["share_upper"] == 0.75          # all unresolved are hits


@check
def check_bounds_collapse_when_nothing_unresolved():
    delays = np.array([1.0, 2.0, 9.0, 10.0])
    b = e1.bounds_for_period(delays, n_unresolved=0)
    assert b["share_lower"] == b["share_upper"] == b["share_complete_case"]


@check
def check_enumeration_collapses_filer_rows_to_accessions():
    rows = e1.enumerate_population()
    accessions = [os.path.basename(r["edgar_path"])[:-4] for r in rows]
    assert len(accessions) == len(set(accessions)), "duplicate accession enumerated"
    counts = pd.Series([r["window"] for r in rows]).value_counts().to_dict()
    assert counts == {"pre": 616, "post": 521}, counts


@check
def check_every_record_carries_a_status_and_reason():
    rows = e1.enumerate_population()[:40]
    for r in rows:
        rec = e1.build_record(r)
        assert rec["status"] in {"resolved", "ineligible", "unresolved"}, rec["status"]
        assert rec["reason"], "every record needs a reason code"
        if rec["status"] == "resolved":
            assert rec["delay_bdays"] is not None


@check
def check_no_outcome_screen_in_the_runner():
    source = open(os.path.join(os.path.dirname(e1.__file__), "e1.py")).read()
    for banned in ("<= 60", "<=60", "delay_bdays >= 0"):
        assert banned not in source, f"outcome screen {banned!r} present"


@check
def check_campaign_collapse_keeps_earliest_acceptance():
    df = pd.DataFrame([
        {"status": "resolved", "subject_cik": "1", "trigger_date": "2023-01-02",
         "accepted": "2023-01-05T10:00:00", "accession": "b", "delay_bdays": 3.0},
        {"status": "resolved", "subject_cik": "1", "trigger_date": "2023-01-02",
         "accepted": "2023-01-03T10:00:00", "accession": "a", "delay_bdays": 1.0},
    ])
    kept = e1.collapse_campaigns(df)
    assert len(kept) == 1
    assert kept.iloc[0]["accession"] == "a"


def main() -> int:
    failed = 0
    for fn in CHECKS:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL {fn.__name__}: {exc}")
    print(f"\n{len(CHECKS) - failed}/{len(CHECKS)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
