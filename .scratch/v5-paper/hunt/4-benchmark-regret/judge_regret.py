"""Independent judge of hunt 4's certified benchmark-policy regret record.

Run from the repository root:

    PYTHONPATH=. .venv/bin/python \
      .scratch/v5-paper/hunt/4-benchmark-regret/judge_regret.py

It takes the compute lock, runs ONE pooled pass (node 1), and prints a report.
It writes no file.
"""
from __future__ import annotations

import importlib.util
import json
import math
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from numerical_v4.flagged import flagged_price_at
from numerical_v4.menu import (
    atoms, b_star, b_star_prime, breakpoints, legal_clock, n_days, signature,
)
from numerical_v4.params import EXIT, HOLD, VOICE, ParamsV4
from numerical_v4.policy import engagement_cost, plan_payoff
from numerical_v4.pooled import inner_price, pooled_pass

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
LOCK = ROOT / ".scratch/v5-paper/runs/COMPUTE_LOCK"
OWNER = "4-benchmark-regret-judge"
WHAT = "hunt 4 judge, one pooled pass at node 1"
SOURCE = ROOT / "numerical_v4/checks/t2_threshold_revelation_check.json"
RECORD = HERE / "regret.json"
PLAN = {EXIT: "Exit", HOLD: "Hold", VOICE: "Voice"}

fails: list[str] = []
nits: list[str] = []


def check(ok: bool, msg: str) -> bool:
    print(("  ok   " if ok else "  FAIL ") + msg, flush=True)
    if not ok:
        fails.append(msg)
    return ok


