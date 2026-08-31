"""Synthetic CLI-seam check for the BID12 blind-audit sampler.

No live outputs, audit keys, caches, or network calls are touched.

Run:
    .venv/bin/python -m empirics.test_bid12_audit_sample
"""

from __future__ import annotations

import json
import os
import tempfile
from unittest import mock

import pandas as pd

from empirics import bid12_audit_sample as sampler

PASS, FAIL = "PASS", "FAIL"
_results: list[tuple[str, bool, str]] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    _results.append((label, bool(condition), detail))
    print(f"  [{PASS if condition else FAIL}] {label}"
          + (f" — {detail}" if detail and not condition else ""))


def _lookup_rows(side: str) -> pd.DataFrame:
    rows = []
    base = 1_000_000 if side == "treated" else 2_000_000
    for post in (False, True):
        for i in range(12):
            cik = f"{base + post * 100 + i:010d}"
            td = f"{2024 if post else 2023}-03-15"
            accession = f"{cik}-23-{i:06d}"
            rows.append({
                "cik": cik,
                "subject_name": f"{side.upper()} {i}",
                "td": td,
                "accession": accession,
                "treated_accession": accession,
                "bid12": i % 2,
                "ambiguous": 0,
                "n_bid_events": i % 2,
                "excluded_prior_bid": 0,
                "prior_bid_any": 0,
                "filer_own_bid": 0,
                "extraction_status": "ok",
                "window_coverage": "complete",
            })
    if side == "control":
        rows.append({
            "cik": "0099999999",
            "subject_name": "UNRESOLVED CONTROL",
            "td": "2023-03-15",
            "treated_accession": "0099999999-23-000001",
            "bid12": "",
            "ambiguous": 0,
            "n_bid_events": 0,
            "excluded_prior_bid": 0,
            "prior_bid_any": 0,
            "filer_own_bid": 0,
            "extraction_status": "not-extracted",
            "window_coverage": "missing",
        })
    return pd.DataFrame(rows)


def _identities(df: pd.DataFrame, side: str) -> set[tuple[str, str]]:
    part = df[df["side"] == side]
    return set(zip(part["cik"].astype(str), part["td"].astype(str)))


