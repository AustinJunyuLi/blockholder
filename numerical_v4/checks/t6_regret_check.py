"""Interim-regret bound at the frozen benchmark policy.

At each calibration node the record reports a certified upper bound on the
essential supremum of the one-step deviation gain R(s) = max_j U_j(s) - U_{j(s)}(s)
at benchmark prices and beliefs, over the truncated signal support.  The
certifier partitions the support at every jump of the assigned plan, of n(s)
and of the Voice clock, evaluates the three closed-form payoff branches on a
mesh of width at most 1e-5, and covers each piece by the sample maximum plus a
proved payoff-gap Lipschitz bound times half the actual mesh spacing, plus a
5e-12 arithmetic allowance.

Checks:

  t6_partition_spans_support          the unmerged breakpoint partition starts
                                      at s_lo and ends at s_hi, and the assigned
                                      plan and Voice clock are constant on the
                                      interior of every piece
  t6_closed_form_equals_plan_payoff   closed-form branch payoffs equal
                                      numerical_v4.policy.plan_payoff at sample
                                      points of every piece, to 1e-12
  t6_independent_cover                the bound recomputed at the attaining
                                      piece and at every cutoff by an independent
                                      routine (plan_payoff on the mesh, same
                                      Lipschitz cover) agrees with the recorded
                                      bound to 1e-12, and cutoff regret lies
                                      under the bound
  t6_refined_search                   a finer mesh over every piece finds a
                                      supremum at or below the bound
  t6_clocks_five_and_ten              at T = 5 and T = 10 the bound agrees with
                                      the reference table to 1e-12
  t6_full_grid                        fifteen nodes are present (five thresholds
                                      at each of T in {3, 5, 10}); not
                                      applicable on a shorter run

Deterministic: no RNG, no Monte Carlo, no network.  One pooled pass per node.
No policy solve: the frozen cutoffs and the threshold ladder are read from
numerical_v4/checks/t2_threshold_revelation_check.json.

Run:    .venv/bin/python numerical_v4/checks/t6_regret_check.py [--nodes n]
Output: numerical_v4/checks/t6_regret_check.json
"""
from __future__ import annotations

import argparse
import atexit
import json
import math
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

try:
    import numpy as np
    from scipy.special import ndtr
    from scipy.stats import norm

    from numerical_v4.menu import (  # noqa: E402
        _sigmoid_inv,
        atoms,
        b_star_inverse,
        b_star_prime,
        breakpoints,
        legal_clock,
        n_days,
    )
    from numerical_v4.params import EXIT, HOLD, VOICE, ParamsV4  # noqa: E402
    from numerical_v4.policy import engagement_cost, plan_payoff  # noqa: E402
    from numerical_v4.pooled import inner_price, pooled_pass  # noqa: E402
except ImportError:
    if __name__ == "__main__":
        raise
    np = ndtr = norm = None  # type: ignore
    _sigmoid_inv = atoms = b_star_inverse = b_star_prime = None  # type: ignore
    breakpoints = legal_clock = n_days = None  # type: ignore
    EXIT = HOLD = VOICE = ParamsV4 = None  # type: ignore
    engagement_cost = plan_payoff = inner_price = pooled_pass = None  # type: ignore

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name("t6_regret_check.json")
SOURCE_RECORD = ROOT / "numerical_v4/checks/t2_threshold_revelation_check.json"
LOCK = ROOT / ".scratch/v5-paper/runs/COMPUTE_LOCK"
OWNER = "rec-regret"
WHAT = "t6 regret check pooled passes"
PLAN_NAMES = {EXIT: "Exit", HOLD: "Hold", VOICE: "Voice"}
PLANS = (EXIT, HOLD, VOICE)
T_GRID = (3, 5, 10)

# Every point of a closed piece lies within this distance of a sample point.
TARGET_MESH_WIDTH = 1.0e-5
# Covers the final float operations and the flagged-price root error.
FLOAT_ALLOWANCE = 5.0e-12
# Finer mesh for the refined search over every piece.
REFINED_MESH_WIDTH = 1.0e-6
REFINED_CHUNK = 250_000
REFINED_MAX_SEG = 2_000_000
REFINED_LOCAL_POINTS = 4001
N_PAYOFF_SAMPLES = 60

TOL_PAYOFF = 1e-12          # closed-form branch vs plan_payoff
TOL_BOUND = 1e-12           # T = 5 and T = 10 vs the reference table
TOL_COVER = 1e-12           # independent cover vs the recorded bound
TOL_REFINED = 1e-15         # refined supremum may not exceed the bound
TOL_PARTITION = 0.0         # partition endpoints equal the support endpoints

