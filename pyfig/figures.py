"""The thirteen manuscript figures, generated from the exported CSV data.

Each ``fig0X_*`` function reads its CSV(s) from ``data_dir`` and writes a single
vector PDF to ``output_dir`` under the filename the manuscript references.
"""
from __future__ import annotations

import os

import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle, Patch
from matplotlib.lines import Line2D

from . import style

KAPPA = r"Liquidity $\kappa$"
DMIN = r"Expected Minority Takeover Gains $\Delta^{\mathrm{min}}$"


def _csv(data_dir, name):
    return pd.read_csv(os.path.join(data_dir, name))


# --------------------------------------------------------------------------
# Figure 1: Equilibrium cutoff structure on the signal number line
# --------------------------------------------------------------------------
def fig01_cutoff_structure(data_dir, output_dir):
    cut = _csv(data_dir, "baseline_cutoffs.csv").iloc[0]
    regions = _csv(data_dir, "cutoff_regions.csv")
    k1, k0, kD, mu = cut["k1"], cut["k0"], cut["kD"], cut["mu"]
    has_hold = abs(k0 - k1) > 1e-4

    fig, ax = style.new_ax(width=8, height=2.5)

    for _, r in regions.iterrows():
        color = style.ACTION_COLORS.get(r["region"], "#cccccc")
        ax.add_patch(Rectangle((r["xmin"], -0.2), r["xmax"] - r["xmin"], 0.4,
                               facecolor=color, alpha=0.7, edgecolor="none"))
        if (r["xmax"] - r["xmin"]) >= 0.8:
            ax.text((r["xmin"] + r["xmax"]) / 2, 0.0, r["region"],
                    ha="center", va="center", fontsize=8.5, fontweight="bold")

    cuts = [(k1, "$k_1$")] + ([(k0, "$k_0$")] if has_hold else []) + [(kD, "$k_D$")]
    for x, _ in cuts:
        ax.axvline(x, linestyle="--", linewidth=0.5, color="black", alpha=0.9)

    # number line with cutoff points + labels
    ax.axhline(-0.32, linewidth=0.5, color="black", alpha=0.8)
    for x, lab in cuts:
        ax.plot([x], [-0.32], marker="o", color="black", markersize=4)
    ax.text(k1, -0.44, "$k_1$" if has_hold else "$k_1 = k_0$",
            ha="center", va="top", fontsize=11)
    if has_hold:
        ax.text(k0, -0.52, "$k_0$", ha="center", va="top", fontsize=11)
    ax.text(kD, -0.44, "$k_D$", ha="center", va="top", fontsize=11)

    # prior mean reference
    ax.axvline(mu, color=style.REF_GREY, linestyle=":", linewidth=0.5)
    ax.text(mu, 0.37, r"$\mu$", ha="center", va="bottom",
            color=style.REF_GREY, fontsize=11)

    ax.set_xlabel(r"Signal $s$")
    ax.set_ylim(-0.6, 0.5)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(False)

    present = [r for r in ["Exit", "Hold", "Quiet Voice", "Public Voice"]
              if r in set(regions["region"])]
    handles = [Patch(facecolor=style.ACTION_COLORS[r], alpha=0.7, label=r)
               for r in present]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 1.0),
              ncol=len(handles), frameon=False, handlelength=1.2,
              columnspacing=1.4)
    style.save_fig(fig, os.path.join(output_dir, "fig_cutoff_structure.pdf"))


# --------------------------------------------------------------------------
# Figure 2: Non-monotonic effect of liquidity on takeover gains
# --------------------------------------------------------------------------
def fig02_nonmonotone(data_dir, output_dir):
    df = _csv(data_dir, "baseline_series.csv").dropna(subset=["Delta_min"])
    df = df.sort_values("kappa")
    kpk = df["kappa"].iloc[df["Delta_min"].values.argmax()]

    fig, ax = style.new_ax()
    ax.plot(df["kappa"], df["Delta_min"], color="#4477aa", linewidth=1.4)
    ax.axvline(kpk, color=style.REF_GREY, linestyle="--", linewidth=0.5, alpha=0.7)
    ax.text(kpk + 0.015, df["Delta_min"].max() * 0.98, r"$\kappa^{\dagger}$",
            color=style.REF_GREY, fontsize=12, va="top")
    ax.set_xlabel(KAPPA)
    ax.set_ylabel(DMIN)
    ax.set_title("Non-Monotonic Effect of Liquidity on Takeover Gains")
    style.save_fig(fig, os.path.join(output_dir, "fig_nonmonotone.pdf"))


