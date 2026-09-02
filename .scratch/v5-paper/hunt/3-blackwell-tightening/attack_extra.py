"""Coverage diagnostics and the alternative information convention.

Runs from the repository root:

    PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/3-blackwell-tightening/attack_extra.py

Part 1 counts how often the random instances of attack_check.py actually
exercise the three branches of the memo's kernel, so that a clean pass is not a
pass on empty cases.  Part 2 tests the memo's paragraph on the alternative
convention, where a flagged path keeps its pre-filing pooled history.
"""

from __future__ import annotations

import itertools
import json
import os

import numpy as np

import importlib.util
_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "attack_check", os.path.join(_here, "attack_check.py"))
ac = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ac)

OUT = os.path.join(_here, "attack_extra.json")


def branch_counts(mod, tight, loose, d):
    """How many types fall in each branch of the kernel at depth d."""
    cp = [mod.clock(i, *tight) for i in range(mod.K)]
    cm = [mod.clock(i, *loose) for i in range(mod.K)]
    b1 = b2 = b3 = 0
    for i in range(mod.K):
        fp = cp[i][2] == 1 and cp[i][1] <= d
        fm = cm[i][2] == 1 and cm[i][1] <= d
        if not fp:
            b1 += 1
        elif fm:
            b2 += 1
        else:
            b3 += 1
    return b1, b2, b3


def alt_experiment(mod, tau, T, kappa, d):
    """Alternative convention: a flagged path keeps its pre-filing history.

    Column key is ('F', tuple, pre-filing flow) or ('P', flow through d).
    """
    cl = [mod.clock(i, tau, T) for i in range(mod.K)]
    cols = {}
    rows = []
    for i in range(mod.K):
        m = mod.marks(i)
        flagged = cl[i][2] == 1 and cl[i][1] <= d
        if flagged:
            f = int(cl[i][1])
            key_head = ("F", round(cl[i][3], 12), round(cl[i][4], 12))
            span = f                      # rounds 0..f-1 are pre-filing
        else:
            key_head = ("P",)
            span = d + 1
        laws = [ac.flow_law(m[e], kappa) for e in range(span)]
        entries = {}
        for h in itertools.product(range(5), repeat=span):
            pr = 1.0
            for e in range(span):
                pr *= laws[e][h[e]]
            if pr > 0:
                entries[key_head + h] = pr
        rows.append(entries)
        for k in entries:
            cols.setdefault(k, len(cols))
    L = np.zeros((mod.K, len(cols)))
    for i, entries in enumerate(rows):
        for k, pr in entries.items():
            L[i, cols[k]] = pr
    return L


def main():
    rec = {}
    rng = np.random.default_rng(7)
    ac.RNG = rng

    counts = {"b1": 0, "b2": 0, "b3": 0, "cases_with_b3": 0, "cases": 0,
              "cases_with_b2": 0}
    for trial in range(40):
        mod = ac.random_model(H=2, K=5, rng=rng)
        for tau_lo, tau_hi in ((0.04, 0.07), (0.05, 0.09)):
            for T in (1, 2):
                for d in range(mod.H + 1):
                    b1, b2, b3 = branch_counts(mod, (tau_lo, T), (tau_hi, T), d)
                    counts["b1"] += b1; counts["b2"] += b2; counts["b3"] += b3
                    counts["cases"] += 1
                    counts["cases_with_b3"] += int(b3 > 0)
                    counts["cases_with_b2"] += int(b2 > 0)
        for tau in (0.04, 0.06, 0.08):
            for Tp, Tm in ((1, 2), (2, 3)):
                for d in range(mod.H + 1):
                    b1, b2, b3 = branch_counts(mod, (tau, Tp), (tau, Tm), d)
                    counts["b1"] += b1; counts["b2"] += b2; counts["b3"] += b3
                    counts["cases"] += 1
                    counts["cases_with_b3"] += int(b3 > 0)
                    counts["cases_with_b2"] += int(b2 > 0)
    rec["branch_coverage"] = counts

    # Part 2: the alternative convention, tested by the LP
    alt = {"cases": 0, "feasible": 0, "infeasible": []}
    for trial in range(12):
        mod = ac.random_model(H=2, K=4, rng=rng)
        for kappa in (0.2, 0.6, 0.9):
            for tight, loose in (((0.04, 1), (0.08, 1)), ((0.06, 1), (0.06, 2))):
                Lp = alt_experiment(mod, *tight, kappa, mod.H)
                Lm = alt_experiment(mod, *loose, kappa, mod.H)
                ok, _ = ac.is_garbling(Lp, Lm)
                alt["cases"] += 1
                alt["feasible"] += int(ok)
                if not ok:
                    alt["infeasible"].append([trial, kappa, tight, loose])
    rec["alternative_convention"] = alt

    # Part 3: does the looser experiment ever garble to the tighter one?
    # (a strict-order probe: the reverse should fail once anything is caught)
    rev = {"cases": 0, "reverse_feasible": 0}
    for trial in range(10):
        mod = ac.random_model(H=2, K=4, rng=rng)
        for kappa in (0.3, 0.7):
            Lp, _, _ = ac.experiment(mod, 0.04, 1, kappa, mod.H)
            Lm, _, _ = ac.experiment(mod, 0.08, 1, kappa, mod.H)
            b1, b2, b3 = branch_counts(mod, (0.04, 1), (0.08, 1), mod.H)
            if b3 == 0:
                continue
            ok, _ = ac.is_garbling(Lm, Lp)
            rev["cases"] += 1
            rev["reverse_feasible"] += int(ok)
    rec["reverse_order"] = rev

    with open(OUT, "w") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print(json.dumps(rec, indent=1, default=str))


if __name__ == "__main__":
    main()
