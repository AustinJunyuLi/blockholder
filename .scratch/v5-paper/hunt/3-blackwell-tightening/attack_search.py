"""Independent search for a counterexample to the memo's theorem.

Runs from the repository root:

    PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/3-blackwell-tightening/attack_search.py

The class is wider than attack_check.py: any weakly increasing stake path, any
binary mark path the coarsening Gamma(x) = 1{x >= gamma_bar} can produce, and a
strictly increasing composed terminal target on the flagged region, which is
(S14).  The test is the linear programme, so it asks whether ANY row-stochastic
kernel works, not whether the memo's kernel works.

It also re-tests the memo's necessity example under the alternative convention
in which a flagged path keeps its pre-filing pooled history.
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

OUT = os.path.join(_here, "attack_search.json")
RNG = np.random.default_rng(4242)


class WideModel:
    """Monotone stake paths, arbitrary binary marks, strict terminal target."""

    def __init__(self, H, b0, paths, marks, a, w):
        self.H = H
        self.b0 = b0
        self.paths = paths          # (K, H+1) stake at dates 0..H
        self.mk = marks             # (K, H+1) binary marks
        self.a = a
        self.w = w
        self.K = len(a)

    def marks(self, i):
        return self.mk[i]

    def clock(self, i, tau, T):
        if self.a[i] == 0:
            return (float("inf"), float("inf"), 0, None, None)
        c = None
        for d in range(self.H + 1):
            if self.paths[i, d] >= tau:
                c = d
                break
        if c is None:
            return (float("inf"), float("inf"), 0, None, None)
        f = c + T
        if f > self.H:
            return (float(c), float(f), 0, None, None)
        BF = float(self.paths[i, f])
        return (float(c), float(f), 1, BF, float(self.paths[i, self.H] - BF))


def wide_model(H=2, K=4, rng=RNG):
    """Draw a model in the class; b* strictly increasing across types."""
    b0 = 0.03
    while True:
        inc = rng.uniform(0.0, 0.04, size=(K, H + 1))
        inc[rng.uniform(size=inc.shape) < 0.35] = 0.0      # idle dates
        paths = b0 + np.cumsum(inc, axis=1)
        order = np.argsort(paths[:, H])
        paths = paths[order]
        inc = inc[order]
        if np.min(np.diff(paths[:, H])) < 1e-6:
            continue                                       # need strict target
        if not np.all(np.diff(paths, axis=0) >= -1e-12):
            continue                                       # monotone in signal
        gamma_bar = float(rng.uniform(0.004, 0.02))
        marks = (inc >= gamma_bar).astype(int)
        a = np.ones(K, int)
        a[rng.uniform(size=K) < 0.25] = 0
        a[-1] = 1
        marks[a == 0] = 0
        w = rng.uniform(0.5, 1.5, K)
        return WideModel(H, b0, paths, marks, a, w / w.sum())


def alt_necessity(kappa):
    """The memo's necessity example when the flagged path keeps its history."""
    H = 2
    BL = [0.0, 0.0, 1.0, 2.0]
    BU = [0.0, 0.5, 1.0, 2.0]
    mL = [1 if BL[d + 1] - BL[d] >= 0.75 else 0 for d in range(H + 1)]
    mU = [1 if BU[d + 1] - BU[d] >= 0.75 else 0 for d in range(H + 1)]
    f = 2                                    # both file at date 2 (T' = 1)

    def rows(spans, marks_list):
        cols, out = {}, []
        for m, span in zip(marks_list, spans):
            laws = [ac.flow_law(m[e], kappa) for e in range(span)]
            entries = {}
            for h in itertools.product(range(5), repeat=span):
                pr = 1.0
                for e in range(span):
                    pr *= laws[e][h[e]]
                if pr > 0:
                    entries[(span,) + h] = pr
            out.append(entries)
            for k in entries:
                cols.setdefault(k, len(cols))
        L = np.zeros((len(out), len(cols)))
        for i, e in enumerate(out):
            for k, pr in e.items():
                L[i, cols[k]] = pr
        return L

    # tighter: the constant tuple plus the pre-filing history over rounds 0..f-1
    Lp = rows([f, f], [mL, mU])
    # looser: both pooled over rounds 0..H
    Lm = rows([H + 1, H + 1], [mL, mU])
    ok, _ = ac.is_garbling(Lp, Lm)
    return bool(ok)


def main():
    rec = {"searched": 0, "counterexamples": [], "infeasible_cases": 0,
           "cases_with_reclassification": 0}
    taus = (0.04, 0.055, 0.07, 0.09)
    for trial in range(120):
        mod = wide_model(H=2, K=4)
        pairs = [(("tau", lo, hi, T), (lo, T), (hi, T))
                 for lo, hi in itertools.combinations(taus, 2) for T in (1, 2)]
        pairs += [(("T", tau, Tp, Tm), (tau, Tp), (tau, Tm))
                  for tau in taus for Tp, Tm in ((1, 2), (1, 3), (2, 3))]
        for tag, tight, loose in pairs:
            for kappa in (0.0, 0.25, 0.6, 1.0):
                for d in range(mod.H + 1):
                    Lp, _, _ = ac.experiment(mod, tight[0], tight[1], kappa, d)
                    Lm, _, _ = ac.experiment(mod, loose[0], loose[1], kappa, d)
                    nf_p = sum(1 for i in range(mod.K)
                               if mod.clock(i, *tight)[2] == 1
                               and mod.clock(i, *tight)[1] <= d)
                    nf_m = sum(1 for i in range(mod.K)
                               if mod.clock(i, *loose)[2] == 1
                               and mod.clock(i, *loose)[1] <= d)
                    rec["searched"] += 1
                    if nf_p > nf_m:
                        rec["cases_with_reclassification"] += 1
                    ok, _ = ac.is_garbling(Lp, Lm)
                    if not ok:
                        rec["infeasible_cases"] += 1
                        if len(rec["counterexamples"]) < 5:
                            rec["counterexamples"].append({
                                "tag": list(map(str, tag)), "kappa": kappa,
                                "d": d,
                                "paths": mod.paths.tolist(),
                                "marks": mod.mk.tolist(),
                                "a": mod.a.tolist()})
    # True means a kernel exists, so under that convention the memo's
    # necessity example is not a counterexample.
    rec["alt_convention_tighter_garbles_to_looser"] = {
        str(k): alt_necessity(k) for k in (0.0, 0.3, 0.6, 1.0)}
    with open(OUT, "w") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print(json.dumps({k: v for k, v in rec.items()
                      if k != "counterexamples"}, indent=1, default=str))
    print("counterexamples:", json.dumps(rec["counterexamples"], indent=1)[:2000])


if __name__ == "__main__":
    main()
