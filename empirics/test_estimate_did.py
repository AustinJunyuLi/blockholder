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


def main() -> int:
    test_demean()
    test_fwl_equivalence_and_recovery()
    test_post_absorbed()
    test_std_diff()
    test_covariates_match_h1()
    test_sic_lookup_both_layouts()
    n_fail = sum(1 for _, ok, _ in _results if not ok)
    print(f"\n{len(_results) - n_fail}/{len(_results)} checks passed"
          + (f", {n_fail} FAILED" if n_fail else ""))
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
