# ADVERSARIAL CHECK — P2 (rule-keyed partition; W3 + W11 extension)

**Role:** adversarial verifier (not the proposer). **Target:** tournament winner `research/positions/P2_partition_infodesign.md`. **Stance:** the proposal overclaims until every claim survives contact with the sources. **Method:** every whitespace claim named a would-be refuter card, which was opened; every factual claim opened at the cited card page/section; the three judge defects re-run against the owning card *and* the CCKV extract; the proof-route labels checked against `research/draft_v2_digest.md` and `quality_reports/fixes/D8_GE_dominance_MCS.tex`. No proposal, card, or judge report edited. No commit.

**Sources opened:** `CONTEXT.md`; `docs/adr/0003`, `0004`; `.scratch/v4-reposition/spec.md`; `research/competitor_map.md` (Part 2 hazards, Part 3 W3/W11); `research/cards/INDEX.md`; `research/positions/P2_partition_infodesign.md`; `JUDGE_1.md`, `JUDGE_2.md`, `JUDGE_3.md`; cards `kyle_vila_1991_rand.md`, `zeng_2026_ras.md`, `cetemen_cisternas_kolb_viswanathan_2026_jf.md`, `maug_1998_jf.md`, `_institutional_sec_33_11253.md`, `corum_levit_2019_jfe_published.md`, `ordonez_calafi_bernhardt_2022_jfqa.md`, `corum_2025_ssrn.md`, `back_et_al_2018_ecta.md`, `collin_dufresne_fos_2016_ecta.md`, `collin_dufresne_fos_2015_jf.md`, `burkart_lee_2022_rfs.md`, `edmans_2009_jf.md`, `levit_malenko_maug_2024_jf.md`, `bebchuk_brav_jackson_jiang_2013_jcl.md`, `author_proposal_outline_2026.md`; `research/empirical_feasibility.md`; `research/draft_v2_digest.md`; `quality_reports/fixes/D7_takeover_game_microfound.tex`, `D8_GE_dominance_MCS.tex`, `d8_ge_dominance_check.json`; `research/txt_extracts/cckv_2026_jf.txt` (Thm 1, fn. 16).

---

## 1. Whitespace dispositions (W3 primary; W11 extension)

For each W3/W11 claim: the card that would refute it, what that card actually says, and whether P2's wording survives.

