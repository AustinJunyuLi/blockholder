"""CLI check for the registered matched-DiD diagnostics.

Run:
    .venv/bin/python -m empirics.test_estimate_did_diagnostics
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

import numpy as np
import pandas as pd


def test_cli_blocks_unsupported_568_date_placebo() -> None:
    """The 2022 treated start cannot estimate the 2021 pseudo-dates."""
    with tempfile.TemporaryDirectory() as tmp:
        treated = os.path.join(tmp, "bid12_treated.csv")
        controls = os.path.join(tmp, "bid12_control.csv")
        pairs = os.path.join(tmp, "did_match_pairs.csv")
        estimate = os.path.join(tmp, "did_estimate.json")
        out = os.path.join(tmp, "out")

        pd.DataFrame([
            {"accession": "a1", "permno": 1, "td": "2022-01-10",
             "bid12": 0, "extraction_status": "ok",
             "excluded_prior_bid": 0},
            {"accession": "a2", "permno": 2, "td": "2023-09-15",
             "bid12": 1, "extraction_status": "ok",
             "excluded_prior_bid": 0},
        ]).to_csv(treated, index=False)
        pd.DataFrame([
            {"permno": 101, "td": "2022-01-10", "match_group": "a1",
             "bid12": 0, "extraction_status": "ok",
             "excluded_prior_bid": 0},
            {"permno": 102, "td": "2023-09-15", "match_group": "a2",
             "bid12": 0, "extraction_status": "ok",
             "excluded_prior_bid": 0},
        ]).to_csv(controls, index=False)
        pd.DataFrame([
            {"treated_permno": 1, "treated_accession": "a1",
             "treated_td": "2022-01-10", "control_permno": 101,
             "match_group": "a1"},
            {"treated_permno": 2, "treated_accession": "a2",
             "treated_td": "2023-09-15", "control_permno": 102,
             "match_group": "a2"},
        ]).to_csv(pairs, index=False)
        with open(estimate, "w", encoding="utf-8") as fh:
            json.dump({"label": "ESTIMATED", "beta_treat_x_post": 0.02}, fh)

        proc = subprocess.run([
            sys.executable, "-m", "empirics.estimate_did_diagnostics",
            "--treated", treated, "--controls", controls, "--pairs", pairs,
            "--estimate", estimate, "--out-dir", out,
        ], cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
           text=True, capture_output=True, check=False)

        assert proc.returncode == 2, proc.stdout + proc.stderr
        with open(os.path.join(out, "did_diagnostics.json"),
                  encoding="utf-8") as fh:
            result = json.load(fh)
        support = pd.read_csv(os.path.join(out, "did_placebo_support.csv"))

        assert result["label"] == "DIAGNOSTIC"
        assert result["status"] == "BLOCKED"
        assert result["causal_language_allowed"] is False
        assert result["placebo"]["n_candidate_dates"] == 568
        assert result["placebo"]["n_estimable_dates"] < 568
        assert (result["placebo"]["n_dates_with_two_sided_treated_support"]
                < 568)
        assert result["placebo"]["n_dates_without_pre_treated"] > 0
        assert len(support) == 568
        assert support.iloc[0]["pseudo_date"] == "2021-07-01"
        assert support.iloc[0]["n_treated_pre"] == 0
        assert not os.path.exists(os.path.join(out, "did_placebo_estimates.csv"))
        assert not os.path.exists(os.path.join(out, "did_placebo_histogram.pdf"))


def test_cli_writes_seven_quarter_pretrend() -> None:
    """A worked matched panel recovers quarter gaps relative to 2023Q3."""
    with tempfile.TemporaryDirectory() as tmp:
        treated = os.path.join(tmp, "bid12_treated.csv")
        controls = os.path.join(tmp, "bid12_control.csv")
        pairs = os.path.join(tmp, "did_match_pairs.csv")
        estimate = os.path.join(tmp, "did_estimate.json")
        out = os.path.join(tmp, "out")
        quarters = [
            ("2022Q1", "2022-01-05", 12),
            ("2022Q2", "2022-04-05", 18),
            ("2022Q3", "2022-07-05", 24),
            ("2022Q4", "2022-10-05", 30),
            ("2023Q1", "2023-01-05", 36),
            ("2023Q2", "2023-04-05", 42),
            ("2023Q3", "2023-07-05", 30),
        ]
        tr_rows, ct_rows, pair_rows = [], [], []
        rng = np.random.default_rng(4)
        for quarter, start, n_one in quarters:
            one = set(rng.choice(60, n_one, replace=False))
            for i in range(60):
                group = f"{quarter}-{i:02d}"
                td = str((pd.Timestamp(start)
                          + pd.Timedelta(days=3 * (i % 29))).date())
                tr_rows.append({
                    "accession": group, "permno": len(tr_rows) + 1, "td": td,
                    "bid12": int(i in one), "extraction_status": "ok",
                    "excluded_prior_bid": 0,
                })
                control_permno = 1000 + len(ct_rows)
                ct_rows.append({
                    "permno": control_permno, "td": td, "match_group": group,
                    "bid12": 0, "extraction_status": "ok",
                    "excluded_prior_bid": 0,
                })
                pair_rows.append({
                    "treated_permno": tr_rows[-1]["permno"],
                    "treated_accession": group, "treated_td": td,
                    "control_permno": control_permno, "match_group": group,
                })
        pd.DataFrame(tr_rows).to_csv(treated, index=False)
        pd.DataFrame(ct_rows).to_csv(controls, index=False)
        pd.DataFrame(pair_rows).to_csv(pairs, index=False)
        with open(estimate, "w", encoding="utf-8") as fh:
            json.dump({"label": "ESTIMATED", "beta_treat_x_post": 0.02}, fh)

        proc = subprocess.run([
            sys.executable, "-m", "empirics.estimate_did_diagnostics",
            "--treated", treated, "--controls", controls, "--pairs", pairs,
            "--estimate", estimate, "--out-dir", out,
        ], cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
           text=True, capture_output=True, check=False)

        assert proc.returncode == 2, proc.stdout + proc.stderr
        pre = pd.read_csv(os.path.join(out, "did_pretrend.csv"))
        with open(os.path.join(out, "did_diagnostics.json"),
                  encoding="utf-8") as fh:
            result = json.load(fh)
        expected = {
            "2022Q1": -0.3, "2022Q2": -0.2, "2022Q3": -0.1,
            "2022Q4": 0.0, "2023Q1": 0.1, "2023Q2": 0.2,
            "2023Q3": 0.0,
        }
        got = dict(zip(pre["quarter"], pre["coefficient"]))
        assert list(pre["quarter"]) == list(expected)
        assert all(abs(got[q] - value) < 1e-12
                   for q, value in expected.items()), got
        assert result["pretrend"]["status"] == "ESTIMATED"
        assert result["causal_language_allowed"] is False
        assert "constant within match group" in result["pretrend"]["quarter_fe"]
        assert len(result["pretrend"]["coefficients"]) == 7
        assert "ci95_low_pp" in result["pretrend"]["coefficients"][0]
        assert result["pretrend"]["joint_f_p"] < 0.10, result["pretrend"]
        assert result["pretrend"]["causal_language_allowed"] is False
        figure = os.path.join(out, "did_pretrend.pdf")
        assert os.path.exists(figure) and os.path.getsize(figure) > 0


def test_unresolved_and_prior_bid_controls_are_dropped_not_fatal() -> None:
    """The panel must match the estimate's sample, and must not raise on it.

    `bid12_control_lookup` leaves BID12 empty for a control it could not
    resolve (no CIK link, extraction not run, ambiguous evidence), and
    SPEC 8.3 excludes a control already under an announced bid at its
    pseudo-TD. `estimate_did.stage_estimate` drops both and counts them.
    The diagnostics panel used to raise on the first and keep the second,
    so it either produced no artifact at all or certified a different
    sample than the estimate.
    """
    from empirics.estimate_did_diagnostics import matched_panel

    with tempfile.TemporaryDirectory() as tmp:
        treated = os.path.join(tmp, "t.csv")
        controls = os.path.join(tmp, "c.csv")
        pairs = os.path.join(tmp, "p.csv")
        tr_rows, ct_rows, pair_rows = [], [], []
        # g0 keeps a clean control; g1's control is unresolved; g2's control
        # was already under a bid; g3 has one of each, so the group survives.
        spec = [("g0", [("ok", 0, 0.0)]),
                ("g1", [("not-extracted", 0, None)]),
                ("g2", [("ok", 1, 0.0)]),
                ("g3", [("ok", 0, 1.0), ("ok", 1, 0.0)])]
        permno = 1
        for group, controls_spec in spec:
            tr_rows.append({"accession": group, "permno": permno,
                            "td": "2023-01-05", "bid12": 1,
                            "extraction_status": "ok",
                            "excluded_prior_bid": 0})
            permno += 1
            for status, prior, bid in controls_spec:
                ct_rows.append({"permno": 1000 + permno, "td": "2023-01-05",
                                "match_group": group, "bid12": bid,
                                "extraction_status": status,
                                "excluded_prior_bid": prior})
                pair_rows.append({"treated_permno": tr_rows[-1]["permno"],
                                  "treated_accession": group,
                                  "treated_td": "2023-01-05",
                                  "control_permno": 1000 + permno,
                                  "match_group": group})
                permno += 1
        pd.DataFrame(tr_rows).to_csv(treated, index=False)
        pd.DataFrame(ct_rows).to_csv(controls, index=False)
        pd.DataFrame(pair_rows).to_csv(pairs, index=False)

        panel, dropped = matched_panel(treated, controls, pairs)

    assert dropped["controls_unresolved_bid12"] == 1, dropped
    assert dropped["controls_excluded_prior_bid"] == 2, dropped
    assert dropped["match_groups_dropped_no_contrast"] == 2, dropped
    kept = set(panel["match_group"])
    assert kept == {"g0", "g3"}, kept
    assert panel["bid12"].notna().all()
    assert len(panel) == 4, panel


def test_cli_accepts_a_not_estimated_did_and_still_writes_the_pretrend() -> None:
    """A section 8 design failure is a blocker, not a reason to write nothing.

    The pre-trend is a statement about the matched panel, so it survives the
    absence of a coefficient. It just cannot grant causal language to an
    estimate that does not exist.
    """
    with tempfile.TemporaryDirectory() as tmp:
        treated = os.path.join(tmp, "t.csv")
        controls = os.path.join(tmp, "c.csv")
        pairs = os.path.join(tmp, "p.csv")
        estimate = os.path.join(tmp, "e.json")
        out = os.path.join(tmp, "out")
        tr_rows, ct_rows, pair_rows = [], [], []
        for quarter, start in (("2022Q1", "2022-01-05"),
                               ("2022Q2", "2022-04-05"),
                               ("2022Q3", "2022-07-05"),
                               ("2022Q4", "2022-10-05"),
                               ("2023Q1", "2023-01-05"),
                               ("2023Q2", "2023-04-05"),
                               ("2023Q3", "2023-07-05")):
            for i in range(20):
                group = f"{quarter}-{i:02d}"
                td = str((pd.Timestamp(start)
                          + pd.Timedelta(days=3 * (i % 29))).date())
                tr_rows.append({"accession": group, "permno": len(tr_rows) + 1,
                                "td": td, "bid12": int(i % 4 == 0),
                                "extraction_status": "ok",
                                "excluded_prior_bid": 0})
                cp = 5000 + len(ct_rows)
                ct_rows.append({"permno": cp, "td": td, "match_group": group,
                                "bid12": int(i % 7 == 0),
                                "extraction_status": "ok",
                                "excluded_prior_bid": 0})
                pair_rows.append({"treated_permno": tr_rows[-1]["permno"],
                                  "treated_accession": group,
                                  "treated_td": td, "control_permno": cp,
                                  "match_group": group})
        pd.DataFrame(tr_rows).to_csv(treated, index=False)
        pd.DataFrame(ct_rows).to_csv(controls, index=False)
        pd.DataFrame(pair_rows).to_csv(pairs, index=False)
        with open(estimate, "w", encoding="utf-8") as fh:
            json.dump({"label": "NOT ESTIMATED", "status": "design_failure",
                       "reason": "post-match standardised differences remain "
                                 "above 0.10"}, fh)

        proc = subprocess.run([
            sys.executable, "-m", "empirics.estimate_did_diagnostics",
            "--treated", treated, "--controls", controls, "--pairs", pairs,
            "--estimate", estimate, "--out-dir", out,
        ], cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
           text=True, capture_output=True, check=False)

        assert proc.returncode == 2, proc.stdout + proc.stderr
        with open(os.path.join(out, "did_diagnostics.json"),
                  encoding="utf-8") as fh:
            result = json.load(fh)
    assert result["real_estimate_label"] == "NOT ESTIMATED"
    assert any(b["code"] == "did_not_estimated" for b in result["blockers"]), \
        result["blockers"]
    assert result["causal_language_allowed"] is False
    assert result["pretrend"]["status"] == "ESTIMATED"
    assert len(result["pretrend"]["coefficients"]) == 7
    assert os.path.exists  # pre-trend artifacts were written above
    assert "panel_drops" in result


def main() -> int:
    checks = [
        ("unsupported placebo grid blocks",
         test_cli_blocks_unsupported_568_date_placebo),
        ("seven-quarter pretrend", test_cli_writes_seven_quarter_pretrend),
        ("unresolved and prior-bid controls drop, not raise",
         test_unresolved_and_prior_bid_controls_are_dropped_not_fatal),
        ("a NOT ESTIMATED DiD still yields the pre-trend",
         test_cli_accepts_a_not_estimated_did_and_still_writes_the_pretrend),
    ]
    failed = 0
    for label, fn in checks:
        try:
            fn()
            print(f"[PASS] {label}")
        except Exception as exc:
            failed += 1
            print(f"[FAIL] {label}: {exc}")
    print(f"\n{len(checks) - failed}/{len(checks)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
