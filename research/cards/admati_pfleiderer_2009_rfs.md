# Admati & Pfleiderer (2009) — "The ’Wall Street Walk’ and Shareholder Activism: Exit as a Form of Voice"

**Venue / status:** Review of Financial Studies 22(7), 2645–2685, 2009 (doi:10.1093/rfs/hhp037; Advance Access 18 May 2009). Earlier circulated as "The ’Wall Street Walk’ as a form of Shareholder Activism."
**Full text from:** `research/txt_extracts/admati_pfleiderer_2009_rfs.pdf` / `.txt` (published OUP PDF, 41 pp) · **Reader:** opus · **Read:** full text, 41 pages (body §1–§8, Appendix proofs, references)
**Type:** theory   **Role for us:** antecedent

**Page numbering:** printed journal pages 2645–2685 of the RFS version named above (PDF page *N* = printed page 2644+*N*). Quotes are copied from the text layer; where the PDF's justification hyphenates a word across a line break the hyphen and line break are closed up (e.g. "informa- tion" → "information"), and line breaks inside a sentence are rendered as single spaces. No other alteration. The paper's model labels carry superscripts/subscripts (model B^a, B^{a,δ}, B_a^{a,δ}); the PDF text layer flattens these, so in quotes below they appear as the paper prints them minus the raising/lowering.

## 1. Question
Can a large shareholder discipline a manager purely by the *threat* of selling ("voting with her feet"), without any costly monitoring? The authors ask four questions in sequence (p. 2646): is the threat credible when exit itself drives the price down and so hurts the seller; does the threat always help or can it backfire; does *more* private information for the blockholder always help; and does the threat survive extra costs of exiting. Their motivation is the standard claim that liquidity is bad for governance because it makes walking away easy (Bhide 1993; Coffee 1993) — they want to show exit is itself a form of voice.

## 2. Model / data and method
Three dates (Periods 0, 1, 2). All agents risk neutral; prices set by competitive risk-neutral market makers.

- **Primitives.** Manager M chooses an action after privately observing δ̃ ≥ 0, drawn from a continuous density f on [0, δ̄]. Two agency problems, analysed side by side: **model B** ("bad" action) — the action cuts firm value to ν − δ̃ and pays M a private benefit β > 0; **model G** ("good" action) — the action raises firm value to ν + δ̃ and costs M a private β > 0. β is fixed and known (p. 2651). Status quo value ν is common knowledge.
- **Compensation.** M is paid ω₁P₁ + ω₂P₂ with ω₁, ω₂ > 0 — this is exogenous (footnote 8, p. 2652). ω₂ > 0 is maintained throughout; ω₂ = 0 is "significantly more complicated to analyze and, in some cases, it admits a large number of equilibria". *(corrected by verifier: footnote 8 does not say the case is unanalysed — it says "we have characterized the set of equilibria and derived their properties for some versions of our model. Details are available upon request", i.e. the analysis exists but is not in the paper.)*
- **Blockholder L.** Observes private information in Period 1 and may sell. **L can only sell or hold — she cannot buy** (the buying variation is described in words on p. 2658 and its details are "available upon request"). With probability 0 < θ < 1 she is hit by a liquidity shock and must sell her entire stake regardless of information. θ is the model's only liquidity-type parameter.
- **Trading technology.** **L's trade is observable — she does not trade anonymously, and there is no order flow to hide in.** Consequently L's ex ante expected trading profits are exactly zero (§6.1, p. 2671). This is the single biggest structural difference from a Kyle-style blockholder model: there is no noise-trader intensity, no market-maker pricing rule over aggregate order flow, and no price impact parameter. θ does double duty as "liquidity" — it is the probability of a forced sale, i.e. it garbles the *inference* from exit, not the *execution* of it.
- **Information structures.** Superscripts = what L sees privately in Period 1, subscripts = what everyone sees. Models analysed: B^a / G^a (§2, L sees ã only); B^{a,δ} / G^{a,δ} (§3, L sees ã and δ̃); B_a^{a,δ} / G_a^{a,δ} (§4, ã public, L sees δ̃); B_δ^{a,δ} / G_δ^{a,δ} (§5, δ̃ public, L sees ã).
- **Equilibrium notion.** Bayesian–Nash. Cutoff strategies for M; tie-breaking assumptions stated p. 2653. Benchmark without L: M acts on δ̃ ≤ β/ω₂ (model B) or δ̃ ≥ β/ω₂ (model G); the paper assumes β/ω₂ < δ̄.
- **Welfare metric.** Ex ante expected agency cost E(δ̃ã) in B, E(δ̃(1 − ã)) in G. An equilibrium is *disciplining* / *nondisciplining* / *dysfunctional* as L's presence lowers / does not change / raises that cost (Definition, p. 2654).
- **Method.** Analytical throughout; every proposition has an Appendix proof (pp. 2678–2684). Two figures are worked numerical examples on a uniform δ̃.
- **No data.** There is no empirical work in the paper at all: §7 proposes regressions but runs none.

