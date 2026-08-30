"""Fixture tests for the BID12 outcome coder (empirics/bid12.py).

Two layers:

1. Synthetic unit tests (no network): the 8-K text-confirmation decision
   table (rulebook §5) and the BID12 lookup window arithmetic (rulebook §3,
   §6).
2. Live fixtures: well-known 2022-2025 takeovers and negative controls,
   verified against the live EDGAR APIs through the throttled fetcher
   (small pulls — a dozen firms' submissions JSONs plus a handful of 8-K
   texts; results are cached under empirics/data/bid12_cache/ so re-runs
   are free). These are small pulls, not a bulk phase, so the
   /tmp/sec_edgar_bulk.lock is not required.

Run:
    .venv/bin/python -m empirics.test_bid12
"""

from __future__ import annotations

import datetime as dt
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from empirics import bid12

PASS, FAIL = "PASS", "FAIL"
_results = []


def check(label: str, cond: bool, detail: str = "") -> None:
    _results.append((label, bool(cond), detail))
    print(f"  [{PASS if cond else FAIL}] {label}"
          + (f" — {detail}" if detail and not cond else ""))


# ---------------------------------------------------------------------------
# 1. Synthetic text-confirmation fixtures (rulebook §5 decision table)
# ---------------------------------------------------------------------------

MERGER_TARGET = (
    "Item 1.01 Entry into a Material Definitive Agreement. On June 18, 2023, "
    "DICE Therapeutics, Inc. (the “Company”), Eli Lilly and Company and "
    "Romeo Acquisition, Inc. (“Merger Sub”) entered into an Agreement and "
    "Plan of Merger, pursuant to which Merger Sub will be merged with and "
    "into the Company, with the Company surviving the Merger as a "
    "wholly-owned subsidiary of Lilly.")

MERGER_TARGET_FIRST_TOKEN = (
    "On July 28, 2023, Reata Pharmaceuticals, Inc. (“Reata” or the "
    "“Company”), Biogen Inc. and River Acquisition, Inc. (“Merger Sub”) "
    "entered into an Agreement and Plan of Merger (the “Merger Agreement”), "
    "pursuant to which Merger Sub will be merged with and into Reata, with "
    "Reata surviving the Merger as a wholly-owned subsidiary of Biogen.")

MERGER_ACQUIRER = (
    "Item 2.01 Completion of Acquisition or Disposition of Assets. On July "
    "21, 2021 the Company completed the acquisition of Slack Technologies, "
    "Inc. (“Slack”), pursuant to that certain Agreement and Plan of Merger, "
    "dated as of December 1, 2020, by and among salesforce.com, inc. (the "
    "“Company”), Skyline Strategies I Inc., a Delaware corporation and "
    "wholly owned subsidiary of the Company (“Merger Sub I”), and Slack.")

LOAN_AGREEMENT = (
    "Item 1.01. Creation of a Direct Financial Obligation. On May 5, 2023, "
    "we, as the Borrower, entered into a loan agreement with BPCR Limited "
    "Partnership, pursuant to which the Lenders agreed to make term loans "
    "to the Borrower of up to $275 million.")

RIGHTS_PLAN = (
    "Item 1.01 Entry into a Material Definitive Agreement. On April 15, "
    "2022, the Board adopted a Rights Agreement. In the event any person "
    "commences a tender offer or exchange offer for shares of the Company, "
    "the rights become exercisable. The Rights Plan is intended to deter "
    "coercive tender offers.")

UNDERWRITING = (
    "Item 1.01 Entry into a Material Definitive Agreement. On June 29, "
    "2021, salesforce.com, inc. (the “Company”) entered into an "
    "underwriting agreement with Citigroup Global Markets Inc., pursuant "
    "to which the Company agreed to issue and sell $1,000,000,000 "
    "aggregate principal amount of 0.625% Senior Notes due 2024. The "
    "Company intends to use the proceeds to fund the acquisition of Slack "
    "under the previously announced Merger Agreement.")

HOLDCO_STRUCTURE = (
    "The Merger Agreement provides that (i) Merger Sub 1 will be merged "
    "with and into the Company (the “First Merger”), with the Company "
    "continuing as the surviving corporation in the First Merger. Verona "
    "Holdco, Inc., a Delaware corporation and a wholly owned subsidiary of "
    "the Company (“Holdco”), was formed solely for this purpose.")

BOTH_DIRECTIONS = (
    "The Company entered into an Agreement and Plan of Merger pursuant to "
    "which the Company will acquire Beta Corp, and separately Beta Corp "
    "disclosed that the Company will be acquired by Gamma LLC, with the "
    "Company surviving as a wholly-owned subsidiary of Gamma LLC.")