# Reference bounds at T in {5, 10} for the five threshold-ladder nodes, in
# ladder order.  T = 3 is a stated grid extension and has no reference row.
REFERENCE_BOUNDS = {
    (5, 0): 9.623219552034791e-05,
    (5, 1): 0.0001592462568311867,
    (5, 2): 0.00018783235544278404,
    (5, 3): 0.00020784219766716692,
    (5, 4): 0.0002248763859580155,
    (10, 0): 0.00024250934252785308,
    (10, 1): 0.00024250936609786458,
    (10, 2): 0.0002425093647088392,
    (10, 3): 0.00024250936470879758,
    (10, 4): 0.00024250936470879758,
}

CONVENTION = {
    "benchmark_pass_fixed": (
        "The pooled pass is taken once at the frozen benchmark cutoffs. "
        "A one-step deviation changes only the signal and the plan, not the pass."
    ),
    "reference_belief_off_path": (
        "Prices and beliefs remain those of the benchmark pass, including on "
        "signals whose assigned plan differs from the plan being evaluated."
    ),
    "truncated_support": (
        "The bound is an essential supremum over the truncated Gaussian signal "
        "support [s_lo, s_hi]."
    ),
    "tie_rule": (
        "A signal at a cutoff is assigned the right-hand plan: Hold at the "
        "Exit-Hold cutoff, Voice at the Hold-Voice cutoff."
    ),
}

_lock_held = False


def acquire_lock() -> None:
    global _lock_held
    deadline = time.monotonic() + 45 * 60
    payload = {
        "pid": os.getpid(),
        "what": WHAT,
        "started": datetime.now(timezone.utc).isoformat(),
        "owner": OWNER,
    }
    while True:
        try:
            with LOCK.open("x") as fh:
                json.dump(payload, fh, indent=2)
                fh.write("\n")
            _lock_held = True
            atexit.register(release_lock)
            return
        except FileExistsError:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise RuntimeError(f"timed out waiting for compute lock {LOCK}")
            print(
                f"compute lock present, waiting 20s ({remaining:.0f}s left)",
                flush=True,
            )
            time.sleep(20)


def release_lock() -> None:
    global _lock_held
    if not _lock_held:
        return
    if not LOCK.exists():
        _lock_held = False
        return
    try:
        payload = json.loads(LOCK.read_text())
    except Exception:
        _lock_held = False
        return
    if payload.get("pid") == os.getpid() and payload.get("owner") == OWNER:
        LOCK.unlink()
    _lock_held = False


def assigned_plan(s: float, k: tuple[float, float]) -> int:
    return EXIT if s < k[0] else (HOLD if s < k[1] else VOICE)


def complete_breakpoints(k: tuple[float, float], p: ParamsV4) -> np.ndarray:
    """Every theoretical jump point, without menu.py's 1e-9 merge.

    Candidates outside [s_lo, s_hi] are dropped, so the partition cannot
    extend past the support.
    """
    pts = [p.s_lo, p.s_hi, *[float(x) for x in k if p.s_lo < x < p.s_hi]]
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            x = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo <= x <= p.s_hi:
                pts.append(float(x))
    for n in range(1, p.H + 2):
        for d in range(p.H + 1):
            y = p.b0 + (p.tau - p.b0) * n / min(d + 1, n)
            if p.b0 < y < p.b_bar:
                x = b_star_inverse(y, p)
                if math.isfinite(x) and p.s_lo <= x <= p.s_hi:
                    pts.append(float(x))
    return np.asarray(sorted(set(float(x) for x in pts)), dtype=float)


def voice_signature(s: float, p: ParamsV4) -> tuple:
    cl = legal_clock(VOICE, s, p)
    return n_days(s, p), cl.c, cl.f, cl.D


def b_values(s: np.ndarray, p: ParamsV4) -> tuple[np.ndarray, np.ndarray]:
    x = (s - p.mu_v) / p.sigma_s
    b = p.b0 + (p.b_bar - p.b0) * 0.5 * (1.0 + x / np.sqrt(1.0 + x * x))
    bp = 0.5 * (p.b_bar - p.b0) * (1.0 + x * x) ** -1.5 / p.sigma_s
    return b, bp


def max_bprime(lo: float, hi: float, p: ParamsV4) -> float:
    near = min(max(p.mu_v, lo), hi)
    return float(b_star_prime(near, p))


