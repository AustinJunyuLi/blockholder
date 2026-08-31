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

**Stage E — estimation.**  SPEC §8.4, linear probability model, with the two
matched dimensions carried as the X_i'θ adjustment terms:

    BID12_i = α + β(Treat×Post) + γTreat + λPost + logcap + logilliq
              + δ_match + ε

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
RECOVERY_CSV = os.path.join(OUT_DIR, "delisted_control_cik_recovery.csv")
SUBMISSIONS_DIRS = (os.path.join(DATA_DIR, "submissions"),
                    os.path.join(DATA_DIR, "bid12_cache", "submissions"))
MATCH_OUT = os.path.join(OUT_DIR, "did_match_pairs.csv")
QUALITY_OUT = os.path.join(OUT_DIR, "did_match_quality.csv")
SHORTFALL_OUT = os.path.join(OUT_DIR, "did_match_shortfalls.csv")
MATCH_META_OUT = os.path.join(OUT_DIR, "did_match_meta.json")
RESULT_OUT = os.path.join(OUT_DIR, "did_estimate.json")

N_BOOT = 9_999
SEED = 20260830
MATCH_RATIO = 3
CALIPER_SD = 0.25
TIGHT_CALIPER_SD = 0.20
STD_DIFF_LIMIT = 0.10          # §8.2: above this, report and tighten
MAIN_SAMPLE_END = pd.Timestamp("2024-12-17")
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

def build_treated(*, main_sample: bool = False) -> tuple:
    """Treated rows with BID12 and the H1 covariates; plus the funnel counts.

    The shared loader keeps 2024-12-18 onward rows so downstream extension
    code can see them. The registered main sample ends 2024-12-17; pass
    ``main_sample=True`` to drop the structured-data regime and the 2025
    extension from the matching/estimation frame.
    """
    tr = pd.read_csv(TREATED_CSV, dtype={"cik": str, "subject_name": str})
    tr["td"] = pd.to_datetime(tr["td"])
    tr["fd"] = pd.to_datetime(tr["date_filed"])
    funnel = {"bid12_treated_rows": len(tr)}

    after_main = tr["td"] > MAIN_SAMPLE_END
    funnel["main_sample_end"] = str(MAIN_SAMPLE_END.date())
    funnel["excluded_structured_data_regime"] = int(after_main.sum())
    funnel["extension_2025_rows"] = int((tr["td"].dt.year == 2025).sum())
    funnel["extension_2025_policy"] = "extension-only; excluded from main"
    if main_sample:
        tr = tr[~after_main].copy()

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


def _listed_false(raw: object) -> bool:
    return str(raw).strip().lower() in {"0", "false", "f", "no", "n"}


def apply_recovery_gate(mapped: pd.DataFrame, controls: pd.DataFrame,
                        recovery: pd.DataFrame | None = None
                        ) -> tuple[dict[int, str], dict]:
    """Permit a recovered CIK only when its validation row says so.

    Ticker-route links are unchanged. A ``13f_name_unique`` map row without a
    matching ``validated`` recovery row is refused, so an unvalidated CIK
    cannot enter matching. Delisted controls that remain unlinked stay out of
    the pool and are counted as the option-1 fallback.
    """
    validated: dict[int, str] = {}
    if recovery is not None and len(recovery):
        for row in recovery.itertuples():
            if str(getattr(row, "status", "")).strip() != "validated":
                continue
            cik = str(getattr(row, "cik", "")).strip()
            if not cik:
                continue
            validated[int(row.permno)] = cik

    allowed: dict[int, str] = {}
    n_refused = 0
    n_recovered = 0
    for row in mapped.itertuples():
        permno = int(row.permno)
        cik = str(getattr(row, "cik", "")).strip()
        if cik in ("", "nan"):
            continue
        route = str(getattr(row, "map_route", "")).strip()
        if route == "13f_name_unique":
            if validated.get(permno) != cik:
                n_refused += 1
                continue
            n_recovered += 1
        allowed[permno] = cik

    delisted_permnos = []
    if "still_listed" in controls.columns:
        delisted_permnos = [int(p) for p, listed in zip(
            controls["permno"], controls["still_listed"]) if _listed_false(listed)]
    n_delisted = len(delisted_permnos)
    n_unresolved = sum(1 for p in delisted_permnos if p not in allowed)
    n_delisted_linked = n_delisted - n_unresolved
    option_1 = n_unresolved > 0 or recovery is None
    if recovery is None:
        gate = "option_1_fallback"
    elif n_recovered:
        gate = "passed_with_validated_rows"
    else:
        gate = "option_1_fallback"
    counts = {
        "n_delisted_controls": n_delisted,
        "n_delisted_in_pool": n_delisted_linked,
        "n_recovered_validated": n_recovered,
        "n_unresolved_delisted": n_unresolved,
        "refused_unvalidated_recovery": n_refused,
        "recovery_gate_status": gate,
        "option_1_fallback": option_1,
        "control_bid_rate_bias": "down",
        "gamma_bias": "up",
        "survivorship_note": (
            "control group is conditioned on survival for unresolved "
            "delisted PERMNOs; treated side keeps acquired firms"),
    }
    return allowed, counts


