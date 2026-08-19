# Levit, Malenko & Maug (2024) — "Trading and Shareholder Democracy"

**Venue / status:** Published as *Journal of Finance* 79(1), 257–304, February 2024. **The version we hold and read is the ECGI Finance Working Paper N° 631/2019 (revised), March 2024** (the ECGI cover page prints the series number as "631/20219", an obvious typo); SSRN abstract id 3463129. Previously circulated as "Trading and Shareholder Voting". Editor: Wei Xiong; an Associate Editor and two anonymous referees are thanked, so this is the accepted version.
**Which version was read, and the page numbers:** the ECGI/SSRN typeset version. **The JF page numbers 257–304 are absent from the body.** They appear once, on the paper's own title page (PDF p. 4: "Journal of Finance, 79 (1), 257-304, February 2024"), and nowhere else; the body restarts its own pagination at 1 and runs to p. 53 (main text pp. 1–47, references pp. 48–53) — **corrected by verifier; the card originally said "to p. 51" and "references pp. 48–58"**. **All page citations in this card are to that internal numbering (printed p. = PDF page − 4), NOT to JF pages.** To convert to JF, add roughly 256, but do not do so without checking against the published article — the WP and JF typesettings differ.
**Full text from:** `lit/levit-malenko-maug-2024-ecgi.pdf` (60 PDF pages) re-extracted with `pdftotext -layout`; `research/txt/levit_malenko_maug_jf2024.txt` is the same document · **Reader:** opus · **Read:** full text, 60 PDF pages (cover, title page, Sections I–VII, Appendix proofs, references)
**Internet Appendix:** not in the original file read; **since fetched and read in full** (`research/txt_extracts/lmm_2024_internet_appendix.pdf`, 81 pp.) — see **§9b**. It carries Sections I.A–I.D (index investors, E&S, post-vote trading, delegation vote), II.A–II.D (generalised preferences, bias-varying `e` and `x`, partial sales, welfare weights), III.A–III.D (the four applications), and IV.A–IV.B (coordinated voting; conservative-equilibrium proofs). Every Section V extension and several conservative-equilibrium proofs live there. Results whose proof is only in the Internet Appendix are labelled accordingly below, now with the IA section and page confirmed.
**Extraction note:** the PDF embeds fonts with a broken ToUnicode map — `fi`→"…", `ff`→"¤", `ffi`→"¢ ", `fl`→"‡". These were repaired deterministically before quoting (verified word-by-word on ~450 instances). The extraction also intermittently drops the space after a curly apostrophe ("shareholders’trading") and drops Greek symbols entirely; quotes below were chosen to avoid both. Words hyphenated across a line break in the source (e.g. "complemen-tary", "concen-trated", "nonfundamen-tal") are joined in the quotes; that is the only other departure from the raw extraction.
**Type:** theory   **Role for us:** template (the "theory + empirical implications" architecture) + antecedent on liquidity-and-governance; **not** a competitor on our margin

## 1. Question

Does shareholder voting actually raise shareholder welfare once you allow the shareholder base to be *chosen* — that is, once investors trade into and out of the firm ahead of the vote based on what they expect the vote to do? Their answer is a qualified no. The corporate setting differs from the political one precisely because there is a market for the votes' carrier (the share), so who votes is endogenous to what the vote is expected to decide. They argue this feedback loop generates multiple equilibria, drives a wedge between prices and welfare, and can make *reducing* trading frictions welfare-destroying.

## 2. Model / data and method

**Primitives.** A firm with a continuum of measure one of risk-neutral shareholders, each endowed with `e > 0` shares. A binary proposal: baseline policy if rejected (`d = 0`), alternative if accepted (`d = 1`). An unknown common-value state; a shareholder-specific private value ("bias") `b` drawn from a differentiable cdf `G` with full support and positive density on a bounded interval. Share value to a type-`b` holder is **linear**: `v(d, θ, b) = v₀ + (θ + b)(d − γ)` (eq. 1, printed p. 9), with `γ ∈ [0,1]` a disagreement parameter and `v₀` large enough to keep value non-negative. High-`b` holders are labelled **activist**, low-`b` **conservative**.

**Timing.** Two stages, **trade then vote** (printed pp. 9–10). At the trading stage all shareholders are uninformed and share the same prior. **After the market clears but before voting, a public signal arrives**: `q = E[θ | public signal]`, distributed by cdf `F` with mean zero and full support, and `H(q) ≡ 1 − F(q)`. There is **no asymmetric information at any point**. Each share has one vote; the proposal passes if more than a fraction `β ∈ (0,1)` of shares are voted in favour. Equilibrium concept: **subgame-perfect Nash equilibrium in undominated strategies** of the induced voting game, which makes type `b` vote for the proposal iff `b + q > 0` (eq. 3, printed p. 11).

**The trading friction — this is their "liquidity".** No short sales; a shareholder may sell up to his endowment `e` or buy up to a **fixed finite quantity `x`**. Market depth is defined as `δ = x/(x+e)` (eq. 8, printed p. 17), and "an increase in `δ`" is what they call *relaxing trading frictions* (printed p. 18). There is **no market maker, no noise trader, no price impact, no adverse selection, no Kyle-style camouflage** — the price is a Walrasian market-clearing price and the only informational event is public and post-trade. **(added by verifier — important)** In footnote 12 (printed p. 10) they say the quantity cap can be swapped for the quadratic trading cost of Levit, Malenko & Maug (2023) — the paper published as LMM (2026), "The Voting Premium" — and that "**Our main results would also obtain under this alternative specification.**" So the authors themselves treat cap-liquidity and cost-liquidity as interchangeable *for their results*. A referee can lean on that sentence, so our own "their δ is not our κ" line has to be about the *informational* role of liquidity (camouflage), not about the functional form.

**Functional forms and devices that buy tractability** (this is what makes the paper work):
1. **Linearity of `v` in `b`.** This is the load-bearing assumption: it is exactly what makes shareholder welfare equal the valuation of the *average* post-trade shareholder (Lemma 2, printed p. 23) rather than some non-linear aggregate.
2. **Private values tied to ownership** — utility from the proposal scales with shares held. They flag this themselves: "This assumption is key to our analysis" (printed p. 8).
3. **Corner trading.** Everyone either buys exactly `x` or sells all of `e`. Market clearing then collapses to a quantile condition, `G(b_a) = δ`, so the **marginal shareholder is `b_a = G⁻¹(δ)`** — a pure quantile of the bias distribution (eq. 7, printed p. 17). The **median voter is likewise a quantile**, `−q_a = G⁻¹(1 − β(1 − δ))` (eq. 10, printed p. 20). Every comparative static in the paper is then a statement about how two quantiles of `G` move.
4. **Public signal after trading, no private information.** Deliberately removes information aggregation so the endogenous-shareholder-base channel stands alone.
5. **Tie-breaking**: no trade when indifferent, which kills the knife-edge equilibrium.
6. **Undominated strategies** ("vote as if pivotal"), standard in voting games, rules out trivial equilibria.

