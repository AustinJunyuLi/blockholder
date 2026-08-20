# E2 — Pre-specified empirical design

**Ticket:** `.scratch/v4-reposition/issues/10-e2-empirical-spec.md` · **Lane:** empirics (`v4`)
**Written:** 2026-08-20, before any estimation. **Status:** pre-specification, unverified.
**Position:** ADR-0006 (P2 partition + P4's bounded null + P4's matched DiD). **Model:** ADR-0007 (two-round).
**Vocabulary:** `CONTEXT.md`. **Inputs:** `research/empirics_v4/data_inventory.md`, `research/empirical_feasibility.md`, `research/cards/`.

---

## The design in one page

*Read this; §1–§13 are the reference behind it.*

**The headline is a timing split.** For every 13D we measure two things: the abnormal
return between the trigger (the 5% crossing) and the day before the filing — the **run-up**
— and the abnormal return on the filing day itself — the **jump**. The paper's claim is
that the disclosure rule partitions the market's information, so the *pooled* half (the
run-up) should move with liquidity and the *flagged* half (the jump) should not. That is
**H1**, it needs no input from the theory lane, and it is the paper's identity in one
regression pair (§3.4). **H2** asks whether the run-up's liquidity slope changed after the
February 2024 acceleration; that needs a sign from the theory lane, which has not landed,
so both possible signs are written out in advance (§3.5.2).

**One check can kill the paper's identity, and it runs first:** if the filing-day jump
moves with liquidity the same way the run-up does, there is no partition to write about.

**The control-outcome leg is a matched difference-in-differences** on whether a bid arrives
within twelve months, 13D targets against never-13D firms matched three-to-one on size,
illiquidity, industry and quarter (§8). It carries every referee-checklist item: control
group, ten named confounds, 568 placebo dates, pre-trends, a power calculation.

**The most important number in this document is a power number, not an estimate.** The
SEC's own tables cap the accumulation channel's effect on the bid hazard at about
**3 percentage points** (§6). The best this design can detect is **4.4** (§8.6). So the
difference-in-differences cannot, even in principle, separate the accumulation effect from
zero — it can only rule out a *large* effect. That is the leg's honest result, it is
written here before any estimate exists, and it goes in the paper's text, not a footnote.

**What has to happen before any estimate:** the whole 13D universe must be re-downloaded
and re-parsed with today's fixed parser (§2.2). The file on disk was built with the broken
one — 2025 trigger dates parse at 0%, and 132 renamed 2024 filings were silently dropped.
Every count in this document is a floor until that is done.

**What we cannot get:** takeover premia (offer price against unaffected price) have no free
source and SDC/Bloomberg is gated, so the control outcome for December is **bidder entry**,
not premium (§11 row 27).

---

## 0. What this document is, and the rule it imposes

Every estimate the December package will report is specified here — variable, window,
sample, specification, standard error, the power the design has, and **what result would
count as supportive and what would count as against**. Nothing below has been run. No
treatment effect has been estimated or looked at. The only numbers computed for this
document are **counts** (how many filings, how many firms) and **power arithmetic** from
those counts plus variance assumptions taken from the literature cards. Those two things
are pre-specification inputs, not results.

Three rules bind the tickets downstream (11 E3, 12 E4, 13 E5, 14 E6, 15 E7):

1. **No specification may be changed after an estimate is seen.** If a change is
   unavoidable, the original estimate is reported alongside it and the change is logged
   in `quality_reports/session_logs/`.
2. **A null is a result, reported with its minimum detectable effect (MDE).** Section 10
   fixes, in advance, the MDE each null must be quoted against.
3. **Honesty label is ESTIMATED** for everything in this document (CONTEXT.md): an
   empirical estimate with a standard error and a stated design. Nothing here is PROVED.

### 0.1 The theory-lane placeholder

> `[PLACEHOLDER — sign from HANDOFF_sign.md, absent as of 2026-08-20; theory lane to supply]`

`research/model_v4/HANDOFF_sign.md` does not exist on `origin/v4-theory` as of 2026-08-20
(checked: `git ls-tree -r origin/v4-theory` returns only the ticket file
`.scratch/v4-reposition/issues/05-t1-sign-handoff.md`). Per ADR-0007 that file is the
empirics lane's **only** dependency, and it supplies exactly one thing: the sign of the
change in the liquidity slope of the run-up after 2024-02-05.

The design is therefore written so that **the headline does not depend on it**:

- **H1 (§3.4) is sign-free.** It tests the partition itself — the flagged cell is
  liquidity-invariant, the pooled cell carries the whole liquidity derivative. It needs
  no post-2024 prediction and it is the paper's identity in one regression pair.
- **H2 (§3.5) needs the sign**, and is written with **both branches spelled out**
  (§3.5.2), so whichever sign lands, the prediction was falsifiable before the estimate
  existed.

If the handoff never lands, H2 is reported as a **two-sided descriptive** with both
branches quoted and no directional claim. That is a demotion, not a failure.

---

## 1. The objects being measured

| Symbol | Name (CONTEXT.md term) | Definition |
|---|---|---|
| TD | trigger date | The date of the event requiring the filing — the 5% crossing printed on the 13D cover page or in `<dateOfEvent>`. |
| FD | filing date | EDGAR `FILED AS OF DATE`. |
| FD* | effective filing date | FD if EDGAR acceptance was before the dissemination cut-off, else the next trading day. See §2.4. |
| **run-up** | timing split, pooled half | Abnormal return accumulated between the trigger and the day before the flag lands. |
| **jump** | timing split, flagged half | Abnormal return on the filing day itself. |
| LIQ | liquidity (κ) | −1 × standardised log Amihud illiquidity, so higher LIQ = more liquid = higher κ. **The sign convention is fixed here in writing** because BBJJ label their variable "Amihud Liquidity Measure" while Amihud (2002) is an *illiquidity* ratio, never state the orientation, never sign it, and never discuss the coefficient in the body; their card's verifier records it as unresolvable and instructs "do not cite R14's sign in either direction". Every table in this paper prints the orientation in the note. |
| Post | Feb-2024 acceleration | 1{TD ≥ 2024-02-05}. Assigned on the **trigger**, not the filing (§2.5). |
| D | bindingness dose | How binding the five-business-day deadline is for this filer, continuous in [0,1] (§4). |
| STK | stake at filing | Percent of class printed on the 13D (§5). |
| BID12 | control outcome | 1{a bid arrives within 365 days of TD} (§8.3). |

---

## 2. Sample construction (shared by every estimate)

### 2.1 The universe

All **initial** Schedule 13D filings (`SC 13D` and its post-2024Q3 EDGAR rename
`SCHEDULE 13D`; amendments excluded) with `date_filed` in 2022-01-01 → 2025-12-31,
enumerated from the sixteen quarterly EDGAR `form.idx` files already on disk
(2022Q1–2025Q4, ~770 MB, `empirics/data/`).

**Counts as they stand today** (computed 2026-08-20 from `empirics/data/fact2_parsed.jsonl`,
which was built with the **old** parser — these are floors, see §2.2).

**Two splits, and they are not the same.** §2.5 assigns Post on the **trigger** date. The
filed-date split is shown as well because it is how the file is organised and how earlier
documents (`research/empirical_feasibility.md` §1.3) reported it — **every estimate in this
spec uses the trigger-date split.**

