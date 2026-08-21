"""T1 / O-1 re-run: the window margin in the CURRENT REPO MODEL (draft_v2).

The experiment (as committed in the v3 referee report and independently
reproduced by the v3 verifier):

  Window / timing margin -- "Public buy flagged versus pooled".
  Hold the blockholder's cutoffs FIXED at the baseline equilibrium
  (k1 = k0 = 0.82174, kD = 2.26113).  Sweep kappa over [0.15, 0.85] on a
  41-point uniform grid.  At each kappa compute the expected activism
  premium Delta^act twice:

    disclosure   (tau_w = 1) -- market sees (X, D):  compute_minority_gains
    no-disclosure(tau_w = 0) -- market sees X only:  compute_minority_gains_
                                                     no_disclosure_given_strategy

  Measure kappa-sensitivity by the total variation of Delta^act over the
  grid (and, equivalently on a uniform grid, by mean |slope|), and report
  the ratio TV_disc / TV_nodisc.  Repeat at four values of kD, i.e. four
  values of the unconditional flagged weight Omega ( = draft_v2's omega_P ):
  kD in {2.26113, 1.80, 1.40, 1.00}  ->  Omega ~ {0.037, 0.129, 0.286, 0.500}.

  A ratio > 1 means the DISCLOSED regime is MORE kappa-sensitive, i.e.
  window-margin attenuation FAILS.

Committed claim being reproduced
  quality_reports/reports/2026-08-19_framework_v3_referee_report.md:113-120
  research/review_v3/verify_theory.md:32,42-53  (independent re-execution)
  docs/adr/0007-one-theorem-two-round-model-two-lanes.md:7  (decision record)

Notation (research/model_v4/MODEL_CARD.md sec. 4.4): kappa = noise-trading
intensity; Omega = Pr(D=1) = unconditional flagged weight = draft_v2's
omega_P.  The O-1 numbers are all Omega-type, NOT omega_a (the disclosed
share of engagements).

Deterministic: no RNG, no file inputs, no network.  Everything is recomputed
from numerical/ -- in particular the exported CSV is NOT read.

Run:    .venv/bin/python quality_reports/fixes/t1_o1_rerun_check.py
Output: quality_reports/fixes/t1_o1_rerun_check.json
"""

from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from numerical.model import (  # noqa: E402
    compute_action_probabilities,
    compute_minority_gains,
    compute_minority_gains_no_disclosure_given_strategy,
)
from numerical.params import ModelParams  # noqa: E402
from numerical.solver import solve_equilibrium  # noqa: E402

OUT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "t1_o1_rerun_check.json"
)

KAPPA_MIN, KAPPA_MAX, N_GRID = 0.15, 0.85, 41
KD_GRID = [None, 1.80, 1.40, 1.00]  # None = the baseline kD, filled in below
TOL_MATCH = 5e-3  # committed ratios are quoted to 2 dp

# Committed claim, verbatim from verify_theory.md's executed table.
COMMITTED = {
    "source": (
        "quality_reports/reports/2026-08-19_framework_v3_referee_report.md:113-120 "
        "(claim); research/review_v3/verify_theory.md:32,42-53 (independent "
        "re-execution, 41-point grid)"
    ),
    "baseline_cutoffs": {"k1": 0.8217375899, "k0": 0.8217375899, "kD": 2.2611270960},
    "baseline_masses": {
        "omega_E": 0.40048,
        "omega_H": 0.0,
        "omega_Q": 0.56227,
        "Omega": 0.03725,
    },
    "rows": [
        {"kD": 2.261, "Omega": 0.0373, "TV_disc": 0.017594, "TV_nodisc": 0.016537, "ratio_TV": 1.0640},
        {"kD": 1.800, "Omega": 0.1289, "TV_disc": 0.015981, "TV_nodisc": 0.013500, "ratio_TV": 1.1837},
        {"kD": 1.400, "Omega": 0.2858, "TV_disc": 0.012110, "TV_nodisc": 0.010658, "ratio_TV": 1.1363},
        {"kD": 1.000, "Omega": 0.5000, "TV_disc": 0.003988, "TV_nodisc": 0.010550, "ratio_TV": 0.3780},
    ],
    "verdict_text": (
        "kappa-sensitivity is NOT lower under disclosure for Omega <~ 0.29; "
        "attenuation appears only at Omega = 0.50, far off calibration"
    ),
    "pointwise": "disclosure is steeper at kappa >= 0.7 for Omega <= 0.29",
    "figure_magnitude": (
        "at baseline the two plotted curves' ranges over kappa in [0.15,0.85] "
        "are 0.01107 (disc) vs 0.01117 (no-disc), a <1% difference; by mean "
        "|slope| the disclosed regime is slightly MORE sensitive (0.0251 vs 0.0236)"
    ),
}