**Method:** pure theory. No data, no estimation, no calibration, no numerical grid. Figures 1–4 are schematic plots of `G` and of `v`, not computed examples.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | Voting always takes a cutoff form: the proposal passes iff `q > q*` | PROVED | printed p. 14, Lemma 1; proof p. 40 |
| R2 | Voting without trading: unique equilibrium, cutoff `q_NoTrade = −G⁻¹(1−β)` (the median voter is the `(1−β)`-quantile of the pre-trade base) | PROVED | printed p. 15, Proposition 1; proof "provided in the main text" |
| R3 | Trading without voting (board decides): unique equilibrium, **activist** if `H(q*) > γ` (activists buy, marginal shareholder `b_a = G⁻¹(δ)`), **conservative** if `H(q*) < γ`, no trade in the knife-edge case | PROVED | printed pp. 16–17, Proposition 2; proof pp. 40–41 |
| R4 | The marginal shareholder becomes more extreme as depth rises (`b_a ↑ δ`, `b_c ↓ δ`); `b_c < b_a` iff `δ > 0.5` | PROVED | printed p. 18, Corollary 1 |
| R5 | **Trading and voting: multiple equilibria.** An activist equilibrium exists iff `H(q_a) > γ`, a conservative one iff `H(q_c) < γ`, and no others exist; an equilibrium always exists | PROVED | printed p. 20, Proposition 3; proof pp. 41–42 |
| R6 | The **median voter is always more extreme than the marginal shareholder**, and becomes more extreme as depth rises; as `δ → 1` both converge to the most extreme type | PROVED | printed p. 21, Corollary 2 |
| R7 | **Welfare = the valuation of the average post-trade shareholder** (and pre-trade welfare equals post-trade welfare) | PROVED | printed p. 23, Lemma 2; proof p. 42 |
| R8 | "Implications" 1–3: post-trade ownership is inefficient; preferences stay heterogeneous so median voter ≠ average shareholder; prices reflect the marginal, not the average, shareholder | ASSERTED (interpretive framing devices, not numbered theorems, though each follows from R3–R7) | printed p. 24, Implications 1–3 |
| R9 | Removing the trading friction entirely (`δ → 1`) raises **both** welfare and price relative to the corresponding equilibrium with frictions | PROVED | printed p. 24, Proposition 4; proof pp. 42–43 |
| R10 | Multiplicity conditions: the two equilibria coexist if the market is liquid (high `δ`), the majority requirement is intermediate, shareholder heterogeneity is not too small, and `γ` is intermediate | PROVED | printed p. 26, Proposition 5; proof p. 43 |
| R11 | Price is maximised when the median voter coincides with the **marginal** shareholder; welfare when he coincides with the **average post-trade** shareholder | PROVED | printed p. 28, Lemma 3 |
| R12 | **Prices and welfare move in opposite directions** for a small parameter change that shifts the median voter without shifting the marginal or average shareholder | PROVED | printed p. 28, Proposition 6; proof p. 43 |
| R13 | A small change in the **majority requirement** `β` that raises the share price necessarily lowers shareholder welfare (and vice versa) | PROVED | printed p. 29, Corollary 3 |
| R14 | With a board (no voting friction) the equilibrium is constrained efficient and welfare **increases** in depth | PROVED | printed p. 30, Lemma 4; proof pp. 43–45 |
| R15 | **With voting, welfare can decrease in depth**: if the no-trade median voter is more extreme than the average shareholder and `|H(q_NoTrade) − γ|` is small, there is a `δ̲ > 0` such that welfare falls in `δ` for `δ < δ̲` (the proof also gives a price threshold `δ̄`) | PROVED | printed p. 31, Proposition 7; proof pp. 45–46 |
| R16 | The **optimal board is always biased** (`−b_m ≠ E[b]`); delegation strictly beats voting except in the knife-edge case where the average post-trade shareholder is the median voter | PROVED | printed p. 33, Proposition 8; proof pp. 46–47 |
| R17 | Coordinated voting (shareholders maximise post-trade welfare) restores constrained efficiency, so the inefficiency in R15 comes from voting *externalities*, not from the decision rule being endogenous | PROVED — **confirmed in IA §IV.A: Prop. IA.18 (IA p. 76), Lemma IA.6 + proof (IA pp. 77–78)** | printed pp. 31–32 |
| R18 | Shareholders may fail to vote to delegate to the optimal board (a collective action problem driven by short-term trading motives) | PROVED — **confirmed in IA §I.D.3: Prop. IA.9 (IA p. 33), proof (IA pp. 35–38)** | printed p. 33 |
| R19 | **Index investors** (vote, do not trade) leave the marginal shareholder unchanged but moderate the median voter; index ownership has a **non-monotonic** effect on price and can raise price while lowering welfare; enough index ownership makes the equilibrium unique | PROVED — **confirmed in IA §I.A: Prop. IA.1 (IA pp. 2–3), Cor. IA.1 (IA p. 4), Prop. IA.2 (IA p. 4), proofs (IA pp. 5–8)**. One qualifier: the *uniqueness as μ→1* half is prose (IA p. 1), not a numbered claim — it follows from Prop. IA.2 because q_a(μ) and q_c(μ) both collapse to q_NoTrade | printed pp. 34–35, Section V.A |
| R20 | **Social (E&S) concerns** amplify biases, make multiple equilibria more likely, and can lower the share price | PROVED — **confirmed in IA §I.B: Prop. IA.3 (IA p. 10), Cor. IA.2 (IA p. 10), Cor. IA.3 (IA p. 11), Prop. IA.4 (IA p. 13), proofs (IA pp. 12–14)** | printed pp. 35–36, Section V.B |
| R21 | **Post-vote trading does not remove the voting friction**; average price and welfare *reactions to proposal approval* can have opposite signs | PROVED — **confirmed in IA §I.C: Prop. IA.5 (IA p. 19), Prop. IA.6 (IA p. 21), derivations IA pp. 15–21; §I.C.2 (IA pp. 22–26) adds the efficiency analysis** | printed pp. 36–37, Section V.C |
| R22 | Empirical predictions: abnormal volume/turnover before important votes; event-study returns unreliable as welfare proxies, especially for **close votes** and **illiquid** shares; nonfundamental indeterminacy more likely in liquid firms and for E&S proposals, less likely with high index or insider ownership | ASSERTED (predictions; the supporting evidence cited is other authors' published work, not estimated here) | printed pp. 37–39, Section VI |

## 4. Institutional facts used

The paper leans on institutional detail mainly to justify its **timing**, not to identify anything. There is **no legal rule with a threshold or a window** anywhere in it.

- **The record date.** The model's trade-then-vote order "puts the record date, that is, the date that determines who is eligible to vote, after the trading stage", which they say "applies to all votes on important issues such as mergers and acquisitions (M&As), proxy fights, special meetings, and high-profile shareholder proposals, which are known well ahead of the record date" (printed p. 11). Reversing the order would produce **empty voting**, which they explicitly exclude (Q4).
- **Proxy advisor recommendations** are the concrete instance of the public signal `q`: "released about one month after the record date on average", citing Figure 1 of Li, Maug & Schwartz-Ziv (2022) (printed p. 11).
- **Majority requirement `β`.** Interpreted not just as the statutory threshold but as "the power of the CEO, the independence of the board, and shareholder rights"; footnote 13 notes most firms use simple majority but many retain supermajority requirements for mergers and charter amendments (printed p. 10).
- **Index-fund voting weight:** "the Big-3 index fund families alone collectively cast about 25% of the votes at S&P 500 firms (Bebchuk and Hirst, 2019)" (printed p. 34).
- **E&S share of proposals:** "about 30% of shareholder proposals in recent years are related to E&S issues (Bolton et al., 2020; Bubb and Catan, 2022)" (printed p. 35).
- **Evidence cited as consistent** (all second-hand, none re-estimated): Cox, Mondino & Thomas (2019) on ownership turnover after M&A announcements predicting deal approval; Li, Maug & Schwartz-Ziv (2022) on volume around votes and on losers reducing holdings afterwards; Listokin (2009) on median voters valuing management control more than marginal shareholders (footnote 24, printed p. 28); Bonnefon et al. (2019) on ownership-tied E&S utility (printed p. 13).
- Mutual-fund vote-disclosure reform (Davis & Kim 2007; Cvijanovic, Dasgupta & Zachariadis 2016) is cited once in footnote 1 (printed p. 1) as background on shareholder empowerment — **this is the only appearance of anything resembling a disclosure rule, and it is about fund voting records, not stakes.**

## 5. Referee-facing strengths / weaknesses

**Strengths.**
- The central object is genuinely new and cleanly isolated: the shareholder base is a *choice variable*, and the model shows that trading and voting are complementary in a way that makes expectations self-fulfilling.
- The quantile structure (`b_a = G⁻¹(δ)`, median voter a quantile too) is elegant and makes every comparative static transparent — the whole paper is about the distance between three points on one distribution: marginal shareholder, median voter, average post-trade shareholder.
- The most useful result for empiricists is a *negative* one — prices are not a valid welfare proxy — and they do not stop there: Section VI says exactly when the failure is worse (close votes, illiquid shares, E&S issues) and when it is milder. That is the discipline our own empirical spec should copy.
- **(added by verifier)** They are willing to end on a normative claim, and it is a blunt one: "Overall, our paper suggests caution in the move to more shareholder democracy. The parallelism to political democracy breaks down in one important respect: shareholders can trade, and trading may exacerbate, rather than alleviate, the collective action problems of the shareholder voting process" (printed p. 39, §VII). A JF theory paper with no data is allowed to close with a policy sentence — useful precedent for our own conclusion.
- The Proposition 4 / Proposition 7 pair is the paper's sharpest move: removing the friction *entirely* is good, but *loosening* it can be bad. Non-monotonicity is proved, not asserted.
- ~~Every main-text result carries a proof.~~ **Corrected by verifier: not so.** The printed Appendix (pp. 40–47) opens "The appendix contains proofs of the main results. Proofs of the supplementary results and extensions are in the Internet Appendix" and then proves Lemmas 1, 2, 4 and Propositions 2–8 (Prop. 1 "is provided in the main text"). **Lemma 3 (p. 28) and Corollaries 2 (p. 21) and 3 (p. 29) carry no proof at all**, and — more seriously — **the conservative-equilibrium half of Lemma 2, Proposition 6 and Proposition 7 is relegated to Internet Appendix §IV.B** ("the proof for the conservative equilibrium is similar and for brevity is presented in Section IV.B of the Internet Appendix", pp. 42, 43, 46). So half of three main results is unverifiable from the printed article. **(supplement reader, 2026-08-19: now closed.** IA §IV.B, "Supplementary Analysis for the Proofs of the Baseline Results", IA pp. 78–80, carries all three conservative-equilibrium proofs in full: Lemma 2 (IA p. 79), Prop. 6 (IA p. 79), Prop. 7 (IA pp. 79–80, eqs. IA89–IA90, both the δ→1 and δ→0 limits). The decision-critical one — welfare falling in depth at low δ in the conservative equilibrium — reaches the stated claim. **Their hump is fully PROVED.)**

**Weaknesses / open flanks.**
- **The trading friction is a quantity cap, not a market.** `x` is exogenous, identical across investors in the baseline, and has no price. There is no liquidity provider, no price impact, no informed trading. A referee can reasonably say the paper's "liquidity" is an ownership constraint wearing liquidity's clothes — and LMM half-concede it by pointing to Levit, Malenko & Maug (2023) for a quadratic-trading-cost specification instead (footnote 12, printed p. 10), while claiming the results survive the swap.
- **Corner trading is doing heavy lifting.** Everyone buys `x` or sells everything. Interior positions would break the clean quantile characterisation; the Internet Appendix relaxes some of this but we cannot check it from the file we hold.
- **Multiplicity is unresolved.** They offer no selection device, only speculation about media visibility and proxy advisors coordinating expectations (footnote 23, printed p. 26). Section VI then converts the multiplicity into an *excuse* for mixed empirical evidence, which a sceptical referee will read as unfalsifiable.
- **No asymmetric information at all.** Given the authors' own literature (Levit & Malenko on voting, the whole strategic-voting tradition), the absence of private information is a deliberate but large abstraction: nothing in this model is about learning.
- **Welfare is defined as the average valuation of the initial shareholders.** Defensible (they invoke Rawls/Hayek behind a veil of ignorance, footnote 20, printed p. 23), but it means "welfare" excludes every non-shareholder and, in the baseline, every consideration beyond ownership-scaled private value.
- **Half the paper is in an Internet Appendix.** All of Section V and several conservative-equilibrium proofs live outside the published PDF — an 81-page IA against a 47-page body. **(supplement reader)** The IA has now been read; everything the body claims is there is there. But the *distribution* is itself a referee-facing fact: a JF theory paper is allowed to put five extensions and three half-proofs online. That is precedent for our own draft_v3 appendix budget.
- **(added from IA by supplement reader) The inefficiency needs an ownership constraint to exist at all.** IA §I.C.2, IA p. 26: "Therefore, externalities in voting create inefficiency if and only if there is a restriction on ownership." Without the position cap (ē → ∞) the most extreme shareholder buys everything post-vote, marginal and average shareholder coincide, and the voting friction vanishes. Their entire result set is a theorem about a *position constraint*, not about liquidity as such.

## 6. What they do NOT do (scope boundary)

**Object.** Voting outcomes, share price, and shareholder welfare — specifically the gap among three statistics of the post-trade bias distribution. **Not** takeover premium, **not** bidder entry, **not** campaign success, **not** announcement returns as an estimand (announcement returns appear only as a *tool they criticise*).

**Margin.** **None.** No disclosure rule, no stake threshold, no filing window, no Schedule 13D, no Williams Act, no 5%. A full-text search for "13D", "Williams", "Schedule", "toehold", "filing", "window", "business day" and "bidder" returns **nothing** (verifier-confirmed on a fresh `pdftotext -layout` extraction of all 60 pages); "disclos" appears only in the JF conflict-of-interest statement and in fn. 1 about mutual-fund *vote* disclosure. "threshold" appears twice and neither is a disclosure threshold (printed p. 3, the signal cutoff; printed p. 10 fn. 13, Levit & Malenko's "endogenously determined voting threshold"). The one date-like institution in the paper is the **record date**, and it is used to justify timing, not as a treatment.

**Liquidity.** Present but in a specific and limited sense: **market depth `δ = x/(x+e)`**, a cap on how many shares an investor may accumulate. No noise trading, no Kyle (1985), no price impact, no market maker, no adverse selection — the only information event is public and arrives *after* trading. When Section VI says "liquid", it means "few barriers to trade", i.e. high `δ` (printed p. 38).

**Takeovers.** Appear **four** ways (fourth added by verifier), none of them as an object of study: (i) as related literature — "Our model also has similarities to models of takeovers … it features a stage in which shares change hands, followed by a stage in which a decision is made by the party in control", but "Different from models of takeovers, decisions are not dictated by a controlling shareholder" (printed pp. 7–8, Q5); (ii) as an *application* — a target's shareholders voting on a merger, facing "a trade-off between selling the firm now for a large premium and keeping it independent" (printed p. 12); (iii) as a proposal type — removing antitakeover defences (printed p. 12). and (iv) **(added by verifier)** as a *coordination analogy*: "However, as in models of tender offers (e.g., Grossman and Hart, 1980), coordination problems in trading prior to decision-making introduce inefficiencies and equilibrium multiplicity" (printed p. 8). That is the sentence in which they touch the free-rider problem — and it is the closest they come to our object. No bidder, no tender-offer game, no premium as an endogenous object. (`bidder` returns zero hits in the whole document; `tender` returns exactly one, the Grossman–Hart line above; `premium` returns four, none of them a takeover premium they model.)

**Explicitly excluded, in their words.**
- **Empty voting / vote-trading**: "we abstract from vote-trading and assume one-share-one-vote throughout" (printed p. 7, Q3) and "we do not analyze such 'empty voting'" (printed p. 11, Q4).
- **Other costs and benefits of delegation**: "we abstract from other benefits of delegation (e.g., specialized knowledge) or costs of delegation (e.g., agency problems)" (printed p. 5).
- **Asymmetric information**: "the signal is public and there is no asymmetric information" (printed p. 2, Q2).
- **Multi-dimensional preferences**: one bias parameter, one proposal, defended as "legitimate abstractions" given the empirical factor structure (printed p. 13).
- **Blockholders**: the endogenous-block literature is cited and set aside — "the majority of this literature focuses on models with a single blockholder" (printed p. 7); LMM's own agents are atomistic.
- **Complete preference independence from ownership** in the E&S extension: "we do not allow for the extreme case in which preferences are completely independent of ownership" (footnote 26, printed p. 35).

**(added from IA by supplement reader — the IA hardens every scope claim above.)** The 81-page Internet Appendix returns **zero** hits for `noise`, `Kyle`, `market maker`, `price impact`, `block`, `disclos`, `13D`, `tender`, `toehold`, `illiquid` and `bid-ask`. `liquidity` appears once (IA p. 29, an IPO owner who "needs liquidity"); `transaction cost` once (IA fn. 2, p. 3, conceding that the model does not capture the diversification and transaction-cost benefits of index investing); `takeover` twice (IA p. 58, the proxy-fight/merger application, and an antitakeover-defence example); `premium` once (IA p. 58, "selling the firm now for a large takeover premium"). **There is no microstructure and no disclosure rule anywhere in the 128 pages of body plus appendix.**

**(added from IA) But four things the IA does that the body does not, and that touch our object:**
1. **The inefficiency is a theorem about an ownership constraint.** IA §I.C.2, IA p. 26: "externalities in voting create inefficiency **if and only if** there is a restriction on ownership." Lift the cap (`ē → ∞`) and the most extreme shareholder buys the whole float post-vote, marginal = average, and the friction disappears. A disclosure rule is *exactly* a legally imposed constraint on position size — so LMM have, without naming it, proved that the class of friction our paper studies is the class that makes voting inefficient.
2. **They separate buy-side from sell-side frictions.** IA §II.C (IA pp. 46–56) lets shareholders sell only `y ≤ e`. This "allows us to separate the effect of market depth (captured by `x` and `y`) from the effects of `x/y`, which captures the asymmetry between trading frictions on the buy side and those on the sell side" (IA p. 47). Two findings we must know: as `y → 0` the equilibrium becomes **unique** and converges to the no-trade benchmark; and with a tight sell-side friction the **median voter can be *less* extreme than the marginal shareholder**, reversing the baseline's Corollary 2. **Prop. IA.13 (IA p. 50) re-proves the welfare-falls-in-depth result for symmetric frictions `x = y`.** A disclosure threshold is a buy-side asymmetry; LMM have already shown their results survive one.
3. **The proxy-fight / merger-vote application is in the IA, not the body.** IA §III.A "Investor Horizon" (IA pp. 58–64) is set up around exactly our institutions — "Proxy contests, together with contentious M&A deals, are the most important issues that shareholders vote on" (IA p. 58) — with the trade-off "between selling the firm now for a large takeover premium to rejecting the offer, keeping the firm independent" (IA p. 58). **Cor. IA.5 (IA p. 62): "The median voter becomes more extreme as market depth increases"**, and the welfare effect of depth can again be negative. This is the closest LMM come to a control outcome, and it is in an appendix.
4. **Private benefits of control are microfounded in the IA too** (§III.C, IA pp. 66–71) and disagreement in §III.D (IA pp. 71–75), with Prop. IA.17 (IA p. 74) mapping the price-vs-welfare result onto heterogeneous priors.

**Identification.** Theory only. Section VI is predictions plus a methodological warning; the supporting evidence is other people's published estimates.

## 7. Implications for our position

**What they occupy:** object = voting outcome / price / shareholder welfare; margin = none (record date used for timing only); identification = theory, with a *prescriptive* empirical section. Their liquidity variable is a quantity cap, not noise-trading intensity.

**A. They are our template, and the task brief is right to call them the taste-setter. Here is the architecture of Section VI, printed pp. 37–39, in the order they use it — copy this shape for draft_v3.**
1. **Scope condition first.** One sentence delimiting when the theory bites: the implications "are most relevant for votes that are sufficiently important to affect shareholders' trading decisions" (printed p. 37). They fence the claim before making it.
2. **One positive, falsifiable prediction**, stated plainly (abnormal volume and turnover in the shareholder base before important votes), immediately followed by **two named papers whose existing findings match it** (Cox, Mondino & Thomas 2019; Li, Maug & Schwartz-Ziv 2022) — Q6. They do not run a regression; they show the prediction is already partly borne out.
3. **A methodological result aimed at the reader's own toolkit.** Their price ≠ welfare finding is turned into a warning about event studies of votes, with the sharpest possible statement of the cost: "the researcher may sometimes not only obtain a biased estimate of the real effect of the proposal, but even get the wrong sign of the effect" (printed p. 30, Q7). **(verifier note)** Q7 sits in §IV.B, not in §VI; §VI merely *points back* to it ("an important limitation to conventional inferences from event studies of shareholder votes (see Section IV.B)", printed p. 37). The template move is therefore: prove the result in the body, then re-state it as a tool warning in the implications section — do not save the punchline for §VI.
4. **Then, crucially, the conditions under which the warning is weaker** — they tell the empiricist when the standard tool is still usable, rather than only when it fails: less heterogeneous post-trade base, which happens "when the firm's shares are sufficiently liquid" (Q8), and for issues involving clear shareholder-vs-management conflict rather than E&S.
5. **A new cross-sectional moderator with an off-the-shelf proxy: the vote tally.** "event-study returns are less reliable as indicators of shareholder welfare when voting results are close" (printed p. 38, Q9). This is the single best move in the section — a testable interaction that requires no new data.
6. **A timing robustness note** tied to institutions: the conclusion survives short event windows provided the pre-vote trade happens after the record date (printed p. 38).
7. **Finally, the awkward prediction (multiplicity) handled honestly**: it is an *empirical challenge*, and they say where it bites — "less likely in firms that have a large proportion of long-term, nontransient shareholders (e.g., firms with high index fund ownership, or with high insider ownership) and … more likely in firms with liquid shares" (printed p. 38, Q10), and more likely for E&S proposals.

**Proxies they name, in one list** (all standard, all available): trading volume / turnover around the vote; ownership change between announcement and record date; index-fund ownership; insider ownership; share liquidity ("few barriers to trade"); the vote tally / margin of approval; proposal type (E&S vs. governance vs. shareholder-management conflict); the record date; proxy-advisor recommendation dates. **Nothing exotic. That is the point.** Our own empirical spec should aim at the same profile: a handful of named, boring proxies, one clean prediction, one interaction, and an explicit statement of when our design fails.

**B. What this constrains for us.**
- **We must not describe their `δ` as our `κ`.** Their market depth is a cap on accumulation; our `κ` is noise-trading intensity, which buys *camouflage* for an informed trader. Different economics, opposite informational roles (their signal is public and post-trade; ours is private and pre-trade). If a referee conflates them, we should have the distinction in one sentence: LMM's liquidity determines *who ends up holding*, ours determines *what the market can infer*. **(added by verifier)** Note that the functional-form defence is not available to us — fn. 12 (printed p. 10) says their results survive replacing the cap with a quadratic trading cost, and LMM (2026) then runs on exactly that cost. The distinction has to be informational or it does not exist.
- **They have already claimed "more liquidity can hurt governance".** Proposition 7 owns the non-monotone welfare-in-liquidity result in the voting context. Our "hump" (draft_v2's R1, non-monotone minority gains in `κ`) must be positioned as a *different* mechanism — partition/inference, not median-voter extremism — or it will read as a re-derivation. Note that our hump is NUMERICAL and theirs is PROVED; that asymmetry is a live referee risk.
- **They have also pre-empted the naive event-study reading of our own empirical leg.** If our clean result is an announcement-return or premium event study around the Feb-2024 acceleration, LMM is the citation a referee will reach for to say returns ≠ welfare. Best response: our object is the **takeover premium / control outcome**, which is a transfer to selling shareholders and not a welfare proxy in their sense, and say so explicitly.
- **(added from IA by supplement reader) Our best separation is now sharper, and it is *legal*, not functional.** LMM's own IA says the inefficiency exists **iff** there is a restriction on ownership (IA p. 26), and their §II.C shows the results survive making that restriction asymmetric between buying and selling. Our disclosure rule is a restriction on ownership that is (i) *legally* imposed rather than technological, (ii) *asymmetric* (it bites on accumulation, not on exit), (iii) *informational* (crossing it changes what the market knows, which nothing in LMM does), and (iv) has a *dated* change we can use for identification. Items (i), (iii) and (iv) are ours; item (ii) is already occupied by IA §II.C, so do not claim asymmetry as the novelty.
- **(added from IA) Do not claim the merger-vote / proxy-fight application as whitespace.** IA §III.A already runs the model on a proxy contest and on a merger vote with a takeover premium, and Cor. IA.5 (IA p. 62) gives the depth comparative static there. What is *not* there: a bidder, an endogenous premium, a free-rider condition, or any disclosure. Our claim must be the endogenous *control outcome*, not the application setting.
- **The record date is the only institutional timing device they use — and it is the structural cousin of our window margin.** Both are a legally fixed date after which trading no longer changes what the market or the electorate sees. That parallel is worth one sentence in our introduction: LMM show what a fixed *voting* cut-off does to the shareholder base; we ask what a fixed *disclosure* cut-off does to the trading path and the control outcome.

**C. What this supports.**
- **Whitespace confirmed on the disclosure margin.** Two of the strongest recent theory papers in this space (LMM here, Burkart–Lee–Voss) have *no* disclosure rule. Neither the threshold margin nor the window margin is occupied by either.
- **Endogenous shareholder base is legitimised as a first-order object.** Our partition story needs the market to care who holds the stake; LMM in the JF establishes that the composition of the base is worth modelling, which lowers the burden on us to justify it.
- **"Theory plus empirical implications, without running the empirics in the theory paper" is a JF-acceptable structure.** LMM's Section VI is three pages, cites others' evidence, estimates nothing, and the paper is in the *Journal of Finance*. For the December package — a full draft plus a written empirical spec for the rest — this is precisely the precedent to name.

## 8. Quotes we may lean on (verbatim, page-cited)

Page numbers are the ECGI/SSRN version's internal pagination (see header). Quotes are from the ligature-repaired extraction described above.

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "While the literature looks at many important questions in the context of shareholder voting, to date it has not examined the effectiveness of voting when the shareholder base forms endogenously through trading." | printed p. 1 | Their claim to whitespace — and the shape of a whitespace sentence we can imitate |
| Q2 | "After shareholders trade but before they vote, they observe a signal on the common value of the proposal; the signal is public and there is no asymmetric information." | printed p. 2 | No private information anywhere — the key difference from our setting |
| Q3 | "Our paper is complementary to the above papers, since we abstract from vote-trading and assume one-share-one-vote throughout." | printed p. 7 | Explicit out-of-scope declaration |
| Q4 | "If the record date were prior to the trading stage, then shareholders who sell their shares during trading could still vote – we do not analyze such “empty voting.”" | printed p. 11 | The record date as their only timing institution; empty voting excluded |
| Q5 | "Our model also has similarities to models of takeovers (see Betton, Eckbo, and Thorburn, 2008, for a survey): it features a stage in which shares change hands, followed by a stage in which a decision is made by the party in control." | printed p. 7 | How they place themselves relative to takeover models — adjacency, not overlap |
| Q6 | "One prediction of our model is that we should expect an abnormal volume of trade and large turnover in the shareholder base before important votes." | printed p. 37 | The template: one plain, falsifiable prediction stated in a single sentence |
| Q7 | "By using prices as a proxy for shareholder welfare, the researcher may sometimes not only obtain a biased estimate of the real effect of the proposal, but even get the wrong sign of the effect." | printed p. 30 | The methodological warning our empirical leg must survive |
| Q8 | "This, in turn, is more likely when the firm’s shares are sufficiently liquid: if there are few barriers to trade, post-trade ownership is more concentrated and homogeneous." | printed p. 38 | Their liquidity is "few barriers to trade" — not noise trading |
| Q9 | "Hence, event-study returns are less reliable as indicators of shareholder welfare when voting results are close." | printed p. 38 | The best single line of Section VI: a testable interaction needing no new data |
| Q10 | "As follows from the analysis in Sections IV.A, V.A, and V.B, nonfundamental indeterminacy is less likely in firms that have a large proportion of long-term, nontransient shareholders (e.g., firms with high index fund ownership, or with high insider ownership) and is more likely in firms with liquid shares" | printed p. 38 | The proxy list, and how to state a cross-sectional moderator |
| Q11 | "These implications are most relevant for votes that are sufficiently important to affect shareholders’ trading decisions." | printed p. 37 | The scope condition that opens their empirical section — copy this move |
| Q12 | "Proposition 7 reveals a new force through which financial markets have real effects." | printed p. 32 | They own "more liquidity can hurt governance"; our hump must differ in mechanism |

## 9. Verification log

**Verifier:** opus, 2026-08-19. **Checked against:** a fresh `pdftotext -layout` extraction of
`lit/levit-malenko-maug-2024-ecgi.pdf` (60 PDF pages per `pdfinfo`), page-tagged with printed page
= PDF page − 4 (confirmed against the printed folios: PDF 5 → 1, PDF 57 → 53). The reader's
ligature warning is correct; matching was done on a copy with `…→fi`, `¤→ff`, `¢ →ffi`, `‡→fl`
applied, plus end-of-line hyphen joining and whitespace collapsing.

**Counts: OK 33 · WRONG 2 · MISCITED 0 · UNCHECKED 5.**

### Quotes (§8)
| Q | Verdict | Checked against |
|---|---|---|
| Q1 | OK | printed p. 1 — exact |
| Q2 | OK | printed p. 2 — exact |
| Q3 | OK | printed p. 7 — exact |
| Q4 | OK | printed p. 11 — exact (the source has a hyphen where the card has an en-dash, and no space before "We also assume"; wording identical) |
| Q5 | OK | printed p. 7 — exact |
| Q6 | OK | printed p. 37 — exact |
| Q7 | OK | printed p. 30 — exact |
| Q8 | OK | printed p. 38 — exact |
| Q9 | OK | printed p. 38 — exact |
| Q10 | OK | printed p. 38 — exact, straddling the fn. 28 marker |
| Q11 | OK | printed p. 37 — exact, opens §VI |
| Q12 | OK | printed p. 32 — exact |

Every §6 in-text quotation was also checked and is verbatim at the page cited: "This assumption is
key to our analysis" (p. 8), "we abstract from other benefits of delegation…" (p. 5), "the majority
of this literature focuses on models with a single blockholder" (p. 7), "we do not allow for the
extreme case…" (fn. 26, p. 35), "Different from models of takeovers, decisions are not dictated by
a controlling shareholder" (straddles pp. 7–8, exactly as cited).

### Results (§3)
Every location was re-read in the print. **R1** Lemma 1 p. 14 / proof p. 40; **R2** Prop. 1 p. 15,
proof in main text; **R3** Prop. 2 p. 16, proof pp. 40–41; **R4** Cor. 1 p. 18; **R5** Prop. 3 p. 20,
proof pp. 41–42; **R6** Cor. 2 p. 21; **R7** Lemma 2 p. 23, proof p. 42; **R8** Implications 1–3
p. 24 (ASSERTED — correct, they are labelled "Implication", not theorems); **R9** Prop. 4 p. 24,
proof pp. 42–43; **R10** Prop. 5 p. 26, proof p. 43 — the four coexistence conditions match the
print word for word; **R11** Lemma 3 p. 28; **R12** Prop. 6 p. 28, proof p. 43; **R13** Cor. 3 p. 29;
**R14** Lemma 4 p. 30, proof pp. 43–45; **R15** Prop. 7 p. 31, proof pp. 45–46; **R16** Prop. 8
p. 33, proof pp. 46–47. All **OK**. §2 anchors also **OK**: eq. (1) p. 9, eq. (3) p. 11, eqs. (7)
and (8) both p. 17, eq. (10) p. 20, "an increase in δ … relaxing trading frictions" p. 18.

**WRONG (2), both fixed:**
1. §5 claimed "Every main-text result carries a proof." It does not. Lemma 3 and Corollaries 2 and 3
   have no proof anywhere, and the **conservative-equilibrium half of Lemma 2, Prop. 6 and Prop. 7
   is in Internet Appendix §IV.B** (stated at pp. 42, 43 and 46). This is decision-critical for the
   card's "their hump is PROVED, ours is NUMERICAL" risk assessment: half of Prop. 7 — the
   welfare-falls-in-depth result — is *not* proved in anything we hold.
2. Header pagination: the body runs to printed p. **53**, references pp. **48–53** (the card said
   p. 51 and pp. 48–58, which is internally inconsistent).

### IA-only results (R17–R21) — the section attributions are all correct
Verified from the body's own pointers: R17 coordinated voting → IA **§IV.A** (p. 32); R18 delegation
vote → IA **§I.D** (p. 33); R19 index investors → IA **§I.A** (p. 34); R20 E&S → IA **§I.B** (p. 35);
R21 post-vote trading → IA **§I.C** (p. 36). The header's IA map (I.A–I.D, II.A–II.D, III.A–III.D,
IV.A–IV.B) matches every pointer in the text. The proofs themselves remain **UNCHECKED** — the
Internet Appendix is not in the repo.

### Scope claims (§6) — all confirmed by full-text search of all 60 pages
Zero hits for `13D`, `Williams`, `Schedule`, `toehold`, `filing`, `window`, `business day`, `noise`,
`Kyle`, `market maker`, `adverse selection`, `bidder`. `5%` matches only inside "S&P 500".
`disclos` → 5 hits: the JF conflict-of-interest sentence (twice, on the two title pages) and fn. 1,
printed p. 1, on mutual-fund *vote* disclosure — exactly as the card says. `threshold` → 2 hits,
neither a disclosure threshold. `record date` → 6 hits, all on printed pp. 11 and 38, all timing.
`numerical`, `calibrat`, `simulat` → zero; four figures only. **The card's core scope claims —
liquidity is market depth δ = x/(x+e) with no noise trading / Kyle / market maker; no disclosure
rule, only the record date; takeovers only as literature and as the merger-vote application — are
confirmed.** Header/venue claims confirmed from the front matter: ECGI FWP N° "631/20219" (typo, as
noted), March 2024, SSRN 3463129, Editor Wei Xiong, previously "Trading and Shareholder Voting",
and the JF citation "79 (1), 257-304, February 2024" appearing only on PDF p. 4.

### §VI structure (§7 A) — confirmed, with one correction
§VI runs printed pp. 37–39 and §VII begins on p. 39. The seven-step architecture the card
reconstructs matches the print in that order. One correction applied: Q7 lives in §IV.B (p. 30), not
in §VI; §VI cross-references it (p. 37). The named proxies — volume/turnover, ownership change
between announcement and record date, index-fund ownership, insider ownership, share liquidity, vote
tally, proposal type, record date, proxy-advisor recommendation dates — are all present at pp. 37–39.
Supporting footnotes verified: fn. 13 p. 10 (supermajority), fn. 20 p. 23 (Rawls/Hayek), fn. 23 p. 26
(media visibility and proxy advisors coordinating expectations), fn. 24 p. 28 (Listokin 2009),
fn. 28 p. 38, Bonnefon et al. (2019) p. 13, Big-3 25% p. 34, E&S 30% p. 35.

### Omissions found and added
1. **fn. 12, printed p. 10 — the sentence that matters most for our positioning**: LMM say the
   quantity cap can be replaced by the quadratic trading cost of LMM (2023) — the paper published
   as LMM (2026) — and "**Our main results would also obtain under this alternative specification.**"
   The two liquidity formalisations are, by the authors' own account, interchangeable for their
   results. Added to §2, §5 and §7B: our separation from their δ must be *informational*
   (camouflage for accumulation, which a disclosure rule destroys), because the functional-form
   separation is closed off by this footnote.
2. **printed p. 8 — a fourth appearance of takeovers**, the one the card missed and the closest to
   our object: "as in models of tender offers (e.g., Grossman and Hart, 1980), coordination problems
   in trading prior to decision-making introduce inefficiencies and equilibrium multiplicity."
   Added to §6.
3. **printed p. 39, §VII — they close with a policy recommendation** ("caution in the move to more
   shareholder democracy") and the political-vs-corporate-democracy contrast. Added to §5 as
   precedent: a data-free JF theory paper is allowed a normative closing sentence.
4. **The proof-coverage correction above** — Lemma 3, Cors. 2–3 unproved; conservative halves of
   Lemma 2, Props. 6–7 in IA §IV.B. Added to §5.
5. Search-negative evidence for `bidder` / `tender` / `premium` written into §6 so the scope claim
   is checkable without re-running the greps.

### UNCHECKED
The **Internet Appendix** is not in the repo. Unverifiable: the proofs behind **R17–R21**; the
conservative-equilibrium halves of **Lemma 2, Proposition 6 and Proposition 7** (§IV.B); the
robustness claims for generalised preferences, bias-varying `x` and `e`, partial sales and arbitrary
welfare weights (§II.A–II.D); and the four applications (§III.A–III.D). **Decision-critical among
these: the conservative half of Proposition 7** — the card's §7B leans on "their hump is PROVED and
ours is NUMERICAL", and only half of their hump is proved in the file we hold. Fetching the Internet
Appendix from the JF article page would close it.

**→ SUPERSEDED 2026-08-19: the Internet Appendix has been fetched and read in full. See §9b.
Every item above is closed as PROVED, including the conservative half of Proposition 7.**

**Overall verdict: the card is sound on scope, quotes and results.** Two wrong claims (proof
coverage; body pagination), no fabricated quote, no page slip in any citation, and the three
decision-critical scope claims — depth-as-liquidity with no microstructure, no disclosure rule, and
takeovers only as literature and application — are confirmed by exhaustive search.

---

## §9b. Internet Appendix supplement — 2026-08-19 (opus supplement reader)

Source read in full: `research/txt_extracts/lmm_2024_internet_appendix.pdf` / `.txt`, 81 pages.
**Page convention: IA printed page = IA PDF page** (verified against the page footers). IA pages are cited as "IA p. N" and are *not* comparable to the body's printed pages.

**IA map as read** — §I.A index investors (IA pp. 1–8) · §I.B social concerns (8–14) · §I.C post-vote trading (14–26) · §I.D delegation (26–38) · §II.A generalised value function (39–43) · §II.B heterogeneous endowments/frictions (43–46) · §II.C partial sales (46–56) · §II.D alternative welfare functions (56–58) · §III.A investor horizon (58–64) · §III.B heterogeneous taxes (64–66) · §III.C private benefits (66–71) · §III.D disagreement (71–75) · §IV.A coordination at the voting stage (75–78) · §IV.B conservative-equilibrium proofs (78–80) · references (81). **This matches the body's IA map exactly.**

| Item that was UNCHECKED | Verdict | Where in the IA |
|---|---|---|
| **Lemma 2, conservative half** | **PROVED** — full derivation, reaches `W_c = e/δ · v(β_c, q_c)` | §IV.B, IA p. 79 |
| **Proposition 6, conservative half** | **PROVED** — reaches "necessarily moves prices and welfare in opposite directions" | §IV.B, IA p. 79 |
| **Proposition 7, conservative half** (decision-critical) | **PROVED** — eqs. (IA89)–(IA90); `lim_{δ→1} ∂W_c/∂δ > 0` and `lim_{δ→0} ∂W_c/∂δ < 0` when the median voter is more extreme than the average post-trade shareholder and `|H(q_NoTrade) − γ|` is small. Both halves of the stated claim are reached. | §IV.B, IA pp. 79–80 |
| **R17** coordinated voting restores constrained efficiency | **PROVED** — Prop. IA.18 (IA p. 76), Lemma IA.6 + proof (IA pp. 77–78). Also proves welfare rises in δ under coordination, and the surrounding text states the interpretation the card gives it: the inefficiency is a voting *externality*, not the endogeneity of the decision rule (IA p. 76). | §IV.A |
| **R18** shareholders may fail to vote to delegate | **PROVED** — Prop. IA.9 (IA p. 33), proof IA pp. 35–38, via the short-term price motive (buyers back boards the marginal shareholder dislikes, to lower the price they pay). | §I.D.3–D.4 |
| **R19** index investors | **PROVED** — Prop. IA.1 (IA pp. 2–3: inverted-U price in μ, welfare falling for large μ), Cor. IA.1 (IA p. 4: price up *and* welfare down), Prop. IA.2 (IA p. 4: full equilibrium, "Other equilibria do not exist"), proofs IA pp. 5–8. **One qualifier:** "enough index ownership makes the equilibrium unique" is stated only as prose (IA p. 1); it follows from Prop. IA.2 (both `q_a(μ)` and `q_c(μ)` collapse to `q_NoTrade`) but is not a numbered claim. Card label narrowed accordingly. | §I.A |
| **R20** social / E&S concerns | **PROVED** — Prop. IA.3 (IA p. 10), Cor. IA.2 (IA p. 10, multiplicity more likely for large λ), Cor. IA.3 (IA p. 11, price falls), Prop. IA.4 (IA p. 13), proofs IA pp. 12–14. | §I.B |
| **R21** post-vote trading | **PROVED** — Prop. IA.5 (IA p. 19, unique equilibrium with two trading rounds), Prop. IA.6 (IA p. 21, welfare and price reactions have opposite signs iff `E[b|b>b₁] > −E[θ|q > q_a] > −b₁`), derivations IA pp. 15–21. §I.C.2 (IA pp. 22–26) adds the efficiency analysis and the "iff there is a restriction on ownership" result. | §I.C |
| §II.A–II.D robustness (generalised preferences, heterogeneous endowments, partial sales, welfare weights) | **PROVED** — Lemma IA.2 + Prop. IA.10 (IA pp. 40–41), Prop. IA.11 (IA p. 45), Props. IA.12–IA.13 + Lemmas IA.3–IA.4 (IA pp. 49–56), §II.D (IA pp. 56–58). | §II |
| §III.A–III.D applications | **PROVED** — Prop. IA.14 + Cor. IA.5 (IA pp. 60–62), Prop. IA.15 (IA p. 65), Prop. IA.16 + Lemma IA.5 (IA pp. 68–69), Prop. IA.17 (IA p. 74). | §III |

**Nothing in the 2024 Internet Appendix is left UNCHECKED.** No claim the body attributes to the IA was missing, mislocated, or unproved.

**Material additions made from the IA** (all marked in place):
- §5 — the proof-coverage weakness is now closed: their non-monotone welfare-in-depth result is fully PROVED, so the card's "their hump is PROVED, ours is NUMERICAL" risk stands at full strength.
- §5 / §6 — IA §I.C.2, IA p. 26: **"externalities in voting create inefficiency if and only if there is a restriction on ownership."** The single most useful sentence in the appendix for us.
- §6 — IA §II.C: market depth is separated from buy/sell asymmetry; `y → 0` gives uniqueness; the median voter can be *less* extreme than the marginal shareholder; **Prop. IA.13 (IA p. 50) re-proves welfare-falls-in-depth for symmetric frictions.**
- §6 — IA §III.A: the proxy-contest and merger-vote applications, with **Cor. IA.5 (IA p. 62), "The median voter becomes more extreme as market depth increases."**
- §6 — negative-search evidence at IA level: zero hits for `noise`, `Kyle`, `market maker`, `price impact`, `disclos`, `13D`, `tender`, `toehold`, `block`.
- §7B — two new constraint bullets: our separation must be legal + informational + dated (asymmetry alone is taken by §II.C), and the merger-vote *application* is not whitespace.