*Split on filing date (reference only — not the design's split):*

| | Filed pre 2024-02-05 | Filed on/after | Total |
|---|---|---|---|
| Initial 13Ds parsed | 5,058 | 4,176 | 9,234 |
| …with a parsed trigger date | 3,403 | 1,235 | 4,638 |
| …with trigger date **and** CUSIP | 2,849 | 1,048 | 3,897 |
| …with a parsed percent-of-class | 4,487 | 1,702 | 6,189 |

*Split on trigger date — **the design's split** (§2.5). Only filings with a parsed trigger
date can be assigned at all, so the top row of the previous table has no counterpart here:*

| | **TD < 2024-02-05** | **TD ≥ 2024-02-05** | Total |
|---|---|---|---|
| …with a parsed trigger date | **3,586** | **1,052** | 4,638 |
| …with trigger date **and** CUSIP | **3,000** | **897** | **3,897** |

So the post share entering the power arithmetic is **w = 897/3,897 = 0.230**, not the
0.269 the filed-date split would imply. §3.6 uses 0.230.

| | Pre | Post | Total |
|---|---|---|---|
| Unique subject CIKs (filed-date split) | 1,617 | 1,430 | 2,735 (312 in both) |
| Unique filer CIKs | — | — | 3,503 |

**Trigger year** (not filing year): 1,550 / 1,616 / 1,199 / **0** in 2022 / 2023 / 2024 /
2025, plus **273 filings whose trigger date is dated 2014–2021** (215 of them 2021). The
2025 zero is the old parser's failure on the structured-XML era. Most of the 273 stale
triggers fail filter 2's 90-day band and drop out; the count is reported, not silently cut.
**183 filings straddle** (TD < 2024-02-05 ≤ FD) and are excluded from the main sample per
§2.5.

### 2.2 The re-fetch and re-parse (mandatory, flagged pull)

The committed `fact2_parsed.jsonl` **cannot be used as-is.** It was produced before
today's parser commits `b026872` (ticket 09) and `775162f` (ticket 09b), which fixed:

- the XML event-date tag (`<dateOfEvent>`; the old tag is absent from the SEC schema) —
  this is why 2025 parses at 0%;
- the XML `<percentOfClass>` path — percent-of-class is `None` for the whole XML era;
- the EDGAR form rename `SC 13D` ↔ `SCHEDULE 13D` — 2024Q3 and 2024Q4 lost 18 and 114
  filings silently, and an explicit caller tuple (`facts.py`) bypassed the alias map;
- a hard 12-character column slice that truncated `SCHEDULE 13D/A` into originals;
- percent-of-class regex defects (3-digit cap, first-match-not-max, CSS `line-height:120%`
  noise, `>100%` guard);
- event-date labels split across HTML tags;
- federal holidays in the business-day arithmetic.

**Therefore:** ticket 11 (E3) must, as its first step, re-fetch the filing texts for the
full 2022Q1–2025Q4 universe through `empirics.edgar_fetch` (the quarterly indexes are on
disk; only the ~9,400 filing texts need downloading, ~1 hour at the throttled ~4 req/s)
and re-parse with the fixed parser. **Every count in §2.1 is a floor.**

Expected after the re-parse, stated as a prediction so it can be checked, **on the
trigger-date split**: the pre leg is stable at **~3,000** (its triggers are all pre-2024
and already parse). The post leg currently holds **897** covering triggers from 2024-02-05
to roughly 2024-12, i.e. ~10.5 months at ~85 per month; the re-parse adds ~12.5 further
months, so the post leg should reach **~1,950**. That gives **N ≈ 4,950** and
**w ≈ 0.394**. Power in §3.6 and §8.6 is computed both ways: on today's counts
(N = 3,897, w = 0.230) and on this projection.

### 2.3 Filters, applied in this order (report the attrition funnel)

1. Form is an initial 13D (either spelling); amendments dropped.
2. Trigger date parses, and 0 ≤ (FD − TD) ≤ 90 calendar days. (Sanity band; the
   distribution's right tail is real — pre-window p90 was 23 business days — so the band
   is deliberately generous. Filings outside it are reported as a count, not silently cut.)
3. Subject CIK links to a CRSP PERMNO with `ShareType` in {common stock} and
   `USIncFlg` = US, and has ≥ 60 valid daily observations in [TD−126, TD−6].
4. One observation per (subject firm, trigger date). Where the same firm is triggered
   twice within 365 days, keep the first and flag the second.
5. **No delay screen.** Zeng keeps only 13Ds filed **1 to 13 calendar days** after the
   trigger, dropping both late filers and **same-day filers** (p. 1312 fn. 13). That
   screen is non-neutral under a five-business-day rule — it would mechanically retain a
   different slice of filers before and after 2024-02-05 — so we impose none, and report
   what a Zeng-style screen would have done to our sample as a robustness row. Delay is
   counted in **business days** with the federal-holiday calendar
   (`empirics/facts.py:business_delay`), never calendar days. Polk et al. counted their
   Delta in calendar days against a rule they themselves state in business days (p. 518),
   capped their sample at 12 calendar days when ten business days can span **14**, and
   their own showcase example (RC Ventures: trigger 24 Feb 2022, filed 7 Mar 2022 =
   11 calendar days but **7 business days**, three inside the limit) falls off the right
   edge of every one of their tables. We do not repeat that.

### 2.4 The EDGAR cut-off, and why FD* exists

Release 33-11253 moved the EDGAR filing cut-off from 5:30 pm to 10:00 pm ET on the same
date the window changed. A filing accepted at 6 pm was disseminated the **next** day
before the change and the **same** day after it. That shifts the flagged day by one for
part of the post sample and would show up as a spurious change in the timing split.

**FD\* = FD if `accepted` is before the era's cut-off, else the next trading day.**
`fact2_parsed.jsonl` already carries `accepted` and `accepted_after_4pm`; the re-parse
must carry them forward. Robustness: re-run with FD* ≡ FD; the two must agree, and if they
do not, the cut-off is doing the work and the result is reported as such.

### 2.5 Post assignment is on the trigger, not the filing

The deadline attaches to the crossing. A block crossed on 2024-01-30 and filed on
2024-02-08 was under the ten-calendar-day rule. So **Post = 1{TD ≥ 2024-02-05}**.

Filings that straddle (TD < 2024-02-05 ≤ FD) are **excluded from the main sample** and
reported separately as a count. Robustness: Post assigned on FD instead.

### 2.6 The pre window ends at adoption, not at the effective date

The amendments were proposed **2022-02-10** (Release 33-11030; 2022-03-10 is the *Federal
Register* publication date, 87 FR 13846) and adopted **2023-10-10** (SEC press release
2023-219). Anticipation between
adoption and effect is a live confound. **The main pre window is 2022-01-01 → 2023-10-09.**
The adoption-to-effect stub (2023-10-10 → 2024-02-04) is a separate, reported bin, never
pooled into "pre". Robustness: pre = full 2022-01-01 → 2024-02-04.

> **All three dates are now confirmed** (ticket-10 verifier, live fetch): proposal
> 2022-02-10 (Release 33-11030), adoption 2023-10-10 (press release 2023-219), effective
> 2024-02-05 (release DATES caption). The earlier "2022-03-10" carried in
> `research/positions/P4_feb2024_did.md` §5 is the *Federal Register* publication date, not
> the proposal date. **Nothing in the sample is cut on the proposal date** — the pre window
> is cut on the adoption date, which is confirmed.

---

## 3. (a) HEADLINE — the timing split

### 3.1 The two dependent variables

Abnormal returns from a market model estimated on [TD−252, TD−22] (minimum 120 valid
days), market return = CRSP value-weighted index rebuilt from `crsp_daily.csv`
(`DlyCap`-weighted `DlyRet`); Ken French daily factors as a robustness market model.

| | Name | Window (trading days) |
|---|---|---|
| RUNUP | run-up, pooled half | CAR[TD, FD*−1] |
| JUMP | filing-day jump, flagged half | CAR[FD*−1, FD*+1] |
| RUNUP5 | fixed-length run-up | CAR[TD, TD+4] |
| TOTAL | whole episode | CAR[TD−1, FD*+1] |
| PRE42 | anticipation control | CAR[TD−42, TD−6] |

**RUNUP5 exists because RUNUP's length changes mechanically at the reform, and because
the cross-section of window lengths is contaminated by selection.** Median delay fell
7.0 → 5.0 business days (`empirics/output/fact1_summary.csv`), so a post-2024 RUNUP
accumulates over fewer days for arithmetic reasons alone. Worse, comparing long-window to
short-window filings *within* a period does not identify a window effect: Polk et al. find
quiet-period CARs rising **1.34% → 5.09%** across Delta = 0 … 10 (Table 3, p. 526), but
their own Table 1 pooled daily CARs sum to only **3.80%** over the identical eleven days
(p. 523) — a ~1.3-point gap saying the gradient is substantially **composition**, i.e.
filers who wait are different filers. We therefore never read a window effect off the
cross-section of delays; only off the reform. Three defences, all pre-specified:

- **RUNUP5** is a fixed five-trading-day window from the trigger, inside the legal window
  in both regimes. **RUNUP5 is the primary run-up measure for H2** (the before/after
  comparison). RUNUP is primary for H1 (the within-regime partition test), where no
  before/after comparison is made.
- **Per-day run-up** = RUNUP / (FD* − TD in trading days), reported alongside.
- **Window length** (business days, holiday-adjusted) enters every H2 specification as a
  control, and the H2 result is re-run on the subsample with identical window length pre
  and post.

### 3.2 Liquidity

`ILLIQ_i` = mean over t ∈ [TD−126, TD−6] of |DlyRet| / (|DlyPrc| × DlyVol) × 10⁶,
requiring ≥ 60 valid days. `LIQ_i` = −1 × (log(ILLIQ_i) standardised within calendar
quarter). Quarter-standardisation removes the market-wide liquidity trend, which would
otherwise load on Post. Tercile version (`LIQ_LOW/MID/HIGH`) reported for the figures and
for the run-up path (§7).

### 3.3 Controls and fixed effects (identical across H1 and H2)

log(DlyCap) at TD−6 · PRE42 · filer-type dummy (activist HF / corporate / other, from
filer-name coding, §11 row 16) · window length in business days · 2-digit SIC fixed
effects · calendar-year-quarter fixed effects.

### 3.4 H1 — the partition test (sign-free, needs no handoff)

P2's theorem says: the **flagged** cell is liquidity-invariant; the **pooled** cell
carries the entire liquidity derivative. The empirical counterpart:

> **The run-up's liquidity slope is non-zero; the jump's liquidity slope is zero; and the
> two slopes differ.**

Estimated as one stacked regression so the difference has a standard error:

```
CAR_iw = α + β1·LIQ_i + β2·(LIQ_i × Flagged_w) + β3·Flagged_w + X_i'θ + δ_SIC2 + δ_YQ + ε_iw
```

where `w ∈ {runup, jump}` (two rows per filing), `Flagged_w = 1{w = jump}`. **β2 is the
partition coefficient.** β1 is the pooled cell's liquidity slope; β1 + β2 is the flagged
cell's.

**Standard errors:** two-way clustered on subject PERMNO and on calendar month of TD
(Cameron–Gelbach–Miller). The month dimension has only ~48 clusters over 2022–2025, which
is few; the primary table therefore also reports a **wild cluster bootstrap** on the month
dimension (Rademacher weights, 9,999 draws) and the paper quotes the more conservative of
the two. Firm-only clustering is a robustness row, never the headline.

### 3.5 H2 — the reform (needs the handoff sign)

```
CAR_i = α + δ·(LIQ_i × Post_i) + β·LIQ_i + γ·Post_i + X_i'θ + δ_SIC2 + δ_YQ + ε_i
```

run separately on RUNUP5 and on JUMP. δ is the change in the liquidity slope.

**Note on collinearity, fixed now:** in the **main sample**, `Post` is absorbed by the
calendar-year-quarter fixed effects — the anticipation window (2023-10-10 → 2024-02-04) is
excluded per §2.6, so every year-quarter left in the sample is entirely pre or entirely
post. **γ is therefore not identified in this specification and must not be reported from
it.** Only δ is. *(The exception is §2.6's robustness sample, where pre runs to 2024-02-04:
there 2024Q1 contains both regimes, so γ is weakly identified off that one quarter alone.
If it is reported at all, it is reported with that fact attached.)* Where a *level* shift
is the object (§5), the specification drops the year-quarter effects and substitutes a
linear time trend plus quarter-of-year dummies.

#### 3.5.1 What the pre-2024 level says (both branches agree)

P2's mechanism: less noise trading (low κ, illiquid) ⇒ order flow more revealing ⇒ more
of the price move happens **before** the flag. So the pre-period prediction is
**β < 0 on RUNUP** (more liquid ⇒ smaller run-up) and **β ≈ 0 on JUMP**. This is H1
restated, and it does not need the handoff.

#### 3.5.2 The post-2024 slope change — both branches, written now

`[PLACEHOLDER — sign from HANDOFF_sign.md, absent as of 2026-08-20; theory lane to supply]`

| | **Branch A — attenuation** (δ shrinks the pre-period slope toward zero) | **Branch B — amplification** (δ pushes it away from zero) |
|---|---|---|
| Mechanism | The shorter window moves mass from the pooled cell to the flagged cell; the flagged cell is κ-invariant, so the composite liquidity slope flattens. This is draft_v2's "disclosure attenuation" claim on the window margin. | The shorter window concentrates the same informed trading into fewer days, raising per-day order-flow intensity; the pooled cell becomes *more* revealing per unit of κ and the slope steepens. |
| Sign, given β < 0 on RUNUP5 | **δ > 0** and \|β + δ\| < \|β\| | **δ < 0** |
| Supportive if | δ̂ > 0, significant at 5% two-sided, and the implied post slope β̂ + δ̂ is closer to zero than β̂. | δ̂ < 0, significant at 5% two-sided. |
| Against if | δ̂ < 0 and significant, **or** δ̂ significant on JUMP as well and of the same sign and comparable size (which would refute the κ-invariance of the flagged cell, i.e. H1, and with it the partition itself). | δ̂ > 0 and significant, **or** the same JUMP contamination. |
| Uninformative if | \|δ̂\| < MDE (§3.6) — reported as a bounded null with the MDE quoted, never as "no effect". | same |

**One test refutes both branches at once:** if δ̂ on JUMP is significant and of the same
sign and comparable magnitude as δ̂ on RUNUP5, then the split is not a partition — the same
force is moving both cells, and the paper's identity claim fails. That check runs first
and is reported first.

**Note on the O-1 history.** ADR-0007 records that the window-margin attenuation claim is
**false at baseline in the repo (draft_v2) model** — the κ-sensitivity ratios run
1.06/1.18/1.14 for flagged mass below ≈0.29 (`research/review_v3/verify_theory.md`,
executed). Branch A is therefore *not* the default expectation. The two-round model is
being rebuilt precisely to settle which branch holds. This spec must not be read as
predicting Branch A.

### 3.6 Power and MDE — the arithmetic

Formula. For the interaction coefficient δ on `LIQ × Post` where LIQ is standardised
(sd = 1) and Post has share w, the residual variance of the interaction after partialling
out both main effects is `w(1−w)`, so

> `SE(δ̂) = σ_CAR / √( N · w(1−w) )` and `MDE = 2.802 · SE(δ̂)`
> (2.802 = z_{0.975} + z_{0.80}, i.e. 5% two-sided, 80% power).

Variance assumptions, to be replaced by realised SDs once the CARs exist:
**σ(JUMP) = 0.12**, **σ(RUNUP) = 0.15**. These are assumptions, not card facts — no card
prints a cross-sectional SD of a 13D window CAR. They are set at roughly four to five
times the mean effect sizes below, which is the usual ratio for short-window event CARs.

Reference magnitudes, so we can say whether a detected slope is economically meaningful
(each with its card and page):

| Source | Object | Magnitude |
|---|---|---|
| Zeng, RAS 2026, pp. 1309–1310 | 13D run-up, trigger → filing | **+2.8%**; **+1.9%** on FD and the next five days; +6.1% by FD+20. Median trigger-to-filing gap **9 calendar days** (p. 1309) |
| Zeng, same | **13G** run-up / jump — our placebo benchmark | **+0.9%** / **+0.4%** / +1.7% |
| Collin-Dufresne–Fos, JF 2015, p. 1563 | run-up (t−60, t−1) before **filing**; two-day filing jump | **~3%** and **~2.5%** (JF, 3,126 events, 1994–2010). NBER WP: **~7%** and **~3%** (1,725 events, 2001–2010) — **always tag the version** |
| Collin-Dufresne–Fos IA, Table IA.III, p. 10 | filing-date and (t−1,t+1) abnormal return, with t-stats | **1.12%** [5.79] and **0.80%** [7.77] |
| Polk et al., JFRC 2024, Table 1, p. 523 | daily CAR at the trigger date; day +1 | **0.90%**; **1.61%**. Days −10 … −1 are flat (≤0.12% in absolute value) — no pre-trigger run-up |
| Polk et al., pp. 520–521, Fig. 2 | abnormal volume at the trigger | **~5×** normal, decaying to normal by day +15 |

Polk et al. report **no standard errors, confidence intervals or regressions anywhere**
(mechanically re-grepped by that card's verifier), so their gradient is a level benchmark,
not an inference benchmark.

**All counts below are on the trigger-date split (§2.1), because §2.5 assigns Post on the
trigger.** Using the filed-date split here would overstate w and understate every MDE.

| Scenario | N | w | √(N·w(1−w)) | SE(JUMP) | MDE(JUMP) | SE(RUNUP) | MDE(RUNUP) |
|---|---|---|---|---|---|---|---|
| Today's counts (no re-parse): 3,000 pre / 897 post | 3,897 | **0.230** | 26.27 | 0.46 pp | **1.28 pp** | 0.57 pp | **1.60 pp** |
| After the re-parse (projected): 3,000 / 1,950 | 4,950 | **0.394** | 34.38 | 0.35 pp | **0.98 pp** | 0.44 pp | **1.22 pp** |

Clustering inflates these. Firm clustering with ~3.4 filings per subject firm and an
intra-firm correlation of 0.10 gives a design effect of 1.24 (×1.11 on the SE). Month
clustering with ~48 clusters averaging ~103 events and ρ = 0.02 gives 3.04 (×1.74).
Two-way, conservatively: **×1.1 to ×1.9**.

> **Honest reading, written before the estimate:** the design can detect a liquidity slope
> of roughly **1.1–2.3 percentage points per standard deviation of illiquidity** after the
> re-parse. The range is the clustering multiplier applied across the two series: the
> **lower end is JUMP** (MDE 0.98 pp × 1.1, the mildest multiplier) and the **upper end is
> RUNUP** (1.22 pp × 1.9, the harshest). On today's counts the same range is
> **1.4–3.0 pp** (JUMP 1.28 × 1.1 to RUNUP 1.60 × 1.9). Against
> Zeng's mean trigger-to-filing run-up of **2.8%**, that is between **40% and 80% of the
> level**. **Anything smaller than that is not detectable here and must be reported as a
> bounded null with the MDE quoted.** The design is not powered to find a small partition
> effect.

**A second power problem, specific to liquidity.** Brav–Jiang–Partnoy–Thomas find activist
targets are **not spread across the liquidity distribution**: 9.1% / 13.9% / **43.4%** /
18.3% / 15.3% across CRSP liquidity quintiles 1–5, i.e. they pile into the **third**
quintile (Table 3, WP printed p. 46). Our LIQ variation *within* the 13D sample is
therefore compressed relative to the CRSP universe, and the standardisation in §3.2 is
within-sample, so a "one standard deviation of illiquidity" is a smaller economic move
than the same phrase means in a cross-section of all firms. The realised within-sample
sd of log ILLIQ is reported next to every slope coefficient, and the effect is also
quoted per interquartile range.

### 3.7 Placebo and pre-trend for the timing split

- **Pseudo-trigger placebo.** Re-run H1 and H2 with TD replaced by TD − 63 trading days
  (one quarter before the real crossing) and windows of identical length. The pseudo
  liquidity slope must be statistically indistinguishable from zero. A significant
  pseudo-slope means LIQ is picking up a firm characteristic, not the trigger, and the
  headline is demoted to descriptive.
- **13G placebo.** Schedule 13G deadlines did not change until **2024-09-30** — compliance
  with the old 13G deadlines was required "through September 29, 2024" (Release 33-11253,
  p. 165), which is exactly why Trivedi uses 13G filers as his untreated comparison group
  (p. 10). Their run-up/jump split over 2022-01-01 → 2024-09-29 must show **no** break at
  2024-02-05. Benchmark levels from Zeng (pp. 1309–1310): 13G run-up **+0.9%** and filing
  jump **+0.4%**, against 13D's +2.8% and +1.9% — so the 13G series is small and should
  stay small.
  **Descriptive only**, for two reasons written down now: (i) 13G selection is plausibly
  rule-responsive (Trivedi card §7), so this placebo can fail without indicting H2;
  (ii) Trivedi's own use of this control group never defends its **comparability**, only
  its untreatedness, and his paper contains zero parallel-trend, pre-trend, placebo or
  anticipation tests (that card's verifier greps "parallel", "trend", "anticipat",
  "placebo" — **0 hits across 25 pages**). We do not inherit that weakness by promoting
  the 13G comparison to identification.
- **Pre-trend.** Quarterly LIQ-slope estimates for 2022Q1–2023Q3 (seven pre quarters,
  ending at adoption), joint F-test of a common slope. p < 0.10 blocks causal language.

---

## 4. (b1) The bindingness dose

**What it is** (CONTEXT.md): how binding the five-business-day rule is for a given filer.
CONTEXT defines it as a split; the ticket asks for it **continuous**. Both are specified;
the continuous one is primary.

**How large is the exposed population?** The Commission expects the amendments to produce
earlier filing for about **59 percent** of timely 13D reports (Release 33-11253, p. 193),
and only about **29 percent** of 2022's initial 13Ds were already inside the amended
deadline (p. 178). Our own Fact 1 has 35.7% inside five business days pre-rule
(`empirics/output/fact1_summary.csv`). So the dose is non-degenerate for roughly two
filers in three — this is not a design searching for a sliver.

**Construction — pre-period behaviour only, so it cannot be contaminated by the reform:**

> `D_j = share of filer j's initial 13Ds filed in 2022-01-01 → 2023-10-09 whose delay
> exceeded five business days` ∈ [0, 1].

Requires ≥ 2 pre-period filings by filer j. On today's (old-parser) counts, **2,004 of
~2,016 pre-period filer CIKs have ≥ 2 pre-period filings**, covering 5,046 of 5,058
pre-period filings — so the repeat-filer restriction costs almost nothing. **This count
must be recomputed after the re-parse before it is quoted anywhere**, because filer-CIK
extraction is a header regex that the re-parse re-runs.

For single-filing filers, the imputed dose is the leave-one-out mean of D over the filer's
stratum (filer type × size tercile × illiquidity tercile), estimated on pre-period data
only. Imputed-dose observations enter only the robustness row, never the primary.

**Alternative continuous dose, reported alongside:** `E_j = max(0, median pre-period delay
in business days − 5) / 5` — excess days over the new deadline, in units of the deadline.

**Binary split (CONTEXT's own definition):** `BIND_j = 1{median pre-period delay > 5
business days}`.

**Specification.** For any outcome y (RUNUP5, JUMP, STK, BID12):

```
y_i = α + φ·(D_j × Post_i) + ψ·D_j + γ·Post_i + X_i'θ + δ_SIC2 + δ_YQ + ε_i
```

φ is the dose-response. **The dose is a filer attribute, so standard errors cluster on
filer CIK as well** — three-way (subject firm, filer, month) with the wild bootstrap on
the month dimension.

**Supportive:** φ̂ significant and of the same sign as the H2 branch that the handoff
selects, with the magnitude ordered — high-dose filers move more than low-dose filers.
And the **first stage must hold**: the post-period delay of high-D filers must fall by
more than that of low-D filers. That first stage is mechanical (a filer who was already
fast cannot get faster), so it is a **validity check, not a finding**, and is labelled as
such. The only published estimate of the same first stage is Trivedi's DiD on the share
filed within five business days: **+0.348, SE 0.130, t = 2.69, p = 0.007** (Table 2,
p. 11), 148 treated 13Ds against 185 13G controls, ±180 days. Cite the **t = 2.69**, not
"t > 3" (AUTHOR_BRIEF, P4 amendment 1), note that his own *primary* pre-registered
outcome — mean calendar-day lag — is **null** (+1.89 days, SE 3.94, p = 0.63), and note
that his sampling frame is never stated anywhere in his 25 pages (that card's §5).

**Why a bunching-based dose is the right shape.** BBJJ's delay distribution is piled at
the old deadline: **45.3%** of filings land in the 8–10-business-day bucket and roughly
**20% file on day 10 itself** (Table 2 and Figure 1, pp. 10–11), with **193 filings —
over 10% — filed after the ten-day deadline**, rising to over 20% on a calendar-day count
(p. 13, fn. 21). A deadline that binds is visible as bunching, and the filers sitting on
the old deadline are exactly the high-dose ones.

**Against:** φ̂ significant with the opposite sign; or φ̂ ≈ 0 while the pooled H2 δ̂ is
large — that pattern says the reform is not working through bindingness and the mechanism
story fails even though the reduced form moves.

**Confound specific to the dose:** slow filers are not a random sample. They are plausibly
smaller, less institutionalised, and in less liquid names — exactly the LIQ dimension the
headline uses. So D and LIQ are correlated by construction. Mandatory diagnostic: report
corr(D, LIQ) and re-run the dose specification **within** liquidity tercile. If the dose
effect lives only in the illiquid tercile, that is reported as the finding, not hidden.

---

## 5. (b2) Stake at filing

**Variable.** `STK_i` = percent of class printed on the 13D (`pct_of_class`), the
empirical counterpart of the two-round model's stake-at-filing object (ADR-0007).

**Cleaning, pre-specified:** drop STK ≤ 0 or > 100 (the parser now guards > 100); report
the 0–5% tail as a count (62 of 300 in the Fact-1 sample were below 5%, i.e. genuine
group/SPV/cleanup filings plus residual parser noise) and **winsorise at the 1st and 99th
percentiles** for regression use. Report the raw distribution, the winsorised
distribution, and a bunching histogram in 0.25-point bins over [4, 8] to see whether mass
piles just above 5%.

**Benchmark distribution** (Bebchuk–Brav–Jackson–Jiang, 2,040 activist-HF 13Ds 1994–2007,
Table 4, p. 12 of the May-2013 draft): **median 6.3%, mean 8.8%, p75 8.8%, p90 14.6%,
p95 21.2%**. Our Fact-1 sample's median was 9.49% — higher, because our universe is all
13D filers, not activist hedge funds only. Both are reported side by side as a validation
check on the parser.

**Specification.** `STK_i = α + δ·(LIQ_i × Post_i) + β·LIQ_i + γ·Post_i + X_i'θ + ε_i`,
plus the dose version from §4.

**Fixed effects, deliberately different here.** γ — the level shift in the stake at filing
— *is* the object in this section, so calendar-year-quarter fixed effects (which absorb
Post) are **dropped** and replaced by a linear time trend in TD plus quarter-of-year
dummies. The interaction δ is additionally reported from the full year-quarter-FE
specification, where γ is not identified and is not reported.

**Prediction.** In the two-round model a shorter window means less time to accumulate
under cover before the flag, so the stake at filing should **fall** post-2024, and fall
more where cover was cheap (high κ). Sign of the interaction:
`[PLACEHOLDER — sign from HANDOFF_sign.md, absent as of 2026-08-20; theory lane to supply]`.

**A hazard that must be stated before the estimate, because it points the other way.**
BBJJ regress stake at filing on days-to-disclosure and get **−0.001\*** (Table A2, p. 37):
"even ten additional days to file (the maximum variation) is associated with just **0.6
percentage points less** ownership" (p. 37). Two things follow.

1. **The cross-sectional sign is negative** — filers who take longer end up with *smaller*
   stakes — which is the opposite of the naive accumulation story. It is almost certainly
   selection (the aggressive accumulators are the fast ones). So the cross-section of
   delays is **not** the prediction, and no part of this design reads the window effect off
   it. Only the reform does.
2. **The magnitude is a power warning.** 0.6 pp per ten days is **0.06 pp per day**. The
   reform cut the median delay by about two business days
   (`empirics/output/fact1_summary.csv`: 7.0 → 5.0), so the historical days–stake gradient
   implies a stake change of roughly **0.12 pp** — one quarter of this design's MDE
   (below). If the reform works only through mechanical accumulation time, **we cannot see
   it.** A detectable γ̂ would therefore have to come from a behavioural change (filers
   targeting a different stake), not from arithmetic — and the paper must say which it is
   claiming.

- **Supportive (Branch A, attenuation):** γ̂ < 0 (mean stake falls) and δ̂ ordered so the
  fall is larger in liquid names.
- **Supportive (Branch B):** γ̂ < 0 with δ̂ of the opposite sign — the fall concentrated in
  illiquid names, because there the window, not cover, was the binding constraint.
- **Against either:** γ̂ > 0 and significant. A *rise* in the stake at filing after the
  window shortened contradicts the accumulation channel in both branches, and would point
  instead at a composition change in who files (§8.5 item vi).
- **Uninformative:** |γ̂| below its MDE. Arithmetic: **the stake sample is bounded by the
  trigger-date sample, not by the 6,189 filings that carry a parsed stake** — §2.5 assigns
  Post on TD, so a filing with a stake but no trigger date cannot be assigned to a regime
  at all. The usable N is therefore the §2.2 projection, **N ≈ 4,950 with w ≈ 0.394**, so
  w(1−w) = 0.2388 and √(4,950 × 0.2388) = 34.38. With a winsorised sd of **8 percentage
  points** (BBJJ-scale; the realised winsorised sd replaces it), SE(γ̂) ≈ 8/34.38 = 0.233
  and **MDE(γ) ≈ 2.802 × 0.233 = 0.65 percentage points of stake.** Clustered on filer,
  ×1.3, **≈ 0.85 pp.** That is still the **best-powered estimate in the package**, and
  still about **seven times** the 0.12 pp the historical days–stake gradient predicts — so
  the conclusion above is unchanged, but the margin is thinner than a stake-count-based
  reading would suggest.

**Parser caveat that must travel with every stake number:** percent-of-class in the
committed file is old-parser output and is `None` for the entire XML era. Nothing in §5
may be quoted before the re-parse.

---

## 6. (b3) The bounded null

**What it is** (CONTEXT.md, ADR-0006): arithmetic on the SEC's own tables that **caps** the
aggregate effect of the rule on the bid hazard at about three percentage points. A
ceiling, not an estimate.

**The source.** SEC Release 33-11253, **Table 3, p. 189** — non-corporate-action initial
13Ds, 2011–2021, classified by how much of the reported stake was already accumulated by
the *amended* (five-business-day) deadline:

| Column | Stake accumulated by the amended deadline | Campaigns | % of campaigns | Campaigns/year |
|---|---|---|---|---|
| (1) | 100% — unconstrained | 1,907 | 80% | 173 |
| (2) | < 100% — some accumulation would have been cut | 463 | **20%** | **42** |
| (3) | < 90% — ≥ a tenth of the stake would have been cut | 78 | **3%** | **7** |
| (4) | < 75% — ≥ a quarter would have been cut | 16 | 1% | 1 |

Columns (3) and (4) are subsets of (2). Confirmed in the release's own prose, p. 188:
"about **97 percent** of the filers completed acquiring 90 percent of their reported stake
by the amended deadline, while the remaining **three percent** … continued to accumulate
shares constituting 10 percent or more of their reported stake after the amended
deadline"; restated pp. 234 and 238, and the campaigns/year row repeats at Table 6,
pp. 225–226 (sample 2,370 non-corporate-action filings, p. 224).

**The arithmetic.** Let `s` = the share of campaigns whose accumulation the rule actually
binds. For an unconstrained campaign the rule changes nothing about accumulation, by
construction. So even if **every** constrained campaign's bid outcome flipped:

> `|ATE on the 12-month bid hazard, accumulation channel| ≤ s`

**The bound is a ladder, and the paper reports all three rungs** rather than picking the
flattering one:

| Rung | `s` | Bound on the bid hazard | Reading |
|---|---|---|---|
| Any accumulation cut at all (col. 2) | 20% | **≤ 20 pp** | The loosest defensible ceiling |
| ≥ 10% of the stake cut (col. 3) | **3%** | **≤ 3 pp** | **The headline bound.** A campaign losing under a tenth of its stake plausibly proceeds unchanged |
| ≥ 25% of the stake cut (col. 4) | 1% | ≤ 1 pp | The tightest |

The 3 pp headline is a **judgement about what counts as a materially cut campaign**, not a
number the SEC computed for this purpose. That judgement is stated in the text, and the
20 pp rung is printed next to it so a referee can see the whole ladder.

**Three restrictions on how this bound may be stated** (AUTHOR_BRIEF, P4 amendment 3 —
these are corrections to the original P4 text and are binding):

1. The bound covers the **accumulation channel only**. It is **not** "the aggregate
   footprint of the rule".
2. The DiD estimate of §8 is **reduced-form** and mixes accumulation, incumbent defence
   (BBJJ's second channel) and selection into filing. Its true value may legitimately
   exceed 3 pp.
3. The **dollar** figures that travel with this bound are the release's own: **$49
   million/year** ($23m from Table 5 column 1 plus $26m from column 2, p. 211), or
   **$42m** / **$36m** under two adaptation assumptions (p. 211 n. 773) — and the
   Commission disclaims even those: the Table 5 wealth-transfer estimates "do not
   represent estimates of the benefit of the final rule amendments" (p. 211). The
   "**$810 million a year**" figure repeated three times in the author's own proposal
   **is not in the release** and must never appear (INDEX §4 item 9).

**Two release facts that bear on the design and belong in the same table.** About
**29 percent** of initial 13Ds filed in 2022 were already inside the amended
five-business-day deadline (p. 178), and the Commission expects the amendments to "result
in earlier filing for about **59 percent** of timely Schedule 13D reports" (p. 193). Our
own Fact 1 puts the pre-rule within-five-business-day share at **35.7%**, rising to
**75.6%** post (`empirics/output/fact1_summary.csv`) — a first stage that is in the same
place as the SEC's own arithmetic, on a different sample and a different window. That
agreement is reported as a validation of the parser, not as a finding.

**Why this matters more than it looks (§8.6 anticipated).** The matched DiD's MDE is
**4.4 pp at best** — larger than 3 pp. So the bound is not a consolation prize — it is arithmetically the
binding statement about the accumulation channel, because the design cannot separate a
true accumulation effect from zero even at the ceiling. **This must be the headline
sentence of the DiD leg, not a footnote.**

**Interpretive rule, fixed in advance:** if |β̂_DiD| exceeds the MDE *and* exceeds 3 pp,
the excess cannot be the accumulation channel and must be attributed to defence or
selection, with a diagnostic (§8.5) offered for which.

---

## 7. (b4) The run-up path

The daily abnormal-return path from TD to FD*, event-time day 0 = TD, plotted to day +10,
cut by liquidity tercile × Post, in the project's house style (`pyfig/style.py`, Paul Tol
palette). Ticket 15 (E7).

**Descriptive, not an estimate.** It exists to show three things a regression coefficient
hides: (i) whether the run-up begins **on** the trigger date — Zeng finds it begins
"precisely on the trigger date" (p. 1310), which is what makes the pooled cell measurably
real; (ii) whether the post-2024 path is the pre-2024 path truncated, or a differently
shaped path; (iii) whether the liquidity ordering is visible in levels or only in slopes.

**Shape benchmark** (Polk et al., Table 1, p. 523, 9,685 filings 2001–2022): daily CAR
**+0.90%** on the trigger date, **+1.61%** on day +1, then ≤0.31% per day; days −10 … −1
are flat. Abnormal volume peaks at **~5× normal** on the trigger day (pp. 520–521). Our
path should reproduce that shape or explain why not.

**Supportive:** the illiquid tercile's path rises above the liquid tercile's from day 0,
and the post-2024 paths separate less than the pre-2024 paths (Branch A) or more
(Branch B).
**Against:** no separation by liquidity in either period — that would say LIQ is not the
operative cut and the headline is measuring something else.
Confidence bands: pointwise 95%, bootstrapped by firm, 2,000 draws. No inference is drawn
from the figure; it illustrates the estimates in §3.

---

## 8. (c) The matched DiD on the twelve-month bid hazard

### 8.1 Treated sample

Initial 13Ds passing §2.3, one observation per (subject firm, trigger date), 2022-01-01 →
2025-12-31. Two nested samples, both reported:

- **S1 — all initial 13Ds** matched to CRSP, **trigger-date split** (§2.1): 3,000 pre /
  897 post today, ~3,000 / ~1,950 after the re-parse.
- **S2 — non-corporate-action campaigns**, roughly 20% of originals per SEC Table 2:
  ~600 pre / ~390 post (post-re-parse). S2 is the economically right sample (the rule's constrained tail
  lives there); S1 is the powered one. **S1 is primary for the reported estimate; S2 is
  primary for the interpretation.** Both MDEs are quoted in the same sentence.

Corporate-action filings (merger cleanups, SPV/group filings, post-restructuring stakes)
are coded from Item 4 purpose language plus filer-name patterns; the coding rule is
written down in ticket 13 before the pass starts, and 30 filings are hand-audited.

### 8.2 Control group and matching

**Never-13D controls**, not 13G filers. 13G filers disclaim control intent and the
13D-vs-13G choice is itself plausibly rule-responsive (Trivedi card §7), so a 13G control
group is contaminated by the treatment. The term is **never-13D**, not "never-targeted"
(AUTHOR_BRIEF, P4 amendment 5).

**Control universe:** CRSP common stocks (US, share type common) present in
`crsp_daily.csv` with no `SC 13D`/`SCHEDULE 13D` original **or amendment** naming them as
subject at any point 2021-01-01 → 2025-12-31. Pool size: 14,092 PERMNOs in the snapshot
minus ~2,735 13D subject firms, so on the order of 11,000 candidates — comfortably enough
for 3:1.

**Matching, 3:1 without replacement, nearest-neighbour on the Mahalanobis distance of:**

| Dimension | Rule |
|---|---|
| Size | log(DlyCap) at TD−6, caliper 0.25 pooled sd |
| Illiquidity | log(ILLIQ) over [TD−126, TD−6], caliper 0.25 pooled sd |
| Industry | 2-digit SIC, **exact** |
| Time | calendar quarter of TD, **exact** |

Each control inherits its treated firm's TD as a **pseudo-trigger date**, so treated and
control are measured over the identical calendar window. Match quality is reported as
standardised differences on all four dimensions plus three unmatched covariates
(book-to-market is unavailable, §11 row 22; substitutes: turnover, past 12-month return,
idiosyncratic volatility). Any standardised difference above 0.10 after matching is
reported and the match is re-run with a tighter caliper.

Firms matched to more than one treated firm across different quarters are allowed; the
match-group identifier clusters the standard errors.

### 8.3 Outcome coding

> `BID12 = 1` if, within **365 calendar days** of TD (or pseudo-TD), the firm is the
> subject of any of: `SC TO-T`, `SC TO-C`, `SC 14D9`, `DEFM14A`, `PREM14A`, or an `8-K`
> carrying Item 1.01 or Item 2.01 whose text names a merger or acquisition agreement for
> the firm itself.

Built in ticket 13 (E5) from the EDGAR submissions API and full-text search through the
existing throttled fetcher. Coding rules fixed before the pass:

- The clock starts at TD, not FD, so it is identical for treated and control.
- A firm already under an announced bid at TD is **excluded** from both groups.
- Withdrawn and completed bids both count as BID12 = 1; **entry** is the object, not
  completion (CONTEXT: control outcome = bidder entry, takeover premium, or campaign
  success — this is the bidder-entry leg).
- Bids by the 13D filer itself count, and are also reported separately.
- **Thirty-filing hand audit**, drawn stratified across treated/control and pre/post, done
  blind by an agent that did not write the coder. Disagreement above 10% blocks the leg.

**The one thing this coding cannot do:** it cannot see a bid that was contemplated and
abandoned before any filing. That is unobservable in EDGAR and is stated as a limitation,
not patched.

### 8.4 Specification

```
BID12_i = α + β·(Treat_i × Post_i) + γ·Treat_i + λ·Post_i + X_i'θ + δ_match + ε_i
```

`δ_match` = match-group fixed effects (so identification is within matched cell). Linear
probability model as primary (coefficients read directly as percentage points, and the
MDE arithmetic below is an LPM arithmetic); logit as robustness with average marginal
effects. Standard errors two-way clustered on match group and on calendar month of TD,
with a wild cluster bootstrap on the month dimension.

**Base rates.** Greenwood–Schor, Table 6, p. 372 (980 activist events, 1993Q3–2006Q3),
**within twelve months of the first 13D**:

| Group | Acquired within 12 months |
|---|---|
| Activist targets | **18.1%** |
| Industry–size–prior-return matched controls | **7.2%** |
| Non-activist 13D targets | 12.6% |
| All small CRSP stocks | 4.7% |

Their matched control is close to ours in construction, so 18.1% / 7.2% are the anchors
for the power arithmetic. Three caveats travel with them, all from that card:

- **Table 6 prints no standard error or test statistic anywhere.**
- 18.1% is **acquired within twelve months**, not a **bid hazard** (AUTHOR_BRIEF, P4
  amendment 2). Ours counts bids that fail; both our rates will be **higher**, which
  raises the variance and therefore the MDE. The arithmetic below is optimistic in that
  direction and is recomputed at the realised control rate before anything is quoted.
- The paper carries **three incompatible acquisition counts** — 26.1% at eighteen months
  (Table 2, p. 367, no denominator), 226 events = 23.1% (p. 368), 21.9% (Table 6) — and
  never reconciles them. We cite Table 6, and say so.

Greenwood–Schor's own gloss (p. 363): "activists increase the probability of takeover by
about **11 percentage points**". That is a **level** difference (our γ, the Treat main
effect), not the reform's effect (our β). Never conflate them.

### 8.5 Confound list

| # | Confound | Handling |
|---|---|---|
| i | **EDGAR cut-off** 5:30 pm → 10:00 pm ET, same date as the window change | FD* (§2.4); robustness with FD* ≡ FD |
| ii | **Anticipation** — proposed 2022-02-10 (Release 33-11030; 87 FR 13846 published 2022-03-10), adopted 2023-10-10 (press release 2023-219) | Pre window ends at adoption (§2.6); the stub is its own bin |
| iii | **T+1 settlement** 2024-05-28 | Dummy; main post window robustness-restricted to Feb–May 2024 |
| iv | **13G deadline changes** 2024-09-30 — shifts 13D/13G composition inside the post period | Re-estimate on Feb–Sep 2024 only; filer-type fixed effects |
| v | **Structured-data mandate 2024-12-18** — a measurement break, and the source of the old parser's 2025 failure | Treated as a second regime break: main sample ends 2024-12-17, 2025 reported as an extension with its own parse-rate table. **Date confirmed** in Release 33-11253 §II.G: "compliance with the structured data requirement for Schedules 13D and 13G will not be required until December 18, **2024**". The card's December 18, **2023** (pp. 164–165) is the *voluntary* date, from the same section — do not confuse them |
| vi | **Selection into 13D** — the marginal filer changes when the rule changes | Filer-mix diagnostics pre/post (fund type, stake size, target size, target illiquidity, Item 4 intent language). β is labelled reduced-form throughout. No instrument is used; index membership as an IV for 13G eligibility is **not** defensible here and is not attempted |
| vii | **Incumbent defence** (BBJJ, p. 28: faster disclosure also speeds up the defences) | Where rights-plan data can be built from EDGAR (8-K Item 3.03, 8-A12B), split on low-trigger pills. Where it cannot, **the bias is signed**: defences push the bid hazard down, so a measured *increase* is conservative and a measured *decrease* is confounded. Stated in the text, not hidden |
| viii | **Universal proxy** — mandatory for meetings after 2022-08-31, inside the pre window | Control dummy; robustness with pre = 2023-01-01 onward |
| ix | **M&A cycle / rates** | Calendar-quarter fixed effects absorb the common cycle; the matched control group absorbs the rest by construction. This is the main thing the control group buys |
| x | **Delisting** — acquired firms leave CRSP | `crsp_daily.csv` carries no delisting-return field (§11 row 25). BID12 is coded from filings, so the outcome survives; only post-TD covariates are affected, and none is used. Flagged, not fatal |

### 8.6 Power and minimum detectable effect — the arithmetic

Binary outcome. Treated rate `p_T = 0.181`, control rate `p_C = 0.072` (§8.4), so
`σ²_T = 0.181 × 0.819 = 0.1482` and `σ²_C = 0.072 × 0.928 = 0.0668`.

Four-cell DiD with `n_T` treated and `3n_T` controls per period:

> `SE(β̂) = √( (σ²_T + σ²_C/3) · (1/n_T,pre + 1/n_T,post) )`
> `MDE = 2.802 · SE(β̂)`, with 2.802 = z₀.₉₇₅ + z₀.₈₀ (5% two-sided, 80% power).

`σ²_T + σ²_C/3 = 0.1482 + 0.0223 = 0.1705`, so `√ = 0.4129`.

| Sample | n_pre | n_post | 1/n_pre + 1/n_post | SE | MDE | ×1.31 clustering | MDE as % of the 18.1% treated base |
|---|---|---|---|---|---|---|---|
| S1, today's counts | 3,000 | 897 | 0.001448 | 1.57 pp | 4.40 pp | **5.8 pp** | 32% |
| S1, after re-parse | 3,000 | 1,950 | 0.000846 | 1.20 pp | 3.37 pp | **4.4 pp** | 24% |
| S2 (≈20% subset) | 600 | 390 | 0.004231 | 2.69 pp | 7.53 pp | **9.9 pp** | 54% |

All counts are the **trigger-date** split (§2.1), matching §2.5's Post assignment.

The clustering multiplier 1.31 is `√(1 + (m̄−1)ρ)` with m̄ = 3.4 observations per subject
firm and ρ = 0.30 — a deliberately pessimistic within-firm correlation for a binary
outcome. Both the unclustered and clustered MDEs are reported. The 20% share behind S2 is
the SEC's own: non-corporate-action filings are **3,067 of 15,724, i.e. 20%**
(Release 33-11253, Table 2, p. 181).

> **Read this next to §6.** The headline bounded null caps the accumulation channel at
> **3 pp**. The best MDE this design can reach is **4.4 pp** (S1, after the re-parse), and
> the economically right sample S2 reaches only **9.9 pp**. **The design is arithmetically
> incapable of detecting the accumulation effect at its own headline ceiling.** That is not
> a reason to drop the leg — it is the leg's result. The December sentence is: *the
> footprint of the acceleration on the twelve-month bid hazard through the accumulation
> channel is bounded above at three percentage points by the SEC's own Table 3, and our
> matched design, which is powered to detect four and a half, finds [estimate] with a
> [CI] — the two statements agree, and neither supports a large effect.*
>
> The design **is** powered against the loose 20 pp rung of the ladder (§6): if β̂ came in
> near 20 pp we would see it comfortably. So the leg is not vacuous — it rules out the
> large-effect world and cannot rule out the small-effect one.

**The precedent for taking this seriously.** Dass et al. attempted the analogous
liquidity-and-premium difference-in-differences and abandoned it: their footnote 27
(printed p. 23) reports that the matched design leaves **19** treated acquirers for the
stock-payment test and that "the count is even smaller for the premium and CAR tests",
so their premium result falls back to cross-sectional OLS. That card's own lesson —
"compute the MDE before committing" — is why this section exists in the spec rather than
in the appendix of a finished paper.

**Consequence for the paper's framing, decided now:** the DiD leg is the **control-outcome
leg with a control group**, and its value is that the checklist is complete, not that the
number is large. The headline detection, if there is one, is the timing split (§3), which
is better powered.

### 8.7 Placebo — ≥ 500 pseudo-reform dates

Draw **every business day** in 2021-07-01 → 2023-10-09 inclusive as a candidate
pseudo-reform date. **Day-count convention, stated so the number is reproducible:** the
half-open `numpy.busday_count('2021-07-01', '2023-10-10')` is **593 raw weekdays**; passing
the repo's own federal-holiday table (`empirics.facts.FEDERAL_HOLIDAYS`) gives **568
holiday-adjusted business days**. Both clear the ≥ 500 requirement without sampling, and
the holiday-adjusted 568 is the set actually used, because the rule itself is written in
business days. The window ends at adoption so no pseudo-date is contaminated by
anticipation, and starts six months into the CRSP snapshot so every pseudo-date has a full
pre period.

For each pseudo-date d: re-run the entire pipeline — re-match, re-code Post as
1{TD ≥ d}, re-estimate β — on the sample restricted to TD < 2023-10-10, keeping the same
pre/post length ratio as the real design. Collect the 568 β̂(d).

**Decision rule, fixed now:** the real β̂ must lie **outside the [2.5th, 97.5th] percentile
band** of the placebo distribution. Additionally, the placebo distribution's own median
must be within 1 pp of zero — if it is not, the pipeline has a bias and the leg is blocked
until the bias is found. The placebo distribution is reported as a histogram with the real
estimate marked, in the paper, not the appendix.

Placebo dates within 30 business days of each other are highly dependent; the
p-value is therefore reported as a **randomisation p-value** (the share of |β̂(d)| ≥ |β̂|),
with the dependence acknowledged, not as an independent-draw p-value.

### 8.8 Pre-trends

Quarterly event-study on the treated-control gap in BID12, seven pre-quarters
2022Q1–2023Q3 (ending at adoption), normalised to 2023Q3:

```
BID12_it = α + Σ_{q≠2023Q3} π_q·(Treat_i × 1{quarter = q}) + γ·Treat_i + δ_q + δ_match + ε_it
```

**Decision rule:** joint F-test of `π_q = 0` for all pre-quarters. `p < 0.10` **blocks
causal language** — the estimate is then reported as a descriptive difference, the word
"effect" is not used, and the bounded null carries the leg alone. The individual π̂_q are
plotted with 95% bands whatever the test says.

### 8.9 Supportive / against — the DiD

- **Supportive of a real control-outcome effect:** |β̂| > MDE, sign matching the branch the
  handoff selects, pre-trend test passes, real estimate outside the placebo band, and the
  S2 point estimate has the same sign as S1's.
- **Against:** β̂ significant with the sign **opposite** to the selected branch, and the
  placebo/pre-trend checks pass (so it is not an artefact). That is a genuine refutation
  and is reported as one.
- **Bounded null (the expected case, given §8.6):** |β̂| < MDE. Reported as: the effect is
  bounded above at 3 pp by the SEC tables and at [CI upper bound] pp by this design; the
  data are consistent with zero and with anything up to the bound.
- **Design failure (leg demoted to descriptive):** pre-trend F-test p < 0.10, or hand-audit
  disagreement > 10%, or placebo median more than 1 pp from zero, or post-matching
  standardised differences above 0.10 that a tighter caliper does not fix.

---

## 9. (d) Bidder entry by liquidity

Same outcome coding, same sample, the liquidity cut instead of (and then interacted with)
the reform.

**Within 13D targets:**
```
BID12_i = α + δ·(LIQ_i × Post_i) + β·LIQ_i + γ·Post_i + X_i'θ + FE + ε_i
```

**Triple difference against the matched controls:**
```
BID12_i = α + τ·(Treat_i × Post_i × LIQ_i) + [all two-way interactions] + X_i'θ + δ_match + ε_i
```
τ is the object: does the reform's effect on bidder entry differ by liquidity?

**Power.** Adding a third (standardised, continuous) dimension roughly **doubles** the
standard error relative to §8.6 — a rule of thumb, not an identity, and it is recomputed
exactly once the realised LIQ variance is known. On that rule of thumb,
**MDE(τ) ≈ 8.8 pp on S1 after the re-parse and ≈ 19.8 pp on S2.** This leg is, on today's
arithmetic, **not powered to detect anything economically plausible**, and that is stated
in the text next to the estimate. It is included because it is the direct empirical
counterpart of the model's κ-derivative on the control outcome, and because reporting an
honest interval is better than not asking.

- **Supportive:** β̂ ≠ 0 with the sign of the pre-period prediction (§3.5.1 implies illiquid
  names, where the pooled cell is more revealing, should show the larger bidder-entry
  response), and τ̂ of the branch-selected sign.
- **Prior evidence, stated accurately.** There is **no** published estimate of liquidity on
  bidder entry after a 13D, which is why the object is ours. What exists is weaker than it
  is usually reported to be, and must be cited as such:
  - Brav–Jiang–Partnoy–Thomas's **−0.075 [t = −3.99]** is *not* a regression coefficient.
    It is the **matched-sample mean difference in the Amihud illiquidity ratio** between
    activist targets and industry×size×B/M matched firms (Table 3, WP printed p. 46) —
    targets are *more liquid* than matched peers. That card's verifier confirms AMIHUD
    appears in **no estimated equation anywhere in the paper** (absent from the Table 4
    probit and the Table 5 regression). Cite it as a descriptive difference or not at all.
  - Fos (2017) shows liquidity predicts activism *entry* (proxy contests), never bidder
    entry or premium.
  - Trivedi's post-reform **Amihud** outcome is an **uninformative** null: **+0.41,
    SE 0.81, p = 0.62** (Table 2, p. 11), reported with no MDE and no confidence interval,
    and added after the pre-registration was locked (Appendix G.2, p. 25). It does not
    establish that the reform leaves liquidity unmoved — it establishes that his design
    could not tell. Cite it as an absence of evidence, never as evidence of absence.
- **Against:** β̂ significant with the opposite sign — that would say liquidity works on
  bidder entry in the direction opposite to the model's pooled-cell mechanism.
- **Uninformative (most likely):** |τ̂| < 9 pp. Reported as an interval with the MDE quoted
  in the same sentence.

---

## 10. (e) Decision table — what counts as supportive, what counts as against

Written 2026-08-20, before any estimate exists. Every row is falsifiable.

| # | Estimate | Supportive | Against | Uninformative (bounded null) |
|---|---|---|---|---|
| 1 | **H1 partition** β2 on `LIQ × Flagged` (§3.4) | β̂2 significant, and β̂1 (pooled slope) significantly ≠ 0 while β̂1 + β̂2 (flagged slope) is inside ±MDE | β̂1 ≈ 0 and β̂1 + β̂2 ≠ 0 — the *flagged* cell carries the liquidity derivative, which inverts the theorem | \|β̂2\| < MDE(1.1–2.3 pp): the two cells cannot be told apart; the partition is not visible in prices |
| 2 | **H2 slope change** δ on RUNUP5 (§3.5) | δ̂ of the handoff-selected sign, significant, JUMP unaffected | δ̂ of the opposite sign, significant; **or** δ̂ equally large on JUMP (refutes the partition itself) | \|δ̂\| < MDE; quote the MDE |
| 3 | **Bindingness dose** φ (§4) | φ̂ same sign as δ̂, magnitude ordered in D, survives within-liquidity-tercile | φ̂ opposite sign; **or** φ̂ ≈ 0 while δ̂ large (mechanism fails though reduced form moves) | \|φ̂\| < MDE |
| 4 | **Stake at filing** γ, δ (§5) | γ̂ < 0 (stake falls post-2024), δ̂ of the branch-selected sign | γ̂ > 0 significant — a *rise* contradicts the accumulation channel under both branches | \|γ̂\| < 0.85 pp of stake (0.65 pp before clustering). Note the historical days–stake gradient predicts only ~0.12 pp |
| 5 | **Bounded null** (§6) | Not an estimate. Supportive of the paper's *claim* if the DiD estimate's CI is consistent with ≤ 3 pp | The bound is arithmetic; it cannot fail. It can only be *mis-stated* — see the three restrictions and the three-rung ladder in §6 | n/a |
| 6 | **Run-up path** (§7) | Liquidity terciles separate from day 0; post-2024 paths separate less (A) or more (B) | No separation by liquidity in either period | n/a — descriptive |
| 7 | **Matched DiD** β (§8) | \|β̂\| > MDE, branch-selected sign, pre-trends pass, outside placebo band, S1 and S2 agree in sign | β̂ significant with the opposite sign, checks passing | \|β̂\| < MDE (5.8 pp today, 4.4 pp after re-parse); report against the 3 pp headline bound and the 20 pp loose rung |
| 8 | **Bidder entry by liquidity** β, τ (§9) | β̂ of the pre-period predicted sign; τ̂ branch-selected | β̂ significant with the opposite sign | \|τ̂\| < ~8.8 pp (S1) / ~19.8 pp (S2) — the expected outcome |

**One sentence that decides the paper's identity claim** (row 1 + row 2's "against"
column): *if the filing-day jump moves with liquidity the same way the run-up does, there
is no partition to write about.* That check runs first in ticket 11 and its answer is
reported first.

