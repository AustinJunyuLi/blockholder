# ADVERSARIAL CHECK — P4 (Feb-2024 matched-control DiD)

**Role:** adversarial verifier (not the proposer). **Target:** runner-up `research/positions/P4_feb2024_did.md` (W2; fallback W13). **Stance:** overclaims until every claim survives contact with the sources. Proposal, cards, and judge reports not edited.

**Sources opened (not trusted from judges):** `CONTEXT.md`; `docs/adr/0003`, `0004`; `.scratch/v4-reposition/spec.md`; `research/competitor_map.md` Part 2–3 (W2, W13); `research/cards/INDEX.md`; P4; `JUDGE_1.md`, `JUDGE_2.md`, `JUDGE_3.md`; then, for every cited claim, the owning card or record: `_institutional_sec_33_11253.md` plus the release extract (`sec_release_33_11253.txt` ll. 196–197, 8716–8740); `trivedi_2026_ssrn.md`; `dass_huang_maharjan_nanda_2020.md`; `zeng_2026_ras.md`; `bebchuk_brav_jackson_jiang_2013_jcl.md`; `greenwood_schor_2009_jfe.md`; `author_proposal_outline_2026.md`; `polk_buchheit_riley_stone_2024_jfrc.md`; `bishop_fos_jiang_partnoy_2026.md`; `johnson_swem_2021_jfe.md`; `gantchev_2013_jfe.md`; `becht_franks_grant_wagner_2017_rfs.md`; `empirical_feasibility.md`; `lit_institutional-facts.md` §1.3; `quality_reports/fixes/D7_takeover_game_microfound.tex` (Prop. `d7:lambda`, Rem. `d7:compstat`, Lemma `d7:entry`); `proposal/sections/empirics.tex` ll. 7–11, 143–146; `research/draft_v2_digest.md` §6.

---

## 1. Whitespace claims (W2 primary; W13 fallback)

For each occupancy claim: the card that would refute it was opened; verdict is whether that card occupies the cell.

| Claim (P4) | Card that would refute | Opened | Verdict | Amendment |
|---|---|---|---|---|
| **W2** rated “CLEAR on the cell; hard on execution” | Any paper occupying control outcome × Feb-2024 window CHANGE × DiD with a control group | `competitor_map.md` W2 header + (d); summary table row W2 | **SURVIVES** — wording is the map header verbatim | None on rating |
| Trivedi: same anchor, has a control group, **wrong object** (`takeover`/`premium`/`stake` = 0, §6) | `trivedi_2026_ssrn.md` §6 | §6 full-text greps: `takeover` 0, `premium` 0, `toehold` 0, `stake` 0, `activis*` 0, `block*` 0; outcomes = lag, compliance share, Δspread, ΔAmihud, forward return | **SURVIVES** | None |
| Polk et al.: same margin, pre-rule, no control group, “baseline projection” (p. 516) | `polk_buchheit_riley_stone_2024_jfrc.md` Q3, §2, §6 | Q3 p. 516 verbatim; sample ends 2022; no DiD, no post-rule estimate; `takeover`/`premium`/`bidder` = 0 | **SURVIVES** | None |
| Author proposal: “no untreated group” (`empirics.tex:7-11`); bid hazard “Confidence intervals only” (`:143-146`) | `author_proposal_outline_2026.md` Q1, P3; `empirics.tex` | Q1 matches ll. 7–11; table ll. 143–146: “Confidence intervals only” | **SURVIVES** | None |
| Bishop et al.: asserts the comparative static (printed p. 36), never estimates; HSR not 13D | `bishop_fos_jiang_partnoy_2026.md` R11, Q11 | Q11 printed p. 36 verbatim; R11 ASSERTED; no 2024-02-05 date; no window-change estimate | **SURVIVES** | None |
| Greenwood–Schor own the *level*, not the rule-induced *change* | `greenwood_schor_2009_jfe.md` R7; map W14 | Table 6 p. 372 is a matched frequency (18.1% vs 7.2%), no disclosure-rule treatment | **SURVIVES** | None |
| **Fallback W13** (campaign success × window CHANGE; CLEAR, power-weak) | Johnson–Swem; Gantchev; Becht; Trivedi | JS: success object, `disclos*` = 0 in article/OA, window only fn. 13 background. Gantchev: ten-day window “Appendix A and never used”; 31.55% / 10.52% are demand shares, not a window CHANGE. Becht: threshold *level* cross-country; IA “Table 18” is a threshold–outcome null, not a window change. Trivedi: no campaign object | **SURVIVES** — map rating “CLEAR on occupancy, weak on power” | Prefer map’s “power-limited” if quoting the summary table |