| Claim (P2) | Card that would refute | Opened | Verdict | Amendment |
|---|---|---|---|---|
| **W3** rated "CLEAR (with a named boundary)" | Any card occupying a *rule-keyed* on-path flagged/pooled split (stake trigger **and** date) | `competitor_map.md` W3 (lines 173–189); rating table line 394 | **SURVIVES** — rating quoted verbatim | None on rating |
| Kyle–Vila **boundary**: claim is "legally imposed, rule-keyed partition", never "the market never learns" / "no one has a pooled/revealed split" | `kyle_vila_1991_rand.md` — mixing equilibria already split on path (pp. 62–63, 69–70); fn. 1 p. 54 disclaims disclosure | Card §7 item 1; Q1 p. 54 n. 1; map W3(d) required sentence | **SURVIVES** — P2 §6 uses the map's sentence almost verbatim: "imposed by a legal trigger and a legal deadline, present in every parameter configuration" | None |
| Zeng **boundary**: pooled = "pooled for the price-setting market"; leak cited (p. 1310 run-up on trigger date) | `zeng_2026_ras.md` — insiders detect before the flag; run-up begins on TD | Q5 p. 1310 verbatim ("the price run-up begins precisely on the trigger date"); §7 item 1 (wording constraint); R1 2.8% pp. 1309–1310 | **SURVIVES** — P2 §3 and §6 use the required phrase and cite Q5 | None |
| CCKV: one permanently pooled state; does not occupy W3 | `cetemen_cisternas_kolb_viswanathan_2026_jf.md` — no flagged event; game interpreted as inside the window | §6(a); Q4 p. 11; fn. 16 p. 15; extract confirms "No agent…" is **absent** from the paper | **SURVIVES as substance**; **citation defect** (see §3(i)) | Cite fn. 16 p. 15 and/or Q4 p. 11; do not quote the card gloss as paper text at p. 11 |
| Corum–Levit: flagged state **off path**, belief μ(α)=1 (p. 14) | `corum_levit_2019_jfe_published.md` | Card §5 / §6: α\*=ᾱ; α>ᾱ off path; p. 14; fn. 27 p. 11 "assumes y=1" | **SURVIVES** — card supports the disposal. Notation μ(α)=1 is the **card's** rendering of the off-path belief; the paper's own words at fn. 27 p. 11 are "assumes y=1" | Optional: add fn. 27 p. 11 as the paper quote |
| OCB: crossing reveals instantly; activist never crosses (p. 2836) | `ordonez_calafi_bernhardt_2022_jfqa.md` | Q1 p. 2836 verbatim; `window` = 0 hits | **SURVIVES** | None |
| Corum (2025): purpose partition **proved irrelevant** (p. 19) | `corum_2025_ssrn.md` | Q5 p. 19 verbatim | **SURVIVES** | None |
| Back et al.: window collapsed into σ²T, a rescaling not a partition (p. 1453) | `back_et_al_2018_ecta.md` | Q7 p. 1453 verbatim | **SURVIVES** | None |
| CDF (2016): insider's presence common knowledge (p. 1464) | `collin_dufresne_fos_2016_ecta.md` | Q8 p. 1464 verbatim; conclusion future-work list | **SURVIVES** | None |
| Maug: disclosure assumed away by timing (p. 73); 13D is neither case | `maug_1998_jf.md` | Q5 p. 73 verbatim ("Hence…"); `disclosure` = 1 hit in the paper | **SURVIVES** | None |
| Burkart–Lee: pre-/post-disclosure interaction left to future work (p. 1891) | `burkart_lee_2022_rfs.md` | Q1 p. 1891 verbatim | **SURVIVES** | None |
| Author proposal: window-CHANGE dose DiD; **no partition object** | `author_proposal_outline_2026.md` | §2 "no equilibrium partition"; §6 Q4/Q5; map Part 1 row 11 | **SURVIVES** | None |
| CDF (2015): names the "learn an insider is present" gap | `collin_dufresne_fos_2015_jf.md` (map W3 nearest-row) | JF pp. 1557–58 in INDEX §4.11 / card | **SURVIVES** — P2 does not claim this inference as novel | None |
| **Standing risk:** Chabakauri et al. (2022), uncarded, live W3 refuter | Map sweep (d); `zeng_2026_ras.md` pp. 1306–1307 | Named correctly; **not read** | **SURVIVES as a named risk**, not as a disposal. Does **not** currently refute W3 | Card before draft_v3 (P2 already says this) |
| **W11** "NARROW — OCB own the architecture on the threshold"; extension only | `ordonez_calafi_bernhardt_2022_jfqa.md` Prop. 4 p. 2847; map W11(d) | Q6 p. 2847 verbatim; map: "the window, unlike the level, lets the blockholder keep buying after crossing" | **SURVIVES** — claimed as extension only; map clause used | None |

**Part 2 hazards P2 must not occupy.** Checked against P2's own drops and wordings:

| Hazard (map Part 2) | Does P2 claim it as new? | Verdict |
|---|---|---|
| 1. Liquidity hump (Maug Prop. 7 / Edmans Prop. 3 / LMM Prop. 7) | No — §8 drops R1 as headline; names the three owners | **SURVIVES** |
| 2. σ²T isomorphism (Back p. 1453) | No — partition vs rescaling | **SURVIVES** |
| 3. Order-flow inference about an intervention (CCKV Thm 1) | Novelty sits on the **partition**, not the inference. §9's Thm 1 sentence is a **mischaracterization** (see §3(ii)), not a novelty claim | **SURVIVES** on occupancy; citation fails |
| 4. Random deadline (Caldentey–Stacchetti via CDF 2016 p. 1450) | Not claimed | **SURVIVES** |

