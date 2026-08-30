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

import os
import sys

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
        # LIQ is built downstream from logilliq, so plant on logilliq and
        # recover the planted tau from the realised design matrix instead of
        # asserting an exact number: what is under test is that the estimator
        # returns the OLS solution of the stated specification.
        tr_rows.append({"accession": acc, "permno": 1000 + gi, "td": td,
                        "post": post, "bid12": np.nan, "logilliq": t_ill,
                        "logcap": 14.0, "liq": np.nan, "sic2": "20"})
        for j in range(3):
            c_ill = float(rng.normal(-6, 2))
            pair_rows.append({"treated_permno": 1000 + gi,
                              "treated_accession": acc, "treated_td": td,
                              "treated_quarter": "", "treated_sic2": "20",
                              "treated_post": post,
                              "control_permno": 5000 + gi * 3 + j,
                              "match_group": acc, "mahalanobis_d2": 0.1,
                              "control_logcap": 14.0,
                              "control_logilliq": c_ill,
                              "control_turnover": np.nan,
                              "control_ret12m": np.nan,
                              "control_idiovol": np.nan})
            ctrl_rows.append({"permno": 5000 + gi * 3 + j, "cik": "1",
                              "td": td, "match_group": acc, "bid12": np.nan})
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
            for r in tr.itertuples():
                allrows.append({"key": ("t", r.accession),
                                "logilliq": r.logilliq, "td": str(r.td.date()),
                                "treat": 1, "post": r.post})
            for r in pairs.itertuples():
                allrows.append({"key": ("c", int(r.control_permno)),
                                "logilliq": r.control_logilliq,
                                "td": str(r.treated_td), "treat": 0,
                                "post": int(r.treated_post)})
            A = pd.DataFrame(allrows)
            A["liq"] = standardise_liq(A["logilliq"], _quarter(A["td"]))
            A["y"] = (base + 0.03 * A["treat"] + 0.02 * A["liq"]
                      + 0.07 * A["treat"] * A["post"] * A["liq"])
            ymap = {k: v for k, v in zip(A["key"], A["y"])}
            tr = tr.copy()
            tr["bid12"] = [ymap[("t", a)] for a in tr["accession"]]
            ctrl = pd.read_csv(c)
            ctrl["bid12"] = [ymap[("c", int(pn))] for pn in ctrl["permno"]]
            ctrl.to_csv(c, index=False)
            r = be.spec_triple(tr)
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
    check("realised MDE reported next to the §9 rule of thumb",
          np.isfinite(r["mde_tau_pp_realised"])
          and r["mde_tau_pp_rule_of_thumb"]["S1"] == 18.2)
    check("control and treated counts reported",
          r["treated_n"] == 120 and r["control_n"] == 360,
          f"{r['treated_n']}/{r['control_n']}")


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


def main() -> int:
    test_standardise_liq()
    test_within_recovery()
    test_triple()
    test_triple_gates()
    n_fail = sum(1 for _, ok, _ in _results if not ok)
    print(f"\n{len(_results) - n_fail}/{len(_results)} checks passed"
          + (f", {n_fail} FAILED" if n_fail else ""))
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