# --------------------------------------------------------------------------
# Figure 3: Decomposition of minority takeover gains (base + activism)
# --------------------------------------------------------------------------
def fig03_decomposition(data_dir, output_dir):
    df = _csv(data_dir, "baseline_series.csv").dropna(subset=["base", "act"])
    df = df.sort_values("kappa")
    total = df["base"] + df["act"]
    kpk = df["kappa"].iloc[total.values.argmax()]

    fig, ax = style.new_ax()
    ax.fill_between(df["kappa"], 0, df["base"], color=style.COL_QUIET, alpha=0.5,
                    label=r"Base: $m_0 \cdot P(\mathrm{bid})$")
    ax.fill_between(df["kappa"], df["base"], total, color=style.COL_EXIT, alpha=0.5,
                    label=r"Activism: $\Delta^{\mathrm{act}}(\kappa)$")
    ax.plot(df["kappa"], total, color="black", linewidth=0.9,
            label=r"Total $\Delta^{\mathrm{min}}$")
    ax.axvline(kpk, color=style.REF_GREY, linestyle="--", linewidth=0.5, alpha=0.7)
    ax.text(kpk + 0.015, total.max() * 0.98, r"$\kappa^{\dagger}$",
            color=style.REF_GREY, fontsize=12, va="top")
    ax.set_xlabel(KAPPA)
    ax.set_ylabel("Expected Minority Takeover Gains")
    ax.set_title("Decomposition of Minority Takeover Gains")
    ax.legend(loc="upper left", framealpha=1.0)
    style.save_fig(fig, os.path.join(output_dir, "fig_decomposition.pdf"))


# --------------------------------------------------------------------------
# Figure 4: Equilibrium prices by state (two panels: D=0, D=1)
# --------------------------------------------------------------------------
def fig04_prices(data_dir, output_dir):
    import matplotlib.pyplot as plt
    df = _csv(data_dir, "prices.csv")
    d0 = df[(df["D"] == 0) & (df["on_path"] == True)].sort_values("X")  # noqa: E712
    d1 = df[df["D"] == 1].sort_values("X")
    allp = np.concatenate([d0["price"].values, d1["price"].values])
    allp = allp[np.isfinite(allp)]
    ymax = allp.max() * 1.18

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for ax, d, col, ttl, ylab, pis in (
        (axes[0], d0, style.COL_QUIET, r"Non-Disclosed States ($D=0$)",
         r"Price $P(X, D=0)$", d0["pi"]),
        (axes[1], d1, style.COL_EXIT, r"Disclosed States ($D=1$)",
         r"Price $P(X, D=1)$", None),
    ):
        style.despine(ax)
        xs = [f"$X={int(x)}$" for x in d["X"]]
        bars = ax.bar(xs, d["price"], color=col, edgecolor="black",
                      linewidth=0.6, alpha=0.8, width=0.6)
        labels = ([f"$\\pi={p:.2f}$" for p in pis] if pis is not None
                  else [r"$\pi=1.00$"] * len(d))
        for b, lab in zip(bars, labels):
            ax.text(b.get_x() + b.get_width() / 2, b.get_height(), lab,
                    ha="center", va="bottom", fontsize=9)
        ax.set_ylim(0, ymax)
        ax.set_title(ttl)
        ax.set_ylabel(ylab)
    fig.tight_layout()
    style.save_fig(fig, os.path.join(output_dir, "fig_prices.pdf"))


# --------------------------------------------------------------------------
# Figure 5: Equilibrium cutoffs vs. liquidity
# --------------------------------------------------------------------------
def fig05_cutoffs_kappa(data_dir, output_dir):
    df = _csv(data_dir, "baseline_series.csv").sort_values("kappa")
    params = _csv(data_dir, "baseline_params.csv")
    mu = float(params.loc[params["param"] == "mu", "value"].iloc[0])
    k0_eq_k1 = np.nanmax(np.abs(df["k0"] - df["k1"])) < 1e-3

    fig, ax = style.new_ax()
    if k0_eq_k1:
        series = [("k1", r"$k_1 = k_0$ (Exit/Quiet)", style.COL_EXIT, "-", "o"),
                  ("kD", r"$k_D$ (Quiet/Public)", style.COL_QUIET, "-.", "^")]
    else:
        series = [("k1", r"$k_1$ (Exit/Hold)", style.COL_EXIT, "-", "o"),
                  ("k0", r"$k_0$ (Hold/Quiet)", style.COL_HOLD, "--", "s"),
                  ("kD", r"$k_D$ (Quiet/Public)", style.COL_QUIET, "-.", "^")]
    for col, lab, c, ls, mk in series:
        ax.plot(df["kappa"], df[col], color=c, linestyle=ls, marker=mk,
                markersize=4, linewidth=1.3, label=lab)
    ax.axhline(mu, color=style.REF_GREY, linestyle=":", linewidth=0.5)
    ax.text(df["kappa"].max() - 0.02, mu + 0.03, r"$\mu$",
            color=style.REF_GREY, fontsize=11)
    ax.set_xlabel(KAPPA)
    ax.set_ylabel("Signal Cutoff")
    ax.set_title("Equilibrium Cutoffs vs. Liquidity")
    style.legend_outside(ax)
    style.save_fig(fig, os.path.join(output_dir, "fig_cutoffs_kappa.pdf"))


