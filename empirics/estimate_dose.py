"""Dose — bindingness of the five-business-day rule (SPEC §4).

Filer attribute, pre-period behaviour only (cannot be contaminated by the
reform):

  D_j   = share of filer j's initial 13Ds filed 2022-01-01 → 2023-10-09
          whose business-day delay exceeded five                      [0,1]
  E_j   = max(0, median pre-period delay − 5) / 5        (alternative)
  BIND_j= 1{median pre-period delay > 5 business days}   (binary split)

Requires ≥ 2 pre-period filings by the filer for the primary D (single
filers enter only through the stratum-imputed robustness row: filer type ×
size tercile × illiquidity tercile, leave-one-out means, pre-period data
only).

Specification, for y ∈ {RUNUP5, JUMP, STK}:

  y_i = α + φ·(D_j × Post_i) + ψ·D_j + γ·Post_i + X_i'θ + δ_SIC2 + δ_YQ + ε_i

φ is the dose-response. The dose is a filer attribute, so SEs cluster
three-way (subject firm, filer CIK, month of TD) with the Rademacher wild
cluster bootstrap on the month dimension (§4).

Also reported: the first stage (post-period delay of high-D vs low-D
filers — a mechanical validity check, labelled as such, benchmarked against
Trivedi's +0.348 SE 0.130 on the within-five-days share), and the mandatory
corr(D, LIQ) diagnostic with the within-liquidity-tercile re-run.

Sample: H1's main sample (funnel + restrictions). STK rows use the §5
cleaning (drop ≤0/>100, winsorise 1/99).

Outputs: empirics/output/dose_estimate.json (ESTIMATED record).
Usage: .venv/bin/python -m empirics.estimate_dose
"""

from __future__ import annotations

import datetime as dt
import json
import math
import os

import numpy as np
import pandas as pd

from empirics.facts import business_delay
from empirics.estimate_h1 import (
    DATA_DIR, FACT2_JSONL, OUT_DIR, RULE_DATE, ADOPTION_DATE, Z_MDE,
    _independent_columns, _cluster_meat, _norm_cdf, load_filings, sha256_of,
    wild_cluster_bootstrap,
)

H1_SAMPLE = os.path.join(OUT_DIR, "h1_sample.csv")
N_BOOT = 9_999
SEED = 20260832


def ols_multiway(y: np.ndarray, X: np.ndarray,
                 codes_list: list) -> tuple:
    """OLS with multi-way clustered covariance over arbitrary cluster
    dimensions (inclusion-exclusion over all intersections):
    V = Σ V_S − Σ V_pairs + Σ V_triples − … for every subset S of the
    dimensions. Returns (beta, V)."""
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    Z = X * (y - X @ beta)[:, None]
    k = len(codes_list)
    total = np.zeros((X.shape[1], X.shape[1]))
    for mask in range(1, 1 << k):
        members = [codes_list[i] for i in range(k) if mask & (1 << i)]
        # joint codes: unique combinations of the selected dimensions
        joint = np.unique(np.stack(members, axis=1), axis=0,
                          return_inverse=True)[1]
        S = _cluster_meat(Z, joint)
        sign = -1.0 if bin(mask).count("1") % 2 == 0 else 1.0
        total += sign * S
    return beta, XtX_inv @ total @ XtX_inv


def build_dose() -> tuple:
    """(D_j, E_j, BIND_j) per filer CIK from pre-period filings."""
    df = load_filings()
    pre = df[(df["fd"] >= pd.Timestamp("2022-01-01"))
             & (df["fd"] < ADOPTION_DATE)
             & df["td"].notna()].copy()
    pre["delay"] = [business_delay(t.date(), f.date())
                    for t, f in zip(pre["td"], pre["fd"])]
    pre = pre.dropna(subset=["delay"])
    pre["delay"] = pre["delay"].astype(float)
    # §2.3 filter 2's sanity band applies to the dose filings too — stale
    # 2014-2021 trigger parses would otherwise inflate D with >90-day junk
    pre = pre[pre["delay"].between(0, 90)]
    g = pre.groupby("filer_cik")["delay"]
    dose = pd.DataFrame({
        "D": g.apply(lambda s: float((s > 5).mean())),
        "median_delay": g.median(),
        "n_pre": g.size(),
    })
    dose["E"] = np.maximum(0.0, dose["median_delay"] - 5) / 5
    dose["BIND"] = (dose["median_delay"] > 5).astype(int)
    dose = dose.reset_index()
    dose["filer_cik"] = dose["filer_cik"].map(
        lambda c: str(int(str(c).strip())))
    return dose, len(pre)