**Whitespace summary.** W3 occupancy **survives** once both named boundaries are respected — and P2 respects them in the claim sentences. W11 as extension **survives**. The CCKV *quotation* does not survive as written; the *cell* does.

---

## 2. Factual claims (papers, rule, repo)

| Claim (P2) | Source opened | Verdict | Amendment |
|---|---|---|---|
| Rule 13d-1(a) as amended: crossing 5% starts a clock; flag within **five business days** (`_institutional_sec_33_11253.md` §1, pp. 1, 10) | Institutional card §1 | **CONFIRMED** | None |
| 13G compliance **2024-09-30** | Institutional card §1 p. 165 | **CONFIRMED** | None |
| XML mandate **2024-12-18** | Feasibility §5.2; `lit_institutional-facts.md` §1. Institutional card §1 states only **voluntary** 13G XML from **2023-12-18** (pp. 164–165) | **CONFIRMED** via feasibility / institutional-facts; **not** in the institutional-card table as a mandate date | Prefer feasibility §5.2 or institutional-facts as the cite |
| EDGAR cut-off same date as the deadline change | Institutional card §3 pp. 9, 11 | **CONFIRMED** (P2 lists it; does not quote the 5:30→10 p.m. numbers) | None |
| Amihud **six months pre-trigger** ("SEC convention") | Institutional card §4.5 pp. 224–225 n. 817 | **CONFIRMED** | None |
| Maug Q5 p. 73: pre-trade publicity kills liquidity; post-trade filing "do not affect F's trading strategy"; 13D is neither | `maug_1998_jf.md` Q5, §6 | **CONFIRMED** — printed connective is "**Hence**", not "Therefore" (already fixed on the card) | None |
| Zeng: run-up begins "precisely on the trigger date" (card §8, Q5, p. 1310) | `zeng_2026_ras.md` Q5 | **CONFIRMED** verbatim | None |
| Zeng 13D run-up **+2.8%** TD→FD | R1, pp. 1309–1310 | **CONFIRMED** (no SE printed) | None |
| Zeng IA.2 size split — insignificant, opposite sign (card §7.2) | Card §7 item 2 / R13: *slightly more pronounced in larger firms, difference not statistically significant*; IA table **not in file** | **CONFIRMED** as the card's body-text gloss; **UNCHECKED** against IA.2 itself | Keep the card's wording; do not treat IA.2 as read |
| Zeng 1–13 calendar-day screen | Q4, fn. 13 p. 1312 | **CONFIRMED** | None |
| CCKV: "No agent in the model ever learns that a blockholder holds a block", **p. 11** | Card §6(a); Q4 p. 11; fn. 16 p. 15; `cckv_2026_jf.txt` grep: string **0 hits** | **MISCITED** (card gloss quoted as paper text; wrong page) | See §3(i) |
| CCKV Theorem 1 (p. 17) "warns order-flow inference need not be monotone" | Card R3/Q8; extract pp. 736–760: Thm 1 = existence + **predictability** E[θᴸ\|F₀] ≠ 0; "From the result, **predictability** is a generic property" | **WRONG** as a characterization of Thm 1 | See §3(ii) |
| Corum–Levit μ(α)=1 (p. 14) | Card §5, §6; fn. 27 p. 11 | **CONFIRMED** against the card; μ(α)=1 is card notation | Optional: quote fn. 27 |
| OCB never crosses (p. 2836); Prop. 4 (p. 2847) | Q1, Q6 | **CONFIRMED** | None |
| Corum purpose threshold irrelevant (p. 19) | Q5 | **CONFIRMED** | None |
| Back σ²T / "isomorphic" (p. 1453) | Q7 | **CONFIRMED** | None |
| CDF (2016) common knowledge (p. 1464) | Q8 | **CONFIRMED** | None |
| CDF (2015) run-up **~3%** | R1 / Q9, JF p. 1563: "about 3% from **60 days** to one day prior" | **CONFIRMED** as the JF number; P2's empirical window is CAR[TD−1, FD−1], not CDF's 60-day run-up | When using 3% as a power anchor, name CDF's window |
| Burkart–Lee p. 1891 future-work hand-off | Q1 | **CONFIRMED** | None |
| Maug Prop. 7 (p. 83) liquidity hump | R10 | **CONFIRMED** — object = initial shareholders' wealth | None |
| Edmans Prop. 3 (p. 2496) | R6 / Q1 | **CONFIRMED** — object = π_X and investment, α fixed | None |
| LMM Prop. 7 liquidity/depth non-monotone | Card R15, printed p. 31 | **CONFIRMED** (P2 gives no page; map/card: p. 31) | Add printed p. 31 if cited in draft_v3 |
| BBJJ faster defences (p. 28) | Q20 p. 28 | **CONFIRMED** — ASSERTED, not estimated | None |
| Sample **~2,849 pre / ~1,048 post**; 2025 parser fix ~1 day, doubles post leg (feasibility §1.2–1.3) | `empirical_feasibility.md` §1.2–1.3: 2,849 / 1,048; fix est. **0.5–1 day**; "roughly doubles the usable post window" | **CONFIRMED** | None |
| Window-CAR SD ≈ **10–15%**; MDE ≈ **0.8 pp** pre / **1.5–2 pp** post × Amihud (**feasibility §5.1**) | Feasibility has **no §5.1** and **no MDE content**. §5 is "Risks and handling". N ≈ 2,800 / 1,000–2,000 can be read off §1.3 | **WRONG** as a citation; MDE arithmetic is **P2's own** and **UNCHECKED** | See §3(iii) |
| Occupied magnitudes CDF ~3%; Zeng 2.8% | CDF R1; Zeng R1 | **CONFIRMED** (see window caveat on CDF) | None |
| Digest §6: fixed-cutoff promotion "**days, not weeks**" | `draft_v2_digest.md` §6 last sentence | **CONFIRMED** verbatim | None |
| D = 1{q = +1} is an ad-hoc one-unit buy, not the rule | Digest §5.3 | **CONFIRMED** | None |
| Baseline collapses Hold | Digest: `fig:cutoff-structure` "Hold collapsed" | **CONFIRMED** | None |
| Existence via Brouwer (`prop:existence`) | Digest §4 / proved-outright list | **CONFIRMED** | None |
| Disclosed-branch κ-invariance proved | Digest: `app:proof-disclosed-invariance` | **CONFIRMED** | None |
| `prop:disclosure-attenuation` is currently a **proof sketch** at fixed cutoffs | Digest line 49 | **CONFIRMED** — P2's "Expected honesty label: PROVED" is a **promotion target**, not a claim that the theorem is already proved | Keep "expected" |
| D7: λ = 1 − q(1−γ)ψ | `D7_takeover_game_microfound.tex` Prop. d7:lambda | **CONFIRMED** | None |
| 13Gs descriptive only (Zeng R1); no 13G control (map W2) | Zeng R1 is a **price** comparison, not a control-group instruction. Map W2 / Trivedi §7 kill 13G as a control for a **control outcome** | **CONFIRMED** on the design choice; the Zeng-R1 pin is loose | Cite map W2 / Trivedi §7 for the no-control clause |
| Placebo: pseudo-triggers at TD − 63 trading days | No card or feasibility section prescribes 63 days | **UNCHECKED** as a design choice (not a paper fact) | None required for a proposal |
| "13Gs descriptive only (Zeng card R1)" as a *reason* 13G prices are a valid descriptive benchmark | Zeng R1: 13G run-up +0.9% / +1.7% | **CONFIRMED** that Zeng reports 13G price reactions; not a licence to treat 13G as a control | Already handled above |

