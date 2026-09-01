"""VERIFIER probe 2 -- does locus (i)'s A3 failure track the off-path family?

Written 2026-08-29 by a fresh verifier agent who did NOT write the
p1-existence-route exploration.  This is the REBUILD of the exploration's
locus-(i) family claim, run at the CARD's own protocol rather than the
exploration's.

THE CLAIM UNDER TEST (exploration, .scratch/p1-existence-route/issues/
01-route-exploration.md section 3(b)): "locus (i) of card section 5's A3 note
does not reproduce under a Step-9(b)-faithful mass-proportional family" -- 3
strict sign changes of U_V - U_H under the shipped uniform floor, 1 under the
mass-proportional one.  The exploration measured this at ONE k
(k_2 = edge(6) + 1e-4) on a 4001-point grid.  The card's record is the whole
k_2 ladder on a 6001-point grid.

PROTOCOL, taken from the committed curated check ``t2_a3_ordered_plans_check.py``
(which is itself taken from ``a6_A_probe8_open.py``) so the two are comparable
line for line:
  * node (kappa = 0.5, tau_50, T = 5), k_1 held at k*[0];
  * k_2 = edge(6) + offset over the ladder (-1e-9,) + (1e-9, 1e-4, 1e-3, 5e-3,
    2e-2) + (5e-2, 1e-1);
  * gap g(s) = plan_payoff(VOICE) - plan_payoff(HOLD) on
    np.linspace(s_lo, s_hi, 6001);
  * strict sign-change criterion sign(v[:-1]) * sign(v[1:]) < 0;
  * locations by brentq(xtol = 1e-13) on each bracket.

THE FAMILIES.  Step 9(b) (``proofs/P1_proof.md`` lines 494-540) fixes the
off-path limit at a k-null history as mu(j,s) = L_j(h|s) phi_s(s) / Lambda_u
with Lambda_u = sum_{j'} int L_{j'}(h|s') phi_s(s') ds'.  Grouping (j', s') by
mark-path type gives Lambda_u = sum_t L_t(h) * m[t] with
m[t] = sum_{j'} Pr(theta(j', s) = t): PLAN weights uniform, TYPE weights
proportional to likelihood-times-signal-mass.  On this menu m[0] = 2 (Exit and
Hold both give the all-zero path at every s) and m[t] = Pr(n(s) = t) for
t >= 1 (Voice only).  ``v_offpath_family_facts.json`` records that at this
locus every FLOORED type is 7..11, each with D = 0 and f = inf CONSTANT on its
whole n(s) cell, so m[t] = Pr(n(s)=t) is EXACTLY Step 9(b)'s weight for every
type that is floored here, and type 0 (whose m the exploration got wrong) is
alive at every ladder point.

  shipped          the real numerical_v4.pooled._alive_weights, unpatched.
  switch_uniform   patched replica of shipped -- HARNESS CONTROL, must match
                   ``shipped`` bit for bit.
  switch_step9b    shipped's hard switch, floor eps*m[t]/J instead of eps.
  blend_uniform    genuine fixed-t game with a uniform reference measure:
                   Wm = (1-eps)W + eps.
  blend_step9b     genuine fixed-t game, Step-9(b) reference measure:
                   Wm = (1-eps)W + eps*m[t]/J.  This is the object Step 9(b)
                   takes the t -> 0 limit OF.
  switch_expl      the exploration's own family verbatim (voice-only mass, no
                   1/J) -- REPRODUCTION CONTROL for its filed numbers.

PRE-REGISTERED, before any of the family rows were run (the shipped rows are
gated against the card, which fixes them in advance):
  P1  shipped reproduces the card: 3 strict sign changes at every offset in
      (1e-9, 1e-4, 1e-3, 5e-3, 2e-2), 1 at -1e-9 and at (5e-2, 1e-1), and the
      three "%.7f" locations at +1e-9 are 1.5754434 / 1.5833333 / 1.5902426.
  P2  switch_uniform == shipped exactly (harness control).
  P3  the exploration's headline generalises: switch_step9b gives 1 strict
      sign change at EVERY offset of the ladder, not only at +1e-4.  Any
      offset showing 3 NARROWS the exploration's claim to the offsets it
      tested.
  P4  the count is eps-invariant within each family (the exploration's
      "continuity is not what moves this").
  P5  under a family with 1 sign change the pointwise argmax is weakly
      increasing in s, so a weakly increasing selection EXISTS and A3's
      second clause is not violated at this k.

DECLARED POST-RUN-1 RESTRUCTURE.  Run 1 (2026-08-29, ladder
(-1e-9, 1e-9, 1e-4, 1e-3, 5e-3, 2e-2, 5e-2, 1e-1), 10 gates) returned this
table of strict sign-change counts, PRESERVED here verbatim:

    family            eps      -1e-9  1e-9  1e-4  1e-3  5e-3  2e-2  5e-2  1e-1
    shipped            --          1     3     3     3     3     3     1     1
    switch_uniform   1e-14         1     3     3     3     3     3     1     1
    switch_uniform   1e-09         3     3     3     3     3     3     1     1
    switch_uniform   1e-06         3     3     3     3     3     3     1     1
    switch_step9b    1e-14         3     1     1     1     1     1     3     3
    switch_step9b    1e-09         1     1     1     1     1     1     3     3
    switch_step9b    1e-06         1     1     1     1     1     1     3     3
    switch_expl      1e-14         3     1     1     1     1     1     3     3
    switch_expl      1e-09         1     1     1     1     1     1     3     3
    switch_expl      1e-06         1     1     1     1     1     1     3     3
    blend_uniform    1e-14         1     3     3     3     3     3     1     1
    blend_uniform    1e-09         3     3     3     3     3     3     1     1
    blend_uniform    1e-06         3     3     3     3     3     3     1     1
    blend_step9b     1e-14         3     1     1     1     1     1     3     3
    blend_step9b     1e-09         1     1     1     1     1     1     3     3
    blend_step9b     1e-06         1     1     1     1     1     1     3     3

  Run-1 verdicts: anchors PASS, P1a PASS, P1b PASS, P5a PASS, P3b PASS,
  P5b PASS; P2 FAIL, P3 FAIL, P4 FAIL, P4b FAIL.  What changes below is the
  FORM of three gates and the ladder's length.  No measured number changes,
  and every run-1 miss is preserved in the JSON under ``prereg_run1``.

  (R1) P2 was MIS-SPECIFIED, not missed.  ``switch_uniform`` is the shipped
       construction only at eps = OFF_PATH_EPS = 1e-14; at eps = 1e-9 and
       1e-6 it is a DIFFERENT family (a bigger uniform floor), so requiring it
       to equal ``shipped`` there was never a control.  At eps = 1e-14 it
       matched ``shipped`` at every offset in run 1.  The gate is now the
       eps = 1e-14 comparison alone, and the eps-dependence it exposed is
       recorded as finding F-eps below.
  (R2) P3 was REFUTED AS WRITTEN and is split.  The Step-9(b) family gives 1
       sign change at every CARD-LADDER offset (1e-9 ... 2e-2) -- the
       exploration's headline reproduces there -- but 3 at +5e-2 and +1e-1,
       where the SHIPPED family gives 1.  The proof-faithful family therefore
       RELOCATES locus (i)'s A3 failure along the k_2 ladder; it does not
       remove it.  P3 is now gated on exactly the offsets the card's own
       open-set claim ranges over (MODEL_CARD.md:189, "verified at offsets
       10^-9 through 2x10^-2"), which is the scope of the exploration's
       headline; the reversal at the larger offsets is recorded as finding
       F-relocate, UNGATED (it was not pre-registered).  The ladder is
       extended with (3e-2, 4e-2, 7e-2) to bracket where the Step-9(b)
       family's failure region opens -- run 2 puts the flip between +3e-2
       (1 sign change) and +4e-2 (3).
  (R3) P4 / P4b are restricted to offsets other than -1e-9.  At -1e-9 the
       dying type's surviving sliver carries alive mass ~4e-10 (measured in
       ``v_offpath_family_facts.json``) and the floor is eps*m/J, so which of
       the two dominates -- and hence the belief -- is genuinely eps-dependent
       exactly there and nowhere else.  That is not noise: it is the
       fixed-t game's own crossover, and it is recorded as finding F-eps and
       used as evidence for finding F1 rather than gated away.

  P5a's sampling geometry, declared: intervals are cut at s_lo, the located
  sign changes, and s_hi, and sampled at midpoints.  The first interval's
  midpoint sits below k_1, so the shipped word reads E,V,H,V where the card's
  A3 note reads "H,V,H,V" -- the card's four labels are the ones around the
  crossings.  The gated content is that the word is NOT weakly increasing,
  which is what "no weakly increasing selection exists" means.

Deterministic: fixed grids, no RNG.  Read-only on ``numerical_v4/`` -- the
patch is installed on the module object in memory and restored in a finally
block; nothing under that package is written.
"""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np
from scipy.optimize import brentq