**Whitespace summary.** No opened card occupies W2 or W13. Execution warnings (13G, power, BBJJ, Zeng screen) are design constraints, not occupancy refutations.

---

## 2. Claim-by-claim factual table

| Claim (P4) | Source opened | Verdict | Amendment if any |
|---|---|---|---|
| Initial 13D: ten **calendar** days → five **business** days, effective 2024-02-05 | `_institutional_sec_33_11253.md` §1, pp. 1, 10; §2 | **CONFIRMED** | None |
| Threshold and 13D/13G *margins* untouched (as the position’s objects) | Same card §1: 5% trigger unchanged; 13G deadlines bind 2024-09-30 (listed by P4 as a contaminant, not a studied margin) | **CONFIRMED** as a position claim | None |
| Fact 1: within-5-bd share 35.7%→75.6%; median delay 7.0→5.0 bd | `empirical_feasibility.md` §1.1 | **CONFIRMED** | None |
| Trivedi DiD **+0.348, p=0.007** on the compliance share | `trivedi_2026_ssrn.md` R2 (Table 2 p. 11): +0.348, SE 0.130, t = 2.69, p = 0.007 | **CONFIRMED** on coefficient and p | None |
| Trivedi cited as “a working paper reports the window bit” | Map-mandated wording; card §7 | **CONFIRMED** | None |
| Parenthetical **“(t>3)”** attached to Trivedi R2 | Card R2 + p. 11 caveat: t = 2.69; “does **not** clear the Harvey, Liu, and Zhu (2016) hurdle of three” | **WRONG / MISCITED** | **REPAIRABLE** (see §3e). Drop `(t>3)`; write `t = 2.69, does not clear the HLZ t>3 hurdle` |
| SEC Table 2 p. 181: **~20%** non-corporate-action | Institutional card §4.3: 3,067 / 15,724 = 20% (2011–2021, extractable transaction histories) | **CONFIRMED** as an SEC-table fact | Do not treat 20% of the **9,234** 2022–25 originals as a measured count — that is an extrapolation (Item 4 / non-CA coding is “not started”, feasibility §2.3) |
| SEC Table 3 p. 189: **~3%** of non-CA campaigns materially constrained, **≈7/year** | Institutional card §4.4 col. (3) `<90%`: **3%**, **7**/year, **78** campaigns. Col. (2) `<100%` is 20% / 42 per year / **463** campaigns — different object | **CONFIRMED** against col. (3) | Name the column: “<90% of stake by the amended deadline (Table 3 col. 3)” |
| EDGAR cut-off 5:30pm→10pm ET, same day (card §3, pp. 9, 11) | Institutional card §3 | **CONFIRMED** | None |
| Anticipation: proposed **2022-03-10**, adopted **2023-10-10** | Release extract n. 5: Commission **Feb. 10, 2022** [87 FR 13846 **(Mar. 10, 2022)**]; reopened Apr. 28, 2023; adopted Oct. 2023. Author-proposal card uses 2022-03-10 | **CONFIRMED** as the FR publication date; **loose** as “proposed” if that means the Commission vote | Optional: “proposed Feb. 10, 2022 (FR Mar. 10)” |
| T+1 **2024-05-28** | Not in 33-11253. `empirical_feasibility.md` §5.2(c); `lit_institutional-facts.md` | **CONFIRMED** on repo secondaries; no dedicated T+1 card | None for the date; see checklist on *identification* inside Feb–May |
| XML **2024-12-18** | Release extract pp. 164–165: structured-data **not required until December 18, 2024**; voluntary from Dec. 18, **2023**. Institutional card §1 table lists only the 2023 voluntary row | **CONFIRMED** against the release extract (card table incomplete) | Cite the extract / p. 164, not only the card’s voluntary-13G row |
| 13G deadlines **2024-09-30** | Institutional card §1 p. 165 | **CONFIRMED** | None |
| Base hazard **≈17–18%** (Greenwood–Schor p. 372, Table 6) | `greenwood_schor_2009_jfe.md` R7: **18.1%** of activist targets **acquired** within 12 months (CRSP delisting), vs 7.2% matched; **no bid count**; no SE on the 11 pp gap | **MISCITED (object)** | “18.1% acquired-within-12-months (Table 6), not bid hazard.” Bid (SC TO-T/DEFM14A/8-K) is a weakly larger set |
| Dass premium DiD died on **<19** treated acquirers, fn. 27 | `dass_huang_maharjan_nanda_2020.md` §2, fn. 27 printed p. 23: **19** is the stock-payment DiD; premium/CAR “even smaller”. JCF 2024 not held | **CONFIRMED** — P4 uses the verifier-corrected form | None |
| Premium SD **≈0.38** | Dass card: mean 0.268, SD **0.383**, N = 2,837 | **CONFIRMED** | None |
| Zeng 1–13 calendar-day screen non-neutral under a 5-bd rule (Q4, p. 1312 fn. 13) | `zeng_2026_ras.md` Q4 + Q3; verifier: kept range is 1–13 days **and** same-day filers dropped; sample ends 2022; Release 33-11253 never mentioned | **CONFIRMED** | None — P4’s “no delay screen, count in business days” is the map’s prescribed mitigation |
| BBJJ p. 28 (Q20); pill moderator pp. 28, 31 | `bebchuk_brav_jackson_jiang_2013_jcl.md` Q20 p. 28 verbatim; R18 pp. 28, 31; R16 Table 10 p. 29; both channels ASSERTED, not estimated | **CONFIRMED** as a stated channel | See §3b — listing ≠ identification |
| Author-proposal R1 quadratic cost **PROVED** | Card R1; verifier OK | **CONFIRMED** | None |
| D7 **λ = 1 − q(1−γ)ψ** **PROVED** | `D7_takeover_game_microfound.tex` Prop. `d7:lambda` | **CONFIRMED** | None |
| Shorter window ⇒ smaller stake ⇒ weaker λ_app ⇒ lower entry (stake-bargaining dominates certification), label **PROVED-conditional** | Proposal R5 (conditional), R6 (corner PROVED), R11 **ASSERTED** unsigned; D7 Rem. `d7:compstat`(iii) is a **jump** at 1−τ_c, not a slope; Lemma `d7:entry` is state-blind | **OVERCLAIMS** the D7/entry fold | See §5 |
| Sample **9,234** parsed originals 2022–25; post doubles after parser fix | Feasibility §1.2–1.3: 9,234; post with event date **1,235** (Feb–Dec 2024); 2025 event-parse **0%** | **CONFIRMED** | None |
| On-disk CRSP 2021–25 | Feasibility §1.2 | **CONFIRMED** | None |
| **~300 campaigns/side** | 20% × event+CUSIP ≈ 0.20×2,849 pre / 0.20×1,048 post ≈ 570 / 210; SEC non-CA flow ≈ 279/year (3,067 / 11) | **PLAUSIBLE** as a 1-year SEC-flow planning number; **optimistic** for the current post-parser state (~210 non-CA with event+CUSIP) | Pre-register *n* from the manifest after the non-CA screen exists |
| Matched-DiD MDE **≈9–10 pp** (1 yr/side), **≈6–7 pp** pooled | Two-sample difference in proportions, p₀ ≈ 0.175, 80% power: n = 300 ⇒ MDE ≈ 8.7 pp; n = 600 ⇒ ≈ 6.1 pp | **CONFIRMED** as order-of-magnitude (author arithmetic, not a card) | Commit the formula with *n* |
| Premium MDE **≈15 pp** at ~50/side, SD ≈ 0.38 | 1.96 × 0.38 × √(2/50) ≈ **14.9 pp** (CI half-width); 80%-power MDE ≈ 2.80 × that ≈ **21 pp** | **MISLEADING** as “MDE” | Call it a 2-SE width, or write ≈21 pp; P4 already marks the leg descriptive |
| Proposal dose-leg MDE 17–31 pp on ~3 exposed bids | Author-proposal card P3 / `empirics.tex:143-146` | **CONFIRMED** | None |
| Placebo ≥500 dates 2021–2023 | Specified in P4; proposal workplan uses ≥500; feasibility silent | **Specified, not run** | None as a position claim |
| draft_v2 §6 bid-hazard prediction | `draft_v2_digest.md` §6 item (5): “13D targets: lower bid hazard, higher conditional premia” | **CONFIRMED** as a recognisable descendant | None |

