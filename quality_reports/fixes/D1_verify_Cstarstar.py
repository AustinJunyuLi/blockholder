#!/usr/bin/env python3
# =====================================================================
#  D1_verify_Cstarstar.py
#  Machine-checkable verification of the boxed claims in
#  D1_prop6_condition_Cstarstar.tex, using the paper's OWN solver/model.
#
#  Prints, from the repo root:
#    [1] baseline equilibrium solve (solver.solve_valid, resid<=1e-5);
#    [2] the realized four-atom D=0 law {0, pi1, pi2, pibar} + masses;
#    [3] price level P(pibar)=P(X=+1,D=0) from compute_equilibrium_prices;
#    [4] max_{pi in [0,pibar]} pi*T*T' and slack=2-max, in TWO price-level
#        conventions (price-informed and P==0 cross-check). T'=(mtilde-m0)/
#        sigma_xi on the hull (Assumption-affine P'=0; conservative);
#    [5] max second-difference of h=pi*p on [0,pibar] (<0 => concave);
#    [6] the realized equilibrium hump amplitude of Delta^min(kappa);
#    [tower] E[pi*1{D=0}] vs omega_Q (should match to ~1e-16).
#
#  ENV (per Phase-0): build a venv with scipy:
#     uv venv /tmp/blk_venv --python 3.12
#     uv pip install --python /tmp/blk_venv/bin/python scipy numpy
#  RUN:
#     PYTHONPATH=/Users/austinli/Projects/blockholder \
#       /tmp/blk_venv/bin/python \
#       /Users/austinli/Projects/blockholder/quality_reports/fixes/D1_verify_Cstarstar.py
# =====================================================================
import sys, dataclasses
import numpy as np
from scipy.stats import norm
Phi, phi = norm.cdf, norm.pdf

REPO = "/Users/austinli/Projects/blockholder"
if REPO not in sys.path:
    sys.path.insert(0, REPO)
from numerical.params import ModelParams
from numerical import solver, model


