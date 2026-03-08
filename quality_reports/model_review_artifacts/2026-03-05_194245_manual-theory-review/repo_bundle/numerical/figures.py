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

from .theme import (
    ACTION_COLORS, FIG_HEIGHT, FIG_WIDTH, PRIMARY_COLOR, SENSITIVITY_COLORS,
    save_figure, setup_theme,
)


def _read_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, na_values=["NA"])


def fig_cutoff_structure(output_dir: str, data_dir: str) -> None:
    regions = _read_csv(os.path.join(data_dir, "cutoff_regions.csv"))
    cutoffs = _read_csv(os.path.join(data_dir, "baseline_cutoffs.csv")).iloc[0]

    k1, k0, kD = float(cutoffs["k1"]), float(cutoffs["k0"]), float(cutoffs["kD"])

    x_min = float(regions["xmin"].min())
    x_max = float(regions["xmax"].max())

    fig, ax = plt.subplots()

    # Band geometry: centered vertically, leaving room for labels above and below.
    y0, h = 0.35, 0.30
    for _, row in regions.iterrows():
        name = str(row["region"])
        xmin = float(row["xmin"])
        xmax = float(row["xmax"])
        color = ACTION_COLORS.get(name, "#999999")
        ax.add_patch(patches.Rectangle((xmin, y0), xmax - xmin, h, facecolor=color, edgecolor="none", alpha=0.85))
        mid_x = 0.5 * (xmin + xmax)
        mid_y = y0 + 0.5 * h

        if name == "Quiet Voice":
            # Narrow band: place label above with an arrow pointing down to the band.
            ax.annotate(
                name, xy=(mid_x, y0 + h), xytext=(mid_x, y0 + h + 0.25),
                ha="center", va="bottom", fontsize=9, fontweight="bold", color="black",
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.2),
            )
        else:
            # Wide bands: plain black label centered inside.
            ax.text(mid_x, mid_y, name, ha="center", va="center", fontsize=9, fontweight="bold", color="black")

    # Cutoff markers: short vertical lines spanning the band only, labels below.
    for x, label in [(k1, r"$k_1$"), (k0, r"$k_0$"), (kD, r"$k_D$")]:
        ax.plot([x, x], [y0 - 0.08, y0 + h + 0.08], linestyle="--", linewidth=1.0, color="#333333", zorder=2)
        ax.text(x, y0 - 0.12, label, ha="center", va="top", fontsize=11)

    ax.set_xlim(x_min - 0.05, x_max + 0.05)
    ax.set_ylim(0.0, 1.0)
    ax.set_yticks([])
    ax.set_xlabel(r"Signal $s$")
    ax.set_title("Cutoff structure")
    ax.spines["left"].set_visible(False)

    save_figure(fig, os.path.join(output_dir, "fig_cutoff_structure.pdf"), width=7, height=2.5)


def fig_nonmonotone(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "baseline_series.csv"))
    df = df.dropna(subset=["kappa", "delta_min"])

    kappa = df["kappa"].values
    delta = df["delta_min"].values
    idx = int(np.nanargmax(delta))
    k_star = float(kappa[idx])
    d_star = float(delta[idx])

    fig, ax = plt.subplots()
    ax.plot(kappa, delta, color=PRIMARY_COLOR)
    ax.scatter([k_star], [d_star], s=45, zorder=3, color=PRIMARY_COLOR)
    ax.axvline(k_star, linestyle="--", linewidth=0.5, color="#333333")
    ax.text(k_star, d_star, r"  $\kappa^{\dagger}$", va="bottom")

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"Minority gains $\Delta^{\min}(\kappa)$")
    ax.set_title(r"Nonmonotone $\Delta^{\min}(\kappa)$")

    save_figure(fig, os.path.join(output_dir, "fig_nonmonotone.pdf"), width=FIG_WIDTH, height=FIG_HEIGHT)


