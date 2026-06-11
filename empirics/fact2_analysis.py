"""Fact 2 analysis: 13D announcement CARs around the 2024 acceleration.

Inputs (see quality_reports/plans/2026-06-10_fact2-event-study-design.md):
  * empirics/output/fact2_filings.csv         -- EDGAR event file (fact2_events.py)
  * empirics/data/wrds_evtstudy.csv[.gz]      -- WRDS "U.S. Daily Event Study:
        Upload your own events" output, security-event-TIME level rows
        (uid/permno, evtdate, evttime, ret, abret [+ car at date level]),
        market model, est. window 220, gap 20, event window [-10, +10]
  * empirics/data/crsp_daily.csv[.gz]         -- CRSP CIZ daily stock file,
        2021-01-01..2025-12-31 for the matched PERMNOs: permno, dlycaldt,
        dlyret, dlyvol, dlyprc, dlycap, cusip, sharetype, securitytype,
        securitysubtype, usincflg, issuertype, primaryexch

Estimates (two-way clustered by subject PERMNO and calendar month):
  (1) CAR ~ Post                                       [beta > 0 predicted]
  (2) CAR ~ Post + lnAmihud + Post*lnAmihud + controls [delta < 0 predicted]
  (3) spec (2) + year-quarter FE (Post absorbed; interaction identified)

Outputs: empirics/output/fact2_summary.csv, fact2_regressions.csv,
fact2_car.pdf.

Usage:
    .venv/bin/python -m empirics.fact2_analysis
"""

from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "data")
OUT_DIR = os.path.join(HERE, "output")
RULE_DATE = pd.Timestamp("2024-02-05")

AMIHUD_WIN = (-250, -30)   # trading-day window for pre-event Amihud
RUNUP_WIN = (-60, -11)     # pre-event run-up window
SIZE_DAY = -30             # market cap measured here (nearest prior valid)
MIN_AMIHUD_OBS = 100


# --------------------------------------------------------------------------
# loading helpers
# --------------------------------------------------------------------------

def _find(path_base: str) -> str:
    for ext in ("", ".gz", ".csv", ".csv.gz"):
        p = path_base + ext
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f"missing input: {path_base}[.csv|.csv.gz]")


def load_evtstudy() -> pd.DataFrame:
    """Per-(cusip, evtdate, evttime) abnormal returns from the WRDS tool.

    Output schema (verified on query 11385273):
        Model,cusip,uid,evtdate,date,evttime,ret,abret
    with uid = "<permno>-<DDMONYYYY>" for matched events and ".-<date>" for
    events the tool could not match to CRSP (those rows have empty evttime
    and are dropped here).
    """
    path = _find(os.path.join(DATA_DIR, "wrds_evtstudy"))
    df = pd.read_csv(path, compression="infer")
    df.columns = [c.strip().lower() for c in df.columns]
    if "permno" not in df.columns:
        uid = df["uid"].astype(str)
        df["permno"] = pd.to_numeric(uid.str.extract(r"^(\d+)")[0],
                                     errors="coerce")
    df["evtdate"] = pd.to_datetime(df["evtdate"], errors="coerce")
    keep = [c for c in ("permno", "cusip", "evtdate", "evttime", "ret",
                        "abret", "date") if c in df.columns]
    df = df[keep].dropna(subset=["permno", "evtdate", "evttime"])
    df["permno"] = df["permno"].astype(int)
    df["evttime"] = df["evttime"].astype(int)
    df["cusip"] = df["cusip"].astype(str).str.strip().str[:8]
    return df


CRSP_COLS = ("permno", "dlycaldt", "dlyret", "dlyvol", "dlyprc", "dlycap",
             "cusip", "sharetype", "securitytype", "securitysubtype",
             "usincflg", "issuertype", "primaryexch", "ticker")


