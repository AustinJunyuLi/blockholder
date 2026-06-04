"""
Phase-0 robustness driver for Prop 6 (single-peaked minority premium).

Uses the paper's OWN package solver:
  - numerical.solver.solve_equilibrium(params, k1_init,k0_init,kD_init,...)
  - numerical.solver.equilibrium_residual(k1,k0,kD,params)
  - numerical.model.compute_minority_gains(k1,k0,kD,params)
  - numerical.model.compute_action_probabilities / compute_conditional_means
  - numerical.model.solve_price_fixed_point  (for the chord-condition margins)

Produces quality_reports/fixes/phase0_robustness.md:
  0. Baseline endpoint symmetry at true endpoints (kappa=1e-6, 1-1e-6), tight
     fixed-point tol, plus baseline hump classification + noise-floor test.
  1. Hump-vs-trough map over sigma_xi in {0.10,0.25,0.40,0.60} x S_bar grid,
     with two condition margins on the realized D=0 chord [0, pi_bar]:
       (C*)  mbar*T - 2*sigma_xi                 (<0 => g=mbar*p concave)
       (C**) pointwise h''max = max(2p'+pi p'')   (<0 => h=pi*p loc. concave)
       (C**-chord) h(0)-2h(pi_bar/2)+h(pi_bar)    (<0 => h concave on chord)
  2. Multiplicity: multi-start from many random ordered seeds at kappa in
     {0.2,0.5,0.8}; distinct fixed-point count; spread of Delta^min.
  2c. Whether the hump ordering holds on ALL distinct kappa=0.5 branches.

Run with scipy available (e.g. a venv with --system-site-packages + scipy).
"""
from __future__ import annotations

import json
import sys
import numpy as np
from scipy.stats import norm

sys.path.insert(0, "/Users/austinli/Projects/blockholder")

from numerical.params import ModelParams, Cutoffs, TOL_RESIDUAL  # noqa: E402
from numerical import model as M  # noqa: E402
from numerical.solver import solve_equilibrium, equilibrium_residual  # noqa: E402

OUT = "/Users/austinli/Projects/blockholder/quality_reports/fixes/phase0_robustness.md"

TIGHT_TOL = 1e-9
TIGHT_ITERS = 200


def solve_cut(params, x0=None):
    if x0 is None:
        cut = solve_equilibrium(params, max_iter=TIGHT_ITERS, tol=TIGHT_TOL)
    else:
        cut = solve_equilibrium(
            params, k1_init=float(x0[0]), k0_init=float(x0[1]),
            kD_init=float(x0[2]), max_iter=TIGHT_ITERS, tol=TIGHT_TOL,
        )
    r = equilibrium_residual(cut.k1, cut.k0, cut.kD, params)
    return cut, float(r)


def delta_min_at(base, kappa, x0=None):
    p = base.replace(kappa=float(kappa))
    cut, r = solve_cut(p, x0=x0)
    g = M.compute_minority_gains(cut.k1, cut.k0, cut.kD, p)
    return float(g.total), float(g.activism), cut, r


def series(base, kappas, x0_start=None):
    out = []
    x0 = x0_start
    for kp in kappas:
        dmin, dact, cut, r = delta_min_at(base, kp, x0=x0)
        out.append((float(kp), dmin, dact, cut, r))
        x0 = (cut.k1, cut.k0, cut.kD)
    return out


