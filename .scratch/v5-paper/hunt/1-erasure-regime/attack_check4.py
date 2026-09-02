"""
Fourth attack check: map the pairs at order size one where the LOWER liquidity experiment
is a garbling of the HIGHER one, at path length q = 1, 2, 3.  The memo's closed form
(2 kappa' + kappa >= 2) is stated for one round.  This asks how the region moves with q.

Runs from the repository root:
    PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/1-erasure-regime/attack_check4.py
"""

import itertools
import json

import numpy as np
from scipy.optimize import linprog


def one_round(kappa):
    A = np.zeros((2, 4))                      # flows -1, 0, 1, 2 ; marks 0 and 1
    A[0] = [kappa / 2, 1 - kappa, kappa / 2, 0]
    A[1] = [0, kappa / 2, 1 - kappa, kappa / 2]
    return A


def path_channel(kappa, q):
    A1 = one_round(kappa)
    hist = list(itertools.product(range(4), repeat=q))
    A = np.zeros((2, len(hist)))
    for p in (0, 1):
        for j, h in enumerate(hist):
            pr = 1.0
            for e in range(q):
                pr *= A1[p, h[e]]
            A[p, j] = pr
    return A


def residual(A, B):
    ns, nx = A.shape
    ny = B.shape[1]
    nk, nt = nx * ny, ns * ny
    rows_ub, rhs_ub = [], []
    for i in range(ns):
        for y in range(ny):
            c = np.zeros(nk + nt)
            for x in range(nx):
                c[x * ny + y] = A[i, x]
            c[nk + i * ny + y] = -1.0
            rows_ub.append(c.copy()); rhs_ub.append(B[i, y])
            c2 = -c.copy(); c2[nk + i * ny + y] = -1.0
            rows_ub.append(c2); rhs_ub.append(-B[i, y])
    rows_eq, rhs_eq = [], []
    for x in range(nx):
        c = np.zeros(nk + nt)
        c[x * ny:(x + 1) * ny] = 1.0
        rows_eq.append(c); rhs_eq.append(1.0)
    res = linprog(np.concatenate([np.zeros(nk), np.ones(nt)]),
                  A_ub=np.array(rows_ub), b_ub=np.array(rhs_ub),
                  A_eq=np.array(rows_eq), b_eq=np.array(rhs_eq),
                  bounds=[(0.0, 1.0)] * nk + [(0.0, None)] * nt, method="highs")
    if res.status != 0:
        return float("inf")
    K = res.x[:nk].reshape(nx, ny)
    return float(np.abs(A @ K - B).max())


out = {}
grid = [round(0.05 * k, 3) for k in range(1, 20)]
for q in (1, 2, 3):
    found = []
    for i, ka in enumerate(grid):
        for kb in grid[i + 1:]:
            if 2 * kb + ka >= 2 - 1e-12:
                continue                     # the one-round rule already allows these
            r = residual(path_channel(kb, q), path_channel(ka, q))
            if r < 1e-10:
                found.append((ka, kb, 2 * kb + ka, r))
    out[f"q={q}|pairs_outside_the_one_round_region_that_are_still_garblings"] = found

print(json.dumps(out, indent=2, default=str))