def test_text_rules() -> None:
    print("\n== 8-K text confirmation (synthetic) ==")
    v, _ = bid12.confirm_8k_text(MERGER_TARGET, "DICE Therapeutics")
    check("target merger (the-Company phrasing) confirmed", v == "confirmed", v)
    v, _ = bid12.confirm_8k_text(MERGER_TARGET_FIRST_TOKEN,
                                 "Reata Pharmaceuticals")
    check("target merger (first-token phrasing) confirmed", v == "confirmed", v)
    v, _ = bid12.confirm_8k_text(MERGER_ACQUIRER, "salesforce.com")
    check("firm-as-acquirer rejected", v == "rejected", v)
    v, _ = bid12.confirm_8k_text(LOAN_AGREEMENT, "Reata Pharmaceuticals")
    check("loan agreement rejected", v == "rejected", v)
    v, _ = bid12.confirm_8k_text(RIGHTS_PLAN, "Twitter")
    check("rights plan rejected (not a bid)", v == "rejected", v)
    v, _ = bid12.confirm_8k_text(UNDERWRITING, "salesforce.com")
    check("underwriting 8-K rejected despite merger mention", v == "rejected", v)
    v, _ = bid12.confirm_8k_text(HOLDCO_STRUCTURE, "VMware")
    check("holdco structure still confirms as target", v == "confirmed", v)
    v, _ = bid12.confirm_8k_text(BOTH_DIRECTIONS, "Acme Holdings")
    check("both directions -> ambiguous, never forced", v == "ambiguous", v)


# ---------------------------------------------------------------------------
# 2. Lookup window arithmetic (rulebook §3, §6)
# ---------------------------------------------------------------------------

def _ev(days_from_td: int, ambiguous: int = 0, form: str = "SC TO-T",
        acc: str = "") -> dict:
    d = dt.date(2023, 3, 15) + dt.timedelta(days=days_from_td)
    return {"event_date": str(d), "form": form, "accession": acc or str(days_from_td),
            "route": "A", "bidder_cik": None, "bidder_name": None,
            "ambiguous": ambiguous, "confirm_detail": "synthetic"}


def test_lookup() -> None:
    print("\n== lookup window arithmetic ==")
    td = dt.date(2023, 3, 15)
    r = bid12.lookup_bid12([_ev(0), _ev(365), _ev(366)], td)
    check("event at TD counts (inclusive)", r["bid12"] == 1)
    check("event at TD+365 counts (inclusive)", r["n_bid_events"] == 2,
          str(r["n_bid_events"]))
    check("event at TD+366 excluded", _ev(366)["event_date"] not in
          (r["first_bid_date"],), r["first_bid_date"])
    check("first bid is earliest", r["first_bid_date"] == str(td))

    r = bid12.lookup_bid12([_ev(366)], td)
    check("no in-window evidence -> 0", r["bid12"] == 0)
    r = bid12.lookup_bid12([_ev(30, ambiguous=1)], td)
    check("only ambiguous in-window -> empty, ambiguous=1",
          r["bid12"] is None and r["ambiguous"] == 1, str(r["bid12"]))
    r = bid12.lookup_bid12([_ev(30, ambiguous=1), _ev(60)], td)
    check("confirmed beats ambiguous -> 1", r["bid12"] == 1)

    r = bid12.lookup_bid12([_ev(-1)], td)
    check("bid day before TD -> excluded_prior_bid", r["excluded_prior_bid"] == 1)
    check("bid day before TD -> prior_bid_any", r["prior_bid_any"] == 1)
    r = bid12.lookup_bid12([_ev(-365)], td)
    check("bid at TD-365 -> excluded (lookback inclusive)",
          r["excluded_prior_bid"] == 1)
    r = bid12.lookup_bid12([_ev(-366)], td)
    check("bid at TD-366 -> not excluded, prior_bid_any still set",
          r["excluded_prior_bid"] == 0 and r["prior_bid_any"] == 1,
          f"{r['excluded_prior_bid']}/{r['prior_bid_any']}")
    r = bid12.lookup_bid12([_ev(-366), _ev(10)], td)
    check("stale prior bid + new in-window bid -> BID12=1, not excluded",
          r["bid12"] == 1 and r["excluded_prior_bid"] == 0)

    own = dict(_ev(30), bidder_cik="59478")
    r = bid12.lookup_bid12([own], td, filer_cik="0000059478")
    check("filer's own bid flagged by CIK", r["filer_own_bid"] == 1)
    r = bid12.lookup_bid12([own], td, filer_cik="0000099999")
    check("other bidder -> filer_own_bid 0", r["filer_own_bid"] == 0)


# ---------------------------------------------------------------------------
# 3. Live fixtures: well-known 2022-2025 takeovers + negative controls
# ---------------------------------------------------------------------------

