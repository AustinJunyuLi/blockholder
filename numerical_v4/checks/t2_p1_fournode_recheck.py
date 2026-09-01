"""P1 four-node recheck: the 30-seed re-run of the sweep's four unresolved nodes.

Ticket 34 (R4). Audit finding 5
(``research/model_v4/threads/2026-08-23_gpt_end_review_audit.md``) found that
``t2_p1_check.py``'s node-set-B sweep gave its four FAILING nodes only
``N_SEEDS_SWEEP = 5`` attempts with early stopping, where the design asked 30
(``impl_design.md`` :25, :138, :320: "P1 wants 30 seeds"; "P1 grid (50 nodes x
30 seeds)"). Their status after 5 seeds was neither existence nor
nonexistence: cutoff residual ~1e-11 (passes the diagnostic scale) but payoff
residual 3.1e-4..1.5e-3 (fails the binding scale by 5-6 orders of magnitude) --
UNCHECKED, not refuting, and A3/A6 were not spot-checked there either.

This script re-runs EXACTLY those four nodes, seeds 0..29, NO early stopping,
and reports the full 30-seed distribution plus A3/A6 spot diagnostics, using
only machinery already in ``numerical_v4/`` (``ParamsV4``, ``solve_policy``,
whose ``Residual`` already carries both proxies on every call) -- no new model
objects, per the ticket. It parametrizes ``t2_p1_check.py``'s own node-set-B
construction; it does not rerun the sweep and does not touch the card.

THE FOUR NODES (t2_p1_check.py's node set B -- KAPPA_SWEEP x {0.05, 0.075} x
T_SWEEP -- restricted to the four combinations that failed to converge on the
payoff scale within 5 seeds, per audit finding 5 / ``t2_p1_check.json``
``p1_multistart_existence_sweep`` rows):

  kappa=0.15  tau=0.05    T=5
  kappa=0.15  tau=0.075   T=1
  kappa=0.85  tau=0.05    T=5
  kappa=0.85  tau=0.075   T=1

WHY ``baseline_frozen()`` IS NOT REPLAYED HERE. ``t2_p1_check.py`` builds its
node-set-B params as ``p.replace(kappa=kap, tau=tau, T=T)`` where ``p =
p_seed.replace(tau=tau_med)`` and ``p_seed = ParamsV4.baseline()`` (two cold
equilibrium solves just to *locate* ``tau_med``). But none of the four target
nodes uses ``tau_med`` -- both of their tau values (0.05, 0.075) are named
literals -- and ``ParamsV4`` (``numerical_v4/params.py``) has no
``__post_init__`` and no cached cross-field state: every derived quantity is a
``@property`` recomputed from the stored fields, and ``dataclasses.replace``
only overrides the named fields. So ``p.replace(kappa=K, tau=TAU, T=T)`` for
TAU in {0.05, 0.075} is *field-for-field identical*, regardless of what
``p``'s own pre-replacement tau (i.e. tau_med) was, to
``ParamsV4.baseline().replace(kappa=K, tau=TAU, T=T)`` -- verified directly by
``dataclasses.asdict`` equality before this script was written, and again by
the fact that this run's own seeds 0..4 reproduce the parent JSON's recorded
5-seed best-of values (``REPRODUCTION_CHECK`` in each node's detail). The two
cold "locate tau_med" solves are therefore dead weight for these four nodes
and are skipped.

EQUILIBRIUM CRITERION -- unchanged from the parent check (design section 13,
ruling 4): BINDING is the payoff scale, no adjacent-plan deviation above
1e-9; cutoff scale 1e-10 is diagnostic only. Operators match the parent
script's own code exactly (``t2_p1_check.py`` check_multistart): payoff uses
``<=``, cutoff uses ``<`` (the ticket text paraphrases both as ``<``; the
boundary convention is immaterial in floating point -- no computed residual is
expected to land exactly on the tolerance). A node is RESOLVED-EXISTS iff at
least one of the 30 seeds satisfies BOTH simultaneously.

A3/A6 SPOT DIAGNOSTICS -- no new diagnostic machinery, only fields
``equilibrium_residual`` already computes on every solve:
  * A3 (ordered plans, single crossing; MODEL_CARD.md :168). ``Residual.slopes``
    is d(U_j - U_{j+1})/ds at each cutoff. Below a cutoff the lower-index plan
    is chosen, above it the higher-index plan is -- so a transversal, single
    crossing requires the gap strictly DECREASING through zero, i.e. both
    slopes strictly negative. A wrong sign is direct numerical evidence
    against the maintained hypothesis at that node, independent of whether the
    fixed point itself converges. Checked at the achieving/closest seed, and
    counted across all 30 (free -- already computed for every seed).
  * A6 (compact outer self-map; MODEL_CARD.md :189). P1_proof.md Step 13 shows
    "maps Theta into itself" is a *derived* consequence of A3 given the
    solver's own construction (``outer_map`` clips brackets to
    [s_lo, s_hi] and orders k1<=k2 by construction) -- so it cannot fail
    numerically except via the one place the derivation's fallback branch
    (no interior sign change found) actually bites: a cutoff pinned at s_lo or
    s_hi. That pinning is checked directly. A COLLAPSED interior cutoff
    (k1==k2, the Hold region carrying zero mass) is explicitly legitimate per
    Step 13 ("including on the collapse faces...") and is reported as a flag,
    never treated as a failure. ``cutoff_scale`` (already the headline
    existence metric) doubles as the self-map fixed-point residual. A genuine
    continuity-of-T-in-k probe (finite-differencing ``outer_map`` at
    perturbed k) was considered and dropped: its only non-arbitrary pass/fail
    criterion (finiteness) passes trivially whenever solve_policy itself
    doesn't crash, so it would be decorative, not a checkable proxy.

RESUMABILITY (added after a host restart killed the first attempt mid-run,
having finished the two kappa=0.15 nodes). The JSON is checkpointed
ATOMICALLY (write-to-temp + os.replace) after EVERY SEED, not just after every
node: a node's ``seeds_data`` accumulates under ``results["in_progress"]``
keyed by node, and only migrates into ``results["checks"]`` (a finalized
node) once all 30 seeds are in. Rerunning this script with the same OUT path
picks up exactly where it left off -- a fully finalized node is loaded
verbatim from disk and NOT recomputed (seeds are deterministic so recomputing
would reproduce it anyway, per the reproduction check above; skipping it just
saves time); a partially-run node resumes at its next unrun seed. Set
``RECHECK_TIME_BUDGET_S`` (seconds) to make one invocation stop cleanly and
checkpoint once that much wall time has elapsed since the invocation started,
rather than always running to completion in one process -- useful for
babysitting this in bounded foreground chunks. Exit code 2 means "checkpointed
but not all four nodes are finalized yet, rerun me"; 0/1 mean a complete run
(0 = all four RESOLVED-EXISTS, 1 = otherwise, mirroring the parent script's
convention where a nonzero exit reports an honest finding, not a bug).

Deterministic: the only randomness is ``solve_policy``'s own seeded jitter
(``np.random.default_rng(seed)``); no Monte Carlo; no file inputs; no network.

Run:    .venv/bin/python numerical_v4/checks/t2_p1_fournode_recheck.py
        RECHECK_TIME_BUDGET_S=420 .venv/bin/python numerical_v4/checks/t2_p1_fournode_recheck.py   # budgeted chunk
Output: numerical_v4/checks/t2_p1_fournode_recheck.json (checkpointed after
        every seed; safe to interrupt and rerun at any point)
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from numerical_v4.params import ParamsV4  # noqa: E402
from numerical_v4.solver import TOL_CUTOFF, TOL_PAYOFF, solve_policy  # noqa: E402

OUT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "t2_p1_fournode_recheck.json"
)

# -- tolerances (verbatim import; DO NOT change) -----------------------------
TOL_EXIST_PAYOFF = TOL_PAYOFF        # 1e-9  -- BINDING (design 13, ruling 4)
TOL_EXIST_CUTOFF = TOL_CUTOFF        # 1e-10 -- diagnostic only
CORNER_EPS = 1e-6                    # A6 proxy: cutoff pinned at s_lo/s_hi
COLLAPSE_EPS = 1e-6                  # informational only: k1 == k2

# -- grid ---------------------------------------------------------------------
N_SEEDS = 30                          # the design's ask; NOT the sweep's 5

NODES = [
    {"kappa": 0.15, "tau": 0.05, "T": 5},
    {"kappa": 0.15, "tau": 0.075, "T": 1},
    {"kappa": 0.85, "tau": 0.05, "T": 5},
    {"kappa": 0.85, "tau": 0.075, "T": 1},
]

# Parent's recorded 5-seed (early-stop, but none tripped it -- all four ran
# the full 5) result for these same nodes, verbatim from
# numerical_v4/checks/t2_p1_check.json -> p1_multistart_existence_sweep ->
# rows, for the REPRODUCTION_CHECK below.
PRIOR_5SEED = {
    (0.15, 0.05, 5): {
        "best_payoff_scale": 0.001488170939392311,
        "best_cutoff_scale": 1.8952395208771122e-11,
        "k": [1.0074676693103841, 1.5613050961812023],
        "seconds": 85.2498247079784,
    },
    (0.15, 0.075, 1): {
        "best_payoff_scale": 0.0010592282017965887,
        "best_cutoff_scale": 1.2545520178264269e-14,
        "k": [1.0039258750690332, 1.5361669836666294],
        "seconds": 83.91239004197996,
    },
    (0.85, 0.05, 5): {
        "best_payoff_scale": 0.00039841768806352096,
        "best_cutoff_scale": 2.2122526033285794e-11,
        "k": [1.0871354370969635, 1.548848450728854],
        "seconds": 86.30552520800848,
    },
    (0.85, 0.075, 1): {
        "best_payoff_scale": 0.0003061479141195228,
        "best_cutoff_scale": 2.173439206387684e-11,
        "k": [1.088861883430131, 1.5387849788427397],
        "seconds": 82.52846516598947,
    },
}

results: dict = {"checks": [], "n_fail": 0}


def record(name: str, ok: bool, kind: str, detail: dict) -> None:
    results["checks"].append({"name": name, "kind": kind, "pass": bool(ok), **detail})
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({kind})", flush=True)


def node_params(kappa: float, tau: float, T: int) -> ParamsV4:
    """ParamsV4 for one of the four nodes -- see module docstring for why this
    is provably identical to what t2_p1_check.py's node-set-B sweep built."""
    return ParamsV4.baseline().replace(kappa=float(kappa), tau=float(tau), T=int(T))