# --------------------------------------------------------------------------
# Figure 6: Disclosure attenuation through the inference channel
# --------------------------------------------------------------------------
def fig06_disclosure(data_dir, output_dir):
    df = _csv(data_dir, "disclosure_attenuation.csv").sort_values("kappa")
    fig, ax = style.new_ax()
    ax.plot(df["kappa"], df["act_disclosure"], color="#4477aa", linestyle="-",
            marker="o", markersize=3.5, linewidth=1.3,
            label="Threshold disclosure (baseline)")
    ax.plot(df["kappa"], df["act_no_disclosure"], color="#ee6677", linestyle="--",
            marker="s", markersize=3.5, linewidth=1.3,
            label="No disclosure (counterfactual)")
    ax.set_xlabel(KAPPA)
    ax.set_ylabel(r"Activism-Driven Minority Gains $\Delta^{\mathrm{act}}$")
    ax.set_title("Disclosure Attenuation of Liquidity Sensitivity")
    ax.legend(loc="upper right", framealpha=1.0)
    style.save_fig(fig, os.path.join(output_dir, "fig_disclosure.pdf"))


# --------------------------------------------------------------------------
# Figures 7-11: Sensitivity panels (shared helper)
# --------------------------------------------------------------------------
def _sensitivity(data_dir, output_dir, csv, param_col, legend_fmt, title,
                 filename):
    df = _csv(data_dir, csv)
    fig, ax = style.new_ax()
    vals = sorted(pd.unique(df[param_col].dropna()))
    plotted = 0
    for i, v in enumerate(vals):
        sub = (df[df[param_col] == v]
               .dropna(subset=["Delta_min"]).sort_values("kappa"))
        if sub.empty:
            continue
        ax.plot(sub["kappa"], sub["Delta_min"],
                color=style.SENS_COLORS[i % 4],
                linestyle=style.SENS_LINESTYLES[i % 4],
                marker=style.SENS_MARKERS[i % 4],
                markersize=4, linewidth=1.3, label=legend_fmt(v))
        plotted += 1
    ax.set_xlabel(KAPPA)
    ax.set_ylabel(DMIN)
    ax.set_title(title)
    if plotted:
        style.legend_outside(ax)
    style.save_fig(fig, os.path.join(output_dir, filename))


def fig07_sensitivity_C0(data_dir, output_dir):
    _sensitivity(data_dir, output_dir, "sensitivity_C0.csv", "C0",
                 lambda v: f"$C_0 = {v:.2f}$",
                 r"Sensitivity to Engagement Cost $C_0$",
                 "fig_sensitivity_C0.pdf")


def fig08_sensitivity_wedge(data_dir, output_dir):
    _sensitivity(data_dir, output_dir, "sensitivity_wedge.csv", "wedge",
                 lambda v: f"$m_1 - m_0 = {v:.2f}$",
                 r"Sensitivity to Premium Wedge $(m_1 - m_0)$",
                 "fig_sensitivity_wedge.pdf")


def fig09_sensitivity_rho(data_dir, output_dir):
    _sensitivity(data_dir, output_dir, "sensitivity_rho.csv", "rho",
                 lambda v: f"$\\rho = {v:.1f}$",
                 r"Sensitivity to Engagement Success $\rho$",
                 "fig_sensitivity_rho.pdf")


def fig10_sensitivity_sigma_xi(data_dir, output_dir):
    _sensitivity(data_dir, output_dir, "sensitivity_sigma_xi.csv", "sigma_xi",
                 lambda v: f"$\\sigma_\\xi = {v:.2f}$",
                 r"Sensitivity to Bidder Heterogeneity $\sigma_\xi$",
                 "fig_sensitivity_sigma_xi.pdf")


