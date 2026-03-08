"""Export data for figures/tables.

Run:

    python -m numerical.export_data --output-dir numerical_output

This writes 13 CSVs (for `figures.py`) and 2 LaTeX tables.

The CSV interface is designed to be stable: figures.py reads only these CSVs.
"""

from __future__ import annotations

import csv
import os
from typing import Callable, Dict, List, Optional, Tuple

import numpy as np

from .params import ModelParams, TOL_PROB, TOL_REGION, TOL_RESIDUAL
from .model import (
    EquilibriumObjects,
    bid_probability,
    bid_probability_tilde,
    compute_action_probabilities,
    compute_conditional_means,
    compute_equilibrium_objects,
    compute_minority_gains,
    compute_minority_gains_no_disclosure_given_strategy,
    compute_minority_gains_noisy_rumor_given_strategy,
    compute_posteriors,
    compute_posteriors_no_disclosure,
    compute_posteriors_noisy_rumor,
    noise_probs,
    compute_E_v_given_XD,
    compute_E_v_given_X_no_disclosure,
)
from .solver import compute_series_over_kappa, solve_equilibrium, solve_valid


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def _write_csv(path: str, header: List[str], rows: List[List[str]]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def _fmt(x: float, decimals: int = 10) -> str:
    if x is None:
        return "NA"
    if isinstance(x, (float, np.floating)):
        if (not np.isfinite(x)) or np.isnan(x):
            return "NA"
    return f"{float(x):.{decimals}f}"


# -----------------------------------------------------------------------------
# Baseline params
# -----------------------------------------------------------------------------

def export_baseline_params(params: ModelParams, data_dir: str) -> None:
    rows = [
        ["mu", _fmt(params.mu)],
        ["sigma_v", _fmt(params.sigma_v)],
        ["sigma_eps", _fmt(params.sigma_eps)],
        ["sigma_s", _fmt(params.sigma_s)],
        ["kappa", _fmt(params.kappa)],
        ["C0", _fmt(params.C0)],
        ["chi", _fmt(params.chi)],
        ["rho", _fmt(params.rho)],
        ["Delta", _fmt(params.Delta)],
        ["m0", _fmt(params.m0)],
        ["m1", _fmt(params.m1)],
        ["m_tilde", _fmt(params.m_tilde)],
        ["S_bar", _fmt(params.S_bar)],
        ["Delta_S", _fmt(params.Delta_S)],
        ["K", _fmt(params.K)],
        ["s_xi", _fmt(params.s_xi)],
        ["lambda_B", _fmt(params.lambda_B)],
        ["delta", _fmt(params.delta)],
        ["beta", _fmt(params.beta)],
        ["Delta_tilde", _fmt(params.Delta_tilde)],
    ]
    _write_csv(os.path.join(data_dir, "baseline_params.csv"), ["param", "value"], rows)


# -----------------------------------------------------------------------------
# Cutoff structure
# -----------------------------------------------------------------------------

def export_cutoff_structure(k1: float, k0: float, kD: float, params: ModelParams, data_dir: str) -> None:
    _write_csv(
        os.path.join(data_dir, "baseline_cutoffs.csv"),
        ["k1", "k0", "kD", "mu", "sigma_s"],
        [[_fmt(k1), _fmt(k0), _fmt(kD), _fmt(params.mu), _fmt(params.sigma_s)]],
    )

    # regions for number-line plot
    x_min = params.mu - 3.0 * params.sigma_s
    x_max = max(params.mu + 4.0 * params.sigma_s, kD + 0.5 * params.sigma_s)

    has_hold = (k0 - k1) > TOL_REGION
    regions: List[List[str]] = [["Exit", _fmt(x_min), _fmt(k1)]]
    quiet_left = k0 if has_hold else k1
    if has_hold:
        regions.append(["Hold", _fmt(k1), _fmt(k0)])
    regions.append(["Quiet Voice", _fmt(quiet_left), _fmt(kD)])
    regions.append(["Public Voice", _fmt(kD), _fmt(x_max)])

    _write_csv(os.path.join(data_dir, "cutoff_regions.csv"), ["region", "xmin", "xmax"], regions)


# -----------------------------------------------------------------------------
# Baseline series
# -----------------------------------------------------------------------------

def export_baseline_series(params: ModelParams, data_dir: str, n_points: int = 35) -> Dict[str, np.ndarray]:
    # Use a wider liquidity range to display the full hump (the left tail is
    # visibly truncated on [0.15, 0.85] under the baseline calibration).
    kappa_values = np.linspace(0.05, 0.95, n_points)
    series = compute_series_over_kappa(params, kappa_values)

    rows = []
    for i in range(len(kappa_values)):
        rows.append([
            _fmt(series["kappa"][i]),
            _fmt(series["k1"][i]),
            _fmt(series["k0"][i]),
            _fmt(series["kD"][i]),
            _fmt(series["delta_min"][i]),
            _fmt(series["base"][i]),
            _fmt(series["act"][i]),
        ])

    _write_csv(
        os.path.join(data_dir, "baseline_series.csv"),
        ["kappa", "k1", "k0", "kD", "delta_min", "base", "act"],
        rows,
    )

    return series


# -----------------------------------------------------------------------------
# Prices
# -----------------------------------------------------------------------------

def export_prices(k1: float, k0: float, kD: float, params: ModelParams, data_dir: str) -> None:
    eq = compute_equilibrium_objects(k1, k0, kD, params)

    rows: List[List[str]] = []

    for X in (-2, -1, 0, 1):
        D = 0
        P_post = eq.P_post.get((X, D), float("nan"))
        P_trade = eq.P_trade.get(X, float("nan"))
        pi = eq.posteriors.get((X, D), 0.0)
        E_v = eq.E_v.get((X, D), params.mu)
        V_hat = E_v + params.Delta_tilde * pi
        m_bar = params.m0 + (params.m_tilde - params.m0) * pi
        p_bid = bid_probability(V_hat, m_bar, pi, params) if np.isfinite(P_post) else float("nan")
        on_path = "TRUE" if eq.prob_XD.get((X, D), 0.0) > 1e-4 else "FALSE"
        rows.append([str(X), str(D), _fmt(P_post), _fmt(P_trade), _fmt(pi), _fmt(p_bid), _fmt(m_bar), on_path])

    for X in (0, 1, 2):
        D = 1
        P_post = eq.P_post.get((X, D), float("nan"))
        P_trade = eq.P_trade.get(X, float("nan"))
        pi = 1.0
        E_v = eq.E_v.get((X, D), params.mu)
        V_hat = E_v + params.Delta_tilde * pi
        m_bar = params.m_tilde
        p_bid = bid_probability(V_hat, m_bar, pi, params) if np.isfinite(P_post) else float("nan")
        on_path = "TRUE" if eq.prob_XD.get((X, D), 0.0) > 1e-4 else "FALSE"
        rows.append([str(X), str(D), _fmt(P_post), _fmt(P_trade), _fmt(pi), _fmt(p_bid), _fmt(m_bar), on_path])

    _write_csv(
        os.path.join(data_dir, "prices.csv"),
        ["X", "D", "P_post", "P_trade", "pi", "p_bid", "m_XD", "on_path"],
        rows,
    )


# -----------------------------------------------------------------------------
# Disclosure attenuation (fixed strategy)
# -----------------------------------------------------------------------------

def export_disclosure_attenuation(base_params: ModelParams, k1_ref: float, k0_ref: float, kD_ref: float, data_dir: str, n_points: int = 35) -> None:
    kappa_values = np.linspace(0.05, 0.95, n_points)
    rows: List[List[str]] = []

    for kappa in kappa_values:
        p = base_params.replace(kappa=float(kappa))
        gains_discl = compute_minority_gains(k1_ref, k0_ref, kD_ref, p)
        gains_nd = compute_minority_gains_no_disclosure_given_strategy(k1_ref, k0_ref, kD_ref, p)
        rows.append([_fmt(kappa), _fmt(gains_discl.activism), _fmt(gains_nd.activism)])

    _write_csv(
        os.path.join(data_dir, "disclosure_attenuation.csv"),
        ["kappa", "act_disclosure", "act_no_disclosure"],
        rows,
    )


# -----------------------------------------------------------------------------
# Sensitivity
# -----------------------------------------------------------------------------

def _export_sensitivity(
    base_params: ModelParams,
    param_name: str,
    values: List[float],
    replace_fn: Callable[[ModelParams, float, float], ModelParams],
    data_dir: str,
    csv_name: str,
) -> None:
    kappa_values = np.linspace(0.25, 0.85, 21)
    rows: List[List[str]] = []

    for val in values:
        prev: Optional[Tuple[float, float, float]] = None
        prev_cut = None
        for kappa in kappa_values:
            try:
                p = replace_fn(base_params, float(kappa), float(val))
                cut, res = solve_valid(p, prev_cut)
                if cut is None or (not np.isfinite(res)) or res > TOL_RESIDUAL:
                    rows.append([_fmt(kappa), _fmt(val), "NA"])
                    prev_cut = None
                    continue
                prev_cut = cut
                gains = compute_minority_gains(cut.k1, cut.k0, cut.kD, p)
                rows.append([_fmt(kappa), _fmt(val), _fmt(gains.total)])
            except Exception:
                rows.append([_fmt(kappa), _fmt(val), "NA"])
                prev_cut = None

    _write_csv(os.path.join(data_dir, csv_name), ["kappa", param_name, "delta_min"], rows)


def export_sensitivity_C0(base_params: ModelParams, data_dir: str) -> None:
    _export_sensitivity(
        base_params,
        "C0",
        # Centered around the baseline calibration to illustrate how engagement
        # costs shift the level and curvature of Δ^{min}(κ).
        [0.24, 0.25, 0.35, 0.40],
        replace_fn=lambda bp, k, v: bp.replace(kappa=k, C0=v),
        data_dir=data_dir,
        csv_name="sensitivity_C0.csv",
    )


def export_sensitivity_wedge(base_params: ModelParams, data_dir: str) -> None:
    # Center the sweep on the baseline wedge (m1-m0). Baseline: m1=0.45, m0=0.10 ⇒ wedge=0.35.
    wedges = [0.35, 0.40, 0.45]
    _export_sensitivity(
        base_params,
        "wedge",
        wedges,
        replace_fn=lambda bp, k, w: bp.replace(kappa=k, m1=bp.m0 + w),
        data_dir=data_dir,
        csv_name="sensitivity_wedge.csv",
    )


def export_sensitivity_rho(base_params: ModelParams, data_dir: str) -> None:
    _export_sensitivity(
        base_params,
        "rho",
        # ρ is “success conditional on engagement”, so we focus on a high-success range.
        [0.88, 0.90, 0.92],
        replace_fn=lambda bp, k, r: bp.replace(kappa=k, rho=r),
        data_dir=data_dir,
        csv_name="sensitivity_rho.csv",
    )


def export_sensitivity_sigma_xi(base_params: ModelParams, data_dir: str) -> None:
    _export_sensitivity(
        base_params,
        "s_xi",
        [0.10, 0.12, 0.15],
        replace_fn=lambda bp, k, sxi: bp.replace(kappa=k, s_xi=sxi),
        data_dir=data_dir,
        csv_name="sensitivity_sigma_xi.csv",
    )


def export_sensitivity_delta(base_params: ModelParams, data_dir: str) -> None:
    _export_sensitivity(
        base_params,
        "delta",
        [0.93, 0.95, 0.97],
        replace_fn=lambda bp, k, d: bp.replace(kappa=k, delta=d),
        data_dir=data_dir,
        csv_name="sensitivity_delta.csv",
    )


# -----------------------------------------------------------------------------
# Noisy rumor (fixed strategy)
# -----------------------------------------------------------------------------

def export_noisy_rumor(base_params: ModelParams, k1_ref: float, k0_ref: float, kD_ref: float, data_dir: str) -> None:
    kappa_values = np.linspace(0.25, 0.85, 21)
    rumor_configs = [
        (0.50, 0.50, "Uninformative"),
        (0.75, 0.25, "Moderate"),
        (0.95, 0.05, "Precise"),
    ]

    rows: List[List[str]] = []
    for eta_1, eta_0, label in rumor_configs:
        for kappa in kappa_values:
            try:
                p = base_params.replace(kappa=float(kappa))
                gains = compute_minority_gains_noisy_rumor_given_strategy(k1_ref, k0_ref, kD_ref, p, eta_1, eta_0)
                rows.append([_fmt(kappa), _fmt(eta_1), _fmt(eta_0), label, _fmt(gains.total)])
            except Exception:
                rows.append([_fmt(kappa), _fmt(eta_1), _fmt(eta_0), label, "NA"])

    _write_csv(
        os.path.join(data_dir, "noisy_rumor.csv"),
        ["kappa", "eta_1", "eta_0", "label", "delta_min"],
        rows,
    )


# -----------------------------------------------------------------------------
# Welfare
# -----------------------------------------------------------------------------

def export_welfare(base_params: ModelParams, data_dir: str) -> None:
    from .model import compute_welfare

    kappa_values = np.linspace(0.25, 0.85, 21)
    rows: List[List[str]] = []

    prev_cut = None
    for kappa in kappa_values:
        try:
            p = base_params.replace(kappa=float(kappa))
            cut, res = solve_valid(p, prev_cut)
            if cut is None or (not np.isfinite(res)) or res > TOL_RESIDUAL:
                rows.append([_fmt(kappa), "NA", "NA", "NA"])
                prev_cut = None
                continue
            prev_cut = cut
            W_min, W_bid, _W_B, W_tot = compute_welfare(cut.k1, cut.k0, cut.kD, p)
            rows.append([_fmt(kappa), _fmt(W_min), _fmt(W_bid), _fmt(W_tot)])
        except Exception:
            rows.append([_fmt(kappa), "NA", "NA", "NA"])
            prev_cut = None

    _write_csv(os.path.join(data_dir, "welfare.csv"), ["kappa", "W_min", "W_bid", "W_tot"], rows)


# -----------------------------------------------------------------------------
# LaTeX tables
# -----------------------------------------------------------------------------

def write_baseline_table(k1: float, k0: float, kD: float, params: ModelParams, output_path: str) -> None:
    """Write table_example.tex (used in the appendix)."""

    eq = compute_equilibrium_objects(k1, k0, kD, params)

    def row_for(X: int, D: int) -> str:
        P = eq.P_post.get((X, D), np.nan)
        pi = 1.0 if D == 1 else eq.posteriors.get((X, 0), 0.0)
        E_v = eq.E_v.get((X, D), params.mu)
        V_hat = E_v + params.Delta_tilde * pi
        m_bar = params.m_tilde if D == 1 else (params.m0 + (params.m_tilde - params.m0) * pi)
        p_bid = bid_probability(V_hat, m_bar, pi, params) if np.isfinite(P) else np.nan
        return f"{D} & ${X}$ & {P:.2f} & {pi:.2f} & {p_bid:.2f} & {m_bar:.2f} \\\\"

    lines = [
        "\\begin{tabular}{llrrrr}",
        "\\toprule",
        "$D$ & Order flow $X$ & $P(X,D)$ & $\\pi(X,D)$ & $p(X,D)$ & $\\bar{m}(X,D)$ \\\\",
        "\\midrule",
    ]
    for X in (-2, -1, 0, 1):
        lines.append(row_for(X, 0))
    lines.append("\\midrule")
    for X in (0, 1, 2):
        lines.append(row_for(X, 1))
    lines.extend(["\\bottomrule", "\\end{tabular}"])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def write_disclosure_extension_table(k1: float, k0: float, kD: float, params: ModelParams, output_path: str, eta_1: float = 0.75, eta_0: float = 0.25) -> None:
    """Write table_disclosure_extensions.tex comparing posteriors across regimes."""

    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)

    post_baseline = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    post_nd = compute_posteriors_no_disclosure(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    post_nr = compute_posteriors_noisy_rumor(omega_E, omega_H, omega_Q, omega_P, params.kappa, eta_1, eta_0)

    # Full information posterior over actions (q,a)
    post_fi = {(-1, 0): 0.0, (0, 0): 0.0, (0, 1): 1.0, (1, 1): 1.0}

    fmt = lambda x: f"{float(x):.2f}"

    lines = [
        "\\begin{tabular}{lrrrr}",
        "\\toprule",
        "$X$ & $\\pi(X,0)$ & $\\pi_{\\textup{ND}}(X)$ & $\\pi_{\\textup{NR}}(X,0,R=0)$ & $\\pi_{\\textup{NR}}(X,0,R=1)$ \\\\",
        "\\midrule",
    ]
    for X in (-1, 0, 1):
        lines.append(
            f"${X}$ & {fmt(post_baseline.get((X, 0), 0.0))} & {fmt(post_nd.get(X, 0.0))} & {fmt(post_nr.get((X, 0, 0), 0.0))} & {fmt(post_nr.get((X, 0, 1), 0.0))} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\vspace{0.6em}"])

    lines.extend([
        "\\begin{tabular}{ll}",
        "\\toprule",
        "$(q,a)$ & $\\pi_{\\textup{FI}}$ \\\\",
        "\\midrule",
    ])
    for key in [(-1, 0), (0, 0), (0, 1), (1, 1)]:
        lines.append(f"$({key[0]},{key[1]})$ & {fmt(post_fi.get(key, 0.0))} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}"])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# -----------------------------------------------------------------------------
