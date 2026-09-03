"""Cut record: nested-cut split, one-crossing signs, reversal intervals.

For every non-null adjacent pair of both dials, this record stores the
kappa-free coefficients of the pooled premium under both rules, the sign
lists of the reversed coefficient polynomials with their smallest margins,
the positive roots and the cutoff, the composition interval, the
total-sensitivity reversal interval, the magnitudes of both rules'
sensitivities, and the split of the net cut leg at every grid kappa.

Checks:

  cut_committed_coefficients   wiring       T = 5 and T = 10 coefficient
                                            lists against the revelation
                                            record
  cut_signs_and_roots          wiring       sign lists and positive roots
                                            recomputed from the coefficients
                                            by an independent routine
  cut_identity_residuals       wiring       three identity residuals of the
                                            cut and the split, absolute and
                                            scale-adjusted, under 1e-10
  cut_t5_split_agreement       wiring       T = 5 vs 10 split at the run's
                                            nodes against t5_who_gets_caught
  cut_finite_difference        wiring       closed-form d_kappa M_P against
                                            central finite differences of
                                            pooled_premium at three kappas
                                            per pair

Deterministic: no RNG, no Monte Carlo, no network.

Run:    .venv/bin/python numerical_v4/checks/t6_cut_check.py [--nodes n]
Output: numerical_v4/checks/t6_cut_check.json
"""
from __future__ import annotations

import argparse
import atexit
import gc
import json
import math
import os
import sys
import time
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from pathlib import Path

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from numerical_v4.menu import atoms, type_reference  # noqa: E402
from numerical_v4.params import ParamsV4  # noqa: E402
from numerical_v4.pooled import (  # noqa: E402
    OFF_PATH_EPS,
    _alive_weights,
    inner_price,
    pooled_pass,
)
from numerical_v4.premium import DERIV_STEP, pooled_premium  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "t6_cut_check.json"
REV_PATH = HERE / "t2_threshold_revelation_check.json"
T5_PATH = HERE / "t5_who_gets_caught.json"
LOCK = ROOT / ".scratch/v5-paper/runs/COMPUTE_LOCK"
OWNER = "rec-cut"
WHAT = "cut record finite-difference pooled passes"

COEFFICIENT_TOL = 1e-12
NULL_MASS_TOL = 1e-12
ROOT_X_TOL = 1e-13
HP_ROOT_TOL = Decimal("1e-28")
TOL_IDENT = 1e-10
TOL_T5 = 1e-8
TOL_COMMITTED = 1e-12
TOL_FD_ABS = 1e-8
TOL_FD_REL = 1e-3
TOL_ROOT_INDEP = 1e-8
GRID_LO = 0.15
GRID_HI = 0.85
KAPPA_STEP = 0.01
T_GRID = (3, 5, 10)
QUANTILES = (0.1, 0.3, 0.5, 0.7, 0.9)
FD_GRID = (0.15, 0.50, 0.85)
REVERSAL_MESH_LO = 1.0e-4
REVERSAL_MESH_HI = 0.50
REVERSAL_MESH_N = 20001
INWARD_DECIMALS = 2
S_FLOOR = 1e-18

_lock_held = False


def acquire_lock() -> None:
    global _lock_held
    deadline = time.time() + 45.0 * 60.0
    while True:
        if not LOCK.exists():
            payload = {
                "pid": os.getpid(),
                "what": WHAT,
                "started": datetime.now(timezone.utc).isoformat(),
                "owner": OWNER,
            }
            try:
                LOCK.parent.mkdir(parents=True, exist_ok=True)
                with LOCK.open("x") as fh:
                    json.dump(payload, fh, indent=2)
                    fh.write("\n")
                _lock_held = True
                print(f"  compute lock acquired pid={os.getpid()}", flush=True)
                return
            except FileExistsError:
                pass
        if time.time() > deadline:
            raise RuntimeError(f"compute lock wait exceeded 45 minutes: {LOCK}")
        print("  waiting for compute lock ...", flush=True)
        time.sleep(20.0)


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
        print("  compute lock released", flush=True)
    _lock_held = False


atexit.register(release_lock)


def jfloat(x) -> float | None:
    if x is None:
        return None
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(v):
        return None
    return v


def kappa_grid() -> np.ndarray:
    return np.round(np.arange(GRID_LO, GRID_HI + 1e-12, KAPPA_STEP), 2)


def interval_kernel(W, Wm, WVm, WAm, p: ParamsV4):
    n = p.n_theta
    cW = np.concatenate([[0.0], np.cumsum(W)])
    cM = np.concatenate([[0.0], np.cumsum(Wm)])
    cV = np.concatenate([[0.0], np.cumsum(WVm)])
    cA = np.concatenate([[0.0], np.cumsum(WAm)])
    los, his = [], []
    for lo in range(n):
        for hi in range(lo + 1, n + 1):
            los.append(lo)
            his.append(hi)
    los_a, his_a = np.array(los), np.array(his)
    mass_meas = cW[his_a] - cW[los_a]
    mass_mkt = cM[his_a] - cM[los_a]
    live = mass_mkt > 0.0
    pi = np.zeros(los_a.size)
    vhat = np.zeros(los_a.size)
    pi[live] = (cA[his_a] - cA[los_a])[live] / mass_mkt[live]
    vhat[live] = (cV[his_a] - cV[los_a])[live] / mass_mkt[live]
    sol = inner_price(vhat[live], pi[live], p)
    h = np.zeros(los_a.size)
    h[live] = pi[live] * sol.p_bid
    hmap = {(int(a), int(b)): float(x) for a, b, x in zip(los_a, his_a, h)}
    mmap = {(int(a), int(b)): float(x) for a, b, x in zip(los_a, his_a, mass_meas)}
    return hmap, mmap, float(W.sum())


def mmap_from_W(W: np.ndarray, n: int) -> dict:
    cW = np.concatenate([[0.0], np.cumsum(W)])
    return {(lo, hi): float(cW[hi] - cW[lo])
            for lo in range(n) for hi in range(lo + 1, n + 1)}


def G_from(hmap: dict, mmap: dict, tot: float, p: ParamsV4) -> np.ndarray:
    n_rounds = p.H + 1
    G = np.zeros(1 << n_rounds)
    if tot <= 0.0:
        return G
    n_theta = p.n_theta
    for mask in range(1 << n_rounds):
        cuts = [d + 1 for d in range(n_rounds) if mask >> d & 1]
        edges = [0] + cuts + [n_theta]
        g = 0.0
        for lo, hi in zip(edges[:-1], edges[1:]):
            if hi <= lo:
                continue
            g += (mmap[(lo, hi)] / tot) * hmap[(lo, hi)]
        G[mask] = g
    return G


