# Edmans (2014) — "Blockholders and Corporate Governance"

**Venue / status:** *Annual Review of Financial Economics* **6**, 23–50 (2014). First published online as a Review in Advance, 22 September 2014. doi:10.1146/annurev-financial-110613-034455. JEL G14, G32, G34.
**Full text from:** `lit/edmans-blockholder-survey-2024.pdf` (31 pp). **The file name is misleading — this is the 2014 Annual Review, not a 2024 paper.** The header of PDF page 1 reads "Annu. Rev. Financ. Econ. 2014. 6:23–50". Extracted with `pdftotext -layout` to `research/txt_extracts/edmans_2014_arfe.txt`; that file already existed and is byte-identical to a fresh extraction, so it was not rewritten. · **Reader:** opus · **Read:** full text, printed pp. 23–46 (article body and conclusion) plus the reference list pp. 46–50.
**Page numbering used:** the **printed journal pages 23–50**. Mapping: printed page = PDF page + 22 (PDF p. 1 = printed p. 23; PDF p. 28 = printed p. 50). PDF pages 29–31 are Annual Reviews front matter and advertising, not part of the article.
**Type:** survey   **Role for us:** anchor / template — it is the canonical statement of the exit-versus-voice frame our paper collapses, and it names our whitespace as an open question in its own words.

## 1. Question

What does a large shareholder actually *do* that changes firm value, and through which channel? Edmans organises the literature around three answers: blockholders improve value through **voice** (costly direct intervention), improve it through **exit** (trading on private information, which disciplines a manager who cares about the stock price), or **reduce** it (private benefits, over-monitoring, lost liquidity). He surveys the theory first, drawing out empirical implications, then the evidence, and throughout emphasises four obstacles: causal identification is hard; governance operates through *threats* that are unobservable; there is no theoretically grounded definition of a blockholder; and blockholders are a heterogeneous class treated as homogeneous.

## 2. Model / data and method

Not applicable in the usual sense — this is a narrative literature review with no data, no estimation and no new theorem. What it does supply is a **shared notation** imposed on the surveyed models, which is worth carrying into our own writing because it is the notation a referee in this literature reads in:

