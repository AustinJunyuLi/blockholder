# Literature Brief — Strand: classic-exit-voice

**Researcher:** LitResearcher_ClassicExitVoice
**Mission:** Read in full Maug (1998, JF), Kahn & Winton (1998, JF), Faure-Grimaud & Gromb (2004, RFS), Admati & Pfleiderer (2009, RFS). Focus: exit-vs-voice tradeoff, role of liquidity, proven vs assumed, institutional facts, and why none combined disclosure regimes with takeover feedback.

**Access confirmation (all four read in full, not abstracts):**

| Paper | Source | Method |
|---|---|---|
| Maug 1998 | Local `lit/maug-1998.pdf` (JSTOR scan, 35 pp.) | No text layer; rendered pages with `pdftoppm`, OCR'd with macOS Vision (Swift), read entire OCR text |
| Kahn & Winton 1998 | Local `lit/kahn-winton-1998.pdf` (JSTOR scan, 32 pp.) | Same OCR pipeline; read entire OCR text |
| Faure-Grimaud & Gromb 2004 | JSTOR scan PDF from edegan.com (mirror of jstor.org/stable/3598056, 31 pp.) | Embedded text layer; read entire text |
| Admati & Pfleiderer 2009 | Stanford GSB Research Paper 1918(R2), July 2007, stamped "Forthcoming in the Review of Financial Studies" (47 pp.) | Downloaded via user's real browser from the GSB faculty page (OUP page itself is behind Cloudflare); read entire text. Content = published RFS version; only pagination differs (RFS 22(7): 2645–2685) |

Note on precision: Maug/KW were read via OCR, so prose is reliable but some displayed equations were garbled; formulas quoted below were cross-checked for internal consistency with the propositions (signs verified against comparative-statics claims). FG2004 and AP2009 come from clean text layers.

---

## 1. Maug (1998), "Large Shareholders as Monitors: Is There a Trade-Off between Liquidity and Control?", *Journal of Finance* 53(1), 65–98.

### Research question & summary
Does a liquid stock market reduce large shareholders' incentives to monitor (the Coffee 1991 / Bhide 1993 "liquidity vs. control" hypothesis)? Answer: **No.** Once the blockholder's stake is endogenous, liquidity *unambiguously raises* equilibrium monitoring, because liquid markets let the monitor recover monitoring costs through informed trading, mitigating the free-rider problem. The alleged trade-off assumes an exogenous block size; endogenizing it destroys the result.