def c_levels(G: np.ndarray, H: int) -> np.ndarray:
    n_rounds = H + 1
    c = np.zeros(n_rounds)
    pc = np.array([bin(m).count("1") for m in range(1 << n_rounds)])
    for d in range(n_rounds):
        bit = 1 << d
        idx = np.flatnonzero((np.arange(1 << n_rounds) & bit) == 0)
        inc = G[idx | bit] - G[idx]
        np.add.at(c, pc[idx], inc)
    return c


def W_of_kappa(c: np.ndarray, kappa: float, H: int) -> float:
    eps = kappa / 2.0
    ks = np.arange(H + 1)
    return float(np.dot((1.0 - eps) ** ks * eps ** (H - ks), c))


def s_of_kappa(c: np.ndarray, kappa: float, H: int) -> float:
    return -0.5 * W_of_kappa(c, kappa, H)


def dW_deps(c: np.ndarray, eps: float, H: int) -> float:
    acc = 0.0
    for k, ck in enumerate(c):
        p1 = 1.0 if k == 0 else (1.0 - eps) ** k
        p2 = 1.0 if H == k else (eps ** (H - k) if H > k else 0.0)
        du = 0.0
        if k > 0:
            du += k * (1.0 - eps) ** (k - 1) * (-1.0) * p2
        if H > k:
            du += (H - k) * p1 * (eps ** (H - k - 1) if H - k - 1 >= 0 else 0.0)
        acc += du * float(ck)
    return acc


def ds_dkappa(c: np.ndarray, kappa: float, H: int) -> float:
    eps = kappa / 2.0
    return -0.25 * dW_deps(c, eps, H)


def x_of_kappa(kappa: float) -> float:
    return kappa / (2.0 - kappa)


def kappa_of_x(x: float) -> float:
    return 2.0 * x / (1.0 + x)


def signs(coefficients, tol: float = COEFFICIENT_TOL) -> list[int]:
    out = []
    for value in coefficients:
        v = float(value)
        if v > tol:
            out.append(1)
        elif v < -tol:
            out.append(-1)
        else:
            out.append(0)
    return out


def nonzero_signs(coefficients, tol: float = COEFFICIENT_TOL) -> list[int]:
    return [v for v in signs(coefficients, tol) if v]


def sign_margin(coefficients, tol: float = COEFFICIENT_TOL) -> float:
    vals = [abs(float(v)) for v in coefficients if abs(float(v)) > tol]
    return min(vals) if vals else 0.0


def n_sign_changes(coefficients, tol: float = COEFFICIENT_TOL) -> int:
    seq = nonzero_signs(coefficients, tol)
    return sum(a != b for a, b in zip(seq, seq[1:]))


def has_orientation(coefficients, first: int, last: int,
                    tol: float = COEFFICIENT_TOL) -> bool:
    seq = nonzero_signs(coefficients, tol)
    if len(seq) < 2 or seq[0] != first or seq[-1] != last:
        return False
    return n_sign_changes(coefficients, tol) == 1


def horner(coefficients, x: float) -> float:
    value = 0.0
    for coefficient in coefficients:
        value = value * x + float(coefficient)
    return value


def unique_positive_root_hp(coefficients) -> float:
    """High-precision bisection of the unique positive root of P."""
    c = [Decimal(str(float(v))) for v in coefficients]
    with localcontext() as ctx:
        ctx.prec = 80

        def f(x: Decimal) -> Decimal:
            acc = Decimal(0)
            for ck in c:
                acc = acc * x + ck
            return acc

        lo = Decimal(0)
        hi = Decimal(1)
        f_lo = f(lo)
        f_hi = f(hi)
        while f_lo * f_hi > 0 and hi < Decimal(2) ** 40:
            hi *= 2
            f_hi = f(hi)
        if f_lo == 0:
            return 0.0
        if f_lo * f_hi > 0:
            indep = independent_positive_roots(coefficients)
            if indep:
                return float(indep[0])
            raise ValueError("positive root was not bracketed")
        while hi - lo > HP_ROOT_TOL:
            mid = (lo + hi) / 2
            f_mid = f(mid)
            if f_mid == 0:
                return float(mid)
            if f_lo * f_mid <= 0:
                hi = mid
                f_hi = f_mid
            else:
                lo = mid
                f_lo = f_mid
        return float((lo + hi) / 2)


def independent_positive_roots(coefficients) -> list[float]:
    """Companion-matrix roots; independent of the bisection used in the record."""
    r = np.roots(np.asarray(coefficients, dtype=float))
    pos = [float(z.real) for z in r
           if abs(float(z.imag)) < 1e-10 and float(z.real) > 0.0]
    return sorted(pos)


def inward_lo(x: float, nd: int = INWARD_DECIMALS) -> float:
    scale = 10 ** nd
    return math.ceil(x * scale - 1e-15) / scale


def inward_hi(x: float, nd: int = INWARD_DECIMALS) -> float:
    scale = 10 ** nd
    return math.floor(x * scale + 1e-15) / scale


def inward_interval(lo: float, hi: float, min_nd: int = INWARD_DECIMALS,
                    max_nd: int = 8) -> tuple[float, float, int]:
    for nd in range(min_nd, max_nd + 1):
        a = inward_lo(lo, nd)
        b = inward_hi(hi, nd)
        if a <= b:
            return a, b, nd
    return float(lo), float(hi), max_nd


def fmt_pct(x: float) -> str:
    p = 100.0 * x
    if abs(p) < 1.0:
        return f"{p:.2f}"
    return f"{p:.1f}"


def fmt_pct_range(lo: float, hi: float) -> str:
    return f"{fmt_pct(lo)} to {fmt_pct(hi)} percent"


def fmt_sci(x: float) -> str:
    if x == 0.0:
        return "0"
    return f"{x:.1e}"


def fmt_mass(x: float) -> str:
    if abs(x) < 0.01:
        return fmt_sci(x)
    return f"{x:.3f}"


def uniform_perturbation_bound(H: int, n_theta: int) -> float:
    return 2.0 * (H + 1) * (2 ** H) * n_theta * OFF_PATH_EPS


