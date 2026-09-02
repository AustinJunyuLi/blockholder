"""Attack checks for hunt 3 (Blackwell tightening).

Runs from the repository root:

    PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/3-blackwell-tightening/attack_check.py

No pooled pass, no cold solve, no numerical_v4 check script is run.  The only
numerical_v4 import is menu.py (breakpoints, atoms, legal_clock, b_star), which
is arithmetic on the signal line and touches no order-flow enumeration.

Parts
  A  small model in the memo's class (S1)-(S14): types, paths, marks, clock
  B  tagged date-d experiment for a rule at a liquidity intensity
  C  the memo's kernel, built explicitly, checked against the looser experiment
  D  linear-programme garbling test (feasibility of L_+ K = L_-, K row-stochastic)
  E  the memo's necessity example and its three-type non-order example
  F  calibration facts used by the memo's part 3
"""

from __future__ import annotations

import itertools
import json
import math
import os

import numpy as np
from scipy.optimize import linprog

RNG = np.random.default_rng(20260902)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attack_check.json")

# ---------------------------------------------------------------------- A ---

class Model:
    """Types, monotone paths, binary marks, legal clock.  Order size two."""

    def __init__(self, H, b0, s, w, a, bstar, n):
        self.H = H
        self.b0 = b0
        self.s = np.asarray(s, float)
        self.w = np.asarray(w, float) / np.sum(w)
        self.a = np.asarray(a, int)
        self.bstar = np.asarray(bstar, float)   # composed terminal target
        self.n = np.asarray(n, int)             # accumulation length
        self.K = len(s)

    def stake(self, i, d):
        """B_i(d), d = -1..H.  Voice accumulates linearly over n_i dates."""
        if d < 0:
            return self.b0
        if self.a[i] == 0:
            return self.b0
        return self.b0 + (self.bstar[i] - self.b0) * min(1.0, (d + 1.0) / self.n[i])

    def marks(self, i):
        """Gamma(increment) with Gamma ordered in the increment: 1 while buying."""
        if self.a[i] == 0:
            return np.zeros(self.H + 1, int)
        return np.array([1 if d < self.n[i] else 0 for d in range(self.H + 1)], int)

    def clock(self, i, tau, T):
        """(c, f, D, B^F, Q^F) at rule (tau, T)."""
        if self.a[i] == 0:
            return (math.inf, math.inf, 0, None, None)
        c = None
        for d in range(self.H + 1):
            if self.stake(i, d) >= tau:
                c = d
                break
        if c is None:
            return (math.inf, math.inf, 0, None, None)
        f = c + T
        if f > self.H:
            return (float(c), float(f), 0, None, None)
        BF = self.stake(i, f)
        return (float(c), float(f), 1, BF, self.bstar[i] - BF)


def random_model(H=2, K=5, rng=RNG):
    """A model in the class: b* strictly increasing, n weakly decreasing."""
    b0 = 0.03
    s = np.sort(rng.uniform(-2.0, 2.0, K))
    while np.min(np.diff(s)) < 1e-3:
        s = np.sort(rng.uniform(-2.0, 2.0, K))
    w = rng.uniform(0.5, 1.5, K)
    a = np.ones(K, int)
    n_non = rng.integers(0, 2, K)          # some non-Voice types (a = 0)
    a[n_non == 1] = 0
    a[-1] = 1                              # keep at least one Voice type
    bstar = b0 + np.sort(rng.uniform(0.01, 0.09, K))   # strictly increasing
    n = np.sort(rng.integers(1, H + 2, K))[::-1]       # weakly decreasing
    return Model(H, b0, s, w, a, bstar, n)


# ---------------------------------------------------------------------- B ---

FLOW = (-1, 0, 1, 2, 3)          # supp X at order size two, one lump = 1


def flow_law(mark, kappa):
    """P(X = x | mark) for x in FLOW."""
    p = np.zeros(5)
    base = 2 if mark else 0
    for z, pz in ((-1, kappa / 2.0), (0, 1.0 - kappa), (1, kappa / 2.0)):
        p[FLOW.index(base + z)] += pz
    return p