def fig_decomposition(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "baseline_series.csv"))
    df = df.dropna(subset=["kappa", "delta_min", "base", "act"])

    # Mark κ†: maximizer of Δ^min on the plotted grid (same definition as fig_nonmonotone).
    idx = int(np.nanargmax(df["delta_min"].values))
    k_dag = float(df["kappa"].iloc[idx])

    fig, ax = plt.subplots()
    ax.plot(df["kappa"], df["delta_min"], color=SENSITIVITY_COLORS[0], label=r"Total $\Delta^{\min}$")
    ax.plot(df["kappa"], df["base"], linestyle="--", color=SENSITIVITY_COLORS[1], label=r"Baseline $\Delta^{\mathrm{base}}$")
    ax.plot(df["kappa"], df["act"], linestyle=":", color=SENSITIVITY_COLORS[2], label=r"Activism $\Delta^{\mathrm{act}}$")

    ax.axvline(k_dag, linestyle="--", linewidth=0.5, color="#333333")

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"Premium components")
    ax.set_title("Minority gains decomposition")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_decomposition.pdf"), width=FIG_WIDTH, height=FIG_HEIGHT)


def fig_prices(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "prices.csv"))
    df["X"] = df["X"].astype(int)
    df["D"] = df["D"].astype(int)
    if "on_path" in df.columns:
        df = df[df["on_path"] == True]  # noqa: E712 (explicit comparison is fine for pandas)

    fig, axes = plt.subplots(1, 2)

    for ax, D in zip(axes, [0, 1]):
        sub = df[df["D"] == D].sort_values("X")
        ax.bar(sub["X"].astype(str), sub["P_post"], alpha=0.9, color=PRIMARY_COLOR, label=r"$P_{post}(X,D)$")
        # Overlay execution price as marker (same across D given X)
        ax.scatter(sub["X"].astype(str), sub["P_trade"], marker="D", s=28, zorder=3, color="#333333", label=r"$P_{trade}(X)$")

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
    ax.plot(df["kappa"], df["k1"], color=ACTION_COLORS["Exit"], label=r"$k_1$ (Exit)")
    ax.plot(df["kappa"], df["k0"], color=ACTION_COLORS["Hold"], label=r"$k_0$ (Hold)")
    ax.plot(df["kappa"], df["kD"], color=ACTION_COLORS["Public Voice"], label=r"$k_D$ (Public)")
    ax.axhline(mu, linestyle="--", linewidth=0.5, color="#333333")

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel("Cutoff")
    ax.set_title(r"Equilibrium cutoffs across $\kappa$")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_cutoffs_kappa.pdf"), width=FIG_WIDTH, height=FIG_HEIGHT)


def fig_disclosure(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "disclosure_attenuation.csv"))
    df = df.dropna(subset=["kappa", "act_disclosure", "act_no_disclosure"])

    fig, ax = plt.subplots()
    ax.plot(df["kappa"], df["act_disclosure"], color=SENSITIVITY_COLORS[0], label="Threshold disclosure")
    ax.plot(df["kappa"], df["act_no_disclosure"], linestyle="--", color=SENSITIVITY_COLORS[1], label="No disclosure")

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"Activism component $\Delta^{\mathrm{act}}(\kappa)$")
    ax.set_title("Disclosure attenuates inference-driven sensitivity")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_disclosure.pdf"), width=FIG_WIDTH, height=FIG_HEIGHT)


def _fig_sensitivity_generic(output_dir: str, data_dir: str, csv_name: str, hue: str, title: str, out_name: str) -> None:
    df = _read_csv(os.path.join(data_dir, csv_name))
    df = df.dropna(subset=["kappa", hue, "delta_min"])

    fig, ax = plt.subplots()

    # Ensure deterministic hue order
    hue_order = sorted(df[hue].unique())

    palette = {val: SENSITIVITY_COLORS[i % len(SENSITIVITY_COLORS)] for i, val in enumerate(hue_order)}

    for val in hue_order:
        sub = df[df[hue] == val]
        ax.plot(sub["kappa"], sub["delta_min"], label=f"{hue}={val:g}", color=palette[val])

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"$\Delta^{\min}(\kappa)$")
    ax.set_title(title)
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, out_name), width=FIG_WIDTH, height=FIG_HEIGHT)


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


