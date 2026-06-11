"""Slide-only figure variants, rendered in the pyfig house style.

Four figures referenced exclusively by the Beamer deck (``pres/presentation.tex``)
and the PPTX build (``pres/make_pptx.py``), written to ``pres/figures/``:

  * ``fig_disclosure_slopes.pdf``  -- slope of the activism component,
    threshold disclosure vs the no-disclosure counterfactual
  * ``fig_sensitivity_panel1.pdf`` -- two-panel sensitivity (sigma_xi, delta)
  * ``fig_sensitivity_panel2.pdf`` -- three-panel sensitivity (C0, wedge, rho)
  * ``fig_noisy_rumor.pdf``        -- rumor-precision variant with a bottom legend

All other slide figures are the canonical manuscript PDFs in
``numerical_output/`` (see ``\\graphicspath`` in the deck). Per house style,
figures carry no in-figure titles: slide titles and captions do that work.

Usage:
    python -m pyfig.slide_figures [--data-dir DIR] [--output-dir DIR]
"""
from __future__ import annotations

import argparse
import os
import sys

import numpy as np
import pandas as pd

from . import style

KAPPA = r"Liquidity $\kappa$"
DMIN_SHORT = r"$\Delta^{\mathrm{min}}$"


def _csv(data_dir, name):
    return pd.read_csv(os.path.join(data_dir, name))


# ---------------------------------------------------------------------------
# Slide figure 1: disclosure attenuation in slopes
# ---------------------------------------------------------------------------
def slide_disclosure_slopes(data_dir, output_dir):
    df = (_csv(data_dir, "disclosure_attenuation.csv")
          .dropna(subset=["act_disclosure", "act_no_disclosure"])
          .sort_values("kappa"))
    k = df["kappa"].to_numpy()
    s_base = np.gradient(df["act_disclosure"].to_numpy(), k)
    s_nd = np.gradient(df["act_no_disclosure"].to_numpy(), k)

    fig, ax = style.new_ax(width=6.0, height=3.4)
    ax.axhline(0, color="black", linewidth=0.4)
    ax.plot(k, s_base, color="#4477aa", linestyle="-", linewidth=1.4,
            label="Threshold disclosure (baseline)")
    ax.plot(k, s_nd, color="#ee6677", linestyle="--", linewidth=1.4,
            label="No disclosure (counterfactual)")
    ax.fill_between(k, s_base, s_nd, color="#4477aa", alpha=0.12,
                    linewidth=0)

    # annotate the attenuation gap where it is widest
    i = int(np.argmax(np.abs(s_nd - s_base)))
    mid = 0.5 * (s_base[i] + s_nd[i])
    span = float(np.nanmax([s_base.max(), s_nd.max()])
                 - np.nanmin([s_base.min(), s_nd.min()]))
    ax.annotate("attenuation",
                xy=(k[i], mid),
                xytext=(k[i] - 0.14, mid + 0.34 * span),
                fontsize=9, color="#4477aa", ha="center",
                bbox=dict(facecolor="white", edgecolor="none",
                          alpha=0.85, pad=1.2),
                arrowprops=dict(arrowstyle="-", linewidth=0.5,
                                color="#4477aa", shrinkB=2))

    ax.set_xlabel(KAPPA)
    ax.set_ylabel(r"Slope $\partial \Delta^{\mathrm{act}} / \partial \kappa$")
    ax.legend(loc="lower left", framealpha=1.0)
    style.save_fig(fig, os.path.join(output_dir, "fig_disclosure_slopes.pdf"))


# ---------------------------------------------------------------------------
# Slide figures 2-3: multi-panel sensitivity grids
# ---------------------------------------------------------------------------
def _sensitivity_panels(data_dir, output_dir, specs, filename, figsize):
    """One row of sensitivity panels; each spec is (csv, col, fmt, subtitle)."""
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, len(specs), figsize=figsize)
    if len(specs) == 1:
        axes = [axes]
    for ax, (csv, col, fmt, subtitle) in zip(axes, specs):
        style.despine(ax)
        df = _csv(data_dir, csv)
        for i, v in enumerate(sorted(pd.unique(df[col].dropna()))):
            sub = (df[df[col] == v]
                   .dropna(subset=["Delta_min"]).sort_values("kappa"))
            if sub.empty:
                continue
            ax.plot(sub["kappa"], sub["Delta_min"],
                    color=style.SENS_COLORS[i % 4],
                    linestyle=style.SENS_LINESTYLES[i % 4],
                    marker=style.SENS_MARKERS[i % 4],
                    markersize=3, linewidth=1.2, label=fmt(v))
        ax.set_xlabel(KAPPA)
        ax.set_title(subtitle, fontsize=10)
        ax.legend(fontsize=7.5, framealpha=1.0, borderpad=0.35,
                  handlelength=1.6)
    axes[0].set_ylabel(DMIN_SHORT)
    fig.tight_layout()
    style.save_fig(fig, os.path.join(output_dir, filename))


