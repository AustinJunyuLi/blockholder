"""
Data export for the Exit-Voice-Takeover model.

Extracts computation logic from figures.py and writes CSV files
for downstream R/ggplot2 visualization.  No matplotlib dependency.

Usage:
    python -m numerical.export_data [--output-dir DIR]
"""

from __future__ import annotations

import csv
import os
from typing import Dict, List, Optional, Tuple

import numpy as np

from numerical.params import (
    Cutoffs,
    ModelParams,
    TOL_PROB,
    TOL_REGION,
    TOL_RESIDUAL,
)
from numerical.model import (
    bid_probability,
    compute_action_probabilities,
    compute_conditional_means,
    compute_equilibrium_prices,
    compute_minority_gains,
    compute_minority_gains_no_disclosure_given_strategy,
    compute_minority_gains_noisy_rumor,
    compute_posteriors,
    compute_posteriors_full_information,
    compute_posteriors_no_disclosure,
    compute_posteriors_noisy_rumor,
    compute_welfare,
)
from numerical.solver import (
    compute_series_over_kappa,
    solve_equilibrium,
    solve_valid,
)


# ============================================================================
# CSV WRITING HELPERS
# ============================================================================


def _write_csv(path: str, header: List[str], rows: List[List]) -> None:
    """Write a CSV file with the given header and rows."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def _fmt(x: float, decimals: int = 10) -> str:
    """Format a float for CSV output, preserving NaN."""
    if x is None or (isinstance(x, float) and (np.isnan(x) or not np.isfinite(x))):
        return "NA"
    return f"{x:.{decimals}f}"


# ============================================================================
# EXPORT FUNCTIONS
# ============================================================================


def export_baseline_params(params: ModelParams, data_dir: str) -> None:
    """Export baseline parameter values."""
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
        ["K", _fmt(params.K)],
        ["sigma_xi", _fmt(params.sigma_xi)],
        ["delta", _fmt(params.delta)],
        ["beta", _fmt(params.beta)],
        ["Delta_tilde", _fmt(params.Delta_tilde)],
    ]
    _write_csv(os.path.join(data_dir, "baseline_params.csv"), ["param", "value"], rows)


def export_cutoff_structure(
    k1: float, k0: float, kD: float,
    params: ModelParams,
    data_dir: str,
) -> None:
    """Export data for Figure 1: Cutoff structure on number line."""
    # Baseline cutoffs
    _write_csv(
        os.path.join(data_dir, "baseline_cutoffs.csv"),
        ["k1", "k0", "kD", "mu", "sigma_s"],
        [[_fmt(k1), _fmt(k0), _fmt(kD), _fmt(params.mu), _fmt(params.sigma_s)]],
    )

    # Cutoff regions
    x_min = params.mu - 3 * params.sigma_s
    x_max = max(params.mu + 4 * params.sigma_s, kD + 0.5 * params.sigma_s)

    tol = TOL_REGION
    has_hold = (k0 - k1) > tol

    regions: List[List[str]] = [["Exit", _fmt(x_min), _fmt(k1)]]
    if has_hold:
        regions.append(["Hold", _fmt(k1), _fmt(k0)])
        quiet_left = k0
    else:
        quiet_left = k1

    regions.append(["Quiet Voice", _fmt(quiet_left), _fmt(kD)])
    regions.append(["Public Voice", _fmt(kD), _fmt(x_max)])

    _write_csv(
        os.path.join(data_dir, "cutoff_regions.csv"),
        ["region", "xmin", "xmax"],
        regions,
    )


def export_baseline_series(
    params: ModelParams,
    data_dir: str,
    n_points: int = 35,
) -> Dict[str, np.ndarray]:
    """Export data for Figures 2, 3, 5: Baseline series over kappa."""
    kappa_values = np.linspace(0.15, 0.85, n_points)
    series = compute_series_over_kappa(params, kappa_values, include_no_disclosure=False)

    rows = []
    for i in range(len(kappa_values)):
        rows.append([
            _fmt(float(series["kappa"][i])),
            _fmt(float(series["k1"][i])),
            _fmt(float(series["k0"][i])),
            _fmt(float(series["kD"][i])),
            _fmt(float(series["Delta_min"][i])),
            _fmt(float(series["base"][i])),
            _fmt(float(series["act"][i])),
        ])

    _write_csv(
        os.path.join(data_dir, "baseline_series.csv"),
        ["kappa", "k1", "k0", "kD", "Delta_min", "base", "act"],
        rows,
    )

    return series


def export_prices(
    k1: float, k0: float, kD: float,
    params: ModelParams,
    data_dir: str,
) -> None:
    """Export data for Figure 4: Equilibrium prices by state."""
    prices = compute_equilibrium_prices(k1, k0, kD, params)
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)

    p0 = 1 - params.kappa
    p1 = params.kappa / 2

    # Compute on-path probabilities
    prob_XD: Dict[Tuple[int, int], float] = {}
    actions = [
        ("E", -1, 0, omega_E),
        ("H", 0, 0, omega_H),
        ("Q", 0, 0, omega_Q),
        ("P", 1, 1, omega_P),
    ]
    for _name, q, D, omega in actions:
        if omega < TOL_PROB:
            continue
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = q + z
            prob_XD[(X, D)] = prob_XD.get((X, D), 0.0) + float(omega) * float(pz)

    rows = []
    # D=0 states
    for X in [-2, -1, 0, 1]:
        on_path = prob_XD.get((X, 0), 0.0) > 1e-4
        P = prices.get((X, 0), float("nan"))
        pi = posteriors.get((X, 0), 0.0)
        m_XD = params.m0 + (params.m_tilde - params.m0) * pi
        p_bid = bid_probability(P, m_XD, params) if np.isfinite(P) else float("nan")
        rows.append([
            str(X), "0", _fmt(P), _fmt(pi), _fmt(p_bid), _fmt(m_XD),
            "TRUE" if on_path else "FALSE",
        ])

    # D=1 states
    for X in [0, 1, 2]:
        on_path = prob_XD.get((X, 1), 0.0) > 1e-4
        P = prices.get((X, 1), float("nan"))
        pi = 1.0  # D=1 => pi=1
        m_XD = params.m_tilde
        p_bid = bid_probability(P, m_XD, params) if np.isfinite(P) else float("nan")
        rows.append([
            str(X), "1", _fmt(P), _fmt(pi), _fmt(p_bid), _fmt(m_XD),
            "TRUE" if on_path else "FALSE",
        ])

    _write_csv(
        os.path.join(data_dir, "prices.csv"),
        ["X", "D", "price", "pi", "p_bid", "m_XD", "on_path"],
        rows,
    )


def export_disclosure_attenuation(
    base_params: ModelParams,
    k1_ref: float, k0_ref: float, kD_ref: float,
    data_dir: str,
    n_points: int = 35,
) -> None:
    """Export data for Figure 6: Disclosure attenuation."""
    kappa_values = np.linspace(0.15, 0.85, n_points)

    rows = []
    for kappa in kappa_values:
        params_k = base_params.replace(kappa=float(kappa))
        _, _, act_k = compute_minority_gains(k1_ref, k0_ref, kD_ref, params_k)
        _, _, act_nd_k = compute_minority_gains_no_disclosure_given_strategy(
            k1_ref, k0_ref, kD_ref, params_k,
        )
        rows.append([_fmt(float(kappa)), _fmt(act_k), _fmt(act_nd_k)])

    _write_csv(
        os.path.join(data_dir, "disclosure_attenuation.csv"),
        ["kappa", "act_disclosure", "act_no_disclosure"],
        rows,
    )


def _export_sensitivity(
    base_params: ModelParams,
    param_name: str,
    param_values: List[float],
    param_field: str,
    data_dir: str,
    csv_name: str,
    n_kappa: int = 21,
    kappa_min: float = 0.25,
    kappa_max: float = 0.85,
    replace_fn=None,
) -> None:
    """Generic sensitivity export: sweep kappa for each parameter value."""
    kappa_values = np.linspace(kappa_min, kappa_max, n_kappa)

    rows = []
    for pval in param_values:
        prev: Optional[Cutoffs] = None
        for kappa in kappa_values:
            try:
                if replace_fn is not None:
                    p = replace_fn(base_params, float(kappa), pval)
                else:
                    p = base_params.replace(kappa=float(kappa), **{param_field: pval})
                cutoffs, res = solve_valid(p, prev)
                if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                    rows.append([_fmt(float(kappa)), _fmt(pval), "NA"])
                    prev = None
                    continue
                prev = cutoffs
                total, _, _ = compute_minority_gains(cutoffs.k1, cutoffs.k0, cutoffs.kD, p)
                rows.append([_fmt(float(kappa)), _fmt(pval), _fmt(total)])
            except Exception:
                rows.append([_fmt(float(kappa)), _fmt(pval), "NA"])

    _write_csv(
        os.path.join(data_dir, csv_name),
        ["kappa", param_name, "Delta_min"],
        rows,
    )


def export_sensitivity_C0(base_params: ModelParams, data_dir: str) -> None:
    """Export data for Figure 7: Sensitivity to engagement cost."""
    _export_sensitivity(
        base_params, "C0", [0.06, 0.12, 0.21, 0.24], "C0",
        data_dir, "sensitivity_C0.csv",
    )


def export_sensitivity_wedge(base_params: ModelParams, data_dir: str) -> None:
    """Export data for Figure 8: Sensitivity to premium wedge."""
    _export_sensitivity(
        base_params, "wedge", [0.10, 0.20, 0.30], "m1",
        data_dir, "sensitivity_wedge.csv",
        replace_fn=lambda bp, k, w: bp.replace(kappa=k, m1=bp.m0 + w),
    )


def export_sensitivity_rho(base_params: ModelParams, data_dir: str) -> None:
    """Export data for Figure 9: Sensitivity to engagement success."""
    _export_sensitivity(
        base_params, "rho", [0.5, 0.7, 0.9], "rho",
        data_dir, "sensitivity_rho.csv",
    )


def export_sensitivity_sigma_xi(base_params: ModelParams, data_dir: str) -> None:
    """Export data for Figure 10: Sensitivity to bidder heterogeneity."""
    _export_sensitivity(
        base_params, "sigma_xi", [0.25, 0.40, 0.60], "sigma_xi",
        data_dir, "sensitivity_sigma_xi.csv",
    )


def export_sensitivity_delta(base_params: ModelParams, data_dir: str) -> None:
    """Export data for Figure 11: Sensitivity to discount factor."""
    _export_sensitivity(
        base_params, "delta", [0.85, 0.90, 0.95], "delta",
        data_dir, "sensitivity_delta.csv",
    )


def export_noisy_rumor(base_params: ModelParams, data_dir: str) -> None:
    """Export data for Figure 12: Noisy rumor precision."""
    kappa_values = np.linspace(0.25, 0.85, 21)
    rumor_configs = [
        (0.50, 0.50, "Uninformative"),
        (0.75, 0.25, "Moderate"),
        (0.95, 0.05, "Precise"),
    ]

    rows = []
    for eta_1, eta_0, label in rumor_configs:
        prev: Optional[Cutoffs] = None
        for kappa in kappa_values:
            try:
                p = base_params.replace(kappa=float(kappa))
                cutoffs, res = solve_valid(p, prev)
                if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                    rows.append([_fmt(float(kappa)), _fmt(eta_1), _fmt(eta_0), label, "NA"])
                    prev = None
                    continue
                prev = cutoffs
                gains = compute_minority_gains_noisy_rumor(
                    cutoffs.k1, cutoffs.k0, cutoffs.kD, p, eta_1, eta_0
                )
                rows.append([
                    _fmt(float(kappa)), _fmt(eta_1), _fmt(eta_0),
                    label, _fmt(gains.total),
                ])
            except Exception:
                rows.append([_fmt(float(kappa)), _fmt(eta_1), _fmt(eta_0), label, "NA"])

    _write_csv(
        os.path.join(data_dir, "noisy_rumor.csv"),
        ["kappa", "eta_1", "eta_0", "label", "Delta_min"],
        rows,
    )


def export_welfare(base_params: ModelParams, data_dir: str) -> None:
    """Export data for Figure 13: Welfare decomposition."""
    kappa_values = np.linspace(0.25, 0.85, 21)

    rows = []
    prev: Optional[Cutoffs] = None
    for kappa in kappa_values:
        try:
            p = base_params.replace(kappa=float(kappa))
            cutoffs, res = solve_valid(p, prev)
            if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                rows.append([_fmt(float(kappa)), "NA", "NA", "NA"])
                prev = None
                continue
            prev = cutoffs
            W_min, W_bid, _, W_tot = compute_welfare(
                cutoffs.k1, cutoffs.k0, cutoffs.kD, p
            )
            rows.append([_fmt(float(kappa)), _fmt(W_min), _fmt(W_bid), _fmt(W_tot)])
        except Exception:
            rows.append([_fmt(float(kappa)), "NA", "NA", "NA"])

    _write_csv(
        os.path.join(data_dir, "welfare.csv"),
        ["kappa", "W_min", "W_bid", "W_tot"],
        rows,
    )


# ============================================================================
# LATEX TABLE FUNCTIONS (preserved from figures.py)
# ============================================================================


def write_baseline_table(
    k1: float, k0: float, kD: float,
    params: ModelParams,
    output_path: str,
) -> None:
    """Write LaTeX table rows for the baseline equilibrium."""
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    prices = compute_equilibrium_prices(k1, k0, kD, params)

    def row_for(X: int, D: int) -> str:
        P = prices.get((X, D), np.nan)
        pi = posteriors.get((X, D), 0.0)
        m_XD = params.m0 + (params.m_tilde - params.m0) * pi
        p_bid = bid_probability(P, m_XD, params) if np.isfinite(P) else np.nan
        return f"{D} & ${X}$ & {P:.2f} & {pi:.2f} & {p_bid:.2f} & {m_XD:.2f} \\\\"

    lines: List[str] = []
    lines.append("\\begin{tabular}{llrrrr}")
    lines.append("\\toprule")
    lines.append(
        "$D$ & Order flow $X$ & $P(X,D)$ & $\\pi(X,D)$ & $p(X,D)$ & $m(X,D)$ \\\\"
    )
    lines.append("\\midrule")
    for X in [-2, -1, 0, 1]:
        lines.append(row_for(X, 0))
    lines.append("\\midrule")
    for X in [0, 1, 2]:
        lines.append(row_for(X, 1))
    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")

    content = "\n".join(lines) + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def write_disclosure_extension_table(
    k1: float, k0: float, kD: float,
    params: ModelParams,
    output_path: str,
    rho1: float = 0.75,
    rho0: float = 0.25,
) -> None:
    """Write LaTeX table for disclosure extensions."""
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)

    post_baseline = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    post_nd = compute_posteriors_no_disclosure(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    post_nr = compute_posteriors_noisy_rumor(
        omega_E, omega_H, omega_Q, omega_P, params.kappa, rho1, rho0,
    )
    post_fi = compute_posteriors_full_information()

    def fmt(x: float) -> str:
        return f"{x:.2f}"

    lines: List[str] = []
    lines.append("\\begin{tabular}{lrrrr}")
    lines.append("\\toprule")
    lines.append(
        "$X$ & $\\pi(X,0)$ & $\\pi_{\\textup{ND}}(X)$"
        " & $\\pi_{\\textup{NR}}(X,0,R=0)$ & $\\pi_{\\textup{NR}}(X,0,R=1)$ \\\\"
    )
    lines.append("\\midrule")
    for X in [-1, 0, 1]:
        pi_base = post_baseline.get((X, 0), 0.0)
        pi_nd = post_nd.get(X, 0.0)
        pi_nr0 = post_nr.get((X, 0, 0), 0.0)
        pi_nr1 = post_nr.get((X, 0, 1), 0.0)
        lines.append(
            f"${X}$ & {fmt(pi_base)} & {fmt(pi_nd)} & {fmt(pi_nr0)} & {fmt(pi_nr1)} \\\\"
        )
    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append("\\vspace{0.6em}")
    lines.append("\\begin{tabular}{ll}")
    lines.append("\\toprule")
    lines.append("$(q,a)$ & $\\pi_{\\textup{FI}}$ \\\\")
    lines.append("\\midrule")
    for key in [(-1, 0), (0, 0), (0, 1), (1, 1)]:
        lines.append(f"$({key[0]},{key[1]})$ & {fmt(post_fi.get(key, 0.0))} \\\\")
    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")

    content = "\n".join(lines) + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


# ============================================================================
# ORCHESTRATOR
# ============================================================================


def export_all(output_dir: str = "numerical_output") -> None:
    """Export all CSV data and LaTeX tables for the manuscript."""
    data_dir = os.path.join(output_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    params = ModelParams()

    print("Solving baseline equilibrium...")
    k1, k0, kD = solve_equilibrium(params)
    print(f"Equilibrium cutoffs: k1={k1:.3f}, k0={k0:.3f}, kD={kD:.3f}")

    # Export baseline parameters
    print("Exporting baseline parameters...")
    export_baseline_params(params, data_dir)

    # Figure 1: cutoff structure
    print("Exporting Figure 1 data: Cutoff Structure...")
    export_cutoff_structure(k1, k0, kD, params, data_dir)

    # Figures 2, 3, 5: baseline series
    print("Exporting Figures 2/3/5 data: Baseline Series...")
    export_baseline_series(params, data_dir)

    # Figure 4: prices
    print("Exporting Figure 4 data: Prices...")
    export_prices(k1, k0, kD, params, data_dir)

    # Figure 6: disclosure attenuation
    print("Exporting Figure 6 data: Disclosure Attenuation...")
    export_disclosure_attenuation(params, k1, k0, kD, data_dir)

    # Figures 7-11: sensitivity analyses
    print("Exporting Figure 7 data: Sensitivity C0...")
    export_sensitivity_C0(params, data_dir)

    print("Exporting Figure 8 data: Sensitivity Premium Wedge...")
    export_sensitivity_wedge(params, data_dir)

    print("Exporting Figure 9 data: Sensitivity Rho...")
    export_sensitivity_rho(params, data_dir)

    print("Exporting Figure 10 data: Sensitivity Sigma Xi...")
    export_sensitivity_sigma_xi(params, data_dir)

    print("Exporting Figure 11 data: Sensitivity Delta...")
    export_sensitivity_delta(params, data_dir)

    # Figure 12: noisy rumor
    print("Exporting Figure 12 data: Noisy Rumor...")
    export_noisy_rumor(params, data_dir)

    # Figure 13: welfare
    print("Exporting Figure 13 data: Welfare...")
    export_welfare(params, data_dir)

    # LaTeX tables
    print("Writing LaTeX tables...")
    write_baseline_table(k1, k0, kD, params, os.path.join(output_dir, "table_example.tex"))
    write_disclosure_extension_table(
        k1, k0, kD, params, os.path.join(output_dir, "table_disclosure_extensions.tex")
    )

    print(f"\nAll data exported to: {data_dir}/")
    print(f"LaTeX tables written to: {output_dir}/")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Export model data to CSV")
    parser.add_argument(
        "--output-dir", default="numerical_output",
        help="Output directory (default: numerical_output)",
    )
    args = parser.parse_args()

    export_all(output_dir=args.output_dir)
