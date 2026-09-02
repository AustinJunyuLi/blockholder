"""
Fifth attack check, exact rational arithmetic and no LP.

For a two state experiment the Blackwell order is the convex order on the distribution of the
posterior under a uniform prior: E is a garbling of E' if and only if the posterior law under E'
is a mean preserving spread of the posterior law under E.  This checks, in exact fractions,
whether the order size one experiment at kappa is a garbling of the one at kappa' for the two
round mark paths (0,0) and (1,1), at pairs the memo's one round rule excludes.

Runs from the repository root:
    PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/1-erasure-regime/attack_check5.py
"""

import itertools
import json
from fractions import Fraction as F


def rows(kappa, q):
    """Exact (P(x|m=0), P(x|m=1)) over all flow histories of length q, order size one."""
    a, c = kappa / 2, 1 - kappa
    one = [(a, F(0)), (c, a), (a, c), (F(0), a)]        # flows -1, 0, 1, 2
    out = []
    for h in itertools.product(range(4), repeat=q):
        p0, p1 = F(1), F(1)
        for e in h:
            p0 *= one[e][0]
            p1 *= one[e][1]
        if p0 or p1:
            out.append((p0, p1))
    return out


def posterior_law(kappa, q):
    """List of (weight, posterior on state 0) under the uniform prior, exact."""
    law = {}
    for p0, p1 in rows(kappa, q):
        w = (p0 + p1) / 2
        if w == 0:
            continue
        p = p0 / (p0 + p1)
        law[p] = law.get(p, F(0)) + w
    return sorted(law.items())


def convex_order(low, high):
    """True iff `high` is a mean preserving spread of `low` (so low is a garbling of high)."""
    mean_l = sum(w * p for p, w in low)
    mean_h = sum(w * p for p, w in high)
    if mean_l != mean_h:
        return False, "means differ"
    ts = sorted({p for p, _ in low} | {p for p, _ in high})
    for t in ts:
        cl = sum(w * max(p - t, F(0)) for p, w in low)
        ch = sum(w * max(p - t, F(0)) for p, w in high)
        if ch < cl:
            return False, f"call payoff at t={t} : high {ch} < low {cl}"
    return True, "all call payoffs weakly larger at the higher node"


out = {}
for name, ka, kb in [("0.55->0.70", F(55, 100), F(70, 100)),
                     ("0.62->0.68", F(62, 100), F(68, 100)),
                     ("0.45->0.75", F(45, 100), F(75, 100)),
                     ("0.50->0.60", F(50, 100), F(60, 100)),
                     ("0.20->0.40", F(20, 100), F(40, 100))]:
    entry = {"two_kb_plus_ka": str(2 * kb + ka),
             "one_round_rule_allows": bool(2 * kb + ka >= 2)}
    for q in (1, 2, 3):
        ok, why = convex_order(posterior_law(ka, q), posterior_law(kb, q))
        entry[f"q={q}_low_is_exact_garbling_of_high"] = [ok, why]
    out[name] = entry

print(json.dumps(out, indent=2))
