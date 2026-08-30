"""H2 — the reform: change in the run-up's liquidity slope (SPEC §3.5).

    CAR_i = α + δ·(LIQ_i × Post_i) + β·LIQ_i + X_i'θ + δ_SIC2 + δ_YQ + ε_i

run separately on RUNUP5 (CAR[TD, TD+4 trading days] — the fixed-length
run-up, primary for H2) and on JUMP. δ is the change in the liquidity slope
at the 2024-02-05 five-business-day reform. In the main sample Post is
absorbed by the year-quarter fixed effects (§3.5's collinearity note), so
γ is not identified and not reported from this specification.

§3.5.2's one-test-refutes-both check runs FIRST and is reported FIRST: if
δ̂ on JUMP is significant and of the same sign and comparable magnitude as
δ̂ on RUNUP5, the split is not a partition and the paper's identity claim
fails. The theory handoff (2026-08-30) selects Branch A (attenuation):
δ > 0 on RUNUP5 given β < 0; Branch B (δ < 0) remains the live alternative.

Defences of §3.1 carried here: window length (business days) enters as a
control; per-day run-up = RUNUP / (FD*−TD trading days) is reported
alongside; the identical-window-length subsample re-run (filings whose
business-day delay equals the modal post-era delay, present in both eras)
is a reported row.

Standard errors: two-way clustered on subject PERMNO and calendar month of
TD (Cameron-Gelbach-Miller; here the dimensions no longer nest) plus the
Rademacher wild cluster bootstrap on month; the more conservative p-value
is quoted (as in H1, §3.4's rule).

Sample: identical to H1's main sample (funnel + straddler/stub exclusions).
FD*, LIQ, controls and the market model are computed by the H1 module and
read from its sample CSV — one construction, two estimates.

Outputs (committed, ``empirics/output/``):
  h2_estimate.json   the ESTIMATED record (both series, all defences)
  h2_runup5_sample.csv not written — h1_sample.csv is the shared record

Usage: .venv/bin/python -m empirics.estimate_h2
"""

from __future__ import annotations

import datetime as dt
import json
import math
import os

import numpy as np
import pandas as pd

from empirics.estimate_h1 import (
    OUT_DIR, RULE_DATE, Z_MDE, _independent_columns, ols_clustered,
    sha256_of, wild_cluster_bootstrap,
)

H1_SAMPLE = os.path.join(OUT_DIR, "h1_sample.csv")
N_BOOT = 9_999
SEED = 20260831


def _norm_cdf(x: float) -> float:
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def run_h2(sample: pd.DataFrame, dep: str, label: str,
           extra_ctrl: list | None = None) -> dict:
    """One §3.5 regression: dep on LIQ, LIQ×Post, controls, SIC2+YQ FE."""
    s = sample.dropna(subset=[dep]).reset_index(drop=True)
    s["liq_x_post"] = s["liq"] * s["post_td"]
    ctrl = ["liq", "liq_x_post", "logcap", "pre42", "wlen_busdays",
            "hf", "corp"] + (extra_ctrl or [])
    D = pd.get_dummies(s[["sic2", "yq"]].astype(str), drop_first=True,
                       dtype=float)
    X_full = np.column_stack([np.ones(len(s)), s[ctrl].values.astype(float),
                              D.values])
    names_full = ["const"] + ctrl + list(D.columns)
    keep = _independent_columns(X_full)
    X = X_full[:, keep]
    names = [nm for nm, k in zip(names_full, keep) if k]
    y = s[dep].values.astype(float)
    f_codes = pd.factorize(s["permno"].values)[0]
    m_codes = pd.factorize(s["td"].dt.to_period("M").astype(str).values)[0]

    fit = ols_clustered(y, X, f_codes, m_codes)
    beta, V = fit["beta"], fit["V_twoway"]
    se = np.sqrt(np.clip(np.diag(V), 0, None))
    k = names.index("liq_x_post")
    i_beta = names.index("liq")
    t_d = float(beta[k] / se[k]) if se[k] > 0 else np.nan
    p_d = float(2 * (1 - _norm_cdf(abs(t_d)))) if math.isfinite(t_d) else 1.0
    p_wild = wild_cluster_bootstrap(y, X, k, m_codes, n_boot=N_BOOT,
                                    seed=SEED)
    var_sum = V[i_beta, i_beta] + V[k, k] + 2 * V[i_beta, k]
    n_post = int(s["post_td"].sum())
    w = n_post / len(s) if len(s) else float("nan")
    sigma = float(np.std(y, ddof=1))
    se_design = sigma / math.sqrt(len(s) * w * (1 - w)) if 0 < w < 1 else np.nan
    return {
        "label": label,
        "dependent": dep,
        "n": len(s),
        "n_pre": len(s) - n_post,
        "n_post": n_post,
        "w": w,
        "beta_liq_pre": float(beta[i_beta]),
        "se_liq_pre": float(se[i_beta]),
        "implied_post_slope": float(beta[i_beta] + beta[k]),
        "post_slope_se": float(math.sqrt(max(var_sum, 0.0))),
        "delta_liq_x_post": float(beta[k]),
        "se_delta_twoway": float(se[k]),
        "t_delta": t_d,
        "p_delta_normal": p_d,
        "p_delta_wild_month": p_wild,
        "p_delta_quoted_conservative": max(p_d, p_wild),
        "sigma_realised": sigma,
        "mde_design_formula_pp": float(Z_MDE * se_design * 100)
        if math.isfinite(se_design) else None,
        "mde_realised_se_pp": float(Z_MDE * se[k] * 100),
        "mean_dep_pre": float(s.loc[s["post_td"] == 0, dep].mean()),
        "mean_dep_post": float(s.loc[s["post_td"] == 1, dep].mean()),
        "coefficients": {nm: float(b) for nm, b in zip(names, beta)},
    }