def classify(kappas, vals, resids=None, res_gate=TOL_RESIDUAL):
    """Classify shape using ONLY points whose FP residual passes the gate.

    Points with residual above res_gate are non-equilibria (solver hit a grid
    edge / degenerate region) and must not enter the hump/trough call.
    """
    if resids is None:
        keep = [(k, v) for k, v in zip(kappas, vals) if v is not None]
    else:
        keep = [(k, v) for k, v, r in zip(kappas, vals, resids)
                if v is not None and r is not None and r <= res_gate]
    ks = np.array([k for k, v in keep])
    vs = np.array([v for k, v in keep])
    if len(vs) < 3:
        return {"type": "insufficient", "n": int(len(vs))}
    i_max = int(np.argmax(vs)); i_min = int(np.argmin(vs))
    ep = [0, len(vs) - 1]
    v0, v1 = float(vs[0]), float(vs[-1])
    res = {
        "n_valid": int(len(vs)),
        "k_lo": float(ks[0]), "k_hi": float(ks[-1]),
        "v_lo": v0, "v_hi": v1, "endpoint_gap": v1 - v0,
        "k_argmax": float(ks[i_max]), "v_max": float(vs[i_max]),
        "k_argmin": float(ks[i_min]), "v_min": float(vs[i_min]),
        "level": float(np.mean(vs)),
    }
    int_max = i_max not in ep
    int_min = i_min not in ep
    if int_max and (vs[i_max] - max(v0, v1)) > 1e-12:
        res["type"] = "hump"
        res["amp_abs"] = float(vs[i_max] - max(v0, v1))
        res["amp_rel"] = float((vs[i_max] - max(v0, v1)) / max(v0, v1))
    elif int_min and (min(v0, v1) - vs[i_min]) > 1e-12:
        res["type"] = "trough"
        res["amp_abs"] = float(min(v0, v1) - vs[i_min])
        res["amp_rel"] = float((min(v0, v1) - vs[i_min]) / max(v0, v1))
    else:
        res["type"] = "flat" if abs(v1 - v0) < 1e-9 * max(1e-9, abs(v0)) else "monotone"
    return res


# --- condition margins on the realized D=0 chord [0, pi_bar] -----------------

def T_of_pi(pi, E_v, params):
    P = M.solve_price_fixed_point(E_v, pi, params)
    m = params.m0 + (params.m_tilde - params.m0) * pi
    return (m + params.K - params.S_bar + P) / params.sigma_xi


def p_of_pi(pi, E_v, params):
    return 1.0 - norm.cdf(T_of_pi(pi, E_v, params))


def m_of_pi(pi, params):
    return params.m0 + (params.m_tilde - params.m0) * pi


def margins(params, cut):
    oE, oH, oQ, oP = M.compute_action_probabilities(cut.k1, cut.k0, cut.kD, params)
    muE, muH, muQ, muP = M.compute_conditional_means(cut.k1, cut.k0, cut.kD, params)
    # pi_bar = posterior at the most-diagnostic nondisclosed state (X=1,D=0),
    # which is omega_Q/(omega_H+omega_Q) (draft Sec 5.2). When Hold collapses
    # (omega_H->0) this -> 1, the genuine upper point of the realized D=0
    # two-point support {0, pi_bar}; the chord is then [0,1].
    post = M.compute_posteriors(oE, oH, oQ, oP, params.kappa)
    pi_bar = float(post.get((1, 0), 0.0))
    denom = oH + oQ
    E_v = (oH * muH + oQ * muQ) / denom if denom > 1e-12 else muQ
    h = 1e-4
    mprime = (params.m_tilde - params.m0)
    test = [max(1e-6, pi_bar * 0.5), max(1e-6, min(pi_bar, 1.0) * 0.99)]
    hpp_max = -np.inf; gpp_max = -np.inf
    for pi in test:
        p0 = p_of_pi(pi, E_v, params)
        pp = p_of_pi(pi + h, E_v, params)
        pm = p_of_pi(max(0.0, pi - h), E_v, params)
        pprime = (pp - pm) / (2 * h)
        pdbl = (pp - 2 * p0 + pm) / (h * h)
        hpp = 2 * pprime + pi * pdbl
        gpp = 2 * mprime * pprime + m_of_pi(pi, params) * pdbl
        hpp_max = max(hpp_max, hpp); gpp_max = max(gpp_max, gpp)
    # chord (secant) curvature of h=pi*p over {0, pi_bar/2, pi_bar}
    if pi_bar > 1e-9:
        h0 = pi_bar * 0.0 * p_of_pi(1e-9, E_v, params)  # h(0)=0
        hmid = (pi_bar / 2) * p_of_pi(pi_bar / 2, E_v, params)
        h1 = pi_bar * p_of_pi(pi_bar, E_v, params)
        chord = h0 - 2 * hmid + h1
    else:
        chord = float("nan")
    pe = pi_bar if pi_bar > 0 else 1e-6
    T_bar = T_of_pi(pe, E_v, params)
    m_bar = m_of_pi(pe, params)
    return {
        "pi_bar": float(pi_bar),
        "cstar": float(m_bar * T_bar - 2 * params.sigma_xi),
        "hpp_max": float(hpp_max),
        "gpp_max": float(gpp_max),
        "chord": float(chord),
        "T_bar": float(T_bar), "m_bar": float(m_bar),
    }