def smooth_branch(j: int, mid: float, lo: float, hi: float, res, p: ParamsV4):
    """Return a closure-piece payoff evaluator and a proved derivative bound."""
    if j == EXIT:
        value = float(p.b0 * res.EP[0][0])

        def evaluate(s: np.ndarray) -> tuple[np.ndarray, float]:
            return np.full_like(s, value, dtype=float), 0.0

        return evaluate, 0.0, {"kind": "constant", "theta": 0}

    if j == HOLD:
        Ep = float(res.Ep_bid[0])
        EpP = float(res.EpP[0])
        slope = p.b0 * (1.0 - Ep) * p.beta

        def evaluate(s: np.ndarray) -> tuple[np.ndarray, float]:
            vh = p.mu_v + p.beta * (s - p.mu_v)
            ey = (1.0 - Ep) * vh + EpP + Ep * p.m0
            return p.b0 * ey, 0.0

        return evaluate, abs(float(slope)), {
            "kind": "linear", "theta": 0, "Ep_bid": Ep, "EpP": EpP
        }

    n = n_days(mid, p)
    cl = legal_clock(VOICE, mid, p)
    bp_max = max_bprime(lo, hi, p)
    lam = p.chi / p.sigma_s
    c_max = engagement_cost(lo, p)

    if cl.D == 0:
        Ep = float(res.Ep_bid[n])
        EpP = float(res.EpP[n])
        q = (1.0 - Ep) * p.beta
        exec_price = float(sum(res.EP[d][n] for d in range(n)) / n)

        def ey_at(x: float) -> float:
            vh = p.mu_v + p.beta * (x - p.mu_v)
            return float((1.0 - Ep) * (vh + p.Delta_V) + EpP + Ep * p.m1)

        ey_abs = max(abs(ey_at(lo) - exec_price), abs(ey_at(hi) - exec_price))
        lipschitz = bp_max * ey_abs + p.b_bar * abs(q) + lam * c_max

        def evaluate(s: np.ndarray) -> tuple[np.ndarray, float]:
            b, _ = b_values(s, p)
            vh = p.mu_v + p.beta * (s - p.mu_v)
            ey = (1.0 - Ep) * (vh + p.Delta_V) + EpP + Ep * p.m1
            u = b * ey - (b - p.b0) * exec_price
            u -= p.C0 * np.exp(-p.chi * (s - p.mu_v) / p.sigma_s)
            return u, 0.0

        return evaluate, float(lipschitz), {
            "kind": "Voice pooled", "theta": n, "D": 0,
            "execution_price_average": exec_price, "Ep_bid": Ep, "EpP": EpP,
        }

    if not (p.m1 > 0.0):
        raise RuntimeError("flagged price derivative bound needs m1 > 0")

    f = int(cl.f)
    r = min(1.0, (f + 1.0) / n)
    exec_coeff = float(sum(res.EP[d][n] for d in range(min(f, n - 1) + 1)) / n)
    v_min = p.mu_v + p.beta * (lo - p.mu_v) + p.Delta_V
    v_max = p.mu_v + p.beta * (hi - p.mu_v) + p.Delta_V
    pb_vmin = float(1.0 - ndtr((v_min + p.K + p.m1 - p.S_bar) / p.sigma_xi))
    one_minus = max(1.0 - pb_vmin, np.finfo(float).tiny)
    p_upper = v_max + p.m1 * pb_vmin / one_minus
    p_abs = max(abs(v_min), abs(p_upper))
    # At pi=1, implicit differentiation gives 0 <= dP/ds = beta*(1-p)/g_P <= beta.
    # The |P_F| bound takes the base from v_max and the tail factor from v_min.
    lipschitz = bp_max * (r * p_abs + abs(exec_coeff))
    lipschitz += p.b_bar * p.beta + lam * c_max

    def evaluate(s: np.ndarray) -> tuple[np.ndarray, float]:
        b, _ = b_values(s, p)
        vh = p.mu_v + p.beta * (s - p.mu_v)
        sol = inner_price(vh, np.ones_like(vh), p)
        bf = p.b0 + r * (b - p.b0)
        u = bf * sol.P - exec_coeff * (b - p.b0)
        u -= p.C0 * np.exp(-p.chi * (s - p.mu_v) / p.sigma_s)
        return u, float(sol.max_residual)

    return evaluate, float(lipschitz), {
        "kind": "Voice flagged", "theta": n, "D": 1, "c": cl.c, "f": cl.f,
        "stake_fraction_at_filing": r, "execution_price_coefficient": exec_coeff,
        "flagged_price_absolute_bound": p_abs,
    }


def interval_mass(lo: float, hi: float, p: ParamsV4) -> float:
    zlo = (lo - p.mu_v) / p.sigma_s
    zhi = (hi - p.mu_v) / p.sigma_s
    den = norm.cdf(p.s_span) - norm.cdf(-p.s_span)
    return float((norm.cdf(zhi) - norm.cdf(zlo)) / den)


def cutoff_payoffs(k: tuple[float, float], res, p: ParamsV4) -> list[dict]:
    out = []
    for which, s, assigned in (("Exit-Hold", k[0], HOLD), ("Hold-Voice", k[1], VOICE)):
        vals = {PLAN_NAMES[j]: float(plan_payoff(j, s, res, p)) for j in PLANS}
        out.append({
            "cutoff": which, "s": s, "assigned_plan": PLAN_NAMES[assigned],
            "assigned_payoff": vals[PLAN_NAMES[assigned]], "all_payoffs": vals,
        })
    return out