# Master export
# -----------------------------------------------------------------------------

def export_all(output_dir: str = "numerical_output") -> None:
    data_dir = os.path.join(output_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    params = ModelParams()

    print("Solving baseline equilibrium...")
    cut = solve_equilibrium(params)
    k1, k0, kD = cut.k1, cut.k0, cut.kD
    print(f"Baseline cutoffs: k1={k1:.6f}, k0={k0:.6f}, kD={kD:.6f}")
    print(f"Net deterrence condition (A5) holds: {params.net_deterrence}")

    export_baseline_params(params, data_dir)
    export_cutoff_structure(k1, k0, kD, params, data_dir)
    export_baseline_series(params, data_dir)
    export_prices(k1, k0, kD, params, data_dir)

    # Partial-equilibrium disclosure attenuation (fixed cutoffs at baseline equilibrium)
    export_disclosure_attenuation(params, k1, k0, kD, data_dir)

    # Sensitivities (solve equilibrium under each parameterization)
    export_sensitivity_C0(params, data_dir)
    export_sensitivity_wedge(params, data_dir)
    export_sensitivity_rho(params, data_dir)
    export_sensitivity_sigma_xi(params, data_dir)
    export_sensitivity_delta(params, data_dir)

    # Noisy rumor regime (fixed cutoffs at baseline equilibrium)
    export_noisy_rumor(params, k1, k0, kD, data_dir)

    # Welfare (solve equilibrium)
    export_welfare(params, data_dir)

    # Tables
    write_baseline_table(k1, k0, kD, params, os.path.join(output_dir, "table_example.tex"))
    write_disclosure_extension_table(k1, k0, kD, params, os.path.join(output_dir, "table_disclosure_extensions.tex"))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Export model data to CSV")
    parser.add_argument("--output-dir", default="numerical_output", help="Output directory")
    args = parser.parse_args()

    export_all(output_dir=args.output_dir)
