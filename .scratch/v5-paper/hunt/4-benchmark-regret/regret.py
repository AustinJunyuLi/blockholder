"""Certified interim-regret bounds for the frozen benchmark policy.

Run from the repository root:

    PYTHONPATH=. .venv/bin/python \
      .scratch/v5-paper/hunt/4-benchmark-regret/regret.py

The script takes the repository compute lock for all ten pooled passes and writes
``regret.json`` only after every node has completed.
"""
from __future__ import annotations

import json
import math
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.special import ndtr
from scipy.stats import norm

from numerical_v4.flagged import flagged_price_at, inner_price
from numerical_v4.menu import (
    _sigmoid_inv, atoms, b_star, b_star_inverse, b_star_prime, breakpoints,
    legal_clock, n_days,
)
from numerical_v4.params import EXIT, HOLD, VOICE, ParamsV4
from numerical_v4.policy import engagement_cost, plan_payoff
from numerical_v4.pooled import pooled_pass

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).with_name("regret.json")
SOURCE_RECORD = ROOT / "numerical_v4/checks/t2_threshold_revelation_check.json"
LOCK = ROOT / ".scratch/v5-paper/runs/COMPUTE_LOCK"
OWNER = "4-benchmark-regret"
WHAT = "hunt 4 regret record, ten pooled passes"
PLAN_NAMES = {EXIT: "Exit", HOLD: "Hold", VOICE: "Voice"}

# Every point of a closed piece lies within this distance of a sample point.
TARGET_MESH_WIDTH = 1.0e-5
# Covers the final float operations and the flagged-price root error.  The
# record also reports the observed root residual at every node.
FLOAT_ALLOWANCE = 5.0e-12


def acquire_lock() -> None:
    if LOCK.exists():
        raise RuntimeError(f"compute lock exists: {LOCK}")
    proc = subprocess.run(
        ["pgrep", "-f", "numerical_v4"], capture_output=True, text=True, check=False
    )
    if proc.returncode == 0 and proc.stdout.strip():
        raise RuntimeError(f"numerical_v4 process is running: {proc.stdout.strip()}")
    payload = {
        "pid": os.getpid(),
        "what": WHAT,
        "started": datetime.now(timezone.utc).isoformat(),
        "owner": OWNER,
    }
    # Exclusive creation closes the race between the existence check and write.
    with LOCK.open("x") as fh:
        json.dump(payload, fh, indent=2)
        fh.write("\n")


def release_lock() -> None:
    if not LOCK.exists():
        return
    try:
        payload = json.loads(LOCK.read_text())
    except Exception:
        return
    if payload.get("pid") == os.getpid() and payload.get("owner") == OWNER:
        LOCK.unlink()




def complete_breakpoints(k: tuple[float, float], p: ParamsV4) -> np.ndarray:
    """Return every theoretical jump point, without menu.py's 1e-9 merge.

    ``menu.breakpoints`` is the source set.  It merges near duplicates to keep
    quadrature atoms stable.  Regret certification instead keeps every distinct
    float candidate, so a narrow branch cannot disappear in that merge.
    """
    pts = [p.s_lo, p.s_hi, *[float(x) for x in k if p.s_lo < x < p.s_hi]]
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            pts.append(p.mu_v + p.sigma_s * _sigmoid_inv(g))
    for n in range(1, p.H + 2):
        for d in range(p.H + 1):
            y = p.b0 + (p.tau - p.b0) * n / min(d + 1, n)
            if p.b0 < y < p.b_bar:
                x = b_star_inverse(y, p)
                if math.isfinite(x) and p.s_lo <= x <= p.s_hi:
                    pts.append(float(x))
    # A set removes exact duplicates only.  No positive-width candidate interval
    # is discarded.
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

    f = int(cl.f)
    r = min(1.0, (f + 1.0) / n)
    exec_coeff = float(sum(res.EP[d][n] for d in range(min(f, n - 1) + 1)) / n)
    v_min = p.mu_v + p.beta * (lo - p.mu_v) + p.Delta_V
    v_max = p.mu_v + p.beta * (hi - p.mu_v) + p.Delta_V
    pb_vmin = float(1.0 - ndtr((v_min + p.K + p.m1 - p.S_bar) / p.sigma_xi))
    one_minus = max(1.0 - pb_vmin, np.finfo(float).tiny)
    p_upper = v_max + p.m1 * pb_vmin / one_minus
    p_abs = max(abs(v_min), abs(p_upper))
    # At pi=1, implicit differentiation gives
    # 0 <= dP/ds = beta*(1-p)/g_P <= beta.
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
        vals = {PLAN_NAMES[j]: float(plan_payoff(j, s, res, p)) for j in (EXIT, HOLD, VOICE)}
        out.append({
            "cutoff": which, "s": s, "assigned_plan": PLAN_NAMES[assigned],
            "assigned_payoff": vals[PLAN_NAMES[assigned]], "all_payoffs": vals,
        })
    return out


