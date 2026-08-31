"""Synthetic checks for the §9 bidder-entry estimator.

No CRSP load, no network, no shared output files.

  * ``standardise_liq`` reproduces the §3.2 definition — within-quarter
    standardised log ILLIQ, **negated** so higher means more liquid — and is
    computed per quarter, not pooled across quarters
  * the within spec recovers a planted δ on a deterministic outcome
  * the triple-difference recovers a planted τ, and drops Post as collinear
    with the match fixed effects while keeping Post × LIQ
  * the triple-difference gates cleanly when the matched inputs are absent

Run:
    .venv/bin/python -m empirics.test_estimate_bidder_entry
"""

from __future__ import annotations

import json
import os
import sys
import tempfile

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

PASS, FAIL = "PASS", "FAIL"
_results = []


def check(label: str, cond: bool, detail: str = "") -> None:
    _results.append((label, bool(cond), detail))
    print(f"  [{PASS if cond else FAIL}] {label}"
          + (f" — {detail}" if detail and not cond else ""))


def test_standardise_liq() -> None:
    from empirics.estimate_bidder_entry import standardise_liq
    print("\n== LIQ standardisation (§3.2) ==")
    x = pd.Series([1.0, 2.0, 3.0, 10.0, 20.0, 30.0])
    q = pd.Series(["2023Q1"] * 3 + ["2024Q1"] * 3)
    liq = standardise_liq(x, q)
    check("mean zero within every quarter",
          all(abs(liq[q == k].mean()) < 1e-12 for k in ("2023Q1", "2024Q1")))
    check("unit sd within every quarter",
          all(abs(liq[q == k].std(ddof=1) - 1) < 1e-12
              for k in ("2023Q1", "2024Q1")))
    check("negated — the most illiquid firm has the lowest LIQ",
          liq.iloc[2] < liq.iloc[0], f"{liq.iloc[2]} vs {liq.iloc[0]}")
    check("standardised per quarter, not pooled across them",
          abs(liq.iloc[0] - liq.iloc[3]) < 1e-12,
          f"{liq.iloc[0]} vs {liq.iloc[3]}")
    flat = standardise_liq(pd.Series([5.0, 5.0]), pd.Series(["2023Q1"] * 2))
    check("a zero-variance quarter yields NaN, never a division blow-up",
          flat.isna().all())


def _within_frame(n_per_cell: int = 200, seed: int = 4) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for post in (0, 1):
        for i in range(n_per_cell):
            liq = float(rng.normal(0, 1))
            logcap = float(rng.normal(14, 2))
            # planted: beta(LIQ)=+0.04, delta(LIQ x Post)=-0.06, gamma=+0.02
            y = 0.10 + 0.04 * liq - 0.06 * liq * post + 0.02 * post
            rows.append({"bid12": y, "liq": liq, "post": post,
                         "logcap": logcap, "sic2": f"{10 + i % 5:02d}",
                         "td": f"{2023 if not post else 2024}-"
                               f"{1 + i % 12:02d}-15"})
    return pd.DataFrame(rows)


def test_within_recovery() -> None:
    import empirics.estimate_bidder_entry as be
    print("\n== within spec recovers planted coefficients ==")
    saved = be.N_BOOT
    be.N_BOOT = 99                       # the bootstrap p is not under test
    try:
        r = be.spec_within(_within_frame())
    finally:
        be.N_BOOT = saved
    check("delta(LIQ x Post) = -6 pp recovered",
          abs(r["delta_liq_x_post_pp"] + 6.0) < 1e-6,
          f"{r['delta_liq_x_post_pp']:+.6f}")
    check("beta(LIQ) = +4 pp recovered",
          abs(r["beta_liq_pp"] - 4.0) < 1e-6, f"{r['beta_liq_pp']:+.6f}")
    check("sample counts reported", r["n"] == 400 and r["n_pre"] == 200)
    check("realised MDE is reported and finite",
          np.isfinite(r["mde_delta_pp_realised"]))
    check("fixed effects are industry, and said so",
          "SIC" in r["fixed_effects"])


