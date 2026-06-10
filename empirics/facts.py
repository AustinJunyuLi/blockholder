"""Fact 1: 13D disclosure-delay compression around the Feb-5-2024 rule.

Samples SC 13D originals from quarterly EDGAR indexes in a pre-rule window
(2023 Q2-Q3) and a post-rule window (2024 Q3-Q4), parses each filing's event
and filed dates, and summarizes the delay distribution (business days).

Usage:
    .venv/bin/python -m empirics.facts --per-window 150
Outputs (committed):
    empirics/output/fact1_filings.csv     -- parsed per-filing rows
    empirics/output/fact1_summary.csv     -- window-level summary stats
    empirics/output/fact1_delay.pdf       -- distribution figure
"""

from __future__ import annotations

import argparse
import os

import numpy as np
import pandas as pd

from empirics.edgar_fetch import (
    DATA_DIR,
    download_form_index,
    fetch_filing_text,
    list_filings,
)
from empirics.parse_13d import parse_filing

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "output")

RULE_DATE = pd.Timestamp("2024-02-05")  # 5-business-day deadline compliance
WINDOWS = {
    "pre (2023Q2-Q3, 10-calendar-day rule)": [(2023, 2), (2023, 3)],
    "post (2024Q3-Q4, 5-business-day rule)": [(2024, 3), (2024, 4)],
}


def sample_window(label: str, quarters: list, per_window: int,
                  rng: np.random.Generator) -> list:
    rows = []
    for year, qtr in quarters:
        idx_path = download_form_index(year, qtr)
        rows.extend([dict(r, window=label) for r in
                     list_filings(idx_path, form_types=("SC 13D",))])
    if len(rows) > per_window:
        keep = rng.choice(len(rows), size=per_window, replace=False)
        rows = [rows[i] for i in sorted(keep)]
    print(f"{label}: {len(rows)} filings sampled")
    parsed = []
    for i, r in enumerate(rows):
        try:
            text = fetch_filing_text(r["edgar_path"])
            p = parse_filing(text)
        except Exception as exc:
            p = {"error": str(exc)}
        parsed.append({**r, **p})
        if (i + 1) % 25 == 0:
            print(f"  ... {i + 1}/{len(rows)}")
    return parsed


def business_delay(event, filed) -> float:
    if pd.isna(event) or pd.isna(filed):
        return np.nan
    return float(np.busday_count(np.datetime64(event, "D"),
                                 np.datetime64(filed, "D")))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Fact 1: 13D delay compression.")
    ap.add_argument("--per-window", type=int, default=150)
    ap.add_argument("--seed", type=int, default=20260610)
    args = ap.parse_args(argv)

    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)
    rng = np.random.default_rng(args.seed)

    parsed = []
    for label, quarters in WINDOWS.items():
        parsed.extend(sample_window(label, quarters, args.per_window, rng))

    df = pd.DataFrame(parsed)
    df["event"] = pd.to_datetime(df.get("event"), errors="coerce")
    df["filed"] = pd.to_datetime(df.get("filed"), errors="coerce")
    df["delay_bdays"] = [business_delay(e, f) for e, f in zip(df["event"], df["filed"])]
    df["delay_cdays"] = (df["filed"] - df["event"]).dt.days
    df.to_csv(os.path.join(OUT_DIR, "fact1_filings.csv"), index=False)

    ok = df.dropna(subset=["delay_bdays"])
    ok = ok[(ok["delay_bdays"] >= 0) & (ok["delay_bdays"] <= 60)]  # filter parse junk
    summary = (ok.groupby("window")["delay_bdays"]
               .agg(["count", "mean", "median",
                     lambda s: float(np.quantile(s, 0.9)),
                     lambda s: float(np.mean(s <= 5)),
                     lambda s: float(np.mean(s <= 10))])
               .rename(columns={"<lambda_0>": "p90",
                                "<lambda_1>": "share_within_5bd",
                                "<lambda_2>": "share_within_10bd"}))
    summary["parse_rate"] = df.groupby("window")["delay_bdays"].apply(
        lambda s: float(s.notna().mean()))
    summary.to_csv(os.path.join(OUT_DIR, "fact1_summary.csv"))
    print("\n", summary.to_string())

    # figure
    import sys
    sys.path.insert(0, os.path.join(HERE, ".."))
    from pyfig import style
    style.apply_style()
    import matplotlib.pyplot as plt
    fig, ax = style.new_ax()
    bins = np.arange(-0.5, 30.5, 1.0)
    for (label, sub), color in zip(ok.groupby("window"), ("#4477aa", "#ee6677")):
        ax.hist(sub["delay_bdays"], bins=bins, density=True, alpha=0.55,
                color=color, label=f"{label} (n={len(sub)})")
    ax.axvline(5, color="black", linestyle="--", linewidth=0.6)
    ax.text(5.2, ax.get_ylim()[1] * 0.95, "5 business days", fontsize=8, va="top")
    ax.set_xlabel("Disclosure delay: filing date − event date (business days)")
    ax.set_ylabel("Density")
    ax.set_title("Fact 1: 13D Disclosure-Delay Compression (2024 acceleration)")
    ax.legend(fontsize=8)
    style.save_fig(fig, os.path.join(OUT_DIR, "fact1_delay.pdf"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