def experiment(mod, tau, T, kappa, d):
    """Tagged date-d experiment: rows = types, columns = flagged tuples then flows.

    Returns (L, tuple_keys, histories).  A flagged column is a distinct
    (B^F, Q^F) pair among the types the rule flags by date d.
    """
    clocks = [mod.clock(i, tau, T) for i in range(mod.K)]
    flagged = [i for i in range(mod.K) if clocks[i][2] == 1 and clocks[i][1] <= d]
    keys = []
    for i in flagged:
        k = (round(clocks[i][3], 12), round(clocks[i][4], 12))
        if k not in keys:
            keys.append(k)
    hists = list(itertools.product(range(5), repeat=d + 1))
    L = np.zeros((mod.K, len(keys) + len(hists)))
    for i in range(mod.K):
        if i in flagged:
            k = (round(clocks[i][3], 12), round(clocks[i][4], 12))
            L[i, keys.index(k)] = 1.0
            continue
        m = mod.marks(i)
        laws = [flow_law(m[e], kappa) for e in range(d + 1)]
        for j, h in enumerate(hists):
            pr = 1.0
            for e in range(d + 1):
                pr *= laws[e][h[e]]
            L[i, len(keys) + j] = pr
    return L, keys, hists


# ---------------------------------------------------------------------- C ---

def memo_kernel(mod, tight, loose, kappa, d):
    """The memo's K_d, built from the tighter output alone.

    Returns (K, note).  note is 'fiber-collision' when two tighter-flagged
    types share a tuple, which is exactly the failure of (S14).
    """
    tau_p, T_p = tight
    tau_m, T_m = loose
    Lp, keys_p, hists = experiment(mod, tau_p, T_p, kappa, d)
    Lm, keys_m, _ = experiment(mod, tau_m, T_m, kappa, d)
    cl_p = [mod.clock(i, tau_p, T_p) for i in range(mod.K)]
    cl_m = [mod.clock(i, tau_m, T_m) for i in range(mod.K)]

    owner = {}
    for i in range(mod.K):
        if cl_p[i][2] == 1 and cl_p[i][1] <= d:
            k = (round(cl_p[i][3], 12), round(cl_p[i][4], 12))
            owner.setdefault(k, []).append(i)
    note = "ok"
    for k, v in owner.items():
        if len(v) > 1:
            note = "fiber-collision"

    K = np.zeros((Lp.shape[1], Lm.shape[1]))
    # pooled columns: the identity on the core history
    for j in range(len(hists)):
        K[len(keys_p) + j, len(keys_m) + j] = 1.0
    # flagged columns: recover the type, then emit or redraw
    for k, v in owner.items():
        i = v[0]                       # the decoder; ill-defined if len(v) > 1
        row = keys_p.index(k)
        if cl_m[i][2] == 1 and cl_m[i][1] <= d:
            km = (round(cl_m[i][3], 12), round(cl_m[i][4], 12))
            K[row, keys_m.index(km)] = 1.0
        else:
            m = mod.marks(i)
            laws = [flow_law(m[e], kappa) for e in range(d + 1)]
            for j, h in enumerate(hists):
                pr = 1.0
                for e in range(d + 1):
                    pr *= laws[e][h[e]]
                K[row, len(keys_m) + j] = pr
    return K, Lp, Lm, note


# ---------------------------------------------------------------------- D ---

def reduce_experiment(L, tol=1e-12):
    """Canonical form: drop null columns, merge columns with the same direction."""
    cols = {}
    out = []
    for j in range(L.shape[1]):
        c = L[:, j]
        t = c.sum()
        if t <= tol:
            continue
        key = tuple(np.round(c / t, 10))
        if key in cols:
            out[cols[key]] += c
        else:
            cols[key] = len(out)
            out.append(c.copy())
    return np.array(out).T if out else np.zeros((L.shape[0], 0))


