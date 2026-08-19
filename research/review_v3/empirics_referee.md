# Empirical-design referee report — framework_v3

**Referee:** empirical-design (identification, measurement, sample arithmetic, honesty)
**Object:** `framework_v3.qmd` §4 "Empirical Design", lines 221–330 (+ risk register, l.352–361)
**Posture:** JF/RFS empirical referee. Every claim below is grounded in a repo file (`path:line`) or in the
project's own lit briefs; literature facts recalled without an in-repo source are flagged `[memory — verify]`.
**Data checks:** executed in-session against the gitignored `empirics/data/` assets (see final section).

---

## Summary verdict (≤150 words)

Section 4 is a well-read *plan*, not committed empirics. The vocabulary is right — placebos, bundled
confounds, selection honesty, medians over means — but the three headline numbers all overstate what is
behind them: F1's "n = 300" is 188 usable filings; H1's "9,234 parsed" is ~1,000 events in the memo's own
preferred windows, 301 of them post-rule; and F3's "medians 1.6% → 2.6%" comes from a 21-day CAR window,
not an announcement window. I ran the disk-resident data: **the half-year median CAR series shows no break
at 2024-02-05**, and the pre/post sign flips if the pre window starts in 2022 rather than 2023. H1 is a
single-group before/after, not a DiD; H2's ratio statistic is undefined in the usual sense; H3 is
underpowered by roughly 4x and conditions on the outcome. Fixable, but not as written.

---

## Findings table