def certify_node(node: int, T: int, tau: float, k: tuple[float, float], p0: ParamsV4) -> dict:
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

    for piece_index, (lo0, hi0) in enumerate(zip(bps[:-1], bps[1:]), start=1):
        lo, hi = float(lo0), float(hi0)
        mid = lo + 0.5 * (hi - lo)
        if not (lo < mid < hi):
            # There is no representable interior float.  Use the one-sided
            # branch.  Its closure still covers the mathematical sliver.
            mid = float(np.nextafter(lo, hi))
        assigned = EXIT if mid < k[0] else (HOLD if mid < k[1] else VOICE)
        for frac in (0.1, 0.9):
            probe = lo + frac * (hi - lo)
            probe_assigned = EXIT if probe < k[0] else (HOLD if probe < k[1] else VOICE)
            if probe_assigned != assigned or voice_signature(probe, p) != voice_signature(mid, p):
                raise RuntimeError(f"incomplete breakpoint partition on [{lo}, {hi}]")
        branches = {}
        lip = {}
        branch_meta = {}
        for j in (EXIT, HOLD, VOICE):
            branches[j], lip[j], branch_meta[j] = smooth_branch(j, mid, lo, hi, res, p)

        nseg = max(1, int(math.ceil((hi - lo) / TARGET_MESH_WIDTH)))
        sgrid = np.linspace(lo, hi, nseg + 1, dtype=float)
        values = {}
        for j in (EXIT, HOLD, VOICE):
            values[j], root_resid = branches[j](sgrid)
            max_flagged_root_residual = max(max_flagged_root_residual, root_resid)

        alt_rows = []
        for alt in (EXIT, HOLD, VOICE):
            if alt == assigned:
                continue
            gap = values[alt] - values[assigned]
            imax = int(np.argmax(gap))
            sample_max = float(gap[imax])
            cover_radius = 0.5 * (hi - lo) / nseg
            Lgap = float(lip[alt] + lip[assigned])
            upper = sample_max + Lgap * cover_radius + FLOAT_ALLOWANCE
            alt_rows.append({
                "alternative_plan": PLAN_NAMES[alt],
                "sample_max_gap": sample_max,
                "sample_argmax": float(sgrid[imax]),
                "gap_lipschitz_bound": Lgap,
                "certified_upper": float(upper),
            })
        alt_rows.sort(key=lambda row: row["certified_upper"], reverse=True)
        piece_bound = max(0.0, alt_rows[0]["certified_upper"])
        sample_regret = max(0.0, max(row["sample_max_gap"] for row in alt_rows))
        pieces.append({
            "piece": piece_index, "lo": lo, "hi": hi, "prior_mass": interval_mass(lo, hi, p),
            "assigned_plan": PLAN_NAMES[assigned],
            "alternative_plan": alt_rows[0]["alternative_plan"],
            "possible_profitable_alternatives": [
                row["alternative_plan"] for row in alt_rows if row["certified_upper"] > 0.0
            ],
            "positive_sample_witness": bool(sample_regret > FLOAT_ALLOWANCE),
            "sample_max_regret": float(sample_regret),
            "bound": float(piece_bound),
            "mesh_segments": nseg,
            "cover_radius": float(0.5 * (hi - lo) / nseg),
            "alternatives": alt_rows,
            "branch_metadata": {PLAN_NAMES[j]: branch_meta[j] for j in (EXIT, HOLD, VOICE)},
        })

    positive = [row for row in pieces if row["bound"] > 0.0]
    attaining = max(pieces, key=lambda row: row["bound"])
    node_seconds = time.perf_counter() - started
    return {
        "node": node, "T": T, "tau": tau, "kappa": p.kappa, "mark": p.mark, "H": p.H,
        "node_params_hash": p.hash_str(), "bound": attaining["bound"],
        "attaining_piece": {
            "piece": attaining["piece"], "lo": attaining["lo"], "hi": attaining["hi"],
            "prior_mass": attaining["prior_mass"], "assigned_plan": attaining["assigned_plan"],
            "alternative_plan": attaining["alternative_plan"],
        },
        "positive_regret_pieces": positive,
        "cutoff_payoff_levels": cutoff_payoffs(k, res, p),
        "n_breakpoint_pieces": len(pieces),
        "n_menu_breakpoint_pieces": len(menu_bps) - 1,
        "pooled_seconds": pooled_seconds, "certification_seconds": node_seconds - pooled_seconds,
        "wall_seconds": node_seconds, "pooled_max_price_residual": res.max_price_residual,
        "certifier_max_flagged_root_residual": max_flagged_root_residual,
    }