def _checkpoint() -> None:
    """Atomic write: temp file + os.replace, so a kill mid-write never leaves
    OUT corrupted (this script has already been killed mid-run once)."""
    tmp = OUT + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    os.replace(tmp, OUT)


def _load_state() -> dict | None:
    if not os.path.exists(OUT):
        return None
    try:
        with open(OUT) as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        return None


def _node_key(node: dict) -> tuple:
    return (node["kappa"], node["tau"], node["T"])


def solve_one_seed(p: ParamsV4, sd: int) -> dict:
    ts = time.perf_counter()
    try:
        pol, r = solve_policy(p, seed=sd)
        dt = time.perf_counter() - ts
        row = {
            "seed": sd,
            "k": [float(pol.k[0]), float(pol.k[1])],
            "cutoff_scale": float(r.cutoff_scale),
            "payoff_scale": float(r.payoff_scale),
            "slopes": [float(x) for x in r.slopes],
            "meets_cutoff": bool(r.cutoff_scale < TOL_EXIST_CUTOFF),
            "meets_payoff": bool(r.payoff_scale <= TOL_EXIST_PAYOFF),
            "seconds": dt,
            "error": None,
        }
    except Exception as exc:  # defensive: 120 cold solves, don't lose the run
        dt = time.perf_counter() - ts
        row = {
            "seed": sd, "k": None, "cutoff_scale": float("inf"),
            "payoff_scale": float("inf"), "slopes": None,
            "meets_cutoff": False, "meets_payoff": False,
            "seconds": dt, "error": f"{type(exc).__name__}: {exc}",
        }
    row["meets_both"] = bool(row["meets_cutoff"] and row["meets_payoff"])
    return row


