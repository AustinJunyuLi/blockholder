"""The three figures the paper carries, from the committed records.

Figure 1 (figures/fig1_sensitivity_factors.pdf): the noise sensitivity
S = |d_kappa Delta^act| and its two factors, the pooled share 1 - Omega and
the pooled sensitivity S_P = |d_kappa M_P|, against kappa under the two
clocks at the calibration node (the median threshold quantile 0.5), from the
mark-2 T1 record numerical_v4/checks/t2_t1_check.json.  The sensitivities are
the slopes over consecutive kappa grid nodes, the convention the record's own
block 1 checks; the kappa grid is 0.15 to 0.85 in steps of 0.01, so the
curves carry no gap.

Figure 2 (figures/fig2_who_gets_caught.pdf): the who-gets-caught record
numerical_v4/checks/t5_who_gets_caught.json across its five threshold nodes:
the caught sensitivity s_B against the pool sensitivity s_A and the upper
limit ((2 - phi)/phi) s_A, and the composition ratio C_T with its ceiling of
one.  The note below the panels marks the degenerate T = 10 flagged cell.

Figure 3 (figures/e1_stake.pdf): the distribution of the stake at filing by
period, from empirics/output/e1_campaigns.csv.  The script checks its counts
and summary statistics against empirics/output/e1_estimate.json and uses the
style of empirics/fingerprints.py.

Deterministic: no RNG, no model evaluation, no network; file inputs only.

Run:    .venv/bin/python numerical_v4/checks/figures.py
Output: figures/fig1_sensitivity_factors.pdf
        figures/fig2_who_gets_caught.pdf
        figures/e1_stake.pdf
"""

from __future__ import annotations

import json
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CHECKS = HERE
FIGURES = os.path.join(REPO, "figures")

T1 = os.path.join(CHECKS, "t2_t1_check.json")
T5 = os.path.join(CHECKS, "t5_who_gets_caught.json")
E1_RESULT = os.path.join(REPO, "empirics", "output", "e1_estimate.json")
E1_TABLE = os.path.join(REPO, "empirics", "output", "e1_campaigns.csv")

# The palette and the spine discipline are empirics/fingerprints.py's.
COLOUR_SHORT, COLOUR_LONG = "#4477aa", "#ee6677"
COLOUR_NEUTRAL = "#666666"


def _finish(fig, path: str) -> None:
    # Matplotlib otherwise writes the current time into the PDF. Omitting both
    # date fields makes repeated runs byte-stable.
    metadata = {"Creator": "numerical_v4/checks/figures.py",
                "CreationDate": None, "ModDate": None}
    fig.savefig(path, metadata=metadata)
    print(f"wrote {os.path.relpath(path, REPO)}", flush=True)


