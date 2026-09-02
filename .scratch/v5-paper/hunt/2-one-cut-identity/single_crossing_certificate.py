"""Check the single-crossing revelation certificate from the Hunt 2 memo.

The script reads the frozen threshold-revelation record. It does not solve a
policy or run a pooled pass. It writes its record beside this file.

Run from the repository root:

    PYTHONPATH=. .venv/bin/python \
      .scratch/v5-paper/hunt/2-one-cut-identity/single_crossing_certificate.py
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "numerical_v4/checks/t2_threshold_revelation_check.json"
OUT = HERE / "single_crossing_certificate.json"

COEFFICIENT_TOL = 1e-12
ROOT_X_TOL = 1e-13
INEQUALITY_TOL = 1e-12
NULL_MASS_TOL = 1e-12
NULL_COEFFICIENT_TOL = 1e-12
GRID_GAP_TOL = 1e-8
GRID_LO = 0.15
GRID_HI = 0.85
FAILURE_LO = 0.1440
FAILURE_HI = 0.1485


def horner(coefficients: list[float], x: float) -> float:
    value = 0.0
    for coefficient in coefficients:
        value = value * x + coefficient
    return value


def signs(coefficients: list[float]) -> list[int]:
    out = []
    for value in coefficients:
        if value > COEFFICIENT_TOL:
            out.append(1)
        elif value < -COEFFICIENT_TOL:
            out.append(-1)
        else:
            out.append(0)
    return out


def nonzero_signs(coefficients: list[float]) -> list[int]:
    return [value for value in signs(coefficients) if value]


def has_orientation(coefficients: list[float], first: int, second: int) -> bool:
    seq = nonzero_signs(coefficients)
    if len(seq) < 2 or seq[0] != first or seq[-1] != second:
        return False
    changes = sum(left != right for left, right in zip(seq, seq[1:]))
    return changes == 1


def unique_positive_root(coefficients: list[float]) -> float:
    """Bisect the unique positive root supplied by the sign certificate."""
    lo = 0.0
    hi = 1.0
    f_lo = horner(coefficients, lo)
    f_hi = horner(coefficients, hi)
    while f_lo * f_hi > 0.0 and hi < 2.0**40:
        hi *= 2.0
        f_hi = horner(coefficients, hi)
    if f_lo == 0.0:
        return 0.0
    if f_lo * f_hi > 0.0:
        raise ValueError("positive root was not bracketed")
    while hi - lo > ROOT_X_TOL:
        mid = 0.5 * (lo + hi)
        f_mid = horner(coefficients, mid)
        if f_mid == 0.0:
            return mid
        if f_lo * f_mid <= 0.0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid
    return 0.5 * (lo + hi)


def x_of_kappa(kappa: float) -> float:
    return kappa / (2.0 - kappa)


def kappa_of_x(x: float) -> float:
    return 2.0 * x / (1.0 + x)


def revelation_value(coefficients: list[float], H: int, kappa: float) -> float:
    eps = kappa / 2.0
    x = x_of_kappa(kappa)
    return (1.0 - eps) ** H * horner(coefficients, x)


def main() -> int:
    source = json.loads(SOURCE.read_text())
    H = int(source["provenance"]["H"])
    node = {
        (int(row["T"]), float(row["tau_quantile"])): row
        for row in source["nodes"]
    }

    rows = []
    nonnull_rows = []
    null_rows = []
    max_wiring_residual = 0.0

    for pair in source["pairs"]:
        T = int(pair["T"])
        q = float(pair["tau_quantile"])
        q_prime = float(pair["tau_prime_quantile"])
        c_A = [float(value) for value in node[(T, q)]["c_k"]]
        c_R = [float(value) for value in node[(T, q_prime)]["c_k"]]
        difference = [right - left for left, right in zip(c_A, c_R)]
        mass = float(pair["reclassified_mass"])

        if mass <= NULL_MASS_TOL:
            max_diff = max(abs(value) for value in difference)
            row = {
                "kind": "null_cut",
                "T": T,
                "tau_quantile": q,
                "tau_prime_quantile": q_prime,
                "reclassified_mass": mass,
                "max_abs_coefficient_difference": max_diff,
                "reported_C_tau_min": pair["C_tau_min"],
                "reported_C_tau_max": pair["C_tau_max"],
                "passes": bool(
                    max_diff <= NULL_COEFFICIENT_TOL
                    and abs(float(pair["C_tau_min"]) - 1.0) <= INEQUALITY_TOL
                    and abs(float(pair["C_tau_max"]) - 1.0) <= INEQUALITY_TOL
                ),
            }
            rows.append(row)
            null_rows.append(row)
            continue

        orientation_A = has_orientation(c_A, -1, 1)
        orientation_R = has_orientation(c_R, -1, 1)
        orientation_difference = has_orientation(difference, 1, -1)
        if not (orientation_A and orientation_R and orientation_difference):
            raise ValueError(f"one-crossing orientation failed at T={T}, q={q}->{q_prime}")

        root_x_A = unique_positive_root(c_A)
        root_x_R = unique_positive_root(c_R)
        root_x_difference = unique_positive_root(difference)
        root_kappa_A = kappa_of_x(root_x_A)
        root_kappa_R = kappa_of_x(root_x_R)
        root_kappa_difference = kappa_of_x(root_x_difference)
        kappa_star = max(root_kappa_A, root_kappa_R, root_kappa_difference)

        phi = mass / (1.0 - float(pair["Omega_tau"]))
        grid_checks = []
        for reported in pair["per_kappa"]:
            kappa = float(reported["kappa"])
            W_A = revelation_value(c_A, H, kappa)
            W_R = revelation_value(c_R, H, kappa)
            s_A = -0.5 * W_A
            s_R = -0.5 * W_R
            s_B = (s_A - (1.0 - phi) * s_R) / phi
            upper = ((2.0 - phi) / phi) * s_A
            lower_margin = s_B - s_A
            upper_margin = upper - s_B
            C_tau = abs(s_R) / abs(s_A)
            wiring = max(
                abs(W_A - float(reported["W_rev_tau"])),
                abs(W_R - float(reported["W_rev_tau_prime"])),
                abs(C_tau - float(reported["C_tau"])),
            )
            max_wiring_residual = max(max_wiring_residual, wiring)
            grid_checks.append(
                {
                    "kappa": kappa,
                    "s_A": s_A,
                    "s_R": s_R,
                    "s_B": s_B,
                    "lower_band_margin": lower_margin,
                    "upper_band_margin": upper_margin,
                    "C_tau": C_tau,
                    "certificate_order": bool(
                        s_A >= -INEQUALITY_TOL
                        and s_R >= -INEQUALITY_TOL
                        and s_R <= s_A + INEQUALITY_TOL
                    ),
                    "band_holds": bool(
                        lower_margin >= -INEQUALITY_TOL
                        and upper_margin >= -INEQUALITY_TOL
                    ),
                }
            )

        row = {
            "kind": "nonnull_cut",
            "T": T,
            "tau_quantile": q,
            "tau_prime_quantile": q_prime,
            "phi": phi,
            "reclassified_mass": mass,
            "signs_c_A": signs(c_A),
            "signs_c_R": signs(c_R),
            "signs_difference": signs(difference),
            "orientations_hold": {
                "c_A_negative_to_positive": orientation_A,
                "c_R_negative_to_positive": orientation_R,
                "difference_positive_to_negative": orientation_difference,
            },
            "root_x": {
                "c_A": root_x_A,
                "c_R": root_x_R,
                "difference": root_x_difference,
            },
            "root_kappa": {
                "c_A": root_kappa_A,
                "c_R": root_kappa_R,
                "difference": root_kappa_difference,
            },
            "kappa_star": kappa_star,
            "gap_from_grid_lower_endpoint": GRID_LO - kappa_star,
            "certificate_covers_grid_interval": bool(
                GRID_LO - kappa_star >= GRID_GAP_TOL
            ),
            "minimum_grid_lower_band_margin": min(
                item["lower_band_margin"] for item in grid_checks
            ),
            "minimum_grid_upper_band_margin": min(
                item["upper_band_margin"] for item in grid_checks
            ),
            "all_grid_orders_hold": all(item["certificate_order"] for item in grid_checks),
            "all_grid_bands_hold": all(item["band_holds"] for item in grid_checks),
            "at_grid_lower_endpoint": grid_checks[0],
            "passes": bool(
                GRID_LO - kappa_star >= GRID_GAP_TOL
                and all(item["certificate_order"] for item in grid_checks)
                and all(item["band_holds"] for item in grid_checks)
            ),
        }
        rows.append(row)
        nonnull_rows.append(row)

    failure_pair = next(
        row
        for row in nonnull_rows
        if row["T"] == 5
        and row["tau_quantile"] == 0.5
        and row["tau_prime_quantile"] == 0.3
    )
    failure_separated = bool(
        FAILURE_HI + GRID_GAP_TOL < failure_pair["kappa_star"] < GRID_LO - GRID_GAP_TOL
    )

    checks = [
        {
            "name": "one_crossing_orientations",
            "pass": all(
                all(row["orientations_hold"].values()) for row in nonnull_rows
            ),
            "tolerance": COEFFICIENT_TOL,
        },
        {
            "name": "certificate_covers_continuous_grid_interval",
            "pass": all(row["certificate_covers_grid_interval"] for row in nonnull_rows),
            "interval": [GRID_LO, GRID_HI],
            "required_kappa_gap": GRID_GAP_TOL,
        },
        {
            "name": "certificate_implies_band_at_every_recorded_grid_node",
            "pass": all(row["all_grid_bands_hold"] for row in nonnull_rows),
            "inequality_tolerance": INEQUALITY_TOL,
        },
        {
            "name": "failure_region_is_below_certificate_cutoff",
            "pass": failure_separated,
            "pair": {"T": 5, "tau_quantile": 0.5, "tau_prime_quantile": 0.3},
            "reported_failure_interval": [FAILURE_LO, FAILURE_HI],
            "certificate_cutoff": failure_pair["kappa_star"],
            "grid_lower_endpoint": GRID_LO,
            "required_gap": GRID_GAP_TOL,
        },
        {
            "name": "null_cuts_have_identical_coefficients_and_unit_ratio",
            "pass": all(row["passes"] for row in null_rows),
            "mass_tolerance": NULL_MASS_TOL,
            "coefficient_tolerance": NULL_COEFFICIENT_TOL,
            "expected_null_pairs": 4,
            "observed_null_pairs": len(null_rows),
        },
        {
            "name": "source_record_wiring",
            "pass": max_wiring_residual <= INEQUALITY_TOL,
            "max_residual": max_wiring_residual,
            "tolerance": INEQUALITY_TOL,
        },
    ]

    result = {
        "status": "PASS" if all(check["pass"] for check in checks) else "FAIL",
        "source": str(SOURCE.relative_to(ROOT)),
        "provenance": {
            "params_hash": source["provenance"]["params_hash"],
            "mark": source["provenance"]["mark"],
            "H": H,
            "frozen_k": source["provenance"]["frozen_k"],
            "tau_ladder": source["provenance"]["tau_ladder"],
            "kappa_grid": source["provenance"]["kappa_grid"],
        },
        "tolerances": {
            "coefficient_zero": COEFFICIENT_TOL,
            "root_x": ROOT_X_TOL,
            "inequality": INEQUALITY_TOL,
            "null_mass": NULL_MASS_TOL,
            "null_coefficient": NULL_COEFFICIENT_TOL,
            "required_kappa_gap": GRID_GAP_TOL,
        },
        "method": (
            "For each non-null pair, c_A and c_R must change sign once from negative "
            "to positive and c_R-c_A once from positive to negative. Descartes' rule "
            "gives one positive root for each reversed polynomial. Above the largest "
            "root, W_A <= W_R <= 0, hence 0 <= s_R <= s_A and the cut identity puts "
            "s_B in the two-sided band."
        ),
        "checks": checks,
        "pairs": rows,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "checks": checks}, indent=2))
    print(f"wrote {OUT}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
