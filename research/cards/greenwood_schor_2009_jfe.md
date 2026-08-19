# Greenwood & Schor (2009) — "Investor activism and takeovers"

**Venue / status:** Journal of Financial Economics 92(3), 362–375, 2009 (published version; the PDF carries the "ARTICLE IN PRESS" running head of the corrected proof but shows the final journal pagination 362–375, received 7 Feb 2008, accepted 12 May 2008, online 13 March 2009)
**Full text from:** `research/txt_extracts/greenwood_schor_2009.pdf` (14 pp) + `greenwood_schor_2009.txt` · **Reader:** opus · **Read:** full text, 14 pages (all pages incl. Appendix A and references)
**Page numbering used:** printed JFE page numbers (362–375). PDF page *n* = printed page *n*+361.
**Type:** empirical **Role for us:** competitor (this is the paper that owns "activism returns = takeover premium")

*Note on transcription:* the PDF's `fi`/`fl` ligatures and its unmapped minus glyph are rendered here as plain `fi`, `fl`, `-`. Otherwise quotes are character-for-character.

## 1. Question

What accounts for the large positive abnormal returns around hedge-fund activist 13D filings? Greenwood & Schor test one alternative to the standard "activists improve the firm as a going concern" story: that the returns are the market pricing in an *expected takeover*, and that activists earn them by putting targets into play. They also ask whether activists *cause* takeovers or merely pick firms that were already likely to be acquired — and whether returns to activism should therefore co-move with market-wide takeover interest.

## 2. Model / data and method

