"""Campaign fingerprints: the shared table behind E1 and E2.

Implements `empirics/spec.md` and adds no measurement rule of its own. The
module builds one campaign table from the EDGAR quarterly indexes and the local
filing cache, then runs each registered exercise from that table.

Usage:
    PYTHONPATH=. .venv/bin/python -m empirics.fingerprints build
    PYTHONPATH=. .venv/bin/python -m empirics.fingerprints run e1
    PYTHONPATH=. .venv/bin/python -m empirics.fingerprints run e2
    PYTHONPATH=. .venv/bin/python -m empirics.fingerprints render e1

Outputs:
    empirics/output/campaigns.csv      the shared build table, one row per campaign
    empirics/output/filings.csv        one row per enumerated accession, with a status
    empirics/output/e1_estimate.json   E1 result file (single authority for E1 numbers)
    empirics/output/e1_campaigns.csv   E1 analysis sample
    empirics/output/e1_stake.pdf       distribution of B^F by period
    empirics/output/e2_estimate.json   E2 result file (single authority for E2 numbers)
    empirics/output/e2_campaigns.csv   E2 analysis sample
    empirics/output/e2_runup_jump.pdf  run-up share by tercile and period

Every run is deterministic: sorted iteration, fixed seeds, no timestamps or
paths written into the result files.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re

import numpy as np
import pandas as pd

from empirics.edgar_fetch import DATA_DIR, fetch_filing_text, list_filings
from empirics.facts import FEDERAL_HOLIDAYS
from empirics.parse_13d import RE_TAG, XML_PERCENT, parse_filing

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "output")
CACHE_DIR = os.path.join(DATA_DIR, "filings")
CRSP_PATH = os.path.join(DATA_DIR, "crsp_daily.csv")
TICKERS_PATH = os.path.join(DATA_DIR, "company_tickers.json")

SPEC = "empirics/spec.md"

# -- registered constants ----------------------------------------------------

QUARTERS = [(y, q) for y in range(2021, 2026) for q in (1, 2, 3, 4)]
FORM_TYPES = ("SC 13D",)          # alias expansion adds "SCHEDULE 13D"
RULE_DATE = dt.date(2024, 2, 5)   # pre if the trigger date is before this
WITHIN_BDAYS = 5                  # the clock paragraph's share threshold
ACCEPTANCE_CUTOFF = dt.time(16, 0)  # reaction day rolls at 16:00 New York
N_BOOT = 2000
BOOT_SEED = 5
STAKE_LOW, STAKE_HIGH = 0.0, 100.0  # B^F lives on (0, 100]

E1_G1_MIN_COVERAGE = 0.90
E1_G3_MAX_GAP = 0.10
E2_G1_MIN_COVERAGE = 0.80
E2_G3_MIN_CELL = 100
E2_G4_MAX_GAP = 0.10

AMIHUD_START, AMIHUD_END = -130, -11   # trading days relative to the trigger
AMIHUD_MIN_DAYS = 60

TRUNCATION_BYTES = 400_000        # the fetch cap the cache was built with

RE_ACCEPTANCE = re.compile(r"<ACCEPTANCE-DATETIME>\s*(\d{14})")
RE_XML_CUSIP = re.compile(r"<issuerCUSIP>\s*([0-9A-Za-z]{6,9})\s*</issuerCUSIP>", re.I)
RE_CUSIP_LABEL = re.compile(
    r"\(?\s*CUSIP\s*(?:No\.?|Number|#)?\s*\)?", re.I)
RE_CUSIP_TOKEN = re.compile(
    r"\b([0-9A-Z]{6})[\s-]?([0-9A-Z]{2})[\s-]?([0-9A-Z])\b")


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------

def enumerate_filings() -> list[dict]:
    """Every initial Schedule 13D in the twenty quarterly indexes, deduped.

    ``form.idx`` is filer-indexed, so one joint filing appears once per
    reporting person under the same accession. Collapse on accession first.
    Rows come back in sorted accession order so the whole pipeline is
    reproducible.
    """
    seen: dict[str, dict] = {}
    for year, qtr in QUARTERS:
        idx = os.path.join(DATA_DIR, f"form_{year}_QTR{qtr}.idx")
        for row in list_filings(idx, form_types=FORM_TYPES):
            accession = os.path.basename(row["edgar_path"])[:-4]
            if accession not in seen:
                seen[accession] = {
                    "accession": accession,
                    "form": row["form"],
                    "company": row["company"],
                    "date_filed": row["date_filed"],
                    "edgar_path": row["edgar_path"],
                }
    return [seen[a] for a in sorted(seen)]


def cache_candidates(accession: str) -> list[str]:
    """Both cache naming schemes: accession with and without hyphens."""
    return [os.path.join(CACHE_DIR, accession + ".txt"),
            os.path.join(CACHE_DIR, accession.replace("-", "") + ".txt")]


def read_cached(accession: str) -> tuple[str | None, bool]:
    """Return (text, truncated) from the local cache, or (None, False)."""
    for path in cache_candidates(accession):
        if os.path.exists(path):
            with open(path, "r", encoding="latin-1") as fh:
                text = fh.read()
            return text, os.path.getsize(path) == TRUNCATION_BYTES
    return None, False


def load_text(accession: str, edgar_path: str,
              allow_fetch: bool = True) -> tuple[str | None, bool]:
    """Cache first; a filing absent from the cache is fetched once and cached.

    Returns (text, truncated). A filing that cannot be obtained returns
    (None, False) and is counted in ``coverage.missing_text``.
    """
    text, truncated = read_cached(accession)
    if text is not None or not allow_fetch:
        return text, truncated
    try:
        text = fetch_filing_text(edgar_path, max_bytes=TRUNCATION_BYTES)
    except Exception:
        return None, False
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, accession + ".txt")
    with open(path, "w", encoding="latin-1", errors="replace") as fh:
        fh.write(text)
    return text, len(text.encode("latin-1", errors="replace")) >= TRUNCATION_BYTES


# ---------------------------------------------------------------------------
# Filing-level fields
# ---------------------------------------------------------------------------

def parse_acceptance(text: str) -> dt.datetime | None:
    """The header ``ACCEPTANCE-DATETIME``, New York time."""
    m = RE_ACCEPTANCE.search(text)
    if not m:
        return None
    try:
        return dt.datetime.strptime(m.group(1), "%Y%m%d%H%M%S")
    except ValueError:
        return None


def _plain_text(text: str) -> str:
    return html.unescape(RE_TAG.sub(" ", text))


def parse_cusip(text: str) -> tuple[str | None, str | None, int]:
    """The subject's CUSIP: structured XML first, the cover-page line otherwise.

    Returns (cusip8, route, n_distinct_near_label). Cover pages print the
    nine-character CUSIP beside a "(CUSIP Number)" or "CUSIP No." label, often
    with internal spaces ("759141 104"). Take the token nearest the label and
    report how many distinct CUSIPs sit in the searched windows so a
    multi-CUSIP filing is visible rather than silently resolved.
    """
    xm = RE_XML_CUSIP.search(text)
    if xm:
        raw = re.sub(r"[^0-9A-Za-z]", "", xm.group(1)).upper()
        if len(raw) >= 8:
            return raw[:8], "xml", 1

    plain = _plain_text(text)
    found: list[str] = []
    nearest: str | None = None
    for lab in RE_CUSIP_LABEL.finditer(plain):
        for window, reverse in ((plain[max(0, lab.start() - 200):lab.start()], True),
                                (plain[lab.end():lab.end() + 200], False)):
            hits = [m for m in RE_CUSIP_TOKEN.finditer(window)]
            hits = [m for m in hits if any(c.isdigit() for c in m.group(0))]
            if not hits:
                continue
            picks = [(m.group(1) + m.group(2) + m.group(3)).upper() for m in hits]
            if reverse:
                picks = picks[::-1]
            for p in picks:
                if p not in found:
                    found.append(p)
            if nearest is None:
                nearest = picks[0]
            break
    if nearest is None:
        return None, None, 0
    return nearest[:8], "cover", len(found)


def parse_stake(text: str) -> tuple[float | None, str | None]:
    """Percent of class on the cover page, the max across reporting persons.

    The existing parser already takes the maximum across the row-11 blocks and
    the structured ``percentOfClass`` elements. Restrict to (0, 100] here, the
    registered support for B^F.
    """
    from empirics.parse_13d import parse_percent_of_class
    value = parse_percent_of_class(text)
    if value is None or not (STAKE_LOW < value <= STAKE_HIGH):
        return None, None
    route = "xml" if XML_PERCENT.search(text) else "cover"
    return float(value), route


# ---------------------------------------------------------------------------
# Calendars
# ---------------------------------------------------------------------------

def business_delay(trigger: dt.date, filed: dt.date) -> int:
    """Federal business days from the trigger date to the filing date.

    Half-open, as ``np.busday_count`` counts: a filing on the first business
    day after the trigger has a delay of one. Negative delays (a filing dated
    before its own trigger) are kept, not screened.
    """
    return int(np.busday_count(np.datetime64(trigger, "D"),
                               np.datetime64(filed, "D"),
                               holidays=FEDERAL_HOLIDAYS))


def reaction_day(filed: dt.date, accepted: dt.datetime | None,
                 trading_days: np.ndarray) -> dt.date | None:
    """The first trading day on which the filing can move the price.

    The filing date if the acceptance time is before 16:00 New York, otherwise
    the next trading day. ``trading_days`` is a sorted array of
    ``datetime64[D]`` trading dates; the candidate day rolls forward to the
    first trading day at or after it.
    """
    if accepted is None:
        return None
    candidate = filed if accepted.time() < ACCEPTANCE_CUTOFF else filed + dt.timedelta(days=1)
    idx = int(np.searchsorted(trading_days, np.datetime64(candidate, "D"), side="left"))
    if idx >= len(trading_days):
        return None
    return trading_days[idx].astype("datetime64[D]").astype(object)


# ---------------------------------------------------------------------------
# The campaign table
# ---------------------------------------------------------------------------

def build_filing_records(allow_fetch: bool = True, progress: bool = True) -> pd.DataFrame:
    """One row per enumerated accession, every row carrying a status."""
    rows = enumerate_filings()
    records = []
    for i, row in enumerate(rows):
        rec = {
            "accession": row["accession"],
            "form": row["form"],
            "company": row["company"],
            "date_filed": row["date_filed"],
            "edgar_path": row["edgar_path"],
            "subject_cik": None,
            "accepted": None,
            "trigger_date": None,
            "parse_route": None,
            "stake": None,
            "stake_route": None,
            "cusip8": None,
            "cusip_route": None,
            "cusip_candidates": 0,
            "truncated": False,
            "status": None,
            "reason": None,
        }
        text, truncated = load_text(row["accession"], row["edgar_path"],
                                    allow_fetch=allow_fetch)
        if text is None:
            rec["status"], rec["reason"] = "unresolved", "missing_text"
            records.append(rec)
            continue
        rec["truncated"] = bool(truncated)

        parsed = parse_filing(text)
        rec["subject_cik"] = parsed.get("subject_cik")
        rec["parse_route"] = "xml" if parsed.get("has_xml") else "cover"
        accepted = parse_acceptance(text)
        rec["accepted"] = accepted.isoformat() if accepted else None
        stake, stake_route = parse_stake(text)
        rec["stake"], rec["stake_route"] = stake, stake_route
        cusip, cusip_route, n_cusip = parse_cusip(text)
        rec["cusip8"], rec["cusip_route"], rec["cusip_candidates"] = (
            cusip, cusip_route, n_cusip)

        trigger = parsed.get("event")
        if trigger is None:
            rec["status"], rec["reason"] = "unresolved", "no_trigger"
        elif rec["subject_cik"] is None:
            rec["status"], rec["reason"] = "unresolved", "no_subject_cik"
        else:
            rec["trigger_date"] = trigger.isoformat()
            rec["status"], rec["reason"] = "resolved", "ok"
        records.append(rec)
        if progress and (i + 1) % 500 == 0:
            print(f"  parsed {i + 1}/{len(rows)}")
    return pd.DataFrame(records)


def collapse_campaigns(filings: pd.DataFrame) -> pd.DataFrame:
    """One row per (subject CIK, trigger date), the earliest acceptance kept.

    Filings with no acceptance timestamp sort last, so a campaign keeps a
    timestamped accession whenever it has one.
    """
    res = filings[filings["status"] == "resolved"].copy()
    res["_accepted_key"] = res["accepted"].fillna("9999")
    res = res.sort_values(["_accepted_key", "accession"], kind="mergesort")
    grouped = res.groupby(["subject_cik", "trigger_date"], sort=True)
    kept = res.loc[grouped.head(1).index].copy()
    kept["n_filings"] = grouped.size().reindex(
        pd.MultiIndex.from_arrays([kept["subject_cik"], kept["trigger_date"]])).to_numpy()
    # a stake present elsewhere in the campaign but not on the kept accession
    any_stake = grouped["stake"].apply(lambda s: bool(s.notna().any()))
    kept["stake_elsewhere"] = (
        any_stake.reindex(pd.MultiIndex.from_arrays(
            [kept["subject_cik"], kept["trigger_date"]])).to_numpy()
        & kept["stake"].isna().to_numpy())
    kept = kept.drop(columns=["_accepted_key"])

    trigger = pd.to_datetime(kept["trigger_date"])
    filed = pd.to_datetime(kept["date_filed"])
    # The universe is stratified by the quarterly indexes, which are keyed on the
    # filing date, so the yearly table runs on the filing year and covers 2021 to
    # 2025 exactly. The trigger year is carried alongside it.
    kept["year"] = filed.dt.year.astype(int)
    kept["trigger_year"] = trigger.dt.year.astype(int)
    kept["period"] = np.where(trigger.dt.date < RULE_DATE, "pre", "post")
    kept["delay_bdays"] = [business_delay(t.date(), f.date())
                           for t, f in zip(trigger, filed)]
    return kept.sort_values(["trigger_date", "accession"],
                            kind="mergesort").reset_index(drop=True)


def build(allow_fetch: bool = True) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Build the shared campaign table and its coverage counts."""
    os.makedirs(OUT_DIR, exist_ok=True)
    filings = build_filing_records(allow_fetch=allow_fetch)
    campaigns = collapse_campaigns(filings)

    reasons = filings["reason"].value_counts().to_dict()
    stake_ok = campaigns["stake"].notna()
    coverage = {
        "index_accessions": int(len(filings)),
        "missing_text": int(reasons.get("missing_text", 0)),
        "no_trigger": int(reasons.get("no_trigger", 0)),
        "no_subject_cik": int(reasons.get("no_subject_cik", 0)),
        "resolved_filings": int((filings["status"] == "resolved").sum()),
        "campaigns": int(len(campaigns)),
        "campaigns_multi_filing": int((campaigns["n_filings"] > 1).sum()),
        "no_acceptance": int(campaigns["accepted"].isna().sum()),
        "truncated_source": int(campaigns["truncated"].sum()),
        "stake_readable": int(stake_ok.sum()),
        "stake_share": float(stake_ok.mean()) if len(campaigns) else float("nan"),
        "stake_only_elsewhere": int(campaigns["stake_elsewhere"].sum()),
        "cusip_readable": int(campaigns["cusip8"].notna().sum()),
        "cusip_multi_candidate": int((campaigns["cusip_candidates"] > 1).sum()),
        "negative_delay": int((campaigns["delay_bdays"] < 0).sum()),
    }
    filings.to_csv(os.path.join(OUT_DIR, "filings.csv"), index=False)
    campaigns.to_csv(os.path.join(OUT_DIR, "campaigns.csv"), index=False)
    return filings, campaigns, coverage