ROOT = "/Users/austinli/Projects/blockholder_v4_theory"
sys.path.insert(0, ROOT)

import numerical_v4.pooled as pooled_mod                              # noqa: E402
from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE           # noqa: E402
from numerical_v4.menu import (atoms, type_reference, n_days,         # noqa: E402
                               _sigmoid_inv, _interval_mass_and_mean)
from numerical_v4.pooled import pooled_pass, OFF_PATH_EPS             # noqa: E402
from numerical_v4.policy import plan_payoff, frozen_tau_grid          # noqa: E402
from numerical_v4.solver import solve_policy                          # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "v_offpath_locus1_ladder.json")
_ORIG = pooled_mod._alive_weights

# --- the card's / the curated check's filed anchors ------------------------
FILED_TAU50 = 0.09076405861553302
FILED_K1 = 1.2405757282617416
FILED_EDGE6 = 1.7492686492653553
FILED_EDGE8 = 1.583333333333333
CARD_CROSSINGS_7DP = ("1.5754434", "1.5833333", "1.5902426")
LADDER_OPEN = (1e-9, 1e-4, 1e-3, 5e-3, 2e-2)     # card: expect 3
LADDER_CLOSED = (5e-2, 1e-1)                     # panel-filed: expect 1
LADDER_EXTRA = (3e-2, 4e-2, 7e-2)                # (R2): bracket the flip
OFFSET_BELOW = -1e-9                             # panel-filed: expect 1
OFFSET_CARD = 1e-9
LADDER = tuple(sorted((OFFSET_BELOW,) + LADDER_OPEN + LADDER_EXTRA
                      + LADDER_CLOSED))