def fig11_sensitivity_delta(data_dir, output_dir):
    _sensitivity(data_dir, output_dir, "sensitivity_delta.csv", "delta",
                 lambda v: f"$\\delta = {v:.2f}$",
                 r"Sensitivity to Discount Factor $\delta$",
                 "fig_sensitivity_delta.pdf")


# --------------------------------------------------------------------------
# Figure 12: Disclosure attenuation via noisy rumors
# --------------------------------------------------------------------------
def fig12_noisy_rumor(data_dir, output_dir):
    df = _csv(data_dir, "noisy_rumor.csv")
    order = ["Uninformative", "Moderate", "Precise"]
    fig, ax = style.new_ax()
    for i, lab in enumerate(order):
        sub = df[df["label"] == lab].dropna(subset=["Delta_min"]).sort_values("kappa")
        if sub.empty:
            continue
        r0 = sub.iloc[0]
        leg = f"{lab} ($\\eta_1={r0['eta_1']:.2f}, \\eta_0={r0['eta_0']:.2f}$)"
        ax.plot(sub["kappa"], sub["Delta_min"],
                color=style.SENS_COLORS[i % 4],
                linestyle=style.SENS_LINESTYLES[i % 4],
                marker=style.SENS_MARKERS[i % 4],
                markersize=4, linewidth=1.3, label=leg)
    ax.set_xlabel(KAPPA)
    ax.set_ylabel(DMIN)
    ax.set_title("Disclosure Attenuation via Noisy Rumors")
    style.legend_outside(ax)
    style.save_fig(fig, os.path.join(output_dir, "fig_noisy_rumor_precision.pdf"))


# --------------------------------------------------------------------------
# Figure 13: Welfare decomposition and optimal liquidity
# --------------------------------------------------------------------------
def fig13_welfare(data_dir, output_dir):
    df = _csv(data_dir, "welfare.csv").dropna(subset=["W_min", "W_bid", "W_tot"])
    df = df.sort_values("kappa")
    k_dagger = df["kappa"].iloc[df["W_min"].values.argmax()]
    k_star = df["kappa"].iloc[df["W_tot"].values.argmax()]

    fig, ax = style.new_ax()
    ax.plot(df["kappa"], df["W_tot"], color="#4477aa", linestyle="-",
            linewidth=1.3, label=r"Total Surplus $W$")
    ax.plot(df["kappa"], df["W_bid"], color="#ee6677", linestyle="--",
            linewidth=1.3, label=r"Bidder Surplus $W_{\mathrm{bid}}$")
    ax.plot(df["kappa"], df["W_min"], color="#228833", linestyle="-.",
            linewidth=1.3, label=r"Minority Gains $W_{\mathrm{min}}$")
    ax.axvline(k_dagger, color="#228833", linestyle=":", linewidth=0.5, alpha=0.7)
    ax.text(k_dagger + 0.015, df["W_min"].min(), r"$\kappa^{\dagger}$",
            color="#228833", fontsize=12)
    ax.axvline(k_star, color="#4477aa", linestyle=":", linewidth=0.5, alpha=0.7)
    ax.text(k_star - 0.015, df["W_tot"].max() * 0.95, r"$\kappa^{*}$",
            color="#4477aa", fontsize=12, ha="right")
    ax.set_xlabel(KAPPA)
    ax.set_ylabel("Expected Welfare / Surplus")
    ax.set_title("Welfare Decomposition")
    ax.legend(loc="center right", framealpha=1.0)
    style.save_fig(fig, os.path.join(output_dir, "fig_welfare.pdf"))


