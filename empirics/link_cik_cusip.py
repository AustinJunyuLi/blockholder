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
   snapshot. The snapshot's identity fields are **time-varying, per row**:
   ``CUSIP``, ``Ticker``, ``ShareType`` and ``SecurityType`` change as the
   security is renamed, reverse-split or reincorporated, while ``HdrCUSIP``
   is the current header value carried on every row. So the table records
   both the last-observed row *and* the full observed history: every
   (PERMNO, normalised ticker) date span and every (PERMNO, CUSIP) date span.
   Delisted PERMNOs (``PrimaryExch == 'X'``, 3,407 in the 2021-2025 snapshot)
   keep their Ticker and CUSIP on the final row but carry **empty**
   ``ShareType``/``SecurityType``; a share-type filter read off the last row
   therefore silently excludes every security that left CRSP before the pull
   date -- 1,607 of which were US common stock while listed. Because SPEC
   section 2.3 filter 3 and section 8.2 evaluate the firm at its event window,
   not at snapshot end, the filter here is applied over the PERMNO's observed
   life (``ever`` NS / EQTY / US-incorporated), not to its last row.
5. Join CIK -> PERMNO on normalised tickers (uppercase, non-alphanumeric
   stripped) against CRSP US-incorporated common stock
   (``SecurityType == 'EQTY'``, ``ShareType == 'NS'``, ``USIncFlg == 'Y'``,
   any observation). The ticker is matched against the PERMNO's **whole
   ticker history**, not just its last ticker: 4,249 PERMNOs carry more than
   one ticker in the snapshot window, so a firm that renamed between the 13D
   and the pull date (Glatfelter GLT -> Magnera MAGN) is invisible to a
   last-ticker join. A candidate PERMNO must have been listed at the CIK's
   first in-window 13D filing. Where more than one PERMNO answers to the
   ticker, the tie is broken on the **ticker's own** date span -- ticker
   reuse across firms is real (PERMNO 25452 carried JCS, then PEGY, then
   SUNE) -- and only a tie that a single PERMNO wins is taken. Collisions
   that survive both filters are reported in ``ambiguous_permnos`` and left
   unmatched, never silently picked. If the submissions document lists no
   ticker, a normalised-name fallback against ``company_tickers.json`` titles
   tries to recover a ticker first (``match_route == 'name_fallback'``).

   Known, quantified limitation: ``company_tickers.json`` and the submissions
   API are current-only, so a firm that was acquired or delisted before the
   pull date usually carries no EDGAR ticker at all and cannot be reached by
   this route in either direction. The count is reported at every run and the
   affected CIKs are left ``unmatched``; the cover-page CUSIPs quantify the
   headroom but are never promoted to a join key.

Outputs (committed, ``empirics/output/``)
-----------------------------------------
- ``cik_cusip_link.csv`` -- one row per subject CIK: permno, permco, cusip9
  (CRSP ``HdrCUSIP``, the 8-character header CUSIP), ticker, match_route,
  matched flag, ambiguous_permnos.
- ``cik_cusip_link_disagreements.csv`` -- CIKs where the reusable cover-page
  CUSIP is absent from the matched PERMNO's **whole** observed CUSIP history,
  with a mechanical ``reason`` classification per row.

