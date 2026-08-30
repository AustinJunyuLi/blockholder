"""Fixture tests for the control-side BID12 lookup.

Synthetic only — no network, no SEC lock, and no touching of the shared
`empirics/data/bid12_cache/` or `empirics/output/`: every test builds its own
temporary event cache and output directory. Safe to run while the extraction
lanes are live.

What is checked:

  * pseudo-TD inheritance — the control is coded on its treated firm's TD,
    with the identical [TD, TD+365] inclusive window (rulebook §3)
  * window edges: TD, TD+365 in; TD+366 and TD−1 out
  * prior-bid flags on the control side (rulebook §6)
  * ambiguity is never forced (rulebook §7): ambiguous-only ⇒ empty BID12
  * unextracted control CIK ⇒ empty BID12 with `not-extracted`, never 0
    (rulebook §5.1 item 5)
  * `filer_own_bid` is 0 by construction for controls
  * a control matched to two treated firms at the same TD is looked up once
    and joined to both pair rows; distinct TDs are distinct lookups
  * unlinked PERMNOs (no CIK) are surfaced as `no-cik-link`, not dropped
  * the run metadata carries the rulebook SHA-256

Run:
    .venv/bin/python -m empirics.test_bid12_control_lookup
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from empirics import bid12, bid12_control_lookup as bcl

PASS, FAIL = "PASS", "FAIL"
_results = []


def check(label: str, cond: bool, detail: str = "") -> None:
    _results.append((label, bool(cond), detail))
    print(f"  [{PASS if cond else FAIL}] {label}"
          + (f" — {detail}" if detail and not cond else ""))


def _event(date: str, form: str = "SC TO-T", ambiguous: bool = False,
           accession: str = "0000000000-00-000000") -> dict:
    return {"event_date": date, "form": form, "accession": accession,
            "route": "A", "bidder_cik": "0000000099",
            "bidder_name": "BIDDER CO", "ambiguous": ambiguous,
            "confirm_detail": "synthetic"}


def _write_cache(cache_dir: str, cik: str, events: list) -> None:
    d = os.path.join(cache_dir, "events")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"{cik}.json"), "w") as fh:
        json.dump({"cik": cik, "name": f"CONTROL {cik}", "events": events,
                   "errors": []}, fh)


def _write_pairs(path: str, rows: list) -> None:
    with open(path, "w") as fh:
        fh.write("treated_permno,treated_accession,treated_td,control_permno,"
                 "match_group,dist\n")
        for tp, acc, td, cp in rows:
            fh.write(f"{tp},{acc},{td},{cp},{acc},0.1\n")


def _write_map(path: str, mapping: dict) -> None:
    with open(path, "w") as fh:
        fh.write("permno,cik\n")
        for permno, cik in mapping.items():
            fh.write(f"{permno},{cik if cik is not None else ''}\n")


def run_case(tmp: str, pairs_rows: list, mapping: dict, caches: dict):
    """Build a self-contained fixture and run the lookup; returns (df, meta)."""
    import pandas as pd

    cache_dir = os.path.join(tmp, "cache")
    out_dir = os.path.join(tmp, "out")
    os.makedirs(out_dir, exist_ok=True)
    for cik, events in caches.items():
        _write_cache(cache_dir, cik, events)
    pairs = os.path.join(tmp, "pairs.csv")
    mpath = os.path.join(tmp, "map.csv")
    _write_pairs(pairs, pairs_rows)
    _write_map(mpath, mapping)

    saved = bid12.CACHE_DIR
    bid12.CACHE_DIR = cache_dir
    try:
        meta = bcl.lookup_control(pairs, out_dir, mpath)
    finally:
        bid12.CACHE_DIR = saved
    df = pd.read_csv(os.path.join(out_dir, "bid12_control.csv"),
                     dtype={"cik": str})
    return df, meta, out_dir


def test_window_and_inheritance() -> None:
    print("\n== control lookup: pseudo-TD inheritance and window edges ==")
    with tempfile.TemporaryDirectory() as tmp:
        td = "2023-06-15"
        caches = {
            # in-window: exactly on TD
            "0000000001": [_event("2023-06-15", accession="A-1")],
            # in-window: TD + 365 (inclusive upper edge)
            "0000000002": [_event("2024-06-14", accession="A-2")],
            # out: TD + 366
            "0000000003": [_event("2024-06-15", accession="A-3")],
            # out (and prior-bid): TD - 1, inside the 365-day lookback
            "0000000004": [_event("2023-06-14", accession="A-4")],
            # prior bid, older than the lookback -> prior_bid_any only
            "0000000005": [_event("2021-03-01", accession="A-5")],
            # ambiguous only, in window -> BID12 empty, never forced
            "0000000006": [_event("2023-08-01", ambiguous=True,
                                  accession="A-6")],
            # no events at all -> searched zero
            "0000000007": [],
        }
        mapping = {100 + i: f"{i:010d}" for i in range(1, 8)}
        pairs = [(9001, "0001234567-23-000001", td, 100 + i)
                 for i in range(1, 8)]
        df, meta, _ = run_case(tmp, pairs, mapping, caches)
        by = {r.permno: r for r in df.itertuples()}

        check("event on TD -> BID12=1", by[101].bid12 == 1,
              f"got {by[101].bid12}")
        check("event on TD+365 -> BID12=1 (inclusive)", by[102].bid12 == 1,
              f"got {by[102].bid12}")
        check("event on TD+366 -> BID12=0", by[103].bid12 == 0,
              f"got {by[103].bid12}")
        check("event on TD-1 -> BID12=0 and excluded_prior_bid=1",
              by[104].bid12 == 0 and by[104].excluded_prior_bid == 1,
              f"got {by[104].bid12}/{by[104].excluded_prior_bid}")
        check("prior bid beyond lookback -> prior_bid_any=1, "
              "excluded_prior_bid=0",
              by[105].prior_bid_any == 1 and by[105].excluded_prior_bid == 0,
              f"got {by[105].prior_bid_any}/{by[105].excluded_prior_bid}")
        check("ambiguous-only in window -> BID12 empty, ambiguous=1",
              (by[106].bid12 != by[106].bid12) and by[106].ambiguous == 1,
              f"got {by[106].bid12}/{by[106].ambiguous}")
        check("no events, extraction ran -> BID12=0",
              by[107].bid12 == 0 and by[107].extraction_status == "ok",
              f"got {by[107].bid12}/{by[107].extraction_status}")
        check("pseudo-TD is the treated TD on every row",
              set(df["td"]) == {td}, f"got {sorted(set(df['td']))}")
        check("filer_own_bid is 0 by construction for controls",
              int(df["filer_own_bid"].sum()) == 0,
              f"got {int(df['filer_own_bid'].sum())}")
        check("run metadata carries the rulebook sha256",
              meta["rules_sha256"] == _rulebook_hash(),
              f"got {meta['rules_sha256'][:12]}")


def test_unresolved_and_unlinked() -> None:
    print("\n== control lookup: unresolved rows are not zeros ==")
    with tempfile.TemporaryDirectory() as tmp:
        caches = {"0000000001": [_event("2023-07-01", accession="B-1")]}
        # permno 202 maps to a CIK with no event cache -> not-extracted
        # permno 203 has no CIK at all -> no-cik-link
        mapping = {201: "0000000001", 202: "0000000002", 203: None}
        pairs = [(9001, "0001234567-23-000001", "2023-06-15", p)
                 for p in (201, 202, 203)]
        df, meta, _ = run_case(tmp, pairs, mapping, caches)
        by = {r.permno: r for r in df.itertuples()}
        check("uncached control CIK -> BID12 empty, not-extracted",
              (by[202].bid12 != by[202].bid12)
              and by[202].extraction_status == "not-extracted",
              f"got {by[202].bid12}/{by[202].extraction_status}")
        check("unlinked PERMNO surfaced as no-cik-link, not dropped",
              203 in by and by[203].extraction_status == "no-cik-link"
              and (by[203].bid12 != by[203].bid12),
              f"rows: {sorted(by)}")
        check("metadata counts the unlinked pairs",
              meta["n_pairs_without_cik_link"] == 1,
              f"got {meta['n_pairs_without_cik_link']}")
        check("metadata counts the not-extracted rows",
              meta["control_lookup"]["bid12_not_extracted"] == 1,
              f"got {meta['control_lookup']['bid12_not_extracted']}")


def test_shared_control_across_treated() -> None:
    print("\n== control lookup: one control, several treated firms ==")
    with tempfile.TemporaryDirectory() as tmp:
        caches = {"0000000001": [_event("2023-07-01", accession="C-1")]}
        mapping = {301: "0000000001"}
        # same control PERMNO matched to two treated firms: same TD (one
        # lookup, two rows) and a third at a different TD (its own lookup)
        pairs = [(9001, "0001234567-23-000001", "2023-06-15", 301),
                 (9002, "0001234567-23-000002", "2023-06-15", 301),
                 (9003, "0001234567-22-000003", "2022-01-10", 301)]
        df, meta, _ = run_case(tmp, pairs, mapping, caches)
        check("every pair row is emitted", len(df) == 3, f"got {len(df)}")
        check("distinct (CIK, pseudo-TD) lookups counted once per TD",
              meta["n_distinct_lookups"] == 2,
              f"got {meta['n_distinct_lookups']}")
        same_td = df[df["td"] == "2023-06-15"]
        check("shared-TD rows agree on BID12",
              set(same_td["bid12"]) == {1}, f"got {set(same_td['bid12'])}")
        other = df[df["td"] == "2022-01-10"].iloc[0]
        check("a different pseudo-TD gets its own window verdict",
              other["bid12"] == 0, f"got {other['bid12']}")
        check("match_group distinguishes the treated firms",
              df["match_group"].nunique() == 3,
              f"got {df['match_group'].nunique()}")


def test_matches_treated_code_path() -> None:
    print("\n== control lookup: identical arithmetic to the treated side ==")
    import datetime as dt
    with tempfile.TemporaryDirectory() as tmp:
        events = [_event("2023-06-15", accession="D-1"),
                  _event("2024-06-14", accession="D-2"),
                  _event("2022-12-01", accession="D-3")]
        caches = {"0000000001": events}
        mapping = {401: "0000000001"}
        pairs = [(9001, "0001234567-23-000001", "2023-06-15", 401)]
        df, _, _ = run_case(tmp, pairs, mapping, caches)
        direct = bid12.lookup_bid12(events, dt.date(2023, 6, 15),
                                    None, None, "0000000001")
        row = df.iloc[0]
        same = all(row[k] == direct[k] for k in
                   ("bid12", "n_bid_events", "excluded_prior_bid",
                    "prior_bid_any", "first_bid_date", "first_bid_form"))
        check("control row reproduces lookup_bid12 exactly", same,
              f"row={dict(row[['bid12', 'n_bid_events']])} direct={direct}")


def _rulebook_hash() -> str:
    with open(bid12.RULEBOOK_PATH, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main() -> int:
    test_window_and_inheritance()
    test_unresolved_and_unlinked()
    test_shared_control_across_treated()
    test_matches_treated_code_path()
    n_fail = sum(1 for _, ok, _ in _results if not ok)
    print(f"\n{len(_results) - n_fail}/{len(_results)} checks passed"
          + (f", {n_fail} FAILED" if n_fail else ""))
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