def load_campaigns(allow_fetch: bool = True) -> tuple[pd.DataFrame, dict]:
    """The campaign table, built if it is not on disk."""
    path = os.path.join(OUT_DIR, "campaigns.csv")
    fpath = os.path.join(OUT_DIR, "filings.csv")
    if not (os.path.exists(path) and os.path.exists(fpath)):
        _, campaigns, coverage = build(allow_fetch=allow_fetch)
        return campaigns, coverage
    campaigns = pd.read_csv(path, dtype={"subject_cik": str, "cusip8": str,
                                         "accession": str})
    filings = pd.read_csv(fpath, dtype={"subject_cik": str, "accession": str})
    reasons = filings["reason"].value_counts().to_dict()
    stake_ok = campaigns["stake"].notna()
    coverage = {
        "index_accessions": int(len(filings)),
        "missing_text": int(reasons.get("missing_text", 0)),
        "no_trigger": int(reasons.get("no_trigger", 0)),
        "no_subject_cik": int(reasons.get("no_subject_cik", 0)),
        "resolved_filings": int((filings["status"] == "resolved").sum()),
        "campaigns": int(len(campaigns)),
        "campaigns_multi_filing": int((campaigns["n_filings"] > 1).sum()),
        "no_acceptance": int(campaigns["accepted"].isna().sum()),
        "truncated_source": int(campaigns["truncated"].sum()),
        "stake_readable": int(stake_ok.sum()),
        "stake_share": float(stake_ok.mean()) if len(campaigns) else float("nan"),
        "stake_only_elsewhere": int(campaigns["stake_elsewhere"].sum()),
        "cusip_readable": int(campaigns["cusip8"].notna().sum()),
        "cusip_multi_candidate": int((campaigns["cusip_candidates"] > 1).sum()),
        "negative_delay": int((campaigns["delay_bdays"] < 0).sum()),
    }
    return campaigns, coverage


