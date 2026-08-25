# HANDOFF — the window-margin sign

**Status: TWO ENTRIES, BOTH LIVE.** §1–§6 are the **repo-model** entry (`draft_v2`, the
`numerical/` package), fixed cutoffs, partial equilibrium — status **PROVISIONAL**, retained
in full and not overwritten. §8 is the **two-round model** entry (`numerical_v4`), added
2026-08-21, status **VERIFIED** (independent re-run of all source scripts 2026-08-22:
ALL REPRODUCE, bit-identical up to timing fields — `quality_reports/fixes/t2_rerun_verify_note.md`).
**The two entries carry opposite signs, and §8.1 says why both are honest.**
**Date: 2026-08-22.** Tickets 05 (T1) and 30.

This is the empirics lane's only dependency on the theory lane. The empirics lane **may
consume the numbers below now**, taking the repo-model entry and the two-round entry as
answers to two different experiments — see §8.1 before quoting either as "the" sign.

Notation follows `research/model_v4/MODEL_CARD.md` §4.4: **κ** is noise-trading intensity
(liquidity), **Ω** is the unconditional flagged weight `Pr(D=1)` (this is `draft_v2`'s
`ω_P`), and **ω_a** is the disclosed share of engagements `Pr(D=1 | a=1)`, the calibration
target. Every number in this file is Ω-type. None of them is ω_a.

---

## 1. The answer in one line

**Flagging the public buy makes the takeover premium MORE sensitive to liquidity, not
less — but only barely.** Window-margin attenuation is **false** at the paper's own
calibration. In the empirics spec's language (`research/empirics_v4/SPEC.md` §3.5.2), the
repo model points at **Branch B (amplification), δ < 0** — with a magnitude so small that
a bounded null is the realistic outcome.

| | |
|---|---|
| **Sign** | **Positive** on the sensitivity: moving the public buy from the pooled cell to the flagged cell *raises* \|∂κ Δ^act\|. Equivalently **δ < 0** on `LIQ × Post`, given `β < 0` on RUNUP5. **Branch B.** |
| **Magnitude** | Ratio of κ-sensitivities (disclosed ÷ pooled), total variation over κ ∈ [0.15, 0.85]: **1.064** at the baseline Ω = 0.0373; **1.184** at Ω = 0.129; **1.136** at Ω = 0.286. Sign flips to **0.378** at Ω = 0.50. At the baseline the two curves are all but on top of each other — ranges 0.01107 vs 0.01117, a **0.9%** gap, at most **2.5%** apart at any κ. |
| **Condition** | Holds for **Ω < 0.343** (the crossing, located by bisection this run — see §3). Fixed cutoffs (partial equilibrium): the blockholder's `(k₁, k₀)` are pinned at the baseline equilibrium and only `k_D` moves. No general-equilibrium cutoff-shift term is signed. |
| **Model version** | Current repo model, `numerical/` package as of `v4-theory` 2026-08-21 (the static `draft_v2` model). Not the two-round model. |
| **Evidence** | `quality_reports/fixes/t1_o1_rerun_check.py` → `t1_o1_rerun_check.json`. Six checks, all pass. Run: `.venv/bin/python quality_reports/fixes/t1_o1_rerun_check.py` |

## 2. What the experiment actually is

The referee's **O-1**. Hold the blockholder's cutoffs fixed at the baseline equilibrium
(`k₁ = k₀ = 0.821738`, `k_D = 2.261127`; the Hold region collapses at baseline). Sweep κ
over a 41-point uniform grid on [0.15, 0.85]. At each κ compute the expected
activism-related premium `Δ^act` twice:

- **flagged** — the market sees the order flow *and* the disclosure flag `(X, D)`;
- **pooled** — the market sees the order flow `X` only, so the public buy hides among the
  other `D = 0` states.

