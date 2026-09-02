"""Existence conditions on a certified box: the grid check for ticket 05.

At order size two an equilibrium of the two-round model is a fixed point of the
outer map T on the ordered cutoff polytope Theta = {s_lo <= k1 <= k2 <= s_hi},
where T(k) holds the unique zeros of the two adjacent-plan payoff gaps at the
prices the cutoffs k induce.  The statement in ``proofs/05_existence.tex`` is
conditional: if a box B inside Theta carries the single down-crossing structure
at every k (B3), clears the k-free breakpoint set in its Voice coordinate (B2),
and satisfies the Miranda face signs (B4), then an equilibrium exists in B.
This script builds B around the solver's candidate at each calibration node and
verifies the conditions on a stated probe grid.

Checks:

  ex_standing_primitives    wiring       the parameter signs the inner-price
                                         lemma needs (m0 > 0, Delta_m > 0,
                                         sigma_xi > 0, sigma_v > 0,
                                         sigma_eps > 0, kappa in (0,1),
                                         0 < b0 < tau < b_bar, mark = 2)
  ex_candidate              wiring       the solver candidate's P1 residuals;
                                         the payoff scale 1e-9 is binding
  ex_B1                     substantive  (B1): B strictly interior to Theta
                                         and ordered (k1+ < k2-)
  ex_B2                     substantive  (B2): the Voice coordinate [k2-, k2+]
                                         is disjoint from the k-free
                                         breakpoint set (n-jumps and
                                         tau-crossing pull-backs)
  ex_B3                     substantive  (B3): at each of the 9 probe cutoffs
                                         (3 x 3 on B), each adjacent-plan gap
                                         has exactly one down-crossing on the
                                         2001-point signal grid, and the zeros
                                         are ordered z_EH <= z_HV.  The probe
                                         is not a proof of (B3) at every
                                         point of B
  ex_B4                     substantive  (B4): T1 >= k1- on the left face,
                                         T1 <= k1+ on the right face,
                                         T2 >= k2- on the lower face,
                                         T2 <= k2+ on the upper face, each
                                         with its minimum margin reported
  ex_inner_certificate      substantive  the inner pricing fixed point's
                                         certified bracket held and converged
                                         at every probe
  ex_a7                     substantive  the flagged-injectivity certificate
                                         passes at every probe

NODES.  A calibration node is a pair (T, tau_q): T in {5, 10} and tau_q the
five frozen quantiles (0.1, 0.3, 0.5, 0.7, 0.9) of the seed equilibrium's Voice
b*(s) distribution, exactly the ladder the t2 checks sweep, at the baseline
liquidity kappa = 0.5.  ``--nodes n`` runs the first n nodes only; node order
is T = 5 first, quantiles ascending, then T = 10.  Each node's candidate is
solved warm from the previous node's solution (node 1 from the seed
equilibrium's cutoffs).

MEASUREMENT.  The gaps are evaluated pointwise by ``plan_payoff`` on a
2001-point signal grid against a fresh pooled pass at each probe; crossings are
located by linear interpolation inside the sign-change bracket.  This route
shares no code with the solver's bracket-and-brentq outer map, so the probe T
at the box centre also cross-checks the candidate's fixed-point residual.

Deterministic: no RNG in the checks themselves (the candidate solve is seeded
at 0), no Monte Carlo, no file inputs, no network.

Run:    .venv/bin/python numerical_v4/checks/t5_existence_conditions.py [--nodes N]
Output: numerical_v4/checks/t5_existence_conditions.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from numerical_v4.menu import a7_certificate, atoms, breakpoints  # noqa: E402
from numerical_v4.params import EXIT, HOLD, VOICE, ParamsV4  # noqa: E402
from numerical_v4.policy import frozen_tau_grid, plan_payoff  # noqa: E402
from numerical_v4.pooled import pooled_pass  # noqa: E402
from numerical_v4.solver import TOL_CUTOFF, TOL_PAYOFF, solve_policy  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "t5_existence_conditions.json")

TOL_INNER: float = 1e-10       # inner fixed point residual, smoke's scale
N_S: int = 2001                # signal grid for the gap evaluation
DELTA0: float = 2e-3           # box half-width, in signal units
DELTA_MIN: float = 1e-5        # smallest admissible half-width
EDGE_FRAC: float = 0.25        # the box keeps delta <= EDGE_FRAC * edge clearance

QUANTILES = (0.1, 0.3, 0.5, 0.7, 0.9)
TS = (5, 10)
NODES = [(T, q) for T in TS for q in QUANTILES]

results: dict = {"checks": [], "n_fail": 0}


def record(name: str, ok: bool, kind: str, detail: dict) -> None:
    results["checks"].append(
        {"name": name, "kind": kind, "pass": bool(ok), **detail}
    )
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({kind})", flush=True)
    print("        " + json.dumps(detail, default=float)[:1200], flush=True)


# ---------------------------------------------------------------------------
# Gap evaluation and crossing structure
# ---------------------------------------------------------------------------


def gap_grid(k: tuple[float, float], p: ParamsV4, sgrid: np.ndarray):
    """Pooled pass at k, then both adjacent-plan gaps on the signal grid."""
    res = pooled_pass(atoms(k, p), p, with_runup=True)
    g_eh = np.empty(sgrid.size)
    g_hv = np.empty(sgrid.size)
    for i, s in enumerate(sgrid):
        s = float(s)
        u_e = plan_payoff(EXIT, s, res, p)
        u_h = plan_payoff(HOLD, s, res, p)
        u_v = plan_payoff(VOICE, s, res, p)
        g_eh[i] = u_e - u_h
        g_hv[i] = u_h - u_v
    return res, g_eh, g_hv


def down_crossing(sgrid: np.ndarray, g: np.ndarray):
    """Unique down-crossing of g on the grid: (z, n_changes) or (None, n).

    A down-crossing is a sign change from nonnegative to negative.  The
    crossing point is linear interpolation inside the bracket.
    """
    neg = np.signbit(g)
    changes = np.flatnonzero(neg[1:] != neg[:-1])
    if changes.size != 1 or neg[0] or not neg[-1]:
        return None, int(changes.size)
    i = int(changes[0])
    if not (g[i] >= 0.0 and g[i + 1] <= 0.0):
        return None, int(changes.size)
    t = float(g[i] / (g[i] - g[i + 1]))
    z = float(sgrid[i] + t * (sgrid[i + 1] - sgrid[i]))
    return z, 1


# ---------------------------------------------------------------------------
# One node
# ---------------------------------------------------------------------------


def run_node(p: ParamsV4, k_init: tuple[float, float],
             sgrid: np.ndarray) -> dict:
    """Solve the candidate, build the box, probe the conditions."""
    node: dict = {"tau": float(p.tau), "T": int(p.T), "kappa": float(p.kappa),
                  "params_hash": p.hash_str()}

    t0 = time.perf_counter()
    pol, resid = solve_policy(p, k_init=k_init)
    khat = (float(pol.k[0]), float(pol.k[1]))
    node["k_hat"] = list(khat)
    node["solve_seconds"] = time.perf_counter() - t0
    node["cutoff_scale"] = float(resid.cutoff_scale)
    node["payoff_scale"] = float(resid.payoff_scale)
    node["candidate_ok"] = bool(resid.payoff_scale < TOL_PAYOFF)
    print(f"  candidate k = ({khat[0]:.8f}, {khat[1]:.8f})   "
          f"cutoff {resid.cutoff_scale:.2e}  payoff {resid.payoff_scale:.2e} "
          f"({node['solve_seconds']:.0f} s)", flush=True)

    # The k-free breakpoint set: n-jumps and tau-crossing pull-backs, i.e. the
    # breakpoint list with the cutoffs placed outside the support.
    free = breakpoints((p.s_lo - 1.0, p.s_hi + 1.0), p)
    free = free[(free > p.s_lo + 1e-12) & (free < p.s_hi - 1e-12)]
    edge_clear = float(np.min(np.abs(free - khat[1]))) if free.size \
        else float("inf")

    delta = min(DELTA0, EDGE_FRAC * edge_clear)
    k1m, k1p = khat[0] - delta, khat[0] + delta
    k2m, k2p = khat[1] - delta, khat[1] + delta
    b1_ok = (delta >= DELTA_MIN
             and k1p < k2m
             and k1m > p.s_lo
             and k2p < p.s_hi
             and np.isfinite(delta))
    if free.size:
        b2_ok = not bool(np.any((free >= k2m - 1e-15) & (free <= k2p + 1e-15)))
    else:
        b2_ok = True
    box_ok = bool(b1_ok and b2_ok)
    node["b0_lt_tau"] = bool(p.b0 < p.tau)
    node["box"] = {"delta": float(delta), "edge_clearance": edge_clear,
                   "k1_minus": float(k1m), "k1_plus": float(k1p),
                   "k2_minus": float(k2m), "k2_plus": float(k2p),
                   "n_free_breakpoints": int(free.size),
                   "B1": bool(b1_ok), "B2": bool(b2_ok),
                   "ok": bool(box_ok)}
    if not box_ok:
        node["probes"] = []
        node["conditions"] = {"B1": bool(b1_ok), "B2": bool(b2_ok),
                              "B3": False, "B4": False,
                              "inner_certificate": False, "a7": False,
                              "candidate": node["candidate_ok"],
                              "b0_lt_tau": node["b0_lt_tau"]}
        node["node_ok"] = False
        node["fail_reason"] = (
            "no admissible box: (B1) interior ordered box or (B2) Voice "
            "coordinate disjoint from the k-free breakpoint set failed "
            "before any probe ran")
        return node

    # The 3 x 3 probe grid on B.  Face tags avoid float-equality on k.
    k1s = (k1m, khat[0], k1p)
    k2s = (k2m, khat[1], k2p)
    probes = []
    for i, k1 in enumerate(k1s):
        for j, k2 in enumerate(k2s):
            k = (float(k1), float(k2))
            faces: list[str] = []
            if i == 0:
                faces.append("left")
            if i == 2:
                faces.append("right")
            if j == 0:
                faces.append("lower")
            if j == 2:
                faces.append("upper")
            if i == 1 and j == 1:
                faces.append("centre")
            row: dict = {"k": list(k), "faces": faces}
            try:
                res, g_eh, g_hv = gap_grid(k, p, sgrid)
                z1, n1 = down_crossing(sgrid, g_eh)
                z2, n2 = down_crossing(sgrid, g_hv)
                a7 = a7_certificate(k, p)
                row.update({
                    "z_EH": z1, "z_HV": z2, "T1": z1, "T2": z2,
                    "n_changes_EH": n1, "n_changes_HV": n2,
                    "g_EH_lo": float(g_eh[0]), "g_EH_hi": float(g_eh[-1]),
                    "g_HV_lo": float(g_hv[0]), "g_HV_hi": float(g_hv[-1]),
                    "zeros_ordered": bool(z1 is not None and z2 is not None
                                          and z1 <= z2),
                    "inner_residual": float(res.max_price_residual),
                    "multiple_root_nodes": int(res.multiple_root_nodes),
                    "inner_ok": bool(res.multiple_root_nodes == 0
                                     and res.max_price_residual < TOL_INNER),
                    "a7_passes": bool(a7.passes),
                    "a7_min_slope": float(a7.min_slope),
                })
            except Exception as exc:  # a raised assert is a finding, recorded
                row.update({"error": f"{type(exc).__name__}: {exc}",
                            "inner_ok": False, "a7_passes": False,
                            "z_EH": None, "z_HV": None, "T1": None, "T2": None,
                            "n_changes_EH": -1, "n_changes_HV": -1,
                            "zeros_ordered": False})
            probes.append(row)
            print(f"    probe k=({k[0]:.6f}, {k[1]:.6f})  z_EH={row['z_EH']} "
                  f"z_HV={row['z_HV']}  changes=({row['n_changes_EH']},"
                  f"{row['n_changes_HV']})", flush=True)
    node["probes"] = probes

    # (B3) single ordered down-crossings at every probe.
    crossing_ok = all(r["n_changes_EH"] == 1 and r["n_changes_HV"] == 1
                      and r["zeros_ordered"] for r in probes)
    # Inner certificate and injectivity at every probe.
    inner_ok = all(r["inner_ok"] for r in probes)
    a7_ok = all(r["a7_passes"] for r in probes)
    # (B4) Miranda face signs, with margins.  On the left face T1 - k1- >= 0,
    # on the right k1+ - T1 >= 0, on the lower T2 - k2- >= 0, on the upper
    # k2+ - T2 >= 0.  T = (z_EH, z_HV) as in the theorem.
    m_left = min((r["T1"] - k1m for r in probes
                  if "left" in r["faces"] and r["T1"] is not None),
                 default=float("nan"))
    m_right = min((k1p - r["T1"] for r in probes
                   if "right" in r["faces"] and r["T1"] is not None),
                  default=float("nan"))
    m_low = min((r["T2"] - k2m for r in probes
                 if "lower" in r["faces"] and r["T2"] is not None),
                default=float("nan"))
    m_high = min((k2p - r["T2"] for r in probes
                  if "upper" in r["faces"] and r["T2"] is not None),
                 default=float("nan"))
    faces_ok = all(np.isfinite(m) and m > 0.0
                   for m in (m_left, m_right, m_low, m_high))
    node["miranda_margins"] = {"left": float(m_left), "right": float(m_right),
                               "lower": float(m_low), "upper": float(m_high)}

    # Diagnostic: the probe T at the box centre against the candidate.
    centre = next(r for r in probes if "centre" in r["faces"])
    node["probe_T_at_centre"] = [centre["T1"], centre["T2"]]
    node["probe_T_minus_khat"] = [
        float(centre["T1"] - khat[0]) if centre["T1"] is not None else None,
        float(centre["T2"] - khat[1]) if centre["T2"] is not None else None,
    ]

    node["conditions"] = {"B1": bool(b1_ok),
                          "B2": bool(b2_ok),
                          "B3": bool(crossing_ok),
                          "B4": bool(faces_ok),
                          "inner_certificate": bool(inner_ok),
                          "a7": bool(a7_ok),
                          "candidate": node["candidate_ok"],
                          "b0_lt_tau": node["b0_lt_tau"]}
    node["node_ok"] = bool(all(node["conditions"].values()))
    return node


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--nodes", type=int, default=len(NODES),
                    help="run only the first n calibration nodes")
    args = ap.parse_args()
    n_run = max(0, min(args.nodes, len(NODES)))

    t0 = time.perf_counter()
    p_seed = ParamsV4.baseline()
    assert p_seed.mark == 2, "this check is stated at order size two"
    print(f"t5_existence_conditions -- mark={p_seed.mark} H={p_seed.H} "
          f"nodes to run: {n_run} of {len(NODES)}", flush=True)

    prim_ok = (p_seed.m0 > 0.0 and p_seed.Delta_m > 0.0
               and p_seed.sigma_xi > 0.0 and p_seed.sigma_v > 0.0
               and p_seed.sigma_eps > 0.0
               and 0.0 < p_seed.kappa < 1.0
               and 0.0 < p_seed.b0 < p_seed.tau < p_seed.b_bar
               and int(p_seed.mark) == 2)
    record("ex_standing_primitives", prim_ok, "wiring",
           {"request": "the parameter signs the inner-price lemma needs, "
                       "together with 0 < b0 < tau < b_bar and mark = 2",
            "m0": p_seed.m0, "Delta_m": p_seed.Delta_m,
            "sigma_xi": p_seed.sigma_xi, "sigma_v": p_seed.sigma_v,
            "sigma_eps": p_seed.sigma_eps, "kappa": p_seed.kappa,
            "b0": p_seed.b0, "tau": p_seed.tau, "b_bar": p_seed.b_bar,
            "mark": int(p_seed.mark),
            "kappa_in_unit_interval": bool(0.0 < p_seed.kappa < 1.0),
            "b0_lt_tau_lt_bbar": bool(0.0 < p_seed.b0 < p_seed.tau
                                      < p_seed.b_bar)})

    print("  seed solve (freezes the tau ladder) ...", flush=True)
    pol_seed, resid_seed = solve_policy(p_seed)
    taus = tuple(float(x) for x in frozen_tau_grid(pol_seed, p_seed, QUANTILES))
    k_prev = (float(pol_seed.k[0]), float(pol_seed.k[1]))
    print(f"  seed k = {k_prev}  tau ladder "
          f"{['%.8f' % t for t in taus]}", flush=True)

    results["provenance"] = {
        "script": "numerical_v4/checks/t5_existence_conditions.py",
        "ticket": "05-existence-if-clean",
        "params_hash": p_seed.hash_str(),
        "mark": int(p_seed.mark), "H": int(p_seed.H),
        "kappa": float(p_seed.kappa),
        "tau_ladder": list(taus), "tau_quantiles": list(QUANTILES),
        "T_grid": list(TS),
        "node_order": [{"T": T, "tau_quantile": q} for T, q in NODES],
        "nodes_requested": int(args.nodes), "nodes_run": int(n_run),
        "seed_k": list(k_prev),
        "seed_cutoff_scale": float(resid_seed.cutoff_scale),
        "seed_payoff_scale": float(resid_seed.payoff_scale),
        "signal_grid_points": N_S,
        "probe_grid": "3 x 3 on the box B = k_hat +/- delta in each coordinate",
        "box_half_width_rule": f"delta = min({DELTA0}, {EDGE_FRAC} x clearance "
                               f"from k2 to the k-free breakpoint set), floor "
                               f"{DELTA_MIN}",
        "tolerances": {"payoff_scale": TOL_PAYOFF, "cutoff_scale": TOL_CUTOFF,
                       "inner_residual": TOL_INNER},
        "measurement": "gaps by pointwise plan_payoff on a 2001-point signal "
                       "grid at a fresh pooled pass per probe; crossings by "
                       "linear interpolation inside the sign-change bracket; "
                       "no code shared with the solver's outer map",
        "statement": "proofs/05_existence.tex; the theorem is conditional on "
                     "(B1)-(B4), which this record verifies node by node on "
                     "the 3 x 3 probe grid (not a proof of (B3) at every "
                     "point of B)",
        "named_conditions": ["B1", "B2", "B3", "B4"],
        "B1": "interior ordered box, strictly inside Theta",
        "B2": "Voice coordinate [k2-, k2+] disjoint from the k-free "
              "breakpoint set",
        "B3": "unique ordered down-crossings of both adjacent-plan gaps "
              "at every k in B; the probe grid checks the nine listed "
              "points",
        "B4": "Miranda face signs of F(k) = T(k) - k on the four faces of B",
    }

    sgrid = np.linspace(p_seed.s_lo, p_seed.s_hi, N_S)
    nodes_out = []
    for i in range(n_run):
        T, q = NODES[i]
        tau = taus[QUANTILES.index(q)]
        p = p_seed.replace(tau=float(tau), T=int(T))
        print(f"  node {i + 1}: T={T} q={q} tau={tau:.8f}", flush=True)
        node = run_node(p, k_prev, sgrid)
        node["node_index"] = i + 1
        node["tau_quantile"] = float(q)
        nodes_out.append(node)
        if node.get("k_hat") is not None and node["candidate_ok"]:
            k_prev = tuple(node["k_hat"])
        print(f"  node {i + 1} verdict: "
              f"{'OK' if node['node_ok'] else 'NOT OK'}  "
              f"{node.get('conditions', node.get('fail_reason'))}", flush=True)

    results["nodes"] = nodes_out
    n_bad = sum(1 for nd in nodes_out if not nd["node_ok"])

    def _all_cond(key: str) -> bool:
        return bool(n_run > 0 and all(
            nd.get("conditions", {}).get(key, False) for nd in nodes_out))

    record("ex_candidate", _all_cond("candidate"), "wiring",
           {"request": "solver candidate payoff residual below the P1 "
                       "binding scale 1e-9 at every run node",
            "nodes_run": n_run})
    record("ex_B1", _all_cond("B1"), "substantive",
           {"request": "(B1) interior ordered box at every run node",
            "nodes_run": n_run})
    record("ex_B2", _all_cond("B2"), "substantive",
           {"request": "(B2) Voice coordinate disjoint from the k-free "
                       "breakpoint set at every run node",
            "nodes_run": n_run})
    record("ex_B3", _all_cond("B3"), "substantive",
           {"request": "(B3) unique ordered down-crossings at all nine "
                       "probes; the probe grid is not a proof of (B3) at "
                       "every point of B",
            "nodes_run": n_run})
    record("ex_B4", _all_cond("B4"), "substantive",
           {"request": "(B4) Miranda face signs strictly positive at every "
                       "run node",
            "nodes_run": n_run})
    record("ex_inner_certificate", _all_cond("inner_certificate"),
           "substantive",
           {"request": "inner pricing fixed point unique and residual "
                       "below 1e-10 at every probe",
            "nodes_run": n_run})
    record("ex_a7", _all_cond("a7"), "substantive",
           {"request": "flagged-injectivity certificate at every probe",
            "nodes_run": n_run})
    record("ex_nodes", n_bad == 0 and n_run > 0, "substantive",
           {"request": "every run node carries a certified box: candidate "
                       "residual below the P1 binding scale, (B1)-(B2) box "
                       "admissible, (B3) single ordered down-crossings at all "
                       "nine probes, (B4) Miranda face signs strictly positive, "
                       "inner certificate and flagged injectivity at every "
                       "probe",
            "nodes_run": n_run, "nodes_not_ok": n_bad,
            "per_node": [{"node_index": nd["node_index"],
                          "T": nd["T"], "tau_quantile": nd["tau_quantile"],
                          "node_ok": nd["node_ok"],
                          "conditions": nd.get("conditions"),
                          "fail_reason": nd.get("fail_reason"),
                          "k_hat": nd.get("k_hat"),
                          "payoff_scale": nd.get("payoff_scale"),
                          "miranda_margins": nd.get("miranda_margins")}
                         for nd in nodes_out]})

    results["seconds"] = time.perf_counter() - t0
    results["all_pass"] = results["n_fail"] == 0
    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    print(f"\n{'ALL PASS' if results['all_pass'] else str(results['n_fail']) + ' FAIL'}"
          f"  in {results['seconds']:.0f} s  ->  {OUT}", flush=True)
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