---

## 3. Required defect dispositions

### (a) 13G is structurally unusable as a control group (`trivedi_2026_ssrn.md` §7)

**Disposition: SURVIVES.**

Card §7 (not merely §5): for a **control outcome**, “13G is structurally unusable as a control: 13G filers disclaim control intent by definition… selection into 13D vs 13G is itself plausibly responsive to the window change.” P4 rejects 13G and substitutes 3:1 matched **never-13D** firms — the card’s own prescribed alternative. Trivedi’s 13G DiD remains a **timing first-stage** resource only (with the t-stat repair in (e)).

§4’s phrase “matched **never-targeted** firms” is sloppy against §5’s “never-13D”. In M&A English, never-targeted often means never received a bid, which would zero the control outcome by construction. **Amendment:** say never-13D everywhere.

### (b) BBJJ second-channel confound (p. 28) — listed? does the bound/DiD address it?

**Disposition: LISTED; NOT addressed by the bounded null; only partly addressed by the DiD.**

- **Listed?** Yes. P4 §5(iv): Q20 p. 28; pill split pp. 28, 31 “where pill data allow”; else signed bias (“defenses push toward a decline — an increase would be conservative”).
- **Bounded null does *not* address it.** Table 3 col. 3 caps the **accumulation** tail (~3% of campaigns still buying ≥10% of the stake after the new deadline). BBJJ’s channel — faster disclosure alerts **incumbents** — binds on **every** flagged campaign, constrained or not (JUDGE_3, re-confirmed). P4 §5’s “population ATE … ≤~3 pp” and §9’s “aggregate footprint on control outcomes is small” read as a bound on the **total** reduced-form effect. That overclaims.
- **DiD does not difference the channel out.** Never-13D firms are not alerted in either period. The DiD coefficient is the reduced-form rule effect on 13D targets (accumulation + defense + selection). The pill split would separate channels; it is **“only specified”** (P4 §5 last line). `empirical_feasibility.md` has **zero** pill / SharkRepellent / FactSet hits; BBJJ’s moderator was FactSet SharkRepellent (card §2). Spec bars new Activist Insight / LSEG pulls.
- **Signed-bias only protects a *positive* finding.** Accumulation (P4’s own sign) and defenses both predict a **decline**. An increase would be conservative; a decline — the predicted sign — is unidentified across channels. (Map W2’s “opposite sign” is the wrong description of Q20 on bid hazard; both channels have the same sign.)