## 3. Results — with honesty labels
| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | In B^a and G^a a unique equilibrium exists and is always disciplining: cutoff x_B (resp. x_G) < β/ω₂; L exits iff M does the wrong thing. | PROVED | p. 2657, Prop. 1(i)–(ii); proof p. 2678 |
| R2 | Both cutoffs are increasing in θ — L's discipline weakens as her trade becomes more likely to be liquidity-driven. | PROVED | p. 2657, Prop. 1(iii) |
| R3 | x_G < x_B: for identical parameters, L disciplines *more* in the "good action" model than in the "bad action" model, because |E_s − E_ns| = E(δ̃ | δ̃ ≥ x) > E(δ̃ | δ̃ ≤ x). In B^a the disciplining tool vanishes as x → 0; in G^a it has a positive lower bound. | PROVED | p. 2657, Prop. 1(iv); discussion p. 2658; proof p. 2678 |
| R4 | In B^{a,δ} an equilibrium exists and *every* equilibrium is disciplining; L sells iff the action was taken and δ̃ ≥ E_s(x_B). Exit probability is positive for θ > 0 and vanishes as θ → 0 — discipline without observed exit. | PROVED | pp. 2659–2660, Prop. 2; proof p. 2679 |
| R5 | **More private information can hurt.** For any distribution of δ̃ and any β, ω₁, ω₂ there is a θ̂ such that for θ > θ̂ agency costs are *lower* in B^a than in any equilibrium of B^{a,δ}. | PROVED | p. 2662, Prop. 3; proof pp. 2679–2680 |
| R6 | Worked example (δ̃ ~ U[0,1], β = 0.4, ω₁ = 1, ω₂ = 0.5; no-L cutoff β/ω₂ = 0.8): B^{a,δ} beats B^a for θ below 0.25 and loses above it ("for values of θ above 0.25, the reverse is true"); x_B rises in θ in both models. | NUMERICAL | p. 2661, Figure 1; parameters p. 2661 |
| R7 | G^{a,δ} has a unique equilibrium whose cutoff either equals the G^a cutoff, or is strictly higher but < β/ω₂, or equals β/ω₂ (nondisciplining). Extra information about δ̃ *never* helps in model G and can make L wholly ineffective. | PROVED | p. 2662, Prop. 4; proof pp. 2680–2681 |
| R8 | Worked example (δ̃ ~ U[0,1], β = 0.33, ω₁ = 0.25, ω₂ = 1): the three regimes of Prop. 4 occur on intervals A, B, C of θ in that order — but footnote 21 states the ordering is not general. | NUMERICAL | p. 2664, Figure 2; footnote 21 p. 2664 |
| R9 | B_a^{a,δ} (action public, L privately informed about δ̃) has a unique disciplining equilibrium whose agency cost is **lower than in both B^a and B^{a,δ}** — the best "bad action" outcome the paper finds. | PROVED | p. 2666, Prop. 5; proof pp. 2681–2682 |
| R10 | **G_a^{a,δ} is dysfunctional**: unique equilibrium, and agency cost is strictly *higher* than with no blockholder at all. L's exit signals a low δ̃ among the taken-action states, so the market marks the price down exactly when M does the right thing. | PROVED | pp. 2668–2669, Prop. 6; proof pp. 2682–2683 |
| R11 | With δ̃ publicly known (B_δ^{a,δ}, G_δ^{a,δ}) the two agency problems are exact mirror images: unique, always-disciplining, mixed-strategy equilibria with m_G(δ) = 1 − m_B(δ) and identical impact on agency cost. | PROVED | p. 2670, Prop. 7; proof pp. 2683–2684 |
| R12 | If information acquisition is endogenous, nondisciplining and dysfunctional equilibria do not arise, since L only pays for information that raises her stake's value; in "good action" problems L will simply never buy information about δ̃. | ASSERTED (argued in text; no proposition, no proof) | p. 2671, §6.1 |
| R13 | Anonymous trading has two offsetting effects — smaller direct price impact but positive trading profits, hence stronger incentive to acquire information; with a later disclosure of the trade, the net disciplinary effect is expected to be *larger*. | ASSERTED (verbal, no model) | pp. 2671–2672, §6.1 |
| R14 | Transaction costs generally weaken the threat of exit ⇒ discipline is lower in less liquid markets. Exit costs that reduce firm value have ambiguous sign and can *raise* welfare. | ASSERTED ("It can be shown that…"; detailed analysis "available upon request", footnote 26) | pp. 2672–2673, §6.2; footnote 26 p. 2672 |
| R15 | If β̃ = γ₀ + γ₁δ̃ with γ₀ > 0 and γ₁ < ω₂, all results carry over with γ₀ for β and ω₂ − γ₁ for ω₂. | PROVED (by direct substitution in text) | pp. 2673–2674, §6.3 |
| R16 | Under uncertainty about *which* agency problem is present, L can discipline only one of the two types, but that "model uncertainty" can *strengthen* her impact on the type she does discipline. | ASSERTED ("it can be shown") | p. 2674, §6.3 |
| R17 | **Proposed test (never run):** regress R_block (abnormal return on block acquisition) on blockholder longevity (1 − θ), short-term pay weight ω₁, and their interaction; a positive interaction coefficient identifies the exit channel against other activism models. A parallel test replaces longevity with a market-liquidity measure. | ASSERTED (prediction; no data, no estimate) | pp. 2675–2676, §7 |
| R18 | Exit does not displace other activism: "the threat of exit as a form of activism does not necessarily rule out other forms of activism; indeed, it may enhance their effectiveness." The complement they name is "jawboning" / behind-the-scenes negotiation, which is also the channel through which M learns L is informed (Carleton, Nelson & Weisbach 1998, p. 2649). Neither is modelled. | ASSERTED (conclusion prose, no model) | p. 2676, §8; also p. 2646 and p. 2678 *(added by verifier)* |
| R19 | The "bad action" is mapped empirically onto **value-reducing mergers and free-cash-flow abuse** by mature, cash-rich firms; and that case is said to have the information structure B_a^{a,δ} (action public, L privately informed about consequences) where discipline is strongest. This is AP's nearest approach to a control-relevant action — but it is an interpretation of the manager's action, not a takeover model. | ASSERTED (interpretive mapping; no data) | p. 2676 §7 and p. 2677 §8; footnote 2, p. 2647 *(added by verifier)* |

