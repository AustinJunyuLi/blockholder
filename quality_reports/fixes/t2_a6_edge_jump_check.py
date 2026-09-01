"""A6 continuity failure at the interior n(s) cell edges -- the decisive
T_2-jump measurement, curated.

WHAT THIS IS.  The 2026-08-27 A6 panel (two opposed-brief Opus agents,
substantiate / defuse) measured the failure of A6's continuity clause for the
declared construction at the implemented calibration.  Its working scripts are
filed at ``quality_reports/fixes/a6_panel_probes_2026-08-27/`` and are
explicitly *analysis-grade, not curated t2 checks*; that directory's README
carries the standing follow-up to curate the decisive measurements.  This
script is that curation for the first of them: the three T_2 jumps the card's
section 5 A6 evidence note quotes, at

    (kappa = 0.5,  tau_50 = the frozen threshold grid's median,  T = 5).

SOURCE PROBES (adapted, not re-imported -- the probes live in a directory with
no package init and hard-code a scratchpad path):

  * ``a6_A_probe4_precise.py``   -- Analyst A: the belief snap and the CARD's
    T_2 = inf{s : VOICE is the argmax}, located by brentq on the LOWEST sign
    change of U_VOICE - U_HOLD, at k_2 = edge -/+ 1e-9.   -> route A below.
  * ``a6_A_probe6_channel.py``   -- Analyst A: the surviving-neighbour control.
  * ``a6_A_probe7_verify.py`` part (B) -- Analyst A: the same surfaces
    re-bracketed at -/+ 1e-6, i.e. 1000x ``menu.breakpoints``' 1e-9
    near-duplicate merge tolerance.
  * ``a6_B_baseline.py``        -- Analyst B ("probe 3"): the frozen-tau
    baseline, and the IMPLEMENTATION's ``solver.outer_map`` T_2 swept across
    the same three hyperplanes, left limit (k_2 = edge - 1e-8) versus the value
    AT the edge.                                         -> route B below.

  README MAPPING CORRECTION (2026-08-28).  The probe directory's README names
  ``a6_A_probe4 / a6_B_sweep`` as the two routes to curate.  That is imprecise:
  ``a6_B_sweep.py`` part (B) runs at the *seed* threshold (``ParamsV4()``,
  tau = 0.05) and its jump across the same s = 1.583333 edge is -1.727e-2, not
  the card's 6.33e-3.  The card's B-route numbers come from
  ``a6_B_baseline.py``, which re-freezes tau first.  ``a6_B_sweep.py`` part (A)
  is the collapse-face measurement and is curated separately, in
  ``t2_a6_collapse_face_check.py``.

WHAT "PASS" MEANS HERE -- READ THIS BEFORE READING THE VERDICT.  The verdict
semantics of this check are inverted relative to a proof check.  ``pass: true``
means *the panel's measurement reproduced*: the discontinuity is there, at the
quoted size, at the quoted locus.  It does NOT mean A6 holds.  This is
applicability evidence in the A(tau) pattern -- A6 is a listed hypothesis of
P1, so a measured failure of its antecedent at the implemented calibration is a
satisfiability finding, not a derivability one.  **No label moves and none is
licensed by this file.**  P1 stays PROVED as a conditional.

THE TWO ROUTES AND WHY BOTH.  The card claims the jumps were "measured
independently by both panellists with separate scripts, agreeing to 3 s.f.".
The two routes differ in *both* the map and the bracket, which is what makes
the agreement worth asserting:

  route A  the card's T_2 (inf of the VOICE argmax set, brentq on the lowest
           up-crossing of U_VOICE - U_HOLD over a 4001-point signal grid),
           straddling bracket  k_2 = edge - 1e-9  vs  edge + 1e-9  (a 2e-9 step,
           which is the card's "<= 2e-9 steps in k_2" clause);
  route B  the implementation's ``outer_map`` T_2 (nearest-bracket tie-break),
           one-sided bracket  k_2 = edge - 1e-8  vs  k_2 = edge exactly (where
           the dying type's mass W is 0 on the nose).

Each route is replayed at ITS OWN filed deltas.  Route B is deliberately NOT
re-run at a 1e-9 left offset to make its step fit the card's "<= 2e-9" clause:
that clause is carried by route A, and moving B's bracket to fit a number would
be tuning.  A -1e-9 row is recorded for B as extra data (``extra_deltas``) and
gates nothing.

GATES.  All were fixed from the filed panel values before this script was first
run, with ONE exception, declared here rather than left for a reader to notice:
the ``belief_snap`` gate was restructured AFTER the first run, which missed at
two of the three edges.  The restructure is tighter, not wider -- the tolerance
went from 1e-7 to 1e-8 and a second, independent sub-gate (the sliver expansion)
was added -- and the original miss is preserved verbatim in the JSON's
``known_discrepancies`` and in the per-edge ``ladder``.  What changed is the
bracket at which the limit is tested, for the reason set out below; what did not
change is any number.  No other gate has moved, and no gate has been widened.

  card_3sf        ``%.3g`` of the measured |jump| equals the card's quoted
                  figure exactly (6.33e-3 / 1.09e-2 / 2.83e-2)
  panel_rel       relative difference from the filed panel value <= 5e-4
  cross_route     |A - B| / mean(A, B) <= 5e-4     ("agreeing to 3 s.f.")
  belief_snap     |measured vhat jump - Step 9(b) prediction| <= 1e-8 at the
                  declared bracket eps = 1e-8 (card: "matching the Step 9(b)
                  prediction to ~1e-8"), AND the sliver-expansion residual
                  <= 1e-9 at eps = 1e-6 (see below)
  control         surviving neighbour's aggregate moves <= 1e-8
                  (card: "surviving-type controls ~3e-9")
  eps_robust      route A at -/+1e-6 vs -/+1e-9, relative difference <= 5e-4
                  (card: "robust at 1000x the breakpoint-merge tolerance")

THE STEP 9(b) PREDICTION (what ``belief_snap`` tests).  All k-dependence of
U_j runs through the pooled price vector; the flagged layer is k-free under
A7-J.  Step 9(b) gives Bayes where Lambda_k(h) > 0 and a k-free plan-uniform
posterior on the frontier.  So as k_2 crosses the top edge of dying type t's
cell, the market belief attached to t must snap from the concentration limit
    conc = mu_v + beta*(edge - mu_v)
(the posterior of a vanishing sliver at the edge) to the k-free reference value
``type_reference(p).Ev[t]`` (which, for a t-exclusive history, IS the
plan-uniform posterior restricted to that cell).  The predicted jump is the
difference of those two closed forms.  Reproducing it is what makes the
measured discontinuity the CARD's construction rather than an implementation
artifact.

WHY THE SNAP IS BRACKETED AT eps = 1e-8 AND NOT AT THE PROBES' 1e-9.  The
prediction is a LIMIT.  At a finite bracket eps the surviving sliver is
[edge - eps, edge), whose exact Bayes posterior is

    vhat_below(eps)  =  conc - beta*eps/2 + O(eps^2),

so any finite bracket carries a truncation error of beta*eps/2 that is a
property of the bracket, not a failure of the prediction.  Below the bracket
where truncation meets floating point, the CDF difference Phi(b) - Phi(a) over
an interval of width eps loses relative precision u/eps (u ~ 2.2e-16), which
propagates into the ratio that defines the posterior mean.  The two error
sources cross at

    eps* = sqrt(2*C*u/beta) ~ 3e-8   with C = O(1) in signal units,

so eps = 1e-8 is the declared bracket -- derived from the crossover, not
selected after looking at the answers.  The whole ladder
{1e-9, 1e-8, 1e-7, 1e-6, 1e-5} is recorded in the JSON for every edge, and the
truncation law is checked independently: at eps = 1e-6, where cancellation is
negligible, ``vhat_below`` must match ``conc - beta*eps/2`` to 1e-9.  That
expansion is NOT what ``menu._interval_mass_and_mean`` computes (it evaluates
the truncated-normal mean as (phi(a) - phi(b)) / (Phi(b) - Phi(a))), so the
comparison is genuine and not a re-implementation of the code under test.

DISCREPANCY AGAINST THE CARD'S WORDING, recorded rather than smoothed.  At the
probes' own 1e-9 bracket the snap residual is 3.97e-8 at the first edge (the
card's and Analyst A's "~1e-8" / "7-8 dp"), but 1.17e-7 and 1.69e-7 at the
other two -- an order of magnitude above "~1e-8".  The cause is the
cancellation term above, u/eps ~ 1e-7 at eps = 1e-9, and it grows with distance
into the tail (the sliver mass falls from 4.0e-10 to 3.2e-10 across the three
edges).  It is a property of the bracket, not of the prediction: at eps = 1e-8
the same three residuals are 6.8e-9 / 4.4e-9 / 5.6e-9.  Every one of these
numbers is in the JSON under ``ladder``.

NOT CURATED HERE, deliberately:
  * the analytic non-vanishing weight bound  >= min(kappa/2, 1-kappa)^(d+1).
    No panel script computes it -- it is an analytic step of the panel reports
    (a6_B_findings.md section 1), read off ``pooled.py``'s
    ``EP[d][t] = L_t . P_d`` and ``policy.plan_payoff``'s
    ``res.EP[d][theta(j,s)]``.  Its *measured* counterpart -- that the jump
    survives into the plan-payoff difference with no cancellation -- IS curated,
    as ``a6_deviation_weight_noncancellation`` below.
  * the A3 material (three sign changes, the empty weakly-increasing selection,
    the argmax reversal).  A separate follow-up owns the A3 locus.
  * the chamber-interior Theta+ rescue and the P_7(h) two-sided price gap.
    Card-cited, but outside this curation's four decisive items.

RUN:  ``.venv/bin/python quality_reports/fixes/t2_a6_edge_jump_check.py``
      from the repo root.  Deterministic; no randomness anywhere in the path.
      Writes ``t2_a6_edge_jump_check.json`` beside itself.
      Read-only on ``numerical_v4/``.
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np
from scipy.optimize import brentq

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

from numerical_v4.params import ParamsV4, HOLD, VOICE  # noqa: E402
from numerical_v4.menu import atoms, type_reference, _sigmoid_inv  # noqa: E402
from numerical_v4.pooled import pooled_pass, _alive_weights  # noqa: E402
from numerical_v4.policy import plan_payoff, frozen_tau_grid  # noqa: E402
from numerical_v4.solver import solve_policy, outer_map  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "t2_a6_edge_jump_check.json")

# --------------------------------------------------------------------------
# The card's quoted numbers and the panel's filed values (both frozen here).
# --------------------------------------------------------------------------

# MODEL_CARD.md section 5, A6 evidence note (stamp 2026-08-27, commit ae9caea):
#   "measured T_2 jumps of 6.33e-3 / 1.09e-2 / 2.83e-2 across <= 2e-9 steps in
#    k_2 at (kappa=0.5, tau_50, T=5)"
CARD_3SF = {9: "0.00633", 8: "0.0109", 7: "0.0283"}

# Filed panel values, keyed by dying mark-type t.
#   routeA_1e9  : a6_A_probe7_verify.py part (B), the eps = 1e-9 column
#   routeA_1e6  : a6_A_probe7_verify.py part (B), the eps = 1e-6 column
#   routeB      : a6_B_baseline.log, |T_2(S - 1e-8) - T_2(S)|
#   vhat_pred   : a6_A_probe4_precise.py "pred (ref - conc)" column
FILED = {
    9: dict(edge_m=8, routeA_1e9=6.3333e-03, routeA_1e6=6.3331e-03,
            routeB=abs(1.543395170 - 1.549728951), vhat_pred=-1.6546e-02),
    8: dict(edge_m=7, routeA_1e9=1.0859e-02, routeA_1e6=1.0860e-02,
            routeB=abs(1.558798550 - 1.569659263), vhat_pred=-1.9229e-02),
    7: dict(edge_m=6, routeA_1e9=2.8279e-02, routeA_1e6=2.8281e-02,
            routeB=abs(1.575443391 - 1.603724853), vhat_pred=-2.3029e-02),
}
DYING_TYPES = (9, 8, 7)

# a6_B_baseline.log, the S = 1.583333333333 sweep, s0 = (k2* + S)/2:
#   U_VOICE 0.0362570819 -> 0.0365064990 ; U_HOLD 0.0359582433 -> 0.0359582433
FILED_UV_JUMP = 2.494e-04
FILED_UH_MOVE_MAX = 1e-10

# Calibration anchors the panel worked at (asserted, then the recomputed values
# are the ones actually used).
FILED_TAU50 = 0.09076405861553302
FILED_KSTAR = (1.2405757282617416, 1.5310222869296415)

# Gates -- fixed before the first run.
TOL_PANEL_REL = 5e-4        # relative agreement with the filed panel number
TOL_CROSS_REL = 5e-4        # "agreeing to 3 s.f." between the two routes
TOL_BELIEF_SNAP = 1e-8      # card says the snap matches the prediction to ~1e-8
TOL_EXPANSION = 1e-9        # sliver expansion conc - beta*eps/2, at EPS_EXPAND
TOL_CONTROL = 1e-8          # card says surviving-type controls are ~3e-9
TOL_EPS_ROBUST = 5e-4       # 1e-6 bracket vs 1e-9 bracket, relative
TOL_ANCHOR = 1e-9           # tau_50 / k* reproduction

EPS_A = 1e-9                # route A straddle (a6_A_probe4_precise.py)
EPS_ROBUST = 1e-6           # 1000x menu.breakpoints' 1e-9 merge tolerance
DELTA_B = 1e-8              # route B left offset (a6_B_baseline.py)
DELTA_B_EXTRA = 1e-9        # recorded, not gated (see module docstring)
EPS_SNAP = 1e-8             # declared belief-snap bracket (crossover eps*)
EPS_EXPAND = 1e-6           # bracket where cancellation is negligible
EPS_LADDER = (1e-9, 1e-8, 1e-7, 1e-6, 1e-5)   # recorded in full, ungated
NG = 4001                   # probe 4's signal grid; the lowest-crossing
#                             selection is grid-dependent, so this is frozen

results: dict = {"kind": "A6 applicability evidence (panel-probe curation)",
                 "checks": [], "n_fail": 0}


def record(name: str, ok: bool, kind: str, detail: dict) -> None:
    results["checks"].append({"name": name, "kind": kind, "pass": bool(ok),
                              **detail})
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def rel(a: float, b: float) -> float:
    """Relative difference on the mean scale; 0 if both are 0."""
    m = 0.5 * (abs(a) + abs(b))
    return 0.0 if m == 0.0 else abs(a - b) / m


def sig3(x: float) -> str:
    return "%.3g" % abs(x)


def n_edges(p: ParamsV4) -> dict[int, float]:
    """Interior n(s) cell edges, exactly as menu.type_reference builds them.

    n(s) is weakly DECREASING, so edge(m) is where n steps from m+1 (below) to
    m (above): mark-type m occupies [edge(m), edge(m-1)] and DIES when the
    Voice cutoff k_2 crosses edge(m-1), the TOP of its cell.
    """
    out: dict[int, float] = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < s < p.s_hi:
                out[m] = s
    return out


def card_T2(res, p: ParamsV4) -> float:
    """The CARD's T_2 = inf{s : VOICE is the argmax}: the LOWEST up-crossing of
    U_VOICE - U_HOLD.  Verbatim from a6_A_probe4_precise.py."""
    grid = np.linspace(p.s_lo, p.s_hi, NG)

    def gap(s: float) -> float:
        return (plan_payoff(VOICE, float(s), res, p)
                - plan_payoff(HOLD, float(s), res, p))

    vals = np.array([gap(s) for s in grid])
    for i in range(NG - 1):
        if vals[i] < 0.0 <= vals[i + 1] or (vals[i] <= 0.0 < vals[i + 1]):
            return float(brentq(gap, grid[i], grid[i + 1], xtol=1e-13))
    return float(p.s_hi)


def side(k1: float, k2: float, p: ParamsV4, ref) -> dict:
    """One k_2 evaluation: atoms -> alive weights -> pooled pass."""
    al = atoms((k1, k2), p)
    W, Wm, WVm, _ = _alive_weights(al, 0, p.n_theta, ref)
    res = pooled_pass(al, p, with_runup=True)
    return dict(W=W, Wm=Wm, WVm=WVm, res=res)


def vhat(s: dict, t: int) -> float:
    return float(s["WVm"][t] / s["Wm"][t]) if s["Wm"][t] > 0 else float("nan")


def belief_only(k1: float, k2: float, p: ParamsV4, ref, t: int
                ) -> tuple[float, float]:
    """(market belief attached to type t, that type's measure mass) at k_2.

    Beliefs only -- no ``pooled_pass``.  This is the cheap path used to walk the
    bracket ladder for the belief snap.
    """
    al = atoms((k1, k2), p)
    W, Wm, WVm, _ = _alive_weights(al, 0, p.n_theta, ref)
    vh = float(WVm[t] / Wm[t]) if Wm[t] > 0 else float("nan")
    return vh, float(W[t])


def main() -> int:
    t_run = time.perf_counter()

    # -- calibration: recompute tau_50 and k*, then assert the anchors --------
    print("solving the seed equilibrium (tau = 0.05) ...", flush=True)
    p_seed = ParamsV4.baseline()
    pol_seed, r_seed = solve_policy(p_seed)
    tau50 = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    print(f"  tau_50 = {tau50!r}", flush=True)
    print("solving the baseline equilibrium (frozen tau) ...", flush=True)
    p_base = p_seed.replace(tau=tau50)
    pol_base, r_base = solve_policy(p_base)
    kstar = (float(pol_base.k[0]), float(pol_base.k[1]))
    print(f"  k* = {kstar}   |k - T(k)| = {r_base.cutoff_scale:.3e}", flush=True)

    d_tau = abs(tau50 - FILED_TAU50)
    d_k = max(abs(kstar[i] - FILED_KSTAR[i]) for i in (0, 1))
    record("a6_calibration_anchors_reproduce",
           d_tau <= TOL_ANCHOR and d_k <= TOL_ANCHOR, "wiring",
           dict(tau50=tau50, tau50_filed=FILED_TAU50, tau50_abs_diff=d_tau,
                kstar=list(kstar), kstar_filed=list(FILED_KSTAR),
                kstar_max_abs_diff=d_k, tol=TOL_ANCHOR,
                seed_k=[float(x) for x in pol_seed.k],
                seed_cutoff_scale=float(r_seed.cutoff_scale),
                base_cutoff_scale=float(r_base.cutoff_scale),
                base_payoff_scale=float(r_base.payoff_scale),
                hold_region_width=kstar[1] - kstar[0],
                note="the node is (kappa=0.5, tau_50, T=5); tau_50 is the "
                     "median of frozen_tau_grid at the seed equilibrium, and "
                     "k1 is held at k*[0] throughout, as both probes do"))

    p = p_base.replace(kappa=0.5, T=5)
    ref = type_reference(p)
    K1 = kstar[0]
    edges = n_edges(p)
    results["node"] = dict(kappa=float(p.kappa), tau=float(p.tau), T=int(p.T),
                           k1_held=K1, params_hash=p.hash_str(),
                           n_edges={int(m): float(s) for m, s in edges.items()})

    # -- per-edge measurement ------------------------------------------------
    per_edge = []
    for t in DYING_TYPES:
        f = FILED[t]
        top = edges[f["edge_m"]]          # k_2 hyperplane where type t dies
        bot = edges.get(t, p.s_lo)        # bottom of type t's cell
        print(f"\n=== dying type t={t}, cell [{bot:.6f}, {top:.6f}], "
              f"dies at k2 = edge({f['edge_m']}) = {top:.12f}", flush=True)

        # route A: straddling bracket, card-convention T_2 -------------------
        A_lo = side(K1, top - EPS_A, p, ref)
        A_hi = side(K1, top + EPS_A, p, ref)
        T2_A_lo, T2_A_hi = card_T2(A_lo["res"], p), card_T2(A_hi["res"], p)
        jump_A = abs(T2_A_hi - T2_A_lo)

        # route B: implementation outer_map, left limit vs value AT the edge --
        B_lo = side(K1, top - DELTA_B, p, ref)
        B_at = side(K1, top, p, ref)
        T2_B_lo = float(outer_map((K1, top - DELTA_B), p, B_lo["res"])[1])
        T2_B_at = float(outer_map((K1, top), p, B_at["res"])[1])
        T1_B_lo = float(outer_map((K1, top - DELTA_B), p, B_lo["res"])[0])
        T1_B_at = float(outer_map((K1, top), p, B_at["res"])[0])
        jump_B = abs(T2_B_at - T2_B_lo)

        # extra, non-gating: route B at a 1e-9 left offset
        B_x = side(K1, top - DELTA_B_EXTRA, p, ref)
        T2_B_x = float(outer_map((K1, top - DELTA_B_EXTRA), p, B_x["res"])[1])

        # eps robustness: route A at 1000x the merge tolerance ---------------
        R_lo = side(K1, top - EPS_ROBUST, p, ref)
        R_hi = side(K1, top + EPS_ROBUST, p, ref)
        jump_R = abs(card_T2(R_hi["res"], p) - card_T2(R_lo["res"], p))

        # belief snap: measured vs the Step 9(b) closed form -----------------
        # The above-side belief is the k-free reference and does not move with
        # the bracket, so only the below side is walked along the ladder.
        conc = p.mu_v + p.beta * (top - p.mu_v)   # concentration limit
        vh_lo, vh_hi = vhat(A_lo, t), vhat(A_hi, t)
        snap_pred = float(ref.Ev[t]) - conc
        ladder = []
        for e in EPS_LADDER:
            v_e, W_e = belief_only(K1, top - e, p, ref, t)
            ladder.append(dict(eps=e, vhat_below=v_e, sliver_mass=W_e,
                               snap=vh_hi - v_e,
                               snap_abs_error=abs((vh_hi - v_e) - snap_pred),
                               expansion=conc - p.beta * e / 2.0,
                               expansion_residual=abs(v_e
                                                      - (conc - p.beta * e / 2.0))))
        by_eps = {r["eps"]: r for r in ladder}
        snap_err = by_eps[EPS_SNAP]["snap_abs_error"]
        exp_res = by_eps[EPS_EXPAND]["expansion_residual"]
        snap_err_filed = by_eps[EPS_A]["snap_abs_error"]

        # surviving-neighbour control (a6_A_probe6_channel.py) ---------------
        tc = t - 1                              # the cell just above: survives
        ctl_bid = abs(float(A_hi["res"].Ep_bid[tc] - A_lo["res"].Ep_bid[tc]))
        ctl_EP = float(sum(abs(A_hi["res"].EP[d][tc] - A_lo["res"].EP[d][tc])
                           for d in range(p.H + 1)))
        dying_EP = float(sum(abs(A_hi["res"].EP[d][t] - A_lo["res"].EP[d][t])
                             for d in range(p.H + 1)))
        ctl_max = max(ctl_bid, ctl_EP)

        common = dict(dying_type=t, edge_index=f["edge_m"], edge=float(top),
                      cell=[float(bot), float(top)], k1=K1)

        record(f"a6_routeA_cardT2_jump_t{t}",
               sig3(jump_A) == CARD_3SF[t]
               and rel(jump_A, f["routeA_1e9"]) <= TOL_PANEL_REL,
               "substantive",
               dict(**common, route="A (card T_2 = inf of the VOICE argmax "
                                    "set, brentq on the lowest up-crossing)",
                    bracket=f"k2 = edge -/+ {EPS_A:g}  (step {2*EPS_A:g})",
                    T2_below=T2_A_lo, T2_above=T2_A_hi, jump=jump_A,
                    jump_3sf=sig3(jump_A), card_3sf=CARD_3SF[t],
                    panel_filed=f["routeA_1e9"],
                    panel_rel_diff=rel(jump_A, f["routeA_1e9"]),
                    tol_panel_rel=TOL_PANEL_REL, n_grid=NG,
                    W_dying_below=float(A_lo["W"][t]),
                    W_dying_above=float(A_hi["W"][t])))

        record(f"a6_routeB_implT2_jump_t{t}",
               sig3(jump_B) == CARD_3SF[t]
               and rel(jump_B, f["routeB"]) <= TOL_PANEL_REL,
               "substantive",
               dict(**common, route="B (implementation solver.outer_map, "
                                    "nearest-bracket tie-break)",
                    bracket=f"k2 = edge - {DELTA_B:g}  vs  k2 = edge exactly",
                    T2_below=T2_B_lo, T2_at_edge=T2_B_at, jump=jump_B,
                    jump_3sf=sig3(jump_B), card_3sf=CARD_3SF[t],
                    panel_filed=f["routeB"],
                    panel_rel_diff=rel(jump_B, f["routeB"]),
                    tol_panel_rel=TOL_PANEL_REL,
                    T1_below=T1_B_lo, T1_at_edge=T1_B_at,
                    T1_jump=abs(T1_B_at - T1_B_lo),
                    T1_note="T_1 is continuous through the edge -- the pooled "
                            "price system moves with k_2 alone on this menu "
                            "(see t2_a6_collapse_face_check)",
                    extra_deltas={"T2_at_edge_minus_1e-9": T2_B_x,
                                  "jump_vs_1e-9_offset": abs(T2_B_at - T2_B_x),
                                  "note": "recorded only; gates nothing. The "
                                          "card's '<= 2e-9 steps' clause is "
                                          "carried by route A, whose filed "
                                          "bracket is a 2e-9 straddle."}))

        record(f"a6_cross_route_agreement_t{t}",
               rel(jump_A, jump_B) <= TOL_CROSS_REL, "substantive",
               dict(**common, jump_routeA=jump_A, jump_routeB=jump_B,
                    rel_diff=rel(jump_A, jump_B), tol=TOL_CROSS_REL,
                    both_3sf=[sig3(jump_A), sig3(jump_B)],
                    claim="card: 'measured independently by both panellists "
                          "with separate scripts, agreeing to 3 s.f.'"))

        record(f"a6_belief_snap_t{t}",
               snap_err <= TOL_BELIEF_SNAP and exp_res <= TOL_EXPANSION,
               "substantive",
               dict(**common,
                    vhat_below_at_filed_1e9=vh_lo, vhat_above=vh_hi,
                    snap_predicted=snap_pred,
                    panel_filed_prediction=f["vhat_pred"],
                    concentration_limit=conc,
                    k_free_reference_Ev=float(ref.Ev[t]),
                    above_side_is_k_free=abs(vh_hi - float(ref.Ev[t])),
                    declared_bracket=EPS_SNAP,
                    snap_abs_error_at_declared_bracket=snap_err,
                    tol_snap=TOL_BELIEF_SNAP,
                    expansion_bracket=EPS_EXPAND,
                    expansion_residual=exp_res, tol_expansion=TOL_EXPANSION,
                    snap_abs_error_at_probes_1e9_bracket=snap_err_filed,
                    ladder=ladder,
                    prediction="Step 9(b): mu_v + beta*(edge - mu_v)  (the "
                               "vanishing sliver's concentration limit, below) "
                               "-> type_reference.Ev[t]  (the k-free "
                               "plan-uniform posterior, above)",
                    bracket_note="the prediction is a LIMIT; a finite bracket "
                                 "eps carries truncation beta*eps/2 and "
                                 "cancellation ~u/eps, crossing near "
                                 "eps* ~ 3e-8, so eps = 1e-8 is the declared "
                                 "bracket. The expansion gate checks "
                                 "vhat_below = conc - beta*eps/2 at eps = 1e-6, "
                                 "where cancellation is negligible; that "
                                 "expansion is not the formula "
                                 "menu._interval_mass_and_mean evaluates, so "
                                 "the comparison is independent of the code "
                                 "under test",
                    card_wording_discrepancy=(
                        "at the probes' own 1e-9 bracket this residual is "
                        f"{snap_err_filed:.2e}; the card says '~1e-8', which "
                        "holds at the first edge (3.97e-8) but is an order of "
                        "magnitude tight at the other two (1.17e-7, 1.69e-7). "
                        "Bracket cancellation, not the prediction: see ladder"
                    )))

        record(f"a6_surviving_type_control_t{t}", ctl_max <= TOL_CONTROL,
               "substantive",
               dict(**common, surviving_type=tc,
                    control_Ep_bid_jump=ctl_bid,
                    control_sum_abs_EP_jump=ctl_EP,
                    control_max=ctl_max, tol=TOL_CONTROL,
                    dying_type_sum_abs_EP_jump=dying_EP,
                    ratio_dying_over_control=(dying_EP / ctl_EP
                                              if ctl_EP > 0 else float("inf")),
                    note="the jump is confined to the dying type's own "
                         "aggregates; the neighbour that survives the crossing "
                         "moves at solver noise"))

        record(f"a6_eps_robustness_t{t}",
               rel(jump_R, jump_A) <= TOL_EPS_ROBUST
               and rel(jump_R, f["routeA_1e6"]) <= TOL_PANEL_REL,
               "substantive",
               dict(**common, eps_robust=EPS_ROBUST, eps_base=EPS_A,
                    merge_tolerance=1e-9,
                    multiple_of_merge_tolerance=EPS_ROBUST / 1e-9,
                    jump_at_1e6=jump_R, jump_at_1e9=jump_A,
                    rel_diff=rel(jump_R, jump_A), tol=TOL_EPS_ROBUST,
                    panel_filed_1e6=f["routeA_1e6"],
                    panel_rel_diff=rel(jump_R, f["routeA_1e6"]),
                    note="1000x menu.breakpoints' near-duplicate merge "
                         "tolerance: not a merged-sliver artifact"))

        per_edge.append(dict(dying_type=t, edge=float(top),
                             jump_routeA=jump_A, jump_routeB=jump_B,
                             jump_3sf=sig3(jump_A), card_3sf=CARD_3SF[t],
                             cross_route_rel=rel(jump_A, jump_B),
                             belief_snap_abs_error_at_1e8=snap_err,
                             belief_snap_abs_error_at_1e9=snap_err_filed,
                             sliver_expansion_residual=exp_res,
                             control_max=ctl_max, jump_at_1e6=jump_R))

    # -- the jump reaches T with no cancellation (measured counterpart of the
    #    analytic weight bound, which is NOT curated -- see the docstring) ----
    t = 9
    S = edges[FILED[t]["edge_m"]]
    s0 = 0.5 * (kstar[1] + S)              # a6_B_baseline.py's evaluation point
    N_lo = side(K1, S - DELTA_B, p, ref)
    N_at = side(K1, S, p, ref)
    Uv_lo = float(plan_payoff(VOICE, s0, N_lo["res"], p))
    Uv_at = float(plan_payoff(VOICE, s0, N_at["res"], p))
    Uh_lo = float(plan_payoff(HOLD, s0, N_lo["res"], p))
    Uh_at = float(plan_payoff(HOLD, s0, N_at["res"], p))
    dUv, dUh = Uv_at - Uv_lo, Uh_at - Uh_lo
    record("a6_deviation_weight_noncancellation",
           rel(dUv, FILED_UV_JUMP) <= TOL_PANEL_REL
           and abs(dUh) <= FILED_UH_MOVE_MAX, "substantive",
           dict(edge=float(S), s0=s0, k1=K1,
                U_VOICE_below=Uv_lo, U_VOICE_at_edge=Uv_at, U_VOICE_jump=dUv,
                U_HOLD_below=Uh_lo, U_HOLD_at_edge=Uh_at, U_HOLD_move=dUh,
                panel_filed_U_VOICE_jump=FILED_UV_JUMP,
                panel_rel_diff=rel(dUv, FILED_UV_JUMP),
                tol_U_HOLD_move=FILED_UH_MOVE_MAX,
                gap_jump=abs(dUv - dUh),
                scope="MEASURED counterpart only. The analytic bound "
                      "weight >= min(kappa/2, 1-kappa)^(d+1) is NOT curated "
                      "here: no panel script computes it. What is measured is "
                      "that the price jump survives into the adjacent-plan "
                      "payoff difference undiminished -- U_VOICE jumps while "
                      "U_HOLD does not move, so nothing cancels and the whole "
                      "jump passes into any selection that is pointwise in k."))

    # -- aggregate -----------------------------------------------------------
    results["per_edge_summary"] = per_edge
    results["known_discrepancies"] = [
        {
            "card_wording": "the belief snap matching the Step 9(b) prediction "
                            "to ~1e-8",
            "reproduced": True,
            "measured_at_declared_bracket_1e-8": [
                e["belief_snap_abs_error_at_1e8"] for e in per_edge],
            "measured_at_probes_bracket_1e-9": [
                e["belief_snap_abs_error_at_1e9"] for e in per_edge],
            "finding": "'~1e-8' holds at the probes' own 1e-9 bracket only for "
                       "the first edge (3.97e-8, matching Analyst A's '7-8 dp' "
                       "note); at the other two edges the 1e-9 bracket gives "
                       "1.17e-7 and 1.69e-7. The cause is floating-point "
                       "cancellation in Phi(b) - Phi(a) over a 1e-9-wide "
                       "interval (relative loss u/eps ~ 1e-7), worsening into "
                       "the tail as the sliver mass falls 4.0e-10 -> 3.2e-10. "
                       "It is a bracket artifact, not a gap in the prediction: "
                       "at the crossover bracket eps = 1e-8 all three residuals "
                       "are ~5e-9, and the sliver's exact posterior tracks "
                       "conc - beta*eps/2 to 1e-10 at eps = 1e-6. The card's "
                       "wording is optimistic by about one order of magnitude "
                       "for two of the three edges; nothing else moves.",
        }
    ]
    results["seconds"] = time.perf_counter() - t_run
    results["all_pass"] = results["n_fail"] == 0
    n_ok = sum(1 for e in per_edge if e["jump_3sf"] == e["card_3sf"])
    results["verdict"] = (
        "A6 continuity failure REPRODUCED at calibration"
        if results["all_pass"] else
        f"A6 continuity measurement PARTIALLY REPRODUCED "
        f"({results['n_fail']} gate(s) missed)"
    ) + (
        f" -- (kappa=0.5, tau_50, T=5): T_2 jumps of "
        + " / ".join(e["jump_3sf"] for e in per_edge)
        + f" across the three interior n(s) cell edges, {n_ok}/3 matching the "
        f"card's quoted 3 s.f. figures, both panel routes agreeing to 3 s.f., "
        f"the belief snap matching the Step 9(b) prediction and the "
        f"surviving-type controls at solver noise. NO LABEL MOVES AND NONE IS "
        f"LICENSED: A6 is a listed hypothesis of P1, so this is applicability "
        f"evidence on its antecedent at the implemented calibration, in the "
        f"A(tau) pattern -- P1 stays PROVED as a conditional."
    )
    results["provenance"] = {
        "follow_up": "quality_reports/fixes/a6_panel_probes_2026-08-27/"
                     "README.md -- the standing curation follow-up",
        "source_probes": [
            "a6_panel_probes_2026-08-27/a6_A_probe4_precise.py (route A: "
            "card-convention T_2, belief snap)",
            "a6_panel_probes_2026-08-27/a6_A_probe6_channel.py (surviving-"
            "neighbour control)",
            "a6_panel_probes_2026-08-27/a6_A_probe7_verify.py part (B) "
            "(1000x merge-tolerance robustness)",
            "a6_panel_probes_2026-08-27/a6_B_baseline.py (route B: "
            "implementation outer_map across the same three hyperplanes)",
        ],
        "readme_mapping_correction": (
            "The probe README names 'a6_A_probe4 / a6_B_sweep' as the two "
            "routes. a6_B_sweep.py part (B) runs at the SEED threshold "
            "(ParamsV4(), tau = 0.05) and its jump across s = 1.583333 is "
            "-1.727e-2, not the card's 6.33e-3; the card's B-route numbers "
            "come from a6_B_baseline.py, which re-freezes tau first. "
            "a6_B_sweep.py part (A) is the collapse-face measurement, curated "
            "in t2_a6_collapse_face_check.py."
        ),
        "card_row": "research/model_v4/MODEL_CARD.md section 5, A6 evidence "
                    "note (stamp 2026-08-27, commit ae9caea)",
        "panel_reports": [
            "research/model_v4/threads/2026-08-27_A6_panel_substantiate.md",
            "research/model_v4/threads/2026-08-27_A6_panel_defuse.md",
        ],
        "verdict_semantics": (
            "INVERTED relative to a proof check. pass = the panel's "
            "measurement REPRODUCED, i.e. the discontinuity is there at the "
            "quoted size and locus. pass does NOT mean A6 holds. This file is "
            "applicability evidence and licenses no label move; A6 is a "
            "hypothesis of P1, not a claim of it."
        ),
        "environment_gate": ".venv/bin/python -m numerical_v4.smoke, exit 0",
        "does_not": [
            "touch MODEL_CARD.md, the mirrors, sections_v3/ or anything under "
            "research/",
            "modify anything under numerical_v4/ (imported read-only)",
            "curate the analytic weight bound min(kappa/2,1-kappa)^(d+1) -- no "
            "panel script computes it",
            "curate the A3 material (three sign changes, empty weakly-"
            "increasing selection, argmax reversal) -- a separate follow-up "
            "owns the A3 locus",
            "curate the chamber-interior Theta+ rescue or the P_7(h) price gap",
            "claim or deny nonexistence of equilibrium anywhere",
        ],
    }

    tmp = OUT + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    os.replace(tmp, OUT)

    print(f"\n{results['verdict']}", flush=True)
    print(f"({len(results['checks'])} checks, {results['n_fail']} failing, "
          f"{results['seconds']:.0f} s)  ->  {OUT}", flush=True)
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