Measure κ-sensitivity as the total variation of `Δ^act` across the grid (mean \|slope\| is
the same number up to the grid constant, so the ratios are identical), and take the ratio
flagged ÷ pooled. Repeat at four values of `k_D`, i.e. four values of Ω. **A ratio above 1
means the flag makes premia *more* liquidity-sensitive — attenuation fails.**

## 3. The numbers, and how they compare with the committed claim

The committed claim lives in
`quality_reports/reports/2026-08-19_framework_v3_referee_report.md` (lines 114–124), and
was independently re-executed by the v3 verifier in
`research/review_v3/verify_theory.md` (row O-1, lines 32 and 42–53). The decision built on
it is `docs/adr/0007-one-theorem-two-round-model-two-lanes.md`.

| `k_D` | Ω | TV flagged | TV pooled | **ratio** | committed ratio | diff |
|---|---|---|---|---|---|---|
| 2.261127 | 0.037252 | 0.017594 | 0.016537 | **1.06397** | 1.0640 | 2.8e-05 |
| 1.800 | 0.128950 | 0.015981 | 0.013500 | **1.18373** | 1.1837 | 3.1e-05 |
| 1.400 | 0.285804 | 0.012110 | 0.010658 | **1.13631** | 1.1363 | 1.2e-05 |
| 1.000 | 0.500000 | 0.003988 | 0.010550 | **0.37798** | 0.3780 | 2.2e-05 |

**Every committed number reproduces**, to the last digit the committed record prints. The
baseline cutoffs and masses reproduce too: `(ω_E, ω_H, ω_Q, Ω) = (0.400481, 0, 0.562266,
0.037252)`. So does the pointwise claim (the flagged curve is steeper at *every* grid point
above κ = 0.7 for all three low-Ω rows) and the figure-magnitude claim (`0.011070` vs
`0.011170`; mean \|slope\| 0.02512 flagged vs 0.02362 pooled).

**One thing this run adds.** The committed record reports the sign at four grid points and
rounds the cut to "≈0.29". That 0.29 is simply the largest grid point at which failure was
confirmed — **the crossing itself was never located.** Bisecting on `k_D` puts it at
`k_D* = 1.28618`, i.e.

> **Ω\* = 0.3428.** Attenuation fails below it, holds above it.

The correct condition is therefore **Ω < 0.343**, not Ω < 0.29. This widens the failure
region rather than narrowing it, so ADR-0007's decision is unaffected — but anything that
quotes "≈0.29" as the boundary should quote 0.343 instead, and should say it came from this
run.

## 4. What the empirics lane should do with this

**Use it. It is a real prediction, not a placeholder.** But use it with three attachments:

1. **Expect Branch B's sign and a bounded null's magnitude.** A 6% difference in
   κ-sensitivity at the paper's own calibration will not clear a realistic MDE on 13D
   announcement CARs. Report it as a bounded null with the MDE quoted (`SPEC.md` §3.6),
   never as "no effect", and do not treat a small \|δ̂\| as evidence against the model.
2. **The mechanism is not the one Branch B's row in the spec describes.** The spec's
   Branch B story is that a shorter window concentrates informed trading into fewer days.
   The repo model has no window `T` at all — it has a flag that is either on or off. What
   produces the sign here is *composition*: when the public buy is flagged, the pooled cell
   loses its most revealing state, and the pooled cell's remaining κ-response more than
   makes up for the flagged cell's κ-invariance. Same sign, different reason. Do not write
   the spec's Branch B mechanism sentence into the paper on this evidence.
3. **The bridge from "shorter window" to "higher Ω" is assumed, not derived.** The repo
   experiment toggles the flag; it does not shorten a window. That gap is exactly why the
   two-round model is being built.

## 5. What would change the sign

- **Ω above 0.343.** The sign flips. Whether the real world sits above or below 0.343 is an
  empirical question about ω_a — and the repo has no answer to it (see §6). This is the
  single most important open input.
