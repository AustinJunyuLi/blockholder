# Python Export and Acceleration Modules

> **NOTE on `accel.py`:** This is the Numba JIT accelerated version of the solver
> that is **CURRENTLY DISABLED** (`HAS_NUMBA = False` in `solver.py`). It has NOT
> been updated to match the new theory fixes applied to `model.py` and `solver.py`.
> Specifically, the following changes from the "theory fixes" bundle are missing
> from `accel.py`:
>
> 1. **Noise distribution** -- `accel.py` still uses the old `p0 = 1 - kappa`,
>    `p1 = kappa/2` parametrisation. The new theory uses `p0 = 1 - 2*kappa/3`,
>    `p1 = kappa/3`.
> 2. **Bid probability** -- `accel.py` still couples bid probability to price P
>    via `T = (m + K - S_bar + P) / sigma_xi`. The new theory decouples it:
>    `T = (m + K - S_bar) / sigma_xi`.
> 3. **Direct pricing** -- `accel.py` still uses fixed-point iteration to solve
>    for prices. The new theory uses a direct formula since bid probability no
>    longer depends on P.
> 4. **Bidder arrival rate** -- `accel.py` does not incorporate `lambda_B`.
>    The new theory multiplies all bid probabilities by `lambda_B`.
>
> The `accel.py` module needs to be updated to match these changes before it can
> be re-enabled.

---

## File: `numerical/export_data.py`

```python
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
    noise_probs,
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
        ["lambda_B", _fmt(params.lambda_B)],
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
    prices, _ = compute_equilibrium_prices(k1, k0, kD, params)
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)

    p0, p1 = noise_probs(params.kappa)

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
        p_bid = params.lambda_B * bid_probability(m_XD, params) if np.isfinite(P) else float("nan")
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
        p_bid = params.lambda_B * bid_probability(m_XD, params) if np.isfinite(P) else float("nan")
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
    prices, _ = compute_equilibrium_prices(k1, k0, kD, params)

    def row_for(X: int, D: int) -> str:
        P = prices.get((X, D), np.nan)
        pi = posteriors.get((X, D), 0.0)
        m_XD = params.m0 + (params.m_tilde - params.m0) * pi
        p_bid = params.lambda_B * bid_probability(m_XD, params) if np.isfinite(P) else np.nan
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
```

---

## File: `numerical/accel.py`