def run_dose(s: pd.DataFrame, dep: str, dose_col: str, label: str) -> dict:
    d = s.dropna(subset=[dep, dose_col]).reset_index(drop=True)
    d["dose_x_post"] = d[dose_col] * d["post_td"]
    ctrl = [dose_col, "dose_x_post", "logcap", "pre42", "wlen_busdays",
            "hf", "corp", "liq"]
    D = pd.get_dummies(d[["sic2", "yq"]].astype(str), drop_first=True,
                       dtype=float)
    X_full = np.column_stack([np.ones(len(d)), d[ctrl].values.astype(float),
                              D.values])
    names_full = ["const"] + ctrl + list(D.columns)
    keep = _independent_columns(X_full)
    X = X_full[:, keep]
    names = [nm for nm, k in zip(names_full, keep) if k]
    y = d[dep].values.astype(float)
    f_codes = pd.factorize(d["permno"].values)[0]
    filer_codes = pd.factorize(d["filer_cik"].astype(str).values)[0]
    m_codes = pd.factorize(d["td"].dt.to_period("M").astype(str).values)[0]
    beta, V = ols_multiway(y, X, [f_codes, filer_codes, m_codes])
    se = np.sqrt(np.clip(np.diag(V), 0, None))
    k = names.index("dose_x_post")
    t = float(beta[k] / se[k]) if se[k] > 0 else np.nan
    p = float(2 * (1 - _norm_cdf(abs(t)))) if math.isfinite(t) else 1.0
    p_wild = wild_cluster_bootstrap(y, X, k, m_codes, n_boot=N_BOOT,
                                    seed=SEED)
    return {
        "label": label, "dependent": dep, "dose": dose_col,
        "n": len(d),
        "phi_dose_x_post": float(beta[k]),
        "se_phi_3way": float(se[k]),
        "t_phi": t,
        "p_phi_normal": p,
        "p_phi_wild_month": p_wild,
        "p_phi_quoted_conservative": max(p, p_wild),
        # CARs are fractions (converted to pp); STK is already in percentage
        # points of stake
        "mde_phi": float(Z_MDE * se[k] * (1 if dep == "stk" else 100)),
        "mde_units": "pp_of_stake" if dep == "stk" else "pp_of_return",
        "psi_dose": float(beta[names.index(dose_col)]),
        "coefficients": {nm: float(b) for nm, b in zip(names, beta)},
    }