def slide_sensitivity_panel1(data_dir, output_dir):
    _sensitivity_panels(
        data_dir, output_dir,
        [("sensitivity_sigma_xi.csv", "sigma_xi",
          lambda v: rf"$\sigma_\xi = {v:.2f}$",
          r"(a) Bidder heterogeneity $\sigma_\xi$"),
         ("sensitivity_delta.csv", "delta",
          lambda v: rf"$\delta = {v:.2f}$",
          r"(b) Discount factor $\delta$")],
        "fig_sensitivity_panel1.pdf", figsize=(9.0, 3.3))


def slide_sensitivity_panel2(data_dir, output_dir):
    _sensitivity_panels(
        data_dir, output_dir,
        [("sensitivity_C0.csv", "C0",
          lambda v: rf"$C_0 = {v:.2f}$",
          r"(a) Engagement cost $C_0$"),
         ("sensitivity_wedge.csv", "wedge",
          lambda v: rf"$m_1 - m_0 = {v:.2f}$",
          r"(b) Premium wedge $m_1 - m_0$"),
         ("sensitivity_rho.csv", "rho",
          lambda v: rf"$\rho = {v:.1f}$",
          r"(c) Engagement success $\rho$")],
        "fig_sensitivity_panel2.pdf", figsize=(11.0, 3.2))


# ---------------------------------------------------------------------------
# Slide figure 4: noisy-rumor variant with a bottom legend
# ---------------------------------------------------------------------------
def slide_noisy_rumor(data_dir, output_dir):
    df = _csv(data_dir, "noisy_rumor.csv")
    order = ["Uninformative", "Moderate", "Precise"]

    fig, ax = style.new_ax(width=6.0, height=3.5)
    for i, lab in enumerate(order):
        sub = (df[df["label"] == lab]
               .dropna(subset=["Delta_min"]).sort_values("kappa"))
        if sub.empty:
            continue
        r0 = sub.iloc[0]
        leg = rf"{lab} ($\eta_1{{=}}{r0['eta_1']:.2f}$, $\eta_0{{=}}{r0['eta_0']:.2f}$)"
        ax.plot(sub["kappa"], sub["Delta_min"],
                color=style.SENS_COLORS[i % 4],
                linestyle=style.SENS_LINESTYLES[i % 4],
                marker=style.SENS_MARKERS[i % 4],
                markersize=3.5, linewidth=1.3, label=leg)
    ax.set_xlabel(KAPPA)
    ax.set_ylabel(DMIN_SHORT)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=3,
              fontsize=7.5, frameon=False, columnspacing=1.2,
              handlelength=1.8)
    style.save_fig(fig, os.path.join(output_dir, "fig_noisy_rumor.pdf"))


ALL_SLIDE_FIGURES = [
    slide_disclosure_slopes,
    slide_sensitivity_panel1,
    slide_sensitivity_panel2,
    slide_noisy_rumor,
]


def main(argv=None):
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap = argparse.ArgumentParser(
        description="Generate slide-only EVT-model figures (Python).")
    ap.add_argument("--data-dir",
                    default=os.path.join(here, "numerical_output", "data"))
    ap.add_argument("--output-dir",
                    default=os.path.join(here, "pres", "figures"))
    args = ap.parse_args(argv)

    os.makedirs(args.output_dir, exist_ok=True)
    style.apply_style()

    print("=== EVT model: generating slide-only figures ===")
    failures = 0
    for fn in ALL_SLIDE_FIGURES:
        print(f"running {fn.__name__} ...")
        try:
            fn(args.data_dir, args.output_dir)
        except Exception as exc:
            failures += 1
            print(f"  ERROR in {fn.__name__}: {exc}")
    print(f"=== done: {len(ALL_SLIDE_FIGURES) - failures}/"
          f"{len(ALL_SLIDE_FIGURES)} slide figures generated ===")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
