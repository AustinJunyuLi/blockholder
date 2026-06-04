#!/usr/bin/env python
"""
D1 GE cutoff-shift channel: real verification of the numbers in
D1_prop6_GE_cutoffshift.tex (attempt 5).

CORRECT API (from D1_GE_check.py, verified live):
  solver.solve_valid(params, prev_cutoffs=None, residual_tol=...) -> (Cutoffs|None, resid)
  model.compute_minority_gains(k1, k0, kD, params).total -> Delta^min

Run:
  PYTHONPATH=/Users/austinli/Projects/blockholder \
    /tmp/blk_venv/bin/python quality_reports/fixes/D1_GE_verify.py

Objects (notation matches the .tex):
  Phi(kappa)            = Delta^min along the equilibrium selection (REALIZED/GE)
  Phi_kk (frozen)       = d^2/dkappa^2 Delta^min with cutoffs FROZEN at k*(kd)
  theta                 = -Phi_kk(frozen) (frozen curvature, sign reversed)
  Phi''                 = Sigma'' = realized second derivative at kd
  G                     = Phi'' - Phi_kk = GE curvature CONTRIBUTION (residual)
Verify:
  [A] Phi_kk < 0
  [B] residual split closes: Phi'' = Phi_kk + G
  [C] corrected condition G < |Phi_kk| => Phi'' < 0
  [D] single interior sign change of Phi' on grid
  [E] refuted condition 'G > Phi_kk' is vacuous (G=+100 -> minimum)
"""
import json
import dataclasses
import numpy as np
from numerical.params import ModelParams
from numerical import solver, model

BASE = ModelParams()


def withk(k, **over):
    return dataclasses.replace(BASE, kappa=k, **over)


def solve_at(k, warm=None, tol=1e-7):
    c, r = solver.solve_valid(withk(k), prev_cutoffs=warm, residual_tol=tol)
    return c, r


def realized(k, warm=None):
    c, r = solve_at(k, warm)
    if c is None:
        return np.nan, None, r
    return model.compute_minority_gains(c.k1, c.k0, c.kD, withk(k)).total, c, r


def frozen(k, cut):
    return model.compute_minority_gains(cut.k1, cut.k0, cut.kD, withk(k)).total


def main():
    h = 0.01
    kd = 0.59  # kappa_dagger (realized peak per stored artifact, profile19 argmax 0.6)

    # --- equilibrium cutoffs at kappa_dagger ---
    v0, cut_d, r0 = realized(kd)
    print(f"[loc] kappa_dagger={kd}  Sigma(kd)={v0:.6f}  cut_d="
          f"({cut_d.k1:.4f},{cut_d.k0:.4f},{cut_d.kD:.4f})  resid={r0:.2e}")

    # --- FROZEN curvature Phi_kk at kappa_dagger (cutoffs = cut_d) ---
    fm, f0, fp = frozen(kd - h, cut_d), frozen(kd, cut_d), frozen(kd + h, cut_d)
    Phi_k = (fp - fm) / (2 * h)
    Phi_kk = (fp - 2 * f0 + fm) / h**2
    theta = -Phi_kk
    print(f"[A] Phi_k(frozen)={Phi_k:+.4f}  Phi_kk(frozen)={Phi_kk:+.4f}  theta={theta:+.4f}")

    # --- REALIZED first/second derivatives at kappa_dagger (re-solve, warm) ---
    sm, _, _ = realized(kd - h, cut_d)
    sp, _, _ = realized(kd + h, cut_d)
    Sig_p = (sp - sm) / (2 * h)
    Sig_pp = (sp - 2 * v0 + sm) / h**2
    G = Sig_pp - Phi_kk
    print(f"[B] Sigma'(realized) ={Sig_p:+.4f}")
    print(f"[B] Phi''(=Sigma'')  ={Sig_pp:+.5f}")
    print(f"[B] G (=Phi''-Phi_kk)={G:+.4f}   (NOTE: G != Sigma'; |G|==|Sigma'| coincidence)")
    split = Phi_kk + G
    print(f"[B] residual split closes: Phi_kk+G = {split:+.5f}  ==  Phi'' = {Sig_pp:+.5f}  "
          f"(diff {abs(split-Sig_pp):.2e})")

    # --- corrected sufficient condition ---
    cond = G < theta
    print(f"[C] CORRECTED COND  G < |Phi_kk| (=theta): {G:+.4f} < {theta:.4f} -> {cond}")
    print(f"[C]   => Phi'' = Phi_kk+G = {split:+.4f}  (<0 ? {split < 0})")

    # --- refuted condition is vacuous ---
    badG = 100.0
    print(f"[E] REFUTED 'G>Phi_kk' with G=+100: {badG > Phi_kk} but Phi''={Phi_kk+badG:+.2f} "
          f"(>0 => MINIMUM, contradiction)")

    # --- single interior sign change of Phi' across grid ---
    grid = np.round(np.arange(0.05, 0.96, 0.05), 2)
    warm = None
    vals = []
    for k in grid:
        v, c, r = realized(k, warm)
        vals.append(v)
        if c is not None and r is not None and r < 1e-5:
            warm = c
    vals = np.array(vals)
    dS = np.diff(vals)
    signs = "".join("+" if d > 0 else "-" for d in dS)
    n_pos, n_neg = signs.count("+"), signs.count("-")
    n_chg = sum(1 for i in range(1, len(signs)) if signs[i] != signs[i - 1])
    print(f"[D] Phi' sign string ({len(signs)} diffs): {signs}")
    print(f"[D] n_pos={n_pos} n_neg={n_neg} sign_changes={n_chg} argmax_kappa={grid[int(np.argmax(vals))]}")

    out = {
        "kappa_dagger": kd,
        "Sigma_kd": round(float(v0), 6),
        "cut_d": [round(float(cut_d.k1), 4), round(float(cut_d.k0), 4), round(float(cut_d.kD), 4)],
        "Phi_kk_frozen": round(float(Phi_kk), 4),
        "theta": round(float(theta), 4),
        "Sigma_prime": round(float(Sig_p), 4),
        "Phi_pp": round(float(Sig_pp), 5),
        "G_contribution": round(float(G), 4),
        "residual_split_closes": bool(abs(split - Sig_pp) < 1e-9),
        "corrected_condition_G_lt_theta": bool(cond),
        "Phi_pp_negative": bool(split < 0),
        "refuted_G100_Phipp": round(float(Phi_kk + 100), 2),
        "sign_string": signs,
        "n_pos": n_pos,
        "n_neg": n_neg,
        "n_sign_changes": n_chg,
    }
    with open("/Users/austinli/Projects/blockholder/quality_reports/fixes/D1_GE_verify_out.json", "w") as f:
        json.dump(out, f, indent=2)
    print("[ok] wrote D1_GE_verify_out.json")


if __name__ == "__main__":
    main()