# ---------------------------------------------------------------------------
# Descriptive statistics and the campaign bootstrap
# ---------------------------------------------------------------------------

def describe(values: np.ndarray) -> dict:
    v = np.asarray(values, dtype=float)
    v = v[np.isfinite(v)]
    if not len(v):
        return {"n": 0, "mean": None, "median": None, "p25": None, "p75": None}
    return {
        "n": int(len(v)),
        "mean": float(np.mean(v)),
        "median": float(np.median(v)),
        "p25": float(np.quantile(v, 0.25)),
        "p75": float(np.quantile(v, 0.75)),
    }


def bootstrap_difference(pre: np.ndarray, post: np.ndarray,
                         stat, seed: int = BOOT_SEED,
                         n_boot: int = N_BOOT) -> dict:
    """Percentile interval for post minus pre, resampling campaigns."""
    pre = np.asarray(pre, dtype=float)
    post = np.asarray(post, dtype=float)
    if not len(pre) or not len(post):
        return {"point": None, "ci_low": None, "ci_high": None,
                "n_boot": n_boot, "seed": seed}
    rng = np.random.default_rng(seed)
    draws = np.empty(n_boot)
    for b in range(n_boot):
        a = pre[rng.integers(0, len(pre), size=len(pre))]
        c = post[rng.integers(0, len(post), size=len(post))]
        draws[b] = stat(c) - stat(a)
    return {
        "point": float(stat(post) - stat(pre)),
        "ci_low": float(np.percentile(draws, 2.5)),
        "ci_high": float(np.percentile(draws, 97.5)),
        "n_boot": n_boot,
        "seed": seed,
    }


