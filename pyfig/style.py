"""Shared matplotlib style, palette, and helpers for EVT-model figures.

Editorial-minimal, publication-grade house style:
  * Computer-Modern math typography (mathtext 'cm') to match the XeLaTeX manuscript
  * Paul Tol muted, colourblind-safe palette (action + sensitivity systems)
  * despined axes, restrained grid, vector PDF with embedded fonts
"""
from __future__ import annotations

import matplotlib as mpl

mpl.use("pdf")  # headless, vector output
import matplotlib.pyplot as plt  # noqa: E402

# -- Palette (Paul Tol muted) ------------------------------------------------
COL_EXIT = "#cc6677"    # rose
COL_HOLD = "#ddcc77"    # sand
COL_QUIET = "#88ccee"   # cyan
COL_PUBLIC = "#44aa99"  # teal

ACTION_COLORS = {
    "Exit": COL_EXIT,
    "Hold": COL_HOLD,
    "Quiet Voice": COL_QUIET,
    "Public Voice": COL_PUBLIC,
}

# Sensitivity / multi-series system
SENS_COLORS = ["#4477aa", "#ee6677", "#228833", "#ccbb44"]
SENS_LINESTYLES = ["-", "--", "-.", ":"]
SENS_MARKERS = ["o", "s", "^", "D"]

# Neutral accents
GRID_GREY = "#D9D9D9"
REF_GREY = "#8c8c8c"

FIG_WIDTH, FIG_HEIGHT, FIG_DPI = 5.5, 3.8, 300


def apply_style() -> None:
    """Install the global rcParams house style. Call once before plotting."""
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": ["CMU Serif", "Latin Modern Roman", "DejaVu Serif",
                       "Times New Roman"],
        "mathtext.fontset": "cm",
        "axes.unicode_minus": True,
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.titleweight": "normal",
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 9.0,
        "axes.linewidth": 0.4,
        "axes.edgecolor": "black",
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": GRID_GREY,
        "grid.linewidth": 0.3,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.major.width": 0.4,
        "ytick.major.width": 0.4,
        "legend.frameon": True,
        "legend.edgecolor": "#cccccc",
        "legend.framealpha": 1.0,
        "legend.fancybox": False,
        "legend.borderpad": 0.5,
        "figure.dpi": 110,
        "savefig.dpi": FIG_DPI,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.05,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })


def new_ax(width: float = FIG_WIDTH, height: float = FIG_HEIGHT):
    """Return (fig, ax) with the house despined style applied."""
    fig, ax = plt.subplots(figsize=(width, height))
    despine(ax)
    return fig, ax


def despine(ax) -> None:
    """Remove top/right spines; restrained left/bottom spines + major grid."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_linewidth(0.4)
    ax.grid(True, which="major", color=GRID_GREY, linewidth=0.3)
    ax.set_axisbelow(True)


def legend_outside(ax, **kwargs):
    """Legend placed just outside the right edge (matches the old ggplot 'right')."""
    return ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5),
                     borderaxespad=0.0, **kwargs)


def save_fig(fig, path: str) -> None:
    fig.savefig(path)
    plt.close(fig)
    print(f"  saved {path}")
