"""Synthetic checks for the matched-DiD estimator (empirics/estimate_did.py).

No CRSP load, no network, no shared output files — every check runs on
constructed arrays or temporary files, so this is safe to run while the
extraction lanes are live.

What is checked:

  * ``_demean`` absorbs group means exactly (the FWL device the estimator
    uses in place of ~1,000 match dummies)
  * the FWL path and the explicit-dummy path agree on β̂ and on the two-way
    clustered SE, which is the equivalence the estimator asserts in its
    output (``fwl_check``)
  * β̂ recovers a planted DiD effect on a synthetic matched panel
  * Post is absorbed by the match fixed effects (SPEC §8.4's λ is not
    identified under pseudo-TD inheritance) and the estimator detects it
  * ``std_diff`` matches the hand arithmetic and is scale-equivariant
  * ``covariates`` reproduces ``estimate_h1``'s own logcap / log-Amihud
    definitions on a synthetic panel — treated and control covariates have to
    be the same object for the matching to mean anything
  * ``sic2_of_cik`` reads both on-disk submissions layouts

Run:
    .venv/bin/python -m empirics.test_estimate_did
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


def test_demean() -> None:
    from empirics.estimate_did import _demean
    print("\n== FWL demeaning ==")
    v = np.array([1.0, 3.0, 10.0, 20.0, 30.0])
    g = np.array([0, 0, 1, 1, 1])
    d = _demean(v, g)
    check("group means removed", np.allclose(d, [-1, 1, -10, 0, 10]),
          f"got {d}")
    check("demeaned series sums to zero within every group",
          all(abs(d[g == k].sum()) < 1e-12 for k in (0, 1)))


def _sample_did(D: pd.DataFrame) -> float:
    m = D.groupby(["treat", "post"])["bid12"].mean()
    return float((m[1, 1] - m[0, 1]) - (m[1, 0] - m[0, 0]))


def _synthetic_panel(n_groups: int = 60, seed: int = 7,
                     deterministic: bool = False) -> pd.DataFrame:
    """Matched panel: one treated + three controls per group, half post.

    ``deterministic`` returns the latent probability itself instead of a
    Bernoulli draw, so the planted coefficients are recoverable exactly."""
    rng = np.random.default_rng(seed)
    rows = []
    for gi in range(n_groups):
        post = int(gi >= n_groups // 2)
        month = f"2023-{1 + gi % 12:02d}" if not post else f"2024-{1 + gi % 10:02d}"
        base = rng.normal(0.10, 0.02)                 # match-group level
        for j in range(4):
            treat = int(j == 0)
            p = base + 0.09 * treat + 0.05 * treat * post
            rows.append({"match_group": f"g{gi}", "treat": treat,
                         "post": post, "month": month,
                         "bid12": (float(p) if deterministic
                                   else float(rng.random()
                                              < min(max(p, 0), 1)))})
    return pd.DataFrame(rows)


def test_fwl_equivalence_and_recovery() -> None:
    from empirics.estimate_did import _demean
    from empirics.estimate_h1 import _independent_columns, ols_clustered
    print("\n== FWL vs explicit dummies; effect recovery ==")
    D = _synthetic_panel(n_groups=400, seed=11)
    D["treat_x_post"] = D["treat"] * D["post"]
    g = pd.factorize(D["match_group"])[0]
    m = pd.factorize(D["month"])[0]

    y_w = _demean(D["bid12"].values.astype(float), g)
    Xw = np.column_stack([_demean(D["treat_x_post"].values.astype(float), g),
                          _demean(D["treat"].values.astype(float), g)])
    fw = ols_clustered(y_w, Xw, g, m)
    se_w = np.sqrt(np.diag(fw["V_twoway"]))

    Xd = np.column_stack([
        np.ones(len(D)),
        D[["treat_x_post", "treat", "post"]].values.astype(float),
        pd.get_dummies(D["match_group"], drop_first=True, dtype=float).values])
    keep = _independent_columns(Xd)
    Xd = Xd[:, keep]
    fd = ols_clustered(D["bid12"].values.astype(float), Xd, g, m)
    se_d = np.sqrt(np.diag(fd["V_twoway"]))

    check("beta agrees between FWL and dummy designs",
          abs(fw["beta"][0] - fd["beta"][1]) < 1e-9,
          f"{fw['beta'][0]:.6f} vs {fd['beta'][1]:.6f}")
    check("two-way clustered SE agrees between the two designs",
          abs(se_w[0] - se_d[1]) < 1e-9, f"{se_w[0]:.6f} vs {se_d[1]:.6f}")
    check("gamma (Treat) agrees too",
          abs(fw["beta"][1] - fd["beta"][2]) < 1e-9)
    # Recovery is checked on a deterministic outcome, so the target is the
    # planted coefficient itself rather than a Bernoulli draw around it: this
    # is an algebra check on the estimator, not a power simulation.
    Dd = _synthetic_panel(n_groups=400, seed=11, deterministic=True)
    Dd["treat_x_post"] = Dd["treat"] * Dd["post"]
    gd = pd.factorize(Dd["match_group"])[0]
    md = pd.factorize(Dd["month"])[0]
    fdet = ols_clustered(
        _demean(Dd["bid12"].values.astype(float), gd),
        np.column_stack([
            _demean(Dd["treat_x_post"].values.astype(float), gd),
            _demean(Dd["treat"].values.astype(float), gd)]), gd, md)
    check("planted DiD effect of +5 pp recovered exactly (deterministic DGP)",
          abs(fdet["beta"][0] - 0.05) < 1e-12,
          f"beta {fdet['beta'][0]:+.8f}")
    check("planted Treat level of +9 pp recovered exactly",
          abs(fdet["beta"][1] - 0.09) < 1e-12,
          f"gamma {fdet['beta'][1]:+.8f}")
    check("beta on the Bernoulli panel equals its realised sample DiD",
          abs(fw["beta"][0] - _sample_did(D)) < 1e-9,
          f"{fw['beta'][0]:.6f} vs {_sample_did(D):.6f}")


def test_post_absorbed() -> None:
    from empirics.estimate_did import _demean
    print("\n== Post is absorbed by the match fixed effects ==")
    D = _synthetic_panel(n_groups=40, seed=3)
    g = pd.factorize(D["match_group"])[0]
    w = _demean(D["post"].values.astype(float), g)
    check("Post has no within-match-group variation",
          float(np.abs(w).max()) < 1e-12, f"max |dev| {np.abs(w).max():.2e}")
    check("Treat does vary within match group",
          float(np.abs(_demean(D["treat"].values.astype(float), g)).max()) > 0.1)


def test_std_diff() -> None:
    from empirics.estimate_did import std_diff
    print("\n== standardised differences ==")
    t = np.array([1.0, 2.0, 3.0, 4.0])
    c = np.array([2.0, 3.0, 4.0, 5.0])
    expect = (t.mean() - c.mean()) / np.sqrt((t.var(ddof=1) + c.var(ddof=1)) / 2)
    check("matches the (mT-mC)/sqrt((vT+vC)/2) convention",
          abs(std_diff(t, c) - expect) < 1e-12,
          f"{std_diff(t, c):.6f} vs {expect:.6f}")
    check("scale-equivariant", abs(std_diff(10 * t, 10 * c)
                                   - std_diff(t, c)) < 1e-12)
    check("NaNs dropped, not propagated",
          np.isfinite(std_diff(np.array([1.0, np.nan, 3.0, 4.0]), c)))
    check("identical distributions give 0", abs(std_diff(t, t.copy())) < 1e-12)


def test_covariates_match_h1() -> None:
    from empirics.estimate_did import covariates
    from empirics.estimate_h1 import _slice
    print("\n== covariates reproduce the h1 definitions ==")
    n = 400
    dates = np.array([np.datetime64("2023-01-02", "D") + i for i in range(n)])
    rng = np.random.default_rng(5)
    panel = {"dates": dates,
             "ret": rng.normal(0, 0.02, n).astype(float),
             "prc": np.full(n, 20.0),
             "vol": np.full(n, 1e5),
             "cap": np.linspace(1e6, 2e6, n),
             "valid": np.ones(n, dtype=bool)}
    td = pd.Timestamp("2023-11-01")
    market = {pd.Timestamp(str(d)): 0.0 for d in dates}
    out = covariates(panel, td, market)

    sl = _slice(panel, td - pd.Timedelta(days=126), td - pd.Timedelta(days=6))
    v = panel["valid"][sl]
    illiq = float(np.mean(np.abs(panel["ret"][sl][v])
                          / (np.abs(panel["prc"][sl][v]) * panel["vol"][sl][v]))
                  * 1e6)
    i = np.searchsorted(panel["dates"],
                        np.datetime64((td - pd.Timedelta(days=6)).date(), "D"),
                        side="right") - 1
    check("logilliq equals h1's log mean-Amihud x 1e6",
          abs(out["logilliq"] - np.log(illiq)) < 1e-12,
          f"{out['logilliq']} vs {np.log(illiq)}")
    check("logcap is log DlyCap at the last day on or before TD-6",
          abs(out["logcap"] - np.log(panel["cap"][i])) < 1e-12)
    check("the three match-quality extras are finite on a full panel",
          all(np.isfinite(out[c]) for c in ("turnover", "ret12m", "idiovol")),
          f"{ {c: out[c] for c in ('turnover', 'ret12m', 'idiovol')} }")

    thin = dict(panel)
    thin["valid"] = np.zeros(n, dtype=bool)
    thin["valid"][:40] = True
    out2 = covariates(thin, td, market)
    check("under 60 valid days leaves logilliq missing, not zero",
          not np.isfinite(out2["logilliq"]), f"got {out2['logilliq']}")


def test_sic_lookup_both_layouts() -> None:
    import empirics.estimate_did as ed
    print("\n== SIC2 read from both submissions layouts ==")
    with tempfile.TemporaryDirectory() as tmp:
        d1 = os.path.join(tmp, "submissions")
        d2 = os.path.join(tmp, "bid12_cache", "submissions")
        os.makedirs(d1)
        os.makedirs(d2)
        with open(os.path.join(d1, "CIK0000000123.json"), "w") as fh:
            json.dump({"cik": "0000000123", "sic": "2834"}, fh)
        with open(os.path.join(d2, "0000000456.json"), "w") as fh:
            json.dump({"cik": "0000000456", "sic": "6022"}, fh)
        # EDGAR knows the filer but publishes no SIC — closed-end funds and
        # trusts on the control side look like this
        with open(os.path.join(d2, "0000000789.json"), "w") as fh:
            json.dump({"cik": "0000000789", "entityType": "other",
                       "sic": "", "sicDescription": ""}, fh)
        saved = ed.SUBMISSIONS_DIRS
        ed.SUBMISSIONS_DIRS = (d1, d2)
        try:
            check("13D-era layout (CIK##########.json)",
                  ed.sic2_of_cik("123") == "28", ed.sic2_of_cik("123"))
            check("BID12 cache layout (##########.json)",
                  ed.sic2_of_cik(456) == "60", ed.sic2_of_cik(456))
            check("file present but SIC blank -> BLANK (counted, not "
                  "confused with a missing file)",
                  ed.sic2_of_cik("789") == "BLANK", ed.sic2_of_cik("789"))
            check("absent CIK -> MISSING, never a guess",
                  ed.sic2_of_cik("999") == "MISSING")
            check("unparseable CIK -> MISSING",
                  ed.sic2_of_cik("not-a-cik") == "MISSING")
        finally:
            ed.SUBMISSIONS_DIRS = saved


def test_main_sample_cutoff() -> None:
    import empirics.estimate_did as ed
    print("\n== main sample ends before the structured-data regime ==")
    with tempfile.TemporaryDirectory() as tmp:
        treated = os.path.join(tmp, "treated.csv")
        h1 = os.path.join(tmp, "h1.csv")
        pd.DataFrame([
            {"accession": "A", "cik": "1", "subject_name": "A",
             "td": "2023-09-01", "date_filed": "2023-09-05", "bid12": 0,
             "extraction_status": "ok", "excluded_prior_bid": 0},
            {"accession": "B", "cik": "2", "subject_name": "B",
             "td": "2024-12-17", "date_filed": "2024-12-17", "bid12": 1,
             "extraction_status": "ok", "excluded_prior_bid": 0},
            {"accession": "C", "cik": "3", "subject_name": "C",
             "td": "2024-12-18", "date_filed": "2024-12-18", "bid12": 0,
             "extraction_status": "ok", "excluded_prior_bid": 0},
            {"accession": "D", "cik": "4", "subject_name": "D",
             "td": "2025-02-01", "date_filed": "2025-02-03", "bid12": 1,
             "extraction_status": "ok", "excluded_prior_bid": 0},
        ]).to_csv(treated, index=False)
        pd.DataFrame([
            {"accession": a, "permno": 100 + i, "logcap": 10 + i,
             "logilliq": -2 + i / 10, "sic2": 28}
            for i, a in enumerate("ABCD")
        ]).to_csv(h1, index=False)
        saved = ed.TREATED_CSV, ed.H1_SAMPLE_CSV
        ed.TREATED_CSV, ed.H1_SAMPLE_CSV = treated, h1
        try:
            full, _ = ed.build_treated()
            sample, funnel = ed.build_treated(main_sample=True)
        finally:
            ed.TREATED_CSV, ed.H1_SAMPLE_CSV = saved
        check("the shared loader keeps extension rows for downstream extension code",
              set(full["accession"]) == {"A", "B", "C", "D"})
        check("2024-12-17 is the last date in the main sample",
              set(sample["accession"]) == {"A", "B"},
              f"got {sorted(sample['accession'])}")
        check("the structured-data transition and 2025 extension are counted",
              funnel["excluded_structured_data_regime"] == 2
              and funnel["extension_2025_rows"] == 1
              and funnel["main_sample_end"] == "2024-12-17")
        check("2025 is explicitly extension-only",
              funnel["extension_2025_policy"] == "extension-only; excluded from main")


def test_cell_shortfalls() -> None:
    from empirics.estimate_did import shortfalls_by_cell
    print("\n== 3:1 shortfalls are reported by SIC2 x quarter ==")
    tr = pd.DataFrame([
        {"accession": "A", "sic2": "28", "quarter": "2023Q1"},
        {"accession": "B", "sic2": "28", "quarter": "2023Q1"},
        {"accession": "C", "sic2": "35", "quarter": "2024Q2"},
    ])
    per = pd.DataFrame([
        {"accession": "A", "n_matches": 3},
        {"accession": "B", "n_matches": 1},
        {"accession": "C", "n_matches": 0},
    ])
    out = shortfalls_by_cell(tr, per).set_index(["sic2", "quarter"])
    a = out.loc[("28", "2023Q1")]
    b = out.loc[("35", "2024Q2")]
    check("cell counts retain treated rows, requested pairs, and shortfall",
          a["treated_rows"] == 2 and a["pairs_requested"] == 6
          and a["pairs_matched"] == 4 and a["pair_shortfall"] == 2)
    check("zero-match cells remain visible",
          b["treated_rows"] == 1 and b["pairs_matched"] == 0
          and b["pair_shortfall"] == 3)
    check("full and short matched-treated counts are separate",
          a["treated_with_3_matches"] == 1
          and a["treated_with_fewer_than_3"] == 1)


def test_estimate_stage_reuses_failed_match() -> None:
    import empirics.estimate_did as ed
    print("\n== estimate stage loads, but never rewrites, the match draw ==")
    with tempfile.TemporaryDirectory() as tmp:
        paths = {name: os.path.join(tmp, name) for name in (
            "treated.csv", "h1.csv", "pairs.csv", "quality.csv",
            "shortfalls.csv", "match_meta.json", "result.json")}
        pd.DataFrame([
            {"accession": "A", "cik": "1", "subject_name": "A",
             "td": "2023-09-01", "date_filed": "2023-09-05", "bid12": 0,
             "extraction_status": "ok", "excluded_prior_bid": 0},
            {"accession": "B", "cik": "2", "subject_name": "B",
             "td": "2024-06-01", "date_filed": "2024-06-03", "bid12": 1,
             "extraction_status": "ok", "excluded_prior_bid": 0},
        ]).to_csv(paths["treated.csv"], index=False)
        pd.DataFrame([
            {"accession": "A", "permno": 101, "logcap": 10.0,
             "logilliq": -2.0, "sic2": 28},
            {"accession": "B", "permno": 102, "logcap": 11.0,
             "logilliq": -1.0, "sic2": 28},
        ]).to_csv(paths["h1.csv"], index=False)
        pd.DataFrame([{"treated_permno": 101, "treated_accession": "A",
                       "treated_td": "2023-09-01", "treated_quarter": "2023Q3",
                       "treated_sic2": "28", "treated_post": 0,
                       "control_permno": 201, "match_group": "A",
                       "control_logcap": 10.1, "control_logilliq": -1.9,
                       "control_turnover": 0.1, "control_ret12m": 0.2,
                       "control_idiovol": 0.03}]).to_csv(paths["pairs.csv"], index=False)
        pd.DataFrame([{"covariate": "logcap", "matched_dimension": True,
                       "treated_mean": 10.0, "control_mean": 10.1,
                       "std_diff_matched": 0.2, "exceeds_0.10": True}]
                     ).to_csv(paths["quality.csv"], index=False)
        pd.DataFrame([{"sic2": "28", "quarter": "2023Q3",
                       "treated_rows": 1, "pairs_requested": 3,
                       "pairs_matched": 1, "pair_shortfall": 2,
                       "treated_with_3_matches": 0,
                       "treated_with_fewer_than_3": 1}]
                     ).to_csv(paths["shortfalls.csv"], index=False)
        with open(paths["match_meta.json"], "w") as fh:
            json.dump({"design_status": "failed_balance",
                       "selected_caliper_sd": 0.20,
                       "balance_exceeds_0.10": ["logcap"],
                       "treated_funnel": {"treated_matched_sample": 3,
                                          "treated_pre": 2,
                                          "treated_post": 1},
                       "control_pool": {
                           "control_universe": 10,
                           "option_1_fallback": True,
                           "recovery_gate_status":
                               "passed_with_validated_rows",
                           "n_unresolved_delisted": 7,
                           "n_recovered_validated": 3,
                           "control_bid_rate_bias": "down",
                           "gamma_bias": "up"}}, fh)

        attrs = ("TREATED_CSV", "H1_SAMPLE_CSV", "MATCH_OUT", "QUALITY_OUT",
                 "SHORTFALL_OUT", "MATCH_META_OUT", "RESULT_OUT",
                 "CONTROL_CSV", "PERMNO_MAP_CSV")
        saved = {a: getattr(ed, a) for a in attrs}
        ed.TREATED_CSV = paths["treated.csv"]
        ed.H1_SAMPLE_CSV = paths["h1.csv"]
        ed.MATCH_OUT = paths["pairs.csv"]
        ed.QUALITY_OUT = paths["quality.csv"]
        ed.SHORTFALL_OUT = paths["shortfalls.csv"]
        ed.MATCH_META_OUT = paths["match_meta.json"]
        ed.RESULT_OUT = paths["result.json"]
        ed.CONTROL_CSV = os.path.join(tmp, "must-not-load-control-universe.csv")
        ed.PERMNO_MAP_CSV = os.path.join(tmp, "must-not-load-permno-map.csv")
        before = (open(ed.MATCH_OUT, "rb").read(),
                  open(ed.QUALITY_OUT, "rb").read())
        try:
            rc = ed.main(["--stage", "estimate"])
            with open(ed.RESULT_OUT) as fh:
                result = json.load(fh)
            after = (open(ed.MATCH_OUT, "rb").read(),
                     open(ed.QUALITY_OUT, "rb").read())
        finally:
            for a, v in saved.items():
                setattr(ed, a, v)
        check("failed 0.20 balance hard-stops before estimation",
              rc != 0 and result["status"] == "design_failure"
              and result["label"] == "NOT ESTIMATED")
        check("--stage estimate does not need or rebuild the control pool",
              before == after)
        check("the failed covariate and selected tighter caliper are recorded",
              result["matching"]["caliper_pooled_sd"] == 0.20
              and result["matching"]["balance_exceeds_0.10"] == ["logcap"])
        check("a design failure still carries quote_as_result false, and "
              "names live bars rather than a satisfied one",
              result["quote_as_result"] is False
              and any("8.2" in b for b in result["quote_as_result_blocked_by"])
              and any("8.8" in b for b in result["quote_as_result_blocked_by"])
              and "quote_as_result_until" not in result,
              str(result.get("quote_as_result_blocked_by")))
        check("a design failure still signs the survivorship bias",
              result["survivorship"]["control_bid_rate_bias"] == "down"
              and result["survivorship"]["gamma_bias"] == "up")
        check("design MDE arithmetic is present and not called realised",
              "mde_pp_design_arithmetic" in result
              and "mde_pp_realised" not in result
              and result["mde_pp_design_arithmetic"]["n_pre"] == 2
              and result["mde_pp_design_arithmetic"]["n_post"] == 1)


def test_balance_gate() -> None:
    from empirics.estimate_did import balance_decision
    print("\n== balance gate gets one predeclared tighter rerun ==")
    bad = pd.DataFrame([{"covariate": "logcap", "exceeds_0.10": True}])
    good = pd.DataFrame([{"covariate": "logcap", "exceeds_0.10": False}])
    check("a failed 0.25 attempt requests the 0.20 rerun",
          balance_decision(bad, 0.25) == "retry_tighter")
    check("a failed 0.20 attempt is a design failure",
          balance_decision(bad, 0.20) == "failed_balance")
    check("passing balance stops at either caliper",
          balance_decision(good, 0.25) == "pass"
          and balance_decision(good, 0.20) == "pass")


def test_conditional_fe_logit() -> None:
    from scipy.special import expit
    from empirics.estimate_did import conditional_fe_logit
    print("\n== SPEC 8.4 conditional-FE logit robustness ==")
    rng = np.random.default_rng(91)
    rows = []
    for gi in range(400):
        post = int(gi >= 200)
        alpha = rng.normal(-1.4, 0.45)
        month = f"{2023 + post}-{1 + gi % 12:02d}-15"
        for j in range(4):
            treat = int(j == 0)
            logcap = rng.normal(0, 0.7)
            logilliq = rng.normal(0, 0.8)
            txp = treat * post
            eta = alpha + 0.65 * txp - 0.20 * treat + 0.18 * logcap - 0.12 * logilliq
            rows.append({"match_group": f"g{gi}", "td": month,
                         "treat_x_post": txp, "treat": treat,
                         "logcap": logcap, "logilliq": logilliq,
                         "bid12": float(rng.random() < expit(eta))})
    out = conditional_fe_logit(
        pd.DataFrame(rows), ["treat_x_post", "treat", "logcap", "logilliq"])
    check("conditional logit estimates the same matched sample and FE",
          out["status"] == "estimated"
          and out["fixed_effects"] == "match group, conditioned out"
          and out["terms"] == ["treat_x_post", "treat", "logcap", "logilliq"],
          str(out))
    check("the planted positive Treat x Post log-odds term is recovered",
          out["coefficient_treat_x_post"] > 0,
          f"got {out.get('coefficient_treat_x_post')}")
    check("the average marginal effect is finite and positive",
          np.isfinite(out["average_marginal_effect_treat_x_post"])
          and out["average_marginal_effect_treat_x_post"] > 0,
          f"got {out.get('average_marginal_effect_treat_x_post')}")
    check("month-clustered uncertainty and informative-group counts are recorded",
          np.isfinite(out["se_month_clustered_treat_x_post"])
          and out["informative_match_groups"] > 0)


def test_estimate_stage_registered_adjustments() -> None:
    import empirics.estimate_did as ed
    from scipy.special import expit
    print("\n== estimate stage applies the registered sample and models ==")
    rng = np.random.default_rng(117)
    treated, pairs, controls = [], [], []
    for gi in range(100):
        post = int(gi >= 50)
        td = (f"2023-{1 + gi % 12:02d}-15" if not post
              else f"2024-{2 + gi % 10:02d}-15")
        accession = f"A{gi:03d}"
        base_cap = rng.normal(10.0, 0.7)
        base_ill = rng.normal(-2.0, 0.8)
        alpha = rng.normal(-1.3, 0.35)
        p_t = expit(alpha + 0.30 * post + 0.15 * base_cap
                    - 0.10 * base_ill)
        treated.append({"accession": accession, "permno": 1000 + gi,
                        "td": pd.Timestamp(td), "post": post,
                        "bid12": float(rng.random() < p_t),
                        "logcap": base_cap, "logilliq": base_ill})
        for j in range(3):
            permno = 5000 + gi * 3 + j
            cap = base_cap + rng.normal(0, 0.04)
            ill = base_ill + rng.normal(0, 0.04)
            p_c = expit(alpha + 0.15 * cap - 0.10 * ill)
            pairs.append({
                "treated_permno": 1000 + gi,
                "treated_accession": accession,
                "treated_td": td,
                "treated_quarter": f"{td[:4]}Q{(int(td[5:7]) - 1) // 3 + 1}",
                "treated_sic2": "28", "treated_post": post,
                "control_permno": permno, "match_group": accession,
                "mahalanobis_d2": 0.01,
                "control_logcap": cap, "control_logilliq": ill,
                "control_turnover": 0.1, "control_ret12m": 0.2,
                "control_idiovol": 0.03,
            })
            controls.append({"permno": permno, "cik": str(permno),
                             "td": td, "match_group": accession,
                             "bid12": float(rng.random() < p_c),
                             "excluded_prior_bid": int(gi == 0 and j == 0)})
    tr = pd.DataFrame(treated)
    pair_df = pd.DataFrame(pairs)
    quality = pd.DataFrame([
        {"covariate": c, "matched_dimension": c in ("logcap", "logilliq"),
         "treated_mean": 0.0, "control_mean": 0.0,
         "std_diff_matched": 0.0, "exceeds_0.10": False}
        for c in ("logcap", "logilliq", "turnover", "ret12m", "idiovol")
    ])
    with tempfile.TemporaryDirectory() as tmp:
        lookup = os.path.join(tmp, "control.csv")
        result_path = os.path.join(tmp, "result.json")
        pairs_path = os.path.join(tmp, "pairs.csv")
        treated_path = os.path.join(tmp, "treated.csv")
        h1_path = os.path.join(tmp, "h1.csv")
        pd.DataFrame(controls).to_csv(lookup, index=False)
        pair_df.to_csv(pairs_path, index=False)
        pd.DataFrame([{"x": 1}]).to_csv(treated_path, index=False)
        pd.DataFrame([{"x": 1}]).to_csv(h1_path, index=False)
        saved = {a: getattr(ed, a) for a in
                 ("CONTROL_LOOKUP_CSV", "RESULT_OUT", "MATCH_OUT",
                  "TREATED_CSV", "H1_SAMPLE_CSV", "N_BOOT")}
        ed.CONTROL_LOOKUP_CSV = lookup
        ed.RESULT_OUT = result_path
        ed.MATCH_OUT = pairs_path
        ed.TREATED_CSV = treated_path
        ed.H1_SAMPLE_CSV = h1_path
        ed.N_BOOT = 19
        try:
            rc = ed.stage_estimate(
                tr, pair_df, {"main_sample_end": "2024-12-17"}, quality,
                {"control_universe": 300})
            with open(result_path) as fh:
                result = json.load(fh)
        finally:
            for a, v in saved.items():
                setattr(ed, a, v)
        check("control rows already under bid are omitted and counted",
              rc == 0 and result["sample"]["controls_excluded_prior_bid"] == 1
              and result["sample"]["control_n"] == 299,
              str(result.get("sample")))
        check("the LPM adjusts for both registered continuous match dimensions",
              result["specification"]["adjustment_terms"]
              == ["logcap", "logilliq"]
              and all(x in result["specification"]["terms_estimated"]
                      for x in ("logcap", "logilliq")))
        check("the logit robustness reports an average marginal effect",
              result["logit_robustness"]["status"] == "estimated"
              and np.isfinite(result["logit_robustness"]
                              ["average_marginal_effect_treat_x_post"]),
              str(result.get("logit_robustness")))
        check("main-window, S2 limitation, ESTIMATED label, and ladder survive",
              result["label"] == "ESTIMATED"
              and result["sample_window"]["main_end"] == "2024-12-17"
              and result["sample_window"]["2025"].startswith("extension-only")
              and result["s2"]["status"] == "not_estimated"
              and result["bounded_null_ladder_pp"] == ed.LADDER_PP)
        check("computed DiD is not yet quotable as a result",
              result["quote_as_result"] is False
              and "control" in result["quote_as_result_until"],
              str(result.get("quote_as_result_until")))
        check("survivorship fallback is signed on the estimate",
              result["survivorship"]["control_bid_rate_bias"] == "down"
              and result["survivorship"]["gamma_bias"] == "up"
              and result["survivorship"]["option_1_fallback"] is True,
              str(result.get("survivorship")))
        check("filer's-own bids are counted separately",
              result["sample"]["treated_filer_own_bid"] == 0)


def test_recovery_gate() -> None:
    from empirics.estimate_did import apply_recovery_gate
    print("\n== recovered CIKs cannot enter matching without the gate ==")
    controls = pd.DataFrame([
        {"permno": 1, "still_listed": "True"},
        {"permno": 2, "still_listed": "False"},
        {"permno": 3, "still_listed": "False"},
        {"permno": 4, "still_listed": "False"},
    ])
    mapped = pd.DataFrame([
        {"permno": 1, "cik": "111", "map_route": "ticker"},
        {"permno": 2, "cik": "222", "map_route": "13f_name_unique"},
        {"permno": 3, "cik": "333", "map_route": "13f_name_unique"},
        {"permno": 4, "cik": "", "map_route": "no_edgar_ticker"},
    ])
    allowed, counts = apply_recovery_gate(mapped, controls, recovery=None)
    check("ticker-linked survivors stay in the pool when recovery has not run",
          allowed == {1: "111"})
    check("unvalidated 13f_name_unique rows are refused",
          counts["refused_unvalidated_recovery"] == 2
          and counts["n_unresolved_delisted"] == 3)
    check("option 1 is recorded when the recovery artefact is absent",
          counts["recovery_gate_status"] == "option_1_fallback"
          and counts["option_1_fallback"] is True
          and counts["control_bid_rate_bias"] == "down"
          and counts["gamma_bias"] == "up")

    recovery = pd.DataFrame([
        {"permno": 2, "cik": "222", "status": "validated"},
        {"permno": 3, "cik": "333", "status": "index_name_ambiguous"},
    ])
    allowed, counts = apply_recovery_gate(mapped, controls, recovery=recovery)
    check("only validated recovery rows enter the pool",
          allowed == {1: "111", 2: "222"})
    check("ambiguous recovery rows stay unresolved",
          counts["n_recovered_validated"] == 1
          and counts["n_unresolved_delisted"] == 2
          and counts["recovery_gate_status"] == "passed_with_validated_rows")


def main() -> int:
    test_demean()
    test_fwl_equivalence_and_recovery()
    test_post_absorbed()
    test_std_diff()
    test_covariates_match_h1()
    test_sic_lookup_both_layouts()
    test_main_sample_cutoff()
    test_cell_shortfalls()
    test_estimate_stage_reuses_failed_match()
    test_balance_gate()
    test_conditional_fe_logit()
    test_estimate_stage_registered_adjustments()
    test_recovery_gate()
    n_fail = sum(1 for _, ok, _ in _results if not ok)
    print(f"\n{len(_results) - n_fail}/{len(_results)} checks passed"
          + (f", {n_fail} FAILED" if n_fail else ""))
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