def load_crsp(permnos: set | None = None) -> pd.DataFrame:
    """CRSP CIZ daily file, chunk-filtered to ``permnos``.

    The web query that produced crsp_daily.csv returned the full 2021-2025
    universe (~11.9M rows, 1.13 GiB) because the WRDS form ignores
    JS-attached upload files; filtering locally per chunk keeps memory flat.
    """
    path = _find(os.path.join(DATA_DIR, "crsp_daily"))
    chunks = []
    for chunk in pd.read_csv(path, compression="infer",
                             usecols=lambda c: c.strip().lower() in CRSP_COLS,
                             chunksize=2_000_000, low_memory=False):
        chunk.columns = [c.strip().lower() for c in chunk.columns]
        chunk["permno"] = pd.to_numeric(chunk["permno"], errors="coerce")
        chunk = chunk.dropna(subset=["permno"])
        if permnos is not None:
            chunk = chunk[chunk["permno"].isin(permnos)]
        chunks.append(chunk)
    df = pd.concat(chunks, ignore_index=True)
    df["dlycaldt"] = pd.to_datetime(df["dlycaldt"], errors="coerce")
    for col in ("dlyret", "dlyvol", "dlyprc", "dlycap"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["permno", "dlycaldt"])
    df["permno"] = df["permno"].astype(int)
    return df.sort_values(["permno", "dlycaldt"]).reset_index(drop=True)


def is_common_stock(g: pd.DataFrame) -> pd.Series:
    """CIZ-v2 equivalent of legacy share codes 10/11 (US common)."""
    need = ("sharetype", "securitytype", "securitysubtype", "usincflg",
            "issuertype")
    if not all(c in g.columns for c in need):
        return pd.Series(True, index=g.index)  # fields not pulled -> no filter
    return ((g["sharetype"] == "NS") & (g["securitytype"] == "EQTY")
            & (g["securitysubtype"] == "COM") & (g["usincflg"] == "Y")
            & (g["issuertype"].isin(["ACOR", "CORP"])))


# --------------------------------------------------------------------------
# per-event pre-period measures from CRSP daily
# --------------------------------------------------------------------------

def event_measures(crsp: pd.DataFrame, events: pd.DataFrame) -> pd.DataFrame:
    """Amihud, ln size, run-up, common-stock flag, cusip8 per (permno, evtdate)."""
    crsp = crsp.copy()
    crsp["dollar_vol"] = crsp["dlyprc"].abs() * crsp["dlyvol"]
    crsp["illiq"] = np.where(crsp["dollar_vol"] > 0,
                             crsp["dlyret"].abs() / crsp["dollar_vol"] * 1e6,
                             np.nan)
    crsp["common"] = is_common_stock(crsp)
    if "cusip" in crsp.columns:
        crsp["cusip8"] = crsp["cusip"].astype(str).str[:8]

    out = []
    for permno, g in crsp.groupby("permno", sort=False):
        evs = events[events["permno"] == permno]
        if evs.empty:
            continue
        dates = g["dlycaldt"].to_numpy()
        for _, ev in evs.iterrows():
            pos = int(np.searchsorted(dates, np.datetime64(ev["evtdate"])))
            if pos >= len(dates):
                continue
            lo, hi = pos + AMIHUD_WIN[0], pos + AMIHUD_WIN[1]
            rlo, rhi = pos + RUNUP_WIN[0], pos + RUNUP_WIN[1]
            spos = pos + SIZE_DAY
            rec = {"permno": permno, "evtdate": ev["evtdate"]}
            if lo >= 0:
                ill = g["illiq"].iloc[lo:hi + 1].dropna()
                rec["amihud"] = ill.mean() if len(ill) >= MIN_AMIHUD_OBS else np.nan
                rec["n_amihud"] = len(ill)
            else:
                rec["amihud"], rec["n_amihud"] = np.nan, 0
            if rlo >= 0:
                rr = g["dlyret"].iloc[rlo:rhi + 1].dropna()
                rec["runup"] = float(np.prod(1 + rr) - 1) if len(rr) >= 20 else np.nan
            else:
                rec["runup"] = np.nan
            cap = (g["dlycap"].iloc[max(0, spos - 5):spos + 1].dropna()
                   if spos >= 0 else pd.Series(dtype=float))
            rec["lnsize"] = float(np.log(cap.iloc[-1])) if len(cap) else np.nan
            at_ev = g.iloc[min(pos, len(g) - 1)]
            rec["common"] = bool(at_ev["common"])
            rec["cusip8"] = at_ev.get("cusip8")
            out.append(rec)
    return pd.DataFrame(out)


# --------------------------------------------------------------------------
# OLS with one/two-way clustered standard errors (CGM)
# --------------------------------------------------------------------------

