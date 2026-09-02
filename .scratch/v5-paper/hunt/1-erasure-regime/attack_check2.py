"""
Second attack check: does the memo's exact b = 1 Blackwell turn (2 kappa' + kappa >= 2)
survive when the experiment is the full mark-path history rather than one round?

Runs from the repository root:
    PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/1-erasure-regime/attack_check2.py
"""

import itertools
import json

import numpy as np
from scipy.optimize import linprog


def one_round(b, kappa):
    flows = list(range(-1, b + 2))
    idx = {f: i for i, f in enumerate(flows)}
    A = np.zeros((2, len(flows)))
    for r, m in enumerate((0, b)):
        A[r, idx[m - 1]] += kappa / 2.0
        A[r, idx[m]] += 1.0 - kappa
        A[r, idx[m + 1]] += kappa / 2.0
    return A, flows


def path_channel(b, kappa, paths):
    A1, flows = one_round(b, kappa)
    fidx = {f: i for i, f in enumerate(flows)}
    n = len(paths[0])
    hist = list(itertools.product(flows, repeat=n))
    A = np.zeros((len(paths), len(hist)))
    for p, path in enumerate(paths):
        for j, h in enumerate(hist):
            pr = 1.0
            for e in range(n):
                pr *= A1[0 if path[e] == 0 else 1, fidx[h[e]]]
            A[p, j] = pr
    return A


def garbling_residual(A, B):
    """Smallest achievable max |A K - B| over row-stochastic K, by an L1 LP.

    Variables: K (nx*ny) and slacks t (ns*ny) with -t <= (AK - B) <= t, minimise sum t.
    A residual of 0 means B is exactly a garbling of A.
    """
    ns, nx = A.shape
    ny = B.shape[1]
    nk = nx * ny
    nt = ns * ny
    nvar = nk + nt
    rows_ub, rhs_ub = [], []
    for i in range(ns):
        for y in range(ny):
            c = np.zeros(nvar)
            for x in range(nx):
                c[x * ny + y] = A[i, x]
            c[nk + i * ny + y] = -1.0
            rows_ub.append(c.copy())
            rhs_ub.append(B[i, y])
            c2 = -c.copy()
            c2[nk + i * ny + y] = -1.0
            rows_ub.append(c2)
            rhs_ub.append(-B[i, y])
    rows_eq, rhs_eq = [], []
    for x in range(nx):
        c = np.zeros(nvar)
        c[x * ny:(x + 1) * ny] = 1.0
        rows_eq.append(c)
        rhs_eq.append(1.0)
    obj = np.concatenate([np.zeros(nk), np.ones(nt)])
    bounds = [(0.0, 1.0)] * nk + [(0.0, None)] * nt
    res = linprog(obj, A_ub=np.array(rows_ub), b_ub=np.array(rhs_ub),
                  A_eq=np.array(rows_eq), b_eq=np.array(rhs_eq),
                  bounds=bounds, method="highs")
    if res.status != 0:
        return float("inf"), None
    K = res.x[:nk].reshape(nx, ny)
    return float(np.abs(A @ K - B).max()), K


out = {}
pairs = [(0.62, 0.68), (0.5, 0.6), (0.55, 0.62), (0.4, 0.5), (0.2, 0.4),
         (0.3, 0.5), (0.6, 0.65), (0.45, 0.6), (0.1, 0.3)]

for q in (1, 2, 3):
    block = {}
    for ka, kb in pairs:
        paths = [tuple([0] * q), tuple([1] * q)]     # two paths differing in every round
        A = path_channel(1, ka, paths)
        B = path_channel(1, kb, paths)
        r_low_garbles_high, K = garbling_residual(B, A)   # is E_kappa a garbling of E_kappa'?
        r_high_garbles_low, _ = garbling_residual(A, B)   # is E_kappa' a garbling of E_kappa?
        block[f"{ka}->{kb}"] = {
            "one_round_rule_says_low_is_garbling_of_high": bool(2 * kb + ka >= 2),
            "residual_low_is_garbling_of_high": r_low_garbles_high,
            "residual_high_is_garbling_of_low": r_high_garbles_low,
        }
    out[f"q={q}"] = block

# Explicit verification of the surprising node, with the kernel written out.
paths = [(0, 0), (1, 1)]
A = path_channel(1, 0.62, paths)
B = path_channel(1, 0.68, paths)
r, K = garbling_residual(B, A)
out["explicit_0.62_0.68_two_rounds"] = {
    "max_abs_residual_of_B_K_minus_A": r,
    "K_min_entry": float(K.min()),
    "K_row_sum_max_dev": float(np.abs(K.sum(1) - 1).max()),
    "A": A.tolist(),
    "B_K": (B @ K).tolist(),
}

print(json.dumps(out, indent=2))