## 4. Institutional facts used
Almost none — this is a pure theory paper with no institutional anchor.
- "13D" occurs exactly three times in the whole paper *(verified by grep)*: twice on **p. 2649**, purely as background to other people's empirical work (Klein & Zur 2009 and Brav et al. 2006 use "13D and other filings"; Klein & Zur's result does not depend on whether a proxy fight was mentioned in the 13D), and once in footnote 23, p. 2671. SEC filings are also invoked once as a possible reason the manager knows L is informed: "The SEC filings made by the large shareholder, which are studied empirically in these studies, may be one source of this awareness." (p. 2650).
- Footnote 23 (p. 2671) is the only place a disclosure rule does any work in the argument, and it is one sentence: 13D filings may make it common knowledge that L has acquired information. No threshold (5%), no filing window, no dated rule change appears anywhere in the paper.
- §6.1 (p. 2672) invokes "trade disclosure requirements" hypothetically, as a reason a trade might become public *after* the fact — again with no rule, threshold or lag specified.
- No data source, no sample, no period.

## 5. Referee-facing strengths / weaknesses
**Strengths:**
- Every headline claim is a proposition with an Appendix proof; existence and uniqueness are handled explicitly, and the one model with multiple equilibria (B^{a,δ}) is flagged (footnote 17, p. 2659).
- The B/G asymmetry is a genuinely non-obvious result and the mechanism (inference from *not* selling, and whether the disciplining tool survives as the cutoff shrinks) is cleanly isolated.
- The dysfunctional case (Prop. 6) is a real negative result, not a robustness caveat — the paper is honest that a better-informed blockholder can destroy value.
- Prop. 2's "discipline without observed exit" is a defensible answer to the obvious empirical objection that blockholders rarely exit.

