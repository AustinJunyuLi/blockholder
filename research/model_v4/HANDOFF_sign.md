# HANDOFF — the window-margin sign

**Status: PROVISIONAL.** Repo model (`draft_v2`, the `numerical/` package), fixed cutoffs,
partial equilibrium. **Date: 2026-08-21.** Ticket 05 (T1).

This is the empirics lane's only dependency on the theory lane. The empirics lane **may
consume the number below now.** It will be replaced — not overwritten — when the two-round
model lands (see "Two-round model" at the bottom).

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

**[PLACEHOLDER — lands with tickets 25 / 30.]**

The re-run of this same experiment in the two-round model (one pooled trading round → the
flag lands or not → one flagged round plus the bidder's decision, per ADR-0007) will be
added **below this line as a new section**. The provisional number in §1 stays visible; it
is not to be overwritten.

What the two-round version changes and this version cannot: the window `T` becomes a genuine
primitive rather than a flag that is on or off, so "shorter window" maps into the model
directly instead of through the assumed bridge in §4.3; the stake at filing becomes an
object the empirics can measure; and the theorem being proved on it (ticket 26, T1) states
the window margin as an **iff** between the weight effect `W_T` and the composition effect
`C_T` — no unconditional window sign. The O-1 numbers in §3 are the live failure case that
iff has to accommodate.

---

*Written by the ticket-05 agent, theory lane, `v4-theory`. Reproduce with
`.venv/bin/python quality_reports/fixes/t1_o1_rerun_check.py` from the worktree root.*