def bootstrap_statistic(values: np.ndarray, stat, seed: int = BOOT_SEED,
                        n_boot: int = N_BOOT) -> dict:
    v = np.asarray(values, dtype=float)
    v = v[np.isfinite(v)]
    if not len(v):
        return {"point": None, "ci_low": None, "ci_high": None,
                "n_boot": n_boot, "seed": seed}
    rng = np.random.default_rng(seed)
    draws = np.array([stat(v[rng.integers(0, len(v), size=len(v))])
                      for _ in range(n_boot)])
    return {
        "point": float(stat(v)),
        "ci_low": float(np.percentile(draws, 2.5)),
        "ci_high": float(np.percentile(draws, 97.5)),
        "n_boot": n_boot,
        "seed": seed,
    }


# ---------------------------------------------------------------------------
# The clock paragraph
# ---------------------------------------------------------------------------

def clock_block(campaigns: pd.DataFrame) -> dict:
    """Share filed within five business days and median delay, by year and period."""
    def cell(frame: pd.DataFrame) -> dict:
        d = frame["delay_bdays"].to_numpy(dtype=float)
        d = d[np.isfinite(d)]
        return {
            "n": int(len(d)),
            "share_within_5bd": float(np.mean(d <= WITHIN_BDAYS)) if len(d) else None,
            "median_delay_bdays": float(np.median(d)) if len(d) else None,
        }

    by_year = {str(y): cell(campaigns[campaigns["year"] == y])
               for y in sorted(campaigns["year"].unique())}
    by_trigger_year = {str(y): cell(campaigns[campaigns["trigger_year"] == y])
                       for y in sorted(campaigns["trigger_year"].unique())}
    by_period = {}
    for p in ("pre", "post"):
        sub = campaigns[campaigns["period"] == p]
        block = cell(sub)
        block["share_within_5bd_ci"] = bootstrap_statistic(
            (sub["delay_bdays"].to_numpy(dtype=float) <= WITHIN_BDAYS).astype(float),
            np.mean)
        by_period[p] = block
    return {
        "definition": ("federal business days from the trigger date to the "
                       "filing date, holidays from empirics/facts.py"),
        "within_bdays": WITHIN_BDAYS,
        "by_year": by_year,
        "by_trigger_year": by_trigger_year,
        "by_period": by_period,
    }


# ---------------------------------------------------------------------------
# E1: stake at filing
# ---------------------------------------------------------------------------

def e1_gates(campaigns: pd.DataFrame) -> dict:
    """E1-G1 parse coverage and E1-G3 differential coverage. G2 is ticket 07."""
    ok = campaigns["stake"].notna()
    share = float(ok.mean()) if len(campaigns) else float("nan")
    g1 = bool(share >= E1_G1_MIN_COVERAGE)

    shares = {}
    for p in ("pre", "post"):
        sub = campaigns[campaigns["period"] == p]
        shares[p] = float(sub["stake"].notna().mean()) if len(sub) else float("nan")
    gap = abs(shares["pre"] - shares["post"])
    g3 = bool(gap <= E1_G3_MAX_GAP)

    return {
        "E1-G1_parse_coverage": {
            "share_with_stake": share,
            "threshold": E1_G1_MIN_COVERAGE,
            "verdict": "PASS" if g1 else "NO-GO",
        },
        "E1-G2_blind_audit": {
            "verdict": "NOT RUN",
            "note": "sixty stratified campaigns, hand-read by an independent worker",
        },
        "E1-G3_differential_coverage": {
            "share_with_stake_pre": shares["pre"],
            "share_with_stake_post": shares["post"],
            "absolute_gap": gap,
            "threshold": E1_G3_MAX_GAP,
            "verdict": "PASS" if g3 else "NO-GO",
        },
    }


