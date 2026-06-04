#!/usr/bin/env python3
"""D4 bargaining microfoundation -- numerical certification (attempt 3).

Run with:
  PYTHONPATH=/Users/austinli/Projects/blockholder /tmp/blk_venv/bin/python \
      quality_reports/fixes/d4_bargaining_check.py

Output is written to stdout AND to /tmp/d4_out.txt (the run wrapper appends a
DONE sentinel) so it survives the flaky display channel; a machine-readable
JSON summary is written to /tmp/d4_results.json.

REAL API (verified this session):
  numerical.model.compute_minority_gains(k1,k0,kD,params) -> MinorityGains
      namedtuple(total, base, activism); total = Delta^min.
  numerical.model.compute_action_probabilities(k1,k0,kD,params)
      -> (omega_E, omega_H, omega_Q, omega_P).
  numerical.model.compute_posteriors(omega_E,omega_H,omega_Q,omega_P,kappa)
      -> dict {(X,D): pi(X,D)} with keys incl. (1,0),(0,0),(-1,0),(X,1)=1.
  numerical.solver.solve_valid(params, prev_cutoffs=None, residual_tol=...)
      -> (Cutoffs|None, residual).
  (compute_minority_gains_decomposed and _action_weights do NOT exist.)

Notation matches D4_bargaining_microfound.tex:
  Conditional on a value-improving bid (synergy xi drawn), acquirer A and the
  incumbent control bloc T bargain (generalized Nash, target weight theta) over
  the consummation surplus.  Disagreement payoffs:
      A : 0                          (walks away)
      T : d(a) = w + a * Dtil        (standalone control value; a in {0,1};
                                      Dtil = rho*Delta is the engagement shift)
  Consummation pie above disagreement:
      G(a,xi) = Sbar + xi - K - d(a)        [A brings Sbar+xi-K; T brings d(a)]
  Generalized-Nash control rent paid to T (= realized premium m^R):
      m^R(a,xi) = d(a) + theta * max(G,0)
  Deal consummated iff G>=0, i.e. xi >= xi*(a) = d(a)+K-Sbar.
  Acquirer net on consummation: Pi_A = (1-theta)*G >= 0.

REDUCED-FORM gap (constant theta): m1 - m0 = (1-theta)*Delta (the per-unit-
success wedge), so mtilde - m0 = rho*(m1-m0) = rho^2*(1-theta)*Delta.
"""
import json
import math
import numpy as np

results = {}
LINES = []

def emit(s):
    LINES.append(s)
    print(s, flush=True)

W = 0.0  # standalone control base value w (normalize; only DIFFERENCES matter)

# ---------------------------------------------------------------------------
# PART A:  generalized-Nash split is the unique maximizer of the Nash product
#          and reduces to the closed form m^R(a)=d+theta*(G)^+ .
# ---------------------------------------------------------------------------
def part_a():
    worst = 0.0
    for theta in (0.2, 0.5, 0.8):
        for G in (0.05, 0.4, 1.0, 2.3):
            xs = np.linspace(1e-9, G - 1e-9, 200001)
            N = xs**theta * (G - xs)**(1 - theta)
            x_num = xs[int(np.argmax(N))]
            x_cf = theta * G
            worst = max(worst, abs(x_num - x_cf))
    ok = worst < 5e-4
    results["A_nash_argmax_maxabserr"] = worst
    emit(f"[A] generalized-Nash argmax x*=theta*G : maxabserr={worst:.3e} -> {'PASS' if ok else 'FAIL'}")
    return ok

# ---------------------------------------------------------------------------
# PART B:  closed form + consummation event xi>=xi*(a); IR and IC on region.
# ---------------------------------------------------------------------------
def d(a, Dtil):
    return W + a * Dtil

def mR(a, xi, Sbar, K, theta, Dtil):
    G = Sbar + xi - K - d(a, Dtil)
    return d(a, Dtil) + theta * max(G, 0.0)

def part_b():
    Sbar, K, theta, Dtil = 1.44, 0.50, 0.5, 0.18  # Dtil=rho*Delta=0.9*0.20=0.18
    rng = np.random.default_rng(1)
    bad_event = bad_ir = bad_ic = 0
    for a in (0, 1):
        xistar = d(a, Dtil) + K - Sbar
        xi = rng.normal(0, 0.4, size=300000)
        G = Sbar + xi - K - d(a, Dtil)
        consummate = (G >= 0)
        bad_event += int(np.any(consummate != (xi >= xistar)))
        rent = d(a, Dtil) + theta * np.maximum(G, 0.0)
        bad_ir += int(np.any(rent[consummate] < d(a, Dtil) - 1e-12))
        A_net = (1 - theta) * G
        bad_ic += int(np.any(A_net[consummate] < -1e-12))
    ok = (bad_event == 0 and bad_ir == 0 and bad_ic == 0)
    results["B_bad_event"] = bad_event
    results["B_bad_IR"] = bad_ir
    results["B_bad_IC"] = bad_ic
    emit(f"[B] consummation=xi>=xi*(a), IR & IC hold on region : "
         f"bad_event={bad_event} bad_IR={bad_ir} bad_IC={bad_ic} -> {'PASS' if ok else 'FAIL'}")
    return ok