def finalize_node(node: dict, p: ParamsV4, seeds_data: list) -> dict:
    key = _node_key(node)
    ok_rows = [row for row in seeds_data if row["error"] is None]
    payoffs = np.array([row["payoff_scale"] for row in ok_rows])
    cutoffs = np.array([row["cutoff_scale"] for row in ok_rows])
    qualifying = [row for row in ok_rows if row["meets_both"]]

    best_payoff_row = min(ok_rows, key=lambda r: r["payoff_scale"])
    best_cutoff_row = min(ok_rows, key=lambda r: r["cutoff_scale"])
    achieving = (
        min(qualifying, key=lambda r: r["payoff_scale"])
        if qualifying else best_payoff_row
    )

    # -- A3 proxy: slope sign at the achieving/closest seed, plus a
    #    node-wide count (free -- already computed for every seed) ----------
    a3_slopes = achieving["slopes"]
    a3_pass = all(s < 0.0 for s in a3_slopes)
    a3_fail_seeds = [
        row["seed"] for row in ok_rows
        if not all(s < 0.0 for s in row["slopes"])
    ]

    # -- A6 proxy: Theta-boundary pinning at the achieving/closest seed,
    #    plus a node-wide count. Collapse (k1==k2) is informational only,
    #    never a failure (P1_proof.md Step 13 allows it explicitly). --------
    k_ach = achieving["k"]
    corner_lo = abs(k_ach[0] - p.s_lo) < CORNER_EPS
    corner_hi = abs(k_ach[1] - p.s_hi) < CORNER_EPS
    collapsed = abs(k_ach[0] - k_ach[1]) < COLLAPSE_EPS
    a6_pass = not (corner_lo or corner_hi)
    a6_corner_seeds = [
        row["seed"] for row in ok_rows
        if abs(row["k"][0] - p.s_lo) < CORNER_EPS
        or abs(row["k"][1] - p.s_hi) < CORNER_EPS
    ]
    a6_collapsed_seeds = [
        row["seed"] for row in ok_rows
        if abs(row["k"][0] - row["k"][1]) < COLLAPSE_EPS
    ]

    # -- verdict --------------------------------------------------------------
    if qualifying:
        verdict = "RESOLVED-EXISTS"
    else:
        failed_proxies = []
        if not a3_pass:
            failed_proxies.append("A3")
        if not a6_pass:
            failed_proxies.append("A6")
        verdict = (
            f"HYPOTHESIS-PROXY-FAILS({','.join(failed_proxies)})"
            if failed_proxies else "STILL UNRESOLVED after 30 seeds"
        )

    # -- reproduction check against the parent's 5-seed result ---------------
    prior = PRIOR_5SEED[key]
    seeds_sorted = sorted(seeds_data, key=lambda r: r["seed"])
    first5 = [row for row in seeds_sorted if row["seed"] < 5]
    if len(first5) == 5 and all(row["error"] is None for row in first5):
        my_best_payoff_5 = min(row["payoff_scale"] for row in first5)
        my_best_cutoff_5 = min(row["cutoff_scale"] for row in first5)
        payoff_reproduces = math.isclose(
            my_best_payoff_5, prior["best_payoff_scale"], rel_tol=1e-6, abs_tol=1e-12
        )
        cutoff_reproduces = math.isclose(
            my_best_cutoff_5, prior["best_cutoff_scale"], rel_tol=1e-6, abs_tol=1e-12
        )
    else:
        my_best_payoff_5 = my_best_cutoff_5 = None
        payoff_reproduces = cutoff_reproduces = False
    reproduction = {
        "prior_5seed_best_payoff_scale": prior["best_payoff_scale"],
        "prior_5seed_best_cutoff_scale": prior["best_cutoff_scale"],
        "prior_5seed_k": prior["k"],
        "this_run_seeds_0to4_best_payoff_scale": my_best_payoff_5,
        "this_run_seeds_0to4_best_cutoff_scale": my_best_cutoff_5,
        "payoff_reproduces": bool(payoff_reproduces),
        "cutoff_reproduces": bool(cutoff_reproduces),
        "note": (
            "seeds 0..4 here use the identical ParamsV4 (see module docstring "
            "derivation), identical seeds and identical solve_policy as the "
            "parent's node-set-B row for this node; a mismatch beyond floating"
            "-point noise means the parametrization or environment drifted."
        ),
    }

    total_seconds = float(sum(row["seconds"] for row in seeds_data))

    return {
        "node": {"kappa": node["kappa"], "tau": node["tau"], "T": node["T"],
                  "H": p.H, "corner": bool(node["T"] == p.H)},
        "params_hash": p.hash_str(),
        "n_seeds_run": len(seeds_data),
        "n_errors": len(seeds_data) - len(ok_rows),
        "early_stop": False,
        "seconds": total_seconds,
        "verdict": verdict,
        "equilibrium_criterion": (
            "cutoff_scale < 1e-10 (diagnostic) AND payoff_scale <= 1e-9 "
            "(binding, design 13 ruling 4); ANY of the 30 seeds meeting both "
            "resolves the node"
        ),
        "best_cutoff_scale": float(cutoffs.min()),
        "best_cutoff_seed": int(best_cutoff_row["seed"]),
        "best_payoff_scale": float(payoffs.min()),
        "best_payoff_seed": int(best_payoff_row["seed"]),
        "achieving_seed": int(achieving["seed"]),
        "achieving_seed_cutoff_scale": float(achieving["cutoff_scale"]),
        "achieving_seed_payoff_scale": float(achieving["payoff_scale"]),
        "achieving_seed_meets_both": bool(achieving["meets_both"]),
        "achieving_seed_k": achieving["k"],
        "payoff_scale_distribution": {
            "min": float(payoffs.min()),
            "p25": float(np.percentile(payoffs, 25)),
            "median": float(np.median(payoffs)),
            "p75": float(np.percentile(payoffs, 75)),
            "max": float(payoffs.max()),
            "mean": float(payoffs.mean()),
            "std": float(payoffs.std()),
        },
        "cutoff_scale_distribution": {
            "min": float(cutoffs.min()),
            "median": float(np.median(cutoffs)),
            "max": float(cutoffs.max()),
        },
        "n_qualifying_seeds": len(qualifying),
        "qualifying_seeds": [row["seed"] for row in qualifying],
        "a3_single_crossing_proxy": {
            "hypothesis": "A3 (MODEL_CARD.md :168): adjacent-plan payoff gap "
                          "crosses zero at most once; preferred plan weakly "
                          "increasing in s",
            "proxy": "Residual.slopes at each cutoff (already computed by "
                     "equilibrium_residual on every solve); expected sign "
                     "strictly negative at both",
            "slopes_at_achieving_seed": a3_slopes,
            "pass_at_achieving_seed": bool(a3_pass),
            "fail_count_of_30": len(a3_fail_seeds),
            "fail_seeds": a3_fail_seeds,
        },
        "a6_self_map_proxy": {
            "hypothesis": "A6 (MODEL_CARD.md :189): cutoffs lie in a common "
                          "compact ordered polytope Theta; T continuous, maps "
                          "Theta into itself",
            "proxy": "cutoff_scale (self-map fixed-point residual, already "
                     "the headline metric) plus Theta-boundary pinning "
                     "(a symptom of outer_map's no-interior-crossing "
                     "fallback -- the one place the self-map derivation in "
                     "P1_proof.md Step 13 can numerically misfire)",
            "s_lo": p.s_lo, "s_hi": p.s_hi,
            "k_at_achieving_seed": k_ach,
            "corner_lo_at_achieving_seed": bool(corner_lo),
            "corner_hi_at_achieving_seed": bool(corner_hi),
            "pass_at_achieving_seed": bool(a6_pass),
            "corner_count_of_30": len(a6_corner_seeds),
            "corner_seeds": a6_corner_seeds,
            "collapsed_informational": {
                "note": "k1==k2 (Hold carries zero mass) is explicitly "
                        "legitimate per P1_proof.md Step 13; reported, never "
                        "gates the verdict",
                "collapsed_at_achieving_seed": bool(collapsed),
                "collapsed_count_of_30": len(a6_collapsed_seeds),
                "collapsed_seeds": a6_collapsed_seeds,
            },
        },
        "reproduction_of_prior_5seed_result": reproduction,
        "seeds": seeds_data,
    }