def run_e1(campaigns: pd.DataFrame, coverage: dict) -> dict:
    sample = campaigns[campaigns["stake"].notna()].copy()

    by_year = {str(y): describe(sample.loc[sample["year"] == y, "stake"].to_numpy())
               for y in sorted(campaigns["year"].unique())}
    by_trigger_year = {
        str(y): describe(sample.loc[sample["trigger_year"] == y, "stake"].to_numpy())
        for y in sorted(campaigns["trigger_year"].unique())}
    by_period = {p: describe(sample.loc[sample["period"] == p, "stake"].to_numpy())
                 for p in ("pre", "post")}

    pre = sample.loc[sample["period"] == "pre", "stake"].to_numpy(dtype=float)
    post = sample.loc[sample["period"] == "post", "stake"].to_numpy(dtype=float)
    difference = {
        "mean": bootstrap_difference(pre, post, np.mean),
        "median": bootstrap_difference(pre, post, np.median),
    }

    gates = e1_gates(campaigns)
    verdicts = [g["verdict"] for g in gates.values()]
    status = ("NO-GO" if "NO-GO" in verdicts
              else ("PENDING" if "NOT RUN" in verdicts else "GO"))

    result = {
        "exercise": "e1",
        "object": "stake at filing, B^F, percent of class",
        "spec": SPEC,
        "label": "ESTIMATED",
        "design": "descriptive",
        "causal_claim": False,
        "population": {
            "forms": ["SC 13D", "SCHEDULE 13D"],
            "quarters": "2021 Q1 through 2025 Q4",
            "unit": "campaign, one (subject CIK, trigger date) pair",
            "period_cut": RULE_DATE.isoformat(),
            "year_key": "calendar year of the filing date",
        },
        "coverage": coverage,
        "by_year": by_year,
        "by_trigger_year": by_trigger_year,
        "by_period": by_period,
        "difference": difference,
        "clock": clock_block(campaigns),
        "gates": gates,
        "status": status,
        "headline_suppressed": status == "NO-GO",
    }
    os.makedirs(OUT_DIR, exist_ok=True)
    sample.to_csv(os.path.join(OUT_DIR, "e1_campaigns.csv"), index=False)
    with open(os.path.join(OUT_DIR, "e1_estimate.json"), "w") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)
    plot_e1(sample)
    return result


