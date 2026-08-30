"""Verification gates for the BID12 treated unit (handoff, 2026-08-30).

Mechanises the five gates the treated unit has to clear before anything
downstream may use its output, so the check is reproducible and its result is
a record rather than a claim:

1. the post-pass chain finished — ``== chain complete ==`` in its log, and no
   failure marker;
2. the fixture suite printed ``N/N checks passed`` with zero failures;
3. ``bid12_run_meta.json``'s ``rules_sha256`` equals the SHA-256 of
   ``research/empirics_v4/bid12_coding_rules.md``, the extraction is not
   missing firms, and the not-extracted count is present in the metadata
   rather than hidden;
4. the treated BID12 base rate **exceeds** Greenwood–Schor's 18.1% (SPEC
   §8.4). Ours counts failed and withdrawn bids too, so a lower rate is a red
   flag to investigate, not a result to carry forward;
5. the three treated CSVs and the run metadata exist and are mutually
   consistent (row counts, ambiguity accounting).

Exit status is 0 only if every gate passes. Gate 4 is a judgement gate: it
fails loudly rather than warning, because the handoff requires it to be
investigated before the leg proceeds.

Usage:
    .venv/bin/python -m empirics.bid12_gates
    .venv/bin/python -m empirics.bid12_gates --json empirics/output/bid12_gates.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re

import pandas as pd

from empirics import bid12

CHAIN_LOG = "/tmp/bid12_postpass_chain.log"
CHAIN_MARKER = "/tmp/bid12_chain_failed.marker"
GS_BASE_RATE = 0.181                     # SPEC §8.4, Greenwood-Schor Table 6

_results = []


def gate(name: str, ok: bool, detail: str) -> None:
    _results.append({"gate": name, "pass": bool(ok), "detail": detail})
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} — {detail}")


def check_chain(log_path: str = CHAIN_LOG) -> None:
    print("\n== gate 1: chain completion ==")
    if not os.path.exists(log_path):
        gate("chain log present", False, f"{log_path} absent")
        return
    with open(log_path) as fh:
        text = fh.read()
    gate("chain complete line", "== chain complete" in text,
         text.strip().splitlines()[-1] if text.strip() else "empty log")
    marker = os.path.exists(CHAIN_MARKER)
    detail = "no failure marker"
    if marker:
        with open(CHAIN_MARKER) as fh:
            detail = fh.read().strip()
    gate("no failure marker", not marker, detail)

    print("\n== gate 2: fixture suite ==")
    hits = re.findall(r"(\d+)/(\d+) checks passed(?:, (\d+) FAILED)?", text)
    if not hits:
        gate("fixture suite result in the chain log", False,
             "no 'N/N checks passed' line found")
        return
    passed, total, failed = hits[-1]
    gate("all fixtures passed", passed == total and not failed,
         f"{passed}/{total} checks passed"
         + (f", {failed} FAILED" if failed else ", 0 failures"))
    rc = re.findall(r"== fixture suite rc=(\d+)", text)
    if rc:
        gate("fixture suite exit status", rc[-1] == "0", f"rc={rc[-1]}")


def check_meta_and_outputs(out_dir: str = bid12.OUT_DIR) -> None:
    print("\n== gate 3: run metadata ==")
    meta_path = os.path.join(out_dir, "bid12_run_meta.json")
    if not os.path.exists(meta_path):
        gate("run metadata present", False, f"{meta_path} absent")
        return
    with open(meta_path) as fh:
        meta = json.load(fh)
    with open(bid12.RULEBOOK_PATH, "rb") as fh:
        rulebook_hash = hashlib.sha256(fh.read()).hexdigest()
    gate("rules_sha256 matches the rulebook on disk",
         meta.get("rules_sha256") == rulebook_hash,
         f"meta {str(meta.get('rules_sha256'))[:16]}… vs rulebook "
         f"{rulebook_hash[:16]}…")
    missing = meta.get("n_ciks_missing_extraction")
    gate("no CIK missing extraction", missing == 0,
         f"n_ciks_missing_extraction = {missing}")
    lookup = meta.get("treated_lookup", {})
    gate("not-extracted count is reported, not hidden",
         "bid12_not_extracted" in lookup,
         f"bid12_not_extracted = {lookup.get('bid12_not_extracted')}, "
         f"ambiguous = {lookup.get('bid12_empty_ambiguous')}")

    print("\n== gate 4: base rate against the SPEC §8.4 anchor ==")
    treated_csv = os.path.join(out_dir, "bid12_treated.csv")
    if not os.path.exists(treated_csv):
        gate("treated CSV present", False, f"{treated_csv} absent")
        return
    df = pd.read_csv(treated_csv, dtype={"cik": str})
    coded = df[df["bid12"].notna()]
    rate = float(coded["bid12"].mean()) if len(coded) else float("nan")
    gate(f"treated BID12 base rate exceeds {GS_BASE_RATE:.1%}",
         rate > GS_BASE_RATE,
         f"{rate:.4f} on {len(coded)} coded rows of {len(df)} "
         f"(ours counts failed and withdrawn bids, so it should exceed the "
         f"Greenwood-Schor 'acquired within 12 months' anchor)")

    print("\n== gate 5: output consistency ==")
    for name in ("bid12_events_treated.csv", "bid12_ambiguous_cases.csv"):
        p = os.path.join(out_dir, name)
        gate(f"{name} present", os.path.exists(p), p)
    gate("rows == metadata n_rows", lookup.get("n_rows") == len(df),
         f"meta {lookup.get('n_rows')} vs csv {len(df)}")
    n_amb = int((df["ambiguous"] == 1).sum())
    n_empty = int(df["bid12"].isna().sum())
    n_notext = int((df["extraction_status"] != "ok").sum())
    gate("every empty BID12 is either ambiguous or not-extracted",
         n_empty <= n_amb + n_notext,
         f"empty {n_empty}, ambiguous {n_amb}, not-extracted {n_notext}")
    # Rulebook §5.1 item 5: "no in-window evidence => 0" presumes the search
    # ran, so an unextracted row must be empty, never a zero. This is the
    # check that fails on pre-repair output.
    bad = df[(df["extraction_status"] != "ok") & df["bid12"].notna()]
    gate("no unextracted row is coded 0 (rulebook §5.1 item 5)",
         len(bad) == 0,
         f"{len(bad)} unextracted rows carry a BID12 value")
    amb_bad = df[(df["ambiguous"] == 1) & df["bid12"].notna()]
    gate("no ambiguous row is forced to 0 or 1 (rulebook §7)",
         len(amb_bad) == 0,
         f"{len(amb_bad)} ambiguous rows carry a BID12 value")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--log", default=CHAIN_LOG)
    ap.add_argument("--out-dir", default=bid12.OUT_DIR)
    ap.add_argument("--json", default="")
    args = ap.parse_args(argv)

    check_chain(args.log)
    check_meta_and_outputs(args.out_dir)
    n_fail = sum(1 for r in _results if not r["pass"])
    print(f"\n{len(_results) - n_fail}/{len(_results)} gates passed"
          + (f", {n_fail} FAILED" if n_fail else ""))
    if args.json:
        with open(args.json, "w") as fh:
            json.dump({"checked_at": dt.datetime.now()
                       .isoformat(timespec="seconds"),
                       "gates": _results,
                       "all_passed": n_fail == 0}, fh, indent=1)
        print(f"wrote {args.json}")
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
