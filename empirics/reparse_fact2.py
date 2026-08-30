"""Re-fetch and re-parse the full 2022Q1-2025Q4 Schedule 13D universe.

SPEC research/empirics_v4/SPEC.md SS2.2 (mandatory re-parse) and SS13 item 2:
the committed ``empirics/data/fact2_parsed.jsonl`` was built with the broken
pre-``b026872`` parser (2025 trigger dates parse at 0%, the 2024
``SC 13D`` -> ``SCHEDULE 13D`` rename silently dropped 132 filings,
percent-of-class is None for the whole XML era). This script re-enumerates
the sixteen on-disk quarterly ``form.idx`` files, re-downloads every initial
13D master submission (cached, resumable), re-parses with the fixed
``empirics.parse_13d``, recovers the EDGAR acceptance timestamp from the
master text's ``<ACCEPTANCE-DATETIME>`` block (submissions-API fallback),
carries ``cusip`` / ``subject_name`` / ``filer_name`` forward from the old
file by accession join, archives the old file, and writes the new canonical
``fact2_parsed.jsonl`` with the identical schema. The ``analyze`` stage then
rebuilds the SPEC SS2.3 attrition funnel, per-quarter parse rates, the SS2.1
count tables, the SS4 dose-filer counts, and the SS3.6 / SS8.6 MDE arithmetic
on realised counts.

Stages (idempotent; re-running is cheap once texts are cached)::

    .venv/bin/python -m empirics.reparse_fact2 --stage fetch     # the slow one
    .venv/bin/python -m empirics.reparse_fact2 --stage finalize  # archive+write
    .venv/bin/python -m empirics.reparse_fact2 --stage analyze   # funnel/counts
    .venv/bin/python -m empirics.reparse_fact2                   # all of the above

``--link-file`` (default None) points at a rebuilt CIK->CUSIP link CSV
(columns ``cik``, ``cusip``); without it the CRSP match uses the cusip values
carried forward from the old file and the funnel marks those rows provisional.

SEC fair access: the caller holds /tmp/sec_edgar_bulk.lock for the download
phase; the fetcher itself is throttled to ~4 req/s (empirics.edgar_fetch).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import re
import sys
import time
from typing import Optional

import numpy as np
import pandas as pd

from empirics.edgar_fetch import DATA_DIR, fetch, fetch_filing_text, list_filings
from empirics.parse_13d import parse_filing

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "output")
FILINGS_DIR = os.path.join(DATA_DIR, "filings")
SUBMISSIONS_DIR = os.path.join(DATA_DIR, "submissions")

OLD_PATH = os.path.join(DATA_DIR, "fact2_parsed.jsonl")
ARCHIVE_PATH = os.path.join(DATA_DIR, "fact2_parsed_oldparser_2026-08-20.jsonl")

QUARTERS = [(y, q) for y in (2022, 2023, 2024, 2025) for q in (1, 2, 3, 4)]
FORM_TYPES = ("SC 13D", "SCHEDULE 13D")  # initials only; aliases expand inside

RULE_DATE = pd.Timestamp("2024-02-05")   # five-business-day rule effective
ADOPTION_DATE = pd.Timestamp("2023-10-10")  # pre window ends 2023-10-09 (SS2.6)
PRE_START = pd.Timestamp("2022-01-01")

RE_ACCEPTANCE = re.compile(r"<ACCEPTANCE-DATETIME>\s*(\d{14})")

CRSP_PATH = os.path.join(DATA_DIR, "crsp_daily.csv")
CRSP_USECOLS = ["PERMNO", "HdrCUSIP", "CUSIP", "USIncFlg", "ShareType",
                "DlyCalDt", "DlyPrc", "DlyRet", "DlyVol"]

# MDE assumptions registered in SPEC SS3.6 / SS8.6 (assumptions, not card facts).
SIGMA_JUMP = 0.12
SIGMA_RUNUP = 0.15
Z_MDE = 2.802  # z_0.975 + z_0.80: 5% two-sided, 80% power
DID_VAR = 0.1705  # sigma^2_T + sigma^2_C/3 from GS base rates 0.181 / 0.072
DID_CLUSTER_MULT = 1.31
SLOPE_CLUSTER_LO, SLOPE_CLUSTER_HI = 1.1, 1.9


# --------------------------------------------------------------------------
# stage 1: enumerate
# --------------------------------------------------------------------------

def enumerate_initials() -> pd.DataFrame:
    """All initial 13D rows from the sixteen on-disk form.idx files."""
    rows = []
    for year, qtr in QUARTERS:
        idx_path = os.path.join(DATA_DIR, f"form_{year}_QTR{qtr}.idx")
        if not os.path.exists(idx_path):
            raise FileNotFoundError(f"missing quarterly index {idx_path}")
        quarter = f"{year}Q{qtr}"
        for r in list_filings(idx_path, form_types=FORM_TYPES):
            rows.append({**r, "quarter": quarter})
    df = pd.DataFrame(rows)
    df["accession"] = df["edgar_path"].map(
        lambda p: os.path.basename(p)[:-4])
    # form.idx lists a 13D twice -- once under the filer's CIK directory and
    # once under the subject's (same accession, same submission text). Keep
    # the first listing; the count of dropped duplicate index rows is
    # reported. Both directory variants are retained in _all_paths so the
    # fetcher can fall back if one 404s.
    n_idx_rows = len(df)
    paths = df.groupby("accession")["edgar_path"].agg(tuple)
    df = df.drop_duplicates(subset="accession", keep="first").reset_index(drop=True)
    df["all_paths"] = df["accession"].map(paths)
    print(f"enumerate: {n_idx_rows} idx rows -> {len(df)} unique filings "
          f"({n_idx_rows - len(df)} duplicate subject/filer index rows dropped)")
    return df


# --------------------------------------------------------------------------
# stage 2: fetch (cached, resumable)
# --------------------------------------------------------------------------

def _cache_path(accession: str) -> str:
    return os.path.join(FILINGS_DIR, accession.replace("-", "") + ".txt")


def fetch_all(enum: pd.DataFrame, max_fetch: Optional[int] = None) -> list:
    """Download every enumerated filing's master .txt into FILINGS_DIR.

    Skips files already cached; returns the list of accessions that failed
    after the fetcher's own retries. Resumable: re-run until it returns [].
    """
    os.makedirs(FILINGS_DIR, exist_ok=True)
    todo = [r for r in enum.itertuples()
            if not (os.path.exists(_cache_path(r.accession))
                    and os.path.getsize(_cache_path(r.accession)) > 0)]
    if max_fetch is not None:
        todo = todo[:max_fetch]
    total = len(todo)
    print(f"fetch: {len(enum)} enumerated, {total} to download "
          f"(cached: {len(enum) - total})")
    failures, t0 = [], time.monotonic()
    for i, r in enumerate(todo):
        try:
            text, last_exc = None, None
            for path in dict.fromkeys(r.all_paths):  # filer dir, then subject dir
                try:
                    text = fetch_filing_text(path)
                    break
                except Exception as exc:
                    last_exc = exc
            if text is None:
                raise last_exc
            with open(_cache_path(r.accession), "w", encoding="latin-1") as fh:
                fh.write(text)
        except Exception as exc:  # logged, retried on the next run
            failures.append({"accession": r.accession, "error": str(exc)})
        if (i + 1) % 100 == 0 or i + 1 == total:
            rate = (i + 1) / max(time.monotonic() - t0, 1e-9)
            eta = (total - i - 1) / max(rate, 1e-9)
            print(f"  ... {i + 1}/{total}  ({rate:.2f}/s, ETA {eta / 60:.1f} min, "
                  f"{len(failures)} failures)", flush=True)
    fail_path = os.path.join(FILINGS_DIR, "_failures.json")
    with open(fail_path, "w") as fh:
        json.dump(failures, fh, indent=1)
    print(f"fetch: done, {len(failures)} failures -> {fail_path}")
    return failures


# --------------------------------------------------------------------------
# stage 3: parse (local, fast)
# --------------------------------------------------------------------------

def parse_acceptance(text: str) -> Optional[pd.Timestamp]:
    """EDGAR acceptance datetime from the master submission's SGML block."""
    m = RE_ACCEPTANCE.search(text)
    if not m:
        return None
    try:
        return pd.Timestamp(dt.datetime.strptime(m.group(1), "%Y%m%d%H%M%S"))
    except ValueError:
        return None