- **General equilibrium.** Everything here holds cutoffs fixed. The cutoff-shift channel is
  unsigned in the repo (`draft_v2` calls its own result "Partial Equilibrium"; the referee's
  T-3 finding is that no GE attenuation theorem exists anywhere in the repo). A GE term
  large enough and of the opposite sign would overturn the composite.
- **The two-round model.** Below.

## 6. The flagged-share data anchor (ω_a) — **absent**

The calibration target named in ADR-0007 is ω_a, the share of engagements that get
disclosed. **The repo contains no empirical estimate of it, and I am not inventing one.**

That absence is not an oversight in our reading — it is a property of the literature, and
three of the cards say so outright:

- **Becht, Franks, Grant & Wagner (2017 RFS)** — footnote 2: "What we cannot capture is
  private activism, that is, activism that is disclosed to the target firm, but not to the
  wider public and because of smaller stakes is not subject to regulatory disclosure." They
  add that the data to study it are "currently not available to us" (fn. 15).
  `research/cards/becht_franks_grant_wagner_2017_rfs.md:119, 96`
- **Norli, Østergaard & Schindele (2015 RFS)** — concedes private engagement may matter and
  that data on it do not exist. `research/cards/norli_ostergaard_schindele_2015_rfs.md:101`
- **Edmans (2014 survey)** — "investors may cluster just below 5% to avoid disclosure, and
  thus be missed by Schedule 13 filings." `research/cards/edmans_2014_arfe_survey.md:114`

**ω_a's denominator is the object the disclosure rule makes unobservable.** That is our
whitespace, and it is also why no card prints the number.

Three bounded proxies do exist in the repo. None of them is ω_a, and each should be labelled
for what it is:

| Proxy | Number | Source | Why it is not ω_a |
|---|---|---|---|
| Brav–Jiang–Partnoy–Thomas (2008 JF) sample construction | 1,032 of 1,059 events are 13D events; 27 non-13D events were added by a 13F sweep → **97.5%** | `research/cards/brav_jiang_partnoy_thomas_2008_jf.md:16-17` | **Upper bound only.** The sweep looked only at firms with market value > $1bn where the fund held > 2%. Undisclosed engagements outside that box are invisible by construction. |
| Gantchev (2013 JFE) sample construction | 21 sub-5% "nonpublic" campaigns out of 1,164 → **98.2%** | `research/cards/gantchev_2013_jfe.md:26, 62` | **Upper bound only, and self-declared non-random.** His own fn. 21: the 21 "represent a nonrandom sample … because they involve large and newsworthy targets with above-average press coverage." |
| SEC Release 33-11253, 2022 filing counts | 1,161 initial 13D vs 8,433 initial 13G → **12.1%** of new blocks are flagged as activist | `research/cards/_institutional_sec_33_11253.md:98, 102` (Release Table 1, p. 177; p. 190) | **Wrong unit.** This is the flagged share of *blocks*, not of *engagements*. A 13G filer is a blockholder who is not engaging, so it belongs in the denominator of a different ratio. |

**What this means for §5's condition.** Ω* = 0.343 is the number that decides the sign, and
Ω = Pr(a=1)·ω_a. The two upper-bound proxies (0.975, 0.982) sit far above Ω*, which would
put us in the *attenuation-holds* region; the block-level proxy (0.121) sits far below it,
in the *attenuation-fails* region. They disagree because they measure different things.
**Until ω_a is anchored, the sign published in §1 rests on the paper's own calibration
(Ω = 0.037) and not on data.** Getting ω_a — or a defensible bound on it tight enough to
sit on one side of 0.343 — is the highest-value calibration input the project can acquire,
and it needs a source outside the current card set.

## 7. Two-round model

**[LANDED — see §8 below. This section stays as written; it is the pre-registration of what
§8 was expected to deliver.]**