def test_cli_contract() -> None:
    print("\n== audit sampler CLI contract ==")
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = os.path.join(tmp, "out")
        os.makedirs(out_dir)
        treated_csv = os.path.join(tmp, "treated.csv")
        control_csv = os.path.join(tmp, "control.csv")
        rulebook = os.path.join(tmp, "rulebook.md")
        paths = {
            "OUT_DIR": out_dir,
            "TREATED_CSV": treated_csv,
            "CONTROL_CSV": control_csv,
            "AMBIG_TREATED": os.path.join(tmp, "ambig-treated.csv"),
            "AMBIG_CONTROL": os.path.join(tmp, "ambig-control.csv"),
            "PAIRS_OUT": os.path.join(out_dir, "pairs.csv"),
            "KEY_OUT": os.path.join(out_dir, "key.csv"),
            "MANIFEST_OUT": os.path.join(out_dir, "manifest.json"),
        }
        _lookup_rows("treated").to_csv(treated_csv, index=False)
        with open(rulebook, "w") as fh:
            fh.write("synthetic rulebook\n")

        with (mock.patch.multiple(sampler, **paths),
              mock.patch.object(sampler.bid12, "RULEBOOK_PATH", rulebook),
              mock.patch.object(sampler.bid12, "HERE", tmp)):
            status = sampler.main(["--side", "both", "--seed", "19"])
            check("both hard-fails when either lookup is absent", status == 1,
                  f"status={status}")
            check("failed both draw writes no audit artifacts",
                  not os.listdir(out_dir), str(os.listdir(out_dir)))

            # Remove artifacts left by the intentionally red implementation,
            # then exercise repeat runs against complete synthetic lookups.
            for name in os.listdir(out_dir):
                os.unlink(os.path.join(out_dir, name))
            _lookup_rows("control").to_csv(control_csv, index=False)

            control_status = sampler.main(
                ["--side", "control", "--seed", "19"])
            control_pairs = pd.read_csv(paths["PAIRS_OUT"], dtype={"cik": str})
            with open(paths["MANIFEST_OUT"]) as fh:
                control_manifest = json.load(fh)
            control_ids = _identities(control_pairs, "control")
            check("control-only draw succeeds", control_status == 0)
            check("control filtering is recorded for this run only",
                  control_manifest["rows_excluded_before_draw"]
                  == {"control_rows_not_auditable": 1},
                  str(control_manifest["rows_excluded_before_draw"]))

            treated_status = sampler.main(
                ["--side", "treated", "--seed", "19"])
            treated_pairs = pd.read_csv(paths["PAIRS_OUT"], dtype={"cik": str})
            with open(paths["MANIFEST_OUT"]) as fh:
                treated_manifest = json.load(fh)
            treated_ids = _identities(treated_pairs, "treated")
            check("treated-only draw succeeds", treated_status == 0)
            # A later draw replaces its own side's filtering record and keeps
            # the other side's, because the pairs and key files still carry
            # the other side's rows and the manifest describes those files.
            check("a treated redraw keeps the control record and adds none "
                  "of its own",
                  treated_manifest["rows_excluded_before_draw"]
                  == {"control_rows_not_auditable": 1},
                  str(treated_manifest["rows_excluded_before_draw"]))
            with open(paths["MANIFEST_OUT"]) as fh:
                probe = json.load(fh)
            probe["rows_excluded_before_draw"]["treated_stale_probe"] = 9
            with open(paths["MANIFEST_OUT"], "w") as fh:
                json.dump(probe, fh)
            sampler.main(["--side", "treated", "--seed", "19"])
            with open(paths["MANIFEST_OUT"]) as fh:
                redrawn = json.load(fh)
            check("a treated redraw drops a stale treated-side record",
                  "treated_stale_probe"
                  not in redrawn["rows_excluded_before_draw"],
                  str(redrawn["rows_excluded_before_draw"]))

            both_status = sampler.main(["--side", "both", "--seed", "19"])
            both_pairs = pd.read_csv(paths["PAIRS_OUT"], dtype={"cik": str})
            with open(paths["MANIFEST_OUT"]) as fh:
                both_manifest = json.load(fh)
            check("complete both draw succeeds and contains 30 pairs",
                  both_status == 0 and len(both_pairs) == 30,
                  f"status={both_status}, n={len(both_pairs)}")
            check("treated split composes into the both draw",
                  treated_ids == _identities(both_pairs, "treated"))
            check("control split composes into the both draw",
                  control_ids == _identities(both_pairs, "control"))
            check("both is stamped as one complete draw",
                  both_manifest["single_draw"] is True)
            check("registered 8/7 cell targets are unchanged",
                  both_manifest["cell_targets"] == {
                      "treated_pre": 8, "treated_post": 7,
                      "control_pre": 8, "control_post": 7,
                  }, str(both_manifest["cell_targets"]))
            check("registered four-of-30 blocking threshold is unchanged",
                  ">= 4 of 30" in both_manifest["disagreement_rule"],
                  both_manifest["disagreement_rule"])
            check("auditor pairs remain verdict-free while key stays separate",
                  set(both_pairs.columns) == {
                      "side", "cell", "cik", "subject_name", "td", "accession",
                  } and os.path.exists(paths["KEY_OUT"]),
                  str(list(both_pairs.columns)))