def fig_sensitivity_panel_a(output_dir: str, data_dir: str) -> None:
    """2-panel composite: s_xi (left) + delta (right)."""
    df_xi = _read_csv(os.path.join(data_dir, "sensitivity_sigma_xi.csv"))
    df_xi = df_xi.dropna(subset=["kappa", "s_xi", "delta_min"])
    df_d = _read_csv(os.path.join(data_dir, "sensitivity_delta.csv"))
    df_d = df_d.dropna(subset=["kappa", "delta", "delta_min"])

    fig, (ax1, ax2) = plt.subplots(1, 2)

    for i, val in enumerate(sorted(df_xi["s_xi"].unique())):
        sub = df_xi[df_xi["s_xi"] == val]
        ax1.plot(sub["kappa"], sub["delta_min"], color=SENSITIVITY_COLORS[i % len(SENSITIVITY_COLORS)], label=f"{val:g}")
    ax1.set_xlabel(r"Liquidity $\kappa$")
    ax1.set_ylabel(r"$\Delta^{\min}(\kappa)$")
    ax1.set_title(r"Bidder shock $s_{\xi}$")
    ax1.legend(title=r"$s_{\xi}$", frameon=False, fontsize=8, title_fontsize=8)

    for i, val in enumerate(sorted(df_d["delta"].unique())):
        sub = df_d[df_d["delta"] == val]
        ax2.plot(sub["kappa"], sub["delta_min"], color=SENSITIVITY_COLORS[i % len(SENSITIVITY_COLORS)], label=f"{val:g}")
    ax2.set_xlabel(r"Liquidity $\kappa$")
    ax2.set_ylabel(r"$\Delta^{\min}(\kappa)$")
    ax2.set_title(r"Discount factor $\delta$")
    ax2.legend(title=r"$\delta$", frameon=False, fontsize=8, title_fontsize=8)

    save_figure(fig, os.path.join(output_dir, "fig_sensitivity_panel1.pdf"), width=2 * FIG_WIDTH, height=FIG_HEIGHT)


def fig_sensitivity_panel_b(output_dir: str, data_dir: str) -> None:
    """3-panel composite: C0 (left) + wedge (center) + rho (right)."""
    configs = [
        ("sensitivity_C0.csv", "C0", r"Engagement cost $C_0$"),
        ("sensitivity_wedge.csv", "wedge", r"Premium wedge $(m_1-m_0)$"),
        ("sensitivity_rho.csv", "rho", r"Success prob.\ $\rho$"),
    ]

    fig, axes = plt.subplots(1, 3)

    for ax, (csv_name, hue, title) in zip(axes, configs):
        df = _read_csv(os.path.join(data_dir, csv_name))
        df = df.dropna(subset=["kappa", hue, "delta_min"])
        for i, val in enumerate(sorted(df[hue].unique())):
            sub = df[df[hue] == val]
            ax.plot(sub["kappa"], sub["delta_min"], color=SENSITIVITY_COLORS[i % len(SENSITIVITY_COLORS)], label=f"{val:g}")
        ax.set_xlabel(r"Liquidity $\kappa$")
        ax.set_ylabel(r"$\Delta^{\min}(\kappa)$")
        ax.set_title(title, fontsize=10)
        ax.legend(title=hue, frameon=False, fontsize=7, title_fontsize=7)

    save_figure(fig, os.path.join(output_dir, "fig_sensitivity_panel2.pdf"), width=2.5 * FIG_WIDTH, height=FIG_HEIGHT)


def fig_disclosure_slopes(output_dir: str, data_dir: str) -> None:
    """Slope figure: d(Delta^act)/d(kappa) for disclosure vs no-disclosure."""
    df = _read_csv(os.path.join(data_dir, "disclosure_attenuation.csv"))
    df = df.dropna(subset=["kappa", "act_disclosure", "act_no_disclosure"])

    kappa = df["kappa"].values
    slope_disc = np.gradient(df["act_disclosure"].values, kappa)
    slope_nodisc = np.gradient(df["act_no_disclosure"].values, kappa)

    fig, ax = plt.subplots()
    ax.plot(kappa, slope_disc, color=SENSITIVITY_COLORS[0], label="Disclosure")
    ax.plot(kappa, slope_nodisc, linestyle="--", color=SENSITIVITY_COLORS[1], label="No disclosure")
    ax.fill_between(kappa, slope_disc, slope_nodisc, alpha=0.15, color=SENSITIVITY_COLORS[1], label="Gap")
    ax.axhline(0.0, linewidth=0.5, color="#333333")

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"Slope $\partial\Delta^{\mathrm{act}}/\partial\kappa$")
    ax.set_title("Disclosure attenuates liquidity sensitivity")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_disclosure_slopes.pdf"), width=FIG_WIDTH, height=FIG_HEIGHT)


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
        ax.plot(sub["kappa"], sub["delta_min"], label=lab, color=palette.get(lab, None))

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"$\Delta^{\min}(\kappa)$")
    ax.set_title("Noisy rumor precision flattens the liquidity sensitivity")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_noisy_rumor_precision.pdf"), width=FIG_WIDTH, height=FIG_HEIGHT)


