"""Independent recheck of the Hunt 2 memo (attacker side).

Reads the committed record numerical_v4/checks/t2_threshold_revelation_check.json.
Runs no pooled pass, no policy solve, no numerical_v4 import.
Writes only .scratch/v5-paper/hunt/2-one-cut-identity/attack_recheck.json.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "numerical_v4/checks/t2_threshold_revelation_check.json"
OUT = HERE / "attack_recheck.json"

rec = json.loads(SOURCE.read_text())
H = int(rec["provenance"]["H"])
nodes = {(int(n["T"]), float(n["tau_quantile"])): n for n in rec["nodes"]}
ck = {k: np.array(v["c_k"], dtype=float) for k, v in nodes.items()}

x_of_k = lambda k: k / (2.0 - k)
k_of_x = lambda x: 2.0 * x / (1.0 + x)

def W_rev(c, kappa):
    eps = kappa / 2.0
    return (1.0 - eps) ** H * np.polyval(c, x_of_k(kappa))

out = {}

# 1. reproduce the record's per-kappa quantities from the c_k alone
res = {"max_W": 0.0, "max_SP": 0.0, "max_C": 0.0, "max_WC": 0.0, "flag_mismatch": 0}
for p in rec["pairs"]:
    T, q, qp = int(p["T"]), float(p["tau_quantile"]), float(p["tau_prime_quantile"])
    cA, cR = ck[(T, q)], ck[(T, qp)]
    for row in p["per_kappa"]:
        kap = float(row["kappa"])
        wA, wR = W_rev(cA, kap), W_rev(cR, kap)
        res["max_W"] = max(res["max_W"], abs(wA - row["W_rev_tau"]), abs(wR - row["W_rev_tau_prime"]))
        res["max_SP"] = max(res["max_SP"], abs(abs(wA) / 10.0 - row["S_P_tau"]),
                            abs(abs(wR) / 10.0 - row["S_P_tau_prime"]))
        C = abs(wR) / abs(wA)
        res["max_C"] = max(res["max_C"], abs(C - row["C_tau"]))
        res["max_WC"] = max(res["max_WC"], abs(float(p["W_tau"]) * C - row["W_tau_C_tau"]))
        if bool(C <= 1.0) != bool(row["condition_D"]):
            res["flag_mismatch"] += 1
out["record_reproduction"] = res

# 2. sign patterns, roots, kappa_star
pairs = []
for p in rec["pairs"]:
    T, q, qp = int(p["T"]), float(p["tau_quantile"]), float(p["tau_prime_quantile"])
    cA, cR = ck[(T, q)], ck[(T, qp)]
    d = cR - cA
    mass = float(p["reclassified_mass"])
    phi = mass / (1.0 - float(p["Omega_tau"]))
    entry = {"T": T, "q": q, "q_prime": qp, "mass": mass, "phi": phi,
             "W_tau_record": float(p["W_tau"]), "one_minus_phi": 1.0 - phi,
             "max_abs_d": float(np.max(np.abs(d)))}
    if mass <= 1e-12:
        entry["kind"] = "null"
        pairs.append(entry)
        continue
    entry["kind"] = "nonnull"
    def sgn(v, tol):
        return [0 if abs(t) <= tol else int(math.copysign(1, t)) for t in v]
    def crossings(v, tol):
        s = [t for t in sgn(v, tol) if t]
        return sum(a != b for a, b in zip(s, s[1:])), (s[0] if s else 0), (s[-1] if s else 0)
    for name, v in (("cA", cA), ("cR", cR), ("d", d)):
        for tol_name, tol in (("1e-12", 1e-12), ("relative_1e-6", 1e-6 * float(np.max(np.abs(v))))):
            ch, first, last = crossings(v, tol)
            entry[f"{name}_crossings_{tol_name}"] = [ch, first, last]
    roots = {}
    for name, v in (("A", cA), ("R", cR), ("D", d)):
        r = np.roots(v)
        pos = sorted(float(t.real) for t in r if abs(t.imag) < 1e-12 and t.real > 0)
        roots[name] = pos
    entry["positive_roots_x"] = roots
    entry["root_kappa"] = {k: [k_of_x(t) for t in v] for k, v in roots.items()}
    rstar = max(v[0] for v in roots.values())
    entry["x_star"] = rstar
    entry["kappa_star"] = k_of_x(rstar)
    entry["gap_to_grid"] = 0.15 - k_of_x(rstar)
    # sensitivity of each root to relative perturbation of the coefficients
    sens = {}
    for name, v in (("A", cA), ("R", cR), ("D", d)):
        r = roots[name][0]
        deriv = np.polyval(np.polyder(v), r)
        amp = float(np.sum(np.abs(v) * r ** np.arange(H, -1, -1)) / abs(deriv))
        sens[name] = amp
    entry["root_x_amplification"] = sens
    pairs.append(entry)
out["pairs"] = pairs

# 3. worst pair: how large a relative error in the c_k would lift kappa_star above 0.15
worst = max((e for e in pairs if e["kind"] == "nonnull"), key=lambda e: e["kappa_star"])
dx = x_of_k(0.15) - worst["x_star"]
out["worst_pair"] = {
    "pair": [worst["T"], worst["q"], worst["q_prime"]],
    "kappa_star": worst["kappa_star"],
    "x_gap_to_grid": dx,
    "critical_relative_coefficient_error": dx / max(worst["root_x_amplification"].values()),
}

# 4. T=10 common polynomial: root and grid values
c10 = ck[(10, 0.5)]
r10 = sorted(float(t.real) for t in np.roots(c10) if abs(t.imag) < 1e-12 and t.real > 0)
grid = [0.15 + 0.01 * i for i in range(71)]
out["T10"] = {
    "identical_across_quantiles": all(float(np.max(np.abs(ck[(10, q)] - c10))) == 0.0
                                      for q in (0.1, 0.3, 0.5, 0.7, 0.9)),
    "positive_roots_x": r10,
    "positive_roots_kappa": [k_of_x(t) for t in r10],
    "min_abs_W_on_grid": min(abs(W_rev(c10, k)) for k in grid),
    "W_sign_change_on_grid": len({int(math.copysign(1, W_rev(c10, k))) for k in grid}) > 1,
}

# 5. exact sets below the grid for the 0.5 -> 0.3 pair
cA, cR = ck[(5, 0.5)], ck[(5, 0.3)]
Wt = float([p for p in rec["pairs"] if p["T"] == 5 and p["tau_quantile"] == 0.5][0]["W_tau"])
fine = np.arange(0.05, 0.2000001, 1e-6)
Cvals = np.array([abs(W_rev(cR, k)) / abs(W_rev(cA, k)) for k in fine])
badC = fine[Cvals > 1.0]
badD = fine[Wt * Cvals > 1.0]
out["below_grid_0p5_to_0p3"] = {
    "C_tau_gt_1_interval": [float(badC.min()), float(badC.max())] if badC.size else None,
    "dial_gt_1_interval": [float(badD.min()), float(badD.max())] if badD.size else None,
    "memo_kappa_star": worst["kappa_star"],
    "brief_reported_interval": [0.1440, 0.1485],
}

# 6. brute-force check of the algebraic equivalences of part (iv), (v), (vi)
rng = np.random.default_rng(20260902)
bad = {"iv": 0, "v": 0, "via": 0, "vib": 0, "vic": 0, "vid": 0}
for _ in range(400000):
    phi = float(rng.uniform(1e-6, 1 - 1e-6))
    sA = float(rng.normal())
    sB = float(rng.normal()) * float(rng.choice([1.0, 1e-3, 1e3]))
    if abs(sA) < 1e-12:
        continue
    sAB = (sA - phi * sB) / (1 - phi)
    C = abs(sAB) / abs(sA)
    WC = (1 - phi) * C
    if (C <= 1) != ((sB - sA) * (phi * sB - (2 - phi) * sA) <= 0):
        bad["iv"] += 1
    if (WC <= 1) != (sB * (2 * sA - phi * sB) >= 0):
        bad["v"] += 1
    if sA * sB <= 0 and not C > 1:
        bad["via"] += 1
    if sA * sB > 0 and ((C <= 1) != (abs(sA) <= abs(sB) <= (2 - phi) / phi * abs(sA))):
        bad["vib"] += 1
    if sAB * sA >= 0 and ((C <= 1) != (sB / sA >= 1)):
        bad["vic"] += 1
    if (WC <= 1) != ((sA * sB > 0 or sB == 0) and abs(sB) <= 2 / phi * abs(sA)):
        bad["vid"] += 1
out["algebra_counterexamples"] = bad

# 7. the certificate's own band inequalities at every recorded grid node
band = {"min_lower_margin": math.inf, "min_upper_margin": math.inf,
        "min_sA": math.inf, "min_sR": math.inf, "min_sA_minus_sR": math.inf}
for e in pairs:
    if e["kind"] != "nonnull":
        continue
    cA, cR = ck[(e["T"], e["q"])], ck[(e["T"], e["q_prime"])]
    phi = e["phi"]
    for kap in grid:
        sA = -0.5 * W_rev(cA, kap)
        sR = -0.5 * W_rev(cR, kap)
        sB = (sA - (1 - phi) * sR) / phi
        band["min_lower_margin"] = min(band["min_lower_margin"], sB - sA)
        band["min_upper_margin"] = min(band["min_upper_margin"], (2 - phi) / phi * sA - sB)
        band["min_sA"] = min(band["min_sA"], sA)
        band["min_sR"] = min(band["min_sR"], sR)
        band["min_sA_minus_sR"] = min(band["min_sA_minus_sR"], sA - sR)
out["band_at_grid_nodes"] = band

OUT.write_text(json.dumps(out, indent=2, default=float) + "\n")
print(json.dumps(out, indent=2, default=float))
