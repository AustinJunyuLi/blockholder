# Edmans & Manso (2011) — "Governance Through Trading and Intervention: A Theory of Multiple Blockholders"

**Venue / status:** *Review of Financial Studies* 24(7), 2395–2428, July 2011 (published; Advance Access 14 December 2010; doi:10.1093/rfs/hhq145)
**Full text from:** `research/txt_extracts/edmans_manso_2011_rfs.pdf` / `.txt` (OUP published version, 34 pp) · **Reader:** opus · **Read:** full text, 34 pages (Sections 1–6 + Table 1 + Table 2 + references). **Appendices A–D are NOT in this PDF** — the article states "All appendices are available online at http://www.sfsrfs.org." (p. 2399 n.3) and "The Appendix contains all proofs not in the main text, some extensions, and other peripheral material" (p. 2399). Proofs of Propositions 1, 2, 7–13 therefore were not read.
**Type:** theory   **Role for us:** antecedent

**Page numbering:** printed *Review of Financial Studies* pages 2395–2428 (PDF page 1 = printed 2395, one-to-one throughout).
**Quote convention:** displayed fractions, subscripts and superscripts are written inline (e.g. `I/(I+1)`, `σε`, `I*costly`) — all words are character-for-character as printed. Two extraction artifacts to expect if you re-grep the `.txt`: the OUP download watermark is injected mid-sentence at page breaks, and large math operators leave stray glyphs in running text (the printed "We use the term 'liquidity' to refer to σε" extracts as "We P use the term..."). Quotes below give the printed form.

## 1. Question

Why do most firms have *several* small blockholders when every intervention theory says one big blockholder governs best? Edmans and Manso answer that splitting a block weakens **intervention** (free-riding) but strengthens a second mechanism, **governance through trading**: blockholders who cannot coordinate trade competitively, like a Cournot oligopoly, which pushes more information into the price, which in turn makes the manager's equity pay track his effort, which elicits effort ex ante. They then ask what determines the *optimal number* of blockholders across firms. Explicit policy framing: "Should policymakers encourage more concentrated stakes, as suggested by existing models, or can such a structure in fact be efficient?" (p. 2396).

## 2. Model / data and method

Pure theory; no estimation, no simulation. One descriptive table (Table 1) of blockholder counts. Two-stage game between a manager, I blockholders and a market maker (Figure 1, p. 2402).

- **Firm value.** ṽ = φ_a·log(1 + a) + φ_b·log(1 + Σ_i b_i) + η̃, with η̃ ~ N(0, σ_η²). a ≥ 0 is the manager's action, b_i ≥ 0 blockholder i's action; each bears *linear* personal cost (a, and b_i). φ_a, φ_b are effort productivities; "output" = effort scaled by productivity (eq. 1, p. 2402). The log-value/linear-cost pair is chosen so that splitting a block does not mechanically improve the monitoring technology (n.10, p. 2403).
- **Ownership.** One share. Manager owns α; each blockholder holds β/I; α + β < 1. **β is held fixed throughout — only the number I is optimised** (p. 2403–2404). Free float 1 − α − β "plays no role" (p. 2404).
- **Information.** In the core model each blockholder observes ṽ perfectly (as in Admati–Pfleiderer 2009); a is privately observed by the manager; b_i is public in the core model (relaxed in §4.4). Noise traders submit ε̃ ~ N(0, σε²), independent of η. **"We use the term 'liquidity' to refer to σε"** (p. 2405).
- **Trading.** Kyle (1985) with multiple informed traders (Kyle 1984; Admati–Pfleiderer 1988; Holden–Subrahmanyam 1992; Foster–Viswanathan 1993). Competitive market maker sets p̃ = E[ṽ | ỹ] on total order flow ỹ = Σ_i x̃_i + ε̃.
- **Objectives.** Manager maximises E[α·p̃ − a] (the *market* value of his shares). Each blockholder maximises trading profits + (β/I)·ṽ − b_i. Generalised in §4.3 to weights ω on p̃ (manager) and ζ on p̃ (blockholder); the core model is ω = 1, ζ = 0.
- **Equilibrium notion.** Unique *linear* trading equilibrium, symmetric; solved by backward induction; unique symmetric action equilibrium (asymmetric equilibria exist but Σ_i b_i is unique, p. 2408).
- **Closed forms.** λ = (√I/(I+1))·(σ_η/σε); γ = (1/√I)·(σε/σ_η); each blockholder's expected trading profit = (1/√(I(I+1)))·σ_η·σε (Prop. 1, eqs. 2–6, p. 2405).
- **Price-informativeness metric.** E[dp̃/dṽ] — the expected price change per unit of firm-value change, chosen because it is what a price-compensated agent responds to. Appendix D (online, unread) is said to show it is equivalent to (Var(ṽ) − Var(ṽ|p̃))/Var(ṽ) (p. 2406).
- **Extensions.** §4.1 costly information acquisition (cost c); §4.2 perfect positive complementarities (Leontief, min) and perfect negative complementarities (max); §4.3 general objectives (ω, ζ); §4.4 unobservable b_i.
- **Descriptive data (Table 1, p. 2401).** 1,240 US firms in 2001 from Dlugosz et al. (2006), blockholder = ≥ 5% of equity: 70% of firms have multiple blockholders, 26% have ≥ 4; for *outside* blockholders 57% and 17%. Holderness (2009) hand-collected: 74% multiple, 26% with ≥ 4. Overseas (10%-voting-rights definition): Laeven–Levine 34% of European firms, Maury–Pajuste 48% of Finnish firms, Faccio–Lang-based 39%.

