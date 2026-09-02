"""
Attack checks for the memo .scratch/v5-paper/hunt/1-erasure-regime/memo.md.

Runs from the repository root:
    PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/1-erasure-regime/attack_check.py

Uses numpy and scipy only. It imports nothing from numerical_v4 and needs no compute lock.
Every check is an exact finite-channel computation: a Blackwell garbling feasibility LP,
an explicit kernel identity, or a decision-problem value.
"""

import itertools
import json

import numpy as np
from scipy.optimize import linprog

TOL = 1e-9


# ----------------------------------------------------------------------------- channels
def one_round(b, kappa):
    """Rows: mark 0 and mark b.  Columns: flows -1 .. b+1 (integers).  zbar = 1."""
    flows = list(range(-1, b + 2))
    idx = {f: i for i, f in enumerate(flows)}
    A = np.zeros((2, len(flows)))
    for r, m in enumerate((0, b)):
        A[r, idx[m - 1]] += kappa / 2.0
        A[r, idx[m]] += 1.0 - kappa
        A[r, idx[m + 1]] += kappa / 2.0
    return A, flows


def path_channel(b, kappa, paths):
    """Product channel over rounds for the given list of mark paths (entries 0 or b)."""
    A1, flows = one_round(b, kappa)
    n = len(paths[0])
    hist = list(itertools.product(flows, repeat=n))
    hidx = {h: i for i, h in enumerate(hist)}
    A = np.zeros((len(paths), len(hist)))
    fidx = {f: i for i, f in enumerate(flows)}
    for p, path in enumerate(paths):
        for h in hist:
            pr = 1.0
            for e in range(n):
                row = 0 if path[e] == 0 else 1
                pr *= A1[row, fidx[h[e]]]
            A[p, hidx[h]] = pr
    return A, hist


# ------------------------------------------------------------------- Blackwell feasibility
def is_garbling(A, B):
    """True iff B = A K for some row-stochastic K >= 0 (B is a garbling of A)."""
    ns, nx = A.shape
    ny = B.shape[1]
    nvar = nx * ny
    rows, rhs = [], []
    for i in range(ns):
        for y in range(ny):
            c = np.zeros(nvar)
            for x in range(nx):
                c[x * ny + y] = A[i, x]
            rows.append(c)
            rhs.append(B[i, y])
    for x in range(nx):
        c = np.zeros(nvar)
        c[x * ny:(x + 1) * ny] = 1.0
        rows.append(c)
        rhs.append(1.0)
    res = linprog(np.zeros(nvar), A_eq=np.array(rows), b_eq=np.array(rhs),
                  bounds=[(0.0, 1.0)] * nvar, method="highs")
    return bool(res.status == 0)


def dp_value(A, prior, payoff):
    """Value of a finite decision problem.  payoff[a, s] is the payoff of action a in state s."""
    joint = A * prior[:, None]                       # states x outcomes
    return float(sum(max((payoff[a] @ joint[:, x]) for a in range(payoff.shape[0]))
                     for x in range(A.shape[1])))


out = {}

# ------------------------------------------------------------- 1. b = 1, one round, both ways
grid = [round(0.02 * k, 4) for k in range(1, 50)]
bad_fwd, bad_rev = [], []
for i, ka in enumerate(grid):
    for kb in grid[i + 1:]:
        A, _ = one_round(1, ka)
        B, _ = one_round(1, kb)
        fwd = is_garbling(A, B)          # higher kappa a garbling of lower kappa?
        rev = is_garbling(B, A)          # lower  kappa a garbling of higher kappa?
        if fwd:
            bad_fwd.append((ka, kb))
        predicted = (2 * kb + ka >= 2 - 1e-12)
        if rev != predicted:
            bad_rev.append((ka, kb, rev, predicted))
out["b1_one_round_higher_is_never_garbling_of_lower"] = (len(bad_fwd) == 0)
out["b1_one_round_counterexamples_to_that"] = bad_fwd[:5]
out["b1_one_round_turn_matches_2kp_plus_k_ge_2"] = (len(bad_rev) == 0)
out["b1_one_round_turn_mismatches"] = bad_rev[:5]

# ------------------------------------------------------------- 2. the memo's kernel (2) at b = 1
worst = 0.0
for ka in grid:
    for kb in grid:
        if not (ka < kb and 2 * kb + ka >= 2):
            continue
        A, _ = one_round(1, ka)
        B, _ = one_round(1, kb)
        r = (kb - ka) / (3 * kb - 2)
        s = ka / kb
        K = np.array([[s, 1 - s, 0, 0],
                      [0, 1 - r, r, 0],
                      [0, r, 1 - r, 0],
                      [0, 0, 1 - s, s]])
        ok = (K >= -TOL).all() and abs(K.sum(1) - 1).max() < TOL
        worst = max(worst, float(np.abs(B @ K - A).max()) if ok else 1.0)
out["b1_memo_kernel_max_error_on_2kp_plus_k_ge_2"] = worst

# ------------------------------------------------------- 3. b = 1, two rounds, both state sets
two_all = [(0, 0), (0, 1), (1, 0), (1, 1)]
two_diag = [(0, 0), (1, 1)]
pairs = [(0.2, 0.4), (0.3, 0.9), (0.1, 0.95), (0.5, 0.6), (0.6, 0.75), (0.62, 0.68)]
res2 = {}
for name, paths in (("all_four", two_all), ("diagonal", two_diag)):
    for ka, kb in pairs:
        A, _ = path_channel(1, ka, paths)
        B, _ = path_channel(1, kb, paths)
        res2[f"{name}|{ka}->{kb}|higher_is_garbling_of_lower"] = is_garbling(A, B)
        res2[f"{name}|{ka}->{kb}|lower_is_garbling_of_higher"] = is_garbling(B, A)
        res2[f"{name}|{ka}->{kb}|one_round_rule_2kp_plus_k_ge_2"] = bool(2 * kb + ka >= 2)