def main() -> int:
    s = pd.read_csv(H1_SAMPLE, dtype={"permno": int})
    s["td"] = pd.to_datetime(s["td"])
    # filer dummies recomputed identically to H1
    s["hf"] = (s["filer_type"] == "activist_hf").astype(float)
    s["corp"] = (s["filer_type"] == "corporate").astype(float)
    s["sic2"] = s["sic2"].fillna("NA")
    s["yq"] = (s["td"].dt.year.astype(str) + "Q"
               + s["td"].dt.quarter.astype(str))

    # main sample: §2.5 straddlers + §2.6 stub excluded (as in H1)
    straddle = (s["td"] < RULE_DATE) & (pd.to_datetime(s["fd"]) >= RULE_DATE)
    stub = (s["td"] >= pd.Timestamp("2023-10-10")) & (s["td"] < RULE_DATE)
    main_s = s[~straddle & ~stub].dropna(
        subset=["runup5", "jump", "liq", "logcap", "pre42",
                "wlen_busdays"]).copy()

    # per-day run-up defence (§3.1): RUNUP / (FD*−TD in trading days)
    main_s["runup_perday"] = main_s["runup"] / main_s["runup_trading_days"]

    jump = run_h2(main_s, "jump", "JUMP")
    runup5 = run_h2(main_s, "runup5", "RUNUP5")
    perday = run_h2(main_s, "runup_perday", "RUNUP_perday_defence",
                    extra_ctrl=[])
    # identical-window-length subsample: the modal post-era delay, present
    # in both eras (§3.1's third defence)
    modal_w = int(main_s.loc[main_s["post_td"] == 1, "wlen_busdays"].mode()[0])
    ident = main_s[main_s["wlen_busdays"] == modal_w]
    runup5_ident = run_h2(ident, "runup5", f"RUNUP5_wlen=={modal_w}")

    # §3.5.2's partition-refutation check, reported FIRST
    sig = 0.05
    jump_sig = jump["p_delta_quoted_conservative"] < sig
    same_sign = (np.sign(jump["delta_liq_x_post"])
                 == np.sign(runup5["delta_liq_x_post"])
                 and jump["delta_liq_x_post"] != 0)
    comparable = abs(jump["delta_liq_x_post"]) >= 0.5 * abs(
        runup5["delta_liq_x_post"])
    partition_refuted = bool(jump_sig and same_sign and comparable)

    result = {
        "estimate": "H2 reform slope change (SPEC §3.5)",
        "label": "ESTIMATED",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "branch_selected": ("Branch A (attenuation, HANDOFF_sign.md §8 "
                            "2026-08-30): δ > 0 on RUNUP5 given β < 0"),
        "partition_check_first": {
            "jump_delta": jump["delta_liq_x_post"],
            "jump_p": jump["p_delta_quoted_conservative"],
            "runup5_delta": runup5["delta_liq_x_post"],
            "runup5_p": runup5["p_delta_quoted_conservative"],
            "partition_refuted": partition_refuted,
        },
        "sample": {"rows_in": len(s), "main_n": len(main_s),
                   "main_pre": int((main_s["post_td"] == 0).sum()),
                   "main_post": int((main_s["post_td"] == 1).sum()),
                   "identical_wlen_subsample_n": len(ident),
                   "identical_wlen_value": modal_w},
        "h2_jump": jump,
        "h2_runup5": runup5,
        "h2_runup_perday": perday,
        "h2_runup5_identical_wlen": runup5_ident,
        "seeds": {"wild_bootstrap": SEED},
    }
    out_path = os.path.join(OUT_DIR, "h2_estimate.json")
    with open(out_path, "w") as fh:
        json.dump(result, fh, indent=1)
    print(f"wrote {out_path}", flush=True)

    print("\n== H2 — ESTIMATED ==")
    print(f"  [PARTITION CHECK FIRST — §3.5.2] δ̂(JUMP) "
          f"{jump['delta_liq_x_post']:+.5f} (p {jump['p_delta_quoted_conservative']:.3f})"
          f" vs δ̂(RUNUP5) {runup5['delta_liq_x_post']:+.5f} "
          f"(p {runup5['p_delta_quoted_conservative']:.3f})"
          f" -> partition_refuted={partition_refuted}")
    for r in (runup5, jump, perday, runup5_ident):
        print(f"  {r['label']:>22}: N {r['n']:4d}  β(LIQ) "
              f"{r['beta_liq_pre']:+.5f}  δ "
              f"{r['delta_liq_x_post']:+.5f} (se {r['se_delta_twoway']:.5f}, "
              f"quoted p {r['p_delta_quoted_conservative']:.3f})  "
              f"MDE {r['mde_realised_se_pp']:.2f} pp")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