def control_pool(crsp: CrspPanel) -> tuple:
    """Never-13D PERMNOs that are usable as controls, with their SIC2."""
    ctrl = pd.read_csv(CONTROL_CSV)
    pm = pd.read_csv(PERMNO_MAP_CSV, dtype=str)
    recovery = None
    if os.path.exists(RECOVERY_CSV):
        recovery = pd.read_csv(RECOVERY_CSV, dtype=str)
    p2c, rec_counts = apply_recovery_gate(pm, ctrl, recovery)

    counts = {"control_universe": len(ctrl), **rec_counts}
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
          sic_by_permno: dict, caliper_sd: float = CALIPER_SD) -> tuple:
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
          f"(calipers {caliper_sd * sd['logcap']:.3f} / "
          f"{caliper_sd * sd['logilliq']:.3f})", flush=True)

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
            if abs(c["logcap"] - row["logcap"]) > caliper_sd * sd["logcap"]:
                continue
            if abs(c["logilliq"] - row["logilliq"]) > caliper_sd * sd["logilliq"]:
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


def shortfalls_by_cell(tr: pd.DataFrame,
                       per_treated: pd.DataFrame) -> pd.DataFrame:
    """3:1 match shortfalls by the registered exact SIC2 x quarter cell."""
    d = tr[["accession", "sic2", "quarter"]].merge(
        per_treated[["accession", "n_matches"]], on="accession", how="left",
        validate="one_to_one")
    d["n_matches"] = d["n_matches"].fillna(0).astype(int)
    d["pair_shortfall"] = (MATCH_RATIO - d["n_matches"]).clip(lower=0)
    d["full"] = (d["n_matches"] == MATCH_RATIO).astype(int)
    d["short"] = (d["n_matches"] < MATCH_RATIO).astype(int)
    return (d.groupby(["sic2", "quarter"], as_index=False)
            .agg(treated_rows=("accession", "size"),
                 pairs_matched=("n_matches", "sum"),
                 pair_shortfall=("pair_shortfall", "sum"),
                 treated_with_3_matches=("full", "sum"),
                 treated_with_fewer_than_3=("short", "sum"))
            .assign(pairs_requested=lambda x: x["treated_rows"] * MATCH_RATIO)
            [["sic2", "quarter", "treated_rows", "pairs_requested",
              "pairs_matched", "pair_shortfall", "treated_with_3_matches",
              "treated_with_fewer_than_3"]]
            .sort_values(["quarter", "sic2"]).reset_index(drop=True))


def balance_decision(quality: pd.DataFrame, caliper_sd: float) -> str:
    """Registered one-rerun gate for post-match standardised differences."""
    if not quality["exceeds_0.10"].astype(bool).any():
        return "pass"
    return ("retry_tighter" if math.isclose(caliper_sd, CALIPER_SD)
            else "failed_balance")