def is_garbling(L_from, L_to, tol=1e-9):
    """True when some row-stochastic K has L_from K = L_to (Blackwell test)."""
    A = reduce_experiment(L_from)
    B = reduce_experiment(L_to)
    n, p = A.shape[1], B.shape[1]
    nv = n * p
    rows, cols, vals, rhs = [], [], [], []
    r = 0
    for i in range(A.shape[0]):
        for j in range(p):
            for y in range(n):
                if abs(A[i, y]) > 0:
                    rows.append(r); cols.append(y * p + j); vals.append(A[i, y])
            rhs.append(B[i, j])
            r += 1
    for y in range(n):
        for j in range(p):
            rows.append(r); cols.append(y * p + j); vals.append(1.0)
        rhs.append(1.0)
        r += 1
    from scipy.sparse import coo_matrix
    Aeq = coo_matrix((vals, (rows, cols)), shape=(r, nv)).tocsc()
    res = linprog(np.zeros(nv), A_eq=Aeq, b_eq=np.array(rhs),
                  bounds=(0, 1), method="highs")
    if not res.success:
        return False, None
    K = res.x.reshape(n, p)
    return float(np.max(np.abs(A @ K - B))) < tol, K


# ---------------------------------------------------------------------- E ---

def necessity_example(kappa):
    """The memo's two-type clock example: H = 2, tau = 1, T' = 1, T = 2.

    Paths B_L = (0, 0, 1, 2) and B_U = (0, 1/2, 1, 2) at dates (-1, 0, 1, 2),
    coarsening Gamma(x) = 1{x >= 3/4}.  Both flag at the shorter clock with the
    same tuple (2, 0, 1); the longer clock pools them with different marks.
    """
    H = 2
    BL = [0.0, 0.0, 1.0, 2.0]
    BU = [0.0, 0.5, 1.0, 2.0]
    mL = [1 if BL[d + 1] - BL[d] >= 0.75 else 0 for d in range(H + 1)]
    mU = [1 if BU[d + 1] - BU[d] >= 0.75 else 0 for d in range(H + 1)]
    tau, Tp, Tm = 1.0, 1, 2
    cL = min(d for d in range(H + 1) if BL[d + 1] >= tau)
    cU = min(d for d in range(H + 1) if BU[d + 1] >= tau)
    flagged_short = (cL + Tp <= H, cU + Tp <= H)
    flagged_long = (cL + Tm <= H, cU + Tm <= H)
    tupleL = (BL[cL + Tp + 1], 2.0 - BL[cL + Tp + 1])
    tupleU = (BU[cU + Tp + 1], 2.0 - BU[cU + Tp + 1])
    hists = list(itertools.product(range(5), repeat=H + 1))
    Lp = np.zeros((2, 1))
    Lp[:, 0] = 1.0                       # one constant flagged tuple
    Lm = np.zeros((2, len(hists)))
    for r, m in enumerate((mL, mU)):
        laws = [flow_law(m[e], kappa) for e in range(H + 1)]
        for j, h in enumerate(hists):
            pr = 1.0
            for e in range(H + 1):
                pr *= laws[e][h[e]]
            Lm[r, j] = pr
    ok, _ = is_garbling(Lp, Lm)
    return {
        "marks_short": mL, "marks_long": mU,
        "crossing": [cL, cU],
        "flagged_short": [bool(x) for x in flagged_short],
        "flagged_long": [bool(x) for x in flagged_long],
        "tuples_equal": bool(np.allclose(tupleL, tupleU)),
        "tighter_garbles_to_looser": bool(ok),
        "looser_rows_differ": float(np.max(np.abs(Lm[0] - Lm[1]))),
    }