results: dict = {"checks": [], "n_fail": 0}


def record(name: str, ok: bool, detail: dict) -> None:
    results["checks"].append({"name": name, "pass": bool(ok), **detail})
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {json.dumps(detail, default=float)}")


def sensitivity(k1: float, k0: float, kD: float, kappas: np.ndarray) -> dict:
    """Delta^act under both regimes on the kappa grid, plus TV and mean |slope|."""
    base = ModelParams()
    disc, nodisc = [], []
    for kappa in kappas:
        p = base.replace(kappa=float(kappa))
        disc.append(compute_minority_gains(k1, k0, kD, p).activism)
        nodisc.append(
            compute_minority_gains_no_disclosure_given_strategy(k1, k0, kD, p).activism
        )
    disc, nodisc = np.asarray(disc), np.asarray(nodisc)
    dk = np.diff(kappas)
    out = {}
    for name, y in (("disc", disc), ("nodisc", nodisc)):
        out[f"TV_{name}"] = float(np.abs(np.diff(y)).sum())
        out[f"meanslope_{name}"] = float(np.mean(np.abs(np.diff(y) / dk)))
        out[f"range_{name}"] = float(y.max() - y.min())
    out["ratio_TV"] = out["TV_disc"] / out["TV_nodisc"]
    out["ratio_meanslope"] = out["meanslope_disc"] / out["meanslope_nodisc"]
    out["series_disc"] = [float(x) for x in disc]
    out["series_nodisc"] = [float(x) for x in nodisc]
    return out


# ---------------------------------------------------------------------------
# 1. Baseline equilibrium: reproduce the fixed cutoffs the experiment holds.
# ---------------------------------------------------------------------------

def check_baseline() -> tuple:
    params = ModelParams()
    k1, k0, kD = solve_equilibrium(params)
    omega_E, omega_H, omega_Q, Omega = compute_action_probabilities(k1, k0, kD, params)
    c = COMMITTED["baseline_cutoffs"]
    ok = all(
        abs(a - b) < 1e-6
        for a, b in ((k1, c["k1"]), (k0, c["k0"]), (kD, c["kD"]))
    ) and abs(Omega - COMMITTED["baseline_masses"]["Omega"]) < 1e-4
    record(
        "baseline_cutoffs_and_masses",
        ok,
        {
            "k1": k1, "k0": k0, "kD": kD,
            "omega_E": omega_E, "omega_H": omega_H, "omega_Q": omega_Q,
            "Omega": Omega,
            "committed": {**c, **COMMITTED["baseline_masses"]},
            "note": "Omega = Pr(D=1) = draft_v2's omega_P; Hold region collapses (k1=k0)",
        },
    )
    return k1, k0, kD, Omega


# ---------------------------------------------------------------------------
# 2. The O-1 window-margin table.
# ---------------------------------------------------------------------------

def check_o1_table(k1: float, k0: float, kD_base: float) -> list:
    params = ModelParams()
    kappas = np.linspace(KAPPA_MIN, KAPPA_MAX, N_GRID)
    kd_values = [kD_base if kd is None else kd for kd in KD_GRID]

    rows = []
    for kd, claim in zip(kd_values, COMMITTED["rows"]):
        _, _, _, Omega = compute_action_probabilities(k1, k0, kd, params)
        s = sensitivity(k1, k0, kd, kappas)
        row = {
            "kD": float(kd),
            "Omega": float(Omega),
            "TV_disc": s["TV_disc"],
            "TV_nodisc": s["TV_nodisc"],
            "ratio_TV": s["ratio_TV"],
            "ratio_meanslope": s["ratio_meanslope"],
            "attenuation_holds": bool(s["ratio_TV"] < 1.0),
            "committed_ratio_TV": claim["ratio_TV"],
            "abs_diff_vs_committed": abs(s["ratio_TV"] - claim["ratio_TV"]),
        }
        rows.append(row)
        print(
            f"  kD={kd:6.3f}  Omega={Omega:7.4f}  TV_disc={s['TV_disc']:.6f} "
            f"TV_nodisc={s['TV_nodisc']:.6f}  ratio={s['ratio_TV']:.4f} "
            f"(committed {claim['ratio_TV']:.4f})"
        )

    ok = all(r["abs_diff_vs_committed"] < TOL_MATCH for r in rows)
    record(
        "o1_ratios_match_committed_claim",
        ok,
        {
            "grid": {"kappa_min": KAPPA_MIN, "kappa_max": KAPPA_MAX, "n": N_GRID},
            "max_abs_diff": max(r["abs_diff_vs_committed"] for r in rows),
            "tol": TOL_MATCH,
            "rows": [{k: v for k, v in r.items() if k != "series"} for r in rows],
        },
    )

    # The claim's substance: ratio > 1 for the three low-Omega rows, < 1 at 0.50.
    substantive = (
        all(r["ratio_TV"] > 1.0 for r in rows[:3]) and rows[3]["ratio_TV"] < 1.0
    )
    record(
        "o1_substance_attenuation_fails_below_Omega_029",
        substantive,
        {
            "ratios": [r["ratio_TV"] for r in rows],
            "Omega": [r["Omega"] for r in rows],
            "reading": COMMITTED["verdict_text"],
        },
    )
    return rows


