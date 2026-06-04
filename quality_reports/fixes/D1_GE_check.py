"""
D1_GE_check.py  --  Reproduction driver for D1_prop6_GE_cutoffshift.tex
=======================================================================

RUNS AS-IS with a scipy-bearing interpreter, e.g.

    PYTHONPATH=/Users/austinli/Projects/blockholder \
        /tmp/blockholder_venv/bin/python \
        quality_reports/fixes/D1_GE_check.py

It writes a machine-readable artifact

    quality_reports/fixes/D1_GE_check_out.json

that CONTAINS every number cited in the proof (the linchpin local-invertibility
evidence det(D_kF^R), rho(D_kT^R), ||D_kT^R||_inf, U_Q-U_H, AND the chain-rule
GE-curvature decomposition).

CORRECT API (verified live; the earlier published driver documented the WRONG
signatures and raised TypeError):
    solver.solve_valid(params, prev_cutoffs=None, residual_tol=...)
        -> (Cutoffs | None, residual)              # params FIRST, multi-start internal
    solver.equilibrium_residual(k1, k0, kD, params) -> float
    model.compute_action_probabilities(k1, k0, kD, params)
        -> (omega_E, omega_H, omega_Q, omega_P)    # a 4-TUPLE, not a dict
    model.compute_posteriors(oE, oH, oQ, oP, kappa) -> dict[(X,D) -> pi]
    model.compute_equilibrium_prices(k1, k0, kD, params) -> dict[(X,D) -> P]
    model.compute_expected_payoff(action, s, prices, posteriors, params) -> float
        # takes PRE-COMPUTED prices+posteriors; does NOT solve prices internally;
        # arg order is (action, s, ...)
    model.compute_minority_gains(k1, k0, kD, params).total -> Delta^min
"""
import json
import dataclasses
import traceback
import numpy as np

from numerical import solver, model
from numerical.params import ModelParams, Action

OUT = ("/Users/austinli/Projects/blockholder/quality_reports/fixes/"
       "D1_GE_check_out.json")

BASE = ModelParams()


def pk(kappa, **over):
    return dataclasses.replace(BASE, kappa=kappa, **over)


def solve(kappa, prev=None, tol=1e-7, **over):
    p = pk(kappa, **over)
    cut, resid = solver.solve_valid(p, prev_cutoffs=prev, residual_tol=tol)
    return cut, resid, p


def dmin(cut, p):
    return model.compute_minority_gains(cut.k1, cut.k0, cut.kD, p).total


def indep_resid(cut, p):
    """Independent recomputation of the gate residual at returned cutoffs."""
    return solver.equilibrium_residual(cut.k1, cut.k0, cut.kD, p)


# --- the merged-cutoff (Case R) reduced residual via the CORRECT payoff path ---
def reduced_F(k1, kD, kappa, **over):
    """F^R = (U_E - U_Q at k1, U_Q - U_P at kD); also returns U_Q - U_H at k1."""
    p = pk(kappa, **over)
    prices = model.compute_equilibrium_prices(k1, k1, kD, p)
    oE, oH, oQ, oP = model.compute_action_probabilities(k1, k1, kD, p)
    post = model.compute_posteriors(oE, oH, oQ, oP, kappa)
    U = lambda a, s: model.compute_expected_payoff(a, s, prices, post, p)
    UE = U(Action.EXIT, k1)
    UQ1 = U(Action.QUIET, k1)
    UH1 = U(Action.HOLD, k1)
    UQd = U(Action.QUIET, kD)
    UP = U(Action.PUBLIC, kD)
    return np.array([UE - UQ1, UQd - UP]), (UQ1 - UH1)