def stage_match() -> tuple:
    tr, funnel = build_treated(main_sample=True)
    print(f"treated matched sample: {len(tr)} "
          f"({funnel['treated_pre']} pre / {funnel['treated_post']} post)")
    for k, v in funnel.items():
        print(f"  {k}: {v}")

    print("== CRSP panel ==", flush=True)
    crsp = CrspPanel()
    pool, sic_by_permno, cik_by_permno, pool_counts = control_pool(crsp)
    for k, v in pool_counts.items():
        print(f"  control pool {k}: {v}")

    attempts = []
    for caliper_sd in (CALIPER_SD, TIGHT_CALIPER_SD):
        print(f"== match attempt: {caliper_sd:.2f} pooled-sd caliper ==",
              flush=True)
        pairs, per_treated, cov_cache = match(
            tr, crsp, pool, sic_by_permno, caliper_sd=caliper_sd)
        q = match_quality(tr, pairs, cov_cache)
        bad = q[q["exceeds_0.10"]]["covariate"].tolist()
        decision = balance_decision(q, caliper_sd)
        attempts.append({
            "caliper_pooled_sd": caliper_sd,
            "n_pairs": len(pairs),
            "balance_exceeds_0.10": bad,
            "match_quality_std_diffs": q.to_dict(orient="records"),
            "decision": decision,
        })
        if decision != "retry_tighter":
            break
        print("  balance exceeds 0.10; rerunning once at the predeclared "
              "0.20 caliper", flush=True)

    pairs.to_csv(MATCH_OUT, index=False)
    dist = per_treated["n_matches"].value_counts().sort_index().to_dict()
    n_full = int((per_treated["n_matches"] == MATCH_RATIO).sum())
    print(f"wrote {MATCH_OUT}: {len(pairs)} pairs for "
          f"{int((per_treated['n_matches'] > 0).sum())} of {len(tr)} treated "
          f"rows; matches-per-treated distribution {dist}")
    print(f"  {MATCH_RATIO}:1 achieved for {n_full}/{len(tr)} "
          f"({100 * n_full / max(len(tr), 1):.1f}%) — the shortfall is the "
          f"tight-pool outcome SPEC §8.2 asks to be reported, not assumed away")

    q.to_csv(QUALITY_OUT, index=False)
    print(f"wrote {QUALITY_OUT}")
    print(q.to_string(index=False))
    shortfalls = shortfalls_by_cell(tr, per_treated)
    shortfalls.to_csv(SHORTFALL_OUT, index=False)
    print(f"wrote {SHORTFALL_OUT}: {len(shortfalls)} SIC2 x quarter cells")
    if bad:
        print(f"  standardised difference above {STD_DIFF_LIMIT} on: "
              f"{bad} after the {caliper_sd:.2f} caliper — estimation blocked")

    meta = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "design_status": "pass" if decision == "pass" else "failed_balance",
        "selected_caliper_sd": caliper_sd,
        "balance_exceeds_0.10": bad,
        "attempts": attempts,
        "treated_funnel": funnel,
        "control_pool": pool_counts,
        "inputs": {p: sha256_of(p) for p in
                   (TREATED_CSV, CONTROL_CSV, H1_SAMPLE_CSV, PERMNO_MAP_CSV)},
        "matching": {
            "ratio_target": MATCH_RATIO,
            "n_pairs": len(pairs),
            "matches_per_treated": {str(k): int(v) for k, v in dist.items()},
            "no_replacement_scope": "per (PERMNO, calendar quarter)",
        },
        "shortfalls": {
            "artifact": SHORTFALL_OUT,
            "n_sic2_quarter_cells": len(shortfalls),
            "cells_with_shortfall": int((shortfalls["pair_shortfall"] > 0).sum()),
            "pairs_requested": int(shortfalls["pairs_requested"].sum()),
            "pairs_matched": int(shortfalls["pairs_matched"].sum()),
            "pair_shortfall": int(shortfalls["pair_shortfall"].sum()),
        },
        "sample_window": {
            "main_end": str(MAIN_SAMPLE_END.date()),
            "2025": "extension-only; excluded from main estimate",
        },
        "s2": {
            "status": "not_estimated",
            "reason": "corporate-action Item-4 coding is absent; no S2 row was synthesized",
        },
    }
    with open(MATCH_META_OUT, "w") as fh:
        json.dump(meta, fh, indent=1)
    print(f"wrote {MATCH_META_OUT}: {meta['design_status']}")
    return tr, pairs, per_treated, q, funnel, pool_counts, meta


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