```python
"""
Numba-JIT accelerated equilibrium solver for the Exit-Voice-Takeover model.

Drop-in replacement for ``numerical.solver.solve_equilibrium`` and
``numerical.solver.compute_series_over_kappa``.  All mathematical operations
are identical to the pure-Python implementation; only the execution strategy
differs — the entire solver loop (including bisection root-finding) is
compiled to native code via ``@numba.njit``.

Key design decisions:
    - scipy.stats.norm replaced by math.erfc/exp implementations
    - Dictionaries replaced by fixed-size arrays with a canonical index layout
    - ModelParams flattened to plain float arguments for Numba compatibility
    - Bisection root-finding replaces scipy.optimize.brentq

Posterior / price array index layout (7 feasible (X,D) states):
    0: (-2, 0)   1: (-1, 0)   2: (0, 0)   3: (1, 0)
    4: (0, 1)    5: (1, 1)    6: (2, 1)
"""

from __future__ import annotations

import math
from typing import Dict, Optional

import numba
import numpy as np

from numerical.params import Cutoffs, MinorityGains, ModelParams, TOL_CONVERGE, TOL_PROB

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_SQRT2 = math.sqrt(2.0)
_INV_SQRT2PI = 1.0 / math.sqrt(2.0 * math.pi)

# (X, D) -> array index mapping (used in Python wrapper code only)
POSTERIOR_INDICES = {
    (-2, 0): 0,
    (-1, 0): 1,
    (0, 0): 2,
    (1, 0): 3,
    (0, 1): 4,
    (1, 1): 5,
    (2, 1): 6,
}

# ---------------------------------------------------------------------------
# Elementary math (Numba-compatible replacements for scipy.stats.norm)
# ---------------------------------------------------------------------------


@numba.njit(cache=True)
def _norm_cdf(x: float) -> float:
    """Standard normal CDF via erfc."""
    return 0.5 * math.erfc(-x / _SQRT2)


@numba.njit(cache=True)
def _norm_pdf(x: float) -> float:
    """Standard normal PDF."""
    return math.exp(-0.5 * x * x) * _INV_SQRT2PI


# ---------------------------------------------------------------------------
# Model primitives
# ---------------------------------------------------------------------------


@numba.njit(cache=True)
def _engagement_cost(s: float, mu: float, sigma_s: float,
                     C0: float, chi: float) -> float:
    """C(s) = C0 * exp(-chi * z), z = (s - mu) / sigma_s."""
    z = (s - mu) / sigma_s
    return C0 * math.exp(-chi * z)


@numba.njit(cache=True)
def _v_hat(s: float, mu: float, beta: float) -> float:
    """Posterior mean: v_hat = mu + beta * (s - mu)."""
    return mu + beta * (s - mu)


# ---------------------------------------------------------------------------
# Action probabilities and conditional means
# ---------------------------------------------------------------------------


@numba.njit(cache=True)
def _compute_action_probs(k1: float, k0: float, kD: float,
                          mu: float, sigma_s: float):
    """Returns (omega_E, omega_H, omega_Q, omega_P)."""
    a1 = (k1 - mu) / sigma_s
    a0 = (k0 - mu) / sigma_s
    aD = (kD - mu) / sigma_s

    omega_E = _norm_cdf(a1)
    omega_H = _norm_cdf(a0) - _norm_cdf(a1)
    omega_Q = _norm_cdf(aD) - _norm_cdf(a0)
    omega_P = 1.0 - _norm_cdf(aD)

    if omega_E < 0.0:
        omega_E = 0.0
    if omega_H < 0.0:
        omega_H = 0.0
    if omega_Q < 0.0:
        omega_Q = 0.0
    if omega_P < 0.0:
        omega_P = 0.0

    return omega_E, omega_H, omega_Q, omega_P


@numba.njit(cache=True)
def _compute_conditional_means(k1: float, k0: float, kD: float,
                               mu: float, sigma_s: float, beta: float):
    """Returns (mu_E, mu_H, mu_Q, mu_P)."""
    a1 = (k1 - mu) / sigma_s
    a0 = (k0 - mu) / sigma_s
    aD = (kD - mu) / sigma_s

    TOL = 1e-10

    # Exit: s < k1
    cdf_a1 = _norm_cdf(a1)
    if cdf_a1 < TOL:
        lambda_L = -a1
    else:
        lambda_L = _norm_pdf(a1) / cdf_a1
    mu_E = mu - beta * sigma_s * lambda_L

    # Hold: k1 <= s < k0
    denom_H = _norm_cdf(a0) - _norm_cdf(a1)
    if denom_H > TOL:
        mu_H = mu + beta * sigma_s * (_norm_pdf(a1) - _norm_pdf(a0)) / denom_H
    else:
        mu_H = mu + beta * (k0 + k1) / 2.0 - beta * mu

    # Quiet Voice: k0 <= s < kD
    denom_Q = _norm_cdf(aD) - _norm_cdf(a0)
    if denom_Q > TOL:
        mu_Q = mu + beta * sigma_s * (_norm_pdf(a0) - _norm_pdf(aD)) / denom_Q
    else:
        mu_Q = mu + beta * (kD + k0) / 2.0 - beta * mu

    # Public Voice: s >= kD
    ccdf_aD = 1.0 - _norm_cdf(aD)
    if ccdf_aD < TOL:
        lambda_U = aD
    else:
        lambda_U = _norm_pdf(aD) / ccdf_aD
    mu_P = mu + beta * sigma_s * lambda_U

    return mu_E, mu_H, mu_Q, mu_P


# ---------------------------------------------------------------------------
# Posteriors — stored in a length-7 array
# ---------------------------------------------------------------------------


@numba.njit(cache=True)
def _compute_posteriors(omega_E: float, omega_H: float,
                        omega_Q: float, omega_P: float,
                        kappa: float):
    """Returns length-7 array of pi(X,D).

    Index layout:
        0: (-2,0)  1: (-1,0)  2: (0,0)  3: (1,0)
        4: (0,1)   5: (1,1)   6: (2,1)
    """
    TOL = 1e-10
    pi = np.zeros(7)

    p0 = 1.0 - kappa
    p1 = kappa / 2.0

    # D=1 states: engagement is known
    pi[4] = 1.0  # (0,1)
    pi[5] = 1.0  # (1,1)
    pi[6] = 1.0  # (2,1)

    # (-2,0): only Exit
    pi[0] = 0.0

    # (1,0): Hold or QuietVoice with z=+1
    denom_1 = omega_H + omega_Q
    if denom_1 > TOL:
        pi[3] = omega_Q / denom_1
    else:
        pi[3] = 0.0

    # (-1,0): Hold/QuietVoice with z=-1, or Exit with z=0
    denom_m1 = (omega_H + omega_Q) * p1 + omega_E * p0
    if denom_m1 > TOL:
        pi[1] = omega_Q * p1 / denom_m1
    else:
        pi[1] = 0.0

    # (0,0): Hold/QuietVoice with z=0, or Exit with z=+1
    denom_0 = (omega_H + omega_Q) * p0 + omega_E * p1
    if denom_0 > TOL:
        pi[2] = omega_Q * p0 / denom_0
    else:
        pi[2] = 0.0

    return pi


# ---------------------------------------------------------------------------
# E[v | X, D]
# ---------------------------------------------------------------------------


@numba.njit(cache=True)
def _compute_E_v_given_XD(X: int, D: int,
                          omega_E: float, omega_H: float,
                          omega_Q: float, omega_P: float,
                          mu_E: float, mu_H: float,
                          mu_Q: float, mu_P: float,
                          kappa: float) -> float:
    """Conditional expectation E[v | X, D]."""
    TOL = 1e-10
    p0 = 1.0 - kappa
    p1 = kappa / 2.0

    if D == 1:
        return mu_P

    if X == -2:
        return mu_E
    elif X == 1:
        denom = omega_H + omega_Q
        if denom < TOL:
            return (mu_H + mu_Q) / 2.0
        return (omega_H * mu_H + omega_Q * mu_Q) / denom
    elif X == -1:
        denom = (omega_H + omega_Q) * p1 + omega_E * p0
        if denom < TOL:
            return (mu_H + mu_Q + mu_E) / 3.0
        return ((omega_H * mu_H + omega_Q * mu_Q) * p1 +
                omega_E * mu_E * p0) / denom
    else:  # X == 0
        denom = (omega_H + omega_Q) * p0 + omega_E * p1
        if denom < TOL:
            return (mu_H + mu_Q + mu_E) / 3.0
        return ((omega_H * mu_H + omega_Q * mu_Q) * p0 +
                omega_E * mu_E * p1) / denom


# ---------------------------------------------------------------------------
# Bid probability and price fixed point
# ---------------------------------------------------------------------------


@numba.njit(cache=True)
def _bid_probability(P: float, m_XD: float,
                     S_bar: float, K: float, sigma_xi: float) -> float:
    """Bid probability: 1 - Phi(T), T = (m + K - S_bar + P) / sigma_xi."""
    T = (m_XD + K - S_bar + P) / sigma_xi
    return 1.0 - _norm_cdf(T)


@numba.njit(cache=True)
def _solve_price_fixed_point(E_v_XD: float, pi_XD: float,
                             m0: float, m_tilde: float,
                             Delta_tilde: float, delta: float,
                             S_bar: float, K: float,
                             sigma_xi: float) -> float:
    """Solve P(X,D) via fixed-point iteration (Eq. 9)."""
    V_hat = E_v_XD + Delta_tilde * pi_XD
    m_XD = m0 + (m_tilde - m0) * pi_XD

    P = delta * V_hat

    for _ in range(100):
        p = _bid_probability(P, m_XD, S_bar, K, sigma_xi)
        P_new = delta * ((1.0 - p) * V_hat + p * (P + m_XD))
        if abs(P_new - P) < 1e-8:
            return P_new
        P = P_new

    return P


# ---------------------------------------------------------------------------
# Equilibrium prices — length-7 array
# ---------------------------------------------------------------------------

# X_VALUES[i] and D_VALUES[i] give the (X,D) pair at index i
_X_VALUES = np.array([-2, -1, 0, 1, 0, 1, 2], dtype=np.int64)
_D_VALUES = np.array([0, 0, 0, 0, 1, 1, 1], dtype=np.int64)


@numba.njit(cache=True)
def _compute_equilibrium_prices(k1: float, k0: float, kD: float,
                                mu: float, sigma_s: float, beta: float,
                                kappa: float, m0: float, m_tilde: float,
                                Delta_tilde: float, delta: float,
                                S_bar: float, K: float,
                                sigma_xi: float):
    """Compute prices for all 7 (X,D) states. Returns (prices, posteriors, omegas, mus)."""
    omega_E, omega_H, omega_Q, omega_P = _compute_action_probs(
        k1, k0, kD, mu, sigma_s)
    mu_E, mu_H, mu_Q, mu_P = _compute_conditional_means(
        k1, k0, kD, mu, sigma_s, beta)
    pi = _compute_posteriors(omega_E, omega_H, omega_Q, omega_P, kappa)

    prices = np.zeros(7)
    for i in range(7):
        X = _X_VALUES[i]
        D = _D_VALUES[i]
        E_v = _compute_E_v_given_XD(
            X, D, omega_E, omega_H, omega_Q, omega_P,
            mu_E, mu_H, mu_Q, mu_P, kappa)
        prices[i] = _solve_price_fixed_point(
            E_v, pi[i], m0, m_tilde, Delta_tilde, delta,
            S_bar, K, sigma_xi)

    return prices, pi, omega_E, omega_H, omega_Q, omega_P, mu_E, mu_H, mu_Q, mu_P


# ---------------------------------------------------------------------------
# Expected payoffs
# ---------------------------------------------------------------------------

# Action indices: 0=EXIT, 1=HOLD, 2=QUIET, 3=PUBLIC
_ACTION_EXIT = 0
_ACTION_HOLD = 1
_ACTION_QUIET = 2
_ACTION_PUBLIC = 3


@numba.njit(cache=True)
def _get_price(prices: np.ndarray, X: int, D: int, mu: float) -> float:
    """Look up price by (X,D) using the canonical index mapping."""
    # Map (X,D) -> index
    if D == 0:
        if X == -2:
            return prices[0]
        elif X == -1:
            return prices[1]
        elif X == 0:
            return prices[2]
        elif X == 1:
            return prices[3]
    else:  # D == 1
        if X == 0:
            return prices[4]
        elif X == 1:
            return prices[5]
        elif X == 2:
            return prices[6]
    return mu  # fallback


@numba.njit(cache=True)
def _get_pi(posteriors: np.ndarray, X: int, D: int) -> float:
    """Look up posterior by (X,D)."""
    if D == 0:
        if X == -2:
            return posteriors[0]
        elif X == -1:
            return posteriors[1]
        elif X == 0:
            return posteriors[2]
        elif X == 1:
            return posteriors[3]
    else:
        if X == 0:
            return posteriors[4]
        elif X == 1:
            return posteriors[5]
        elif X == 2:
            return posteriors[6]
    return 0.0


@numba.njit(cache=True)
def _compute_expected_payoff(action_idx: int, s: float,
                             prices: np.ndarray, posteriors: np.ndarray,
                             mu: float, beta: float, sigma_s: float,
                             kappa: float, C0: float, chi: float,
                             m0: float, m_tilde: float,
                             Delta_tilde: float, delta: float,
                             S_bar: float, K: float,
                             sigma_xi: float) -> float:
    """Expected payoff for a given action (0=E, 1=H, 2=Q, 3=P) and signal s."""
    p0 = 1.0 - kappa
    p1 = kappa / 2.0
    v_post = _v_hat(s, mu, beta)

    if action_idx == _ACTION_EXIT:
        # q = -1, a = 0, h = 0 -> sell 1 share, receive P(X,0)
        # X = -1 + z
        payoff = 0.0
        for iz in range(3):
            z = iz - 1  # -1, 0, 1
            pz = p1 if z != 0 else p0
            X = -1 + z
            P = _get_price(prices, X, 0, mu)
            payoff += pz * P
        return payoff

    elif action_idx == _ACTION_HOLD:
        # q = 0, a = 0, h = 1 -> X = z
        payoff = 0.0
        for iz in range(3):
            z = iz - 1
            pz = p1 if z != 0 else p0
            X = z
            P = _get_price(prices, X, 0, mu)
            pi_XD = _get_pi(posteriors, X, 0)
            m_XD = m0 + (m_tilde - m0) * pi_XD
            p_bid = _bid_probability(P, m_XD, S_bar, K, sigma_xi)
            expected_terminal = p_bid * (P + m0) + (1.0 - p_bid) * v_post
            payoff += pz * delta * expected_terminal
        return payoff

    elif action_idx == _ACTION_QUIET:
        # q = 0, a = 1, h = 1 -> X = z, D = 0
        C = _engagement_cost(s, mu, sigma_s, C0, chi)
        payoff = -C
        for iz in range(3):
            z = iz - 1
            pz = p1 if z != 0 else p0
            X = z
            P = _get_price(prices, X, 0, mu)
            pi_XD = _get_pi(posteriors, X, 0)
            m_XD = m0 + (m_tilde - m0) * pi_XD
            p_bid = _bid_probability(P, m_XD, S_bar, K, sigma_xi)
            expected_terminal = (p_bid * (P + m_tilde) +
                                 (1.0 - p_bid) * (v_post + Delta_tilde))
            payoff += pz * delta * expected_terminal
        return payoff

    else:  # PUBLIC
        # q = +1, a = 1, h = 2, D = 1 -> X = 1 + z
        C = _engagement_cost(s, mu, sigma_s, C0, chi)
        payoff = -C
        for iz in range(3):
            z = iz - 1
            pz = p1 if z != 0 else p0
            X = 1 + z
            P = _get_price(prices, X, 1, mu)
            p_bid = _bid_probability(P, m_tilde, S_bar, K, sigma_xi)
            trading_cf = -P
            expected_terminal = (p_bid * 2.0 * (P + m_tilde) +
                                 (1.0 - p_bid) * 2.0 * (v_post + Delta_tilde))
            payoff += pz * (trading_cf + delta * expected_terminal)
        return payoff


# ---------------------------------------------------------------------------
# Bisection root finder (replaces scipy.optimize.brentq)
# ---------------------------------------------------------------------------


@numba.njit(cache=True)
def _bisect(func_vals: np.ndarray, grid: np.ndarray,
            target: float) -> tuple:
    """Find the sign-change bracket closest to target.

    Returns (found, a, b) where found is True if a bracket exists.
    """
    n = len(grid)
    best_a = 0.0
    best_b = 0.0
    best_dist = 1e30
    found = False

    for i in range(n - 1):
        if math.isnan(func_vals[i]) or math.isnan(func_vals[i + 1]):
            continue
        if func_vals[i] == 0.0:
            mid = grid[i]
            dist = abs(mid - target)
            if not found or dist < best_dist:
                best_a = grid[i]
                best_b = grid[i]
                best_dist = dist
                found = True
        elif func_vals[i] * func_vals[i + 1] < 0.0:
            mid = (grid[i] + grid[i + 1]) / 2.0
            dist = abs(mid - target)
            if not found or dist < best_dist:
                best_a = grid[i]
                best_b = grid[i + 1]
                best_dist = dist
                found = True

    return found, best_a, best_b


@numba.njit(cache=True)
def _brentq(f_a: float, f_b: float, a: float, b: float,
            func_id: int, s_grid: np.ndarray,
            prices: np.ndarray, posteriors: np.ndarray,
            mu: float, beta: float, sigma_s: float,
            kappa: float, C0: float, chi: float,
            m0: float, m_tilde: float,
            Delta_tilde: float, delta: float,
            S_bar: float, K: float, sigma_xi: float) -> float:
    """Brent's method for root finding within [a, b].

    func_id: 0 = diff_E_best0, 1 = diff_H_Q, 2 = diff_lower_P (Quiet),
             3 = diff_lower_P (Hold).

    Follows the SciPy/Numerical Recipes formulation where:
    - b is always the current best estimate
    - a is the previous best estimate
    - c is the contrapoint (f(c) has opposite sign from f(b))
    """
    tol = 1e-12
    max_iter = 100

    fa = f_a
    fb = f_b

    # c is the contrapoint — must have opposite sign from b
    c = a
    fc = fa
    d = b - a
    e = b - a

    for _ in range(max_iter):
        # Ensure c is the contrapoint (opposite sign from b)
        if fb * fc > 0.0:
            c = a
            fc = fa
            d = b - a
            e = b - a

        # Make b the better approximation
        if abs(fc) < abs(fb):
            a = b
            b = c
            c = a
            fa = fb
            fb = fc
            fc = fa

        tol1 = 2.0 * 2.2e-16 * abs(b) + 0.5 * tol
        m = 0.5 * (c - b)

        if abs(m) <= tol1 or fb == 0.0:
            return b

        if abs(e) >= tol1 and abs(fa) > abs(fb):
            # Try inverse quadratic interpolation
            s_val = fb / fa
            if a == c:
                # Linear interpolation (secant)
                p = 2.0 * m * s_val
                q = 1.0 - s_val
            else:
                # Inverse quadratic interpolation
                q = fa / fc
                r = fb / fc
                p = s_val * (2.0 * m * q * (q - r) - (b - a) * (r - 1.0))
                q = (q - 1.0) * (r - 1.0) * (s_val - 1.0)

            if p > 0.0:
                q = -q
            else:
                p = -p

            if 2.0 * p < min(3.0 * m * q - abs(tol1 * q), abs(e * q)):
                e = d
                d = p / q
            else:
                d = m
                e = m
        else:
            d = m
            e = m

        a = b
        fa = fb

        if abs(d) > tol1:
            b = b + d
        else:
            if m > 0.0:
                b = b + tol1
            else:
                b = b - tol1

        # Evaluate function at new b
        fb = _eval_diff(func_id, b, prices, posteriors,
                        mu, beta, sigma_s, kappa, C0, chi,
                        m0, m_tilde, Delta_tilde, delta,
                        S_bar, K, sigma_xi)

    return b


@numba.njit(cache=True)
def _eval_diff(func_id: int, s: float,
               prices: np.ndarray, posteriors: np.ndarray,
               mu: float, beta: float, sigma_s: float,
               kappa: float, C0: float, chi: float,
               m0: float, m_tilde: float,
               Delta_tilde: float, delta: float,
               S_bar: float, K: float, sigma_xi: float) -> float:
    """Evaluate the difference function identified by func_id at signal s."""
    args = (s, prices, posteriors, mu, beta, sigma_s,
            kappa, C0, chi, m0, m_tilde, Delta_tilde, delta,
            S_bar, K, sigma_xi)

    if func_id == 0:
        # diff_E_best0: U(EXIT, s) - max(U(HOLD, s), U(QUIET, s))
        u_e = _compute_expected_payoff(_ACTION_EXIT, *args)
        u_h = _compute_expected_payoff(_ACTION_HOLD, *args)
        u_q = _compute_expected_payoff(_ACTION_QUIET, *args)
        return u_e - max(u_h, u_q)
    elif func_id == 1:
        # diff_H_Q: U(HOLD, s) - U(QUIET, s)
        u_h = _compute_expected_payoff(_ACTION_HOLD, *args)
        u_q = _compute_expected_payoff(_ACTION_QUIET, *args)
        return u_h - u_q
    elif func_id == 2:
        # diff_Q_P: U(QUIET, s) - U(PUBLIC, s)
        u_q = _compute_expected_payoff(_ACTION_QUIET, *args)
        u_p = _compute_expected_payoff(_ACTION_PUBLIC, *args)
        return u_q - u_p
    else:  # func_id == 3
        # diff_H_P: U(HOLD, s) - U(PUBLIC, s)
        u_h = _compute_expected_payoff(_ACTION_HOLD, *args)
        u_p = _compute_expected_payoff(_ACTION_PUBLIC, *args)
        return u_h - u_p


# ---------------------------------------------------------------------------
# Full equilibrium solver (JIT'd)
# ---------------------------------------------------------------------------


@numba.njit(cache=True)
def _solve_equilibrium_inner(mu: float, sigma_v: float, sigma_eps: float,
                             kappa: float, C0: float, chi: float,
                             rho: float, Delta: float,
                             m0: float, m1: float,
                             S_bar: float, K: float, sigma_xi: float,
                             delta: float,
                             k1_init: float, k0_init: float, kD_init: float,
                             max_iter: int, tol: float):
    """Damped fixed-point solver for (k1, k0, kD). Returns (k1, k0, kD)."""

    # Derived quantities
    sigma_s = math.sqrt(sigma_v**2 + sigma_eps**2)
    beta = sigma_v**2 / (sigma_v**2 + sigma_eps**2)
    m_tilde = m0 + rho * (m1 - m0)
    Delta_tilde = rho * Delta

    s_min = mu - 6.0 * sigma_s
    s_max = mu + 6.0 * sigma_s

    # Signal grid for bracket search
    n_grid = 61
    s_grid = np.empty(n_grid)
    for i in range(n_grid):
        s_grid[i] = s_min + (s_max - s_min) * i / (n_grid - 1)

    k1 = k1_init
    k0 = k0_init
    kD = kD_init

    # Pre-allocate evaluation buffer
    func_vals = np.empty(n_grid)

    TOL_REGION = 1e-4
    eps_bracket = 1e-4

    for _iteration in range(max_iter):
        # Enforce ordering
        if k0 < k1:
            k0 = k1
        if kD < k0:
            kD = k0

        # Compute prices, posteriors for current cutoffs
        (prices, posteriors,
         omega_E, omega_H, omega_Q, omega_P,
         mu_E, mu_H, mu_Q, mu_P) = _compute_equilibrium_prices(
            k1, k0, kD, mu, sigma_s, beta, kappa,
            m0, m_tilde, Delta_tilde, delta, S_bar, K, sigma_xi)

        # Common args for payoff evaluation
        # func_id: 0=diff_E_best0, 1=diff_H_Q, 2=diff_Q_P, 3=diff_H_P

        # === k1: Exit vs best q=0 option ===
        for i in range(n_grid):
            func_vals[i] = _eval_diff(0, s_grid[i], prices, posteriors,
                                      mu, beta, sigma_s, kappa, C0, chi,
                                      m0, m_tilde, Delta_tilde, delta,
                                      S_bar, K, sigma_xi)

        found, a, b = _bisect(func_vals, s_grid, k1)
        if not found:
            # If exit dominates at s_min, push to top; otherwise bottom
            if func_vals[0] >= 0.0:
                k1_new = s_max
            else:
                k1_new = s_min
        elif a == b:
            k1_new = a
        else:
            fa = _eval_diff(0, a, prices, posteriors,
                            mu, beta, sigma_s, kappa, C0, chi,
                            m0, m_tilde, Delta_tilde, delta,
                            S_bar, K, sigma_xi)
            fb = _eval_diff(0, b, prices, posteriors,
                            mu, beta, sigma_s, kappa, C0, chi,
                            m0, m_tilde, Delta_tilde, delta,
                            S_bar, K, sigma_xi)
            k1_new = _brentq(fa, fb, a, b, 0, s_grid, prices, posteriors,
                             mu, beta, sigma_s, kappa, C0, chi,
                             m0, m_tilde, Delta_tilde, delta,
                             S_bar, K, sigma_xi)

        # === k0: Hold vs Quiet Voice (above k1) ===
        # Filter grid to [k1_new, s_max]
        n_sub = 0
        for i in range(n_grid):
            if s_grid[i] >= k1_new:
                n_sub += 1

        if n_sub < 2:
            k0_new = k1_new
        else:
            sub_grid = np.empty(n_sub)
            sub_vals = np.empty(n_sub)
            j = 0
            for i in range(n_grid):
                if s_grid[i] >= k1_new:
                    sub_grid[j] = s_grid[i]
                    sub_vals[j] = _eval_diff(1, s_grid[i], prices, posteriors,
                                             mu, beta, sigma_s, kappa, C0, chi,
                                             m0, m_tilde, Delta_tilde, delta,
                                             S_bar, K, sigma_xi)
                    j += 1

            found, a, b = _bisect(sub_vals, sub_grid, k0)
            if not found:
                s0 = k1_new + eps_bracket
                if s0 > s_max:
                    s0 = s_max
                val_at_s0 = _eval_diff(1, s0, prices, posteriors,
                                       mu, beta, sigma_s, kappa, C0, chi,
                                       m0, m_tilde, Delta_tilde, delta,
                                       S_bar, K, sigma_xi)
                if val_at_s0 <= 0.0:
                    k0_new = k1_new
                else:
                    k0_new = s_max
            elif a == b:
                k0_new = a
            else:
                fa = _eval_diff(1, a, prices, posteriors,
                                mu, beta, sigma_s, kappa, C0, chi,
                                m0, m_tilde, Delta_tilde, delta,
                                S_bar, K, sigma_xi)
                fb = _eval_diff(1, b, prices, posteriors,
                                mu, beta, sigma_s, kappa, C0, chi,
                                m0, m_tilde, Delta_tilde, delta,
                                S_bar, K, sigma_xi)
                k0_new = _brentq(fa, fb, a, b, 1, s_grid, prices, posteriors,
                                 mu, beta, sigma_s, kappa, C0, chi,
                                 m0, m_tilde, Delta_tilde, delta,
                                 S_bar, K, sigma_xi)

        # === kD: (Quiet or Hold) vs Public Voice ===
        # Choose lower action
        if k0_new < s_max - 1e-6:
            lower_func_id = 2  # Quiet vs Public
        else:
            lower_func_id = 3  # Hold vs Public

        start_kD = k0_new
        if start_kD > s_max:
            start_kD = s_max

        n_sub = 0
        for i in range(n_grid):
            if s_grid[i] >= start_kD:
                n_sub += 1

        if n_sub < 2:
            kD_new = start_kD
        else:
            sub_grid = np.empty(n_sub)
            sub_vals = np.empty(n_sub)
            j = 0
            for i in range(n_grid):
                if s_grid[i] >= start_kD:
                    sub_grid[j] = s_grid[i]
                    sub_vals[j] = _eval_diff(lower_func_id, s_grid[i],
                                             prices, posteriors,
                                             mu, beta, sigma_s, kappa, C0, chi,
                                             m0, m_tilde, Delta_tilde, delta,
                                             S_bar, K, sigma_xi)
                    j += 1

            found, a, b = _bisect(sub_vals, sub_grid, kD)
            if not found:
                s0 = start_kD + eps_bracket
                if s0 > s_max:
                    s0 = s_max
                val_at_s0 = _eval_diff(lower_func_id, s0, prices, posteriors,
                                       mu, beta, sigma_s, kappa, C0, chi,
                                       m0, m_tilde, Delta_tilde, delta,
                                       S_bar, K, sigma_xi)
                if val_at_s0 <= 0.0:
                    kD_new = start_kD
                else:
                    kD_new = s_max
            elif a == b:
                kD_new = a
            else:
                fa = _eval_diff(lower_func_id, a, prices, posteriors,
                                mu, beta, sigma_s, kappa, C0, chi,
                                m0, m_tilde, Delta_tilde, delta,
                                S_bar, K, sigma_xi)
                fb = _eval_diff(lower_func_id, b, prices, posteriors,
                                mu, beta, sigma_s, kappa, C0, chi,
                                m0, m_tilde, Delta_tilde, delta,
                                S_bar, K, sigma_xi)
                kD_new = _brentq(fa, fb, a, b, lower_func_id, s_grid,
                                 prices, posteriors,
                                 mu, beta, sigma_s, kappa, C0, chi,
                                 m0, m_tilde, Delta_tilde, delta,
                                 S_bar, K, sigma_xi)

        # Enforce ordering
        if k0_new < k1_new:
            k0_new = k1_new
        if kD_new < k0_new:
            kD_new = k0_new

        # Check convergence
        if (abs(k1_new - k1) < tol and
                abs(k0_new - k0) < tol and
                abs(kD_new - kD) < tol):
            return k1_new, k0_new, kD_new

        # Damped update
        alpha = 0.75
        k1 = alpha * k1_new + (1.0 - alpha) * k1
        k0 = alpha * k0_new + (1.0 - alpha) * k0
        kD = alpha * kD_new + (1.0 - alpha) * kD

    return k1, k0, kD


# ---------------------------------------------------------------------------
# Minority gains (JIT'd)
# ---------------------------------------------------------------------------


@numba.njit(cache=True)
def _compute_minority_gains_inner(k1: float, k0: float, kD: float,
                                  mu: float, sigma_s: float, beta: float,
                                  kappa: float, m0: float, m_tilde: float,
                                  Delta_tilde: float, delta: float,
                                  S_bar: float, K: float, sigma_xi: float):
    """Returns (total, base, activism) minority gains."""
    omega_E, omega_H, omega_Q, omega_P = _compute_action_probs(
        k1, k0, kD, mu, sigma_s)

    (prices, pi,
     _, _, _, _,
     _, _, _, _) = _compute_equilibrium_prices(
        k1, k0, kD, mu, sigma_s, beta, kappa,
        m0, m_tilde, Delta_tilde, delta, S_bar, K, sigma_xi)

    TOL = 1e-10
    p0 = 1.0 - kappa
    p1 = kappa / 2.0

    total_gains = 0.0
    base_gains = 0.0
    activism_gains = 0.0

    # actions: (q, a_engaged, omega)
    # EXIT: q=-1, a=0
    # HOLD: q=0, a=0
    # QUIET: q=0, a=1
    # PUBLIC: q=+1, a=1
    qs = np.array([-1, 0, 0, 1], dtype=np.int64)
    a_vals = np.array([0, 0, 1, 1], dtype=np.int64)
    D_vals = np.array([0, 0, 0, 1], dtype=np.int64)
    omegas = np.array([omega_E, omega_H, omega_Q, omega_P])

    for act_i in range(4):
        omega_a = omegas[act_i]
        if omega_a < TOL:
            continue

        q = qs[act_i]
        a = a_vals[act_i]
        D = D_vals[act_i]
        m_realized = m_tilde if a == 1 else m0

        for iz in range(3):
            z = iz - 1  # -1, 0, 1
            pz = p1 if z != 0 else p0
            X = q + z

            P = _get_price(prices, X, D, mu)
            pi_XD = _get_pi(pi, X, D)
            m_XD = m0 + (m_tilde - m0) * pi_XD
            p_bid = _bid_probability(P, m_XD, S_bar, K, sigma_xi)

            weight = omega_a * pz
            total_gains += weight * p_bid * m_realized
            base_gains += weight * p_bid * m0
            activism_gains += weight * p_bid * (m_realized - m0)

    return total_gains, base_gains, activism_gains


# ---------------------------------------------------------------------------
# Python wrappers (public API)
# ---------------------------------------------------------------------------


def solve_equilibrium_fast(
    params: ModelParams,
    k1_init: Optional[float] = None,
    k0_init: Optional[float] = None,
    kD_init: Optional[float] = None,
    max_iter: int = 60,
    tol: float = TOL_CONVERGE,
) -> Cutoffs:
    """Numba-accelerated equilibrium solver. Drop-in replacement for solver.solve_equilibrium."""
    k1_i = params.mu - 1.0 * params.sigma_s if k1_init is None else float(k1_init)
    k0_i = params.mu - 0.5 * params.sigma_s if k0_init is None else float(k0_init)
    kD_i = params.mu + 0.5 * params.sigma_s if kD_init is None else float(kD_init)

    k1, k0, kD = _solve_equilibrium_inner(
        params.mu, params.sigma_v, params.sigma_eps, params.kappa,
        params.C0, params.chi, params.rho, params.Delta,
        params.m0, params.m1, params.S_bar, params.K, params.sigma_xi,
        params.delta,
        k1_i, k0_i, kD_i, max_iter, tol,
    )
    return Cutoffs(k1, k0, kD)


def compute_minority_gains_fast(
    k1: float, k0: float, kD: float, params: ModelParams,
) -> MinorityGains:
    """Numba-accelerated minority gains. Drop-in replacement for model.compute_minority_gains."""
    sigma_s = params.sigma_s
    beta = params.beta
    m_tilde = params.m_tilde
    Delta_tilde = params.Delta_tilde

    total, base, activism = _compute_minority_gains_inner(
        k1, k0, kD,
        params.mu, sigma_s, beta, params.kappa,
        params.m0, m_tilde, Delta_tilde, params.delta,
        params.S_bar, params.K, params.sigma_xi,
    )
    return MinorityGains(total=total, base=base, activism=activism)


def compute_series_over_kappa_fast(
    base_params: ModelParams,
    kappa_values,
    include_no_disclosure: bool = False,
) -> Dict[str, np.ndarray]:
    """Accelerated kappa sweep. Drop-in replacement for solver.compute_series_over_kappa.

    Note: include_no_disclosure is accepted for API compatibility but not
    implemented in the accelerated path (the no-disclosure counterfactual
    requires additional model functions that are not yet JIT'd). Falls back
    to the pure-Python path for that component.
    """
    kappa_arr = np.asarray(kappa_values, dtype=float)
    n = len(kappa_arr)

    k1_vals = np.empty(n)
    k0_vals = np.empty(n)
    kD_vals = np.empty(n)
    Delta_min_vals = np.empty(n)
    base_vals = np.empty(n)
    act_vals = np.empty(n)

    prev_k1 = base_params.mu - 1.0 * base_params.sigma_s
    prev_k0 = base_params.mu - 0.5 * base_params.sigma_s
    prev_kD = base_params.mu + 0.5 * base_params.sigma_s

    sigma_s = base_params.sigma_s
    beta = base_params.beta

    for i in range(n):
        kappa = kappa_arr[i]
        m_tilde = base_params.m_tilde
        Delta_tilde = base_params.Delta_tilde

        try:
            k1, k0, kD = _solve_equilibrium_inner(
                base_params.mu, base_params.sigma_v, base_params.sigma_eps,
                kappa, base_params.C0, base_params.chi,
                base_params.rho, base_params.Delta,
                base_params.m0, base_params.m1,
                base_params.S_bar, base_params.K, base_params.sigma_xi,
                base_params.delta,
                prev_k1, prev_k0, prev_kD, 60, TOL_CONVERGE,
            )
            prev_k1, prev_k0, prev_kD = k1, k0, kD

            total, base_c, act_c = _compute_minority_gains_inner(
                k1, k0, kD,
                base_params.mu, sigma_s, beta, kappa,
                base_params.m0, m_tilde, Delta_tilde, base_params.delta,
                base_params.S_bar, base_params.K, base_params.sigma_xi,
            )

            k1_vals[i] = k1
            k0_vals[i] = k0
            kD_vals[i] = kD
            Delta_min_vals[i] = total
            base_vals[i] = base_c
            act_vals[i] = act_c
        except Exception:
            k1_vals[i] = np.nan
            k0_vals[i] = np.nan
            kD_vals[i] = np.nan
            Delta_min_vals[i] = np.nan
            base_vals[i] = np.nan
            act_vals[i] = np.nan

    series: Dict[str, np.ndarray] = {
        "kappa": kappa_arr,
        "k1": k1_vals,
        "k0": k0_vals,
        "kD": kD_vals,
        "Delta_min": Delta_min_vals,
        "base": base_vals,
        "act": act_vals,
    }

    if include_no_disclosure:
        # Fall back to pure-Python for the no-disclosure counterfactual
        from numerical.model import compute_minority_gains_no_disclosure_given_strategy
        act_nd = np.empty(n)
        for i in range(n):
            if np.isnan(k1_vals[i]):
                act_nd[i] = np.nan
                continue
            params_i = base_params.replace(kappa=float(kappa_arr[i]))
            _, _, nd_act = compute_minority_gains_no_disclosure_given_strategy(
                k1_vals[i], k0_vals[i], kD_vals[i], params_i,
            )
            act_nd[i] = nd_act
        series["act_no_disclosure"] = act_nd

    return series
```