def plot_e1(sample: pd.DataFrame) -> None:
    """Distribution of B^F by period."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(5.5, 3.4))
    bins = np.arange(0, 52, 2.0)
    for period, colour in (("pre", "#4477aa"), ("post", "#ee6677")):
        v = sample.loc[sample["period"] == period, "stake"].to_numpy(dtype=float)
        if not len(v):
            continue
        ax.hist(np.clip(v, 0, 50), bins=bins, density=True, alpha=0.55,
                color=colour, label=f"{period} (n={len(v)})")
    ax.set_xlabel("Stake at filing, percent of class")
    ax.set_ylabel("Density")
    ax.legend(fontsize=8, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "e1_stake.pdf"))
    plt.close(fig)


# ---------------------------------------------------------------------------
# E2: run-up versus jump by pre-trigger liquidity (built here, run in ticket 08)
# ---------------------------------------------------------------------------

CRSP_COLUMNS = ["PERMNO", "HdrCUSIP", "CUSIP", "Ticker", "DlyCalDt",
                "DlyPrc", "DlyRet", "DlyVol"]


def load_crsp(path: str = CRSP_PATH) -> pd.DataFrame:
    """Raw CRSP daily file, the columns the link and the returns need."""
    df = pd.read_csv(path, usecols=CRSP_COLUMNS,
                     dtype={"PERMNO": "int32", "HdrCUSIP": "string",
                            "CUSIP": "string", "Ticker": "string"},
                     parse_dates=["DlyCalDt"])
    df["DlyCalDt"] = df["DlyCalDt"].dt.date
    return df


def trading_calendar(crsp: pd.DataFrame) -> np.ndarray:
    """Sorted array of trading days present in the CRSP file."""
    days = pd.unique(pd.Series(crsp["DlyCalDt"]))
    return np.sort(np.array(list(days), dtype="datetime64[D]"))


def market_return(crsp: pd.DataFrame) -> pd.Series:
    """Equal-weighted mean of DlyRet across all securities, by day."""
    return crsp.groupby("DlyCalDt")["DlyRet"].mean()


def cik_ticker_map(path: str = TICKERS_PATH) -> dict[str, str]:
    """SEC CIK-to-ticker map, the listing proxy and the link fallback."""
    with open(path) as fh:
        raw = json.load(fh)
    out: dict[str, str] = {}
    for entry in raw.values():
        cik = str(int(entry["cik_str"]))
        out.setdefault(cik, str(entry["ticker"]).upper())
    return out


def build_link(crsp: pd.DataFrame) -> tuple[dict[str, int], dict[str, int]]:
    """(cusip8 -> PERMNO, ticker -> PERMNO) lookups from the raw CRSP file.

    A CUSIP or ticker mapping to more than one PERMNO is dropped rather than
    guessed, so an ambiguous identifier fails the link instead of matching the
    wrong security.
    """
    by_cusip: dict[str, set[int]] = {}
    by_ticker: dict[str, set[int]] = {}
    frame = crsp[["PERMNO", "HdrCUSIP", "CUSIP", "Ticker"]].drop_duplicates()
    for permno, hdr, cus, tic in frame.itertuples(index=False):
        for raw in (hdr, cus):
            if isinstance(raw, str) and len(raw) >= 8:
                by_cusip.setdefault(raw[:8].upper(), set()).add(int(permno))
        if isinstance(tic, str) and tic:
            by_ticker.setdefault(tic.upper(), set()).add(int(permno))
    return ({k: next(iter(v)) for k, v in by_cusip.items() if len(v) == 1},
            {k: next(iter(v)) for k, v in by_ticker.items() if len(v) == 1})


def link_campaign(cusip8: str | None, subject_cik: str | None,
                  by_cusip: dict[str, int], by_ticker: dict[str, int],
                  tickers: dict[str, str]) -> tuple[int | None, str | None]:
    """CUSIP first, the SEC CIK-to-ticker map as the fallback."""
    if isinstance(cusip8, str) and cusip8.upper() in by_cusip:
        return by_cusip[cusip8.upper()], "cusip"
    if subject_cik is not None:
        tic = tickers.get(str(int(subject_cik))) if str(subject_cik).isdigit() else None
        if tic and tic in by_ticker:
            return by_ticker[tic], "ticker"
    return None, None


def runup_and_jump(panel: pd.DataFrame, mkt: pd.Series, trigger: dt.date,
                   reaction: dt.date) -> tuple[float | None, float | None]:
    """Market-adjusted run-up R and jump J.

    R accumulates the adjusted return from the close of the last trading day
    before the trigger to the close of the last trading day before the reaction
    day. J is the adjusted return on the reaction day. A missing day on the
    path returns (None, None): the link must hold on every needed day.
    """
    days = panel.index.to_numpy()
    if reaction not in panel.index:
        return None, None
    pre_idx = np.searchsorted(days, trigger, side="left")
    react_idx = np.searchsorted(days, reaction, side="left")
    if pre_idx == 0 or react_idx <= pre_idx:
        return None, None
    window = panel.iloc[pre_idx:react_idx]
    if window["DlyRet"].isna().any():
        return None, None
    adj = window["DlyRet"].to_numpy(dtype=float) - np.array(
        [mkt.get(d, np.nan) for d in window.index])
    if not np.isfinite(adj).all():
        return None, None
    r = float(np.prod(1.0 + adj) - 1.0)
    jump_ret = panel.loc[reaction, "DlyRet"]
    jump_mkt = mkt.get(reaction, np.nan)
    if not np.isfinite(jump_ret) or not np.isfinite(jump_mkt):
        return None, None
    return r, float(jump_ret - jump_mkt)


def amihud(panel: pd.DataFrame, trigger: dt.date) -> float | None:
    """Amihud illiquidity over trading days t-130 to t-11 before the trigger.

    The mean of |DlyRet| divided by dollar volume, requiring at least sixty
    days with positive volume. Higher is less liquid.
    """
    days = panel.index.to_numpy()
    t = int(np.searchsorted(days, trigger, side="left"))
    lo, hi = t + AMIHUD_START, t + AMIHUD_END + 1
    if lo < 0:
        lo = 0
    if hi <= lo:
        return None
    window = panel.iloc[lo:hi]
    dollar = window["DlyPrc"].abs() * window["DlyVol"]
    keep = window["DlyRet"].notna() & (dollar > 0)
    if int(keep.sum()) < AMIHUD_MIN_DAYS:
        return None
    return float((window.loc[keep, "DlyRet"].abs() / dollar[keep]).mean())


def e2_gates(eligible: int, linked: int, listed: int, listed_linked: int,
             cells: dict, pre_share: float, post_share: float) -> dict:
    """E2-G1 link coverage, E2-G3 cell size, E2-G4 differential coverage."""
    share = (listed_linked / listed) if listed else float("nan")
    g1 = bool(share >= E2_G1_MIN_COVERAGE)
    smallest = min(cells.values()) if cells else 0
    g3 = bool(smallest >= E2_G3_MIN_CELL)
    gap = abs(pre_share - post_share)
    g4 = bool(gap <= E2_G4_MAX_GAP)
    return {
        "E2-G1_link_coverage": {
            "listed_campaigns": int(listed),
            "listed_linked": int(listed_linked),
            "share": share,
            "threshold": E2_G1_MIN_COVERAGE,
            "verdict": "PASS" if g1 else "NO-GO",
        },
        "E2-G2_link_audit": {
            "verdict": "NOT RUN",
            "note": "sixty matched campaigns checked by an independent worker",
        },
        "E2-G3_cell_size": {
            "cells": {k: int(v) for k, v in sorted(cells.items())},
            "smallest": int(smallest),
            "threshold": E2_G3_MIN_CELL,
            "verdict": "PASS" if g3 else "NO-GO",
        },
        "E2-G4_differential_coverage": {
            "link_share_pre": pre_share,
            "link_share_post": post_share,
            "absolute_gap": gap,
            "threshold": E2_G4_MAX_GAP,
            "verdict": "PASS" if g4 else "NO-GO",
        },
    }


def run_e2(campaigns: pd.DataFrame, coverage: dict) -> dict:
    """Run-up and jump by pre-trigger liquidity tercile and period."""
    crsp = load_crsp()
    calendar = trading_calendar(crsp)
    mkt = market_return(crsp)
    by_cusip, by_ticker = build_link(crsp)
    tickers = cik_ticker_map()
    panels = {p: g.sort_values("DlyCalDt").set_index("DlyCalDt")
              for p, g in crsp.groupby("PERMNO")}

    rows = []
    counts = {"no_window": 0, "no_link": 0, "no_prices": 0, "no_liquidity": 0}
    for rec in campaigns.to_dict("records"):
        trigger = dt.date.fromisoformat(str(rec["trigger_date"]))
        filed = dt.date.fromisoformat(str(rec["date_filed"]))
        accepted = (dt.datetime.fromisoformat(str(rec["accepted"]))
                    if isinstance(rec["accepted"], str) else None)
        listed = str(rec["subject_cik"]).isdigit() and (
            str(int(rec["subject_cik"])) in tickers)
        react = reaction_day(filed, accepted, calendar)
        if react is None or react <= trigger:
            counts["no_window"] += 1
            rows.append({**rec, "listed": listed, "permno": None,
                         "link_route": None, "reaction_day": None,
                         "R": None, "J": None, "amihud": None})
            continue
        permno, route = link_campaign(rec["cusip8"], rec["subject_cik"],
                                      by_cusip, by_ticker, tickers)
        if permno is None or permno not in panels:
            counts["no_link"] += 1
            rows.append({**rec, "listed": listed, "permno": None,
                         "link_route": None,
                         "reaction_day": react.isoformat(),
                         "R": None, "J": None, "amihud": None})
            continue
        panel = panels[permno]
        r, j = runup_and_jump(panel, mkt, trigger, react)
        if r is None:
            counts["no_prices"] += 1
        a = amihud(panel, trigger)
        if a is None:
            counts["no_liquidity"] += 1
        rows.append({**rec, "listed": listed, "permno": int(permno),
                     "link_route": route, "reaction_day": react.isoformat(),
                     "R": r, "J": j, "amihud": a})

    table = pd.DataFrame(rows)
    linked = table["R"].notna() & table["J"].notna()
    listed_mask = table["listed"].astype(bool)
    sample = table[linked & table["amihud"].notna()].copy()
    if len(sample):
        sample["tercile"] = pd.qcut(sample["amihud"], 3,
                                    labels=["liquid", "middle", "illiquid"])

    cells: dict[str, int] = {}
    cell_stats: dict[str, dict] = {}
    for tercile in ("liquid", "middle", "illiquid"):
        for period in ("pre", "post"):
            key = f"{tercile}|{period}"
            sub = sample[(sample.get("tercile") == tercile)
                         & (sample["period"] == period)] if len(sample) else sample
            cells[key] = int(len(sub))
            if not len(sub):
                cell_stats[key] = {"n": 0}
                continue
            r = sub["R"].to_numpy(dtype=float)
            j = sub["J"].to_numpy(dtype=float)
            mean_r, mean_j = float(np.mean(r)), float(np.mean(j))
            denom = mean_r + mean_j
            cell_stats[key] = {
                "n": int(len(sub)),
                "R": describe(r),
                "J": describe(j),
                "R_ci": bootstrap_statistic(r, np.mean),
                "J_ci": bootstrap_statistic(j, np.mean),
                "runup_share_of_cell_means": (mean_r / denom
                                              if denom != 0 else None),
                "runup_share_ci": _bootstrap_ratio(r, j),
            }

    pre_listed = table[listed_mask & (table["period"] == "pre")]
    post_listed = table[listed_mask & (table["period"] == "post")]
    pre_share = (float((pre_listed["R"].notna() & pre_listed["J"].notna()).mean())
                 if len(pre_listed) else float("nan"))
    post_share = (float((post_listed["R"].notna() & post_listed["J"].notna()).mean())
                  if len(post_listed) else float("nan"))
    gates = e2_gates(int(len(table)), int(linked.sum()), int(listed_mask.sum()),
                     int((linked & listed_mask).sum()), cells,
                     pre_share, post_share)
    verdicts = [g["verdict"] for g in gates.values()]
    status = ("NO-GO" if "NO-GO" in verdicts
              else ("PENDING" if "NOT RUN" in verdicts else "GO"))

    cov = dict(coverage)
    cov.update({
        "no_window": counts["no_window"],
        "no_link": counts["no_link"],
        "no_prices": counts["no_prices"],
        "no_liquidity": counts["no_liquidity"],
        "listed_share": (float(listed_mask.mean()) if len(table)
                         else float("nan")),
        "linked": int(linked.sum()),
    })
    result = {
        "exercise": "e2",
        "object": "run-up R and jump J by pre-trigger liquidity",
        "spec": SPEC,
        "label": "ESTIMATED",
        "design": "descriptive",
        "causal_claim": False,
        "coverage": cov,
        "cells": cell_stats,
        "gates": gates,
        "status": status,
        "headline_suppressed": status == "NO-GO",
    }
    os.makedirs(OUT_DIR, exist_ok=True)
    table.to_csv(os.path.join(OUT_DIR, "e2_campaigns.csv"), index=False)
    with open(os.path.join(OUT_DIR, "e2_estimate.json"), "w") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)
    plot_e2(sample)
    return result


def _bootstrap_ratio(r: np.ndarray, j: np.ndarray, seed: int = BOOT_SEED,
                     n_boot: int = N_BOOT) -> dict:
    """Interval for mean R over (mean R plus mean J), resampling campaigns."""
    if not len(r):
        return {"point": None, "ci_low": None, "ci_high": None,
                "n_boot": n_boot, "seed": seed}
    rng = np.random.default_rng(seed)
    draws = np.empty(n_boot)
    for b in range(n_boot):
        pick = rng.integers(0, len(r), size=len(r))
        mr, mj = float(np.mean(r[pick])), float(np.mean(j[pick]))
        draws[b] = mr / (mr + mj) if (mr + mj) != 0 else np.nan
    draws = draws[np.isfinite(draws)]
    mr, mj = float(np.mean(r)), float(np.mean(j))
    return {
        "point": mr / (mr + mj) if (mr + mj) != 0 else None,
        "ci_low": float(np.percentile(draws, 2.5)) if len(draws) else None,
        "ci_high": float(np.percentile(draws, 97.5)) if len(draws) else None,
        "n_boot": n_boot,
        "seed": seed,
    }


def plot_e2(sample: pd.DataFrame) -> None:
    """Run-up share by tercile and period."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(5.5, 3.4))
    terciles = ["liquid", "middle", "illiquid"]
    width = 0.38
    for offset, (period, colour) in enumerate((("pre", "#4477aa"),
                                               ("post", "#ee6677"))):
        heights = []
        for tercile in terciles:
            sub = (sample[(sample.get("tercile") == tercile)
                          & (sample["period"] == period)]
                   if len(sample) else sample)
            if not len(sub):
                heights.append(np.nan)
                continue
            mr = float(np.mean(sub["R"].to_numpy(dtype=float)))
            mj = float(np.mean(sub["J"].to_numpy(dtype=float)))
            heights.append(mr / (mr + mj) if (mr + mj) != 0 else np.nan)
        ax.bar(np.arange(3) + (offset - 0.5) * width, heights, width=width,
               color=colour, label=period)
    ax.set_xticks(np.arange(3))
    ax.set_xticklabels(terciles)
    ax.set_xlabel("Pre-trigger liquidity tercile")
    ax.set_ylabel("Run-up share of the cell means")
    ax.legend(fontsize=8, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "e2_runup_jump.pdf"))
    plt.close(fig)