**Weaknesses / open flanks:**
- **No trading microstructure.** L's trade is fully observable, expected trading profits are zero, and there is no order flow, no noise-trader intensity, no price-impact coefficient. "Liquidity" enters only as θ, the probability of a forced sale, which is a *shock* parameter, not a market-depth parameter. The paper's own liquidity comparative static (R14) comes from transaction costs bolted on verbally in §6.2, not from the model.
- **The action space is crippled by assumption.** L cannot buy. The buy extension is asserted not to change results but is only "available upon request" (footnote 16, p. 2658), and footnote 28 (p. 2674) concedes that a third trade would change the model-uncertainty result.
- ω₂ > 0 is required everywhere; ω₂ = 0 admits many equilibria and its analysis is not in the paper — "available upon request" (footnote 8, p. 2652).
- **The θ = 0 limit is not clean.** Footnote 9 (p. 2652) concedes that at θ = 0 there may be extra equilibria "in which L never sells" or "where L sells only some of her shares", and that killing them "would require restrictions on out-of-equilibrium beliefs". This is the *only* place a partial sale appears anywhere in the paper. *(added by verifier)*
- **They consciously decline the liquidity-through-speculator-profit channel.** p. 2648 distinguishes Holmström & Tirole (1993), "focus[ing] on how the ownership structure of the firm affects the value of market monitoring through its effect on liquidity and on the profits speculators realize in trading on information" — i.e. exactly FGG's channel — and says their own focus is different. So AP's silence on order flow is a choice, not an oversight. *(added by verifier)*
- Minor (second): p. 2648 says endogenous information acquisition "is discussed in Section 7.1"; it is discussed in §6.1. A second internal cross-reference error. *(added by verifier)*
- The private benefit β is common knowledge; privately known β is declared out of scope (footnote 7, p. 2651).
- §7's empirical design is a sketch: R_block, "some measure of longevity", "some measure of short-term compensation". No sample, no identification strategy, no discussion of endogenous block formation.
- Minor: p. 2675 refers the reader to "the discussion in 7.2" for costly exit; the costly-exit subsection is §6.2. Internal cross-reference error.
- The compensation contract is exogenous, so all welfare statements are conditional on a contract the shareholders are not choosing.

## 6. What they do NOT do (scope boundary)
**OBJECT.** The object is the *manager's action choice* and the resulting ex ante agency cost E(δ̃ã) — i.e. an internal governance outcome. It is **not** a control outcome in our sense. Grep counts for the whole paper: "tender" 0, "premium" 0, "bidder" 1, "takeover" 3, "proxy" 4 — and none of them is a modelled object. "Takeover" appears (i) in the first paragraph, p. 2645, listing "overt forms of shareholder activism such as takeovers, proxy fights, strategic voting, shareholders' proposals" that most large shareholders **do not** engage in — AP's object is expressly the *non-overt* channel; (ii) in the Gopalan paragraph quoted below; and (iii) in the reference list. "Proxy" appears only in the Klein & Zur background on p. 2649. *(count added by verifier)* The one substantive takeover passage is there only to *distinguish* the mechanism from Gopalan's: "In Gopalan’s study, exit by an informed large shareholder creates value by encouraging another bidder to acquire information and implement improvements through a takeover mechanism. This mechanism for bringing about improvement is very different from the one at work in our model, which focuses on managerial incentives, and where the impact of large shareholder exit is due to its effect on managerial compensation." (p. 2648). The one derived observable, R_block, is a block-acquisition announcement return — not a premium.

**MARGIN of a disclosure rule: none.** There is no disclosure rule in the model. There is no stake threshold, no filing window, no flagged-vs-pooled partition. Disclosure enters twice, both times as an aside with no modelling consequence: footnote 23, "Disclosure requirements such as 13D filings may help bring this about." (p. 2671); and §6.1's hypothetical, "Further, suppose that L’s trade, and possibly the motive for her trade, becomes public subsequent to the trade, due perhaps to trade disclosure requirements." (p. 2672). The second is the closest thing in the paper to our window margin — a lag between trade and revelation — and it is left as a paragraph of prose in an extensions section, never solved.

**IDENTIFICATION: theory only.** No data of any kind. §7 proposes two cross-sectional interaction regressions (longevity × ω₁, and liquidity × ω₁) and explicitly leaves the estimation to others: "The critical coefficient in identifying the importance of the threat of exit in disciplining managers is the one on the interaction term." (p. 2675). No design, no sample, no shock.