---

## 3. Judge-reported defects — dispositions

### (i) CCKV sentence at "p. 11"

**Judges:** the string is the card's §6(a) gloss; paper support is fn. 16 p. 15; p. 11 carries Q4.

**Disposition: CONFIRMED. REPAIRABLE, not FATAL to W3.**

- Grep of `research/txt_extracts/cckv_2026_jf.txt`: **"No agent in the model ever learns that a blockholder holds a block" = 0 hits.**
- Card §6(a) (line 101) prints that sentence as the card's own summary, immediately after citing fn. 16.
- Paper text that *does* exist: fn. 16, p. 15 — "All these expressions hold on and off the equilibrium path, as an activist's trades are hidden from others." And Q4, p. 11 — "Our model is then best interpreted as taking place in such a pre-disclosure window…"
- Substance of the W3 disposal (one permanently pooled state; crossing outside the model) is **true**.

**Minimal amended wording.** Replace the quoted sentence and "p. 11" with:

> CCKV — a single permanently pooled state: activist trades "are hidden from others" on and off path (fn. 16, p. 15); the whole game is "best interpreted as taking place in such a pre-disclosure window" (p. 11).

### (ii) "CCKV Theorem 1 warns order-flow inference need not be monotone"

**Judges (esp. Judge 2):** Thm 1 is a **predictability** result, not a monotonicity result.