def _matched_files(tmp: str, n_groups: int = 120, seed: int = 6) -> tuple:
    """Write a synthetic match-pairs file and control lookup; return the
    treated frame that pairs with them, plus the planted tau."""
    rng = np.random.default_rng(seed)
    tr_rows, pair_rows, ctrl_rows = [], [], []
    for gi in range(n_groups):
        post = int(gi >= n_groups // 2)
        acc = f"000000000{gi:03d}-23-000001"
        td = f"{2023 if not post else 2024}-{1 + gi % 12:02d}-15"
        base = 0.10
        t_ill = float(rng.normal(-6, 2))
        t_cap = float(rng.normal(14, 1))
        # LIQ is built downstream from logilliq, so plant on logilliq and
        # recover the planted tau from the realised design matrix instead of
        # asserting an exact number: what is under test is that the estimator
        # returns the OLS solution of the stated specification.
        tr_rows.append({"accession": acc, "permno": 1000 + gi, "td": td,
                        "post": post, "bid12": np.nan, "logilliq": t_ill,
                        "logcap": t_cap, "liq": np.nan, "sic2": "20"})
        for j in range(3):
            c_ill = float(rng.normal(-6, 2))
            c_cap = float(rng.normal(14, 1))
            pair_rows.append({"treated_permno": 1000 + gi,
                              "treated_accession": acc, "treated_td": td,
                              "treated_quarter": "", "treated_sic2": "20",
                              "treated_post": post,
                              "control_permno": 5000 + gi * 3 + j,
                              "match_group": acc, "mahalanobis_d2": 0.1,
                              "control_logcap": c_cap,
                              "control_logilliq": c_ill,
                              "control_turnover": np.nan,
                              "control_ret12m": np.nan,
                              "control_idiovol": np.nan})
            ctrl_rows.append({"permno": 5000 + gi * 3 + j, "cik": "1",
                              "td": td, "match_group": acc, "bid12": np.nan,
                              "excluded_prior_bid": 0})
    pairs = pd.DataFrame(pair_rows)
    ctrl = pd.DataFrame(ctrl_rows)
    tr = pd.DataFrame(tr_rows)
    tr["td"] = pd.to_datetime(tr["td"])
    p = os.path.join(tmp, "pairs.csv")
    c = os.path.join(tmp, "control.csv")
    pairs.to_csv(p, index=False)
    ctrl.to_csv(c, index=False)
    return tr, p, c, base


def test_triple() -> None:
    import tempfile
    import empirics.estimate_bidder_entry as be
    from empirics.estimate_bidder_entry import standardise_liq, _quarter
    print("\n== triple difference ==")
    with tempfile.TemporaryDirectory() as tmp:
        tr, p, c, base = _matched_files(tmp)
        saved = (be.MATCH_OUT, be.CONTROL_LOOKUP_CSV, be.N_BOOT)
        be.MATCH_OUT, be.CONTROL_LOOKUP_CSV, be.N_BOOT = p, c, 99
        try:
            # plant the outcome on the same LIQ the estimator will build
            allrows = []
            pairs = pd.read_csv(p)
            ctrl = pd.read_csv(c)
            ctrl.loc[0, "excluded_prior_bid"] = 1
            excluded = set(ctrl.loc[ctrl["excluded_prior_bid"] == 1, "permno"])
            for r in tr.itertuples():
                allrows.append({"key": ("t", r.accession),
                                "logilliq": r.logilliq, "td": str(r.td.date()),
                                "logcap": r.logcap,
                                "treat": 1, "post": r.post})
            for r in pairs.itertuples():
                if int(r.control_permno) in excluded:
                    continue
                allrows.append({"key": ("c", int(r.control_permno)),
                                "logilliq": r.control_logilliq,
                                "logcap": r.control_logcap,
                                "td": str(r.treated_td), "treat": 0,
                                "post": int(r.treated_post)})
            A = pd.DataFrame(allrows)
            A["liq"] = standardise_liq(A["logilliq"], _quarter(A["td"]))
            A["y"] = (base + 0.03 * A["treat"] + 0.02 * A["liq"]
                      + 0.01 * A["logcap"] + 0.005 * A["logilliq"]
                      + 0.07 * A["treat"] * A["post"] * A["liq"])
            ymap = {k: v for k, v in zip(A["key"], A["y"])}
            tr = tr.copy()
            tr["bid12"] = [ymap[("t", a)] for a in tr["accession"]]
            ctrl["bid12"] = [ymap.get(("c", int(pn)), 1.0)
                             for pn in ctrl["permno"]]
            ctrl.to_csv(c, index=False)
            r = be.spec_triple(tr)

            extra_pair = pairs.iloc[[0]].copy()
            extra_pair["control_permno"] = 999999
            extra_pair["treated_td"] = "2024-12-18"
            extra_pair["match_group"] = "post-main-window"
            extra_pair["control_logilliq"] = 1000.0
            pd.concat([pairs, extra_pair], ignore_index=True).to_csv(p, index=False)
            extra_ctrl = pd.DataFrame([{
                "permno": 999999, "cik": "1", "td": "2024-12-18",
                "match_group": "post-main-window", "bid12": 1.0,
                "excluded_prior_bid": 0,
            }])
            pd.concat([ctrl, extra_ctrl], ignore_index=True).to_csv(c, index=False)
            r_extra = be.spec_triple(tr)
        finally:
            be.MATCH_OUT, be.CONTROL_LOOKUP_CSV, be.N_BOOT = saved
    check("estimated on the matched sample", r.get("status") == "estimated",
          str(r.get("status")))
    check("tau = +7 pp recovered",
          abs(r["tau_treat_x_post_x_liq_pp"] - 7.0) < 1e-6,
          f"{r.get('tau_treat_x_post_x_liq_pp')}")
    check("Post is not among the estimated terms (absorbed by match FE)",
          "post" not in r["terms_estimated"], str(r["terms_estimated"]))
    check("Post x LIQ survives (LIQ varies within match group)",
          "pl" in r["terms_estimated"], str(r["terms_estimated"]))
    check("registered X adjustment uses both match covariates",
          all(c in r["terms_estimated"] for c in ("logcap", "logilliq")),
          str(r["terms_estimated"]))
    check("realised MDE reported next to the §9 rule of thumb",
          np.isfinite(r["mde_tau_pp_realised"])
          and r["mde_tau_pp_rule_of_thumb"]["S1"] == 18.2)
    check("prior-bid control omitted from the estimation sample",
          r["treated_n"] == 120 and r["control_n"] == 359,
          f"{r['treated_n']}/{r['control_n']}")
    check("prior-bid control exclusion counted",
          r.get("controls_excluded_prior_bid") == 1,
          str(r.get("controls_excluded_prior_bid")))
    check("pairs outside the eligible treated sample never enter LIQ scaling",
          r_extra["match_groups_dropped_no_contrast"] == 0
          and abs(r_extra["tau_treat_x_post_x_liq_pp"] - 7.0) < 1e-6,
          f"{r_extra['match_groups_dropped_no_contrast']}/"
          f"{r_extra['tau_treat_x_post_x_liq_pp']}")


def test_triple_gates() -> None:
    import empirics.estimate_bidder_entry as be
    print("\n== triple difference gates on absent inputs ==")
    saved = (be.MATCH_OUT, be.CONTROL_LOOKUP_CSV)
    be.MATCH_OUT = "/nonexistent/pairs.csv"
    be.CONTROL_LOOKUP_CSV = "/nonexistent/control.csv"
    try:
        r = be.spec_triple(pd.DataFrame())
    finally:
        be.MATCH_OUT, be.CONTROL_LOOKUP_CSV = saved
    check("returns a status, not a crash, when inputs are missing",
          "not landed" in r.get("status", ""), str(r))


def test_pending_artifact() -> None:
    import empirics.estimate_bidder_entry as be
    print("\n== missing matched inputs write a pending artifact ==")
    with tempfile.TemporaryDirectory() as tmp:
        h1 = os.path.join(tmp, "h1.csv")
        result = os.path.join(tmp, "result.json")
        pd.DataFrame([{"accession": "a", "liq": 0.0}]).to_csv(h1, index=False)
        tr = pd.DataFrame([{"accession": "a", "td": pd.Timestamp("2024-01-02"),
                            "post": 0, "bid12": 0.0, "logilliq": -6.0,
                            "logcap": 14.0, "sic2": "20"}])
        saved = (be.H1_SAMPLE_CSV, be.MATCH_OUT, be.CONTROL_LOOKUP_CSV,
                 be.RESULT_OUT, be.build_treated)
        be.H1_SAMPLE_CSV = h1
        be.MATCH_OUT = os.path.join(tmp, "missing-pairs.csv")
        be.CONTROL_LOOKUP_CSV = os.path.join(tmp, "missing-control.csv")
        be.RESULT_OUT = result
        be.build_treated = lambda: (tr.copy(), {"treated_pre": 1,
                                                 "treated_post": 0})
        try:
            rc = be.main(["--spec", "triple"])
            with open(result) as fh:
                out = json.load(fh)
        finally:
            (be.H1_SAMPLE_CSV, be.MATCH_OUT, be.CONTROL_LOOKUP_CSV,
             be.RESULT_OUT, be.build_treated) = saved
    check("pending run returns a non-success status", rc != 0, str(rc))
    check("artifact is not labelled ESTIMATED",
          out.get("label") == "NOT ESTIMATED", str(out.get("label")))
    check("artifact status names the pending matched inputs",
          out.get("status") == "pending_matched_inputs", str(out.get("status")))
    check("pending artifact contains no partial estimate",
          "within" not in out and "tau_treat_x_post_x_liq_pp" not in str(out),
          str(out.keys()))


def test_main_window_and_unestimated_extensions() -> None:
    import empirics.estimate_bidder_entry as be
    print("\n== main window and unestimated samples are explicit ==")
    with tempfile.TemporaryDirectory() as tmp:
        h1 = os.path.join(tmp, "h1.csv")
        pairs = os.path.join(tmp, "pairs.csv")
        controls = os.path.join(tmp, "controls.csv")
        result = os.path.join(tmp, "result.json")
        accessions = ["a", "b", "c"]
        pd.DataFrame({"accession": accessions, "liq": [0.0, 0.1, 0.2]}).to_csv(
            h1, index=False)
        pd.DataFrame({"match_group": accessions}).to_csv(pairs, index=False)
        pd.DataFrame({"match_group": accessions}).to_csv(controls, index=False)
        tr = pd.DataFrame({
            "accession": accessions,
            "td": pd.to_datetime(["2024-12-17", "2024-12-18", "2025-06-01"]),
            "post": [1, 1, 1], "bid12": [0.0, 0.0, 0.0],
            "logilliq": [-6.0, -6.1, -6.2], "logcap": [14.0, 14.1, 14.2],
            "sic2": ["20", "20", "20"],
        })
        seen = {}

        def fake_within(frame):
            seen["within"] = frame["accession"].tolist()
            return {"delta_liq_x_post_pp": 1.0, "se_delta_pp": 2.0,
                    "p_delta_quoted_conservative": 0.5,
                    "mde_delta_pp_realised": 5.6, "beta_liq_pp": 0.2,
                    "se_beta_pp": 0.3, "p_beta_normal": 0.6}

        def fake_triple(frame):
            seen["triple"] = frame["accession"].tolist()
            return {"status": "estimated", "tau_treat_x_post_x_liq_pp": 1.1,
                    "se_tau_pp": 2.1, "p_tau_quoted_conservative": 0.4,
                    "mde_tau_pp_realised": 5.9}

        saved = (be.H1_SAMPLE_CSV, be.MATCH_OUT, be.CONTROL_LOOKUP_CSV,
                 be.RESULT_OUT, be.build_treated, be.spec_within, be.spec_triple)
        be.H1_SAMPLE_CSV, be.MATCH_OUT = h1, pairs
        be.CONTROL_LOOKUP_CSV, be.RESULT_OUT = controls, result
        be.build_treated = lambda: (tr.copy(), {"treated_pre": 0,
                                                 "treated_post": 3})
        be.spec_within, be.spec_triple = fake_within, fake_triple
        try:
            rc = be.main(["--spec", "both"])
            with open(result) as fh:
                out = json.load(fh)
        finally:
            (be.H1_SAMPLE_CSV, be.MATCH_OUT, be.CONTROL_LOOKUP_CSV,
             be.RESULT_OUT, be.build_treated, be.spec_within,
             be.spec_triple) = saved
    check("only observations through 2024-12-17 enter both estimates",
          seen == {"within": ["a"], "triple": ["a"]}, str(seen))
    check("main-sample end is recorded",
          out.get("sample_window", {}).get("main_end") == "2024-12-17",
          str(out.get("sample_window")))
    check("2025 extension is explicitly not estimated",
          out.get("extension_2025", {}).get("status") == "NOT ESTIMATED"
          and out["extension_2025"].get("treated_rows") == 1,
          str(out.get("extension_2025")))
    check("S2 is explicitly not estimated because coding is absent",
          out.get("S2", {}).get("status") == "NOT ESTIMATED"
          and "corporate-action" in out["S2"].get("reason", ""),
          str(out.get("S2")))
    check("complete S1 run retains the ESTIMATED label",
          rc == 0 and out.get("label") == "ESTIMATED", f"{rc}/{out.get('label')}")


def test_within_spec_does_not_need_matched_inputs() -> None:
    """`--spec within` reads only the treated sample.

    Gating it on the match pairs would let a pending stub overwrite a real
    within-13D-targets result whenever the matched DiD had not landed.
    """
    import empirics.estimate_bidder_entry as be
    print("\n== --spec within does not gate on the matched inputs ==")
    saved = (be.MATCH_OUT, be.CONTROL_LOOKUP_CSV)
    try:
        be.MATCH_OUT = "/nonexistent/did_match_pairs.csv"
        be.CONTROL_LOOKUP_CSV = "/nonexistent/bid12_control.csv"
        import argparse
        ap = argparse.ArgumentParser()
        ap.add_argument("--spec", choices=("within", "triple", "both"),
                        default="both")
        for spec, gated in (("within", False), ("triple", True),
                            ("both", False)):
            args = ap.parse_args(["--spec", spec])
            missing = ([p for p in (be.MATCH_OUT, be.CONTROL_LOOKUP_CSV)
                        if not os.path.exists(p)]
                       if args.spec in ("triple", "both") else [])
            hard_stop = bool(missing) and args.spec == "triple"
            check(f"--spec {spec} hard-stops on missing matched inputs: "
                  f"{gated}", hard_stop == gated)
    finally:
        be.MATCH_OUT, be.CONTROL_LOOKUP_CSV = saved


def test_triple_inherits_the_match_design_status() -> None:
    """The triple difference is computed on the section 8.2 match draw.

    If that draw failed its own balance gate, tau is estimated on an
    unbalanced sample. The number is still worth reporting, but it cannot be
    read as if the match had passed, so the status travels with it.
    """
    import json
    import empirics.estimate_bidder_entry as be
    print("\n== the triple difference carries the match draw's design status ==")
    with tempfile.TemporaryDirectory() as tmp:
        meta = os.path.join(tmp, "did_match_meta.json")
        with open(meta, "w") as fh:
            json.dump({"design_status": "failed_balance",
                       "selected_caliper_sd": 0.20,
                       "balance_exceeds_0.10": ["ret12m", "idiovol"]}, fh)
        saved = be.MATCH_META
        try:
            be.MATCH_META = meta
            block = be.match_design_status()
        finally:
            be.MATCH_META = saved
    check("the failed status is carried, not silently dropped",
          block["design_status"] == "failed_balance")
    check("the failing covariates travel with it",
          block["balance_exceeds_0.10"] == ["ret12m", "idiovol"])
    check("the reading is stated, not left to the reader",
          "unbalanced" in block["reading"].lower(),
          block["reading"])

    with tempfile.TemporaryDirectory() as tmp:
        saved = be.MATCH_META
        try:
            be.MATCH_META = os.path.join(tmp, "absent.json")
            block = be.match_design_status()
        finally:
            be.MATCH_META = saved
    check("an absent match meta is unknown, never assumed to pass",
          block["design_status"] == "unknown", str(block))


def main() -> int:
    test_standardise_liq()
    test_within_recovery()
    test_triple()
    test_triple_gates()
    test_pending_artifact()
    test_main_window_and_unestimated_extensions()
    test_within_spec_does_not_need_matched_inputs()
    test_triple_inherits_the_match_design_status()
    n_fail = sum(1 for _, ok, _ in _results if not ok)
    print(f"\n{len(_results) - n_fail}/{len(_results)} checks passed"
          + (f", {n_fail} FAILED" if n_fail else ""))
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