| id | severity | memo text (qmd line) | problem | evidence | fix |
|---|---|---|---|---|---|
| E1a | **MAJOR** | "the DiD must be bulletproof" (l.348); spec l.249–256 | Single-group before/after with a continuous interaction is called a DiD. There is no untreated group anywhere in the design. | Spec has `Post`, `Amihud`, `Amihud×Post` only; every US 13D filer is treated on 2024-02-05 | Rename to "before/after with dose-response and rich controls". Add the bindingness dose (below). Reserve "DiD" for the triple-difference. |
| E1b | **MAJOR** | H1 as a whole | No pre-trend evidence on the *outcome*; the memo shows a pre/post contrast only. | My check: half-year median CAR 2022H1 4.38%, 2022H2 2.96%, 2023H1 1.69%, 2023H2 0.36%, **2024H1 1.01%**, 2024H2 5.95%, 2025H1 2.80%, 2025H2 0.82% — no break at the rule date; 2024H1 (treated) is *below* 2023H1 | Lead with a calendar-time coefficient figure (quarterly β̂₁ by quarter, 2022–2025). If it does not break, say so and reposition H1 as a bounded null. |
| E1c | **MAJOR** | "Placebos: 13G filers (untreated by the 13D change before September 2024)" (l.273–275) | 13G filers are not a control group: different population (QII/passive/exempt), different outcome (CAR ≈ 0.6%, EFZ 2013), *and* the same October 2023 release retimed their filings. A "placebo" that is a different population tests nothing. | `research/lit_institutional-facts.md` §1.3 (13G table); `research/lit_liquidity-premia-empirics.md` §1 (13G CAR 0.7%) | Drop 13G as a control; keep it as a *composition diagnostic* (13D/13G share pre/post). Replace with the within-13D dose design. |
| E1d | **MAJOR** | l.269–275 | Anticipation is unhandled: the rule was adopted 2023-10-10 (proposed 2022-02-10). The memo's pre window (2023 onward) contains four months of announced-but-not-effective regime. | `research/lit_institutional-facts.md` §1.3 | Donut out 2023-10-10 → 2024-02-04, or model it as a partially-treated segment and show it. |
| E2a | **MAJOR** | l.269–273 lists 4 confounds | The filing cut-off extension to **10 p.m. ET, same date 2024-02-05**, is missing. It mechanically re-maps filing timestamps to trading days: a 6 p.m. filing that pre-rule stamped the next business day now stamps the same day. That shifts CAR[−1,+1] alignment by one day for exactly the treated period. | `research/lit_institutional-facts.md` §1.3 final bullet; `fact2_parsed.jsonl` already carries `accepted` and `accepted_after_4pm` | Align event day on the *first trading session after acceptance*, not `date_filed`; report the share `accepted_after_4pm` pre vs post as a first-order diagnostic. |
| E2b | **MAJOR** | l.270–272 | T+1 (2024-05-28) sits **inside** the memo's own main post window (Feb–Aug 2024). A "dummy" for a pure time break inside a 7-month post window is not separately identified from the treatment's own time path. | `research/empirical_feasibility.md` §5.2(c) | Either end the main post window 2024-05-24, or drop the dummy and report the Feb–May and Jun–Aug post halves separately. |
| E3a | **MAJOR** | ρ = CAR[−10,−2]/CAR[−10,+1] (l.284–287) | Ratio of two signed returns with a denominator that crosses zero: no finite mean, sign flips discontinuously. E[ρ|Post] < E[ρ|Pre] is not a testable statement. | My check: only 52–62% of event CARs are positive by half-year, so the denominator is negative for ~40% of events | Replace with stacked-levels regression (text below). |
| E3b | **MAJOR** | l.284–287, 291–292 | Window/anchor incoherence. CAR[−10,−2] and CAR[−10,+1] are filing-relative in the formula but l.291–292 says run-up windows use event dates. Under the new rule the same filing-relative window covers a different economic phase (mostly pre-trigger) than under the old — a mechanical "shift" with zero behavioural change. | l.285 vs l.291–292 | Anchor all run-up windows on the **event (crossing) date** and add the crossing→filing segment as its own window whose *length is the treatment*. |
| E3c | **MAJOR** | "CDF (2015) benchmark of a ~7% run-up vs ~3% jump" (l.288–290) | CDF's 7% is over **(t−60, t−1)**, ~60 trading days. A 9-day [−10,−2] window is not comparable. Also the 7%/3% and "2001–2010" figures are the NBER WP numbers; the published JF version uses 1994–2007. | `research/lit_liquidity-premia-empirics.md` §3 and its access caveat | Use CDF's own (−60,−1) window, or drop the numeric benchmark and keep the direction. Verify against the published JF before citing "2001–2010". |
| E4 | MINOR | Amihud formula (l.264–265) | Single-day formula. Amihud (2002) is a *pre-period average*; measuring it near the event is contaminated precisely by the treatment (CDF: Amihud falls 46% on filer trade days). | `research/lit_liquidity-premia-empirics.md` §3 | Replacement definition below (E4). |
| E5a | **MAJOR** | H3 5 quintiles (l.302–307) | Underpowered. ~300 deals / 5 cells = 60 per cell; with premium SD ≈ 35pp, SE(θ₃−θ₁) ≈ 6.4pp, so an 8pp hump gives t ≈ 1.25. | premium SD from mean premia 25.9–36.6% in `lit_liquidity-premia-empirics.md` §5a and the C&L row at l.327; SE arithmetic mine | Terciles, or a quadratic with a Lind–Mehlum (2010) U-test. State the MDE. |
| E5b | **MAJOR** | "H₃: θ₃ > θ₁ ∧ θ₃ > θ₅" (l.307) | Not a Wald hypothesis. Two one-sided inequalities are an intersection–union test (reject only if *both* one-sided t's reject at α). A Wald test of θ₃=θ₁=θ₅ tests the wrong null. | — | Use the IU test, or the Lind–Mehlum U-test on a quadratic with a Fieller CI for the turning point. |
| E5c | **MAJOR** | "deals receiving a bid within 12 months" (l.297) | Conditions on an outcome the model says κ moves. If liquidity raises bidder entry, the bid-receiving subsample is selected on Amihud and the "hump" can be pure selection. | model: bidder entry p; l.328 lists a takeover-probability moment | Report P(bid \| Amihud quintile) as its own result, and report the unconditional p·Premium as the headline object. |
| E6a | **MAJOR** | "$n = 300$ SC 13D originals" (l.231) | 300 were *sampled*; 188 carry a usable delay (98 pre + 90 post). Parse rates 0.68 / 0.64. | `empirics/output/fact1_summary.csv` (count 98/90, parse_rate 0.68/0.64) | Replacement text below (E6). |
| E6b | **MAJOR** | l.229–231 | Manski bounds on the headline do not sign the effect at the current parse rate: worst-case Δ(share within 5 bd) ∈ **[−7.9pp, +60.1pp]**. A parse rate above ~0.72 in both windows would sign it. | my arithmetic from `fact1_summary.csv` | Report the bounds; make raising the parse rate a precondition for calling F1 "done, committed". |
| E6c | MINOR | F1 machinery | `np.busday_count` counts Mon–Fri with **no US federal holiday calendar** (`empirics/facts.py:68`), so any filing spanning a holiday reads one business day late. The post window 2024Q3–Q4 contains 4 federal holidays. The 75.6% within-5-bd share is a lower bound. | `empirics/facts.py:65-70` | `np.busdaycalendar(holidays=<US federal holidays>)`. |
| E6d | MINOR | F1 machinery | The `0 ≤ delay ≤ 60` junk filter (`empirics/facts.py:94`) truncates asymmetrically — pre p90 = 23 bd vs post 11.1 bd — biasing the *mean* compression downward and removing 4 pre / 6 post rows silently. | `empirics/facts.py:94`; `fact1_summary.csv` p90 column | Report the filter and the untruncated quantiles. |
| E7a | **MAJOR** | F2 (l.233–234) | `pct_of_class` is not usable. The regex `[0-9]{1,2}(\.[0-9]+)?` **cannot capture 100%**: I fed it `"…ROW (11): 100.0%"` and it returned **0.0**. In the full universe 347 filings read exactly 0.0 and **448 read exactly 2.6%** — 7.2% of all parsed values at one impossible number for a 13D original. 22.9% of parsed values are below 5%. | `empirics/parse_13d.py:105-106`; my regex test + `fact2_parsed.jsonl` | Fix the regex (allow 3 digits; anchor to "ROW (11)"), take the **aggregate** row not the first reporting person, and hand-verify 100 filings. |
| E7b | **MAJOR** | F2 target moments (l.233–234) | Comparing an *unscreened* 2022–2025 all-filer universe (raw median 9.55%) against CDF's *screened* 2001–2010 activist sample (median 6.20%) is not a moment match. Today's universe is full of SPAC sponsors, PIPE investors, founders and post-merger cleanups CDF screened out. | `research/lit_liquidity-premia-empirics.md` §3; my full-universe median 9.55% | Replicate CDF's screens; report raw and screened. |
| E7c | **MAJOR** | Calibration table (l.319–330) | 4–5 of 10 rows have **no counterpart** in the three-branch model as specified (unit stake, one blockholder, static, no staged costs). Printed as "moments the model must match", the table invites "your model matches half of nothing". | model spec per CLAUDE.md and l.336–345 | Split into "targeted" and "motivating" blocks with a `model object` column — mapping below. |
| E8 | **MAJOR** | F3 (l.235–236) + discipline (l.224–226) | F3 *is* a signed model prediction (larger disclosure jump when less is inferred pre-filing) but is filed under "facts", and its decisive confound — a shorter window means a **smaller stake at filing**, pushing the jump the other way — is nowhere stated. Also the 1.6→2.6 numbers are 21-day-window CARs, not announcement CARs. | `wrds_evtstudy_edate.csv` `nrets`=21 for 2,264 of 2,285 rows; `research/empirical_feasibility.md` §1.2 | State both forces; test the intermediate outcome (stake at filing) directly; re-run on [−1,+1]. |
| E9 | **MAJOR** | "Boyson et al.'s 70% within 2 years" (l.239) | Mismatched objects. G&S's 18.1% is an *unconditional* 12-month acquisition rate (21.9% at 18 months). The Boyson figure as the repo records it is "70% of **bids** within 2 years of campaign start" — a share of bids conditional on a bid. Printed side by side they imply an unconditional 18% → 70% path, which contradicts G&S's own 18-month number. | `research/lit_activism-empirics.md:59`; `research/lit_theory-to-empirics-templates.md` §2 (Corum–Levit citing Boyson et al. 2016) | Relabel or drop. Also add G&S's control rates (7.2% matched, 12.6% non-activist 13D) — without them 18.1% means nothing. Cite Boyson, Gantchev & Shivdasani (2017, JFE 126) with a year. |
| E10a | **MAJOR** | l.262–263 "9,234 parsed" | The memo's own main spec (post = Feb–Aug 2024, l.269–270; pre starts 2023, l.272) yields **989 matched events, 301 post**, in the existing WRDS output. 9,234 is 9x the estimation sample. | my check on `wrds_evtstudy_edate.csv` | Print an attrition table (below); quote the estimation sample, not the parse count. |
| E10b | **MAJOR** | "cluster by firm and month" (design note) | The main post window has **7 month-clusters**. Cluster-robust inference with 7 clusters on one side is badly undersized, and a month-clustered SE cannot service a month-level treatment. | my check; `quality_reports/plans/2026-06-10_fact2-event-study-design.md` | Cluster by firm (403 repeat firms, max 9 events); handle the time dimension with randomization inference over placebo rule dates (Conley–Taber 2011) [memory — verify]. |
| E10c | **MAJOR** | H1 power | Back-of-envelope: with n ≈ 989, post share 0.30 and CAR[−1,+1] SD ≈ 0.15, SE(β₂ per SD Amihud) ≈ 0.15/√(989·0.3·0.7) ≈ **1.0pp**. Detectable at t = 2 is a 2.1pp-per-SD attenuation — more than **twice the entire Amihud level loading** AFS estimate (+0.9pp/SD). | AFS loading from `lit_liquidity-premia-empirics.md` §6; SE arithmetic mine | State the MDE explicitly. Consider pooling windows or accepting H1 as a bounded null. |
| E10d | MINOR | l.267 "filer type via name regex with hand spot-checks" | A name regex is not a defensible classifier for a JF table when filer type carries the composition story. | — | Hand-code a random 150; report precision/recall; or use SharkWatch/Activist Insight. |
| E10e | NOTE | F1–F4, H1–H3, multiple windows and quantiles | Dozens of tests, no multiplicity discipline, in a paper whose selling point is discipline. | l.223 "one dated shock, one signed prediction per test" | Pre-specify a primary set; Romano–Wolf or BH for the rest. |
| E10f | NOTE | `wrds_evtstudy_edate.csv` | Provenance ambiguity: the filename says `edate` (event date) but the content is consistent with **filing** dates — 582 rows fall in 2025, where the parser recovers **zero** event dates. `research/empirical_feasibility.md` §2.1 also calls them filing-date CARs. | my check: 2025 event-parse rate = 0.000 but 582 evtdate rows in 2025 | Nail down and document before any number leaves the repo. |

---

## Detailed notes E1–E10

### E1. What does β₂ identify? — **MAJOR**

**What it is.** β₂ is the change, across a single calendar break, in the cross-sectional covariance between
pre-event illiquidity and the filing-window return. It is a *before/after* estimand. It differences out
nothing that is common to firms; it differences out only the level shift γ. Calling this a "DiD"
(l.348) is not honest by JF/RFS standards, and a referee who reads the specification at l.249–256 will
say so in the first paragraph of the report. There is no second group, treated or otherwise, in the
equation.

**Threat (a) — filer selection.** The model itself predicts the marginal filer changes: a shorter window
lowers the value of the accumulation option, so the filers who still find a 13D worthwhile post-rule are
different. `research/empirical_feasibility.md` §5.3 says exactly this. β₂ then confounds
"inference channel weakened" with "who files changed". The memo's answer (l.276–279, "report filer-mix
diagnostics") is a diagnostic, not an identification strategy.

**Threat (b) — mechanical composition.** This is the one I would push hardest. Five business days
instead of ten calendar days means less time to accumulate after crossing 5%. CDF document that
filers acquire **1.8% of shares outstanding between the trigger and the filing, ~23% of the final stake**
(`research/lit_liquidity-premia-empirics.md` §3). Cutting that window mechanically cuts the disclosed
stake. Smaller disclosed stakes are weaker news, and stake size is itself correlated with liquidity
(illiquid names are harder to accumulate fast). So the Amihud slope can move purely through the stake
channel with no change whatsoever in how the market infers. **β₂ is not identified without conditioning
on, or instrumenting, the disclosed stake.** The memo never mentions this.

**Threat (c) — time-varying liquidity–return relation.** 2022–23 (hiking, small-cap drawdown, M&A trough)
versus 2024 (cuts, recovery) is precisely the kind of regime shift under which the illiquidity premium
moves. AFS estimate a +0.9pp-per-SD Amihud loading on 13D announcement returns that is *pure stock-picking*
(`lit_liquidity-premia-empirics.md` §6) — that loading is a risk-premium object and there is no reason to
believe it is constant across a rate cycle. β₂ absorbs any change in it.

**Threat (d) — pre-window contamination.** The memo starts pre in 2023 to escape universal proxy
(l.272). That leaves 13 months of pre window, of which the last four (Oct 2023 → Feb 2024) are
post-adoption and therefore anticipatory.

**On the proposed placebos.** 13G filers fail on three counts (population, outcome, and their own
treatment on 2024-09-30 — `lit_institutional-facts.md` §1.3). "Non-activist 13D filers" are treated by the
identical rule; they are a *dose* group at best, not a placebo. "Low-activism-exposure targets" is a
target-side split, not an exposure-to-the-rule split. None of the three is a placebo in the sense a
referee means.

**The credible design.** Four pieces, all executable on data already on disk:

1. **Rename.** "A before/after comparison around a dated regulatory change, with a dose-response design
   and rich controls." Reserve "difference-in-differences" for piece 3.
2. **Event-time / calendar-time coefficients.** Estimate β₁ separately by quarter, 2022Q1–2025Q4, and plot
   with CIs. Same for the median CAR. This is the figure the referee will look for first, and it doubles
   as the pre-trend test. I ran the median version already and it does not break at the rule date
   (see Data checks) — better to find that out now than in a referee report.
3. **Bindingness as a dose (the triple difference).** For each filer CIK, compute the pre-2024 leave-one-out
   median disclosure delay from `fact1_filings.csv` / `fact2_parsed.jsonl` (requiring ≥3 pre-period
   filings). Filers whose historical median exceeded 5 business days are the ones the rule actually
   binds; filers already inside 5 days are, for practical purposes, untreated. Then

   ```
   CAR_i = β₁ Amihud_i + β₂ (Amihud_i × Post_i) + β₃ (Amihud_i × Dose_f)
         + β₄ (Amihud_i × Post_i × Dose_f) + [all lower-order interactions]
         + δ′X_i + FE + ε_i
   ```

   β₄ is the object with a control group. Report the first stage — that Dose predicts the actual delay
   compression — as its own panel. Caveat honestly: Dose is measured with error and mean-reverts;
   leave-one-out construction and a ≥3-filing screen mitigate, and an alternative dose (filer-type,
   or the *target's* pre-period average time-to-file across all its filers) can be shown alongside.
4. **Placebo dates and randomization inference.** Re-estimate with fake rule dates on the first
   business day of February in 2022, 2023 and 2025, and more generally at every month-start in the sample.
   The distribution of |β̂₂| across placebo dates *is* the inference — this is the right answer to the
   7-post-month-cluster problem, not a cluster-robust SE.

**Replacement text for l.241–248 (hypothesis and posture):**

> **Hypothesis and design posture.** Shortening the accumulation window moves information release from
> pre-filing inference to the filing event; the sensitivity of 13D announcement returns to pre-event
> liquidity should fall after February 5, 2024. Because every US 13D filer is treated on the same date,
> this is a *before/after* comparison with rich controls, not a difference-in-differences: we say so, and
> we do not report it as one. Identification therefore rests on three things and is only as good as the
> weakest — (i) a calendar-time plot of the liquidity slope showing that any break sits at the rule date
> and not elsewhere; (ii) a dose-response design in which filers whose pre-rule filing behaviour already
> satisfied the five-day deadline serve as the plausibly-untreated comparison, delivering a genuine
> triple difference; (iii) randomization inference over placebo rule dates. Absent all three, β₂ is a
> descriptive statistic and we label it as one.

### E2. Bundled confounds — **MAJOR**

Everything sharing the treatment date, or landing inside a plausible post window, with a verdict on whether
it bites. Dates from `research/lit_institutional-facts.md` §1.3 (primary-sourced there to SEC Releases
33-11253 / 34-98704, 88 FR 76896).

| # | Change | Date | Bites H1? | Bites H2? | Handling |
|---|---|---|---|---|---|
| 1 | 13D initial deadline 10 cal. days → 5 business days | 2024-02-05 | *the shock* | *the shock* | — |
| 2 | 13D amendment "promptly" → **2 business days** | 2024-02-05 | Yes, second-order | **Yes, first-order** | Post-rule, ±1% amendments and wolf-pack follow-ons arrive inside the [−10,+1] window. Flag events with any 13D/A on the subject inside the window; report with and without. |
| 3 | 13G→13D switch: file within 5 bd; cooling-off 10 cal. → 5 bd **after** filing | 2024-02-05 | Yes — composition of 13D originals, and post-filing drift | Yes | Flag 13G→13D switches (prior 13G by the same filer/subject) and report separately. |
| 4 | **Filing cut-off extended to 10 p.m. ET** | 2024-02-05 | **Yes, mechanically** | Yes | The sharpest bundling problem, and the memo omits it entirely. Align the event day on the first trading session after `accepted`; report the `accepted_after_4pm` share pre/post. Data already parsed. |
| 5 | Cash-settled-derivatives guidance (Rule 13d-3(b) reaffirmation; Item 6) | 2023-10-10 release | Yes — changes who crosses 5% and when | Yes | Flag derivative language; the design note already anticipates the parser field. |
| 6 | Group-formation guidance under §13(d)(3) | 2023-10-10 release | Yes — wolf-pack aggregation | Yes | Report multi-filer group filings separately. |
| 7 | 13G initial (QII/Exempt): 45 days after year-end → after **quarter**-end | 2024-09-30 | Only via 13D/13G composition | Same | Memo handles by ending the main post window in Aug 2024 — correct. |
| 8 | 13G initial (Passive) 10 days → 5 bd; 13G amendments quarterly; passive ±5% → 2 bd | 2024-09-30 | Composition | Composition | Same; and it kills the 13G placebo. |
| 9 | Structured XML mandate | 2024-12-18 | Measurement break (and the parser dies) | Same | End the main sample there; 2025 as extension. |
| 10 | **T+1 settlement** | 2024-05-28 | Inside the main post window | Inside | Not a dummy — split the post window Feb–May / Jun–Aug. |
| 11 | Universal proxy Rule 14a-19 (meetings after 2022-08-31) | 2022-08-31 | In the earlier pre window | Same | Memo handles by starting pre in 2023 (l.272). State the cost: it halves the pre window and weakens the pre-trend evidence. |
| 12 | **Anticipation**: rule proposed 2022-02-10, adopted 2023-10-10 | — | **Yes** | Yes | Missing from the memo. Donut Oct 2023 → Feb 2024. |
| 13 | Macro/market regime: 2022–23 hikes, 2024 cuts; M&A trough → recovery; activism-volume cycle | — | Yes | Yes | Missing. Add month FE where identified, and report the Amihud slope for a *non-event* matched sample of firm-quarters as a background-slope control. |

The memo's four-item list (l.269–275) covers #7, #9, #10 and #11. Items **#2, #4, #12 and #13** are absent,
and #4 is the one that can move CAR[−1,+1] by a day for exactly the treated observations.

### E3. The H2 statistic — **MAJOR**

**Why ρ fails.** CAR[−10,+1] is a signed return, near zero for a large share of events and negative for
roughly 40% of them (my half-year check: only 52–62% of event CARs are positive). A ratio with such a
denominator has no finite mean, and ρ flips from +∞ to −∞ as the denominator crosses zero. Comparing
E[ρ|Post] to E[ρ|Pre] is not a well-posed test, and no amount of winsorizing rescues it — winsorizing a
Cauchy-like variable produces a number that depends entirely on the trim point.

**Replacement — the stacked-levels test.** Compute two window CARs per event, `RunUp_i = CAR_i[−40,−1]`
(event-date-anchored) and `Jump_i = CAR_i[−1,+1]` (filing-anchored). Stack them, two rows per event:

```
CAR_iw = a + b·Post_i + c·1{w = Jump} + d·(Post_i × 1{w = Jump}) + δ′X_i + ε_iw ,
```

clustered by event and by firm. `d` is the object: the differential post-rule change in the jump relative
to the run-up. It is a real difference-in-differences — across *windows within an event* — which is the
one place in this whole design where a DiD label is earned. Report the two window-level medians with
bootstrap CIs alongside, and, if a share is wanted, use the bounded
`RunUp_i / (|RunUp_i| + |Jump_i|) ∈ [−1,1]`, never a ratio of signed returns.

**Timing logic.** With a 5-business-day deadline, [−10,−2] *relative to filing* is roughly 12 calendar days
before the filing, i.e. about a week **before** the 5% crossing — pre-trigger accumulation. Under the old
10-calendar-day rule the same filing-relative window straddled the crossing. The same window is a
different economic object in the two regimes, so a "shift" appears mechanically. This must be fixed by
anchoring on the event date, and the memo's own sentence at l.291–292 ("run-up windows use parsed event
dates") contradicts the formula at l.285 — reconcile them explicitly. Practical warning: event dates are
parsed for only 64–68% of 2022–2024 filings and **0% of 2025** (my check), so H2's sample is that
intersection, not 9,234.

**Third window.** Add `CAR_i[event, filing−1]` — the disclosure-lag window whose *length is the treatment*.
Its shrinkage is the mechanism, and it is the panel that makes H2 about the rule rather than about windows.

**CDF benchmark.** Wrong window. CDF's ~7% is over (t−60, t−1), ~60 trading days, against a ~3%
filing-day jump (`research/lit_liquidity-premia-empirics.md` §3). Either adopt (−60,−1) or drop the number.
And note the access caveat in that same brief: 7%/3% and "2001–2010" are the **NBER WP 18452** figures; the
published JF 2015 version uses 1994–2007. Citing "2001–2010" as the JF sample is a verifiable error.

### E4. Amihud measurement — MINOR (but embarrassing if left)

The single-day formula at l.264–265 is not the Amihud measure and would be corrected by a referee in one
line. Worse, measuring illiquidity *at* the event is contaminated by the treatment itself: CDF show Amihud
falls **46%** on filer trade days and hits a local minimum around the filing date
(`lit_liquidity-premia-empirics.md` §3).

**Replacement text for l.263–265:**

> Illiquidity is the Amihud (2002) measure, computed as a **pre-event average over trading days
> [−250, −11] relative to the filing**, deliberately excluding the accumulation window:
> $\mathrm{ILLIQ}_i = \frac{1}{D_i}\sum_{t=-250}^{-11} \frac{|r_{i,t}|}{\mathrm{DVOL}_{i,t}}$ (dollar
> volume in millions), requiring $D_i \ge 100$ valid days. We use
> $\mathrm{Amihud}_i = \ln(1 + \mathrm{ILLIQ}_i)$, winsorized at the 1st and 99th percentiles, and follow
> Edmans, Fang & Zur (2013) in reporting the $-\ln(1+\cdot)$ liquidity orientation in an appendix table.
> Because Amihud is close to an inverse transform of size, every specification includes log market
> capitalization and log turnover, and we report the Amihud–log-cap correlation in the summary table; the
> preferred specification uses within-industry-and-size-decile Amihud ranks so that $\beta_1$ is not a size
> slope in disguise. We note the standard Nasdaq dealer-volume caveat. Firm fixed effects are reported for
> the repeat-filer subsample only (403 subject firms with more than one event, maximum 9), with
> cross-sectional estimates as the baseline.

### E5. H3 — **MAJOR** on three counts

**Power.** Five quintiles on "a few hundred deals" is ~60 per cell. With a premium SD around 35pp
(consistent with mean premia of 25.9–36.6% in `lit_liquidity-premia-empirics.md` §5a and the Celentano–Levine
row at l.327), SE(θ₃−θ₁) ≈ 35·√(2/60) ≈ 6.4pp, so an 8pp hump gives t ≈ 1.25. Terciles give ~100/cell and
SE ≈ 4.9pp — still thin. State the minimum detectable effect.

**The joint test.** θ₃ > θ₁ ∧ θ₃ > θ₅ is an **intersection–union** hypothesis: the size-α test rejects only
if both one-sided t-statistics reject at α, and no multiplicity adjustment is needed (power is the
minimum of the two). A Wald test of θ₃ = θ₁ = θ₅ tests equality and is the wrong null. The cleaner and
more standard route is a quadratic, `Premium = a + b·Amihud + c·Amihud² + δ′X`, tested with the
**Lind & Mehlum (2010)** U-test — it asks jointly whether the turning point lies inside the observed
Amihud range and whether the slope is positive at the low end and negative at the high end, which is
exactly the inverse-U hypothesis. Report the turning point with a Fieller confidence interval.

**Premium measurement.** −42 trading days is Schwert's (1996) convention and is defensible; name it as such
[memory — verify Schwert 1996 JFE 41]. SDC's own fields are −1 day, −1 week and −4 weeks
(`lit_institutional-facts.md` §7), and Massa–Xu use 63 days (`lit_liquidity-premia-empirics.md` §5b). Report
all four. The hazard specific to this sample is not mentioned in the memo: for a 13D target the **13D
filing itself typically precedes the bid**, so a "unaffected" price 42 trading days before the bid may
already contain the activism news. Use `min(−42 trading days, the day before the 13D filing)` as the base
and report both.

**Selection.** Conditioning on a bid within 12 months conditions on the outcome that κ is supposed to move.
Three fixes, in increasing order of honesty: (i) report `P(bid | Amihud quintile)` as its own panel — it is
a model prediction in its own right, and the premium hump has to be read jointly with it; (ii) a
control-function correction needs an exclusion restriction that shifts bid arrival but not the premium —
industry merger-wave intensity or cross-industry acquirer cash are the usual candidates and neither is
clean; (iii) **report the unconditional object `P(bid|q) × E[Premium|bid,q]`**, which is not conditioned on
the outcome and is closer to what the model produces.

**Model counterpart.** The model's Δ^min is the **minority gain conditional on a takeover occurring** —
so its counterpart is the bid premium conditional on a bid, *not* the 13D announcement return. State
this. The unconditional analogue is p·Δ^min. The memo currently leaves which object is being matched to
inference.

**Currency vs inference channel.** Huang–Maharjan–Nanda (2024, JCF) is about *acquirer minus target*
liquidity and is null in cash deals — that null is what identifies their channel
(`lit_liquidity-premia-empirics.md` §5a). Massa–Xu (2013, JFQA) is about target liquidity levels and is
public-bidder-specific. AFS's +0.9pp/SD is a level loading present for both filing types. The memo lists
all three as "anchors to confront" (l.309–316) but never says what specification separates them. Concretely:
control for the acquirer–target Amihud difference wherever the acquirer is public; **split cash versus
stock and require the hump to appear in both** (an inference channel is not payment-method-specific — if
the hump shows up only in stock deals it is the currency channel and H3 has failed); split public versus
private acquirer (Massa–Xu's channel is public-bidder-specific); and include the Amihud level control
throughout so the hump is identified off curvature, not level.

### E6. F1 — **MAJOR** on wording, MINOR on machinery

The memo says "$n = 300$ SC 13D originals" (l.231). `empirics/output/fact1_summary.csv` says the statistics
rest on **98 pre and 90 post** filings, at parse rates of 0.68 and 0.64, after a `0 ≤ delay ≤ 60` filter
(`empirics/facts.py:94`) that itself removes 4 and 6 more rows. The honest number is 188.

**Is the parse failure non-random?** Almost certainly. The cover-page date is found by regex
(`empirics/parse_13d.py:76-96`); filings that fail are disproportionately scanned/exhibit-style layouts,
group filings with several cover pages, and foreign filers — exactly the tail where delays are long.
So the parsed sample plausibly over-represents compliant filers.

**Bounding.** With share-within-5-bd point estimates 0.357 (pre) and 0.756 (post) at parse rates 0.68 and
0.64, the worst-case Manski bounds are pre ∈ [0.243, 0.563] and post ∈ [0.484, 0.844], so
Δ ∈ **[−7.9pp, +60.1pp]**: the bounds *overlap* and do not sign the effect. Algebra: with equal parse rate
r and the same point estimates, the lower bound on Δ is 1.399r − 1, positive for **r > 0.715**. So raising
the parse rate to ~0.72 would make F1 worst-case-robust. That is a concrete, cheap target and it should
gate the word "committed".

**Good news I can hand you.** I re-ran the delay statistics on the **full universe** in
`empirics/data/fact2_parsed.jsonl` (9,234 originals), and F1 replicates and comes with a clean pre-trend:

| filing year | n (0–60 bd) | mean | median | share ≤ 5 bd |
|---|---|---|---|---|
| 2022 | 1,400 | 8.34 | 7.0 | 0.319 |
| 2023 | 1,530 | 8.48 | 7.0 | 0.357 |
| 2024 | 1,231 | 7.22 | 5.0 | **0.706** |
| 2025 | 0 | — | — | — (parser dead) |

Flat, flat, break. That is a first-stage figure with a visible pre-trend test, and it is far stronger than
the two-window contrast the memo prints. Use it.

**Rule effect vs compliance mechanics.** The right framing is not "the median fell" but "**the deadline
binds**": mass piles at exactly 5 business days and the right tail halves (p90 23 → 11.1). Show the
histogram (`empirics/output/fact1_delay.pdf` already has it) and the bunching mass at exactly 5. Note the
economically careful statement: a compressed *filing* delay does not by itself mean information reaches
the market sooner relative to the *decision* — filers can accumulate faster and cross 5% later. That is a
distinction a theory referee will press on, and F1 alone cannot settle it.

**Sept 30, 2024.** F1's post window is 2024Q3–Q4, so one of its two quarters sits after the 13G retiming.
For a pure delay statistic this is second-order; for anything composition-sensitive it is first-order,
because 13G eligibility loss now routes into a 5-business-day 13D. Report **2024Q2–Q3** as the clean post
window and put Q4 in robustness.

**Replacement text for l.229–232:**

> **F1 (executed):** the five-business-day deadline binds. On the full 2022–2025 universe of SC 13D
> originals, the median disclosure delay is 7.0 business days in 2022 and 2023 and 5.0 in 2024, and the
> share filed within five business days moves 31.9% → 35.7% → 70.6% — flat before the rule, a break at it.
> Delays are measured on a US-federal-holiday business-day calendar; filings whose cover-page event date
> cannot be parsed are reported as a per-quarter parse rate (0.64–0.68 in the 2022–2024 windows) rather
> than dropped silently, and we report worst-case bounds treating all unparsed filings as compliant and as
> non-compliant in turn. At the current parse rate those bounds overlap; raising it above roughly 0.72 —
> the target of the structured-era parser fix — signs the effect under the worst case. The identifying
> picture is the bunching mass at exactly five business days and the halving of the right tail
> (p90 23 → 11.1), not the movement in the median.

### E7. F2 and the calibration table — **MAJOR**

**The parser is broken in a way that invalidates F2 today.** `empirics/parse_13d.py:105-106` uses
`([0-9]{1,2}(?:\.[0-9]+)?)\s*%`, which cannot match a three-digit percentage. I fed it
`"PERCENT OF CLASS REPRESENTED BY AMOUNT IN ROW (11): 100.0%"` and it returned **0.0**. Consistent with
that, the full universe has **347 filings recorded at exactly 0.0%** and — far more alarming — **448
recorded at exactly 2.6%**, which is 7.2% of all parsed values sitting on one number that no genuine 13D
original can take. 22.9% of parsed values are below 5%. Separately, `RE_PERCENT.search` returns the
**first** "PERCENT OF CLASS REPRESENTED BY AMOUNT IN ROW (11)" in the document, which is the first
reporting person's row, not the group aggregate — systematically understating wolf-pack and SPV stakes.
None of this is usable for a bunching test at 5%, which is the very thing F2 promises.

**Comparability.** CDF's median 6.20% / mean 7.68% come from **1,725 screened original 13D events,
2001–2010, derivatives excluded** (`lit_liquidity-premia-empirics.md` §3). The repo's 9.55% raw median is an
*unscreened* 2022–2025 all-filer universe: SPAC sponsors, PIPE investors, founders, post-merger cleanups.
Matching a screened activist moment to an unscreened universe is not a moment match. Replicate CDF's
screens and report the raw/screened pair.

**No model counterpart.** With a unit (or exogenous) stake, "stake at first 13D" is not a moment the model
produces. F2 is motivation and a data-quality exhibit, not calibration. Say so.

### E8. F3 and the CAR interpretation — **MAJOR**

The discipline sentence at l.224–226 is exactly right and should survive verbatim: 13D announcement CARs
are disclosure price impact, and Ben-David et al. is correctly pre-empted. But that does not make F3
atheoretical, and the memo undersells its own model by filing F3 as a "fact".

**What the model says.** In the model the disclosure CAR is the jump from the price conditional on no
disclosure to the price conditional on disclosure — the D = 0 to D = 1 move. A shorter pre-filing window
means less of the activist's presence has been impounded before the filing, so the D = 0 price sits closer
to the prior and **the jump at disclosure is larger**. That is a signed prediction and should be labelled
as one, not smuggled in as a stylized fact.

**The confound the memo does not state.** A shorter window also means a **smaller stake at filing** (CDF:
23% of the final stake is accumulated between trigger and filing). A smaller disclosed stake is weaker news
about intervention intensity and delivers less mechanical price pressure — pushing the jump *down*. The net
sign is ambiguous. F3 is therefore uninformative unless it conditions on stake size.

**Three fixes.** (i) State both forces and the ambiguity. (ii) Test the **intermediate outcome directly** —
does the stake at first 13D fall after the rule? That is a sharper prediction with far fewer confounds, it
is measurable from `pct_of_class` once E7's parser bug is fixed, and it is the missing link that makes the
CAR test interpretable. (iii) Run the CAR comparison within stake deciles.

**Measurement.** The existing 1.6% → 2.6% medians come from a **21-day** CAR window (`nrets` = 21 for 2,264
of 2,285 rows), which straddles the event and therefore contains the run-up — mixing exactly the two
objects H2 exists to separate. F3 must be re-run on [−1, +1]. And see E10f: the file is named `_edate` but
its contents are consistent with filing dates.

### E9. F4 — **MAJOR** (a separate facts-verifier is doing the full number check)

Greenwood & Schor (2009, JFE 92) checks out: **18.1% of activist targets acquired within 12 months**,
against 7.2% for industry-size-return matched firms, 12.6% for non-activist 13D filers and 4.7% for all
small stocks; 21.9% at 18 months; roughly an 11pp lift (`research/lit_activism-empirics.md:59`).

The Boyson figure does not. As the repo records it, via Corum & Levit's citation, the object is
"**70% of bids within 2 years of campaign start**" (`research/lit_theory-to-empirics-templates.md` §2) — a
share of *bids conditional on a bid arriving*, not an unconditional two-year acquisition rate. Printed
beside G&S's 18.1% as a "benchmark" for the same F4 object, it implies an unconditional path from 18% at
12 months to 70% at 24 months, which contradicts G&S's own 21.9% at 18 months. Either relabel it as the
conditional statistic it is, or drop it. Also give it a year and a full cite: Boyson, Gantchev &
Shivdasani, "Activism mergers," *JFE* 126(1), 2017 [memory — verify volume/pages]; the repo's source cites
a 2016 working paper.

Finally, quoting 18.1% without G&S's control rates strips it of meaning. F4's benchmark line should read
"18.1% within 12 months versus 12.6% for non-activist 13D filers and 7.2% for matched firms".

### E10. Overall — would a JF/RFS referee read this as committed empirics?

**No — as a plan.** The tell is that every executable claim shrinks under inspection while every promised
claim is weeks away. A referee reading l.221–330 sees: one fact that is genuinely done (F1, at 188 filings);
one regression on ~1,000 events with 301 post observations and no control group; one statistic that is not
well defined; one hand-collection promise ("weeks-scale", l.294) with a conditioning-on-the-outcome problem
and no power at five quintiles; and a ten-row moment table of which the model can produce perhaps five.
The tone is admirably honest — l.223's discipline statement and l.235's "vet outliers" are the sort of
thing referees like — but tone is not identification.

**What is missing, concretely.**

1. **Sample-construction / attrition table**, pre and post separately: filings → originals → CUSIP →
   CRSP match → common stock (shrcd 10/11) → non-missing Amihud with ≥100 estimation days → final.
   My numbers for the memo's own main spec: 1,381 filings in Feb 5 – Sep 29 2024, 1,161 with a CUSIP,
   ~754 expected at a 65% CRSP match, and **301 actually present** in the existing event-study output.
2. **A validated filer-type classifier**, not "name regex with hand spot-checks" (l.267). Hand-code 150
   at random; report precision and recall; the composition story rests on this variable.
3. **Calendar-time figures**: the quarterly Amihud slope and the quarterly median CAR, 2022–2025, with CIs.
4. **Inference that survives 7 post month-clusters**: cluster by firm (403 repeat firms, max 9 events per
   firm) and handle the time dimension by randomization inference over placebo rule dates, not by a
   month-clustered SE.
5. **Multiplicity discipline**: F1–F4 plus H1–H3 across several windows, quantile regressions, and
   robustness cuts is dozens of tests. Pre-specify a primary set; Romano–Wolf or BH for the rest.
6. **A pre-registration-style box**: the signed prediction, the primary sample, the primary window, the
   primary specification, written before the results — which for a theory paper costs nothing and buys
   a great deal of credibility.
7. **A model-object → empirical-counterpart table.** The moments table is not this.
8. **Power statements** for H1 (see E10c: MDE ≈ 2.1pp per SD, versus an AFS level loading of 0.9pp per SD)
   and H3.

**Minimal credible package for JF/RFS.** Keep three things and execute them properly:

- **F1 as the first stage**, upgraded: full universe, fixed parser, holiday-corrected business days,
  bunching at exactly 5, per-quarter parse rates, Manski bounds. It already replicates on the full
  universe and it has a clean pre-trend. This is the honest headline, and "the deadline bound" is a real
  contribution to a theory paper about disclosure windows.
- **The stake-at-filing test**: does the disclosed stake fall after the rule? Sharper than the CAR, fewer
  confounds, and it is the mechanism that makes any CAR result interpretable. Requires only the E7 parser
  fix and data already on disk.
- **H1 restated** as a before/after with the bindingness dose, calendar-time coefficients, placebo dates,
  and an explicit MDE — reported as either a signed result or a bounded null, whichever the data give.

**Demote or drop.** F3 becomes a diagnostic panel inside H1, not a standalone fact. H2 loses the ratio and
keeps two window-level levels as a secondary table (or, better, becomes the stacked-window DiD of E3, which
is the one genuine DiD available). **H3 should be cut from this paper** and stated as the falsifiable
prediction the theory *offers*, with the design spelled out and no numbers promised: it is a
weeks-to-months hand-collection with a selection problem and no power at the proposed granularity, and
promising it in the same paper as the theory converts a solvable referee problem into a broken promise.
The calibration table splits into "targeted" and "motivating".

One further honesty point on the risk register: l.356–357 says "execute H1/H2 now (~3–4 days of work on
disk-resident data)". Given the parser fixes (E6c, E7a), the event-day realignment (E2a), the dose
construction (E1), the placebo-date inference (E1), and the attrition table, three to four days is optimistic
by a factor of several. Under-promising here costs nothing.

---

## Model-object → empirical-counterpart map

Table rows as printed at l.319–330. "Matchable" means the three-branch model as specified (unit stake, one
blockholder, static, no staged campaign costs, bidder entry p) can produce the object.

| # | Moment (l.) | Model object | Matchable? | Verdict |
|---|---|---|---|---|
| 1 | 13D announcement CAR 6.34%, 75.2% treatment (l.321) | price jump from D=0 to D=1 | **Level: yes. Decomposition: no** | Target the 6.34% level. The treatment/stock-picking/selection split has no model counterpart — the model has no stock-picking channel. Cite as level only. |
| 2 | Run-up ~7% vs jump ~3% (l.322) | — | **No** | A static model with one disclosure decision has no run-up. Motivation only, unless a pre-disclosure trading stage is added. This is also the moment H2 is built on, which is worth noticing. |
| 3 | Stake at first 13D, median 6.2% / mean 7.68% (l.323) | — | **No** | Unit stake. Motivation / data-quality exhibit. |
| 4 | Pre-announcement accumulation 54% of block, 8.5% profit (l.324) | — | **No** | Needs dynamic accumulation and a block size. Motivation. |
| 5 | Liquidity → targeting sign positive, 0.33% → 0.73% IV (l.325) | ∂P(engage)/∂κ | **Sign: yes. Level: no** | The model has no firm cross-section, so the probability level is not produced. Target the sign. |
| 6 | Voice→exit mode shift, −6.9pp on 13D share (l.326) | ∂P(Public)/∂κ vs ∂P(Exit)/∂κ | **Sign: yes. Level: conditional** | The −6.9pp level needs a calibrated signal distribution. Target the sign; report the level as a stretch. |
| 7 | Mean bid premium 36.6% (l.327) | Δ^min conditional on takeover | **Yes** | The cleanest calibration target in the table: it pins the premium wedge (m₀, m₁) or the D7 tender-game primitives. |
| 8 | Activism → premium interaction −13.7% / −5.2pp (l.328) | Δ^min \| D=1 vs Δ^min \| D=0 | **Yes** | The paper's central object and its most valuable target. State which of the two numbers (relative or absolute) is matched — they are not the same moment. |
| 9 | Takeover prob. lift from activism +11pp / +7.7pp (l.329) | bidder entry p | **Yes if p is endogenous; input if not** | If p is a primitive this is a calibration *input*, not a match. Say which. |
| 10 | Campaign costs by stage $1.8M/$2.9M/$5.9M (l.330) | — | **No** | The model has no staged campaign costs. Drop, or move to "not targeted". |

**Summary: 4 rows genuinely targetable (1-level, 7, 8, 9), 2 as signs (5, 6), 4 with no counterpart at all
(2, 3, 4, 10).** As printed, a referee counts ten promises and finds the model delivers four.
Recommended split:

- *Panel A — moments targeted in calibration*: rows 1 (level), 7, 8, 9, with a `model object` column.
- *Panel B — signs the model must reproduce*: rows 5, 6.
- *Panel C — motivating facts the model does not target*: rows 2, 3, 4, 10, with one line saying why
  (static model, unit stake, no staged costs) — which is a *strength* when stated, and a hole when not.

---

## Recommended Section 4 rewrite outline (≤25 lines)

- Open with the discipline paragraph unchanged (l.223–226) — it is the best thing in the section.
- Add one sentence: this section is a *before/after* around a dated rule change; the word DiD is used only
  where a second difference exists (the within-event window contrast, and the bindingness dose).
- **§4.1 First stage — the deadline binds (F1).** Full 2022–2025 universe, holiday-corrected business days,
  bunching at exactly 5, per-quarter parse rates, Manski bounds, the 2022/2023/2024 pre-trend table.
- **§4.2 Sample construction.** Attrition table, pre and post separately, down to the estimation sample.
  Filer-type classifier with a hand-coded validation subsample and reported precision/recall.
- **§4.3 What the model predicts.** Pre-registration-style box: three signed predictions, primary sample,
  primary windows, primary specification, before any result.
- **§4.4 Intermediate outcome — the stake at filing.** Does the disclosed stake fall post-rule? Sharpest
  prediction, fewest confounds, executable on disk data once the percent parser is fixed.
- **§4.5 H1 — the liquidity slope.** Amihud defined as a pre-event [−250,−11] average, log and winsorized,
  with log-cap and turnover throughout. Calendar-time coefficient figure first, the pooled estimate second.
  Triple difference on the bindingness dose. Placebo-date randomization inference. Stated MDE.
- **§4.6 H2 — run-up versus jump.** Stacked-window DiD in levels; three windows anchored on the event date,
  including the crossing→filing segment whose length is the treatment. No ratio statistic.
- **§4.7 Confounds.** The full thirteen-row table of E2, not four items — with the 10 p.m. ET cut-off and
  the Oct-2023 anticipation window given their own paragraphs.
- **§4.8 Calibration.** Three panels: targeted moments, signs, motivating facts, with a `model object`
  column throughout.
- **§4.9 What this design cannot do.** No untreated group; single time-series break; composition changes
  with the treatment; CARs are disclosure price impact only. One honest paragraph beats three defensive ones.
- **Move H3 to a "predictions for future work" subsection** with the design (terciles or quadratic,
  Lind–Mehlum U-test, Schwert −42 base with SDC-convention robustness, cash/stock split as the falsification,
  P(bid|q) reported alongside) and **no promised numbers**.

---

## Data checks performed

All run in-session from the repo root with `.venv/bin/python` against the gitignored `empirics/data/`.
Files present: `fact2_parsed.jsonl` (9,234 rows), `wrds_evtstudy_edate.csv` (2,285 rows), `crsp_daily.csv`
(1.2 GB, not opened).

**1. SC 13D originals per filing year, parse rates** (`fact2_parsed.jsonl`):

| year | n | with event date | rate | with CUSIP | rate | has_xml |
|---|---|---|---|---|---|---|
| 2022 | 2,319 | 1,580 | 0.681 | 1,900 | 0.819 | 0 |
| 2023 | 2,501 | 1,660 | 0.664 | 2,081 | 0.832 | 0 |
| 2024 | 2,184 | 1,398 | 0.640 | 1,855 | 0.849 | 0 |
| 2025 | 2,230 | **0** | **0.000** | 2,134 | 0.957 | 0 |

Confirms `research/empirical_feasibility.md` §1.2: the structured era is entirely lost, and `has_xml` is
false for all 9,234 rows including post-2024-12-18 filings. The memo's "9,234 parsed" (l.262) is a *filing*
count; the event-date sample is 4,638.

**2. Post-rule sample arithmetic.** Post (filed ≥ 2024-02-05): 4,176 filings, 1,235 with an event date,
1,048 with event + CUSIP. The memo's **main spec window (Feb 5 – Sep 29 2024): 1,381 filings, 1,161 with a
CUSIP, ~754 expected at a 65% CRSP match.**

**3. Full-universe replication of F1** (0 ≤ delay ≤ 60 bd, `np.busday_count`): 2022 median 7.0 / 31.9%
within 5 bd (n=1,400); 2023 median 7.0 / 35.7% (n=1,530); 2024 median 5.0 / **70.6%** (n=1,231); 2025 no
data. F1 replicates on the universe and gains a pre-trend.

**4. CAR pre/post** (`wrds_evtstudy_edate.csv`, market model, `nrets` = 21 for 2,264 of 2,285 rows,
`nrets_est` = 220 for 2,111):

| | n | mean | median | p01 | p25 | p75 | p99 | min | max |
|---|---|---|---|---|---|---|---|---|---|
| pre | 1,234 | 0.0379 | **0.0157** | −1.55 | −0.088 | 0.174 | 1.31 | −2.16 | 5.46 |
| post | 1,051 | 0.1277 | **0.0261** | −1.10 | −0.099 | 0.196 | 2.11 | −2.37 | **28.99** |

The memo's "1.6% → 2.6%" (l.235) reproduces exactly — **but on a 21-day window, not [−1,+1]**. The outlier
picture is far worse than "vet outliers" suggests: one post event has a **2,899%** 21-day CAR, two more
exceed 900%, and 4.2% (pre) / 4.9% (post) of events have |CAR| > 100%. Winsorizing at 1/99 still leaves
means of 3.75% vs 8.05% — because the 1/99 trim points are themselves ±130% to ±211%. Only the median is
defensible, and even it is measured on the wrong window. (Some `car` values are NaN, which silently broke
my first t-test — worth a non-missing screen in the harness.)

**5. Pre-trend on the outcome — the finding that matters most.** Median CAR by half-year:

| | 2022H1 | 2022H2 | 2023H1 | 2023H2 | 2024H1 | 2024H2 | 2025H1 | 2025H2 |
|---|---|---|---|---|---|---|---|---|
| n | 277 | 266 | 304 | 326 | 284 | 243 | 296 | 284 |
| median | 0.0438 | 0.0296 | 0.0169 | 0.0036 | **0.0101** | 0.0595 | 0.0280 | 0.0082 |
| mean | 0.0758 | 0.0125 | 0.0907 | −0.0089 | 0.0677 | 0.0935 | 0.0859 | 0.2264 |

**There is no break at 2024-02-05.** 2024H1 — six of whose months are treated — has a median CAR of 1.01%,
*below* 2023H1 (1.69%) and far below 2022H1 (4.38%). The whole pre/post gap comes from 2024H2 (5.95%),
which falls **outside the memo's own main post window** and straddles the 2024-09-30 13G change. Draw the
pre window from 2022 instead of 2023 and the sign flips. This is the single most important thing in this
report: the F3/H1 direction is an artifact of window choice, and a referee with the data will find it.

**6. Cluster and estimation-sample arithmetic** (memo's own windows). Post Feb 5 – Aug 31 2024: **n = 301,
7 month-clusters**, median CAR 2.25%. Pre 2023-01-01 – 2024-02-04: n = 688, 14 month-clusters, median CAR
0.93%. **Implied main-spec estimation sample: 989 events**, before CRSP common-stock screens and before
requiring a valid Amihud. 1,744 unique CUSIPs, 403 firms with more than one event, maximum 9 events per firm.

**7. Percent-of-class regex** (`empirics/parse_13d.py:105`), tested directly:

| input tail | parsed |
|---|---|
| `…ROW (11): 100.0%` | **0.0** |
| `…ROW (11)  100%` | **0.0** |
| `…ROW (11): 6.2%` | 6.2 |
| `…ROW (11)\n 9.49 %` | 9.49 |

Full universe: 6,189 of 9,234 parsed; median 9.55%, mean 17.30%; **22.9% below 5%**; 307 exactly zero;
548 above 50%; 98 above 90%. Most common rounded values: **2.6% appears 448 times** (7.2% of all parsed
values — impossible for genuine 13D originals), 0.0% 347 times, then 5.1/5.0/10.0. `pct_of_class` is not
fit for F2 in its current state.

**8. Event-date provenance.** `wrds_evtstudy_edate.csv` carries 582 rows dated in 2025, but the parser
recovers **zero** 2025 event dates — so `evtdate` cannot be the parsed crossing date. Its year distribution
(24/28/23/25%) tracks the CUSIP-available filing distribution (24/26/23/27%) almost exactly, so the file
holds **filing**-date CARs despite the `_edate` name. `research/empirical_feasibility.md` §2.1 agrees.
Document this before any number is quoted.
