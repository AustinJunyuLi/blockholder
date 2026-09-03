"""Detection record: silent mass, entry by state, premium levels and cut split.

Grid verification of the two detection technologies at order size two.  A
revealed building mark sets the engagement posterior to one.  An engaged type
with n building rounds is silent with probability (kappa/2)^n.  The pooled
premium is the erasure polynomial of Lemma g1, with the entry probability and
the engagement posterior kept separately per level set.

Per threshold node, per clock T in {3, 5, 10} and per grid kappa:

  (a) silent mass of pooled Voice types, by the level-set route and by an
      independent enumeration of silent histories
  (b) bidder entry conditional on Voice in the flagged cell, on tape-detected
      pooled histories and on silent pooled histories
  (c) the engagement premium split across those three states
  (d) the pooled and total premium in kappa, matched to t2_t1_check.json
      kappa_profiles at T = 5 and T = 10
  (e) the level effect of each adjacent clock pair and each adjacent
      threshold pair
  (f) the level cut split, caught histories against survivors' re-pricing
  (g) the ratio of silent entry to tape-detected entry
  (h) the three entries recomputed from a pooled pass that classifies
      detection states on histories, at three kappas per node

T = 10 equals the horizon.  Its flagged mass sits below the cell-mass floor,
so every ten-round node is one pool.  T = 3 is a stated grid extension.

Entry is a function of the engagement posterior and the price at the unique
competitive pricing root.

Checks:

  t6_params_hash                 wiring       provenance hash against the
                                              revelation record
  t6_silent_mass_routes          wiring       level-set silent mass against
                                              the history enumeration
  t6_premium_decomp              wiring       three-state split sums to the
                                              total premium
  t6_profiles_match_t1           wiring       M_P and Delta_act against
                                              t2_t1_check.json at T = 5, 10
  t6_cut_split                   wiring       caught plus re-pricing equals
                                              the total level effect
  t6_entry_history_route         wiring       level-set entries against a
                                              pooled pass at three kappas
  t6_T3_representation           wiring       T = 3 M_P against a pooled pass
  t6_T5_representation           wiring       T = 5 M_P against a pooled pass
  t6_threshold_pairs             reported     adjacent threshold pairs; not
                                              applicable at one node

Deterministic: no RNG, no Monte Carlo, no network.

Run:    .venv/bin/python numerical_v4/checks/t6_detection_check.py [--nodes n]
Output: numerical_v4/checks/t6_detection_check.json
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

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

try:
    from scipy.stats import norm                                        # noqa: E402

    from numerical_v4.flagged import flagged_nodes                      # noqa: E402
    from numerical_v4.menu import (                                     # noqa: E402
        VOICE,
        atoms,
        b_star_inverse_brentq,
        legal_clock,
        type_reference,
    )
    from numerical_v4.params import ParamsV4, TOL_PROB                   # noqa: E402
    from numerical_v4.pooled import (                                    # noqa: E402
        _alive_weights,
        inner_price,
        pooled_pass,
    )
    from numerical_v4.premium import (                                   # noqa: E402
        MIN_CELL_MASS,
        cell_weights,
        pooled_premium,
    )
except ImportError:
    if __name__ == "__main__":
        raise
    norm = flagged_nodes = VOICE = atoms = None  # type: ignore
    b_star_inverse_brentq = legal_clock = type_reference = None  # type: ignore
    ParamsV4 = TOL_PROB = None  # type: ignore
    _alive_weights = inner_price = pooled_pass = None  # type: ignore
    MIN_CELL_MASS = cell_weights = pooled_premium = None  # type: ignore

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, "t6_detection_check.json")
SOURCE = os.path.join(HERE, "t2_threshold_revelation_check.json")
T1_PATH = os.path.join(HERE, "t2_t1_check.json")
LOCK = Path(REPO) / ".scratch" / "v5-paper" / "runs" / "COMPUTE_LOCK"
OWNER = "rec-detection"
WHAT = "t6_detection_check pooled passes"

TOL_MASS = 1e-12
TOL_DECOMP = 1e-12
TOL_REP = 1e-12
TOL_PROFILE = 1e-12
TOL_SPLIT = 1e-12
TOL_ENTRY = 1e-9
LOCK_WAIT_S = 20.0
LOCK_WAIT_MAX_S = 45.0 * 60.0
PP = 100.0

KAPPAS = np.round(np.arange(0.15, 0.8501, 0.01), 2)
KAPPAS_REP = (0.15, 0.50, 0.85)
QUANTILES = (0.1, 0.3, 0.5, 0.7, 0.9)
TS = (3, 5, 10)

results: dict = {"checks": [], "n_fail": 0}


def record(name: str, ok: bool, kind: str, detail: dict) -> None:
    results["checks"].append(
        {"name": name, "kind": kind, "pass": bool(ok), **detail}
    )
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({kind})", flush=True)
    print("        " + json.dumps(detail, default=float)[:1200], flush=True)


def record_na(name: str, kind: str, detail: dict) -> None:
    results["checks"].append(
        {"name": name, "kind": kind, "pass": True, "not_applicable": True,
         "status": "not_applicable", **detail}
    )
    print(f"[N/A] {name} ({kind})", flush=True)
    print("        " + json.dumps(detail, default=float)[:1200], flush=True)


def acquire_lock() -> None:
    deadline = time.time() + LOCK_WAIT_MAX_S
    while True:
        if not LOCK.exists():
            payload = {
                "pid": os.getpid(),
                "what": WHAT,
                "started": datetime.now(timezone.utc).isoformat(),
                "owner": OWNER,
            }
            try:
                with LOCK.open("x") as fh:
                    json.dump(payload, fh, indent=2)
                    fh.write("\n")
                return
            except FileExistsError:
                pass
        if time.time() >= deadline:
            raise RuntimeError(
                f"timed out waiting for compute lock at {LOCK}"
            )
        time.sleep(LOCK_WAIT_S)


def release_lock() -> None:
    if not LOCK.exists():
        return
    try:
        payload = json.loads(LOCK.read_text())
    except Exception:
        return
    if payload.get("pid") == os.getpid() and payload.get("owner") == OWNER:
        LOCK.unlink()


atexit.register(release_lock)


def popcount_table(n_rounds: int) -> np.ndarray:
    return np.array([bin(m).count("1") for m in range(1 << n_rounds)],
                    dtype=int)


def erasure_weights(pc: np.ndarray, n_rounds: int, kappa: float) -> np.ndarray:
    eps = kappa / 2.0
    return (1.0 - eps) ** pc * eps ** (n_rounds - pc)


_SILENT_CACHE: dict = {}


def silent_history_tables(H: int):
    cached = _SILENT_CACHE.get(H)
    if cached is not None:
        return cached
    n_rounds = H + 1
    n_sil = 3 ** n_rounds
    idx = np.arange(n_sil)
    digits = np.empty((n_sil, n_rounds), dtype=np.int8)
    tmp = idx
    for d in range(n_rounds - 1, -1, -1):
        digits[:, d] = (tmp % 3).astype(np.int8) - 1
        tmp //= 3
    n0 = np.sum(digits == 0, axis=1)
    oks = []
    for t in range(H + 2):
        if t <= 0:
            oks.append(np.ones(n_sil, dtype=bool))
        else:
            oks.append(np.all(digits[:, :t] == 1, axis=1))
    _SILENT_CACHE[H] = (n0, oks)
    return n0, oks


def silent_mass_enumeration(W: np.ndarray, kappa: float, H: int) -> float:
    """Voice measure on histories whose every flow lies in {-1, 0, 1}."""
    n0, oks = silent_history_tables(H)
    eps = kappa / 2.0
    stay = 1.0 - kappa
    n_rounds = H + 1
    lut = stay ** n0.astype(float) * eps ** (n_rounds - n0.astype(float))
    total = 0.0
    for t in range(1, H + 2):
        wt = float(W[t])
        if wt <= 0.0:
            continue
        total += wt * float(lut[oks[t]].sum())
    return total


def silent_mass_closed(W: np.ndarray, kappa: float, H: int) -> float:
    eps = kappa / 2.0
    return float(sum(float(W[t]) * eps ** t for t in range(1, H + 2)))


def interval_stats(W, Wm, WVm, WAm, p: ParamsV4) -> dict:
    """pi, p_bid, h and masses on every type interval [lo, hi)."""
    n = p.n_theta
    cW = np.concatenate([[0.0], np.cumsum(W)])
    cM = np.concatenate([[0.0], np.cumsum(Wm)])
    cV = np.concatenate([[0.0], np.cumsum(WVm)])
    cA = np.concatenate([[0.0], np.cumsum(WAm)])
    voice_w = np.array(W, dtype=float)
    voice_w[0] = 0.0
    cVoice = np.concatenate([[0.0], np.cumsum(voice_w)])

    los, his = [], []
    for lo in range(n):
        for hi in range(lo + 1, n + 1):
            los.append(lo)
            his.append(hi)
    los_a, his_a = np.array(los), np.array(his)
    mass_meas = cW[his_a] - cW[los_a]
    mass_mkt = cM[his_a] - cM[los_a]
    voice = cVoice[his_a] - cVoice[los_a]
    live = mass_mkt > 0.0
    pi = np.zeros(los_a.size)
    vhat = np.zeros(los_a.size)
    pi[live] = (cA[his_a] - cA[los_a])[live] / mass_mkt[live]
    vhat[live] = (cV[his_a] - cV[los_a])[live] / mass_mkt[live]
    sol = inner_price(vhat[live], pi[live], p)
    h = np.zeros(los_a.size)
    pb = np.zeros(los_a.size)
    h[live] = pi[live] * sol.p_bid
    pb[live] = sol.p_bid

    out = {}
    for i in range(los_a.size):
        out[(int(los_a[i]), int(his_a[i]))] = {
            "mass": float(mass_meas[i]),
            "voice": float(voice[i]),
            "pi": float(pi[i]),
            "p": float(pb[i]),
            "h": float(h[i]),
        }
    return out


def build_erasure(k: tuple[float, ...], p: ParamsV4) -> dict:
    """Kappa-free level-set tables at one (tau, T)."""
    al = atoms(k, p)
    ref = type_reference(p)
    W, Wm, WVm, WAm = _alive_weights(al, p.H, p.n_theta, ref)
    cw = cell_weights(al)
    fl = flagged_nodes(al, p)
    stats = interval_stats(W, Wm, WVm, WAm, p)
    n_rounds = p.H + 1
    nmask = 1 << n_rounds
    n_theta = p.n_theta
    tot = float(W.sum())
    pc = popcount_table(n_rounds)
    G = np.zeros(nmask)
    sil_voice = np.zeros(nmask)
    sil_p_num = np.zeros(nmask)
    sil_h_mass = np.zeros(nmask)
    det_voice = np.zeros(nmask)
    det_p_num = np.zeros(nmask)
    det_h_mass = np.zeros(nmask)
    h_mt = np.zeros((nmask, n_theta))

    for mask in range(nmask):
        cuts = [d + 1 for d in range(n_rounds) if mask >> d & 1]
        edges = [0] + cuts + [n_theta]
        g = 0.0
        for i, (lo, hi) in enumerate(zip(edges[:-1], edges[1:])):
            if hi <= lo:
                continue
            st = stats[(lo, hi)]
            h_mt[mask, lo:hi] = st["h"]
            if tot > 0.0:
                g += (st["mass"] / tot) * st["h"]
            if i == 0:
                sil_voice[mask] = st["voice"]
                sil_p_num[mask] = st["voice"] * st["p"]
                sil_h_mass[mask] = st["mass"] * st["h"]
            else:
                det_voice[mask] += st["voice"]
                det_p_num[mask] += st["voice"] * st["p"]
                det_h_mass[mask] += st["mass"] * st["h"]
        G[mask] = g

    Omega = float(cw.Omega)
    M_F = float(fl.M_F) if Omega > 0.0 and np.isfinite(fl.M_F) else 0.0
    entry_flagged = (M_F / p.Delta_m) if Omega > 0.0 else float("nan")
    one_pool = bool(p.T == p.H or Omega < MIN_CELL_MASS
                    or (1.0 - Omega) < MIN_CELL_MASS)
    return {
        "T": int(p.T), "tau": float(p.tau),
        "W": np.asarray(W, dtype=float),
        "tot": tot, "G": G, "pc": pc, "H": int(p.H),
        "sil_voice": sil_voice, "sil_p_num": sil_p_num,
        "sil_h_mass": sil_h_mass,
        "det_voice": det_voice, "det_p_num": det_p_num,
        "det_h_mass": det_h_mass,
        "h_mt": h_mt,
        "Omega": Omega, "M_F": M_F, "entry_flagged": entry_flagged,
        "degenerate": list(cw.degenerate), "one_pool": one_pool,
        "Pr_a": float(cw.Pr_a),
        "pooled_type_weights": [float(x) for x in W],
        "Voice_pooled_mass": float(np.sum(W[1:])),
    }


def stats_at_kappa(er: dict, kappa: float, Delta_m: float) -> dict:
    n_rounds = er["H"] + 1
    wS = erasure_weights(er["pc"], n_rounds, float(kappa))
    tot = er["tot"]
    M_P = Delta_m * float(np.dot(wS, er["G"]))
    Omega = er["Omega"]
    M_F = er["M_F"]
    Delta_act = Omega * M_F + (1.0 - Omega) * M_P
    sil_voice = float(np.dot(wS, er["sil_voice"]))
    sil_p_num = float(np.dot(wS, er["sil_p_num"]))
    sil_h = float(np.dot(wS, er["sil_h_mass"]))
    det_voice = float(np.dot(wS, er["det_voice"]))
    det_p_num = float(np.dot(wS, er["det_p_num"]))
    det_h = float(np.dot(wS, er["det_h_mass"]))
    entry_sil = sil_p_num / sil_voice if sil_voice > 0.0 else float("nan")
    entry_det = det_p_num / det_voice if det_voice > 0.0 else float("nan")
    ratio = (entry_sil / entry_det
             if np.isfinite(entry_sil) and np.isfinite(entry_det)
             and abs(entry_det) > 0.0 else float("nan"))
    prem_sil = Delta_m * sil_h
    prem_det = Delta_m * det_h
    prem_fl = Omega * M_F
    decomp = prem_fl + prem_det + prem_sil
    closed = silent_mass_closed(er["W"], float(kappa), er["H"])
    enum = silent_mass_enumeration(er["W"], float(kappa), er["H"])
    return {
        "kappa": float(kappa),
        "silent_mass": sil_voice,
        "silent_mass_closed": closed,
        "silent_mass_enum": enum,
        "silent_mass_residual_enum": abs(sil_voice - enum),
        "silent_mass_residual_closed": abs(sil_voice - closed),
        "entry_flagged": er["entry_flagged"],
        "entry_detected": entry_det,
        "entry_silent": entry_sil,
        "entry_ratio_silent_to_detected": ratio,
        "premium_flagged": prem_fl,
        "premium_detected": prem_det,
        "premium_silent": prem_sil,
        "premium_total": Delta_act,
        "decomp_residual": abs(decomp - Delta_act),
        "M_P": M_P, "Delta_act": Delta_act,
        "M_P_pp": M_P * PP, "Delta_act_pp": Delta_act * PP,
        "pooled_mass": tot,
    }


def lambda_h(h_mt: np.ndarray, W_sub: np.ndarray, wS: np.ndarray) -> float:
    """E[h 1_{types}] = sum_S P(S) sum_t W_sub[t] h(S, t)."""
    return float(np.dot(wS, h_mt @ W_sub))


def flagged_split(k: tuple[float, ...], p_tight: ParamsV4,
                  p_loose: ParamsV4) -> dict:
    """Flagged premium mass of newly caught histories and of the rest."""
    al = atoms(k, p_tight)
    flagged = [a for a in al if a.D == 1]
    if not flagged:
        return {"Omega_B": 0.0, "prem_B": 0.0, "Omega_already": 0.0,
                "prem_already": 0.0, "Omega_tight": 0.0, "prem_tight": 0.0}

    x_gl, w_gl = np.polynomial.legendre.leggauss(p_tight.n_gl)
    s_all, w_all, v_all = [], [], []
    B_mask = []
    for a in flagged:
        half = 0.5 * (a.hi - a.lo)
        mid = 0.5 * (a.hi + a.lo)
        s_nodes = mid + half * x_gl
        dens = norm.pdf((s_nodes - p_tight.mu_v) / p_tight.sigma_s) / p_tight.sigma_s
        wq = w_gl * half * dens
        wq = wq * (a.w / wq.sum()) if wq.sum() > TOL_PROB else wq
        for s, w in zip(s_nodes, wq):
            cl_t = legal_clock(VOICE, float(s), p_tight)
            cl_l = legal_clock(VOICE, float(s), p_loose)
            s_all.append(float(s))
            w_all.append(float(w))
            B_mask.append(bool(cl_t.D == 1 and cl_l.D == 0))
            v_all.append(p_tight.mu_v + p_tight.beta * (
                b_star_inverse_brentq(float(cl_t.B_F + cl_t.Q_F), p_tight)
                - p_tight.mu_v))

    w = np.asarray(w_all)
    vhat = np.asarray(v_all)
    is_B = np.asarray(B_mask, dtype=bool)
    sol = inner_price(vhat, np.ones_like(vhat), p_tight)
    pb = sol.p_bid
    prem = p_tight.Delta_m * w * pb
    Omega_t = float(w.sum())
    prem_t = float(prem.sum())
    Omega_B = float(w[is_B].sum())
    prem_B = float(prem[is_B].sum())
    Omega_al = float(w[~is_B].sum())
    prem_al = float(prem[~is_B].sum())
    return {
        "Omega_B": Omega_B, "prem_B": prem_B,
        "Omega_already": Omega_al, "prem_already": prem_al,
        "Omega_tight": Omega_t, "prem_tight": prem_t,
    }


def detected_history_mask(H: int, mark: int) -> np.ndarray:
    """True on histories with at least one flow of mark or mark+1."""
    base = mark + 3
    n = base ** (H + 1)
    tmp = np.arange(n)
    det = np.zeros(n, dtype=bool)
    for _ in range(H + 1):
        dig = tmp % base
        det |= dig >= (mark + 1)
        tmp //= base
    return det


def entries_from_pass(res, detected: np.ndarray, H: int) -> dict:
    mass = res.mass[H]
    pi = res.pi[H]
    pb = res.p_bid[H]
    live = np.isfinite(pi) & (mass > 0.0)
    td = detected & live
    sil = (~detected) & live
    den_td = float(mass[td].sum())
    entry_td = (float(np.dot(mass[td], pb[td]) / den_td)
                if den_td > 0.0 else float("nan"))
    num_s = float(np.dot(mass[sil], pi[sil] * pb[sil]))
    den_s = float(np.dot(mass[sil], pi[sil]))
    entry_s = num_s / den_s if den_s > 0.0 else float("nan")
    return {"entry_detected": entry_td, "entry_silent": entry_s}


def node_public(er: dict, per_kappa: list[dict], qi: float) -> dict:
    return {
        "tau_quantile": float(qi), "tau": er["tau"], "T": er["T"],
        "Omega": er["Omega"], "M_F": er["M_F"],
        "entry_flagged": er["entry_flagged"],
        "degenerate": er["degenerate"], "one_pool": er["one_pool"],
        "Pr_a": er["Pr_a"],
        "Voice_pooled_mass": er["Voice_pooled_mass"],
        "pooled_type_weights": er["pooled_type_weights"],
        "per_kappa": per_kappa,
    }


def _finite(x) -> bool:
    return isinstance(x, (int, float)) and math.isfinite(x)


def _pick_node(nodes: list[dict], T: int, qi: float | None = None):
    if qi is None:
        for n in nodes:
            if n["T"] == T and abs(n["tau_quantile"] - 0.5) < 1e-12:
                return n
        cands = [n for n in nodes if n["T"] == T]
        return cands[0] if cands else None
    for n in nodes:
        if n["T"] == T and abs(n["tau_quantile"] - qi) < 1e-12:
            return n
    return None


def _at_kappa(node: dict, kappa: float) -> dict | None:
    target = round(float(kappa), 2)
    for row in node.get("per_kappa", []):
        if round(float(row["kappa"]), 2) == target:
            return row
    return None


def _fmt_pct_one(x: float) -> str:
    return f"{100.0 * x:.1f} percent"


def _fmt_pct(x: float) -> str:
    p = 100.0 * x
    if abs(p) < 1.0:
        return f"{p:.2f} percent"
    return f"{p:.1f} percent"


def _fmt_mass(x: float) -> str:
    p = 100.0 * x
    ap = abs(p)
    if ap >= 1.0:
        return f"{p:.1f} percent"
    if ap >= 0.01:
        return f"{p:.2f} percent"
    if ap >= 0.0001:
        return f"{p:.4f} percent"
    return "below 0.0001 percent"


def _fmt_range(vals: list[float]) -> str:
    a, b = min(vals), max(vals)

    def one(x: float) -> str:
        p = 100.0 * x
        if abs(p) < 1.0:
            return f"{p:.2f}"
        return f"{p:.1f}"

    return f"{one(a)} to {one(b)} percent"


def render(record: dict) -> dict[str, str]:
    """Manuscript strings printed verbatim from this record."""
    nodes = record.get("nodes") or []
    if not nodes:
        return {}
    out: dict[str, str] = {}
    med5 = _pick_node(nodes, 5)
    if med5 is None:
        return out

    def put_state(kap: float, tag: str) -> None:
        row = _at_kappa(med5, kap)
        if row is None:
            return
        if _finite(row.get("entry_flagged")):
            out[f"entry_flagged_median_T5_{tag}"] = _fmt_pct_one(
                row["entry_flagged"])
        if _finite(row.get("entry_detected")):
            out[f"entry_detected_median_T5_{tag}"] = _fmt_pct_one(
                row["entry_detected"])
        if _finite(row.get("entry_silent")):
            out[f"entry_silent_median_T5_{tag}"] = _fmt_pct_one(
                row["entry_silent"])
        if _finite(row.get("silent_mass")):
            out[f"silent_mass_median_T5_{tag}"] = _fmt_mass(row["silent_mass"])

    put_state(0.15, "k015")
    put_state(0.50, "k050")
    put_state(0.85, "k085")

    row05 = _at_kappa(med5, 0.50)
    if row05 is not None and _finite(row05.get("entry_ratio_silent_to_detected")):
        r = row05["entry_ratio_silent_to_detected"]
        out["silent_to_detected_entry_ratio_median_T5_k050"] = f"{r:.1f}"

    row015 = _at_kappa(med5, 0.15)
    row085 = _at_kappa(med5, 0.85)
    if row015 is not None and row085 is not None:
        d015 = row015.get("Delta_act")
        d085 = row085.get("Delta_act")
        if _finite(d015) and _finite(d085) and abs(d015) > 0.0:
            out["premium_rise_factor_median_T5"] = f"{d085 / d015:.2f}"

    pairs = record.get("clock_pairs") or []

    def clock_share(T_tight, T_loose, qi, kap):
        for pr in pairs:
            if (pr.get("T_tight") == T_tight and pr.get("T_loose") == T_loose
                    and abs(pr.get("tau_quantile", -1) - qi) < 1e-12):
                for r in pr.get("per_kappa") or []:
                    if round(float(r["kappa"]), 2) == round(float(kap), 2):
                        return r.get("share")
        return None

    qi_med = med5["tau_quantile"]
    for T_t, T_l, lab in ((5, 10, "5v10"), (3, 5, "3v5")):
        for kap, ktag in ((0.15, "k015"), (0.85, "k085")):
            sh = clock_share(T_t, T_l, qi_med, kap)
            if _finite(sh):
                out[f"clock_level_{lab}_median_{ktag}"] = _fmt_pct(abs(sh))
        shares_085 = []
        for pr in pairs:
            if pr.get("T_tight") == T_t and pr.get("T_loose") == T_l:
                for r in pr.get("per_kappa") or []:
                    if round(float(r["kappa"]), 2) == 0.85 and _finite(r.get("share")):
                        shares_085.append(abs(r["share"]))
        if shares_085:
            out[f"clock_level_{lab}_k085_range"] = _fmt_range(shares_085)

    thr = record.get("threshold_pairs") or []
    below = []
    mixed_k = []
    for pr in thr:
        signs_by_k = {}
        for r in pr.get("per_kappa") or []:
            kap = round(float(r["kappa"]), 2)
            sh = r.get("share")
            sg = r.get("sign")
            if not _finite(sh):
                continue
            signs_by_k[kap] = sg
            if kap < 0.45:
                below.append(abs(sh))
        if not signs_by_k:
            continue
        ref = signs_by_k.get(0.85)
        if ref is None:
            continue
        for kap, sg in signs_by_k.items():
            if sg != ref:
                mixed_k.append(kap)
    if below:
        mag = max(below) * 100.0
        out["threshold_effect_max_below_k045"] = f"{mag:.2f} percent"
    if mixed_k:
        lo, hi = min(mixed_k), max(mixed_k)
        out["threshold_effect_mixed_kappa_region"] = f"{lo:.2f} to {hi:.2f}"
    elif thr:
        out["threshold_effect_mixed_kappa_region"] = "none"
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--nodes", type=int, default=None,
                    help="limit the run to the first n threshold nodes")
    args = ap.parse_args()

    t0 = time.perf_counter()
    source = json.loads(Path(SOURCE).read_text())
    prov = source["provenance"]
    k = tuple(float(x) for x in prov["frozen_k"])
    taus = [float(x) for x in prov["tau_ladder"]]
    quantiles = [float(x) for x in prov["tau_quantiles"]]
    if tuple(quantiles) != QUANTILES:
        raise RuntimeError("tau_quantiles in the source record do not match")
    p0 = ParamsV4.baseline()
    tau_med = taus[quantiles.index(0.5)]
    p_base = p0.replace(tau=float(tau_med))
    if p_base.hash_str() != prov["params_hash"]:
        raise RuntimeError(
            f"params hash {p_base.hash_str()} != {prov['params_hash']}"
        )
    if int(prov["mark"]) != 2 or int(prov["H"]) != 10:
        raise RuntimeError("source provenance is not mark 2, H 10")

    t1 = json.loads(Path(T1_PATH).read_text())
    t1_profiles = t1.get("kappa_profiles") or {}

    nodes_spec = list(zip(quantiles, taus))
    if args.nodes is not None:
        nodes_spec = nodes_spec[:args.nodes]

    results["provenance"] = {
        "script": "numerical_v4/checks/t6_detection_check.py",
        "params_hash": p_base.hash_str(),
        "mark": int(p_base.mark), "H": int(p_base.H),
        "frozen_k": [float(x) for x in k],
        "cutoff_scale": float(prov["cutoff_scale"]),
        "payoff_scale": float(prov["payoff_scale"]),
        "tau_ladder": list(taus), "tau_quantiles": list(quantiles),
        "T_grid": list(TS),
        "kappa_grid": {"lo": float(KAPPAS[0]), "hi": float(KAPPAS[-1]),
                       "n": int(KAPPAS.size), "step": 0.01},
        "measurement": (
            "Silent mass is the pooled Voice measure on histories with no "
            "revealed building mark, equal to sum_n w_n (kappa/2)^n.  "
            "Entry in each state is E[p | Voice, state].  On flagged and "
            "tape-detected histories the engagement posterior is one, so "
            "this is E[p | state].  On silent histories it is "
            "E[pi p]/E[pi].  Entry is a function of the engagement "
            "posterior and the price at the unique competitive pricing "
            "root.  The three-state premium split is Delta_m E[h 1_state] "
            "and sums to the engagement premium.  Level effects compare "
            "the total premium at a tighter rule with the looser rule, "
            "in premium percentage points and as a share of the looser "
            "level.  The cut split is the caught histories' change plus "
            "survivors' re-pricing, including already-flagged re-pricing, "
            "and sums to the total level effect.  Cell mass uses measure "
            "weights.  Beliefs, and therefore p and pi, use market weights."
        ),
        "nodes_run": (len(nodes_spec) if args.nodes is not None else "all"),
        "source_record": "numerical_v4/checks/t2_threshold_revelation_check.json",
    }

    heavy: dict[tuple, dict] = {}
    node_rows: list[dict] = []
    max_mass_res = 0.0
    max_decomp = 0.0

    for qi, tau in nodes_spec:
        for T in TS:
            p = p_base.replace(tau=float(tau), T=int(T))
            t1n = time.perf_counter()
            er = build_erasure(k, p)
            per = []
            for kap in KAPPAS:
                row = stats_at_kappa(er, float(kap), p.Delta_m)
                per.append(row)
                max_mass_res = max(
                    max_mass_res,
                    row["silent_mass_residual_enum"],
                    row["silent_mass_residual_closed"],
                )
                max_decomp = max(max_decomp, row["decomp_residual"])
            pub = node_public(er, per, qi)
            node_rows.append(pub)
            heavy[(int(T), float(qi))] = er
            print(
                f"  T={T:2d} q={qi:.1f} tau={tau:.8f} "
                f"Omega={er['Omega']:.6f} one_pool={er['one_pool']} "
                f"M_P(0.50)={per[35]['M_P']:.6e} "
                f"({time.perf_counter() - t1n:.1f}s)",
                flush=True,
            )

    clock_pairs = []
    threshold_pairs = []
    max_split = 0.0
    Delta_m = float(p_base.Delta_m)

    clock_adj = ((3, 5), (5, 10))
    for qi, tau in nodes_spec:
        for T_t, T_l in clock_adj:
            er_t = heavy.get((T_t, float(qi)))
            er_l = heavy.get((T_l, float(qi)))
            if er_t is None or er_l is None:
                continue
            p_t = p_base.replace(tau=float(tau), T=int(T_t))
            p_l = p_base.replace(tau=float(tau), T=int(T_l))
            parts = flagged_split(k, p_t, p_l)
            W_B = np.maximum(er_l["W"] - er_t["W"], 0.0)
            W_surv = er_t["W"]
            n_rounds = er_l["H"] + 1
            per = []
            for kap in KAPPAS:
                wS = erasure_weights(er_l["pc"], n_rounds, float(kap))
                st_t = stats_at_kappa(er_t, float(kap), Delta_m)
                st_l = stats_at_kappa(er_l, float(kap), Delta_m)
                Eh_l_B = lambda_h(er_l["h_mt"], W_B, wS)
                Eh_l_surv = lambda_h(er_l["h_mt"], W_surv, wS)
                Eh_t_surv = (1.0 - er_t["Omega"]) * st_t["M_P"] / Delta_m
                caught = parts["prem_B"] - Delta_m * Eh_l_B
                surv = (Delta_m * (Eh_t_surv - Eh_l_surv)
                        + (parts["prem_already"] - er_l["Omega"] * er_l["M_F"]))
                d_act = st_t["Delta_act"] - st_l["Delta_act"]
                split_res = abs((caught + surv) - d_act)
                max_split = max(max_split, split_res)
                share = ((st_l["Delta_act"] - st_t["Delta_act"]) / st_l["Delta_act"]
                         if abs(st_l["Delta_act"]) > 0.0 else float("nan"))
                per.append({
                    "kappa": float(kap),
                    "d_act": d_act,
                    "d_pp": d_act * PP,
                    "share": share,
                    "sign": (int(np.sign(d_act)) if _finite(d_act)
                             and abs(d_act) > TOL_SPLIT else 0),
                    "caught_contrib": caught,
                    "surv_repricing": surv,
                    "split_residual": split_res,
                })
            clock_pairs.append({
                "tau_quantile": float(qi), "tau": float(tau),
                "T_tight": int(T_t), "T_loose": int(T_l),
                "Omega_tight": er_t["Omega"], "Omega_loose": er_l["Omega"],
                "Omega_B": parts["Omega_B"],
                "one_pool_loose": er_l["one_pool"],
                "per_kappa": per,
            })

    if len(nodes_spec) >= 2:
        for T in TS:
            for i in range(len(nodes_spec) - 1, 0, -1):
                qi_l, tau_l = nodes_spec[i]
                qi_t, tau_t = nodes_spec[i - 1]
                er_t = heavy.get((int(T), float(qi_t)))
                er_l = heavy.get((int(T), float(qi_l)))
                if er_t is None or er_l is None:
                    continue
                p_t = p_base.replace(tau=float(tau_t), T=int(T))
                p_l = p_base.replace(tau=float(tau_l), T=int(T))
                parts = flagged_split(k, p_t, p_l)
                W_B = np.maximum(er_l["W"] - er_t["W"], 0.0)
                W_surv = er_t["W"]
                n_rounds = er_l["H"] + 1
                per = []
                for kap in KAPPAS:
                    wS = erasure_weights(er_l["pc"], n_rounds, float(kap))
                    st_t = stats_at_kappa(er_t, float(kap), Delta_m)
                    st_l = stats_at_kappa(er_l, float(kap), Delta_m)
                    Eh_l_B = lambda_h(er_l["h_mt"], W_B, wS)
                    Eh_l_surv = lambda_h(er_l["h_mt"], W_surv, wS)
                    Eh_t_surv = (1.0 - er_t["Omega"]) * st_t["M_P"] / Delta_m
                    caught = parts["prem_B"] - Delta_m * Eh_l_B
                    surv = (Delta_m * (Eh_t_surv - Eh_l_surv)
                            + (parts["prem_already"]
                               - er_l["Omega"] * er_l["M_F"]))
                    d_act = st_t["Delta_act"] - st_l["Delta_act"]
                    split_res = abs((caught + surv) - d_act)
                    max_split = max(max_split, split_res)
                    share = ((st_l["Delta_act"] - st_t["Delta_act"])
                             / st_l["Delta_act"]
                             if abs(st_l["Delta_act"]) > 0.0 else float("nan"))
                    per.append({
                        "kappa": float(kap),
                        "d_act": d_act,
                        "d_pp": d_act * PP,
                        "share": share,
                        "sign": (int(np.sign(d_act)) if _finite(d_act)
                                 and abs(d_act) > TOL_SPLIT else 0),
                        "caught_contrib": caught,
                        "surv_repricing": surv,
                        "split_residual": split_res,
                    })
                threshold_pairs.append({
                    "T": int(T),
                    "tau_quantile_tight": float(qi_t),
                    "tau_quantile_loose": float(qi_l),
                    "tau_tight": float(tau_t), "tau_loose": float(tau_l),
                    "Omega_tight": er_t["Omega"], "Omega_loose": er_l["Omega"],
                    "Omega_B": parts["Omega_B"],
                    "one_pool": er_t["one_pool"] or er_l["one_pool"],
                    "per_kappa": per,
                })

    # Pooled-pass checks under the compute lock.
    pass_rows = []
    max_entry = 0.0
    max_rep3 = 0.0
    max_rep5 = 0.0
    detected = None
    acquire_lock()
    try:
        detected = detected_history_mask(p_base.H, p_base.mark)
        for pub in node_rows:
            er = heavy[(pub["T"], pub["tau_quantile"])]
            p = p_base.replace(tau=float(pub["tau"]), T=int(pub["T"]))
            for kap in KAPPAS_REP:
                pk = p.replace(kappa=float(kap))
                print(f"  pooled pass T={pk.T} q={pub['tau_quantile']:.1f} "
                      f"kappa={kap:.2f} ...", flush=True)
                tpass = time.perf_counter()
                res = pooled_pass(atoms(k, pk), pk, with_runup=False)
                M_code = float(pooled_premium(res, pub["Omega"], pk))
                st = _at_kappa(pub, kap)
                M_rep = float(st["M_P"])
                ent = entries_from_pass(res, detected, pk.H)

                def _ad(a, b) -> float:
                    fa, fb = _finite(a), _finite(b)
                    if not fa and not fb:
                        return 0.0
                    if not fa or not fb:
                        return 1.0
                    return abs(float(a) - float(b))

                d_det = _ad(ent["entry_detected"], st["entry_detected"])
                d_sil = _ad(ent["entry_silent"], st["entry_silent"])
                d_rep = _ad(M_code, M_rep)
                max_entry = max(max_entry, d_det, d_sil)
                if pk.T == 3:
                    max_rep3 = max(max_rep3, d_rep)
                if pk.T == 5:
                    max_rep5 = max(max_rep5, d_rep)
                pass_rows.append({
                    "T": int(pk.T), "tau_quantile": pub["tau_quantile"],
                    "kappa": float(kap),
                    "M_P_pooled_pass": M_code, "M_P_level_set": M_rep,
                    "abs_diff_M_P": d_rep,
                    "entry_detected_pass": ent["entry_detected"],
                    "entry_detected_level_set": st["entry_detected"],
                    "abs_diff_detected": d_det,
                    "entry_silent_pass": ent["entry_silent"],
                    "entry_silent_level_set": st["entry_silent"],
                    "abs_diff_silent": d_sil,
                    "seconds": time.perf_counter() - tpass,
                })
                del res
    finally:
        release_lock()

    record(
        "t6_params_hash", p_base.hash_str() == prov["params_hash"], "wiring",
        {"request": "params hash equals the revelation record",
         "params_hash": p_base.hash_str(),
         "source_params_hash": prov["params_hash"]},
    )
    record(
        "t6_silent_mass_routes", max_mass_res < TOL_MASS, "wiring",
        {"request": "silent mass from level-set sums against the independent "
                    "enumeration of silent histories and against "
                    "sum_n w_n (kappa/2)^n, at every node and kappa",
         "tol": TOL_MASS, "max_residual": max_mass_res},
    )
    record(
        "t6_premium_decomp", max_decomp < TOL_DECOMP, "wiring",
        {"request": "flagged plus tape-detected plus silent premium equals "
                    "the engagement premium, at every node and kappa",
         "tol": TOL_DECOMP, "max_residual": max_decomp},
    )

    profile_rows = []
    max_prof = 0.0
    n_matched = 0
    for pub in node_rows:
        if pub["T"] not in (5, 10):
            continue
        key = f"T={pub['T']},q={pub['tau_quantile']}"
        prof = t1_profiles.get(key)
        if prof is None:
            continue
        mp = prof["M_P_pp"]
        da = prof["Delta_act_pp"]
        for i, kap in enumerate(KAPPAS):
            st = pub["per_kappa"][i]
            d_mp = abs(st["M_P_pp"] - mp[i])
            d_da = abs(st["Delta_act_pp"] - da[i])
            max_prof = max(max_prof, d_mp, d_da)
        n_matched += 1
        profile_rows.append({"key": key, "n_kappa": int(KAPPAS.size)})
    if n_matched == 0:
        record_na(
            "t6_profiles_match_t1", "wiring",
            {"request": "M_P_pp and Delta_act_pp against t2_t1_check.json "
                        "kappa_profiles at T = 5 and 10",
             "why": "no overlapping node with that record"},
        )
    else:
        record(
            "t6_profiles_match_t1", max_prof < TOL_PROFILE, "wiring",
            {"request": "M_P_pp and Delta_act_pp against t2_t1_check.json "
                        "kappa_profiles at the same node and T, for T = 5 "
                        "and T = 10; T = 3 is a grid extension and is not "
                        "in that record",
             "tol": TOL_PROFILE, "max_residual": max_prof,
             "n_nodes_matched": n_matched, "rows": profile_rows},
        )

    if clock_pairs or threshold_pairs:
        record(
            "t6_cut_split", max_split < TOL_SPLIT, "wiring",
            {"request": "caught histories' contribution plus survivors' "
                        "re-pricing equals the total premium level effect, "
                        "at every adjacent pair and kappa",
             "tol": TOL_SPLIT, "max_residual": max_split,
             "n_clock_pairs": len(clock_pairs),
             "n_threshold_pairs": len(threshold_pairs)},
        )
    else:
        record_na(
            "t6_cut_split", "wiring",
            {"request": "caught plus re-pricing equals the level effect",
             "why": "no adjacent pair was computed"},
        )

    record(
        "t6_entry_history_route", max_entry < TOL_ENTRY, "wiring",
        {"request": "Voice-conditional entry on tape-detected and silent "
                    "histories from a pooled pass, cells and detection "
                    "states classified on histories, against the level-set "
                    "route at kappa in {0.15, 0.50, 0.85} per node",
         "tol": TOL_ENTRY, "max_residual": max_entry,
         "n_passes": len(pass_rows)},
    )

    has_T3 = any(r["T"] == 3 for r in pass_rows)
    has_T5 = any(r["T"] == 5 for r in pass_rows)
    if has_T3:
        record(
            "t6_T3_representation", max_rep3 < TOL_REP, "wiring",
            {"request": "T = 3 M_P from the erasure representation against "
                        "the enumerated pooled pass at three kappas per node",
             "tol": TOL_REP, "max_abs_diff": max_rep3},
        )
    else:
        record_na(
            "t6_T3_representation", "wiring",
            {"request": "T = 3 representation against a pooled pass",
             "why": "no T = 3 pass was run"},
        )
    if has_T5:
        record(
            "t6_T5_representation", max_rep5 < TOL_REP, "wiring",
            {"request": "T = 5 M_P from the erasure representation against "
                        "the enumerated pooled pass at three kappas per node",
             "tol": TOL_REP, "max_abs_diff": max_rep5},
        )
    else:
        record_na(
            "t6_T5_representation", "wiring",
            {"request": "T = 5 representation against a pooled pass",
             "why": "no T = 5 pass was run"},
        )

    if len(nodes_spec) < 2:
        record_na(
            "t6_threshold_pairs", "reported",
            {"request": "adjacent threshold pairs on the ladder, with the "
                        "level effect, the mixed kappa region and the "
                        "largest magnitude below kappa = 0.45",
             "why": "one threshold node does not form an adjacent pair",
             "nodes_run": len(nodes_spec)},
        )
    else:
        record(
            "t6_threshold_pairs", True, "reported",
            {"request": "adjacent threshold pairs on the ladder at every T",
             "n_pairs": len(threshold_pairs)},
        )

    abstract = {
        "median_T5_kappa05_entry_ratio_silent_to_detected": None,
        "clock_level_effect": [],
    }
    med5 = _pick_node(node_rows, 5)
    if med5 is not None:
        row = _at_kappa(med5, 0.50)
        if row is not None:
            abstract["median_T5_kappa05_entry_ratio_silent_to_detected"] = (
                row["entry_ratio_silent_to_detected"]
            )
    for pr in clock_pairs:
        for kap in (0.15, 0.85):
            r = None
            for row in pr["per_kappa"]:
                if round(float(row["kappa"]), 2) == kap:
                    r = row
                    break
            if r is None:
                continue
            abstract["clock_level_effect"].append({
                "tau_quantile": pr["tau_quantile"],
                "T_tight": pr["T_tight"], "T_loose": pr["T_loose"],
                "kappa": kap,
                "share": r["share"], "d_pp": r["d_pp"], "sign": r["sign"],
            })

    results["nodes"] = node_rows
    results["clock_pairs"] = clock_pairs
    results["threshold_pairs"] = threshold_pairs
    results["pooled_pass_rows"] = pass_rows
    results["abstract_inputs"] = abstract
    results["seconds"] = time.perf_counter() - t0
    results["all_pass"] = results["n_fail"] == 0
    results["n_nodes_run"] = len(nodes_spec)
    results["largest_residuals"] = {
        "silent_mass": max_mass_res,
        "premium_decomp": max_decomp,
        "profiles_match_t1": max_prof,
        "cut_split": max_split,
        "entry_history_route": max_entry,
        "T3_representation": max_rep3,
        "T5_representation": max_rep5,
    }

    tmp = OUT + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
        fh.write("\n")
    os.replace(tmp, OUT)
    print(
        f"\n{'ALL PASS' if results['all_pass'] else str(results['n_fail']) + ' FAIL'}"
        f"  in {results['seconds']:.0f} s  "
        f"({len(nodes_spec)} threshold node(s), {len(TS)} clocks)  ->  {OUT}",
        flush=True,
    )
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