def main() -> None:
    source = json.loads(SOURCE_RECORD.read_text())
    provenance = source["provenance"]
    k = tuple(float(x) for x in provenance["frozen_k"])
    taus = [float(x) for x in provenance["tau_ladder"]]
    if provenance["mark"] != 2 or provenance["H"] != 10:
        raise RuntimeError("the frozen provenance is not mark 2, H 10")
    p0 = ParamsV4.baseline()
    run_started = time.perf_counter()
    nodes = []
    acquire_lock()
    try:
        node = 0
        for T in (5, 10):
            for tau in taus:
                node += 1
                print(f"node {node}/10: T={T}, tau={tau:.17g}", flush=True)
                nodes.append(certify_node(node, T, tau, k, p0))
                print(
                    f"  bound={nodes[-1]['bound']:.9g}, wall={nodes[-1]['wall_seconds']:.1f}s",
                    flush=True,
                )
        record = {
            "status": "PASS", "claim": "upper bounds on maximal interim regret",
            "method": {
                "name": "breakpoint pieces with a proved Lipschitz cover",
                "breakpoints": "the full unmerged candidate set underlying numerical_v4.menu.breakpoints at the frozen benchmark cutoffs",
                "target_mesh_width": TARGET_MESH_WIDTH,
                "float_allowance": FLOAT_ALLOWANCE,
                "cover": "sample maximum plus the payoff-gap Lipschitz bound times half the actual mesh width, plus float allowance",
                "derivatives": "analytic on each piece; the flagged price uses implicit differentiation and 0 <= dP_F/ds <= beta",
                "positive_piece_rule": "all pieces with a positive certified upper bound are reported; positive_sample_witness distinguishes a computed profitable type from a conservative endpoint allowance",
            },
            "provenance": {
                "source_record": str(SOURCE_RECORD.relative_to(ROOT)),
                "source_params_hash": provenance["params_hash"], "frozen_k": list(k),
                "tau_ladder": taus, "kappa": 0.5, "mark": 2, "H": 10,
                "T_grid": [5, 10],
            },
            "nodes": nodes,
            "total_wall_seconds": time.perf_counter() - run_started,
        }
        tmp = OUT.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(record, indent=2) + "\n")
        tmp.replace(OUT)
    finally:
        release_lock()


if __name__ == "__main__":
    main()