def _ols(y: np.ndarray, X: np.ndarray):
    XtX_inv = np.linalg.pinv(X.T @ X)
    beta = XtX_inv @ (X.T @ y)
    resid = y - X @ beta
    return beta, resid, XtX_inv


def _cluster_meat(X: np.ndarray, resid: np.ndarray, groups: np.ndarray):
    meat = np.zeros((X.shape[1], X.shape[1]))
    for gval in np.unique(groups):
        idx = groups == gval
        Xg = X[idx]
        ug = resid[idx]
        s = Xg.T @ ug
        meat += np.outer(s, s)
    return meat, len(np.unique(groups))


def ols_twoway(y, X, g1, g2):
    """OLS point estimates + CGM two-way clustered covariance."""
    n, k = X.shape
    beta, resid, bread = _ols(y, X)
    m1, G1 = _cluster_meat(X, resid, g1)
    m2, G2 = _cluster_meat(X, resid, g2)
    g12 = pd.factorize(pd.Series(g1).astype(str) + "_"
                       + pd.Series(g2).astype(str))[0]
    m12, _ = _cluster_meat(X, resid, g12)
    V = bread @ (m1 + m2 - m12) @ bread
    Gmin = min(G1, G2)
    V *= Gmin / max(Gmin - 1, 1) * (n - 1) / max(n - k, 1)
    se = np.sqrt(np.maximum(np.diag(V), 0))
    tstat = np.divide(beta, se, out=np.full_like(beta, np.nan), where=se > 0)
    from scipy import stats
    pval = 2 * stats.t.sf(np.abs(tstat), df=max(Gmin - 1, 1))
    r2 = 1 - resid @ resid / ((y - y.mean()) @ (y - y.mean()))
    return beta, se, tstat, pval, r2