def fig1() -> None:
    """S and its two factors against kappa, both clocks, calibration node."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    with open(T1) as fh:
        rec = json.load(fh)
    assert rec["provenance"]["mark"] == 2
    assert rec["grid"]["H"] == 10
    kappa = np.array(rec["grid"]["kappa"], dtype=float)
    dk = np.diff(kappa)
    np.testing.assert_allclose(kappa, np.arange(0.15, 0.851, 0.01),
                               rtol=0.0, atol=1e-12)
    q = 0.5  # the calibration node: the median threshold quantile
    omega, profiles, node_rows = {}, {}, {}
    for T in (5, 10):
        row = [r for r in rec["node_table"]
               if r["T"] == T and r["tau_quantile"] == q]
        assert len(row) == 1, "the calibration node is unique in the record"
        node_rows[T] = row[0]
        omega[T] = float(row[0]["Omega"])
        profiles[T] = rec["kappa_profiles"][f"T={T},q={q}"]
        assert all(len(profiles[T][key]) == len(kappa)
                   for key in ("Delta_act_pp", "M_P_pp"))
    assert node_rows[10]["corner"] is True
    assert any("flagged cell mass" in item
               for item in node_rows[10]["degenerate"])

    mid = 0.5 * (kappa[:-1] + kappa[1:])
    sens = {T: {obj: np.abs(np.diff(np.array(profiles[T][key], dtype=float)) / dk)
                for obj, key in (("S", "Delta_act_pp"), ("S_P", "M_P_pp"))}
            for T in (5, 10)}

    fig, (ax, axr) = plt.subplots(
        1, 2, figsize=(8.6, 3.4), sharex=True,
    )
    for axis in (ax, axr):
        axis.spines[["top", "right"]].set_visible(False)
        axis.set_xlabel(r"Liquidity $\kappa$")
        axis.set_xlim(kappa[0], kappa[-1])
        axis.set_xticks(np.arange(0.2, 0.9, 0.1))

    ax.plot(mid, sens[5]["S"], color=COLOUR_SHORT,
            label=r"$T = 5$")
    ax.plot(mid, sens[10]["S"], color=COLOUR_LONG,
            label="$T = 10$ (corner $T = H$;\n"
                  "degenerate flagged cell)")
    ax.set_yscale("log")
    ax.set_ylabel(r"$S$ (premium pp per unit $\kappa$)")
    ax.set_title("Noise sensitivity", fontsize=10)
    ax.legend(fontsize=8, frameon=False)

    axr.plot(mid, sens[5]["S_P"], color=COLOUR_SHORT, label=r"$S_P$, $T = 5$")
    axr.plot(mid, sens[10]["S_P"], color=COLOUR_LONG, label=r"$S_P$, $T = 10$")
    axr.set_yscale("log")
    axr.set_ylabel(r"$S_P$ (premium pp per unit $\kappa$)")
    axr.set_title("The two factors", fontsize=10)
    axr.legend(fontsize=8, frameon=False, loc="lower right")
    share = axr.twinx()
    share.set_ylim(0.90, 1.005)
    share.spines[["top"]].set_visible(False)
    for T, colour in ((5, COLOUR_SHORT), (10, COLOUR_LONG)):
        share.axhline(1.0 - omega[T], color=colour, linestyle=":", lw=1.2)
    share.set_ylabel(r"Pooled share $1 - \Omega$")
    share.annotate(r"$1-\Omega$, $T=5$", (kappa[2], 1 - omega[5]),
                   xytext=(0, -9), textcoords="offset points",
                   fontsize=8, color=COLOUR_SHORT)
    share.annotate(r"$1-\Omega$, $T=10$", (kappa[2], 1 - omega[10]),
                   xytext=(0, 4), textcoords="offset points",
                   fontsize=8, color=COLOUR_LONG)

    fig.suptitle("Noise sensitivity and its two factors at the calibration",
                 fontsize=11)
    fig.tight_layout()
    _finish(fig, os.path.join(FIGURES, "fig1_sensitivity_factors.pdf"))
    plt.close(fig)


def fig2() -> None:
    """The who-gets-caught record across its five threshold nodes."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    with open(T5) as fh:
        rec = json.load(fh)
    assert rec["provenance"]["mark"] == 2
    assert rec["provenance"]["H"] == 10
    assert rec["provenance"]["windows"] == {"T_long": 10, "T_short": 5}
    nodes = rec["nodes"]
    assert len(nodes) == 5
    assert all(n["corollary_condition_holds"] and n["C_T_le_1"]
               for n in nodes)
    assert all(n["T_long"] == 10 and n["T_short"] == 5 for n in nodes)
    assert all(n["Omega_T10"] < 0.01 for n in nodes)
    assert all(n.get("corner_T10_equals_H", True) for n in nodes)
    assert all(any("flagged cell mass" in item
                   for item in n.get("degenerate_T10", ["flagged cell mass"]))
               for n in nodes)
    q = np.array([n["tau_quantile"] for n in nodes])
    s_A = np.array([n["s_A"] for n in nodes])
    s_B = np.array([n["s_B"] for n in nodes])
    upper = np.array([n["upper_limit_b"] for n in nodes]) * s_A
    C_T = np.array([n["C_T"] for n in nodes])

    fig, (ax, axr) = plt.subplots(1, 2, figsize=(8.6, 3.4))
    for axis in (ax, axr):
        axis.spines[["top", "right"]].set_visible(False)
        axis.set_xlabel(r"Threshold quantile of the $\tau$ ladder")
        axis.set_xticks(q)

    ax.plot(q, s_A, "o-", color=COLOUR_NEUTRAL, label=r"$s_A$")
    ax.plot(q, upper, "^--", color=COLOUR_NEUTRAL, mfc="none",
            label=r"$((2-\varphi)/\varphi)\,s_A$")
    ax.plot(q, s_B, "s-", color=COLOUR_SHORT, label=r"$s_B$")
    ax.set_yscale("log")
    ax.set_ylabel(r"$\kappa$-derivative of the kernel expectation")
    ax.set_title("The caught sensitivity inside its band", fontsize=10)
    ax.legend(fontsize=8, frameon=False, loc="center left")

    axr.plot(q, C_T, "s-", color=COLOUR_SHORT, label=r"$C_T$")
    axr.axhline(1.0, color=COLOUR_NEUTRAL, linestyle=":", lw=1.2)
    axr.annotate("one", (q[-1], 1.0), xytext=(-6, 5),
                 textcoords="offset points", ha="right",
                 fontsize=8, color=COLOUR_NEUTRAL)
    axr.set_ylabel(r"Composition ratio $C_T$")
    axr.set_ylim(0.0, 1.15)
    axr.set_title("The composition ratio", fontsize=10)
    axr.legend(fontsize=8, frameon=False, loc="lower right")

    fig.suptitle("Who gets caught at five threshold nodes", fontsize=11)
    fig.text(0.5, 0.01,
             r"$T = 10 = H$: the flagged cell is degenerate at every node.",
             ha="center", fontsize=8, color=COLOUR_NEUTRAL)
    fig.tight_layout(rect=(0.0, 0.06, 1.0, 0.95))
    _finish(fig, os.path.join(FIGURES, "fig2_who_gets_caught.pdf"))
    plt.close(fig)


