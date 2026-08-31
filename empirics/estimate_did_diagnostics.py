"""Registered placebo and pre-trend diagnostics for the matched BID12 DiD.

The SPEC section 8.7 placebo is blocked before estimation when any registered
pseudo-date lacks treated observations on both sides. A blocked run writes the
full 568-date support table and a JSON diagnostic, but no estimate or figure.

Usage:
    .venv/bin/python -m empirics.estimate_did_diagnostics
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os

import numpy as np
import pandas as pd
from scipy.stats import f as f_dist

from empirics.estimate_did import _demean
from empirics.estimate_h1 import OUT_DIR, sha256_of
from empirics.estimate_h1 import ols_clustered
from empirics.facts import FEDERAL_HOLIDAYS
from pyfig.style import SENS_COLORS, apply_style, new_ax, save_fig


TREATED = os.path.join(OUT_DIR, "bid12_treated.csv")
CONTROLS = os.path.join(OUT_DIR, "bid12_control.csv")
PAIRS = os.path.join(OUT_DIR, "did_match_pairs.csv")
ESTIMATE = os.path.join(OUT_DIR, "did_estimate.json")

PLACEBO_START = np.datetime64("2021-07-01")
ADOPTION = np.datetime64("2023-10-10")
PRE_QUARTERS = [
    "2022Q1", "2022Q2", "2022Q3", "2022Q4",
    "2023Q1", "2023Q2", "2023Q3",
]
PRE_REFERENCE = "2023Q3"


def placebo_dates() -> np.ndarray:
    days = np.arange(PLACEBO_START, ADOPTION)
    return days[np.is_busday(days, holidays=FEDERAL_HOLIDAYS)]


def matched_panel(treated_path: str, controls_path: str,
                  pairs_path: str) -> tuple[pd.DataFrame, dict]:
    treated = pd.read_csv(treated_path, usecols=["accession", "td", "bid12"])
    pairs = pd.read_csv(pairs_path, usecols=[
        "treated_permno", "treated_accession", "treated_td",
        "control_permno", "match_group",
    ])
    groups = pairs[[
        "treated_permno", "treated_accession", "treated_td", "match_group",
    ]].drop_duplicates()
    if groups["match_group"].duplicated().any():
        raise ValueError("match groups map to more than one treated row")
    merged = groups.merge(
        treated, left_on="treated_accession", right_on="accession",
        how="left", validate="one_to_one")
    if merged["bid12"].isna().any():
        raise ValueError("matched treated rows contain missing BID12 values")
    pair_td = pd.to_datetime(merged["treated_td"], errors="coerce")
    treated_td = pd.to_datetime(merged["td"], errors="coerce")
    if pair_td.isna().any() or treated_td.isna().any():
        raise ValueError("matched treated rows contain invalid trigger dates")
    if not pair_td.equals(treated_td):
        raise ValueError("treated trigger dates disagree between inputs")
    tr = pd.DataFrame({
        "permno": merged["treated_permno"].astype(int),
        "td": pair_td,
        "treat": 1,
        "bid12": merged["bid12"].astype(float),
        "match_group": merged["match_group"].astype(str),
    })

    control_cols = ["permno", "td", "match_group", "bid12"]
    optional = [c for c in ("excluded_prior_bid",)
                if c in pd.read_csv(controls_path, nrows=0).columns]
    controls = pd.read_csv(controls_path, usecols=control_cols + optional)
    selected = pairs[["control_permno", "treated_td", "match_group"]]
    ct = selected.merge(
        controls, left_on=["control_permno", "match_group"],
        right_on=["permno", "match_group"], how="left", validate="one_to_one")
    control_td = pd.to_datetime(ct["td"], errors="coerce")
    pair_control_td = pd.to_datetime(ct["treated_td"], errors="coerce")
    if control_td.isna().any() or not control_td.equals(pair_control_td):
        raise ValueError("control pseudo-trigger dates disagree between inputs")

    # Two registered drops, both of which estimate_did.stage_estimate makes.
    # The diagnostics must certify the sample the estimate is computed on,
    # so they are made identically here and counted rather than raised on:
    # an unresolved control BID12 (rulebook 7 and 5.1 item 5) is a missing
    # value, not a zero, and a control already under an announced bid at its
    # pseudo-TD is excluded by SPEC 8.3.
    dropped = {}
    keep = ct["bid12"].notna()
    dropped["controls_unresolved_bid12"] = int((~keep).sum())
    if optional:
        prior = pd.to_numeric(ct["excluded_prior_bid"],
                              errors="coerce").fillna(0) == 1
        dropped["controls_excluded_prior_bid"] = int((keep & prior).sum())
        keep &= ~prior
    else:
        dropped["controls_excluded_prior_bid"] = 0
    ct = ct[keep]

    ct = pd.DataFrame({
        "permno": ct["control_permno"].astype(int),
        "td": pd.to_datetime(ct["treated_td"]),
        "treat": 0,
        "bid12": ct["bid12"].astype(float),
        "match_group": ct["match_group"].astype(str),
    })
    panel = pd.concat([tr, ct], ignore_index=True)

    # A group with no surviving control carries no within-group contrast and
    # is absorbed entirely by the match fixed effects. Dropped and counted,
    # exactly as stage_estimate does.
    live = panel.groupby("match_group")["treat"].agg(["min", "max"])
    keep_groups = set(live[(live["min"] == 0) & (live["max"] == 1)].index)
    dropped["match_groups_dropped_no_contrast"] = int(
        live.shape[0] - len(keep_groups))
    panel = panel[panel["match_group"].isin(keep_groups)].reset_index(drop=True)
    if panel.empty:
        raise ValueError("no match group retains both a treated and a "
                         "control row after the registered drops")
    return panel, dropped


def placebo_support(treated_td: pd.Series) -> pd.DataFrame:
    pre_adoption = treated_td[treated_td < pd.Timestamp(str(ADOPTION))]
    rows = []
    for day in placebo_dates():
        d = pd.Timestamp(str(day))
        n_pre = int((pre_adoption < d).sum())
        n_post = int((pre_adoption >= d).sum())
        rows.append({
            "pseudo_date": str(day),
            "n_treated_pre": n_pre,
            "n_treated_post": n_post,
            "two_sided_treated_support": int(n_pre > 0 and n_post > 0),
        })
    return pd.DataFrame(rows)


def pretrend(panel: pd.DataFrame, out_dir: str) -> dict:
    sample = panel.copy()
    sample["quarter"] = sample["td"].dt.to_period("Q").astype(str)
    sample = sample[sample["quarter"].isin(PRE_QUARTERS)].copy()
    present = set(sample["quarter"])
    missing = [q for q in PRE_QUARTERS if q not in present]
    if missing:
        return {"status": "BLOCKED", "missing_quarters": missing}

    g_codes = pd.factorize(sample["match_group"])[0]
    m_codes = pd.factorize(sample["td"].dt.to_period("M").astype(str))[0]
    treat = sample["treat"].to_numpy(dtype=float)
    interaction_quarters = [q for q in PRE_QUARTERS if q != PRE_REFERENCE]
    X = np.column_stack([
        _demean(treat, g_codes),
        *[_demean(treat * (sample["quarter"] == q).to_numpy(dtype=float),
                  g_codes) for q in interaction_quarters],
    ])
    fit = ols_clustered(
        _demean(sample["bid12"].to_numpy(dtype=float), g_codes),
        X, g_codes, m_codes)
    beta = fit["beta"]
    covariance = fit["V_twoway"]
    se = np.sqrt(np.clip(np.diag(covariance), 0, None))

    joint_beta = beta[1:]
    joint_covariance = covariance[1:, 1:]
    joint_rank = int(np.linalg.matrix_rank(joint_covariance))
    if joint_rank != len(interaction_quarters):
        return {
            "status": "BLOCKED",
            "detail": (f"joint covariance rank {joint_rank}, expected "
                       f"{len(interaction_quarters)}"),
        }
    joint_f = float(
        joint_beta @ np.linalg.inv(joint_covariance) @ joint_beta
        / len(interaction_quarters))
    denominator_df = int(min(len(np.unique(g_codes)),
                             len(np.unique(m_codes))) - 1)
    joint_p = float(f_dist.sf(
        joint_f, len(interaction_quarters), denominator_df))

    rows = []
    for quarter in PRE_QUARTERS:
        if quarter == PRE_REFERENCE:
            coefficient = standard_error = 0.0
        else:
            i = interaction_quarters.index(quarter) + 1
            coefficient, standard_error = float(beta[i]), float(se[i])
        rows.append({
            "quarter": quarter,
            "coefficient": coefficient,
            "coefficient_pp": 100 * coefficient,
            "se_twoway": standard_error,
            "ci95_low": coefficient - 1.96 * standard_error,
            "ci95_high": coefficient + 1.96 * standard_error,
            "ci95_low_pp": 100 * (coefficient - 1.96 * standard_error),
            "ci95_high_pp": 100 * (coefficient + 1.96 * standard_error),
            "reference": int(quarter == PRE_REFERENCE),
        })
    coefficients = pd.DataFrame(rows)
    coefficients.to_csv(os.path.join(out_dir, "did_pretrend.csv"), index=False)

    apply_style()
    fig, ax = new_ax()
    x = np.arange(len(coefficients))
    ax.errorbar(
        x, coefficients["coefficient_pp"],
        yerr=1.96 * coefficients["se_twoway"] * 100,
        fmt="o", color=SENS_COLORS[0], capsize=3)
    ax.axhline(0, color="#8c8c8c", linewidth=0.8)
    ax.set_xticks(x, coefficients["quarter"], rotation=45, ha="right")
    ax.set_ylabel("Treat-control gap relative to 2023Q3 (pp)")
    ax.set_title("Matched BID12 pre-trends")
    save_fig(fig, os.path.join(out_dir, "did_pretrend.pdf"))

    return {
        "status": "ESTIMATED",
        "label": "ESTIMATED",
        "reference_quarter": PRE_REFERENCE,
        "n_rows": len(sample),
        "n_match_groups": int(sample["match_group"].nunique()),
        "n_month_clusters": int(len(np.unique(m_codes))),
        "joint_f": joint_f,
        "joint_f_numerator_df": len(interaction_quarters),
        "joint_f_denominator_df": denominator_df,
        "joint_f_p": joint_p,
        "causal_language_allowed": joint_p >= 0.10,
        "decision_rule": "p < 0.10 blocks causal language",
        "quarter_fe": (
            "not identified; quarter is constant within match group under "
            "pseudo-TD inheritance, the same reason lambda Post is absorbed "
            "in the section 8.4 LPM"),
        "coefficients": coefficients.to_dict(orient="records"),
    }


def run(treated_path: str, controls_path: str, pairs_path: str,
        estimate_path: str, out_dir: str) -> int:
    for path in (treated_path, controls_path, pairs_path, estimate_path):
        if not os.path.exists(path):
            raise FileNotFoundError(path)
    with open(estimate_path, encoding="utf-8") as fh:
        estimate = json.load(fh)
    label = estimate.get("label")
    if label not in ("ESTIMATED", "NOT ESTIMATED"):
        raise ValueError(
            f"DiD input carries an unrecognised label {label!r}; expected "
            "ESTIMATED or the registered NOT ESTIMATED design failure")

    panel, panel_drops = matched_panel(treated_path, controls_path, pairs_path)
    treated_td = panel.loc[panel["treat"] == 1, "td"]
    support = placebo_support(treated_td)
    if len(support) != 568:
        raise AssertionError(f"registered placebo grid has {len(support)}, not 568 dates")

    n_two_sided = int(support["two_sided_treated_support"].sum())
    n_no_pre = int((support["n_treated_pre"] == 0).sum())
    n_no_post = int((support["n_treated_post"] == 0).sum())
    blockers = []
    # A section 8 design failure bars the coefficient, not the panel. The
    # pre-trend is a statement about the matched sample and still runs; it
    # simply has no estimate to license causal language for.
    if label != "ESTIMATED":
        blockers.append({
            "code": "did_not_estimated",
            "detail": (f"the section 8 estimate carries label {label!r} "
                       f"({estimate.get('status', 'unknown status')}: "
                       f"{estimate.get('reason', 'no reason recorded')}), so "
                       "there is no coefficient for the placebo band or the "
                       "pre-trend to certify"),
        })
    if n_two_sided != len(support):
        blockers.append({
            "code": "pseudo_date_support",
            "detail": (f"{len(support) - n_two_sided} of 568 registered "
                       "pseudo-dates lack treated observations on one side"),
        })
    blockers.extend([
        {
            "code": "rematch_inputs_missing",
            "detail": ("Final match pairs contain selected controls only. They "
                       "cannot reproduce the section 8.7 requirement to re-match "
                       "the full candidate pool at every pseudo-date."),
        },
        {
            "code": "length_ratio_rule_undefined",
            "detail": ("Section 8.7 fixes the real pre/post length ratio but does "
                       "not state the window-selection rule around each pseudo-date."),
        },
    ])
    os.makedirs(out_dir, exist_ok=True)
    pretrend_result = pretrend(panel, out_dir)
    if pretrend_result["status"] == "BLOCKED":
        blockers.append({
            "code": "pretrend_not_estimable",
            "detail": pretrend_result.get(
                "detail", f"missing quarters {pretrend_result['missing_quarters']}"),
        })
    result = {
        "label": "DIAGNOSTIC",
        "status": "BLOCKED",
        "causal_language_allowed": False,
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "script": "empirics/estimate_did_diagnostics.py",
        "inputs": {path: sha256_of(path) for path in
                   (treated_path, controls_path, pairs_path, estimate_path)},
        "real_estimate_label": label,
        "real_beta_treat_x_post": estimate.get("beta_treat_x_post"),
        "panel_drops": panel_drops,
        "placebo": {
            "registered_range": ["2021-07-01", "2023-10-09"],
            "calendar": "repo FEDERAL_HOLIDAYS",
            "n_candidate_dates": len(support),
            "n_dates_with_two_sided_treated_support": n_two_sided,
            "n_estimable_dates": 0,
            "n_dates_without_pre_treated": n_no_pre,
            "n_dates_without_post_treated": n_no_post,
            "estimates_written": 0,
        },
        "pretrend": pretrend_result,
        "blockers": blockers,
    }
    support.to_csv(os.path.join(out_dir, "did_placebo_support.csv"), index=False)
    with open(os.path.join(out_dir, "did_diagnostics.json"), "w",
              encoding="utf-8") as fh:
        json.dump(result, fh, indent=1)
    print("BLOCKED: section 8.7 cannot produce the registered 568 estimates")
    for blocker in blockers:
        print(f"  {blocker['code']}: {blocker['detail']}")
    return 2


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--treated", default=TREATED)
    ap.add_argument("--controls", default=CONTROLS)
    ap.add_argument("--pairs", default=PAIRS)
    ap.add_argument("--estimate", default=ESTIMATE)
    ap.add_argument("--out-dir", default=OUT_DIR)
    args = ap.parse_args(argv)
    try:
        return run(args.treated, args.controls, args.pairs,
                   args.estimate, args.out_dir)
    except (FileNotFoundError, ValueError, AssertionError) as exc:
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