def test_split_draw_preserves_other_side() -> None:
    print("\n== split draw keeps the other half ==")
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = os.path.join(tmp, "out")
        os.makedirs(out_dir)
        treated_csv = os.path.join(tmp, "treated.csv")
        control_csv = os.path.join(tmp, "control.csv")
        rulebook = os.path.join(tmp, "rulebook.md")
        paths = {
            "OUT_DIR": out_dir,
            "TREATED_CSV": treated_csv,
            "CONTROL_CSV": control_csv,
            "AMBIG_TREATED": os.path.join(tmp, "ambig-treated.csv"),
            "AMBIG_CONTROL": os.path.join(tmp, "ambig-control.csv"),
            "PAIRS_OUT": os.path.join(out_dir, "pairs.csv"),
            "KEY_OUT": os.path.join(out_dir, "key.csv"),
            "MANIFEST_OUT": os.path.join(out_dir, "manifest.json"),
        }
        _lookup_rows("treated").to_csv(treated_csv, index=False)
        _lookup_rows("control").to_csv(control_csv, index=False)
        with open(rulebook, "w") as fh:
            fh.write("synthetic rulebook\n")
        with (mock.patch.multiple(sampler, **paths),
              mock.patch.object(sampler.bid12, "RULEBOOK_PATH", rulebook),
              mock.patch.object(sampler.bid12, "HERE", tmp)):
            sampler.main(["--side", "treated", "--seed", "19"])
            treated_ids = _identities(
                pd.read_csv(paths["PAIRS_OUT"], dtype={"cik": str}), "treated")
            # A shortfall recorded when the treated half was drawn must
            # survive the control draw; the manifest is the audit's record
            # of what the draw could not fill.
            with open(paths["MANIFEST_OUT"]) as fh:
                m0 = json.load(fh)
            m0["cell_shortfalls_moved_to_paired_cell"]["treated_post"] = 2
            m0["rows_excluded_before_draw"]["treated_rows_probe"] = 5
            with open(paths["MANIFEST_OUT"], "w") as fh:
                json.dump(m0, fh)
            sampler.main(["--side", "control", "--seed", "19"])
            merged = pd.read_csv(paths["PAIRS_OUT"], dtype={"cik": str})
            key = pd.read_csv(paths["KEY_OUT"], dtype={"cik": str})
            with open(paths["MANIFEST_OUT"]) as fh:
                manifest = json.load(fh)
        check("control draw does not erase the treated half",
              treated_ids == _identities(merged, "treated")
              and len(_identities(merged, "control")) == 15,
              f"n={len(merged)} sides={sorted(set(merged['side']))}")
        check("merged split still has 30 pairs and four cells",
              len(merged) == 30
              and set(merged["cell"]) == {
                  "treated_pre", "treated_post", "control_pre", "control_post",
              })
        check("merged key has one verdict row per pair, no blank duplicates",
              len(key) == 30
              and not key.duplicated(subset=["side", "cik", "td"]).any()
              and key["bid12"].notna().all(),
              f"n={len(key)} "
              f"dups={int(key.duplicated(subset=['side', 'cik', 'td']).sum())} "
              f"blank_bid12={int(key['bid12'].isna().sum())}")
        check("merged key and merged pairs describe the same 30 pairs",
              _identities(key, "treated") == _identities(merged, "treated")
              and _identities(key, "control") == _identities(merged, "control"))
        check("the control draw keeps the treated half's manifest record",
              manifest["cell_shortfalls_moved_to_paired_cell"]
              .get("treated_post") == 2
              and manifest["rows_excluded_before_draw"]
              .get("treated_rows_probe") == 5,
              json.dumps(manifest["cell_shortfalls_moved_to_paired_cell"]))
        check("treated-half escalation is recorded, blocking stays 4 of 30",
              "3 or more" in manifest.get("treated_half_escalation", "")
              and ">= 4 of 30" in manifest["disagreement_rule"],
              str(manifest.get("treated_half_escalation")))


def main() -> int:
    test_cli_contract()
    test_split_draw_preserves_other_side()
    n_fail = sum(1 for _, ok, _ in _results if not ok)
    print(f"\n{len(_results) - n_fail}/{len(_results)} checks passed"
          + (f", {n_fail} FAILED" if n_fail else ""))
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
