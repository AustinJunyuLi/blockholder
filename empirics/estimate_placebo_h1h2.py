"""Pseudo-trigger placebo for H1/H2 (SPEC §3.7, first bullet).

Re-runs the H1 partition regression and the H2 reform regressions with the
trigger replaced by TD − 63 trading days (one quarter before the real
crossing) and all windows shifted by the same 63 trading days, so window
lengths are identical by construction. LIQ, the market model and every
window are recomputed at the pseudo-trigger.

Decision rule (registered): the pseudo liquidity slope must be
statistically indistinguishable from zero. A significant pseudo-slope
means LIQ is picking up a firm characteristic, not the trigger, and the
headline is demoted to descriptive.

(The §3.7 13G descriptive placebo needs its own 13G fetch/parse pass and is
NOT run here — flagged as pending in the session log.)

Usage: .venv/bin/python -m empirics.estimate_placebo_h1h2
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
    CrspPanel, OUT_DIR, RULE_DATE, ADOPTION_DATE, Z_MDE, _independent_columns,
    _slice, car, classify_filers, effective_filing_date, load_filings,
    market_model, ols_clustered, sha256_of, trading_day_window,
    wild_cluster_bootstrap,
)

H1_SAMPLE = os.path.join(OUT_DIR, "h1_sample.csv")
PSEUDO_SHIFT_TRADE_DAYS = 63
N_BOOT = 9_999
SEED = 20260834


def shift_trading_days(day: pd.Timestamp, trade_days, n: int) -> pd.Timestamp:
    """n trading days earlier (n > 0 => earlier)."""
    i = np.searchsorted(trade_days, np.datetime64(day.date(), "D"))
    j = i - n
    if j < 0:
        return pd.NaT
    return pd.Timestamp(str(trade_days[j]))


def main() -> int:
    s = pd.read_csv(H1_SAMPLE, dtype={"permno": int})
    s["td"] = pd.to_datetime(s["td"])
    s["fd"] = pd.to_datetime(s["fd"])
    s["fdstar"] = pd.to_datetime(s["fdstar"])
    s["hf"] = (s["filer_type"] == "activist_hf").astype(float)
    s["corp"] = (s["filer_type"] == "corporate").astype(float)
    s["sic2"] = s["sic2"].map(
        lambda v: "MISSING" if pd.isna(v) else f"{int(float(v)):02d}")
    s["yq"] = (s["td"].dt.year.astype(str) + "Q"
               + s["td"].dt.quarter.astype(str))

    print("== CRSP panel ==", flush=True)
    crsp = CrspPanel()

    print("== pseudo-trigger variables (TD - 63 trading days) ==", flush=True)
    rows, n_model_fail, n_pre_snapshot = [], 0, 0
    for r in s.itertuples():
        ptd = shift_trading_days(r.td, crsp.trade_days,
                                 PSEUDO_SHIFT_TRADE_DAYS)
        pfd = shift_trading_days(r.fdstar, crsp.trade_days,
                                 PSEUDO_SHIFT_TRADE_DAYS)
        if pd.isna(ptd) or pd.isna(pfd):
            n_pre_snapshot += 1
            continue
        panel = crsp.panel[int(r.permno)]
        model = market_model(panel, ptd, crsp.market)
        if model is None:
            n_model_fail += 1
            continue
        runup = car(panel, crsp.market, model, ptd,
                    pfd - pd.Timedelta(days=1), crsp.trade_days)
        j_lo, j_hi, _ = trading_day_window(pfd, crsp.trade_days, 1, 1)
        jump = car(panel, crsp.market, model, j_lo, j_hi, crsp.trade_days)
        i5 = np.searchsorted(crsp.trade_days, np.datetime64(ptd.date(), "D"))
        r5_hi = pd.Timestamp(str(crsp.trade_days[min(i5 + 4,
                                                     len(crsp.trade_days) - 1)]))
        runup5 = car(panel, crsp.market, model,
                     pd.Timestamp(str(crsp.trade_days[i5])), r5_hi,
                     crsp.trade_days)
        sl = _slice(panel, ptd - pd.Timedelta(days=126),
                    ptd - pd.Timedelta(days=6))
        v = panel["valid"][sl]
        ret, prc, vol = panel["ret"][sl], panel["prc"][sl], panel["vol"][sl]
        if v.sum() >= 60:
            illiq = float(np.mean(np.abs(ret[v]) / (np.abs(prc[v])
                                                    * vol[v])) * 1e6)
        else:
            illiq = np.nan
        rows.append({
            "accession": r.accession, "permno": int(r.permno),
            "td": r.td, "ptd": ptd, "pfd": pfd,
            "post_td": int(r.td >= RULE_DATE),   # era assignment stays real
            "prunup": runup, "pjump": jump, "prunup5": runup5,
            "pilliq": illiq, "logcap": r.logcap, "pre42": r.pre42,
            "wlen_busdays": r.wlen_busdays, "hf": r.hf, "corp": r.corp,
            "sic2": r.sic2, "yq": r.yq,
        })
    p = pd.DataFrame(rows)
    p["logpilliq"] = np.log(p["pilliq"].where(p["pilliq"] > 0))
    p["pq"] = p["ptd"].dt.year.astype(str) + "Q" + p["ptd"].dt.quarter.astype(str)
    p["pliq"] = p.groupby("pq")["logpilliq"].transform(
        lambda x: -(x - x.mean()) / x.std() if x.std() > 0 else np.nan)
    print(f"  {len(p)} pseudo rows ({n_model_fail} model failures, "
          f"{n_pre_snapshot} shifted before the snapshot)", flush=True)

    def _run(dep, label: str, stacked: bool) -> dict:
        need = ["pliq", "logcap", "pre42", "wlen_busdays"] + (
            ["prunup", "pjump"] if stacked else [dep])
        d = p.dropna(subset=need).reset_index(drop=True)
        if stacked:
            n = len(d)
            L = pd.DataFrame(np.repeat(d.values, 2, axis=0),
                             columns=d.columns)
            L["flagged"] = np.tile([0.0, 1.0], n)
            L["car"] = np.where(L["flagged"] == 1.0, L["pjump"], L["prunup"])
            L["pliq_x_flag"] = L["pliq"] * L["flagged"]
            ctrl = ["pliq", "pliq_x_flag", "flagged", "logcap", "pre42",
                    "wlen_busdays", "hf", "corp"]
        else:
            L = d.copy()
            L["car"] = L[dep]
            L["pliq_x_post"] = L["pliq"] * L["post_td"]
            ctrl = ["pliq", "pliq_x_post", "logcap", "pre42", "wlen_busdays",
                    "hf", "corp"]
        D = pd.get_dummies(L[["sic2", "yq"]].astype(str), drop_first=True,
                           dtype=float)
        X_full = np.column_stack([np.ones(len(L)),
                                  L[ctrl].values.astype(float), D.values])
        names_full = ["const"] + ctrl + list(D.columns)
        keep = _independent_columns(X_full)
        X = X_full[:, keep]
        names = [nm for nm, k in zip(names_full, keep) if k]
        y = L["car"].values.astype(float)
        f_codes = pd.factorize(L["permno"].values)[0]
        m_codes = pd.factorize(
            L["td"].dt.to_period("M").astype(str).values)[0]
        fit = ols_clustered(y, X, f_codes, m_codes)
        beta, V = fit["beta"], fit["V_twoway"]
        se = np.sqrt(np.clip(np.diag(V), 0, None))
        target = "pliq_x_flag" if stacked else "pliq_x_post"
        k = names.index(target)
        t = float(beta[k] / se[k]) if se[k] > 0 else np.nan
        p_n = float(2 * (1 - 0.5 * math.erfc(-abs(t) / math.sqrt(2)))) \
            if math.isfinite(t) else 1.0
        p_w = wild_cluster_bootstrap(y, X, k, m_codes, n_boot=N_BOOT,
                                     seed=SEED)
        return {"label": label, "n": len(L), "coef": float(beta[k]),
                "se": float(se[k]), "t": t, "p_normal": p_n,
                "p_wild_month": p_w,
                "p_quoted_conservative": max(p_n, p_w),
                "mde_pp": float(Z_MDE * se[k] * 100)}

    h1p = _run(None, "pseudo_H1_partition_stacked", stacked=True)
    h2p_r5 = _run("prunup5", "pseudo_H2_RUNUP5", stacked=False)
    h2p_j = _run("pjump", "pseudo_H2_JUMP", stacked=False)

    result = {
        "estimate": "Pseudo-trigger placebo for H1/H2 (SPEC §3.7)",
        "label": "ESTIMATED",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "design": {"shift": f"TD and FD* replaced by -{PSEUDO_SHIFT_TRADE_DAYS} "
                            "trading days; windows identical by construction",
                   "decision_rule": "pseudo slope must be indistinguishable "
                                    "from zero; a significant pseudo-slope "
                                    "demotes the headline to descriptive"},
        "n_rows": len(p),
        "n_model_failures": n_model_fail,
        "n_shifted_before_snapshot": n_pre_snapshot,
        "pseudo_H1_partition": h1p,
        "pseudo_H2_runup5": h2p_r5,
        "pseudo_H2_jump": h2p_j,
        "not_run": ["13G descriptive placebo (needs its own 13G "
                    "fetch/parse pass — pending, §3.7 bullet 2)"],
        "seeds": {"wild_bootstrap": SEED},
    }
    out_path = os.path.join(OUT_DIR, "placebo_h1h2_estimate.json")
    with open(out_path, "w") as fh:
        json.dump(result, fh, indent=1)
    print(f"wrote {out_path}\n")
    print("== PSEUDO-TRIGGER PLACEBO — ESTIMATED ==")
    for r in (h1p, h2p_r5, h2p_j):
        print(f"  {r['label']:>28}: coef {r['coef']:+.5f} "
              f"(se {r['se']:.5f}, quoted p "
              f"{r['p_quoted_conservative']:.3f}, N {r['n']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