def piece_gap_cover(values: dict, assigned: int, lip: dict,
                    cover_radius: float) -> tuple[list[dict], float, float]:
    alt_rows = []
    for alt in PLANS:
        if alt == assigned:
            continue
        gap = values[alt] - values[assigned]
        imax = int(np.argmax(gap))
        sample_max = float(gap[imax])
        Lgap = float(lip[alt] + lip[assigned])
        upper = sample_max + Lgap * cover_radius + FLOAT_ALLOWANCE
        alt_rows.append({
            "alternative_plan": PLAN_NAMES[alt],
            "sample_max_gap": sample_max,
            "sample_argmax": None,  # filled by the caller who has the grid
            "argmax_index": imax,
            "gap_lipschitz_bound": Lgap,
            "certified_upper": float(upper),
        })
    alt_rows.sort(key=lambda row: row["certified_upper"], reverse=True)
    piece_bound = max(0.0, alt_rows[0]["certified_upper"])
    sample_regret = max(0.0, max(row["sample_max_gap"] for row in alt_rows))
    return alt_rows, piece_bound, sample_regret


def independent_cover_on_piece(lo: float, hi: float, assigned: int, lip: dict,
                               res, p: ParamsV4) -> tuple[float, float]:
    """Cover the piece using plan_payoff on the certification mesh."""
    nseg = max(1, int(math.ceil((hi - lo) / TARGET_MESH_WIDTH)))
    sgrid = np.linspace(lo, hi, nseg + 1, dtype=float)
    values = {}
    for j in PLANS:
        values[j] = np.array(
            [float(plan_payoff(j, float(s), res, p)) for s in sgrid],
            dtype=float,
        )
    cover_radius = 0.5 * (hi - lo) / nseg
    alt_rows, piece_bound, sample_regret = piece_gap_cover(
        values, assigned, lip, cover_radius
    )
    del alt_rows
    return float(piece_bound), float(sample_regret)


def refined_supremum(lo: float, hi: float, assigned: int, branches: dict) -> tuple[float, float]:
    """Finer mesh over the piece, with a local refinement around the argmax."""
    span = hi - lo
    if not (span > 0.0):
        s = np.array([lo], dtype=float)
        va = branches[assigned](s)[0]
        best = -1e9
        for alt in PLANS:
            if alt == assigned:
                continue
            best = max(best, float((branches[alt](s)[0] - va)[0]))
        return float(best), float(lo)
    target = max(1, int(math.ceil(span / REFINED_MESH_WIDTH)))
    nseg = min(target, REFINED_MAX_SEG)
    best, arg = -1e9, lo
    for c0 in range(0, nseg + 1, REFINED_CHUNK):
        c1 = min(nseg, c0 + REFINED_CHUNK - 1)
        gg = lo + span * (np.arange(c0, c1 + 1) / nseg)
        va = branches[assigned](gg)[0]
        r = np.full(gg.shape, -1e9)
        for alt in PLANS:
            if alt == assigned:
                continue
            r = np.maximum(r, branches[alt](gg)[0] - va)
        i = int(np.argmax(r))
        if float(r[i]) > best:
            best, arg = float(r[i]), float(gg[i])
    w = 4.0 * span / nseg
    for _ in range(4):
        gg = np.linspace(max(lo, arg - w), min(hi, arg + w), REFINED_LOCAL_POINTS)
        va = branches[assigned](gg)[0]
        r = np.full(gg.shape, -1e9)
        for alt in PLANS:
            if alt == assigned:
                continue
            r = np.maximum(r, branches[alt](gg)[0] - va)
        i = int(np.argmax(r))
        if float(r[i]) > best:
            best, arg = float(r[i]), float(gg[i])
        w *= 0.02
    return float(best), float(arg)