def _submissions_acceptance(cik: str, accession: str) -> Optional[pd.Timestamp]:
    """Fallback: acceptance datetime from the EDGAR submissions API.

    Cached per-CIK under ``data/submissions/`` (the JSON can exceed the
    fetcher's 400 KB default, so pull with a larger cap, same throttle).
    Only used when the master .txt lacks an <ACCEPTANCE-DATETIME> block.
    """
    os.makedirs(SUBMISSIONS_DIR, exist_ok=True)
    cik10 = f"{int(cik):010d}"
    cache = os.path.join(SUBMISSIONS_DIR, f"CIK{cik10}.json")
    if not os.path.exists(cache):
        url = f"https://data.sec.gov/submissions/CIK{cik10}.json"
        with open(cache, "wb") as fh:
            fh.write(fetch(url, max_bytes=20_000_000))
    try:
        with open(cache, "rb") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError):
        return None
    recent = data.get("filings", {}).get("recent", {})
    accs = recent.get("accessionNumber", [])
    if accession in accs:
        raw = recent.get("acceptanceDateTime", [None] * len(accs))[accs.index(accession)]
        return pd.Timestamp(raw) if raw else None
    # older filings live in paginated extra files listed in filings.files
    for extra in data.get("filings", {}).get("files", []):
        name = extra.get("name")
        if not name:
            continue
        page = os.path.join(SUBMISSIONS_DIR, f"CIK{cik10}_{name}")
        if not os.path.exists(page):
            url = f"https://data.sec.gov/submissions/{name}"
            with open(page, "wb") as fh:
                fh.write(fetch(url, max_bytes=20_000_000))
        try:
            with open(page, "rb") as fh:
                pdata = json.load(fh)
        except (json.JSONDecodeError, OSError):
            continue
        accs = pdata.get("accessionNumber", [])
        if accession in accs:
            raw = pdata.get("acceptanceDateTime", [None] * len(accs))[accs.index(accession)]
            return pd.Timestamp(raw) if raw else None
    return None