def main():
    P0 = ModelParams()
    sigma_xi, Sbar, K = P0.sigma_xi, P0.S_bar, P0.K
    m0, mtilde = P0.m0, P0.m_tilde

    print("=== D1 verification: baseline (C**) margin & hump ===")
    print(f"sigma_xi={sigma_xi} Sbar={Sbar} K={K} m0={m0} "
          f"mtilde={mtilde:.4f} delta={P0.delta} rho={P0.rho}")

    def with_k(k):
        return dataclasses.replace(P0, kappa=k)

    def solve(k, prev=None):
        cut, res = solver.solve_valid(with_k(k), prev_cutoffs=prev, residual_tol=1e-5)
        return with_k(k), cut, res

    # [1] baseline equilibrium
    Pk, cut, res = solve(0.59)
    assert cut is not None, "baseline did not converge"
    print(f"[1] kappa=0.59 solve: k1={cut.k1:.5f} k0={cut.k0:.5f} "
          f"kD={cut.kD:.5f} resid={res:.2e}")

    # [2] realized four-atom law + pibar from the model itself
    oE, oH, oQ, oP = model.compute_action_probabilities(cut.k1, cut.k0, cut.kD, Pk)
    post = model.compute_posteriors(oE, oH, oQ, oP, Pk.kappa)
    pibar = oQ / (oH + oQ) if (oH + oQ) > 0 else 1.0
    atoms = {X: post.get((X, 0)) for X in (-2, -1, 0, 1)}
    print(f"[2] omega: E={oE:.4f} H={oH:.6f} Q={oQ:.4f} P={oP:.4f}; "
          f"pibar={pibar:.6f}")
    print("    D=0 atoms: " + ", ".join(f"pi(X={X},0)={v:.4f}"
          for X, v in atoms.items() if v is not None))

    # [3] price level P(pibar) = price at (X=+1, D=0)
    prices = model.compute_equilibrium_prices(cut.k1, cut.k0, cut.kD, Pk)
    P_pibar = prices.get((1, 0))
    print(f"[3] price fixed point: P(pibar)=P(X=+1,D=0)={P_pibar}")

    # [4]/[5] curvature & slack on the hull, two price-level conventions
    hull = np.linspace(0.0, pibar, 801)
    mbar = m0 + hull * (mtilde - m0)
    Tprime = (mtilde - m0) / sigma_xi          # P'(pi)=0 on hull (Assumption affine)
    step = hull[1] - hull[0]

    def report(Plevel, tag):
        T = (mbar + K - Sbar + Plevel) / sigma_xi
        p = 1.0 - Phi(T)
        h = hull * p
        piTT = hull * T * Tprime
        mx = float(np.nanmax(piTT)); slack = 2.0 - mx
        d2 = (h[:-2] - 2 * h[1:-1] + h[2:]) / step**2
        maxd2 = float(np.nanmax(d2))
        print(f"[4|{tag}] max pi*T*T' = {mx:.4f}   slack = 2-max = {slack:.4f}"
              f"   ((C**) holds iff slack>=0)")
        print(f"[5|{tag}] max h''(2nd diff) on [0,pibar] = {maxd2:.4e}"
              f"   (<0 => concave)")
        return mx, slack, maxd2

    mx_pi, slack_pi, d2_pi = report(P_pibar if P_pibar is not None else 0.0,
                                    "price-informed")
    mx_0, slack_0, d2_0 = report(0.0, "P==0 cross-check")

    # [tower] identity at several kappa
    print("[tower] E[pi*1{D=0}] vs omega_Q:")
    for k in (0.05, 0.59, 0.95):
        Pkk, ck, _ = solve(float(k))
        e, b = ModelParams_action_eb(ck, Pkk)
        p0, p1 = 1 - k, k / 2
        po = model.compute_posteriors(*model.compute_action_probabilities(
            ck.k1, ck.k0, ck.kD, Pkk), Pkk.kappa)
        PX = {-2: e * p1, -1: e * p0 + b * p1, 0: e * p1 + b * p0, 1: b * p1}
        tower = sum(PX[X] * po.get((X, 0), 0.0) for X in PX)
        oQk = model.compute_action_probabilities(ck.k1, ck.k0, ck.kD, Pkk)[2]
        print(f"    kappa={k}: tower={tower:.6f} omega_Q={oQk:.6f} "
              f"err={abs(tower - oQk):.2e}")

    # [6] equilibrium hump amplitude.
    #   The interior peak is at kappa*~0.59 (Phase-0 99-pt grid).  We sweep the
    #   RESIDUAL-FILTERED interior [0.05,0.95]; the extreme near-endpoints
    #   (kappa<=0.03, kappa>=0.97) are grid-edge degenerate (large residual,
    #   spuriously high Delta^min) and are EXCLUDED from the peak search, per
    #   Phase-0 (the exact endpoints are not solvable equilibria).
    ks = np.round(np.linspace(0.05, 0.95, 19), 3); dmin = []; res6 = []; prev = None
    for k in ks:
        Pkk, ck, rk = solve(float(k), prev=prev)
        if ck is None or rk is None or rk > 1e-4:
            dmin.append(np.nan); res6.append(rk); continue
        prev = ck
        mg = model.compute_minority_gains(ck.k1, ck.k0, ck.kD, Pkk)
        dmin.append(float(mg.total)); res6.append(rk)
    dmin = np.array(dmin)
    fin = np.isfinite(dmin)
    peak = float(np.nanmax(dmin)); kstar = float(ks[int(np.nanargmax(dmin))])
    ends = 0.5 * (dmin[fin][0] + dmin[fin][-1]); amp = peak - ends
    # count sign changes of the first difference over residual-passing points
    d = np.diff(dmin[fin]); sg = np.sign(d); sg = sg[sg != 0]
    nsc = int(np.sum(sg[1:] != sg[:-1]))
    print(f"[6] equilibrium Delta^min (residual-filtered [0.05,0.95]): "
          f"peak={peak:.6f} at kappa*={kstar:.2f}; near-endpoint-avg={ends:.6f}; "
          f"amplitude={amp:.6f} ({100 * amp / peak:.1f}% of peak); "
          f"first-diff sign changes={nsc} (1 => single peak)")

    print("=== SUMMARY: slack>0 and h''<0 in BOTH conventions => (C**) holds; "
          "single interior peak => hump. ===")


def ModelParams_action_eb(cut, Pk):
    oE, oH, oQ, oP = model.compute_action_probabilities(cut.k1, cut.k0, cut.kD, Pk)
    return oE, oH + oQ


if __name__ == "__main__":
    main()
