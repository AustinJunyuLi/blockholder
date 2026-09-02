"""Does the new order have bite at the paper's frozen grid?

Runs from the repository root:

    PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/3-blackwell-tightening/attack_bite.py

Compares the flagged signal sets across the reported threshold ladder and the
two windows, on a fine signal grid.  menu.py only; no enumeration.
"""

from __future__ import annotations

import json
import os

import numpy as np

from numerical_v4.menu import VOICE, atoms, legal_clock, n_days
from numerical_v4.params import ParamsV4

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attack_bite.json")


def main():
    prov = json.load(open(
        "numerical_v4/checks/t2_threshold_revelation_check.json"))["provenance"]
    k = tuple(prov["frozen_k"])
    ladder = prov["tau_ladder"]
    p0 = ParamsV4()
    grid = np.linspace(p0.mu_v - 6 * p0.sigma_s, p0.mu_v + 6 * p0.sigma_s, 60001)
    rec = {"frozen_k": list(k), "tau_ladder": ladder, "sets": {}}
    masks = {}
    for T in prov["T_grid"]:
        for tau in ladder:
            p = ParamsV4(tau=float(tau), T=int(T))
            m = np.array([legal_clock(VOICE, float(s), p).D == 1 and s >= k[1]
                          for s in grid])
            masks[(T, round(float(tau), 6))] = m
            lo = float(grid[m].min()) if m.any() else float("nan")
            al = atoms(k, p)
            rec["sets"][f"T={T},tau={tau:.6f}"] = {
                "flagged_s_min": lo,
                "n_flagged_grid": int(m.sum()),
                "omega": float(sum(a.w for a in al if a.D == 1)),
                "n_at_lo": int(n_days(lo, p)) if m.any() else -1,
            }
    keys = sorted(masks)
    rec["pairwise_equal"] = {
        f"{a} vs {b}": bool(np.array_equal(masks[a], masks[b]))
        for i, a in enumerate(keys) for b in keys[i + 1:]
    }
    with open(OUT, "w") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print(json.dumps(rec, indent=1, default=str))


if __name__ == "__main__":
    main()