def parse_all(enum: pd.DataFrame, use_api_fallback: bool = True) -> pd.DataFrame:
    """Re-parse every cached filing text; recover the acceptance timestamp."""
    rows, n_missing_cache, n_api = [], 0, 0
    for r in enum.itertuples():
        path = _cache_path(r.accession)
        rec = {"form": r.form, "company": r.company, "cik": r.cik,
               "date_filed": r.date_filed, "edgar_path": r.edgar_path,
               "quarter": r.quarter, "accession": r.accession}
        if not os.path.exists(path):
            n_missing_cache += 1
            rec.update({"filed": None, "subject_cik": None, "filer_cik": None,
                        "event": None, "pct_of_class": None, "has_xml": None,
                        "accepted": None, "accepted_after_4pm": None,
                        "_fetched": False})
            rows.append(rec)
            continue
        with open(path, "r", encoding="latin-1", errors="replace") as fh:
            text = fh.read()
        p = parse_filing(text)
        acc = parse_acceptance(text)
        if acc is None and use_api_fallback:
            acc = _submissions_acceptance(r.cik, r.accession)
            n_api += 1
        rec.update({
            "filed": p["filed"].isoformat() if p["filed"] else None,
            "subject_cik": p["subject_cik"],
            "filer_cik": p["filer_cik"],
            "event": p["event"].isoformat() if p["event"] else None,
            "pct_of_class": p["pct_of_class"],
            "has_xml": p["has_xml"],
            "accepted": acc.strftime("%Y-%m-%d %H:%M:%S") if acc is not None else None,
            "accepted_after_4pm": (bool(acc.hour >= 16) if acc is not None else None),
            "_fetched": True,
        })
        rows.append(rec)
    df = pd.DataFrame(rows)
    print(f"parse: {len(df)} rows, {n_missing_cache} without cached text, "
          f"{n_api} needed the submissions-API fallback")
    return df


# --------------------------------------------------------------------------
# stage 4: carry-forward, archive, write canonical file
# --------------------------------------------------------------------------

def load_carry_source() -> pd.DataFrame:
    """Old-parser rows to carry cusip/subject_name/filer_name forward from."""
    src = ARCHIVE_PATH if os.path.exists(ARCHIVE_PATH) else OLD_PATH
    df = pd.read_json(src, lines=True)
    carry = df.set_index("accession")[["cusip", "subject_name", "filer_name"]]
    return carry[~carry.index.duplicated(keep="first")]