def main() -> int:
    dose_tbl, n_pre_filings = build_dose()
    s = pd.read_csv(H1_SAMPLE, dtype={"permno": int, "filer_cik": str})
    s["filer_cik"] = s["filer_cik"].map(
        lambda c: str(int(str(c).strip())) if str(c).strip() else "")
    s["td"] = pd.to_datetime(s["td"])
    s["fd"] = pd.to_datetime(s["fd"])
    s["hf"] = (s["filer_type"] == "activist_hf").astype(float)
    s["corp"] = (s["filer_type"] == "corporate").astype(float)
    s["sic2"] = s["sic2"].map(
        lambda v: "MISSING" if pd.isna(v) else f"{int(float(v)):02d}")
    s["yq"] = (s["td"].dt.year.astype(str) + "Q"
               + s["td"].dt.quarter.astype(str))
    s = s.merge(dose_tbl, on="filer_cik", how="left")
    s["logilliq_raw"] = np.log(s["illiq"].where(s["illiq"] > 0))
    # STK with the §5 cleaning
    s["stk_raw"] = pd.to_numeric(s["pct_of_class"], errors="coerce")
    s = s[(s["stk_raw"].isna()) | ((s["stk_raw"] > 0) & (s["stk_raw"] <= 100))]
    lo, hi = s["stk_raw"].quantile([0.01, 0.99])
    s["stk"] = s["stk_raw"].clip(lo, hi)

    straddle = (s["td"] < RULE_DATE) & (s["fd"] >= RULE_DATE)
    stub = (s["td"] >= ADOPTION_DATE) & (s["td"] < RULE_DATE)
    main_s = s[~straddle & ~stub].copy()

    multi = main_s[main_s["n_pre"] >= 2].dropna(
        subset=["runup5", "jump", "liq", "logcap", "pre42",
                "wlen_busdays"]).copy()
    # imputed-dose robustness row: single-filing filers, stratum imputation
    # (filer type × size tercile × illiquidity tercile, leave-one-out means,
    # pre-period rows only). Terciles are cut on the pooled frame so both
    # halves share one binning.
    single = main_s[main_s["n_pre"].isna() | (main_s["n_pre"] < 2)].copy()
    if len(single):
        single = single.dropna(subset=["runup5", "liq", "logcap", "pre42",
                                       "wlen_busdays"])
    pooled = pd.concat([multi.assign(_src=0), single.assign(_src=1)],
                       ignore_index=True)
    pooled["size_terc"] = pd.qcut(pooled["logcap"].rank(method="first"), 3,
                                  labels=["S1", "S2", "S3"])
    pooled["illiq_terc"] = pd.qcut(pooled["logilliq_raw"].rank(method="first"),
                                   3, labels=["I1", "I2", "I3"])
    multi = pooled[pooled["_src"] == 0].drop(columns="_src").copy()
    single = pooled[pooled["_src"] == 1].drop(columns="_src").copy()
    if len(single):
        # stratum means from REAL doses (n_pre >= 2), pre-period rows only;
        # the imputed value then applies to the single filer's rows in both
        # periods — only the mean's estimation is pre-period-only
        pre_only = pooled[(pooled["post_td"] == 0)
                          & (pooled["n_pre"] >= 2)]
        grp = pre_only.groupby(["filer_type", "size_terc", "illiq_terc"],
                               observed=True)["D"]
        means = grp.mean()
        gmean = float(pre_only["D"].mean())

        def _impute(r):
            key = (r["filer_type"], r["size_terc"], r["illiq_terc"])
            m = means.get(key, np.nan)
            return m if math.isfinite(m) else gmean
        single["D"] = single.apply(_impute, axis=1)

    results = {}
    for dep in ("runup5", "jump", "stk"):
        results[f"{dep}_D"] = run_dose(multi, dep, "D", f"{dep}~D")
        results[f"{dep}_E"] = run_dose(multi, dep, "E", f"{dep}~E")
    if len(single):
        single_fit = single.dropna(
            subset=["runup5", "liq", "logcap", "pre42", "wlen_busdays"])
        results["runup5_D_imputed"] = run_dose(
            single_fit, "runup5", "D", "runup5~D_imputed_robustness")

    # first stage: post-period delay of high- vs low-D filers (validity
    # check, mechanical — labelled as such)
    fs = multi.dropna(subset=["runup5"]).copy()  # same rows as primary
    fs["delay"] = [business_delay(t.date(), f.date())
                   for t, f in zip(fs["td"], fs["fd"])]  # TD→FD, as in D
    fs = fs[fs["delay"] >= 0]
    fs["dose_x_post"] = fs["D"] * fs["post_td"]
    fs["month"] = fs["td"].dt.to_period("M").astype(str)
    Xf = np.column_stack([
        np.ones(len(fs)), fs[["D", "post_td", "dose_x_post", "logcap",
                              "hf", "corp"]].values.astype(float),
        pd.get_dummies(fs[["sic2"]].astype(str), drop_first=True,
                       dtype=float).values])
    keepf = _independent_columns(Xf)
    Xf = Xf[:, keepf]
    yf = fs["delay"].values.astype(float)
    f_codes = pd.factorize(fs["permno"].values)[0]
    filer_codes = pd.factorize(fs["filer_cik"].astype(str).values)[0]
    m_codes = pd.factorize(fs["month"].values)[0]
    beta_f, V_f = ols_multiway(yf, Xf, [f_codes, filer_codes, m_codes])
    se_f = np.sqrt(np.clip(np.diag(V_f), 0, None))
    # locate dose_x_post coefficient (column 3 of the ctrl block)
    names_f = ["const", "D", "post_td", "dose_x_post", "logcap", "hf",
               "corp"] + [
        f"sic2_{c}" for c in sorted(fs["sic2"].unique())[1:]]
    names_f = [nm for nm, k in zip(names_f, keepf) if k]
    kf = names_f.index("dose_x_post")
    first_stage = {
        "n": len(fs), "phi_delay": float(beta_f[kf]),
        "se": float(se_f[kf]), "t": float(beta_f[kf] / se_f[kf]),
        "note": ("mechanical validity check, not a finding; Trivedi's "
                 "published analogue on the within-5-days share is +0.348 "
                 "(SE 0.130, t 2.69), different outcome scale"),
    }

    # diagnostics: corr(D, LIQ) and within-liquidity-tercile re-run
    corr_d_liq = float(multi[["D", "liq"]].corr().iloc[0, 1])
    multi["liq_terc"] = pd.qcut(multi["liq"], 3, labels=["low", "mid", "high"])
    within_tercile = {}
    for terc, sub in multi.groupby("liq_terc", observed=True):
        sub = sub.dropna(subset=["runup5", "liq", "logcap", "pre42",
                                 "wlen_busdays"])
        within_tercile[str(terc)] = run_dose(sub, "runup5", "D",
                                             f"runup5~D_liq_{terc}")

    result = {
        "estimate": "Bindingness dose (SPEC §4)",
        "label": "ESTIMATED",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "dose_construction": {
            "pre_window": "2022-01-01..2023-10-09 (filing date)",
            "n_pre_filings": int(n_pre_filings),
            "n_filers_with_dose": int(dose_tbl["n_pre"].ge(2).sum()),
            "n_filers_any_pre": int(len(dose_tbl)),
            "delay_def": "business_delay(TD, FD), holiday-adjusted",
            "D_def": "share of pre-period filings with delay > 5 bus. days",
        },
        "sample": {"main_multi_filer_n": len(multi),
                   "single_filer_n": len(single)},
        "first_stage_validity_check": first_stage,
        "corr_D_LIQ": corr_d_liq,
        "results": results,
        "within_liquidity_tercile": within_tercile,
        "branch_context": ("Branch A selected (δ > 0 on RUNUP5 given β < 0); "
                           "supportive dose sign is φ same as that branch"),
        "seeds": {"wild_bootstrap": SEED},
    }
    out_path = os.path.join(OUT_DIR, "dose_estimate.json")
    with open(out_path, "w") as fh:
        json.dump(result, fh, indent=1)
    print(f"wrote {out_path}\n")
    print("== DOSE — ESTIMATED ==")
    print(f"  filers with D (>=2 pre filings): "
          f"{result['dose_construction']['n_filers_with_dose']} of "
          f"{result['dose_construction']['n_filers_any_pre']}; "
          f"multi-filer estimation rows {len(multi)}, single {len(single)}")
    print(f"  corr(D, LIQ) = {corr_d_liq:+.3f}")
    print(f"  first stage (validity check): delay φ = "
          f"{first_stage['phi_delay']:+.3f} (t {first_stage['t']:+.2f})")
    for key in ("runup5_D", "jump_D", "stk_D", "runup5_E", "jump_E", "stk_E",
                "runup5_D_imputed"):
        r = results.get(key)
        if not r:
            continue
        print(f"  {key:>18}: φ {r['phi_dose_x_post']:+.5f} "
              f"(se {r['se_phi_3way']:.5f}, quoted p "
              f"{r['p_phi_quoted_conservative']:.3f}, MDE "
              f"{r['mde_phi']:.2f} {r['mde_units']}, N {r['n']})")
    for terc, r in within_tercile.items():
        print(f"  liq-{terc:>4}: φ {r['phi_dose_x_post']:+.5f} "
              f"(p {r['p_phi_quoted_conservative']:.3f}, N {r['n']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