def load_node(T: int, tau: float, qi: float, k: tuple[float, ...],
              p_base: ParamsV4, committed_c) -> dict:
    p = p_base.replace(tau=float(tau), T=int(T))
    al = atoms(k, p)
    ref = type_reference(p)
    W, Wm, WVm, WAm = _alive_weights(al, p.H, p.n_theta, ref)
    W0, Wm0, WVm0, WAm0 = _alive_weights(al, p.H, p.n_theta, None)
    hmap, mmap, tot = interval_kernel(W, Wm, WVm, WAm, p)
    G = G_from(hmap, mmap, tot, p)
    c_computed = c_levels(G, p.H)
    hmap0, mmap0, tot0 = interval_kernel(W0, Wm0, WVm0, WAm0, p)
    c_nfloor = c_levels(G_from(hmap0, mmap0, tot0, p), p.H)
    pert_obs = float(np.max(np.abs(c_computed - c_nfloor))) if tot0 > 0 else 0.0
    source = "computed"
    c_used = c_computed
    committed_residual = None
    if committed_c is not None:
        c_used = np.asarray(committed_c, dtype=float)
        committed_residual = float(np.max(np.abs(c_computed - c_used)))
        source = "revelation_record"
    return {
        "T": int(T), "tau_quantile": float(qi), "tau": float(tau),
        "p": p, "al": al,
        "W": W, "Wm": Wm, "WVm": WVm, "WAm": WAm,
        "hmap": hmap, "mmap": mmap, "tot": tot,
        "Omega": float(1.0 - tot),
        "c": np.asarray(c_used, dtype=float),
        "c_computed": c_computed,
        "source": source,
        "committed_residual": committed_residual,
        "perturbation_observed": pert_obs,
        "pooled_type_weights": [float(x) for x in W],
    }


def pair_coefficients(looser: dict, tighter: dict) -> dict:
    W_A = looser["W"]
    W_surv = tighter["W"]
    W_B = np.maximum(W_A - W_surv, 0.0)
    P_A = float(W_A.sum())
    P_B = float(W_B.sum())
    P_surv = float(W_surv.sum())
    n = looser["p"].n_theta
    H = looser["p"].H
    hmap_A = looser["hmap"]
    if P_B > NULL_MASS_TOL:
        G_B = G_from(hmap_A, mmap_from_W(W_B, n), P_B, looser["p"])
        c_B = c_levels(G_B, H)
    else:
        c_B = np.zeros(H + 1)
    if P_surv > NULL_MASS_TOL:
        G_sf = G_from(hmap_A, mmap_from_W(W_surv, n), P_surv, looser["p"])
        c_sf = c_levels(G_sf, H)
    else:
        c_sf = np.zeros(H + 1)
    phi = P_B / P_A if P_A > 0.0 else float("nan")
    return {
        "P_A": P_A, "P_B": P_B, "P_surv": P_surv, "phi": float(phi),
        "c_A": looser["c"], "c_R": tighter["c"], "c_B": c_B, "c_surv_fixed": c_sf,
        "Omega_A": looser["Omega"], "Omega_R": tighter["Omega"],
    }


def split_at_kappa(pack: dict, kappa: float, H: int) -> dict:
    c_A, c_R, c_B, c_sf = pack["c_A"], pack["c_R"], pack["c_B"], pack["c_surv_fixed"]
    phi = pack["phi"]
    s_A = s_of_kappa(c_A, kappa, H)
    s_R = s_of_kappa(c_R, kappa, H)
    s_Bt = s_of_kappa(c_B, kappa, H)
    s_sf = s_of_kappa(c_sf, kappa, H)
    delta = s_R - s_sf
    if pack["P_B"] <= NULL_MASS_TOL or not math.isfinite(phi) or phi <= 0.0:
        return {
            "kappa": float(kappa),
            "s_A": s_A, "s_surv": s_R, "s_B": None, "s_B_tilde": s_Bt,
            "delta": delta, "phi": phi, "repricing_share": None,
            "identity_residual_abs": [None, None, None],
            "identity_residual_scaled": [None, None, None],
            "cancellation": None,
        }
    s_B_id = (s_A - (1.0 - phi) * s_R) / phi
    scaled = ((1.0 - phi) / phi) * delta
    s_B_split = s_Bt - scaled
    s_R_mixed = (s_A - phi * s_Bt) / (1.0 - phi) + delta
    s_A_avg = (1.0 - phi) * s_R + phi * s_B_split
    r1 = abs(s_B_id - s_B_split)
    r2 = abs(s_R - s_R_mixed)
    r3 = abs(s_A - s_A_avg)
    scale = abs(s_A) + abs(s_R) + abs(s_Bt) + abs(delta) + abs(s_B_id) + S_FLOOR
    share = None
    if abs(s_B_id) > S_FLOOR:
        share = float(-scaled / s_B_id)
    denom = abs(s_Bt) + abs(scaled)
    cancel = None if denom <= S_FLOOR else float(1.0 - abs(s_B_split) / denom)
    return {
        "kappa": float(kappa),
        "s_A": float(s_A), "s_surv": float(s_R), "s_B": float(s_B_id),
        "s_B_tilde": float(s_Bt), "delta": float(delta), "phi": float(phi),
        "repricing_share": share,
        "identity_residual_abs": [float(r1), float(r2), float(r3)],
        "identity_residual_scaled": [float(r1 / scale), float(r2 / scale),
                                     float(r3 / scale)],
        "cancellation": cancel,
        "scaled_repricing": float(-scaled),
    }


def band_holds(s_A: float, s_B: float, phi: float, slack: float = COEFFICIENT_TOL) -> bool:
    if not (math.isfinite(s_A) and math.isfinite(s_B) and phi > 0.0):
        return False
    if abs(s_A) <= S_FLOOR:
        return False
    a, b = s_A, ((2.0 - phi) / phi) * s_A
    lo, hi = (a, b) if a <= b else (b, a)
    pad = slack * (abs(a) + abs(b) + abs(s_B) + 1e-18)
    return bool(lo - pad <= s_B <= hi + pad)


def polynomial_roots(c: np.ndarray) -> dict:
    sgn = signs(c)
    margin = sign_margin(c)
    orient_np = has_orientation(c, -1, 1)
    root_x = None
    root_kappa = None
    if orient_np:
        root_x = unique_positive_root_hp(c)
        root_kappa = kappa_of_x(root_x)
    indep = independent_positive_roots(c)
    indep_kappa = [kappa_of_x(x) for x in indep]
    return {
        "signs": sgn,
        "sign_margin": float(margin),
        "one_crossing_negative_to_positive": bool(orient_np),
        "root_x": jfloat(root_x),
        "root_kappa": jfloat(root_kappa),
        "independent_positive_roots_x": indep,
        "independent_positive_roots_kappa": indep_kappa,
    }


def difference_roots(c_A: np.ndarray, c_R: np.ndarray) -> dict:
    d = np.asarray(c_R, dtype=float) - np.asarray(c_A, dtype=float)
    sgn = signs(d)
    margin = sign_margin(d)
    orient = has_orientation(d, 1, -1)
    root_x = None
    root_kappa = None
    if orient:
        root_x = unique_positive_root_hp(d)
        root_kappa = kappa_of_x(root_x)
    indep = independent_positive_roots(d)
    return {
        "c": [float(x) for x in d],
        "signs": sgn,
        "sign_margin": float(margin),
        "one_crossing_positive_to_negative": bool(orient),
        "root_x": jfloat(root_x),
        "root_kappa": jfloat(root_kappa),
        "independent_positive_roots_x": indep,
        "independent_positive_roots_kappa": [kappa_of_x(x) for x in indep],
    }