**Disposition: CONFIRMED. REPAIRABLE, not FATAL to the weakest-point warning.**

Opened in the extract (printed p. 17) and the card (R3, Q8):

> Theorem 1. … (i) If ρ > 0, the leader sells on average … E[θL \| F0] < 0; (ii) If ρ < 0, the leader buys on average … E[θL \| F0] > 0. … From the result, **predictability** is a generic property of the leader's trading.

The only "monotone" hit near this result in the extract is firm value **monotone decreasing in ρ** (Prop. A.6) — a different object. Card §7 does say Figure 3 shows \|E[θᴸ]\| **monotone increasing in σ** (Thm 2(iii) neighbourhood), which is the *opposite* of a "need not be monotone" warning: liquidity's effect on their object *is* monotone.

The claim Thm 1 supports in P2 §9 is that pooled-cell inference is not a free, well-behaved Kyle object. That warning **is** in Thm 1 if stated as predictability / breakdown of E[θ\|F]=0. It is **not** a monotonicity theorem.

**Minimal amended wording** (P2 §9):

> CCKV Theorem 1 (p. 17) shows informed order flow need not be unpredictable: E[θᴸ \| F₀] ≠ 0 once a second correlated activist is present. Any pooled-cell inference that assumes conditionally mean-zero order flow is exposed (card §7).

Do **not** cite Thm 1 for non-monotonicity. If a liquidity-sign warning is wanted, cite Thm 2(iii) / Fig. 3 (more noise → **more** |E[θᴸ]|), which is a different — and for κ, live — hazard (map Part 2 item 21 / INDEX §4.21).

### (iii) MDE numbers cited to "feasibility §5.1"

**Judge 3:** no §5.1; the document has no MDE content.

**Disposition: CONFIRMED. REPAIRABLE, not FATAL to the power sketch.**

- `empirical_feasibility.md` sections are 1–5. **There is no §5.1.** Section 5 is a numbered risk list (short post window, bundled confounds, selection, Ben-David, parse noise, access, reproducibility).
- Full-text search: **MDE does not appear** in the file.
- What *is* in the file: N = 2,849 pre / 1,048 post (§1.3); parser 0.5–1 day (§1.2). Those inputs are real. The SD ≈ 10–15% and the 0.8 / 1.5–2 pp MDE figures are **P2's own arithmetic**, not re-derived here.

**Minimal amended wording:**

> Window-CAR SD ≈ 10–15% (author sketch); N ≈ 2,800 pre (`empirical_feasibility.md` §1.3) ⇒ MDE ≈ 0.8 pp on a standardized slope, inside occupied magnitudes (CDF ~3% over (t−60, t−1), JF p. 1563; Zeng 2.8% TD→FD, pp. 1309–1310). Post × Amihud (N ≈ 1,000–2,000) MDE ≈ 1.5–2 pp (same sketch). Formal MDE in the spec.

Not fatal: the design does not stand or fall on a cited MDE table that does not exist; the N and the occupied magnitudes do.

---