out["b1_two_rounds"] = res2

# ---------------------------------------------- 4. b = 2, Lemma g2 kernel, interior and endpoints
def g2_error(kappa, kprime, nrounds):
    """Max error of the Lemma g2 delete-and-redraw kernel, applied round by round."""
    A1, flows = one_round(2, kappa)          # flows -1,0,1,2,3
    B1, _ = one_round(2, kprime)
    fidx = {f: i for i, f in enumerate(flows)}
    delta = (kprime - kappa) / (2 - kappa)
    epsp = kprime / 2.0
    p_zero = (1 - kprime) / (1 - epsp)       # weight on the zero-noise revealing value
    p_out = epsp / (1 - epsp)                # weight on the other revealing value
    K = np.zeros((len(flows), len(flows)))
    for f in flows:
        if f == 1:                            # erased input: stays erased
            K[fidx[1], fidx[1]] = 1.0
            continue
        mark = 0 if f <= 0 else 2             # revealing flow identifies the mark
        K[fidx[f], fidx[1]] += delta
        K[fidx[f], fidx[mark]] += (1 - delta) * p_zero
        K[fidx[f], fidx[mark + (1 if mark == 2 else -1)]] += (1 - delta) * p_out
    err_rows = float(np.abs(A1 @ K - B1).max())
    err_stoch = float(max(abs(K.sum(1) - 1).max(), -K.min(), 0.0))
    paths = [tuple(2 * x for x in p) for p in itertools.product((0, 1), repeat=nrounds)]
    A, _ = path_channel(2, kappa, paths)
    B, _ = path_channel(2, kprime, paths)
    Kp = K
    for _ in range(nrounds - 1):
        Kp = np.kron(Kp, K)
    return err_rows, err_stoch, float(np.abs(A @ Kp - B).max())

g2 = {}
for ka, kb in [(0.0, 0.3), (0.15, 0.85), (0.3, 0.9), (0.5, 1.0), (0.0, 1.0), (0.7, 0.71)]:
    g2[f"{ka}->{kb}"] = g2_error(ka, kb, 2)
out["b2_lemma_g2_kernel_errors_rows_stochastic_twoRoundPaths"] = g2

# --------------------------------------------- 5. b = 2, reverse direction and non revelation
rev2 = {}
for ka, kb in [(0.15, 0.85), (0.3, 0.4), (0.6, 0.9)]:
    A, _ = one_round(2, ka)
    B, _ = one_round(2, kb)
    rev2[f"{ka}->{kb}|lower_is_garbling_of_higher"] = is_garbling(B, A)
out["b2_reverse_direction"] = rev2

overlap = {}
for b in (1, 2, 3, 4):
    A, flows = one_round(b, 0.4)
    s0 = {f for f, p in zip(flows, A[0]) if p > 0}
    s1 = {f for f, p in zip(flows, A[1]) if p > 0}
    overlap[b] = sorted(s0 & s1)
out["support_overlap_at_kappa_0.4"] = overlap

A1, flows = one_round(2, 1.0)
out["b2_supports_at_kappa_1"] = [sorted(f for f, p in zip(flows, A1[r]) if p > 0) for r in (0, 1)]

# ------------------------------------------------- 6. the memo's two decision-problem values
dp = {}
for t in (0.1, 0.3, 0.5, 2 / 3, 0.7, 0.9):
    A, _ = one_round(1, t)
    a, c = t / 2, 1 - t
    C = 10 + max(a / c, c / a) if 0 < t < 1 else 10.0
    # actions: abstain, claim mark 0, claim mark 1
    payoff = np.array([[0.0, 0.0], [1.0, -C], [-C, 1.0]])
    prior = np.array([0.5, 0.5])
    dp[f"false_claim_value_at_{round(t, 4)}"] = (dp_value(A, prior, payoff), t / 4)
    guess = np.array([[1.0, 0.0], [0.0, 1.0]])
    v = dp_value(A, prior, guess)
    predicted = 1 - t / 2 if t <= 2 / 3 else t
    dp[f"correct_guess_value_at_{round(t, 4)}"] = (v, predicted)
out["b1_decision_values"] = dp

# multi-round version of the false-claim value: 1 - (1 - t/2)**q
mr = {}
for q in (1, 2, 3):
    paths = [tuple([0] * q), tuple([1] * q)]
    for t in (0.3, 0.6):
        A, _ = path_channel(1, t, paths)
        C = 10 + max((t / 2) / (1 - t), (1 - t) / (t / 2)) ** q
        payoff = np.array([[0.0, 0.0], [1.0, -C], [-C, 1.0]])
        mr[f"q={q}|t={t}"] = (dp_value(A, np.array([0.5, 0.5]), payoff),
                              1 - (1 - t / 2) ** q)
out["b1_multiround_false_claim"] = mr

# --------------------------------------------------- 7. b >= 3 Blackwell equivalence of nodes
eq = {}
for b in (3, 4):
    for ka, kb in [(0.2, 0.8), (0.0, 0.5), (0.5, 1.0)]:
        A, _ = one_round(b, ka)
        B, _ = one_round(b, kb)
        eq[f"b={b}|{ka}<->{kb}"] = (is_garbling(A, B), is_garbling(B, A))
out["b_ge_3_equivalence"] = eq

print(json.dumps(out, indent=2, default=str))
