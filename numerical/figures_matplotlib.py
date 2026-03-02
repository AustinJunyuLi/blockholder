"""
Figure generation for the Exit-Voice-Takeover model.

All figures use a muted Seaborn-style colour palette (Paul Tol's
colourblind-friendly scheme) with line style + marker shape as secondary
differentiation channels.  Output format is PDF vector graphics.
"""

from __future__ import annotations

import os
from typing import Dict, List, Optional, Tuple

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from numerical.params import (
    Action,
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
# STYLE CONFIGURATION
# ============================================================================


def configure_matplotlib() -> None:
    """Set rcParams for publication-quality muted-palette figures."""
    params: dict = {
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 11,
        "axes.labelsize": 12,
        "axes.titlesize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.figsize": (5.5, 3.8),
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "lines.linewidth": 1.5,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.15,
    }
    plt.rcParams.update(params)


# -- Consistent series styles ------------------------------------------------

STYLES: Dict[str, dict] = {
    "Exit":         {"color": "#cc6677", "linestyle": "-",  "marker": "o", "markersize": 4},  # muted rose
    "Hold":         {"color": "#ddcc77", "linestyle": "--", "marker": "s", "markersize": 4},  # muted sand
    "Quiet Voice":  {"color": "#88ccee", "linestyle": "-.", "marker": "^", "markersize": 4},  # muted cyan
    "Public Voice": {"color": "#44aa99", "linestyle": ":",  "marker": "D", "markersize": 4},  # muted teal
}

HATCHES: Dict[str, str] = {
    "Exit":         "",
    "Hold":         "",
    "Quiet Voice":  "",
    "Public Voice": "",
}

FILLS: Dict[str, str] = {
    "Exit":         "#cc6677",   # muted rose
    "Hold":         "#ddcc77",   # muted sand
    "Quiet Voice":  "#88ccee",   # muted cyan
    "Public Voice": "#44aa99",   # muted teal
}

# Sensitivity analysis gets its own colourblind-friendly rotation.
SENSITIVITY_STYLES: List[dict] = [
    {"color": "#4477aa", "linestyle": "-",  "marker": "o", "markersize": 4},  # blue
    {"color": "#ee6677", "linestyle": "--", "marker": "s", "markersize": 4},  # red
    {"color": "#228833", "linestyle": "-.", "marker": "^", "markersize": 4},  # green
    {"color": "#ccbb44", "linestyle": ":",  "marker": "D", "markersize": 4},  # yellow
]

# Apply style settings at import time.
configure_matplotlib()


# ============================================================================
# FIGURE FUNCTIONS
# ============================================================================


def plot_cutoff_structure(
    k1: float, k0: float, kD: float,
    params: ModelParams,
    save_path: Optional[str] = None,
) -> None:
    """Figure 1: Equilibrium cutoff structure on number line."""
    fig, ax = plt.subplots(figsize=(8, 2.5))

    # Define range
    x_min = params.mu - 3 * params.sigma_s
    x_max = max(params.mu + 4 * params.sigma_s, kD + 0.5 * params.sigma_s)

    tol = TOL_REGION
    has_hold = (k0 - k1) > tol
    hold_label = "$k_0$" if has_hold else "$k_1{=}k_0$"

    # Draw regions
    regions: List[Tuple[float, float, str]] = [(x_min, k1, "Exit")]
    if has_hold:
        regions.append((k1, k0, "Hold"))
        quiet_left = k0
    else:
        quiet_left = k1

    regions.append((quiet_left, kD, "Quiet Voice"))
    regions.append((kD, x_max, "Public Voice"))

    y_height = 0.4
    for left, right, name in regions:
        if right <= left:
            continue
        ax.add_patch(mpatches.FancyBboxPatch(
            (left, -y_height / 2), right - left, y_height,
            boxstyle="square,pad=0",
            facecolor=FILLS.get(name, "#cccccc"),
            edgecolor="none",
            hatch=HATCHES.get(name, ""),
            alpha=0.7,
        ))
        # Label (skip if region is too narrow; legend carries names)
        if (right - left) >= 0.8:
            mid = (left + right) / 2
            ax.text(
                mid, 0, name, ha="center", va="center", fontsize=9,
                fontweight="bold",
                bbox=dict(
                    boxstyle="round,pad=0.15",
                    facecolor="white",
                    edgecolor="none",
                    alpha=0.85,
                ),
            )

    # Mark cutoffs (draw below the colored bar to avoid label clutter)
    cutoffs_labels = [(k1, "$k_1$"), (k0, hold_label), (kD, "$k_D$")]
    cut_y = -0.32
    ax.axhline(y=cut_y, color="black", linewidth=1.0, alpha=0.8)

    stagger_y = [cut_y - 0.08, cut_y - 0.16]
    sorted_cutoffs = sorted(cutoffs_labels, key=lambda t: t[0])
    min_sep = 0.10
    last_k: Optional[float] = None
    for idx, (k, label) in enumerate(sorted_cutoffs):
        x_off = 0.0
        if last_k is not None and abs(k - last_k) < min_sep:
            x_off = 0.05 if (idx % 2 == 0) else -0.05
        ax.axvline(
            x=k, color="black", linewidth=1.2, linestyle="--",
            ymin=0.18, ymax=0.82, alpha=0.9,
        )
        ax.plot(k, cut_y, "ko", markersize=5, zorder=5)
        ax.text(
            k + x_off, stagger_y[idx % 2], label,
            ha="center", va="top", fontsize=11,
        )
        last_k = k

    # Mark mu
    ax.axvline(
        x=params.mu, color="gray", linewidth=1, linestyle=":",
        ymin=0.2, ymax=0.8,
    )
    ax.text(
        params.mu, 0.35, "$\\mu$", ha="center", va="bottom",
        fontsize=11, color="gray",
    )

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-0.6, 0.5)
    ax.set_xlabel("Signal $s$", fontsize=12)
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Legend (only show regions that appear on the main axis)
    legend_order = ["Exit", "Hold", "Quiet Voice", "Public Voice"]
    present = {name for _, _, name in regions}
    handles = [
        mpatches.Patch(
            facecolor=FILLS.get(name, "#cccccc"),
            hatch=HATCHES.get(name, ""),
            alpha=0.7,
            label=name,
        )
        for name in legend_order
        if name in present
    ]
    ax.legend(
        handles=handles, loc="upper center", bbox_to_anchor=(0.5, 1.25),
        ncol=4, frameon=False, fontsize=9,
    )

    # If k1 and k0 are very close, add a zoom inset to make the Hold region visible.
    try:
        from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
        if (k0 - k1) > tol and abs(k0 - k1) < 0.15:
            pad = max(0.08, 8 * abs(k0 - k1))
            x1, x2 = k1 - pad, k0 + pad
            axins = inset_axes(ax, width="33%", height="55%", loc="lower left", borderpad=1.0)
            for left, right, name in regions:
                axins.add_patch(mpatches.FancyBboxPatch(
                    (left, -y_height / 2), right - left, y_height,
                    boxstyle="square,pad=0",
                    facecolor=FILLS.get(name, "#cccccc"),
                    edgecolor="none",
                    hatch=HATCHES.get(name, ""),
                    alpha=0.7,
                ))
            for k, _label in [(k1, "$k_1$"), (k0, "$k_0$")]:
                axins.axvline(x=k, color="black", linewidth=1.0, linestyle="--", alpha=0.9)
            axins.set_xlim(x1, x2)
            axins.set_ylim(-0.25, 0.25)
            axins.set_xticks([])
            axins.set_yticks([])
            for spine in axins.spines.values():
                spine.set_alpha(0.6)
            mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.4", lw=0.8, alpha=0.8)
    except Exception:
        pass

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_nonmonotonicity(
    base_params: ModelParams,
    save_path: Optional[str] = None,
    series: Optional[Dict[str, np.ndarray]] = None,
) -> Tuple[np.ndarray, list]:
    """Figure 2: Non-monotonicity in liquidity (main result)."""
    if series is None:
        kappa_values = np.linspace(0.15, 0.85, 35)
        series = compute_series_over_kappa(base_params, kappa_values, include_no_disclosure=False)

    kappa_values = series["kappa"]
    Delta_min_values = series["Delta_min"]

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    # Single line: blue, no marker (main result)
    ax.plot(
        kappa_values, Delta_min_values,
        color="#4477aa", linestyle="-", linewidth=2,
        label="$\\Delta^{\\mathrm{min}}(\\kappa)$",
    )

    # Mark interior peak (turning point)
    Delta_arr = np.array(Delta_min_values, dtype=float)
    if np.any(~np.isnan(Delta_arr)):
        peak_idx = int(np.nanargmax(Delta_arr))
        kappa_peak = float(kappa_values[peak_idx])
        ax.axvline(
            x=kappa_peak, color="gray", linestyle="--", linewidth=1.0, alpha=0.7,
        )
        ax.text(
            kappa_peak + 0.015, float(np.nanmax(Delta_arr)) * 0.98,
            "$\\kappa^{\\dagger}$", fontsize=11, color="gray",
        )

    ax.set_xlabel("Liquidity $\\kappa$")
    ax.set_ylabel("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$")
    ax.set_title("Non-Monotonic Effect of Liquidity on Takeover Gains")
    ax.legend(loc="best", frameon=True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()

    return kappa_values, Delta_min_values


def plot_decomposition(
    base_params: ModelParams,
    save_path: Optional[str] = None,
    series: Optional[Dict[str, np.ndarray]] = None,
) -> None:
    """Figure 3: Decomposition of minority gains."""
    if series is None:
        kappa_values = np.linspace(0.15, 0.85, 35)
        series = compute_series_over_kappa(base_params, kappa_values, include_no_disclosure=False)

    kappa_values = series["kappa"]
    base_arr = np.array(series["base"], dtype=float)
    activism_arr = np.array(series["act"], dtype=float)

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    # Base component: muted cyan fill
    ax.fill_between(
        kappa_values,
        0,
        base_arr,
        facecolor="#88ccee",
        alpha=0.5,
        label="Base: $m_0 \\cdot \\mathbb{P}(\\mathrm{bid})$",
    )
    # Activism component: muted rose fill
    ax.fill_between(
        kappa_values,
        base_arr,
        base_arr + activism_arr,
        facecolor="#cc6677",
        alpha=0.5,
        label="Activism: $\\Delta^{\\mathrm{act}}(\\kappa)$",
    )
    # Total line on top: solid black
    ax.plot(
        kappa_values, base_arr + activism_arr,
        "k-", linewidth=1.5, label="Total $\\Delta^{\\mathrm{min}}$",
    )

    total_arr = base_arr + activism_arr
    if np.any(~np.isnan(total_arr)):
        peak_idx = int(np.nanargmax(total_arr))
        kappa_peak = float(kappa_values[peak_idx])
        ax.axvline(
            x=kappa_peak, color="gray", linestyle="--", linewidth=1.0, alpha=0.7,
        )
        ax.text(
            kappa_peak + 0.015, float(np.nanmax(total_arr)) * 0.98,
            "$\\kappa^{\\dagger}$", fontsize=11, color="gray",
        )

    ax.set_xlabel("Liquidity $\\kappa$")
    ax.set_ylabel("Expected Minority Takeover Gains")
    ax.set_title("Decomposition of Minority Takeover Gains")
    ax.legend(loc="best", frameon=True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_prices(
    k1: float, k0: float, kD: float,
    params: ModelParams,
    save_path: Optional[str] = None,
) -> None:
    """Figure 4: Equilibrium prices by state."""
    prices = compute_equilibrium_prices(k1, k0, kD, params)
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Compute on-path probabilities for each (X,D) to avoid displaying infeasible states.
    p0 = 1 - params.kappa
    p1 = params.kappa / 2
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

    # D=0 states
    X_D0 = [X for X in [-2, -1, 0, 1] if prob_XD.get((X, 0), 0.0) > 1e-4]
    P_D0 = [prices.get((X, 0), np.nan) for X in X_D0]
    pi_D0 = [posteriors.get((X, 0), 0) for X in X_D0]

    x_pos = np.arange(len(X_D0))
    ax1.bar(
        x_pos, P_D0,
        color="#88ccee", edgecolor="black", alpha=0.7,
    )
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels([f"$X={x}$" for x in X_D0])
    ax1.set_ylabel("Price $P(X, D=0)$", fontsize=11)
    ax1.set_title("Non-Disclosed States ($D=0$)", fontsize=11)

    # Add pi values as text
    for i, (p, pi) in enumerate(zip(P_D0, pi_D0)):
        if not np.isnan(p):
            ax1.text(i, p + 0.02, f"$\\pi$={pi:.2f}", ha="center", fontsize=9)

    # D=1 states (always show; probability mass can be tiny under some calibrations)
    X_D1 = [0, 1, 2]
    P_D1 = [prices.get((X, 1), np.nan) for X in X_D1]

    x_pos2 = np.arange(len(X_D1))
    ax2.bar(
        x_pos2, P_D1,
        color="#cc6677", edgecolor="black", alpha=0.7,
    )
    ax2.set_xticks(x_pos2)
    ax2.set_xticklabels([f"$X={x}$" for x in X_D1])
    ax2.set_ylabel("Price $P(X, D=1)$", fontsize=11)
    ax2.set_title("Disclosed States ($D=1$)", fontsize=11)

    # Add pi=1 as text
    for i, p in enumerate(P_D1):
        if not np.isnan(p):
            ax2.text(i, p + 0.02, "$\\pi$=1.00", ha="center", fontsize=9)

    # Match y-axis limits
    all_P = [p for p in P_D0 + P_D1 if not np.isnan(p)]
    if all_P:
        y_max = max(all_P) * 1.15
        ax1.set_ylim(0, y_max)
        ax2.set_ylim(0, y_max)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_cutoffs_vs_kappa(
    base_params: ModelParams,
    save_path: Optional[str] = None,
    series: Optional[Dict[str, np.ndarray]] = None,
) -> None:
    """Figure 5: Cutoffs as functions of liquidity."""
    if series is None:
        kappa_values = np.linspace(0.15, 0.85, 35)
        series = compute_series_over_kappa(base_params, kappa_values, include_no_disclosure=False)

    kappa_values = series["kappa"]
    k1_vals = series["k1"]
    k0_vals = series["k0"]
    kD_vals = series["kD"]

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    tol = 1e-3
    k0_equals_k1 = np.nanmax(np.abs(k0_vals - k1_vals)) < tol

    # Use STYLES dict entries for distinct linestyle + marker
    style_k1 = STYLES["Exit"]
    style_k0 = STYLES["Hold"]
    style_kD = STYLES["Quiet Voice"]

    if k0_equals_k1:
        ax.plot(
            kappa_values, k1_vals, linewidth=2.2,
            label="$k_1{=}k_0$ (Exit/Quiet)",
            **style_k1,
        )
    else:
        ax.plot(
            kappa_values, k1_vals, linewidth=2.2,
            label="$k_1$ (Exit/Hold)",
            **style_k1,
        )
        ax.plot(
            kappa_values, k0_vals, linewidth=2.2,
            label="$k_0$ (Hold/Quiet)",
            **style_k0,
        )

    ax.plot(
        kappa_values, kD_vals, linewidth=2.2,
        label="$k_D$ (Quiet/Public)",
        **style_kD,
    )

    # mu reference line: thin gray dotted
    ax.axhline(y=base_params.mu, color="gray", linestyle=":", linewidth=1, label="$\\mu$")

    ax.set_xlabel("Liquidity $\\kappa$")
    ax.set_ylabel("Signal Cutoff")
    ax.set_title("Equilibrium Cutoffs vs.\\ Liquidity")
    ax.legend(loc="best", frameon=True)

    # Tighten y-limits to the relevant cutoffs.
    plotted = [k1_vals, kD_vals]
    if not k0_equals_k1:
        plotted.append(k0_vals)
    y_vals = np.concatenate([np.asarray(x)[np.isfinite(x)] for x in plotted if x is not None])
    if len(y_vals) > 0:
        y_min_v = float(np.min(y_vals))
        y_max_v = float(np.max(y_vals))
        pad = 0.08 * (y_max_v - y_min_v + 1e-6)
        ax.set_ylim(y_min_v - pad, y_max_v + pad)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_disclosure_attenuation(
    base_params: ModelParams,
    save_path: Optional[str] = None,
    kappa_values: Optional[np.ndarray] = None,
    kappa_ref: Optional[float] = None,
    cutoffs_ref: Optional[Tuple[float, float, float]] = None,
) -> None:
    """Figure 6: Disclosure attenuation through the inference channel.

    Partial equilibrium in kappa: hold fixed the blockholder's cutoff strategy
    and vary kappa only through the order-flow noise distribution (hence
    inference/prices).

    The baseline curve plots Delta^act(kappa) under threshold disclosure.
    The counterfactual curve plots the no-disclosure case with the same fixed
    cutoffs.
    """
    if kappa_values is None:
        kappa_values = np.linspace(0.15, 0.85, 35)
    kappa_values = np.asarray(kappa_values, dtype=float)

    if kappa_ref is None:
        kappa_ref = float(base_params.kappa)

    if cutoffs_ref is None:
        params_ref = base_params.replace(kappa=float(kappa_ref))
        k1_ref, k0_ref, kD_ref = solve_equilibrium(params_ref)
    else:
        k1_ref, k0_ref, kD_ref = cutoffs_ref

    act_disclosure: List[float] = []
    act_no_disclosure: List[float] = []
    for kappa in kappa_values:
        params_k = base_params.replace(kappa=float(kappa))
        _, _, act_k = compute_minority_gains(k1_ref, k0_ref, kD_ref, params_k)
        _, _, act_nd_k = compute_minority_gains_no_disclosure_given_strategy(
            k1_ref, k0_ref, kD_ref, params_k,
        )
        act_disclosure.append(act_k)
        act_no_disclosure.append(act_nd_k)

    Delta_act_disclosure = np.asarray(act_disclosure, dtype=float)
    Delta_act_no_disclosure = np.asarray(act_no_disclosure, dtype=float)

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    # Baseline: blue solid line with circle markers
    ax.plot(
        kappa_values, Delta_act_disclosure,
        color="#4477aa", linewidth=2.2, linestyle="-", marker="o", markersize=3,
        label="Threshold disclosure (baseline)",
    )
    # No-disclosure counterfactual: red dashed line with square markers
    ax.plot(
        kappa_values, Delta_act_no_disclosure,
        color="#ee6677", linewidth=2.2, linestyle="--", marker="s", markersize=3,
        label="No disclosure (counterfactual)",
    )

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"Activism-Driven Minority Gains $\Delta^{\mathrm{act}}$")
    ax.set_title("Disclosure Attenuation of Liquidity Sensitivity")
    ax.legend(loc="best", frameon=True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_sensitivity_C0(
    base_params: ModelParams,
    save_path: Optional[str] = None,
) -> None:
    """Figure 7: Sensitivity analysis -- Engagement cost."""
    kappa_values = np.linspace(0.25, 0.85, 21)
    C0_values = [0.06, 0.12, 0.21, 0.24]

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    for idx, C0 in enumerate(C0_values):
        style = SENSITIVITY_STYLES[idx % len(SENSITIVITY_STYLES)]
        Delta_min_vals: List[float] = []
        prev: Optional[Cutoffs] = None

        for kappa in kappa_values:
            try:
                p = base_params.replace(kappa=float(kappa), C0=C0)
                cutoffs, res = solve_valid(p, prev)
                if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                    Delta_min_vals.append(np.nan)
                    prev = None
                    continue
                prev = cutoffs
                total, _, _ = compute_minority_gains(cutoffs.k1, cutoffs.k0, cutoffs.kD, p)
                Delta_min_vals.append(total)
            except Exception:
                Delta_min_vals.append(np.nan)

        ax.plot(
            kappa_values, Delta_min_vals, linewidth=2.2,
            label=f"$C_0 = {C0:.2f}$", **style,
        )

    ax.set_xlabel("Liquidity $\\kappa$")
    ax.set_ylabel("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$")
    ax.set_title("Sensitivity to Engagement Cost $C_0$")
    ax.legend(loc="best", frameon=True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_sensitivity_premium_wedge(
    base_params: ModelParams,
    save_path: Optional[str] = None,
) -> None:
    """Figure 8: Sensitivity analysis -- Premium wedge."""
    kappa_values = np.linspace(0.25, 0.85, 21)
    wedge_values = [0.10, 0.20, 0.30]

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    for idx, wedge in enumerate(wedge_values):
        style = SENSITIVITY_STYLES[idx % len(SENSITIVITY_STYLES)]
        Delta_min_vals: List[float] = []
        prev: Optional[Cutoffs] = None

        for kappa in kappa_values:
            try:
                p = base_params.replace(kappa=float(kappa), m1=base_params.m0 + wedge)
                cutoffs, res = solve_valid(p, prev)
                if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                    Delta_min_vals.append(np.nan)
                    prev = None
                    continue
                prev = cutoffs
                total, _, _ = compute_minority_gains(cutoffs.k1, cutoffs.k0, cutoffs.kD, p)
                Delta_min_vals.append(total)
            except Exception:
                Delta_min_vals.append(np.nan)

        ax.plot(
            kappa_values, Delta_min_vals, linewidth=2.2,
            label=f"$m_1 - m_0 = {wedge:.2f}$", **style,
        )

    ax.set_xlabel("Liquidity $\\kappa$")
    ax.set_ylabel("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$")
    ax.set_title("Sensitivity to Premium Wedge $(m_1 - m_0)$")
    ax.legend(loc="best", frameon=True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_sensitivity_rho(
    base_params: ModelParams,
    save_path: Optional[str] = None,
) -> None:
    """Figure 9: Sensitivity analysis -- Engagement success probability."""
    kappa_values = np.linspace(0.25, 0.85, 21)
    rho_values = [0.5, 0.7, 0.9]

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    for idx, rho in enumerate(rho_values):
        style = SENSITIVITY_STYLES[idx % len(SENSITIVITY_STYLES)]
        Delta_min_vals: List[float] = []
        prev: Optional[Cutoffs] = None

        for kappa in kappa_values:
            try:
                p = base_params.replace(kappa=float(kappa), rho=rho)
                cutoffs, res = solve_valid(p, prev)
                if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                    Delta_min_vals.append(np.nan)
                    prev = None
                    continue
                prev = cutoffs
                total, _, _ = compute_minority_gains(
                    cutoffs.k1, cutoffs.k0, cutoffs.kD, p
                )
                Delta_min_vals.append(total)
            except Exception:
                Delta_min_vals.append(np.nan)

        ax.plot(
            kappa_values, Delta_min_vals, linewidth=2.2,
            label=f"$\\rho = {rho:.1f}$", **style,
        )

    ax.set_xlabel("Liquidity $\\kappa$")
    ax.set_ylabel("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$")
    ax.set_title("Sensitivity to Engagement Success $\\rho$")
    ax.legend(loc="best", frameon=True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_sensitivity_sigma_xi(
    base_params: ModelParams,
    save_path: Optional[str] = None,
) -> None:
    """Figure 10: Sensitivity analysis -- Bidder synergy volatility."""
    kappa_values = np.linspace(0.25, 0.85, 21)
    sigma_xi_values = [0.25, 0.40, 0.60]

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    for idx, sigma_xi in enumerate(sigma_xi_values):
        style = SENSITIVITY_STYLES[idx % len(SENSITIVITY_STYLES)]
        Delta_min_vals: List[float] = []
        prev: Optional[Cutoffs] = None

        for kappa in kappa_values:
            try:
                p = base_params.replace(kappa=float(kappa), sigma_xi=sigma_xi)
                cutoffs, res = solve_valid(p, prev)
                if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                    Delta_min_vals.append(np.nan)
                    prev = None
                    continue
                prev = cutoffs
                total, _, _ = compute_minority_gains(
                    cutoffs.k1, cutoffs.k0, cutoffs.kD, p
                )
                Delta_min_vals.append(total)
            except Exception:
                Delta_min_vals.append(np.nan)

        ax.plot(
            kappa_values, Delta_min_vals, linewidth=2.2,
            label=f"$\\sigma_\\xi = {sigma_xi:.2f}$", **style,
        )

    ax.set_xlabel("Liquidity $\\kappa$")
    ax.set_ylabel("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$")
    ax.set_title("Sensitivity to Bidder Heterogeneity $\\sigma_\\xi$")
    ax.legend(loc="best", frameon=True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_sensitivity_delta(
    base_params: ModelParams,
    save_path: Optional[str] = None,
) -> None:
    """Figure 11: Sensitivity analysis -- Discount factor."""
    kappa_values = np.linspace(0.25, 0.85, 21)
    delta_values = [0.85, 0.90, 0.95]

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    for idx, delta in enumerate(delta_values):
        style = SENSITIVITY_STYLES[idx % len(SENSITIVITY_STYLES)]
        Delta_min_vals: List[float] = []
        prev: Optional[Cutoffs] = None

        for kappa in kappa_values:
            try:
                p = base_params.replace(kappa=float(kappa), delta=delta)
                cutoffs, res = solve_valid(p, prev)
                if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                    Delta_min_vals.append(np.nan)
                    prev = None
                    continue
                prev = cutoffs
                total, _, _ = compute_minority_gains(
                    cutoffs.k1, cutoffs.k0, cutoffs.kD, p
                )
                Delta_min_vals.append(total)
            except Exception:
                Delta_min_vals.append(np.nan)

        ax.plot(
            kappa_values, Delta_min_vals, linewidth=2.2,
            label=f"$\\delta = {delta:.2f}$", **style,
        )

    ax.set_xlabel("Liquidity $\\kappa$")
    ax.set_ylabel("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$")
    ax.set_title("Sensitivity to Discount Factor $\\delta$")
    ax.legend(loc="best", frameon=True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_noisy_rumor_precision(
    base_params: ModelParams,
    save_path: Optional[str] = None,
) -> None:
    """Figure 12: Disclosure attenuation via noisy rumors."""
    kappa_values = np.linspace(0.25, 0.85, 21)
    rumor_configs = [
        (0.50, 0.50, "Uninformative"),
        (0.75, 0.25, "Moderate"),
        (0.95, 0.05, "Precise"),
    ]

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    for idx, (eta_1, eta_0, label) in enumerate(rumor_configs):
        style = SENSITIVITY_STYLES[idx % len(SENSITIVITY_STYLES)]
        Delta_min_vals: List[float] = []
        prev: Optional[Cutoffs] = None

        for kappa in kappa_values:
            try:
                p = base_params.replace(kappa=float(kappa))
                cutoffs, res = solve_valid(p, prev)
                if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                    Delta_min_vals.append(np.nan)
                    prev = None
                    continue
                prev = cutoffs
                gains = compute_minority_gains_noisy_rumor(
                    cutoffs.k1, cutoffs.k0, cutoffs.kD, p, eta_1, eta_0
                )
                Delta_min_vals.append(gains.total)
            except Exception:
                Delta_min_vals.append(np.nan)

        ax.plot(
            kappa_values, Delta_min_vals, linewidth=2.2,
            label=f"{label} ($\\eta_1={eta_1}, \\eta_0={eta_0}$)", **style,
        )

    ax.set_xlabel("Liquidity $\\kappa$")
    ax.set_ylabel("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$")
    ax.set_title("Disclosure Attenuation via Noisy Rumors")
    ax.legend(loc="best", frameon=True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def plot_welfare(
    base_params: ModelParams,
    save_path: Optional[str] = None,
) -> None:
    """Figure 13: Welfare Decomposition and Optimal Liquidity."""
    kappa_values = np.linspace(0.25, 0.85, 21)
    W_min_vals: List[float] = []
    W_bid_vals: List[float] = []
    W_tot_vals: List[float] = []

    prev: Optional[Cutoffs] = None
    for kappa in kappa_values:
        try:
            p = base_params.replace(kappa=float(kappa))
            cutoffs, res = solve_valid(p, prev)
            if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                W_min_vals.append(np.nan)
                W_bid_vals.append(np.nan)
                W_tot_vals.append(np.nan)
                prev = None
                continue
            prev = cutoffs
            W_min, W_bid, _, W_tot = compute_welfare(
                cutoffs.k1, cutoffs.k0, cutoffs.kD, p
            )
            W_min_vals.append(W_min)
            W_bid_vals.append(W_bid)
            W_tot_vals.append(W_tot)
        except Exception:
            W_min_vals.append(np.nan)
            W_bid_vals.append(np.nan)
            W_tot_vals.append(np.nan)

    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    ax.plot(
        kappa_values, W_tot_vals, color="#4477aa", linestyle="-",
        linewidth=2.2, label="Total Surplus $W$",
    )
    ax.plot(
        kappa_values, W_bid_vals, color="#ee6677", linestyle="--",
        linewidth=2.2, label="Bidder Surplus $W_{\\mathrm{bid}}$",
    )
    ax.plot(
        kappa_values, W_min_vals, color="#228833", linestyle="-.",
        linewidth=2.2, label="Minority Gains $W_{\\mathrm{min}}$",
    )

    W_min_arr = np.array(W_min_vals, dtype=float)
    W_tot_arr = np.array(W_tot_vals, dtype=float)

    if np.any(~np.isnan(W_min_arr)):
        idx_min = int(np.nanargmax(W_min_arr))
        kappa_dagger = float(kappa_values[idx_min])
        ax.axvline(
            kappa_dagger, color="#228833", linestyle=":", linewidth=1.2,
            alpha=0.7,
        )
        ax.text(
            kappa_dagger + 0.015, np.nanmin(W_min_arr),
            "$\\kappa^\\dagger$", color="#228833", fontsize=11,
        )

    if np.any(~np.isnan(W_tot_arr)):
        idx_tot = int(np.nanargmax(W_tot_arr))
        kappa_star = float(kappa_values[idx_tot])
        ax.axvline(
            kappa_star, color="#4477aa", linestyle=":", linewidth=1.2,
            alpha=0.7,
        )
        ax.text(
            kappa_star - 0.015, np.nanmax(W_tot_arr) * 0.95,
            "$\\kappa^*$", color="#4477aa", fontsize=11, ha="right",
        )

    ax.set_xlabel("Liquidity $\\kappa$")
    ax.set_ylabel("Expected Welfare / Surplus")
    ax.set_title("Welfare Decomposition")
    ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.4), frameon=True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


# ============================================================================
# LATEX TABLE FUNCTIONS
# ============================================================================


def write_baseline_table(
    k1: float, k0: float, kD: float,
    params: ModelParams,
    output_path: str,
) -> None:
    """Write LaTeX table rows for the baseline equilibrium (values rounded to two decimals)."""
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
    """Write LaTeX table for disclosure extensions (values rounded to two decimals)."""
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


def generate_all_figures(
    output_dir: str = "figures",
    include_sensitivity: bool = True,
    fast: bool = False,
) -> Tuple[ModelParams, Cutoffs]:
    """Generate all figures for the manuscript.

    Parameters
    ----------
    output_dir :
        Destination folder (created if missing).
    include_sensitivity :
        If False, only generates the baseline figures (1-6).
    fast :
        If True, uses a coarser liquidity grid for the baseline series to
        reduce runtime.  This does not change the model; it only reduces
        plot resolution.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Baseline parameters
    params = ModelParams()

    print("Solving baseline equilibrium...")
    k1, k0, kD = solve_equilibrium(params)
    print(f"Equilibrium cutoffs: k1={k1:.3f}, k0={k0:.3f}, kD={kD:.3f}")

    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    print(
        "Action probabilities (unconditional): "
        f"Exit={omega_E:.3f}, Hold={omega_H:.3f}, Quiet={omega_Q:.3f}, Public={omega_P:.2e}"
    )
    if omega_P < 1e-4:
        print(
            "NOTE: Public Voice probability is <1e-4 under this calibration; "
            "disclosed states (D=1) will be essentially absent on-path, so "
            "disclosure-vs-no-disclosure curves may overlap and D=1 bars may look irrelevant."
        )

    # Validate cutoff ordering (weak inequalities allow region collapse)
    if k1 <= k0 <= kD:
        print("Cutoff ordering verified: k1 <= k0 <= kD")
    else:
        print("WARNING: Cutoff ordering may be violated!")

    # Write baseline LaTeX table rows
    table_path = os.path.join(output_dir, "table_example.tex")
    write_baseline_table(k1, k0, kD, params, table_path)
    print(f"Baseline table rows written to: {table_path}")

    ext_table_path = os.path.join(output_dir, "table_disclosure_extensions.tex")
    write_disclosure_extension_table(k1, k0, kD, params, ext_table_path)
    print(f"Disclosure extensions table written to: {ext_table_path}")

    # Figure 1: cutoff structure
    print("\nGenerating Figure 1: Cutoff Structure...")
    plot_cutoff_structure(k1, k0, kD, params, f"{output_dir}/fig_cutoff_structure.pdf")

    # Precompute baseline series once and reuse across figures
    kappa_grid = np.linspace(0.15, 0.85, 21 if fast else 35)
    print(f"Computing baseline series over liquidity grid (N={len(kappa_grid)})...")
    baseline_series = compute_series_over_kappa(params, kappa_grid, include_no_disclosure=False)

    # Figures 2-3: non-monotonicity + decomposition
    print("Generating Figure 2: Non-Monotonicity...")
    plot_nonmonotonicity(params, f"{output_dir}/fig_nonmonotone.pdf", series=baseline_series)

    print("Generating Figure 3: Decomposition...")
    plot_decomposition(params, f"{output_dir}/fig_decomposition.pdf", series=baseline_series)

    # Figure 4: prices
    print("Generating Figure 4: Prices...")
    plot_prices(k1, k0, kD, params, f"{output_dir}/fig_prices.pdf")

    # Figure 5: cutoffs vs. liquidity
    print("Generating Figure 5: Cutoffs vs Kappa...")
    plot_cutoffs_vs_kappa(params, f"{output_dir}/fig_cutoffs_kappa.pdf", series=baseline_series)

    # Figure 6: disclosure attenuation
    print("Generating Figure 6: Disclosure Attenuation...")
    plot_disclosure_attenuation(
        params,
        f"{output_dir}/fig_disclosure.pdf",
        kappa_values=kappa_grid,
        kappa_ref=float(params.kappa),
        cutoffs_ref=(k1, k0, kD),
    )

    if include_sensitivity:
        # Figures 7-13: sensitivity and extensions (can be slow)
        print("Generating Figure 7: Sensitivity - C0...")
        plot_sensitivity_C0(params, f"{output_dir}/fig_sensitivity_C0.pdf")

        print("Generating Figure 8: Sensitivity - Premium Wedge...")
        plot_sensitivity_premium_wedge(params, f"{output_dir}/fig_sensitivity_wedge.pdf")

        print("Generating Figure 9: Sensitivity - Rho...")
        plot_sensitivity_rho(params, f"{output_dir}/fig_sensitivity_rho.pdf")

        print("Generating Figure 10: Sensitivity - Sigma Xi...")
        plot_sensitivity_sigma_xi(params, f"{output_dir}/fig_sensitivity_sigma_xi.pdf")

        print("Generating Figure 11: Sensitivity - Delta...")
        plot_sensitivity_delta(params, f"{output_dir}/fig_sensitivity_delta.pdf")

        print("Generating Figure 12: Extension - Noisy Rumor Precision...")
        plot_noisy_rumor_precision(params, f"{output_dir}/fig_noisy_rumor_precision.pdf")

        print("Generating Figure 13: Extension - Welfare...")
        plot_welfare(params, f"{output_dir}/fig_welfare.pdf")

    print(f"\nFigures written to: {output_dir}/")

    return params, Cutoffs(k1, k0, kD)