def conditional_fe_logit(D: pd.DataFrame, terms: list[str]) -> dict:
    """Conditional match-FE logit and AME for the Treat x Post term."""
    from itertools import combinations
    from scipy.optimize import brentq, minimize
    from scipy.special import expit, logsumexp

    y = D["bid12"].to_numpy(dtype=float)
    if not np.isin(y, (0.0, 1.0)).all():
        return {"status": "not_estimated",
                "blocker": "conditional logit requires binary BID12 rows"}
    pieces = []
    for group, g in D.groupby("match_group", sort=False):
        Xg = g[terms].to_numpy(dtype=float)
        yg = g["bid12"].to_numpy(dtype=int)
        successes = int(yg.sum())
        if successes in (0, len(g)):
            continue
        stats = np.array([Xg[list(ix)].sum(axis=0)
                          for ix in combinations(range(len(g)), successes)])
        pieces.append((group, str(pd.Timestamp(g["td"].iloc[0]).to_period("M")),
                       Xg[yg == 1].sum(axis=0), stats))
    if not pieces:
        return {"status": "not_estimated",
                "blocker": "no match group has within-group BID12 variation"}

    def objective(beta: np.ndarray) -> tuple[float, np.ndarray]:
        value = 0.0
        gradient = np.zeros(len(terms))
        for _, _, observed, stats in pieces:
            logits = stats @ beta
            weights = np.exp(logits - logsumexp(logits))
            value += float(logsumexp(logits) - observed @ beta)
            gradient += weights @ stats - observed
        return value, gradient

    fit = minimize(lambda b: objective(b)[0], np.zeros(len(terms)),
                   jac=lambda b: objective(b)[1], method="BFGS",
                   options={"gtol": 1e-9, "maxiter": 1000})
    gradient_norm = float(np.linalg.norm(objective(fit.x)[1], ord=np.inf))
    if not np.isfinite(fit.x).all() or (not fit.success and gradient_norm > 1e-6):
        return {"status": "not_estimated",
                "blocker": "conditional-FE logit did not converge",
                "optimizer_message": str(fit.message),
                "gradient_inf_norm": gradient_norm}

    beta = fit.x
    information = np.zeros((len(terms), len(terms)))
    month_scores: dict[str, np.ndarray] = {}
    for _, month, observed, stats in pieces:
        logits = stats @ beta
        weights = np.exp(logits - logsumexp(logits))
        mean = weights @ stats
        centered = stats - mean
        information += (centered.T * weights) @ centered
        month_scores.setdefault(month, np.zeros(len(terms)))
        month_scores[month] += observed - mean
    if np.linalg.matrix_rank(information) < len(terms):
        return {"status": "not_estimated",
                "blocker": "conditional-FE logit terms are not jointly identified"}
    bread = np.linalg.inv(information)
    meat = sum(np.outer(score, score) for score in month_scores.values())
    if len(month_scores) > 1:
        meat *= len(month_scores) / (len(month_scores) - 1)
    covariance = bread @ meat @ bread
    se = np.sqrt(np.clip(np.diag(covariance), 0, None))

    k = terms.index("treat_x_post")
    marginal = []
    for _, g in D.groupby("match_group", sort=False):
        Xg = g[terms].to_numpy(dtype=float)
        yg = g["bid12"].to_numpy(dtype=float)
        successes = int(yg.sum())
        if successes == 0:
            probability = np.zeros(len(g))
        elif successes == len(g):
            probability = np.ones(len(g))
        else:
            xb = Xg @ beta
            # The group intercept solves fitted successes = observed
            # successes. It is monotone in alpha, but its root sits at
            # roughly -mean(xb), and matching drives the within-group
            # covariate spread towards zero, which is exactly the regime
            # where the conditional-logit coefficients blow up and |xb|
            # runs to tens. A fixed [-50, 50] bracket then fails to
            # straddle the root and brentq raises. Centre the bracket on
            # the data and widen it until it does straddle.
            lo, hi = -float(np.max(xb)) - 1.0, -float(np.min(xb)) + 1.0
            f = lambda a: float(expit(a + xb).sum() - successes)
            for _ in range(60):
                if f(lo) < 0 < f(hi):
                    break
                lo -= 10.0
                hi += 10.0
            else:
                return {"status": "not_estimated",
                        "blocker": "conditional-FE logit group intercept "
                                   "has no bracketed root; the fitted "
                                   "coefficients are degenerate"}
            alpha = brentq(f, lo, hi)
            probability = expit(alpha + xb)
        marginal.extend(beta[k] * probability * (1 - probability))
    z = float(beta[k] / se[k]) if se[k] > 0 else float("nan")
    return {
        "status": "estimated",
        "method": "conditional logit; match-group fixed effects conditioned out",
        "fixed_effects": "match group, conditioned out",
        "terms": terms,
        "n": len(D),
        "match_groups": int(D["match_group"].nunique()),
        "informative_match_groups": len(pieces),
        "month_clusters": len(month_scores),
        "coefficient_treat_x_post": float(beta[k]),
        "se_month_clustered_treat_x_post": float(se[k]),
        "z_treat_x_post": z,
        "p_normal_treat_x_post": float(
            2 * (1 - 0.5 * math.erfc(-abs(z) / math.sqrt(2)))),
        "average_marginal_effect_treat_x_post": float(np.mean(marginal)),
        "average_marginal_effect_definition":
            "mean beta*p*(1-p) over the same matched rows; group intercepts "
            "solve fitted successes = observed successes",
        "optimizer": {"success": bool(fit.success),
                      "message": str(fit.message),
                      "gradient_inf_norm": gradient_norm},
    }