# ---------------------------------------------------------------------------
# 3. Pointwise slopes: disclosure steeper at high kappa for low Omega.
# ---------------------------------------------------------------------------

def check_pointwise(k1: float, k0: float, kD_base: float) -> dict:
    params = ModelParams()
    kappas = np.linspace(KAPPA_MIN, KAPPA_MAX, N_GRID)
    kd_values = [kD_base if kd is None else kd for kd in KD_GRID]
    detail = {"claim": COMMITTED["pointwise"], "per_kD": []}
    ok = True
    for kd in kd_values:
        _, _, _, Omega = compute_action_probabilities(k1, k0, kd, params)
        s = sensitivity(k1, k0, kd, kappas)
        d = np.abs(np.diff(np.asarray(s["series_disc"])) / np.diff(kappas))
        n = np.abs(np.diff(np.asarray(s["series_nodisc"])) / np.diff(kappas))
        mid = 0.5 * (kappas[:-1] + kappas[1:])
        hi = mid >= 0.7
        steeper = bool(np.all(d[hi] > n[hi]))
        detail["per_kD"].append(
            {
                "kD": float(kd),
                "Omega": float(Omega),
                "disc_steeper_everywhere_above_kappa_0.7": steeper,
                "mean_slope_disc_hi": float(d[hi].mean()),
                "mean_slope_nodisc_hi": float(n[hi].mean()),
            }
        )
        if Omega <= 0.29 and not steeper:
            ok = False
    record("o1_pointwise_slopes_above_kappa_07", ok, detail)
    return detail


# ---------------------------------------------------------------------------
# 4. Figure magnitude at baseline (the "<1% difference" claim), 35-point grid
#    matching export_disclosure_attenuation; recomputed, not read from CSV.
# ---------------------------------------------------------------------------

def check_figure_magnitude(k1: float, k0: float, kD: float) -> dict:
    kappas = np.linspace(KAPPA_MIN, KAPPA_MAX, 35)
    s = sensitivity(k1, k0, kD, kappas)
    rel_range = abs(s["range_disc"] - s["range_nodisc"]) / s["range_nodisc"]
    d = np.asarray(s["series_disc"])
    n = np.asarray(s["series_nodisc"])
    max_rel_gap = float(np.max(np.abs(d - n) / np.abs(n)))
    ok = (
        rel_range < 0.02
        and s["meanslope_disc"] > s["meanslope_nodisc"]
        and abs(s["range_disc"] - 0.01107) < 5e-5
        and abs(s["range_nodisc"] - 0.01117) < 5e-5
    )
    detail = {
        "claim": COMMITTED["figure_magnitude"],
        "n_grid": 35,
        "range_disc": s["range_disc"],
        "range_nodisc": s["range_nodisc"],
        "relative_range_gap": float(rel_range),
        "max_pointwise_relative_gap": max_rel_gap,
        "meanslope_disc": s["meanslope_disc"],
        "meanslope_nodisc": s["meanslope_nodisc"],
        "TV_ratio_35pt": s["ratio_TV"],
    }
    record("o1b_figure_magnitude_at_baseline", ok, detail)
    return detail


# ---------------------------------------------------------------------------
# 5. Locate the sign flip.  The committed claim reports ratio > 1 at
#    Omega = 0.286 and < 1 at Omega = 0.50 and rounds the cut to "~0.29";
#    the crossing itself was never located.  Bisect on kD.
# ---------------------------------------------------------------------------

def check_crossing(k1: float, k0: float) -> dict:
    from scipy.optimize import brentq

    params = ModelParams()
    kappas = np.linspace(KAPPA_MIN, KAPPA_MAX, N_GRID)

    def f(kd: float) -> float:
        return sensitivity(k1, k0, float(kd), kappas)["ratio_TV"] - 1.0

    lo, hi = 1.0, 1.4  # f(1.4) > 0, f(1.0) < 0
    f_lo, f_hi = f(lo), f(hi)
    ok = f_lo < 0 < f_hi
    detail = {
        "bracket": [lo, hi],
        "ratio_minus_1_at_bracket": [float(f_lo), float(f_hi)],
    }
    if ok:
        kd_star = float(brentq(f, lo, hi, xtol=1e-10, rtol=1e-12))
        _, _, _, Omega_star = compute_action_probabilities(k1, k0, kd_star, params)
        detail.update(
            {
                "kD_star": kd_star,
                "Omega_star": float(Omega_star),
                "reading": (
                    "window-margin attenuation FAILS (disclosure more "
                    f"kappa-sensitive) for Omega < {Omega_star:.4f}, and HOLDS "
                    "above it; the committed claim's '~0.29' is the largest "
                    "grid point at which failure was confirmed, not the crossing"
                ),
                "committed_cut_is_a_grid_point_not_the_crossing": True,
            }
        )
    record("o1_sign_flip_located", ok, detail)
    return detail