def finalize(new: pd.DataFrame, allow_incomplete: bool = False) -> pd.DataFrame:
    n_unfetched = int((~new["_fetched"]).sum())
    if n_unfetched and not allow_incomplete:
        raise RuntimeError(f"{n_unfetched} filings have no cached text; "
                           f"re-run --stage fetch first")
    carry = load_carry_source()
    joined = new.join(carry, on="accession")
    n_matched = int(joined["cusip"].notna().sum())
    n_old_matched = int(joined["subject_name"].notna().sum())
    print(f"carry-forward: {n_old_matched}/{len(joined)} rows matched the old "
          f"file by accession; {n_matched} carry a cusip; "
          f"{len(joined) - n_old_matched} rows get null cusip")
    out = joined[["form", "company", "cik", "date_filed", "edgar_path",
                  "quarter", "accession", "filed", "subject_cik", "filer_cik",
                  "event", "pct_of_class", "has_xml", "cusip", "subject_name",
                  "filer_name", "accepted", "accepted_after_4pm"]]
    if not os.path.exists(ARCHIVE_PATH):
        os.rename(OLD_PATH, ARCHIVE_PATH)
        print(f"archived old file -> {ARCHIVE_PATH}")
    out.to_json(OLD_PATH + ".tmp", orient="records", lines=True)
    os.replace(OLD_PATH + ".tmp", OLD_PATH)
    print(f"wrote {len(out)} rows -> {OLD_PATH}")
    return out


# --------------------------------------------------------------------------
# stage 5: analysis -- funnel, parse rates, counts, MDE arithmetic
# --------------------------------------------------------------------------

def _cusip8(value) -> Optional[str]:
    if not isinstance(value, str) or not value.strip():
        return None
    v = value.strip()
    return v[:8] if len(v) >= 8 else None


def load_crsp_eligible(path: str = CRSP_PATH) -> tuple:
    """Load the CRSP snapshot (usecols only -- the file is 1.2 GB).

    Returns (cusip8 -> [PERMNO], {PERMNO: (dates, valid)}) where `valid`
    marks days usable for the Amihud screen (return, nonzero price and
    positive volume all present). A PERMNO is eligible when any daily row
    is ShareType == 'NS' (the snapshot's common-stock code; AD/SB/UG/CE are
    ADRs / beneficial-interest shares / units / other) with USIncFlg == 'Y'.
    """
    t0 = time.monotonic()
    dtype = {"PERMNO": "int32", "HdrCUSIP": "category", "CUSIP": "category",
             "ShareType": "category", "USIncFlg": "category",
             "DlyPrc": "float32", "DlyRet": "float32", "DlyVol": "float64"}
    df = pd.read_csv(path, usecols=CRSP_USECOLS, dtype=dtype, low_memory=False)
    df["date"] = pd.to_datetime(df["DlyCalDt"])
    eligible = set(map(int, df.loc[(df["ShareType"] == "NS")
                                   & (df["USIncFlg"] == "Y"), "PERMNO"].unique()))
    pairs = pd.concat([
        df[["PERMNO", "CUSIP"]].rename(columns={"CUSIP": "c8"}),
        df[["PERMNO", "HdrCUSIP"]].rename(columns={"HdrCUSIP": "c8"}),
    ])
    pairs = pairs[pairs["PERMNO"].isin(eligible)]
    pairs["c8"] = pairs["c8"].astype("string").str[:8]
    pairs = pairs.dropna(subset=["c8"]).drop_duplicates()
    link = {k: sorted(map(int, g)) for k, g in
            pairs.groupby("c8")["PERMNO"].agg(lambda s: set(s)).items()}
    sub = df[df["PERMNO"].isin(eligible)].copy()
    sub["valid"] = (sub["DlyRet"].notna() & sub["DlyPrc"].notna()
                    & (sub["DlyPrc"] != 0) & sub["DlyVol"].notna()
                    & (sub["DlyVol"] > 0))
    sub = sub.sort_values(["PERMNO", "date"])
    windows = {int(p): (g["date"].values.astype("datetime64[D]"),
                        g["valid"].values)
               for p, g in sub.groupby("PERMNO")}
    print(f"crsp: {len(df)} rows, {len(eligible)} eligible PERMNOs, "
          f"{len(link)} cusip8 keys ({time.monotonic() - t0:.0f}s)")
    return link, windows