---

## 11. (f) Data manifest

Every variable named anywhere in §3–§9. Exactly one status each:
**[DISK]** = on disk now, file and column named · **[PULL]** = a flagged pull, source and
request named · **[NONE]** = not obtainable, replacement or consequence named.

`empirics/data/` is a **symlink** to `/Users/austinli/Projects/blockholder/empirics/data`
(the pre-v4 checkout) and is gitignored. It does not survive a machine change. Backing it
up off-repo is an open item (§13).

| # | Variable | Status | File / column, or source and request |
|---|---|---|---|
| 1 | Filing list (form, company, CIK, date filed, EDGAR path) | **[DISK]** | `empirics/data/form_2022_QTR1.idx` … `form_2025_QTR4.idx` (16 files, all quarters present); parsed by `empirics.edgar_fetch.list_filings` |
| 2 | Filing texts (the ~9,400 master `.txt` submissions) | **[PULL]** | EDGAR, via `empirics.edgar_fetch.fetch_filing_text`, ~4 req/s, ~1 h. **Not cached on disk** (ticket 09 comment). Required by rows 3, 4, 8, 9, 10 |
| 3 | TD — trigger date | **[PULL]** | Re-parse of row 2 with the **fixed** `empirics/parse_13d.py` (`<dateOfEvent>` XML path + detagged cover-page label). Old values in `fact2_parsed.jsonl:event` are 0% for 2025 and must not be used |
| 4 | FD — filing date | **[DISK]** | `fact2_parsed.jsonl:date_filed` / `:filed`; also row 1's `Date Filed`. Unaffected by the parser bugs |
| 5 | FD* — effective filing date | derived | From row 4 + row 6 + the era's cut-off (5:30 pm → 10:00 pm ET, 2024-02-05) |
| 6 | EDGAR acceptance timestamp | **[DISK]** | `fact2_parsed.jsonl:accepted`, `:accepted_after_4pm`. Re-parse must carry both forward |
| 7 | Form type; original vs amendment | **[DISK]** | Row 1 + `fact2_parsed.jsonl:form`. Alias map (`SC 13D` ↔ `SCHEDULE 13D`) lives in `list_filings` after commit 775162f |
| 8 | Subject CIK, filer CIK | **[DISK]**, re-derive | `fact2_parsed.jsonl:subject_cik`, `:filer_cik`. Header regex, unchanged by the fixes, but re-derived in the re-parse for consistency |
| 9 | Subject name, filer name | **[DISK]** | `fact2_parsed.jsonl:subject_name`, `:filer_name` |
| 10 | STK — percent of class | **[PULL]** | Re-parse (row 2). XML `<percentOfClass>` path added in 775162f. `fact2_parsed.jsonl:pct_of_class` is `None` for the whole XML era and carries the 3-digit / first-match / CSS bugs before it |
| 11 | CUSIP for the subject firm | **[DISK]** values, **[PULL]** code | `fact2_parsed.jsonl:cusip`, present for 7,970 of 9,234 (86%; 7,948 nine-char, 22 eight-char). **The CIK→CUSIP linking code is not in the repo.** The values can be reused; the link must be rebuilt and committed before the section is defensible (feasibility §5.7). Free rebuild route: EDGAR company-submissions API + CRSP `HdrCUSIP` |
| 12 | Daily price, return, volume, market cap | **[DISK]** | `empirics/data/crsp_daily.csv` — `DlyPrc`, `DlyRet`, `DlyVol`, `DlyCap`; 11,884,715 rows, 2021-01-04 → 2025-12-31, 14,092 PERMNOs |
| 13 | PERMNO, PERMCO, CUSIP, HdrCUSIP, Ticker, exchange, share type, US flag | **[DISK]** | `crsp_daily.csv` — `PERMNO`, `PERMCO`, `CUSIP`, `HdrCUSIP`, `Ticker`, `PrimaryExch`, `ShareType`, `SecurityType`, `USIncFlg` |
| 14 | ILLIQ / LIQ — Amihud illiquidity | derived | From row 12: mean \|DlyRet\|/(\|DlyPrc\|×DlyVol)×10⁶ over [TD−126, TD−6] |
| 15 | log market cap | derived | `crsp_daily.csv:DlyCap` at TD−6 |
| 16 | Market-model abnormal return; CARs | derived | Value-weighted index rebuilt from `DlyCap`×`DlyRet` in row 12. **Cross-check available on disk:** `wrds_evtstudy_edate.csv` (2,285 events, 21-day window / 220 estimation days) and `wrds_evtstudy.csv` (49,116 event×day rows). The harness that produced them is **not committed** — treat them as a validation target, not the source |
| 17 | Ken French daily factors (robustness market model) | **[PULL]** | Ken French data library, free, direct download. Not yet in the repo |
| 18 | 2-digit SIC (industry, for exact matching) | **[PULL]** | **Not a column in `crsp_daily.csv`.** Free route: EDGAR company-submissions API (`data.sec.gov/submissions/CIK##########.json`) returns `sic` per CIK, stdlib-fetchable with the existing throttled fetcher. Gated alternative: CRSP header / Compustat. If the free route fails for a firm, matching falls back to 1-digit SIC for that firm and the count is reported |
| 19 | Filer type (activist HF / corporate / other) | **[PULL]**, hand-coded | Filer-name regex over row 9 plus a hand check of the top ~200 filers by count. Activist Insight would do it properly and is gated (out of scope, ADR/spec) |
| 20 | Business-day delay; federal holidays | **[DISK]** in code | `empirics/facts.py:business_delay` with the 2021–2026 US federal-holiday table passed to `np.busday_count` (commit b026872) |
| 21 | D / E / BIND — bindingness dose | derived | From rows 3, 4, 8, 20, pre-period only |
| 22 | BID12 — bid within 12 months | **[PULL]** | EDGAR submissions API + full-text search for `SC TO-T`, `SC TO-C`, `SC 14D9`, `DEFM14A`, `PREM14A`, `8-K` Items 1.01/2.01. Ticket 13 (E5). Estimated 1–3 weeks including validation (feasibility §2.3). **This is the long pole of the whole package** |
| 23 | Never-13D control universe | derived, needs row 11 | `crsp_daily.csv` PERMNOs minus 13D subject firms. Requires the CIK→PERMNO link (row 11) to be rebuilt first, or the control group is contaminated by unmatched 13D targets |
| 24 | Match covariates (size, illiquidity, SIC2, quarter) | rows 14, 15, 18 | — |
| 25 | Match-quality extras (turnover, past 12-m return, idio vol) | derived | From row 12 |
| 26 | SEC constrained-share `s` for the bounded null; the 20% non-corporate-action share; the 29%/59% exposure figures; the $49m/$42m/$36m foregone-value figures | **[DISK]** | `research/txt_extracts/sec_release_33_11253.pdf` / `.txt`, via `research/cards/_institutional_sec_33_11253.md`. Cites: Table 3 p. 189 and prose p. 188 (the ladder); Table 6 pp. 225–226 and p. 224 (the 2,370 sample); Table 2 p. 181 (20%); pp. 178, 193 (29%, 59%); Table 5 p. 210 and p. 211 + n. 773 (dollars). All were read and verified against the release in ticket 01; **ticket 11 re-confirms Table 3 p. 189 in the text file before the bound enters the draft** |
| 27 | Takeover premium (offer price ÷ unaffected price − 1) | **[NONE]** | SDC / Bloomberg — gated, and the one variable with no complete free substitute (feasibility §3). **Replaced by:** BID12 (bidder entry) as the control outcome for December; a hand-collected offer-price subsample (≤ 300 deals, EDGAR SC TO-T / DEFM14A / 8-K, unaffected price from `crsp_daily.csv`) is **specified only**, per ADR-0006 and the spec's Out of Scope. **What dies without it:** the premium magnitude. The paper's control-outcome claim is entry, not premium, and says so |
| 28 | Poison pills / low-trigger rights plans (BBJJ defence channel) | **[NONE]** at scale | SharkRepellent / FactSet — gated. **Best-effort substitute [PULL]:** 8-K Item 3.03 and 8-A12B rights-plan filings via EDGAR full-text search, coverage unknown until tried. **If it fails:** the defence channel is *signed* not estimated (§8.5 row vii) — defences push the hazard down, so a measured increase is conservative |
| 29 | Book-to-market; governance indices | **[NONE]** free | Compustat / ISS — gated, and WRDS standing access is **unconfirmed** (feasibility §5.6: it worked once on 2026-06-11). **Replaced by:** log market cap (row 15) + 2-digit SIC (row 18) + the row-25 extras. **What dies:** a value-vs-growth control in the matching. Consequence is a robustness row, not a headline |
| 30 | Delisting returns | **[NONE]** in the snapshot | `crsp_daily.csv` has no `DLRET`/`DLSTCD` column. **Consequence:** post-TD covariates for acquired firms are truncated. BID12 is coded from filings so the **outcome is unaffected**; no post-TD covariate is used in any specification, by design. A WRDS delisting-file pull would close it and is not required |
| 31 | Cross-country threshold notices, non-US premia | **[NONE]** / out of scope | UK RNS, BaFin, AMF, Consob, CNMV, AFM, FINMA, SEDAR+, ASIC, EDINET — free but each a bespoke scrape; non-US premia gated. Explicitly out of scope (spec.md Out of Scope). **What dies:** nothing in this document |
| 32 | Trivedi's pre-registration; competitor replication files | **[NONE]** | No repository, DOI or registry exists for either SHA-256 hash (INDEX §2). Nothing here depends on it |