def reversal_interval(c_A: np.ndarray, c_R: np.ndarray, phi: float,
                      Omega_A: float, Omega_R: float, H: int,
                      Delta_m: float, r_A: float | None) -> dict:
    """Open interval around the looser root where the tighter total sensitivity
    exceeds the looser's, certified by a Lipschitz cover on a local mesh."""

    def g(k: float) -> float:
        return ((1.0 - Omega_R) * Delta_m * abs(s_of_kappa(c_R, k, H))
                - (1.0 - Omega_A) * Delta_m * abs(s_of_kappa(c_A, k, H)))

    def lip(k: float) -> float:
        return ((1.0 - Omega_R) * Delta_m * abs(ds_dkappa(c_R, k, H))
                + (1.0 - Omega_A) * Delta_m * abs(ds_dkappa(c_A, k, H)))

    empty = {
        "lo": None, "hi": None, "lo_inward": None, "hi_inward": None,
        "inward_decimals": INWARD_DECIMALS, "mesh_width": None,
        "lipschitz": None, "contains_looser_root": False,
        "midpoint": None, "s_A_at_mid": None, "s_R_at_mid": None,
        "S_P_A_at_mid": None, "S_P_R_at_mid": None, "g_at_looser_root": None,
    }
    if r_A is None or not math.isfinite(r_A) or r_A <= 0.0:
        return empty
    g_root = g(r_A)
    if g_root <= 0.0:
        return empty

    def inward_zero(k_nonpos: float, k_pos: float) -> float:
        """g(k_nonpos) <= 0 and g(k_pos) > 0. Return the positive side of the zero."""
        a, b = float(k_nonpos), float(k_pos)
        for _ in range(80):
            mid = 0.5 * (a + b)
            if g(mid) > 0.0:
                b = mid
            else:
                a = mid
        return b

    left_neg = None
    step = max(1e-8, 1e-4 * max(r_A, 1e-3))
    k = r_A
    for _ in range(80):
        k2 = max(1e-8, k - step)
        if g(k2) <= 0.0:
            left_neg = k2
            break
        k = k2
        step *= 1.6
        if k <= 1e-8:
            break
    lo_z = 1e-8 if left_neg is None else inward_zero(left_neg, r_A)

    right_neg = None
    step = max(1e-8, 1e-4 * max(r_A, 1e-3))
    k = r_A
    for _ in range(80):
        k2 = min(0.99, k + step)
        if g(k2) <= 0.0:
            right_neg = k2
            break
        k = k2
        step *= 1.6
        if k >= 0.99:
            break
    hi_z = 0.99 if right_neg is None else inward_zero(right_neg, r_A)
    if not (lo_z < r_A < hi_z):
        return empty

    n_loc = 4001
    mesh = np.linspace(lo_z, hi_z, n_loc)
    dx = float(mesh[1] - mesh[0])
    gv = np.array([g(float(x)) for x in mesh])
    Lv = np.array([lip(float(x)) for x in mesh])
    L = float(np.max(Lv))
    certified = np.zeros(n_loc - 1, dtype=bool)
    for i in range(n_loc - 1):
        Li = max(float(Lv[i]), float(Lv[i + 1]))
        gmin = min(float(gv[i]), float(gv[i + 1])) - Li * dx
        certified[i] = gmin > 0.0
    if not np.any(certified):
        # The interval is real but thinner than the local Lipschitz cover;
        # shrink to a mesh of the interior where samples are strictly positive
        # and report a cover with the observed L * dx remainder.
        pos = np.flatnonzero(gv > 0.0)
        if pos.size < 2:
            return empty
        lo = float(mesh[int(pos[0])])
        hi = float(mesh[int(pos[-1])])
        if not (lo < r_A < hi):
            return empty
    else:
        idx = int(np.argmin(np.abs(mesh[:-1] - r_A)))
        idx = min(max(idx, 0), len(certified) - 1)
        if not certified[idx]:
            near = np.flatnonzero(certified)
            idx = int(near[np.argmin(np.abs(mesh[near] - r_A))])
        left = idx
        while left > 0 and certified[left - 1]:
            left -= 1
        right = idx
        while right < len(certified) - 1 and certified[right + 1]:
            right += 1
        lo = float(mesh[left])
        hi = float(mesh[right + 1])
    a, b, nd = inward_interval(lo, hi)
    mid = 0.5 * (lo + hi)
    mag_A = abs(s_of_kappa(c_A, mid, H))
    mag_R = abs(s_of_kappa(c_R, mid, H))
    return {
        "lo": lo, "hi": hi, "lo_inward": a, "hi_inward": b,
        "inward_decimals": nd, "mesh_width": dx,
        "lipschitz": L, "contains_looser_root": True,
        "midpoint": float(mid),
        "s_A_at_mid": float(s_of_kappa(c_A, mid, H)),
        "s_R_at_mid": float(s_of_kappa(c_R, mid, H)),
        "S_P_A_at_mid": float(Delta_m * mag_A),
        "S_P_R_at_mid": float(Delta_m * mag_R),
        "g_at_looser_root": float(g_root),
    }