**Explicitly declared out of scope (their words):**
- Privately known private benefit: "Such a model is beyond the scope of this paper." (p. 2651, footnote 7).
- A third trading action (buying) under model uncertainty: "A full examination of this is beyond the scope of this paper." (p. 2674, footnote 28).
- Anonymous trading with real order flow, costly exit, and endogenous information are all §6 sketches; the anonymous-trading case is argued verbally and the costly-exit analysis is "available upon request" (footnote 26, p. 2672), i.e. not in the paper.

## 7. Implications for our position
**What they occupy.** OBJECT: manager's action / ex ante agency cost, plus a proposed (unestimated) block-acquisition announcement return. MARGIN: none — no disclosure rule of any kind is in the model. IDENTIFICATION: theory only, with an unexecuted cross-sectional interaction test.

**What this leaves open for us.** All three of our coordinates are free. The control outcome (bidder entry, takeover premium, campaign success) is not their object; the disclosure rule's threshold and window margins are not in their model; and they have no identification at all. Our position sits in whitespace relative to this paper on every axis.

**Where they constrain us.**
1. **They own the "exit is voice" mechanism.** Any claim that the mere threat of selling disciplines the target must cite them, and must say what our model adds beyond it. Our addition is that the *partition* (flagged vs pooled) and the *control outcome* are what move, not the manager's effort cutoff.
2. **They already have a liquidity comparative static — but a weak one.** Two distinct liquidity notions appear. (a) θ, the forced-sale probability: discipline is monotonically *decreasing* in θ (Prop. 1(iii), PROVED). (b) transaction costs: discipline is *lower in less liquid markets* (p. 2673, ASSERTED, no proof, analysis not in the paper). Note the two are opposite in sign in "liquidity" language — higher θ is more noise in L's trade and *hurts*, whereas lower transaction costs are more liquidity and *help*. Because (b) is only asserted, our κ-driven comparative statics are not pre-empted by a proved result; but we should quote their sentence and say we microfound the sign they conjecture, and that our κ is noise-trader intensity, not a transaction cost.
3. **The non-monotonicity precedent.** Their "more information is not always better" (Prop. 3, PROVED) and the intervals A/B/C of Figure 2 are proved/numerical precedents for non-monotone comparative statics in a blockholder model. This is helpful cover for our own hump — but note theirs is proved in a limit (θ → 1) and ours is grid-certified only. Do not claim parity of label.
4. **They rule out the buy action; we need it.** Our public-voice branch is "buy above the threshold and be flagged". AP explicitly restrict L to sell-or-hold and only gesture at buying. Our four-action space is a genuine extension, and their footnote 28 (p. 2674) is the sentence to cite when saying so.
5. **They already interpret the bad action as a value-reducing merger.** p. 2676 and p. 2677 map model B onto "value-reducing mergers" and free-cash-flow abuse, and say that is exactly the case (B_a^{a,δ}) where the exit threat works best. A referee can therefore say AP already speak to merger decisions. The answer is that the merger is *the manager's* decision inside their model — there is no bidder, no premium and no tender offer; our object is the outcome of an external control contest, which their framework cannot even state. *(added by verifier)*
6. **They claim exit complements voice, without modelling either.** p. 2676: exit "does not necessarily rule out other forms of activism; indeed, it may enhance their effectiveness", with jawboning as the named complement (pp. 2646, 2678). Our quiet-voice / public-voice split is the model they gesture at; we should cite this sentence as the invitation. *(added by verifier)*
7. **Their trading environment is the opposite of ours.** Observable trade, zero expected trading profits, no order flow. A referee who knows AP will ask why we need κ at all. The answer must be that κ is what determines how much of the stake can be accumulated *before* the flag — a question that cannot even be posed in a model with no anonymous trading and no window. Their §6.1 paragraph on trade-becoming-public-later (p. 2672) is the hook: they name the ingredient and do not build it.

**Sentence for the referee report:** AP prove that exit disciplines, in a model with no disclosure rule, no bidder, and no order flow; the window margin they gesture at in a single extensions paragraph is the one we solve.