def fig_welfare(output_dir: str, data_dir: str) -> None:
    df = _read_csv(os.path.join(data_dir, "welfare.csv"))
    df = df.dropna(subset=["kappa", "W_min", "W_bid", "W_tot"])

    kappa = df["kappa"].values

    idx_min = int(np.nanargmax(df["W_min"].values))
    idx_tot = int(np.nanargmax(df["W_tot"].values))
    k_dag = float(kappa[idx_min])
    k_star = float(kappa[idx_tot])

    fig, ax = plt.subplots()
    ax.plot(df["kappa"], df["W_min"], color=SENSITIVITY_COLORS[0], label=r"$W_{\min}=\Delta^{\min}$")
    ax.plot(df["kappa"], df["W_bid"], linestyle="--", color=SENSITIVITY_COLORS[1], label=r"$W_{\mathrm{bid}}$")
    ax.plot(df["kappa"], df["W_tot"], linestyle=":", color=SENSITIVITY_COLORS[2], label=r"$W_{\mathrm{tot}}$")

    ax.axvline(k_dag, linestyle="--", linewidth=0.5, color="#333333")
    ax.axvline(k_star, linestyle="-.", linewidth=0.5, color="#333333")
    ax.text(k_dag, df["W_min"].iloc[idx_min], r"  $\kappa^{\dagger}$", va="bottom")
    ax.text(k_star, df["W_tot"].iloc[idx_tot], r"  $\kappa^{*}$", va="bottom")

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel("Welfare")
    ax.set_title("Welfare decomposition")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_welfare.pdf"), width=FIG_WIDTH, height=FIG_HEIGHT)


def fig_timeline(output_dir: str, data_dir: str) -> None:
    """5-stage model timeline with color-coded annotations."""
    fig, ax = plt.subplots()

    # Stage positions (map model times to evenly-spaced visual positions)
    stages = [0, 1, 2, 3, 4]
    stage_labels = [r"$t=0$", r"$t=1$", r"$t=1.2$", r"$t=1.5$", r"$t=2$"]

    # Draw timeline arrow
    ax.annotate("", xy=(4.5, 0), xytext=(-0.4, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.5))

    # Stage markers
    for x, lab in zip(stages, stage_labels):
        ax.plot(x, 0, "o", color="black", markersize=7, zorder=5)
        ax.text(x, 0.12, lab, ha="center", va="bottom", fontsize=11, fontweight="bold")

    # Color-coded annotations (blue=choices, rose=observables, green=outcomes)
    blue = "#4477aa"    # choices
    rose = "#cc6677"    # observables
    green = "#228833"   # outcomes

    # t=0: Nature draws v, blockholder sees s
    ax.text(0, -0.15, "Nature draws $v$", ha="center", va="top", fontsize=8.5, color="black")
    ax.text(0, -0.28, "Blockholder sees $s$", ha="center", va="top", fontsize=8.5, color=blue)

    # t=1: Choose (q,a), noise z, anonymous execution
    ax.text(1, -0.15, "Choose $(q, a)$", ha="center", va="top", fontsize=8.5, color=blue)
    ax.text(1, -0.28, "Noise $z$ realized", ha="center", va="top", fontsize=8.5, color=rose)
    ax.text(1, -0.41, "Trade at $P_{\\mathrm{trade}}(X)$",
            ha="center", va="top", fontsize=8.5, color=rose)

    # t=1.2: Disclosure revealed, price updates
    ax.text(2, -0.15, "$D = \\mathbf{1}\\{q=+1\\}$ revealed",
            ha="center", va="top", fontsize=8.5, color=rose)
    ax.text(2, -0.28, "Price $\\to P_{\\mathrm{post}}(X,D)$",
            ha="center", va="top", fontsize=8.5, color=green)

    # t=1.5: Bidder arrives, observes (X,D), draws xi
    ax.text(3, -0.15, "Bidder arrives w.p. $\\lambda_B$",
            ha="center", va="top", fontsize=8.5, color="black")
    ax.text(3, -0.28, "Observes $(X, D)$, draws $\\xi$",
            ha="center", va="top", fontsize=8.5, color=rose)

    # t=2: Payoffs
    ax.text(4, -0.15, "Takeover or not", ha="center", va="top", fontsize=8.5, color="black")
    ax.text(4, -0.28, "Payoffs realized", ha="center", va="top", fontsize=8.5, color=green)

    ax.set_xlim(-0.5, 4.8)
    ax.set_ylim(-0.55, 0.3)
    ax.axis("off")

    save_figure(fig, os.path.join(output_dir, "fig_timeline.pdf"), width=9.5, height=2.8)


