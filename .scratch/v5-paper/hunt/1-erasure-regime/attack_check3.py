"""
Third attack check.

(1) The memo's two-action false-claim problem, exactly as written (abstain, claim mark zero),
    to test the claimed value a_t / 2 = t / 4 at order size one.
(2) How far the one-round Blackwell turn 2 kappa' + kappa >= 2 fails to describe the
    full mark-path experiment: pairs with kappa < kappa' < 2/3 at path length q.

Runs from the repository root:
    PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/1-erasure-regime/attack_check3.py
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
    ns, nx = A.shape
    ny = B.shape[1]
    nk, nt = nx * ny, ns * ny
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
    res = linprog(obj, A_ub=np.array(rows_ub), b_ub=np.array(rhs_ub),
                  A_eq=np.array(rows_eq), b_eq=np.array(rhs_eq),
                  bounds=[(0.0, 1.0)] * nk + [(0.0, None)] * nt, method="highs")
    if res.status != 0:
        return float("inf")
    K = res.x[:nk].reshape(nx, ny)
    return float(np.abs(A @ K - B).max())


out = {}

# (1) the memo's exact two-action problem: abstain, or claim the mark is zero
vals = {}
for t in (0.1, 0.3, 0.5, 0.7, 0.9):
    A, _ = one_round(1, t)
    a, c = t / 2, 1 - t
    C = 1.0 + max(a / c, c / a)
    joint = A * 0.5
    v = 0.0
    for x in range(A.shape[1]):
        v += max(0.0, joint[0, x] * 1.0 + joint[1, x] * (-C))
    vals[str(t)] = {"computed": v, "memo_claim_t_over_4": t / 4}
out["two_action_false_claim_value"] = vals

# (2) pairs below 2/3, longer paths
probe = [(0.62, 0.68), (0.64, 0.66), (0.6, 0.66), (0.5, 0.6), (0.4, 0.6), (0.2, 0.4)]
tbl = {}
for q in (1, 2, 3, 4):
    for ka, kb in probe:
        if q == 4 and (ka, kb) not in [(0.64, 0.66), (0.6, 0.66), (0.5, 0.6)]:
            continue
        paths = [tuple([0] * q), tuple([1] * q)]
        A = path_channel(1, ka, paths)
        B = path_channel(1, kb, paths)
        tbl[f"q={q}|{ka}->{kb}"] = {
            "both_below_two_thirds": bool(kb < 2 / 3),
            "one_round_rule": bool(2 * kb + ka >= 2),
            "residual_low_is_garbling_of_high": garbling_residual(B, A),
        }
out["longer_paths_vs_one_round_turn"] = tbl

print(json.dumps(out, indent=2))
