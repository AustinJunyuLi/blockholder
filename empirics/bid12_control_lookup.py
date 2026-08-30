"""Control-side BID12 lookup (SPEC §8.2/§8.3) — part of the DiD unit.

The coder (`empirics/bid12.py`) extracts a bid-event table per firm over
2021-01-01 → 2026-12-31. The treated lookup runs off the 13D universe's own
trigger dates; the control side has no trigger date of its own — each matched
control **inherits its treated firm's TD as a pseudo-trigger date** (SPEC §8.2),
so the control rows only exist once matching has run. That is why this lookup
lives outside the coder: it consumes `did_match_pairs.csv`, not a universe file.

Given the match pairs it expands to one row per (control CIK, pseudo-TD),
applies the *identical* `bid12.lookup_bid12` window arithmetic used on the
treated side (rulebook §3, §6, §7 — same code, not a re-implementation), and
writes:

  * ``empirics/output/bid12_control.csv``        — one row per matched pair
  * ``empirics/output/bid12_events_control.csv`` — the event table for the
    control CIKs that appear in the pairs
  * ``empirics/output/bid12_control_run_meta.json`` — counts + the rulebook
    SHA-256, so the blind audit can verify the rule version on this side too

Two conventions, written down because they are not derivable from the treated
code path:

1. **`filer_own_bid` is 0 by construction for controls.** Rulebook §7 defines
   it against the *13D filer*; a never-13D control has no filer, so the flag
   carries no information here and is emitted as 0 (not as evidence of
   absence). The treated-side separate reporting of filer's-own bids is
   unaffected.
2. **Unextracted control CIKs are unresolved, not zeros** (rulebook §5.1
   item 5). A control whose event extraction has not run leaves BID12 empty
   with ``extraction_status = not-extracted``; the DiD funnel counts them.

Cache-only: no network, no SEC lock (identical to `lookup-treated`).

Usage:
    .venv/bin/python -m empirics.bid12_control_lookup
    .venv/bin/python -m empirics.bid12_control_lookup --pairs PATH --out-dir DIR
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from typing import Optional

from empirics import bid12

OUT_DIR = bid12.OUT_DIR
PAIRS_PATH = os.path.join(OUT_DIR, "did_match_pairs.csv")
CONTROL_MAP_PATH = bid12.CONTROL_MAP_PATH


def load_permno_cik_map(path: str = CONTROL_MAP_PATH) -> dict:
    """PERMNO → 10-digit CIK for the rows that carry a CIK.

    Rows whose link route left the CIK blank are simply absent; the caller
    counts them as unlinked rather than guessing.
    """
    import pandas as pd

    m = pd.read_csv(path, dtype=str)
    out = {}
    for permno, cik in zip(m["permno"], m["cik"]):
        if cik is None or str(cik).strip() in ("", "nan"):
            continue
        try:
            out[int(str(permno).strip())] = bid12.normalize_cik(cik)
        except (TypeError, ValueError):
            continue
    return out


def _load_events(cik: str) -> tuple:
    """(events, status) for one CIK from the coder's event cache."""
    path = bid12._cache_path("events", f"{cik}.json")
    if not os.path.exists(path):
        return [], "not-extracted"
    with open(path) as fh:
        return json.load(fh)["events"], "ok"


def _coverage(td: dt.date) -> str:
    return ("full" if td >= bid12.EXTRACT_START
            and td + dt.timedelta(days=bid12.WINDOW_DAYS) <= bid12.EXTRACT_END
            else "partial")