| Symbol | Meaning (printed p. 25) |
|---|---|
| *V* | firm value **without** intervention (in exit theories, the long-run fundamental value after the manager's action) |
| *V̄* | firm value **with** intervention |
| *G* = *V̄* − *V* | value created by intervention |
| *P* | price at which the blockholder can trade |
| *a* | the blockholder's stake |
| (1 − *a*) | free float held by liquidity investors |

**Structure.** §1 introduction; §2.1 theories of voice; §2.2 theories of exit; §2.3 theories of the costs of blockholders; §3.1 evidence on blockholders and firm outcomes; §3.2 evidence specific to voice; §3.3 evidence specific to exit; §3.4 evidence on costs; §4 conclusion and directions for future research. Scope is restricted to **outside** blockholders — "large shareholders who are not the firm's officers" (p. 25) — with inside blockholders referred out to the CEO-compensation surveys.

**Two empirical implication classes it defines (p. 33), which are worth adopting:** with *F* a firm characteristic and *B* a blockholder action or holding, **I1** is the effect of *F* on *B* (what determines blockholder presence/action) and **I2** is the effect of *B* on *F* (what blockholders do to the firm). It then lists the identification strategies actually used — instruments for *B* or *F*, lagged variables, event studies in narrow windows, and success/failure or hostile/non-hostile splits — and rates none of them watertight (pp. 33–34).

## 3. Results — with honesty labels

*(Surveyed results, all ASSERTED, each with the underlying paper it is attributed to.)*

Everything in this section is **ASSERTED**: these are the survey's one- or two-sentence summaries of other people's papers. The survey proves nothing and estimates nothing. Where the summary reports a number, the number is the *original* paper's, restated here. Any of these that we want to lean on must be checked against the source paper before it goes into a draft.

### 3a. Theory — voice

| # | Result as the survey states it | Attributed to | Page |
|---|---|---|---|
| V1 | Firm value is monotonically increasing in block size; a larger *a* means a larger share *aG* of restructuring gains, so the blockholder takes the costly control route rather than jawboning | Shleifer & Vishny (1986) | p. 26 |
| V2 | Small shareholders will not tender for *V*, wishing to free-ride on post-acquisition restructuring, which reduces the blockholder's takeover gains | Grossman & Hart (1980) | p. 26 and n. 3 |
| V2b | **(added by verifier) The survey does contain a takeover-premium comparative static.** Because small shareholders cannot observe the restructuring gain *G*, the price *P* they demand exceeds *V* but falls short of *V̄*; and the **larger** the blockholder's initial stake *a*, the *smaller* the restructuring gain small shareholders expect, so the lower *P* is — "Knowing that she will not have to pay as high a takeover premium, the blockholder monitors more to begin with." So: **larger block → lower takeover premium → more ex ante monitoring** | Shleifer & Vishny (1986) with Grossman & Hart (1980) | p. 26 |
| V2c | **(added by verifier) The free-rider problem is channel-specific.** Footnote 3: the Grossman–Hart free-rider problem "is specific to the takeover channel"; it "does not apply to the other channels (e.g., jawboning or voting) that do not require the purchase of additional shares" | Grossman & Hart (1980), as the survey reads them | p. 26 n. 3 |
| V3 | Splitting a block among *N* investors each holding *a*/*N* weakens voice by worsening the free-rider problem | Winton (1993); Noe (2002); Edmans & Manso (2011) | p. 26 |
| V4 | The blockholder may "cut and run" instead of intervening, selling at *P* > *V* because the price embeds a chance of intervention; hence **illiquidity encourages intervention**. But liquidity facilitates block *formation*, because small shareholders sell at a greater discount fearing second-period trading losses | Kahn & Winton (1998) | pp. 26–28 |
| V5 | Liquidity deters voice by making cutting and running easy — argued verbally, later modelled | Coffee (1991); Bhide (1993); formalised by Aghion, Bolton & Tirole (2004) | p. 27 |
| V6 | **Liquidity encourages intervention** if and only if *a* is small, because it lets the blockholder buy more shares at *P* < *V̄*; and with *a* chosen endogenously (via an observable purchase) the blockholder picks a small *a*, so liquidity encourages intervention **overall** | Maug (1998) | p. 27 |
| V7 | **Liquidity deters intervention** — with the stake acquired through an optimal IPO mechanism, dynamic Kyle trading, liquidity trades independent of the free float, and private information on intervention cost, the chosen *a* is typically large, so "cutting and running" dominates | Back, Li & Ljungqvist (2014) | pp. 27–28 |
| V8 | Liquidity helps because speculators' trading pushes *P* toward *V̄*, letting a liquidity-shocked blockholder earn a return on intervention even if forced to sell early | Faure-Grimaud & Gromb (2004) | p. 28 |
| V9 | Liquidity traders let the raider camouflage her accumulation and overcome the free-rider problem; extended to continuous dynamic accumulation with intervention value endogenous in the block size reached | Kyle & Vila (1991); Collin-Dufresne & Fos (2014b) | p. 28 |
| V10 | Insider trading makes cutting and running worse: the manager will voluntarily leak bad news to induce the blockholder to sell rather than intervene | Maug (2002) | p. 27 n. 6 |

### 3b. Theory — exit

| # | Result as the survey states it | Attributed to | Page |
|---|---|---|---|
| X1 | A blockholder who cannot exercise voice still governs by trading: her informed selling drives *P* toward the true *V*, and because the manager weights *P*, his ex ante incentives improve. Admati & Pfleiderer show exit "typically" raises effort but "in some cases can worsen the agency problem" | Admati & Pfleiderer (2009); Edmans (2009) | p. 29 |
| X2 | Exit is *not* the same as selling: it works through the **threat**, and the blockholder need not be aware of her disciplinary effect for it to operate | Edmans (2009) as read by the survey | p. 30 |
| X3 | Short-sale constraints microfound why the *blockholder* is the informed trader: a zero-position trader cannot act on bad news, so information-gathering incentives rise in *a* — but only up to a point, because price impact caps how much she can dump. Hence a **finite optimal block size**, matching the prevalence of small US blocks | Edmans (2009) | p. 30 |
| X4 | **Liquidity enhances exit through three channels** — she trades more aggressively on given information; she gathers more information because trading is more profitable; and she acquires a larger initial block. The one offsetting cost is that camouflage reduces the price impact of a given trade. The **net effect on price informativeness, and hence on managerial incentives, is positive** | Edmans (2009); with transaction-cost version in Admati & Pfleiderer (2009) | p. 30 |
| X5 | Multiple blockholders **strengthen** exit — the same coordination failure that ruins voice makes them trade Cournot-aggressively rather than strategically limiting orders as a monopolist would | Edmans & Manso (2011); cf. Holden & Subrahmanyam (1992) | pp. 30–31 |
| X6 | Exit's power rises with the manager's **short-term** concerns (weight on *P* rather than *V*), which is a different object from his total equity incentives; measurable by equity scheduled to vest in the period | Edmans, Fang & Lewellen (2014); Edmans et al. (2014) | p. 31 |
| X7 | Blockholder liquidity shocks weaken exit (she may sell even when the manager behaves); forced-liquidation risk can even make her buy to prop up the price, and the manager then chooses excessive asset complexity to sustain the manipulation | Admati & Pfleiderer (2009); Goldman & Strobl (2013) | p. 31 |
| X8 | Career concerns weaken exit — a fund will not sell because selling admits a bad pick — but can *strengthen* voice by breaking the free-rider problem among reputation-conscious blockholders | Dasgupta & Piacentino (2014); Song (2013) | p. 31 |
| X9 | Multi-firm ownership: exit can be disguised as a portfolio-wide liquidity shock (weakening governance), but also allows punishing one manager by selling only his firm (strengthening it). Net effect is stronger governance than a single-firm benchmark **iff the agency problem is strong**; it also induces correlated prices with uncorrelated fundamentals | Edmans, Levit & Reilly (2014) | pp. 31–32 |
| X10 | Voice and exit combined in a cheap-talk model: the option to exit makes the blockholder less misaligned with the manager, so he follows her recommendation. Exit improves governance **even if the manager does not care about *P***, by making voice credible. And **more frequent liquidity shocks can raise her effectiveness** | Levit (2013) | p. 32 |
| X11 | A blockholder with a large enough stake will buy to counteract a manipulative bear raid, even at a trading loss; more private information can *weaken* governance by tempting her to trade rather than defend | Khanna & Mathews (2012), building on Goldstein & Guembel (2008) | p. 32 |

### 3c. Theory — costs of blockholders

| # | Result as the survey states it | Attributed to | Page |
|---|---|---|---|
| C1 | The ex ante *threat* of intervention destroys managerial initiative, so optimal block size is finite even in a pure voice model | Burkart, Gromb & Panunzi (1997) | p. 32 |
| C2 | A founder going public chooses a low block size because the blockholder's monitoring calculus ignores the private benefits it destroys | Pagano & Röell (1998) | p. 32 |
| C3 | **A larger block lowers the free float 1 − *a* and reduces liquidity** | Bolton & von Thadden (1998) | p. 33 |
| C4 | Private benefits need not come at other shareholders' expense; block trades at a premium to the post-announcement price also raise the stock price | Barclay & Holderness (1992) | p. 33 |
| C5 | A majority investor deters other blocks from forming — "large shareholders 'create their own space'" | Zwiebel (1995) | p. 33 |
| C6 | Conflicted voting: labour-union funds vote for labour-friendly directors; mutual funds side with management to preserve business ties | Agrawal (2012); Davis & Kim (2007) | p. 33 |

### 3d. Evidence — the numbers the survey restates

| # | Result as the survey states it | Attributed to | Page |
|---|---|---|---|
| E1 | **96% of US firms have at least one 5% blockholder**; 15th highest of 22 countries | Holderness (2009) | p. 24 |
| E2 | Only **20% (10%) of large (medium) US firms** have a blockholder with ≥20%, the estimated control threshold; median US block size is 8.9% (Holderness, personal correspondence) | La Porta, Lopez-de-Silanes & Shleifer (1999); Holderness (2009) | p. 29 and n. 9 |
| E3 | **70% of US firms have multiple 5% blockholders**; 34% of European firms at a 10% threshold, 48% in Finland, 39% in Western Europe | Edmans & Manso (2011) using Dlugosz et al. (2006); Laeven & Levine (2007); Maury & Pajuste (2005); Faccio & Lang (2002) | p. 41 |
| E4 | Large-block trades produce a **16% increase in market value** | Barclay & Holderness (1991) | p. 36 |
| E5 | Negotiated block trades occur at a **20% premium** to market, reflecting private benefits of control | Barclay & Holderness (1989) | p. 43 |
| E6 | Private benefits estimated structurally at **10% of block value / 3–4% of target equity**; firm value falls **$1.76 per $1 of private benefit**; block trades raise firm value **19%** | Albuquerque & Schroth (2010) | p. 43 |
| E7 | **13D filings by activist hedge funds earn 7–8% abnormal returns over (−20, +20)**; +3.9% more when tactics are hostile; exits following failed activism earn 8% less than the full exit sample; and 13D filings improve total payout, ROA and operating margins | Brav et al. (2008) | p. 39 |
| E7b | **(added by verifier) 13D versus 13G is priced.** Compared with 13G filings, **13D filings by hedge fund activists produce larger event-study returns and larger improvements in return on assets** — read by the survey as the return to activism over and above stock picking | Clifford (2008) | p. 39 |
| E8 | Confrontational hedge-fund activism earns **10.2% over (−30, +30)** versus 5.1% for other activist targets | Klein & Zur (2009) | p. 39 |
| E9 | **The abnormal returns to 13D filings come from the activist's ability to force a takeover** — announcement and long-term returns are significant only for targets ultimately acquired, insignificant for those that stay independent | Greenwood & Schor (2009) | p. 39 |
| E10 | Behind-the-scenes activism: TIAA-CREF reached agreement 95% of the time, >70% of those without a shareholder vote, with little short-term price effect because the letters were private | Carleton, Nelson & Weisbach (1998) | p. 40 |
| E11 | Hermes UK Focus Fund: "engagement rarely took a public form"; mean abnormal (−3, +3) return of **5.3%** when objectives were achieved and announced, higher for confrontational engagements | Becht et al. (2009) | p. 40 |
| E12 | **Exit is the number-one governance mechanism blockholders report using: 80% of institutions will sell shares** in response to dissatisfaction, more than any voice channel | McCahery, Sautner & Starks (2011) | p. 41 |
| E13 | Proxy-fight *threat* (two-stage model, liquidity as the instrument) causes higher leverage, dividends and CEO turnover, and lower R&D, capex and executive pay. **(added by verifier) The survey's own caveat: "He studies all proxy fights, rather than only proxy fights by blockholders" (p. 40)** | Fos (2013) | p. 40 |
| E14 | **Decimalization (2001) → liquidity raises the frequency of proxy fights and shareholder proposals**, and investors buy additional shares before engaging, as Maug (1998) predicts | Norli, Ostergaard & Schindele (2014) | p. 40 |
| E15 | **Three other liquidity shocks (brokerage closures, market-maker closures, retail–institutional brokerage mergers) → liquidity *reduces* hedge-fund activist campaigns and shareholder proposals** | Back, Li & Ljungqvist (2014) | p. 40 |
| E16 | **Decimalization → liquidity causally raises the likelihood of an activist hedge fund filing a 13D**, and raises block acquisition generally (13D or 13G); conditional on a block forming it raises the probability of a **13G rather than a 13D**, with the unconditional 13D effect still positive; a 13G filing produces a positive event reaction, positive holding-period returns and operating improvements, especially in high-liquidity firms | Edmans, Fang & Zur (2013) | pp. 40, 42 and n. 19 |
| E17 | Liquidity causes higher firm value; the effect is stronger where block ownership is greater, and stronger still where the manager has more equity incentives — read as support for the **exit** channel | Fang, Noe & Tice (2009); Bharath, Jayaraman & Nagar (2013) | p. 42 |
| E18 | **In M&A specifically:** liquidity correlates with *lower* M&A returns when there is a single blockholder (voice most likely) but not with multiple blockholders (exit most likely) | Roosenboom, Schlingemann & Vasconcelos (2014) | p. 42 |
| E19 | Capital-gains lock-in (an investor-specific liquidity friction) **raises** the likelihood of voting against management and **lowers** the likelihood of exit | Dimmock et al. (2013) | p. 43 |
| E20 | **Trades by 13D filers over the 60 days before the filing date — which the filing itself must disclose — are highly profitable**, and purchases by eventual 13D filers over that window raise prices | Collin-Dufresne & Fos (2014a) | pp. 41–42 |
| E21 | No correlation between liquidity and governance choices for blockholders in general (as opposed to hedge funds) | Gerken (2014) | p. 42 |
| E22 | Null results: majority-blockholder firms show insignificant differences in investment, accounting returns, Tobin's Q, leverage and control-transaction frequency; no correlation between outside block ownership and firm value or ROA | Holderness & Sheehan (1988); McConnell & Servaes (1990); Mehran (1995) | p. 36 |
| E23 | Russell 1000/2000 index assignment as an instrument for institutional ownership → higher dividends, repurchases and operating performance, lower CEO pay, **not driven by activists** (read as evidence for exit); a fuzzy-RD version finds higher pay-performance sensitivity, more CEO turnover, lower capex | Crane, Michenaud & Weston (2014); Mullins (2014) | p. 37 |
| E24 | Activism became "particularly frequent after the 1992 proxy form that reduced the costs of communication among shareholders" | (survey's own reading of the activism literature) | p. 39 |

## 4. Institutional facts used

- **Schedule 13 / the 5% threshold.** "In the United States, a blockholder is typically defined as a 5% shareholder. However, rather than being motivated by theory, this definition arises because investors are required to file a Schedule 13 disclosure upon crossing a 5% threshold" (p. 35). The survey states the rule *as the reason the empirical literature's central variable exists*.
- **13D versus 13G.** On crossing 5%, a shareholder files a Schedule 13; **13D** if she intends to intervene, and she must "state in Item 4 the form of intervention she intends to employ"; **13G** if she intends to remain passive, "which is shorter and comes with fewer disclosure requirements" (p. 39). A blockholder intending passivity *may* still file a 13D but is unlikely to, given the benefits of the 13G route (p. 39).
- **The pre-filing window.** 13D filers must disclose their trades over the **60 days before the filing date** (p. 41, via Collin-Dufresne & Fos 2014a). This is the survey's only reference to the filing-window margin, and it appears as a *data source* rather than as an economic object.
- **Clustering below the threshold.** "In practice, investors may cluster just below 5% to avoid disclosure, and thus be missed by Schedule 13 filings" (p. 35).
- **13F filings** identify institutional stakes below 5% and are repeatedly proposed as the way around the 5% definitional problem (pp. 35, 45).
- **Investment Company Act of 1940**: a "diversified" mutual fund may, over 75% of its portfolio, hold no more than 5% in any one security and no more than 10% of one company's voting rights (p. 38 n. 17). "Prudent man" rules constrain pension funds from taking stakes in troubled firms (p. 38, citing Del Guercio 1996).
- **1992 proxy rule change** reduced shareholder communication costs and coincided with a jump in activism (p. 39).
- **Decimalization of the major US exchanges in 2001** is the workhorse liquidity shock in the surveyed empirical literature (pp. 40, 42).
- **Financial transaction tax**: ten EU member states agreed to implement one by January 2016, "partly motivated by" the argument that illiquidity locks shareholders in and induces voice (p. 27).

## 5. Referee-facing strengths / weaknesses

**Strengths.**
- It is the field's standard citation for the exit/voice taxonomy and is written by the author of the central exit model, so its framing *is* the frame a referee has in mind.
- The imposed common notation (*V*, *V̄*, *G*, *P*, *a*) makes the models genuinely comparable rather than merely listed, and it is a notation we can adopt for free.
- It is unusually candid about what the literature does not know, and it names the open questions in a form specific enough to be quoted back.
- The four "empirical challenges" (unobservable threats, no blockholder definition, heterogeneity, endogeneity) are a ready-made referee checklist for anyone writing blockholder empirics.

**Weaknesses / open flanks — for us, these are opportunities.**
- **It is 2014.** It predates the 2024 acceleration of the 13D window entirely, predates the modern activism-disclosure debate, and its most-cited empirical anchors (decimalization, Russell reconstitution) are exactly the shocks the subsequent decade used up.
- **The disclosure rule appears only as a measurement nuisance, never as an economic mechanism.** The 5% threshold is discussed three times (pp. 25, 35, 45) and every time the point is "this is an arbitrary place to cut the data". That the rule *creates a partition of the market's information* — that some blockholders are flagged and others pooled, and that this changes prices, entry and premia — is never raised. The closest the survey comes is E16, where the 13D/13G choice is treated as a *revealed preference* over governance mechanism rather than as a choice over how much to reveal.
- **The filing window is invisible.** The 60-day pre-filing trading disclosure appears once, as a source of data on profitable accumulation, not as a policy margin with a length that could be changed.
- **Liquidity's effect on governance is left genuinely unresolved and the survey says so.** Maug says liquidity helps voice; Kahn-Winton and Back-Li-Ljungqvist say it hurts; Edmans says it helps exit; and the empirical evidence is directly contradictory (E14 vs E15 — decimalization raises activism, other liquidity shocks lower it). The survey reports this without adjudicating.
- **No numbers of its own, no meta-analysis, no vote count.** Everything is ASSERTED at second hand, so nothing in it can be cited as evidence, only as a characterisation of the literature.
- **Its own scope note excludes control:** the survey routes takeovers and corporate control out to Holderness (2003) as "an excellent survey" of the earlier voice-and-control literature (p. 25). Control outcomes are therefore not systematically covered here.

## 6. What they do NOT do (scope boundary)

**Object.** The survey's objects are **firm value, profitability, investment, payout, CEO pay and turnover, price informativeness, and block formation**. **Takeover premium is not an object** — but *(corrected by verifier)* it is not absent either: on **p. 26** the survey states a takeover-premium comparative static as part of the Shleifer–Vishny/Grossman–Hart mechanism ("Knowing that she will not have to pay as high a takeover premium, the blockholder monitors more to begin with"), and footnote 3 on the same page restricts the free-rider problem to the takeover channel. So the premium enters as a *price the blockholder pays*, a determinant of her monitoring incentive — never as an outcome to be explained, and never measured. See §7.3a. Corporate control otherwise appears only as (i) one of three intervention channels in Shleifer & Vishny (p. 26), (ii) Greenwood & Schor's finding that 13D returns come from forced takeovers (p. 39), and (iii) the Roosenboom et al. M&A-returns result (p. 42). The survey explicitly hands the control literature off: it notes that "early voice theories spawned an empirical literature on blockholders and corporate control (for an excellent survey, see Holderness 2003)" (p. 25). **Bidder entry is nowhere.**

**Margin.** **The disclosure rule is described but never studied as a margin.** Neither the threshold level nor the filing window is treated as something that could move, or whose movement would have consequences. Every mention of the 5% rule **as a definitional matter** is a caveat about measurement: p. 25 ("rather than a discontinuity at 5%"), p. 35 ("rather than being motivated by theory"), p. 45 ("theory models do not predict a discontinuity at 5%"). *(verifier: "Schedule 13" also appears at p. 37 — heterogeneity in event-study returns to Schedule 13 filings across investor types — and at p. 39 for the 13D/13G mechanics. Neither is a measurement caveat, but neither treats the rule as a movable margin, so the claim stands with those two pages added to the tally.)* The 13D/13G choice (E16) is the single place where the *content* of disclosure has economic consequences, and even there the interpretation is about which governance channel the blockholder has chosen, not about what the market learns.

**Identification.** None — it is a survey. Its methodological contribution is a taxonomy of *other people's* identification strategies (pp. 33–34) and an explicit statement that "None is watertight".

**What it names as open questions (verbatim).** The conclusion (§4, pp. 44–45) lists these, and three of them sit directly on top of our position:
1. *"Even a question as fundamental as the impact of blockholders on firm value remains unanswered."* (p. 44)
2. *"Current exit theories consider a single trading round, but in reality there may be multiple periods across which the blockholder may trade on her information."* (p. 44)
3. *"In addition, the recent financial crisis has led to a number of regulatory changes (e.g., short-sale restrictions) that affect financial markets, and thus may be used to identify casual effects."* (p. 44 — "casual" is a typo for "causal" in the original; reproduce with [sic] if quoted)
4. *"Although most empirical papers define a blockholder as a 5% shareholder, theory models do not predict a discontinuity at 5%. Particular attention could be paid to how the effectiveness of governance depends on block size."* (p. 45)
5. *"In addition, other data sources such as 13F filings may allow researchers to consider blockholders with stakes below 5%."* (p. 45)
6. On voice–exit interaction: the few papers combining them "assume the same blockholder engages in both, but in reality, different blockholders have expertise in different strategies" (p. 45).
7. **(added by verifier)** Immediately after (2), the same paragraph goes further: *"combining liquidity shocks with multiple periods and multiple informed traders may lead to additional interesting insights, such as the possibility of **front running** (e.g., Brunnermeier & Pedersen 2005)."* (p. 44). This is the survey asking, in 2014, for exactly the object our window margin creates — pre-flag accumulation with more than one informed trader in the market, where the length of the disclosure delay determines how much accumulation happens before anyone can trade against it.
8. Blockholder-level agency problems, index funds (BlackRock was the largest shareholder of one in five US-listed firms in 2011, per Davis 2013), and empty voting are named as under-studied categories (p. 45).

## 7. Implications for our position

**What this paper occupies:** object = firm value and firm policies (not premium, not bidder entry); margin = **none** — the disclosure rule is a measurement caveat, not an object; identification = none, it is a survey. **It is not a competitor. It is the map of the field our position has to be placed on, and it draws our whitespace for us.**

**7.1 It hands us the whitespace in its own words.**
Read (4) above carefully. The survey's complaint is that the 5% threshold is *theoretically unmotivated* — theory predicts monitoring rises smoothly in *a*, so cutting the data at 5% is an artefact of a filing rule. **Our position is the inversion of that complaint.** We say the discontinuity at 5% is not an artefact at all: it is a legal partition of the market's information, and once you model the partition rather than apologise for it, the discontinuity is exactly where the economics lives. Edmans (2014) says "theory models do not predict a discontinuity at 5%"; our contribution is a theory model that does, and one whose comparative statics run on the two margins of the rule (threshold and window) rather than on *a*. **This sentence, quoted in the introduction of draft_v3, is the cleanest possible motivation for the paper.** It is a survey by the leading author in the field conceding that nobody has modelled the thing we are modelling.

**7.2 Exit versus voice: how the survey frames it, and how our core model should relate to it.**
The frame (p. 24, following Hirschman 1970) is two mechanisms:
- **Voice** = "direct intervention within a firm" — shareholder proposals, private letters, voting against directors. Theories yield "implications for the causes and consequences of activism".
- **Exit** = "trading a firm's shares", the "Wall Street Rule"/"voting with your feet". If the manager destroys value the blockholder sells, pushing the price down and punishing him ex post; ex ante the threat induces value maximisation. Theories "predict how blockholders affect financial markets and how their effectiveness depends on microstructure factors" (p. 24).
Two structural asymmetries the survey stresses and we must not get backwards:
- **Number of blockholders works in opposite directions.** More blockholders weaken voice (free-riding) and *strengthen* exit (Cournot-aggressive trading, Edmans & Manso 2011, p. 30).
- **Only exit depends on the manager's *short-term* weight on *P*** (X6, p. 31). Voice does not.
For draft_v3: our four actions (Exit / Hold / Quiet voice / Public voice) sit inside this frame but our identity is orthogonal to it — CONTEXT.md already says these are "machinery, not identity". The right positioning sentence is that **we do not adjudicate exit versus voice; we show that the disclosure rule partitions the state space in a way that changes what both channels deliver as a *control outcome*.** Levit (2013) (X10) is the nearest antecedent for combining the two, and the survey's own open question (6) — that combined papers assume one blockholder does both — is a flank we can either occupy or explicitly leave alone.

**7.3 Liquidity's two-sided effect: the survey leaves it unresolved, which is both our licence and our hazard.**
The survey's framing of liquidity is the most useful thing in it for us, and it is genuinely two-sided in **three** distinct places:
- **On voice, theory disagrees.** Coffee (1991)/Bhide (1993)/Aghion-Bolton-Tirole (2004): liquidity lets the blockholder cut and run, so it *deters* voice — an argument with real policy weight (it motivated the Japanese lock-in model and, per p. 27, the EU financial transaction tax). Maug (1998): liquidity lets her double down and intervene, and since she endogenously picks a *small* stake, liquidity *encourages* voice on net. Back, Li & Ljungqvist (2014): flip the stake-formation mechanism to an IPO and the chosen stake is *large*, so cutting-and-running dominates and liquidity *deters*. **The sign of the theory turns entirely on how the block is formed and how big it ends up.**
- **On exit, theory agrees:** liquidity helps, through three channels (aggressiveness, information acquisition, larger initial block), net of the camouflage cost (X4, p. 30).
- **On block formation, theory agrees:** liquidity facilitates it (p. 28).
- **Empirically it is a straight contradiction:** decimalization raises proxy fights and proposals (E14) while three other liquidity shocks lower activist campaigns and proposals (E15) — both reported without adjudication on the same page (p. 40).
**Hazard for us:** our κ is a single parameter driving a control outcome, and a referee holding this survey will ask which side of the Maug/Back-Li-Ljungqvist divide we are on. We need an explicit answer. **Licence for us:** the survey establishes that the sign is *not settled*, so a model that produces a **non-monotone** or **partition-contingent** answer is not an oddity — it is the resolution the literature is missing. That is precisely what draft_v2's hump (R1) and disclosure attenuation (T2) claim. But note the honesty constraint from CONTEXT.md: the hump is NUMERICAL, certified only on a grid, and disposable. If we want to say "the sign of the liquidity effect depends on the disclosure margin", that had better be PROVED, not gridded.

**7.3a (added by verifier) The survey already has a takeover-premium mechanism, and it runs the other way. We must say so before a referee does.**
The card originally recorded that "takeover premium is not an object" and left it there. It is not an object, but **p. 26 contains a signed comparative static on the takeover premium** and the sign is the opposite of the one a naive activism story assumes. In Shleifer & Vishny (1986) read through Grossman & Hart (1980): small shareholders will not tender at *V*, they demand a price *P* that impounds their *estimate* of the restructuring gain, so *P* > *V* but *P* < *V̄*. A **larger** initial stake *a* means the blockholder needs a smaller *G* to make bidding worthwhile, so small shareholders rationally expect *less* restructuring, so *P* falls — "Knowing that she will not have to pay as high a takeover premium, the blockholder monitors more to begin with."
**Three consequences for us.**
1. **The premium here is a cost to the blockholder, not a benefit to target shareholders.** Our premium wedge m₁ − m₀ is a transfer *to* minority holders. In this frame the same object is the *price the blockholder must pay to free-riders*, and it *discourages* engagement. A referee holding this survey will ask which of the two we mean. Answer it explicitly in draft_v3: our wedge is the realised offer premium in a completed control transaction, theirs is the tender price in a self-launched bid, and the two coincide only if the blockholder is the acquirer.
2. **The sign clash is real and useful.** Their mechanism says more block → lower premium → more monitoring. Ours says more liquidity → easier accumulation → more engagement → higher premium. Both can be true simultaneously (theirs is about who captures the gain, ours about whether the gain is created), but the paper must say so rather than leave the reader to notice.
3. **Footnote 3 on p. 26 is a gift for our action space.** The Grossman–Hart free-rider problem "is specific to the takeover channel" and "does not apply to the other channels (e.g., jawboning or voting) that do not require the purchase of additional shares." That is precisely the line between our **public voice** (buy above the threshold, be flagged, pay the free-rider price) and our **quiet voice** (engage below it, no share purchase, no free-rider price). The survey has already drawn the boundary our four-action machinery needs, in the canonical source.

**7.3b (added by verifier) The disclosure *content* result the card missed, and the open question that is our window margin.**
- **Clifford (2008), p. 39.** Compared with 13G filings, **13D filings by hedge fund activists produce larger event-study returns and larger improvements in ROA.** The card's §6 says E16 (Edmans, Fang & Zur) is "the single place where the *content* of disclosure has economic consequences". It is not the only one: Clifford is a second, and it is cleaner for us, because it is a straight flagged-versus-pooled price comparison rather than a liquidity comparative static. Read Clifford (2008) directly before citing — like everything in §3, it is second-hand here.
- **p. 44, the front-running sentence.** Right after the multi-period open question the card already quotes, the survey adds that "combining liquidity shocks with **multiple periods and multiple informed traders** may lead to additional interesting insights, such as the possibility of **front running** (e.g., Brunnermeier & Pedersen 2005)." A disclosure window is exactly a rule about how long a blockholder accumulates before the market can trade against her, and shortening it from ten to five business days shortens precisely that. The survey named the theoretical object in 2014 without naming the policy lever. **That pairing — its open question plus our institutional anchor — is a stronger opening for draft_v3 than the 5%-discontinuity line alone, and the two should be used together.**
- **Holden, Jacobsen & Subrahmanyam (2014)** is the survey's own pointer for empirical liquidity measures suitable for testing exit theories (p. 44). Worth consulting before we fix on an Amihud specification.

**7.4 Blockholder disclosure rules: exactly how the survey frames them, and where the gap is.**
Three passages, and the framing is identical in all three — **the rule is a measurement problem, not an economic force**:
- p. 25 (challenge 3): the 5% definition exists "because this level triggers disclosure requirements in the United States", but theory predicts continuity, so the cut is arbitrary.
- p. 35 (the fullest treatment): the definition "arises because investors are required to file a Schedule 13 disclosure upon crossing a 5% threshold"; the required stake for effective control "differs across firms (rather than being a blanket 5%)"; and — the one behavioural observation — **"investors may cluster just below 5% to avoid disclosure, and thus be missed by Schedule 13 filings"**.
- p. 45 (open questions): repeat of the complaint, with 13F filings proposed as the workaround.
The **13D/13G distinction** (p. 39) is the only place the *content* of the rule does economic work: 13D requires stating in Item 4 the intended form of intervention; 13G is "shorter and comes with fewer disclosure requirements". Edmans, Fang & Zur (2013) then show liquidity pushes filers toward 13G, read as a choice of governance channel.
**Three gaps this leaves that our paper occupies:**
1. **Clustering below 5% is reported as a data-loss problem. It is an equilibrium object.** Investors optimising against a threshold is exactly a threshold-margin comparative static, and the survey has no model of it. Ours should.
2. **The 60-day pre-filing window is treated purely as a data source** (E20). That the *length* of that window is a policy choice, that it determines how much accumulation happens before the flag, and that it moved from 10 to 5 business days on 2024-02-05, is entirely absent — necessarily, given the date. **The window margin is unoccupied by the survey and by everything it surveys.**
3. **13D/13G is framed as revealed preference over channel, not as choice over disclosure.** Our partition language (flagged vs pooled) is a strictly richer reading of the same institutional fact.

**7.5 Concrete uses.**
- **Introduction of draft_v3:** open with the survey's own concession (**Q17** below — *corrected by verifier; the card said Q10, which is the Edmans-2009-three-channels quote*) that theory predicts no discontinuity at 5%, then say that a rule-generated discontinuity is precisely what we model. **(added by verifier)** Pair it with the p. 44 front-running sentence (§7.3b): one quote says nobody has modelled the threshold, the other says nobody has modelled multi-period accumulation against multiple informed traders. Our two margins answer one each.
- **Related literature:** use the survey as the single citation for the exit/voice taxonomy and for "the sign of the liquidity–governance relation is contested", rather than re-litigating Maug versus Back-Li-Ljungqvist ourselves. That is one paragraph instead of three.
- **Empirical section:** E20 (Collin-Dufresne & Fos 2014a) is the pointer to the pre-filing accumulation data our window-margin design needs — the filing itself discloses the 60-day trade history. That is a real, in-hand data asset for the Feb-2024 leg, and it is worth a card of its own if it is not already in the set (`research/txt_extracts/collin_dufresne_fos_2015_jf.txt` is present in the repo).
- **Referee checklist:** add the survey's four empirical challenges. The one that bites hardest on us is challenge 2 — governance operates through unobservable *threats*, so a null on realised filings does not imply a null on the rule's effect. Our bounded-null requirement should be stated in those terms.
- **What NOT to do:** do not cite any number in §3d as evidence. Every one of them is second-hand. E7 (7–8% 13D CAR) and E9 (returns come from forced takeovers) in particular are load-bearing for anyone linking activism to control outcomes, and both must be read in Brav et al. (2008) and Greenwood & Schor (2009) directly before use.

**7.6 One-line index entry.** *ARFE 2014 survey · object: firm value and firm policies via voice, exit and blockholder costs — not premium, not bidder entry · margin: none — the 5% rule appears three times, every time as a measurement caveat · identification: none (survey) · so-what: it is the canonical exit/voice frame, it documents that liquidity's sign on governance is unresolved, and on p. 45 it names our whitespace by complaining that "theory models do not predict a discontinuity at 5%".*

## 8. Quotes we may lean on (verbatim, page-cited)

Printed journal pages of *Annu. Rev. Financ. Econ.* 6:23–50 (2014).

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "Large shareholders can exert governance through two main mechanisms (see Hirschman 1970). The first is direct intervention within a firm, otherwise known as “voice.”" | p. 24 | The taxonomy, in the canonical source |
| Q2 | "If the manager destroys value, blockholders can sell their shares, pushing down the stock price and thus punishing the manager ex post. Ex ante, the threat of exit induces the manager to maximize value." | p. 24 | The exit mechanism in one sentence |
| Q3 | "The empirical literature typically defines a blockholder as a 5% shareholder, because this level triggers disclosure requirements in the United States. However, theoretical models predict that monitoring increases continuously with block size (up to a point), rather than a discontinuity at 5%." | p. 25 | The disclosure rule framed as a measurement artefact — the framing we invert |
| Q4 | "whereas exit theories predict how blockholders affect financial markets and how their effectiveness depends on microstructure factors." | p. 24 | Exit is where liquidity and microstructure enter governance — our lane |
| Q5 | "Voice theories reach different conclusions on whether liquidity hinders or helps intervention." | p. 27 | **The two-sidedness, stated flatly** |
| Q6 | "Coffee (1991) and Bhide (1993) verbally argued that liquidity deters voice, as it facilitates cutting and running." | p. 27 | The "liquidity hurts governance" side |
| Q7 | "Since a small a is chosen, liquidity encourages intervention overall." | p. 27 | Maug's resolution — the "liquidity helps" side |
| Q8 | "As a result, the “cutting and running” effect dominates and so liquidity deters intervention." | p. 28 | Back, Li & Ljungqvist reversing Maug on stake formation |
| Q9 | "In addition, liquidity also affects the block size a that is formed in the first place. Here, the results are more consistent, with theories generally finding that liquidity facilitates block formation." | p. 28 | The one part of the liquidity story theory agrees on |
| Q10 | "but, while voice theories have differing predictions, Edmans (2009) shows that liquidity (a parameter for the volume of liquidity trader demand) enhances exit through three channels." | p. 30 | Liquidity unambiguously helps exit — the contrast with voice |
| Q11 | "In the United States, a blockholder is typically defined as a 5% shareholder. However, rather than being motivated by theory, this definition arises because investors are required to file a Schedule 13 disclosure upon crossing a 5% threshold." | p. 35 | The rule as the origin of the field's central variable |
| Q12 | "In practice, investors may cluster just below 5% to avoid disclosure, and thus be missed by Schedule 13 filings." | p. 35 | Threshold-margin behaviour, reported as a data problem rather than modelled |
| Q13 | "When acquiring a 5% stake in a public firm, a shareholder must file a Schedule 13, which can take one of two forms. If she intends to engage in intervention, she must file a 13D and state in Item 4 the form of intervention she intends to employ; if she intends to remain passive, she can file a 13G, which is shorter and comes with fewer disclosure requirements." | p. 39 | The 13D/13G mechanics as the survey states them |
| Q14 | "Collin-Dufresne & Fos (2014a) show that the trades made by 13D filers over the 60 days before the filing date (which must be disclosed in the filing) are highly profitable." | p. 41 | The pre-filing window — as a data source, never as a margin |
| Q15 | "Moreover, liquidity increases the likelihood that the hedge fund blockholder files a 13G rather than a 13D." | p. 42 | Liquidity shifting the *disclosure* choice, the closest the survey comes to our object |
| Q16 | "Even a question as fundamental as the impact of blockholders on firm value remains unanswered." | p. 44 | Open question, stated bluntly |
| Q17 | "Although most empirical papers define a blockholder as a 5% shareholder, theory models do not predict a discontinuity at 5%. Particular attention could be paid to how the effectiveness of governance depends on block size." | p. 45 | **The open question our position answers** |
| Q18 | "Current exit theories consider a single trading round, but in reality there may be multiple periods across which the blockholder may trade on her information." | p. 44 | Open question on dynamics — relevant to accumulation inside the filing window |

## 9. Verification log

**Verifier:** adversarial second read, 2026-08-19. Checked against `lit/edmans-blockholder-survey-2024.pdf` directly (`pdftotext -f N -l N -layout`) and against `research/txt_extracts/edmans_2014_arfe.txt`.

**Counts: 33 OK · 2 WRONG · 0 MISCITED · 1 UNCHECKED.**

### Header / version / pagination
| Item | Verdict | Checked against |
|---|---|---|
| The file is the **2014** *Annu. Rev. Financ. Econ.* **6:23–50**, not a 2024 paper | **OK — confirmed** | PDF p. 1 masthead and the running "Annu. Rev. Fin. Econ. 2014.6:23-50" side-stamp on every page |
| **31 PDF pages**; article body = PDF 1–28; PDF 29–31 front matter/advertising | OK | `pdfinfo` Pages: 31 |
| Page rule **printed = PDF + 22** | **OK — spot-checked at both ends and in the middle** | PDF 1 → printed 23; PDF 23 → printed 45 (footer reads "45"); PDF 28 → printed 50 |
| Author affiliations (LBS, Wharton, NBER, …), JEL, doi | **UNCHECKED** in part | masthead confirms LBS/Wharton/NBER; the doi and JEL codes were not re-read and are not decision-critical |

### Quotes (§8) — every one re-matched at its cited printed page
Q1 p. 24 **OK** · Q2 p. 24 **OK** · **Q3 p. 25 OK — verbatim, both sentences** · Q4 p. 24 **OK** · Q5 p. 27 **OK** · Q6 p. 27 **OK** · **Q7 p. 27 OK, and the attribution is right** — the sentence sits at the end of the **Maug (1998)** paragraph, immediately before "Back, Li & Ljungqvist (2014) reach a different conclusion" · **Q8 p. 28 OK, and the attribution is right** — it follows "the stake *a* chosen in the IPO is typically large", which is the **Back, Li & Ljungqvist (2014)** paragraph. The card's small-*a* / large-*a* contrast is exactly as the survey states it · Q9 p. 28 **OK** · Q10 p. 30 **OK** · **Q11 p. 35 OK — verbatim** · **Q12 p. 35 OK — verbatim** · Q13 p. 39 **OK** · Q14 p. 41 **OK** (a near-identical restatement also appears on p. 42) · Q15 p. 42 **OK** · Q16 p. 44 **OK** · **Q17 p. 45 OK — verbatim, character for character: "Although most empirical papers define a blockholder as a 5% shareholder, theory models do not predict a discontinuity at 5%. Particular attention could be paid to how the effectiveness of governance depends on block size."** This is the quote the whole position rests on and it is exact · Q18 p. 44 **OK**.

**The "casual effects" typo on p. 44 is CONFIRMED** — the original reads "may be used to identify **casual** effects". Any quotation must carry [sic], as the card instructs.

### §3 attributions — 16 of the 51 spot-checked against the survey's own text (the brief asked for 10)
All 16 are the **survey's own** attributions, not the reader's inference, and all are ASSERTED at second hand as §3's preamble states.
V1 Shleifer & Vishny (1986), "firm value is monotonically increasing in block size" **OK** p. 26 · V2 Grossman & Hart (1980) **OK** p. 26 and n. 3 · V3 Winton (1993), Noe (2002), Edmans & Manso (2011) **OK** p. 26 · V4 Kahn & Winton (1998) "cut and run" **OK** p. 26 · V5 Coffee (1991), Bhide (1993), formalised by Aghion, Bolton & Tirole (2004) **OK** p. 27 · V6 Maug (1998) **OK** p. 27 · V7 Back, Li & Ljungqvist (2014) **OK** pp. 27–28 · X4 Edmans (2009) three channels **OK** p. 30 · X10 Levit (2013), including "increasing the frequency of the blockholder's liquidity shocks can … raise her effectiveness" **OK** p. 32 · C3 Bolton & von Thadden (1998) **OK** p. 33 · C5 Zwiebel (1995) "create their own space" **OK** p. 33 · E1 Holderness (2009) 96%, 15th of 22 **OK** p. 24 · E3 Edmans & Manso (2011) via Dlugosz et al. (2006), 70% **OK** p. 41 · E4 Barclay & Holderness (1991) 16% **OK** p. 36 · **E7 Brav et al. (2008) 7–8% over (−20, +20), +3.9% hostile, exits 8% lower OK p. 39** · E8 Klein & Zur (2009) 10.2% vs 5.1% over (−30, +30) **OK** p. 39 · E9 Greenwood & Schor (2009) **OK** p. 39 · E10 Carleton, Nelson & Weisbach (1998) 95% / >70% **OK** p. 40 · E11 Becht et al. (2009) Hermes 5.3% **OK** p. 40 · E12 McCahery, Sautner & Starks (2011) 80% **OK** p. 41 · E13 Fos (2013) **OK** p. 40 · **E14 vs E15 — both on printed p. 40, in consecutive sentences, reported without adjudication. Confirmed exactly as §5 and §7.3 describe.** Norli, Ostergaard & Schindele (2014) use decimalization and find liquidity *increases* proxy fights and proposals; Back, Li & Ljungqvist (2014) use brokerage closures, market-maker closures and retail–institutional brokerage mergers and "in contrast, find a negative effect" · E18 Roosenboom, Schlingemann & Vasconcelos (2014) **OK** p. 42 · E19 Dimmock et al. (2013) — introduced p. 42, result stated p. 43, so the card's p. 43 is right · E23 Crane, Michenaud & Weston (2014) Russell instrument **OK** p. 37.

### §2, §4, §5 structural claims
| Item | Verdict | Checked against |
|---|---|---|
| Notation table *V*, *V̄*, *G*, *P*, *a*, (1 − *a*) | OK | p. 25 |
| Scope = **outside** blockholders, "large shareholders who are not the firm's officers" | OK | p. 25 |
| Control literature handed off to Holderness (2003), "for an excellent survey" | OK | p. 25 |
| I1 = effect of *F* on *B*; I2 = effect of *B* on *F*; "None is watertight" | OK | p. 33 |
| The four empirical challenges (identification; unobservable threats; no blockholder definition; heterogeneity) | OK | p. 25, in that order |
| EU financial transaction tax, ten member countries, by January 2016 | OK | p. 27 |
| Investment Company Act 1940, 75% / 5% / 10% | OK | p. 38 n. 17 |
| "1992 proxy form that reduced the costs of communication among shareholders" | OK | p. 39 (the survey says proxy *form*, not *rule*) |
| All seven open questions in §6, verbatim | OK | pp. 44–45 |

### Scope claims (§6) — greps over the full extract
**"bidder" — 0 hits.** "Bidder entry is nowhere" **confirmed outright**. · **"business days", "filing window" — 0 hits.** The window margin never appears as a length. · "Schedule 13" appears at pp. 35 (×3), **37**, 39 — the card's "pp. 25, 35, 45" tally covers the *definitional caveats* but missed p. 37; corrected in §6, and the substance of the claim is unaffected. · "disclos*" appears at pp. 25, 35 (×2), 38, 39, 41, 46 — p. 38 is a list of engagement channels ("disclose that they voted against management"), p. 46 is the boilerplate DISCLOSURE STATEMENT; neither is a counterexample.

### WRONG items found and fixed
1. **The card's own §9(f) note claimed the word "premium" on p. 26 is a block-trade premium.** It is not. **Printed p. 26 says "takeover premium" literally**, inside the Shleifer–Vishny/Grossman–Hart passage: "Because small shareholders expect fewer restructuring gains, they sell for a lower price P. Knowing that she will not have to pay as high a takeover premium, the blockholder monitors more to begin with." Of the four "premium" hits in the article, **p. 26 is a takeover premium**; pp. 33 and 43 are the Barclay–Holderness block-trade premia the card correctly identified. Fixed: a new result **V2b** in §3a, a correction in §6, and a new **§7.3a** working out what it means for our premium wedge.
2. **§7.5 cited "Q10" for the no-discontinuity-at-5% quote.** Q10 is the Edmans-2009-three-channels quote on p. 30; the intended quote is **Q17** (p. 45). Fixed.

### Omissions found and added
1. **The takeover-premium comparative static on p. 26** — added as **V2b** and worked out in **§7.3a**. Material because it is the *only* premium mechanism in the canonical survey, it has the **opposite sign** to ours, and its premium is a cost to the blockholder rather than a transfer to minorities. A referee will ask which one we mean.
2. **Footnote 3 on p. 26** — the Grossman–Hart free-rider problem is "specific to the takeover channel" and "does not apply to the other channels (e.g., jawboning or voting) that do not require the purchase of additional shares." Added as **V2c**. Material because it is exactly the economic boundary between our **public voice** (buys shares, pays the free-rider price, gets flagged) and our **quiet voice** (buys nothing, pays nothing), drawn in the canonical source.
3. **Clifford (2008), p. 39** — 13D filings beat 13G filings on event-study returns *and* on ROA improvements. Added as **E7b** and to §7.3b. Material because it is a second place, besides E16, where the *content* of the disclosure has priced consequences, and it is a cleaner flagged-versus-pooled comparison than E16's liquidity comparative static.
4. **The front-running open question on p. 44** — "combining liquidity shocks with multiple periods and multiple informed traders may lead to additional interesting insights, such as the possibility of front running (e.g., Brunnermeier & Pedersen 2005)." Added as open question **(7)** in §6 and to §7.3b/§7.5. Material because it is the survey asking for the theoretical object the **window margin** creates, and pairing it with Q17 gives draft_v3 two open questions from the same page-range, one per margin, instead of one.
5. **Fos (2013) "studies all proxy fights, rather than only proxy fights by blockholders"** (p. 40) — added as a caveat at E13. Material because Fos is in our competitor set and the card presented the result without the survey's own scope limit.
6. **Holden, Jacobsen & Subrahmanyam (2014)** named at p. 44 as the reference on empirical liquidity measures for testing exit theories — added to §7.3b as a pointer before we fix an Amihud specification.

### Verdict
**The card is accurate and unusually well-judged on the framing.** All eighteen quotes are verbatim at their cited pages, the page-mapping rule holds at both ends, the "casual" typo is real, the Norli-versus-Back contradiction is on one page exactly as claimed, the sixteen spot-checked §3 attributions are all the survey's own, and the two hardest scope claims — **no "bidder" anywhere, no filing window as a length** — are confirmed by grep with zero hits. Two errors fixed, one of them substantive: the survey *does* carry a takeover-premium mechanism on p. 26, with the opposite sign to ours, and the card had ruled it out. Nothing decision-critical is left unchecked.