The re-run of this same experiment in the two-round model (one pooled trading round → the
flag lands or not → one flagged round plus the bidder's decision, per ADR-0007) will be
added **below this line as a new section**. The provisional number in §1 stays visible; it
is not to be overwritten.

**Amended 2026-08-23 (post-review):** What the two-round version changes and this version cannot: the window `T` becomes a genuine
primitive rather than a flag that is on or off, so "shorter window" maps into the model
directly instead of through the assumed bridge in §4.3; the stake at filing becomes an
object the empirics can measure; and the theorem being proved on it (ticket 26, T1) states
the window margin as an **iff** between the weight effect `W_T` and the composition effect
`C_T` — no unconditional window sign. The O-1 numbers in §3 are a **disclosure-regime analogy**:
they show that a composition factor can exceed one when a flag is observed versus hidden, but they
are not a window comparison and are not the live failure case for T1's iff. The genuine window-margin
record is `t2_t1_check` block 4, where `W_T C_T < 1` at every checked node at this calibration.

---

## Two-round model (2026-08-21)

**VERIFIED (2026-08-22): an independent agent re-ran every source script in full; all JSONs
reproduced bit-identically up to wall-clock timing fields
(`quality_reports/fixes/t2_rerun_verify_note.md`). The numbers in this section are final.**
Nothing above this line was changed by the re-run.

### 8.1 The answer in one line — and why it points the other way from §1

**Shortening the disclosure window makes the takeover premium LESS sensitive to liquidity at
the implemented two-round calibration.** Cutting the window from `T = 10` to `T = 5` cuts the
κ-sensitivity of the activism premium to between **18% and 77%** of its long-window value —
attenuation, at every node checked.

**This reverses §1's Branch-B amplification, and both are honest, because they are not the
same experiment.** §1 moves a *disclosure regime* (flag on vs flag off) in the static repo
model at **Ω = 0.037**; §8 moves the *window* `T` in the two-round model at **Ω ≈ 0.138**, and
T1's theorem states the window margin as an **iff** between the weight effect `W_T` and the
composition effect `C_T` — it signs nothing unconditionally, so the calibration decides, and
these two calibrations decide differently. Neither result refutes the other. The empirics
lane should treat §1 as the answer to "what does flagging do", §8 as the answer to "what does
a shorter window do", and quote the second when writing about the 2024 five-business-day rule.

| | |
|---|---|
| **Sign** | **Attenuation.** `W_T · C_T ≤ 1` at every node: 0/5 nodes above one at `H = 10`, 0/5 at `H = 12`. Equivalently the short window is *less* liquidity-sensitive, i.e. **δ > 0** on `LIQ × Post` given `β < 0` on RUNUP5 — the **opposite branch from §1**. |
| **Magnitude** | `W_T · C_T` for `(T', T) = (5, 10)`, by τ-quantile: **0.1818 / 0.1818 / 0.2055 / 0.4299 / 0.7724**. Weight leg `W_T` = 0.8559 / 0.8559 / 0.8622 / 0.9176 / 0.9730; composition leg `C_T` = 0.2124 / 0.2124 / 0.2384 / 0.4686 / 0.7939. `C_T` carries the effect; `W_T` is a 3–14% shave. |
| **Grid** | κ ∈ [0.15, 0.85], 71 nodes. τ ∈ {0.084627, 0.087884, 0.090764, 0.093376, 0.096028} (quantiles 0.1/0.3/0.5/0.7/0.9 of the seed-equilibrium Voice terminal-stake distribution). `H = 10`, `M = 2`, `T ∈ {5, 10}`. Sensitivity measured as total variation of `Δ^act` over the κ grid. 710 model evaluations, 826,686 feasible histories, 0 discarded mass. |
| **Condition** | **Fixed policies** — cutoffs frozen at the baseline equilibrium at every node (H5); no GE cutoff-shift term is signed here either. **The implemented calibration only**, i.e. `k = (1.240576, 1.531022)`, Ω = **13.8396%**, ω_a = `Pr(D=1\|a=1)` = **61.1473%**, `M_F` = **0.552818 pp**, `M_P` = **0.222798 pp**, π̄ = `Pr(a=1\|D=0)` = 10.2061%. |
| **Corner caveat** | At `H = 10` the long window is the corner `T = H = 10`, which drives `Ω(10)` to **6.81e-04** and makes the comparison corner-vs-interior rather than the two-interior-window comparison the theorem contemplates. The check flags its own result as suspect for exactly this reason (`suspected_forced_attenuation_bug: true` is an audit flag, not a detected bug — `C_T` is computed from independently enumerated `S_P` levels and is never clipped or signed). **The `H = 12` re-run, where `T = 10` is strictly interior, confirms attenuation**: `W_T · C_T` = 0.1099 / 0.1099 / 0.2406 / 0.5772 / 1.0000, with Ω(T=5) = 0.1687 → Ω(T=10) = 0.0289. The 0.9-quantile node returns exactly 1.0 there because the τ ladder stops biting, not because the product crosses. At `H = 12` the enumerated `S_P` is unavailable (8,503,056 × 14 = 1.19e8 exceeds the design's 1e8 gate, respected not overridden), so that column's `C_T` is the chord route. |
| **Model version** | `numerical_v4` two-round model, built 2026-08-21 on `v4-theory` (ticket 25; current card stamp 2026-08-23 · post-review repairs). The check JSONs' embedded provenance strings read "`0c9185b` / 2026-08-20" — the scripts captured the card stamp field as it stood when their provenance block was templated, not the build commit; params hashes `8ef7c5c2d3896bf8` (checks) / `b4482d7fee83a8e8` (smoke baseline) are the binding identifiers. Design: `research/model_v4/impl_design.md` §13 APPROVED. |
| **Evidence** | `quality_reports/fixes/t2_t1_check.json` (blocks 1–6 + `t1_H12_window_robustness`), `quality_reports/fixes/t2_l2_check.json`, `numerical_v4/smoke_output.txt`. |

### 8.2 Supporting checks that passed

- **Threshold margin (block 2).** The τ ladder gives the same direction: **0 of 8 pairs**
  have `W_τ · C_τ > 1`. The three pairs that reclassify real mass (all at `T = 5`) give
  **0.5566 / 0.4780 / 0.8846**; the other **5 pairs reclassify zero mass** and return
  1.000 to within 3e-16 — Step 14's null case, reported explicitly rather than inferred.
  Max identity residual **5.55e-16** (tolerance 1e-10).
- **Factorisation (block 1).** `S = (1-Ω) S_P` holds to machine noise: max pointwise
  residual **2.06e-16**, max TV residual **3.47e-18**, both against a 1e-10 tolerance. This
  is **wiring, not evidence** — at frozen policy Ω and `M_F` are κ-free by construction.
- **Ω flat in κ (block 1).** `max_κ |Ω(κ) - Ω(κ₀)| = 0.0` exactly, over all 71 κ nodes. H6
  is implemented, not merely asserted; a nonzero value here would have invalidated §8.1.
- **Flagged-side invariance (`t2_l2`).** Every flagged object is **exactly** κ-invariant —
  range 0.0 for `v̂`, `π_flagged`, `P^F`, `p_bid`, `M_F` and Ω, pointwise over the flagged
  quadrature nodes, and all four central-difference derivatives return exactly 0.0. The
  target is not vacuous: the pooled `M_P` moves **0.0722 premium pp** over the same grid,
  and the filing jump `J` moves **5,090 bp**.
- **O-1 benchmark (block 6) — repo model, reproduced.** The four committed ratios come back
  as **1.06397 / 1.18373 / 1.13631 / 0.37798** at Ω = 0.037252 / 0.128950 / 0.285804 / 0.500,
  max absolute difference **2.09e-06**; the bisected boundary reproduces at `k_D* = 1.286184`,
  **Ω\* = 0.342840**. Composition factors `C_O1` = 1.10514 / 1.35897 / 1.59104 / 0.75596
  against a predicted 1.1051 / 1.3590 / 1.5910 / 0.7560, max difference 4.32e-05. **§3 stands
  exactly as written**; nothing in the two-round work disturbs it.
- **Not evaluable: the local form (block 5).** `numerical_v4`'s legal clock computes the
  filing date as `f = c + T` with `c` an integer trading date and indexes the stake path at
  `int(f)+1`, so a fractional `T` is truncated rather than interpolated. The (21a) integral
  check of ρ and the count of nodes with ρ > 0 are therefore **unavailable**, and are reported
  as such rather than skipped. The finite form of Step 20 is still exercised by block 4.

### 8.3 Honesty: the theorem stack remains open at this calibration

**Amended 2026-08-23 (post-review):** The two recorded diagnostic failures do not establish that
the implemented pooled cell violates A($\tau$). The decisive support-enumeration check is ticket 33.

**The applicability of the chord mechanism `A(τ)` at the implemented pooled cell is OPEN.**
The two recorded failures were test-design artifacts, and neither was smoothed.

- **`t2_t1` block 3 (magnitude).** The residual `|S_P − Δ_m |A'_κ| |C_h(π̄)||` is
  **0.006279 (0.628 premium pp)** against a 1e-10 tolerance — a **relative** residual of up
  to **3.63**, i.e. the closed form is off by a factor of roughly four, not by a rounding.
  The check hard-coded `|A'_κ| = 0.25` from Example A, while the implied coefficient from the
  enumerated sensitivity is **[0.997, 1.158]**. The chord's *shape* is fine —
  `|C_h(π̄)|/π̄²` is constant to **0.48%** between the two smallest π̄ nodes, well inside 5%.
  Thus this check rejects the hard-coded Example-A calibration, not A($\tau$)'s general support
  representation; the coefficient level remains open.
- **`t2_l2` placebo (orientation).** The placebo demanded `∂κ M_P ≤ 0` from the maintained
  `C_h(π̄) ≤ 0`, but A($\tau$) does not sign `A'_κ`. The card's own Example A has
  `A'_κ = -1/4`, so the demanded sign is not implied by A($\tau$). The enumerated pooled `M_P`
  is **hump-shaped in κ** — rising to a peak near **κ = 0.55** and falling after, with **10 of 18**
  increments positive and one sign change. This placebo is therefore misformulated; it does not
  decide whether the support representation holds.

**What this costs, stated plainly.** The theorem stack's *conditional* legs — anything that
runs through `A(τ)`'s three-atom closed form, including L4's prediction 5 and the chord route
to `C_τ` — **remain conditional and are not mechanically validated by these diagnostics.** The
numbers stand on the executed enumeration; the theorems stand on their stated hypotheses; the
two are not currently joined at this calibration. This is an open applicability question, **not**
a wiring error: the design ruled from the outset that the enumeration never imposes `A(τ)`, so
the queued support check is the appropriate test. Two consequences
for the empirics lane: **(i)** do not write any mechanism sentence that leans on the chord
formula; **(ii)** the `H = 12` column's `C_T` travels the chord route, so treat it as
directional corroboration of the corner audit, not as a second independent magnitude.

One further limit worth naming: all five `T = 10` nodes at `H = 10` are flagged
**degenerate** — flagged-cell mass 0.000681 is below the 0.01 threshold — which is the same
corner §8.1 already discloses, seen from the mass side.

---

*Written by the ticket-05 agent, theory lane, `v4-theory`. Reproduce §1–§6 with
`.venv/bin/python quality_reports/fixes/t1_o1_rerun_check.py` from the worktree root.
§8 added by the ticket-30 agent, 2026-08-21, from the committed
`quality_reports/fixes/t2_t1_check.json`, `t2_l2_check.json` and
`numerical_v4/smoke_output.txt`.*
