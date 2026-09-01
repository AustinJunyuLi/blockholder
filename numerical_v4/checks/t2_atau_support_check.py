"""A(tau) -- the decisive check: enumerate the pooled cell's posterior support.

Ticket 33 (R3).  Written against audit finding 3 of
``research/model_v4/threads/2026-08-23_gpt_end_review_audit.md`` (which upheld
GPT Pro's end-review finding 3 as MISCITED and re-opened A(tau)'s applicability
as OPEN), the NUMERICAL CHECK REQUEST it queues, and the A(tau) block of
``research/model_v4/MODEL_CARD.md`` section 5.

WHAT A(tau) CLAIMS, AND WHAT IS MEASURED HERE.  The card's A(tau) says the
pooled cell's posterior law is the symmetric ternary family

    E[h] = A_0(kappa) h(0) + A_{1/2}(kappa) h(pi_bar/2) + A_1(kappa) h(pi_bar)

with, per clause (tau-ii), the three support points and pi_bar itself kappa-free
and only the weights moving, and with the derivative pattern
A_0' = A_1' = A'_kappa, A_{1/2}' = -2 A'_kappa.  Per the binding pi_bar ruling
(card section 5, the pi_bar row of the notation table), **pi_bar is the UPPER
SUPPORT POINT of the pooled engagement posterior**, never twice the pooled
engagement share: the share is the MEAN of that law.  Level symmetry is NOT
assumed anywhere in this script -- imposing it (pi_bar = 2 pi_bar_pr) together
with Example A's |A'_kappa| = 0.25 is precisely the block-3 error that made
``t2_t1_check.py``'s chord test MISCITED.

THE ENUMERATED OBJECT.  The law of the pooled engagement posterior

    Pi = pi(X_{0:H}) = Pr(a = 1 | X_{0:H}, D = 0)

under the pooled measure ``mass[H]``, over the 4^(H+1) = 4,194,304 order-flow
paths of ``numerical_v4.pooled``.  That is exactly the law ``pooled_premium``
integrates to form M_P = Delta_m E[h | D = 0], so the object under test is the
one A(tau) is a hypothesis about, not a proxy for it.  Two independent guards
that the object is right:

  * WIRING GATE.  This script re-enumerates mass and Pi from ``mark_stats``,
    the atom list and the ternary noise law, independently of ``pooled_pass``,
    and requires agreement to 1e-15 at every node.  A failure here means the
    enumerated object is wrong and every later number is meaningless; it is the
    only condition that makes this script exit nonzero.
  * MEAN GATE.  The enumerated mean E[Pi] must equal the pooled engagement
    share pi_bar_pr = Pr(a = 1 | D = 0) computed off the s-partition with no
    enumeration at all (tower property).  This is the check that would catch a
    posterior built on the wrong conditioning set.

THE BELIEF FLOOR.  ``pooled.OFF_PATH_EPS`` = 1e-14 gives zero-mass mark paths a
full-support weight floor (card section 3 clause vi, an eps -> 0 limit).  The
support is counted on BOTH laws: the FLOORED law that the package prices, and
the FLOOR-FREE law (on-path weights only) that is the eps -> 0 limit on
mass-carrying histories.  The floor-free law is the primary one -- it is the
limit the card's clause actually names -- and the floored count is reported
beside it so that "the floor manufactured your atoms" cannot be asserted in
either direction after the fact.

Checks (all clause checks are APPLICABILITY MEASUREMENTS, not build gates):

  atau_wiring_reenumeration      GATE         own enumeration == pooled_pass
  atau_mean_equals_share         GATE         E[Pi] == Pr(a=1|D=0)
  atau_support_three_point       clause       support == {0, pi_bar/2, pi_bar}?
  atau_support_kappa_free        clause (tau-ii) support moves < 1e-12 in kappa?
  atau_pi_bar_kappa_free         clause (tau-ii) pi_bar moves < 1e-12 in kappa?
  atau_derivative_pattern_A0_A1  clause       A_0' == A_1'?
  atau_derivative_pattern_Ahalf  clause       A_{1/2}' == -2 A_0'?
  atau_chord_identity            clause       |S_P| == Delta_m |A'_kappa| |C_h|?
  atau_tau_i_kernel_through_pi   diagnostic   is h constant within a Pi-cluster?

A SUPPORT FAILURE AND A DERIVATIVE-PATTERN FAILURE ARE DIFFERENT FINDINGS and
are recorded separately, as are the two halves of (tau-ii) (the three-point
support and the kappa-freeness of pi_bar): one may fail while the other holds.
Where A_{1/2} is identically zero the residual |A_{1/2}' + 2A_0'| is 2|A_0'|
and restates the support failure rather than adding an independent one; it is
marked ``inherited`` in that case.

EXIT CODE -- DELIBERATE DEVIATION FROM THE t2_* CONVENTION.  The other t2_*
scripts return 1 if any check fails.  Here a failing clause is the *result*: it
is evidence about an assumption's applicability, not a broken build.  This
script returns 0 whenever it completes a measurement and writes a verdict, and
nonzero only if a GATE fails (the enumerated object is wrong).  The verdict is
``results["verdict"]``, one of HOLDS / FAILS / MIXED at this calibration.

NO LABEL MOVES.  A(tau) is an assumption, not a labelled claim.  This is
NUMERICAL-class applicability evidence at one calibration; it neither promotes
nor demotes L3, L4 or T1, whose conditional statements are untouched.

Deterministic: no RNG, no Monte Carlo, no file inputs, no network.  Two cold
solver calls at the top (the seed equilibrium and the frozen-tau baseline),
exactly as ``t2_t1_check.py`` and ``t2_l2_check.py`` do.

Run:    .venv/bin/python numerical_v4/checks/t2_atau_support_check.py
Output: numerical_v4/checks/t2_atau_support_check.json
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from numerical_v4.menu import atoms, type_reference  # noqa: E402
from numerical_v4.params import ParamsV4  # noqa: E402
from numerical_v4.policy import frozen_tau_grid  # noqa: E402
from numerical_v4.pooled import OFF_PATH_EPS, mark_stats, pooled_pass  # noqa: E402
from numerical_v4.premium import cell_weights, chord, pooled_premium  # noqa: E402
from numerical_v4.solver import solve_policy  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "t2_atau_support_check.json")

# -- tolerances -------------------------------------------------------------
TOL_WIRING = 1e-15          # GATE: own enumeration vs pooled_pass
TOL_MEAN = 1e-12            # GATE: E[Pi] vs Pr(a=1|D=0)
TOL_CLUSTER = 1e-12         # ticket: cluster distinct posterior values at 1e-12
TOL_SUPPORT_MOVE = 1e-12    # ticket: A(tau) predicts support movement < 1e-12
TOL_OFF_MASS = 1e-12        # mass A(tau) requires to sit off {0, pi_bar/2, pi_bar}
TOL_PATTERN = 1e-10         # ticket: derivative-pattern residuals < 1e-10
TOL_IDENT = 1e-10           # ticket: chord-identity residual < 1e-10
MASS_MATERIAL = 1e-6        # "material" atom: carries at least this mass
DK = 1e-3                   # central-difference step (numerical_v4.premium.DERIV_STEP)
PP = 100.0                  # premium percentage points

# -- grid (design section 6.2; the established t2 ladder) -------------------
KAPPAS = tuple(round(0.05 + 0.10 * i, 2) for i in range(10))   # 0.05 .. 0.95
QUANTILES = (0.1, 0.3, 0.5, 0.7, 0.9)
TS = (1, 2, 5, 10)          # T = 10 is H, the corner (design risk 9.5)
CLUSTER_TOLS = (1e-12, 1e-9, 1e-6, 1e-3)   # dust audit on the support count

results: dict = {"checks": [], "n_fail": 0, "n_vacuous": 0, "n_gate_fail": 0}


def record(name: str, ok: bool, kind: str, detail: dict,
           vacuous: bool = False) -> None:
    results["checks"].append(
        {"name": name, "kind": kind, "pass": bool(ok), "vacuous": bool(vacuous),
         **detail}
    )
    if not ok:
        results["n_fail"] += 1
        if kind == "gate":
            results["n_gate_fail"] += 1
    if vacuous:
        results["n_vacuous"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({kind})", flush=True)
    print("        " + json.dumps(detail, default=float)[:1400], flush=True)


# ---------------------------------------------------------------------------
# The enumerated law
# ---------------------------------------------------------------------------


def own_posterior(al, p: ParamsV4, with_floor: bool
                  ) -> tuple[np.ndarray, np.ndarray, np.ndarray | None]:
    """Re-enumerate (mass, Pi_floorfree, Pi_floored) at the control node d = H.

    Independent of ``pooled_pass``: rebuilt here from ``mark_stats``, the atom
    list and the ternary noise law, so that the agreement asserted by the wiring
    gate is real information about the object rather than a tautology.

    ``mass`` uses on-path weights only (it is the pooled measure).  ``Pi`` is the
    belief, which the package floors at OFF_PATH_EPS on mark paths no atom
    selects.  ``with_floor=False`` skips the floored column, which is only
    needed where the wiring gate runs (the base nodes, not the FD stencil).
    """
    H, nt = p.H, p.n_theta
    ms = mark_stats(H)
    n0, feas = ms.n0[H], ms.feas[H]
    e = np.arange(H + 2, dtype=float)
    lut = (1.0 - p.kappa) ** e * (p.kappa / 2.0) ** (H + 1.0 - e)

    W = np.zeros(nt)
    WA = np.zeros(nt)
    for a in al:
        if a.D == 1 and a.f <= H:
            continue                          # flag already public at date H
        W[a.theta] += a.w
        WA[a.theta] += a.w * a.a

    Wf = np.zeros(nt)
    WAf = np.zeros(nt)
    if with_floor:
        ref = type_reference(p)
        for t in range(nt):
            if W[t] > 0.0:
                continue
            if ref.D[t] == 1.0 and ref.f[t] <= H:
                continue
            Wf[t] = OFF_PATH_EPS
            WAf[t] = OFF_PATH_EPS * ref.a[t]

    n = n0.shape[0]
    mass = np.zeros(n)
    num0 = np.zeros(n)
    denf = np.zeros(n) if with_floor else None
    numf = np.zeros(n) if with_floor else None
    for t in range(nt):
        if W[t] <= 0.0 and Wf[t] <= 0.0:
            continue
        Lt = lut[n0[:, t]] * feas[:, t]
        if W[t] > 0.0:
            mass += W[t] * Lt
            num0 += WA[t] * Lt
        if with_floor:
            denf += (W[t] + Wf[t]) * Lt
            numf += (WA[t] + WAf[t]) * Lt

    pi0 = np.full(n, np.nan)
    lv0 = mass > 0.0
    pi0[lv0] = num0[lv0] / mass[lv0]
    pif = None
    if with_floor:
        pif = np.full(n, np.nan)
        lvf = denf > 0.0
        pif[lvf] = numf[lvf] / denf[lvf]
    return mass, pi0, pif


def cluster_sorted(v: np.ndarray, m: np.ndarray, tol: float
                   ) -> tuple[np.ndarray, np.ndarray]:
    """Single-linkage clustering of an already-sorted, mass-normalised sample.

    Single linkage is the ticket's "cluster tol 1e-12"; a chain of atoms spaced
    below the tolerance can therefore span more than the tolerance, which is why
    the support count is reported at four tolerances (see CLUSTER_TOLS).
    """
    cuts = np.flatnonzero(np.diff(v) > tol)
    st = np.concatenate(([0], cuts + 1))
    wts = np.add.reduceat(m, st)
    vals = np.add.reduceat(v * m, st) / wts
    return vals, wts


def mass_at(mass: np.ndarray, pi: np.ndarray, target: float,
            tol: float = TOL_CLUSTER) -> float:
    """Normalised pooled mass within ``tol`` of ``target``."""
    live = mass > 0.0
    m = mass[live]
    sel = np.abs(pi[live] - target) <= tol
    return float(m[sel].sum() / m.sum())


def hausdorff(a: np.ndarray, b: np.ndarray) -> float:
    """Two-sided Hausdorff distance between two sorted support arrays."""
    if a.size == 0 or b.size == 0:
        return float("nan")

    def one_way(x: np.ndarray, y: np.ndarray) -> float:
        if y.size == 1:
            return float(np.abs(x - y[0]).max())
        idx = np.clip(np.searchsorted(y, x), 1, y.size - 1)
        d = np.minimum(np.abs(x - y[idx]), np.abs(x - y[idx - 1]))
        return float(d.max())

    return max(one_way(a, b), one_way(b, a))


# ---------------------------------------------------------------------------
# One node
# ---------------------------------------------------------------------------


def node_law(pol_k, p_base: ParamsV4, tau: float, T: int, kappa: float) -> dict:
    """The pooled cell's engagement-posterior law at one node, fully reduced.

    Every 4.19M-element array is consumed here and discarded; only the clustered
    support (a few hundred floats) and scalars survive into the node table.
    """
    p = p_base.replace(kappa=float(kappa), tau=float(tau), T=int(T))
    al = atoms(pol_k, p)
    cw = cell_weights(al)
    res = pooled_pass(al, p, with_runup=False)
    H = p.H
    mass = res.mass[H]
    pi_pkg = res.pi[H]
    pb = res.p_bid[H]

    massO, pi0, piF = own_posterior(al, p, with_floor=True)
    live = mass > 0.0
    wiring = max(float(np.max(np.abs(massO - mass))),
                 float(np.max(np.abs(piF[live] - pi_pkg[live]))))

    # sort the live sample once and reuse for every clustering
    m_live = mass[live]
    tot = float(m_live.sum())
    order = np.argsort(pi0[live], kind="mergesort")
    v_s = pi0[live][order]
    m_s = m_live[order] / tot
    p_s = pb[live][order]

    vals, wts = cluster_sorted(v_s, m_s, TOL_CLUSTER)
    n_by_tol = {f"{t:.0e}": int(cluster_sorted(v_s, m_s, t)[0].size)
                for t in CLUSTER_TOLS}

    orderF = np.argsort(piF[live], kind="mergesort")
    valsF, _ = cluster_sorted(piF[live][orderF], m_live[orderF] / tot,
                              TOL_CLUSTER)

    pib = float(vals[-1])
    mean_pi = float(np.dot(vals, wts))

    # (tau-i) diagnostic: within a Pi-cluster, does h = Pi p still move?
    cuts = np.flatnonzero(np.diff(v_s) > TOL_CLUSTER)
    st = np.concatenate(([0], cuts + 1))
    spread_p = np.maximum.reduceat(p_s, st) - np.minimum.reduceat(p_s, st)
    material = wts >= MASS_MATERIAL
    max_spread_p = float(spread_p[material].max()) if material.any() else 0.0
    mw_spread_h = float(np.dot(wts, spread_p * np.abs(vals)))

    # A(tau)'s three weights, at the ACTUAL upper support point
    A0 = mass_at(mass, pi0, 0.0)
    Ah = mass_at(mass, pi0, 0.5 * pib)
    A1 = mass_at(mass, pi0, pib)

    # h(pi_bar) straight off the enumeration: the mass-weighted mean of the
    # entry probability on the Pi = pi_bar cluster, times pi_bar.  h(0) = 0
    # identically, so pi_bar/2 is the only chord point needing a convention.
    sel = np.abs(v_s - pib) <= TOL_CLUSTER
    h_top = (pib * float(np.dot(m_s[sel], p_s[sel]) / m_s[sel].sum())
             if sel.any() else float("nan"))

    # the pooled cell's own v_hat = E[v | D = 0]: an atom-level average, since
    # each type's likelihood sums to one over histories
    wa = np.array([a.w for a in al if not (a.D == 1 and a.f <= H)])
    va = np.array([a.Ev for a in al if not (a.D == 1 and a.f <= H)])
    v_hat_mean = float(np.dot(wa, va) / wa.sum()) if wa.size else float("nan")

    return {
        "tau": float(tau), "T": int(T), "kappa": float(kappa),
        "Omega": float(cw.Omega), "pi_bar_pr": float(cw.pi_bar),
        "M_P": float(pooled_premium(res, cw.Omega, p)),
        "wiring_residual": wiring,
        "n_live_histories": int(live.sum()),
        "n_support_floorfree": int(vals.size),
        "n_support_floored": int(valsF.size),
        "pi_bar_floorfree": pib,
        "pi_bar_floored": float(valsF[-1]),
        "mean_pi": mean_pi,
        "mean_gate_residual": abs(mean_pi - float(cw.pi_bar)),
        "n_support_by_tol": n_by_tol,
        "n_material_atoms": int(material.sum()),
        "A_0": A0, "A_half": Ah, "A_1": A1,
        "A_off_three_points": float(1.0 - A0 - Ah - A1),
        "three_point_support": bool(
            vals.size == 3 and abs(vals[0]) <= TOL_CLUSTER
            and abs(vals[1] - 0.5 * pib) <= TOL_CLUSTER
            and abs(1.0 - A0 - Ah - A1) <= TOL_OFF_MASS),
        "midpoint_gap": (float(abs(vals[1] - 0.5 * pib)) if vals.size >= 2
                         else float("nan")),
        "h_pi_bar_enumerated": h_top,
        "v_hat_pooled_mean": v_hat_mean,
        "top5_values": [float(x) for x in vals[-5:]],
        "top5_masses": [float(x) for x in wts[-5:]],
        "bottom5_values": [float(x) for x in vals[:5]],
        "bottom5_masses": [float(x) for x in wts[:5]],
        "tau_i_max_p_spread_in_cluster": max_spread_p,
        "tau_i_massweighted_h_spread": mw_spread_h,
        "_vals": vals, "_wts": wts,
    }


def stencil_weights(pol_k, p_base: ParamsV4, tau: float, T: int, kappa: float,
                    pi_bar: float) -> tuple[float, float, float, float]:
    """(A_0, A_{1/2}, A_1, M_P) at one kappa, at FIXED A(tau) target points.

    The targets {0, pi_bar/2, pi_bar} are taken from the base node.  Under
    A(tau)(tau-ii) they are kappa-free, so differentiating the mass at a fixed
    target is exactly differentiating the A(tau) weight; if they are not
    kappa-free that is the separate support-movement finding, measured on its
    own by ``atau_support_kappa_free``.
    """
    p = p_base.replace(kappa=float(kappa), tau=float(tau), T=int(T))
    al = atoms(pol_k, p)
    cw = cell_weights(al)
    res = pooled_pass(al, p, with_runup=False)
    mass, pi0, _ = own_posterior(al, p, with_floor=False)
    return (mass_at(mass, pi0, 0.0),
            mass_at(mass, pi0, 0.5 * pi_bar),
            mass_at(mass, pi0, pi_bar),
            float(pooled_premium(res, cw.Omega, p)))


def fd4(f_p1, f_m1, f_p2, f_m2, h: float) -> float:
    """4th-order central difference, matching ``numerical_v4.premium.d_dkappa``."""
    return float((8.0 * (f_p1 - f_m1) - (f_p2 - f_m2)) / (12.0 * h))


# ---------------------------------------------------------------------------


def main() -> int:
    t0 = time.perf_counter()
    print("t2_atau_support_check -- frozen baseline (2 cold solves) ...",
          flush=True)
    p_seed = ParamsV4.baseline()
    pol_seed, _ = solve_policy(p_seed)
    taus = tuple(float(x) for x in frozen_tau_grid(pol_seed, p_seed, QUANTILES))
    tau_med = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau_med)
    pol, resid = solve_policy(p_base)
    k = tuple(pol.k)
    print(f"  frozen k = {k}\n  tau ladder {['%.8f' % t for t in taus]}",
          flush=True)

    results["provenance"] = {
        "ticket": "33 (R3) -- A(tau) support enumeration, the decisive check",
        "premise": "research/model_v4/threads/2026-08-23_gpt_end_review_audit.md "
                   "finding 3 (UPHELD as MISCITED): t2_t1_check block 3 "
                   "hard-coded A'_kappa = 0.25 (Example A) and imposed level "
                   "symmetry pi_bar = 2 pi_bar_pr, so its 0.628 pp residual "
                   "refuted that witness calibration, not A(tau). A(tau)'s "
                   "applicability at the implemented pooled cell was reset to "
                   "OPEN and this enumeration queued as the decisive test.",
        "statement_under_test": "research/model_v4/MODEL_CARD.md section 5, "
                                "A(tau) Threshold chord restriction, clauses "
                                "(tau-i) and (tau-ii), with the binding pi_bar "
                                "ruling (pi_bar = the UPPER SUPPORT POINT of "
                                "the pooled engagement posterior)",
        "design": "research/model_v4/impl_design.md section 6.2 (frozen "
                  "policies, frozen tau ladder) and section 13",
        "not_imposed": ["Example A's |A'_kappa| = 0.25",
                        "level symmetry pi_bar = 2 pi_bar_pr",
                        "any three-point structure -- the enumeration never "
                        "imposes A(tau) (design section 0)"],
        "params_hash": p_base.hash_str(),
        "label_class": "NUMERICAL -- applicability evidence for an assumption "
                       "at one calibration; A(tau) carries no label and none "
                       "moves on this run",
    }
    results["grid"] = {
        "kappa": list(KAPPAS), "tau": list(taus), "tau_quantiles": list(QUANTILES),
        "T": list(TS), "H": p_base.H, "M": 2,
        "n_nodes": len(KAPPAS) * len(TS) * len(QUANTILES),
        "policy": "frozen at the baseline equilibrium cutoffs at every node",
        "tau_frozen_from": "percentiles of the seed-equilibrium (tau = 0.05) "
                           "Voice b*(s) terminal-stake distribution, design 6.2",
        "cutoff_residual": resid.cutoff_scale,
        "payoff_residual": resid.payoff_scale,
        "derivative_step": DK,
        "derivative_stencil": "4th-order central, matching "
                              "numerical_v4.premium.d_dkappa",
        "evaluations": "5 pooled passes per non-degenerate node (kappa, "
                       "kappa +/- h, kappa +/- 2h) plus one independent "
                       "re-enumeration at the base kappa",
    }

    # -- the sweep ----------------------------------------------------------
    nodes: dict = {}
    n_eval = 0
    for T in TS:
        for qi, tau in zip(QUANTILES, taus):
            for kap in KAPPAS:
                r = node_law(k, p_base, tau, T, kap)
                r["tau_quantile"] = qi
                nodes[(T, qi, kap)] = r
                n_eval += 1
            r0 = nodes[(T, qi, KAPPAS[len(KAPPAS) // 2])]
            print(f"  T={T:2d} q={qi:.1f} tau={tau:.6f} Omega={r0['Omega']:.6f} "
                  f"share={r0['pi_bar_pr']:.8f} "
                  f"n_support={r0['n_support_floorfree']} "
                  f"pi_bar={r0['pi_bar_floorfree']:.12f} "
                  f"A_off={r0['A_off_three_points']:.6f}", flush=True)

    rows = list(nodes.values())

    # -- GATE 1: the enumerated object is the package's --------------------
    worst_wire = max(r["wiring_residual"] for r in rows)
    record(
        "atau_wiring_reenumeration", worst_wire <= TOL_WIRING, "gate",
        {"request": "the enumerated object must be exactly the pooled cell's "
                    "engagement-posterior law that pooled_premium integrates; a "
                    "wrong object silently passes every later clause",
         "tol": TOL_WIRING, "max_residual": worst_wire,
         "compared": "this script's independent re-enumeration of (mass, Pi) "
                     "from mark_stats + the atom list + the ternary noise law, "
                     "against numerical_v4.pooled.pooled_pass",
         "n_nodes": len(rows)},
    )

    # -- GATE 2: the mean of the enumerated law is the pooled share ---------
    worst_mean = max(r["mean_gate_residual"] for r in rows)
    record(
        "atau_mean_equals_share", worst_mean <= TOL_MEAN, "gate",
        {"request": "E[Pi] over the enumerated law must equal "
                    "pi_bar_pr = Pr(a = 1 | D = 0) computed off the s-partition "
                    "with no enumeration (tower property). This is the gate that "
                    "catches a posterior built on the wrong conditioning set, "
                    "and it is also the card's statement that the pooled "
                    "engagement SHARE is the MEAN of this law, not pi_bar.",
         "tol": TOL_MEAN, "max_residual": worst_mean, "n_nodes": len(rows)},
    )

    if results["n_gate_fail"]:
        results["verdict"] = "NOT EVALUABLE -- gate failed"
        results["seconds"] = time.perf_counter() - t0
        with open(OUT, "w") as fh:
            json.dump(results, fh, indent=2, default=float)
        print("\nGATE FAILED -- the enumerated object is not the pooled law. "
              "No clause verdict is reported.", flush=True)
        return 2

    # -- degenerate nodes ---------------------------------------------------
    # pi_bar_pr = 0: no engaging atom survives into the pooled cell, the law is
    # the point mass at 0, h == 0, C_h(0) = 0 and M_P = 0.  A(tau) holds
    # vacuously at pi_bar = 0 and the node carries no information either way.
    for r in rows:
        r["degenerate"] = bool(r["pi_bar_pr"] <= 0.0
                               or r["pi_bar_floorfree"] <= 0.0)
    nd = [r for r in rows if not r["degenerate"]]
    deg = [r for r in rows if r["degenerate"]]
    if not nd:
        results["verdict"] = "NOT EVALUABLE -- every node degenerate"
        results["seconds"] = time.perf_counter() - t0
        with open(OUT, "w") as fh:
            json.dump(results, fh, indent=2, default=float)
        print("\nEVERY NODE DEGENERATE -- no clause is evaluable.", flush=True)
        return 0

    # -- clause: three-point support ---------------------------------------
    n_3pt = sum(1 for r in nd if r["three_point_support"])
    record(
        "atau_support_three_point", n_3pt == len(nd), "clause",
        {"request": "is the pooled posterior's support exactly "
                    "{0, pi_bar/2, pi_bar} -- three points, with the midpoint "
                    "relation to 1e-12 and no mass off them?",
         "tol_cluster": TOL_CLUSTER, "tol_off_mass": TOL_OFF_MASS,
         "n_nondegenerate_nodes": len(nd), "n_three_point": n_3pt,
         "n_not_three_point": len(nd) - n_3pt,
         "support_count_range": [min(r["n_support_floorfree"] for r in nd),
                                 max(r["n_support_floorfree"] for r in nd)],
         "max_off_three_point_mass": max(r["A_off_three_points"] for r in nd),
         "min_off_three_point_mass": min(r["A_off_three_points"] for r in nd),
         "support_count_range_by_cluster_tol": {
             f"{t:.0e}": [min(r["n_support_by_tol"][f"{t:.0e}"] for r in nd),
                          max(r["n_support_by_tol"][f"{t:.0e}"] for r in nd)]
             for t in CLUSTER_TOLS},
         "max_floored_minus_floorfree_support_count": max(
             r["n_support_floored"] - r["n_support_floorfree"] for r in nd),
         "reading": "the cluster-tolerance ladder is the dust audit: if the "
                    "count stayed large only at 1e-12 the atoms could be "
                    "floating-point noise, and if the floored and floor-free "
                    "counts diverged the belief floor could be manufacturing "
                    "them. Both columns are reported so neither objection can "
                    "be raised after the fact."},
    )

    # -- clause: kappa-free support, and kappa-free pi_bar ------------------
    mv = []
    for T in TS:
        for qi in QUANTILES:
            seq = [nodes[(T, qi, kp)] for kp in KAPPAS]
            if any(r["degenerate"] for r in seq):
                continue
            worst_h = worst_hm = worst_pb = 0.0
            for a, b in zip(seq[:-1], seq[1:]):
                va, vb = a["_vals"], b["_vals"]
                worst_h = max(worst_h, hausdorff(va, vb))
                ma = va[a["_wts"] >= MASS_MATERIAL]
                mb = vb[b["_wts"] >= MASS_MATERIAL]
                worst_hm = max(worst_hm, hausdorff(ma, mb))
                worst_pb = max(worst_pb, abs(a["pi_bar_floorfree"]
                                             - b["pi_bar_floorfree"]))
            mv.append({"T": T, "tau_quantile": qi, "tau": seq[0]["tau"],
                       "max_adjacent_kappa_hausdorff": worst_h,
                       "max_adjacent_kappa_hausdorff_material": worst_hm,
                       "max_adjacent_kappa_pi_bar_shift": worst_pb,
                       "pi_bar_range_over_grid": float(
                           max(r["pi_bar_floorfree"] for r in seq)
                           - min(r["pi_bar_floorfree"] for r in seq)),
                       "pi_bar": seq[0]["pi_bar_floorfree"],
                       "A_0_over_grid": [r["A_0"] for r in seq],
                       "A_1_over_grid": [r["A_1"] for r in seq],
                       "n_support_over_grid": [r["n_support_floorfree"]
                                               for r in seq]})
    n_move_ok = sum(1 for r in mv
                    if r["max_adjacent_kappa_hausdorff"] < TOL_SUPPORT_MOVE)
    record(
        "atau_support_kappa_free", bool(mv) and n_move_ok == len(mv), "clause",
        {"request": "clause (tau-ii), first half: the three support points do "
                    "not vary with kappa. Measured as the two-sided Hausdorff "
                    "distance between the support sets at adjacent kappa at "
                    "fixed (tau, T); A(tau) predicts < 1e-12",
         "tol": TOL_SUPPORT_MOVE,
         "n_series": len(mv), "n_series_kappa_free": n_move_ok,
         "max_hausdorff": max((r["max_adjacent_kappa_hausdorff"] for r in mv),
                              default=float("nan")),
         "max_hausdorff_material_atoms_only": max(
             (r["max_adjacent_kappa_hausdorff_material"] for r in mv),
             default=float("nan")),
         "material_mass_floor": MASS_MATERIAL,
         "rows": mv},
    )
    n_pb_ok = sum(1 for r in mv
                  if r["max_adjacent_kappa_pi_bar_shift"] < TOL_SUPPORT_MOVE)
    record(
        "atau_pi_bar_kappa_free", bool(mv) and n_pb_ok == len(mv), "clause",
        {"request": "clause (tau-ii), second half: pi_bar itself -- the UPPER "
                    "SUPPORT POINT, per the binding ruling -- is kappa-free at "
                    "fixed (tau, T). The L3 re-deriver's CH2 says L3's "
                    "conclusion is FALSE without this half, so it is checked on "
                    "its own and reported as its own finding",
         "tol": TOL_SUPPORT_MOVE,
         "n_series": len(mv), "n_series_pi_bar_kappa_free": n_pb_ok,
         "max_pi_bar_shift": max((r["max_adjacent_kappa_pi_bar_shift"]
                                  for r in mv), default=float("nan")),
         "max_pi_bar_range_over_grid": max(
             (r["pi_bar_range_over_grid"] for r in mv), default=float("nan")),
         "distinct_pi_bar_values": sorted({round(r["pi_bar"], 12) for r in mv}),
         "separation_note": "this clause and atau_support_three_point are "
                            "DIFFERENT findings: pi_bar can be pinned while the "
                            "interior of the support moves, and the card's two "
                            "halves of (tau-ii) must be reported separately"},
    )

    # -- weights, derivatives, and the chord identity -----------------------
    dm = p_base.Delta_m
    for r in nd:
        tau, T, kap, pib = r["tau"], r["T"], r["kappa"], r["pi_bar_floorfree"]
        st = {}
        for lbl, kk in (("p1", kap + DK), ("m1", kap - DK),
                        ("p2", kap + 2 * DK), ("m2", kap - 2 * DK)):
            st[lbl] = stencil_weights(k, p_base, tau, T, kk, pib)
            n_eval += 1
        r["A_0_prime"] = fd4(st["p1"][0], st["m1"][0], st["p2"][0],
                             st["m2"][0], DK)
        r["A_half_prime"] = fd4(st["p1"][1], st["m1"][1], st["p2"][1],
                                st["m2"][1], DK)
        r["A_1_prime"] = fd4(st["p1"][2], st["m1"][2], st["p2"][2],
                             st["m2"][2], DK)
        r["S_P"] = fd4(st["p1"][3], st["m1"][3], st["p2"][3], st["m2"][3], DK)
        r["res_A0_eq_A1"] = abs(r["A_0_prime"] - r["A_1_prime"])
        r["res_Ahalf_eq_m2A0"] = abs(r["A_half_prime"] + 2.0 * r["A_0_prime"])
        r["A_half_identically_zero"] = bool(
            r["A_half"] <= TOL_OFF_MASS and abs(r["A_half_prime"]) <= 1e-14)

        c_mu = chord(pib, p_base.mu_v, p_base)
        c_ph = chord(pib, r["v_hat_pooled_mean"], p_base)
        cands = {
            "v_hat_mu_v": abs(c_mu.C_h),
            "v_hat_pooled_mean": abs(c_ph.C_h),
            # h(0) = 0 exactly and h(pi_bar) read off the enumeration, so only
            # h(pi_bar/2) carries a kernel convention at all
            "hybrid_enumerated_top": abs(-2.0 * c_ph.h_half
                                         + r["h_pi_bar_enumerated"]),
        }
        r["C_h_variants"] = {kk2: float(vv) for kk2, vv in cands.items()}
        r["identity_residual_variants"] = {
            kk2: abs(abs(r["S_P"]) - dm * abs(r["A_0_prime"]) * vv)
            for kk2, vv in cands.items()}
        best = min(r["identity_residual_variants"],
                   key=lambda kk2: r["identity_residual_variants"][kk2])
        r["identity_best_convention"] = best
        r["identity_residual"] = float(r["identity_residual_variants"][best])
        r["abs_A_prime_kappa_recovered"] = abs(r["A_0_prime"])
        r["abs_A_prime_kappa_implied"] = (
            abs(r["S_P"]) / (dm * cands[best]) if cands[best] > 0 else None)

    n_pat = sum(1 for r in nd if r["res_A0_eq_A1"] < TOL_PATTERN)
    record(
        "atau_derivative_pattern_A0_A1", n_pat == len(nd), "clause",
        {"request": "A(tau)'s derivative pattern, independent half: "
                    "A_0' = A_1' = A'_kappa. Weights recovered from the "
                    "enumeration at the A(tau) target points {0, pi_bar/2, "
                    "pi_bar} with pi_bar the ACTUAL upper support point; "
                    "4th-order central differences in kappa at h = 1e-3; "
                    "A(tau) predicts a residual < 1e-10",
         "tol": TOL_PATTERN,
         "n_nondegenerate_nodes": len(nd), "n_pattern_holds": n_pat,
         "max_residual": max(r["res_A0_eq_A1"] for r in nd),
         "min_residual": min(r["res_A0_eq_A1"] for r in nd),
         "A_0_prime_range": [min(r["A_0_prime"] for r in nd),
                             max(r["A_0_prime"] for r in nd)],
         "A_1_prime_range": [min(r["A_1_prime"] for r in nd),
                             max(r["A_1_prime"] for r in nd)],
         "separation_note": "a derivative-pattern failure is a DIFFERENT "
                            "finding from a support failure: the pattern is "
                            "about how the weights move, the support clause "
                            "about where the mass sits"},
    )
    n_inherit = sum(1 for r in nd if r["A_half_identically_zero"])
    n_pat2 = sum(1 for r in nd if r["res_Ahalf_eq_m2A0"] < TOL_PATTERN)
    record(
        "atau_derivative_pattern_Ahalf", n_pat2 == len(nd), "clause",
        {"request": "A(tau)'s derivative pattern, second half: "
                    "A_{1/2}' = -2 A'_kappa, predicted residual < 1e-10",
         "tol": TOL_PATTERN,
         "n_nondegenerate_nodes": len(nd), "n_pattern_holds": n_pat2,
         "max_residual": max(r["res_Ahalf_eq_m2A0"] for r in nd),
         "n_nodes_with_A_half_identically_zero": n_inherit,
         "A_half_range": [min(r["A_half"] for r in nd),
                          max(r["A_half"] for r in nd)],
         "inherited": bool(n_inherit == len(nd)),
         "reading": "where A_{1/2} == 0 with a vanishing derivative, this "
                    "residual is exactly 2|A_0'| and RESTATES the support "
                    "failure rather than adding an independent one. It is "
                    "reported as INHERITED and must not be counted as a second "
                    "piece of evidence"},
        vacuous=bool(n_inherit == len(nd)),
    )

    n_id = sum(1 for r in nd if r["identity_residual"] < TOL_IDENT)
    imp = [r["abs_A_prime_kappa_implied"] for r in nd
           if r["abs_A_prime_kappa_implied"] is not None]
    record(
        "atau_chord_identity", n_id == len(nd), "clause",
        {"request": "|S_P - Delta_m |A'_kappa| |C_h(pi_bar)|| with the "
                    "RECOVERED A'_kappa (= A_0' from the enumerated weights, "
                    "not Example A's 0.25) and the ACTUAL upper support point "
                    "as pi_bar (not 2 pi_bar_pr). A(tau) + (br-ii) predict "
                    "< 1e-10",
         "tol": TOL_IDENT,
         "n_nondegenerate_nodes": len(nd), "n_identity_holds": n_id,
         "max_residual": max(r["identity_residual"] for r in nd),
         "min_residual": min(r["identity_residual"] for r in nd),
         "max_residual_pp": max(r["identity_residual"] for r in nd) * PP,
         "convention": "reported on three kernel conventions -- v_hat = mu_v "
                       "(block 3's convention, kept for continuity), v_hat = "
                       "the pooled cell's own E[v | D = 0], and a hybrid with "
                       "h(0) = 0 exactly and h(pi_bar) read off the "
                       "enumeration. The verdict is taken on the MOST "
                       "FAVOURABLE of the three, which is the honest way to "
                       "report a refutation",
         "conventions_chosen": sorted({r["identity_best_convention"]
                                       for r in nd}),
         "abs_A_prime_kappa_recovered_range": [
             min(r["abs_A_prime_kappa_recovered"] for r in nd),
             max(r["abs_A_prime_kappa_recovered"] for r in nd)],
         "abs_A_prime_kappa_implied_range": [min(imp), max(imp)] if imp else None,
         "S_P_signed_range": [min(r["S_P"] for r in nd),
                              max(r["S_P"] for r in nd)],
         "S_P_sign_changes": bool(min(r["S_P"] for r in nd) < 0.0
                                  < max(r["S_P"] for r in nd)),
         "block3_comparison": "t2_t1_check block 3 reported an IMPLIED "
                              "|A'_kappa| in [0.997, 1.158]. That number is a "
                              "DIFFERENT object: it inverted the identity using "
                              "the MEAN ABSOLUTE SLOPE of M_P over the kappa "
                              "grid and the LEVEL-SYMMETRIC pi_bar = 2 "
                              "pi_bar_pr. Here the derivative is pointwise and "
                              "pi_bar is the actual upper support point, so the "
                              "two ranges are not comparable; the gap between "
                              "them measures how much the level-symmetry "
                              "assumption was doing",
         "delta_m": dm},
    )

    # -- (tau-i) diagnostic --------------------------------------------------
    worst_taui = max(r["tau_i_max_p_spread_in_cluster"] for r in nd)
    record(
        "atau_tau_i_kernel_through_pi", worst_taui < TOL_PATTERN, "diagnostic",
        {"request": "clause (tau-i): h(I) = h(pi(I)), the kernel touches the "
                    "information set only through the engagement posterior. "
                    "Measured directly: within a Pi-cluster (Pi constant to "
                    "1e-12), how far apart do the enumerated entry "
                    "probabilities p get? h = Pi p, so a nonzero spread is a "
                    "(tau-i) violation and nothing else",
         "tol": TOL_PATTERN,
         "max_p_spread_within_a_material_cluster": worst_taui,
         "max_massweighted_h_spread": max(r["tau_i_massweighted_h_spread"]
                                          for r in nd),
         "material_mass_floor": MASS_MATERIAL,
         "reading": "the card already flags (tau-i) as a RESTRICTION and not a "
                    "reading, because the model's h = pi p(v_hat, pi) is a "
                    "function of two scalars. This column measures how much "
                    "the second one moves at a fixed posterior. It is reported "
                    "as a diagnostic and is NOT part of the three-way verdict, "
                    "which is about the support condition"},
    )

    # -- verdict ------------------------------------------------------------
    move_ok = {(r["T"], r["tau_quantile"]):
               (r["max_adjacent_kappa_hausdorff"] < TOL_SUPPORT_MOVE)
               for r in mv}
    n_hold = 0
    for r in nd:
        ok = (r["three_point_support"]
              and move_ok.get((r["T"], r["tau_quantile"]), False)
              and r["res_A0_eq_A1"] < TOL_PATTERN
              and r["identity_residual"] < TOL_IDENT)
        r["node_holds"] = bool(ok)
        n_hold += int(ok)
    if n_hold == len(nd):
        verdict = "HOLDS at calibration"
    elif n_hold == 0:
        verdict = "FAILS at calibration"
    else:
        verdict = "MIXED at calibration"

    results["verdict"] = verdict
    results["verdict_detail"] = {
        "n_nodes_total": len(rows),
        "n_nodes_degenerate": len(deg),
        "n_nodes_nondegenerate": len(nd),
        "n_nodes_A_tau_holds": n_hold,
        "n_nodes_A_tau_fails": len(nd) - n_hold,
        "clause_breakdown": {
            "support_three_point_fails": len(nd) - n_3pt,
            "support_kappa_free_series_fails": len(mv) - n_move_ok,
            "pi_bar_kappa_free_series_fails": len(mv) - n_pb_ok,
            "derivative_pattern_A0_A1_fails": len(nd) - n_pat,
            "derivative_pattern_Ahalf_fails_inherited": len(nd) - n_pat2,
            "chord_identity_fails": len(nd) - n_id,
        },
        "degenerate_reason": "pi_bar_pr = 0: no engaging atom survives into the "
                             "pooled cell at that (tau, T), so the law is the "
                             "point mass at 0, M_P = 0 and C_h(0) = 0. A(tau) "
                             "holds vacuously at pi_bar = 0 and the node "
                             "carries no information either way; these nodes "
                             "are excluded from both counts",
        "scope": "one calibration (params_hash in provenance), frozen policies, "
                 "H = 10. This is evidence about A(tau)'s APPLICABILITY at the "
                 "implemented two-round pooled cell, not about A(tau) as a "
                 "hypothesis and not about any labelled result: L3, L4 leg 3 "
                 "and T1 Part B are conditionals and their proofs are untouched",
    }

    results["degenerate_nodes"] = [
        {kk: r[kk] for kk in ("tau", "tau_quantile", "T", "kappa", "Omega",
                              "pi_bar_pr", "M_P", "n_support_floorfree",
                              "n_support_floored", "pi_bar_floorfree")}
        for r in deg]
    keep = ("tau", "tau_quantile", "T", "kappa", "Omega", "pi_bar_pr", "M_P",
            "n_live_histories", "n_support_floorfree", "n_support_floored",
            "n_support_by_tol", "n_material_atoms", "pi_bar_floorfree",
            "mean_pi", "three_point_support", "midpoint_gap",
            "A_0", "A_half", "A_1", "A_off_three_points",
            "A_0_prime", "A_half_prime", "A_1_prime", "S_P",
            "res_A0_eq_A1", "res_Ahalf_eq_m2A0", "A_half_identically_zero",
            "C_h_variants", "identity_residual_variants",
            "identity_best_convention", "identity_residual",
            "abs_A_prime_kappa_recovered", "abs_A_prime_kappa_implied",
            "h_pi_bar_enumerated", "v_hat_pooled_mean",
            "tau_i_max_p_spread_in_cluster", "tau_i_massweighted_h_spread",
            "node_holds", "wiring_residual",
            "top5_values", "top5_masses", "bottom5_values", "bottom5_masses")
    results["node_table"] = [{kk: r[kk] for kk in keep} for r in nd]
    results["node_table_truncation_rule"] = (
        "per node: support counts at four cluster tolerances, pi_bar, the three "
        "A(tau) weights and the mass off them, the kappa-derivatives, the "
        "clause residuals, and the five largest and five smallest support atoms "
        "with their masses. The full support (up to ~800 atoms per node over "
        "200 nodes) is not dumped; one exemplar node is dumped in full below")

    ex = nodes[(5, 0.5, KAPPAS[len(KAPPAS) // 2])]
    results["exemplar_full_support"] = {
        "node": {kk: ex[kk] for kk in ("tau", "tau_quantile", "T", "kappa",
                                       "Omega", "pi_bar_pr",
                                       "pi_bar_floorfree")},
        "values": [float(x) for x in ex["_vals"]],
        "masses": [float(x) for x in ex["_wts"]],
        "note": "floor-free law; single-linkage clustering at 1e-12",
    }
    results["baseline"] = {
        "k": list(k), "tau_reference": tau_med, "T": p_base.T, "H": p_base.H,
        "Delta_m": dm,
        "cutoff_scale": resid.cutoff_scale, "payoff_scale": resid.payoff_scale,
    }
    results["n_pooled_evaluations"] = n_eval
    results["seconds"] = time.perf_counter() - t0
    results["all_pass"] = results["n_fail"] == 0
    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2, default=float)

    print(f"\nVERDICT: {verdict}")
    print(f"  nodes {len(rows)} total, {len(deg)} degenerate, {len(nd)} "
          f"non-degenerate, {n_hold} where A(tau) holds")
    print("  clause failures: "
          f"{json.dumps(results['verdict_detail']['clause_breakdown'])}")
    print(f"  {results['n_fail']} check(s) report FAIL "
          f"({results['n_vacuous']} vacuous, {results['n_gate_fail']} gate)"
          f"  in {results['seconds']:.0f} s  ->  {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