def certify_node(node: int, T: int, tau: float, tau_index: int,
                 tau_quantile: float, k: tuple[float, float],
                 p0: ParamsV4) -> tuple[dict, dict]:
    started = time.perf_counter()
    p = p0.replace(tau=float(tau), T=int(T), kappa=0.5, mark=2, H=10)
    al = atoms(k, p)
    pooled_started = time.perf_counter()
    res = pooled_pass(al, p, with_runup=True)
    pooled_seconds = time.perf_counter() - pooled_started
    menu_bps = breakpoints(k, p)
    bps = complete_breakpoints(k, p)
    if not set(menu_bps).issubset(set(bps)):
        raise RuntimeError("complete breakpoint set lost a menu breakpoint")
    pieces = []
    max_flagged_root_residual = 0.0
    closed_form_max_diff = 0.0
    refined_max = -1e9
    refined_arg = float(bps[0])
    sample_frac = np.linspace(0.0, 1.0, N_PAYOFF_SAMPLES + 2)[1:-1]

    for piece_index, (lo0, hi0) in enumerate(zip(bps[:-1], bps[1:]), start=1):
        lo, hi = float(lo0), float(hi0)
        mid = lo + 0.5 * (hi - lo)
        if not (lo < mid < hi):
            mid = float(np.nextafter(lo, hi))
        assigned = assigned_plan(mid, k)
        for frac in (0.1, 0.9):
            probe = lo + frac * (hi - lo)
            probe_assigned = assigned_plan(probe, k)
            if (probe_assigned != assigned
                    or voice_signature(probe, p) != voice_signature(mid, p)):
                raise RuntimeError(f"incomplete breakpoint partition on [{lo}, {hi}]")
        branches = {}
        lip = {}
        branch_meta = {}
        for j in PLANS:
            branches[j], lip[j], branch_meta[j] = smooth_branch(j, mid, lo, hi, res, p)

        nseg = max(1, int(math.ceil((hi - lo) / TARGET_MESH_WIDTH)))
        sgrid = np.linspace(lo, hi, nseg + 1, dtype=float)
        values = {}
        for j in PLANS:
            values[j], root_resid = branches[j](sgrid)
            max_flagged_root_residual = max(max_flagged_root_residual, root_resid)

        cover_radius = 0.5 * (hi - lo) / nseg
        alt_rows, piece_bound, sample_regret = piece_gap_cover(
            values, assigned, lip, cover_radius
        )
        for row in alt_rows:
            row["sample_argmax"] = float(sgrid[row.pop("argmax_index")])

        ss = lo + sample_frac * (hi - lo)
        for j in PLANS:
            branch_vals, _ = branches[j](ss)
            for s, v in zip(ss, branch_vals):
                d = abs(float(v) - float(plan_payoff(j, float(s), res, p)))
                if d > closed_form_max_diff:
                    closed_form_max_diff = d

        dense, darg = refined_supremum(lo, hi, assigned, branches)
        if dense > refined_max:
            refined_max, refined_arg = dense, darg

        pieces.append({
            "piece": piece_index, "lo": lo, "hi": hi, "prior_mass": interval_mass(lo, hi, p),
            "assigned_plan": PLAN_NAMES[assigned],
            "assigned": assigned,
            "lip": lip,
            "alternative_plan": alt_rows[0]["alternative_plan"],
            "possible_profitable_alternatives": [
                row["alternative_plan"] for row in alt_rows if row["certified_upper"] > 0.0
            ],
            "positive_sample_witness": bool(sample_regret > FLOAT_ALLOWANCE),
            "sample_max_regret": float(sample_regret),
            "bound": float(piece_bound),
            "mesh_segments": nseg,
            "cover_radius": float(cover_radius),
            "alternatives": alt_rows,
            "branch_metadata": {PLAN_NAMES[j]: branch_meta[j] for j in PLANS},
            "attaining_signal": float(alt_rows[0]["sample_argmax"]),
        })

    positive = []
    for row in pieces:
        if row["bound"] > 0.0:
            positive.append({kk: v for kk, v in row.items()
                             if kk not in ("assigned", "lip")})
    attaining = max(pieces, key=lambda row: row["bound"])
    cut_levels = cutoff_payoffs(k, res, p)
    voice_cutoff = next(c for c in cut_levels if c["cutoff"] == "Hold-Voice")
    normaliser = float(voice_cutoff["assigned_payoff"])
    if not (normaliser > 0.0):
        raise RuntimeError("Hold-Voice assigned payoff is not a positive scale")

    ind_cover, _ = independent_cover_on_piece(
        attaining["lo"], attaining["hi"], attaining["assigned"], attaining["lip"],
        res, p,
    )
    cutoff_rows = []
    cutoff_regret_max = 0.0
    for row in cut_levels:
        s = float(row["s"])
        assigned = assigned_plan(s, k)
        ua = {j: float(plan_payoff(j, s, res, p)) for j in PLANS}
        regret = max(ua.values()) - ua[assigned]
        cutoff_regret_max = max(cutoff_regret_max, regret)
        recorded = float(row["all_payoffs"][PLAN_NAMES[assigned]])
        cutoff_rows.append({
            "cutoff": row["cutoff"], "s": s,
            "regret": float(regret),
            "assigned_payoff_plan_payoff": ua[assigned],
            "assigned_payoff_recorded": recorded,
            "payoff_diff": abs(ua[assigned] - recorded),
        })

    node_seconds = time.perf_counter() - started
    node_record = {
        "node": node, "T": T, "tau": tau, "tau_index": tau_index,
        "tau_quantile": tau_quantile, "kappa": p.kappa, "mark": p.mark, "H": p.H,
        "node_params_hash": p.hash_str(), "bound": attaining["bound"],
        "attaining_signal": attaining["attaining_signal"],
        "attaining_piece": {
            "piece": attaining["piece"], "lo": attaining["lo"], "hi": attaining["hi"],
            "prior_mass": attaining["prior_mass"],
            "assigned_plan": attaining["assigned_plan"],
            "alternative_plan": attaining["alternative_plan"],
            "attaining_signal": attaining["attaining_signal"],
        },
        "positive_regret_pieces": positive,
        "cutoff_payoff_levels": cut_levels,
        "n_breakpoint_pieces": len(pieces),
        "n_menu_breakpoint_pieces": len(menu_bps) - 1,
        "mesh_width": TARGET_MESH_WIDTH,
        "allowance": FLOAT_ALLOWANCE,
        "normaliser": normaliser,
        "normaliser_definition": (
            "the assigned Voice payoff at the Hold-Voice cutoff, the payoff "
            "scale of the benchmark at that cutoff"
        ),
        "bound_share": float(attaining["bound"] / normaliser),
        "pooled_seconds": pooled_seconds,
        "certification_seconds": node_seconds - pooled_seconds,
        "wall_seconds": node_seconds,
        "pooled_max_price_residual": res.max_price_residual,
        "certifier_max_flagged_root_residual": max_flagged_root_residual,
    }
    node_checks = {
        "T": T, "tau_index": tau_index,
        "partition_lo": float(bps[0]), "partition_hi": float(bps[-1]),
        "s_lo": float(p.s_lo), "s_hi": float(p.s_hi),
        "n_pieces": len(pieces),
        "closed_form_max_diff": float(closed_form_max_diff),
        "independent_attaining_cover": float(ind_cover),
        "recorded_bound": float(attaining["bound"]),
        "cover_diff": abs(float(ind_cover) - float(attaining["bound"])),
        "cutoff_regret_max": float(cutoff_regret_max),
        "cutoff_payoff_max_diff": max(r["payoff_diff"] for r in cutoff_rows),
        "cutoff_rows": cutoff_rows,
        "refined_sup": float(refined_max),
        "refined_arg": float(refined_arg),
        "refined_minus_bound": float(refined_max - attaining["bound"]),
    }
    return node_record, node_checks


