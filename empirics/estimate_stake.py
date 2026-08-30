"""Stake at filing (SPEC §5) — the level object γ and the LIQ interaction δ.

    STK_i = α + δ·(LIQ_i × Post_i) + β·LIQ_i + γ·Post_i + X_i'θ + ε_i

γ — the level shift in stake at filing — is the object here, so year-quarter
fixed effects (which absorb Post) are DROPPED in the primary specification
and replaced by a linear time trend in TD plus quarter-of-year dummies
(§5's deliberate FE difference). δ is additionally reported from the full
YQ-FE specification (where γ is not identified and not reported).

Cleaning, pre-specified: drop STK ≤ 0 or > 100; report the 0–5% tail count;
winsorise at 1st/99th percentiles for regression. Report the raw and
winsorised distributions and the bunching histogram in 0.25-point bins over
[4, 8] (does mass pile just above 5%?).

Benchmarks carried alongside (§5): Bechuk–Brav–Jackson–Jiang 2,040
activist-HF 13Ds 1994–2007 — median 6.3 / mean 8.8 / p75 8.8 / p90 14.6 /
p95 21.2 (%); BBJJ's days–stake gradient −0.001*/day ⇒ ~0.12 pp for a
two-business-day median delay cut (the power warning: a mechanical
accumulation effect is ~1/7 of this design's clustered MDE).

Outputs: empirics/output/stake_estimate.json (ESTIMATED record).
Usage: .venv/bin/python -m empirics.estimate_stake
"""

from __future__ import annotations

import datetime as dt
import json
import math
import os

import numpy as np
import pandas as pd

from empirics.estimate_h1 import (
    OUT_DIR, RULE_DATE, ADOPTION_DATE, Z_MDE, _independent_columns,
    ols_clustered, wild_cluster_bootstrap,
)

H1_SAMPLE = os.path.join(OUT_DIR, "h1_sample.csv")
N_BOOT = 9_999
SEED = 20260833

BBJJ_BENCH = {"median": 6.3, "mean": 8.8, "p75": 8.8, "p90": 14.6,
              "p95": 21.2}


def run_spec(s: pd.DataFrame, fe: str, label: str) -> dict:
    """STK on LIQ×Post + LIQ + Post + controls under one FE structure.

    fe = 'trend_qoy' (primary: linear TD trend + quarter-of-year dummies,
    γ identified) or 'yq' (γ absorbed, δ identified)."""
    d = s.dropna(subset=["stk", "liq", "logcap", "pre42",
                         "wlen_busdays"]).reset_index(drop=True)
    d["liq_x_post"] = d["liq"] * d["post_td"]
    d["t_trend"] = (d["td"] - pd.Timestamp("2022-01-01")).dt.days / 365.25
    d["qoy"] = "Q" + d["td"].dt.quarter.astype(str)
    ctrl = ["liq", "liq_x_post", "logcap", "pre42", "wlen_busdays",
            "hf", "corp", "t_trend"]
    if fe == "trend_qoy":
        D = pd.get_dummies(d[["sic2", "qoy"]].astype(str), drop_first=True,
                           dtype=float)
    else:
        D = pd.get_dummies(d[["sic2", "yq"]].astype(str), drop_first=True,
                           dtype=float)
    X_full = np.column_stack(
        [np.ones(len(d)),
         d[ctrl + (["post_td"] if fe == "trend_qoy" else [])]
         .values.astype(float),
         D.values])
    names_full = (["const"] + ctrl
                  + (["post_td"] if fe == "trend_qoy" else [])
                  + list(D.columns))
    keep = _independent_columns(X_full)
    X = X_full[:, keep]
    names = [nm for nm, k in zip(names_full, keep) if k]
    y = d["stk"].values.astype(float)
    f_codes = pd.factorize(d["permno"].values)[0]
    m_codes = pd.factorize(d["td"].dt.to_period("M").astype(str).values)[0]
    fit = ols_clustered(y, X, f_codes, m_codes)
    beta, V = fit["beta"], fit["V_twoway"]
    se = np.sqrt(np.clip(np.diag(V), 0, None))

    def _entry(name):
        if name not in names:
            return None
        i = names.index(name)
        t = float(beta[i] / se[i]) if se[i] > 0 else np.nan
        p = float(2 * (1 - 0.5 * math.erfc(-abs(t) / math.sqrt(2)))) \
            if math.isfinite(t) else 1.0
        return {"coef": float(beta[i]), "se": float(se[i]), "t": t,
                "p_normal": p}

    out = {
        "label": label, "fe": fe, "n": len(d),
        "n_clusters_permno": int(pd.unique(f_codes).size),
        "n_clusters_month": int(pd.unique(m_codes).size),
        "gamma_post": _entry("post_td"),
        "beta_liq": _entry("liq"),
        "delta_liq_x_post": _entry("liq_x_post"),
        "coefficients": {nm: float(b) for nm, b in zip(names, beta)},
    }
    k = names.index("liq_x_post")
    out["p_delta_wild_month"] = wild_cluster_bootstrap(
        y, X, k, m_codes, n_boot=N_BOOT, seed=SEED)
    if out["gamma_post"]:
        kg = names.index("post_td")
        out["gamma_mde_pp_stake"] = float(Z_MDE * se[kg])
        # wild bootstrap for gamma in the primary spec
        out["p_gamma_wild_month"] = wild_cluster_bootstrap(
            y, X, kg, m_codes, n_boot=N_BOOT, seed=SEED + 1)
    out["delta_mde_pp_stake"] = float(Z_MDE * se[k])
    return out