# --------------------------------------------------------------------------
# Figure 14: GE cutoff-shift channel decomposition + hump/trough map (App D8)
# --------------------------------------------------------------------------
def fig14_ge_decomposition(data_dir, output_dir):
    import matplotlib.pyplot as plt
    path = _csv(data_dir, "ge_decomposition.csv").dropna(subset=["chanA", "chanB"])
    cells = _csv(data_dir, "ge_cellmap.csv").dropna(subset=["shape"])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 3.6))
    style.despine(ax1)
    style.despine(ax2)

    path = path.sort_values("kappa")
    ax1.axhline(0, color="black", linewidth=0.5)
    ax1.plot(path["kappa"], path["chanA"], color="#4477aa", linestyle="-",
             linewidth=1.3, label="Channel (A): posterior/pricing")
    ax1.plot(path["kappa"], path["chanB"], color="#ee6677", linestyle="--",
             linewidth=1.3, label="Channel (B): GE cutoff-shift")
    ax1.plot(path["kappa"], path["total"], color="black", linestyle="-.",
             linewidth=1.0, label=r"Total $\mathrm{d}\Delta^{\mathrm{min}}/\mathrm{d}\kappa$")
    ax1.set_xlabel(KAPPA)
    ax1.set_ylabel(r"$\mathrm{d}\Delta^{\mathrm{min}}/\mathrm{d}\kappa$")
    ax1.set_title("Baseline decomposition", fontsize=11)
    ax1.legend(fontsize=8, framealpha=1.0)

    shape_style = {"hump": ("o", style.COL_PUBLIC, "Hump"),
                   "trough": ("s", style.COL_EXIT, "Trough"),
                   "flat": ("D", style.COL_HOLD, "Flat")}
    seen = set()
    for _, r in cells.iterrows():
        m, c, lab = shape_style.get(r["shape"], ("x", "grey", r["shape"]))
        ax2.scatter(r["S_bar"], r["sigma_xi"], marker=m, s=120, color=c,
                    edgecolors="black", linewidths=0.4,
                    label=lab if lab not in seen else None)
        seen.add(lab)
    ax2.set_xlabel(r"Baseline synergy $\bar{S}$")
    ax2.set_ylabel(r"Bidder heterogeneity $\sigma_\xi$")
    ax2.set_title("Hump/trough boundary (App. D8 counterexample)", fontsize=11)
    ax2.legend(fontsize=8, framealpha=1.0, loc="center left")
    ax2.set_yticks([0.20, 0.40, 0.60])
    ax2.set_xticks([1.24, 1.44, 1.64])

    fig.suptitle("The GE Cutoff-Shift Channel", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    style.save_fig(fig, os.path.join(output_dir, "fig_ge_decomposition.pdf"))


# --------------------------------------------------------------------------
# Figure 15: Minority gains under the microfounded wedge (Appendix D7)
# --------------------------------------------------------------------------
def fig15_wedge_primitives(data_dir, output_dir):
    import matplotlib.pyplot as plt
    df = _csv(data_dir, "wedge_primitives.csv")

    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6), sharey=True)
    specs = [
        ("gamma", r"Portability $\gamma$ (fringe intensity $q$ fixed)",
         axes[0], lambda v: rf"$\gamma = {v:.1f}$"),
        ("q", r"Fringe intensity $q$ (portability $\gamma$ fixed)",
         axes[1], lambda v: rf"$q = {v:.1f}$"),
    ]
    for sweep, subtitle, ax, lab in specs:
        style.despine(ax)
        sub_all = df[df["sweep"] == sweep]
        for i, value in enumerate(sorted(sub_all["value"].unique())):
            sub = (sub_all[sub_all["value"] == value]
                   .dropna(subset=["Delta_min"]).sort_values("kappa"))
            if sub.empty:
                continue
            lam = sub["lambda"].iloc[0]
            ax.plot(sub["kappa"], sub["Delta_min"],
                    color=style.SENS_COLORS[i % 4],
                    linestyle=style.SENS_LINESTYLES[i % 4],
                    marker=style.SENS_MARKERS[i % 4],
                    markersize=3.5, linewidth=1.2,
                    label=lab(value) + rf"  ($\lambda = {lam:.2f}$)")
        ax.set_xlabel(KAPPA)
        ax.set_title(subtitle, fontsize=11)
        ax.legend(framealpha=1.0, fontsize=8)
    axes[0].set_ylabel(r"$\Delta^{\mathrm{min}}$")
    fig.suptitle("Minority Gains under the Microfounded Wedge "
                 r"$m_1 - m_0 = (1-\theta)\,\lambda\,\rho\,\Delta_{\mathrm{eng}}$",
                 fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    style.save_fig(fig, os.path.join(output_dir, "fig_wedge_primitives.pdf"))


ALL_FIGURES = [
    fig01_cutoff_structure, fig02_nonmonotone, fig03_decomposition,
    fig04_prices, fig05_cutoffs_kappa, fig06_disclosure,
    fig07_sensitivity_C0, fig08_sensitivity_wedge, fig09_sensitivity_rho,
    fig10_sensitivity_sigma_xi, fig11_sensitivity_delta,
    fig12_noisy_rumor, fig13_welfare,
    fig14_ge_decomposition, fig15_wedge_primitives,
]