def main() -> int:
    run_t0 = time.perf_counter()
    budget_env = os.environ.get("RECHECK_TIME_BUDGET_S", "").strip()
    time_budget = float(budget_env) if budget_env else None

    prior = _load_state()
    finalized: dict = {}
    in_progress: dict = {}
    if prior:
        for c in prior.get("checks", []):
            n = c.get("node") or {}
            key = (n.get("kappa"), n.get("tau"), n.get("T"))
            if all(x is not None for x in key):
                finalized[key] = c
                results["checks"].append(c)
                if not c.get("pass", False):
                    results["n_fail"] += 1
        for v in (prior.get("in_progress") or {}).values():
            n = v.get("node") or {}
            key = (n.get("kappa"), n.get("tau"), n.get("T"))
            if all(x is not None for x in key) and key not in finalized:
                in_progress[key] = v

    print("t2_p1_fournode_recheck -- P1's four unresolved nodes, 30 seeds, "
          "no early stop.", flush=True)
    print(f"Nodes: {NODES}", flush=True)
    if finalized:
        print(f"Resuming: {len(finalized)} node(s) already finalized on disk "
              f"{sorted(finalized.keys())} -- loaded verbatim, not recomputed.",
              flush=True)
    if in_progress:
        print(f"Resuming: {len(in_progress)} node(s) partially run "
              f"{ {k: len(v['seeds_data']) for k, v in in_progress.items()} } "
              "-- continuing from the next unrun seed.", flush=True)
    if time_budget:
        print(f"Time budget this invocation: {time_budget:.0f}s (babysat in "
              "chunks; checkpoints per seed, exits cleanly with code 2 if the "
              "budget is hit mid-node -- rerun to continue).", flush=True)

    results["provenance"] = {
        "ticket": "34 (R4)",
        "audit_finding": (
            "research/model_v4/threads/2026-08-23_gpt_end_review_audit.md "
            "Finding 5 (UPHELD as UNCHECKED)"
        ),
        "parent_check": "numerical_v4/checks/t2_p1_check.py / .json "
                        "(p1_multistart_existence_sweep, node set B)",
        "design": "research/model_v4/impl_design.md :25, :138, :320 "
                  "(N_SEEDS = 30 is the design's ask for the P1 grid; the "
                  "sweep's N_SEEDS_SWEEP = 5 was a runtime cut, not the ask)",
        "binding_criterion": (
            "payoff scale, no adjacent-plan deviation above 1e-9 (design "
            "section 13, ruling 4); cutoff-scale 1e-10 diagnostic only"
        ),
        "operator_note": (
            "payoff uses <=, cutoff uses < -- copied verbatim from "
            "t2_p1_check.py check_multistart; the ticket text paraphrases "
            "both as strict <, an immaterial boundary-convention difference"
        ),
        "resume_note": (
            "This run was interrupted once (host process restart) after the "
            "two kappa=0.15 nodes finished; it was resumed with per-seed "
            "checkpointing rather than rerun from scratch. See the module "
            "docstring's RESUMABILITY section."
            if finalized or in_progress else None
        ),
        "does_not": "rerun the full sweep; change TOL_CUTOFF/TOL_PAYOFF; "
                   "write to MODEL_CARD.md, LABEL_LEDGER.md, or the session log",
    }
    results["grid"] = {"nodes": NODES, "n_seeds": N_SEEDS, "early_stop": False}
    _checkpoint()

    node_results = []
    for node in NODES:
        key = _node_key(node)
        if key in finalized:
            node_results.append(finalized[key])
            continue

        p = node_params(*key)
        state = in_progress.get(key)
        seeds_data = list(state["seeds_data"]) if state else []
        if state:
            print(f"\n=== resuming node kappa={node['kappa']} tau={node['tau']} "
                  f"T={node['T']} at seed {len(seeds_data)}/{N_SEEDS} ===",
                  flush=True)
        else:
            print(f"\n=== node kappa={node['kappa']} tau={node['tau']} "
                  f"T={node['T']} (H={p.H}, corner={node['T'] == p.H}) ===",
                  flush=True)

        for sd in range(len(seeds_data), N_SEEDS):
            if time_budget and (time.perf_counter() - run_t0) >= time_budget:
                break
            row = solve_one_seed(p, sd)
            seeds_data.append(row)
            tag = "OK " if row["error"] is None else "ERR"
            print(f"    [{tag}] seed {sd:2d}  cutoff={row['cutoff_scale']:.3e}  "
                  f"payoff={row['payoff_scale']:.3e}  slopes={row['slopes']}  "
                  f"({row['seconds']:.1f}s)", flush=True)
            ip = results.get("in_progress", {})
            key_str = f"{key[0]},{key[1]},{key[2]}"
            ip[key_str] = {"node": node, "seeds_data": seeds_data}
            results["in_progress"] = ip
            _checkpoint()

        if len(seeds_data) < N_SEEDS:
            print(f"=== node kappa={node['kappa']} tau={node['tau']} "
                  f"T={node['T']} PARTIAL: {len(seeds_data)}/{N_SEEDS} seeds "
                  "done, time budget hit, checkpointed -- rerun this script "
                  "to continue ===", flush=True)
            break

        detail = finalize_node(node, p, seeds_data)
        node_results.append(detail)
        record(
            f"p1_fournode_k{node['kappa']}_tau{node['tau']}_T{node['T']}",
            detail["verdict"] == "RESOLVED-EXISTS", "substantive", detail,
        )
        ip = results.get("in_progress", {})
        ip.pop(f"{key[0]},{key[1]},{key[2]}", None)
        results["in_progress"] = ip
        results["nodes_so_far"] = len(node_results)
        _checkpoint()
        print(f"=== node kappa={node['kappa']} tau={node['tau']} "
              f"T={node['T']} FINALIZED: {detail['verdict']} "
              f"({detail['seconds']:.0f}s total) ===", flush=True)

    if len(node_results) < len(NODES):
        print(f"\nPARTIAL RUN: {len(node_results)}/4 nodes finalized. Rerun "
              "the same command to continue -- state is checkpointed per "
              "seed, nothing is lost.", flush=True)
        print(f"(this invocation ran {time.perf_counter() - run_t0:.0f}s)",
              flush=True)
        return 2

    # -- all four nodes finalized: build the final aggregate ------------------
    results["seconds"] = float(sum(d["seconds"] for d in node_results))
    results["all_pass"] = results["n_fail"] == 0
    results.pop("in_progress", None)
    results["summary_table"] = [
        {
            "kappa": d["node"]["kappa"], "tau": d["node"]["tau"], "T": d["node"]["T"],
            "verdict": d["verdict"],
            "best_cutoff_scale": d["best_cutoff_scale"],
            "best_cutoff_seed": d["best_cutoff_seed"],
            "best_payoff_scale": d["best_payoff_scale"],
            "best_payoff_seed": d["best_payoff_seed"],
            "achieving_seed": d["achieving_seed"],
            "achieving_seed_meets_both": d["achieving_seed_meets_both"],
            "a3_pass": d["a3_single_crossing_proxy"]["pass_at_achieving_seed"],
            "a6_pass": d["a6_self_map_proxy"]["pass_at_achieving_seed"],
            "payoff_reproduces_prior_5seed": d["reproduction_of_prior_5seed_result"][
                "payoff_reproduces"
            ],
            "seconds": d["seconds"],
        }
        for d in node_results
    ]
    n_resolved = sum(1 for d in node_results if d["verdict"] == "RESOLVED-EXISTS")
    results["verdict"] = (
        f"{n_resolved}/4 nodes RESOLVED-EXISTS after 30 seeds each; "
        + "; ".join(
            f"(kappa={d['node']['kappa']}, tau={d['node']['tau']}, "
            f"T={d['node']['T']}): {d['verdict']}"
            for d in node_results
        )
    )

    _checkpoint()
    print(f"\n{'ALL RESOLVED' if results['all_pass'] else str(4 - n_resolved) + ' of 4 NOT resolved'}"
          f"  cumulative solve time {results['seconds']:.0f} s  ->  {OUT}", flush=True)
    print(results["verdict"], flush=True)
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