def main() -> int:
    s = pd.read_csv(H1_SAMPLE, dtype={"permno": int})
    s["td"] = pd.to_datetime(s["td"])
    s["fd"] = pd.to_datetime(s["fd"])
    s["hf"] = (s["filer_type"] == "activist_hf").astype(float)
    s["corp"] = (s["filer_type"] == "corporate").astype(float)
    s["sic2"] = s["sic2"].map(
        lambda v: "MISSING" if pd.isna(v) else f"{int(float(v)):02d}")
    s["yq"] = (s["td"].dt.year.astype(str) + "Q"
               + s["td"].dt.quarter.astype(str))

    # -- cleaning (§5) --------------------------------------------------------
    raw_all = pd.to_numeric(s["pct_of_class"], errors="coerce")
    n_total = len(s)
    n_stk = int(raw_all.notna().sum())
    keep = raw_all.notna() & (raw_all > 0) & (raw_all <= 100)
    s["stk_raw"] = raw_all.where(keep)
    n_dropped = int(raw_all.notna().sum() - keep.sum())
    n_tail_below5 = int((s["stk_raw"] < 5).sum())
    lo, hi = s["stk_raw"].quantile([0.01, 0.99])
    s["stk"] = s["stk_raw"].clip(lo, hi)
    sd_winsor = float(s["stk"].std())

    dist_raw = {f"p{q}": float(s["stk_raw"].quantile(q / 100))
                for q in (5, 25, 50, 75, 90, 95)}
    dist_raw.update(mean=float(s["stk_raw"].mean()),
                    sd=float(s["stk_raw"].std()))
    # bunching: 0.25-point bins over [4, 8]
    edges = np.arange(4.0, 8.25, 0.25)
    counts, _ = np.histogram(s["stk_raw"].dropna(), bins=edges)
    bunching = {f"{edges[i]:.2f}-{edges[i+1]:.2f}": int(counts[i])
                for i in range(len(counts))}

    # main sample restrictions as everywhere
    straddle = (s["td"] < RULE_DATE) & (s["fd"] >= RULE_DATE)
    stub = (s["td"] >= ADOPTION_DATE) & (s["td"] < RULE_DATE)
    main_s = s[~straddle & ~stub].copy()

    primary = run_spec(main_s, "trend_qoy", "primary_gamma_trend_qoy")
    yq_spec = run_spec(main_s, "yq", "delta_from_yq_fe")

    n = primary["n"]
    w = float(main_s["post_td"].mean())
    se_design = sd_winsor / math.sqrt(n * w * (1 - w))
    result = {
        "estimate": "Stake at filing (SPEC §5)",
        "label": "ESTIMATED",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "cleaning": {
            "n_rows_total": n_total, "n_with_stk": n_stk,
            "n_dropped_le0_or_gt100": n_dropped,
            "n_tail_below_5pct": n_tail_below5,
            "winsor_bounds_pct": [float(lo), float(hi)],
            "sd_winsorised": sd_winsor,
        },
        "distribution_raw_pct": dist_raw,
        "bunching_hist_025_bins_4_to_8": bunching,
        "benchmark_bbjj_1994_2007_pct": BBJJ_BENCH,
        "bbjj_days_stake_gradient_warning": {
            "gradient_pp_per_day": 0.06,
            "median_delay_cut_busdays": 2.0,
            "implied_mechanical_stake_change_pp": 0.12,
        },
        "sample": {"main_n": n, "w_post": w},
        "primary_trend_qoy": primary,
        "yq_fe_delta_spec": yq_spec,
        "mde_design_formula_pp_stake": float(Z_MDE * se_design),
        "branch_context": ("Branch A selected: supportive is γ̂ < 0 with the "
                           "fall larger in liquid names (δ̂ > 0 given the "
                           "§3.5.2 orientation); against either branch is "
                           "γ̂ > 0 significant"),
        "seeds": {"wild_bootstrap": SEED},
    }
    out_path = os.path.join(OUT_DIR, "stake_estimate.json")
    with open(out_path, "w") as fh:
        json.dump(result, fh, indent=1)
    print(f"wrote {out_path}\n")
    print("== STAKE AT FILING — ESTIMATED ==")
    print(f"  cleaning: {n_stk}/{n_total} with STK; dropped {n_dropped}; "
          f"<5% tail {n_tail_below5}; winsor [{lo:.2f}, {hi:.2f}]; "
          f"sd(winsor) {sd_winsor:.2f}pp")
    print(f"  raw dist: " + ", ".join(f"{k}={v:.2f}"
                                      for k, v in dist_raw.items()))
    g = primary["gamma_post"]
    if g:
        pw = primary.get("p_gamma_wild_month")
        print(f"  PRIMARY γ̂(Post) = {g['coef']:+.3f} pp of stake "
              f"(se {g['se']:.3f}, t {g['t']:+.2f}, p_normal "
              f"{g['p_normal']:.3f}, wild p {pw:.3f}, MDE "
              f"{primary['gamma_mde_pp_stake']:.2f}pp)")
    dl = primary["delta_liq_x_post"]
    print(f"  δ̂(LIQ×Post) primary = {dl['coef']:+.4f} (se {dl['se']:.4f}, "
          f"wild p {primary['p_delta_wild_month']:.3f}, MDE "
          f"{primary['delta_mde_pp_stake']:.2f}pp)")
    dl2 = yq_spec["delta_liq_x_post"]
    print(f"  δ̂ from YQ-FE spec   = {dl2['coef']:+.4f} (se {dl2['se']:.4f}, "
          f"wild p {yq_spec['p_delta_wild_month']:.3f})")
    print(f"  design MDE(γ) formula = "
          f"{result['mde_design_formula_pp_stake']:.2f}pp vs BBJJ-gradient "
          f"mechanical prediction 0.12pp")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
