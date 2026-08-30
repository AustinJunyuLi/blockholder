"""H1 — the partition test (SPEC §3.4, sign-free; decision table row 1).

    CAR_iw = α + β1·LIQ_i + β2·(LIQ_i × Flagged_w) + β3·Flagged_w
             + X_i'θ + δ_SIC2 + δ_YQ + ε_iw

stacked over w ∈ {runup, jump} (two rows per filing); β2 is the partition
coefficient (P2: the flagged cell is liquidity-invariant, the pooled cell
carries the derivative).

Sample: the SPEC §2.3 funnel on the re-parsed universe (registered route:
cover-page CUSIP → CRSP eligible PERMNO, ≥60 valid Amihud days), keep-first
per (firm, TD), then the main-sample restrictions of §2.5/§2.6 — straddlers
(TD < 2024-02-05 ≤ FD) excluded and the adoption-to-effect stub
(2023-10-10 ≤ TD < 2024-02-05) excluded; both counted. The full-funnel
variant (restrictions off) is reported as a robustness row.

Variables (SPEC §3.1-§3.3):
  RUNUP  CAR[TD, FD*-1]        market model on [TD-252, TD-22], ≥120 valid
  JUMP   CAR[FD*-1, FD*+1]     days, VW index = Σ DlyCap·DlyRet / Σ DlyCap
  FD*    FD if accepted < the era's EDGAR cut-off (5:30 pm ET before
        2024-02-05, 10:00 pm ET after), else the next trading day (§2.4)
  LIQ    -1 × z-score within TD's calendar quarter of log(ILLIQ); ILLIQ =
        mean |DlyRet| / (|DlyPrc|·DlyVol) × 1e6 over [TD-126, TD-6]
  X      log(DlyCap) at TD-6 · PRE42 · filer-type dummies (activist-HF /
        corporate; hand-coded top-200 overrides + name regex, §11 row 19) ·
        window length in business days (holiday-adjusted)
  FE     2-digit SIC (cached EDGAR submissions sic; missing bucket reported)
        · year-quarter

Standard errors: two-way clustered on subject PERMNO and calendar month of
TD (Cameron-Gelbach-Miller), plus a Rademacher wild cluster bootstrap on the
month dimension (9,999 draws, null imposed); the more conservative p-value
is the quoted one (§3.4).

Outputs (committed, ``empirics/output/``):
  h1_estimate.json   coefficients, SEs, p-values, N, MDE, sample counts —
                     the ESTIMATED record
  h1_sample.csv      the estimation rows (CARs, LIQ, controls) for the audit

Usage: .venv/bin/python -m empirics.estimate_h1 [--limit N]
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import os
import re
from typing import Optional

import numpy as np
import pandas as pd

from empirics.facts import business_delay

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "output")
DATA_DIR = os.path.join(HERE, "data")
FACT2_JSONL = os.path.join(DATA_DIR, "fact2_parsed.jsonl")
CRSP_PATH = os.path.join(DATA_DIR, "crsp_daily.csv")
SUBMISSIONS_DIR = os.path.join(DATA_DIR, "submissions")
FILER_OVERRIDES = os.path.join(OUT_DIR, "filer_type_overrides.csv")

RULE_DATE = pd.Timestamp("2024-02-05")        # effective date (§2.5)
ADOPTION_DATE = pd.Timestamp("2023-10-10")    # pre window ends (§2.6)
CUTOFF_PRE = "17:30"                          # 5:30 pm ET EDGAR cut-off
CUTOFF_POST = "22:00"                         # 10:00 pm ET (§2.4)

CRSP_USECOLS = ["PERMNO", "CUSIP", "HdrCUSIP", "ShareType", "USIncFlg",
                "DlyPrc", "DlyCap", "DlyRet", "DlyVol", "DlyCalDt"]

N_BOOT = 9_999
Z_MDE = 2.802                                 # z_.975 + z_.80 (§3.6)
SEED = 20260830

# Filer-type name regex (§11 row 19); the hand-coded top-200 overrides take
# precedence. Deliberately conservative: unclear names fall to "other".
_FILER_HF_RE = re.compile(
    r"\b(capital|fund|funds|partners|partner|asset management|investments?|"
    r"advisors?|advisers?|opportunity fund|value fund|activist|"
    r"equity partners)\b|\bl?\.?p\.?\b|\bllc\b", re.I)
_FILER_CORP_RE = re.compile(
    r"\b(corp\.?|corporation|inc\.?|incorporated|co\.?|company|ltd\.?|"
    r"limited|holdings|industries|systems|pharmaceuticals|therapeutics|"
    r"technologies|biosciences|laboratories)\b\s*$"
    r"|\b(s\.?a\.?|n\.?v\.?|plc|a\.?g)\b\s*$", re.I)
_FILER_NOT_HF_RE = re.compile(
    r"\b(estate|executor|successor|bank|trust company|pension|insurance|"
    r"liquidating|liquidation)\b", re.I)


def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _cusip8(value) -> Optional[str]:
    if not isinstance(value, str) or not value.strip():
        return None
    v = value.strip()
    return v[:8].upper() if len(v) >= 8 else None


def _norm_cdf(x: float) -> float:
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


# ---------------------------------------------------------------------------
# inputs
# ---------------------------------------------------------------------------

def load_filings(path: str = FACT2_JSONL) -> pd.DataFrame:
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    df = pd.DataFrame(rows)
    df["td"] = pd.to_datetime(df["event"], errors="coerce")
    df["fd"] = pd.to_datetime(df["filed"]).fillna(
        pd.to_datetime(df["date_filed"]))
    df["cusip8"] = df["cusip"].map(_cusip8)
    return df


class CrspPanel:
    """One pass over the CRSP snapshot: eligibility, the CUSIP link used by
    the registered funnel, per-PERMNO daily arrays, and the VW market
    return."""

    def __init__(self, path: str = CRSP_PATH) -> None:
        t0 = dt.datetime.now()
        dtype = {"PERMNO": "int32", "CUSIP": "category", "HdrCUSIP": "category",
                 "ShareType": "category", "USIncFlg": "category",
                 "DlyPrc": "float32", "DlyCap": "float64", "DlyRet": "float32",
                 "DlyVol": "float64"}
        df = pd.read_csv(path, usecols=CRSP_USECOLS, dtype=dtype,
                         low_memory=False)
        df["date"] = pd.to_datetime(df["DlyCalDt"])
        self.n_rows = len(df)

        eligible = set(map(int, df.loc[(df["ShareType"] == "NS")
                                       & (df["USIncFlg"] == "Y"),
                                       "PERMNO"].unique()))
        self.eligible = eligible

        # cusip8 -> [PERMNO] over the eligible set (the registered route)
        pairs = pd.concat([
            df[["PERMNO", "CUSIP"]].rename(columns={"CUSIP": "c8"}),
            df[["PERMNO", "HdrCUSIP"]].rename(columns={"HdrCUSIP": "c8"}),
        ])
        pairs = pairs[pairs["PERMNO"].isin(eligible)]
        pairs["c8"] = pairs["c8"].astype("string").str[:8].str.upper()
        pairs = pairs.dropna(subset=["c8"]).drop_duplicates()
        self.cusip_link: dict[str, list[int]] = {
            k: sorted(map(int, g)) for k, g in
            pairs.groupby("c8")["PERMNO"].agg(lambda s: set(s)).items()}

        # VW market return: Σ DlyCap·DlyRet / Σ DlyCap per day (SPEC §3.1)
        mkt = df.dropna(subset=["DlyRet", "DlyCap"])
        mkt = mkt[mkt["DlyCap"] > 0]
        w = mkt["DlyCap"]
        mkt_ret = (mkt["DlyRet"] * w).groupby(mkt["date"]).sum() / \
            w.groupby(mkt["date"]).sum()
        self.market: dict[pd.Timestamp, float] = mkt_ret.to_dict()
        self.trade_days = np.array(sorted(mkt_ret.index.values),
                                   dtype="datetime64[D]")

        # per-PERMNO arrays for the eligible set
        sub = df[df["PERMNO"].isin(eligible)].sort_values(
            ["PERMNO", "date"], kind="stable")
        valid = (sub["DlyRet"].notna() & sub["DlyPrc"].notna()
                 & (sub["DlyPrc"] != 0) & sub["DlyVol"].notna()
                 & (sub["DlyVol"] > 0)).values
        self.panel: dict[int, dict] = {}
        for key, idx in sub.groupby("PERMNO", sort=False,
                                    observed=True).indices.items():
            g = sub.iloc[idx]
            self.panel[int(key)] = {
                "dates": g["date"].values.astype("datetime64[D]"),
                "ret": g["DlyRet"].values.astype("float64"),
                "prc": g["DlyPrc"].values.astype("float64"),
                "vol": g["DlyVol"].values.astype("float64"),
                "cap": g["DlyCap"].values.astype("float64"),
                "valid": valid[idx],
            }
        print(f"crsp: {self.n_rows} rows, {len(eligible)} eligible PERMNOs, "
              f"{len(self.cusip_link)} cusip8 keys "
              f"({(dt.datetime.now() - t0).total_seconds():.0f}s)", flush=True)


def _slice(panel: dict, lo: pd.Timestamp, hi: pd.Timestamp) -> slice:
    """Row slice for trading days in [lo, hi] (calendar-inclusive)."""
    dates = panel["dates"]
    i = np.searchsorted(dates, np.datetime64(lo.date(), "D"))
    j = np.searchsorted(dates, np.datetime64(hi.date(), "D"), side="right")
    return slice(i, j)


def count_valid_obs(panel: dict, td: pd.Timestamp,
                    lo_days: int = 126, hi_days: int = 6) -> int:
    sl = _slice(panel, td - pd.Timedelta(days=lo_days),
                td - pd.Timedelta(days=hi_days))
    return int(panel["valid"][sl].sum())


def next_trading_day(day: pd.Timestamp, trade_days) -> pd.Timestamp:
    i = np.searchsorted(trade_days, np.datetime64(day.date(), "D"),
                        side="right")
    if i >= len(trade_days):
        return pd.NaT
    return pd.Timestamp(str(trade_days[i]))


# ---------------------------------------------------------------------------
# FD* (§2.4)
# ---------------------------------------------------------------------------

def effective_filing_date(fd: pd.Timestamp, accepted,
                          trade_days) -> tuple:
    """(FD*, route). FD* = FD if accepted is before the era's EDGAR cut-off,
    else the next trading day. Accepted strings are ET with offset, e.g.
    '2023-05-01 18:03:23-04:00'; the time-of-day comparison is in ET."""
    if not isinstance(accepted, str) or len(accepted) < 16:
        return fd, "accepted-missing"
    hhmm = accepted[11:16]
    cutoff = CUTOFF_PRE if fd < RULE_DATE else CUTOFF_POST
    if hhmm < cutoff:
        return fd, "same-day"
    return next_trading_day(fd, trade_days), "next-day"


# ---------------------------------------------------------------------------
# filer type (§11 row 19): hand-coded top-200 overrides + name regex
# ---------------------------------------------------------------------------

def classify_filers(df: pd.DataFrame) -> pd.Series:
    overrides: dict[str, str] = {}
    n_overridden = 0
    if os.path.exists(FILER_OVERRIDES):
        ov = pd.read_csv(FILER_OVERRIDES, dtype=str)
        overrides = dict(zip(ov["filer_cik"].str.strip(),
                             ov["filer_type"].str.strip()))

    def _norm(cik: object) -> str:
        """Unpadded integer CIK string, '' when unusable."""
        try:
            return str(int(str(cik).strip()))
        except (TypeError, ValueError):
            return ""

    norm_overrides = {_norm(k): v for k, v in overrides.items()}
    out = []
    for cik, name in zip(df["filer_cik"], df["filer_name"]):
        key = _norm(cik)
        if key and key in norm_overrides:
            out.append(norm_overrides[key])
            n_overridden += 1
            continue
        n = "" if name is None else str(name).strip()
        if _FILER_HF_RE.search(n) and not _FILER_NOT_HF_RE.search(n):
            out.append("activist_hf")
        elif _FILER_CORP_RE.search(n):
            out.append("corporate")
        else:
            out.append("other")
    res = pd.Series(out, index=df.index, name="filer_type")
    res.attrs["n_overridden"] = n_overridden
    return res


# ---------------------------------------------------------------------------
# market model + CARs
# ---------------------------------------------------------------------------

def market_model(panel: dict, td: pd.Timestamp, market: dict):
    """OLS of the firm's return on the VW market return over [TD-252, TD-22]
    (SPEC §3.1). Returns (alpha, beta) or None if fewer than 120 valid days."""
    sl = _slice(panel, td - pd.Timedelta(days=252), td - pd.Timedelta(days=22))
    r = panel["ret"][sl]
    d = panel["dates"][sl]
    rm = np.array([market.get(pd.Timestamp(str(x)), np.nan) for x in d])
    ok = np.isfinite(r) & np.isfinite(rm)
    if ok.sum() < 120:
        return None
    X = np.column_stack([np.ones(int(ok.sum())), rm[ok]])
    coef, *_ = np.linalg.lstsq(X, r[ok], rcond=None)
    return float(coef[0]), float(coef[1])


def car(panel: dict, market: dict, model, lo: pd.Timestamp,
        hi: pd.Timestamp, trade_days) -> float:
    """Cumulative abnormal return over trading days in [lo, hi].

    A window that contains no trading days at all (e.g. RUNUP for a
    same-day filer: FD*−1 < TD) is a **zero-length** window — 0.0 by
    definition, not missing; §2.3 imposes no delay screen, so same-day
    filers stay in the sample with a genuine zero run-up. A window that
    spans open-market days but has no PERMNO rows is unobserved (NaN)."""
    if model is None:
        return np.nan
    i = np.searchsorted(trade_days, np.datetime64(lo.date(), "D"))
    j = np.searchsorted(trade_days, np.datetime64(hi.date(), "D"),
                        side="right")
    if i >= j:
        return 0.0
    alpha, beta = model
    sl = _slice(panel, lo, hi)
    r = panel["ret"][sl]
    d = panel["dates"][sl]
    if len(d) == 0:
        return np.nan
    rm = np.array([market.get(pd.Timestamp(str(x)), np.nan) for x in d])
    ok = np.isfinite(r) & np.isfinite(rm)
    if not ok.any():
        return np.nan
    return float(np.sum(r[ok] - alpha - beta * rm[ok]))


def trading_day_window(day: pd.Timestamp, trade_days,
                       before: int = 1, after: int = 1) -> tuple:
    """Calendar-date bounds of the [before, after] trading-day window around
    ``day`` (SPEC §3.1 brackets are trading-day offsets: JUMP = the trading
    day before FD*, FD*, and the trading day after). If ``day`` itself is
    not a trading day (a rare weekend EDGAR acceptance), the window becomes
    the trading days bracketing it."""
    d64 = np.datetime64(day.date(), "D")
    i = np.searchsorted(trade_days, d64)
    exact = i < len(trade_days) and trade_days[i] == d64
    if exact:
        lo_i = max(i - before, 0)
        hi_i = min(i + after, len(trade_days) - 1)
        n = hi_i - lo_i + 1
    else:
        lo_i, hi_i, n = max(i - 1, 0), min(i, len(trade_days) - 1), None
    return (pd.Timestamp(str(trade_days[lo_i])),
            pd.Timestamp(str(trade_days[hi_i])), n)


# ---------------------------------------------------------------------------
# OLS with clustered SEs (vectorised cluster meat)
# ---------------------------------------------------------------------------

def _independent_columns(X: np.ndarray) -> np.ndarray:
    """Boolean mask of linearly independent columns (QR with column
    pivoting, statsmodels' tolerance convention). Rare SIC2×YQ dummy
    combinations can be aliased in small samples; aliased columns are
    dropped and their coefficients reported as 0 (not identified)."""
    from scipy.linalg import qr
    _, r, piv = qr(X, mode="economic", pivoting=True)
    diag = np.abs(np.diag(r))
    tol = diag[0] * max(X.shape) * np.finfo(float).eps if diag.size else 1.0
    keep = np.zeros(X.shape[1], dtype=bool)
    keep[piv[diag > tol]] = True
    return keep


def _cluster_meat(Z: np.ndarray, codes: np.ndarray) -> np.ndarray:
    """S = Σ_g v_g v_g' with v_g = Σ_{i∈g} z_i, via integer-coded grouping."""
    g = int(codes.max()) + 1
    V = np.zeros((g, Z.shape[1]))
    np.add.at(V, codes, Z)
    return V.T @ V


def ols_clustered(y: np.ndarray, X: np.ndarray, codes_a: np.ndarray,
                  codes_b: np.ndarray) -> dict:
    """OLS + Cameron-Gelbach-Miller two-way clustered covariance.

    V_twoway = V_a + V_b − V_intersection, the intersection clusters being
    the unique (a, b) pairs. Also returns the one-way variances."""
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    Z = X * (y - X @ beta)[:, None]           # rows x_i·u_i
    inter = np.unique(np.stack([codes_a, codes_b], axis=1), axis=0,
                      return_inverse=True)[1]
    Sa = _cluster_meat(Z, codes_a)
    Sb = _cluster_meat(Z, codes_b)
    Si = _cluster_meat(Z, inter)
    return {
        "beta": beta,
        "V_twoway": XtX_inv @ (Sa + Sb - Si) @ XtX_inv,
        "V_a": XtX_inv @ Sa @ XtX_inv,
        "V_b": XtX_inv @ Sb @ XtX_inv,
    }


def wild_cluster_bootstrap(y: np.ndarray, X: np.ndarray, col_idx: int,
                           codes_month: np.ndarray, n_boot: int = N_BOOT,
                           seed: int = SEED) -> float:
    """Rademacher wild cluster bootstrap on the month dimension, null imposed
    (§3.4). Bootstrap p-value for the coefficient at ``col_idx``, whose
    reference variance is month-clustered."""
    rng = np.random.default_rng(seed)
    k = X.shape[1]
    keep = np.ones(k, dtype=bool)
    keep[col_idx] = False
    Xr = X[:, keep]
    XtX_r_inv = np.linalg.inv(Xr.T @ Xr)
    gamma = XtX_r_inv @ Xr.T @ y
    fit_r = Xr @ gamma
    u = y - fit_r
    months = np.unique(codes_month)

    def _wald(y_: np.ndarray) -> float:
        XtX_inv = np.linalg.inv(X.T @ X)
        beta = XtX_inv @ X.T @ y_
        Z = X * (y_ - X @ beta)[:, None]
        S = _cluster_meat(Z, codes_month)
        V = XtX_inv @ S @ XtX_inv
        v = V[col_idx, col_idx]
        return beta[col_idx] ** 2 / v if v > 0 else np.inf

    w0 = _wald(y)
    n_ex = 0
    for _ in range(n_boot):
        w_map = dict(zip(months, rng.choice([-1.0, 1.0], size=len(months))))
        w_vec = np.array([w_map[c] for c in codes_month])
        if _wald(fit_r + w_vec * u) >= w0:
            n_ex += 1
    return n_ex / n_boot


# ---------------------------------------------------------------------------
# estimation
# ---------------------------------------------------------------------------

def run_h1(sample: pd.DataFrame, label: str) -> dict:
    """Stacked regression of SPEC §3.4 on one sample."""
    base = sample.reset_index(drop=True)
    n = len(base)
    L = pd.DataFrame(np.repeat(base.values, 2, axis=0), columns=base.columns)
    L["td"] = pd.to_datetime(L["td"])
    L["flagged"] = np.tile([0.0, 1.0], n)
    is_jump = L["flagged"] == 1.0
    L["car"] = np.where(is_jump, L["jump"], L["runup"])
    L["liq_x_flag"] = L["liq"] * L["flagged"]
    L["hf"] = (L["filer_type"] == "activist_hf").astype(float)
    L["corp"] = (L["filer_type"] == "corporate").astype(float)
    L["sic2"] = L["sic2"].fillna("NA").astype(str)
    L["month"] = L["td"].dt.to_period("M").astype(str)

    ctrl = ["liq", "liq_x_flag", "flagged", "logcap", "pre42",
            "wlen_busdays", "hf", "corp"]
    D = pd.get_dummies(L[["sic2", "yq"]].astype(str), drop_first=True,
                       dtype=float)
    X_full = np.column_stack([np.ones(len(L)), L[ctrl].values.astype(float),
                              D.values])
    names_full = ["const"] + ctrl + list(D.columns)
    keep_cols = _independent_columns(X_full)
    dropped_cols = [nm for nm, k in zip(names_full, keep_cols) if not k]
    X = X_full[:, keep_cols]
    names = [nm for nm, k in zip(names_full, keep_cols) if k]
    y = L["car"].values.astype(float)
    a_codes = pd.factorize(L["permno"].values)[0]
    m_codes = pd.factorize(L["month"].values)[0]

    fit = ols_clustered(y, X, a_codes, m_codes)
    beta = fit["beta"]
    V = fit["V_twoway"]
    se = np.sqrt(np.clip(np.diag(V), 0, None))
    k = names.index("liq_x_flag")
    i1 = names.index("liq")
    se_b2 = float(se[k])
    t_b2 = float(beta[k] / se_b2) if se_b2 > 0 else np.nan
    p_b2 = float(2 * (1 - _norm_cdf(abs(t_b2)))) if math.isfinite(t_b2) else 1.0
    p_wild = wild_cluster_bootstrap(y, X, k, m_codes)
    var_sum = V[i1, i1] + V[k, k] + 2 * V[i1, k]
    return {
        "label": label,
        "n_filings": n,
        "n_stacked_rows": len(L),
        "n_clusters_permno": int(pd.unique(a_codes).size),
        "n_clusters_month": int(pd.unique(m_codes).size),
        "beta_liq_pooled": float(beta[i1]),
        "se_liq_pooled": float(se[i1]),
        "beta_liq_flagged_sum": float(beta[i1] + beta[k]),
        "flagged_slope_se": float(math.sqrt(max(var_sum, 0.0))),
        "beta2_partition": float(beta[k]),
        "beta3_flagged_level": float(beta[names.index("flagged")]),
        "se_beta2_twoway": se_b2,
        "t_beta2": t_b2,
        "p_beta2_normal": p_b2,
        "p_beta2_wild_month": p_wild,
        "p_beta2_quoted_conservative": max(p_b2, p_wild),
        "mde_beta2_pp": float(Z_MDE * se_b2 * 100),
        "n_rank_dropped_columns": len(dropped_cols),
        "dropped_columns": dropped_cols[:50],
        "coefficients": {nm: float(b) for nm, b in zip(names, beta)},
        "se_twoway": {nm: float(s) for nm, s in zip(names, se)},
        "note_se": ("two-way CGM on (PERMNO, month of TD), intersection = "
                    "unique (firm, month) pairs — a firm filing in two "
                    "months contributes to both, so the intersection is "
                    "finer than the firm cluster"),
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="H1 partition test (SPEC §3.4)")
    ap.add_argument("--limit", type=int, default=0,
                    help="smoke: first N matched filings only")
    args = ap.parse_args(argv)

    os.makedirs(OUT_DIR, exist_ok=True)
    print("== inputs ==", flush=True)
    jsonl_hash = sha256_of(FACT2_JSONL)
    df = load_filings()
    print(f"  fact2_parsed.jsonl sha256 {jsonl_hash[:16]}... -> {len(df)} rows",
          flush=True)

    print("== CRSP panel ==", flush=True)
    crsp = CrspPanel()

    # -- funnel (§2.3, registered route) ------------------------------------
    has_td = df["td"].notna()
    gap = (df["fd"] - df["td"]).dt.days
    band = df[has_td & gap.between(0, 90)].copy()
    permnos, reasons, n_obs = [], [], []
    for r in band.itertuples():
        c8 = r.cusip8
        if c8 is None or (isinstance(c8, float) and math.isnan(c8)):
            permnos.append(None); reasons.append("no_cusip"); n_obs.append(0)
            continue
        cands = crsp.cusip_link.get(c8, ())
        if not cands:
            permnos.append(None); reasons.append("cusip_not_in_crsp")
            n_obs.append(0)
            continue
        best_p, best_n = None, -1
        for p in cands:
            n = count_valid_obs(crsp.panel[int(p)], r.td)
            if n > best_n:
                best_p, best_n = int(p), n
        if best_n < 60:
            permnos.append(None); reasons.append("insufficient_obs")
            n_obs.append(best_n)
        else:
            permnos.append(best_p); reasons.append("matched")
            n_obs.append(best_n)
    band[["permno", "match_reason", "n_valid_obs"]] = pd.DataFrame(
        {"permno": permnos, "match_reason": reasons, "n_valid_obs": n_obs},
        index=band.index)
    matched = band[band["match_reason"] == "matched"].copy()

    keep, flagged_second, dropped_exact = [], [], []
    matched = matched.sort_values(["permno", "td", "fd", "accession"])
    for _, g in matched.groupby("permno", sort=False):
        last_kept = None
        seen_td = set()
        for r in g.itertuples():
            if r.td in seen_td:
                dropped_exact.append(r.Index)
                continue
            if last_kept is not None and (r.td - last_kept).days < 365:
                flagged_second.append(r.Index)
                continue
            seen_td.add(r.td)
            keep.append(r.Index)
            last_kept = r.td
    final = matched.loc[matched.index.isin(keep)].copy()
    if args.limit:
        final = final.head(args.limit)
    funnel = {
        "enumerated": len(df),
        "trigger_parsed": int(has_td.sum()),
        "band_0_90": len(band),
        "crsp_matched": len(matched),
        "keep_first_final": len(final),
        "flagged_second": len(flagged_second),
        "dropped_exact": len(dropped_exact),
    }
    print(f"  funnel: {funnel}", flush=True)

    # -- per-filing variables -------------------------------------------------
    print("== per-filing variables ==", flush=True)
    rows = []
    n_model_fail = n_fdstar_na = n_zero_runup = n_jump_short = 0
    for r in final.itertuples():
        panel = crsp.panel[int(r.permno)]
        fdstar, how = effective_filing_date(r.fd, r.accepted,
                                            crsp.trade_days)
        if pd.isna(fdstar):
            n_fdstar_na += 1
            continue
        model = market_model(panel, r.td, crsp.market)
        if model is None:
            n_model_fail += 1
            continue
        runup = car(panel, crsp.market, model, r.td,
                    fdstar - pd.Timedelta(days=1), crsp.trade_days)
        # JUMP on trading-day offsets (§3.1): the trading day before FD*,
        # FD*, and the trading day after — calendar bounds would drop the
        # preceding Friday for Monday filings (49% of the sample)
        j_lo, j_hi, j_n = trading_day_window(fdstar, crsp.trade_days, 1, 1)
        if j_n is not None and j_n < 3:
            n_jump_short += 1
        jump = car(panel, crsp.market, model, j_lo, j_hi, crsp.trade_days)
        pre42 = car(panel, crsp.market, model, r.td - pd.Timedelta(days=42),
                    r.td - pd.Timedelta(days=6), crsp.trade_days)
        # RUNUP5: fixed five-trading-day window from the trigger (§3.1) —
        # first trading day on/after TD through the 4th after it
        i5 = np.searchsorted(crsp.trade_days, np.datetime64(r.td.date(), "D"))
        if i5 < len(crsp.trade_days):
            r5_hi = pd.Timestamp(str(crsp.trade_days[min(i5 + 4,
                                                        len(crsp.trade_days) - 1)]))
            runup5 = car(panel, crsp.market, model,
                         pd.Timestamp(str(crsp.trade_days[i5])), r5_hi,
                         crsp.trade_days)
        else:
            runup5 = np.nan
        # FD* ≡ FD robustness CARs (§2.4)
        runup_fdeq = car(panel, crsp.market, model, r.td,
                         r.fd - pd.Timedelta(days=1), crsp.trade_days)
        f_lo, f_hi, _ = trading_day_window(r.fd, crsp.trade_days, 1, 1)
        jump_fdeq = car(panel, crsp.market, model, f_lo, f_hi,
                        crsp.trade_days)
        if fdstar <= r.td:
            n_zero_runup += 1
        # trading days accumulated in the run-up (for the per-day defence)
        rt_i = np.searchsorted(crsp.trade_days, np.datetime64(r.td.date(), "D"))
        rt_j = np.searchsorted(crsp.trade_days,
                               np.datetime64((fdstar - pd.Timedelta(days=1)).date(), "D"),
                               side="right")
        runup_tdays = int(max(rt_j - rt_i, 0))
        sl = _slice(panel, r.td - pd.Timedelta(days=126),
                    r.td - pd.Timedelta(days=6))
        v = panel["valid"][sl]
        ret, prc, vol = panel["ret"][sl], panel["prc"][sl], panel["vol"][sl]
        if v.sum() >= 60:
            illiq = float(np.mean(np.abs(ret[v]) / (np.abs(prc[v])
                                                    * vol[v])) * 1e6)
        else:
            illiq = np.nan
        cap_day = r.td - pd.Timedelta(days=6)
        i = np.searchsorted(panel["dates"], np.datetime64(cap_day.date(), "D"),
                            side="right") - 1
        logcap = (float(np.log(panel["cap"][i]))
                  if i >= 0 and np.isfinite(panel["cap"][i])
                  and panel["cap"][i] > 0 else np.nan)
        wlen = business_delay(r.td.date(), fdstar.date())
        rows.append({
            "accession": r.accession, "subject_cik": r.subject_cik,
            "filer_cik": r.filer_cik, "filer_name": r.filer_name,
            "permno": int(r.permno), "td": r.td, "fd": r.fd, "fdstar": fdstar,
            "fdstar_how": how, "post_td": int(r.td >= RULE_DATE),
            "gap_days": int((r.fd - r.td).days),
            "runup": runup, "jump": jump, "pre42": pre42,
            "runup5": runup5, "runup_trading_days": runup_tdays,
            "runup_fdeq": runup_fdeq, "jump_fdeq": jump_fdeq,
            "illiq": illiq, "logcap": logcap, "wlen_busdays": float(wlen),
            "pct_of_class": r.pct_of_class,
        })
    est = pd.DataFrame(rows)
    print(f"  {len(est)} filings with a market model ({n_model_fail} failed "
          f"the 120-day requirement, {n_fdstar_na} FD* beyond the snapshot)",
          flush=True)

    # LIQ: quarter-standardised (§3.2)
    est["logilliq"] = np.log(est["illiq"].where(est["illiq"] > 0))
    est["yq"] = (est["td"].dt.year.astype(str) + "Q"
                 + est["td"].dt.quarter.astype(str))
    est["liq"] = est.groupby("yq")["logilliq"].transform(
        lambda s: -(s - s.mean()) / s.std() if s.std() > 0 else np.nan)

    # filer type (overrides + regex) and SIC2
    ft = classify_filers(est)
    est["filer_type"] = ft
    n_filer_overridden = ft.attrs.get("n_overridden", 0)

    def _sic(cik) -> Optional[str]:
        try:
            p = os.path.join(SUBMISSIONS_DIR,
                             f"CIK{int(str(cik).strip()):010d}.json")
            with open(p, "rb") as fh:
                head = fh.read(4096).decode("utf-8", errors="replace")
            m = re.search(r'"sic"\s*:\s*"?(\d{2,4})', head)
            return m.group(1)[:2] if m else None
        except (OSError, ValueError):
            return None

    est["sic2"] = est["subject_cik"].map(_sic)

    # -- main sample restrictions (§2.5 straddlers, §2.6 stub) ---------------
    straddle = (est["td"] < RULE_DATE) & (est["fd"] >= RULE_DATE)
    stub = (est["td"] >= ADOPTION_DATE) & (est["td"] < RULE_DATE)
    needed = ["runup", "jump", "liq", "logcap", "pre42", "wlen_busdays"]
    n_car_missing = int(est.loc[~straddle & ~stub,
                                needed].isna().any(axis=1).sum())
    main_s = est[~straddle & ~stub].dropna(subset=needed).copy()
    full_s = est.dropna(subset=needed).copy()
    print(f"  main sample: {len(main_s)} of {len(est)} "
          f"(straddlers {int(straddle.sum())}, stub {int(stub.sum())}, "
          f"variable-missing {n_car_missing}); filer overrides applied to "
          f"{n_filer_overridden} rows", flush=True)

    h1_main = run_h1(main_s, "main")
    h1_full = run_h1(full_s, "full_funnel_robustness")

    # robustness rows registered by §2.4 (FD* ≡ FD) and §2.3 filter 5
    # (what a Zeng-style 1-13 calendar-day delay screen would leave)
    fd_eq = main_s.copy()
    fd_eq["runup"] = fd_eq["runup_fdeq"]
    fd_eq["jump"] = fd_eq["jump_fdeq"]
    h1_fdeq = run_h1(fd_eq.dropna(subset=["runup", "jump"]),
                     "fdstar_equal_fd_robustness")
    zeng = main_s[main_s["gap_days"].between(1, 13)]
    h1_zeng = run_h1(zeng, "zeng_delay_screen_robustness")

    # §3.6 realised MDEs (registered) quoted alongside
    mde_registered = None
    rc_path = os.path.join(OUT_DIR, "reparse_counts.json")
    if os.path.exists(rc_path):
        with open(rc_path) as fh:
            rc = json.load(fh)
        m = rc.get("mde", {}).get("s36_estimation_sample", {})
        mde_registered = {k: m.get(k) for k in ("jump", "runup")}

    result = {
        "estimate": "H1 partition test (SPEC §3.4)",
        "label": "ESTIMATED",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "inputs": {"fact2_jsonl_sha256": jsonl_hash,
                   "crsp": os.path.basename(CRSP_PATH),
                   "filer_overrides_present":
                       os.path.exists(FILER_OVERRIDES)},
        "funnel": funnel,
        "sample": {"full_funnel_with_model": len(est),
                   "market_model_failures": n_model_fail,
                   "fdstar_beyond_snapshot": n_fdstar_na,
                   "zero_length_runup_windows": n_zero_runup,
                   "jump_windows_shorter_than_3_tdays": n_jump_short,
                   "straddlers_excluded": int(straddle.sum()),
                   "stub_excluded": int(stub.sum()),
                   "variable_missing": n_car_missing,
                   "main_n": len(main_s),
                   "main_pre": int((main_s["td"] < RULE_DATE).sum()),
                   "main_post": int((main_s["td"] >= RULE_DATE).sum()),
                   "full_n": len(full_s),
                   "zeng_screen_n": len(zeng)},
        "liquidity_reporting_s36": {
            "sd_logilliq_within_sample": float(est["logilliq"].std()),
            "iqr_logilliq": float(est["logilliq"].quantile(0.75)
                                  - est["logilliq"].quantile(0.25)),
            "note": ("§3.6: the within-sample sd of log ILLIQ is reported "
                     "next to every slope coefficient; effects quote per "
                     "sd of LIQ (=1 by construction) and per IQR of "
                     "log ILLIQ")},
        "filer_type_distribution": est["filer_type"].value_counts().to_dict(),
        "sic2_missing": int(est["sic2"].isna().sum()),
        "h1_main": h1_main,
        "h1_full": h1_full,
        "h1_fdstar_equal_fd": h1_fdeq,
        "h1_zeng_delay_screen": h1_zeng,
        "mde_registered_s36_estimation_sample": mde_registered,
        "seeds": {"wild_bootstrap": SEED},
    }
    out_path = os.path.join(OUT_DIR, "h1_estimate.json")
    with open(out_path, "w") as fh:
        json.dump(result, fh, indent=1)
    est.to_csv(os.path.join(OUT_DIR, "h1_sample.csv"), index=False)
    print(f"wrote {out_path} and h1_sample.csv", flush=True)

    h = h1_main
    print("\n== H1 (main sample) — ESTIMATED ==")
    print(f"  N filings {h['n_filings']} (stacked rows {h['n_stacked_rows']}; "
          f"clusters: {h['n_clusters_permno']} firms, "
          f"{h['n_clusters_month']} months)")
    print(f"  β1 (pooled LIQ slope)      {h['beta_liq_pooled']:+.5f} "
          f"(se {h['se_liq_pooled']:.5f})")
    print(f"  β1+β2 (flagged LIQ slope)  {h['beta_liq_flagged_sum']:+.5f} "
          f"(se {h['flagged_slope_se']:.5f})")
    print(f"  β2 (PARTITION)             {h['beta2_partition']:+.5f}  "
          f"se {h['se_beta2_twoway']:.5f}  t {h['t_beta2']:+.2f}")
    print(f"  p: normal {h['p_beta2_normal']:.4f}, wild-month "
          f"{h['p_beta2_wild_month']:.4f} -> quoted "
          f"{h['p_beta2_quoted_conservative']:.4f}")
    print(f"  MDE(β2) = 2.802·se = {h['mde_beta2_pp']:.4f} pp")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
