"""Randomised test of the memo's Part 2 implication (R1)-(R3) => band."""
import numpy as np, json
from pathlib import Path
rng = np.random.default_rng(7)
H = 10
def one_crossing(neg_to_pos, rng):
    j = rng.integers(1, H+1)          # first index with the second sign
    mag = np.exp(rng.normal(0, 3, H+1))
    s = np.array([-1.0]*j + [1.0]*(H+1-j)) if neg_to_pos else np.array([1.0]*j + [-1.0]*(H+1-j))
    return s*mag
bad = 0; trials = 0; worst = 0.0
for _ in range(200000):
    cA = one_crossing(True, rng)
    d  = one_crossing(False, rng)
    cR = cA + d
    # cR must itself satisfy (R1)
    sg = [int(np.sign(t)) for t in cR if abs(t) > 0]
    if len(sg) < 2 or sg[0] != -1 or sg[-1] != 1: continue
    if sum(a != b for a, b in zip(sg, sg[1:])) != 1: continue
    rts = []
    ok = True
    for v in (cA, cR, d):
        r = [t.real for t in np.roots(v) if abs(t.imag) < 1e-9 and t.real > 0]
        if len(r) != 1: ok = False; break
        rts.append(r[0])
    if not ok: continue
    rstar = max(rts)
    x = rstar*(1.0 + abs(rng.normal(0, 1)))       # strictly above the cutoff
    if x <= rstar: continue
    trials += 1
    eps = x/(1.0+x)                                # x = eps/(1-eps)
    kappa = 2*eps
    if not (0 < kappa < 1): continue
    sA = -0.5*(1-eps)**H*np.polyval(cA, x)
    sR = -0.5*(1-eps)**H*np.polyval(cR, x)
    phi = float(rng.uniform(1e-4, 1-1e-4))
    sB = (sA - (1-phi)*sR)/phi
    scale = max(abs(sA), abs(sR), 1e-300)
    cond = (sA >= -1e-12*scale and sR >= -1e-12*scale and sR <= sA + 1e-12*scale
            and sB >= sA - 1e-9*abs(sB) and sB <= sA/phi + 1e-9*abs(sB)
            and (sB-sA)*(phi*sB-(2-phi)*sA) <= 1e-9*abs(sB*sA)
            and abs(sR)/abs(sA) <= 1 + 1e-9)
    if not cond:
        bad += 1
        worst = max(worst, abs(sR)/abs(sA))
print(json.dumps({"trials": trials, "violations": bad, "worst_C_tau": worst}))