# ---------------------------------------------------------------------------
# Rendering: the strings the paper carries
# ---------------------------------------------------------------------------

def _pct(x, digits: int = 1) -> str:
    return "" if x is None else f"{100.0 * float(x):.{digits}f}"


def _num(x, digits: int = 1) -> str:
    return "" if x is None else f"{float(x):.{digits}f}"


def render_e1(result: dict) -> dict[str, str]:
    """Every E1 number the paper may print, as the exact string it prints."""
    if result.get("status") == "NO-GO":
        return {}
    out: dict[str, str] = {}
    for period in ("pre", "post"):
        block = result["by_period"][period]
        out[f"e1_{period}_n"] = str(block["n"])
        out[f"e1_{period}_mean"] = _num(block["mean"], 1)
        out[f"e1_{period}_median"] = _num(block["median"], 1)
        out[f"e1_{period}_p25"] = _num(block["p25"], 1)
        out[f"e1_{period}_p75"] = _num(block["p75"], 1)
    for year, block in sorted(result["by_year"].items()):
        if not block["n"]:
            continue
        out[f"e1_{year}_n"] = str(block["n"])
        out[f"e1_{year}_mean"] = _num(block["mean"], 1)
        out[f"e1_{year}_median"] = _num(block["median"], 1)
        out[f"e1_{year}_p25"] = _num(block["p25"], 1)
        out[f"e1_{year}_p75"] = _num(block["p75"], 1)
    for stat in ("mean", "median"):
        d = result["difference"][stat]
        out[f"e1_diff_{stat}"] = _num(d["point"], 2)
        out[f"e1_diff_{stat}_ci_low"] = _num(d["ci_low"], 2)
        out[f"e1_diff_{stat}_ci_high"] = _num(d["ci_high"], 2)
    clock = result["clock"]["by_period"]
    for period in ("pre", "post"):
        out[f"clock_{period}_n"] = str(clock[period]["n"])
        out[f"clock_{period}_share_within5"] = _pct(clock[period]["share_within_5bd"])
        out[f"clock_{period}_median_delay"] = _num(clock[period]["median_delay_bdays"], 1)
        ci = clock[period]["share_within_5bd_ci"]
        out[f"clock_{period}_share_within5_ci_low"] = _pct(ci["ci_low"])
        out[f"clock_{period}_share_within5_ci_high"] = _pct(ci["ci_high"])
    for year, block in sorted(result["clock"]["by_year"].items()):
        if not block["n"]:
            continue
        out[f"clock_{year}_n"] = str(block["n"])
        out[f"clock_{year}_share_within5"] = _pct(block["share_within_5bd"])
        out[f"clock_{year}_median_delay"] = _num(block["median_delay_bdays"], 1)
    out["e1_campaigns"] = str(result["coverage"]["campaigns"])
    out["e1_stake_coverage"] = _pct(result["coverage"]["stake_share"])
    return out