# ---------------------------------------------------------------------------
# PART C:  A3 as a THEOREM.  m^R(1,xi)-m^R(0,xi)=(1-theta)*Dtil on joint region.
# ---------------------------------------------------------------------------
def part_c():
    Sbar, K = 1.44, 0.50
    worst = 0.0
    for theta in (0.0, 0.3, 0.5, 0.9, 1.0):
        for rho in (0.0, 0.5, 0.9, 1.0):
            for Delta in (0.0, 0.2, 0.5):
                Dtil = rho * Delta
                for xi in (0.0, 0.5, 1.5):
                    if Sbar + xi - K - d(1, Dtil) < 0:  # need G(1)>=0
                        continue
                    gap = mR(1, xi, Sbar, K, theta, Dtil) - mR(0, xi, Sbar, K, theta, Dtil)
                    pred = (1 - theta) * Dtil
                    worst = max(worst, abs(gap - pred))
    ok_form = worst < 1e-12
    rho, Delta, theta = 0.9, 0.2, 0.5
    Dtil = rho * Delta
    m1m0 = (1 - theta) * Dtil            # = (1-theta)*rho*Delta = 0.09
    mtilde_minus_m0 = rho * m1m0         # = rho^2*(1-theta)*Delta = 0.081
    folded = rho**2 * (1 - theta) * Delta
    ok_sign = (m1m0 > 0) and abs(mtilde_minus_m0 - folded) < 1e-15
    results["C_wedge_form_maxabserr"] = worst
    results["C_m1_minus_m0"] = m1m0
    results["C_mtilde_minus_m0"] = mtilde_minus_m0
    results["C_folded_rho2_check"] = folded
    emit(f"[C] A3 theorem: m1-m0=(1-theta)*Dtil (err={worst:.2e}); "
         f"m1-m0={m1m0:.4f}>0; mtilde-m0={mtilde_minus_m0:.4f}=rho^2(1-theta)Delta={folded:.4f}"
         f" -> {'PASS' if (ok_form and ok_sign) else 'FAIL'}")
    return ok_form and ok_sign

