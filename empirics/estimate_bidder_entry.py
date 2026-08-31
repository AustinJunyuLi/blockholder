"""Bidder entry by liquidity (SPEC §9) — the κ-derivative on the control outcome.

Two specifications, both on the BID12 outcome of §8.3:

**W — within 13D targets.**

    BID12_i = α + δ(LIQ_i × Post_i) + β LIQ_i + γ Post_i + X_i'θ + FE + ε_i

**T — triple difference against the matched controls.**

    BID12_i = α + τ(Treat_i × Post_i × LIQ_i) + [all two-way interactions]
              + X_i'θ + δ_match + ε_i

τ is the object: does the Feb-2024 acceleration's effect on bidder entry differ
by liquidity?

Five implementation decisions the SPEC leaves open, fixed here and reported in
the output rather than left to be inferred:

1. **The within spec carries industry fixed effects, not calendar-quarter
   ones.** Quarter FE would absorb Post, which is the interaction's own base
   term; §9's "FE" is therefore read as 2-digit SIC. The quarter dimension
   enters through clustering instead.
2. **Control-side LIQ is constructed here, because it does not exist
   upstream.** SPEC §9 says so explicitly: the control universe file carries
   identity and listing columns only. LIQ keeps its §3.2 definition — the
   within-quarter standardisation of log ILLIQ, **negated so that higher means
   more liquid** — and is standardised over the pooled matched sample
   (treated + matched controls) within each calendar quarter, so treated and
   control sit on one scale. The treated-only H1 standardisation is *not*
   reused: applying a treated-sample mean and sd to controls would put the two
   groups on different scales and load the difference onto β and τ.
3. **Match fixed effects are absorbed by within-group demeaning** (FWL), as in
   `estimate_did`, so the 9,999-draw wild bootstrap stays tractable. Post is
   absorbed with them (constant within match group); Post × LIQ is not, since
   LIQ varies within group.
4. **The main sample ends 2024-12-17**, before the structured-data mandate.
   Observations from 2024-12-18 onward stay out of the estimate; the 2025
   extension remains unestimated until it has its own parse-rate table.
5. **S2 remains unestimated.** The corporate-action Item-4 coding and its
   30-filing audit do not exist, so the script reports the registered realised-
   count MDE rule of thumb without inventing an S2 sample.

The realised MDE of τ is computed and printed against SPEC §9's rule of thumb
(≈ 18.2 pp on S1, obtained by doubling §8.6's 9.09 pp). §9's registered
reading — this leg is not powered to detect anything economically plausible —
is reported with the estimate whichever way the number lands.

Usage:
    .venv/bin/python -m empirics.estimate_bidder_entry
    .venv/bin/python -m empirics.estimate_bidder_entry --spec within
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os

import numpy as np
import pandas as pd

from empirics.estimate_h1 import (
    OUT_DIR, RULE_DATE, ADOPTION_DATE, Z_MDE,
    _independent_columns, ols_clustered, sha256_of, wild_cluster_bootstrap,
)
from empirics.estimate_did import (
    CONTROL_LOOKUP_CSV, H1_SAMPLE_CSV, MATCH_OUT, _demean, build_treated,
)

RESULT_OUT = os.path.join(OUT_DIR, "bidder_entry_estimate.json")
N_BOOT = 9_999
SEED = 20260830
MAIN_SAMPLE_END = pd.Timestamp("2024-12-17")

# SPEC §9's rescaled rule of thumb, printed alongside the realised MDE.
MDE_RULE_OF_THUMB_PP = {"S1": 18.2, "S1_crsp_matched_variant": 15.8,
                        "S2": 40.6}


def _p_normal(t: float) -> float:
    return float(2 * (1 - 0.5 * math.erfc(-abs(t) / math.sqrt(2))))


def _quarter(td: pd.Series) -> pd.Series:
    td = pd.to_datetime(td)
    return td.dt.year.astype(str) + "Q" + td.dt.quarter.astype(str)


def standardise_liq(logilliq: pd.Series, quarter: pd.Series) -> pd.Series:
    """§3.2 LIQ: within-quarter standardised log ILLIQ, negated so that a
    higher value means a *more liquid* firm."""
    df = pd.DataFrame({"x": logilliq.astype(float), "q": quarter})
    return df.groupby("q")["x"].transform(
        lambda s: -(s - s.mean()) / s.std() if s.std(ddof=1) > 0 else np.nan)


def spec_within(tr: pd.DataFrame) -> dict:
    """W — within 13D targets, industry FE, month-clustered."""
    D = tr.dropna(subset=["bid12", "liq", "logcap"]).copy()
    D["liq_x_post"] = D["liq"] * D["post"]
    X = np.column_stack([
        np.ones(len(D)),
        D[["liq_x_post", "liq", "post", "logcap"]].values.astype(float),
        pd.get_dummies(D["sic2"].astype(str), drop_first=True,
                       dtype=float).values])
    keep = _independent_columns(X)
    X = X[:, keep]
    y = D["bid12"].values.astype(float)
    m_codes = pd.factorize(
        pd.to_datetime(D["td"]).dt.to_period("M").astype(str).values)[0]
    s_codes = pd.factorize(D["sic2"].astype(str).values)[0]
    fit = ols_clustered(y, X, s_codes, m_codes)
    se = np.sqrt(np.clip(np.diag(fit["V_twoway"]), 0, None))
    k = 1                                    # liq_x_post
    kb = 2                                   # liq main effect
    t = float(fit["beta"][k] / se[k]) if se[k] > 0 else float("nan")
    tb = float(fit["beta"][kb] / se[kb]) if se[kb] > 0 else float("nan")
    p_w = wild_cluster_bootstrap(y, X, k, m_codes, n_boot=N_BOOT, seed=SEED)
    return {
        "n": len(D),
        "n_pre": int((D["post"] == 0).sum()),
        "n_post": int((D["post"] == 1).sum()),
        "bid12_rate": float(D["bid12"].mean()),
        "fixed_effects": "2-digit SIC (not calendar quarter — quarter FE would "
                         "absorb Post, the interaction's own base term)",
        "se": "two-way clustered (SIC2, calendar month of TD)",
        "delta_liq_x_post_pp": float(fit["beta"][k] * 100),
        "se_delta_pp": float(se[k] * 100),
        "t_delta": t,
        "p_delta_normal": _p_normal(t),
        "p_delta_wild_month": p_w,
        "p_delta_quoted_conservative": max(_p_normal(t), p_w),
        "mde_delta_pp_realised": float(Z_MDE * se[k] * 100),
        "beta_liq_pp": float(fit["beta"][kb] * 100),
        "se_beta_pp": float(se[kb] * 100),
        "t_beta": tb,
        "p_beta_normal": _p_normal(tb),
        "liq_sd_in_sample": float(D["liq"].std(ddof=1)),
    }


def spec_triple(tr: pd.DataFrame) -> dict:
    """T — triple difference on the matched sample, or a pending status."""
    if not (os.path.exists(MATCH_OUT) and os.path.exists(CONTROL_LOOKUP_CSV)):
        return {"status": "matched inputs not landed — run estimate_did's "
                          "matching stage and bid12_control_lookup first"}
    pairs = pd.read_csv(MATCH_OUT)
    eligible_groups = set(tr["accession"].astype(str))
    n_pairs_outside_sample = int(
        (~pairs["match_group"].astype(str).isin(eligible_groups)).sum())
    pairs = pairs[pairs["match_group"].astype(str).isin(eligible_groups)].copy()
    cl = pd.read_csv(CONTROL_LOOKUP_CSV, dtype={"cik": str})
    cl["td"] = cl["td"].astype(str).str[:10]
    ckey = {(int(r.permno), str(r.td), str(r.match_group)): r
            for r in cl.itertuples()}

    rows = []
    for r in tr.itertuples():
        rows.append({"treat": 1, "post": int(r.post), "bid12": r.bid12,
                     "logilliq": float(r.logilliq), "logcap": float(r.logcap),
                     "td": str(r.td.date()), "match_group": r.accession})
    n_missing = 0
    n_prior_bid = 0
    for r in pairs.itertuples():
        key = (int(r.control_permno), str(r.treated_td), str(r.match_group))
        if key not in ckey or not np.isfinite(r.control_logilliq):
            n_missing += 1
            continue
        if int(ckey[key].excluded_prior_bid) == 1:
            n_prior_bid += 1
            continue
        rows.append({"treat": 0, "post": int(r.treated_post),
                     "bid12": ckey[key].bid12,
                     "logilliq": float(r.control_logilliq),
                     "logcap": float(r.control_logcap),
                     "td": str(r.treated_td), "match_group": r.match_group})
    D = pd.DataFrame(rows).dropna(
        subset=["bid12", "logcap", "logilliq"]).copy()

    # LIQ on one scale across treated and control (decision 2 in the docstring)
    D["quarter"] = _quarter(D["td"])
    D["liq"] = standardise_liq(D["logilliq"], D["quarter"])
    D = D.dropna(subset=["liq"]).copy()

    sizes = D.groupby("match_group")["treat"].agg(["min", "max"])
    live = sizes[(sizes["min"] == 0) & (sizes["max"] == 1)].index
    n_dropped_groups = int(sizes.shape[0] - len(live))
    D = D[D["match_group"].isin(set(live))].copy()
    if D.empty:
        return {"status": "no match group retains both a treated and a "
                          "control row"}

    D["tp"] = D["treat"] * D["post"]
    D["tl"] = D["treat"] * D["liq"]
    D["pl"] = D["post"] * D["liq"]
    D["tpl"] = D["treat"] * D["post"] * D["liq"]
    g_codes = pd.factorize(D["match_group"].values)[0]
    m_codes = pd.factorize(
        pd.to_datetime(D["td"]).dt.to_period("M").astype(str).values)[0]

    cols = ["tpl", "tp", "tl", "pl", "treat", "liq",
            "logcap", "logilliq"]   # post absorbed by FE
    Xw = np.column_stack([_demean(D[c].values.astype(float), g_codes)
                          for c in cols])
    keep = _independent_columns(Xw)
    dropped = [c for c, k in zip(cols, keep) if not k]
    Xw = Xw[:, keep]
    kept = [c for c, k in zip(cols, keep) if k]
    y = _demean(D["bid12"].values.astype(float), g_codes)
    fit = ols_clustered(y, Xw, g_codes, m_codes)
    se = np.sqrt(np.clip(np.diag(fit["V_twoway"]), 0, None))
    k = kept.index("tpl")
    t = float(fit["beta"][k] / se[k]) if se[k] > 0 else float("nan")
    p_w = wild_cluster_bootstrap(y, Xw, k, m_codes, n_boot=N_BOOT, seed=SEED)
    mde = float(Z_MDE * se[k] * 100)
    return {
        "status": "estimated",
        "n": len(D),
        "treated_n": int((D["treat"] == 1).sum()),
        "control_n": int((D["treat"] == 0).sum()),
        "match_groups": int(D["match_group"].nunique()),
        "pairs_dropped_no_control_outcome_or_liq": n_missing,
        "pairs_excluded_outside_treated_sample": n_pairs_outside_sample,
        "controls_excluded_prior_bid": n_prior_bid,
        "match_groups_dropped_no_contrast": n_dropped_groups,
        "terms_estimated": kept,
        "terms_dropped_collinear": dropped,
        "x_adjustment": ["logcap", "logilliq"],
        "post_main_effect": "absorbed by the match fixed effects (constant "
                            "within group); Post x LIQ is not, since LIQ "
                            "varies within group",
        "liq_definition": "§3.2 within-quarter standardised log ILLIQ, "
                          "negated (higher = more liquid), standardised over "
                          "the pooled matched sample",
        "liq_sd_in_matched_sample": float(D["liq"].std(ddof=1)),
        "tau_treat_x_post_x_liq_pp": float(fit["beta"][k] * 100),
        "se_tau_pp": float(se[k] * 100),
        "t_tau": t,
        "p_tau_normal": _p_normal(t),
        "p_tau_wild_month": p_w,
        "p_tau_quoted_conservative": max(_p_normal(t), p_w),
        "mde_tau_pp_realised": mde,
        "mde_tau_pp_rule_of_thumb": MDE_RULE_OF_THUMB_PP,
        "coefficients_pp": {c: float(b * 100)
                            for c, b in zip(kept, fit["beta"])},
        "se_pp": {c: float(s * 100) for c, s in zip(kept, se)},
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--spec", choices=("within", "triple", "both"),
                    default="both")
    args = ap.parse_args(argv)

    out = {
        "estimate": "Bidder entry by liquidity (SPEC §9)",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "script": "empirics/estimate_bidder_entry.py",
        "requested_spec": args.spec,
        "sample_window": {
            "main_end": str(MAIN_SAMPLE_END.date()),
            "structured_data_extension_start": "2024-12-18",
        },
        "extension_2025": {
            "status": "NOT ESTIMATED",
            "treated_rows": None,
            "reason": "The 2025 extension requires its own structured-data "
                      "parse-rate table.",
        },
        "S2": {
            "status": "NOT ESTIMATED",
            "reason": "The corporate-action Item-4 coding and 30-filing "
                      "audit are absent.",
            "mde_tau_pp_rule_of_thumb_realised_counts":
                MDE_RULE_OF_THUMB_PP["S2"],
        },
    }

    # The matched inputs are needed by the triple difference only. Gating the
    # whole script on them would let `--spec within`, which reads nothing but
    # the treated sample, overwrite a real result with a pending stub.
    missing = ([p for p in (MATCH_OUT, CONTROL_LOOKUP_CSV)
                if not os.path.exists(p)]
               if args.spec in ("triple", "both") else [])
    if missing and args.spec == "triple":
        out.update({
            "label": "NOT ESTIMATED",
            "status": "pending_matched_inputs",
            "pending_inputs": missing,
            "next_step": "Run the matched DiD matching stage and the BID12 "
                         "control lookup before estimating §9.",
        })
        with open(RESULT_OUT, "w") as fh:
            json.dump(out, fh, indent=1)
        print("§9 NOT ESTIMATED: matched inputs have not landed")
        print(f"wrote pending artifact {RESULT_OUT}")
        return 2
    if missing:
        # --spec both: the within-13D-targets half stands on its own, so run
        # it and let spec_triple record its own pending status.
        print("§9 matched inputs have not landed: "
              f"{', '.join(os.path.basename(p) for p in missing)}. The "
              "within-13D-targets leg does not need them and still runs.")

    tr, funnel = build_treated()
    extension = tr[tr["td"] > MAIN_SAMPLE_END].copy()
    funnel = dict(funnel)
    funnel["excluded_after_2024_12_17"] = len(extension)
    tr = tr[tr["td"] <= MAIN_SAMPLE_END].copy()
    funnel["bidder_entry_main_sample"] = len(tr)
    funnel["bidder_entry_main_pre"] = int((tr["post"] == 0).sum())
    funnel["bidder_entry_main_post"] = int((tr["post"] == 1).sum())
    h1 = pd.read_csv(H1_SAMPLE_CSV)
    tr = tr.merge(h1[["accession", "liq"]], on="accession", how="left")
    print(f"treated sample: {len(tr)} rows "
          f"({funnel['bidder_entry_main_pre']} pre / "
          f"{funnel['bidder_entry_main_post']} post), main sample through "
          f"{MAIN_SAMPLE_END.date()}")

    out.update({
        "label": "ESTIMATED",
        "status": "estimated",
        "inputs": {p: sha256_of(p) for p in
                   (os.path.join(OUT_DIR, "bid12_treated.csv"),
                    H1_SAMPLE_CSV, MATCH_OUT, CONTROL_LOOKUP_CSV)
                   if os.path.exists(p)},
        "treated_funnel": funnel,
        "seeds": {"wild_bootstrap": SEED}, "n_boot": N_BOOT,
        "registered_reading_spec_sec9": (
            "This leg is not powered to detect anything economically "
            "plausible (SPEC §9, rescaled 2026-08-30). The registered reading "
            "is reported with the estimate whichever way the number lands; "
            "the realised MDE is quoted in the same sentence as the point "
            "estimate."),
    })
    out["sample_window"]["rows_excluded_after_main_end"] = len(extension)
    out["extension_2025"]["treated_rows"] = int(
        (extension["td"].dt.year == 2025).sum())
    if args.spec in ("within", "both"):
        print("== W: within 13D targets ==", flush=True)
        out["within"] = spec_within(tr)
        w = out["within"]
        print(f"  δ(LIQ×Post) = {w['delta_liq_x_post_pp']:+.2f} pp "
              f"(se {w['se_delta_pp']:.2f}, quoted p "
              f"{w['p_delta_quoted_conservative']:.3f}, realised MDE "
              f"{w['mde_delta_pp_realised']:.2f} pp)")
        print(f"  β(LIQ) = {w['beta_liq_pp']:+.2f} pp "
              f"(se {w['se_beta_pp']:.2f}, p {w['p_beta_normal']:.3f})")
    if args.spec in ("triple", "both"):
        print("== T: triple difference ==", flush=True)
        out["triple"] = spec_triple(tr)
        tt = out["triple"]
        if tt.get("status") == "estimated":
            print(f"  τ(Treat×Post×LIQ) = {tt['tau_treat_x_post_x_liq_pp']:+.2f}"
                  f" pp (se {tt['se_tau_pp']:.2f}, quoted p "
                  f"{tt['p_tau_quoted_conservative']:.3f}, realised MDE "
                  f"{tt['mde_tau_pp_realised']:.2f} pp vs the §9 rule of "
                  f"thumb {MDE_RULE_OF_THUMB_PP['S1']} pp)")
        else:
            print(f"  {tt['status']}")

    with open(RESULT_OUT, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"wrote {RESULT_OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