# (cik, name, TD, expected first confirmed event date, expected forms among
#  confirmed events, notes)
LIVE_POSITIVE = [
    ("1418091", "TWITTER, INC.", "2022-03-15", "2022-04-26", {"8-K"},
     "Musk merger agreement signed 2022-04-25, 8-K filed 04-26"),
    ("718877", "Activision Blizzard, Inc.", "2021-12-01", "2022-01-19", {"8-K"},
     "Microsoft merger agreement signed 2022-01-18"),
    ("1124610", "VMware, Inc.", "2022-04-01", "2022-05-26", {"8-K"},
     "Broadcom merger agreement announced 2022-05-26"),
    ("1645569", "DICE Therapeutics, Inc.", "2023-05-15", "2023-06-20",
     {"8-K", "SC TO-C"},
     "Lilly tender: SC TO-C + merger-agreement 8-K on 2023-06-20, "
     "SC TO-T 2023-06-30"),
    ("1358762", "REATA PHARMACEUTICALS INC", "2023-06-01", "2023-07-31",
     {"8-K"}, "Biogen merger agreement 2023-07-28, 8-K filed 07-31; the "
     "2023-07-11 loan 8-K must NOT appear"),
    ("1771917", "Karuna Therapeutics, Inc.", "2023-11-01", "2023-12-22",
     {"8-K"}, "BMS deal announced 2023-12-22"),
]

LIVE_NEGATIVE = [
    ("1108524", "Salesforce, Inc.", "2023-01-29",
     "Elliott 13D Jan-2023; no bid for Salesforce 2022-2025 (its own Slack "
     "and Informatica 8-Ks are acquirer-side and must be rejected)"),
    ("1051470", "Crown Castle Inc.", "2023-06-01",
     "activist campaigns but no bid in window"),
]


def test_live() -> None:
    print("\n== live fixtures (EDGAR APIs, cached) ==")
    for cik, name, td_s, first_date, first_forms, note in LIVE_POSITIVE:
        rec = bid12.extract_firm_events(cik, name)
        confirmed = [e for e in rec["events"] if not e["ambiguous"]]
        td = dt.date.fromisoformat(td_s)
        r = bid12.lookup_bid12(rec["events"], td)
        ok_first = bool(confirmed) and confirmed[0]["event_date"] == first_date
        check(f"{name}: first confirmed event {first_date}", ok_first,
              f"got {confirmed[0]['event_date'] if confirmed else 'none'} ({note})")
        check(f"{name}: first event form in {sorted(first_forms)}",
              bool(confirmed) and confirmed[0]["form"] in first_forms,
              f"got {confirmed[0]['form'] if confirmed else 'none'}")
        check(f"{name}: BID12=1 from TD {td_s}", r["bid12"] == 1,
              f"got {r['bid12']}")
        check(f"{name}: no extraction errors", not rec["errors"],
              str(rec["errors"]))
    # Reata: the 2023-07-11 loan 8-K must not be an event
    rec = bid12.extract_firm_events("1358762", "REATA PHARMACEUTICALS INC")
    check("Reata: 2023-07-11 loan 8-K rejected",
          all(e["event_date"] != "2023-07-11" for e in rec["events"]))
    # DICE: filer's-own-bid flag via bidder CIK (Lilly = 59478)
    rec = bid12.extract_firm_events("1645569", "DICE Therapeutics, Inc.")
    r = bid12.lookup_bid12(rec["events"], dt.date(2023, 5, 15),
                           filer_cik="0000059478")
    check("DICE: filer_own_bid=1 when filer is Lilly", r["filer_own_bid"] == 1)
    r = bid12.lookup_bid12(rec["events"], dt.date(2023, 5, 15),
                           filer_cik="0000099999")
    check("DICE: filer_own_bid=0 for unrelated filer", r["filer_own_bid"] == 0)
    # Twitter: already-under-bid exclusion (TD after the 2022-04-26 8-K)
    rec = bid12.extract_firm_events("1418091", "TWITTER, INC.")
    r = bid12.lookup_bid12(rec["events"], dt.date(2022, 5, 10))
    check("Twitter: TD after announced bid -> excluded_prior_bid=1",
          r["excluded_prior_bid"] == 1)

    for cik, name, td_s, note in LIVE_NEGATIVE:
        rec = bid12.extract_firm_events(cik, name)
        confirmed = [e for e in rec["events"] if not e["ambiguous"]]
        r = bid12.lookup_bid12(rec["events"], dt.date.fromisoformat(td_s))
        check(f"{name}: no confirmed bid events", not confirmed,
              f"got {[(e['event_date'], e['form']) for e in confirmed]} ({note})")
        check(f"{name}: BID12=0 from TD {td_s}", r["bid12"] == 0,
              f"got {r['bid12']}")


def main() -> int:
    test_text_rules()
    test_lookup()
    test_live()
    n_fail = sum(1 for _, ok, _ in _results if not ok)
    print(f"\n{len(_results) - n_fail}/{len(_results)} checks passed"
          + (f", {n_fail} FAILED" if n_fail else ""))
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