def fig_mechanism_chain(output_dir: str, data_dir: str) -> None:
    """Feed-forward mechanism chain: s -> (q,a) -> (X,D) -> pi -> p -> Delta^min."""
    fig, ax = plt.subplots()

    blue = "#4477aa"    # choices
    rose = "#cc6677"    # observables
    green = "#228833"   # outcomes

    nodes = [
        (0.0, r"$s$", blue),
        (1.0, r"$(q, a)$", blue),
        (2.0, r"$(X, D)$", rose),
        (3.0, r"$\pi$", green),
        (4.0, r"$p$", green),
        (5.0, r"$\Delta^{\min}$", green),
    ]

    for x, label, color in nodes:
        circle = plt.Circle((x, 0), 0.3, facecolor=color, edgecolor="black",
                            alpha=0.2, linewidth=1.2, zorder=2)
        ax.add_patch(circle)
        ax.text(x, 0, label, ha="center", va="center", fontsize=13,
                fontweight="bold", color=color, zorder=3)

    # Arrows between nodes
    for i in range(len(nodes) - 1):
        x_start = nodes[i][0] + 0.32
        x_end = nodes[i + 1][0] - 0.32
        ax.annotate("", xy=(x_end, 0), xytext=(x_start, 0),
                    arrowprops=dict(arrowstyle="-|>", color="#333333", lw=1.5))

    # Category labels below
    ax.text(0.5, -0.55, "Choices", ha="center", va="top", fontsize=10, color=blue, fontstyle="italic")
    ax.text(2.0, -0.55, "Observables", ha="center", va="top", fontsize=10, color=rose, fontstyle="italic")
    ax.text(4.0, -0.55, "Outcomes", ha="center", va="top", fontsize=10, color=green, fontstyle="italic")

    ax.set_xlim(-0.6, 5.6)
    ax.set_ylim(-0.75, 0.55)
    ax.set_aspect("equal")
    ax.axis("off")

    save_figure(fig, os.path.join(output_dir, "fig_mechanism_chain.pdf"), width=8.0, height=2.5)


def make_all(output_dir: str, data_dir: Optional[str] = None) -> None:
    if data_dir is None:
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
    fig_sensitivity_panel_a(output_dir, data_dir)
    fig_sensitivity_panel_b(output_dir, data_dir)
    fig_disclosure_slopes(output_dir, data_dir)

    fig_noisy_rumor_precision(output_dir, data_dir)
    fig_welfare(output_dir, data_dir)

    fig_timeline(output_dir, data_dir)
    fig_mechanism_chain(output_dir, data_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate PDF figures from exported CSVs")
    parser.add_argument("--output-dir", default="numerical_output", help="Output directory for PDFs")
    parser.add_argument("--data-dir", default=None, help="Data directory (default: OUTPUT_DIR/data)")
    args = parser.parse_args()

    make_all(output_dir=args.output_dir, data_dir=args.data_dir)
