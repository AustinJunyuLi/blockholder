"""Fact 2 event-file builder: SC 13D originals, 2022Q1-2025Q4.

Enumerates every original SC 13D in the sample window from the quarterly
EDGAR form indexes, fetches and parses each filing (CUSIP, event/filed
dates, CIKs, names, acceptance time), and writes
  * empirics/output/fact2_filings.csv      -- one row per filing
  * empirics/data/fact2_events_upload.txt  -- (CUSIP8, DD-MMM-YYYY) lines for
    the WRDS "U.S. Daily Event Study: Upload your own events" query.

Notes
-----
* form.idx lists one row per company-accession association, so a 13D appears
  twice (subject row + filer row): we dedupe by ``edgar_path``.
* Filings accepted after 16:00 ET are assigned to the next business day
  (the market trades on them the following session).
* Parsing is resume-safe: parsed rows append to ``data/fact2_parsed.jsonl``;
  rerunning skips already-parsed filings.

Usage:
    .venv/bin/python -m empirics.fact2_events                 # full universe
    .venv/bin/python -m empirics.fact2_events --limit-per-quarter 40 --seed 1
"""

from __future__ import annotations

import argparse
import json
import os

import numpy as np
import pandas as pd

from empirics.edgar_fetch import (
    DATA_DIR,
    download_form_index,
    fetch_filing_text,
    list_filings,
)
from empirics.parse_13d import parse_filing_fact2

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "output")
PARSE_CACHE = os.path.join(DATA_DIR, "fact2_parsed.jsonl")
UPLOAD_TXT = os.path.join(DATA_DIR, "fact2_events_upload.txt")

QUARTERS = [(y, q) for y in (2022, 2023, 2024, 2025) for q in (1, 2, 3, 4)]
RULE_DATE = pd.Timestamp("2024-02-05")
MMM = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
       "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


def enumerate_originals(limit_per_quarter: int | None,
                        rng: np.random.Generator) -> list:
    """All SC 13D original rows, deduped by edgar_path."""
    rows, seen = [], set()
    for year, qtr in QUARTERS:
        idx_path = download_form_index(year, qtr)
        # EDGAR renamed the form type to "SCHEDULE 13D" from Dec 2024
        qrows = list_filings(idx_path, form_types=("SC 13D", "SCHEDULE 13D"))
        uniq = []
        for r in qrows:
            if r["edgar_path"] in seen:
                continue
            seen.add(r["edgar_path"])
            uniq.append(dict(r, quarter=f"{year}Q{qtr}"))
        dup_share = 1.0 - len(uniq) / max(len(qrows), 1)
        if limit_per_quarter and len(uniq) > limit_per_quarter:
            keep = rng.choice(len(uniq), size=limit_per_quarter, replace=False)
            uniq = [uniq[i] for i in sorted(keep)]
        print(f"{year}Q{qtr}: {len(qrows)} index rows -> {len(uniq)} unique "
              f"filings kept (subject/filer dup share {dup_share:.0%})")
        rows.extend(uniq)
    return rows


def load_cache() -> dict:
    cache = {}
    if os.path.exists(PARSE_CACHE):
        with open(PARSE_CACHE, "r", encoding="utf-8") as fh:
            for line in fh:
                try:
                    rec = json.loads(line)
                    cache[rec["edgar_path"]] = rec
                except (json.JSONDecodeError, KeyError):
                    continue
    return cache


def parse_all(rows: list) -> list:
    cache = load_cache()
    n_cached = sum(1 for r in rows if r["edgar_path"] in cache)
    print(f"parse cache: {n_cached}/{len(rows)} already done")
    out = []
    with open(PARSE_CACHE, "a", encoding="utf-8") as fh:
        for i, r in enumerate(rows):
            if r["edgar_path"] in cache:
                out.append(cache[r["edgar_path"]])
                continue
            try:
                text = fetch_filing_text(r["edgar_path"])
                p = parse_filing_fact2(text)
                p["filed"] = p["filed"].isoformat() if p.get("filed") else None
                p["event"] = p["event"].isoformat() if p.get("event") else None
            except Exception as exc:  # noqa: BLE001 -- record and continue
                p = {"error": str(exc)}
            rec = {**r, **p}
            fh.write(json.dumps(rec) + "\n")
            fh.flush()
            out.append(rec)
            if (i + 1) % 100 == 0:
                print(f"  ... {i + 1}/{len(rows)}")
    return out


def build_outputs(parsed: list) -> pd.DataFrame:
    df = pd.DataFrame(parsed)
    df["filed"] = pd.to_datetime(df.get("filed"), errors="coerce")
    df["event"] = pd.to_datetime(df.get("event"), errors="coerce")
    df["delay_bdays"] = [
        float(np.busday_count(np.datetime64(e.date(), "D"),
                              np.datetime64(f.date(), "D")))
        if pd.notna(e) and pd.notna(f) else np.nan
        for e, f in zip(df["event"], df["filed"])]
    df["post"] = (df["filed"] >= RULE_DATE).astype("Int64")

    # market reaction day: filed date, shifted to the next business day when
    # the filing was accepted after 16:00 ET (and weekend-rolled regardless)
    shift = df["accepted_after_4pm"].fillna(False).astype(bool).to_numpy()
    filed64 = df["filed"].to_numpy().astype("datetime64[D]")
    trade = np.full(len(df), np.datetime64("NaT"), dtype="datetime64[D]")
    ok = ~pd.isna(df["filed"]).to_numpy()
    trade[ok & ~shift] = np.busday_offset(filed64[ok & ~shift], 0,
                                          roll="forward")
    trade[ok & shift] = np.busday_offset(filed64[ok & shift], 1,
                                         roll="forward")
    df["event_trade_date"] = trade

    df["cusip8"] = df["cusip"].str[:8].where(df["cusip"].notna())
    os.makedirs(OUT_DIR, exist_ok=True)
    df.to_csv(os.path.join(OUT_DIR, "fact2_filings.csv"), index=False)

    ok_rows = df.dropna(subset=["cusip8", "event_trade_date"])
    pairs = (ok_rows[["cusip8", "event_trade_date"]]
             .drop_duplicates()
             .sort_values(["event_trade_date", "cusip8"]))
    with open(UPLOAD_TXT, "w", encoding="ascii") as fh:
        for _, row in pairs.iterrows():
            d = pd.Timestamp(row["event_trade_date"])
            fh.write(f"{row['cusip8']} {d.day:02d}-{MMM[d.month - 1]}-{d.year}\n")

    n = len(df)
    print(f"\nfilings parsed: {n}")
    print(f"  cusip found:        {df['cusip'].notna().sum()} "
          f"({df['cusip'].notna().mean():.0%})")
    print(f"  event date found:   {df['event'].notna().sum()} "
          f"({df['event'].notna().mean():.0%})")
    print(f"  pre  (filed < {RULE_DATE.date()}): {(df['post'] == 0).sum()}")
    print(f"  post (filed >= {RULE_DATE.date()}): {(df['post'] == 1).sum()}")
    print(f"WRDS upload lines: {len(pairs)} -> {UPLOAD_TXT}")
    return df


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Fact 2: build 13D event file.")
    ap.add_argument("--limit-per-quarter", type=int, default=None)
    ap.add_argument("--seed", type=int, default=20260611)
    args = ap.parse_args(argv)
    os.makedirs(DATA_DIR, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    rows = enumerate_originals(args.limit_per_quarter, rng)
    parsed = parse_all(rows)
    build_outputs(parsed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
