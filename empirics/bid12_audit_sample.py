"""Blind hand-audit sampler for the BID12 coding (rulebook §10, SPEC §8.3).

Draws the registered 30 (firm, TD) pairs — stratified treated/control ×
{TD < 2024-02-05, TD ≥ 2024-02-05}, 7–8 per cell — and splits the draw into
two files that must be kept apart:

  * ``bid12_audit_pairs.csv``  — the **auditor's** input: CIK, firm name,
    trigger date, stratum, side.  It carries **no verdict, no flag and no
    event**, so an agent given this file plus the rulebook can re-derive
    BID12 from raw EDGAR without seeing the coder's answer.
  * ``bid12_audit_key.csv``    — the coder's verdicts for the same pairs,
    revealed only after the auditor's independent readings are recorded.

Rulebook §10 details this implements:

  * a cell short of observations draws its balance from its paired cell, and
    the shortfall is recorded in the manifest rather than silently rebalanced;
  * every ambiguous in-window case among the sampled firms is listed
    additionally, for adjudication — those rows do **not** count against the
    30;
  * the rulebook SHA-256 is stamped into the manifest, so the auditor can
    verify which version of the rule they are reading;
  * the draw is seeded and re-runnable: same inputs, same 30 pairs.

The control side can only be sampled once the control-side lookup has run
(controls have no trigger date of their own until matching supplies the
pseudo-TDs).  ``--side treated`` draws the treated half alone; the split is a
**documented deviation** from the single 30-draw, recorded in the manifest and
in the dated note under ``research/empirics_v4/`` — never a quiet cell drop.

Usage:
    .venv/bin/python -m empirics.bid12_audit_sample --side treated
    .venv/bin/python -m empirics.bid12_audit_sample --side both
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os

import pandas as pd

from empirics import bid12

OUT_DIR = bid12.OUT_DIR
TREATED_CSV = os.path.join(OUT_DIR, "bid12_treated.csv")
CONTROL_CSV = os.path.join(OUT_DIR, "bid12_control.csv")
AMBIG_TREATED = os.path.join(OUT_DIR, "bid12_ambiguous_cases.csv")
AMBIG_CONTROL = os.path.join(OUT_DIR, "bid12_control_ambiguous_cases.csv")
PAIRS_OUT = os.path.join(OUT_DIR, "bid12_audit_pairs.csv")
KEY_OUT = os.path.join(OUT_DIR, "bid12_audit_key.csv")
MANIFEST_OUT = os.path.join(OUT_DIR, "bid12_audit_manifest.json")

SEED = 20260830
RULE_DATE = "2024-02-05"
CELL_TARGET = {"treated_pre": 8, "treated_post": 7,
               "control_pre": 8, "control_post": 7}
_FILTERED: dict = {}
KEY_COLS = ["bid12", "ambiguous", "n_bid_events", "first_bid_date",
            "first_bid_form", "first_bid_route", "first_bid_accession",
            "excluded_prior_bid", "prior_bid_any", "filer_own_bid",
            "extraction_status", "window_coverage"]


def _load_side(side: str) -> pd.DataFrame:
    path = TREATED_CSV if side == "treated" else CONTROL_CSV
    if not os.path.exists(path):
        return pd.DataFrame()
    df = pd.read_csv(path, dtype={"cik": str})
    df["side"] = side
    if side == "control":
        # the control lookup names the firm by CIK only; keep the columns the
        # auditor needs and fill the rest so both sides share a schema
        df["subject_name"] = df.get("subject_name", "")
        df["accession"] = df.get("treated_accession", "")
        # Only coded rows are auditable: `no-cik-link` rows have no firm to
        # look up, and `not-extracted` rows are not coder output at all
        # (rulebook §5.1 item 5). The filter count goes in the manifest.
        n_before = len(df)
        df = df[df["extraction_status"] == "ok"].copy()
        _FILTERED["control_rows_not_auditable"] = n_before - len(df)
    df["cell"] = side + "_" + (df["td"].astype(str) >= RULE_DATE).map(
        {True: "post", False: "pre"})
    return df


def _draw(df: pd.DataFrame, cells: list, rng) -> tuple:
    """Draw the target per cell; a cell short of observations passes its
    balance to its **paired** cell on the same side (rulebook §10), and the
    shortfall is recorded rather than silently rebalanced."""
    # one row per (firm, TD): a firm with two triggers offers two candidate
    # pairs, which is what the rule audits
    pool = df.drop_duplicates(subset=["cik", "td"]).copy()
    picked_idx: list = []
    shortfall: dict = {}

    def take_from(cell: str, want: int) -> int:
        cand = pool[(pool["cell"] == cell) & (~pool.index.isin(picked_idx))]
        n = min(want, len(cand))
        if n:
            picked_idx.extend(
                rng.choice(cand.index.values, size=n, replace=False).tolist())
        return want - n

    sides = []
    for c in cells:
        side = c.rsplit("_", 1)[0]
        if side not in sides:
            sides.append(side)
    for side in sides:
        pair = [c for c in cells if c.rsplit("_", 1)[0] == side]
        # pass 1: each cell's own target
        deficit = {c: take_from(c, CELL_TARGET[c]) for c in pair}
        # pass 2: a cell's deficit is offered to its paired cell
        for c in pair:
            if not deficit[c]:
                continue
            other = [x for x in pair if x != c]
            moved = deficit[c]
            for o in other:
                moved = take_from(o, moved)
            shortfall[c] = moved          # still unfilled after borrowing
        for c in pair:
            shortfall.setdefault(c, 0)
    return pool.loc[picked_idx].copy(), shortfall


def main(argv=None) -> int:
    import numpy as np

    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--side", choices=("treated", "control", "both"),
                    default="both")
    ap.add_argument("--seed", type=int, default=SEED)
    args = ap.parse_args(argv)

    frames, cells = [], []
    for side in ("treated", "control"):
        if args.side not in (side, "both"):
            continue
        df = _load_side(side)
        if df.empty:
            print(f"{side} lookup not landed — cannot sample that side yet")
            if args.side == side:
                return 1
            continue
        frames.append(df)
        cells.extend([f"{side}_pre", f"{side}_post"])
    if not frames:
        return 1
    df = pd.concat(frames, ignore_index=True)

    rng = np.random.default_rng(args.seed)
    sample, shortfall = _draw(df, cells, rng)
    sample = sample.sort_values(["side", "cell", "cik", "td"])

    auditor_cols = ["side", "cell", "cik", "subject_name", "td", "accession"]
    for c in auditor_cols:
        if c not in sample.columns:
            sample[c] = ""
    sample[auditor_cols].to_csv(PAIRS_OUT, index=False)
    print(f"wrote {PAIRS_OUT}: {len(sample)} pairs "
          f"({sample['cell'].value_counts().to_dict()}) — auditor input, "
          f"carries no verdicts")

    key_cols = [c for c in KEY_COLS if c in sample.columns]
    sample[auditor_cols + key_cols].to_csv(KEY_OUT, index=False)
    print(f"wrote {KEY_OUT}: the coder's verdicts — reveal only after the "
          f"auditor's independent readings are recorded")

    # Ambiguous in-window cases among the sampled firms, listed additionally
    # for adjudication (rulebook §10: they do not count against the 30).
    amb_rows = []
    for path, side in ((AMBIG_TREATED, "treated"), (AMBIG_CONTROL, "control")):
        if not os.path.exists(path):
            continue
        a = pd.read_csv(path, dtype={"cik": str})
        if a.empty:
            continue
        want = set(sample[sample["side"] == side]["cik"].astype(str))
        hit = a[a["cik"].astype(str).isin(want)].copy()
        hit["side"] = side
        amb_rows.append(hit)
    amb = (pd.concat(amb_rows, ignore_index=True) if amb_rows
           else pd.DataFrame())
    amb_out = os.path.join(OUT_DIR, "bid12_audit_ambiguous.csv")
    amb.to_csv(amb_out, index=False)
    print(f"wrote {amb_out}: {len(amb)} ambiguous events among the sampled "
          f"firms (adjudicated, not counted against the 30)")

    rules_hash = ""
    if os.path.exists(bid12.RULEBOOK_PATH):
        with open(bid12.RULEBOOK_PATH, "rb") as fh:
            rules_hash = hashlib.sha256(fh.read()).hexdigest()
    manifest = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "seed": args.seed,
        "sides_drawn": sorted(set(sample["side"])),
        "single_draw": args.side == "both",
        "split_draw_note": None if args.side == "both" else (
            f"Only the {args.side} half was drawn: the other side's lookup "
            f"had not landed at draw time. Rulebook §10 expects a single "
            f"30-draw; this split is a documented deviation, recorded here "
            f"and in the dated note under research/empirics_v4/. The "
            f"remaining cells are drawn with the same seed once their "
            f"lookup lands, and no cell is dropped."),
        "cell_targets": CELL_TARGET,
        "cells_drawn": sample["cell"].value_counts().to_dict(),
        "cell_shortfalls_moved_to_paired_cell": shortfall,
        "rows_excluded_before_draw": dict(_FILTERED),
        "n_pairs": len(sample),
        "n_ambiguous_listed": len(amb),
        "rules_sha256": rules_hash,
        "rulebook": os.path.relpath(bid12.RULEBOOK_PATH, bid12.HERE),
        "disagreement_rule": "disagreement > 10% (>= 4 of 30) blocks the leg "
                             "(rulebook §10, SPEC §8.3/§8.9)",
        "blindness": "bid12_audit_pairs.csv is the auditor's only input "
                     "besides the rulebook; bid12_audit_key.csv is revealed "
                     "after the auditor's readings are recorded",
    }
    with open(MANIFEST_OUT, "w") as fh:
        json.dump(manifest, fh, indent=1)
    print(f"wrote {MANIFEST_OUT}")
    if any(v for v in shortfall.values()):
        print(f"  cell shortfalls (moved to the paired cell, rulebook §10): "
              f"{ {k: v for k, v in shortfall.items() if v} }")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