def lookup_control(pairs_path: str = PAIRS_PATH,
                   out_dir: str = OUT_DIR,
                   map_path: str = CONTROL_MAP_PATH) -> dict:
    """Expand the match pairs to (control CIK, pseudo-TD) rows and code BID12.

    Returns the run-metadata dict (also written to disk).
    """
    import pandas as pd

    pairs = pd.read_csv(pairs_path)
    p2c = load_permno_cik_map(map_path)

    # One lookup per distinct (CIK, pseudo-TD); a control matched to two
    # treated firms sharing a TD is coded once and joined back to both pairs.
    rows, cache = [], {}
    n_unlinked = 0
    for r in pairs.itertuples():
        permno = int(r.control_permno)
        cik = p2c.get(permno)
        td = dt.date.fromisoformat(str(r.treated_td)[:10])
        if cik is None:
            n_unlinked += 1
            rows.append({
                "permno": permno, "cik": "", "td": str(td),
                "treated_permno": int(r.treated_permno),
                "treated_accession": getattr(r, "treated_accession", ""),
                "match_group": str(getattr(r, "match_group",
                                           r.treated_accession)),
                "extraction_status": "no-cik-link",
                "window_coverage": _coverage(td),
                "bid12": None, "first_bid_date": "", "first_bid_form": "",
                "first_bid_route": "", "first_bid_accession": "",
                "n_bid_events": 0, "filer_own_bid": 0, "ambiguous": 0,
                "n_ambiguous_events": 0, "excluded_prior_bid": 0,
                "prior_bid_any": 0, "prior_bid_last_date": "",
            })
            continue
        key = (cik, td)
        if key not in cache:
            events, status = _load_events(cik)
            # filer_cik / filer_name are None: a never-13D control has no 13D
            # filer, so filer_own_bid is 0 by construction (module docstring).
            res = bid12.lookup_bid12(events, td, None, None, cik)
            if status != "ok":
                res["bid12"] = None
            cache[key] = (res, status)
        res, status = cache[key]
        rows.append({
            "permno": permno, "cik": cik, "td": str(td),
            "treated_permno": int(r.treated_permno),
            "treated_accession": getattr(r, "treated_accession", ""),
            "match_group": str(getattr(r, "match_group",
                                       getattr(r, "treated_accession", ""))),
            "extraction_status": status, "window_coverage": _coverage(td),
            **res,
        })

    df = pd.DataFrame(rows).sort_values(["cik", "td", "treated_permno"])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "bid12_control.csv")
    df.to_csv(out_path, index=False)
    n_ciks = int(df.loc[df["cik"].astype(str).str.strip() != "",
                        "cik"].nunique())
    print(f"wrote {out_path}: {len(df)} matched-control rows "
          f"({n_ciks} distinct linked CIKs, {len(cache)} distinct "
          f"(CIK, pseudo-TD) lookups)", flush=True)

    # Event table for the control CIKs that actually appear in the pairs.
    records = []
    for cik in sorted({c for c, _ in cache}):
        path = bid12._cache_path("events", f"{cik}.json")
        if os.path.exists(path):
            with open(path) as fh:
                records.append(json.load(fh))
    bid12._events_csv(records,
                      os.path.join(out_dir, "bid12_events_control.csv"),
                      "control")

    amb = []
    for rec in records:
        for e in rec["events"]:
            if e["ambiguous"]:
                amb.append({"cik": rec["cik"], "name": rec["name"],
                            "event_date": e["event_date"], "form": e["form"],
                            "accession": e["accession"], "route": e["route"],
                            "confirm_detail": e.get("confirm_detail", "")})
    amb_path = os.path.join(out_dir, "bid12_control_ambiguous_cases.csv")
    pd.DataFrame(amb, columns=["cik", "name", "event_date", "form",
                               "accession", "route", "confirm_detail"]
                 ).to_csv(amb_path, index=False)
    print(f"wrote {amb_path}: {len(amb)} ambiguous control events", flush=True)

    rules_hash = ""
    if os.path.exists(bid12.RULEBOOK_PATH):
        with open(bid12.RULEBOOK_PATH, "rb") as fh:
            rules_hash = hashlib.sha256(fh.read()).hexdigest()
    meta = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "rules_sha256": rules_hash,
        "rulebook": os.path.relpath(bid12.RULEBOOK_PATH, bid12.HERE),
        "pairs_file": bid12._file_meta(pairs_path),
        "permno_cik_map": bid12._file_meta(map_path),
        "window_days": bid12.WINDOW_DAYS,
        "extraction_window": [str(bid12.EXTRACT_START),
                              str(bid12.EXTRACT_END)],
        "n_pair_rows": len(df),
        "n_distinct_control_ciks": n_ciks,
        "n_distinct_lookups": len(cache),
        "n_pairs_without_cik_link": n_unlinked,
        "control_lookup": {
            "bid12_1": int((df["bid12"] == 1).sum()),
            "bid12_0": int((df["bid12"] == 0).sum()),
            "bid12_empty_ambiguous": int(df["ambiguous"].sum()),
            "bid12_not_extracted": int(
                (df["extraction_status"] == "not-extracted").sum()),
            "excluded_prior_bid": int(df["excluded_prior_bid"].sum()),
            "prior_bid_any": int(df["prior_bid_any"].sum()),
        } if len(df) else {},
        "conventions": [
            "filer_own_bid is 0 by construction for controls (no 13D filer)",
            "unextracted control CIKs leave BID12 empty (rulebook §5.1 item 5)",
        ],
    }
    meta_path = os.path.join(out_dir, "bid12_control_run_meta.json")
    with open(meta_path, "w") as fh:
        json.dump(meta, fh, indent=1)
    print(f"wrote {meta_path}", flush=True)
    return meta


def main(argv: Optional[list] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pairs", default=PAIRS_PATH)
    ap.add_argument("--out-dir", default=OUT_DIR)
    ap.add_argument("--map", default=CONTROL_MAP_PATH)
    args = ap.parse_args(argv)
    if not os.path.exists(args.pairs):
        print(f"match pairs not landed yet ({args.pairs}) — run the matching "
              f"stage of empirics.estimate_did first")
        return 1
    lookup_control(args.pairs, args.out_dir, args.map)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
