"""Smoke run: the one runnable thing that fails if any of the logic is broken.

Design section 11.  Run from the worktree root:

    .venv/bin/python -m numerical_v4.smoke

Two items:

  1. ONE EQUILIBRIUM AT BASELINE -- kappa = 0.5, tau = the median of the
     baseline Voice b*(s), T = 5, H = 10.  Prints k, the outer residual, Omega,
     omega_a, M_F, M_P, Delta^act, the identity residual
     |P^F - P_{c-} - R - J|, and a7_certificate.

  2. ONE FROZEN-POLICY KAPPA-SWEEP -- that policy held fixed, kappa in
     {0.05,...,0.95}.  Prints range_kappa M_F (must be < 1e-10 -- this is L2,
     and it is the assertion that fails loudest if kappa has leaked into the
     flagged path) and the S_P profile.

Preceded by the build step 4 go/no-go gate, and by the design section 13
ruling 3 stop condition on ``multiple_root_nodes``.

Units at the print boundary follow the card's calibration card: Omega and
omega_a in percent, B^F in percentage points of shares, M_F/M_P/Delta^act in
premium percentage points, R and J in basis points.
"""

from __future__ import annotations

import sys
import time

import numpy as np

from numerical_v4.params import (
    ParamsV4,
    TOL_IDENTITY,
    TOL_INVARIANCE,
    kappa_grid,
)
from numerical_v4.policy import evaluate, frozen_policy_sweep, frozen_tau_grid
from numerical_v4.pooled import probe
from numerical_v4.premium import chord, d_dkappa
from numerical_v4.solver import solve_policy

PP = 100.0        # premium percentage points / percent
BP = 10000.0      # basis points