**Amendment:** (i) bound = accumulation-channel footprint only; (ii) DiD = reduced-form (accumulation + defense + selection); (iii) pill split remains specified-only unless a free pill source is named.

### (c) Power arithmetic (SEC Table 3; Dass fn. 27)

**Disposition: SURVIVES.** Numbers match the opened sources.

| Number | P4 | Opened | Match |
|---|---|---|---|
| ~3% of non-CA campaigns materially constrained | §3, §5, §9 | Institutional §4.4 col. (3): **3%**, 78 campaigns | Yes |
| ≈7/year | §3, §9 | Same column: **7** avg campaigns/year | Yes |
| Dass premium DiD **<19** treated acquirers | §5 | Card fn. 27 p. 23: 19 = stock-payment count; premium **even smaller** | Yes |

Do not recycle the 463-campaign figure (that is col. 2, the `<100%` set).

### (d) Zeng’s 1–13 calendar-day screen

**Disposition: SURVIVES.** Q4 / fn. 13 p. 1312 confirmed verbatim; the screen is non-neutral once the filing cluster moves left under five business days. P4 imposes no delay screen and counts business days — the map W2 sweep’s prescribed handling.

### (e) Judges’ P4 finding: “(t>3)” vs Trivedi R2 (t = 2.69)

**Disposition: CONFIRMED. REPAIRABLE, not FATAL.**

Card R2: t = **2.69**, p = 0.007. The author’s own sentence (p. 11) is that the secondary effect “does **not** clear” the HLZ hurdle of three (and that hurdle “governs the cross-sectional return-factor test of Section 8 rather than a policy treatment effect”). P4’s `(t>3)` reads as a claim about this statistic. It is false.

**Minimal amended wording:** delete `(t>3)`; keep the map’s “a working paper reports the window bit” and, if the number is kept, `+0.348 (p = 0.007; t = 2.69; does not clear HLZ t>3)`. Optional: attach the card’s sampling-frame warning (333 filings, universe unstated).

Not fatal: first-stage parenthetical, not the W2 occupancy or the estimand.

---

## 4. Referee checklist vs P4 vs `empirical_feasibility.md`

CONTEXT.md list: control group or bounded null; confound list (EDGAR cut-off, anticipation, T+1); power/MDE; placebo; pre-trend; parser validation.