## 4. Main result — proof route, duplication, honesty labels

**Statement (P2 §4).** Rule (τ, T) imposes a two-cell partition at the control-decision node; E[premium] decomposes; flagged cell κ-invariant; pooled cell carries the entire κ-derivative; tightening either key shifts mass onto the flagged cell and attenuates liquidity-sensitivity.

**Duplication against the cards.** No competitor card states this theorem.

| Nearest card result | Why it is not this theorem |
|---|---|
| Back et al. p. 1453 | Window = σ²T **rescaling**; no flagged/pooled split; no premium |
| CCKV Thm 1 p. 17 | Predictability of E[θᴸ] inside a **permanently pooled** game; no flag |
| OCB Prop. 4 p. 2847 | Welfare ranking over a **threshold cap**; activist never crosses |
| Corum–Levit Prop. 5 / p. 14 | Flagged cell **off path**; ᾱ fused with liquidity |
| Maug Prop. 7 p. 83 | Hump in **initial shareholder wealth**; disclosure assumed away |
| Kyle–Vila mixing (pp. 62–63, 69–70) | Endogenous, un-keyed split; disclosure disclaimed (p. 54 n. 1) |
| Draft_v2 `prop:disclosure-attenuation` | **Own prior**: fixed-cutoff **proof sketch**, D = 1{q=+1}, not (τ, T) |

The result is a **promotion and re-keying** of draft_v2's R2, not a restatement of a competitor proposition. That is allowed (ADR-0004: recognizable descendant). It is **not** already PROVED as a rule-keyed partition theorem.

**Label vs what the records actually deliver.**

| P2 expected label | What the digest / D8 actually deliver | Consistent? |
|---|---|---|
| **PROVED** for (i)–(iv) **at fixed cutoffs** | (i) `prop:existence` PROVED (Brouwer). (ii) disclosed-branch invariance PROVED. (iii) decomposition is an accounting identity. (iv) attenuation is still a **proof sketch** (digest line 49); §6 says the missing cross-partial is "one line" / "**days, not weeks**" | **Yes, as an expected label.** P2 says "Expected honesty label", not that (iv) is already proved. Do not ship "PROVED" in draft_v3 until the sketch is upgraded |
| **Region-certified PROVED in GE** | D8's `thm:d8-region` certifies **Δ^min single-peakedness** (the hump), not the attenuation cross-partial. Digest §6 tells the author to **reuse** `lem:d8-cutoff`'s inversion-free bound for a *parallel* region theorem on the cross-partial. `d8_ge_dominance_check.json` certifies the hump interval (e.g. [0.3, 0.85] under the exact-Bift check), plus a trough counterexample at σ_ξ = 0.60 | **Yes, if read as "D8-type", not "D8 already proves attenuation".** P2's wording ("via D8-type bounds—no global sign claimed") matches. The GE attenuation region is **not yet certified** |
| **NUMERICAL off-region** | D8 `prop:d8-counter` shows a global GE sign is false for the hump; digest warns against chasing a global attenuation sign | **Yes** — honest parallel, not a delivered off-region grid for attenuation |

**Interior-crossing condition.** Named in P2 §4 as the biggest technical risk; digest confirms baseline **Hold collapsed**. The partition-as-information-structure vs positive cell-mass distinction is correctly drawn. Not a source defect.

**Mechanical-headline risk** (P2 §9; all three judges). Source-consistent: once the flagged cell is κ-invariant, mass-shifting attenuates by construction at fixed cutoffs. That is a **content** risk, not a citation failure.

---

## 5. Master claim table (condensed)

