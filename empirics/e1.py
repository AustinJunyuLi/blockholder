"""E1: realised 13D filing delay around the Feb-2024 acceleration.

Registered specification: research/empirics_v4/e1_spec.md. Read it first; this
module implements it and adds no rule of its own.

Usage:
    .venv/bin/python -m empirics.e1 run
    .venv/bin/python -m empirics.e1 audit-sample
    .venv/bin/python -m empirics.e1 audit-report

Outputs (committed):
    empirics/output/e1_delays.csv     one row per enumerated accession
    empirics/output/e1_estimate.json  the single result authority
    empirics/output/e1_cdf.pdf        empirical CDF by period
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re

import numpy as np
import pandas as pd

from empirics.edgar_fetch import DATA_DIR, list_filings
from empirics.facts import FEDERAL_HOLIDAYS
from empirics.parse_13d import EVENT_LABEL, RE_TAG, parse_filing

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "output")
CACHE_DIR = os.path.join(DATA_DIR, "filings")

SEED = 20260901
N_BOOT = 2000
WITHIN = 5                     # business days, the primary threshold
TRUNCATION_BYTES = 400_000     # cached sources were fetched with this cap
CUTOFF = dt.time(17, 30)       # EDGAR same-day acceptance cut-off, America/New_York

WINDOWS = {"pre": [(2023, 2), (2023, 3)], "post": [(2024, 3), (2024, 4)]}

RE_ACCEPTANCE = re.compile(r"<ACCEPTANCE-DATETIME>\s*(\d{14})")


# -- sources -----------------------------------------------------------------

def cache_path(edgar_path: str) -> str:
    accession = os.path.basename(edgar_path)[:-4].replace("-", "")
    return os.path.join(CACHE_DIR, accession + ".txt")


def read_source(edgar_path: str) -> tuple[str | None, bool]:
    """Return (text, truncated). Local cache only; the population is complete."""
    path = cache_path(edgar_path)
    if not os.path.exists(path):
        return None, False
    size = os.path.getsize(path)
    with open(path, "r", encoding="latin-1") as fh:
        return fh.read(), size >= TRUNCATION_BYTES


# -- time --------------------------------------------------------------------

def parse_acceptance(text: str) -> dt.datetime | None:
    m = RE_ACCEPTANCE.search(text)
    if not m:
        return None
    try:
        return dt.datetime.strptime(m.group(1), "%Y%m%d%H%M%S")
    except ValueError:
        return None


def is_business_day(d: dt.date) -> bool:
    return bool(np.is_busday(np.datetime64(d, "D"), holidays=FEDERAL_HOLIDAYS))


def _busday(d: dt.date, offset: int, roll: str) -> dt.date:
    out = np.busday_offset(np.datetime64(d, "D"), offset, roll=roll,
                           holidays=FEDERAL_HOLIDAYS)
    return out.astype("datetime64[D]").astype(object)


def next_business_day(d: dt.date) -> dt.date:
    """The first business day strictly after d."""
    return _busday(d, 1, "forward") if is_business_day(d) else _busday(d, 0, "forward")


def effective_filing_date(accepted: dt.datetime) -> dt.date:
    """When the filing becomes public.

    Acceptance on a non-business day arrives at the next session, whatever the
    time. Acceptance after the 17:30 cut-off on a business day arrives at the
    following session. Otherwise it is public the same day.
    """
    day = accepted.date()
    if not is_business_day(day):
        return _busday(day, 0, "forward")
    if accepted.time() > CUTOFF:
        return _busday(day, 1, "forward")
    return day


def business_delay(trigger: dt.date, effective: dt.date) -> int:
    return int(np.busday_count(np.datetime64(trigger, "D"),
                               np.datetime64(effective, "D"),
                               holidays=FEDERAL_HOLIDAYS))


# -- enumeration and parsing -------------------------------------------------

def enumerate_population() -> list[dict]:
    """Unique accessions per window.

    form.idx is filer-indexed: one joint filing appears once per reporting
    person, under each person's CIK, all pointing at the same accession. Those
    rows are one document, so collapse on accession before parsing.
    """
    rows: list[dict] = []
    for window, quarters in WINDOWS.items():
        seen: dict[str, dict] = {}
        for year, qtr in quarters:
            idx = os.path.join(DATA_DIR, f"form_{year}_QTR{qtr}.idx")
            for r in list_filings(idx, form_types=("SC 13D",)):
                accession = os.path.basename(r["edgar_path"])[:-4]
                if accession not in seen:
                    seen[accession] = {**r, "window": window}
        rows.extend(seen[a] for a in sorted(seen))
    return rows


def build_record(row: dict) -> dict:
    """One enumerated accession, with a status and a reason code. Never dropped."""
    out = {**row, "accession": None, "trigger_date": None, "accepted": None,
           "effective_date": None, "delay_bdays": None, "subject_cik": None,
           "parse_route": None, "status": None, "reason": None}

    text, truncated = read_source(row["edgar_path"])
    if text is None:
        out["status"], out["reason"] = "unresolved", "source_missing"
        return out

    parsed = parse_filing(text)
    out["accession"] = parsed.get("accession")
    out["subject_cik"] = parsed.get("subject_cik")
    out["parse_route"] = "xml" if parsed.get("has_xml") else "text"

    accepted = parse_acceptance(text)
    if accepted is None:
        out["status"], out["reason"] = "unresolved", "no_acceptance_timestamp"
        return out
    out["accepted"] = accepted.isoformat()

    trigger = parsed.get("event")
    if trigger is None:
        out["status"] = "unresolved"
        out["reason"] = "truncated_source" if truncated else "no_trigger_date"
        return out

    if out["subject_cik"] is None:
        out["status"], out["reason"] = "unresolved", "no_subject_cik"
        return out

    effective = effective_filing_date(accepted)
    out["trigger_date"] = trigger.isoformat()
    out["effective_date"] = effective.isoformat()
    out["delay_bdays"] = business_delay(trigger, effective)
    out["status"], out["reason"] = "resolved", "ok"
    return out


def collapse_campaigns(df: pd.DataFrame) -> pd.DataFrame:
    """One row per (subject_cik, trigger_date); keep the earliest acceptance."""
    resolved = df[df["status"] == "resolved"].copy()
    resolved = resolved.sort_values(["accepted", "accession"])
    keep = resolved.drop_duplicates(subset=["subject_cik", "trigger_date"], keep="first")
    return keep


# -- estimands ---------------------------------------------------------------

def share_within(delays: np.ndarray) -> float:
    return float(np.mean(delays <= WITHIN)) if len(delays) else float("nan")


def bounds_for_period(delays: np.ndarray, n_unresolved: int) -> dict:
    """Worst-case bounds putting every unresolved campaign at both extremes."""
    n_elig = len(delays) + n_unresolved
    hits = int(np.sum(delays <= WITHIN))
    lo = hits / n_elig if n_elig else float("nan")
    hi = (hits + n_unresolved) / n_elig if n_elig else float("nan")
    low_med = np.concatenate([delays, np.full(n_unresolved, -1e9)])
    high_med = np.concatenate([delays, np.full(n_unresolved, 1e9)])
    return {
        "n_resolved": int(len(delays)),
        "n_unresolved": int(n_unresolved),
        "n_eligible": int(n_elig),
        "share_complete_case": share_within(delays),
        "share_lower": lo,
        "share_upper": hi,
        "median_complete_case": float(np.median(delays)) if len(delays) else float("nan"),
        "median_lower": float(np.median(low_med)) if n_elig else float("nan"),
        "median_upper": float(np.median(high_med)) if n_elig else float("nan"),
    }


def cluster_bootstrap_ci(pre: pd.DataFrame, post: pd.DataFrame) -> dict:
    """Percentile CI for the post-minus-pre share difference, clustered on subject."""
    rng = np.random.default_rng(SEED)
    draws = np.empty(N_BOOT)
    parts = {}
    for name, frame in (("pre", pre), ("post", post)):
        subjects = frame["subject_cik"].to_numpy()
        uniq, inverse = np.unique(subjects, return_inverse=True)
        buckets = [frame["delay_bdays"].to_numpy()[inverse == i] for i in range(len(uniq))]
        parts[name] = buckets
    for b in range(N_BOOT):
        vals = {}
        for name in ("pre", "post"):
            buckets = parts[name]
            pick = rng.integers(0, len(buckets), size=len(buckets))
            vals[name] = share_within(np.concatenate([buckets[i] for i in pick]))
        draws[b] = vals["post"] - vals["pre"]
    return {"difference_ci_low": float(np.percentile(draws, 2.5)),
            "difference_ci_high": float(np.percentile(draws, 97.5)),
            "n_boot": N_BOOT, "seed": SEED}


# -- gates -------------------------------------------------------------------

def evaluate_gates(pre: dict, post: dict) -> dict:
    diff_lower = post["share_lower"] - pre["share_upper"]
    diff_upper = post["share_upper"] - pre["share_lower"]
    g1 = diff_lower > 0

    pre_unres = pre["n_unresolved"] / pre["n_eligible"]
    post_unres = post["n_unresolved"] / post["n_eligible"]
    gap = abs(pre_unres - post_unres)
    g2 = gap <= 0.10

    return {
        "G1_worst_case_bound": {
            "difference_lower": diff_lower,
            "difference_upper": diff_upper,
            "verdict": "PASS" if g1 else "NO-GO",
        },
        "G2_differential_coverage": {
            "unresolved_share_pre": pre_unres,
            "unresolved_share_post": post_unres,
            "absolute_gap": gap,
            "threshold": 0.10,
            "verdict": "PASS" if g2 else "NO-GO",
        },
        "G3_parser_validation": {
            "verdict": "NOT RUN",
            "note": "run audit-sample, hand-code, commit, then audit-report",
        },
    }


# -- commands ----------------------------------------------------------------

def cmd_run(args) -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    rows = enumerate_population()
    print(f"enumerated {len(rows)} accessions")
    records = [build_record(r) for r in rows]
    df = pd.DataFrame(records)
    df.to_csv(os.path.join(OUT_DIR, "e1_delays.csv"), index=False)

    print("\nstatus by window:")
    print(pd.crosstab(df["window"], df["status"]).to_string())
    print("\nunresolved reasons:")
    print(df[df["status"] == "unresolved"].groupby(["window", "reason"]).size().to_string())

    camp = collapse_campaigns(df)
    per = {}
    for w in ("pre", "post"):
        res = camp[camp["window"] == w]
        n_unres = int(((df["window"] == w) & (df["status"] == "unresolved")).sum())
        per[w] = bounds_for_period(res["delay_bdays"].to_numpy(dtype=float), n_unres)

    gates = evaluate_gates(per["pre"], per["post"])
    ci = cluster_bootstrap_ci(camp[camp["window"] == "pre"], camp[camp["window"] == "post"])

    result = {
        "spec": "research/empirics_v4/e1_spec.md",
        "label": "descriptive",
        "causal_claim": False,
        "enumerated": {w: int((df["window"] == w).sum()) for w in ("pre", "post")},
        "campaigns": {w: int((camp["window"] == w).sum()) for w in ("pre", "post")},
        "per_period": per,
        "difference_complete_case": per["post"]["share_complete_case"] - per["pre"]["share_complete_case"],
        "inference": ci,
        "gates": gates,
        "headline_suppressed": gates["G1_worst_case_bound"]["verdict"] != "PASS"
        or gates["G2_differential_coverage"]["verdict"] != "PASS",
    }
    with open(os.path.join(OUT_DIR, "e1_estimate.json"), "w") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)

    _plot_cdf(camp)
    print("\n" + json.dumps({k: result[k] for k in
                             ("difference_complete_case", "inference", "gates",
                              "headline_suppressed")}, indent=2))
    return 0


def _plot_cdf(camp: pd.DataFrame) -> None:
    import sys
    sys.path.insert(0, os.path.join(HERE, ".."))
    from pyfig import style
    style.apply_style()
    fig, ax = style.new_ax()
    for w, colour in (("pre", "#4477aa"), ("post", "#ee6677")):
        d = np.sort(camp[camp["window"] == w]["delay_bdays"].to_numpy(dtype=float))
        if not len(d):
            continue
        ax.step(d, np.arange(1, len(d) + 1) / len(d), where="post",
                color=colour, label=f"{w} (n={len(d)})")
    ax.axvline(WITHIN, color="black", linestyle="--", linewidth=0.6)
    ax.set_xlim(-2, 40)
    ax.set_xlabel("Filing delay (business days)")
    ax.set_ylabel("Empirical CDF")
    ax.legend(fontsize=8)
    style.save_fig(fig, os.path.join(OUT_DIR, "e1_cdf.pdf"))


def cmd_audit_sample(args) -> int:
    """Emit 60 cases with source excerpts and no parser answer."""
    df = pd.read_csv(os.path.join(OUT_DIR, "e1_delays.csv"))
    rng = np.random.default_rng(SEED)
    picks = []
    for w in ("pre", "post"):
        for route in ("xml", "text"):
            pool = df[(df["window"] == w) & (df["parse_route"] == route)]
            if pool.empty:
                continue
            take = min(15, len(pool))
            picks.append(pool.iloc[rng.choice(len(pool), size=take, replace=False)])
    sample = pd.concat(picks).sort_values(["window", "parse_route", "accession"])

    path = os.path.join(OUT_DIR, "e1_audit_cases.csv")
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["case_id", "window", "parse_route", "accession",
                    "excerpt", "coded_trigger_date", "coder"])
        for i, (_, r) in enumerate(sample.iterrows(), start=1):
            text, _ = read_source(r["edgar_path"])
            plain = RE_TAG.sub(" ", text or "")
            lab = EVENT_LABEL.search(plain)
            excerpt = (plain[max(0, lab.start() - 300):lab.end() + 100]
                       if lab else "LABEL NOT FOUND")
            excerpt = " ".join(excerpt.split())
            w.writerow([f"C{i:03d}", r["window"], r["parse_route"],
                        r["accession"], excerpt, "", ""])
    print(f"wrote {len(sample)} blind cases to {path}")
    print("hand-code coded_trigger_date (YYYY-MM-DD) and coder, then commit, "
          "then run audit-report")
    return 0


def cmd_audit_report(args) -> int:
    cases = pd.read_csv(os.path.join(OUT_DIR, "e1_audit_cases.csv"))
    df = pd.read_csv(os.path.join(OUT_DIR, "e1_delays.csv"))
    merged = cases.merge(df[["accession", "trigger_date", "window"]],
                         on="accession", how="left", suffixes=("", "_parsed"))
    coded = merged.dropna(subset=["coded_trigger_date"])
    if coded.empty:
        print("no hand-coded rows; nothing to report")
        return 1
    coded = coded.assign(
        error=coded["coded_trigger_date"].astype(str) != coded["trigger_date"].astype(str))
    n_err = int(coded["error"].sum())
    by_window = coded.groupby("window")["error"].sum().to_dict()
    verdict = "PASS" if n_err <= 3 else "NO-GO"
    report = {"n_coded": int(len(coded)), "material_errors": n_err,
              "errors_by_window": {k: int(v) for k, v in by_window.items()},
              "threshold": 3, "verdict": verdict}
    print(json.dumps(report, indent=2))
    return 0 if verdict == "PASS" else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="E1 filing-delay comparison.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("run").set_defaults(fn=cmd_run)
    sub.add_parser("audit-sample").set_defaults(fn=cmd_audit_sample)
    sub.add_parser("audit-report").set_defaults(fn=cmd_audit_report)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