def load_regret_module():
    spec = importlib.util.spec_from_file_location("hunt4_regret", HERE / "regret.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def acquire_lock() -> None:
    if LOCK.exists():
        raise SystemExit(f"compute lock present: {LOCK}")
    proc = subprocess.run(["pgrep", "-f", "numerical_v4"], capture_output=True,
                          text=True, check=False)
    live = [ln for ln in proc.stdout.split() if ln.strip() and int(ln) != os.getpid()]
    if live:
        raise SystemExit(f"numerical_v4 process running: {live}")
    with LOCK.open("x") as fh:
        json.dump({"pid": os.getpid(), "what": WHAT,
                   "started": datetime.now(timezone.utc).isoformat(),
                   "owner": OWNER}, fh, indent=2)
        fh.write("\n")


def release_lock() -> None:
    try:
        payload = json.loads(LOCK.read_text())
    except Exception:
        return
    if payload.get("pid") == os.getpid() and payload.get("owner") == OWNER:
        LOCK.unlink()


# ---------------------------------------------------------------------------
# Part A: record integrity and breakpoint completeness, all ten nodes, no pass
# ---------------------------------------------------------------------------


def part_a(reg, record, k, taus, p0) -> None:
    print("\nA. record arithmetic and piece structure at all ten nodes")
    worst_sig = 0
    worst_arith = 0.0
    worst_edge = 0.0
    node_i = 0
    for T in (5, 10):
        for tau in taus:
            node_i += 1
            nd = record["nodes"][node_i - 1]
            p = p0.replace(tau=float(tau), T=int(T), kappa=0.5, mark=2, H=10)
            assert nd["T"] == T and abs(nd["tau"] - tau) == 0.0
            if nd["node_params_hash"] != p.hash_str():
                fails.append(f"node {node_i}: params hash mismatch")
            bps = reg.complete_breakpoints(k, p)
            menu_bps = breakpoints(k, p)
            if not set(menu_bps).issubset(set(bps)):
                fails.append(f"node {node_i}: menu breakpoint lost")
            if len(bps) - 1 != nd["n_breakpoint_pieces"]:
                fails.append(f"node {node_i}: piece count mismatch")
            if bps[0] != p.s_lo or bps[-1] != p.s_hi:
                fails.append(f"node {node_i}: partition does not span the support")
            # signature constancy on every piece, 200 interior points each
            for lo, hi in zip(bps[:-1], bps[1:]):
                fr = np.linspace(0.0, 1.0, 202)[1:-1]
                ss = lo + fr * (hi - lo)
                sigs = set()
                for s in ss:
                    j = EXIT if s < k[0] else (HOLD if s < k[1] else VOICE)
                    cl = legal_clock(VOICE, float(s), p)
                    sigs.add((j, n_days(float(s), p), cl.c, cl.f, cl.D))
                if len(sigs) != 1:
                    worst_sig += 1
                    fails.append(f"node {node_i}: signature changes inside "
                                 f"piece [{lo!r}, {hi!r}]: {sigs}")
            # every recorded positive piece is a piece of the partition, and its
            # mesh, radius and certified upper reproduce from its own fields
            edges = set(float(x) for x in bps)
            for pc in nd["positive_regret_pieces"]:
                if pc["lo"] not in edges or pc["hi"] not in edges:
                    fails.append(f"node {node_i}: reported piece is not a partition piece")
                nseg = max(1, int(math.ceil((pc["hi"] - pc["lo"]) / 1.0e-5)))
                worst_edge = max(worst_edge, abs(nseg - pc["mesh_segments"]))
                rad = 0.5 * (pc["hi"] - pc["lo"]) / nseg
                worst_edge = max(worst_edge, abs(rad - pc["cover_radius"]))
                for row in pc["alternatives"]:
                    got = (row["sample_max_gap"]
                           + row["gap_lipschitz_bound"] * pc["cover_radius"]
                           + 5.0e-12)
                    worst_arith = max(worst_arith, abs(got - row["certified_upper"]))
                if len(pc["alternatives"]) != 2:
                    fails.append(f"node {node_i}: piece does not compare both alternatives")
                best = max(row["certified_upper"] for row in pc["alternatives"])
                worst_arith = max(worst_arith, abs(max(0.0, best) - pc["bound"]))
            declared = max(pc["bound"] for pc in nd["positive_regret_pieces"])
            worst_arith = max(worst_arith, abs(declared - nd["bound"]))
    check(worst_sig == 0, f"signature constant on every piece of all ten nodes")
    check(worst_arith < 1e-18, f"record arithmetic self-consistent (max dev {worst_arith:.2e})")
    check(worst_edge == 0.0, f"mesh segments and cover radius reproduce (max dev {worst_edge:.2e})")


# ---------------------------------------------------------------------------
# Part B: node 1 recompute with one pooled pass
# ---------------------------------------------------------------------------


def part_b(reg, record, k, tau, p0):
    p = p0.replace(tau=float(tau), T=5, kappa=0.5, mark=2, H=10)
    print("\nB. one pooled pass at node 1 (T=5, tau=%.17g)" % tau)
    t0 = time.perf_counter()
    al = atoms(k, p)
    res = pooled_pass(al, p, with_runup=True)
    print("  pooled pass %.1f s, max price residual %.3e"
          % (time.perf_counter() - t0, res.max_price_residual), flush=True)
    reg.pooled_pass = lambda *a, **kw: res          # one pass only
    node = reg.certify_node(1, 5, float(tau), k, p0)
    ref = record["nodes"][0]
    check(node["bound"] == ref["bound"],
          "node 1 bound reproduces bit for bit: %.17g vs %.17g"
          % (node["bound"], ref["bound"]))
    same = all(node["attaining_piece"][key] == ref["attaining_piece"][key]
               for key in ("lo", "hi", "assigned_plan", "alternative_plan"))
    check(same, "node 1 attaining piece reproduces")
    devs = []
    for a, b in zip(node["positive_regret_pieces"], ref["positive_regret_pieces"]):
        devs.append(abs(a["bound"] - b["bound"]))
        devs.append(abs(a["sample_max_regret"] - b["sample_max_regret"]))
    check(max(devs) == 0.0, "node 1 positive pieces reproduce (max dev %.2e)" % max(devs))
    for row in ref["cutoff_payoff_levels"]:
        for name, j in (("Exit", EXIT), ("Hold", HOLD), ("Voice", VOICE)):
            got = float(plan_payoff(j, row["s"], res, p))
            if abs(got - row["all_payoffs"][name]) > 0.0:
                fails.append("cutoff payoff level mismatch at %r" % row["s"])
    check(True, "cutoff payoff levels recomputed from plan_payoff")
    return p, res, node


# ---------------------------------------------------------------------------
# Part C: closed forms against plan_payoff, Lipschitz constants, dense search
# ---------------------------------------------------------------------------


def part_c(reg, record, k, p, res, node):
    print("\nC. node 1: closed forms, derivative bounds, dense maximisation")
    bps = reg.complete_breakpoints(k, p)
    n_pts = 60
    fr = np.linspace(0.0, 1.0, n_pts + 2)[1:-1]
    worst_payoff = 0.0
    worst_payoff_where = None
    worst_lip_ratio = 0.0
    worst_lip_where = None
    worst_dP = -1.0
    worst_absP = 0.0
    dense_max = -1e9
    dense_arg = None
    per_piece = []

    for idx, (lo, hi) in enumerate(zip(bps[:-1], bps[1:]), start=1):
        lo, hi = float(lo), float(hi)
        mid = 0.5 * (lo + hi)
        assigned = EXIT if mid < k[0] else (HOLD if mid < k[1] else VOICE)
        ev, lip, meta = {}, {}, {}
        for j in (EXIT, HOLD, VOICE):
            ev[j], lip[j], meta[j] = reg.smooth_branch(j, mid, lo, hi, res, p)

        # C1 closed form vs plan_payoff at 60 interior points per piece
        ss = lo + fr * (hi - lo)
        for j in (EXIT, HOLD, VOICE):
            vals, _ = ev[j](ss)
            for s, v in zip(ss, vals):
                d = abs(float(v) - float(plan_payoff(j, float(s), res, p)))
                if d > worst_payoff:
                    worst_payoff, worst_payoff_where = d, (idx, PLAN[j], float(s))

        # C2 finite differences of every payoff and of each gap vs the claimed L
        ng = 20001
        g = np.linspace(lo, hi, ng)
        vv = {j: ev[j](g)[0] for j in (EXIT, HOLD, VOICE)}
        h = g[1] - g[0]
        # a forward difference of float64 values carries rounding noise of
        # order eps*|U|/h; the bound is only violated beyond that noise.
        def noise(arr):
            return 8.0 * np.finfo(float).eps * float(np.max(np.abs(arr))) / h

        for j in (EXIT, HOLD, VOICE):
            fd = np.abs(np.diff(vv[j])) / h
            m = float(fd.max()) if fd.size else 0.0
            ratio = m / (lip[j] + noise(vv[j]))
            if ratio > worst_lip_ratio:
                worst_lip_ratio, worst_lip_where = ratio, (idx, PLAN[j], m, lip[j])
        for alt in (EXIT, HOLD, VOICE):
            if alt == assigned:
                continue
            gap = vv[alt] - vv[assigned]
            fd = float(np.max(np.abs(np.diff(gap))) / h)
            L = lip[alt] + lip[assigned] + noise(vv[alt]) + noise(vv[assigned])
            if fd / L > worst_lip_ratio:
                worst_lip_ratio = fd / L
                worst_lip_where = (idx, PLAN[alt] + "-" + PLAN[assigned], fd, L)

        # C3 dense search for the true supremum of R on the piece
        best, arg = -1e9, lo
        span = hi - lo
        target = max(1, int(math.ceil(span / 1.0e-6)))
        nseg = min(target, 2_000_000)
        for c0 in range(0, nseg + 1, 250_000):
            c1 = min(nseg, c0 + 250_000 - 1)
            gg = lo + span * (np.arange(c0, c1 + 1) / nseg)
            va = ev[assigned](gg)[0]
            r = np.full(gg.shape, -1e9)
            for alt in (EXIT, HOLD, VOICE):
                if alt == assigned:
                    continue
                r = np.maximum(r, ev[alt](gg)[0] - va)
            i = int(np.argmax(r))
            if float(r[i]) > best:
                best, arg = float(r[i]), float(gg[i])
        # local refinement around the dense argmax
        w = 4.0 * span / nseg
        for _ in range(4):
            gg = np.linspace(max(lo, arg - w), min(hi, arg + w), 4001)
            va = ev[assigned](gg)[0]
            r = np.full(gg.shape, -1e9)
            for alt in (EXIT, HOLD, VOICE):
                if alt == assigned:
                    continue
                r = np.maximum(r, ev[alt](gg)[0] - va)
            i = int(np.argmax(r))
            if float(r[i]) > best:
                best, arg = float(r[i]), float(gg[i])
            w *= 0.02
        if best > dense_max:
            dense_max, dense_arg = best, arg
        rec_piece = next((q for q in record["nodes"][0]["positive_regret_pieces"]
                          if q["piece"] == idx), None)
        per_piece.append((idx, lo, hi, PLAN[assigned], best,
                          rec_piece["bound"] if rec_piece else 0.0))

        # C4 flagged price: bracket, |P| bound and 0 <= dP/ds <= beta
        if meta[VOICE].get("D") == 1:
            gg = lo + fr * (hi - lo)
            vh = p.mu_v + p.beta * (gg - p.mu_v)
            sol = inner_price(vh, np.ones_like(vh), p)
            worst_absP = max(worst_absP, float(np.max(np.abs(sol.P))))
            if float(np.max(np.abs(sol.P))) > meta[VOICE]["flagged_price_absolute_bound"]:
                fails.append("piece %d: |P_F| exceeds the certified bound" % idx)
            V = vh + p.Delta_V
            if float(np.min(sol.P - V)) < -1e-12:
                fails.append("piece %d: flagged price below V" % idx)
            eps = 1e-6
            s2 = inner_price(vh + p.beta * eps, np.ones_like(vh), p)
            s1 = inner_price(vh - p.beta * eps, np.ones_like(vh), p)
            dP = (s2.P - s1.P) / (2.0 * eps)
            worst_dP = max(worst_dP, float(np.max(dP)))
            if float(np.min(dP)) < -1e-9:
                fails.append("piece %d: dP_F/ds negative" % idx)

    check(worst_payoff < 1e-12,
          "closed-form branches equal plan_payoff at 60 interior points per piece "
          "(max |diff| %.3e at %r)" % (worst_payoff, worst_payoff_where))
    check(worst_lip_ratio <= 1.0,
          "every finite difference is inside the claimed Lipschitz bound plus "
          "difference noise (worst ratio %.6f at %r)" % (worst_lip_ratio, worst_lip_where))
    check(worst_dP <= p.beta + 1e-9,
          "flagged price slope dP_F/ds within [0, beta]: max %.6f, beta %.6f"
          % (worst_dP, p.beta))
    print("  max |P_F| seen on flagged pieces: %.6f" % worst_absP)
    print("  per-piece dense supremum of R against the record's bound:")
    for idx, lo, hi, asg, best, bound in per_piece:
        flag = "  <-- over bound" if best > bound + 1e-15 else ""
        print("    piece %2d [%.10f, %.10f] %-5s dense %.6e vs bound %.6e%s"
              % (idx, lo, hi, asg, best, bound, flag))
        if best > bound + 1e-15:
            fails.append("piece %d: dense search beats the piece bound" % idx)
    check(dense_max <= node["bound"],
          "dense supremum %.10e at s = %.12f is under the node bound %.10e"
          % (dense_max, dense_arg, node["bound"]))
    # the dense argmax evaluated through plan_payoff itself
    s = dense_arg
    ua = {j: float(plan_payoff(j, s, res, p)) for j in (EXIT, HOLD, VOICE)}
    asg = EXIT if s < k[0] else (HOLD if s < k[1] else VOICE)
    true_R = max(ua.values()) - ua[asg]
    check(true_R <= node["bound"],
          "plan_payoff regret at the dense argmax %.10e <= bound %.10e"
          % (true_R, node["bound"]))
    print("  dense argmax %.15g, R from plan_payoff %.10e, record bound %.10e"
          % (s, true_R, node["bound"]))


def main() -> None:
    record = json.loads(RECORD.read_text())
    prov = json.loads(SOURCE.read_text())["provenance"]
    k = tuple(float(x) for x in prov["frozen_k"])
    taus = [float(x) for x in prov["tau_ladder"]]
    p0 = ParamsV4.baseline()
    reg = load_regret_module()
    check(list(record["provenance"]["frozen_k"]) == list(k),
          "record frozen_k equals the provenance block")
    check(record["provenance"]["tau_ladder"] == taus,
          "record tau ladder equals the provenance block")
    part_a(reg, record, k, taus, p0)
    if "--structure-only" in sys.argv:
        print("\nstructure-only run, no pooled pass")
        print("\nFAILURES: %d" % len(fails))
        for f in fails:
            print("  - " + f)
        return
    acquire_lock()
    try:
        p, res, node = part_b(reg, record, k, taus[0], p0)
        part_c(reg, record, k, p, res, node)
    finally:
        release_lock()
    print("\nFAILURES: %d" % len(fails))
    for f in fails:
        print("  - " + f)


if __name__ == "__main__":
    main()