def fig_e1() -> None:
    """The E1 figure: distribution of B^F by period, fingerprints style."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    with open(E1_RESULT) as fh:
        rec = json.load(fh)
    assert rec["exercise"] == "e1" and rec["status"] == "GO"
    sample = pd.read_csv(E1_TABLE)
    sample = sample[sample["stake"].notna()]

    fig, ax = plt.subplots(figsize=(5.5, 3.4))
    bins = np.arange(0, 52, 2.0)
    for period, colour in (("pre", COLOUR_SHORT), ("post", COLOUR_LONG)):
        v = sample.loc[sample["period"] == period, "stake"].to_numpy(dtype=float)
        reported = rec["by_period"][period]
        assert len(v) == reported["n"]
        assert np.isclose(np.mean(v), reported["mean"])
        assert np.isclose(np.median(v), reported["median"])
        assert np.isclose(np.quantile(v, 0.25), reported["p25"])
        assert np.isclose(np.quantile(v, 0.75), reported["p75"])
        ax.hist(np.clip(v, 0, 50), bins=bins, density=True, alpha=0.55,
                color=colour, label=f"{period} (n={reported['n']})")
    ax.set_xlabel("Stake at filing, percent of class (above 50 clipped)")
    ax.set_ylabel("Density")
    ax.set_title("The stake at filing, before and after the clock moved",
                 fontsize=10)
    ax.legend(fontsize=8, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    _finish(fig, os.path.join(FIGURES, "e1_stake.pdf"))
    plt.close(fig)


def main() -> int:
    os.makedirs(FIGURES, exist_ok=True)
    fig1()
    fig2()
    fig_e1()
    return 0


if __name__ == "__main__":
    sys.exit(main())