### Model architecture
- **Players:** one firm (value L, or H>L if restructured); one risk-neutral large investor F (no liquidity shocks, can monitor at cost c_M); continuum of households (measure 1) holding all shares initially; competitive market maker.
- **Market structure:** binary Kyle/Glosten–Milgrom hybrid. With prob 1/2 a fraction φ of households suffers a correlated liquidity shock and sells everything. Market maker observes only aggregate net order flow, sets P1 = E[v | flow]. Order flow takes three values {-3u, -u, u} with u = φ(1−α)/2; flow −u is uninformative, ±3u/u fully revealing.
- **Timing:** (1) F buys initial stake α from households at price P0 (households marginal, so P0 embeds an adverse-selection discount exactly equal to F's per-share trading gains G); (2) F chooses monitoring/trading strategy; (3) shocks; (4) trading & pricing; (5) payoff realization.
- **Strategy structure:** F mixes — with prob q buy u and monitor; with prob 1−q sell u and don't. Camouflage constraint: F's buy+sell quantities must straddle household flow so the market maker cannot distinguish "F buys, households sell" from "F sells, no shock." Other strategies (buy-without-monitoring, sell-and-monitor) are strictly dominated.
- **Solution concept:** subgame perfection, solved backward; mixed strategy purified via private monitoring-cost types (Fudenberg–Tirole).

### Key results (all proven analytically, closed form; proofs in Appendix B)
- **Prop 1 (Equilibrium):** unique mixed-strategy equilibrium, q = 1/2 + 2[α(H−L) − c_M]/[φ(1−α)(H−L)] (signs verified against the text: q increases in α — the **lock-in effect**; the (1−α) factor is the **liquidity effect**; q decreases in c_M).
- **Prop 2 (Liquidity):** monitoring probability *decreases* in liquidity φ **iff** α ≥ c_M/(H−L), i.e., iff the capital gain on the initial stake alone covers monitoring costs. This cost-coverage condition is the pivot of the whole paper.
- **Prop 3 (Social optimum):** requires α ≥ α* where α* strictly exceeds c_M/(H−L), gap increasing in φ (more liquidity → larger opportunity cost of not selling).
- **Prop 4 (Commitment effect — the main result):** F's payoff from the initial stake is α·G and from trading (1−α)·G − qc_M, totaling G − qc_M; α enters only through q. F chooses a stake **strictly below** the cost-recovery stake: â = c_M/(2(H−L) − c_M) < c_M/(H−L), committing to q̂ = 1/2 − c_M/(φ(H−L)) < 1/2, which **increases strictly in liquidity φ**. Because â < c_M/(H−L), Prop 2's condition implies liquidity always helps in equilibrium.
- **Prop 5 (No monitoring):** if the charter's majority requirement μ exceeds μ̄ (μ̄ increasing in φ), no profitable monitoring equilibrium exists.
- **Prop 6 (Majority requirement):** for intermediate binding μ, F is forced to α > c_M/(H−L) and then q *decreases* in liquidity (sign flip).
- **Prop 7 + Cor 2:** initial shareholders' wealth is **non-monotone (single-peaked) in liquidity** — interior optimum φ* (more monitoring vs. larger adverse-selection discount); optimal charter sets majority requirements to extract F's rents; founders prefer *lower*-than-social liquidity if they cannot extract rents via the charter.
- **Section IV (takeovers vs. monitoring):** two intervention technologies, takeover (cost c_T, success prob s_T) vs. monitoring (c_M, s_M). **Prop 8/9:** F randomizes between selling and *one* intervention mode; never mixes the two modes except on a knife-edge. **Lemma 2 & Prop 10:** if takeovers have a cost advantage (s_T/s_M ≥ c_T/c_M), then (i) q̂_T > q̂_M; (ii) **higher liquidity makes the takeover equilibrium less likely to be preferred** — cost advantages matter in illiquid markets, effectiveness (surplus s_j(H−L) − c_j) matters in liquid ones; (iii) shareholders' optimal φ* is lower under the takeover equilibrium.

### Proven vs assumed
Everything is analytical; no numerics. Load-bearing assumptions: binary firm values; risk neutrality; symmetric trading quantities x_B = −x_S (generalized in Appendix A — results robust); exogenous monitoring success; the exact offset between the IPO discount and trading gains (eq. 13) that makes F's total profit α-independent except through q; single blockholder; one-shot.

### Institutional facts
US mutual funds' 5% holding limit per firm (footnote 6); 1980s institutional activism targeting takeover defenses, later shifting to performance/governance issues (confidential voting), citing Nesbitt (1994), Gillan & Starks (1995), Wahal (1996); Gordon & Pound (1993) on failure rates of shareholder proposals; institutions "often legally prohibited from hostile bidding"; CalPERS effect studies (Smith 1996); Leleux et al. (1995) French block purchases; Brickley et al. (1988) antitakeover amendments. **Disclosure appears once, as an unmodeled remark:** "any disclosure requirement that forces F to publicize her trades prior to trading would effectively limit market liquidity" (p. 73); post-trade filing requirements "do not affect F's trading strategy."

### Referee-facing strengths/weaknesses
Strengths: clean closed forms; the α-endogeneity critique of Coffee/Bhide is decisive within the model; commitment effect is a memorable, citable mechanism. Weaknesses a referee would attack: the exact knife-edge offset (profits = G − qc_M) that makes α a pure commitment device; binary values; mixed-strategy monitoring (no pure-strategy core); households mechanical; "monitoring" is a black box (no manager, no bidder, no tendering); the free-rider problem is asserted through P0 rather than derived from tendering decisions; Section IV's takeover is just a relabeled intervention technology — **no bidder, no offer, no minority response**.

### Why no disclosure × takeover feedback
Disclosure is acknowledged to matter (it would destroy camouflage) but is binary and exogenous in his framing — a regime switch, not a threshold interacting with inference. Takeovers are folded into the same "intervention" reduced form as monitoring; there is no price-setting bidder, so there is no object like a takeover premium whose liquidity-sensitivity could be analyzed.

---

## 2. Kahn & Winton (1998), "Ownership Structure, Speculation, and Shareholder Intervention", *Journal of Finance* 53(1), 99–129.

### Research question & summary
An institution can use private information either to speculate or to decide whether to intervene ("voice"). How does the ability to speculate affect intervention, and what does this imply for which firms attract activists and for ownership structure? Central insight: intervention has a **direct impact** (stake value ↑) and a **trading impact** of ambiguous sign — intervention raises trading profits **iff it increases the institution's information advantage**, i.e., iff success was the less-expected outcome (q′ < 1/2 in their binary model). Speculation can therefore *discourage* intervention in firms the market expects to do well ("cut and run").

### Model architecture
- **Players:** risk-neutral institution (stake v, exogenous then endogenous); continuum of small investors; a large number of potential speculators who pay g to become perfectly informed (incl. about intervention outcome); competitive market makers.
- **Uncertainty:** firm returns X w.p. q, else 0 at t=2. If distressed (prob 1−q), institution can intervene at cost m; intervention succeeds w.p. δ, raising value 0→X. θ_max = q + δ(1−q).
- **Market:** Admati–Pfleiderer (1989)/Easley–O'Hara (1992) style — market makers quote bid P_B and ask P_A **independent of order flow** (Bertrand, zero profit); P_B = E[value | sell], P_A = E[value | buy]. Small investors hit by liquidity shocks (prob u each direction); each informed trader can trade ≤ w shares (wealth/margin limit). Expected liquidity volume Λ = u(1−v); informed volume Z = (S+1)w.
- **Timing:** t=0 ownership structure chosen; speculators decide whether to acquire info. t=1 institution learns distress, decides intervention (prob α), trading occurs. t=2 liquidation.
- **Equilibrium:** Bayesian–Nash in (α, S) with free entry pinning S via R_S = 0.

### Key results (all analytical)
- **Lemma 1:** closed-form bid/ask; returns R_D, R_I, R_S. More liquidity trading narrows the spread; more informed trading widens it; higher α raises both prices.
- **Prop 2:** equilibrium always exists (Kakutani). **Prop A.1/A.2:** sufficient conditions for active speculators (w ≤ 1/2, wX/g large enough); **uniqueness only under those conditions**.
- **Prop 3 (critical stake):** there is v* such that α = 0 below v* and α increases in v above it. v* ≷ v_M ≡ m/(δX) (the zero-direct-impact stake) iff q ≷ 1/2. Full intervention (α = 1) attainable only if θ_max < 1/2. Crucially, **while speculators are active, changes in the liquidity-shock probability u have NO effect on intervention** — speculator entry exactly offsets changes in liquidity volume (an irrelevance result, contrasting Maug's monotone liquidity effect).
- **Corollaries 4–7:** higher base success prob q raises v* and lowers α (intervention discouraged when success expected); higher effectiveness δ and higher spread X lower v* (with ambiguous effects on α once intervening); higher information cost g amplifies the trading impact (less speculator competition).
- **Trading impact sign:** intervention raises trading profits iff sign(1 − 2q′) > 0. **Delayed resolution** of intervention's outcome skews the trading impact negative (precise bad news exchanged for imprecise maybe-good news).
- **Ownership structure (Section III):** an initial owner selling the firm generally prefers to give the institution the maximum stake w; below v* concentration only crowds out speculators. With open-market purchases, a Grossman–Hart holdout externality appears; private placements circumvent it.
- **Section IV (policy):** **short-swing rules (Section 16(b)) are likely counterproductive** — they tax all trading, may push institutions below the 10% insider threshold, reducing intervention; **restricted shares (Rule 144A)** tilt the institution toward intervention by limiting cut-and-run while leaving buying untouched; most useful where trading profits loom large (opaque, young, small firms).

### Proven vs assumed
Analytical throughout, but the whole liquidity-irrelevance result loads on: order-flow-independent quotes (no price impact *within* the quote — depth is exogenous), free entry of identical speculators (zero-profit condition pins the informed/liquidity ratio), binary outcomes, immediate resolution of intervention, risk neutrality. They flag heterogeneous-speculator and dynamic extensions verbally.

### Institutional facts
**Section 16(b) short-swing rule** (10% ownership → insider status, 6-month profit forfeiture) analyzed formally; **SEC Rule 144A** restricted shares; Silber (1991): ~34% average discount on restricted stock; Hertzel & Smith (1993): private placements of restricted shares have a +7.8% larger announcement effect, concentrated in single-investor placements; Zeckhauser & Pound (1990): large-shareholder presence associated with lower E/P in low-R&D industries only (39% of low-R&D vs 28% of high-R&D firms have a large outside shareholder); early-1990s activism wave (CalPERS, Putnam, J.P. Morgan targeting Kodak, IBM, Westinghouse, GM); Fidelity Magellan 1995: 49% of holdings in ≥5% stakes, then cut tech from 45% to 8.5% ahead of the downturn; the Vinik/Micron talk-up-while-selling episode; Robert Pozen (Fidelity GC) quote that activism is reactive, "beyond the pale."

### Referee-facing strengths/weaknesses
Strengths: the direct/trading impact decomposition is a durable conceptual contribution; produces cross-sectional predictions (which firms attract activists) that match anecdotes and Z&P evidence; policy analysis (16(b), 144A) is rare and concrete. Weaknesses: quotes independent of order flow removes the price-impact channel that is central to the microstructure literature (and to our paper); liquidity irrelevance is an artifact of free entry; speculators' information is implausibly perfect and instant; intervention technology is a reduced-form (δ, m) pair; the manager is absent — no agency problem is formally modeled, so "intervention" is mechanical; multiple-equilibrium and mixed-strategy regions are handled by sufficient conditions rather than characterization.

### Why no disclosure × takeover feedback
Disclosure regimes never appear — the paper's policy instruments are trading restrictions (short-swing) and share transferability (144A), not information revelation about *stakes*. Takeovers/proxy fights are explicitly abstracted away ("getting management to make the change might involve threatening... a takeover or proxy fight, but we abstract from these details"). There is no bidder, no premium, and no feedback from price to a control transaction.

---

## 3. Faure-Grimaud & Gromb (2004), "Public Trading and Private Incentives", *Review of Financial Studies* 17(4), 985–1014.

### Research question & summary
How does public trading of a firm's stock affect a large shareholder's ("insider's") incentive to undertake privately costly, value-increasing actions? Because the insider may face a liquidity shock forcing him to sell before his effort becomes public, a more informative stock price rewards effort — **market monitoring and insider incentives are complements, not substitutes**. Applications: the going-public decision (informational, not financial, motive), entrepreneurship/VC, security design (information-sensitive outside claims; a reversed pecking order for initial offerings), and exit-as-signal.

### Model architecture
- **Players:** risk-neutral insider holding (1−α) with control rights; dispersed outsiders holding α; one speculator S; competitive market maker; liquidity traders.
- **Technology:** insider exerts unobservable effort e at cost e²/2; V = V_H w.p. (1+e)/2, V_L otherwise; Δv = V_H − V_L; first-best e = Δv/2. **Key functional form: effort raises the mean and lowers the variance** of V (their footnote 2 concedes this drives some signs).
- **Trading (t=2), simplified Kyle:** liquidity demand d_L ∈ {0, −d} equiprobable, d = d(α) increasing in float; S observes his info-acquisition cost k ~ F (publicly drawn) and pays k to learn V perfectly; informed S submits d_s = 0 if V_H, −d if V_L (camouflage). MM observes the two orders but not identities; if orders match, price = V(e^a) (uninformative); if they differ, price fully reveals. Price informativeness p = F(π(e)) with speculator profit π increasing in d and Δv, decreasing in e^a.
- **Exit (t=3):** insider hit by liquidity shock w.p. λ and must sell his entire stake at P3 = P2 (buyers have public info only; insider cannot trade anonymously). V revealed at t=4.
- **Section 3 (exit as signal):** shock replaced by an outside investment opportunity with return (1+ρ), ρ ~ G; insider observes V at t=2 and sells iff ρ > (V − P3)/P3 — a lemons problem in the block sale.

### Key results (all analytical)
- **Lemma 1:** p increases in liquidity-trade variance d, in Δv, and with FOSD-lower info costs k; decreases in anticipated effort e^a (via the variance-reduction assumption). **Lemma 2:** effort increases in stake (direct effect) and in p (indirect/market-monitoring effect).
- **Prop 1:** equilibrium effort e* (fixed point of p(e) decreasing and e(p) increasing) rises with the informativeness function and Δv, falls in λ.
- **Prop 2:** even if IPO proceeds are zero, for λ and Δv large enough firm value is maximized with 0 < α < 1 — going public is optimal purely for information production.
- **Prop 3:** with IPO pricing à la Holmström–Tirole (P0 discounted by speculator profits), there is a threshold λ* ∈ (0,1): go public iff λ > λ*. **Cor 1:** IPOs are preludes to further equity sales (SEOs/private placements). **Prop 4 & Cor 2:** more informative markets → more IPOs and more firm creation; speculator-investment complementarity can generate multiple equilibria.
- **Cor 3 (security design):** high-λ insiders prefer issuing equity to risk-free debt; more generally a trade-off between value-sensitivity of the insider's claim and information-sensitivity of traded claims; a **reverse pecking order** (information-sensitive securities first) can arise for initial offerings.
- **Prop 5 (exit-as-signal):** an increase in price informativeness (i) has an **ambiguous** effect on the unconditional probability of exit (direct effect ↑ exit in the good state; feedback effect ↑ effort → ↑ V_H frequency → ↓ exit), yet (ii) **strictly increases effort** — more exit can coincide with more effort. **Lemma 3/Cor 4:** under uninformative prices the insider always exits when V = V_L and exits when V = V_H only if ρ exceeds the lemons threshold ρ̂(P2) = (V_H − P2)/P2.
- **Appendix F:** closed-form optimal float α* (uniform k, discrete effort), α* increasing in λ. **Appendix I:** partial-sale signaling; the "best" separating equilibrium survives Cho–Kreps.

### Proven vs assumed
All propositions proven. Deliberate simplifications a referee will note: p(·) is not tied to float in the main text ("we do not assume price informativeness to increase with the float") — the interior optimal float exists only in the specialized Appendix F; the effort-reduces-variance assumption drives Lemma 1(ii) and the stability of the e–p fixed point; insider barred from anonymous trading (kills the Kyle–Vila camouflage channel by assumption, explicitly to differentiate from Maug/KW); P3 = P2 rules out bilateral block bargaining; multiple equilibria in the exit game resolved by an admitted "somewhat arbitrary" selection (most-exit equilibrium).

### Institutional facts
VCs do not liquidate at IPO (Lerner 1994); issue splitting and SEO clustering (Jegadeesh–Weinstein–Welch 1990; Welch 1996); Black & Gilson (1998) on active IPO markets enabling VC; Brennan & Franks (1997) UK IPO dispersion. Notably, the paper **explicitly brackets both disclosure and takeovers**: "this disciplinary effect is not related to the firm facing more stringent disclosure requirements or being on the market for corporate control" (p. 996). Footnote 8 contains the closest thing to a disclosure observation: stricter disclosure rules in developed markets would raise k (less private information to acquire) — an ambiguity they set aside.

### Referee-facing strengths/weaknesses
Strengths: a clean, novel mechanism (price informativeness as incentive device via liquidation risk) with wide applicability; honest about functional-form drivers; the exit-as-signal section anticipates the "exit vs. voice" framing. Weaknesses: informativeness is essentially exogenous w.r.t. float in the core model; the variance-reduction assumption is non-standard and load-bearing; no anonymity means the paper cannot speak to order-flow inference at all — its "liquidity" is d, the depth of noise trading, not a κ measuring inference precision; no manager, no bidder, no premium.

### Why no disclosure × takeover feedback
By design: the paper's contribution is the informativeness→effort channel, and the authors explicitly disclaim disclosure-regime and control-market channels. A bidder responding to the price would introduce a second loop (price → control transfer → value) orthogonal to their liquidation-risk loop; they leave it to future work ("we have not considered the firm's fate following the insider's exit... whether exit results in dispersion of the block or its transfer to a new large shareholder").

---

## 4. Admati & Pfleiderer (2009), "The 'Wall Street Walk' and Shareholder Activism: Exit as a Form of Voice", *Review of Financial Studies* 22(7), 2645–2685.

### Research question & summary
Can the credible *threat of exit* by a privately informed large shareholder discipline a manager whose compensation depends on the stock price? Yes, often — but the mechanism's power depends sharply on (i) the type of agency problem (deterring a "bad" action, Model B, vs. inducing a "good" action, Model G) and (ii) the information structure. More private information need not help; in Model G the large shareholder's presence can be **dysfunctional** (raise agency costs). Exit need not occur in equilibrium for the threat to work.

### Model architecture
- **Players:** manager M; large shareholder L (female); competitive risk-neutral market makers setting P1 and P2 equal to conditional expectations of value given public information (including L's *observable* trade — no anonymous trading in the base model).
- **Uncertainty:** status-quo value ν known; action's impact δ̃ ~ f(·) on [0, δ̄], observed by M before deciding. Model B: action destroys δ̃, gives M private benefit β; Model G: action creates δ̃, costs M private cost β (β fixed, known). Final period: ã and δ̃ publicly revealed; P2 = ν ∓ ãδ̃.
- **Compensation:** exogenous linear contract ω1P1 + ω2P2 (ω1, ω2 > 0) — the channel through which L's trade disciplines M.
- **L's trading:** with prob θ a liquidity shock forces a full sale; otherwise L sells iff E[value | her info] < P1. Liquidity-shock noise θ is what makes exit *not fully revealing* and gives L trading profits in extended versions; in the base model her ex ante trading profit is zero (observable trade).
- **Equilibrium:** Bayesian–Nash; cutoff strategies (B: act iff δ̃ ≤ x_B; G: act iff δ̃ ≥ x_G); benchmark without L: x = β/ω2. Agency cost: E[ãδ̃] (B) and E[δ̃] − E[ãδ̃] (G). Equilibria classified **disciplining / non-disciplining / dysfunctional**.
- **Information structures:** L sees action only (B^a, G^a); L sees action + impact (B^{a,δ}, G^{a,δ}); action public + L sees impact privately (B^{a,δ}_a, G^{a,δ}_a); impact public + L sees action (B^{a,δ}_δ, G^{a,δ}_δ).

### Key results (all analytical)
- **Prop 1:** B^a and G^a have unique, always-disciplining equilibria; cutoffs satisfy β − (1−θ)ω1(E_s − E_ns) − ω2x = 0 (B) and the mirrored version (G); both cutoffs **increase in θ** (more liquidity-shock noise → less informative exit → less discipline); **x_G < x_B** — L is more effective in Model G because E[δ̃|δ̃≥x] > E[δ̃|δ̃≤x] makes the exit/no-exit price wedge larger. In Model B the disciplining tool |E_s − E_ns| → 0 as x → 0 (the tool vanishes as alignment improves); not so in G.
- **Prop 2:** B^{a,δ}: equilibrium exists (unique under uniform δ̃), always disciplining; L sells only if action taken **and** δ̃ ≥ E_s — exit can be vanishingly rare (prob → 0 as θ → 0) yet discipline survives (off-path threat).
- **Prop 3 (more information can hurt):** for every distribution there is θ̂ such that for θ > θ̂, L is *more* effective in B^a (less information) than in any equilibrium of B^{a,δ} — as exit noise grows, the no-sale event's information content dominates, and it differs across the two structures.
- **Prop 4:** G^{a,δ} has a unique equilibrium that is **never better** than G^a and can be wholly non-disciplining (if E_s(x_G) > x_G, L prefers selling even when M acts — discipline unravels).
- **Prop 5:** B^{a,δ}_a (action public): unique, disciplining, and yields the **lowest agency cost among all Model-B structures**. **Prop 6:** G^{a,δ}_a: unique and **dysfunctional** — L's exit at the cutoff causes the market to revise δ̃ *downward* relative to the action-only inference, weakening M's reward for acting; shareholders are better off without L.
- **Prop 7:** with δ̃ public and only the action private, B and G become exact mirror images (mixed-strategy equilibrium, m_G(δ) = 1 − m_B(δ)); both disciplining — proving the B/G asymmetry comes entirely from inference about δ̃ from L's trade.
- **Section 6.1 (endogenous information & anonymity):** with observable trades L's ex ante trading profit is zero, so information is valuable only through stake appreciation; with anonymous trading among other liquidity traders, L earns positive trading profits (bigger in more liquid markets) which can *fund information acquisition* and increase discipline; discipline can also operate through **post-trade disclosure** of an earlier anonymous exit: "Disclosure requirements such as 13D filings may help bring this about" (footnote 23) — the paper's only (asides-level) disclosure mechanism. **Section 6.2:** transaction costs weaken discipline; exit costs that destroy firm value can paradoxically strengthen it. **Section 6.3:** random β correlated with δ̃ is covered; "model uncertainty" (investors unsure whether B or G) means L can discipline at most one type.
- **Section 7 (empirical predictions):** block-purchase abnormal return R_block should load positively on the **interaction** of L's longevity (1−θ) with ω1 (short-term pay sensitivity), and on the interaction of market liquidity with ω1 — complementarities no monitoring model predicts; effects differ by agency-problem type (mature cash-rich firms ≈ Model B; growth/risky-project firms ≈ Model G). Cites Brenner (2007) global evidence that liquidity and CEO equity-pay share are complements.

### Proven vs assumed
All propositions proven; several comparative statics shown by example (uniform δ̃, Figures 1–2). Load-bearing assumptions a referee will attack: **exogenous linear price-sensitive compensation** (they defend it as a reduced form of a richer contracting problem); MM pricing with no noise traders in the base model (L's trade perfectly observed, so "price impact" is pure inference, not order-flow camouflage); risk neutrality; fixed β; L can sell-or-hold only (buying allowed in an unpublished variant, claimed robust); tie-breaking rules; equilibrium multiplicity at θ = 0 handled by taking limits from θ > 0. The mechanism requires that **M knows L is informed** — an awareness assumption they tie to 13D filings and jawboning.

### Institutional facts
Schedule 13D filings as the device making L's informed status public (fn 23); hedge-fund activism evidence (Brav et al. 2006; Klein & Zur 2006 — threat of proxy fight works even unmentioned; Clifford 2007 — Steel Partners' 13D threatening to sell); Parrino, Sias & Starks (2003) — institutions sell ahead of CEO turnover with price impact; Sias, Starks & Titman (2001); Carleton, Nelson & Weisbach (1998) — private negotiations (jawboning) work; Massimo & Simonov (2006) and Qiu (2006) — non-controlling blockholders deter bad acquisitions; Brenner (2007) cross-country liquidity × pay-sensitivity complementarity.

### Referee-facing strengths/weaknesses
Strengths: reframes exit as governance (answering Coffee/Bhide from a new angle); the disciplining/non-disciplining/dysfunctional taxonomy and the B/G asymmetry are sharp, falsifiable contributions; empirical-prediction section is unusually concrete (interaction regressions). Weaknesses: compensation exogeneity is the biggest target (ω1 exogenous; if shareholders could design the contract, the L-channel might be redundant); no microstructure — liquidity enters only as θ (shock noise) or transaction costs, not as order-flow inference; static; "awareness" assumption; no bidder/takeover anywhere — governance runs entirely through managerial pay.

### Why no disclosure × takeover feedback
13D appears only as an off-model justification for why M knows L is informed; the threshold structure of disclosure (5% trigger, 10-day window) is never modeled, and disclosure never interacts with inference about fundamentals from order flow. Takeovers are excluded because the disciplining sink is managerial compensation, not control transfer; adding a bidder would require a second strategic player responding to P1, which their Bayesian pricing structure (P1 = conditional expectation, no noise traders) cannot accommodate without a Kyle-style apparatus.

---

## Cross-strand synthesis: implications for repositioning our paper

### A. The state of the classics' playing field
All four papers answer Coffee/Bhide with variants of "liquidity need not hurt governance," but through four *different, non-nested* liquidity concepts:
1. **Maug:** liquidity = camouflage for informed trading (φ) → funds monitoring → **liquidity monotone-good** (given endogenous stakes below cost-recovery).
2. **KW:** liquidity = noise volume (u) → **irrelevant** to intervention when speculators can enter freely; what matters is whether intervention *increases* the activist's information advantage (sign of 1−2q′).
3. **FG:** liquidity/informativeness = probability the price reflects effort (p) → **monotone-good** for effort via liquidation risk.
4. **AP:** liquidity noise = θ (probability exit is non-informational) → **monotone-bad** for the exit-threat channel, but anonymous-trading profits (bigger in liquid markets) can fund information acquisition — the only non-monotone tension in the set, and it is discussed, not modeled.

**None has a bidder, a tender decision, or a takeover premium.** Takeovers in Maug are a relabeled intervention technology; in KW and FG they are explicitly abstracted away; in AP they are absent. Minority shareholders in all four are mechanical price-takers or free-riders — never players whose tendering determines a premium. **Our paper's core objects — expected minority takeover gains Δ(κ) and the sensitivity of premia to liquidity under different disclosure regimes — occupy genuinely unclaimed territory in this strand.** The claim "first to combine stake-triggered disclosure with takeover feedback in a microstructure model" is defensible against these four (the takeover-game literature — Grossman–Hart, Shleifer–Vishny, Kyle–Vila, Burkart–Gromb–Panunzi — is the other flank and must be checked by the takeover-strand researcher).

### B. Proven-vs-numerical bar (critical for our R1/R2 repositioning)
The classics set a discipline: **every comparative static is a signed derivative or a monotone comparative static proven from closed-form cutoffs**, all under binary values + risk neutrality + one strategic mixing probability. Their honesty labels are clean because their algebras are small. Against that bar, our R1 (hump shape of Δ(κ)) being "numerically verified" and uniqueness "numerical only" is the exposed flank. Concrete borrowings to convert numerics into theorems:
- **Adopt AP's cutoff architecture:** their entire paper runs on one indifference condition β − (1−θ)ω1(E_s − E_ns) − ω2x = 0 with E_s, E_ns closed-form conditional expectations over a cutoff strategy; all results follow from monotonicity of truncated means (E[δ|δ≤x] vs E[δ|δ≥x]). Our bidder-entry and disclosure-branch objects should be forced into the same shape: one indifference condition per player, comparative statics = signs of monotone truncated means.
- **Adopt Maug's three-point order flow** ({−3u, −u, u}) as the simplest inference structure in which a disclosed vs inferred branch split can be written in closed form; his Prop 2 pivot condition (α(H−L) ≷ c_M) is the template for how a single inequality can carry an entire paper's sign results — our disclosure-attenuation theorem (R2) should be presented as such a pivot inequality.
- **KW's sign(1−2q′) trick:** a whole taxonomy from the derivative of variance q′(1−q′). Our hump shape likely comes from Δ(κ) inheriting the product of two monotone terms (entry probability × premium conditional on entry); exhibiting it as the derivative of a variance-like object with an interior max may give an analytical interior-maximum proof under endpoint symmetry.
- Where full generality fails, do what all four do: **prove the base model and label extensions** (KW's Prop A.1 "sufficient conditions"; AP's uniform-distribution examples; FG's Appendix F specialization). A numerically-verified extension is acceptable to referees *if the stripped core is fully proved* — none of the four proves everything they claim interest in.

### C. Institutional facts to harvest (for the empirics move)
From these four papers, citable institutional anchors: 5% mutual-fund holding limit (Maug fn 6); **Section 16(b) short-swing rule — 10% threshold, 6-month forfeiture** (KW, formal analysis of its perverse effects); **Rule 144A restricted shares** and their 34%/13.5% discounts (KW, citing Silber 1991, Hertzel & Smith 1993); **Schedule 13D as the device making informed status common knowledge** (AP fn 23 — exactly the awareness channel our disclosure threshold formalizes); hedge-fund 13D activism facts (Brav et al., Klein & Zur, Clifford via AP); CalPERS targeting and vote outcomes (Maug's citations: Nesbitt, Smith, Wahal, Gordon & Pound); VC exit behavior and IPO→SEO sequencing (FG, citing Lerner, Welch). Our EDGAR 13D/G empirics should be framed as testing the information-structure comparative statics (disclosed vs inferred blocks), which AP's Section 7 explicitly invites but never tests.

### D. Framing/differentiation opportunities
1. **"Liquidity" is not one object.** The four classics use four different parameters (φ, u, p, θ) with three different signs of effect. Our κ can be positioned as the *inference-precise* notion (order-flow signal-to-noise), and our hump shape as the reconciliation: liquidity helps the activist's camouflage (Maug) while hurting minority information rents/bidder entry — the sign flips exactly because we add the takeover margin they all lacked.
2. **Disclosure is the missing strategic variable in all four.** Maug: disclosure kills camouflage (one sentence). KW: short-swing disclosure/trading rules backfire (analyzed, but as trading restrictions). AP: 13D helps by certifying informedness (one footnote). FG: stricter disclosure raises k (one footnote, flagged as ambiguous). These are *four contradictory one-liners* — our model is the first to let a disclosure threshold reallocate inference across branches and interact with bidder entry. This is the strongest repositioning hook this strand offers.
3. **Anticipate the "why no bidder in the classics" referee question** and turn it into our motivation: adding a bidder to Maug's camouflage algebra or AP's observable-trade pricing breaks their closed forms; our technical contribution is doing it with a tractable branch split. But referees conditioned on these four papers will demand the same standard: binary values, risk neutrality, one mixing probability, closed-form cutoffs.
4. **The B/G asymmetry (AP) is a caution for our welfare statements:** any claim that "disclosure/attenuation is good" must specify whose agency problem; AP shows identical information structures flip welfare signs across agency types. Our R2 (attenuation) should be stated as a sensitivity result, not a welfare result, unless we add a welfare module.
5. **Cite-or-differentiate list:** Maug (liquidity funds monitoring; endogenous stake as commitment; takeovers as alternative intervention — differentiate: no bidder/premium), KW (trading impact sign; 16(b)/144A analysis — differentiate: order-flow-independent quotes, liquidity irrelevance), FG (informativeness→effort; explicitly disclaims disclosure and control-market channels — cite for the disclaimer itself), AP (exit-as-voice; 13D awareness footnote; empirical-interaction predictions — cite for the awareness assumption we endogenize, differentiate: they have no bidder and liquidity only as exit noise).

### E. What to kill or de-emphasize in our draft, given this strand
- Any framing implying we are the first to link liquidity and activism — four JF/RFS classics own that ground; we must own **liquidity × disclosure × takeover premia**.
- Overstated welfare language (see D4).
- Any claim that disclosure unambiguously helps or hurts: the classics' one-liners point in all directions, which is precisely why a model with an interior, regime-dependent answer is publishable — but only if presented as resolving an open ambiguity, not as the first word on the subject.