def count_valid_obs(windows: dict, permno: int, td: pd.Timestamp,
                    lo_days: int = 126, hi_days: int = 6) -> int:
    """Valid daily observations in [TD-lo_days, TD-hi_days] (calendar days)."""
    entry = windows.get(permno)
    if entry is None:
        return 0
    dates, valid = entry
    lo = np.datetime64((td - pd.Timedelta(days=lo_days)).date(), "D")
    hi = np.datetime64((td - pd.Timedelta(days=hi_days)).date(), "D")
    i, j = np.searchsorted(dates, lo), np.searchsorted(dates, hi, side="right")
    return int(valid[i:j].sum())


def crsp_match(df: pd.DataFrame, link: dict, windows: dict) -> pd.Series:
    """Funnel step 3: subject -> eligible PERMNO with >=60 valid obs."""
    permnos, reasons, n_obs = [], [], []
    for r in df.itertuples():
        td = r.td
        c8 = _cusip8(r.cusip)
        if c8 is None:
            permnos.append(None); reasons.append("no_cusip"); n_obs.append(0)
            continue
        cands = sorted(link.get(c8, ()))
        if not cands:
            permnos.append(None); reasons.append("cusip_not_in_crsp")
            n_obs.append(0)
            continue
        best_p, best_n = None, -1
        for p in cands:
            n = count_valid_obs(windows, p, td)
            if n > best_n:
                best_p, best_n = p, n
        if best_n < 60:
            permnos.append(None); reasons.append("insufficient_obs")
            n_obs.append(best_n)
        else:
            permnos.append(best_p); reasons.append("matched"); n_obs.append(best_n)
    out = pd.DataFrame({"permno": permnos, "match_reason": reasons,
                        "n_valid_obs": n_obs}, index=df.index)
    return out


def dedup_firm_trigger(df: pd.DataFrame) -> tuple:
    """Funnel step 4: one obs per (subject firm, trigger date); where the same
    firm is triggered twice within 365 days, keep the first, flag the second."""
    df = df.sort_values(["permno", "td", "fd", "accession"])
    keep, flagged_second, dropped_exact = [], [], []
    for _, g in df.groupby("permno", sort=False):
        last_kept: Optional[pd.Timestamp] = None
        seen_td = set()
        for r in g.itertuples():
            if r.td in seen_td:
                dropped_exact.append(r.Index)
                continue
            if last_kept is not None and (r.td - last_kept).days < 365:
                flagged_second.append(r.Index)
                continue
            seen_td.add(r.td)
            keep.append(r.Index)
            last_kept = r.td
    return keep, flagged_second, dropped_exact


def mde_slope(n: int, w: float, sigma: float) -> dict:
    """SPEC SS3.6: SE = sigma / sqrt(N w (1-w)); MDE = 2.802 * SE."""
    denom = math.sqrt(n * w * (1.0 - w))
    se = sigma / denom
    return {"N": n, "w": w, "sqrt_term": denom, "sigma": sigma,
            "SE": se, "MDE": Z_MDE * se,
            "MDE_clustered": [Z_MDE * se * SLOPE_CLUSTER_LO,
                              Z_MDE * se * SLOPE_CLUSTER_HI]}


def mde_did(n_pre: int, n_post: int) -> dict:
    """SPEC SS8.6: SE = sqrt(0.1705 * (1/n_pre + 1/n_post)); MDE = 2.802 * SE."""
    inv = 1.0 / n_pre + 1.0 / n_post
    se = math.sqrt(DID_VAR * inv)
    return {"n_pre": n_pre, "n_post": n_post, "inv_sum": inv, "SE": se,
            "MDE": Z_MDE * se, "MDE_clustered": Z_MDE * se * DID_CLUSTER_MULT}