def run_spec(df: pd.DataFrame, ycol: str, rhs: list, fe_yq: bool,
             label: str) -> list:
    sub = df.dropna(subset=[ycol] + rhs).copy()
    cols = list(rhs)
    X = [np.ones(len(sub))]
    names = ["const"]
    for c in cols:
        X.append(sub[c].to_numpy(float))
        names.append(c)
    if fe_yq:
        dummies = pd.get_dummies(sub["yq"], drop_first=True, dtype=float)
        for c in dummies.columns:
            X.append(dummies[c].to_numpy())
            names.append(f"yq_{c}")
    Xm = np.column_stack(X)
    y = sub[ycol].to_numpy(float)
    beta, se, t, p, r2 = ols_twoway(
        y, Xm, sub["permno"].to_numpy(), sub["month"].to_numpy())
    rows = []
    for i, nm in enumerate(names):
        if nm.startswith("yq_"):
            continue
        rows.append({"spec": label, "depvar": ycol, "param": nm,
                     "coef": beta[i], "se": se[i], "t": t[i], "p": p[i],
                     "n": len(sub), "r2": r2, "yq_fe": fe_yq})
    return rows


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    evt = load_evtstudy()
    crsp = load_crsp(permnos=set(evt["permno"].unique()))
    filings = pd.read_csv(os.path.join(OUT_DIR, "fact2_filings.csv"),
                          low_memory=False)
    filings["event_trade_date"] = pd.to_datetime(filings["event_trade_date"])

    # CARs from per-day abnormal returns
    daily = evt[evt["evttime"].between(-10, 10)]
    car = daily.pivot_table(index=["permno", "cusip", "evtdate"],
                            columns="evttime", values="abret",
                            aggfunc="first")
    cars = pd.DataFrame(index=car.index)
    cars["car_m1_p1"] = car.loc[:, [c for c in (-1, 0, 1) if c in car]].sum(
        axis=1, min_count=3)
    cars["car_m10_p1"] = car.loc[:, [c for c in range(-10, 2) if c in car]].sum(
        axis=1, min_count=10)
    cars = cars.reset_index()

    # pre-event measures (by permno) + filing covariates (by cusip, evtdate)
    meas = event_measures(crsp, cars[["permno", "evtdate"]])
    meas = meas.drop(columns=["cusip8"], errors="ignore")
    df = cars.merge(meas, on=["permno", "evtdate"], how="left")
    fil = filings.dropna(subset=["cusip8"]).copy()
    fil = fil.drop_duplicates(subset=["cusip8", "event_trade_date"])
    df = df.merge(
        fil[["cusip8", "event_trade_date", "subject_cik", "filer_name",
             "pct_of_class", "quarter", "filed"]],
        left_on=["cusip", "evtdate"], right_on=["cusip8", "event_trade_date"],
        how="left")

    df["filed"] = pd.to_datetime(df["filed"], errors="coerce")
    df["post"] = (df["evtdate"] >= RULE_DATE).astype(float)
    df["month"] = df["evtdate"].dt.to_period("M").astype(str)
    df["yq"] = df["evtdate"].dt.to_period("Q").astype(str)
    df["ln_amihud"] = np.log(df["amihud"].where(df["amihud"] > 0))
    df["post_x_lnamihud"] = df["post"] * df["ln_amihud"]
    df["pct"] = pd.to_numeric(df["pct_of_class"], errors="coerce")
    hf_pat = (r"capital|partners|fund|management|advis|value|invest|"
              r"asset|activ|opportunit")
    df["hf_filer"] = (df["filer_name"].astype(str).str.lower()
                      .str.contains(hf_pat, regex=True)).astype(float)

    # sample filters: US common stock, sane CARs
    n0 = len(df)
    df = df[df["common"].fillna(False)]
    df = df[df["car_m1_p1"].abs() < 1.0]
    print(f"events: {n0} matched by WRDS -> {len(df)} after common-stock & "
          f"CAR-sanity filters; post share {df['post'].mean():.2f}")

    # summary
    summ = (df.groupby("post")[["car_m1_p1", "car_m10_p1", "amihud",
                                "lnsize"]]
            .agg(["count", "mean", "median"]))
    os.makedirs(OUT_DIR, exist_ok=True)
    summ.to_csv(os.path.join(OUT_DIR, "fact2_summary.csv"))
    print(summ.to_string())

    # regressions
    rows = []
    for ycol in ("car_m1_p1", "car_m10_p1"):
        rows += run_spec(df, ycol, ["post"], False, "1_level")
        rows += run_spec(df, ycol,
                         ["post", "ln_amihud", "post_x_lnamihud",
                          "lnsize", "runup", "pct", "hf_filer"],
                         False, "2_interaction")
        rows += run_spec(df, ycol,
                         ["ln_amihud", "post_x_lnamihud",
                          "lnsize", "runup", "pct", "hf_filer"],
                         True, "3_interaction_yqFE")
    reg = pd.DataFrame(rows)
    reg.to_csv(os.path.join(OUT_DIR, "fact2_regressions.csv"), index=False)
    show = reg[reg["param"].isin(["post", "ln_amihud", "post_x_lnamihud"])]
    print("\n", show.to_string(index=False))

    # figure: mean CAR path, pre vs post
    sys.path.insert(0, os.path.join(HERE, ".."))
    from pyfig import style
    style.apply_style()
    fig, ax = style.new_ax()
    daily2 = daily.merge(df[["permno", "evtdate", "post"]],
                         on=["permno", "evtdate"], how="inner")
    for post_val, color, lab in ((0.0, "#4477aa", "pre (10-calendar-day rule)"),
                                 (1.0, "#ee6677", "post (5-business-day rule)")):
        sub = daily2[daily2["post"] == post_val]
        path = (sub.groupby("evttime")["abret"].mean().sort_index().cumsum())
        n_ev = sub[["permno", "evtdate"]].drop_duplicates().shape[0]
        ax.plot(path.index, 100 * path.values, color=color,
                label=f"{lab} (n={n_ev})")
    ax.axvline(0, color="black", linestyle="--", linewidth=0.6)
    ax.axhline(0, color="black", linewidth=0.4)
    ax.set_xlabel("Trading day relative to 13D filing")
    ax.set_ylabel("Mean cumulative abnormal return (%)")
    ax.set_title("Fact 2: 13D Announcement Returns, Pre vs Post Acceleration")
    ax.legend(fontsize=8)
    style.save_fig(fig, os.path.join(OUT_DIR, "fact2_car.pdf"))
    print(f"\nwrote {OUT_DIR}/fact2_summary.csv, fact2_regressions.csv, "
          f"fact2_car.pdf")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
