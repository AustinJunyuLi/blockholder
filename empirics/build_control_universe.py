"""Regenerate the never-13D control universe (SPEC section 11 row 23, §8.2).

Universe: CRSP common stocks (``SecurityType == 'EQTY'``,
``ShareType == 'NS'``, ``USIncFlg == 'Y'``) present in the on-disk
``crsp_daily.csv`` snapshot with no ``SC 13D``/``SCHEDULE 13D`` original **or
amendment** naming them as subject at any point 2021-01-01 -> 2025-12-31.

Exclusion set (conservative union -- a PERMNO is excluded if ANY route ties
it to an in-window 13D subject):

- E1  rebuilt CIK->PERMNO link, matched rows (2022-2025 originals;
      ``output/cik_cusip_link.csv`` from ``empirics.link_cik_cusip``)
- E2  ambiguous ticker-collision candidate PERMNOs from that link (never
      silently resolved, so all candidates come out of the pool)
- E3  reusable cover-page CUSIPs in ``fact2_parsed.jsonl`` (2022-2025
      originals), matched to CRSP ``HdrCUSIP`` -- this is the only route that
      reaches PERMNOs delisted before the snapshot pull (the snapshot header
      is current-only; delisted PERMNOs carry no ticker)
- E4  2021 gap: the on-disk idx files start 2022Q1 but the SPEC window starts
      2021-01-01, so the four 2021 quarterly form.idx files are downloaded,
      2021 initial 13Ds enumerated, their texts fetched (cached under
      ``empirics/data/filings/``) and parsed for subject CIK + cover-page
      CUSIP; CIKs are linked via the same ticker machinery plus the CUSIP
      route
- E5  in-window ``SC 13D/A`` amendments: a seeded random 200-filing sample
      (fetching all amendments is out of scope). Sampled amendment subjects
      join the exclusion set; the rate at which an amendment's subject lacks
      an in-window original quantifies the residual contamination from the
      unsampled remainder
- E6  reverse map: any candidate PERMNO whose current ticker maps (via
      ``company_tickers.json``) to a CIK in the in-window subject set

Outputs (committed, ``empirics/output/``):
- ``never13d_control_universe.csv`` -- PERMNO + identifying columns
- ``never13d_control_summary.csv`` -- funnel counts and the
  amendment-contamination estimate

SEC fair access: bulk pulls run under ``/tmp/sec_edgar_bulk.lock`` and every
response is cached, so re-runs are free and deterministic.

Usage: ``.venv/bin/python -m empirics.build_control_universe``
"""

from __future__ import annotations

import os
import random
import re
from typing import Optional

import pandas as pd

from empirics.edgar_fetch import DATA_DIR, download_form_index, fetch, list_filings
from empirics.parse_13d import RE_TAG, parse_filing
from empirics.link_cik_cusip import (
    OUTPUT_DIR,
    build_permno_table,
    common_us_universe,
    ensure_cached,
    fetch_company_tickers,
    fetch_submissions,
    load_submissions,
    load_subject_ciks,
    match_subjects,
    sec_bulk_lock,
    sha256_of,
)

FILINGS_DIR = os.path.join(DATA_DIR, "filings")
LINK_CSV = os.path.join(OUTPUT_DIR, "cik_cusip_link.csv")
REVERSE_MAP_CSV = os.path.join(OUTPUT_DIR, "permno_cik_map.csv")
FACT2_JSONL = os.path.join(DATA_DIR, "fact2_parsed.jsonl")

WINDOW_START = "2021-01-01"
WINDOW_END = "2025-12-31"
AMENDMENT_SAMPLE_N = 200
AMENDMENT_SAMPLE_SEED = 20260830
FILING_MAX_BYTES = 400_000

# Cover-page CUSIP: "CUSIP No. 74347W108" / "CUSIP: 03783310" etc. Require a
# digit-heavy 8-9 char token so the label itself can never match.
RE_COVER_CUSIP = re.compile(
    r"CUSIP\s*(?:NO\.?|NUMBER|#)?\s*[:\-]?\s*([0-9A-Z]{8,9})\b", re.I)


def parse_cover_cusip(text: str) -> Optional[str]:
    """First cover-page CUSIP (8-9 chars, >=6 digits), tags stripped."""
    plain = RE_TAG.sub(" ", text[:200_000])
    m = RE_COVER_CUSIP.search(plain)
    if not m:
        return None
    cusip = m.group(1).upper()
    if sum(ch.isdigit() for ch in cusip) < 6:
        return None
    return cusip


def norm_cik(raw: object) -> str:
    """Unpadded integer string ('0001173514' -> '1173514')."""
    return str(int(str(raw).strip()))