## 8. Quotes we may lean on (verbatim, page-cited)
| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "What seems to have not been widely recognized is that the threat of exit itself can be a form of shareholder activism." | p. 2646 | The claim they own; our antecedent sentence |
| Q2 | "In Gopalan’s study, exit by an informed large shareholder creates value by encouraging another bidder to acquire information and implement improvements through a takeover mechanism. This mechanism for bringing about improvement is very different from the one at work in our model, which focuses on managerial incentives, and where the impact of large shareholder exit is due to its effect on managerial compensation." | p. 2648 | §6 — takeovers explicitly disclaimed as their mechanism |
| Q3 | "Fixing β, θ, ω1 , ω2 , and the distribution of δ̃, x G < x B . That is, all else equal, the large shareholder is more effective in disciplining the manager in model Ga than in model Ba ." | p. 2657 | R3, Prop. 1(iv) — the B/G asymmetry |
| Q4 | "For any given distribution of δ̃ and parameters β, ω1 , and ω2 , there exists θ̂ such that if θ > θ̂, then the large shareholder is more effective in disciplining the manager, and thus the agency costs are lower, in the equilibrium of model Ba than in any equilibrium of model Ba,δ ." | p. 2662 | R5, Prop. 3 — proved non-monotonicity in information |
| Q5 | "Disclosure requirements such as 13D filings may help bring this about." | p. 2671 | §6 — the *only* substantive appearance of the disclosure rule, in a footnote |
| Q6 | "Further, suppose that L’s trade, and possibly the motive for her trade, becomes public subsequent to the trade, due perhaps to trade disclosure requirements." | p. 2672 | §6/§7 — the window margin named and left unbuilt |
| Q7 | "This implies that the disciplinary impact of the large shareholder will be lower when the market for the firm’s stock is less liquid to the extent that less liquid markets can be interpreted as those having higher transactions costs." | p. 2673 | R14 — their liquidity comparative static, ASSERTED not proved |
| Q8 | "This means that the large shareholder’s threat of exit is less effective in illiquid markets, which are characterized by higher transactions costs." | p. 2675 | §7 — the liquidity prediction they hand to empiricists |
| Q9 | "The critical coefficient in identifying the importance of the threat of exit in disciplining managers is the one on the interaction term." | p. 2675 | §6 — identification: proposed, never executed |
| Q10 | "Such a model is beyond the scope of this paper." | p. 2651 (footnote 7) | §6 — declared scope boundary (privately known β) |
| Q11 | "A full examination of this is beyond the scope of this paper." | p. 2674 (footnote 28) | §6 — declared scope boundary (a third trade, i.e. buying) |
| Q12 | "Our results generally support the notion that liquidity need not interfere with, and in fact may enhance, corporate governance." | p. 2678 | The headline they are cited for; our point of departure |
| Q13 | "However, the threat of exit as a form of activism does not necessarily rule out other forms of activism; indeed, it may enhance their effectiveness." | p. 2676 (§8) | R18 — exit/voice complementarity claimed, never modelled *(added by verifier)* |
| Q14 | "In particular, Holmstrom and Tirole focus on how the ownership structure of the firm affects the value of market monitoring through its effect on liquidity and on the profits speculators realize in trading on information. In our model, by contrast, we focus on the disciplining impact of a large shareholder’s threat of exit…" | p. 2648 | §5/§7 — they name and decline the speculator-profit liquidity channel (FGG's channel) *(added by verifier)* |
| Q15 | "most large shareholders play a limited role in overt forms of shareholder activism such as takeovers, proxy fights, strategic voting, shareholders’ proposals, etc." | p. 2645 | §6 — takeovers placed outside the object in the paper's first paragraph *(added by verifier)* |
| Q16 | "This would correspond empirically to such actions as value-reducing mergers or to other situations involving the abuse of “free cash flows.”" | p. 2677 (§8) | R19 — the closest AP get to a control-relevant action *(added by verifier)* |

*Note on Q3 and Q4: the printed text sets model labels with superscripts (model G^a, B^a, B^{a,δ}) and the PDF text layer flattens them to "Ga", "Ba", "Ba,δ"; spacing inside the flattened labels is as extracted. The wording is otherwise character-for-character.*
## 9. Verification log

**Verifier:** adversarial pass, 2026-08-19. **Method:** the PDF was re-extracted one page at a time (`pdftotext -f N -l N -layout`) into a page-tagged file, so every quote and citation was matched against the *printed* page it claims, not against the flat `.txt`. Matching normalised soft hyphens, line-break hyphenation and curly quotes only. Page map confirmed: PDF page *N* = printed 2644+*N*, 41 pp, 2645–2685.

**Header / venue — OK.** p. 2645 footer prints `doi:10.1093/rfs/hhp037`, "Advance Access publication May 18, 2009", "The Review of Financial Studies Vol. 22, No. 7". The earlier title "The 'Wall Street Walk' as a form of Shareholder Activism" is confirmed in the unnumbered acknowledgment footnote, p. 2646. `pdfinfo` confirms 41 pages.

**Quotes (§8).**
| Q | Verdict | Checked against |
|---|---|---|
| Q1 | OK | p. 2646, verbatim |
| Q2 | OK | p. 2648, verbatim (both sentences) |
| Q3 | OK | p. 2657, Prop. 1(iv), verbatim incl. flattened superscripts |
| Q4 | OK | p. 2662, Prop. 3. NB the text layer splits this sentence around an OUP download watermark; both halves are on p. 2662 and the printed sentence is continuous |
| Q5 | OK | p. 2671, footnote 23, verbatim |
| Q6 | OK | p. 2672, §6.1, verbatim |
| Q7 | OK | p. 2673, verbatim |
| Q8 | OK | p. 2675, verbatim |
| Q9 | OK | p. 2675, verbatim |
| Q10 | OK | p. 2651, footnote 7, verbatim |
| Q11 | OK | p. 2674, footnote 28, verbatim |
| Q12 | OK | p. 2678, first paragraph of the closing section, verbatim |
| Q13–Q16 | OK | added by the verifier and matched verbatim at pp. 2676, 2648, 2645, 2677 respectively |

**Results (§3).**
- R1–R3 **OK** — Prop. 1(i)–(iv), p. 2657; proof p. 2678. PROVED confirmed. Prop. 1(iii) reads "both x_B and x_G are increasing in θ" exactly as the card states.
- R4 **OK** — Prop. 2 spans pp. 2659–2660; proof p. 2679. "There exists at least one equilibrium … and every equilibrium is disciplining" and the θ→0 vanishing-exit clause both confirmed.
- R5 **OK** — Prop. 3, p. 2662; proof pp. 2679–2680 (proof of Prop. 4 begins p. 2680). PROVED.
- R6 **OK, one number tightened** — Figure 1 and its parameters are on p. 2661; β = 0.4, ω₁ = 1, ω₂ = 0.5, no-L cutoff 0.8 all confirmed. The paper states the crossing at 0.25 exactly ("for values of θ above 0.25, the reverse is true"), so the card's "≈ 0.25" was removed.
- R7 **OK** — Prop. 4, p. 2662; proof pp. 2680–2681.
- R8 **OK** — Figure 2 p. 2664; footnote 21 p. 2664 confirms the A/B/C ordering is not general.
- R9 **OK** — Prop. 5, p. 2666, incl. part (iii) "lower than … model B^a and … any equilibrium of model B^{a,δ}"; proof pp. 2681–2682.
- R10 **OK** — Prop. 6, statement p. 2668 with parts (i)–(iii) running onto p. 2669; proof pp. 2682–2683.
- R11 **OK** — Prop. 7, p. 2670, incl. m_G(δ) = 1 − m_B(δ) and equal agency-cost impact; proof pp. 2683–2684.
- R12 **OK** — §6.1, p. 2671, ASSERTED confirmed (argument in prose, no proposition).
- R13 **OK** — §6.1, pp. 2671–2672, ASSERTED confirmed.
- R14 **OK** — §6.2, pp. 2672–2673. "It can be shown that…" appears verbatim on p. 2673 (twice in the subsection); footnote 26 on p. 2672 says the detailed analysis is "available upon request". ASSERTED confirmed.
- R15 **OK** — §6.3, pp. 2673–2674; γ₀ for β and ω₂ − γ₁ for ω₂ confirmed; footnote 27 (p. 2674) adds the γ₁ > ω₂ case, which merely switches the direction of the cutoffs.
- R16 **OK** — p. 2674, "it can be shown that L can only provide discipline for one of the two types" and the E_s − E_ns enhancement. ASSERTED confirmed.
- R17 **OK** — §7, pp. 2675–2676; both regressions confirmed, neither run; wording "some measure of the longevity" / "some measure of the importance of short-term compensation" confirmed.
- R18, R19 **added by verifier** (see omissions).
- Count check: **7 propositions, 7 Appendix proofs** — Proofs of Propositions 1–7 located at pp. 2678, 2679, 2679, 2680, 2681, 2682, 2683. The card's claim that every proposition is proved in the Appendix is **confirmed**.

**Scope claims (§6) — all confirmed by grep over the full text.** "tender" 0 hits; "premium" 0 hits; "window" 0 hits; "five business" 0 hits; "threshold" 0 hits; "bidder" 1 hit (the Gopalan sentence, p. 2648); "noise" 1 hit and it is metaphorical ("communicated with some noise", p. 2669) — there is no noise trader anywhere; "13D" 3 hits (p. 2649 ×2 as background to Klein & Zur / Brav et al., p. 2671 footnote 23); "disclos*" 3 hits in the body (p. 2671 fn 23, p. 2672 ×2 in the §6.1 hypothetical) plus one reference-list title. "takeover" 3 hits, "proxy" 4 hits — none modelled; the intro hit (p. 2645) was missing from the card and has been added.

**Corrections applied.**
1. §2, compensation bullet — **MISCITED → fixed.** The card said ω₂ = 0 "is not analysed". Footnote 8 (p. 2652) actually says the authors *have* characterised the ω₂ = 0 equilibria and that "Details are available upon request". The distinction matters: it is not in the paper, but it is not unexamined either.
2. §3 R6 — "≈ 0.25" → "0.25" (the paper prints the number).
3. §4 — 13D bullet rewritten with the verified count and the correct page for each occurrence (the background mentions are on p. 2649, not p. 2650; p. 2650 carries the separate "SEC filings … source of this awareness" sentence, which the card had cited correctly).
4. §6 — "Takeovers appear exactly once in substance" replaced with the verified occurrence-by-occurrence account, adding the p. 2645 intro sentence.

**Omissions added.**
- **R18 / Q13 (p. 2676).** AP claim exit *complements* other activism ("does not necessarily rule out other forms of activism; indeed, it may enhance their effectiveness"), with jawboning and behind-the-scenes negotiation as the named complement (pp. 2646, 2678) and Carleton–Nelson–Weisbach (p. 2649) as the evidence. For a paper that models exit *and* voice, this is the sentence a referee will hold up; the card had no line on it.
- **R19 / Q16 (pp. 2676, 2677; fn 2 p. 2647).** AP interpret the "bad action" empirically as a **value-reducing merger** or free-cash-flow abuse and say the exit threat is *most* effective there. This is the closest the paper comes to a control-relevant action, and it partially undercuts a flat "they have nothing to do with mergers" framing. §7 now carries the rebuttal (their merger is the manager's own decision; there is still no bidder, premium or tender offer).
- **§5, Holmström–Tirole (p. 2648) / Q14.** AP explicitly name and decline the "liquidity → speculator profits → market monitoring" channel. This is *exactly* FGG's channel, so AP's silence on order flow is a modelling choice, not a gap — worth knowing before we claim the lane is empty.
- **§5, footnote 9 (p. 2652).** At θ = 0 there can be equilibria "in which L never sells" or "where L sells only some of her shares", removable only with out-of-equilibrium belief restrictions. This is the single appearance of a *partial* sale in the paper and the only crack in the θ-as-liquidity story.
- **§6 / Q15 (p. 2645).** The paper's opening sentence places takeovers and proxy fights among the "overt forms of shareholder activism" that large shareholders mostly avoid — a cleaner scope citation than the Gopalan paragraph.
- **§5, second cross-reference error (p. 2648).** "This is discussed in Section 7.1"; it is §6.1. The card had already caught the p. 2675 "7.2"/§6.2 slip; there are two.
- Noted but not added as a section item: the unnumbered four-row **summary table on p. 2677** compares model B and model G on all four information structures in one place — the most citable single object in the paper if we ever need AP's results compressed.

**UNCHECKED:** none. Every quote, page, proposition, label and scope claim in this card was checked against the printed page.

**Overall verdict: SOUND.** 16 quotes OK (12 original + 4 added), 0 WRONG, 1 MISCITED (§2 footnote-8 characterisation, fixed), 2 small precision fixes, 0 unchecked. Every honesty label (PROVED / NUMERICAL / ASSERTED) matches the source. The card's three positioning claims — no control outcome, no disclosure rule with a threshold or window, no identification — all hold against a full-text grep. The one thing the card understated is that AP's "bad action" is explicitly read as a value-reducing merger; that is now in §3, §7 and §8.