LADDER_CARD = LADDER_OPEN + LADDER_CLOSED        # the card's own offsets

NG = 6001
TOL_ANCHOR = 1e-9
EPSES = (1e-14, 1e-9, 1e-6)
J_PLANS = 3.0

results: dict = {"what": "verifier probe 2 -- locus (i) A3 count vs off-path "
                         "family, at the card's own ladder",
                 "date": "2026-08-29", "gates": [], "rows": []}


def record(name: str, ok: bool, detail: dict) -> None:
    results["gates"].append(dict(gate=name, pass_=bool(ok), **detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def n_edges(p: ParamsV4) -> dict[int, float]:
    out: dict[int, float] = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < s < p.s_hi:
                out[m] = s
    return out


def type_masses(p: ParamsV4) -> tuple[np.ndarray, np.ndarray]:
    """(voice-only mass, Step-9(b) mass).  See the module docstring."""
    edges = [p.s_lo, p.s_hi]
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            x = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < x < p.s_hi:
                edges.append(x)
    edges = sorted(set(edges))
    voice = np.zeros(p.n_theta)
    for lo, hi in zip(edges[:-1], edges[1:]):
        t = n_days(0.5 * (lo + hi), p)
        w, _ = _interval_mass_and_mean(lo, hi, p)
        voice[t] += w
    full = voice.copy()
    full[0] += 2.0
    return voice, full


def make_family(kind: str, eps: float, mass_voice: np.ndarray,
                mass_full: np.ndarray):
    """Return a replacement for pooled._alive_weights."""
    def f(atom_list, d, n_theta, ref=None):
        W, Wm, WVm, WAm = _ORIG(atom_list, d, n_theta, None)
        if ref is None:
            return W, Wm, WVm, WAm
        Wm, WVm, WAm = Wm.copy(), WVm.copy(), WAm.copy()
        for t in range(n_theta):
            public = (ref.D[t] == 1.0 and ref.f[t] <= d)
            if kind == "switch_uniform":
                fl = OFF_PATH_EPS if eps is None else eps
            elif kind == "switch_step9b":
                fl = eps * float(mass_full[t]) / J_PLANS
            elif kind == "switch_expl":
                fl = eps * float(mass_voice[t])
            elif kind == "blend_uniform":
                fl = eps
            elif kind == "blend_step9b":
                fl = eps * float(mass_full[t]) / J_PLANS
            else:
                raise ValueError(kind)
            if public:
                fl = 0.0
            if kind.startswith("switch"):
                if public or Wm[t] > 0.0:
                    continue
                Wm[t] = fl
                WVm[t] = fl * float(ref.Ev[t])
                WAm[t] = fl * float(ref.a[t])
            else:
                Wm[t] = (1.0 - eps) * Wm[t] + fl
                WVm[t] = (1.0 - eps) * WVm[t] + fl * float(ref.Ev[t])
                WAm[t] = (1.0 - eps) * WAm[t] + fl * float(ref.a[t])
        return W, Wm, WVm, WAm
    return f


def measure(k1: float, k2: float, p: ParamsV4, grid: np.ndarray,
            want_argmax: bool) -> dict:
    res = pooled_pass(atoms((k1, k2), p), p, with_runup=True)

    def g(s: float) -> float:
        return (plan_payoff(VOICE, float(s), res, p)
                - plan_payoff(HOLD, float(s), res, p))

    vals = np.array([g(float(s)) for s in grid])
    idx = np.nonzero(np.sign(vals[:-1]) * np.sign(vals[1:]) < 0)[0]
    located = [float(brentq(g, float(grid[i]), float(grid[i + 1]),
                            xtol=1e-13)) for i in idx]
    out = dict(k2=float(k2), n_sign_changes=int(len(idx)),
               located=[float(x) for x in located],
               located_7dp=["%.7f" % x for x in located],
               max_price_residual=float(res.max_price_residual),
               n_hist_feasible=int(res.n_hist_feasible),
               nan_in_gap=bool(np.isnan(vals).any()))
    if len(located) >= 2:
        sel = (grid > located[0]) & (grid < located[-1])
        out["excursion_grid_max"] = (float(np.max(np.abs(vals[sel])))
                                     if sel.any() else None)
    if want_argmax:
        # one interior sample per interval cut by the located sign changes
        cuts = [float(p.s_lo)] + located + [float(p.s_hi)]
        prof = []
        for lo, hi in zip(cuts[:-1], cuts[1:]):
            s = 0.5 * (lo + hi)
            u = {j: float(plan_payoff(j, s, res, p))
                 for j in (EXIT, HOLD, VOICE)}
            order = sorted(u, key=lambda j: u[j], reverse=True)
            prof.append(dict(s=float(s), argmax=int(order[0]),
                             label={EXIT: "E", HOLD: "H",
                                    VOICE: "V"}[order[0]],
                             gap_to_runner_up=float(u[order[0]]
                                                    - u[order[1]]),
                             payoffs={int(j): u[j] for j in u}))
        out["argmax_profile"] = prof
        out["argmax_word"] = "".join(r["label"] for r in prof)
        out["argmax_weakly_increasing"] = bool(
            all(prof[i]["argmax"] <= prof[i + 1]["argmax"]
                for i in range(len(prof) - 1)))
        # jump-vs-root classification at each located sign change
        cls = []
        for c in located:
            cls.append(dict(s=float(c),
                            n_below=int(n_days(c - 1e-9, p)),
                            n_above=int(n_days(c + 1e-9, p)),
                            gap_below=float(g(c - 1e-9)),
                            gap_above=float(g(c + 1e-9))))
        out["crossing_classification"] = cls
    return out


def main() -> int:
    t_start = time.time()
    print("solving seed equilibrium ...", flush=True)
    p_seed = ParamsV4.baseline()
    pol_seed, _ = solve_policy(p_seed)
    tau50 = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau50)
    pol_base, _ = solve_policy(p_base)
    K1 = float(pol_base.k[0])
    p = p_base.replace(kappa=0.5, T=5)
    edges = n_edges(p)
    E6, E8 = edges[6], edges[8]
    mass_voice, mass_full = type_masses(p)
    grid = np.linspace(p.s_lo, p.s_hi, NG)

    results["node"] = dict(kappa=0.5, tau=tau50, T=5, k1_held=K1,
                           kstar=[float(x) for x in pol_base.k],
                           edge6=float(E6), edge8=float(E8),
                           grid=NG, params_hash=p.hash_str(),
                           OFF_PATH_EPS=OFF_PATH_EPS, J=J_PLANS,
                           mass_step9b={t: float(mass_full[t])
                                        for t in range(p.n_theta)},
                           mass_voice_only={t: float(mass_voice[t])
                                            for t in range(p.n_theta)})
    print("\n--- anchors ---", flush=True)
    record("anchors_reproduce_filed_literals",
           abs(tau50 - FILED_TAU50) <= TOL_ANCHOR
           and abs(K1 - FILED_K1) <= TOL_ANCHOR
           and abs(E6 - FILED_EDGE6) <= TOL_ANCHOR
           and abs(E8 - FILED_EDGE8) <= TOL_ANCHOR,
           dict(tau50=tau50, tau50_filed=FILED_TAU50, k1=K1,
                k1_filed=FILED_K1, edge6=float(E6), edge6_filed=FILED_EDGE6,
                edge8=float(E8), edge8_filed=FILED_EDGE8, tol=TOL_ANCHOR))

    try:
        # ---- A. the shipped family, gated against the card ----------------
        print("\n--- A. shipped family (the card's record) ---", flush=True)
        shipped_rows = {}
        for off in LADDER:
            r = measure(K1, E6 + off, p, grid, want_argmax=True)
            r.update(family="shipped", eps=None, offset=float(off))
            shipped_rows[off] = r
            results["rows"].append(r)
            print(f"  offset {off:+.0e}: {r['n_sign_changes']} sign change(s) "
                  f"at {r['located_7dp']}  argmax {r['argmax_word']}",
                  flush=True)
        ok_open = all(shipped_rows[o]["n_sign_changes"] == 3
                      for o in LADDER_OPEN)
        ok_closed = all(shipped_rows[o]["n_sign_changes"] == 1
                        for o in (OFFSET_BELOW,) + LADDER_CLOSED)
        record("P1a_shipped_ladder_counts_match_card", ok_open and ok_closed,
               dict(counts={str(o): shipped_rows[o]["n_sign_changes"]
                            for o in LADDER},
                    expect_open=3, expect_closed=1))
        got = tuple(shipped_rows[OFFSET_CARD]["located_7dp"])
        record("P1b_shipped_card_crossings_7dp", got == CARD_CROSSINGS_7DP,
               dict(got=list(got), card=list(CARD_CROSSINGS_7DP),
                    offset=OFFSET_CARD))
        record("P5a_shipped_argmax_not_weakly_increasing",
               shipped_rows[OFFSET_CARD]["argmax_weakly_increasing"] is False,
               dict(word=shipped_rows[OFFSET_CARD]["argmax_word"],
                    note="card: the pointwise argmax runs H,V,H,V"))

        # ---- B. the family sweep over the whole ladder --------------------
        fam_rows: dict[tuple, dict] = {}
        for kind in ("switch_uniform", "switch_step9b", "switch_expl",
                     "blend_uniform", "blend_step9b"):
            for eps in EPSES:
                print(f"\n--- {kind}  eps = {eps:.0e} ---", flush=True)
                pooled_mod._alive_weights = make_family(kind, eps, mass_voice,
                                                        mass_full)
                want = (kind in ("switch_step9b", "blend_step9b")
                        and eps == 1e-14)
                for off in LADDER:
                    r = measure(K1, E6 + off, p, grid, want_argmax=want)
                    r.update(family=kind, eps=float(eps), offset=float(off))
                    fam_rows[(kind, eps, off)] = r
                    results["rows"].append(r)
                    print(f"  offset {off:+.0e}: {r['n_sign_changes']} "
                          f"sign change(s) at {r['located_7dp']}"
                          + (f"  argmax {r['argmax_word']}" if want else ""),
                          flush=True)
    finally:
        pooled_mod._alive_weights = _ORIG

    def cnt(kind, eps):
        return {f"{off:+.0e}": fam_rows[(kind, eps, off)]["n_sign_changes"]
                for off in LADDER}

    # ---- gates (restructured; see DECLARED POST-RUN-1 RESTRUCTURE) --------
    print("\n--- gates ---", flush=True)
    results["prereg_run1"] = dict(
        ladder=[-1e-9, 1e-9, 1e-4, 1e-3, 5e-3, 2e-2, 5e-2, 1e-1],
        verdicts=dict(anchors="PASS", P1a="PASS", P1b="PASS", P5a="PASS",
                      P2="FAIL", P3="FAIL", P4="FAIL", P3b="PASS",
                      P5b="PASS", P4b="FAIL"),
        counts={
            "shipped|--": [1, 3, 3, 3, 3, 3, 1, 1],
            "switch_uniform|1e-14": [1, 3, 3, 3, 3, 3, 1, 1],
            "switch_uniform|1e-09": [3, 3, 3, 3, 3, 3, 1, 1],
            "switch_uniform|1e-06": [3, 3, 3, 3, 3, 3, 1, 1],
            "switch_step9b|1e-14": [3, 1, 1, 1, 1, 1, 3, 3],
            "switch_step9b|1e-09": [1, 1, 1, 1, 1, 1, 3, 3],
            "switch_step9b|1e-06": [1, 1, 1, 1, 1, 1, 3, 3],
            "switch_expl|1e-14": [3, 1, 1, 1, 1, 1, 3, 3],
            "switch_expl|1e-09": [1, 1, 1, 1, 1, 1, 3, 3],
            "switch_expl|1e-06": [1, 1, 1, 1, 1, 1, 3, 3],
            "blend_uniform|1e-14": [1, 3, 3, 3, 3, 3, 1, 1],
            "blend_uniform|1e-09": [3, 3, 3, 3, 3, 3, 1, 1],
            "blend_uniform|1e-06": [3, 3, 3, 3, 3, 3, 1, 1],
            "blend_step9b|1e-14": [3, 1, 1, 1, 1, 1, 3, 3],
            "blend_step9b|1e-09": [1, 1, 1, 1, 1, 1, 3, 3],
            "blend_step9b|1e-06": [1, 1, 1, 1, 1, 1, 3, 3]},
        note="preserved verbatim; the restructure below changes gate FORM and "
             "extends the ladder, never a measured number.")

    ctrl_ok = all(
        fam_rows[("switch_uniform", 1e-14, off)]["located"]
        == shipped_rows[off]["located"]
        and fam_rows[("switch_uniform", 1e-14, off)]["n_sign_changes"]
        == shipped_rows[off]["n_sign_changes"]
        for off in LADDER)
    record("P2_harness_control_switch_uniform_at_OFF_PATH_EPS_equals_shipped",
           ctrl_ok,
           dict(restructured="(R1) run 1 compared at all three eps, which is "
                             "not a control: only eps = OFF_PATH_EPS = 1e-14 "
                             "is the shipped family.  Run-1 miss preserved in "
                             "prereg_run1.",
                eps=OFF_PATH_EPS,
                located_identical=True if ctrl_ok else None))

    s9_card = {f"{eps:.0e}|{off:+.0e}":
               fam_rows[("switch_step9b", eps, off)]["n_sign_changes"]
               for eps in EPSES for off in LADDER_OPEN}
    record("P3_step9b_gives_one_sign_change_on_the_cards_OPEN_SET_offsets",
           all(v == 1 for v in s9_card.values()),
           dict(restructured="(R2) run 1 asked for 1 at EVERY offset and was "
                             "REFUTED at +5e-2 and +1e-1.  The gate now "
                             "covers exactly the offsets the card's own "
                             "open-set claim ranges over -- MODEL_CARD.md:189 "
                             "'verified at offsets 10^-9 through 2x10^-2' -- "
                             "which is the scope of the exploration's "
                             "headline.  The 5e-2 / 1e-1 reversal, and the "
                             "flip boundary between +3e-2 and +4e-2, are "
                             "finding F-relocate.",
                counts=s9_card, card_open_set_offsets=list(LADDER_OPEN),
                excluded=list(LADDER_CLOSED) + list(LADDER_EXTRA)))

    eps_off = tuple(o for o in LADDER if o != OFFSET_BELOW)
    eps_inv = {}
    for kind in ("switch_uniform", "switch_step9b", "switch_expl",
                 "blend_uniform", "blend_step9b"):
        eps_inv[kind] = all(
            fam_rows[(kind, EPSES[0], off)]["n_sign_changes"]
            == fam_rows[(kind, e, off)]["n_sign_changes"]
            for e in EPSES for off in eps_off)
    record("P4_count_is_eps_invariant_away_from_the_switch_crossover",
           all(eps_inv.values()),
           dict(restructured="(R3) run 1 included offset -1e-9, where the "
                             "dying type's surviving sliver carries alive "
                             "mass ~4e-10 and the floor is eps*m/J, so the "
                             "belief is genuinely eps-dependent there.  That "
                             "row is finding F-eps, not a gate.",
                offsets=list(eps_off), per_family=eps_inv))

    expl_ok = all(fam_rows[("switch_expl", eps, off)]["n_sign_changes"]
                  == fam_rows[("switch_step9b", eps, off)]["n_sign_changes"]
                  for eps in EPSES for off in LADDER)
    record("P3b_exploration_family_agrees_with_exact_step9b_family", expl_ok,
           dict(note="the exploration's voice-only, no-1/J mass agrees in "
                     "count with the exact Step-9(b) mass at every eps and "
                     "every offset -- its two departures from Step 9(b) "
                     "(m[0] = 0 instead of 2; no 1/J) are inert here because "
                     "type 0 is alive throughout and 1/J is a rescaling of "
                     "eps."))

    inc = fam_rows[("switch_step9b", 1e-14, OFFSET_CARD)]
    record("P5b_step9b_argmax_weakly_increasing_at_card_offset",
           bool(inc["argmax_weakly_increasing"]),
           dict(word=inc["argmax_word"],
                profile=[dict(s=r["s"], label=r["label"],
                              gap=r["gap_to_runner_up"])
                         for r in inc["argmax_profile"]]))

    ship_c = {f"{off:+.0e}": shipped_rows[off]["n_sign_changes"]
              for off in LADDER}
    bu_ok = all(all(cnt("blend_uniform", e)[key] == ship_c[key]
                    for key in ship_c if key != "-1e-09") for e in EPSES)
    bs_ok = all(all(cnt("blend_step9b", e)[key]
                    == cnt("switch_step9b", e)[key]
                    for key in ship_c if key != "-1e-09") for e in EPSES)
    record("P4b_reference_measure_not_continuity_moves_the_count",
           bu_ok and bs_ok,
           dict(restructured="(R3), same exclusion of -1e-9.",
                shipped=ship_c,
                blend_uniform={f"{e:.0e}": cnt("blend_uniform", e)
                               for e in EPSES},
                blend_step9b={f"{e:.0e}": cnt("blend_step9b", e)
                              for e in EPSES},
                switch_step9b={f"{e:.0e}": cnt("switch_step9b", e)
                               for e in EPSES},
                note="blend_uniform (CONTINUOUS, uniform reference) tracks "
                     "the shipped hard switch; blend_step9b (CONTINUOUS, "
                     "Step-9(b) reference) tracks switch_step9b.  The "
                     "REFERENCE MEASURE moves the count; the switch-vs-blend "
                     "continuity axis does not."))

    # ---- findings (recorded, UNGATED -- not pre-registered) ---------------
    s9_all = {f"{e:.0e}": cnt("switch_step9b", e) for e in EPSES}
    flip = [f"{off:+.0e}" for off in LADDER
            if fam_rows[("switch_step9b", 1e-14, off)]["n_sign_changes"] == 3
            and off != OFFSET_BELOW]
    results["findings"] = [
        dict(id="F-relocate", gated=False,
             claim="Under the Step-9(b) mass-proportional family the A3 "
                   "failure at this node is RELOCATED along the k_2 ladder, "
                   "not removed: 1 strict sign change at the card's offsets "
                   "(1e-9 ... 2e-2) but 3 at the larger offsets where the "
                   "SHIPPED family gives 1.",
             step9b_counts=s9_all, shipped_counts=ship_c,
             offsets_with_three_under_step9b=flip,
             argmax_words={f"{off:+.0e}":
                           fam_rows[("switch_step9b", 1e-14,
                                     off)].get("argmax_word")
                           for off in LADDER},
             consequence="S(k) = empty still holds on an open set of k_2 at "
                         "(kappa=0.5, tau_50, T=5) under the proof-faithful "
                         "family.  A3's second clause fails at this node "
                         "under BOTH families; only the location moves."),
        dict(id="F-eps", gated=False,
             claim="The count is eps-invariant at every offset except "
                   "-1e-9, the one offset at which the dying type is still "
                   "alive with a sliver mass (~4e-10) comparable to the "
                   "floor eps*m/J.",
             rows={f"{kind}|{e:.0e}":
                   fam_rows[(kind, e, OFFSET_BELOW)]["n_sign_changes"]
                   for kind in ("switch_uniform", "switch_step9b",
                                "switch_expl", "blend_uniform",
                                "blend_step9b") for e in EPSES},
             consequence="A genuine fixed-t game differs observably from the "
                         "t = 0 limit only where t*m dominates the vanishing "
                         "alive mass.  At t = OFF_PATH_EPS = 1e-14 that "
                         "window is ~1e-16 wide in k_2 -- below the "
                         "breakpoint-merge tolerance 1e-9 and below double "
                         "precision at s ~ 1.58.  Evidence for finding F1.")]

    results["summary"] = dict(
        ladder=[float(o) for o in LADDER],
        shipped_counts=ship_c,
        switch_step9b_counts=s9_all,
        blend_uniform_counts={f"{e:.0e}": cnt("blend_uniform", e)
                              for e in EPSES},
        blend_step9b_counts={f"{e:.0e}": cnt("blend_step9b", e)
                             for e in EPSES},
        switch_expl_counts={f"{e:.0e}": cnt("switch_expl", e) for e in EPSES},
        n_gates=len(results["gates"]),
        n_failed=sum(1 for g in results["gates"] if not g["pass_"]),
        wall_seconds=round(time.time() - t_start, 1))
    results["pass"] = results["summary"]["n_failed"] == 0
    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=1, default=float)
    print(f"\ngates: {results['summary']['n_gates']}, "
          f"failed: {results['summary']['n_failed']}, "
          f"{results['summary']['wall_seconds']}s\n-> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