| # | Claim | Source | Verdict | Amendment |
|---|---|---|---|---|
| 1 | W3 CLEAR with named boundary | map W3 | **SURVIVES** | — |
| 2 | Kyle–Vila rule-keyed wording | kyle_vila §7 / map W3(d) | **SURVIVES** | — |
| 3 | Zeng "pooled for the price-setting market" + p. 1310 | zeng Q5 / §7.1 | **SURVIVES** | — |
| 4 | W11 NARROW, extension, OCB Prop. 4 p. 2847 | ocb Q6; map W11 | **SURVIVES** | — |
| 5 | Nearest-row disposals (CL, OCB, Corum, Back, CDF, Maug, BL, author proposal) | owning cards | **SURVIVES** | Optional fn. 27 on CL |
| 6 | Chabakauri live uncarded refuter | map sweep (d); zeng pp. 1306–07 | **SURVIVES** as risk | Card before draft_v3 |
| 7 | 13d-1(a) / 5 bd / 2024-02-05 | institutional §1 | **CONFIRMED** | — |
| 8 | Maug p. 73 | maug Q5 | **CONFIRMED** | — |
| 9 | Sample 2,849 / 1,048; parser doubles post | feasibility §1.2–1.3 | **CONFIRMED** | — |
| 10 | CDF ~3%; Zeng 2.8% | cdf R1; zeng R1 | **CONFIRMED** | Name CDF's 60-day window |
| 11 | CCKV "No agent…" p. 11 | card §6(a); extract 0 hits | **MISCITED** | fn. 16 p. 15 + Q4 p. 11 |
| 12 | CCKV Thm 1 = non-monotone inference | Thm 1 extract p. 17 | **WRONG** | Predictability wording |
| 13 | MDE via feasibility §5.1 | feasibility (no §5.1, no MDE) | **WRONG** cite | Own sketch; cite §1.3 for N |
| 14 | Proof route / expected labels | digest §6; D8 record | **CONSISTENT** as expected labels | Do not claim D8 already certifies attenuation |
| 15 | D7 λ formula | D7 Prop. d7:lambda | **CONFIRMED** | — |
| 16 | Hump owners (Maug / Edmans / LMM) | owning cards | **CONFIRMED** | LMM page = printed p. 31 |
| 17 | BBJJ p. 28 | bbjj Q20 | **CONFIRMED** | — |
| 18 | Window-CAR SD 10–15%; MDE 0.8 / 1.5–2 pp | no source | **UNCHECKED** | Spec |
| 19 | Zeng IA.2 coefficients | IA not in file | **UNCHECKED** | Body gloss only |
| 20 | Placebo TD−63 | no source | **UNCHECKED** | Design choice |

---

## 6. Final verdict

**SURVIVES WITH AMENDMENTS:**

1. **CCKV quotation.** Do not attribute "No agent in the model ever learns that a blockholder holds a block" to p. 11 as paper text. Cite fn. 16, p. 15 ("trades are hidden from others") and/or Q4, p. 11 (pre-disclosure-window interpretation). W3 disposal unchanged.
2. **CCKV Theorem 1.** Replace "order-flow inference need not be monotone" with the theorem's actual content: E[θᴸ \| F₀] ≠ 0 (predictability; Kyle mean-zero fails). If a liquidity-sign warning is wanted, cite Theorem 2(iii) / Figure 3, not Theorem 1.
3. **MDE citation.** Drop "(feasibility §5.1)". Keep N from `empirical_feasibility.md` §1.3; label the 0.8 / 1.5–2 pp figures as an author sketch; put a formal MDE in the spec.

**Not fatal.** W3 occupancy survives both named boundaries (Kyle–Vila rule-keyed wording; Zeng "pooled for the price-setting market" + p. 1310). W11 as a NARROW extension survives. The proof-route labels match what the digest says can be earned (fixed-cutoff promotion in days; D8-**type** region theorem; no global GE sign) and do not duplicate a competitor-card theorem. The three defects are wording and citation, not cell occupancy.

**Could not check in this pass.** (i) Independent recomputation of the MDE arithmetic (no formula in the repo). (ii) Zeng IA Table IA.2 coefficients (Internet Appendix not held; body gloss only). (iii) Chabakauri et al. (2022) — uncarded; named correctly as a live W3/W8 risk. (iv) Placebo at TD−63 as a paper fact (it is a design choice). (v) Corum–Levit printed p. 14 image for the exact μ(α)=1 symbols (card-confirmed; paper extract garbled).