# -- EDGAR legs ---------------------------------------------------------------

def ensure_form_indexes(years: range) -> None:
    """Download (cached) any missing quarterly form.idx under the lock."""
    missing = [
        (y, q) for y in years for q in (1, 2, 3, 4)
        if not os.path.exists(os.path.join(DATA_DIR, f"form_{y}_QTR{q}.idx"))
    ]
    if not missing:
        return
    print(f"  downloading {len(missing)} quarterly form.idx files")
    with sec_bulk_lock():
        for y, q in missing:
            download_form_index(y, q)


def list_originals(years: range) -> pd.DataFrame:
    """All SC 13D originals in the given years' idx files."""
    rows = []
    for y in years:
        for q in (1, 2, 3, 4):
            path = os.path.join(DATA_DIR, f"form_{y}_QTR{q}.idx")
            for r in list_filings(path, form_types=("SC 13D",)):
                r["quarter"] = f"{y}Q{q}"
                rows.append(r)
    return pd.DataFrame(rows)


def list_amendments(years: range) -> pd.DataFrame:
    rows = []
    for y in years:
        for q in (1, 2, 3, 4):
            path = os.path.join(DATA_DIR, f"form_{y}_QTR{q}.idx")
            for r in list_filings(path, form_types=("SC 13D/A",)):
                r["quarter"] = f"{y}Q{q}"
                rows.append(r)
    return pd.DataFrame(rows)


def filing_cache_path(edgar_path: str) -> str:
    accession = os.path.basename(edgar_path).removesuffix(".txt")
    return os.path.join(FILINGS_DIR, f"{accession}.txt")


def fetch_filing_texts(edgar_paths: list[str]) -> None:
    """Cache master submission texts (throttled, one lock hold)."""
    os.makedirs(FILINGS_DIR, exist_ok=True)
    requests = {
        p: (f"https://www.sec.gov/Archives/{p}", filing_cache_path(p))
        for p in edgar_paths
    }
    ensure_cached(requests, max_bytes=FILING_MAX_BYTES)


def parse_filings(edgar_paths: list[str]) -> pd.DataFrame:
    """Parse cached filing texts: subject CIK + cover-page CUSIP."""
    records = []
    for p in edgar_paths:
        path = filing_cache_path(p)
        rec: dict = {"edgar_path": p, "subject_cik": None, "cover_cusip": None}
        if os.path.exists(path):
            with open(path, "r", encoding="latin-1") as fh:
                text = fh.read()
            parsed = parse_filing(text)
            rec["subject_cik"] = parsed.get("subject_cik")
            rec["cover_cusip"] = parse_cover_cusip(text)
        records.append(rec)
    return pd.DataFrame(records)


# -- exclusion helpers --------------------------------------------------------

def hdrcusip_permnos(pool: pd.DataFrame, cusips: list[str]) -> set[int]:
    """Pool PERMNOs whose HdrCUSIP matches any 8-char CUSIP prefix."""
    prefixes = {c.upper()[:8] for c in cusips if c and len(c) >= 8}
    if not prefixes:
        return set()
    mask = pool["hdrcusip"].str.upper().isin(prefixes)
    return set(pool.loc[mask, "permno"])


def link_ciks(ciks: list[str], filed: pd.DataFrame,
              company_tickers: pd.DataFrame,
              permno_common: pd.DataFrame) -> pd.DataFrame:
    """Run the ticker-match machinery for a fresh set of CIKs.

    ``filed`` carries subject_cik + filed_min/filed_max for the date-range
    disambiguation. Submissions documents are fetched (cached) first.
    """
    if not ciks:
        return pd.DataFrame()
    fetch_submissions(sorted(ciks, key=int))
    edgar = load_submissions(sorted(ciks, key=int))
    subjects = filed.copy()
    for col, default in (("old_cusip", None), ("subject_name", None),
                         ("n_filings", 1)):
        if col not in subjects:
            subjects[col] = default
    return match_subjects(subjects, edgar, permno_common, company_tickers)


def permnos_from_link(link: pd.DataFrame) -> tuple[set[int], set[int]]:
    """(matched permnos, ambiguous candidate permnos) from a link table."""
    matched = set(link.loc[link["matched"], "permno"].dropna().astype(int))
    ambiguous: set[int] = set()
    for cell in link["ambiguous_permnos"].dropna():
        for tok in str(cell).split(";"):
            if tok.strip():
                ambiguous.add(int(tok))
    return matched, ambiguous


# -- main ---------------------------------------------------------------------