def analyze(df: pd.DataFrame, link_source: str) -> dict:
    """Rebuild the SPEC SS2.1 tables, the SS2.3 funnel, parse rates, SS4 dose
    counts and the SS3.6/SS8.6 MDE arithmetic on the realised counts."""
    os.makedirs(OUT_DIR, exist_ok=True)
    df = df.copy()
    df["td"] = pd.to_datetime(df["event"])
    df["fd"] = pd.to_datetime(df["filed"]).fillna(pd.to_datetime(df["date_filed"]))
    df["cusip8"] = df["cusip"].map(_cusip8)
    has_td = df["td"].notna()
    df["post_td"] = np.where(has_td, df["td"] >= RULE_DATE, np.nan)
    df["post_fd"] = df["fd"] >= RULE_DATE
    df["gap_days"] = (df["fd"] - df["td"]).dt.days
    in_band = has_td & df["gap_days"].between(0, 90)
    stale = has_td & (df["td"].dt.year <= 2021)

    # -- per-quarter trigger-date parse rates (the referee's first number) --
    q = (df.groupby("quarter")
           .agg(n_filings=("accession", "size"),
                n_trigger=("td", lambda s: int(s.notna().sum()))))
    q["parse_rate"] = q["n_trigger"] / q["n_filings"]
    q.to_csv(os.path.join(OUT_DIR, "reparse_quarterly_parse_rates.csv"))

    # -- funnel (SPEC SS2.3, in order) --------------------------------------
    link, windows = load_crsp_eligible()
    band = df[in_band].copy()
    match = crsp_match(band, link, windows)
    band = band.join(match)
    matched = band[band["match_reason"] == "matched"].copy()
    keep, flagged_second, dropped_exact = dedup_firm_trigger(matched)
    final = matched.loc[matched.index.isin(keep)].copy()

    def split(sub: pd.DataFrame) -> tuple:
        s = sub["post_td"].dropna()
        return int((s == 0).sum()), int((s == 1).sum())

    pre1, post1 = split(df[has_td])
    pre2, post2 = split(df[in_band])
    pre3, post3 = split(matched)
    pre4, post4 = split(final)
    oob = df[has_td & ~in_band]
    funnel_rows = [
        {"step": 0, "description": "enumerated initial 13Ds (SC 13D / SCHEDULE 13D, amendments excluded)",
         "n": len(df), "n_pre": None, "n_post": None, "dropped": None,
         "notes": "16 quarterly form.idx files, 2022Q1-2025Q4"},
        {"step": 1, "description": "trigger date parsed",
         "n": int(has_td.sum()), "n_pre": pre1, "n_post": post1,
         "dropped": int((~has_td).sum()),
         "notes": "drop = no parseable trigger date"},
        {"step": 2, "description": "0 <= (FD - TD) <= 90 calendar days",
         "n": int(in_band.sum()), "n_pre": pre2, "n_post": post2,
         "dropped": int(len(oob)),
         "notes": f"out-of-band: {int((oob['gap_days'] < 0).sum())} negative, "
                  f"{int((oob['gap_days'] > 90).sum())} over 90d; of which stale "
                  f"2014-2021 triggers: {int((oob['td'].dt.year <= 2021).sum())} "
                  f"of {int(stale.sum())} stale total"},
        {"step": 3, "description": "subject CIK links to CRSP PERMNO (ShareType common + USIncFlg US + >=60 valid obs in [TD-126, TD-6])",
         "n": len(matched), "n_pre": pre3, "n_post": post3,
         "dropped": len(band) - len(matched),
         "notes": "drop reasons: "
                  + ", ".join(f"{k}={v}" for k, v in
                              band["match_reason"].value_counts().items()
                              if k != "matched")
                  + f"; link source: {link_source}"},
        {"step": 4, "description": "one obs per (subject firm, trigger date), 365-day keep-first",
         "n": len(final), "n_pre": pre4, "n_post": post4,
         "dropped": len(matched) - len(final),
         "notes": f"{len(dropped_exact)} exact (firm, TD) duplicates, "
                  f"{len(flagged_second)} flagged-second within 365 days"},
    ]
    funnel = pd.DataFrame(funnel_rows)
    funnel.to_csv(os.path.join(OUT_DIR, "reparse_funnel.csv"), index=False)

    # -- SPEC SS2.1 tables ----------------------------------------------------
    def _tab(mask):
        sub = df[mask]
        return {"n": len(sub),
                "with_trigger": int(sub["td"].notna().sum()),
                "with_trigger_and_cusip": int((sub["td"].notna()
                                               & sub["cusip8"].notna()).sum()),
                "with_pct": int(sub["pct_of_class"].notna().sum())}

    filed_pre, filed_post = _tab(~df["post_fd"]), _tab(df["post_fd"])
    td_pre = df[df["post_td"] == 0]
    td_post = df[df["post_td"] == 1]
    trig_split = {
        "pre": {"with_trigger": len(td_pre),
                "with_trigger_and_cusip": int(td_pre["cusip8"].notna().sum())},
        "post": {"with_trigger": len(td_post),
                 "with_trigger_and_cusip": int(td_post["cusip8"].notna().sum())},
    }
    subj_pre = set(df.loc[~df["post_fd"], "subject_cik"].dropna())
    subj_post = set(df.loc[df["post_fd"], "subject_cik"].dropna())
    straddle = has_td & (df["td"] < RULE_DATE) & (df["fd"] >= RULE_DATE)
    trig_years = (df.loc[has_td, "td"].dt.year.value_counts().sort_index()
                  .to_dict())

    # -- SPEC SS4 dose filers (pre-period behaviour) --------------------------
    def dose_counts(lo: pd.Timestamp, hi: pd.Timestamp) -> dict:
        pre = df[(df["fd"] >= lo) & (df["fd"] <= hi)]
        per_filer = pre.groupby("filer_cik").size()
        repeat = per_filer[per_filer >= 2]
        return {"window": f"{lo.date()}..{hi.date()}",
                "n_filings": len(pre), "n_filers": int(per_filer.size),
                "filers_ge2": int(repeat.size),
                "filings_covered_by_ge2": int(repeat.sum())}

    dose = {"dose_window_2023_10_09": dose_counts(PRE_START, ADOPTION_DATE
                                                  - pd.Timedelta(days=1)),
            "filed_pre_rule_2024_02_05": dose_counts(PRE_START, RULE_DATE
                                                     - pd.Timedelta(days=1))}

    # -- accepted-timestamp verification against the old file ----------------
    old_rows = pd.read_json(ARCHIVE_PATH, lines=True)
    old_acc = old_rows[["accession", "accepted"]].dropna()
    ver = old_acc.merge(df[["accession", "accepted"]], on="accession",
                        suffixes=("_old", "_new")).dropna()
    if len(ver) > 20:
        ver = ver.sample(20, random_state=20260830)
    agree = int((ver["accepted_old"] == ver["accepted_new"]).sum())

    # -- MDE arithmetic on realised counts ------------------------------------
    n3, w3 = pre3 + post3, post3 / (pre3 + post3) if pre3 + post3 else float("nan")
    n4, w4 = pre4 + post4, post4 / (pre4 + post4) if pre4 + post4 else float("nan")
    mde = {
        "assumptions": {"sigma_jump": SIGMA_JUMP, "sigma_runup": SIGMA_RUNUP,
                        "z": Z_MDE, "did_var": DID_VAR,
                        "did_cluster_mult": DID_CLUSTER_MULT,
                        "slope_cluster_range": [SLOPE_CLUSTER_LO, SLOPE_CLUSTER_HI],
                        "note": "sigma values and GS base rates remain assumptions"},
        "s36_crsp_matched": {"jump": mde_slope(n3, w3, SIGMA_JUMP),
                             "runup": mde_slope(n3, w3, SIGMA_RUNUP)},
        "s36_estimation_sample": {"jump": mde_slope(n4, w4, SIGMA_JUMP),
                                  "runup": mde_slope(n4, w4, SIGMA_RUNUP)},
        "s86_S1": mde_did(pre4, post4),
        "s86_S1_crsp_matched_variant": mde_did(pre3, post3),
        "s86_S2_20pct": mde_did(max(1, round(0.2 * pre4)),
                                max(1, round(0.2 * post4))),
    }

    counts = {
        "generated": dt.datetime.now().isoformat(timespec="seconds"),
        "link_source": link_source,
        "enumerated_total": len(df),
        "per_quarter_enumerated": {str(k): int(v) for k, v in
                                   df["quarter"].value_counts().sort_index().items()},
        "fetch_failures": int((df["_fetched"] == False).sum()) if "_fetched" in df else 0,
        "filed_date_split_reference": {"filed_pre_2024_02_05": filed_pre,
                                       "filed_on_or_after": filed_post,
                                       "total": _tab(pd.Series(True, index=df.index))},
        "trigger_date_split_design": trig_split,
        "unique_subject_ciks_filed_split": {
            "pre": len(subj_pre), "post": len(subj_post),
            "total": len(subj_pre | subj_post), "in_both": len(subj_pre & subj_post)},
        "unique_filer_ciks": int(df["filer_cik"].nunique()),
        "trigger_year_distribution": {int(k): int(v) for k, v in trig_years.items()},
        "stale_trigger_2014_2021": int(stale.sum()),
        "stale_dropped_by_90d_band": int((oob["td"].dt.year <= 2021).sum()),
        "straddle_td_pre_fd_post": int(straddle.sum()),
        "straddle_within_final_sample": int((straddle & df.index.isin(final.index)).sum()),
        "cusip_carry_forward": {
            "rows_with_old_match": int(df["cusip"].notna().sum()),
            "rows_null_cusip": int(df["cusip"].isna().sum())},
        "pct_of_class_parsed": int(df["pct_of_class"].notna().sum()),
        "accepted_recovered": int(df["accepted"].notna().sum()),
        "accepted_route": "<ACCEPTANCE-DATETIME> in master .txt (submissions-API fallback)",
        "accepted_verification": {"n_compared": len(ver), "n_agree_exact": agree,
                                  "agreement": agree / len(ver) if len(ver) else None},
        "funnel": funnel_rows,
        "quarterly_parse_rates": [
            {"quarter": str(r.quarter), "n_filings": int(r.n_filings),
             "n_trigger": int(r.n_trigger), "parse_rate": float(r.parse_rate)}
            for r in q.reset_index().itertuples()],
        "dose_filers": dose,
        "mde": mde,
        "prediction_check_s22": {
            "predicted": {"pre": 3000, "post": 1950, "N": 4950, "w": 0.394},
            "realised_crsp_matched": {"pre": pre3, "post": post3, "N": n3, "w": w3},
            "realised_estimation_sample": {"pre": pre4, "post": post4,
                                           "N": n4, "w": w4}},
    }
    with open(os.path.join(OUT_DIR, "reparse_counts.json"), "w") as fh:
        json.dump(counts, fh, indent=1, default=str)
    print(f"analyze: wrote funnel ({len(final)} final), parse rates, counts")
    return counts