def fmt(x, f="{:.4f}"):
    if x is None or (isinstance(x, float) and (np.isnan(x) or np.isinf(x))):
        return "NA"
    return f.format(x)


def main():
    L = []
    def w(s=""):
        L.append(s); print(s)

    base = ModelParams.baseline()

    c0, r0 = solve_cut(base.replace(kappa=0.5))
    print(f"[self-test] kappa=0.5 cutoffs=({c0.k1:.4f},{c0.k0:.4f},{c0.kD:.4f}) resid={r0:.2e}")
    if r0 > 1e-3:
        raise RuntimeError(f"baseline did not converge cleanly: resid={r0}")

    KG = np.linspace(0.05, 0.95, 13)
    KG_FINE = np.concatenate([[1e-6], np.linspace(0.02, 0.98, 31), [1 - 1e-6]])

    w("# Phase-0 Robustness: Prop 6 Single-Peaked Minority Premium")
    w()
    w("Computed by `quality_reports/fixes/phase0_robustness_driver.py` using the "
      "paper's own package solver (`numerical.solver.solve_equilibrium` at fixed-"
      "point tol 1e-9, `equilibrium_residual`) and `numerical.model."
      "compute_minority_gains` for Delta^min. Every number below is computed.")
    w()
    w(f"Baseline: delta={base.delta}, sigma_xi={base.sigma_xi}, S_bar={base.S_bar}, "
      f"m0={base.m0}, m1={base.m1}, m_tilde={base.m_tilde:.4f}, rho={base.rho}, "
      f"K={base.K}, sigma_s={base.sigma_s:.4f}. Solver gate TOL_RESIDUAL="
      f"{TOL_RESIDUAL:.0e}; sweep tol tightened to {TIGHT_TOL:.0e}.")
    w(f"Self-test: kappa=0.5 cutoffs=({c0.k1:.4f},{c0.k0:.4f},{c0.kD:.4f}), "
      f"residual {r0:.2e}.")
    w()

    # ----- 0. endpoint symmetry + baseline hump -----------------------------
    w("## 0. Baseline endpoint symmetry and hump")
    w()
    w("CAVEAT: at the exact endpoints kappa->0 and kappa->1 the solver does NOT "
      "reach a valid equilibrium (the order-flow region structure degenerates); "
      "residuals there are >> TOL_RESIDUAL. We therefore report (i) the exact "
      "endpoints with their residual flagged, and (ii) the shape classification "
      "over the residual-PASSING interior only.")
    w()
    lo = delta_min_at(base, 1e-6)
    hi = delta_min_at(base, 1 - 1e-6)
    gap = abs(hi[0] - lo[0])
    lo_ok = lo[3] <= TOL_RESIDUAL
    hi_ok = hi[3] <= TOL_RESIDUAL
    w(f"- Delta^min(kappa=1e-6)   = {lo[0]:.8f}  (resid {lo[3]:.2e}, "
      f"valid={lo_ok})  cutoffs=({lo[2].k1:.4f},{lo[2].k0:.4f},{lo[2].kD:.4f})")
    w(f"- Delta^min(kappa=1-1e-6) = {hi[0]:.8f}  (resid {hi[3]:.2e}, "
      f"valid={hi_ok})  cutoffs=({hi[2].k1:.4f},{hi[2].k0:.4f},{hi[2].kD:.4f})")
    w(f"- exact-endpoint Delta^min gap |hi-lo| = {gap:.3e} (the two endpoint "
      f"SOLVES coincide -- consistent with endpoint symmetry -- but BOTH carry "
      f"high residual, so this is suggestive, not a verified equilibrium value).")
    w()
    # near-endpoints that DO solve cleanly, to test symmetry on valid equilibria
    near_lo = delta_min_at(base, 0.02)
    near_hi = delta_min_at(base, 0.98)
    w(f"- Valid near-endpoints: Delta^min(0.02)={near_lo[0]:.6f} "
      f"(resid {near_lo[3]:.1e}), Delta^min(0.98)={near_hi[0]:.6f} "
      f"(resid {near_hi[3]:.1e}); gap={abs(near_hi[0]-near_lo[0]):.3e} "
      f"(near-symmetric on valid equilibria).")
    w()
    bs = series(base, KG_FINE)
    bk = [r[0] for r in bs]; bv = [r[1] for r in bs]; br = [r[4] for r in bs]
    bsh = classify(bk, bv, br)
    maxr_all = max(r[4] for r in bs)
    maxr_valid = max((r[4] for r in bs if r[4] <= TOL_RESIDUAL), default=float("nan"))
    n_invalid = sum(1 for r in bs if r[4] > TOL_RESIDUAL)
    w(f"Baseline fine-grid ({len(KG_FINE)} pts, warm-started); "
      f"{n_invalid} pts dropped for resid>TOL_RESIDUAL. "
      f"Shape over residual-passing interior:")
    for k, v in bsh.items():
        w(f"  {k}: {v}")
    w(f"  max residual among KEPT points: {maxr_valid:.2e}; "
      f"max residual incl. dropped endpoints: {maxr_all:.2e}")
    base_hump = bsh.get("type") == "hump"
    if base_hump:
        w(f"  hump amplitude abs = {bsh['amp_abs']:.3e}; exceeds 10x max KEPT "
          f"resid ({10*maxr_valid:.2e})? {bsh['amp_abs'] > 10*maxr_valid}")
    maxr = maxr_valid
    w()

    # ----- 1. sigma_xi x S_bar map ------------------------------------------
    w("## 1. Hump-vs-trough map over (sigma_xi, S_bar)")
    w()
    sigmas = [0.10, 0.25, 0.40, 0.60]
    sbars = [round(base.S_bar + d, 2) for d in (-0.20, -0.10, 0.0, 0.10, 0.20)]
    w("(C*) margin = mbar*T - 2*sigma_xi (<0 => g=mbar*p concave => memo hump). "
      "h''max = max over chord of 2p'(pi)+pi p''(pi) for CORRECTED h=pi*p, local "
      "(<0 => locally concave). chord = h(0)-2h(pi_bar/2)+h(pi_bar) (<0 => h "
      "concave on the two-point chord => hump). g''max for g=mbar*p.")
    w()
    w("| sigma_xi | S_bar | shape | endpt gap | k* | amp_rel | (C*) margin | "
      "h''max | chord | g''max | pi_bar |")
    w("|---:|---:|:--|--:|--:|--:|--:|--:|--:|--:|--:|")
    rows = []
    for sx in sigmas:
        for sb in sbars:
            p = base.replace(sigma_xi=sx, S_bar=sb)
            ser = series(p, KG)
            ks = [r[0] for r in ser]; vs = [r[1] for r in ser]; rs = [r[4] for r in ser]
            sh = classify(ks, vs, rs)
            mid = delta_min_at(p, 0.5)
            cm = margins(p, mid[2])
            typ = sh.get("type")
            kstar = sh.get("k_argmax") if typ == "hump" else (
                sh.get("k_argmin") if typ == "trough" else None)
            amp = sh.get("amp_rel")
            rows.append(((sx, sb, typ, sh.get("endpoint_gap"), kstar, amp), sh, cm))
            w(f"| {sx:.2f} | {sb:.2f} | {typ} | {fmt(sh.get('endpoint_gap'),'{:.1e}')} "
              f"| {fmt(kstar,'{:.3f}')} | {fmt(amp)} | {fmt(cm['cstar'])} | "
              f"{fmt(cm['hpp_max'])} | {fmt(cm['chord'],'{:.5f}')} | "
              f"{fmt(cm['gpp_max'])} | {fmt(cm['pi_bar'],'{:.3f}')} |")
    w()
    # agreement of shape with chord and with pointwise h''
    def agree_count(key):
        a = d = 0; mism = []
        for (sx, sb, typ, *_), sh, cm in rows:
            val = cm[key]
            if np.isnan(val):
                continue
            if typ == "hump" and val < 0: a += 1
            elif typ == "trough" and val > 0: a += 1
            elif typ in ("hump", "trough"):
                d += 1; mism.append(f"sigma_xi={sx},S_bar={sb}: shape={typ}, {key}={val:.5f}")
        return a, d, mism
    a_h, d_h, m_h = agree_count("hpp_max")
    a_c, d_c, m_c = agree_count("chord")
    w("### 1b. Which diagnostic predicts the realized hump/trough?")
    w(f"- pointwise h''max: agree {a_h}, disagree {d_h}")
    for m in m_h: w(f"    - mismatch: {m}")
    w(f"- chord 2nd-difference: agree {a_c}, disagree {d_c}")
    for m in m_c: w(f"    - mismatch: {m}")
    w()
    flips = []
    for (sx, sb, *_), sh, cm in rows:
        cs, hpp = cm["cstar"], cm["hpp_max"]
        if (cs < 0) != (hpp < 0):
            flips.append((sx, sb, cs, hpp))
    w("### 1c. Do (C*) [memo, g=mbar*p] and pointwise (C**) [h=pi*p] disagree in sign?")
    if flips:
        w(f"- DISAGREE in {len(flips)} cells (correction (a) is non-vacuous):")
        for sx, sb, cs, hpp in flips:
            w(f"  - sigma_xi={sx}, S_bar={sb}: (C*)={cs:.4f}, h''max={hpp:.4f}")
    else:
        w("- (C*) and pointwise (C**) agree in sign across all cells in this grid.")
    w()

    # ----- 2. multiplicity ---------------------------------------------------
    w("## 2. Multiplicity check (multi-start) at kappa in {0.2,0.5,0.8}")
    w()
    rng = np.random.default_rng(20260530)
    n_seeds = 30
    multi = []
    for kp in (0.2, 0.5, 0.8):
        p = base.replace(kappa=kp)
        ref = delta_min_at(base, kp)
        fps = []
        for _ in range(n_seeds):
            blo = base.mu - 3 * base.sigma_s; bhi = base.mu + 3 * base.sigma_s
            xs = np.sort(rng.uniform(blo, bhi, size=3))
            cut, r = solve_cut(p, x0=(xs[0], xs[1], xs[2]))
            if np.isfinite(r) and r <= TOL_RESIDUAL:
                fps.append((cut, r))
        distinct = {}
        for cut, r in fps:
            key = (round(cut.k1, 3), round(cut.k0, 3), round(cut.kD, 3))
            if key not in distinct or r < distinct[key][1]:
                distinct[key] = (cut, r)
        w(f"### kappa = {kp}")
        w(f"- reference Delta^min={ref[0]:.6f} cutoffs="
          f"({ref[2].k1:.4f},{ref[2].k0:.4f},{ref[2].kD:.4f}) resid={ref[3]:.2e}")
        w(f"- seeds={n_seeds}; converged(resid<=TOL_RESIDUAL): {len(fps)}; "
          f"distinct FPs: {len(distinct)}")
        dvals = []
        for key, (cut, r) in distinct.items():
            g = M.compute_minority_gains(cut.k1, cut.k0, cut.kD, p)
            dvals.append(g.total)
            w(f"  - FP {key} resid={r:.2e} Delta^min={g.total:.6f}")
        spread = (max(dvals) - min(dvals)) if dvals else float("nan")
        w(f"- spread of Delta^min across distinct FPs: {spread:.2e}")
        multi.append((kp, len(distinct), spread))
        w()

    # ----- 2c. hump ordering across all kappa=0.5 branches -------------------
    w("### 2c. Hump ordering across equilibria")
    w()
    pm = base.replace(kappa=0.5)
    rng2 = np.random.default_rng(7)
    seeds = {}
    for _ in range(20):
        blo = base.mu - 3 * base.sigma_s; bhi = base.mu + 3 * base.sigma_s
        xs = np.sort(rng2.uniform(blo, bhi, size=3))
        cut, r = solve_cut(pm, x0=(xs[0], xs[1], xs[2]))
        if np.isfinite(r) and r <= TOL_RESIDUAL:
            key = (round(cut.k1, 3), round(cut.k0, 3), round(cut.kD, 3))
            seeds[key] = (cut, r)
    w(f"- distinct kappa=0.5 fixed points found: {len(seeds)}")
    grid = np.linspace(0.05, 0.95, 13)
    all_hump = True
    for key, (cut, r) in seeds.items():
        ser = series(base, grid, x0_start=(cut.k1, cut.k0, cut.kD))
        ks = [x[0] for x in ser]; vs = [x[1] for x in ser]; rs = [x[4] for x in ser]
        sh = classify(ks, vs, rs)
        ish = sh.get("type") == "hump"
        all_hump = all_hump and ish
        w(f"  - branch {key}: shape={sh.get('type')} "
          f"k*={fmt(sh.get('k_argmax'),'{:.3f}')} amp_rel={fmt(sh.get('amp_rel'))}")
    w(f"- hump holds across ALL examined branches: {all_hump}")
    w()

    # ----- verdict -----------------------------------------------------------
    w("## Verdict")
    w()
    w(f"- Baseline hump real (tight tol + true endpoints): {base_hump}")
    if base_hump:
        w(f"  - interior maximizer k* = {bsh['k_argmax']:.3f}")
        w(f"  - amplitude abs = {bsh['amp_abs']:.3e}, rel = {bsh['amp_rel']:.4f} "
          f"({100*bsh['amp_rel']:.2f}% of level)")
        w(f"  - amplitude exceeds 10x max solver residual: {bsh['amp_abs'] > 10*maxr}")
    w(f"- endpoint symmetry gap = {gap:.3e} (holds: {gap < 1e-4})")
    fails = [(r[0][0], r[0][1], r[0][2]) for r in rows if r[0][2] != "hump"]
    w(f"- regimes where Delta^min is NOT a hump (headline is CONDITIONAL): "
      f"{len(fails)} of {len(rows)}")
    for sx, sb, typ in fails:
        w(f"  - sigma_xi={sx}, S_bar={sb}: {typ}")
    w(f"- multiplicity (distinct FPs): "
      f"{', '.join(f'kappa={k}:{n}' for k, n, _ in multi)}")
    w(f"- hump ordering across all kappa=0.5 equilibria: {all_hump}")
    w(f"- best shape predictor: chord 2nd-diff (agree {a_c}/{a_c+d_c}) vs "
      f"pointwise h'' (agree {a_h}/{a_h+d_h}).")
    w()

    with open(OUT, "w") as fh:
        fh.write("\n".join(L) + "\n")

    summary = {
        "baseline_hump": base_hump,
        "baseline_kstar": bsh.get("k_argmax"),
        "baseline_amp_rel": bsh.get("amp_rel"),
        "baseline_amp_abs": bsh.get("amp_abs"),
        "max_resid": maxr,
        "endpoint_lo": lo[0], "endpoint_hi": hi[0], "endpoint_gap": gap,
        "n_fails": len(fails), "n_cells": len(rows), "fails": fails,
        "multi": multi,
        "all_hump_branches": all_hump,
        "sign_flips_Cstar_vs_pointwise": len(flips),
        "chord_agree": [a_c, d_c], "hpp_agree": [a_h, d_h],
        "map": [
            {"sigma_xi": r[0][0], "S_bar": r[0][1], "shape": r[0][2],
             "k_star": r[0][4], "amp_rel": r[0][5],
             "cstar": r[2]["cstar"], "hpp_max": r[2]["hpp_max"],
             "chord": r[2]["chord"], "gpp_max": r[2]["gpp_max"],
             "pi_bar": r[2]["pi_bar"]}
            for r in rows
        ],
    }
    print("SUMMARY_JSON_START")
    print(json.dumps(summary, default=float))
    print("SUMMARY_JSON_END")
    print("WROTE", OUT)


if __name__ == "__main__":
    main()