- **Source / sample:** all Schedule 13D and DFAN14A filings merged from SEC EDGAR, 1993Q3–2006Q3 (13 years). Initial sample 20,771 filings, from a universe of 173,078 13Ds in the period. Closed-end funds and firms not on CRSP at initial filing are dropped. To keep the sample to *portfolio* investors (not corporate crossholdings) filers are cross-referenced against the list of managers that have ever filed a 13F. Several hundred boilerplate Gabelli "engage management" events are excluded (70 Gabelli events survive) (pp. 364, 364 n.3).
- **Final N:** **980 activist events**, 811 unique target–activist pairs; **784 events by 139 unique hedge funds**, **196 events by 38 non-hedge funds** (Table 1 Panel A, p. 365). Events by year run from 10 (1994) to 153 (2005) and 137 (2006).
- **Unit:** activist–target event, classified into 9 non-exclusive demand categories from the 13D "purpose of transaction" section plus attached exhibits (pp. 365–366; full definitions Appendix A, p. 375).
- **Target characteristics (Table 1 Panel C, p. 365):** activist AUM $6,793m (HF $1,775m, non-HF $24,200m); market value of stake in target $63.7m; **stake = 10.47% of target shares outstanding** (HF 9.83%, non-HF 12.97%); **mean size decile 2.82**; **3.69 analysts covering the target**; market-to-book 1.49; target 24-month return net of industry −15.12%.
- **Design / identification: event study with a factor-mimicking matched portfolio, plus a matched-sample comparison of takeover frequency.** Abnormal return = target return − return on a portfolio whose weights are the target's own estimated HML/SMB/market loadings, estimated over 100 daily returns in [t−110, t−10] (daily) or 24 monthly returns in [t−25, t−1] (monthly) — Eqs. (1)–(3), p. 366. No DiD, no instrument, no structural model. The causal claim rests on (i) an industry × size × prior-return matched control sample, (ii) a second control of *non-activist* 13D filings, (iii) all small CRSP stocks, and (iv) a time-series "shock" narrative from the July–August 2007 credit crunch.
- **Outcome coding:** outcomes read off subsequent 13D filings, communications and newswires, capped at 18 months after the initial filing; takeover identified from CRSP delisting code first digit 2 (Mergers) or 3 (Exchanges) within 18 months (p. 368).
- **Credit-crisis test (Section 4, pp. 373–374):** 16 activists with ≥10 incidents and ≥1 incident in 2005–06; their top-10 13F positions as of end-June 2007 = **144 target companies**; abnormal returns vs. 125 value-weighted Daniel–Grinblatt–Titman–Wermers (1997) size × book-to-market × momentum characteristic portfolios.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | Full-sample announcement CAR over the [−10, +5] day window is 3.61% (t = 6.2); filing-date cumulative 2.41% (t = 4.5); +1 day 3.22% (t = 6.1). (The text on p. 366 rounds this to "approximately 3.5% over the 15-day event window".) | ESTIMATED | p. 367, Table 2 Panel A, "All events" |
| R2 | Full-sample cumulative monthly abnormal return to +18 months is 10.26% (t = 3.4); +12 months 7.78% (t = 2.9) | ESTIMATED | p. 367, Table 2 Panel B |
| R3 | **26.1% of events end in acquisition within 18 months** (Table 2 header row; the paper never states this row's denominator — see the verifier note under R3 below); the share varies sharply by demand type — asset sale 35.7%, block merger 78.1%, strategic alternatives 31.0%, financing/bankruptcy 26.7%, engage management 23.7%, capital structure 20.9%, corporate strategy 20.8%, proxy contest 18.2%, **corporate governance only 15.7%** | ESTIMATED (frequencies, no SE printed) | p. 367, Table 2 header row "% Acquired" |
| R4 | **CAR conditional on outcome — the paper's core comparison.** Targets **acquired** within 18 months (226 events): [−10,+5] daily CAR **5.72% (t = 4.9)**; filing date 4.14% (t = 3.6). Targets that **remain independent**, all: [−10,+5] CAR **2.36% (t = 3.0)** — "about half" | ESTIMATED | pp. 368, 369, Table 4 Panel A |
| R5 | **Long-run returns are entirely a takeover phenomenon.** +18-month cumulative monthly abnormal return: acquired **25.85% (t = 7.9)**; remain independent, all **2.85% (t = 0.6)**; no news 0.00% (t = 0.0); board/resignations −5.62% (t = −0.7); spinoff −3.41% (t = −0.1); share repurchase 29.97% (t = 0.8); activist cuts stake <5% −2.83% (t = −0.2) | ESTIMATED | p. 369, Table 4 Panel B |
| R6 | Among independent targets, only two short-window CARs by outcome are significant — spinoff 6.40% (t = 4.5) and "no news" 2.51% (t = 2.9); board/resignations 1.34% (t = 0.8), share repurchase 1.36% (t = 0.5) and "activist reduces stake <5%" 4.75% (t = 1.2) are not. (*Corrected by verifier: the card previously called spinoff "the only significant" while itself printing t = 2.9 for "no news".*) | ESTIMATED | p. 369, Table 4 Panel A |
| R7 | **Activism raises takeover probability by ~11 percentage points.** Within 12 months of the first 13D: 18.1% of activist targets acquired vs. 7.2% in the industry–size–prior-return matched sample (11 pp gap); vs. 12.6% for non-activist 13D targets; vs. 4.7% for all small CRSP stocks. Within 18 months: 21.9% vs. 9.1% vs. 16.1% vs. 7.2%. Delisting overall: 22.6% (12m) / 27.5% (18m) for activist targets vs. 10.6% / 14.3% matched | ESTIMATED (frequencies; no SE or test statistic printed for the difference) | p. 372, Table 6 |
| R8 | 11 pp × a 30% takeover premium ≈ 3.3% announcement return, "commensurate with what we observe in the data" | ASSERTED (explicitly a "back-of-the-envelope calculation"; the 30% premium is imported from Cremers, Nair & John 2007, not estimated here) | p. 372 |
| R9 | Outcome counts within 18 months (non-exclusive; unique in parentheses): no news 379 (379); **merger or asset sale completed 178 (178)**; merger or asset sale announced 48 (25); merger called off or bid increased 12 (8); spinoff 7 (2); activist takes over target 7 (0); target hires IB or begins auction 14 (5); board seats granted to activist 96 (69); resignation of CEO/CFO/Chairman 25 (5); removal of poison pill 15 (10); proxy defeated 14 (10); shares repurchased/special dividend 23 (9); greenmail 4 (3); activist cuts position below 5% 35 (31); financing/bankruptcy agreement 17 (10) | ESTIMATED (counts) | p. 368, Table 3 |
| R10 | Operating outcomes for **non-acquired** targets, year before vs. year after filing: leverage +0.408 (t = 2.69); capital expenditures −0.144 (t = −4.11) — capex/PP&E falls from 36.5% to 22.1%; dividends/earnings +0.019 (t = 1.31); ΔA/A −1 +0.079 (t = 0.59); ΔS/S −1 −0.203 (t = −1.06); ROA −0.001 (t = −0.15); operating ROA +0.010 (t = 0.70) | ESTIMATED | p. 371, Table 5 left column |
| R11 | **None of these operating changes correlates with long-run returns** except ROA: correlations with 18-month abnormal return — leverage ρ = −0.031 (p = 0.58); capex −0.053 (0.34); dividends/earnings −0.067 (0.25); ΔA/A −1 0.022 (0.67); ΔS/S −1 0.051 (0.24); **ROA 0.165 (p = 0.00)**; operating ROA 0.018 (0.74) | ESTIMATED | p. 371, Table 5 right column |
| R12 | Activist portfolios underperform when takeover interest collapses. Equal-weighted CAR: pre-crisis (Jun 1–Jul 24 2007) −0.21% (t = −0.25); Chrysler/Boots week (Jul 25–31) **−1.01% (t = −2.51)**, raw CR −4.71% (t = −11.30); Home Depot week (Aug 25–29) −0.40% (t = −1.20); extended crisis (Jul 25–Aug 29) **−2.04% (t = −2.72)**. Value-weighted: −1.13% (t = −3.39) and −2.97% (t = −4.32) | ESTIMATED | p. 374, Table 7 |
| R13 | Announcement returns by demand type: asset sale [−10,+5] 6.83% (t = 5.7); engage management 4.18% (t = 5.0); proxy contest 4.56% (t = 2.8); block merger 5.91% (t = 2.4); corporate governance 2.30% (t = 2.1); capital structure 1.68% (t = 1.0); corporate strategy −2.32% (t = −0.5); strategic alternatives 1.73% (t = 0.8) | ESTIMATED | p. 367, Table 2 Panel A |

**No takeover-premium estimate is produced in this paper.** The 30% premium in R8 is borrowed. There is no bid-level analysis, no premium regression, and no bidder-entry count.

**Verifier note on R3 — "the share acquired" is three different numbers inside this one paper (added by verifier).** Table 2's header row prints **26.1%** with no stated denominator (26.1% × 980 ≈ 256). Table 4's acquired column is built from **226 events** "for which an acquisition was announced or completed within 18 months" (p. 368) = 23.1% of 980. Table 6, using CRSP delisting codes over the same 18 months, gives **21.9%**. The paper never reconciles the three. Quote 26.1% only with the Table 2 attribution attached; for anything load-bearing, prefer the 226 events (news-coded, the basis of R4/R5) or 21.9% (delisting-coded, the basis of R7), and say which. This matters directly for the Klein & Zur card's "the share acquired is a contested number" argument — it is contested *within* Greenwood & Schor, not only across papers.

## 4. Institutional facts used

- **Threshold margin + window margin, both stated as one sentence:** "13Ds are filed with the SEC within 10 days of an entity attaining 5% or greater share in any class of a company's securities. The filing documents the size of the purchase and summarizes the investors' intentions." (p. 364).
- **The 13D "purpose of transaction" section is the disclosure of *purpose*, not merely of stake:** "Every Schedule 13D filing includes a 'purpose of transaction' section, in which the filer discloses any plans or proposals that could relate to or result in a significant change at the company" (p. 364 — *corrected by verifier from p. 365*). Since 2000 activists began attaching letters to management as exhibits (p. 364).
- **The 13D/13G partition is named explicitly:** "If the filer has no activist intentions, the SEC allows for the filing of a Schedule 13G (instead of a 13D), which indicates that the large shareholder is a passive investor." (p. 365, and repeated in n.5).
- **The window is used as a *measurement* fact:** pre-filing drift is attributed to the 10-business-day window (p. 366) — see Q3. This is the closest any of the three activism classics comes to treating the window margin as economics.
- **Amended 13D:** "Any subsequent change in holdings or intention is then reported in an amended 13D filing." (p. 365).
- **The paper's own statement of the identity our premium wedge sits inside (added by verifier):** "Thus, the market rationally bids up the price of the target stock in anticipation of a takeover premium." (p. 372) — the sentence immediately before the back-of-the-envelope. Announcement return = Δ Pr(takeover) × premium is not our reconstruction; it is theirs, stated in words on the same page where the premium is imported as a constant.
- **Falling below 5% ends the obligation:** the Table 4 outcome "reduces stake to <5%" is defined as the activist reducing its stake below 5% "thereby ending its 13D filing requirements" (p. 369).
- **DFAN14A:** definitive proxy statements filed by non-management; a proxy fight can start with <5%, though the sample mean stake is 10.8% "implying that these activists usually show up on both filings" (p. 364).
- Data sources: EDGAR, CRSP (delisting codes/dates), Compustat (item-level definitions in Table 5, p. 371), CDA/Spectrum 13F holdings, CISDM hedge-fund database for the HF/non-HF split (pp. 364–366).

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- The conditioning is the whole contribution and it is executed cleanly: the same event study, split only by realised outcome, produces 25.85% (t = 7.9) vs. 2.85% (t = 0.6) at 18 months. That gap does the persuading without any modelling.
- Explicitly addresses the survivorship/selection problem that plagues the operating-performance literature: acquired firms leave Compustat, so accounting studies mechanically condition on the *un*successful subsample (p. 363).
- Three nested control groups for the takeover-frequency claim (matched sample, non-activist 13D filers, all small stocks), so the 11 pp is not resting on one match.
- The 2007 credit-crunch test is a genuinely separate identification channel: a shock to *acquirer financing*, not to activists, moving activist portfolio value.
- Appendix A gives the full demand taxonomy with sample shares — replicable coding.
- **They do adduce *qualitative* evidence on bidder entry, twice (added by verifier).** Target selection: "The activist Robert Chapman, for example, seeks out companies that are 'digestible' in the sense that they are easy to market to bidders as potential takeover targets" (p. 363, n.2). And the buy side: Thomas H. Lee, quoted in a 2007 speech, "I'd like to thank my friends Carl Icahn, Nelson Peltz, Jana Partners, Third Point … for teeing up deals because … many times [activist targets] are being driven into some form of auction" (p. 372, n.7). No bidder is *counted* anywhere — but the auction mechanism is named, sourced and used as support, so "bidder entry is absent" is true only of the measurement, not of the argument.

**Weaknesses / open flanks:**
- **Conditioning on a realised outcome is not identification.** Table 4 splits on an event that happens *after* the announcement return is measured. It shows the market was right on average, not that activism caused the takeover. The authors are aware and lean on Table 6 instead, but Table 6 is a matched frequency comparison with no standard error, no covariate balance table, and no formal test of the 11 pp difference.
- **The 11 pp is a raw difference, unlabelled by significance.** Nothing in Table 6 carries a t-statistic or confidence interval. R7 is the load-bearing causal number and it is printed bare.
- Selection on unobservables is conceded in the text but only argued away ("there is no way to fully rule out the importance of unobserved characteristics", p. 372).
- **No takeover premium is measured.** The premium enters only as an imported 30% in a back-of-the-envelope (p. 372). Bidder entry, number of bidders, deal terms, and hostile vs. friendly are all absent.
- The matched portfolio is factor-loading-based, not matched-firm-based, because Compustat coverage is incomplete (p. 366 and n.6); loadings are estimated on 100 days and held fixed.
- The 2007 credit-crisis test has 144 stocks, 16 funds, a handful of weeks, and overlapping event windows — the authors themselves flag the value/momentum confound (p. 373 and n.10).
- No liquidity measure anywhere. Target illiquidity is proxied only by size decile (2.82) and analyst coverage (3.69) as descriptive statistics; it is never a right-hand-side variable, never interacted, never an outcome.
- Outcome coding relies on newswire search, and the authors flag that small targets generate fewer hits — so "no news" (379 events, 39%) is partly a search-intensity artifact (p. 368).

## 6. What they do NOT do (scope boundary)

- **Object: they measure announcement returns and long-run abnormal returns, not the takeover premium.** The premium is imported, never estimated. Bidder entry is never *counted* — but note (added by verifier) that it is *argued*: the "digestible… easy to market to bidders" target-selection story (p. 363, n.2) and the Thomas H. Lee auction quote (p. 372, n.7) are offered as support, and one Table 3 outcome row is "target hires IB or begins auction" (14 events, 5 unique). The whitespace is a *measured* bidder-entry margin, not an unnoticed one.
- **Margin: neither margin of the disclosure rule is a treatment.** The 5% threshold and the 10-day window are recited as data-construction facts (p. 364) and, once, as an explanation for pre-filing drift (p. 366). No filing deadline is varied, no cross-country threshold contrast, no policy change. The 13D/13G choice is described (p. 365) but never exploited.
- **Identification: event study + matched frequencies only.** No DiD, no IV, no structural estimation, no theory. The word "cause" appears in a question the paper poses rather than answers: "we try to shed light on the question of whether the activist investor causes the takeover or is simply effective at picking a stock that was likely to be taken over in the first place." (p. 368).
- **They explicitly decline the acquirer-side welfare question:** "An important question, which we do not answer here, is whether the shareholder activism associated with takeovers creates long-term value for acquiring company shareholders." (p. 374). They then name the two competing readings — real synergies vs. Roll (1986)-style overpayment — and leave both open: "Given enough data on the future performance of the takeovers in our sample, it should be straightforward to distinguish between these possibilities." (p. 374).
- **Liquidity is never studied.** It appears once as a *motive* (Q4 below: exiting via a merger avoids price pressure) and never again. No Amihud-type measure, no turnover, no depth, no interaction with outcome.
- **Their own normative conclusion, which the card should not restate as ours (added by verifier):** "One implication of our work is that the scope for hedge fund activism to have pervasive effects on corporate governance is limited… it follows that the activists are less interested in making corporate governance changes that might improve the firm but leave it independent." (p. 374). The control outcome crowding out the governance channel is already in print as their reading.
- Hostile vs. friendly is deliberately not coded: "we avoid classifying events as either hostile or friendly because potentially friendly investments may become hostile when management resists activist demands." (pp. 365–366).

## 7. Implications for our position

**What this paper occupies:** object = announcement CAR and 18-month abnormal return, conditioned on a realised control outcome; margin = **none** (the disclosure rule is a data source, not a treatment); identification = event study plus a matched-frequency comparison. It is a *competitor* only on the object, and only on the reduced-form association side.

**How it constrains us (the hard constraint):**
1. **The control outcome is the right dependent object, and this paper proves the market thinks so.** 26.1% of events end in acquisition; the acquired subsample earns 5.72% on announcement and 25.85% over 18 months while the independent subsample earns 2.85% (t = 0.6). Any model of blockholder engagement whose payoff object is an operating improvement is arguing against R5. Our broadened **control outcome** (bidder entry, premium, campaign success) is the object the data already picks out.
2. **The premium wedge is exactly the quantity Greenwood & Schor need and do not have.** Their bridge from the 11 pp takeover-probability increase to the 3.3% announcement return multiplies by an *imported, constant* 30% premium (p. 372, Q7). Our m₁ − m₀ is that multiplicand made endogenous. This is a clean statement of what a theory of the premium wedge buys: it replaces an assumed constant with an object that moves with liquidity and with the disclosure partition. The paper hands us the arithmetic identity — announcement return ≈ Δ Pr(takeover) × premium — and leaves the second factor undefended.
3. **Liquidity enters their story only through the activist's exit motive, and they state it in our language.** Q4 (p. 363) says a merger is doubly beneficial because it avoids "the price pressure associated with an exit in the public markets". That is exit-versus-voice with an explicit market-microstructure cost — the κ channel — but as a one-sentence aside, never measured.

**The whitespace this leaves:**
- **Margin is completely open.** Nobody in this paper touches the threshold margin or the window margin as a treatment. The one sentence that gestures at the window (Q3, p. 366) uses it to explain a nuisance (pre-filing drift), which is precisely the mechanism our **partition** formalises: trading before the flag. The Feb-2024 acceleration (10 → 5 business days) is a treatment on exactly the object Greenwood & Schor identify as decisive.
- **Liquidity as a driving variable is open.** Their targets are second-to-third-decile stocks with 3.69 analysts — i.e. concentrated in the illiquid tail, which is where our κ comparative statics have the most bite and where they have zero variation exploited.
- **The causal link from activism to bidder entry is asserted, not identified.** An 11 pp raw difference with no standard error is the weakest link in the most-cited claim in this literature. (Verifier: the 11 pp is also *within-paper* fragile — the three "share acquired" numbers, 26.1% / 23.1% / 21.9%, are never reconciled; see the verifier note under §3.) A model that predicts *when* the 11 pp should be larger (in κ, in the window margin) converts their descriptive gap into a testable cross-sectional prediction — and that is a position, not a replication.

**Anchor discipline:** this paper is our best evidence that the takeover is the control outcome that matters *and* the best evidence that the disclosure rule has never been used as a margin on it. Cite R3/R4/R5 for the first, Section 6 for the second.

**Danger:** they also supply the strongest referee objection to our story. If activism returns are just takeover-probability × premium, and the premium is constant, then liquidity affects control outcomes only through the *probability*, not the *premium*. Our premium-wedge channel has to be argued against this default, not around it.

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "We show that these returns are largely explained by the ability of activists to force target firms into a takeover." | p. 362 (abstract) | The competitor's headline claim: control outcome, not operating improvement, is the object |
| Q2 | "announcement returns and long-term abnormal returns are high for targets that are ultimately acquired, but not detectably different from zero for firms that remain independent." | p. 362 (abstract) | R4/R5 in the authors' own words |
| Q3 | "Note that announcement returns accrue starting a few days before the filing date, which we attribute to the 10-day window during which investors are required to file the 13D." | p. 366 | **Window margin as an observed fact.** Pre-flag trading moves price — our partition, seen in their data as a nuisance |
| Q4 | "From the perspective of the activist, exiting the position in the stock via a merger or a takeover is doubly beneficial: it generates a high premium, as well as allowing the activist to avoid the price pressure associated with an exit in the public markets (in a merger or acquisition, the activist exits in cash or with stock of a larger, more liquid company)." | p. 363 | **Liquidity in their story:** exit cost is a takeover motive. The κ channel, stated and dropped |
| Q5 | "In our full sample, activists increase the probability of takeover by about 11 percentage points. That is, activists put firms into play." | p. 363 | R7 — the load-bearing causal claim, reported without a standard error |
| Q6 | "The average announcement return, over all of these events, is 2.36%, about half of that earned by firms that are eventually taken over." | p. 368 | R4 — the conditional CAR split |
| Q7 | "A back-of-the-envelope calculation suggests that it is: activists increase the probability of takeover by about 11 percentage points. Multiplied by an expected takeover premium of 30% (e.g., Cremers, Nair, and John, 2007) yields 3.3% abnormal returns on announcement, commensurate with what we observe in the data." | p. 372 | **The premium wedge is an imported constant.** The exact gap our theory fills |
| Q8 | "For the full set of events that do not end in acquisition, post-13D filing returns are not significantly different from zero." | p. 370 | R5 — no long-run value absent a control outcome |
| Q9 | "the most ''successful'' targets of activism are those that leave the public markets (and hence the Compustat database) soon after the activist becomes involved. Thus, there is a significant selection bias, in that the firms with the largest returns tend to drop out of the sample by way of takeover." | p. 363 | Why operating-performance evidence understates activism; guards our choice of control outcome as the object |
| Q10 | "13Ds are filed with the SEC within 10 days of an entity attaining 5% or greater share in any class of a company's securities." | p. 364 | Threshold + window margin, stated as institutional fact |
| Q11 | "we show that—ironically, from the perspective of value creation—activists are most successful at creating value when they are able to effect a change in control." | p. 374 | Conclusion: control outcome is where the value is |
| Q12 | "An important question, which we do not answer here, is whether the shareholder activism associated with takeovers creates long-term value for acquiring company shareholders." | p. 374 | Declared scope boundary (Section 6) |

## 9. Verification log

**Verifier:** adversarial pass, 2026-08-19. **Source used:** `research/txt_extracts/greenwood_schor_2009.pdf` re-extracted two ways — `pdftotext -layout` (for tables) and plain `pdftotext` (for prose, because the two-column layout breaks running sentences under `-layout`) — both with the unmapped minus glyph (byte `\002`) mapped to `-`. Page mapping confirmed from the running heads on every page: **PDF *n* = printed *n*+361** (PDF 1 = 362 … PDF 14 = 375).

### Quotes (§8)

| # | Verdict | Checked against |
|---|---|---|
| Q1 | OK | PDF 1 = p. 362, abstract, verbatim |
| Q2 | OK | PDF 1 = p. 362, abstract, verbatim |
| Q3 | OK | PDF 5 = p. 366, verbatim |
| Q4 | OK | PDF 2 = p. 363, verbatim |
| Q5 | OK | PDF 2 = p. 363, verbatim |
| Q6 | OK | PDF 7 = p. 368, verbatim |
| Q7 | OK | PDF 11 = p. 372, verbatim |
| Q8 | OK | PDF 9 = p. 370, verbatim |
| Q9 | OK | PDF 2 = p. 363, verbatim |
| Q10 | OK | PDF 3 = p. 364, verbatim |
| Q11 | OK | PDF 13 = p. 374, verbatim |
| Q12 | OK | PDF 13 = p. 374, verbatim |

**12 / 12 quotes OK.** One §4 in-line quote was **MISCITED and is fixed**: "Every Schedule 13D filing includes a 'purpose of transaction' section…" is on **p. 364**, not p. 365 (PDF 3; the running head on that page reads 364). The 13G sentence and the amended-13D sentence, both also in §4, *are* on p. 365 (PDF 4) as the card said.

### Results (§3)

- **R4 (decision-critical): OK.** Table 4 Panel A, p. 369. I re-read the column structure to check the card had not slipped a column: the table is **one** "acquired" column followed by **six** "remains independent" columns (All, No news, Board/resignations, Spinoff, Share repurchase, Activist reduces stake <5%), and row `+5` reads `5.72 [4.9] | 2.36 [3.0] | 2.51 [2.9] | 1.34 [0.8] | 6.40 [4.5] | 1.36 [0.5] | 4.75 [1.2]`. The card's assignment is correct throughout. Filing-date 4.14 [3.6] confirmed. The 226-event count confirmed in the text at p. 368.
- **R5 (decision-critical): OK.** Table 4 Panel B, `+18` row: `25.85 [7.9] | 2.85 [0.6] | 0.00 [0.0] | −5.62 [−0.7] | −3.41 [−0.1] | 29.97 [0.8] | −2.83 [−0.2]`. Every figure matches.
- **R6: WRONG (internal contradiction) → fixed.** The card called spinoff "the *only* significant" short-window CAR among independents while itself printing "no news" at t = 2.9. Both are significant; rewritten, and the omitted seventh column ("activist reduces stake <5%", 4.75%, t = 1.2) added.
- **R3 (decision-critical): OK as a transcription of Table 2, but the horizon and denominator were unstated → fixed, with a verifier note.** All ten "% Acquired" figures match Table 2 exactly. But 26.1% is an 18-month figure whose denominator the paper never gives, and it sits alongside 226/980 = 23.1% (Table 4) and 21.9% (Table 6, CRSP delisting, same 18 months). See the note added under §3. **This is the item most likely to be mis-cited downstream and it is now flagged on the card.**
- **The imported 30% premium (decision-critical): OK.** p. 372 verbatim, attributed to Cremers, Nair and John (2007), inside a passage the paper itself labels "A back-of-the-envelope calculation". The ASSERTED label is correct — it is the only ASSERTED row on the card and it is the right one.
- **N = 980 events, 1993Q3–2006Q3 (decision-critical): OK.** p. 364: "the 13-year period from the third quarter of 1993 through the third quarter of 2006"; "a total of 980 activist events covering 811 unique target–activist pairs"; 784 by 139 hedge funds and 196 by 38 non-hedge funds (p. 364 text and Table 1 Panel A, p. 365). The universe of 173,078 13Ds, the 20,771-filing initial sample and the 70 surviving Gabelli events all verified. **One nuance:** Table 1 is headed "investor activism **1994**–2006" and Panel A's first year is 1994 — the *filing search* starts 1993Q3, the *events* start 1994. Card wording is consistent with this; no change needed.
- R1, R2, R13: OK — Table 2, p. 367, every CAR and t-statistic including the negative corporate-strategy row.
- R7: OK — Table 6, p. 372, all twelve figures (18.1/7.2/12.6/4.7 at 12m; 21.9/9.1/16.1/7.2 at 18m; 22.6/27.5 vs 10.6/14.3 delisting). Confirmed that Table 6 carries **no** standard error or test statistic anywhere — §5's "the load-bearing causal number is printed bare" stands.
- R9: OK — Table 3, p. 368, all fifteen count pairs.
- R10, R11: OK — Table 5, p. 371, all seven coefficients/t-statistics and all seven correlations/p-values; the 36.5% → 22.1% capex/PP&E figures verified in the text on the same page.
- R12: OK — Table 7, p. 374, all eight CAR figures and the −4.71 [−11.30] raw cumulative return.
- §2's credit-crisis description: OK — "Our final sample includes 144 target companies owned by 16 activist investors" (p. 373); the ≥10-incidents and ≥1-in-2005-or-2006 screens and the 125 DGTW portfolios all verified.
- Honesty labels: all correct. R7's "no SE or test statistic printed for the difference" and R3's "no SE printed" are literally true of the tables.

### Scope claims (§6)

- **"Liquidity is never studied": CONFIRMED, and it is stronger than the card says.** A case-insensitive grep over the full text for `liquid* | turnover | price pressure | Amihud | bid-ask | volume` returns **three** hits in the entire paper: "price pressure" and "more liquid company" (both inside Q4, p. 363) and "liquidity" in the *title* of the Brunnermeier (2009) reference. No liquidity measure, no turnover, no volume, no Amihud, anywhere.
- **"Neither margin is a treatment": CONFIRMED.** The only 13D-rule statements are the p. 364 institutional sentence, the p. 365 13G sentence, the p. 366 drift attribution (Q3) and the p. 369 "<5% ends the obligation" outcome definition. No deadline is varied, no cross-country threshold, no policy change.
- **"Bidder entry is never counted": partially REFINED (see §6).** True of measurement; false of argument — the paper twice offers qualitative bidder/auction evidence and carries one auction-related outcome row.
- "No takeover premium is estimated": CONFIRMED — every "premium" hit is either the imported 30%, the abstract's framing, or the p. 374 discussion of what a premium *would* represent.

### Version / venue (header)

- OK. Journal of Financial Economics 92(3), 362–375, 2009; running heads on all fourteen pages read "Journal of Financial Economics 92 (2009) 362–375"; "ARTICLE IN PRESS" banner present on every page as the card says.

### Omissions added

1. **§4 — their own statement of the identity.** "Thus, the market rationally bids up the price of the target stock in anticipation of a takeover premium." (p. 372). §7.2 builds our position on announcement return ≈ Δ Pr(takeover) × premium; that identity is Greenwood & Schor's own words on the page where they import the constant, which strengthens the "they need the wedge and don't have it" framing and removes any suggestion we inferred it.
2. **§5 / §6 — the two pieces of bidder-entry evidence.** The Robert Chapman "digestible… easy to market to bidders" target-selection story (p. 363, n.2) and the Thomas H. Lee "driven into some form of auction" quote (p. 372, n.7). Material because the card's whitespace claim on bidder entry needs to be about *measurement*, not novelty of the idea.
3. **§3 — the three incompatible "share acquired" numbers** (26.1% / 23.1% / 21.9%), never reconciled in the paper. Decision-critical: the Klein & Zur card leans on "the share acquired is a contested number"; it is contested inside this paper too.
4. **§6 — their normative conclusion** that the scope for activism to affect governance is limited because activists are "less interested" in changes that leave the firm independent (p. 374). Already in print, so it cannot be presented as our reading of R5.

### Overall verdict

**PASS with one WRONG and one MISCITED, both fixed.** 12/12 quotes verbatim; one quote's page corrected (364, not 365); R6's internal contradiction corrected; R3 given its missing horizon and a note on the paper's three incompatible acquisition shares. Every decision-critical number (5.72/4.9 vs 2.36/3.0; 25.85/7.9 vs 2.85/0.6; 26.1%; the imported 30%; N = 980 for 1993Q3–2006Q3) confirmed against the print. Four omissions added. Nothing UNCHECKED.
