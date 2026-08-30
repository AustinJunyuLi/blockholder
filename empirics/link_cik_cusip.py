"""Rebuild the CIK -> CUSIP -> PERMNO link (empirics_v4 SPEC section 11, row 11).

The original Fact-2 linking code was never committed (SPEC section 13 item 3);
this is the free rebuild route: EDGAR company-submissions API + CRSP
``HdrCUSIP``, no WRDS.

Method
------
1. Subject CIKs come from ``empirics/data/fact2_parsed.jsonl`` (read at run
   time; deduplicated). The file also carries reusable cover-page CUSIPs for
   ~2.4k CIKs -- used here ONLY as an independent validation set, never as a
   join key.
2. For each subject CIK, fetch the company-submissions API document
   ``https://data.sec.gov/submissions/CIK{10-digit}.json`` (throttled via
   ``empirics.edgar_fetch.fetch``, cached under ``empirics/data/submissions/``)
   and extract ``name``/``tickers``/``exchanges``/``sic``. The document does
   NOT carry CUSIPs; the join key to CRSP is the ticker.
3. Fetch ``https://www.sec.gov/files/company_tickers.json`` once
   (ticker -> CIK map) for the reverse direction and the name fallback.
4. Build a PERMNO-level identifying table from the on-disk CRSP daily
   snapshot (last-observed Ticker/HdrCUSIP/CUSIP/PERMCO/exchange plus the
   first/last trading dates). The snapshot's header fields are current-only:
   PERMNOs that delisted before the pull date carry no Ticker/ShareType
   (PrimaryExch 'X'), so the ticker route can only match securities listed at
   pull time; delisted targets land in ``unmatched`` and are quantified via
   the validation CUSIPs.
5. Join CIK -> PERMNO on normalised tickers (uppercase, non-alphanumeric
   stripped) against CRSP US-incorporated common stock
   (``SecurityType == 'EQTY'``, ``ShareType == 'NS'``, ``USIncFlg == 'Y'``).
   A candidate PERMNO must have been listed at the CIK's first in-window 13D
   filing. Ticker collisions (share classes, reuse) that survive the
   date-range filter are reported in ``ambiguous_permnos`` and left unmatched
   -- never silently picked. If the submissions document lists no ticker, a
   normalised-name fallback against ``company_tickers.json`` titles tries to
   recover a ticker first (``match_route == 'name_fallback'``).

Outputs (committed, ``empirics/output/``)
-----------------------------------------
- ``cik_cusip_link.csv`` -- one row per subject CIK: permno, permco, cusip9
  (CRSP ``HdrCUSIP``, the 8-character header CUSIP), ticker, match_route,
  matched flag, ambiguous_permnos.
- ``cik_cusip_link_disagreements.csv`` -- CIKs where the rebuilt PERMNO's
  CUSIP disagrees with the reusable cover-page CUSIP.
- ``permno_cik_map.csv`` -- reverse map: every CRSP US common-stock PERMNO
  whose last ticker maps to a CIK via ``company_tickers.json`` (this is what
  the BID12 coder needs for controls).

SEC fair access: all bulk pulls run under the host-wide lock
``/tmp/sec_edgar_bulk.lock`` (another agent may be downloading filings);
every response is cached so re-runs are free and deterministic.

Usage: ``.venv/bin/python -m empirics.link_cik_cusip``
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
import random
import re
import time
from typing import Iterator, Optional

import pandas as pd

from empirics.edgar_fetch import DATA_DIR, fetch

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(HERE, "output")
SUBMISSIONS_DIR = os.path.join(DATA_DIR, "submissions")
COMPANY_TICKERS_PATH = os.path.join(DATA_DIR, "company_tickers.json")
FACT2_JSONL = os.path.join(DATA_DIR, "fact2_parsed.jsonl")
CRSP_DAILY = os.path.join(DATA_DIR, "crsp_daily.csv")

SEC_BULK_LOCK = "/tmp/sec_edgar_bulk.lock"
LOCK_POLL_SECONDS = 60

# The jsonl covers initial 13Ds filed 2022Q1-2025Q4; used as the fallback era
# when a CIK has no usable filing dates.
ERA_START = "2022-01-01"
ERA_END = "2025-12-31"

COMPANY_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"
# Head fields (name/tickers/exchanges/sic) sit in the first ~1 KB, ahead of
# the potentially huge filings.recent array; 2 MB covers all but the most
# prolific filers, and the regex fallback parses the head of truncated bodies.
SUBMISSIONS_MAX_BYTES = 2_000_000

CRSP_USECOLS = [
    "PERMNO", "PERMCO", "HdrCUSIP", "CUSIP", "Ticker", "PrimaryExch",
    "ShareType", "USIncFlg", "SecurityType", "DlyCalDt",
]
CRSP_CATEGORY_COLS = [
    "HdrCUSIP", "CUSIP", "Ticker", "PrimaryExch", "ShareType", "USIncFlg",
    "SecurityType", "DlyCalDt",
]

SPOT_CHECK_N = 300
SPOT_CHECK_SEED = 20260830

_NAME_SUFFIXES = {
    "INC", "CORP", "CORPORATION", "CO", "COMPANY", "LLC", "LLP", "LP",
    "LTD", "PLC", "NV", "SA", "AG", "SE", "GROUP", "HOLDINGS",
}


# -- SEC fair-access lock -----------------------------------------------------

@contextlib.contextmanager
def sec_bulk_lock(poll_seconds: int = LOCK_POLL_SECONDS) -> Iterator[None]:
    """Host-wide mutex for bulk EDGAR pulls (mkdir; poll while held)."""
    waited = 0
    while True:
        try:
            os.mkdir(SEC_BULK_LOCK)
            break
        except FileExistsError:
            if waited % 600 == 0:
                print(f"  ... waiting for {SEC_BULK_LOCK} "
                      f"(held by another pull; polled {waited}s)")
            time.sleep(poll_seconds)
            waited += poll_seconds
    try:
        yield
    finally:
        os.rmdir(SEC_BULK_LOCK)


def fetch_many_locked(missing: list[tuple[str, str, int]]) -> None:
    """Fetch ``(url, cache_path, max_bytes)`` triples; caller holds the lock."""
    for i, (url, path, max_bytes) in enumerate(missing, 1):
        data = fetch(url, max_bytes=max_bytes)
        tmp = path + ".tmp"
        with open(tmp, "wb") as fh:
            fh.write(data)
        os.replace(tmp, path)
        if i % 250 == 0:
            print(f"    {i}/{len(missing)} fetched")


def ensure_cached(requests: dict[str, tuple[str, str]],
                  max_bytes: int = SUBMISSIONS_MAX_BYTES) -> None:
    """Fetch any missing cache files under one lock hold.

    ``requests`` maps a label to ``(url, cache_path)``; existing files are
    skipped so re-runs only pull what is missing.
    """
    missing = [(url, path, max_bytes) for url, path in requests.values()
               if not os.path.exists(path)]
    if not missing:
        return
    print(f"  fetching {len(missing)} missing EDGAR documents "
          f"(of {len(requests)} requested)")
    with sec_bulk_lock():
        fetch_many_locked(missing)


# -- inputs -------------------------------------------------------------------

def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_subject_ciks(jsonl_path: str = FACT2_JSONL) -> pd.DataFrame:
    """Deduplicated subject-CIK table from the current fact2_parsed.jsonl.

    Returns one row per subject_cik with the first non-null reusable CUSIP
    and subject name (earliest filing first, deterministic) plus the span of
    in-window filing dates used for date-range disambiguation.
    """
    rows: list[dict] = []
    with open(jsonl_path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    df = pd.DataFrame(rows)
    # tolerate a re-parsed jsonl landing mid-session with missing columns
    for col in ("subject_cik", "cusip", "subject_name", "filed", "date_filed"):
        if col not in df:
            df[col] = None
    df = df[df["subject_cik"].notna()].copy()
    df["subject_cik"] = df["subject_cik"].astype(str).str.strip()
    df = df[df["subject_cik"] != ""]
    df["filed_eff"] = df["filed"].fillna(df["date_filed"]).astype(str)
    df = df.sort_values(["subject_cik", "filed_eff"], kind="stable")

    def _first_non_null(s: pd.Series) -> Optional[str]:
        s = s.dropna()
        return str(s.iloc[0]) if len(s) else None

    out = df.groupby("subject_cik", sort=True).agg(
        old_cusip=("cusip", _first_non_null),
        subject_name=("subject_name", _first_non_null),
        filed_min=("filed_eff", "min"),
        filed_max=("filed_eff", "max"),
        n_filings=("filed_eff", "size"),
    ).reset_index()
    return out


def build_permno_table(crsp_path: str = CRSP_DAILY) -> pd.DataFrame:
    """PERMNO-level identifying table from the CRSP daily snapshot.

    Identity fields are last-observed values; ``first_date``/``last_date``
    bound the PERMNO's listed span in the snapshot. Note the snapshot's
    header is current-only: PERMNOs delisted before the pull date carry no
    Ticker/ShareType/SecurityType and PrimaryExch 'X'.
    """
    dtypes = {c: "category" for c in CRSP_CATEGORY_COLS}
    df = pd.read_csv(crsp_path, usecols=CRSP_USECOLS, dtype=dtypes)
    df = df.sort_values(["PERMNO", "DlyCalDt"], kind="stable")
    g = df.groupby("PERMNO", observed=True)
    last = g.tail(1).set_index("PERMNO")
    out = pd.DataFrame({
        "permco": last["PERMCO"].astype("int64"),
        "hdrcusip": last["HdrCUSIP"].astype(str),
        "cusip": last["CUSIP"].astype(str),
        "ticker": last["Ticker"].astype(str),
        "primary_exch": last["PrimaryExch"].astype(str),
        "share_type": last["ShareType"].astype(str),
        "security_type": last["SecurityType"].astype(str),
        "us_inc": last["USIncFlg"].astype(str),
        "first_date": g["DlyCalDt"].first().astype(str),
        "last_date": g["DlyCalDt"].last().astype(str),
        "n_days": g.size(),
    })
    out.index.name = "permno"
    # 'nan' strings from astype(str) on missing categoricals -> empty
    for col in ("hdrcusip", "cusip", "ticker", "primary_exch", "share_type",
                "security_type", "us_inc"):
        out.loc[out[col].isin(["nan", "NaN", "None"]), col] = ""
    return out.reset_index()


def common_us_universe(permno_df: pd.DataFrame) -> pd.DataFrame:
    """US-incorporated common stock per the SPEC section 8.2 filter."""
    mask = ((permno_df["security_type"] == "EQTY")
            & (permno_df["share_type"] == "NS")
            & (permno_df["us_inc"] == "Y"))
    return permno_df[mask].copy()


# -- normalisation ------------------------------------------------------------

def norm_ticker(raw: object) -> str:
    """Uppercase, stripped, non-alphanumerics removed (BRK-B/BRK.B -> BRKB)."""
    if raw is None:
        return ""
    return re.sub(r"[^A-Z0-9]", "", str(raw).upper().strip())


def norm_name(raw: object) -> str:
    """Uppercase, punctuation removed, trailing entity suffixes dropped."""
    if raw is None:
        return ""
    txt = re.sub(r"[^A-Z0-9 ]", " ", str(raw).upper())
    tokens = [t for t in txt.split() if t]
    while tokens and tokens[-1] in _NAME_SUFFIXES:
        tokens.pop()
    return " ".join(tokens)


# -- EDGAR submissions API ----------------------------------------------------

_RE_JSON_STR = r'"((?:[^"\\]|\\.)*)"'


def parse_submissions(raw: bytes) -> dict:
    """Extract name/tickers/exchanges/sic from a submissions API document.

    Falls back to head-of-document regexes when the cached body is truncated
    mid-JSON (the fields we need precede the large filings.recent array).
    """
    text = raw.decode("utf-8", errors="replace")
    try:
        j = json.loads(text)
        return {
            "cik": j.get("cik"),
            "name": j.get("name"),
            "sic": j.get("sic"),
            "tickers": [str(t) for t in (j.get("tickers") or [])],
            "exchanges": [str(e) for e in (j.get("exchanges") or [])],
        }
    except json.JSONDecodeError:
        pass

    def _str_field(key: str) -> Optional[str]:
        m = re.search(rf'"{key}"\s*:\s*{_RE_JSON_STR}', text)
        return m.group(1) if m else None

    def _list_field(key: str) -> list[str]:
        m = re.search(rf'"{key}"\s*:\s*\[(.*?)\]', text, re.S)
        if not m:
            return []
        return re.findall(_RE_JSON_STR, m.group(1))

    cik_raw = re.search(r'"cik"\s*:\s*"?(\d+)"?', text)
    return {
        "cik": cik_raw.group(1) if cik_raw else None,
        "name": _str_field("name"),
        "sic": _str_field("sic"),
        "tickers": _list_field("tickers"),
        "exchanges": _list_field("exchanges"),
    }


def submissions_cache_path(cik: str) -> str:
    return os.path.join(SUBMISSIONS_DIR, f"CIK{int(cik):010d}.json")


def fetch_submissions(ciks: list[str]) -> None:
    """Cache the submissions API document for each CIK (throttled, locked)."""
    os.makedirs(SUBMISSIONS_DIR, exist_ok=True)
    requests = {
        cik: (SUBMISSIONS_URL.format(cik=int(cik)), submissions_cache_path(cik))
        for cik in ciks
    }
    ensure_cached(requests)


def load_submissions(ciks: list[str]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for cik in ciks:
        path = submissions_cache_path(cik)
        if os.path.exists(path):
            with open(path, "rb") as fh:
                out[cik] = parse_submissions(fh.read())
    return out


def load_company_tickers() -> pd.DataFrame:
    """Load the cached company_tickers.json (ticker -> CIK map)."""
    with open(COMPANY_TICKERS_PATH, "r", encoding="utf-8") as fh:
        j = json.load(fh)
    df = pd.DataFrame([
        {"cik": str(v["cik_str"]), "ticker": str(v["ticker"]),
         "title": str(v["title"])}
        for v in j.values()
    ])
    df["norm_ticker"] = df["ticker"].map(norm_ticker)
    df["norm_name"] = df["title"].map(norm_name)
    return df


def fetch_company_tickers() -> pd.DataFrame:
    """Cache (if needed) and load company_tickers.json."""
    os.makedirs(DATA_DIR, exist_ok=True)
    ensure_cached({"company_tickers": (COMPANY_TICKERS_URL,
                                       COMPANY_TICKERS_PATH)},
                  max_bytes=20_000_000)
    return load_company_tickers()


# -- matching -----------------------------------------------------------------

def match_subjects(subjects: pd.DataFrame, edgar: dict[str, dict],
                   permno_common: pd.DataFrame,
                   company_tickers: pd.DataFrame) -> pd.DataFrame:
    """Join subject CIKs to PERMNOs via tickers (with name fallback).

    A candidate PERMNO must have been listed at the CIK's first in-window
    13D filing (``first_date <= filed_min <= last_date``). Collisions that
    survive the date filter are reported, never silently picked.
    """
    permno_common = permno_common.copy()
    permno_common["norm_ticker"] = permno_common["ticker"].map(norm_ticker)
    by_ticker: dict[str, pd.DataFrame] = {}
    for nt, sub in permno_common[permno_common["norm_ticker"] != ""].groupby(
            "norm_ticker"):
        by_ticker[nt] = sub

    tickers_by_name: dict[str, list[str]] = {}
    for nn, sub in company_tickers[company_tickers["norm_name"] != ""].groupby(
            "norm_name"):
        tickers_by_name[nn] = sorted(sub["norm_ticker"].unique())

    records = []
    for row in subjects.itertuples(index=False):
        cik = row.subject_cik
        info = edgar.get(cik, {})
        filed_min = row.filed_min
        if not isinstance(filed_min, str) or not filed_min:
            filed_min = ERA_START
        edgar_tickers = sorted({norm_ticker(t) for t in info.get("tickers", [])
                                if norm_ticker(t)})
        route = "ticker"
        tickers_tried = list(edgar_tickers)
        if not tickers_tried:
            # name fallback: recover a ticker from company_tickers titles
            names = {norm_name(info.get("name")),
                     norm_name(row.subject_name)} - {""}
            recovered: set[str] = set()
            for nn in names:
                recovered.update(tickers_by_name.get(nn, []))
            tickers_tried = sorted(recovered)
            route = "name_fallback"

        candidates: dict[int, pd.Series] = {}
        for nt in tickers_tried:
            for cand in by_ticker.get(nt, pd.DataFrame()).itertuples(
                    index=False):
                if cand.first_date <= filed_min <= cand.last_date:
                    candidates[cand.permno] = cand

        ambiguous = sorted(candidates)
        matched: Optional[pd.Series] = None
        if len(candidates) == 1:
            matched = next(iter(candidates.values()))
            route = route if route == "name_fallback" else "ticker_unique"
        elif len(candidates) > 1:
            route = ("ambiguous_name" if route == "name_fallback"
                     else "ambiguous_ticker")
        else:
            route = "unmatched" if route == "ticker" else "unmatched_name"

        records.append({
            "subject_cik": cik,
            "permno": matched.permno if matched is not None else pd.NA,
            "permco": matched.permco if matched is not None else pd.NA,
            "cusip9": matched.hdrcusip if matched is not None else "",
            "ticker": matched.ticker if matched is not None else "",
            "match_route": route,
            "matched": matched is not None,
            "ambiguous_permnos": ";".join(str(p) for p in ambiguous)
            if len(candidates) > 1 else "",
            "edgar_name": str(info.get("name") or ""),
            "edgar_tickers": ";".join(edgar_tickers),
            "edgar_sic": str(info.get("sic") or ""),
            "filed_min": row.filed_min,
            "filed_max": row.filed_max,
            "n_filings": row.n_filings,
        })
    out = pd.DataFrame.from_records(records)
    return out.sort_values("subject_cik", kind="stable",
                           key=lambda s: s.astype(int)).reset_index(drop=True)


# -- validation ---------------------------------------------------------------

def validate_against_old_cusips(link: pd.DataFrame,
                                subjects: pd.DataFrame) -> tuple[float, pd.DataFrame, dict]:
    """Compare the rebuilt link against the reusable cover-page CUSIPs.

    The old values are never a join key -- only an independent check. A
    9-character old CUSIP agrees when its 8-character prefix equals the
    PERMNO's HdrCUSIP (or last CUSIP prefix).
    """
    merged = link.merge(subjects[["subject_cik", "old_cusip"]],
                        on="subject_cik", how="left")
    old_len = merged["old_cusip"].str.len()
    has_old = merged["old_cusip"].notna() & (old_len.fillna(0) >= 8)
    both = merged[has_old & merged["matched"]].copy()
    old8 = both["old_cusip"].str.upper().str[:8]
    agree = (old8 == both["cusip9"].str.upper().str[:8])
    stats = {
        "ciks_with_old_cusip": int(has_old.sum()),
        "matched_with_old_cusip": int(len(both)),
        "agree": int(agree.sum()),
        "agreement_rate": (float(agree.mean()) if len(both) else float("nan")),
    }
    disagreements = both[~agree][[
        "subject_cik", "old_cusip", "permno", "cusip9", "ticker",
        "match_route", "edgar_name",
    ]].rename(columns={"cusip9": "hdrcusip_linked"}).sort_values("subject_cik")
    return stats["agreement_rate"], disagreements, stats


# -- reverse map --------------------------------------------------------------

def build_reverse_map(permno_common: pd.DataFrame,
                      company_tickers: pd.DataFrame) -> pd.DataFrame:
    """Map every CRSP US common-stock PERMNO to a CIK via its last ticker."""
    by_ticker: dict[str, list[str]] = {}
    for nt, sub in company_tickers[company_tickers["norm_ticker"] != ""].groupby(
            "norm_ticker"):
        by_ticker[nt] = sorted({str(c) for c in sub["cik"]})

    records = []
    for row in permno_common.itertuples(index=False):
        nt = norm_ticker(row.ticker)
        ciks = by_ticker.get(nt, [])
        records.append({
            "permno": row.permno,
            "permco": row.permco,
            "hdrcusip": row.hdrcusip,
            "cusip": row.cusip,
            "ticker": row.ticker,
            "primary_exch": row.primary_exch,
            "first_date": row.first_date,
            "last_date": row.last_date,
            "cik": ciks[0] if len(ciks) == 1 else "",
            "map_route": "ticker" if len(ciks) == 1 else (
                "ambiguous_ticker" if ciks else "no_edgar_ticker"),
            "ambiguous_ciks": ";".join(ciks) if len(ciks) > 1 else "",
        })
    return pd.DataFrame.from_records(records).sort_values("permno").reset_index(
        drop=True)


# -- main ---------------------------------------------------------------------

def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(SUBMISSIONS_DIR, exist_ok=True)
    print("== inputs ==")
    jsonl_hash = sha256_of(FACT2_JSONL)
    subjects = load_subject_ciks(FACT2_JSONL)
    print(f"  fact2_parsed.jsonl sha256 {jsonl_hash[:16]}... "
          f"-> {len(subjects)} unique subject CIKs")

    print("== CRSP PERMNO table ==")
    permno_df = build_permno_table()
    permno_common = common_us_universe(permno_df)
    print(f"  {len(permno_df)} PERMNOs in snapshot; "
          f"{len(permno_common)} US common stock (EQTY/NS/Y)")

    print("== EDGAR fetch phase (single lock hold; cached re-runs free) ==")
    ciks = sorted(subjects["subject_cik"].tolist(), key=int)
    with sec_bulk_lock():
        if not os.path.exists(COMPANY_TICKERS_PATH):
            fetch_many_locked([(COMPANY_TICKERS_URL, COMPANY_TICKERS_PATH,
                                20_000_000)])
        company_tickers = load_company_tickers()
        print(f"  company_tickers.json: {len(company_tickers)} rows")

        # reverse map first so its spot-check CIKs join the same lock hold
        reverse_map = build_reverse_map(permno_common, company_tickers)
        mapped = reverse_map[reverse_map["cik"] != ""].reset_index(drop=True)
        idx = list(range(len(mapped)))
        random.Random(SPOT_CHECK_SEED).shuffle(idx)
        spot_sample = mapped.iloc[sorted(idx[: min(SPOT_CHECK_N, len(mapped))])]
        spot_ciks = sorted(spot_sample["cik"].unique(), key=int)

        todo = [
            (SUBMISSIONS_URL.format(cik=int(c)), submissions_cache_path(c),
             SUBMISSIONS_MAX_BYTES)
            for c in sorted(set(ciks) | set(spot_ciks), key=int)
            if not os.path.exists(submissions_cache_path(c))
        ]
        if todo:
            print(f"  fetching {len(todo)} submissions documents "
                  f"(~{len(todo) // 4 / 60:.0f} min at 4 req/s)")
            fetch_many_locked(todo)
        else:
            print("  all submissions documents already cached")
    edgar = load_submissions(ciks)
    print(f"  submissions documents cached for {len(edgar)}/{len(ciks)} "
          f"subject CIKs")

    print("== CIK -> PERMNO match ==")
    link = match_subjects(subjects, edgar, permno_common, company_tickers)
    route_counts = link["match_route"].value_counts().to_dict()
    print(f"  match routes: {route_counts}")

    print("== validation vs reusable CUSIPs ==")
    rate, disagreements, stats = validate_against_old_cusips(link, subjects)
    print(f"  {stats}")
    if stats["matched_with_old_cusip"] and rate < 0.95:
        print("  WARNING: agreement below 95% -- investigate the join before "
              "using this link downstream")
    # delisted diagnostic: old-CUSIP CIKs the ticker route cannot see
    merged = link.merge(subjects[["subject_cik", "old_cusip"]],
                        on="subject_cik", how="left")
    old8 = merged["old_cusip"].dropna()
    old8 = old8[old8.str.len() >= 8].str.upper().str[:8]
    unmatched_old = merged[~merged["matched"] & merged["old_cusip"].notna()]
    xstub_hdr = set(permno_df.loc[permno_df["primary_exch"] == "X",
                                  "hdrcusip"].str.upper())
    n_delisted_in_file = sum(
        str(c).upper()[:8] in xstub_hdr
        for c in unmatched_old["old_cusip"].dropna())
    print(f"  old-CUSIP CIKs unmatched by ticker route: "
          f"{len(unmatched_old)}; of these, HdrCUSIP present among "
          f"header-less (delisted) PERMNOs in snapshot: {n_delisted_in_file}")
    print(f"  distinct old CUSIP prefixes: {old8.nunique()}")

    print("== reverse map (PERMNO -> CIK) ==")
    n_mapped = int((reverse_map["cik"] != "").sum())
    print(f"  {n_mapped}/{len(reverse_map)} common-US PERMNOs mapped to a CIK "
          f"({n_mapped / len(reverse_map):.1%})")
    docs = load_submissions(spot_ciks)
    agree = checked = 0
    for row in spot_sample.itertuples(index=False):
        doc = docs.get(row.cik)
        if doc is None:
            continue
        checked += 1
        if norm_ticker(row.ticker) in {norm_ticker(t)
                                       for t in doc.get("tickers", [])}:
            agree += 1
    print(f"  spot-check vs submissions API: {agree}/{checked} agree "
          f"({agree / checked:.1%})" if checked else "  spot-check: none")

    link_path = os.path.join(OUTPUT_DIR, "cik_cusip_link.csv")
    dis_path = os.path.join(OUTPUT_DIR, "cik_cusip_link_disagreements.csv")
    rev_path = os.path.join(OUTPUT_DIR, "permno_cik_map.csv")
    link.to_csv(link_path, index=False)
    disagreements.to_csv(dis_path, index=False)
    reverse_map.to_csv(rev_path, index=False)
    print(f"  wrote {link_path} ({len(link)} rows)")
    print(f"  wrote {dis_path} ({len(disagreements)} rows)")
    print(f"  wrote {rev_path} ({len(reverse_map)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