def main() -> int:
    print("=== T1 / O-1 re-run: window margin, repo (draft_v2) model ===\n")
    k1, k0, kD, Omega = check_baseline()
    print("\n=== O-1 table: TV of Delta^act, disclosure vs no-disclosure ===")
    rows = check_o1_table(k1, k0, kD)
    print()
    pointwise = check_pointwise(k1, k0, kD)
    print()
    figmag = check_figure_magnitude(k1, k0, kD)
    print()
    crossing = check_crossing(k1, k0)

    all_pass = results["n_fail"] == 0
    reproduced = all(r["abs_diff_vs_committed"] < TOL_MATCH for r in rows)

    results["experiment"] = {
        "name": "O-1 window margin (public buy flagged vs pooled) at fixed cutoffs",
        "model": "current repo model, numerical/ package (draft_v2 static model)",
        "regimes": {
            "disclosure (tau_w = 1)": "market observes (X, D); model.compute_minority_gains",
            "no disclosure (tau_w = 0)": (
                "market observes X only; "
                "model.compute_minority_gains_no_disclosure_given_strategy"
            ),
        },
        "object": "Delta^act = expected activism-related minority takeover gain",
        "sensitivity_measure": (
            "total variation of Delta^act over the kappa grid; mean |slope| is "
            "the same number divided by (n-1)*step, so ratios coincide exactly "
            "on a uniform grid"
        ),
        "held_fixed": "blockholder cutoffs (k1, k0) at the baseline equilibrium",
        "varied": "kD, which moves Omega = Pr(D=1) = draft_v2's omega_P",
        "notation": (
            "kappa = noise-trading intensity; Omega = unconditional flagged "
            "weight (MODEL_CARD sec. 4.4); omega_a (disclosed share of "
            "engagements) is NOT what this table varies"
        ),
        "date": "2026-08-21",
    }
    results["grid"] = {
        "kappa_min": KAPPA_MIN,
        "kappa_max": KAPPA_MAX,
        "n_kappa": N_GRID,
        "kD_values": [r["kD"] for r in rows],
        "Omega_values": [r["Omega"] for r in rows],
    }
    results["numbers"] = rows
    results["committed_claim"] = COMMITTED
    results["comparison"] = {
        "reproduced": bool(reproduced),
        "tolerance": TOL_MATCH,
        "max_abs_ratio_diff": max(r["abs_diff_vs_committed"] for r in rows),
        "explained_differences": (
            [] if reproduced else ["see per-row abs_diff_vs_committed"]
        ),
        "note": (
            "Committed ratios are quoted to 4 dp in verify_theory.md and 2 dp "
            "in the referee report; the kD values 1.80/1.40/1.00 are the "
            "referee's own grid, and Omega is a deterministic function of kD "
            "at fixed (k1,k0), so Omega reproduces exactly."
        ),
    }
    results["pointwise"] = pointwise
    results["figure_magnitude"] = figmag
    results["crossing"] = crossing
    results["sign"] = {
        "d_sensitivity_d_flag": "POSITIVE at baseline",
        "plain": (
            "Flagging the public buy RAISES the liquidity-sensitivity of the "
            "expected activism premium at the paper's calibration; window-"
            "margin attenuation is FALSE at baseline in the repo model."
        ),
        "magnitude": (
            "TV ratio 1.06 at Omega=0.037 (baseline), 1.18 at 0.129, 1.14 at "
            "0.286; sign flips to 0.38 only at Omega=0.50"
        ),
        "condition": "holds for Omega <~ 0.29 at fixed cutoffs (partial equilibrium)",
    }
    results["all_pass"] = all_pass
    results["verdict"] = (
        "REPRODUCED — committed O-1 claim confirmed in the current repo model: "
        "window-margin attenuation is FALSE at baseline (TV ratio > 1 for "
        "Omega <~ 0.29), attenuation appearing only at Omega = 0.50."
        if all_pass
        else f"FAILED — {results['n_fail']} check(s) did not reproduce; see checks[]."
    )

    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    print(f"\n{results['verdict']}")
    print(f"JSON: {OUT}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