# SPEC §8.6 anchors: p_T = 0.181, p_C = 0.072, so sigma^2_T + sigma^2_C/3 =
# 0.1705, and the clustering multiplier is 1.31. These are the registered
# design inputs, not anything measured here.
VAR_TERM_SEC86 = 0.1705
CLUSTER_MULT_SEC86 = 1.31


def design_mde_pp(n_pre: int, n_post: int) -> dict:
    """§8.6's counts-based MDE. Design arithmetic, never a realised MDE.

    A realised MDE is Z x SE from an estimated regression. On the
    design-failure path no regression exists, so this is the only MDE that can
    honestly be printed, and it is labelled as what it is.
    """
    if n_pre <= 0 or n_post <= 0:
        return {"n_pre": int(n_pre), "n_post": int(n_post),
                "status": "not_computable",
                "reason": "a period with no treated rows"}
    inv = 1.0 / n_pre + 1.0 / n_post
    se = math.sqrt(VAR_TERM_SEC86 * inv)
    mde = Z_MDE * se
    return {
        "n_pre": int(n_pre), "n_post": int(n_post),
        "basis": "SPEC §8.6 arithmetic on the realised treated counts: "
                 "p_T = 0.181, p_C = 0.072 (Greenwood-Schor Table 6), "
                 "variance term 0.1705, clustering multiplier 1.31",
        "se_pp": se * 100,
        "mde_pp": mde * 100,
        "mde_pp_clustered": mde * CLUSTER_MULT_SEC86 * 100,
        "not_a_realised_mde": "no regression was estimated on this path; a "
                              "realised MDE is Z x SE from a fitted model",
    }


def survivorship_block(pool_counts: dict) -> dict:
    """The signed survivorship caveat. True whether or not an estimate exists."""
    return {
        "option_1_fallback": bool(pool_counts.get("option_1_fallback", True)),
        "recovery_gate_status": pool_counts.get(
            "recovery_gate_status", "option_1_fallback"),
        "n_unresolved_delisted": int(
            pool_counts.get("n_unresolved_delisted", 0)),
        "n_recovered_validated": int(
            pool_counts.get("n_recovered_validated", 0)),
        "control_bid_rate_bias": pool_counts.get(
            "control_bid_rate_bias", "down"),
        "gamma_bias": pool_counts.get("gamma_bias", "up"),
        "note": pool_counts.get(
            "survivorship_note",
            "control group is conditioned on survival for unresolved "
            "delisted PERMNOs; treated side keeps acquired firms"),
    }


class StaleMatchDraw(RuntimeError):
    """The frozen match draw was built from different inputs than are on disk."""