| Item | Present in P4? | Consistent with data on disk? | Asserted but not specified? |
|---|---|---|---|
| **Control group** | Yes — 3:1 never-13D on size, Amihud, SIC2, quarter | Size/Amihud/SIC2 from on-disk CRSP (feasibility §2.1). Never-13D needs a lookback; the parsed 13D universe is 2022–25 only | **Lookback window, caliper, replacement, exact-vs-coarsened SIC2** unnamed |
| **Bounded null** | Yes — Table 3 ⇒ ATE ≤~3 pp if every constrained campaign “dies” | SEC tables are in the fact sheet; no new data | Extreme bound (constrained bid rate 1→0). Honest only for the **accumulation** channel (see §3b) |
| **EDGAR cut-off** | Yes, dated, same-day | Institutional card §3 | None |
| **Anticipation** | Yes — pre ends at adoption (2023-10-10) | Matches proposal/feasibility practice | Proposal date convention (Feb 10 vs Mar 10) only |
| **T+1** | Yes — main post **Feb–May 2024**, later months as extensions | Feasibility §5.2(c): T+1 is **2024-05-28**, i.e. **inside** a Feb–May window if May is kept | Whether “Feb–May” ends **before** 2024-05-28 is unnamed |
| **Other dated contaminants** | 13G 2024-09-30; XML 2024-12-18 | Both real | None |
| **Power/MDE** | Yes — 9–10 / 6–7 pp; premium descriptive | Inputs partly verified (GS 18.1% acquired; SEC tail; Dass SD) | Formula not committed; *n* ≈ 300 is planning; premium “MDE” is a 2-SE width |
| **Placebo** | ≥500 dates 2021–2023 | No placebo harness on disk (Fact-2 code uncommitted, feasibility §5.7) | **Specified, not implemented** |
| **Pre-trend** | Quarterly 2022–23 event study; failure **blocks causal language** | Needs outcome match (feasibility §2.3: 1–3 weeks, **not on disk**) | Outcome-coding rules (which 8-K items?) unnamed — feasibility names 1.01/2.01 |
| **Parser validation** | 30-filing audit, per-quarter parse rates, `numpy busday` asserts | Feasibility §5.5 recommends exactly the 30-filing audit; 2025 parse is 0% until the XML-attachment fix (0.5–1 day) | **Specified**; the fix is gating |
| **Universal proxy** (meetings after 2022-08-31) | **Absent** | Feasibility §5.2(d) puts it **inside** a 2022–23 pre | Omitted confound (not on the CONTEXT named list; on the feasibility list) |
| **Pill split** | Specified-only | No pill file on the feasibility manifest | Data source unnamed |

**Feasibility alignment (what is on disk).** Fact 1, 9,234-row universe, CRSP 2021–25, CUSIP on 86%, event dates on ~50% (0% in 2025) — all as P4 states. Bid outcomes and offer prices are **not** on disk (feasibility §2.3 / §3). Non-CA / Item 4 coding is **not started**. That is consistent with P4’s week-2–5 outcome-matching plan and with “only specified: pill split, causal premium reading.” It is **not** consistent with treating the December clean result as already runnable without that engineering.

---

## 5. Theory leg vs the D7 record

P4’s chain: shorter window ⇒ smaller filing stake ⇒ weaker λ_app ⇒ lower entry “where stake–bargaining dominates certification.” Label: **ESTIMATED + PROVED-conditional.** Tools: one-shot accumulation/entry algebra + MCS. Reuses proposal R1 (quadratic cost) and D7’s λ.

| Piece | Record | Honesty |
|---|---|---|
| C(x; d) = (λ_L/2) x²/d | Proposal R1 **PROVED** | Honest |
| Smaller *d* ⇒ smaller post-threshold increment | R6 **PROVED** at the constrained corner; R5 **PROVED-conditional** (single-crossing on an unrestricted *b*) | “One stated condition” is true for the *interior* stake response; name it |
| Smaller stake ⇒ weaker λ_app | D7 Rem. `d7:compstat`(iii): as α crosses **1−τ_c from below**, λ **jumps up** by q(1−γ)(1−ψ). Within a regime, λ does **not** depend on α. Typical 6–10% 13D stakes make 1−τ_c bind only if τ_c is a 90%+ squeeze-out/blocking threshold | Continuous “weaker λ_app” is **not** a D7 theorem. The jump is PROVED; a slope is the proposal’s β(x) reduced form, not D7 |
| Weaker λ_app ⇒ lower **entry** | D7 Lemma `d7:entry`: fringe-raid probability q = H(φ) is **state-blind** — engagement does not attract or deter fringe entry through profit. P4’s “entry” is the proposal’s strategic-bidder hazard. Proposal R11: d log h/de = ε_cert − ε_det, **no sign imposed**, label **ASSERTED** | Folding the entry sign into **PROVED-conditional** overclaims D7 and upgrades R11 |