**No variable named in §3–§9 is left unmapped.** Rows 2, 3, 10, 17, 18, 19, 22, 28 are the
flagged pulls; rows 27, 29, 30, 31, 32 are the not-obtainables; everything else is on disk
or derived from something on disk.

---

## 12. (g) Referee checklist

The fixed list from CONTEXT.md, each item answered with the section that answers it.

| Item | Answer | Where |
|---|---|---|
| **Control group or bounded null** | Both. The DiD has a never-13D control group matched 3:1 (§8.2). The timing split has no control group by design — a 13G control is contaminated by rule-responsive selection — and carries the pseudo-trigger placebo and the 13G *descriptive* placebo instead (§3.7). The bounded null is computed from the SEC's own tables and is arithmetically the binding statement about the accumulation channel (§6, §8.6) | §3.7, §6, §8.2, §8.6 |
| **Confound list** | Ten named confounds with a stated handling each, including the three the cards specifically warn about: the EDGAR cut-off moving on the same date as the window (i), Zeng's non-neutral calendar-day screen (§2.3 filter 5), and BBJJ's defence channel (vii) | §8.5, §2.3, §2.4, §2.6 |
| **Power / MDE** | Computed from counts on disk plus stated variance assumptions, arithmetic shown in full, both on today's counts and on the post-re-parse projection. Timing split: **1.1–2.3 pp** per sd of illiquidity. Stake: **0.85 pp**. DiD: **4.4 pp** (S1) / **9.9 pp** (S2). Triple difference: **~8.8 / ~19.8 pp**. **The DiD's MDE exceeds the 3 pp headline bound, and the spec says so before the estimate exists** | §3.6, §5, §8.6, §9 |
| **Placebos** | 568 holiday-adjusted pseudo-reform business days (593 raw weekdays) (2021-07-01 → 2023-10-09, every one, no sampling), randomisation p-value, decision rule fixed in advance; plus the pseudo-trigger placebo at TD−63 and the 13G descriptive placebo | §8.7, §3.7 |
| **Pre-trends** | Seven pre-quarters to 2023Q3, joint F-test, and an explicit blocking rule: p < 0.10 removes causal language from the leg | §8.8, §3.7 |
| **Parser validation** | Eleven fail-old/pass-new assert checks in `empirics/test_parse_13d.py`, run as `.venv/bin/python -m empirics.test_parse_13d` (11/11 passing at commit 775162f). Hand audits: ticket 09 builder 12 filings + verifier 3 filings independently sampled, all matching; ticket 09b caught four further defects plus a fifth stacked one, with one retry-with-evidence round and a fresh re-verify that found nothing new. **Two gaps stated, not papered over:** (i) the committed `fact1_filings.csv` is entirely pre-XML (max `date_filed` 2024-12-16), so the XML event-date path is validated against live EDGAR fetches rather than against committed pipeline output; (ii) the full-universe re-parse has not been run, so every count in this document is an old-parser floor. Ticket 11 pays for the re-fetch once and re-runs per-quarter parse rates as a table | §2.2, `empirics/test_parse_13d.py`, `.scratch/v4-reposition/issues/09-e1-parser-fixes.md` |

