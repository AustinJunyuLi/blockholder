"""Hand recall check for the BID12 coder (rulebook §9 / status-note input).

Draws a reproducible random sample of treated firms and runs a *broader*
full-text search than the coder's route B, then compares against the coder's
cached events. The point is to quantify route-B recall: bid-like filings the
hand search finds but the coder did not are potential misses and are listed
for manual adjudication (the adjudication itself is recorded in
``research/empirics_v4/bid12_status_2026-08-30.md`` — this script only
produces the comparison table).

Two hand queries per firm, both CIK-verified exactly like route B:

- H1: ``q='"<core name>"'`` over ALL FIVE bid forms (SC TO-T, SC TO-C,
  SC 14D9, DEFM14A, PREM14A) — a superset of the coder's routes (route B
  covers only the two bidder-filed forms; route A covers target-filed forms
  via the submissions feed, not FTS).
- H2: ``q='"<core name>" "tender offer"'`` with NO forms filter — a
  vocabulary stress test that surfaces bid-like filings under any form label
  (e.g. form variants the registered list excludes, or mis-indexed forms).

Usage::

    .venv/bin/python -m empirics.bid12_recall_check [--n 20] [--seed 20260830]

Reads the coder's events from cache only (``cache_only=True``) — run this
AFTER the bulk extraction pass has processed the sampled firms. Writes
``empirics/output/bid12_recall_check.csv`` and
``empirics/output/bid12_recall_check_detail.json``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import urllib.parse
from typing import Optional

from .bid12 import (
    EXTRACT_END,
    EXTRACT_START,
    FTS_PAGE_SIZE,
    FTS_URL,
    ROUTE_B_FORMS,
    _cached_json,
    _display_name_ciks,
    clean_core_name,
    extract_firm_events,
    load_treated_universe,
    normalize_cik,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.normpath(os.path.join(HERE, "output"))

#: All five registered bid forms (route A + route B forms together).
ALL_BID_FORMS = ("SC TO-T", "SC TO-C", "SC 14D9", "DEFM14A", "PREM14A")

#: Forms surfaced by the vocabulary query (H2) that count as bid-like for
#: comparison purposes. Includes the /A amendments so the hand check can see
#: them, flagged separately — the registered rule counts originals only.
BID_LIKE_FORMS = set(ALL_BID_FORMS) | {f + "/A" for f in ALL_BID_FORMS} | {
    "8-K",
    "SC 13D",
    "SC 13D/A",
    "SC14D9C",
    "SC TO-I",
    "SC 14D-9",
    "SCHEDULE 14D-9",
    "425",
    "DEFA14A",
}


def _fts_query(query: str, forms: Optional[tuple], max_pages: int = 3) -> list:
    """Raw FTS hits for ``query`` (already plain text, will be quoted here).

    Returns a list of dicts with accession / form / file_date /
    display_names, de-duplicated by accession. NOT CIK-filtered — the caller
    does that, so discarded hits can be counted for diagnostics.
    """
    q = urllib.parse.quote(query)
    forms_q = ("&forms=" + urllib.parse.quote(",".join(forms))) if forms else ""
    seen: set = set()
    out: list = []
    for page in range(max_pages):
        url = (
            f"{FTS_URL}?q={q}&dateRange=custom&startdt={EXTRACT_START}"
            f"&enddt={EXTRACT_END}{forms_q}&from={page * FTS_PAGE_SIZE}"
        )
        data = _cached_json(
            url, "fts_pages", "recall_" + hashlib.md5(url.encode()).hexdigest() + ".json",
            max_bytes=4_000_000,
        )
        if data is None:
            break
        hits = data.get("hits", {})
        total = hits.get("total", {}).get("value", 0)
        page_hits = hits.get("hits", [])
        if not page_hits:
            break
        for h in page_hits:
            s = h.get("_source", {})
            acc = s.get("adsh")
            if not acc or acc in seen:
                continue
            seen.add(acc)
            out.append(
                {
                    "accession": acc,
                    "form": s.get("form"),
                    "event_date": s.get("file_date"),
                    "display_names": s.get("display_names") or [],
                    # keep the raw _source so bid12._display_name_ciks (which
                    # reads hit["_source"]["display_names"]) works unchanged
                    "_source": s,
                }
            )
        if (page + 1) * FTS_PAGE_SIZE >= total:
            break
    return out


def _cik_verified(hits: list, cik10: str) -> tuple:
    """Split hits into (verified, discarded-count) by target-CIK membership."""
    verified = [h for h in hits if str(int(cik10)) in _display_name_ciks(h)]
    return verified, len(hits) - len(verified)


def check_firm(cik: str, name: str) -> dict:
    """Run both hand queries for one firm and compare with coder events."""
    cik10 = normalize_cik(cik)
    core = clean_core_name(name)
    coder = extract_firm_events(cik10, name, cache_only=True)
    coder_events = coder.get("events", []) if coder.get("cached") else []
    coder_accs = {e["accession"] for e in coder_events}

    h1_raw = _fts_query(f'"{core}"', ALL_BID_FORMS)
    h1, h1_disc = _cik_verified(h1_raw, cik10)

    h2_raw = _fts_query(f'"{core}" "tender offer"', None)
    h2_all, h2_disc = _cik_verified(h2_raw, cik10)
    h2 = [h for h in h2_all if h["form"] in BID_LIKE_FORMS]

    hand = {h["accession"]: h for h in h1 + h2}
    misses = [h for acc, h in sorted(hand.items()) if acc not in coder_accs]
    coder_only = [a for a in sorted(coder_accs) if a not in hand]

    return {
        "cik": cik10,
        "name": name,
        "core_name": core,
        "coder_cached": bool(coder.get("cached")),
        "coder_n_events": len(coder_events),
        "coder_events": [
            {
                "accession": e["accession"],
                "form": e["form"],
                "event_date": e["event_date"],
                "route": e.get("route"),
                "ambiguous": e.get("ambiguous", 0),
            }
            for e in coder_events
        ],
        "h1_n": len(h1),
        "h1_discarded": h1_disc,
        "h2_n": len(h2),
        "h2_discarded": h2_disc,
        "hand_hits": sorted(hand.values(), key=lambda h: h["event_date"] or ""),
        "potential_misses": misses,
        "coder_only_accessions": coder_only,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="BID12 route-B hand recall check.")
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--seed", type=int, default=20260830)
    ap.add_argument("--ciks", default="", help="comma-separated CIKs to check "
                    "instead of sampling (for follow-up adjudication)")
    args = ap.parse_args(argv)

    uni = load_treated_universe()
    ciks: list = uni["ciks"]
    names: dict = uni["names"]
    if args.ciks:
        sample = [normalize_cik(c) for c in args.ciks.split(",") if c.strip()]
    else:
        rng = random.Random(args.seed)
        sample = rng.sample(ciks, min(args.n, len(ciks)))

    rows: list = []
    detail: list = []
    n_uncached = 0
    for i, cik in enumerate(sample, 1):
        name = names.get(cik, "")
        res = check_firm(cik, name)
        detail.append(res)
        if not res["coder_cached"]:
            n_uncached += 1
        rows.append(
            {
                "cik": cik,
                "name": name,
                "coder_cached": res["coder_cached"],
                "coder_n_events": res["coder_n_events"],
                "h1_hits": res["h1_n"],
                "h2_bidlike_hits": res["h2_n"],
                "potential_misses": len(res["potential_misses"]),
                "miss_forms": ";".join(
                    f"{h['form']}:{h['event_date']}" for h in res["potential_misses"]
                ),
            }
        )
        print(
            f"[{i}/{len(sample)}] {cik} {name[:40]!r} coder={res['coder_n_events']} "
            f"h1={res['h1_n']} h2={res['h2_n']} misses={len(res['potential_misses'])}"
            + ("" if res["coder_cached"] else " (CODER CACHE MISSING)"),
            flush=True,
        )

    os.makedirs(OUT_DIR, exist_ok=True)
    csv_path = os.path.join(OUT_DIR, "bid12_recall_check.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    json_path = os.path.join(OUT_DIR, "bid12_recall_check_detail.json")
    with open(json_path, "w") as fh:
        json.dump(
            {"seed": args.seed, "n": len(sample), "universe_meta": uni["meta"],
             "results": detail},
            fh, indent=1,
        )
    total_misses = sum(r["potential_misses"] for r in rows)
    print(
        f"\nDone: {len(sample)} firms, {total_misses} potential misses, "
        f"{n_uncached} firms without coder cache. Wrote {csv_path} and {json_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
