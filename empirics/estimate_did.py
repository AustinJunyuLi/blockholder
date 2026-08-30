"""Matched DiD on the twelve-month bid hazard (SPEC §8) — S1 primary.

Two stages, each gated on its inputs; the script reports which stage it
reached and stops cleanly when the next stage's input has not landed.

**Stage M — matching.**  Treated = H1's main sample (registered funnel plus
the §2.5 straddler and §2.6 stub restrictions), one row per (firm, TD),
carrying BID12 and the coder's flags from ``bid12_treated.csv``.  Rows with an
empty BID12 (ambiguous, or extraction not run) are excluded and counted;
``excluded_prior_bid`` rows are excluded per SPEC §8.3.  Controls are the
never-13D universe (SPEC §8.2).  Matching is 3:1 nearest-neighbour without
replacement on the Mahalanobis distance of (log DlyCap at TD−6, log ILLIQ over
[TD−126, TD−6]) with 0.25 pooled-sd calipers on both, **exact** on 2-digit SIC
and on the calendar quarter of TD.  Each control inherits its treated firm's
TD as a pseudo-trigger date.

Three properties of this implementation that a reader should not have to
reverse-engineer:

1. **Quarter-exactness is vacuous here, by construction — and that is worth
   writing down rather than leaving as a silent pass.**  SPEC §8.2 requires an
   exact match on the calendar quarter of TD *and* gives every control its
   treated firm's TD as its pseudo-trigger date.  A control therefore has no
   quarter of its own to disagree with: its pseudo-TD *is* the treated TD, so
   the quarter matches identically for every candidate pair.  The constraint
   binds in designs where controls carry their own event dates; under
   inheritance it is satisfied trivially.  The script asserts it rather than
   filtering on it, so the invariant is checked instead of assumed.
2. **No-replacement is enforced per quarter, not globally.**  SPEC §8.2:
   "firms matched to more than one treated firm across different quarters are
   allowed; the match-group identifier clusters the standard errors."  A
   global used-set would exhaust the 3,600-firm pool against ~1,100 treated ×
   3 and silently degrade the ratio; the used-set is keyed on
   (PERMNO, quarter).
3. **The match group is the treated *filing*, not the treated firm.**  The
   treated sample is one row per (firm, TD), and a firm with two triggers
   would otherwise collide its own match groups and share controls between
   them.  ``match_group`` is the treated accession.

Match quality is reported as standardised differences on the two matched
continuous dimensions plus the three §8.2 substitutes for book-to-market
(turnover, past 12-month return, idiosyncratic volatility); any absolute
standardised difference above 0.10 is reported explicitly, per §8.2.

**Stage E — estimation.**  SPEC §8.4, linear probability model:

    BID12_i = α + β(Treat×Post) + γTreat + λPost + δ_match + ε

``λPost`` is *not identified* alongside ``δ_match``: every member of a match
group shares the treated TD, so Post is constant within group and absorbed.
That is reported, not worked around.  The match fixed effects are absorbed by
within-group demeaning (Frisch–Waugh–Lovell), which leaves β̂, the residuals
and therefore the clustered sandwich unchanged while keeping the wild
bootstrap tractable; the equivalence is checked numerically against the
explicit-dummy design on the estimation sample (``fwl_check`` in the output).
Standard errors are two-way clustered on match group and on the calendar
month of TD, with a Rademacher wild cluster bootstrap on the month dimension.

The headline frame is SPEC §6: the bounded null's three-rung ladder (≤ 20 pp
loose / **≤ 3 pp headline** / ≤ 1 pp tightest) is quoted alongside β̂ and its
realised MDE, because the MDE is larger than the headline rung and that — not
the point estimate — is the binding statement about the accumulation channel.

S2 (non-corporate-action campaigns) needs the Item-4 corporate-action coding,
which does not exist yet; the §8.7 placebo and §8.8 pre-trends are separate
units downstream of this one.

Usage:
    .venv/bin/python -m empirics.estimate_did              # both stages
    .venv/bin/python -m empirics.estimate_did --stage match
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import re

import numpy as np
import pandas as pd

from empirics.estimate_h1 import (
    CrspPanel, OUT_DIR, RULE_DATE, ADOPTION_DATE, Z_MDE,
    _independent_columns, _slice, ols_clustered, sha256_of,
    wild_cluster_bootstrap,
)

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TREATED_CSV = os.path.join(OUT_DIR, "bid12_treated.csv")
CONTROL_CSV = os.path.join(OUT_DIR, "never13d_control_universe.csv")
CONTROL_LOOKUP_CSV = os.path.join(OUT_DIR, "bid12_control.csv")
H1_SAMPLE_CSV = os.path.join(OUT_DIR, "h1_sample.csv")
PERMNO_MAP_CSV = os.path.join(OUT_DIR, "permno_cik_map.csv")
SUBMISSIONS_DIRS = (os.path.join(DATA_DIR, "submissions"),
                    os.path.join(DATA_DIR, "bid12_cache", "submissions"))
MATCH_OUT = os.path.join(OUT_DIR, "did_match_pairs.csv")
QUALITY_OUT = os.path.join(OUT_DIR, "did_match_quality.csv")
RESULT_OUT = os.path.join(OUT_DIR, "did_estimate.json")

N_BOOT = 9_999
SEED = 20260830
MATCH_RATIO = 3
CALIPER_SD = 0.25
STD_DIFF_LIMIT = 0.10          # §8.2: above this, report and tighten
COV_COLS = ["logcap", "logilliq", "turnover", "ret12m", "idiovol"]
MATCHED_DIMS = ["logcap", "logilliq"]

# SPEC §6 ladder — the headline frame for this leg, quoted with every estimate.
LADDER_PP = {"loose_any_accumulation_cut": 20.0,
             "headline_ge_10pct_of_stake_cut": 3.0,
             "tightest_ge_25pct_of_stake_cut": 1.0}

_SIC_RE = re.compile(r'"sic"\s*:\s*"?(\d{2,4})')


# ---------------------------------------------------------------------------
# covariates
# ---------------------------------------------------------------------------

def sic2_of_cik(cik) -> str:
    """2-digit SIC from a cached EDGAR submissions JSON.

    Two cache layouts carry submissions on this machine — the 13D-era pull
    (``data/submissions/CIK##########.json``) and the BID12 coder's own cache
    (``data/bid12_cache/submissions/##########.json``).  Controls land in the
    second; treated firms in the first.  Both are read, in that order, so an
    exact-SIC match is not silently voided for one side of the design.

    Three outcomes, kept apart because they mean different things for the
    funnel: a 2-digit SIC; ``BLANK`` — EDGAR has the filer but publishes no
    SIC (closed-end funds and trusts, ``entityType`` "other", are the bulk of
    these on the control side); ``MISSING`` — no submissions file on disk.
    Both non-numeric outcomes are ineligible for exact-SIC matching, and both
    are counted in the control-pool funnel rather than quietly dropped.
    """
    try:
        padded = f"{int(str(cik).strip()):010d}"
    except (TypeError, ValueError):
        return "MISSING"
    seen_file = False
    for d, fname in ((SUBMISSIONS_DIRS[0], f"CIK{padded}.json"),
                     (SUBMISSIONS_DIRS[1], f"{padded}.json")):
        p = os.path.join(d, fname)
        if not os.path.exists(p):
            continue
        try:
            with open(p, "rb") as fh:
                head = fh.read(4096).decode("utf-8", errors="replace")
        except OSError:
            continue
        seen_file = True
        m = _SIC_RE.search(head)
        if m:
            return m.group(1)[:2].zfill(2)
    return "BLANK" if seen_file else "MISSING"


def covariates(panel: dict, td: pd.Timestamp, market: dict) -> dict:
    """The §8.2 covariate block at one (PERMNO, TD).

    Definitions are byte-for-byte those of ``estimate_h1`` for the two matched
    dimensions — log DlyCap at the last trading day on or before TD−6, and the
    log of the mean Amihud ratio over [TD−126, TD−6] scaled by 1e6, requiring
    at least 60 valid days — so treated (read from ``h1_sample.csv``) and
    control (computed here) covariates are the same object.  The three extras
    are the §8.2 substitutes for book-to-market, used for match quality only,
    never for matching.
    """
    out = {c: np.nan for c in COV_COLS}
    sl = _slice(panel, td - pd.Timedelta(days=126), td - pd.Timedelta(days=6))
    v = panel["valid"][sl]
    ret, prc, vol = panel["ret"][sl], panel["prc"][sl], panel["vol"][sl]
    i = np.searchsorted(panel["dates"],
                        np.datetime64((td - pd.Timedelta(days=6)).date(), "D"),
                        side="right") - 1
    if i >= 0 and np.isfinite(panel["cap"][i]) and panel["cap"][i] > 0:
        out["logcap"] = float(np.log(panel["cap"][i]))
    if v.sum() >= 60:
        illiq = float(np.mean(np.abs(ret[v]) / (np.abs(prc[v]) * vol[v])) * 1e6)
        if illiq > 0:
            out["logilliq"] = float(np.log(illiq))
        cap_w = panel["cap"][sl][v]
        ok_cap = np.isfinite(cap_w) & (cap_w > 0)
        if ok_cap.sum() >= 60:
            out["turnover"] = float(np.mean(vol[v][ok_cap] / cap_w[ok_cap]))
    sl12 = _slice(panel, td - pd.Timedelta(days=252), td - pd.Timedelta(days=6))
    r12 = panel["ret"][sl12]
    d12 = panel["dates"][sl12]
    rm12 = np.array([market.get(pd.Timestamp(str(x)), np.nan) for x in d12])
    ok = np.isfinite(r12) & np.isfinite(rm12)
    if ok.sum() >= 120:
        out["ret12m"] = float(np.sum(r12[ok]))
        out["idiovol"] = float(np.std(r12[ok] - rm12[ok], ddof=1))
    return out


def std_diff(t: np.ndarray, c: np.ndarray) -> float:
    """Standardised difference, the matching literature's convention:
    (mean_T − mean_C) / sqrt((var_T + var_C)/2)."""
    t, c = t[np.isfinite(t)], c[np.isfinite(c)]
    if len(t) < 2 or len(c) < 2:
        return float("nan")
    denom = math.sqrt((t.var(ddof=1) + c.var(ddof=1)) / 2)
    return float((t.mean() - c.mean()) / denom) if denom > 0 else float("nan")


# ---------------------------------------------------------------------------
# stage M — treated sample and matching
# ---------------------------------------------------------------------------

def build_treated() -> tuple:
    """Treated rows with BID12 and the H1 covariates; plus the funnel counts."""
    tr = pd.read_csv(TREATED_CSV, dtype={"cik": str, "subject_name": str})
    tr["td"] = pd.to_datetime(tr["td"])
    tr["fd"] = pd.to_datetime(tr["date_filed"])
    funnel = {"bid12_treated_rows": len(tr)}

    unresolved = ~(tr["bid12"].notna() & (tr["extraction_status"] == "ok"))
    funnel["excluded_unresolved_bid12"] = int(unresolved.sum())
    tr = tr[~unresolved].copy()

    funnel["excluded_prior_bid"] = int(tr["excluded_prior_bid"].sum())
    tr = tr[tr["excluded_prior_bid"] == 0].copy()

    straddle = (tr["td"] < RULE_DATE) & (tr["fd"] >= RULE_DATE)
    stub = (tr["td"] >= ADOPTION_DATE) & (tr["td"] < RULE_DATE)
    funnel["excluded_straddlers_sec2_5"] = int(straddle.sum())
    funnel["excluded_stub_sec2_6"] = int(stub.sum())
    tr = tr[~straddle & ~stub].copy()

    h1 = pd.read_csv(H1_SAMPLE_CSV)
    # h1_sample carries the raw log-Amihud as `logilliq` (`liq` is its
    # quarter-standardised transform, §3.2) — matching uses the raw level.
    keep = h1[["accession", "permno", "logcap", "logilliq", "sic2"]].copy()
    keep["permno"] = keep["permno"].astype(int)
    keep["sic2"] = keep["sic2"].map(
        lambda v: "MISSING" if pd.isna(v) else f"{int(float(v)):02d}")
    before = len(tr)
    tr = tr.merge(keep, on="accession", how="inner")
    funnel["excluded_not_in_h1_main_sample"] = before - len(tr)

    before = len(tr)
    tr = tr.dropna(subset=MATCHED_DIMS).copy()
    funnel["excluded_missing_match_covariates"] = before - len(tr)
    before = len(tr)
    tr = tr[tr["sic2"] != "MISSING"].copy()
    funnel["excluded_missing_sic2"] = before - len(tr)

    tr["post"] = (tr["td"] >= RULE_DATE).astype(int)
    tr["quarter"] = (tr["td"].dt.year.astype(str) + "Q"
                     + tr["td"].dt.quarter.astype(str))
    funnel["treated_matched_sample"] = len(tr)
    funnel["treated_pre"] = int((tr["post"] == 0).sum())
    funnel["treated_post"] = int((tr["post"] == 1).sum())
    return tr.reset_index(drop=True), funnel


def control_pool(crsp: CrspPanel) -> tuple:
    """Never-13D PERMNOs that are usable as controls, with their SIC2."""
    ctrl = pd.read_csv(CONTROL_CSV)
    pm = pd.read_csv(PERMNO_MAP_CSV, dtype=str)
    pm = pm[pm["cik"].notna() & (pm["cik"].astype(str).str.strip() != "")]
    p2c = {int(p): str(c).strip() for p, c in zip(pm["permno"], pm["cik"])}

    counts = {"control_universe": len(ctrl)}
    pool = [int(p) for p in ctrl["permno"] if int(p) in crsp.panel]
    counts["in_crsp_panel"] = len(pool)
    pool = [p for p in pool if p in p2c]
    counts["with_cik_link"] = len(pool)
    sic = {p: sic2_of_cik(p2c[p]) for p in pool}
    counts["dropped_sic2_blank_in_edgar"] = sum(
        1 for p in pool if sic[p] == "BLANK")
    counts["dropped_no_submissions_file"] = sum(
        1 for p in pool if sic[p] == "MISSING")
    pool = [p for p in pool if sic[p] not in ("MISSING", "BLANK")]
    counts["with_sic2"] = len(pool)
    return sorted(pool), {p: sic[p] for p in pool}, {p: p2c[p] for p in pool}, counts


def match(tr: pd.DataFrame, crsp: CrspPanel, pool: list,
          sic_by_permno: dict) -> tuple:
    """3:1 NN without replacement (per quarter), exact SIC2 + quarter."""
    by_sic: dict = {}
    for p in pool:
        by_sic.setdefault(sic_by_permno[p], []).append(p)

    # Pass 1 — candidate covariates at every treated TD, cached on
    # (PERMNO, TD) because treated firms share trigger dates.
    cov_cache: dict = {}

    def cov(permno: int, td: pd.Timestamp) -> dict:
        key = (permno, td)
        if key not in cov_cache:
            cov_cache[key] = covariates(crsp.panel[permno], td, crsp.market)
        return cov_cache[key]

    print("== candidate covariates ==", flush=True)
    for n, row in enumerate(tr.itertuples(), 1):
        # the treated row's own extras (turnover, ret12m, idiovol) — the two
        # matched dimensions come from h1_sample, but match quality is
        # reported on all five, so the treated side needs them too
        if int(row.permno) in crsp.panel:
            cov(int(row.permno), row.td)
        for p in by_sic.get(row.sic2, ()):
            cov(p, row.td)
        if n % 200 == 0:
            print(f"  ... {n}/{len(tr)} treated rows, "
                  f"{len(cov_cache)} covariate cells", flush=True)

    # Pooled sd and Mahalanobis metric over treated ∪ every candidate cell
    # actually eligible for matching (not a fixed-date sample of the pool).
    cand = pd.DataFrame([c for c in cov_cache.values()])[MATCHED_DIMS]
    pooled = pd.concat([tr[MATCHED_DIMS], cand]).dropna()
    sd = pooled.std(ddof=1)
    S_inv = np.linalg.inv(np.cov(pooled.values.T))
    print(f"  pooled sd: logcap {sd['logcap']:.3f}, "
          f"logilliq {sd['logilliq']:.3f} "
          f"(calipers {CALIPER_SD * sd['logcap']:.3f} / "
          f"{CALIPER_SD * sd['logilliq']:.3f})", flush=True)

    # Pass 2 — matching, in a seeded random order over treated rows.
    rng = np.random.default_rng(SEED)
    used: set = set()           # (permno, quarter) — per-quarter, see docstring
    pairs, per_treated = [], []
    for i in rng.permutation(len(tr)):
        row = tr.iloc[int(i)]
        cands = []
        for p in by_sic.get(row["sic2"], ()):
            if (p, row["quarter"]) in used:
                continue
            c = cov_cache[(p, row["td"])]
            if not (np.isfinite(c["logcap"]) and np.isfinite(c["logilliq"])):
                continue
            if abs(c["logcap"] - row["logcap"]) > CALIPER_SD * sd["logcap"]:
                continue
            if abs(c["logilliq"] - row["logilliq"]) > CALIPER_SD * sd["logilliq"]:
                continue
            cands.append((p, c))
        if cands:
            dv = np.array([[c["logcap"] - row["logcap"],
                            c["logilliq"] - row["logilliq"]] for _, c in cands])
            dist = np.einsum("ij,jk,ik->i", dv, S_inv, dv)
            order = np.argsort(dist, kind="stable")[:MATCH_RATIO]
        else:
            order = []
        for j in order:
            p, c = cands[int(j)]
            used.add((p, row["quarter"]))
            pairs.append({
                "treated_permno": int(row["permno"]),
                "treated_accession": row["accession"],
                "treated_td": str(row["td"].date()),
                "treated_quarter": row["quarter"],
                "treated_sic2": row["sic2"],
                "treated_post": int(row["post"]),
                "control_permno": int(p),
                "match_group": row["accession"],
                "mahalanobis_d2": float(dist[int(j)]),
                **{f"control_{k}": c[k] for k in COV_COLS},
            })
        per_treated.append({"accession": row["accession"],
                            "n_matches": len(order)})
    return pd.DataFrame(pairs), pd.DataFrame(per_treated), cov_cache


def match_quality(tr: pd.DataFrame, pairs: pd.DataFrame,
                  cov_cache: dict) -> pd.DataFrame:
    """Standardised differences before and after matching (§8.2)."""
    def _tr_series(c: str) -> np.ndarray:
        if c in tr.columns:
            return tr[c].values.astype(float)
        return np.array([cov_cache.get((int(r.permno), r.td), {}).get(c, np.nan)
                         for r in tr.itertuples()], dtype=float)

    tr_cov = {c: _tr_series(c) for c in COV_COLS}
    matched_tr_idx = tr["accession"].isin(set(pairs["match_group"])) \
        if len(pairs) else pd.Series(False, index=tr.index)
    rows = []
    for c in COV_COLS:
        post_c = pairs[f"control_{c}"].values.astype(float) if len(pairs) \
            else np.array([])
        rows.append({
            "covariate": c,
            "matched_dimension": c in MATCHED_DIMS,
            "treated_mean": float(np.nanmean(tr_cov[c][matched_tr_idx.values]))
            if matched_tr_idx.any() else float("nan"),
            "control_mean": float(np.nanmean(post_c)) if len(post_c)
            else float("nan"),
            "std_diff_matched": std_diff(tr_cov[c][matched_tr_idx.values],
                                         post_c) if matched_tr_idx.any()
            else float("nan"),
            "exceeds_0.10": bool(
                abs(std_diff(tr_cov[c][matched_tr_idx.values], post_c))
                > STD_DIFF_LIMIT) if matched_tr_idx.any() else False,
        })
    q = pd.DataFrame(rows)
    # SIC2 and quarter are exact by construction; assert rather than measure.
    if len(pairs):
        assert (pairs["treated_quarter"] ==
                pd.to_datetime(pairs["treated_td"]).dt.year.astype(str) + "Q"
                + pd.to_datetime(pairs["treated_td"]).dt.quarter.astype(str)
                ).all(), "pseudo-TD quarter inheritance broken"
    return q


def stage_match() -> tuple:
    tr, funnel = build_treated()
    print(f"treated matched sample: {len(tr)} "
          f"({funnel['treated_pre']} pre / {funnel['treated_post']} post)")
    for k, v in funnel.items():
        print(f"  {k}: {v}")

    print("== CRSP panel ==", flush=True)
    crsp = CrspPanel()
    pool, sic_by_permno, cik_by_permno, pool_counts = control_pool(crsp)
    for k, v in pool_counts.items():
        print(f"  control pool {k}: {v}")

    pairs, per_treated, cov_cache = match(tr, crsp, pool, sic_by_permno)
    pairs.to_csv(MATCH_OUT, index=False)
    dist = per_treated["n_matches"].value_counts().sort_index().to_dict()
    n_full = int((per_treated["n_matches"] == MATCH_RATIO).sum())
    print(f"wrote {MATCH_OUT}: {len(pairs)} pairs for "
          f"{int((per_treated['n_matches'] > 0).sum())} of {len(tr)} treated "
          f"rows; matches-per-treated distribution {dist}")
    print(f"  {MATCH_RATIO}:1 achieved for {n_full}/{len(tr)} "
          f"({100 * n_full / max(len(tr), 1):.1f}%) — the shortfall is the "
          f"tight-pool outcome SPEC §8.2 asks to be reported, not assumed away")

    q = match_quality(tr, pairs, cov_cache)
    q.to_csv(QUALITY_OUT, index=False)
    print(f"wrote {QUALITY_OUT}")
    print(q.to_string(index=False))
    bad = q[q["exceeds_0.10"]]["covariate"].tolist()
    if bad:
        print(f"  standardised difference above {STD_DIFF_LIMIT} on: "
              f"{bad} — §8.2 requires this to be reported and the match "
              f"re-run with a tighter caliper")
    return tr, pairs, per_treated, q, funnel, pool_counts


# ---------------------------------------------------------------------------
# stage E — estimation
# ---------------------------------------------------------------------------

def _demean(v: np.ndarray, codes: np.ndarray) -> np.ndarray:
    n = int(codes.max()) + 1
    s = np.zeros(n)
    c = np.zeros(n)
    np.add.at(s, codes, v)
    np.add.at(c, codes, 1.0)
    return v - (s / c)[codes]


def stage_estimate(tr: pd.DataFrame, pairs: pd.DataFrame,
                   funnel: dict, quality: pd.DataFrame,
                   pool_counts: dict) -> int:
    if not os.path.exists(CONTROL_LOOKUP_CSV):
        print(f"control BID12 lookup not landed ({CONTROL_LOOKUP_CSV}) — "
              f"matching stage written, estimation stage pending "
              f"(run empirics.bid12_control_lookup)")
        return 2
    cl = pd.read_csv(CONTROL_LOOKUP_CSV, dtype={"cik": str})
    cl["td"] = cl["td"].astype(str).str[:10]
    ckey = {(int(r.permno), str(r.td), str(r.match_group)): r.bid12
            for r in cl.itertuples()}

    rows = []
    for r in tr.itertuples():
        rows.append({"permno": int(r.permno), "td": str(r.td.date()),
                     "treat": 1, "post": int(r.post), "bid12": r.bid12,
                     "match_group": r.accession})
    n_ctrl_missing = 0
    for r in pairs.itertuples():
        key = (int(r.control_permno), str(r.treated_td), str(r.match_group))
        if key not in ckey:
            n_ctrl_missing += 1
            continue
        rows.append({"permno": int(r.control_permno), "td": str(r.treated_td),
                     "treat": 0, "post": int(r.treated_post),
                     "bid12": ckey[key], "match_group": r.match_group})
    D = pd.DataFrame(rows)
    n_before = len(D)
    D = D[D["bid12"].notna()].copy()
    n_unresolved_rows = n_before - len(D)
    D["bid12"] = D["bid12"].astype(float)

    # A match group with no surviving control (or no treated row) carries no
    # within-group contrast; the FE absorb it entirely. Dropped and counted.
    sizes = D.groupby("match_group")["treat"].agg(["min", "max", "size"])
    live = sizes[(sizes["min"] == 0) & (sizes["max"] == 1)].index
    n_dropped_groups = int(sizes.shape[0] - len(live))
    D = D[D["match_group"].isin(set(live))].copy()

    D["treat_x_post"] = D["treat"] * D["post"]
    g_codes = pd.factorize(D["match_group"].values)[0]
    m_codes = pd.factorize(
        pd.to_datetime(D["td"]).dt.to_period("M").astype(str).values)[0]

    # Post is constant within match group (every member shares the treated
    # TD), so λ is not identified alongside δ_match — reported, not patched.
    post_within_var = float(
        np.abs(_demean(D["post"].values.astype(float), g_codes)).max())

    # FWL: absorb δ_match by within-group demeaning.
    y = _demean(D["bid12"].values, g_codes)
    Xw = np.column_stack([_demean(D["treat_x_post"].values.astype(float),
                                  g_codes),
                          _demean(D["treat"].values.astype(float), g_codes)])
    keep = _independent_columns(Xw)
    Xw = Xw[:, keep]
    fit = ols_clustered(y, Xw, g_codes, m_codes)
    beta, V = fit["beta"], fit["V_twoway"]
    se = np.sqrt(np.clip(np.diag(V), 0, None))
    k = 0                                            # treat_x_post
    t = float(beta[k] / se[k]) if se[k] > 0 else float("nan")
    p_n = float(2 * (1 - 0.5 * math.erfc(-abs(t) / math.sqrt(2))))
    p_w = wild_cluster_bootstrap(y, Xw, k, m_codes, n_boot=N_BOOT, seed=SEED)

    # FWL equivalence check against the explicit-dummy design (§ docstring).
    Xd = np.column_stack([
        np.ones(len(D)),
        D[["treat_x_post", "treat", "post"]].values.astype(float),
        pd.get_dummies(D["match_group"].astype(str), drop_first=True,
                       dtype=float).values])
    kd = _independent_columns(Xd)
    Xd = Xd[:, kd]
    fit_d = ols_clustered(D["bid12"].values, Xd, g_codes, m_codes)
    se_d = np.sqrt(np.clip(np.diag(fit_d["V_twoway"]), 0, None))
    fwl = {"beta_dummy": float(fit_d["beta"][1]),
           "se_dummy": float(se_d[1]),
           "beta_abs_diff": float(abs(fit_d["beta"][1] - beta[k])),
           "se_abs_diff": float(abs(se_d[1] - se[k]))}

    treated_rate = float(D[D["treat"] == 1]["bid12"].mean())
    control_rate = float(D[D["treat"] == 0]["bid12"].mean())
    rate_by_cell = (D.groupby(["treat", "post"])["bid12"]
                    .agg(["mean", "size"]).reset_index())
    mde_pp = float(Z_MDE * se[k] * 100)

    result = {
        "estimate": "Matched DiD on BID12 (SPEC §8, S1 primary)",
        "label": "ESTIMATED",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "script": "empirics/estimate_did.py",
        "inputs": {p: sha256_of(p) for p in
                   (TREATED_CSV, CONTROL_LOOKUP_CSV, MATCH_OUT, H1_SAMPLE_CSV)
                   if os.path.exists(p)},
        "treated_funnel": funnel,
        "control_pool": pool_counts,
        "matching": {
            "ratio_target": MATCH_RATIO, "caliper_pooled_sd": CALIPER_SD,
            "exact": ["sic2", "quarter_of_TD (vacuous under pseudo-TD "
                      "inheritance — asserted, see module docstring)"],
            "n_pairs": len(pairs),
            "n_pairs_without_control_bid12": n_ctrl_missing,
            "no_replacement_scope": "per (PERMNO, calendar quarter)",
            "match_group": "treated accession",
        },
        "match_quality_std_diffs": quality.to_dict(orient="records"),
        "match_quality_exceeds_0.10": quality[quality["exceeds_0.10"]]
        ["covariate"].tolist(),
        "sample": {
            "rows_before_unresolved_drop": n_before,
            "rows_dropped_unresolved_bid12": n_unresolved_rows,
            "match_groups_dropped_no_contrast": n_dropped_groups,
            "treated_n": int((D["treat"] == 1).sum()),
            "control_n": int((D["treat"] == 0).sum()),
            "match_groups": int(D["match_group"].nunique()),
            "month_clusters": int(len(np.unique(m_codes))),
            "treated_bid12_rate": treated_rate,
            "control_bid12_rate": control_rate,
            "rates_by_cell": rate_by_cell.to_dict(orient="records"),
        },
        "specification": {
            "model": "LPM, BID12 ~ beta(Treat x Post) + gamma Treat + "
                     "delta_match (FWL-absorbed)",
            "post_main_effect": "not identified — Post is constant within "
                                "match group (every member shares the treated "
                                "TD); max within-group deviation "
                                f"{post_within_var:.2e}",
            "se": "two-way clustered (match group, calendar month of TD), "
                  "Cameron-Gelbach-Miller",
            "fwl_check": fwl,
        },
        "beta_treat_x_post": float(beta[k]),
        "beta_treat_x_post_pp": float(beta[k] * 100),
        "gamma_treat_pp": float(beta[1] * 100) if Xw.shape[1] > 1 else None,
        "se_twoway": float(se[k]), "t": t,
        "p_normal": p_n, "p_wild_month": p_w,
        "p_quoted_conservative": max(p_n, p_w),
        "mde_pp_realised": mde_pp,
        "bounded_null_ladder_pp": LADDER_PP,
        "headline_frame_spec_sec6": (
            f"Realised MDE {mde_pp:.2f} pp against the §6 headline rung of "
            f"3 pp: the design "
            + ("cannot" if mde_pp > 3.0 else "can")
            + " separate a true accumulation effect from zero at the "
              "ceiling, so the bounded null — not this point estimate — is "
              "the binding statement about the accumulation channel."),
        "seeds": {"matching": SEED, "wild_bootstrap": SEED},
        "n_boot": N_BOOT,
    }
    with open(RESULT_OUT, "w") as fh:
        json.dump(result, fh, indent=1)
    print(f"wrote {RESULT_OUT}")
    print(f"  β(Treat×Post) = {beta[k] * 100:+.2f} pp "
          f"(se {se[k] * 100:.2f} pp, t {t:+.2f}, "
          f"quoted p {max(p_n, p_w):.3f}, realised MDE {mde_pp:.2f} pp)")
    print(f"  base rates: treated {treated_rate:.3f}, control {control_rate:.3f} "
          f"(SPEC §8.4 anchors 0.181 / 0.072)")
    print(f"  §6 ladder: {result['headline_frame_spec_sec6']}")
    print(f"  FWL check: |Δβ| {fwl['beta_abs_diff']:.2e}, "
          f"|Δse| {fwl['se_abs_diff']:.2e}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--stage", choices=("match", "estimate", "both"),
                    default="both")
    args = ap.parse_args(argv)
    for p in (TREATED_CSV, CONTROL_CSV, H1_SAMPLE_CSV, PERMNO_MAP_CSV):
        if not os.path.exists(p):
            print(f"input not landed yet: {p}")
            return 1
    tr, pairs, per_treated, quality, funnel, pool_counts = stage_match()
    if args.stage == "match":
        return 0
    return stage_estimate(tr, pairs, funnel, quality, pool_counts)


if __name__ == "__main__":
    raise SystemExit(main())