def _sci(x: float) -> str:
    return f"{float(x):.1e}"


def _pct_share(share: float) -> str:
    return f"{100.0 * float(share):.2f} percent"


def render(record: dict) -> dict[str, str]:
    """Manuscript strings.  Deterministic; uses whatever nodes the record holds."""
    prov = record.get("provenance") or {}
    t_grid = list(prov.get("T_grid") or [])
    taus = list(prov.get("tau_ladder") or [])
    n_design = (len(t_grid) * len(taus)) if t_grid and taus else 0
    method = record.get("method") or {}
    mesh = method.get("target_mesh_width", TARGET_MESH_WIDTH)
    if abs(float(mesh) - 1.0e-5) < 1e-18:
        mesh_s = "1e-5"
    else:
        mesh_s = f"{float(mesh):g}"
    out = {
        "n_nodes": str(n_design if n_design else len(record.get("nodes") or [])),
        "mesh_width": mesh_s,
    }
    nodes = list(record.get("nodes") or [])
    if not nodes:
        return out
    top = max(nodes, key=lambda n: float(n["bound"]))
    out["largest_bound"] = _sci(top["bound"])
    t510 = [n for n in nodes if int(n["T"]) in (5, 10)]
    if t510:
        top510 = max(t510, key=lambda n: float(n["bound"]))
        out["largest_bound_T5_T10"] = _sci(top510["bound"])
    share = top.get("bound_share")
    if share is None and top.get("normaliser"):
        share = float(top["bound"]) / float(top["normaliser"])
    if share is not None:
        out["largest_bound_share_of_normaliser"] = _pct_share(share)
    if top.get("normaliser") is not None:
        out["normaliser"] = f"{float(top['normaliser']):.3f}"
    return out