def load_match_state() -> tuple:
    """Load the frozen match draw for the estimate-only stage.

    Stage M records the SHA-256 of every input it consumed. Verify them
    rather than trusting them: a rebuilt treated file paired with a stale
    draw would estimate on one sample and report another sample's funnel,
    and nothing downstream would notice.
    """
    with open(MATCH_META_OUT) as fh:
        meta = json.load(fh)
    stale = [p for p, want in (meta.get("inputs") or {}).items()
             if os.path.exists(p) and sha256_of(p) != want]
    if stale:
        raise StaleMatchDraw(
            "the match draw in "
            f"{os.path.basename(MATCH_META_OUT)} was built from a different "
            f"version of: {', '.join(os.path.basename(p) for p in stale)}. "
            "Re-run --stage match before estimating.")
    tr, current_funnel = build_treated(main_sample=True)
    pairs = pd.read_csv(MATCH_OUT)
    quality = pd.read_csv(QUALITY_OUT)
    return (tr, pairs, quality, meta.get("treated_funnel", current_funnel),
            meta.get("control_pool", {}), meta)


def write_design_failure(meta: dict) -> int:
    """Record the registered hard stop without producing an estimate."""
    funnel = meta.get("treated_funnel", {})
    result = {
        "estimate": "Matched DiD on BID12 (SPEC §8, S1 primary)",
        "label": "NOT ESTIMATED",
        "status": "design_failure",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "script": "empirics/estimate_did.py",
        "reason": "post-match standardised differences remain above 0.10 "
                  "after the predeclared 0.20-caliper rerun",
        "treated_funnel": funnel,
        "control_pool": meta.get("control_pool", {}),
        "matching": {
            "caliper_pooled_sd": meta.get("selected_caliper_sd"),
            "balance_exceeds_0.10": meta.get("balance_exceeds_0.10", []),
            "attempts": meta.get("attempts", []),
        },
        "sample_window": {
            "main_end": str(MAIN_SAMPLE_END.date()),
            "2025": "extension-only; excluded from main estimate",
        },
        "s2": {
            "status": "not_estimated",
            "reason": "corporate-action Item-4 coding is absent; no S2 row was synthesized",
        },
        "quote_as_result": False,
        "quote_as_result_until": (
            "control half of the BID12 blind audit (protocol section 5); the "
            "design failure above is a separate and prior bar"),
        "survivorship": survivorship_block(meta.get("control_pool", {})),
        "mde_pp_design_arithmetic": design_mde_pp(
            int(funnel.get("treated_pre", 0)),
            int(funnel.get("treated_post", 0))),
        "bounded_null_ladder_pp": LADDER_PP,
    }
    with open(RESULT_OUT, "w") as fh:
        json.dump(result, fh, indent=1)
    print(f"design failure recorded in {RESULT_OUT}: {result['reason']}")
    return 3