def three_type_cross(kappa_lo, kappa_hi):
    """Cross comparison: tighter at kappa_hi against looser at kappa_lo.

    Types A, B share a mark path; the tighter clock flags A only.  C differs
    from them in one round.
    """
    H = 2
    marks = {"A": [1, 1, 0], "B": [1, 1, 0], "C": [1, 0, 0]}
    hists = list(itertools.product(range(5), repeat=H + 1))

    def pooled_rows(kappa, names):
        L = np.zeros((len(names), len(hists)))
        for r, nm in enumerate(names):
            laws = [flow_law(marks[nm][e], kappa) for e in range(H + 1)]
            for j, h in enumerate(hists):
                pr = 1.0
                for e in range(H + 1):
                    pr *= laws[e][h[e]]
                L[r, j] = pr
        return L

    names = ["A", "B", "C"]
    L_loose = pooled_rows(kappa_lo, names)                       # all pooled
    L_tight = np.zeros((3, 1 + len(hists)))
    L_tight[0, 0] = 1.0                                          # A flagged
    L_tight[1:, 1:] = pooled_rows(kappa_hi, ["B", "C"])
    a, _ = is_garbling(L_tight, L_loose)
    b, _ = is_garbling(L_loose, L_tight)
    return {"kappa_lo": kappa_lo, "kappa_hi": kappa_hi,
            "tight_hi_garbles_to_loose_lo": bool(a),
            "loose_lo_garbles_to_tight_hi": bool(b)}


# ---------------------------------------------------------------------- F ---

def calibration_facts():
    """b* strictly increasing on the flagged region, and B^F + Q^F = b*(s)."""
    from numerical_v4.menu import (VOICE, atoms, b_star, b_star_prime,
                                   legal_clock, a7_certificate)
    from numerical_v4.params import ParamsV4
    prov = json.load(open("numerical_v4/checks/t2_threshold_revelation_check.json")
                     )["provenance"]
    k = tuple(prov["frozen_k"])
    out = {}
    for T in prov["T_grid"]:
        for tau in prov["tau_ladder"]:
            p = ParamsV4(tau=float(tau), T=int(T))
            al = atoms(k, p)
            cert = a7_certificate(k, p, al)
            err = 0.0
            flagged_s = []
            for at in al:
                if at.D != 1:
                    continue
                for s in np.linspace(at.lo, at.hi, 9)[1:-1]:
                    cl = legal_clock(VOICE, float(s), p)
                    if cl.D != 1:
                        continue
                    err = max(err, abs(cl.B_F + cl.Q_F - float(b_star(float(s), p))))
                    flagged_s.append(float(s))
            out[f"T={T},tau={tau:.6f}"] = {
                "omega": float(sum(a.w for a in al if a.D == 1)),
                "min_slope": cert.min_slope,
                "collisions": cert.n_collisions,
                "max_|BF+QF-bstar|": err,
                "n_flagged_atoms": cert.n_flagged_atoms,
            }
    # nesting of the flagged signal sets in tau and in T
    p0 = ParamsV4(tau=float(prov["tau_ladder"][2]), T=5)
    grid = np.linspace(p0.mu_v - 5 * p0.sigma_s, p0.mu_v + 5 * p0.sigma_s, 4001)

    def flagged_mask(tau, T):
        p = ParamsV4(tau=float(tau), T=int(T))
        return np.array([legal_clock(VOICE, float(s), p).D == 1 for s in grid])

    tau_hi, tau_lo = prov["tau_ladder"][3], prov["tau_ladder"][1]
    nest_tau = bool(np.all(flagged_mask(tau_hi, 5) <= flagged_mask(tau_lo, 5)))
    nest_T = bool(np.all(flagged_mask(tau_hi, 10) <= flagged_mask(tau_hi, 5)))
    out["nesting"] = {"tighter_threshold_flags_more": nest_tau,
                      "shorter_clock_flags_more": nest_T}
    return out


# --------------------------------------------------------------------------

