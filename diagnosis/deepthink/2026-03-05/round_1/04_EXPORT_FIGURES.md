# Export Pipeline and Figures

## evt_codebase/numerical/export_data.py

```python
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
    kappa_values = np.linspace(0.15, 0.85, n_points)
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
    kappa_values = np.linspace(0.15, 0.85, n_points)
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
        # ρ is "success conditional on engagement", so we focus on a high-success range.
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
```

## evt_codebase/numerical/figures.py

```python
"""Generate all figures from exported CSVs.

Run:

    python -m numerical.figures --output-dir numerical_output

This reads `numerical_output/data/*.csv` and writes 13 PDF figures to
`numerical_output/`.
"""

from __future__ import annotations

import os
from typing import Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns

from .theme import ACTION_COLORS, SENSITIVITY_COLORS, save_figure, setup_theme


def _read_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, na_values=["NA"])


def fig_cutoff_structure(output_dir: str, data_dir: str) -> None:
    regions = _read_csv(os.path.join(data_dir, "cutoff_regions.csv"))
    cutoffs = _read_csv(os.path.join(data_dir, "baseline_cutoffs.csv")).iloc[0]

    k1, k0, kD = float(cutoffs["k1"]), float(cutoffs["k0"]), float(cutoffs["kD"])

    x_min = float(regions["xmin"].min())
    x_max = float(regions["xmax"].max())

    fig, ax = plt.subplots()

    y0, h = 0.45, 0.20
    for _, row in regions.iterrows():
        name = str(row["region"])
        xmin = float(row["xmin"])
        xmax = float(row["xmax"])
        color = ACTION_COLORS.get(name, "#999999")
        ax.add_patch(patches.Rectangle((xmin, y0), xmax - xmin, h, facecolor=color, edgecolor="none", alpha=0.9))

    # Cutoff markers
    for x, label in [(k1, r"$k_1$"), (k0, r"$k_0$"), (kD, r"$k_D$")]:
        ax.axvline(x, linestyle="--", linewidth=1)
        ax.text(x, y0 + h + 0.05, label, ha="center", va="bottom")

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0.0, 1.0)
    ax.set_yticks([])
    ax.set_xlabel(r"Signal $s$")
    ax.set_title("Equilibrium cutoff structure")

    # Legend
    handles = [patches.Patch(color=ACTION_COLORS[n], label=n) for n in ["Exit", "Hold", "Quiet Voice", "Public Voice"] if n in ACTION_COLORS]
    ax.legend(handles=handles, loc="upper left", frameon=False, ncol=2)

    save_figure(fig, os.path.join(output_dir, "fig_cutoff_structure.pdf"), width=6, height=4)


def fig_nonmonotone(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "baseline_series.csv"))
    df = df.dropna(subset=["kappa", "delta_min"])

    kappa = df["kappa"].values
    delta = df["delta_min"].values
    idx = int(np.nanargmax(delta))
    k_star = float(kappa[idx])
    d_star = float(delta[idx])

    fig, ax = plt.subplots()
    ax.plot(kappa, delta, linewidth=2)
    ax.scatter([k_star], [d_star], s=45, zorder=3)
    ax.axvline(k_star, linestyle="--", linewidth=1)
    ax.text(k_star, d_star, r"  $\kappa^{\dagger}$", va="bottom")

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"Minority gains $\Delta^{\min}(\kappa)$")
    ax.set_title(r"Nonmonotone $\Delta^{\min}(\kappa)$")

    save_figure(fig, os.path.join(output_dir, "fig_nonmonotone.pdf"), width=6, height=4)


def fig_decomposition(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "baseline_series.csv"))
    df = df.dropna(subset=["kappa", "delta_min", "base", "act"])

    # Mark κ†: maximizer of Δ^min on the plotted grid (same definition as fig_nonmonotone).
    idx = int(np.nanargmax(df["delta_min"].values))
    k_dag = float(df["kappa"].iloc[idx])

    fig, ax = plt.subplots()
    ax.plot(df["kappa"], df["delta_min"], linewidth=2, label=r"Total $\Delta^{\min}$")
    ax.plot(df["kappa"], df["base"], linewidth=2, linestyle="--", label=r"Baseline $\Delta^{\mathrm{base}}$")
    ax.plot(df["kappa"], df["act"], linewidth=2, linestyle=":", label=r"Activism $\Delta^{\mathrm{act}}$")

    ax.axvline(k_dag, linestyle="--", linewidth=1)

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"Premium components")
    ax.set_title("Minority gains decomposition")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_decomposition.pdf"), width=6, height=4)


def fig_prices(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "prices.csv"))
    df["X"] = df["X"].astype(int)
    df["D"] = df["D"].astype(int)
    if "on_path" in df.columns:
        df = df[df["on_path"] == True]  # noqa: E712 (explicit comparison is fine for pandas)

    fig, axes = plt.subplots(1, 2)

    for ax, D in zip(axes, [0, 1]):
        sub = df[df["D"] == D].sort_values("X")
        ax.bar(sub["X"].astype(str), sub["P_post"], alpha=0.9, label=r"$P_{post}(X,D)$")
        # Overlay execution price as marker (same across D given X)
        ax.scatter(sub["X"].astype(str), sub["P_trade"], marker="D", s=28, zorder=3, label=r"$P_{trade}(X)$")

        # Annotate posterior engagement probability above the bars (matches appendix caption).
        for xlab, p_post, pi in zip(sub["X"].astype(str), sub["P_post"], sub["pi"]):
            if pd.isna(p_post) or pd.isna(pi):
                continue
            ax.text(xlab, float(p_post), f"{float(pi):.2f}", ha="center", va="bottom", fontsize=9)

        ax.set_title(f"D = {D}")
        ax.set_xlabel("Order flow X")
        ax.set_ylabel(r"Price")
        ax.grid(True, axis="y")

    # One shared legend is enough.
    axes[0].legend(frameon=False)
    fig.suptitle("Post-disclosure prices and execution prices")

    save_figure(fig, os.path.join(output_dir, "fig_prices.pdf"), width=10, height=4)


def fig_cutoffs_kappa(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "baseline_series.csv"))
    df = df.dropna(subset=["kappa", "k1", "k0", "kD"])

    # Prior mean μ (used as reference line in the appendix caption).
    mu = float(_read_csv(os.path.join(data_dir, "baseline_cutoffs.csv")).iloc[0]["mu"])

    fig, ax = plt.subplots()
    ax.plot(df["kappa"], df["k1"], linewidth=2, label=r"$k_1$")
    ax.plot(df["kappa"], df["k0"], linewidth=2, label=r"$k_0$")
    ax.plot(df["kappa"], df["kD"], linewidth=2, label=r"$k_D$")
    ax.axhline(mu, linestyle="--", linewidth=1)

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel("Cutoff")
    ax.set_title("Equilibrium cutoffs across liquidity")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_cutoffs_kappa.pdf"), width=6, height=4)


def fig_disclosure(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "disclosure_attenuation.csv"))
    df = df.dropna(subset=["kappa", "act_disclosure", "act_no_disclosure"])

    fig, ax = plt.subplots()
    ax.plot(df["kappa"], df["act_disclosure"], linewidth=2, label="Threshold disclosure")
    ax.plot(df["kappa"], df["act_no_disclosure"], linewidth=2, linestyle="--", label="No disclosure")

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"Activism component $\Delta^{\mathrm{act}}(\kappa)$")
    ax.set_title("Disclosure attenuates inference-driven sensitivity")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_disclosure.pdf"), width=6, height=4)


def _fig_sensitivity_generic(output_dir: str, data_dir: str, csv_name: str, hue: str, title: str, out_name: str) -> None:
    df = _read_csv(os.path.join(data_dir, csv_name))
    df = df.dropna(subset=["kappa", hue, "delta_min"])

    fig, ax = plt.subplots()

    # Ensure deterministic hue order
    hue_order = sorted(df[hue].unique())

    palette = {val: SENSITIVITY_COLORS[i % len(SENSITIVITY_COLORS)] for i, val in enumerate(hue_order)}

    for val in hue_order:
        sub = df[df[hue] == val]
        ax.plot(sub["kappa"], sub["delta_min"], linewidth=2, label=f"{hue}={val:g}", color=palette[val])

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"$\Delta^{\min}(\kappa)$")
    ax.set_title(title)
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, out_name), width=6, height=4)


def fig_sensitivity_C0(output_dir: str, data_dir: str) -> None:
    _fig_sensitivity_generic(
        output_dir,
        data_dir,
        csv_name="sensitivity_C0.csv",
        hue="C0",
        title=r"Sensitivity: engagement cost scale $C_0$",
        out_name="fig_sensitivity_C0.pdf",
    )


def fig_sensitivity_wedge(output_dir: str, data_dir: str) -> None:
    _fig_sensitivity_generic(
        output_dir,
        data_dir,
        csv_name="sensitivity_wedge.csv",
        hue="wedge",
        title=r"Sensitivity: premium wedge $(m_1-m_0)$",
        out_name="fig_sensitivity_wedge.pdf",
    )


def fig_sensitivity_rho(output_dir: str, data_dir: str) -> None:
    _fig_sensitivity_generic(
        output_dir,
        data_dir,
        csv_name="sensitivity_rho.csv",
        hue="rho",
        title=r"Sensitivity: engagement success probability $\rho$",
        out_name="fig_sensitivity_rho.pdf",
    )


def fig_sensitivity_sigma_xi(output_dir: str, data_dir: str) -> None:
    _fig_sensitivity_generic(
        output_dir,
        data_dir,
        csv_name="sensitivity_sigma_xi.csv",
        hue="s_xi",
        title=r"Sensitivity: bidder shock dispersion $s_{\xi}$",
        out_name="fig_sensitivity_sigma_xi.pdf",
    )


def fig_sensitivity_delta(output_dir: str, data_dir: str) -> None:
    _fig_sensitivity_generic(
        output_dir,
        data_dir,
        csv_name="sensitivity_delta.csv",
        hue="delta",
        title=r"Sensitivity: discount factor $\delta$",
        out_name="fig_sensitivity_delta.pdf",
    )


def fig_noisy_rumor_precision(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "noisy_rumor.csv"))
    df = df.dropna(subset=["kappa", "label", "delta_min"])

    fig, ax = plt.subplots()
    labels = ["Uninformative", "Moderate", "Precise"]
    palette = {
        "Uninformative": SENSITIVITY_COLORS[0],
        "Moderate": SENSITIVITY_COLORS[1],
        "Precise": SENSITIVITY_COLORS[2],
    }

    for lab in labels:
        sub = df[df["label"] == lab]
        if sub.empty:
            continue
        ax.plot(sub["kappa"], sub["delta_min"], linewidth=2, label=lab, color=palette.get(lab, None))

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"$\Delta^{\min}(\kappa)$")
    ax.set_title("Noisy rumor precision flattens the liquidity sensitivity")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_noisy_rumor_precision.pdf"), width=6, height=4)


def fig_welfare(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "welfare.csv"))
    df = df.dropna(subset=["kappa", "W_min", "W_bid", "W_tot"])

    kappa = df["kappa"].values

    idx_min = int(np.nanargmax(df["W_min"].values))
    idx_tot = int(np.nanargmax(df["W_tot"].values))
    k_dag = float(kappa[idx_min])
    k_star = float(kappa[idx_tot])

    fig, ax = plt.subplots()
    ax.plot(df["kappa"], df["W_min"], linewidth=2, label=r"$W_{min}=\Delta^{\min}$")
    ax.plot(df["kappa"], df["W_bid"], linewidth=2, linestyle="--", label=r"$W_{bid}$")
    ax.plot(df["kappa"], df["W_tot"], linewidth=2, linestyle=":", label=r"$W_{tot}$")

    ax.axvline(k_dag, linestyle="--", linewidth=1)
    ax.axvline(k_star, linestyle="-.", linewidth=1)
    ax.text(k_dag, df["W_min"].iloc[idx_min], r"  $\kappa^{\dagger}$", va="bottom")
    ax.text(k_star, df["W_tot"].iloc[idx_tot], r"  $\kappa^{*}$", va="bottom")

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel("Welfare")
    ax.set_title("Welfare decomposition")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_welfare.pdf"), width=6, height=4)


def make_all(output_dir: str) -> None:
    data_dir = os.path.join(output_dir, "data")
    os.makedirs(output_dir, exist_ok=True)

    setup_theme()

    fig_cutoff_structure(output_dir, data_dir)
    fig_nonmonotone(output_dir, data_dir)
    fig_decomposition(output_dir, data_dir)
    fig_prices(output_dir, data_dir)
    fig_cutoffs_kappa(output_dir, data_dir)
    fig_disclosure(output_dir, data_dir)

    fig_sensitivity_C0(output_dir, data_dir)
    fig_sensitivity_wedge(output_dir, data_dir)
    fig_sensitivity_rho(output_dir, data_dir)
    fig_sensitivity_sigma_xi(output_dir, data_dir)
    fig_sensitivity_delta(output_dir, data_dir)

    fig_noisy_rumor_precision(output_dir, data_dir)
    fig_welfare(output_dir, data_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate PDF figures from exported CSVs")
    parser.add_argument("--output-dir", default="numerical_output", help="Output directory")
    args = parser.parse_args()

    make_all(output_dir=args.output_dir)
```

## evt_codebase/numerical/theme.py

```python
"""Plotting theme (Paul Tol palette + publication defaults).

The goal is clean, journal-ready vector PDFs without chartjunk.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# Paul Tol (muted) inspired colors used in the paper draft.
ACTION_COLORS: Dict[str, str] = {
    "Exit": "#cc6677",
    "Hold": "#ddcc77",
    "Quiet Voice": "#88ccee",
    "Public Voice": "#44aa99",
}

SENSITIVITY_COLORS: List[str] = [
    "#4477aa",
    "#ee6677",
    "#228833",
    "#ccbb44",
]


def setup_theme() -> None:
    """Apply global matplotlib/seaborn styling."""

    sns.set_theme(context="paper", style="whitegrid")

    mpl.rcParams.update({
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "font.size": 11,
        "axes.titlesize": 11,
        "axes.labelsize": 11,
        "legend.fontsize": 10,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "grid.alpha": 0.25,
        "pdf.fonttype": 42,      # TrueType fonts
        "ps.fonttype": 42,
    })


def save_figure(fig: plt.Figure, path: str, width: float, height: float) -> None:
    """Save a figure as vector PDF with consistent sizing."""
    fig.set_size_inches(width, height)
    fig.tight_layout()
    fig.savefig(path, format="pdf", bbox_inches="tight")
    plt.close(fig)
```

## evt_codebase/numerical/__init__.py

```python
"""Numerical package for "Liquidity, Activism Disclosure, and Takeover Premia".

The public surface area is intentionally small. Most users should run:

    python -m numerical.export_data --output-dir numerical_output
    python -m numerical.figures     --output-dir numerical_output

or simply:

    make clean && make all
"""

from .params import ModelParams, Cutoffs, MinorityGains, Action
from .solver import solve_valid, solve_equilibrium
from .model import compute_minority_gains

__all__ = [
    "ModelParams",
    "Cutoffs",
    "MinorityGains",
    "Action",
    "solve_valid",
    "solve_equilibrium",
    "compute_minority_gains",
]
```