def stage_estimate(tr: pd.DataFrame, pairs: pd.DataFrame,
                   funnel: dict, quality: pd.DataFrame,
                   pool_counts: dict, match_meta: dict | None = None) -> int:
    if not os.path.exists(CONTROL_LOOKUP_CSV):
        print(f"control BID12 lookup not landed ({CONTROL_LOOKUP_CSV}) — "
              f"matching stage written, estimation stage pending "
              f"(run empirics.bid12_control_lookup)")
        return 2
    cl = pd.read_csv(CONTROL_LOOKUP_CSV, dtype={"cik": str})
    cl["td"] = cl["td"].astype(str).str[:10]
    ckey = {(int(r.permno), str(r.td), str(r.match_group)): r
            for r in cl.itertuples()}

    rows = []
    for r in tr.itertuples():
        rows.append({"permno": int(r.permno), "td": str(r.td.date()),
                     "treat": 1, "post": int(r.post), "bid12": r.bid12,
                     "match_group": r.accession,
                     "logcap": float(r.logcap),
                     "logilliq": float(r.logilliq)})
    n_ctrl_missing = 0
    n_ctrl_prior_bid = 0
    for r in pairs.itertuples():
        key = (int(r.control_permno), str(r.treated_td), str(r.match_group))
        if key not in ckey:
            n_ctrl_missing += 1
            continue
        control = ckey[key]
        if getattr(control, "excluded_prior_bid", 0) == 1:
            n_ctrl_prior_bid += 1
            continue
        rows.append({"permno": int(r.control_permno), "td": str(r.treated_td),
                     "treat": 0, "post": int(r.treated_post),
                     "bid12": control.bid12, "match_group": r.match_group,
                     "logcap": float(r.control_logcap),
                     "logilliq": float(r.control_logilliq)})
    D = pd.DataFrame(rows)
    n_before = len(D)
    D = D[D["bid12"].notna()].copy()
    n_unresolved_rows = n_before - len(D)
    n_before_adjustments = len(D)
    D = D.dropna(subset=MATCHED_DIMS).copy()
    n_missing_adjustments = n_before_adjustments - len(D)
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
    terms = ["treat_x_post", "treat", *MATCHED_DIMS]
    Xw = np.column_stack([_demean(D[c].values.astype(float), g_codes)
                          for c in terms])
    keep = _independent_columns(Xw)
    Xw = Xw[:, keep]
    kept_terms = [c for c, k0 in zip(terms, keep) if k0]
    dropped_terms = [c for c, k0 in zip(terms, keep) if not k0]
    fit = ols_clustered(y, Xw, g_codes, m_codes)
    beta, V = fit["beta"], fit["V_twoway"]
    se = np.sqrt(np.clip(np.diag(V), 0, None))
    k = kept_terms.index("treat_x_post")
    t = float(beta[k] / se[k]) if se[k] > 0 else float("nan")
    p_n = float(2 * (1 - 0.5 * math.erfc(-abs(t) / math.sqrt(2))))
    p_w = wild_cluster_bootstrap(y, Xw, k, m_codes, n_boot=N_BOOT, seed=SEED)

    # FWL equivalence check against the explicit-dummy design (§ docstring).
    Xd = np.column_stack([
        np.ones(len(D)),
        D[[*terms, "post"]].values.astype(float),
        pd.get_dummies(D["match_group"].astype(str), drop_first=True,
                       dtype=float).values])
    dummy_names = ["const", *terms, "post"] + [
        f"match_group:{x}" for x in
        pd.get_dummies(D["match_group"].astype(str), drop_first=True).columns]
    kd = _independent_columns(Xd)
    Xd = Xd[:, kd]
    kept_dummy_names = [c for c, k0 in zip(dummy_names, kd) if k0]
    fit_d = ols_clustered(D["bid12"].values, Xd, g_codes, m_codes)
    se_d = np.sqrt(np.clip(np.diag(fit_d["V_twoway"]), 0, None))
    kd_beta = kept_dummy_names.index("treat_x_post")
    fwl = {"beta_dummy": float(fit_d["beta"][kd_beta]),
           "se_dummy": float(se_d[kd_beta]),
           "beta_abs_diff": float(abs(fit_d["beta"][kd_beta] - beta[k])),
           "se_abs_diff": float(abs(se_d[kd_beta] - se[k]))}

    logit = conditional_fe_logit(D, terms)

    treated_rate = float(D[D["treat"] == 1]["bid12"].mean())
    control_rate = float(D[D["treat"] == 0]["bid12"].mean())
    rate_by_cell = (D.groupby(["treat", "post"])["bid12"]
                    .agg(["mean", "size"]).reset_index())
    mde_pp = float(Z_MDE * se[k] * 100)

    result = {
        "estimate": "Matched DiD on BID12 (SPEC §8, S1 primary)",
        "label": "ESTIMATED",
        "status": "estimated",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "script": "empirics/estimate_did.py",
        "inputs": {p: sha256_of(p) for p in
                   (TREATED_CSV, CONTROL_LOOKUP_CSV, MATCH_OUT, QUALITY_OUT,
                    SHORTFALL_OUT, MATCH_META_OUT, H1_SAMPLE_CSV)
                   if os.path.exists(p)},
        "treated_funnel": funnel,
        "control_pool": pool_counts,
        "matching": {
            "ratio_target": MATCH_RATIO,
            "caliper_pooled_sd": (match_meta or {}).get(
                "selected_caliper_sd", CALIPER_SD),
            "exact": ["sic2", "quarter_of_TD (vacuous under pseudo-TD "
                      "inheritance — asserted, see module docstring)"],
            "n_pairs": len(pairs),
            "n_pairs_without_control_bid12": n_ctrl_missing,
            "no_replacement_scope": "per (PERMNO, calendar quarter)",
            "match_group": "treated accession",
            "shortfalls": (match_meta or {}).get("shortfalls", {}),
        },
        "match_quality_std_diffs": quality.to_dict(orient="records"),
        "match_quality_exceeds_0.10": quality[quality["exceeds_0.10"]]
        ["covariate"].tolist(),
        "sample": {
            "rows_before_unresolved_drop": n_before,
            "rows_dropped_unresolved_bid12": n_unresolved_rows,
            "rows_dropped_missing_adjustment_terms": n_missing_adjustments,
            "controls_excluded_prior_bid": n_ctrl_prior_bid,
            "match_groups_dropped_no_contrast": n_dropped_groups,
            "treated_n": int((D["treat"] == 1).sum()),
            "control_n": int((D["treat"] == 0).sum()),
            "match_groups": int(D["match_group"].nunique()),
            "month_clusters": int(len(np.unique(m_codes))),
            "treated_bid12_rate": treated_rate,
            "control_bid12_rate": control_rate,
            "rates_by_cell": rate_by_cell.to_dict(orient="records"),
            "treated_filer_own_bid": (
                int(pd.to_numeric(tr["filer_own_bid"], errors="coerce")
                    .fillna(0).sum()) if "filer_own_bid" in tr.columns else 0),
        },
        "quote_as_result": False,
        "quote_as_result_until": (
            "control half of the BID12 blind audit (protocol section 5)"),
        "survivorship": survivorship_block(pool_counts),
        "specification": {
            "model": "LPM, BID12 ~ beta(Treat x Post) + gamma Treat + "
                     "logcap + logilliq + delta_match (FWL-absorbed)",
            "adjustment_terms": MATCHED_DIMS,
            "terms_estimated": kept_terms,
            "terms_dropped_collinear": dropped_terms,
            "post_main_effect": "not identified — Post is constant within "
                                "match group (every member shares the treated "
                                "TD); max within-group deviation "
                                f"{post_within_var:.2e}",
            "se": "two-way clustered (match group, calendar month of TD), "
                  "Cameron-Gelbach-Miller",
            "fwl_check": fwl,
        },
        "logit_robustness": logit,
        "beta_treat_x_post": float(beta[k]),
        "beta_treat_x_post_pp": float(beta[k] * 100),
        "gamma_treat_pp": (float(beta[kept_terms.index("treat")] * 100)
                           if "treat" in kept_terms else None),
        "se_twoway": float(se[k]), "t": t,
        "p_normal": p_n, "p_wild_month": p_w,
        "p_quoted_conservative": max(p_n, p_w),
        "mde_pp_realised": mde_pp,
        "mde_pp_design_arithmetic": design_mde_pp(
            int(funnel.get("treated_pre", 0)),
            int(funnel.get("treated_post", 0))),
        "bounded_null_ladder_pp": LADDER_PP,
        "sample_window": {
            "main_end": str(MAIN_SAMPLE_END.date()),
            "2025": "extension-only; excluded from main estimate",
        },
        "s2": {
            "status": "not_estimated",
            "reason": "corporate-action Item-4 coding is absent; no S2 row was synthesized",
        },
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
    if args.stage == "estimate":
        for p in (TREATED_CSV, H1_SAMPLE_CSV, MATCH_OUT, QUALITY_OUT,
                  MATCH_META_OUT):
            if not os.path.exists(p):
                print(f"input not landed yet: {p}")
                return 1
        try:
            tr, pairs, quality, funnel, pool_counts, meta = load_match_state()
        except StaleMatchDraw as exc:
            print(str(exc))
            return 1
        if meta.get("design_status") != "pass":
            return write_design_failure(meta)
        return stage_estimate(tr, pairs, funnel, quality, pool_counts, meta)
    for p in (TREATED_CSV, CONTROL_CSV, H1_SAMPLE_CSV, PERMNO_MAP_CSV):
        if not os.path.exists(p):
            print(f"input not landed yet: {p}")
            return 1
    tr, pairs, per_treated, quality, funnel, pool_counts, meta = stage_match()
    if args.stage == "match":
        return 0 if meta["design_status"] == "pass" else write_design_failure(meta)
    if meta["design_status"] != "pass":
        return write_design_failure(meta)
    return stage_estimate(tr, pairs, funnel, quality, pool_counts, meta)


if __name__ == "__main__":
    raise SystemExit(main())