**Two additions this design imposes on itself beyond the checklist:**

- **Reproducibility.** The Fact-2 execution code (CIK→CUSIP link, event-study harness,
  regressions) is not in the repo (feasibility §5.7). Every estimate in this document ships
  as a committed script that runs from the manifest in §11. An estimate whose script is not
  committed does not enter draft_v3.
- **Attrition funnel.** Every table reports the funnel from §2.3: filings enumerated →
  originals → trigger date parsed → CRSP-matched → in the estimation sample, with
  per-quarter parse rates. The 2025 parse rate is the number a referee will check first.

---

## 13. Open items — not resolved by assumption

Blocking = a downstream ticket cannot proceed correctly until it is closed.

| # | Open item | Who closes it | Blocking? |
|---|---|---|---|
| 1 | **`research/model_v4/HANDOFF_sign.md` does not exist** — confirmed absent from `origin/v4-theory`, 2026-08-20. Every directional prediction in §3.5.2, §5, §9 carries the placeholder and both branches | theory lane | No — H1 is sign-free |
| 2 | **The full re-fetch and re-parse has not been run.** Every count here is an old-parser floor; the §2.2 projections are predictions; §3.6 and §8.6 must be recomputed on realised counts | ticket 11 | **Yes** |
| 3 | **CIK→CUSIP link code is not in the repo.** The 7,970 values on disk are reusable but not reproducible or extensible, and the never-13D control universe (§11 row 23) depends on it | ticket 11/13 | **Yes** for the DiD |
| 4 | **`empirics/data/` is a gitignored symlink to the pre-v4 checkout.** The 1.2 GB CRSP snapshot does not survive a machine change and is not backed up off-repo | author | **Operational risk #1** |
| 5 | **WRDS standing access unconfirmed** (worked once, 2026-06-11). Nothing here needs a new pull — but if item 4 bites, the free fallbacks carry survivorship bias that is fatal for a takeover sample | author | No, unless 4 bites |
| 6 | **Which rung of the §6 ladder is "the" bound (20 / 3 / 1 pp) is a judgement**, not something the release settles. All three are printed here and must be in the draft. Also read from the card, not from a first-hand read of the release in this ticket | ticket 11 | No |
| 7 | **The base rates are borrowed and mismatched.** GS's 18.1% / 7.2% are *acquired*, 1993–2006, with no SEs in Table 6 and three inconsistent counts in the paper. Our *bid* rates are higher, so the true MDE exceeds §8.6's | ticket 14 | No — recompute |
| 8 | **The repeat-filer count behind the dose** (2,004 of ~2,016) is old-parser output and looks high. If it does not survive the re-parse, the dose falls back to stratum imputation | ticket 11 | No |
| 9 | **Rights-plan coverage from EDGAR is untested** (§11 row 28). Until tried, the BBJJ defence channel is signed, not estimated | ticket 13 | No |
| 10 | **Zeng's IA Table IA.2 (firm-size split) is not in hand** — flagged decision-critical in `research/cards/INDEX.md` §3, and the nearest occupied cut to our liquidity split | author (Springer IA) | No, but a referee will raise it |
| 11 | **Dass et al.'s premium numbers need the published JCF (2024) version** before any of them enters a draft (INDEX §2). The premium leg is out of scope, so nothing here depends on it | author | No |
| 12 | **Few-cluster inference on the month dimension** (~48 clusters). Wild bootstrap is the standard fix, not a guarantee; if it disagrees with the analytic SEs, the more conservative is reported and the disagreement stated | ticket 11/14 | No |
| 13 | ~~Proposal / adoption dates second-hand~~ — **CLOSED** by the ticket-10 verifier: proposal **2022-02-10** (Release 33-11030; 2022-03-10 was the *Federal Register* date carried by P4), adoption **2023-10-10** (press release 2023-219), effective **2024-02-05**. Nothing is cut on the proposal date | closed | No |
| 14 | ~~Structured-data mandate date unverified~~ — **CLOSED** by the ticket-10 verifier: Release 33-11253 §II.G says compliance "will not be required until December 18, **2024**". The card's December 18, **2023** is the *voluntary* date from the same section. §2.2's sample end and §8.5 row v stand | closed | No |
| 15 | **σ(JUMP) = 0.12, σ(RUNUP) = 0.15 are assumptions**, not card facts; no card prints a 13D window-CAR standard deviation. Every §3.6 MDE scales linearly in them | ticket 11 | No — recompute |
| 16 | **The triple-difference MDE uses a "SE roughly doubles" rule of thumb** (§9), pending the realised within-sample variance of LIQ | ticket 14 | No |
| 17 | **BBJJ's cross-sectional days→stake sign runs against the accumulation story** (−0.001\*, Table A2 p. 37). Read as selection — but if §5's reform estimate comes back with the same orientation, the two are not independent evidence and the paper must say so | ticket 12 | No |

---

*Nothing in this document is an estimate. The first estimate is ticket 11.*