def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if not os.path.exists(LINK_CSV) or not os.path.exists(REVERSE_MAP_CSV):
        raise SystemExit(
            "run `python -m empirics.link_cik_cusip` first: "
            f"missing {LINK_CSV} or {REVERSE_MAP_CSV}")

    print("== inputs ==")
    jsonl_hash = sha256_of(FACT2_JSONL)
    subjects_2225 = load_subject_ciks(FACT2_JSONL)
    subject_ciks_2225 = {norm_cik(c) for c in subjects_2225["subject_cik"]}
    print(f"  fact2_parsed.jsonl sha256 {jsonl_hash[:16]}... "
          f"-> {len(subject_ciks_2225)} unique subject CIKs (2022-2025)")

    permno_df = build_permno_table()
    pool = common_us_universe(permno_df)
    print(f"  snapshot {len(permno_df)} PERMNOs; "
          f"US common-stock candidate pool {len(pool)}")

    link = pd.read_csv(LINK_CSV, dtype={"subject_cik": str})
    reverse_map = pd.read_csv(REVERSE_MAP_CSV, dtype={"cik": str})

    print("== 2021 gap: idx + filing texts ==")
    ensure_form_indexes(range(2021, 2022))
    originals_2021 = list_originals(range(2021, 2022))
    in_window_2021 = originals_2021[
        (originals_2021["date_filed"] >= WINDOW_START)
        & (originals_2021["date_filed"] <= WINDOW_END)]
    print(f"  2021 SC 13D originals in idx: {len(originals_2021)}; "
          f"in window: {len(in_window_2021)}")
    fetch_filing_texts(sorted(in_window_2021["edgar_path"].tolist()))
    parsed_2021 = parse_filings(sorted(in_window_2021["edgar_path"].tolist()))
    parsed_2021 = parsed_2021.merge(
        in_window_2021[["edgar_path", "date_filed"]], on="edgar_path",
        how="left")
    n_subj_parsed = int(parsed_2021["subject_cik"].notna().sum())
    print(f"  subject CIK parsed for {n_subj_parsed}/{len(parsed_2021)} "
          f"2021 filings; cover CUSIP for "
          f"{int(parsed_2021['cover_cusip'].notna().sum())}")

    print("== amendment sample (contamination estimate) ==")
    amendments = list_amendments(range(2021, 2026))
    amendments = amendments[
        (amendments["date_filed"] >= WINDOW_START)
        & (amendments["date_filed"] <= WINDOW_END)]
    amendments = amendments.sort_values(["date_filed", "edgar_path"],
                                        kind="stable").reset_index(drop=True)
    n_amend = len(amendments)
    sample_idx = sorted(random.Random(AMENDMENT_SAMPLE_SEED).sample(
        range(n_amend), min(AMENDMENT_SAMPLE_N, n_amend)))
    amend_sample = amendments.iloc[sample_idx]
    print(f"  in-window SC 13D/A rows: {n_amend}; sampled {len(amend_sample)} "
          f"(seed {AMENDMENT_SAMPLE_SEED})")
    fetch_filing_texts(sorted(amend_sample["edgar_path"].tolist()))
    parsed_amend = parse_filings(sorted(amend_sample["edgar_path"].tolist()))

    print("== link 2021 + amendment subjects ==")
    company_tickers = fetch_company_tickers()

    subj_2021 = parsed_2021[parsed_2021["subject_cik"].notna()].copy()
    subj_2021["cik_norm"] = subj_2021["subject_cik"].map(norm_cik)
    filed_2021 = subj_2021.groupby("cik_norm").agg(
        filed_min=("date_filed", "min"), filed_max=("date_filed", "max"),
    ).reset_index().rename(columns={"cik_norm": "subject_cik"})
    link_2021 = link_ciks(sorted(filed_2021["subject_cik"].tolist(), key=int),
                          filed_2021, company_tickers, pool)
    print(f"  2021 subjects: {len(filed_2021)} unique CIKs; ticker-link "
          f"routes: {link_2021['match_route'].value_counts().to_dict()}")

    amend_subj = parsed_amend[parsed_amend["subject_cik"].notna()].copy()
    amend_subj["cik_norm"] = amend_subj["subject_cik"].map(norm_cik)
    amend_subj = amend_subj.merge(
        amend_sample[["edgar_path", "date_filed"]], on="edgar_path",
        how="left")
    filed_amend = amend_subj.groupby("cik_norm").agg(
        filed_min=("date_filed", "min"), filed_max=("date_filed", "max"),
    ).reset_index().rename(columns={"cik_norm": "subject_cik"})
    link_amend = link_ciks(
        sorted(filed_amend["subject_cik"].tolist(), key=int),
        filed_amend, company_tickers, pool)

    # contamination: sampled amendment subjects with no in-window original
    subject_ciks_2021 = set(filed_2021["subject_cik"])
    in_window_originals = subject_ciks_2225 | subject_ciks_2021
    amend_subject_set = set(filed_amend["subject_cik"])
    n_amend_parsed = len(amend_subject_set)
    orphan = amend_subject_set - in_window_originals
    orphan_rate = (len(orphan) / n_amend_parsed) if n_amend_parsed else float(
        "nan")
    print(f"  amendment subjects parsed: {n_amend_parsed}; without an "
          f"in-window original: {len(orphan)} ({orphan_rate:.1%})")

    print("== exclusion set ==")
    e1, e2 = permnos_from_link(link)
    e3 = hdrcusip_permnos(
        pool, [c for c in subjects_2225["old_cusip"].dropna().tolist()])
    e4_matched, e4_ambig = permnos_from_link(link_2021)
    e4_cusip = hdrcusip_permnos(
        pool, parsed_2021["cover_cusip"].dropna().tolist())
    e4 = e4_matched | e4_ambig | e4_cusip
    e5_matched, e5_ambig = permnos_from_link(link_amend)
    e5_cusip = hdrcusip_permnos(
        pool, parsed_amend["cover_cusip"].dropna().tolist())
    e5 = e5_matched | e5_ambig | e5_cusip
    all_subject_ciks = in_window_originals | amend_subject_set
    e6 = set(reverse_map.loc[
        reverse_map["cik"].fillna("").map(
            lambda c: c != "" and norm_cik(c) in all_subject_ciks),
        "permno"].astype(int))

    excluded: set[int] = set()
    funnel = []
    for name, s in [("E1_link_matched", e1), ("E2_link_ambiguous", e2),
                    ("E3_old_cusip_hdr", e3), ("E4_gap2021", e4),
                    ("E5_amendment_sample", e5), ("E6_reverse_map", e6)]:
        before = len(excluded)
        excluded |= {int(p) for p in s}
        funnel.append((name, len({int(p) for p in s}), len(excluded) - before,
                       len(excluded)))
    for name, total, marginal, cum in funnel:
        print(f"  {name}: {total} PERMNOs (+{marginal} new; cum {cum})")

    universe = pool[~pool["permno"].isin(excluded)].copy()
    universe = universe.sort_values("permno").reset_index(drop=True)

    out_path = os.path.join(OUTPUT_DIR, "never13d_control_universe.csv")
    universe.to_csv(out_path, index=False)
    print(f"  wrote {out_path} ({len(universe)} PERMNOs)")

    summary_rows = [
        ("snapshot_permnos", len(permno_df), "all PERMNOs in crsp_daily.csv"),
        ("candidate_pool", len(pool),
         "SecurityType EQTY, ShareType NS, USIncFlg Y"),
        ("subjects_2022_2025", len(subject_ciks_2225),
         "unique subject CIKs in fact2_parsed.jsonl"),
        ("originals_2021_filings", len(in_window_2021),
         "2021 SC 13D originals enumerated from downloaded idx"),
        ("originals_2021_subjects", len(subject_ciks_2021),
         "unique 2021 subject CIKs parsed"),
        ("excluded_total", len(excluded), "union of E1-E6"),
        ("universe_size", len(universe), "candidate_pool minus excluded"),
        ("amendments_in_window", n_amend, "SC 13D/A rows 2021-2025 in idx"),
        ("amendment_sample", len(amend_sample),
         f"seeded sample (seed {AMENDMENT_SAMPLE_SEED})"),
        ("amendment_orphan_rate", round(orphan_rate, 4),
         "share of sampled amendment subjects with no in-window original; "
         "the unsampled remainder is the residual contamination"),
        ("amendment_orphan_extrapolated",
         round(orphan_rate * n_amend) if n_amend_parsed else "",
         "rough upper-bound estimate of missed amendment-only subjects "
         "(assumes sample rate applies to all amendments and one subject "
         "per amendment; not added to the exclusion set)"),
        ("jsonl_sha256", jsonl_hash[:16], "fact2_parsed.jsonl used"),
    ]
    summary = pd.DataFrame(summary_rows, columns=["metric", "value", "note"])
    sum_path = os.path.join(OUTPUT_DIR, "never13d_control_summary.csv")
    summary.to_csv(sum_path, index=False)
    print(f"  wrote {sum_path}")

    detail_path = os.path.join(OUTPUT_DIR, "never13d_exclusion_detail.csv")
    detail = pd.DataFrame(
        [(name, total, marginal, cum) for name, total, marginal, cum in funnel],
        columns=["component", "permnos", "marginal_new", "cumulative"])
    detail.to_csv(detail_path, index=False)
    print(f"  wrote {detail_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