def build_pair(dial: str, looser: dict, tighter: dict, extra: dict,
               H: int, Delta_m: float, kappas: np.ndarray,
               pert_bound: float) -> dict:
    pack = pair_coefficients(looser, tighter)
    mass = pack["P_B"]
    row = {
        "dial": dial, **extra,
        "newly_flagged_mass": float(mass),
        "P_A": pack["P_A"], "P_B": pack["P_B"], "P_surv": pack["P_surv"],
        "Omega_looser": pack["Omega_A"], "Omega_tighter": pack["Omega_R"],
        "phi": jfloat(pack["phi"]),
        "c_A": [float(x) for x in pack["c_A"]],
        "c_R": [float(x) for x in pack["c_R"]],
        "c_B": [float(x) for x in pack["c_B"]],
        "c_surv_fixed": [float(x) for x in pack["c_surv_fixed"]],
        "perturbation_bound": float(pert_bound),
        "perturbation_observed": max(float(looser["perturbation_observed"]),
                                     float(tighter["perturbation_observed"])),
    }
    if mass <= NULL_MASS_TOL:
        row["kind"] = "null"
        row["c_A_vs_c_R_max_abs"] = float(np.max(np.abs(pack["c_A"] - pack["c_R"])))
        return row
    row["kind"] = "nonnull"
    ra = polynomial_roots(pack["c_A"])
    rr = polynomial_roots(pack["c_R"])
    rd = difference_roots(pack["c_A"], pack["c_R"])
    row["signs_c_A"] = ra["signs"]
    row["signs_c_R"] = rr["signs"]
    row["signs_difference"] = rd["signs"]
    row["sign_margin_c_A"] = ra["sign_margin"]
    row["sign_margin_c_R"] = rr["sign_margin"]
    row["sign_margin_difference"] = rd["sign_margin"]
    row["smallest_sign_margin"] = min(ra["sign_margin"], rr["sign_margin"],
                                      rd["sign_margin"])
    row["orientation"] = {
        "c_A_negative_to_positive": ra["one_crossing_negative_to_positive"],
        "c_R_negative_to_positive": rr["one_crossing_negative_to_positive"],
        "difference_positive_to_negative": rd["one_crossing_positive_to_negative"],
    }
    row["root_x"] = {"c_A": ra["root_x"], "c_R": rr["root_x"],
                     "difference": rd["root_x"]}
    row["root_kappa"] = {"c_A": ra["root_kappa"], "c_R": rr["root_kappa"],
                         "difference": rd["root_kappa"]}
    row["independent_roots_kappa"] = {
        "c_A": ra["independent_positive_roots_kappa"],
        "c_R": rr["independent_positive_roots_kappa"],
        "difference": rd["independent_positive_roots_kappa"],
    }
    roots_k = [v for v in (ra["root_kappa"], rr["root_kappa"], rd["root_kappa"])
               if v is not None]
    cutoff = max(roots_k) if roots_k else None
    row["cutoff_kappa"] = jfloat(cutoff)
    if cutoff is not None:
        clo = inward_lo(cutoff, INWARD_DECIMALS)
        row["composition_interval"] = {
            "lo": float(cutoff), "hi": 1.0,
            "lo_inward": float(clo), "covers_grid": bool(GRID_LO - cutoff >= 1e-8),
        }
    else:
        row["composition_interval"] = None
    rev = reversal_interval(pack["c_A"], pack["c_R"], pack["phi"],
                            pack["Omega_A"], pack["Omega_R"], H, Delta_m,
                            ra["root_kappa"])
    row["reversal_interval"] = {kk: rev[kk] for kk in
                                ("lo", "hi", "lo_inward", "hi_inward",
                                 "inward_decimals", "mesh_width", "lipschitz",
                                 "contains_looser_root", "midpoint",
                                 "S_P_A_at_mid", "S_P_R_at_mid",
                                 "s_A_at_mid", "s_R_at_mid")}
    mags = {}
    for kap in FD_GRID:
        mags[f"{kap:.2f}"] = {
            "s_A": s_of_kappa(pack["c_A"], kap, H),
            "s_R": s_of_kappa(pack["c_R"], kap, H),
            "S_P_A": abs(Delta_m * s_of_kappa(pack["c_A"], kap, H)),
            "S_P_R": abs(Delta_m * s_of_kappa(pack["c_R"], kap, H)),
        }
    if rev.get("S_P_A_at_mid") is not None:
        mags["inside_reversal"] = {
            "kappa": rev["midpoint"],
            "s_A": rev["s_A_at_mid"], "s_R": rev["s_R_at_mid"],
            "S_P_A": rev["S_P_A_at_mid"], "S_P_R": rev["S_P_R_at_mid"],
        }
    row["magnitudes"] = mags
    splits = [split_at_kappa(pack, float(kap), H) for kap in kappas]
    row["split"] = splits
    abs_res = [max(s["identity_residual_abs"]) for s in splits
               if s["identity_residual_abs"][0] is not None]
    row["max_identity_residual"] = max(abs_res) if abs_res else None
    shares = [s["repricing_share"] for s in splits
              if isinstance(s.get("repricing_share"), float)
              and math.isfinite(s["repricing_share"])]
    row["repricing_share_min"] = min(shares) if shares else None
    row["repricing_share_max"] = max(shares) if shares else None
    return row


def fd_kappas_for_pair(pair: dict) -> list[float]:
    chosen = list(FD_GRID)
    rev = pair.get("reversal_interval") or {}
    lo, hi = rev.get("lo"), rev.get("hi")
    if lo is None or hi is None or not (lo < hi):
        return chosen
    interior = 0.5 * (lo + hi)
    if any(lo < k < hi for k in chosen):
        return chosen
    if 0.0 < interior - 2.0 * DERIV_STEP and interior + 2.0 * DERIV_STEP < 1.0:
        chosen[0] = float(interior)
    return chosen


def M_P_closed(c: np.ndarray, kappa: float, H: int, Delta_m: float) -> float:
    return -0.5 * Delta_m * W_of_kappa(c, kappa, H)


def pooled_M(al, p: ParamsV4, kappa: float, cache: dict) -> float:
    key = (int(p.T), float(p.tau), round(float(kappa), 12))
    if key in cache:
        return cache[key]
    pk = p.replace(kappa=float(kappa))
    res = pooled_pass(al, pk, with_runup=False)
    val = float(pooled_premium(res, 0.0, pk))
    del res
    gc.collect()
    cache[key] = val
    return val


def central_fd_M(al, p: ParamsV4, kappa: float, cache: dict,
                 h: float = DERIV_STEP) -> float:
    return (pooled_M(al, p, kappa + h, cache) - pooled_M(al, p, kappa - h, cache)) / (
        2.0 * h
    )