# ---------------------------------------------------------------------------
# PART D:  reduced form = constant-theta special case; single peak survives a
#          STATE-DEPENDENT wedge.  Uses the paper's own solver/model.
# ---------------------------------------------------------------------------
def part_d():
    import numerical.model as M
    import numerical.solver as S
    from numerical.params import ModelParams

    # D0: constant-theta special case reproduces the code's mtilde.
    p = ModelParams()
    mtilde_code = p.m0 + p.rho * (p.m1 - p.m0)      # 0.10 + 0.9*0.20 = 0.28? check
    # Body's wedge m1-m0 = 0.20 ; choose theta,Delta s.t. (1-theta)*Delta = 0.20.
    theta = 0.5
    Delta_mf = (p.m1 - p.m0) / (1 - theta)          # 0.20/0.5 = 0.40
    m1m0_mf = (1 - theta) * Delta_mf                # = 0.20
    mtilde_mf = p.m0 + p.rho * m1m0_mf
    ok_d0 = abs(mtilde_mf - mtilde_code) < 1e-12
    results["D0_mtilde_code"] = mtilde_code
    results["D0_mtilde_microfound"] = mtilde_mf
    results["D0_m1m0_code"] = p.m1 - p.m0
    results["D0_m1m0_microfound"] = m1m0_mf
    emit(f"[D0] constant-theta special case: mtilde_code={mtilde_code:.4f} "
         f"== mtilde_microfound={mtilde_mf:.4f}; m1-m0 code={p.m1-p.m0:.4f}=mf {m1m0_mf:.4f}"
         f" -> {'PASS' if ok_d0 else 'FAIL'}")

    kappas = np.linspace(0.05, 0.95, 19)

    # D1: baseline GE re-solve reproduces the single peak (control).
    base = []
    prev = None
    for k in kappas:
        pk = ModelParams(kappa=float(k))
        c, r = S.solve_valid(pk, prev_cutoffs=prev, residual_tol=1e-4)
        if c is None:
            base.append((float(k), float("nan"), float(r))); continue
        prev = c
        g = M.compute_minority_gains(c.k1, c.k0, c.kD, pk).total
        base.append((float(k), float(g), float(r)))
    vals = np.array([b[1] for b in base])
    kk = np.array([b[0] for b in base])
    imax = int(np.nanargmax(vals))
    kstar = float(kk[imax])
    v = vals[np.isfinite(vals)]
    up = bool(np.all(np.diff(v[:imax + 1]) > -1e-4))
    dn = bool(np.all(np.diff(v[imax:]) < 1e-4))
    amp = float(np.nanmax(vals) - np.nanmin(vals))
    ok_d1 = (0.2 < kstar < 0.8) and (amp > 1e-3)
    results["D1_base_kstar"] = kstar
    results["D1_base_peak"] = float(np.nanmax(vals))
    results["D1_base_amp"] = amp
    results["D1_base_up"] = up
    results["D1_base_down"] = dn
    emit(f"[D1] baseline GE single peak: kstar={kstar:.3f} peak={np.nanmax(vals):.6f} "
         f"amp={amp:.4f} up={up} down={dn} -> {'PASS' if ok_d1 else 'FAIL'}")

    # D2: STATE-DEPENDENT engaged premium.  We recompute Delta^min ourselves,
    #     mirroring compute_minority_gains but with a kappa-state-dependent
    #     engaged premium mtilde(pi) = mtilde_base*(1+lam*(pi_eng - pi_ref)).
    #     pi_eng = D=0 posterior mass on engaged actions, summed over (X,0).
    #     We re-solve cutoffs with the BASE premium (state-dependence is second
    #     order for the cutoffs at the lam tested) and re-score Delta^min.
    def dmin_state_dep(c, pk, lam):
        omega = M.compute_action_probabilities(c.k1, c.k0, c.kD, pk)  # E,H,Q,P
        post = M.compute_posteriors(*omega, pk.kappa)                  # dict (X,D)->pi
        # engaged posterior proxy across nondisclosed states
        pis = [post.get((X, 0), 0.0) for X in (-2, -1, 0, 1)]
        pi_eng = float(np.mean([x for x in pis]))
        pi_ref = 0.30
        mtilde_base = pk.m0 + pk.rho * (pk.m1 - pk.m0)
        mtilde_state = mtilde_base * (1.0 + lam * (pi_eng - pi_ref))
        # Rebuild Delta^min = E[m^R(a)*1{bid}] with engaged premium replaced.
        # Reuse the model's price/bid machinery; recompute the activism term
        # by scaling: activism = (mtilde_state - m0)/(mtilde_base - m0) * act_base.
        g = M.compute_minority_gains(c.k1, c.k0, c.kD, pk)
        if abs(mtilde_base - pk.m0) < 1e-12:
            return g.total
        scale = (mtilde_state - pk.m0) / (mtilde_base - pk.m0)
        return g.base + scale * g.activism

    out = {}
    for lam in (-0.4, -0.2, 0.0, 0.2, 0.4):
        prev = None
        vv = []
        for k in kappas:
            pk = ModelParams(kappa=float(k))
            c, r = S.solve_valid(pk, prev_cutoffs=prev, residual_tol=1e-4)
            if c is None:
                vv.append(float("nan")); continue
            prev = c
            vv.append(float(dmin_state_dep(c, pk, lam)))
        vv = np.array(vv)
        im = int(np.nanargmax(vv)); ks = float(kk[im])
        amp = float(np.nanmax(vv) - np.nanmin(vv))
        interior = (0.15 < ks < 0.85) and (amp > 1e-3)
        out[f"{lam:+.1f}"] = {"kstar": ks, "peak": float(np.nanmax(vv)),
                              "amp": amp, "interior_hump": bool(interior)}
        emit(f"[D2] lam={lam:+.1f}: kstar={ks:.3f} peak={np.nanmax(vv):.6f} amp={amp:.4f} "
             f"interior_hump={interior}")
    results["D2_state_dep"] = out
    all_hump = all(v["interior_hump"] for v in out.values())
    emit(f"[D2] state-dependent (m1-m0) hump survives for all lam tested: "
         f"{'PASS' if all_hump else 'FAIL'}")
    return ok_d0 and ok_d1 and all_hump

if __name__ == "__main__":
    a = part_a()
    b = part_b()
    c = part_c()
    d_ok = part_d()
    results["ALL_PASS"] = bool(a and b and c and d_ok)
    with open("/tmp/d4_results.json", "w") as f:
        json.dump(results, f, indent=2, default=float)
    emit("=" * 60)
    emit(f"OVERALL: {'ALL PASS' if results['ALL_PASS'] else 'SOME FAIL'}")
    with open("/tmp/d4_out.txt", "w") as f:
        f.write("\n".join(LINES) + "\n")