# --------------------------------------------------------------------------

def _load_link_file(path: str) -> pd.Series:
    """Rebuilt CIK->CUSIP link; overrides the carry-forward cusip. Expects the
    ticket-13 format (``subject_cik`` + ``cusip9``); index normalised to the
    unpadded integer string so it joins on the filing's ``subject_cik``."""
    link = pd.read_csv(path, dtype=str)
    link.columns = [c.lower() for c in link.columns]
    cik_col = next(c for c in link.columns if c in ("subject_cik", "cik"))
    cusip_col = next(c for c in link.columns if c.startswith("cusip"))
    s = link.set_index(cik_col)[cusip_col].dropna()
    s.index = s.index.map(lambda c: str(int(c)))
    return s


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--stage", default="all",
                    choices=["all", "enumerate", "fetch", "parse", "finalize",
                             "analyze"])
    ap.add_argument("--max-fetch", type=int, default=None,
                    help="cap downloads (smoke tests)")
    ap.add_argument("--link-file", default=None,
                    help="rebuilt CIK->CUSIP link CSV (default: carry-forward "
                         "cusip from the old file, marked provisional)")
    ap.add_argument("--allow-incomplete", action="store_true")
    ap.add_argument("--no-api-fallback", action="store_true")
    args = ap.parse_args(argv)

    enum = enumerate_initials()
    print(f"enumerate: {len(enum)} initial 13Ds across {len(QUARTERS)} quarters")
    if args.stage == "enumerate":
        return 0

    if args.stage in ("all", "fetch"):
        failures = fetch_all(enum, max_fetch=args.max_fetch)
        if failures and not args.allow_incomplete:
            print(f"WARNING: {len(failures)} fetch failures; re-run to resume",
                  file=sys.stderr)
        if args.stage == "fetch":
            return 0 if not failures else 1

    link_source = ("provisional: cusip carried forward from old-parser file"
                   if not args.link_file else
                   f"rebuilt link file {args.link_file}")

    if args.stage in ("all", "parse", "finalize"):
        new = parse_all(enum, use_api_fallback=not args.no_api_fallback)
        if args.stage == "parse":
            cols = ["accession", "quarter", "event", "pct_of_class", "accepted"]
            print(new[cols].head(20).to_string())
            return 0
        finalized = finalize(new, allow_incomplete=args.allow_incomplete
                             or args.max_fetch is not None)
        if args.stage == "finalize":
            return 0
    else:  # analyze standalone: read the canonical file written by finalize
        finalized = pd.read_json(OLD_PATH, lines=True)

    if args.link_file:
        link = _load_link_file(args.link_file)
        finalized = finalized.copy()
        finalized["cusip"] = finalized["subject_cik"].map(
            lambda c: link.get(str(int(c))) if pd.notna(c) else None)
    analyze(finalized, link_source)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