def main():
    out = {"_api_ok": True}

    # ---------- GATE (Lemma: independent residual recompute, accept < 1e-5) ----
    gate = {}
    for k in [0.05, 0.30, 0.59, 0.95, 0.02, 0.98]:
        try:
            cut, _, p = solve(k, None, 1e-5)
            r = indep_resid(cut, p)
            gate[str(k)] = {"resid": float(r), "Dmin": float(dmin(cut, p)),
                            "cut": [cut.k1, cut.k0, cut.kD],
                            "pass": bool(r < 1e-5)}
        except Exception as e:
            gate[str(k)] = {"error": repr(e)}
    out["gate"] = gate

    # ---------- 19-point certified profile (sign pattern of Phi') -------------
    grid = [round(0.05 + i * 0.05, 2) for i in range(19)]  # 0.05..0.95
    prof = {}
    prev = None
    for k in grid:
        cut, _, p = solve(k, prev, 1e-7)
        r = indep_resid(cut, p)
        prof[str(k)] = {"Dmin": float(dmin(cut, p)), "resid": float(r),
                        "cut": [cut.k1, cut.k0, cut.kD]}
        prev = cut
    out["profile19"] = prof
    vals = [prof[str(k)]["Dmin"] for k in grid]
    diffs = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
    signs = "".join("+" if d > 0 else "-" for d in diffs)
    out["Phi_prime_signs"] = signs
    out["grid_argmax_kappa"] = grid[int(np.argmax(vals))]
    out["n_pos"] = signs.count("+")
    out["n_neg"] = signs.count("-")
    out["all_gate_pass19"] = all(prof[str(k)]["resid"] < 1e-5 for k in grid)

    # ---------- dk/dkappa at kstar -- ONE committed invocation ----------------
    KS = 0.59
    H = 0.02
    cs, _, ps = solve(KS, None, 1e-7)
    cm, _, pm = solve(KS - H, cs, 1e-7)
    cpu, _, pp = solve(KS + H, cs, 1e-7)
    dk1 = (cpu.k1 - cm.k1) / (2 * H)
    dk0 = (cpu.k0 - cm.k0) / (2 * H)
    dkD = (cpu.kD - cm.kD) / (2 * H)
    out["dk_dkappa"] = {"dk1": dk1, "dk0": dk0, "dkD": dkD,
                        "kstar": KS, "h": H,
                        "cut_star": [cs.k1, cs.k0, cs.kD]}

    # ---------- theta (PE, cutoffs FROZEN) and Phi'' (full eq) ----------------
    # theta := -d^2 hatDelta/dkappa^2 with cutoffs frozen at c*(KS)
    def hatDelta(kappa):  # cutoffs frozen at cs
        return model.compute_minority_gains(cs.k1, cs.k0, cs.kD, pk(kappa)).total
    theta = -(hatDelta(KS + H) - 2 * hatDelta(KS) + hatDelta(KS - H)) / H ** 2
    # Phi'' full-equilibrium second difference (cutoffs move with kappa)
    Phi_pp = (dmin(cpu, pp) - 2 * dmin(cs, ps) + dmin(cm, pm)) / H ** 2
    out["theta_PE_curv"] = theta
    out["Phi_pp_fulleq"] = Phi_pp
    out["Sigma_curv_residual_def"] = Phi_pp + theta  # = Phi'' - (-theta)
    out["ratio_residual_def"] = abs(Phi_pp + theta) / abs(theta)

    # ---------- NON-CIRCULAR Sigma'' via the chain rule on Sigma(kappa) -------
    # Sigma(kappa) = grad_k hatDelta . dk/dkappa.  We compute Sigma at three
    # kappa nodes by (a) solving cutoffs k(kappa), (b) grad_k hatDelta by
    # central differences in (k1=k0, kD) at frozen kappa, (c) dk/dkappa by
    # central differences of the warm-started selection.  Then
    #   Sigma''(kstar) ~ [Sigma(KS+H) - 2 Sigma(KS) + Sigma(KS-H)]/H^2 .
    # This is an INDEPENDENT second derivative of the GE channel, NOT the
    # residual Phi''+theta, so the smallness check is non-tautological.
    def grad_k_hat(cut, kappa):
        p = pk(kappa)
        ek, eD = 1e-5, 1e-5
        # k1 and k0 move together in Case R; perturb the merged cutoff km=k1=k0
        def D(k1, k0, kD):
            return model.compute_minority_gains(k1, k0, kD, p).total
        dkm = (D(cut.k1 + ek, cut.k0 + ek, cut.kD)
               - D(cut.k1 - ek, cut.k0 - ek, cut.kD)) / (2 * ek)
        dD = (D(cut.k1, cut.k0, cut.kD + eD)
              - D(cut.k1, cut.k0, cut.kD - eD)) / (2 * eD)
        return dkm, dD  # (d/dkm, d/dkD) with km the merged Exit/Quiet cutoff

    def dk_dkappa_at(kappa, seed):
        h = 0.02
        cl, _, _ = solve(kappa - h, seed, 1e-7)
        cr, _, _ = solve(kappa + h, seed, 1e-7)
        return (cr.k1 - cl.k1) / (2 * h), (cr.kD - cl.kD) / (2 * h)

    def Sigma_at(kappa, seed):
        c, _, _ = solve(kappa, seed, 1e-7)
        gkm, gD = grad_k_hat(c, kappa)
        dkm, dkDk = dk_dkappa_at(kappa, c)
        return gkm * dkm + gD * dkDk, c

    Sig_m, c_m = Sigma_at(KS - H, cm)
    Sig_0, c_0 = Sigma_at(KS, cs)
    Sig_p, c_p = Sigma_at(KS + H, cpu)
    Sigma_pp = (Sig_p - 2 * Sig_0 + Sig_m) / H ** 2
    out["Sigma_chainrule"] = {"Sigma_minus": Sig_m, "Sigma_star": Sig_0,
                              "Sigma_plus": Sig_p, "Sigma_pp": Sigma_pp,
                              "ratio_chainrule": abs(Sigma_pp) / abs(theta)}
    # Consistency check: Phi'' should ~ -theta + Sigma'' (chain rule identity,
    # up to the Sigma' first-order term being differentiated; we report both).
    out["consistency_Phi_pp_vs_minus_theta_plus_Sigma_pp"] = {
        "Phi_pp": Phi_pp, "minus_theta_plus_Sigma_pp": -theta + Sigma_pp}

    # ---------- V2: local invertibility (det, rho, inf-norm, U_Q-U_H) ---------
    v2 = {}
    for k in [0.2, 0.5, 0.8]:
        c, _, p = solve(k, None, 1e-7)
        eps = 1e-5
        F0, uqmh = reduced_F(c.k1, c.kD, k)
        J = np.zeros((2, 2))
        J[:, 0] = (reduced_F(c.k1 + eps, c.kD, k)[0]
                   - reduced_F(c.k1 - eps, c.kD, k)[0]) / (2 * eps)
        J[:, 1] = (reduced_F(c.k1, c.kD + eps, k)[0]
                   - reduced_F(c.k1, c.kD - eps, k)[0]) / (2 * eps)
        Sd = np.diag(np.diag(J))
        DkT = np.eye(2) - np.linalg.inv(Sd) @ J
        v2[str(k)] = {
            "cut": [c.k1, c.k0, c.kD],
            "Fnorm": float(np.linalg.norm(F0)),
            "UQ_minus_UH_at_k1": float(uqmh),
            "det_DkF": float(np.linalg.det(J)),
            "rho_DkT": float(np.max(np.abs(np.linalg.eigvals(DkT)))),
            "inf_DkT": float(np.max(np.sum(np.abs(DkT), axis=1))),
            "omega_H": float(model.compute_action_probabilities(
                c.k1, c.k0, c.kD, p)[1]),
        }
    out["V2_local_invertibility"] = v2

    # ---------- Case F exhibit: a calibration with omega_H > 0 (pi_bar < 1) ---
    # Hold collapses at the headline calibration (high engagement value). To open
    # Hold we raise the engagement cost C0 modestly so Quiet is no longer
    # preferred just above k1, creating a genuine k1<k0<kD interior (3x3) regime
    # WITH omega_Q>0 (so pi_bar in (0,1) is a nondegenerate chord). Too-large C0
    # kills Quiet entirely (omega_Q->0, pi_bar->0, residual blows up); the clean
    # window is around C0=0.20 at low/moderate kappa. We scan C0 and kappa and
    # keep gate-passing Case-F points.
    caseF = {}
    for C0 in [0.18, 0.20, 0.22]:
        for k in [0.15, 0.20, 0.25]:
            c, _, p = solve(k, None, 1e-6, C0=C0)
            r = indep_resid(c, p)
            oE, oH, oQ, oP = model.compute_action_probabilities(c.k1, c.k0, c.kD, p)
            pibar = oQ / (oH + oQ) if (oH + oQ) > 1e-12 else None
            caseF[f"C0={C0},k={k}"] = {
                "cut": [c.k1, c.k0, c.kD], "resid": float(r),
                "omega_H": float(oH), "omega_Q": float(oQ),
                "pi_bar": (float(pibar) if pibar is not None else None),
                "hold_open": bool(c.k0 - c.k1 > 1e-4),
                "gate_pass": bool(r < 1e-5),
                "Dmin": float(dmin(c, p))}
    out["caseF_exhibit"] = caseF
    # Case-F hump check on a gate-passing Case-F branch (C0=0.20), warm-started.
    caseFhump = {}
    prevF = None
    for k in [0.10, 0.15, 0.20, 0.25, 0.30]:
        c, _, p = solve(k, prevF, 1e-6, C0=0.20)
        r = indep_resid(c, p)
        oE, oH, oQ, oP = model.compute_action_probabilities(c.k1, c.k0, c.kD, p)
        pibar = oQ / (oH + oQ) if (oH + oQ) > 1e-12 else None
        caseFhump[str(k)] = {"Dmin": float(dmin(c, p)), "resid": float(r),
                             "omega_H": float(oH),
                             "pi_bar": (float(pibar) if pibar is not None else None),
                             "hold_open": bool(c.k0 - c.k1 > 1e-4),
                             "cut": [round(c.k1, 4), round(c.k0, 4), round(c.kD, 4)]}
        prevF = c
    out["caseF_hump"] = caseFhump

    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print("WROTE", OUT)
    # echo the linchpin numbers
    print("Phi' signs:", signs, "argmax", out["grid_argmax_kappa"])
    print("dk1,dk0,dkD:", round(dk1, 5), round(dk0, 5), round(dkD, 5))
    print("theta:", round(theta, 4), "Phi'':", round(Phi_pp, 4),
          "Sigma_curv(resid):", round(Phi_pp + theta, 4),
          "Sigma''(chain):", round(Sigma_pp, 4))
    for k, rec in v2.items():
        print("V2", k, "det", round(rec["det_DkF"], 4),
              "rho", round(rec["rho_DkT"], 3),
              "inf", round(rec["inf_DkT"], 3),
              "UQ-UH", round(rec["UQ_minus_UH_at_k1"], 4))
    for c0, rec in caseF.items():
        print("CaseF", c0, [round(x, 4) for x in rec["cut"]], "wH",
              round(rec["omega_H"], 5), "wQ", round(rec["omega_Q"], 5),
              "pi_bar", (round(rec["pi_bar"], 4) if rec["pi_bar"] else None),
              "hold_open", rec["hold_open"], "gate", rec["gate_pass"],
              "resid", f"{rec['resid']:.2e}")
    print("--- Case F hump (C0=0.20) ---")
    for k, rec in caseFhump.items():
        print("  k", k, "Dmin", round(rec["Dmin"], 6), "wH", round(rec["omega_H"], 5),
              "pi_bar", (round(rec["pi_bar"], 4) if rec["pi_bar"] else None),
              "hold_open", rec["hold_open"], "resid", f"{rec['resid']:.2e}")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(traceback.format_exc())
        with open(OUT, "w") as f:
            json.dump({"FATAL": traceback.format_exc()}, f, indent=2)
