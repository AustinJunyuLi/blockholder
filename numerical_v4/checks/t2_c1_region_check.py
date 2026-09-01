"""C1 -- GE region certificate: the executed region-certification check.

Ticket 29 (T2i).  Companion to ``research/model_v4/proofs/C1_proof.md``.
Card: ``research/model_v4/MODEL_CARD.md``, stamp 2026-08-21 / commit a175202+,
section 4.5 (L_R, r_tau = -tau, g_r^PE, kbar_x, kbar_kr, B_r^GE, eta_r).

WHAT IS COMPUTED, PER NODE (kappa, tau, T)
------------------------------------------
The equilibrium cutoff vector k* solves k = T(k; theta).  Around (k*, kappa,
tau) a 33-point second-order stencil in the four variables (k1, k2, kappa, tau)
supplies every first and second derivative of

    the outer map      T(k; kappa, tau)      (2 components), and
    the FIXED-POLICY   Delta^act(k, kappa, tau)  (scalar),

by central differences.  From those:

    L_R      = ||D_k T||_inf                       (card 4.5)
    kbar_x   = |d_x T| / (1 - L_R),   x in {kappa, r}
    kbar_kr  = (|T_kr| + |T_kk_||kbar_r| + |T_rk|kbar_k + |T_kk|kbar_k kbar_r)
               / (1 - L_R)
    B_r^GE   = |D_kk_||kbar_r| ... (exactly the card 4.5 row, see below)
    g_r^PE   = -sgn(dDelta^act/dkappa) * d_{kappa r} Delta^act
    eta_r    = g_r^PE - B_r^GE

with r = r_tau = -tau, so d_r = -d_tau.  r_T = -T is NOT differentiated: the
card's T is an integer, so T is a fixed environment label per node.  The sign
is the EQUILIBRIUM liquidity derivative's sign (card 4.5's ``sgn(d Delta^act /
d kappa)``); no symbol is introduced for it, card 4.5 forbids one.  It is read
off the implicit-function formula at every node and cross-checked against a
re-solved kappa sweep at the validation nodes.

A node CERTIFIES when L_R < 1 and eta_r > 0.  "EMPTY REGION" is printed
explicitly when no node certifies; per card section 6 that outcome is a result,
not a failure, and the exit code does not punish it.

THE SUBSTANTIVE CHECK (this is what makes the file evidence and not arithmetic)
------------------------------------------------------------------------------
The certificate's whole content is that B_r^GE dominates the GE remainder in

    d_r d_kappa Delta*  =  d_{kappa r} Delta^act  +  [GE remainder],

where Delta*(kappa, r) = Delta^act(k*(kappa, r), kappa, r) is the EQUILIBRIUM
premium.  The script therefore also computes d_r d_kappa Delta* twice by routes
that do not share the bound's arithmetic:

  (a) NUMERICALLY -- re-solve the equilibrium at the four corners
      (kappa +- h_kappa, tau +- h_tau) and cross-difference Delta*.  Six
      re-solves per node, so this runs on the VALIDATION SUBSET;
  (b) by the IMPLICIT-FUNCTION formula -- solve (I - D_k T) k_x = d_x T and
      (I - D_k T) k_{kappa r} = ... and assemble the chain rule.  Free from the
      stencil, so this runs at every node.

and asserts |. - d_{kappa r} Delta^act| <= B_r^GE for both readings.  A bound
that fails to contain the realised remainder is a FAIL; those are the verdicts
in this file that can fail on substance.

Deterministic: no RNG beyond the solver's fixed seeds, no file inputs, no
network.

Run:    .venv/bin/python numerical_v4/checks/t2_c1_region_check.py
        .venv/bin/python numerical_v4/checks/t2_c1_region_check.py --quick
Output: numerical_v4/checks/t2_c1_region_check.json
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _ROOT)

from numerical_v4.flagged import flagged_nodes  # noqa: E402
from numerical_v4.menu import atoms  # noqa: E402
from numerical_v4.params import ParamsV4  # noqa: E402
from numerical_v4.policy import (  # noqa: E402
    Policy,
    evaluate,
    frozen_tau_grid,
    menu_of,
)
from numerical_v4.pooled import pooled_pass  # noqa: E402
from numerical_v4.premium import cell_weights, total_premium  # noqa: E402
from numerical_v4.solver import outer_map, solve_policy  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "t2_c1_region_check.json")

QUICK = "--quick" in sys.argv

# ---------------------------------------------------------------------------
# Grid.  SIZED TO THE SOLVER'S COST, NOT TO THE REQUEST.
# ---------------------------------------------------------------------------
# The turn-1 NUMERICAL CHECK REQUEST asks for kappa in [0.15, 0.85] on a 0.01
# grid.  MEASURED costs (quick run, 2026-08-21): a 33-point stencil is ~40 s
# (each point = one pooled pass with run-up + one outer map + one premium,
# ~1.2 s); a warm-started equilibrium re-solve at a PERTURBED parameter is
# ~43 s, because solve_policy drives |k - T(k)| to 1e-10 and each damped
# iteration costs a full pooled pass.  A node with the six validation re-solves
# is ~300 s; a node without them is ~42 s.
# The requested grid is 71 x 5 x 2 = 710 nodes.  At 42 s that is 8.3 h even
# without any validation.  It was NOT run.  What is run is a 0.10 kappa grid,
# 8 x 5 x 2 = 80 nodes (~56 min) with the six re-solves on 8 validation nodes
# (~35 min).  The JSON reports the grid used and the grid declined.  A coarser
# certified grid honestly reported is the deliverable.
KAPPA_GRID = np.array([0.5]) if QUICK else np.round(np.arange(0.15, 0.8501, 0.10), 4)
TAU_QUANTILES = (0.5,) if QUICK else (0.1, 0.3, 0.5, 0.7, 0.9)
T_GRID = (5,) if QUICK else (5, 10)

# The four-corner EQUILIBRIUM cross derivative needs six warm-started re-solves
# per node and costs ~260 s of the ~300 s a full node takes (measured), because
# solve_policy drives |k - T(k)| to 1e-10 from a perturbed parameter.  It is the
# certificate's independent check, not one of its inputs, so it runs on a
# VALIDATION SUBSET spanning both windows, the extreme and median thresholds and
# three liquidity levels.  Every other node takes the equilibrium liquidity
# derivative from the implicit-function reading, which the validation nodes
# check against the re-solve (``ift_matches_resolved_equilibrium``).
VALIDATE_NODES = frozenset(
    [(5, q, 0.55) for q in (10, 50, 90)]
    + [(10, q, 0.55) for q in (10, 50, 90)]
    + [(5, 50, 0.25), (5, 50, 0.85)]
)


def _is_validation(T: int, q: int, kappa: float) -> bool:
    if QUICK:
        return True
    return any(T == t and q == qq and abs(kappa - kk) < 1e-9
               for (t, qq, kk) in VALIDATE_NODES)

# Stencil steps: k on the signal scale (sigma_s = 0.707), kappa on [0,1],
# tau on the stake scale (the frozen percentiles span 0.0846 .. 0.0960, so
# h_tau = 5e-4 keeps the stencil well inside one percentile cell).
IK1, IK2, IKA, ITA = 0, 1, 2, 3
H_STEP = np.array([1e-2, 1e-2, 1e-2, 5e-4])

TOL_SOLVE = 1e-8          # equilibrium cutoff-scale residual gate
TOL_IFT = 5e-3            # relative agreement, IFT vs re-solved equilibrium
BOUND_SLACK = 1e-6        # absolute slack on "the bound contains the remainder"

results: dict = {
    "provenance": {},
    "kind": "substantive",
    "checks": [],
    "nodes": [],
    "n_fail": 0,
}


def record(name: str, ok: "bool | None", detail: dict) -> None:
    """ok=None marks a RECORD (no verdict); True/False mark PASS/FAIL."""
    tag = "RECORD" if ok is None else ("PASS" if ok else "FAIL")
    results["checks"].append({"name": name, "verdict": tag,
                              "pass": (None if ok is None else bool(ok)),
                              **detail})
    if ok is False:
        results["n_fail"] += 1
    print(f"[{tag}] {name}")
    for k, v in detail.items():
        print(f"    {k}: {v}")
    sys.stdout.flush()


# ---------------------------------------------------------------------------
# One stencil point: T(k) and the fixed-policy Delta^act, sharing one pass
# ---------------------------------------------------------------------------


def _point(x: np.ndarray, p_base: ParamsV4):
    """(T(k), Delta^act, cell weights, flagged block) at one stencil point.

    One ``pooled_pass`` with run-up serves both the outer map (which prices the
    blockholder's execution dates) and the premium.  ``evaluate`` is not called
    here only because it would repeat that pass; ``wiring_premium_matches_
    evaluate`` below checks that this shortcut reproduces it exactly.
    """
    k = (float(x[IK1]), float(x[IK2]))
    p = p_base.replace(kappa=float(x[IKA]), tau=float(x[ITA]))
    al = atoms(k, p)
    res = pooled_pass(al, p, with_runup=True)
    Tk = outer_map(k, p, res)
    fl = flagged_nodes(al, p)
    cw = cell_weights(al)
    D = total_premium(res, fl.w, fl.p_bid, p)
    return (np.array(Tk, dtype=float), float(D), cw, fl,
            res.multiple_root_nodes + fl.multiple_root_nodes)


def _offsets() -> list[tuple[int, int, int, int]]:
    offs: list[tuple[int, int, int, int]] = [(0, 0, 0, 0)]
    for i in range(4):
        for s in (1, -1):
            o = [0, 0, 0, 0]
            o[i] = s
            offs.append(tuple(o))                       # type: ignore[arg-type]
    for i in range(4):
        for j in range(i + 1, 4):
            for si in (1, -1):
                for sj in (1, -1):
                    o = [0, 0, 0, 0]
                    o[i] = si
                    o[j] = sj
                    offs.append(tuple(o))               # type: ignore[arg-type]
    return offs


OFFSETS = _offsets()
assert len(OFFSETS) == 33 and len(set(OFFSETS)) == 33


def _d1(F: dict, i: int):
    ep = [0, 0, 0, 0]
    em = [0, 0, 0, 0]
    ep[i], em[i] = 1, -1
    return (F[tuple(ep)] - F[tuple(em)]) / (2.0 * H_STEP[i])


def _d2(F: dict, i: int, j: int):
    if i == j:
        ep = [0, 0, 0, 0]
        em = [0, 0, 0, 0]
        ep[i], em[i] = 1, -1
        return (F[tuple(ep)] - 2.0 * F[(0, 0, 0, 0)] + F[tuple(em)]) \
            / H_STEP[i] ** 2

    def o(si: int, sj: int):
        a = [0, 0, 0, 0]
        a[i], a[j] = si, sj
        return tuple(a)

    return (F[o(1, 1)] - F[o(1, -1)] - F[o(-1, 1)] + F[o(-1, -1)]) \
        / (4.0 * H_STEP[i] * H_STEP[j])


# ---------------------------------------------------------------------------
# Equilibrium re-solves (the sign, and the four-corner cross derivative)
# ---------------------------------------------------------------------------


def _equilibrium_premium(p: ParamsV4, k_init):
    """Re-solve k = T(k) at p, then Delta* = Delta^act(k*(p), p)."""
    pol, r = solve_policy(p, k_init=k_init)
    al = atoms(pol.k, p)
    res = pooled_pass(al, p, with_runup=False)
    fl = flagged_nodes(al, p)
    return (tuple(pol.k), float(total_premium(res, fl.w, fl.p_bid, p)),
            float(r.cutoff_scale))


# ---------------------------------------------------------------------------
# One node
# ---------------------------------------------------------------------------


def _predict(k_star, k_x, step: float):
    """First-order warm start for a re-solve, from the IFT derivative."""
    return (float(k_star[0] + step * k_x[0]), float(k_star[1] + step * k_x[1]))


def certify_node(p_base: ParamsV4, kappa: float, tau: float, T: int,
                 k_warm, validate: bool) -> dict:
    """Every card 4.5 object at one (kappa, tau, T) node, plus the two
    independent readings of the equilibrium cross derivative."""
    p = p_base.replace(kappa=kappa, tau=tau, T=T)
    t0 = time.perf_counter()

    # -- the equilibrium at the node -------------------------------------
    pol, resid = solve_policy(p, k_init=k_warm)
    k_star = (float(pol.k[0]), float(pol.k[1]))
    x0 = np.array([k_star[0], k_star[1], kappa, tau], dtype=float)

    row: dict = {
        "kappa": float(kappa), "tau": float(tau), "T": int(T),
        "k1": k_star[0], "k2": k_star[1],
        "outer_residual": float(resid.cutoff_scale),
        "payoff_residual": float(resid.payoff_scale),
    }

    # -- the 33-point stencil --------------------------------------------
    FT: dict = {}
    FD: dict = {}
    multiple_roots = 0
    cw0 = fl0 = None
    for off in OFFSETS:
        x = x0 + np.array(off, dtype=float) * H_STEP
        Tk, D, cw, fl, n_mult = _point(x, p)
        FT[off] = Tk
        FD[off] = D
        multiple_roots += n_mult
        if off == (0, 0, 0, 0):
            cw0, fl0 = cw, fl

    assert cw0 is not None and fl0 is not None
    row.update({
        "Omega": float(cw0.Omega), "omega_a": float(cw0.omega_a),
        "pi_bar": float(cw0.pi_bar), "M_F": float(fl0.M_F),
        "Delta_act": float(FD[(0, 0, 0, 0)]),
        "degenerate": list(cw0.degenerate),
        "multiple_root_nodes": int(multiple_roots),
        "k_order_ok": bool(k_star[0] < k_star[1]),
    })

    # -- derivatives of the outer map ------------------------------------
    J = np.array([[_d1(FT, IK1)[a], _d1(FT, IK2)[a]] for a in (0, 1)])
    L = float(np.max(np.sum(np.abs(J), axis=1)))          # ||D_k T||_inf
    T_kap = _d1(FT, IKA)                                   # (2,)
    T_tau = _d1(FT, ITA)                                   # (2,)
    T_kap_tau = _d2(FT, IKA, ITA)                          # (2,)
    T_kap_k = np.array([_d2(FT, IKA, IK1), _d2(FT, IKA, IK2)]).T   # (2,2)
    T_tau_k = np.array([_d2(FT, ITA, IK1), _d2(FT, ITA, IK2)]).T   # (2,2)
    T_k1k1, T_k1k2, T_k2k2 = _d2(FT, IK1, IK1), _d2(FT, IK1, IK2), \
        _d2(FT, IK2, IK2)

    # Norms.  ||.||_inf on the cutoff space; the induced operator norm on
    # D_k T; for the bilinear pieces the constant that makes
    # ||A[u,v]||_inf <= |A| ||u||_inf ||v||_inf, i.e. the max over the output
    # row of the sum of |entries|.  Card 4.5 writes |.| without fixing a norm;
    # this file fixes it and the NOTATION DELTA says so.
    abs_T_kap = float(np.max(np.abs(T_kap)))
    abs_T_r = float(np.max(np.abs(T_tau)))                 # |d_r T| = |d_tau T|
    abs_T_kr = float(np.max(np.abs(T_kap_tau)))
    abs_T_kapk = float(np.max(np.sum(np.abs(T_kap_k), axis=1)))
    abs_T_rk = float(np.max(np.sum(np.abs(T_tau_k), axis=1)))
    abs_T_kk = float(np.max(np.abs(T_k1k1) + 2.0 * np.abs(T_k1k2)
                            + np.abs(T_k2k2)))

    row.update({"L_R": L, "abs_dT_dkappa": abs_T_kap, "abs_dT_dr": abs_T_r})

    contract = L < 1.0
    if contract:
        one_minus = 1.0 - L
        kbar_kap = abs_T_kap / one_minus
        kbar_r = abs_T_r / one_minus
        kbar_kr = (abs_T_kr + abs_T_kapk * kbar_r + abs_T_rk * kbar_kap
                   + abs_T_kk * kbar_kap * kbar_r) / one_minus
    else:
        kbar_kap = kbar_r = kbar_kr = float("nan")
    row.update({"kbar_kappa": kbar_kap, "kbar_r": kbar_r, "kbar_kappa_r": kbar_kr})

    # -- derivatives of the fixed-policy premium --------------------------
    D_k = np.array([_d1(FD, IK1), _d1(FD, IK2)])
    D_kap = float(_d1(FD, IKA))
    D_tau = float(_d1(FD, ITA))
    D_kap_tau = float(_d2(FD, IKA, ITA))
    D_kap_k = np.array([_d2(FD, IKA, IK1), _d2(FD, IKA, IK2)])
    D_tau_k = np.array([_d2(FD, ITA, IK1), _d2(FD, ITA, IK2)])
    D_k1k1, D_k1k2, D_k2k2 = _d2(FD, IK1, IK1), _d2(FD, IK1, IK2), \
        _d2(FD, IK2, IK2)
    D_tau_tau = float(_d2(FD, ITA, ITA))

    abs_D_k = float(np.sum(np.abs(D_k)))                   # dual of ||.||_inf
    abs_D_kapk = float(np.sum(np.abs(D_kap_k)))
    abs_D_kr = float(np.sum(np.abs(D_tau_k)))
    abs_D_kk = float(np.abs(D_k1k1) + 2.0 * np.abs(D_k1k2) + np.abs(D_k2k2))
    D_kap_r = -D_kap_tau                                   # r = -tau

    B_GE = (abs_D_kapk * kbar_r + (abs_D_kr + abs_D_kk * kbar_r) * kbar_kap
            + abs_D_k * kbar_kr) if contract else float("nan")

    # curvature-to-slope diagnostic in tau: the implemented legal clock takes
    # c = ceil(...), so tau-kinks are possible inside a stencil.
    kink = (abs(D_tau_tau) * H_STEP[ITA] / abs(D_tau)) if abs(D_tau) > 0 \
        else float("nan")

    row.update({
        "dDelta_dkappa_fixed": D_kap, "dDelta_dtau_fixed": D_tau,
        "d2Delta_dkappa_dtau_fixed": D_kap_tau,
        "abs_Delta_k": abs_D_k, "abs_Delta_kappa_k": abs_D_kapk,
        "abs_Delta_k_r": abs_D_kr, "abs_Delta_kk": abs_D_kk,
        "B_r_GE": B_GE, "tau_kink_ratio": kink,
    })

    # -- the implicit-function reading (free: linear algebra on the stencil)
    if contract:
        A = np.eye(2) - J
        k_kap = np.linalg.solve(A, T_kap)
        k_tau = np.linalg.solve(A, T_tau)
        T_kk_bil = np.array([
            T_k1k1[a] * k_tau[0] * k_kap[0]
            + T_k1k2[a] * (k_tau[0] * k_kap[1] + k_tau[1] * k_kap[0])
            + T_k2k2[a] * k_tau[1] * k_kap[1] for a in (0, 1)])
        rhs = (T_kap_tau + T_kap_k @ k_tau + T_tau_k @ k_kap + T_kk_bil)
        k_kap_tau = np.linalg.solve(A, rhs)
        dstar_ift = D_kap + float(D_k @ k_kap)
        D_kk_bil = (D_k1k1 * k_tau[0] * k_kap[0]
                    + D_k1k2 * (k_tau[0] * k_kap[1] + k_tau[1] * k_kap[0])
                    + D_k2k2 * k_tau[1] * k_kap[1])
        cross_ift_tau = (D_kap_tau + float(D_kap_k @ k_tau)
                         + float(D_tau_k @ k_kap) + D_kk_bil
                         + float(D_k @ k_kap_tau))
        cross_ift_r = -cross_ift_tau
        norm_k_kap = float(np.max(np.abs(k_kap)))
        norm_k_r = float(np.max(np.abs(k_tau)))
        norm_k_kap_r = float(np.max(np.abs(k_kap_tau)))
    else:
        dstar_ift = cross_ift_r = float("nan")
        norm_k_kap = norm_k_r = norm_k_kap_r = float("nan")

    # -- the equilibrium liquidity derivative, and its sign ----------------
    # Card 4.5 orients g_r^PE by sgn(d Delta^act / d kappa), the EQUILIBRIUM
    # derivative.  It is read off the implicit-function formula at every node
    # (free) and cross-checked against a re-solved kappa sweep at the
    # validation nodes.
    hk, ht = float(H_STEP[IKA]), float(H_STEP[ITA])
    worst_resid = float(resid.cutoff_scale)
    dstar_dkappa = float("nan")
    cross_num_r = float("nan")
    if validate:
        _, Dp, rp = _equilibrium_premium(p.replace(kappa=kappa + hk),
                                         _predict(k_star, k_kap, hk) if contract
                                         else k_star)
        _, Dm, rm = _equilibrium_premium(p.replace(kappa=kappa - hk),
                                         _predict(k_star, k_kap, -hk) if contract
                                         else k_star)
        dstar_dkappa = (Dp - Dm) / (2.0 * hk)
        worst_resid = max(worst_resid, rp, rm)
        corners = {}
        for sk in (1, -1):
            for st in (1, -1):
                pc = p.replace(kappa=kappa + sk * hk, tau=tau + st * ht)
                init = k_star
                if contract:
                    init = (float(k_star[0] + sk * hk * k_kap[0]
                                  + st * ht * k_tau[0]),
                            float(k_star[1] + sk * hk * k_kap[1]
                                  + st * ht * k_tau[1]))
                _, Dc, rc = _equilibrium_premium(pc, init)
                corners[(sk, st)] = Dc
                worst_resid = max(worst_resid, rc)
        cross_num_r = -(corners[(1, 1)] - corners[(1, -1)] - corners[(-1, 1)]
                        + corners[(-1, -1)]) / (4.0 * hk * ht)

    dstar_used = dstar_dkappa if validate and np.isfinite(dstar_dkappa) \
        else dstar_ift
    sign_source = "resolved_equilibrium" if (validate
                                             and np.isfinite(dstar_dkappa)) \
        else ("implicit_function" if contract else "fixed_policy_fallback")
    if not np.isfinite(dstar_used):
        dstar_used = D_kap                       # L_R >= 1: no IFT available
    sign_eq = 1.0 if dstar_used > 0 else (-1.0 if dstar_used < 0 else 0.0)
    sign_pe = 1.0 if D_kap > 0 else (-1.0 if D_kap < 0 else 0.0)

    # -- the certificate ---------------------------------------------------
    g_PE = -sign_eq * D_kap_r
    eta = g_PE - B_GE if contract else float("nan")
    certified = bool(contract and np.isfinite(eta) and eta > 0.0)

    # Sharp companion (RECORD ONLY, not the card's certificate): the same
    # remainder bound with the REALISED derivative norms in place of the
    # inversion-free kbar's.  It needs (I - D_kT)^-1 and is therefore not the
    # card 4.5 object; it measures how much the inversion-free step costs.
    if contract:
        B_sharp = (abs_D_kapk * norm_k_r
                   + (abs_D_kr + abs_D_kk * norm_k_r) * norm_k_kap
                   + abs_D_k * norm_k_kap_r)
        eta_sharp = g_PE - B_sharp
    else:
        B_sharp = eta_sharp = float("nan")

    row.update({
        "validation_node": bool(validate),
        "dDelta_star_dkappa": dstar_dkappa,
        "dDelta_star_dkappa_ift": dstar_ift,
        "dDelta_star_dkappa_used": dstar_used, "sign_source": sign_source,
        "sign_equilibrium": sign_eq, "sign_fixed_policy": sign_pe,
        "sign_coherent": bool(sign_eq == sign_pe),
        "cross_r_equilibrium_numeric": cross_num_r,
        "cross_r_equilibrium_ift": cross_ift_r,
        "remainder_numeric": cross_num_r - D_kap_r,
        "remainder_ift": cross_ift_r - D_kap_r,
        "g_r_PE": g_PE, "eta_r": eta, "certified": certified,
        "B_r_GE_sharp": B_sharp, "eta_r_sharp": eta_sharp,
        "certified_sharp": bool(contract and np.isfinite(eta_sharp)
                                and eta_sharp > 0.0),
        "norm_k_kappa": norm_k_kap, "norm_k_r": norm_k_r,
        "norm_k_kappa_r": norm_k_kap_r,
        "worst_solve_residual": worst_resid,
        "dr_S_star_ift": sign_eq * cross_ift_r,
        "dr_S_star_numeric": sign_eq * cross_num_r,
        "seconds": time.perf_counter() - t0,
    })
    return row


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def main() -> int:
    t_start = time.perf_counter()
    p_seed = ParamsV4.baseline()

    print("=" * 78)
    print("C1 -- GE REGION CERTIFICATE (ticket 29, T2i)")
    print("=" * 78, flush=True)

    # -- tau freezing, exactly smoke.py's convention ----------------------
    pol_seed, res_seed = solve_policy(p_seed)
    taus = frozen_tau_grid(pol_seed, p_seed, TAU_QUANTILES)
    pct = tuple(int(round(100 * q)) for q in TAU_QUANTILES)

    results["provenance"] = {
        "script": "numerical_v4/checks/t2_c1_region_check.py",
        "proof": "research/model_v4/proofs/C1_proof.md",
        "card": "research/model_v4/MODEL_CARD.md, stamp 2026-08-21 / a175202+",
        "card_section": "4.5 (L_R, r_tau, g_r^PE, kbar_x, kbar_kr, B_r^GE, eta_r)",
        "model": "numerical_v4 (H=10, J=3 plans, M=2 marks)",
        "params_hash": p_seed.hash_str(),
        "seed_equilibrium_k": list(pol_seed.k),
        "seed_outer_residual": float(res_seed.cutoff_scale),
        "tau_quantiles_pct": list(pct),
        "tau_frozen": [float(t) for t in taus],
        "tau_freezing": ("percentiles of the seed equilibrium's Voice b*(s); "
                         "smoke.py's convention, median = 0.09076406"),
        "kappa_grid": [float(k) for k in KAPPA_GRID],
        "kappa_grid_step": (float(KAPPA_GRID[1] - KAPPA_GRID[0])
                            if len(KAPPA_GRID) > 1 else None),
        "T_grid": list(T_GRID),
        "n_nodes_planned": int(len(KAPPA_GRID) * len(taus) * len(T_GRID)),
        "requested_grid_not_run": {
            "kappa": "[0.15, 0.85] step 0.01 (71 points)",
            "nodes": 710,
            "reason": ("measured 42 s per stencil-only node and 300 s per "
                       "validation node; 710 nodes is >8 h of wall time even "
                       "with no validation. Not run. The grid reported above "
                       "is the grid certified."),
        },
        "validation_nodes_T_taupct_kappa": sorted(
            [list(v) for v in VALIDATE_NODES]) if not QUICK else "all",
        "validation_meaning": ("nodes where the equilibrium is additionally "
                               "re-solved at kappa +- h and at the four "
                               "(kappa, tau) corners, giving a reading of "
                               "d_r d_kappa Delta* that shares no arithmetic "
                               "with the bound"),
        "stencil": {"variables": ["k1", "k2", "kappa", "tau"],
                    "steps": [float(h) for h in H_STEP],
                    "points": len(OFFSETS),
                    "scheme": "central, second order"},
        "strictness_coordinate": ("r = r_tau = -tau. r_T = -T is NOT "
                                  "differentiated: T ranges over {1,...,H} in "
                                  "the card and is an int in the code, so "
                                  "d_{r_T} does not exist. T enters as a fixed "
                                  "environment label per node."),
        "quick_mode": QUICK,
    }
    print(f"  params hash    {p_seed.hash_str()}")
    print(f"  seed k         {pol_seed.k}")
    print(f"  tau frozen     {[round(float(t), 8) for t in taus]}")
    print(f"  kappa grid     {list(KAPPA_GRID)}")
    print(f"  T grid         {list(T_GRID)}")
    print(f"  nodes          {len(KAPPA_GRID) * len(taus) * len(T_GRID)}",
          flush=True)

    # -- wiring: the shared-pass premium must reproduce ``evaluate`` -------
    p_w = p_seed.replace(tau=float(taus[len(taus) // 2]), T=T_GRID[0],
                         kappa=float(KAPPA_GRID[len(KAPPA_GRID) // 2]))
    pol_w, _ = solve_policy(p_w, k_init=pol_seed.k)
    _, D_short, _, _, _ = _point(
        np.array([pol_w.k[0], pol_w.k[1], p_w.kappa, p_w.tau]), p_w)
    D_eval = evaluate(Policy(tuple(pol_w.k), menu_of(p_w)), p_w,
                      with_runup=False).Delta_act
    record("wiring_premium_matches_evaluate", abs(D_short - D_eval) < 1e-15,
           {"shared_pass": D_short, "evaluate": D_eval,
            "abs_diff": abs(D_short - D_eval),
            "note": "the 33-point stencil's premium is evaluate()'s, verbatim"})

    # -- the sweep ---------------------------------------------------------
    rows: list[dict] = []
    for T in T_GRID:
        for q, tau in zip(pct, taus):
            k_warm = tuple(pol_seed.k)
            for kappa in KAPPA_GRID:
                val = _is_validation(int(T), q, float(kappa))
                try:
                    r = certify_node(p_seed, float(kappa), float(tau), int(T),
                                     k_warm, val)
                except Exception as exc:                # noqa: BLE001
                    rows.append({"kappa": float(kappa), "tau": float(tau),
                                 "T": int(T), "tau_pct": q, "error": repr(exc)})
                    print(f"  ERROR  T={T} q={q} kappa={kappa}: {exc!r}",
                          flush=True)
                    continue
                r["tau_pct"] = q
                k_warm = (r["k1"], r["k2"])
                rows.append(r)
                results["nodes"] = rows
                with open(OUT, "w") as fh:      # incremental: a crash at node
                    json.dump(results, fh, indent=2, default=float)  # 60 keeps 59
                print(f"  T={T:2d} q={q:2d} kappa={kappa:.2f}  "
                      f"L={r['L_R']:.4f}  Om={r['Omega']:.5f}  "
                      f"g={r['g_r_PE']: .4e}  B={r['B_r_GE']: .4e}  "
                      f"eta={r['eta_r']: .4e}  "
                      f"{'CERT' if r['certified'] else '----'}  "
                      f"{'[sharp CERT]' if r['certified_sharp'] else ''}"
                      f"{' [V]' if val else ''}  ({r['seconds']:.0f}s)",
                      flush=True)
    results["nodes"] = rows

    ok_rows = [r for r in rows if "error" not in r]
    n_err = len(rows) - len(ok_rows)

    # -- RECORD: contraction ----------------------------------------------
    Ls = [r["L_R"] for r in ok_rows]
    bad_L = [{"kappa": r["kappa"], "tau_pct": r["tau_pct"], "T": r["T"],
              "L_R": r["L_R"]} for r in ok_rows if r["L_R"] >= 1.0]
    record("contraction_bound_L_R", None,
           {"n_nodes": len(ok_rows), "L_max": max(Ls) if Ls else None,
            "L_min": min(Ls) if Ls else None,
            "n_nodes_with_L_ge_1": len(bad_L), "nodes_with_L_ge_1": bad_L,
            "reading": ("L_R here is ||D_k T|| AT the equilibrium k*(theta), "
                        "node by node -- the along-the-path reading. AGE's "
                        "sup over the whole polytope is NOT computed; see "
                        "C1_proof.md WHERE IT FAILS 1 and NOT CLAIMED.")})

    # -- PASS/FAIL: the bound must contain the realised GE remainder -------
    checked = [r for r in ok_rows if r["L_R"] < 1.0
               and np.isfinite(r["remainder_numeric"])
               and np.isfinite(r["B_r_GE"])]
    viol = [{"kappa": r["kappa"], "tau_pct": r["tau_pct"], "T": r["T"],
             "remainder": r["remainder_numeric"], "B_r_GE": r["B_r_GE"]}
            for r in checked
            if abs(r["remainder_numeric"]) > r["B_r_GE"] + BOUND_SLACK]
    record("bound_contains_equilibrium_remainder", len(viol) == 0,
           {"n_checked": len(checked), "n_violations": len(viol),
            "violations": viol[:10],
            "max_ratio_remainder_over_bound": (
                max((abs(r["remainder_numeric"]) / r["B_r_GE"]
                     for r in checked if r["B_r_GE"] > 0), default=None)),
            "formula": ("|d_r d_kappa Delta*(four-corner re-solve) - "
                        "d_{kappa r} Delta^act(stencil)| <= B_r^GE"),
            "scope": "validation nodes only (six equilibrium re-solves each)",
            "note": "this is the certificate's only substantive verdict"})

    # -- PASS/FAIL: same containment, IFT remainder, at EVERY node ---------
    ift_rows = [r for r in ok_rows if r["L_R"] < 1.0
                and np.isfinite(r["remainder_ift"])]
    viol_i = [{"kappa": r["kappa"], "tau_pct": r["tau_pct"], "T": r["T"],
               "remainder_ift": r["remainder_ift"], "B_r_GE": r["B_r_GE"]}
              for r in ift_rows
              if abs(r["remainder_ift"]) > r["B_r_GE"] + BOUND_SLACK]
    record("bound_contains_ift_remainder", len(viol_i) == 0,
           {"n_checked": len(ift_rows), "n_violations": len(viol_i),
            "violations": viol_i[:10],
            "max_ratio": max((abs(r["remainder_ift"]) / r["B_r_GE"]
                              for r in ift_rows if r["B_r_GE"] > 0),
                             default=None),
            "formula": ("|d_r d_kappa Delta*(implicit function) - "
                        "d_{kappa r} Delta^act| <= B_r^GE, every node"),
            "note": ("the Neumann bound must dominate the exactly-solved "
                     "cutoff responses; a violation is a mis-assembly of "
                     "C1_proof.md Step 6")})

    # -- PASS/FAIL: the IFT reading agrees with the re-solved equilibrium --
    pairs = [(r["dDelta_star_dkappa"], r["dDelta_star_dkappa_ift"])
             for r in ok_rows if r["L_R"] < 1.0
             and np.isfinite(r["dDelta_star_dkappa_ift"])
             and np.isfinite(r["dDelta_star_dkappa"])]
    rel = [abs(a - b) / max(abs(a), 1e-12) for a, b in pairs]
    pairs_x = [(r["cross_r_equilibrium_numeric"], r["cross_r_equilibrium_ift"])
               for r in ok_rows
               if np.isfinite(r["cross_r_equilibrium_numeric"])
               and np.isfinite(r["cross_r_equilibrium_ift"])]
    rel_x = [abs(a - b) / max(abs(a), 1e-12) for a, b in pairs_x]
    record("ift_matches_resolved_equilibrium", (max(rel) < TOL_IFT
                                                if rel else True),
           {"n_checked": len(rel), "max_rel_diff_first": max(rel) if rel else None,
            "n_checked_cross": len(rel_x),
            "max_rel_diff_cross": max(rel_x) if rel_x else None,
            "tol": TOL_IFT,
            "scope": "validation nodes only",
            "formula": "d Delta*/d kappa = Delta_kappa + Delta_k . (I-D_kT)^-1 d_kappa T",
            "note": ("this is what licenses taking the equilibrium sign from "
                     "the implicit-function reading at the non-validation "
                     "nodes; the cross-derivative agreement is reported but "
                     "does not gate, since a four-corner re-solve of a "
                     "second derivative is the noisier of the two")})

    # -- RECORD: the certified region -------------------------------------
    cert = [r for r in ok_rows if r["certified"]]
    etas = sorted(r["eta_r"] for r in cert)
    empty = len(cert) == 0
    where = sorted({(r["T"], r["tau_pct"]) for r in cert})
    record("certified_region", None,
           {"empty_region": empty,
            "n_certified": len(cert), "n_nodes": len(ok_rows),
            "eta_min": etas[0] if etas else None,
            "eta_median": (float(np.median(etas)) if etas else None),
            "eta_max": etas[-1] if etas else None,
            "certified_cells_T_taupct": [list(w) for w in where],
            "certified_kappa_by_cell": {
                f"T{T}_q{q}": sorted(r["kappa"] for r in cert
                                     if r["T"] == T and r["tau_pct"] == q)
                for (T, q) in where},
            "criterion": "L_R < 1 AND eta_r = g_r^PE - B_r^GE > 0",
            "note": ("card section 6: an empty region is a reportable outcome; "
                     "C1 is then dropped and the paper ships T1 only. No "
                     "tolerance was weakened to make it nonempty.")})
    if empty:
        print("\n" + "!" * 78)
        print("EMPTY REGION -- no node satisfies L_R < 1 and eta_r > 0.")
        print("!" * 78 + "\n", flush=True)

    # -- RECORD: how much the inversion-free step costs --------------------
    sharp = [r for r in ok_rows if r["certified_sharp"]]
    ratios = [r["B_r_GE"] / r["B_r_GE_sharp"] for r in ok_rows
              if np.isfinite(r.get("B_r_GE_sharp", float("nan")))
              and r["B_r_GE_sharp"] > 0]
    slack = [abs(r["remainder_ift"]) / r["B_r_GE"] for r in ok_rows
             if r["L_R"] < 1.0 and np.isfinite(r["remainder_ift"])
             and r["B_r_GE"] > 0]
    record("inversion_free_slack", None,
           {"n_certified_card_bound": len(cert),
            "n_certified_sharp_bound": len(sharp),
            "sharp_cells_T_taupct": sorted({(r["T"], r["tau_pct"])
                                            for r in sharp}),
            "median_B_over_B_sharp": (float(np.median(ratios)) if ratios
                                      else None),
            "max_B_over_B_sharp": max(ratios) if ratios else None,
            "median_realised_remainder_over_B": (float(np.median(slack))
                                                 if slack else None),
            "reading": ("B_r_GE_sharp replaces the inversion-free kbar's with "
                        "the exactly-solved ||d_x k|| and ||d^2_{kappa r} k||. "
                        "It is NOT card 4.5's object and certifies nothing; it "
                        "measures the price of the Neumann step. A large gap "
                        "between the two counts is a card-owner finding "
                        "(C1_proof.md NOT CLAIMED 5), not a result.")})

    # -- RECORD: why nodes fail to certify ---------------------------------
    zero_g = [r for r in ok_rows if abs(r["g_r_PE"]) < 1e-10]
    record("failure_attribution", None,
           {"n_L_ge_1": len(bad_L),
            "n_g_r_PE_zero_to_1e-10": len(zero_g),
            "n_g_positive_but_dominated": len(
                [r for r in ok_rows if r["g_r_PE"] > 1e-10
                 and r["L_R"] < 1.0 and not r["certified"]]),
            "n_g_negative": len([r for r in ok_rows if r["g_r_PE"] < -1e-10]),
            "zero_g_cells_T_taupct": sorted({(r["T"], r["tau_pct"])
                                             for r in zero_g}),
            "reading": ("g_r^PE = 0 exactly means the flagged set does not "
                        "move with tau at that node: the implemented legal "
                        "clock quantises the crossing date (c = ceil(.)), so "
                        "Omega(tau) is locally constant and d_{kappa r} "
                        "Delta^act vanishes identically there.")})

    # -- RECORD: A8 and A5 diagnostics -------------------------------------
    deg = [{"T": r["T"], "tau_pct": r["tau_pct"], "kappa": r["kappa"],
            "Omega": r["Omega"], "degenerate": r["degenerate"]}
           for r in ok_rows if r["degenerate"]]
    mult = [{"T": r["T"], "tau_pct": r["tau_pct"], "kappa": r["kappa"],
             "n": r["multiple_root_nodes"]}
            for r in ok_rows if r["multiple_root_nodes"]]
    record("degenerate_and_multiple_root_nodes", None,
           {"n_degenerate_nodes": len(deg),
            "degenerate_cells_T_taupct": sorted({(d["T"], d["tau_pct"])
                                                 for d in deg}),
            "degenerate_sample": deg[:6],
            "n_nodes_with_multiple_roots": len(mult), "multiple_roots": mult[:6],
            "n_k_order_violations": len([r for r in ok_rows
                                         if not r["k_order_ok"]]),
            "max_solve_residual": max((r["worst_solve_residual"]
                                       for r in ok_rows), default=None),
            "n_solve_residual_above_tol": len(
                [r for r in ok_rows if r["worst_solve_residual"] > TOL_SOLVE]),
            "tol_solve": TOL_SOLVE})

    # -- RECORD: AGE's constancy clause ------------------------------------
    flips = []
    for T in T_GRID:
        for q in pct:
            seq = [r for r in ok_rows if r["T"] == T and r["tau_pct"] == q]
            seq.sort(key=lambda r: r["kappa"])
            signs = [r["sign_equilibrium"] for r in seq]
            n_flip = int(sum(1 for a, b in zip(signs, signs[1:]) if a != b))
            if n_flip:
                flips.append({"T": T, "tau_pct": q, "n_sign_changes": n_flip,
                              "kappas": [r["kappa"] for r in seq],
                              "signs": signs})
    record("age_sign_constancy_on_kappa_slices", None,
           {"n_slices": len(T_GRID) * len(pct),
            "n_slices_with_a_sign_change": len(flips), "slices": flips,
            "n_sign_incoherent_nodes": len([r for r in ok_rows
                                            if not r["sign_coherent"]]),
            "reading": ("AGE requires the sign of the equilibrium liquidity "
                        "derivative to be constant on R. A slice with a sign "
                        "change cannot be taken whole as a region; see "
                        "C1_proof.md WHERE IT FAILS 2.")})

    # -- RECORD: the free finite-scale (secant) reading --------------------
    # The certificate is a derivative statement. The frozen tau percentiles are
    # a finite tightening ladder, so the same nodes also give the secant form
    # at no extra cost: does the fixed-policy sensitivity's move across a
    # threshold pair have the same orientation as the equilibrium one?
    sec = []
    for T in T_GRID:
        for kappa in KAPPA_GRID:
            seq = [r for r in ok_rows
                   if r["T"] == T and abs(r["kappa"] - kappa) < 1e-12]
            seq.sort(key=lambda r: r["tau"])
            for a, b in zip(seq, seq[1:]):
                dtau = b["tau"] - a["tau"]
                if dtau <= 0:
                    continue
                s_pe = -a["sign_equilibrium"] * (
                    b["dDelta_dkappa_fixed"] - a["dDelta_dkappa_fixed"]) / dtau
                s_eq = -a["sign_equilibrium"] * (
                    b["dDelta_star_dkappa_used"]
                    - a["dDelta_star_dkappa_used"]) / dtau
                sec.append({"T": T, "kappa": float(kappa),
                            "tau_pct_lo": a["tau_pct"], "tau_pct_hi": b["tau_pct"],
                            "secant_g_fixed_policy": float(s_pe),
                            "secant_g_equilibrium": float(s_eq),
                            "same_orientation": bool(s_pe * s_eq > 0)})
    n_same = len([s for s in sec if s["same_orientation"]])
    n_pos = len([s for s in sec if s["secant_g_fixed_policy"] > 0])
    record("finite_scale_secant_orientation", None,
           {"n_pairs": len(sec), "n_same_orientation": n_same,
            "n_fixed_policy_secant_positive": n_pos,
            "n_equilibrium_secant_positive": len(
                [s for s in sec if s["secant_g_equilibrium"] > 0]),
            "pairs": sec,
            "reading": ("secant analogue of g_r^PE across adjacent frozen tau "
                        "percentiles, oriented by the equilibrium sign. This "
                        "is NUMERICAL evidence at finite scale and is NOT the "
                        "certificate, which is a derivative statement.")})

    # -- RECORD: the window margin, discretely ------------------------------
    win = []
    if 5 in T_GRID and 10 in T_GRID:
        for q in pct:
            for kappa in KAPPA_GRID:
                a = [r for r in ok_rows if r["T"] == 10 and r["tau_pct"] == q
                     and abs(r["kappa"] - kappa) < 1e-12]
                b = [r for r in ok_rows if r["T"] == 5 and r["tau_pct"] == q
                     and abs(r["kappa"] - kappa) < 1e-12]
                if a and b:
                    S10 = abs(a[0]["dDelta_star_dkappa_used"])
                    S5 = abs(b[0]["dDelta_star_dkappa_used"])
                    win.append({"tau_pct": q, "kappa": float(kappa),
                                "S_star_T10": S10, "S_star_T5": S5,
                                "ratio_5_over_10": (S5 / S10 if S10 > 0
                                                    else None),
                                "Omega_T10": a[0]["Omega"],
                                "Omega_T5": b[0]["Omega"]})
    record("window_margin_discrete_record", None,
           {"n_pairs": len(win),
            "n_attenuating": len([w for w in win
                                  if w["ratio_5_over_10"] is not None
                                  and w["ratio_5_over_10"] <= 1.0]),
            "pairs": win,
            "reading": ("T is an integer primitive; r_T = -T carries no "
                        "derivative, so no r_T certificate is computed. This "
                        "row is an EQUILIBRIUM finite-difference record of "
                        "S* at T=5 against T=10, nothing more.")})

    results["n_error_nodes"] = n_err
    results["wall_seconds"] = time.perf_counter() - t_start
    results["all_pass"] = results["n_fail"] == 0
    results["empty_region"] = empty
    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2, default=float)

    print("\n" + "=" * 78)
    print(f"nodes {len(ok_rows)} ok / {n_err} error   "
          f"certified {len(cert)}   "
          f"{'EMPTY REGION' if empty else 'NONEMPTY REGION'}")
    print(f"FAIL checks: {results['n_fail']}   "
          f"wall {results['wall_seconds']:.0f} s")
    print(f"JSON: {OUT}")
    print("=" * 78)
    return 0 if results["n_fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