def write_record(record: dict) -> None:
    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(record, indent=2, default=float) + "\n")
    tmp.replace(OUT)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--nodes", type=int, default=None,
                    help="limit the run to the first n threshold-ladder nodes")
    args = ap.parse_args()

    t0 = time.perf_counter()
    source = json.loads(SOURCE_RECORD.read_text())
    provenance = source["provenance"]
    k = tuple(float(x) for x in provenance["frozen_k"])
    taus = [float(x) for x in provenance["tau_ladder"]]
    quantiles = [float(x) for x in provenance["tau_quantiles"]]
    if len(taus) != len(quantiles):
        raise RuntimeError("tau_ladder and tau_quantiles differ in length")
    if provenance["mark"] != 2 or provenance["H"] != 10:
        raise RuntimeError("the frozen provenance is not mark 2, H 10")
    p0 = ParamsV4.baseline()
    med_i = quantiles.index(0.5)
    p_med = p0.replace(tau=float(taus[med_i]))
    if p_med.hash_str() != provenance["params_hash"]:
        raise RuntimeError(
            f"params hash {p_med.hash_str()} != provenance {provenance['params_hash']}"
        )

    threshold_nodes = list(zip(quantiles, taus))
    n_threshold_all = len(threshold_nodes)
    if args.nodes is not None:
        threshold_nodes = threshold_nodes[: args.nodes]

    n_fail = 0
    checks: dict = {}

    def add_check(name: str, ok, **detail) -> None:
        nonlocal n_fail
        if ok == "na":
            checks[name] = {"pass": False, "status": "not_applicable", **detail}
            print(f"[N/A ] {name}", flush=True)
            return
        checks[name] = {"pass": bool(ok), **detail}
        if not ok:
            n_fail += 1
        print(f"[{'PASS' if ok else 'FAIL'}] {name}", flush=True)

    node_records = []
    node_checks = []
    acquire_lock()
    try:
        for T in T_GRID:
            for tau_index, (qi, tau) in enumerate(threshold_nodes):
                node_id = T_GRID.index(T) * n_threshold_all + tau_index + 1
                print(
                    f"node {node_id}: T={T}, q={qi:.1f}, tau={tau:.17g}",
                    flush=True,
                )
                rec, chk = certify_node(
                    node_id, T, tau, tau_index, qi, k, p0
                )
                node_records.append(rec)
                node_checks.append(chk)
                print(
                    f"  bound={rec['bound']:.9g} share={rec['bound_share']:.6g} "
                    f"wall={rec['wall_seconds']:.1f}s",
                    flush=True,
                )
    finally:
        release_lock()

    max_end = max(
        max(abs(c["partition_lo"] - c["s_lo"]), abs(c["partition_hi"] - c["s_hi"]))
        for c in node_checks
    )
    add_check(
        "t6_partition_spans_support",
        max_end <= TOL_PARTITION,
        request=(
            "the unmerged breakpoint partition starts at s_lo and ends at s_hi "
            "at every node"
        ),
        tol=TOL_PARTITION,
        max_endpoint_gap=max_end,
        rows=[{
            "T": c["T"], "tau_index": c["tau_index"], "n_pieces": c["n_pieces"],
            "partition_lo": c["partition_lo"], "partition_hi": c["partition_hi"],
            "s_lo": c["s_lo"], "s_hi": c["s_hi"],
        } for c in node_checks],
    )

    max_payoff = max(c["closed_form_max_diff"] for c in node_checks)
    add_check(
        "t6_closed_form_equals_plan_payoff",
        max_payoff < TOL_PAYOFF,
        request=(
            "closed-form branch payoffs equal plan_payoff at "
            f"{N_PAYOFF_SAMPLES} interior points of every piece, all three plans"
        ),
        tol=TOL_PAYOFF,
        max_abs_diff=max_payoff,
        n_sample_points_per_piece=N_PAYOFF_SAMPLES,
        rows=[{
            "T": c["T"], "tau_index": c["tau_index"],
            "closed_form_max_diff": c["closed_form_max_diff"],
        } for c in node_checks],
    )

    max_cover = max(c["cover_diff"] for c in node_checks)
    max_cut_regret_gap = max(
        c["cutoff_regret_max"] - r["bound"]
        for c, r in zip(node_checks, node_records)
    )
    max_cut_pay = max(c["cutoff_payoff_max_diff"] for c in node_checks)
    cover_ok = (
        max_cover < TOL_COVER
        and max_cut_regret_gap <= TOL_COVER
        and max_cut_pay < TOL_PAYOFF
    )
    add_check(
        "t6_independent_cover",
        cover_ok,
        request=(
            "the Lipschitz cover recomputed from plan_payoff at the attaining "
            "piece agrees with the recorded bound to 1e-12, cutoff regret lies "
            "under the bound, and cutoff assigned payoffs match plan_payoff"
        ),
        tol_cover=TOL_COVER,
        tol_payoff=TOL_PAYOFF,
        max_cover_diff=max_cover,
        max_cutoff_regret_minus_bound=max_cut_regret_gap,
        max_cutoff_payoff_diff=max_cut_pay,
        rows=[{
            "T": c["T"], "tau_index": c["tau_index"],
            "independent_attaining_cover": c["independent_attaining_cover"],
            "recorded_bound": c["recorded_bound"],
            "cover_diff": c["cover_diff"],
            "cutoff_regret_max": c["cutoff_regret_max"],
            "cutoff_payoff_max_diff": c["cutoff_payoff_max_diff"],
        } for c in node_checks],
    )

    max_refined_over = max(c["refined_minus_bound"] for c in node_checks)
    add_check(
        "t6_refined_search",
        max_refined_over <= TOL_REFINED,
        request=(
            "a mesh of width 1e-6 over every piece, refined locally around the "
            "argmax, finds a supremum at or below the certified bound"
        ),
        tol=TOL_REFINED,
        refined_mesh_width=REFINED_MESH_WIDTH,
        max_refined_minus_bound=max_refined_over,
        rows=[{
            "T": c["T"], "tau_index": c["tau_index"],
            "refined_sup": c["refined_sup"],
            "refined_arg": c["refined_arg"],
            "bound": c["recorded_bound"],
            "refined_minus_bound": c["refined_minus_bound"],
        } for c in node_checks],
    )

    ref_rows = []
    ref_ok = True
    for rec in node_records:
        key = (int(rec["T"]), int(rec["tau_index"]))
        if key not in REFERENCE_BOUNDS:
            continue
        want = REFERENCE_BOUNDS[key]
        got = float(rec["bound"])
        diff = abs(got - want)
        ref_rows.append({
            "T": rec["T"], "tau_index": rec["tau_index"], "tau": rec["tau"],
            "bound": got, "reference_bound": want, "abs_diff": diff,
        })
        if diff >= TOL_BOUND:
            ref_ok = False
    if not ref_rows:
        add_check(
            "t6_clocks_five_and_ten",
            "na",
            request=(
                "at T = 5 and T = 10 the certified bound agrees with the "
                "reference table to 1e-12"
            ),
            reason="no T = 5 or T = 10 node was run",
        )
    else:
        add_check(
            "t6_clocks_five_and_ten",
            ref_ok,
            request=(
                "at T = 5 and T = 10 the certified bound agrees with the "
                "reference table to 1e-12"
            ),
            tol=TOL_BOUND,
            n_compared=len(ref_rows),
            max_abs_diff=max(r["abs_diff"] for r in ref_rows),
            rows=ref_rows,
        )

    n_expected = len(T_GRID) * n_threshold_all
    if len(node_records) == n_expected:
        add_check(
            "t6_full_grid",
            True,
            request="fifteen nodes, five thresholds at each of T in {3, 5, 10}",
            n_nodes=len(node_records),
            n_expected=n_expected,
        )
    else:
        add_check(
            "t6_full_grid",
            "na",
            request="fifteen nodes, five thresholds at each of T in {3, 5, 10}",
            reason=(
                f"the record contains {len(node_records)} of {n_expected} nodes"
            ),
            n_nodes=len(node_records),
            n_expected=n_expected,
        )

    record = {
        "checks": checks,
        "n_fail": n_fail,
        "all_pass": n_fail == 0,
        "convention": CONVENTION,
        "method": {
            "name": "breakpoint pieces with a proved Lipschitz cover",
            "breakpoints": (
                "the full unmerged candidate set underlying "
                "numerical_v4.menu.breakpoints at the frozen benchmark cutoffs, "
                "restricted to the signal support"
            ),
            "target_mesh_width": TARGET_MESH_WIDTH,
            "float_allowance": FLOAT_ALLOWANCE,
            "cover": (
                "sample maximum plus the payoff-gap Lipschitz bound times half "
                "the actual mesh width, plus float allowance"
            ),
            "derivatives": (
                "analytic on each piece; the flagged price uses implicit "
                "differentiation and 0 <= dP_F/ds <= beta, with the |P_F| bound "
                "taking the base from v_max and the tail factor from v_min"
            ),
            "positive_piece_rule": (
                "all pieces with a positive certified upper bound are reported; "
                "positive_sample_witness distinguishes a computed profitable "
                "type from a conservative endpoint allowance"
            ),
            "normaliser": (
                "the assigned Voice payoff at the Hold-Voice cutoff of the node"
            ),
        },
        "provenance": {
            "script": "numerical_v4/checks/t6_regret_check.py",
            "params_hash": provenance["params_hash"],
            "mark": int(provenance["mark"]),
            "H": int(provenance["H"]),
            "frozen_k": [float(x) for x in k],
            "cutoff_scale": float(provenance["cutoff_scale"]),
            "payoff_scale": float(provenance["payoff_scale"]),
            "tau_ladder": list(taus),
            "tau_quantiles": list(quantiles),
            "T_grid": list(T_GRID),
            "kappa_grid": provenance.get("kappa_grid", {
                "lo": 0.15, "hi": 0.85, "n": 71, "step": 0.01,
            }),
            "measurement": (
                "certified upper bound on the essential supremum of the "
                "one-step deviation gain at benchmark prices and beliefs over "
                "the truncated signal support, evaluated at kappa = 0.5; the "
                "share is that bound divided by the assigned Voice payoff at "
                "the Hold-Voice cutoff"
            ),
            "nodes_run": (len(threshold_nodes) if args.nodes is not None else "all"),
        },
        "nodes": node_records,
        "seconds": time.perf_counter() - t0,
        "n_nodes_run": len(node_records),
    }
    write_record(record)
    rendered = render(record)
    print(
        f"\n{'ALL PASS' if record['all_pass'] else str(n_fail) + ' FAIL'}"
        f"  in {record['seconds']:.1f}s  ({len(node_records)} node(s))  ->  {OUT}",
        flush=True,
    )
    print("render: " + json.dumps(rendered), flush=True)
    return 0 if record["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