def render_e2(result: dict) -> dict[str, str]:
    """Every E2 number the paper may print, as the exact string it prints."""
    if result.get("status") == "NO-GO":
        return {}
    out: dict[str, str] = {}
    for key, cell in sorted(result.get("cells", {}).items()):
        if not cell.get("n"):
            continue
        tag = "e2_" + key.replace("|", "_")
        out[tag + "_n"] = str(cell["n"])
        out[tag + "_mean_R"] = _pct(cell["R"]["mean"], 2)
        out[tag + "_mean_J"] = _pct(cell["J"]["mean"], 2)
        share = cell.get("runup_share_of_cell_means")
        if share is not None:
            out[tag + "_runup_share"] = _num(share, 2)
    return out


def load_result(exercise: str) -> dict | None:
    path = os.path.join(OUT_DIR, f"{exercise}_estimate.json")
    if not os.path.exists(path):
        return None
    with open(path) as fh:
        return json.load(fh)


def render(exercise: str) -> dict[str, str]:
    result = load_result(exercise)
    if result is None:
        return {}
    return render_e1(result) if exercise == "e1" else render_e2(result)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def cmd_build(args) -> int:
    _, campaigns, coverage = build(allow_fetch=not args.no_fetch)
    print("\ncoverage:")
    for key, value in coverage.items():
        print(f"  {key:26s} {value}")
    print("\ncampaigns by period:")
    print(campaigns.groupby("period").size().to_string())
    print("\ncampaigns by year:")
    print(campaigns.groupby("year").size().to_string())
    return 0


def cmd_run(args) -> int:
    campaigns, coverage = load_campaigns(allow_fetch=not args.no_fetch)
    result = (run_e1(campaigns, coverage) if args.exercise == "e1"
              else run_e2(campaigns, coverage))
    print(json.dumps({"status": result["status"],
                      "gates": result["gates"],
                      "coverage": result["coverage"]}, indent=2, sort_keys=True))
    return 0


def cmd_render(args) -> int:
    print(json.dumps(render(args.exercise), indent=2, sort_keys=True))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Campaign fingerprints: E1 and E2.")
    ap.add_argument("--no-fetch", action="store_true",
                    help="cache only; do not fetch a missing filing")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build").set_defaults(fn=cmd_build)
    run = sub.add_parser("run")
    run.add_argument("exercise", choices=("e1", "e2"))
    run.set_defaults(fn=cmd_run)
    ren = sub.add_parser("render")
    ren.add_argument("exercise", choices=("e1", "e2"))
    ren.set_defaults(fn=cmd_render)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