Validation
----------
The cover-page CUSIP is printed on the 13D as of the **filing date**; CRSP's
``HdrCUSIP`` is the issuer's identity as of the **snapshot pull date**. Those
are different vintages, and 1,800 PERMNOs change CUSIP inside the snapshot
window (reverse splits, renames, reincorporations), so comparing the two
measures drift, not linkage error. Agreement is therefore evaluated against
the PERMNO's observed CUSIP history (``CUSIP`` values union ``HdrCUSIP``).
The denominator is unchanged -- matched CIKs carrying a reusable cover-page
CUSIP -- and the old header-only rate is printed alongside at every run so
the two are directly comparable. Two stricter variants are reported and never
substituted for the gate: the date-consistent subset (the cover CUSIP was the
PERMNO's CUSIP on the filing date) and the header-only rate.
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
import sys
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
# Poll at 15s: peer lanes release the lock for ~20s gaps between holds, and
# a 60s poll kept missing them (a control-universe build starved 35+ min
# behind a bulk extraction on 2026-08-30). More polling never means more
# requests — it only improves the odds of catching a release gap.
LOCK_POLL_SECONDS = 15

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
    for col in ("subject_cik", "cusip", "subject_name", "filed", "date_filed",
                "filer_cik"):
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

    def _all_cusips(s: pd.Series) -> str:
        vals = sorted({str(v).strip().upper() for v in s.dropna()
                       if str(v).strip()})
        return ";".join(vals)

    # EDGAR header degeneracy: a handful of accessions name the same entity as
    # both SUBJECT COMPANY and FILED BY, so the subject CIK is not recoverable
    # from the header for them (verified on 0000104169-22-000040, whose header
    # names Walmart on both sides while the cover page carries Symbotic's
    # CUSIP). Faithfully parsed, not a parser defect -- flagged, never patched.
    df["self_filed"] = (df["filer_cik"].notna()
                        & (df["subject_cik"].astype(str).str.strip()
                           == df["filer_cik"].astype(str).str.strip()))

    out = df.groupby("subject_cik", sort=True).agg(
        old_cusip=("cusip", _first_non_null),
        old_cusips_all=("cusip", _all_cusips),
        subject_name=("subject_name", _first_non_null),
        filed_min=("filed_eff", "min"),
        filed_max=("filed_eff", "max"),
        n_filings=("filed_eff", "size"),
        n_self_filed=("self_filed", "sum"),
    ).reset_index()
    return out


_BLANKS = ("nan", "NaN", "None", "")


def _clean(series: pd.Series) -> pd.Series:
    """Categorical/object column -> str with the missing sentinels emptied."""
    s = series.astype(str)
    return s.where(~s.isin(_BLANKS), "")


class CrspIdentity:
    """Everything the link needs from one pass over the CRSP daily snapshot.

    ``permno_df``    one row per PERMNO: last-observed identity, the listed
                     span, and ``ever_ns``/``ever_eqty``/``ever_us`` flags
                     computed over the PERMNO's whole observed life.
    ``ticker_spans`` (permno, norm_ticker, t_first, t_last) -- the ticker
                     history the join runs against.
    ``cusip_spans``  (permno, cusip8, c_first, c_last) -- the CUSIP history
                     validation runs against.
    ``cusip_hist``   permno -> set of 8-character CUSIPs (``CUSIP`` values
                     union ``HdrCUSIP``).
    ``cusip_owner``  cusip8 -> set of PERMNOs that ever carried it, used to
                     classify residual disagreements.
    """

    def __init__(self, permno_df: pd.DataFrame, ticker_spans: pd.DataFrame,
                 cusip_spans: pd.DataFrame) -> None:
        self.permno_df = permno_df
        self.ticker_spans = ticker_spans
        self.cusip_spans = cusip_spans
        self.cusip_hist: dict[int, set[str]] = {}
        self.cusip_owner: dict[str, set[int]] = {}
        for p, c in zip(cusip_spans["permno"], cusip_spans["cusip8"]):
            self.cusip_hist.setdefault(int(p), set()).add(c)
            self.cusip_owner.setdefault(c, set()).add(int(p))


def build_crsp_identity(crsp_path: str = CRSP_DAILY) -> CrspIdentity:
    """Read the CRSP daily snapshot once; return last-observed + history.

    CRSP's identity columns are per-row and time-varying. Reading them off
    the final row alone (the previous behaviour) both misses renamed tickers
    and, because delisted PERMNOs carry empty ShareType/SecurityType on that
    final row, drops every security that left CRSP before the pull date.
    """
    dtypes = {c: "category" for c in CRSP_CATEGORY_COLS}
    df = pd.read_csv(crsp_path, usecols=CRSP_USECOLS, dtype=dtypes)
    df = df.sort_values(["PERMNO", "DlyCalDt"], kind="stable")
    g = df.groupby("PERMNO", observed=True)
    last = g.tail(1).set_index("PERMNO")

    out = pd.DataFrame({
        "permco": last["PERMCO"].astype("int64"),
        "hdrcusip": _clean(last["HdrCUSIP"]),
        "cusip": _clean(last["CUSIP"]),
        "ticker": _clean(last["Ticker"]),
        "primary_exch": _clean(last["PrimaryExch"]),
        "share_type": _clean(last["ShareType"]),
        "security_type": _clean(last["SecurityType"]),
        "us_inc": _clean(last["USIncFlg"]),
        "first_date": g["DlyCalDt"].first().astype(str),
        "last_date": g["DlyCalDt"].last().astype(str),
        "n_days": g.size(),
    })
    out.index.name = "permno"

    # ever-flags: the SPEC filter evaluated over the PERMNO's observed life
    flags = df[["PERMNO", "ShareType", "SecurityType", "USIncFlg"]].astype(
        {"ShareType": str, "SecurityType": str, "USIncFlg": str}
    ).drop_duplicates()
    for col, want, name in (("ShareType", "NS", "ever_ns"),
                            ("SecurityType", "EQTY", "ever_eqty"),
                            ("USIncFlg", "Y", "ever_us")):
        hit = set(flags.loc[flags[col] == want, "PERMNO"])
        out[name] = [p in hit for p in out.index]

    # CRSP marks a delisted security with PrimaryExch 'X' on its final rows;
    # that is the still-listed guard the reverse map needs.
    out["still_listed"] = out["primary_exch"] != "X"

    # ticker history: normalise on the (small) set of distinct raw tickers
    tk = df[["PERMNO", "Ticker", "DlyCalDt"]].copy()
    tk["Ticker"] = _clean(tk["Ticker"])
    tk = tk[tk["Ticker"] != ""]
    tmap = {t: norm_ticker(t) for t in tk["Ticker"].unique()}
    tk["norm_ticker"] = tk["Ticker"].map(tmap)
    tk = tk[tk["norm_ticker"] != ""]
    tk["DlyCalDt"] = tk["DlyCalDt"].astype(str)
    ticker_spans = (tk.groupby(["PERMNO", "norm_ticker"], observed=True)
                    ["DlyCalDt"].agg(["min", "max"]).reset_index()
                    .rename(columns={"PERMNO": "permno", "min": "t_first",
                                     "max": "t_last"}))

    # CUSIP history: the time-varying CUSIP column union the header CUSIP
    frames = []
    for col in ("CUSIP", "HdrCUSIP"):
        part = df[["PERMNO", col, "DlyCalDt"]].copy()
        part[col] = _clean(part[col])
        part = part[part[col] != ""]
        part["DlyCalDt"] = part["DlyCalDt"].astype(str)
        part = (part.groupby(["PERMNO", col], observed=True)["DlyCalDt"]
                .agg(["min", "max"]).reset_index()
                .rename(columns={"PERMNO": "permno", col: "cusip8",
                                 "min": "c_first", "max": "c_last"}))
        frames.append(part)
    cusip_spans = pd.concat(frames, ignore_index=True)
    cusip_spans["cusip8"] = cusip_spans["cusip8"].str.upper().str[:8]
    cusip_spans = (cusip_spans.groupby(["permno", "cusip8"], as_index=False)
                   .agg(c_first=("c_first", "min"), c_last=("c_last", "max")))

    return CrspIdentity(out.reset_index(), ticker_spans, cusip_spans)


def build_permno_table(crsp_path: str = CRSP_DAILY) -> pd.DataFrame:
    """PERMNO-level identifying table (last-observed identity + ever-flags).

    Kept as the module's public entry point for callers that need only the
    table (``empirics.build_control_universe``); it is a thin wrapper over
    :func:`build_crsp_identity`.
    """
    return build_crsp_identity(crsp_path).permno_df


def common_us_universe(permno_df: pd.DataFrame) -> pd.DataFrame:
    """US-incorporated common stock per the SPEC section 8.2 filter.

    Evaluated over the PERMNO's observed life, not its last row: SPEC 2.3
    filter 3 and 8.2 qualify the firm at its event window, and CRSP blanks
    ShareType/SecurityType once a security delists, so a last-row test
    excludes every firm that was acquired or delisted before the pull date --
    exactly the firms a takeover study must keep.
    """
    if "ever_ns" in permno_df.columns:
        mask = (permno_df["ever_eqty"] & permno_df["ever_ns"]
                & permno_df["ever_us"])
    else:  # table built by an older caller: fall back to last-row identity
        mask = ((permno_df["security_type"] == "EQTY")
                & (permno_df["share_type"] == "NS")
                & (permno_df["us_inc"] == "Y"))
    return permno_df[mask].copy()


# -- normalisation ------------------------------------------------------------

def norm_ticker(raw: object) -> str:
    """Uppercase, stripped, non-alphanumerics removed (BRK-B/BRK.B -> BRKB).

    A **missing** ticker must normalise to the empty string, and the guard is
    load-bearing rather than defensive. CRSP blanks the ticker when a security
    delists; pandas reads a blank as float NaN; ``str(nan).upper()`` is
    ``"NAN"``; and NAN is a real NYSE ticker, the Nuveen New York Quality
    Municipal Income Fund (CIK 1074769). Without this guard every delisted
    no-ticker PERMNO mapped to that one fund through the ``ticker_delisted``
    route -- 1,607 of them in the 2026-08-30 snapshot, found 2026-08-30 while
    tracing blank SIC codes in the control pool.
    """
    if raw is None:
        return ""
    try:
        if pd.isna(raw):
            return ""
    except (TypeError, ValueError):      # arrays and other non-scalars
        pass
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
                   company_tickers: pd.DataFrame,
                   ticker_spans: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    """Join subject CIKs to PERMNOs via tickers (with name fallback).

    The ticker is matched against the PERMNO's whole observed ticker history
    (``ticker_spans``), so a firm renamed between its 13D and the CRSP pull
    date still resolves. A candidate PERMNO must have been listed at the
    CIK's first in-window 13D filing (``first_date <= filed_min <=
    last_date``). Where several PERMNOs answer to the same ticker, the tie is
    broken on the *ticker's own* span -- ticker reuse across firms is real --
    and only a tie a single PERMNO wins is taken (``ticker_span``).
    Collisions that survive both filters are reported, never silently picked.

    ``ticker_spans`` is optional so the last-ticker behaviour remains
    available; passing it is what the committed pipeline does.
    """
    permno_common = permno_common.copy()
    ident = permno_common.set_index("permno")

    # ticker -> [(permno, t_first, t_last)] over the whole observed history,
    # restricted to the US-common universe
    by_ticker: dict[str, list[tuple[int, str, str]]] = {}
    if ticker_spans is not None:
        keep = set(permno_common["permno"])
        for p, nt, tf, tl in zip(ticker_spans["permno"],
                                 ticker_spans["norm_ticker"],
                                 ticker_spans["t_first"],
                                 ticker_spans["t_last"]):
            if p in keep and nt:
                by_ticker.setdefault(nt, []).append((int(p), tf, tl))
    else:
        for row in permno_common.itertuples(index=False):
            nt = norm_ticker(row.ticker)
            if nt:
                by_ticker.setdefault(nt, []).append(
                    (int(row.permno), row.first_date, row.last_date))

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

        # listed at the first in-window filing; note which candidates also
        # carried the matching ticker on that date
        candidates: dict[int, bool] = {}
        for nt in tickers_tried:
            for permno, t_first, t_last in by_ticker.get(nt, ()):
                rec = ident.loc[permno]
                if not (rec.first_date <= filed_min <= rec.last_date):
                    continue
                on_date = t_first <= filed_min <= t_last
                candidates[permno] = candidates.get(permno, False) or on_date

        ambiguous = sorted(candidates)
        matched: Optional[int] = None
        if len(candidates) == 1:
            matched = ambiguous[0]
            route = route if route == "name_fallback" else "ticker_unique"
        elif len(candidates) > 1:
            on_date = [p for p, ok in candidates.items() if ok]
            if len(on_date) == 1:
                matched = on_date[0]
                route = ("name_fallback_span" if route == "name_fallback"
                         else "ticker_span")
            else:
                route = ("ambiguous_name" if route == "name_fallback"
                         else "ambiguous_ticker")
        else:
            route = "unmatched" if route == "ticker" else "unmatched_name"

        rec = ident.loc[matched] if matched is not None else None
        records.append({
            "subject_cik": cik,
            "permno": matched if matched is not None else pd.NA,
            "permco": rec.permco if rec is not None else pd.NA,
            "cusip9": rec.hdrcusip if rec is not None else "",
            "ticker": rec.ticker if rec is not None else "",
            "still_listed": bool(rec.still_listed) if rec is not None
            and "still_listed" in permno_common.columns else pd.NA,
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

def classify_disagreement(old8: str, permno: int, hdr8: str, filed_min: str,
                          crsp: "CrspIdentity", n_self_filed: int) -> str:
    """Mechanical reason for a cover-page CUSIP absent from the PERMNO history.

    Classification only -- no row is rescued into agreement by any branch.
    """
    hist = crsp.cusip_hist.get(int(permno), set())
    owners = crsp.cusip_owner.get(old8, set())
    if len(old8) >= 8 and not old8[6:8].isdigit():
        # a letter in the issue position is a debt/derivative line, not the
        # common-stock CUSIP CRSP carries (e.g. Coherent 902104AB4)
        return "non_equity_cusip_line"
    if hist and old8[:6] in {c[:6] for c in hist} and old8[6:8] not in {
            c[6:8] for c in hist}:
        return "same_issuer_different_issue"
    shifted = {("0" + c)[:8] for c in hist} | {c[1:] + "0" for c in hist}
    if old8 in shifted:
        return "leading_zero_shift_parse_artifact"
    if owners and int(permno) not in owners:
        if n_self_filed:
            return "subject_filer_header_collapse"
        return "cusip_owned_by_other_permno"
    if not owners:
        return "cusip_absent_from_crsp_window"
    return "unclassified"


def validate_against_old_cusips(
        link: pd.DataFrame, subjects: pd.DataFrame,
        crsp: Optional["CrspIdentity"] = None
) -> tuple[float, pd.DataFrame, dict]:
    """Compare the rebuilt link against the reusable cover-page CUSIPs.

    The old values are never a join key -- only an independent check.

    The cover-page CUSIP is the issuer's identity **on the filing date**; the
    PERMNO's ``HdrCUSIP`` is its identity **on the CRSP pull date**. Agreement
    is therefore evaluated against the PERMNO's whole observed CUSIP history.
    The denominator is exactly the one the header-only rule used -- matched
    CIKs carrying a reusable cover-page CUSIP -- and that header-only rate is
    reported alongside so the two are directly comparable. Where ``crsp`` is
    not supplied the function degrades to the header-only rule.
    """
    cols = ["subject_cik", "old_cusip", "old_cusips_all", "n_self_filed"]
    cols = [c for c in cols if c in subjects.columns]
    merged = link.merge(subjects[cols], on="subject_cik", how="left")
    old_len = merged["old_cusip"].str.len()
    has_old = merged["old_cusip"].notna() & (old_len.fillna(0) >= 8)
    both = merged[has_old & merged["matched"]].copy()
    old8 = both["old_cusip"].str.upper().str[:8]
    hdr8 = both["cusip9"].str.upper().str[:8]

    agree_header = (old8 == hdr8)
    if crsp is None:
        agree = agree_header
        reasons = pd.Series("", index=both.index)
        date_ok = pd.Series(False, index=both.index)
        agree_any = agree_header
    else:
        permnos = both["permno"].astype("int64")
        agree = pd.Series(
            [o in crsp.cusip_hist.get(int(p), set())
             for o, p in zip(old8, permnos)], index=both.index)
        # stricter variant: the cover CUSIP was the PERMNO's CUSIP that day
        spans: dict[tuple[int, str], tuple[str, str]] = {
            (int(p), c): (f, l) for p, c, f, l in zip(
                crsp.cusip_spans["permno"], crsp.cusip_spans["cusip8"],
                crsp.cusip_spans["c_first"], crsp.cusip_spans["c_last"])}
        date_ok = pd.Series(
            [(lambda s: bool(s) and s[0] <= str(fm) <= s[1])(
                spans.get((int(p), o)))
             for o, p, fm in zip(old8, permnos, both["filed_min"])],
            index=both.index)
        # secondary variant: ANY cover-page CUSIP this CIK ever printed
        agree_any = pd.Series(
            [bool({c.upper()[:8] for c in str(a).split(";") if c}
                  & crsp.cusip_hist.get(int(p), set()))
             for a, p in zip(both.get("old_cusips_all", ""), permnos)],
            index=both.index) if "old_cusips_all" in both.columns else agree
        reasons = pd.Series([
            "" if ok else classify_disagreement(
                o, int(p), h, str(fm), crsp, int(ns or 0))
            for ok, o, p, h, fm, ns in zip(
                agree, old8, permnos, hdr8, both["filed_min"],
                both.get("n_self_filed", pd.Series(0, index=both.index)))
        ], index=both.index)

    stats = {
        "ciks_with_old_cusip": int(has_old.sum()),
        "matched_with_old_cusip": int(len(both)),
        "agree": int(agree.sum()),
        "agreement_rate": (float(agree.mean()) if len(both) else float("nan")),
        "agreement_rate_header_only": (float(agree_header.mean())
                                       if len(both) else float("nan")),
        "agreement_rate_date_consistent": (float(date_ok.mean())
                                           if len(both) else float("nan")),
        "agreement_rate_any_cover_cusip": (float(agree_any.mean())
                                           if len(both) else float("nan")),
    }
    both["reason"] = reasons
    disagreements = both[~agree][[
        "subject_cik", "old_cusip", "permno", "cusip9", "ticker",
        "match_route", "edgar_name", "reason",
    ]].rename(columns={"cusip9": "hdrcusip_linked"}).sort_values("subject_cik")
    stats["disagreement_reasons"] = (
        disagreements["reason"].value_counts().to_dict())
    return stats["agreement_rate"], disagreements, stats


# -- reverse map --------------------------------------------------------------

def build_reverse_map(permno_common: pd.DataFrame,
                      company_tickers: pd.DataFrame) -> pd.DataFrame:
    """Map every CRSP US common-stock PERMNO to a CIK via its last ticker.

    ``company_tickers.json`` is **current-only**, so for a PERMNO that already
    delisted the ticker may since have been reassigned to a live registrant --
    mapping it would hand the BID12 coder a different company's CIK. A
    delisted PERMNO is therefore mapped only when no still-listed PERMNO
    claims the same ticker, and the route is labelled ``ticker_delisted`` so
    the survivorship exposure is visible downstream rather than silent.
    """
    by_ticker: dict[str, list[str]] = {}
    for nt, sub in company_tickers[company_tickers["norm_ticker"] != ""].groupby(
            "norm_ticker"):
        by_ticker[nt] = sorted({str(c) for c in sub["cik"]})

    has_still_listed = "still_listed" in permno_common.columns
    live_tickers: set[str] = set()
    if has_still_listed:
        live_tickers = {norm_ticker(t) for t, s
                        in zip(permno_common["ticker"],
                               permno_common["still_listed"]) if s}
        live_tickers.discard("")

    records = []
    for row in permno_common.itertuples(index=False):
        nt = norm_ticker(row.ticker)
        ciks = by_ticker.get(nt, [])
        listed = bool(getattr(row, "still_listed", True))
        if len(ciks) != 1:
            cik, route = "", ("ambiguous_ticker" if ciks else "no_edgar_ticker")
        elif listed or not has_still_listed:
            cik, route = ciks[0], "ticker"
        elif nt in live_tickers:
            # the ticker now belongs to a live security: unsafe to map
            cik, route = "", "delisted_ticker_reused"
        else:
            cik, route = ciks[0], "ticker_delisted"
        records.append({
            "permno": row.permno,
            "permco": row.permco,
            "hdrcusip": row.hdrcusip,
            "cusip": row.cusip,
            "ticker": row.ticker,
            "primary_exch": row.primary_exch,
            "first_date": row.first_date,
            "last_date": row.last_date,
            "still_listed": listed,
            "cik": cik,
            "map_route": route,
            "ambiguous_ciks": ";".join(ciks) if len(ciks) > 1 else "",
        })
    return pd.DataFrame.from_records(records).sort_values("permno").reset_index(
        drop=True)


# -- main ---------------------------------------------------------------------

def rebuild_reverse_map_only() -> int:
    """Rebuild ``permno_cik_map.csv`` from files already on disk.

    No EDGAR request and no SEC lock: CRSP and ``company_tickers.json`` are
    the only inputs, and both are cached. Added 2026-08-30 so the
    ``norm_ticker`` NaN repair could be applied to the committed map while two
    extraction lanes held the SEC lock. A full ``main()`` run reproduces the
    same file; this path only skips the fetch and spot-check phases.
    """
    if not os.path.exists(COMPANY_TICKERS_PATH):
        print(f"{COMPANY_TICKERS_PATH} absent — this path does no fetching; "
              f"run the full link build when a SEC lane is free")
        return 1
    print("== CRSP identity ==")
    crsp = build_crsp_identity()
    permno_common = common_us_universe(crsp.permno_df)
    company_tickers = load_company_tickers()
    print(f"  {len(permno_common)} US common-stock PERMNOs; "
          f"company_tickers.json {len(company_tickers)} rows")
    reverse_map = build_reverse_map(permno_common, company_tickers)
    n_mapped = int((reverse_map["cik"] != "").sum())
    print("== reverse map (PERMNO -> CIK) ==")
    print(f"  {n_mapped}/{len(reverse_map)} mapped ({n_mapped / len(reverse_map):.1%})")
    print(f"  routes: {reverse_map['map_route'].value_counts().to_dict()}")
    dl = reverse_map[~reverse_map["still_listed"]]
    dl_mapped = int((dl["cik"] != "").sum())
    print(f"  SURVIVORSHIP: of {len(dl)} delisted common-US PERMNOs, "
          f"{dl_mapped} carry a CIK and {len(dl) - dl_mapped} do not")
    rev_path = os.path.join(OUTPUT_DIR, "permno_cik_map.csv")
    reverse_map.to_csv(rev_path, index=False)
    print(f"  wrote {rev_path} ({len(reverse_map)} rows)")
    return 0


def main() -> int:
    if "--reverse-map-only" in sys.argv[1:]:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        return rebuild_reverse_map_only()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(SUBMISSIONS_DIR, exist_ok=True)
    print("== inputs ==")
    jsonl_hash = sha256_of(FACT2_JSONL)
    subjects = load_subject_ciks(FACT2_JSONL)
    print(f"  fact2_parsed.jsonl sha256 {jsonl_hash[:16]}... "
          f"-> {len(subjects)} unique subject CIKs")

    n_self = int(subjects["n_self_filed"].gt(0).sum())
    if n_self:
        print(f"  {n_self} subject CIKs carry >=1 filing whose EDGAR header "
              f"names the same entity as SUBJECT COMPANY and FILED BY "
              f"(header degeneracy, parsed faithfully; see load_subject_ciks)")

    print("== CRSP identity (last-observed + full history) ==")
    crsp = build_crsp_identity()
    permno_df = crsp.permno_df
    permno_common = common_us_universe(permno_df)
    last_row_universe = int(((permno_df["security_type"] == "EQTY")
                             & (permno_df["share_type"] == "NS")
                             & (permno_df["us_inc"] == "Y")).sum())
    n_delisted = int((~permno_df["still_listed"]).sum())
    print(f"  {len(permno_df)} PERMNOs in snapshot; "
          f"{len(permno_common)} US common stock (EQTY/NS/Y, any observation)")
    print(f"  for comparison, a last-row identity test yields "
          f"{last_row_universe} -- it drops all {n_delisted} securities that "
          f"left CRSP before the pull date (CRSP blanks ShareType/"
          f"SecurityType on delisting), which SPEC 2.3 filter 3 does not")
    print(f"  ticker history: {len(crsp.ticker_spans)} (PERMNO, ticker) spans; "
          f"CUSIP history: {len(crsp.cusip_spans)} (PERMNO, CUSIP) spans")

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
    link = match_subjects(subjects, edgar, permno_common, company_tickers,
                          ticker_spans=crsp.ticker_spans)
    route_counts = link["match_route"].value_counts().to_dict()
    print(f"  match routes: {route_counts}")
    print(f"  matched {int(link['matched'].sum())}/{len(link)} subject CIKs "
          f"({link['matched'].mean():.1%})")

    print("== validation vs reusable CUSIPs ==")
    rate, disagreements, stats = validate_against_old_cusips(link, subjects,
                                                             crsp)
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"  GATE (cover CUSIP in the PERMNO's observed CUSIP history): "
          f"{rate:.4f} on n={stats['matched_with_old_cusip']}")
    print(f"  for comparison, the header-only rule scores "
          f"{stats['agreement_rate_header_only']:.4f} on the same rows -- "
          f"the gap is CRSP identity drift, not linkage error")
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
    print(f"  routes: {reverse_map['map_route'].value_counts().to_dict()}")
    if "still_listed" in reverse_map.columns:
        dl = reverse_map[~reverse_map["still_listed"]]
        dl_mapped = int((dl["cik"] != "").sum())
        print(f"  SURVIVORSHIP: of {len(dl)} delisted common-US PERMNOs "
              f"(precisely the acquired firms a bid outcome is about), "
              f"{dl_mapped} carry a CIK and {len(dl) - dl_mapped} do not; "
              f"the unmapped cannot be BID12-extracted and would drop from "
              f"the control pool, suppressing control-side bid rates")
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