**Does not overclaim the λ *formula*.** P4 does not re-derive the tender game, does not claim the measured-premium reversal (`prop:d7-afs`), and does not hide the “one stated condition.” The overclaim is the **composition** and the continuous λ(α) wording.

**Amendment:** Split labels. **PROVED:** R1 cost; D7 λ = 1−q(1−γ)ψ; λ jump at 1−τ_c. **PROVED-conditional:** interior stake response (R5). **ASSERTED-conditional:** entry sign (ε_det > ε_cert / “stake-bargaining dominates certification”). Do not write as if D7 signs bidder entry.

---

## 6. Master table (condensed)

| # | Claim | Source opened | Verdict | Amendment |
|---|---|---|---|---|
| 1 | W2 CLEAR / hard on execution | map W2 | SURVIVES | — |
| 2 | W13 CLEAR, power-weak | map W13; JS, Gantchev, Becht, Trivedi | SURVIVES | — |
| 3 | Trivedi wrong object | trivedi §6 | SURVIVES | — |
| 4 | 13G unusable for a control outcome | trivedi §7 | SURVIVES | never-targeted → never-13D |
| 5 | SEC ~3% / ≈7 per year | institutional §4.4 col. 3 | CONFIRMED | Name the column |
| 6 | Dass <19 | dass fn. 27 | CONFIRMED | — |
| 7 | Zeng 1–13d screen | zeng Q4 | CONFIRMED; mitigated | — |
| 8 | BBJJ p. 28 listed; bound/DiD “address” it | bbjj Q20; P4 §5, §9 | CONFIRMED listed; **bound does not address**; DiD is reduced-form | Scope the bound; pill data not on disk |
| 9 | Trivedi (t>3) | trivedi R2 | **WRONG** | t = 2.69; does not clear HLZ t>3 |
| 10 | GS 17–18% bid hazard | greenwood_schor R7 | **MISCITED object** | 18.1% *acquired* |
| 11 | PROVED-conditional full chain | author R1/R5/R11 + D7 | **PARTIAL** | Entry ASSERTED; λ(α) is a jump |
| 12 | Checklist complete on data in hand | P4 §5 vs feasibility | **Present**; several items specified-not-built | Lookback, match, 8-K items, pill source, T+1 end-date |
| 13 | XML 2024-12-18 | release extract p. 164 | CONFIRMED | Card table is incomplete |

---

## 7. Final verdict

**SURVIVES WITH AMENDMENTS:**

1. **Trivedi R2:** delete `(t>3)`; write `t = 2.69, does not clear the HLZ t>3 hurdle` (keep “a working paper reports the window bit”).
2. **Greenwood–Schor:** 18.1% is **acquired** within 12 months (Table 6), not a bid hazard.
3. **Bounded null / BBJJ:** Table 3 bounds the **accumulation** tail only. The DiD is reduced-form (accumulation + defense + selection). The pill split is specified-only; pill data are not on the feasibility manifest. Do not call ≤~3 pp the bound on the **aggregate** control-outcome footprint.
4. **Theory labels:** **PROVED** for quadratic cost and D7’s λ (including the jump at 1−τ_c); **PROVED-conditional** for the interior stake response; **ASSERTED-conditional** for the entry sign (ε_det vs ε_cert). Do not attribute a continuous λ(α) slope or an entry sign to D7.
5. **Wording:** “never-targeted” → **never-13D**.

**Not fatal.** W2/W13 occupancy, 13G rejection, Zeng handling, SEC/Dass power numbers, Fact 1, and the checklist *as a list of named items* survive. Defects are wording, object slips, and honesty about what the bound and D7 actually cover.

**Could not check, and why.** (i) Pill / SharkRepellent files on this machine — `empirics/data/` is gitignored and feasibility mentions none. (ii) Trivedi’s self-hosted pre-registration (card UNCHECKED; no registry URL). (iii) Dass JCF 2024 typeset version (not held; fn. 27 is the June 2020 WP). (iv) T+1 2024-05-28 from a primary SEC/FINRA PDF (repo secondaries only). (v) Executed 30-filing audit and `busday` asserts (specified, not run).