def main():
    rec = {}

    # C: the memo's kernel against the looser experiment, random instances
    worst = 0.0
    fails = []
    n_case = 0
    for trial in range(60):
        mod = random_model(H=2, K=5)
        taus = sorted(set(np.round(RNG.uniform(0.035, 0.095, 3), 6)))
        for tau_lo, tau_hi in itertools.combinations(taus, 2):
            for T in (1, 2):
                for kappa in (0.0, 0.15, 0.5, 0.85, 1.0):
                    for d in range(mod.H + 1):
                        # threshold margin: tighter is the lower tau
                        K, Lp, Lm, note = memo_kernel(
                            mod, (tau_lo, T), (tau_hi, T), kappa, d)
                        err = float(np.max(np.abs(Lp @ K - Lm)))
                        n_case += 1
                        worst = max(worst, err)
                        if err > 1e-12 or note != "ok":
                            fails.append(["tau", trial, tau_lo, tau_hi, T,
                                          kappa, d, err, note])
        for tau in taus:
            for Tp, Tm in ((1, 2), (1, 3), (2, 3)):
                for kappa in (0.0, 0.15, 0.5, 0.85, 1.0):
                    for d in range(mod.H + 1):
                        K, Lp, Lm, note = memo_kernel(
                            mod, (tau, Tp), (tau, Tm), kappa, d)
                        err = float(np.max(np.abs(Lp @ K - Lm)))
                        n_case += 1
                        worst = max(worst, err)
                        if err > 1e-12 or note != "ok":
                            fails.append(["T", trial, tau, Tp, Tm, kappa, d,
                                          err, note])
    rec["kernel_check"] = {"cases": n_case, "max_error": worst,
                           "failures": fails[:20], "n_failures": len(fails)}

    # C2: the same instances, independent LP confirmation on a subset
    lp_ok = True
    lp_cases = 0
    for trial in range(6):
        mod = random_model(H=2, K=4)
        for kappa in (0.15, 0.5, 0.85):
            Lp, _, _ = experiment(mod, 0.045, 1, kappa, mod.H)
            Lm, _, _ = experiment(mod, 0.075, 1, kappa, mod.H)
            ok, _ = is_garbling(Lp, Lm)
            lp_cases += 1
            lp_ok = lp_ok and ok
            Lp2, _, _ = experiment(mod, 0.06, 1, kappa, mod.H)
            Lm2, _, _ = experiment(mod, 0.06, 2, kappa, mod.H)
            ok2, _ = is_garbling(Lp2, Lm2)
            lp_cases += 1
            lp_ok = lp_ok and ok2
    rec["lp_confirmation"] = {"cases": lp_cases, "all_feasible": bool(lp_ok)}

    # C3: posterior variance corollary on the same instances
    def evar(L, w, x):
        post_num = L * w[:, None] * x[:, None]
        mass = (L * w[:, None]).sum(axis=0)
        live = mass > 1e-15
        m1 = np.zeros_like(mass)
        m1[live] = post_num.sum(axis=0)[live] / mass[live]
        ex2 = np.zeros_like(mass)
        num2 = (L * w[:, None] * (x ** 2)[:, None]).sum(axis=0)
        ex2[live] = num2[live] / mass[live]
        return float(np.sum(mass[live] * (ex2[live] - m1[live] ** 2)))

    bad_var = []
    for trial in range(15):
        mod = random_model(H=2, K=5)
        for kappa in (0.15, 0.5, 0.85):
            Lp, _, _ = experiment(mod, 0.045, 1, kappa, mod.H)
            Lm, _, _ = experiment(mod, 0.075, 1, kappa, mod.H)
            vp = evar(Lp, mod.w, mod.a.astype(float))
            vm = evar(Lm, mod.w, mod.a.astype(float))
            if vp > vm + 1e-12:
                bad_var.append([trial, kappa, vp, vm])
    rec["posterior_variance"] = {"violations": bad_var}

    # E: the necessity example and the cross comparison
    rec["necessity_example"] = {str(k): necessity_example(k)
                                for k in (0.0, 0.3, 0.5, 1.0)}
    rec["cross_comparison"] = [three_type_cross(a, b) for a, b in
                               ((0.0, 1.0), (0.15, 0.85), (0.3, 0.7),
                                (0.45, 0.55))]

    # F: calibration facts
    rec["calibration"] = calibration_facts()

    with open(OUT, "w") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print(json.dumps(rec, indent=1, default=str)[:6000])


if __name__ == "__main__":
    main()