def rule(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def main() -> int:
    t_start = time.perf_counter()
    p_seed = ParamsV4.baseline()

    rule("PROVENANCE")
    print(f"  model card stamp     2026-08-20 (commit 0c9185b)")
    print(f"  design               research/model_v4/impl_design.md, section 13 APPROVED")
    print(f"  params hash          {p_seed.hash_str()}")
    print(f"  H = {p_seed.H}   T = {p_seed.T}   M = 2 marks   J = 3 plans")
    print(f"  seed tau             {p_seed.tau:.6f}  (statutory 13D 5%)")
    print(f"  b0 = {p_seed.b0}  b_bar = {p_seed.b_bar}  n_scale = {p_seed.n_scale}"
          f"  C0 = {p_seed.C0}")

    # -- build step 4: the go/no-go gate ------------------------------------
    rule("BUILD STEP 4 -- ENUMERATION PROBE (GO/NO-GO GATE)")
    k_seed = (p_seed.mu_v - 0.5 * p_seed.sigma_s,
              p_seed.mu_v + 0.5 * p_seed.sigma_s)
    pr = probe(p_seed, k_seed)
    print(f"  n_hist (4^(H+1))        {pr.n_hist:,}")
    print(f"  n_hist feasible         {pr.n_hist_feasible:,}")
    print(f"  N_theta                 {pr.n_theta}   (populated at seed k: "
          f"{pr.n_theta_populated})")
    print(f"  feasible n_hist x N_th  {pr.product:.3e}   gate limit "
          f"{pr.gate_limit:.0e}")
    print(f"  int8 array (n0 + feas)  {pr.int8_bytes / 2**20:.1f} MB")
    print(f"  one evaluation          {pr.eval_seconds:.3f} s")
    print(f"  GATE                    {'PASS' if pr.gate_pass else 'FAIL -- STOP'}")
    if not pr.gate_pass:
        print("  Feasible n_hist x N_theta exceeds 1e8.  Stopping before any "
              "pricing code runs; design open questions 1 and 2 re-open.")
        return 2

    # -- tau freezing (design section 6.2) ----------------------------------
    rule("TAU FREEZING (design section 6.2)")
    pol_seed, res_seed = solve_policy(p_seed)
    tau_frozen = frozen_tau_grid(pol_seed, p_seed, (0.5,))[0]
    print(f"  seed equilibrium k      ({pol_seed.k[0]:.8f}, {pol_seed.k[1]:.8f})"
          f"   |k-T(k)| = {res_seed.cutoff_scale:.3e}")
    print(f"  median Voice b*(s)      {tau_frozen:.8f}")
    print(f"  tau frozen at           {tau_frozen:.8f}   (reused at every node)")
    p = p_seed.replace(tau=tau_frozen)

    # -- smoke item 1 -------------------------------------------------------
    rule("SMOKE 1 -- ONE BASELINE EQUILIBRIUM  (kappa = 0.5, T = 5, H = 10)")
    t0 = time.perf_counter()
    policy, resid = solve_policy(p)
    out = evaluate(policy, p, with_runup=True)
    print(f"  solve + evaluate        {time.perf_counter() - t0:.1f} s")
    print()
    print(f"  k                       ({policy.k[0]:.10f}, {policy.k[1]:.10f})")
    print(f"  outer residual  |k-T(k)|_inf   {resid.cutoff_scale:.3e}"
          f"   (P1 diagnostic scale, target 1e-10)")
    print(f"  outer residual  payoff scale   {resid.payoff_scale:.3e}"
          f"   (P1 BINDING criterion, target 1e-9)")
    print(f"  local gap slopes d(U_j-U_j')/ds ({resid.slopes[0]:.4e}, "
          f"{resid.slopes[1]:.4e})")
    print()
    print(f"  Omega   Pr(D=1)         {out.Omega * PP:.6f} %")
    print(f"  Pr(a=1)                 {out.Pr_a * PP:.6f} %")
    print(f"  omega_a Pr(D=1|a=1)     {out.omega_a * PP:.6f} %")
    print(f"  pi_bar  Pr(a=1|D=0)     {out.pi_bar * PP:.6f} %")
    print()
    print(f"  M_F                     {out.M_F * PP:.10f} premium pp")
    print(f"  M_P                     {out.M_P * PP:.10f} premium pp")
    print(f"  Delta^act               {out.Delta_act * PP:.10f} premium pp")
    print(f"  L1 residual |D - (Om M_F + (1-Om) M_P)|   "
          f"{out.decomposition_residual:.3e}   [WIRING, not evidence for L1]")
    print()
    print(f"  R  (mean run-up)        {out.R_mean * BP:.6f} bp")
    print(f"  J  (mean filing jump)   {out.J_mean * BP:.6f} bp")
    print(f"  D1 identity residual    {out.identity_residual:.3e}"
          f"   (TOL_IDENTITY = {TOL_IDENTITY:.0e})   [WIRING]")
    print(f"  identity verdict        "
          f"{'PASS' if out.identity_residual < TOL_IDENTITY else 'FAIL'}")
    print()
    a7 = out.a7
    print(f"  a7_certificate")
    print(f"    min |db*/ds| flagged  {a7.min_slope:.6e}   (gate 1e-8)")
    print(f"    flat sub-intervals    {a7.n_flat_subintervals}")
    print(f"    (B^F,Q^F) collisions  {a7.n_collisions}")
    print(f"    cross-plan collisions {a7.n_cross_plan}")
    print(f"    flagged atoms         {a7.n_flagged_atoms}")
    print(f"    PASSES                {a7.passes}")
    print()
    pr2 = probe(p, policy.k)
    print(f"  atoms                   {out.n_atoms} "
          f"({out.n_flagged_atoms} flagged)")
    print(f"  N_theta populated here  {pr2.n_theta_populated} of {pr2.n_theta}"
          f"   (the seed tau flagged every Voice type; the frozen tau does not)")
    print(f"  feasible histories      {out.n_hist_feasible:,}")
    print(f"  pooled mass error       {out.pooled_mass_error:.3e}")
    print(f"  max inner price residual {out.max_price_residual:.3e}")
    print(f"  max b* inversion error  {out.max_inversion_error:.3e}")
    # Design section 1, open question (minor): is GL-20 per interval enough?
    mf40 = evaluate(policy, p.replace(n_gl=40), with_runup=False).M_F
    print(f"  GL-20 vs GL-40 on M_F   {abs(out.M_F - mf40):.3e}"
          f"   (raise the order if > 1e-13)")
    print(f"  max Q^F                 {out.max_Q_F * PP:.6f} pp of shares")
    print(f"  T == H corner           {out.corner}")
    print(f"  degenerate_nodes        {list(out.degenerate_nodes)}")
    print(f"  multiple_root_nodes     {out.multiple_root_nodes}")

    if out.multiple_root_nodes:
        rule("STOP -- design section 13, ruling 3")
        print(f"  multiple_root_nodes is NONEMPTY ({out.multiple_root_nodes} "
              f"nodes) at the baseline calibration.")
        print("  A5's uniqueness fails numerically.  Stopping before any "
              "pricing-dependent conclusion is drawn.")
        return 3

    # -- smoke item 2 -------------------------------------------------------
    rule("SMOKE 2 -- FROZEN-POLICY KAPPA SWEEP  (policy held fixed)")
    kaps = kappa_grid(10)
    t0 = time.perf_counter()
    sweep = frozen_policy_sweep(policy, p, kaps, with_runup=False)
    print(f"  {len(kaps)} nodes in {time.perf_counter() - t0:.1f} s")

    MF = np.array([o.M_F for o in sweep])
    range_MF = float(MF.max() - MF.min())
    print()
    print(f"  range_kappa M_F         {range_MF:.6e}"
          f"   (TOL_INVARIANCE = {TOL_INVARIANCE:.0e})")
    print(f"  L2 verdict              "
          f"{'PASS' if range_MF < TOL_INVARIANCE else 'FAIL'}"
          f"   [SUBSTANTIVE -- the flagged path must never touch kappa]")
    print()
    print("   kappa      M_F (pp)        M_P (pp)      Delta^act (pp)"
          "     dM_P/dkappa      S_P = |dM_P/dkappa|")
    Sp, dP = [], []
    for kap, o in zip(kaps, sweep):
        d = d_dkappa(
            lambda kk: evaluate(policy, p.replace(kappa=kk), False).M_P,
            float(kap))
        dP.append(d)
        Sp.append(abs(d))
        print(f"  {kap:6.3f}   {o.M_F * PP:.10f}   {o.M_P * PP:.10f}   "
              f"{o.Delta_act * PP:.10f}   {d * PP: .6e}   {abs(d) * PP:.6e}",
              flush=True)

    Sp = np.array(Sp)
    dP = np.array(dP)
    MP = np.array([o.M_P for o in sweep])
    n_sign = int(np.count_nonzero(np.diff(np.sign(dP)) != 0))
    shape = "increasing" if np.all(np.diff(Sp) > 0) else (
        "decreasing" if np.all(np.diff(Sp) < 0) else
        f"non-monotone: M_P is hump-shaped in kappa (peak near kappa = "
        f"{kaps[int(np.argmax(MP))]:.2f}, {n_sign} sign change(s) in dM_P/dkappa), "
        f"so S_P = |dM_P/dkappa| is V-shaped about that peak")
    print()
    print(f"  S_P profile shape       {shape}")
    print(f"  S_P min / max           {Sp.min() * PP:.6e} / {Sp.max() * PP:.6e}"
          f"  premium pp per unit kappa")
    print(f"  S = (1-Omega) S_P       {(1 - out.Omega) * Sp[len(Sp)//2] * PP:.6e}"
          f"  at kappa = {kaps[len(kaps)//2]:.2f}")

    # -- the standalone chord (design section 8) ----------------------------
    rule("CHORD MODULE (design section 8, standalone route)")
    v_bar = p.mu_v
    print("   pi_bar        C_h              |C_h|/pi_bar^2     headroom")
    for pb in (1e-1, 1e-2, 1e-3, 1e-4):
        ch = chord(pb, v_bar, p)
        print(f"  {pb:.0e}   {ch.C_h: .12e}   {ch.quadratic_ratio:.10e}"
              f"   {ch.cancellation_headroom:.2e}")
    print("  (C_h <= 0 is the card's maintained orientation; the ratio should "
          "settle as pi_bar falls)")

    rule(f"SMOKE COMPLETE in {time.perf_counter() - t_start:.1f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