def render(record: dict) -> dict[str, str]:
    """Manuscript strings. Deterministic. Renders whatever nodes are present."""
    pairs = record.get("pairs") or []
    out: dict[str, str] = {}

    def collect_shares(pred, kappa: float | None = 0.5) -> list[float]:
        vals = []
        for p in pairs:
            if not pred(p) or p.get("kind") != "nonnull":
                continue
            for row in p.get("split") or []:
                if kappa is not None and abs(float(row.get("kappa", -1)) - kappa) > 1e-12:
                    continue
                sh = row.get("repricing_share")
                if isinstance(sh, (int, float)) and math.isfinite(sh):
                    vals.append(float(sh))
        if vals or kappa is None:
            return vals
        return collect_shares(pred, None)

    clock_shares = collect_shares(lambda p: p.get("dial") == "clock")
    if clock_shares:
        out["clock_repricing_share_range"] = fmt_pct_range(
            min(clock_shares), max(clock_shares)
        )
    thresh5_shares = collect_shares(
        lambda p: p.get("dial") == "threshold" and int(p.get("T", -1)) == 5
    )
    if thresh5_shares:
        out["threshold_T5_repricing_share_range"] = fmt_pct_range(
            min(thresh5_shares), max(thresh5_shares)
        )

    def median_pair(dial: str, **extra) -> dict | None:
        for p in pairs:
            if p.get("kind") != "nonnull" or p.get("dial") != dial:
                continue
            if extra.get("T_long") is not None:
                if int(p.get("T_long", -1)) != extra["T_long"]:
                    continue
                if int(p.get("T_short", -1)) != extra["T_short"]:
                    continue
                if abs(float(p.get("tau_quantile", -1)) - 0.5) > 1e-12:
                    continue
                return p
            if extra.get("T") is not None:
                if int(p.get("T", -1)) != extra["T"]:
                    continue
                if abs(float(p.get("tau_quantile", -1)) - 0.5) > 1e-12:
                    continue
                if abs(float(p.get("tau_prime_quantile", -1)) - 0.3) > 1e-12:
                    continue
                return p
        return None

    med_clock = median_pair("clock", T_long=10, T_short=5)
    med_thr = median_pair("threshold", T=5)
    if med_clock is not None:
        ci = med_clock.get("composition_interval") or {}
        if ci.get("lo_inward") is not None:
            out["median_clock_composition_lo"] = f"{ci['lo_inward']:.2f}"
        rev = med_clock.get("reversal_interval") or {}
        if rev.get("lo_inward") is not None and rev.get("hi_inward") is not None:
            nd = int(rev.get("inward_decimals") or 2)
            out["median_clock_reversal_interval"] = (
                f"{rev['lo_inward']:.{nd}f} to {rev['hi_inward']:.{nd}f}"
            )
        mag = med_clock.get("magnitudes") or {}
        inside = mag.get("inside_reversal") or {}
        at05 = mag.get("0.50") or {}
        if inside.get("S_P_A") is not None:
            out["median_clock_sensitivity_inside_reversal_looser"] = fmt_sci(
                abs(float(inside["S_P_A"]))
            )
        if inside.get("S_P_R") is not None:
            out["median_clock_sensitivity_inside_reversal_tighter"] = fmt_sci(
                abs(float(inside["S_P_R"]))
            )
        if at05.get("S_P_A") is not None:
            out["median_clock_sensitivity_at_0_5_looser"] = fmt_sci(
                abs(float(at05["S_P_A"]))
            )
        if at05.get("S_P_R") is not None:
            out["median_clock_sensitivity_at_0_5_tighter"] = fmt_sci(
                abs(float(at05["S_P_R"]))
            )
    if med_thr is not None:
        ci = med_thr.get("composition_interval") or {}
        if ci.get("lo_inward") is not None:
            out["median_threshold_composition_lo"] = f"{ci['lo_inward']:.2f}"
        rev = med_thr.get("reversal_interval") or {}
        if rev.get("lo_inward") is not None and rev.get("hi_inward") is not None:
            nd = int(rev.get("inward_decimals") or 2)
            out["median_threshold_reversal_interval"] = (
                f"{rev['lo_inward']:.{nd}f} to {rev['hi_inward']:.{nd}f}"
            )

    margins = [float(p["smallest_sign_margin"]) for p in pairs
               if p.get("kind") == "nonnull"
               and p.get("smallest_sign_margin") is not None]
    if margins:
        out["smallest_sign_margin"] = fmt_sci(min(margins))
    bounds = [float(p["perturbation_bound"]) for p in pairs
              if p.get("perturbation_bound") is not None]
    if bounds:
        out["perturbation_bound"] = fmt_sci(max(bounds))

    clock_mass = [float(p["newly_flagged_mass"]) for p in pairs
                  if p.get("dial") == "clock"]
    thr_mass = [float(p["newly_flagged_mass"]) for p in pairs
                if p.get("dial") == "threshold"]
    if clock_mass:
        out["largest_flagged_mass_clock"] = fmt_mass(max(clock_mass))
    if thr_mass:
        out["largest_flagged_mass_threshold"] = fmt_mass(max(thr_mass))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--nodes", type=int, default=None,
                    help="limit the run to the first n threshold nodes")
    args = ap.parse_args()

    t0 = time.perf_counter()
    rev = json.loads(REV_PATH.read_text())
    prov_src = rev["provenance"]
    k = tuple(float(x) for x in prov_src["frozen_k"])
    taus = [float(x) for x in prov_src["tau_ladder"]]
    quantiles = [float(x) for x in prov_src["tau_quantiles"]]
    if list(quantiles) != list(QUANTILES):
        raise RuntimeError("revelation record tau_quantiles do not match the ladder")
    p0 = ParamsV4.baseline()
    assert p0.mark == 2, "this check is stated at order size two"
    assert p0.H == 10, "the horizon is the calibration value"
    tau_med = taus[quantiles.index(0.5)]
    p_base = p0.replace(tau=float(tau_med))
    if p_base.hash_str() != prov_src["params_hash"]:
        raise RuntimeError(
            f"params hash {p_base.hash_str()} != {prov_src['params_hash']}"
        )

    nodes_spec = list(zip(quantiles, taus))
    if args.nodes is not None:
        nodes_spec = nodes_spec[: args.nodes]

    H = int(p_base.H)
    Delta_m = float(p_base.Delta_m)
    kappas = kappa_grid()
    pert_bound = uniform_perturbation_bound(H, p_base.n_theta)

    committed = {}
    for n in rev["nodes"]:
        committed[(int(n["T"]), float(n["tau_quantile"]))] = n

    print(
        f"t6_cut_check -- mark={p_base.mark} H={H} nodes={len(nodes_spec)} "
        f"T={list(T_GRID)} hash={p_base.hash_str()}",
        flush=True,
    )

    node_map: dict[tuple[int, float], dict] = {}
    for T in T_GRID:
        for qi, tau in nodes_spec:
            key = (int(T), float(qi))
            comm = None
            if key in committed:
                comm = committed[key]["c_k"]
            print(f"  coefficients T={T} q={qi:.1f} tau={tau:.8f}", flush=True)
            node_map[key] = load_node(T, tau, qi, k, p_base, comm)

    pairs: list[dict] = []
    for qi, tau in nodes_spec:
        for T_long, T_short in ((5, 3), (10, 5)):
            looser = node_map[(T_long, qi)]
            tighter = node_map[(T_short, qi)]
            extra = {
                "T_long": int(T_long), "T_short": int(T_short),
                "tau_quantile": float(qi), "tau": float(tau),
            }
            print(f"  pair clock T={T_long}->{T_short} q={qi:.1f}", flush=True)
            pairs.append(build_pair("clock", looser, tighter, extra,
                                    H, Delta_m, kappas, pert_bound))
    for T in T_GRID:
        for i in range(len(nodes_spec) - 1):
            q_tight, tau_tight = nodes_spec[i]
            q_loose, tau_loose = nodes_spec[i + 1]
            looser = node_map[(T, q_loose)]
            tighter = node_map[(T, q_tight)]
            extra = {
                "T": int(T),
                "tau_quantile": float(q_loose),
                "tau_prime_quantile": float(q_tight),
                "tau": float(tau_loose),
                "tau_prime": float(tau_tight),
            }
            print(f"  pair threshold T={T} q={q_loose:.1f}->{q_tight:.1f}",
                  flush=True)
            pairs.append(build_pair("threshold", looser, tighter, extra,
                                    H, Delta_m, kappas, pert_bound))

    checks: dict = {}

    committed_rows = []
    max_comm = 0.0
    n_comm = 0
    for node in node_map.values():
        if node["committed_residual"] is None:
            continue
        n_comm += 1
        max_comm = max(max_comm, float(node["committed_residual"]))
        committed_rows.append({
            "T": node["T"], "tau_quantile": node["tau_quantile"],
            "residual": node["committed_residual"],
        })
    if n_comm == 0:
        checks["cut_committed_coefficients"] = {
            "pass": True, "status": "not_applicable",
            "reason": "no T = 5 or T = 10 node in this run matches the revelation record",
        }
    else:
        checks["cut_committed_coefficients"] = {
            "pass": bool(max_comm < TOL_COMMITTED),
            "tol": TOL_COMMITTED, "max_residual": max_comm,
            "n_compared": n_comm, "rows": committed_rows,
            "request": "computed T = 5 and T = 10 coefficient lists against the "
                       "revelation record, predicted below 1e-12",
        }

    root_rows = []
    max_root = 0.0
    n_root = 0
    signs_ok = True
    for pair in pairs:
        if pair.get("kind") != "nonnull":
            continue
        n_root += 1
        for name in ("c_A", "c_R", "difference"):
            if name == "difference":
                rec_signs = pair["signs_difference"]
                rec_root = (pair.get("root_kappa") or {}).get("difference")
                indep = (pair.get("independent_roots_kappa") or {}).get(
                    "difference"
                ) or []
                recomputed = signs(
                    np.array(pair["c_R"], dtype=float)
                    - np.array(pair["c_A"], dtype=float)
                )
            else:
                rec_signs = pair[f"signs_{name}"]
                rec_root = (pair.get("root_kappa") or {}).get(name)
                indep = (pair.get("independent_roots_kappa") or {}).get(name) or []
                recomputed = signs(pair[name])
            if recomputed != rec_signs:
                signs_ok = False
            if rec_root is None or not indep:
                gap = None
            else:
                gap = min(abs(rec_root - x) for x in indep)
                max_root = max(max_root, gap)
            root_rows.append({
                "dial": pair["dial"], "name": name,
                "recorded_root_kappa": rec_root,
                "independent_roots_kappa": indep,
                "root_gap": gap,
            })
    if n_root == 0:
        checks["cut_signs_and_roots"] = {
            "pass": True, "status": "not_applicable",
            "reason": "no non-null pair in this run",
        }
    else:
        checks["cut_signs_and_roots"] = {
            "pass": bool(signs_ok and max_root < TOL_ROOT_INDEP),
            "tol": TOL_ROOT_INDEP, "max_root_gap": max_root,
            "signs_agree": signs_ok, "n_compared": n_root, "rows": root_rows,
            "request": "sign lists and positive roots recomputed from the "
                       "coefficients by an independent companion-matrix routine",
        }

    ident_vals = [p["max_identity_residual"] for p in pairs
                  if p.get("kind") == "nonnull"
                  and p.get("max_identity_residual") is not None]
    if not ident_vals:
        checks["cut_identity_residuals"] = {
            "pass": True, "status": "not_applicable",
            "reason": "no non-null pair in this run",
        }
    else:
        max_ident = max(ident_vals)
        checks["cut_identity_residuals"] = {
            "pass": bool(max_ident < TOL_IDENT),
            "tol": TOL_IDENT, "max_residual": max_ident,
            "n_pairs": len(ident_vals),
            "request": "three identity residuals of the cut and the split, "
                       "absolute, under 1e-10, at every grid kappa of every "
                       "non-null pair",
        }

    t5_rows = []
    max_t5 = 0.0
    n_t5 = 0
    if not T5_PATH.exists():
        checks["cut_t5_split_agreement"] = {
            "pass": True, "status": "not_applicable",
            "reason": "t5_who_gets_caught.json is not present",
        }
    else:
        t5 = json.loads(T5_PATH.read_text())
        t5_by_q = {float(n["tau_quantile"]): n for n in t5.get("nodes") or []}
        for pair in pairs:
            if pair.get("dial") != "clock":
                continue
            if int(pair.get("T_long", -1)) != 10 or int(pair.get("T_short", -1)) != 5:
                continue
            q = float(pair["tau_quantile"])
            if q not in t5_by_q:
                continue
            src = t5_by_q[q]
            split05 = next((s for s in pair.get("split") or []
                            if abs(s["kappa"] - 0.5) < 1e-12), None)
            if split05 is None:
                continue
            n_t5 += 1
            diffs = {
                "s_A": abs(split05["s_A"] - float(src["s_A"])),
                "s_B": abs(split05["s_B"] - float(src["s_B"])),
                "s_B_tilde": abs(split05["s_B_tilde"] - float(src["s_B_tilde"])),
                "s_surv": abs(split05["s_surv"] - float(src["s_AB_own"])),
                "delta": abs(split05["delta"] - float(src["repricing_remainder_delta"])),
                "phi": abs(split05["phi"] - float(src["phi"])),
            }
            gap = max(diffs.values())
            max_t5 = max(max_t5, gap)
            t5_rows.append({"tau_quantile": q, "max_abs_diff": gap, **diffs})
        if n_t5 == 0:
            checks["cut_t5_split_agreement"] = {
                "pass": True, "status": "not_applicable",
                "reason": "no T = 5 vs 10 clock pair in this run matches t5",
            }
        else:
            checks["cut_t5_split_agreement"] = {
                "pass": bool(max_t5 < TOL_T5),
                "tol": TOL_T5, "max_residual": max_t5,
                "n_compared": n_t5, "rows": t5_rows,
                "request": "T = 5 vs 10 split at the run's nodes against "
                           "t5_who_gets_caught.json to 1e-8",
            }

    nonnull = [p for p in pairs if p.get("kind") == "nonnull"]
    if not nonnull:
        checks["cut_finite_difference"] = {
            "pass": True, "status": "not_applicable",
            "reason": "no non-null pair in this run",
        }
    else:
        print("  finite-difference pooled passes ...", flush=True)
        acquire_lock()
        try:
            cache: dict = {}
            fd_rows = []
            max_fd = 0.0
            for pair in nonnull:
                if pair["dial"] == "clock":
                    p_looser = node_map[(pair["T_long"], pair["tau_quantile"])]
                    p_tight = node_map[(pair["T_short"], pair["tau_quantile"])]
                else:
                    p_looser = node_map[(pair["T"], pair["tau_quantile"])]
                    p_tight = node_map[(pair["T"], pair["tau_prime_quantile"])]
                ks = fd_kappas_for_pair(pair)
                margin = float(pair.get("smallest_sign_margin") or 0.0)
                for kap in ks:
                    closed_A = M_P_closed(np.array(pair["c_A"]), kap, H, Delta_m)
                    closed_R = M_P_closed(np.array(pair["c_R"]), kap, H, Delta_m)
                    fd_A = central_fd_M(p_looser["al"], p_looser["p"], kap, cache)
                    fd_R = central_fd_M(p_tight["al"], p_tight["p"], kap, cache)
                    dA = abs(closed_A - fd_A)
                    dR = abs(closed_R - fd_R)
                    scale_A = max(abs(closed_A), abs(fd_A), S_FLOOR)
                    scale_R = max(abs(closed_R), abs(fd_R), S_FLOOR)
                    tol_A = max(TOL_FD_ABS, TOL_FD_REL * scale_A,
                                COEFFICIENT_TOL * Delta_m, margin * Delta_m * 1e-6)
                    tol_R = max(TOL_FD_ABS, TOL_FD_REL * scale_R,
                                COEFFICIENT_TOL * Delta_m, margin * Delta_m * 1e-6)
                    max_fd = max(max_fd, dA, dR)
                    fd_rows.append({
                        "dial": pair["dial"], "kappa": float(kap),
                        "closed_A": closed_A, "fd_A": fd_A, "abs_A": dA,
                        "closed_R": closed_R, "fd_R": fd_R, "abs_R": dR,
                        "tol_A": tol_A, "tol_R": tol_R,
                        "pass_A": bool(dA <= tol_A), "pass_R": bool(dR <= tol_R),
                        "inside_reversal": bool(
                            (pair.get("reversal_interval") or {}).get("lo") is not None
                            and (pair["reversal_interval"]["lo"]
                                 < kap < pair["reversal_interval"]["hi"])
                        ),
                        "sign_margin": margin,
                    })
                    print(f"    fd kappa={kap:.5f} dA={dA:.3e} dR={dR:.3e}",
                          flush=True)
        finally:
            release_lock()
        fd_ok = all(r["pass_A"] and r["pass_R"] for r in fd_rows)
        checks["cut_finite_difference"] = {
            "pass": bool(fd_ok),
            "tol_abs": TOL_FD_ABS, "tol_rel": TOL_FD_REL,
            "max_residual": max_fd, "n_evaluations": len(fd_rows),
            "deriv_step": float(DERIV_STEP),
            "request": "closed-form d_kappa M_P against central finite "
                       "differences of pooled_premium at three kappas per "
                       "non-null pair, one inside the reversal interval where "
                       "one exists; tolerance is the max of an absolute floor, "
                       "a relative share of the derivative, and a floor from "
                       "the sign margin",
            "rows": fd_rows,
        }

    n_fail = sum(1 for c in checks.values()
                 if not c.get("pass") and c.get("status") != "not_applicable")
    node_out = []
    for (T, qi), node in sorted(node_map.items()):
        node_out.append({
            "T": int(T), "tau_quantile": float(qi), "tau": float(node["tau"]),
            "Omega": float(node["Omega"]),
            "c_k": [float(x) for x in node["c"]],
            "source": node["source"],
            "committed_residual": node["committed_residual"],
            "perturbation_observed": node["perturbation_observed"],
            "pooled_type_weights": node["pooled_type_weights"],
        })

    record = {
        "provenance": {
            "script": "numerical_v4/checks/t6_cut_check.py",
            "params_hash": p_base.hash_str(),
            "mark": int(p_base.mark), "H": int(H),
            "frozen_k": [float(x) for x in k],
            "cutoff_scale": float(prov_src["cutoff_scale"]),
            "payoff_scale": float(prov_src["payoff_scale"]),
            "tau_ladder": list(taus),
            "tau_quantiles": list(quantiles),
            "T_grid": list(T_GRID),
            "kappa_grid": {
                "lo": float(GRID_LO), "hi": float(GRID_HI),
                "n": int(kappas.size), "step": float(KAPPA_STEP),
            },
            "measurement": (
                "s_A is the closed-form kappa-derivative of E[h | A] from the "
                "erasure coefficients of the looser pool; s_surv is the same "
                "for the surviving pool at the tighter rule's own kernel; "
                "the net cut leg s_B is (s_A - (1 - phi) s_surv) / phi; the "
                "caught-only leg is the derivative of E[h_looser | B]; the "
                "re-pricing term delta is the derivative of "
                "E[h_tighter - h_looser | A minus B]; phi is P(B)/P(A) and "
                "does not depend on kappa; the re-pricing share is "
                "minus ((1 - phi)/phi) delta over s_B; sensitivities reported "
                "as S_P = Delta_m |s|; roots are of the reversed coefficient "
                "polynomial in x = kappa/(2 - kappa); the reversal interval "
                "is where the tighter rule's total sensitivity exceeds the "
                "looser's, covered on a mesh by a Lipschitz bound on the "
                "polynomial derivative, endpoints rounded inward"
            ),
            "weights": (
                "cell mass from the measure weights, cell belief from the "
                "market weights including the off-path floor, as in the "
                "pooled pass; subset masses for B and the survivors from the "
                "alive measure weights of the two rules"
            ),
            "nodes_run": (len(nodes_spec) if args.nodes is not None else "all"),
        },
        "checks": checks,
        "pairs": pairs,
        "nodes": node_out,
        "n_fail": int(n_fail),
        "all_pass": bool(n_fail == 0),
        "seconds": time.perf_counter() - t0,
        "tolerances": {
            "coefficient_zero": COEFFICIENT_TOL,
            "null_mass": NULL_MASS_TOL,
            "identity": TOL_IDENT,
            "t5_split": TOL_T5,
            "committed_coefficients": TOL_COMMITTED,
            "finite_difference_abs": TOL_FD_ABS,
            "finite_difference_rel": TOL_FD_REL,
            "independent_root": TOL_ROOT_INDEP,
            "off_path_eps": OFF_PATH_EPS,
            "uniform_perturbation_bound": pert_bound,
        },
    }

    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(record, indent=2, default=float) + "\n")
    tmp.replace(OUT)
    print(
        f"\n{'ALL PASS' if record['all_pass'] else str(n_fail) + ' FAIL'}"
        f"  in {record['seconds']:.1f} s  ({len(pairs)} pair(s))  ->  {OUT}",
        flush=True,
    )
    rendered = render(record)
    print("render: " + json.dumps(rendered), flush=True)
    return 0 if record["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
