"""Plotting theme (Paul Tol palette + publication defaults).

The goal is clean, journal-ready vector PDFs without chartjunk.
Matches the R/ggplot2 publication standard: serif fonts, Paul Tol muted
palette, thin lines, light grid, consistent sizing.
"""

from __future__ import annotations

from typing import Dict, List

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------------------------
# Paul Tol (muted) palette — colourblind-friendly
# ---------------------------------------------------------------------------

ACTION_COLORS: Dict[str, str] = {
    "Exit": "#C9A0DC",        # soft lavender
    "Hold": "#9999B8",        # muted gray-purple
    "Quiet Voice": "#6B3FA0", # UCL mid purple
    "Public Voice": "#361A54",# UCL dark purple
}

SENSITIVITY_COLORS: List[str] = [
    "#361A54",  # UCL dark purple
    "#993BFF",  # UCL bright purple
    "#C77CFF",  # light violet
    "#6B3FA0",  # UCL mid purple
]

# Single-line color for figures with one primary series
PRIMARY_COLOR: str = "#6B3FA0"  # UCL mid purple

# ---------------------------------------------------------------------------
# Default figure dimensions (inches) — matches R output
# ---------------------------------------------------------------------------

FIG_WIDTH: float = 5.5
FIG_HEIGHT: float = 3.8


def setup_theme() -> None:
    """Apply global matplotlib/seaborn styling.

    Font hierarchy mirrors the R theme (``base_family = "serif"``):
    - Title / axis labels: 12 pt  (R ``rel(1.09)`` of 11 ≈ 12)
    - Tick labels / legend: 10 pt (R ``rel(0.91)`` of 11 ≈ 10)
    """
    sns.set_theme(context="paper", style="whitegrid")

    mpl.rcParams.update({
        # --- Font ---
        "font.family": "serif",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 12,
        "legend.fontsize": 10,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        # --- Lines ---
        "lines.linewidth": 1.0,
        # --- Grid (R grey85 = #d9d9d9) ---
        "grid.color": "#d9d9d9",
        "grid.alpha": 0.5,
        # --- Spines ---
        "axes.spines.top": False,
        "axes.spines.right": False,
        # --- Export ---
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "pdf.fonttype": 42,      # TrueType fonts in PDF
        "ps.fonttype": 42,
    })


def save_figure(fig: plt.Figure, path: str, width: float, height: float) -> None:
    """Save a figure as vector PDF with consistent sizing."""
    fig.set_size_inches(width, height)
    fig.tight_layout()
    # Make both figure and axes backgrounds transparent so figures
    # blend with any slide/document background color.
    fig.patch.set_alpha(0.0)
    for ax in fig.get_axes():
        ax.patch.set_alpha(0.0)
    fig.savefig(path, format="pdf", bbox_inches="tight", transparent=True)
    plt.close(fig)