## 3. Results — with honesty labels

Proof location matters here. *(Refined by verifier against the printed text.)* Props. 3 and 4 carry **complete** proofs in print. Props. 5 and 6 carry only the printed derivation — the statement of each explicitly defers uniqueness and the comparative statics to online Appendix A. Props. 1, 2 and 7–13 have **no printed proof at all**. Appendix A is not in this PDF. All are analytical propositions, so all are PROVED, but the proof-read status is flagged.

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | Unique linear trading equilibrium: x_i = γ(ṽ − conjectured value), p = conjecture + λỹ, with λ = (√I/(I+1))(σ_η/σε), γ = (1/√I)(σε/σ_η); each blockholder's expected profit = σ_η σε/√(I(I+1)) | PROVED (proof in online Appendix, not read) | p. 2405, Prop. 1, eqs. 2–6 |
| R2 | **Price informativeness = I/(I+1)**: rising in the number of blockholders, → 1 as I → ∞, = ½ under monopoly | PROVED (proof in online Appendix, not read) | p. 2406, Prop. 2 |
| R3 | **Liquidity σε has NO effect on price informativeness in the core model** — more noise exactly offsets more aggressive informed trading | PROVED (immediate from R1–R2) | p. 2406, §2.1 |
| R4 | Manager's effort a = φ_a·α·(I/(I+1)) − 1 (rising in I); combined blockholder effort Σb_i = φ_b·β·(1/I) − 1 (falling in I, free-riding); each b_i = φ_b·β/I² − 1/I | PROVED (proof in printed text) | p. 2407, Prop. 3, eqs. 7–9 |
| R5 | **Firm-value-optimal number of blockholders I\* = (φ_a − φ_b)/φ_b** — interior, rising in managerial-effort productivity, falling in intervention productivity | PROVED (proof in printed text) | p. 2409, Prop. 4, eq. 15 |
| R6 | Social optimum I\*soc solves eq. (18); may be above or below I\*; rising in φ_a and β, falling in φ_b and α | PROVED (in-text derivation; uniqueness and comparative statics in online Appendix A, not read) | pp. 2409–2410, Prop. 5 |
| R7 | Private optimum I\*priv solves eq. (20); may be above or below I\* and I\*soc; rising in φ_a and β, **falling in φ_b and in σ_η·σε** (more valuable information → fewer blockholders, to limit competition) | PROVED (in-text derivation; uniqueness and comparative statics in online Appendix A, not read) | p. 2410, Prop. 6 |
| R8 | With costly information, J = min{I, n} blockholders become informed, where n solves σ_η σε/√(n(n+1)) = c; uninformed blockholders do not trade | PROVED (proof in online Appendix, not read) | p. 2411, Prop. 7 |
| R9 | **I\*costly = min{(φ_a − φ_b)/φ_b, n}. If the liquidity constraint binds (n < (φ_a − φ_b)/φ_b), both I\*costly and firm value are increasing in σε (and in σ_η, decreasing in c); if it does not bind, they are independent of σε, σ_η, c** — liquidity matters only on one side of a kink, and monotonically, never with a hump | PROVED (proof in online Appendix, not read) | p. 2412, Prop. 8, eq. 26 |
| R10 | Perfect positive complementarities (Leontief min): I\* solves I²/(I+1) = (φ_b β/φ_a α)·exp(φ_b − φ_a); **comparative statics flip** — I\* rising in φ_b and β, falling in φ_a and α | PROVED (proof in online Appendix, not read) | p. 2414, Prop. 9, eqs. 28–30 |
| R11 | Perfect negative complementarities (max): corner solution — I\* = ∞ if φ_a log(φ_a α) ≥ φ_b log(φ_b β), else I\* = 1; φ_a's effect is discontinuous | PROVED (proof in online Appendix, not read) | pp. 2415–2416, Prop. 10, eqs. 32–34 |
| R12 | With general contracts, I\*gen is the larger root of eq. (36); increasing in ω (manager's price weight), ζ (blockholder's price weight) and φ_a, decreasing in φ_b; = 1 if no root ≥ 1 | PROVED (proof in online Appendix, not read) | p. 2417, Prop. 11, eq. 36 |
| R13 | With unobservable b_i, the core-model actions remain an equilibrium if either β/(φ_b(1 + ln(φ_b β))) > σε/σ_η or (φ_b β − 1)/(φ_b² ln(φ_b β)) > σε/σ_η | PROVED (proof in online Appendix, not read) | p. 2418, Prop. 12, eqs. 38–39 |
| R14 | That equilibrium is the unique symmetric pure-strategy equilibrium; any asymmetric pure-strategy equilibrium has Σ_i b_i = φ_b β/I − 1; mixed strategies not analysed | PROVED (proof in online Appendix, not read) | p. 2419, Prop. 13 |
| R15 | Descriptive: 70% of 1,240 US firms (2001) have ≥ 2 blockholders at the 5% definition; 26% have ≥ 4; outside-blockholder figures 57% and 17% | ESTIMATED (frequency counts from Dlugosz et al. 2006; no SEs) | p. 2401, Table 1 |
| R16 | Empirical implications: I lowers total trading profits and raises price efficiency and firm value; I rises with φ_a, ω, ζ, σ_η, σε and falls with φ_b and c; blockholder numbers should be studied as both dependent and independent variable | ASSERTED (predictions; supporting cites are other authors' estimates, and the authors state none of the structure-determinant predictions have been tested) | §5, pp. 2419–2423 |

## 4. Institutional facts used

- **Schedule 13D / Section 13(d) is named exactly twice, both outside the model.**
  1. **Footnote 7, p. 2400** — the 5% trigger and the 10% insider threshold are offered as a *rival explanation* for multiple blockholders, and set aside: regulation "prevents investors from building large blocks and thus forces firms to be held by multiple blockholders. Existing theories advocating a single large blockholder would suggest that such institutional constraints lead to inefficient ownership structures; this article reaches a different conclusion." No model of this channel follows.
  2. **p. 2402** — a *measurement* remark: because their blockholder need not have control rights, "empirical studies of blockholders may wish to use data sources other than 13d filings to identify sizable shareholders below the 5% threshold".
- **Thresholds used only to define the sample, never as a policy margin:** blockholder = ≥ 5% of equity (Dlugosz et al. 2006) for the US, ≥ 10% of *voting rights* for the European studies (pp. 2401–2402). Mutual funds "typically hold under 5%" (p. 2402).
- **The filing window is never mentioned.** No filing deadline, no 10-day rule, no timing of any disclosure appears anywhere in the article.
- **Insider-trading law** appears once, to explain why insiders are excluded from the blockholder definition for US firms (n.9, p. 2402).
- **Legal barriers to intervention** (Black 1990; Bebchuk 2007) are used to argue φ_b is low in the US, hence high I* — an institutional fact deployed as a comparative static (p. 2421).
- **Survey/market facts:** McCahery–Sautner–Starks — trading is used by 80% of institutions, 66% vote against management, 55% engage the board, six other intervention channels used by ≥ 10% (n.6, p. 2400). The 2007 hedge-fund crisis is cited once as an example of multiple investors trading in the same direction (n.1, p. 2396).
- **Negotiated block trades vs on-market trades (added by verifier).** n.15, p. 2405: blockholders "typically trade on the market rather than using a negotiated block trade", because only an on-market trade lets them camouflage with noise traders, while a negotiated counterparty "engages in extensive due diligence since she is trading a large stake". Barclay–Holderness (1991) are cited for negotiated block trades being rare, and for the event-study returns being "independent of whether the block is traded at a premium or discount". This is the only place the article touches block *transactions* or block premia — as a justification for the Kyle setup, never as an object.
- **Lockups (added by verifier).** p. 2421: the social optimum may actually be observed "if the firm has recently undergone an IPO, or lockups prevent blockholders from retrading from the initial structure." Lockups are the article's only institutional device that pins an ownership structure in place. A disclosure threshold would be another; they never say so.
- **Control rights enter only as a determinant of φ_b (added by verifier).** p. 2421: "Another determinant of φ_b is blockholders' control rights and thus ability to intervene (holding constant the size of their individual stakes)", with Black (1990) and Bebchuk (2007) used to argue φ_b is low in the US. n.22, p. 2421 concedes the mechanism they do not build: "In reality, control rights will likely be increasing in the size of each blockholder's individual stake β/I. This will reinforce the negative effect of I on intervention currently in this article."
- **"Disclosure" appears exactly once in the whole article (added by verifier)** — n.4, p. 2400, describing Fishman and Hagerty (1989), where price efficiency "is enhanced by firms' voluntary disclosures". Someone else's mechanism, in a literature footnote.
- **No econometrics of any kind.** Table 1 is a frequency count; every other number in the paper is a parameter.

## 5. Referee-facing strengths / weaknesses

**Strengths:** The cleanest available statement of the trading-vs-intervention trade-off, and the first to put both mechanisms in one blockholder's hands (they claim to be "the first theory that analyzes both of these major governance mechanisms and the tradeoffs between them", p. 2400). The Cournot analogy is exactly right and instantly legible to a referee. Closed forms throughout, with an interior optimum I* = (φ_a − φ_b)/φ_b that a referee can hold in his head. Three optima (firm value, social, private) are separated and shown to share the key comparative statics — a discipline most papers skip. §4.2 shows the headline comparative static *reverses* under positive complementarities, which is unusually candid.

**Weaknesses / open flanks (our whitespace):**
- **Liquidity is inert in the core model.** Prop. 2 makes price informativeness I/(I+1), independent of σε. Liquidity only bites through the information-acquisition constraint in §4.1, and then only when that constraint binds (Prop. 8). There is no liquidity comparative static on any real outcome in the core model at all. *(Sharpened by verifier — the card's "inert" must be stated as core-model-only, because the authors flag the exception in the same paragraph:)* "In Section 4.1, we show that liquidity has a positive effect on price informativeness under costly information acquisition" (p. 2406). The accurate two-part statement is: liquidity is **inert** on price informativeness in the core model, and **monotone-positive, never humped** once information is costly and the constraint binds.
- **β is fixed by assumption.** The total block is a parameter; only its division is optimised. So there is no stake accumulation, no threshold to cross, and hence no place a disclosure rule could attach. The authors say so: free float "plays no role", and endogenising β is left undone (p. 2404).
- **The market maker's information set is a single Gaussian order flow.** There is no public event, no flag, no partition of states into disclosed and undisclosed. The model structurally cannot represent a disclosure rule.
- **Blockholders are symmetric and perfectly informed** in the core model; asymmetric blockholders are explicitly left to future work and admitted to need "a quite different framework" (n.23, p. 2424). *(Qualified by verifier:)* perfect information is relaxed off-page — "Appendix B shows that our results are unchanged if each blockholder obtains an imperfect signal of ṽ" (p. 2404), and "Appendix C allows signal precision to be increasing in the blockholder's individual stake and thus fall with I" (n.14, p. 2404). **Both appendices are online and were not read — UNCHECKED.** Do not attack symmetry-of-information without obtaining them.
- **The Cournot assumption is pre-defended (added by verifier).** n.16, p. 2405: "The results are unchanged if blockholders can coordinate (either to share the costs of intervention, or limit their trading volumes), but the cost is increasing in the number of coordinating parties." A "why can't they just collude?" objection will not land.
- **No control outcome.** No bidder, no tender offer, no premium, no campaign, no voting contest. Control contests are named only as *other people's* modelling channel (p. 2400) and dismissed as not theirs.
- **Zero identification.** The authors concede the key parameters φ_a, φ_b are hard to measure, that none of the structure-determinant predictions has been tested, and that "identification of causal effects will require careful instrumentation" (p. 2423).

## 6. What they do NOT do (scope boundary)

- **OBJECT.** Price informativeness E[dp̃/dṽ] = I/(I+1); the manager's effort a; blockholders' intervention effort Σb_i; expected firm value E[ṽ]; total surplus; blockholders' combined payoff; and above all the **optimal number of blockholders I\***. **Never** a takeover premium, bidder entry, announcement return, or campaign success. "Takeover" appears twice in the entire article, both times as an *exogenous* reason the manager weights the stock price: "takeover threat (Stein 1988)" (p. 2416) and the empirical proxy that I should be higher where "takeover defenses are weaker" (p. 2422). There is no acquirer, no control transaction, and no premium in the model. *(Verified by grep; one refinement added by verifier: "premium" does occur twice, both outside the model — n.15, p. 2405, citing Barclay–Holderness (1991) event-study returns on negotiated block trades traded "at a premium or discount", and p. 2409, the IPO price premium blockholders pay in expectation of trading gains. Neither is a takeover premium.)*
- **MARGIN of a disclosure rule: NONE.** No disclosure margin is a parameter, a choice variable, or a comparative static. The 5% threshold and the 10% insider threshold appear only in footnote 7 (p. 2400) as a *competing* explanation for multiple blockholders that the article deliberately does not adopt, and at p. 2402 as advice about which *data source* an empiricist should use. The filing window is never mentioned. Nothing in the model responds to a change in either margin.
- **IDENTIFICATION: theory only.** One descriptive frequency table (Table 1). No regression, no event study, no structural estimation, no numerical grid. §5 hands the testing to others and flags two obstacles: unmeasurable φ_a and φ_b, and the endogeneity of blockholder structure. *(added by verifier)* They do name exogenous shifters of the observed structure — "a blockholder suffering a change in management or a liquidity shock" (n.20, p. 2420) — and they anticipate the Demsetz–Lehn null: if I always sat at the firm-value optimum there would be no I–firm-value relation, but the observed I is likely the *private* optimum, so a null is not evidence against the model (n.20, p. 2420). n.21, p. 2421 records that Maury–Pajuste (2005) and Laeven–Levine (2007) report blockholder counts but never relate them to cross-sectional determinants. The proxies they suggest are managerial characteristics or salary for φ_a (Gabaix–Landier 2008), activist-vs-passive investor type for φ_b, vesting length and weak takeover defenses for ω, and blockholder trading frequency for ζ (pp. 2421–2423).
- **Explicitly left undone, in their own words:**
  - Endogenous total block and float-dependent liquidity: "In this model, free float is fixed at 1 − α − β and plays no role. Endogenizing β and allowing liquidity (introduced shortly) to depend on free float will lead to the same tradeoff as these earlier papers." (p. 2404).
  - Asymmetric blockholders and the distribution of shares among a fixed number (p. 2424 and n.23).
  - Multiple trading periods, information timeliness, liquidity shocks and front-running (pp. 2424–2425).
  - Mixed-strategy equilibria under unobservable actions (p. 2419).
  - Managerial risk aversion and endogenous α (n.13, p. 2404).
- **On disclosure rules and takeovers as future work: no such sentence exists.** The conclusion's future-research agenda (pp. 2424–2425) names asymmetric blockholders, trading/intervention specialists, joint determination of α and β, multiple trading rounds, and front-running — and on the theory side only that "Future corporate finance models of multiple blockholders could incorporate more complex effects currently analyzed in asset pricing models of many informed traders." Neither a disclosure rule nor a takeover is ever named as an open question. The single place regulation is raised (n.7, p. 2400) treats it as a **rival explanation they decline**, not as deferred work. **Recorded as: declined rival, not deferred.**

## 7. Implications for our position

**What Edmans–Manso occupy:** OBJECT = price informativeness and the *number* of blockholders (plus manager effort and firm value); MARGIN = none (the 5% threshold is named once, as a rival explanation they reject); IDENTIFICATION = theory only, with one descriptive table. **Antecedent, not competitor.**

**How this constrains and supports us:**

1. **Their footnote 7 is the single most useful sentence in the paper for us — and it is a gift, not a threat.** They name Section 13(d)'s 5% trigger as a candidate explanation of ownership structure and then *decline to model it*, saying only that existing single-blockholder theories would call the resulting structure inefficient while theirs would not. That is the disclosure margin left on the table by the two authors best placed to take it. Our position — a disclosure rule as a **partition** of what the market observes, with a threshold margin and a window margin — sits exactly in the ground footnote 7 vacates. Cite it early.
2. **Liquidity is inert here, which sharpens what our κ has to do.** Prop. 2 says price informativeness is I/(I+1) regardless of σε; liquidity only moves outcomes through the information-acquisition constraint in §4.1, and then monotonically. So the literature's two canonical liquidity statements are: Edmans (2009) — inverse-U in liquidity when the stake is fixed; Edmans–Manso (2011) — *no* liquidity effect in the core, monotone increasing under costly information. **Neither delivers a liquidity effect on a control outcome, and neither delivers a non-monotonicity that survives endogenous ownership.** That is our whitespace stated precisely.
3. **They hand us the reason a stake can be fixed.** Their whole model holds β fixed and admits free float "plays no role" (p. 2404). A referee may ask us why our blockholder's stake does not simply adjust. The honest answer — the disclosure rule pins it — is one Edmans (2009, p. 2499) and Edmans–Manso (2011, n.7) both gesture at and neither models.
4. **Do not claim the exit/voice trade-off as ours.** They own "trading vs intervention" and claim first-mover status on modelling both (p. 2400). Draft_v2's exit/hold/quiet-voice/public-voice action set must be presented as *machinery* (per CONTEXT.md), with our identity resting on the partition and the control outcome, not on the fact that a blockholder can both trade and engage.
5. **Their Cournot/free-rider asymmetry is a template we can borrow for the two disclosure margins.** They show one primitive (coordination difficulty) hurting one mechanism and helping another. Our threshold margin and window margin plausibly cut opposite ways on the same control outcome; their exposition is the model for how to present that cleanly.
6. **Their one concession on control is a gift too (added by verifier).** n.22, p. 2421 admits that "control rights will likely be increasing in the size of each blockholder's individual stake β/I", and that modelling this would only *reinforce* their intervention result — so they concede a stake-dependent control technology matters and decline to build one. Our control outcome is exactly that technology made explicit. Pair this with n.7 (point 1 above): they decline the disclosure margin *and* they decline the stake–control link, in two footnotes on facing sides of the same paper.
7. **Whitespace confirmed on all three coordinates.** Object: no control outcome anywhere in the paper. Margin: neither threshold nor window is a parameter; the window is never mentioned; the threshold is explicitly declined. Identification: one frequency table, no estimation. Nothing here competes with a liquidity × disclosure-rule × control-outcome position.

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "Another explanation is that regulation (e.g., Section 13(d) filing requirements upon acquisition of a 5% stake, or becoming classified as an insider upon acquisition of a 10% stake) prevents investors from building large blocks and thus forces firms to be held by multiple blockholders." | p. 2400 (n. 7) | The disclosure rule named as a rival explanation — the ground they vacate and we occupy |
| Q2 | "Existing theories advocating a single large blockholder would suggest that such institutional constraints lead to inefficient ownership structures; this article reaches a different conclusion." | p. 2400 (n. 7) | They decline to model the rule; declined, not deferred |
| Q3 | "As is standard in Kyle-type models, liquidity σε has no effect on price informativeness." | p. 2406 | Liquidity is inert in their core model — the sharpest contrast with our κ |
| Q4 | "Proposition 2. (Price Informativeness) Price informativeness is equal to I /(I + 1)." | p. 2406 | Their central object, and its independence of liquidity |
| Q5 | "If n < (φa − φb)/φb, I*costly and firm value are increasing in ση and σε and decreasing in c. If n ≥ (φa − φb)/φb, I*costly and firm value are independent of ση, σε, and c." *[fractions and sub/superscripts written inline; words verbatim]* | p. 2412 (Prop. 8) | The only liquidity comparative static in the paper: a binding-constraint kink, monotone, never a hump |
| Q6 | "By contrast, multiple blockholders trade aggressively to compete for profits, as in a Cournot oligopoly." | p. 2396 | The paper's identity: free-riding in intervention vs Cournot competition in trading |
| Q7 | "By contrast, multiple blockholders trade aggressively, augmenting price informativeness, and thus constitute a commitment device to reward the manager ex post for his actions." | p. 2408 | The dynamic-consistency mechanism, stated in one line |
| Q8 | "In this model, free float is fixed at 1 − α − β and plays no role. Endogenizing β and allowing liquidity (introduced shortly) to depend on free float will lead to the same tradeoff as these earlier papers." | p. 2404 | Total block size and float-dependent liquidity are explicitly outside their model |
| Q9 | "It thus can apply to shareholders with less than 5% and suggests that empirical studies of blockholders may wish to use data sources other than 13d filings to identify sizable shareholders below the 5% threshold (e.g., Gallagher, Gardner, and Swan 2010)." | p. 2402 | The 5% threshold treated purely as a measurement nuisance, never as a policy margin |
| Q10 | "Section 4.1 shows that if information is costly, the optimal number of blockholders depends on microstructure features: It is decreasing in the information cost c, increasing in blockholders' private information ση, and increasing in market liquidity σε." | p. 2422 | Their own summary of where liquidity does bite — monotone, on ownership structure, not on any control outcome |
| Q11 | "Therefore, documenting correlations will be insufficient to support the model; identification of causal effects will require careful instrumentation." | p. 2423 | Their identification standard — theory only, empirics deferred to others |
| Q12 | "Future corporate finance models of multiple blockholders could incorporate more complex effects currently analyzed in asset pricing models of many informed traders." | p. 2424 | The full extent of the theoretical future-work agenda: no disclosure rule, no takeover |
| Q13 *(added by verifier)* | "In Section 4.1, we show that liquidity has a positive effect on price informativeness under costly information acquisition." | p. 2406 | The exception to Q3, in the same paragraph as Q3 — never quote Q3 without it, or "liquidity is inert here" is overstated |
| Q14 *(added by verifier)* | "In reality, control rights will likely be increasing in the size of each blockholder's individual stake β/I. This will reinforce the negative effect of I on intervention currently in this article." | p. 2421 (n. 22) | They concede a stake-dependent control technology and decline to build it — the second piece of ground they vacate |
| Q15 *(added by verifier)* | "This is because only the former method allows them to trade on their information by camouflaging with noise traders (as in Kyle 1985). Blockholders cannot trade on information in a negotiated trade because the counterparty engages in extensive due diligence since she is trading a large stake." | p. 2405 (n. 15) | Their reason blockholders trade on-market rather than in negotiated blocks: camouflage — the very thing a filing window interrupts |

## 9. Verification log

**Verifier:** adversarial second reader (Opus), 2026-08-19. **Checked against:** `research/txt_extracts/edmans_manso_2011_rfs.pdf`, re-extracted page-by-page with `pdftotext -f N -l N -layout` (34 PDF pages; PDF page N = printed 2394+N, confirmed from the folio on every page). Every quote was also grepped as an exact string against a de-hyphenated flattening of that extraction. Appendices A–D are online-only and could not be obtained.

**Header / venue.** OK. Front matter gives doi:10.1093/rfs/hhq145 and "Advance Access publication December 14, 2010"; the running head reads "The Review of Financial Studies / v 24 n 7 2011"; first printed page 2395, last 2428; 34 pages. Matches the header. n.3, p. 2399 "All appendices are available online at http://www.sfsrfs.org." — **OK, verbatim.** "The Appendix contains all proofs not in the main text, some extensions, and other peripheral material" (p. 2399) — **OK, verbatim.**

**Quotes (§8).**

| # | Verdict | Checked against |
|---|---|---|
| Q1 (n.7, 13(d)) | OK | p. 2400 n.7, word-for-word |
| Q2 (n.7, declined) | OK | p. 2400 n.7, word-for-word |
| Q3 (liquidity inert) | OK | p. 2406 — but see Q13; quoting Q3 alone overstates the claim |
| Q4 (Prop. 2) | OK | p. 2406 |
| Q5 (Prop. 8) | OK | p. 2412, word-for-word including both branches of the kink |
| Q6 (Cournot) | OK | p. 2396 |
| Q7 (commitment device) | OK | p. 2408 |
| Q8 (free float) | OK | p. 2404 |
| Q9 (13d as data source) | OK | p. 2402 |
| Q10 (where liquidity bites) | OK | p. 2422 |
| Q11 (instrumentation) | OK | p. 2423 |
| Q12 (future work) | OK | p. 2424 |
| Q13–Q15 | OK (added by verifier) | pp. 2406, 2421 n.22, 2405 n.15 — each grepped verbatim |

**Results (§3).** R1–R5, R8–R14 OK: statements, equation numbers and pages all match the print. R6 and R7 OK. R7 was **incomplete** — Prop. 6 states I\*priv is "increasing in φa and β, and decreasing in φb and ση σε"; the card had dropped φ_b. Corrected. **Proof-location claim re-derived from the print and refined:** Props. 3 and 4 have complete printed proofs; Props. 5 and 6 print only the derivation and defer uniqueness plus comparative statics to Appendix A; Props. 1, 2 and 7–13 carry no printed proof. The card's original "Props. 3–6 carry proofs in the printed text" was too strong for 5 and 6 and is fixed. **The contents of Appendices A–D are UNCHECKED — not in this PDF.** That covers the proofs of Props. 1, 2, 7–13 (including Prop. 8, the *only* liquidity comparative static in the paper), the claimed equivalence of E[dp̃/dṽ] to the variance-ratio measure (Appendix D), the imperfect-signal robustness (Appendix B) and the stake-dependent-precision robustness (Appendix C). R15 OK — Table 1 numbers match exactly (70%/26% all blockholders, 57%/17% outside, Holderness 74%/26%). R16 OK.

**Scope claims (§6), each executed as a grep over the full text.**
- "the filing window is never mentioned" — **CONFIRMED.** Zero hits for *window*, *business day*, *ten day*, *10 day*, *deadline* anywhere, including footnotes and references.
- "13(d) named exactly twice" — **CONFIRMED.** n.7 p. 2400 and p. 2402, and nowhere else.
- "takeover appears twice, both as an exogenous reason the manager weights the price / as an empirical proxy" — **CONFIRMED.** p. 2416 ("takeover threat (Stein 1988)") and p. 2422 ("takeover defenses are weaker"); the only other hit is the Stein 1988 reference entry.
- "no control outcome" — **CONFIRMED for the model.** No bidder, no tender offer, no acquirer, no merger, no campaign anywhere. Refinement added in §6: "premium" occurs twice, both outside the model (block-trade premium/discount in n.15 p. 2405; IPO premium p. 2409).
- "liquidity inert on price informativeness in the core model" — **CONFIRMED** at p. 2406, but the same paragraph flags the §4.1 exception; §5 and Q13 now carry it.
- "monotone-positive only under a binding information-acquisition constraint (Prop. 8, p. 2412)" — **CONFIRMED**, verbatim, both branches.
- "no regression, no event study, no structural estimation, no numerical grid" — CONFIRMED. Table 1 is the only table of data; Table 2 (p. 2413) is a 2×3 taxonomy of action types, not data.

**Omissions added.** (1) n.15, p. 2405 — negotiated block trades vs on-market trades, camouflage as the reason for the latter, and the Barclay–Holderness (1991) block premium/discount evidence (§4, Q15). (2) p. 2421 — lockups as the article's only ownership-pinning institution (§4). (3) p. 2421 and n.22 — control rights as a determinant of φ_b, and the conceded but unmodelled dependence of control rights on the individual stake β/I (§4, §7 point 6, Q14). (4) n.4, p. 2400 — the single occurrence of "disclosure" in the whole article, describing Fishman–Hagerty's voluntary-disclosure channel (§4). (5) p. 2406 — the sentence announcing that liquidity *does* raise price informativeness under costly information, which the card's "inert" framing had left implicit (§5, Q13). (6) n.16, p. 2405 — the pre-emptive defence of the Cournot assumption against a coordination objection (§5). (7) p. 2404 and n.14 — Appendices B and C relax perfect and symmetric information, both unread (§5, flagged UNCHECKED). (8) n.20, p. 2420 and n.21, p. 2421 — their named exogenous shifters (blockholder management change, liquidity shock), the Demsetz–Lehn null defence, and the proxies they suggest for φ_a, φ_b, ω and ζ (§6).

**Overall verdict: SOUND; one incomplete comparative static and one over-strong proof-location claim fixed, one framing sharpened.** No quote was misquoted and no page was wrong. All three whitespace coordinates survive adversarial grep: no control outcome, no disclosure margin (threshold declined in a footnote, window never named), no estimation.

**Decision-critical items that could not be checked — named, not triaged away.**
1. **Appendix A (proofs of Props. 1, 2, 7–13) — UNCHECKED.** This includes **Prop. 8**, which is the paper's only liquidity comparative static and the load-bearing citation for "the literature's second canonical liquidity statement is monotone, not humped" (§7 point 2). If a referee disputes that, we currently cannot show the proof.
2. **Appendix D — UNCHECKED.** The claimed equivalence of their E[dp̃/dṽ] to the standard variance-ratio measure of price informativeness. Our §2 records the claim on their authority only; if we ever compare their informativeness object to ours, this equivalence is an unverified link.
3. **Appendices B and C — UNCHECKED.** The imperfect-signal and stake-dependent-precision robustness. These matter if we argue their symmetric-perfect-information setup is what makes liquidity inert.


## 9b. Supplement supplement-reader log — 2026-08-19

**Trigger.** The fetcher's log (`research/txt_extracts/FETCH_LOG_C.md`, row `edmans_manso_2011_appendices`) reported:
"Appendices A–D are **embedded in the main published PDF itself** (confirmed via text search: 'Appendix A.12', 'Appendix B ...',
'Appendix C ...'), not a separate Supplementary-data file", and inferred that the reader and verifier had wrongly believed them
online-only. This pass was asked to check that and, if the appendices were there, to close the UNCHECKED proofs.

### Verdict: the fetcher's row is a FALSE POSITIVE. The appendices are NOT in the PDF. The card was right.

**Check run:** `pdftotext -layout` and `pdftotext -raw` over the whole of
`research/txt_extracts/edmans_manso_2011_rfs.pdf` (`pdfinfo`: **34 pages**), then string counts over both extractions:

| String | Hits in the whole PDF |
|---|---|
| `Proof of` | **0** |
| `Proof.` | **0** |
| `Q.E.D` | **0** |
| `Appendix` | **7 — every one of them an in-text cross-reference** |
| `Proposition 8` | 1 (the *statement*, printed p. 2412) |
| `informativeness measure` | 0 |

Thirteen propositions are **stated** in the body (Props. 1–13, all located). **Not one proof environment exists anywhere in the
file.** A document containing Appendices A–D of a 13-proposition theory paper cannot have zero occurrences of "Proof".

**All seven `Appendix` hits, with printed pages — these are what the fetcher's grep matched:**

| Printed p. | The actual sentence |
|---|---|
| 2399 | "The Appendix contains all proofs not in the main text, some extensions, and other peripheral material" |
| 2399 (n. 3) | "All appendices are available online at http://www.sfsrfs.org." |
| 2403 | "Sufficient conditions are given in Appendix A.<sup>12</sup>" — **the fetcher's "Appendix A.12" is "Appendix A" plus footnote marker 12**, not a section number |
| 2404 | "Appendix B shows that our results are unchanged if each blockholder obtains…" |
| 2404 (n. 14) | "Appendix C allows signal precision to be increasing in the blockholder's individual stake and thus fall with I." |
| 2410 | "Appendix A proves that there is a unique posi[tive root]…" |
| 2411 | "Appendix A proves that there is a unique pos[itive root]…" |

Every hit is a *pointer to* an appendix. None is appendix content. **The last page of the PDF is p. 2428, the end of the
reference list** (references run pp. 2425–2428); the file ends there.

### Consequence for the card

- The header line "**Appendices A–D are NOT in this PDF**" and §9's "Appendices A–D are online-only and could not be obtained"
  are **correct as written and are left unchanged**. No correction was needed.
- The three decision-critical UNCHECKED items at the foot of §9 all **stay open**:
  1. **Appendix A** — proofs of Props. 1, 2 and 7–13, including **Prop. 8**, the paper's only liquidity comparative static and
     our load-bearing citation for "the second canonical liquidity statement is monotone, not humped."
  2. **Appendix D** — the claimed equivalence of `E[dp̃/dṽ]` to the variance-ratio measure of price informativeness.
  3. **Appendices B and C** — imperfect-signal and stake-dependent-precision robustness.
- Also still unproved-in-print, as §9 already records: Props. 5 and 6 print the derivation but defer uniqueness and the
  comparative statics to Appendix A.

### Where the appendices might actually be found (added by supplement reader — not attempted in this pass)

The URL the article gives, `http://www.sfsrfs.org`, is the Society for Financial Studies' pre-2013 host and no longer serves RFS
supplementary files; RFS moved to `academic.oup.com/rfs`. The fetcher separately recorded that OUP's Supplementary-data link on
this article "renders no actual file" — so the OUP route is a dead end too, exactly as for Edmans (2009) (see the
`edmans_2009_internet_appendix` row, NOT FOUND). Two untried routes, in order of likelihood: **(a)** Alex Edmans' own site,
`alexedmans.com/research/`, which hosts working-paper versions — a **pre-publication version would normally carry the
appendices inline**, which is the usual way this class of gap gets closed (WP series and number not verified here); **(b)**
Gustavo Manso's Berkeley faculty page. Either would give a *working-paper* proof, not the published one, so any resulting label must say which version
was read.

**Counts after this pass: UNCHECKED 3 → 3 (unchanged). One external claim REFUTED** — the fetcher's "appendices are embedded"
row. `FETCH_LOG_C.md` was not edited (this pass touches cards only), but that row should not be relied on.
