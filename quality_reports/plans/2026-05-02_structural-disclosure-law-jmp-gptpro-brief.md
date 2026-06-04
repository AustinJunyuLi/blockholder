# GPT Pro Expansion Brief: Structural Law-and-Finance JMP on Ownership Disclosure

Date: 2026-05-02
Author: Austin Li, with Codex drafting support
Intended use: Upload or paste into GPT Pro and ask it to expand, critique, and convert this into a serious research agenda.

## Instructions to GPT Pro

You are advising a PhD student in financial economics who wants to develop a groundbreaking job market paper at the intersection of law, finance, corporate governance, shareholder activism, market microstructure, and structural estimation.

Your task is to expand this idea into a high-ambition JMP concept. Do not merely summarize it. Treat it as a serious research-design problem and stress-test it like a skeptical top finance faculty member, law-and-economics scholar, and structural econometrician.

Produce a detailed output with:

1. A sharpened one-paragraph thesis.
2. Three alternative paper architectures, ranked by ambition, feasibility, and expected placement value.
3. A literature map with direct competitors and gaps.
4. A law/regulation taxonomy that can be converted into data.
5. A structural model proposal with primitives, timing, choices, observables, unobservables, moments, identification, and counterfactuals.
6. A reduced-form evidence plan that complements the structural estimation.
7. Data requirements and practical construction steps.
8. The most likely referee objections and how to preempt them.
9. A 6-month and 12-month research roadmap.
10. A draft abstract and introduction skeleton.

Important constraints:

- Verify all legal/regulatory facts. Do not rely on memory for current rules.
- Distinguish ownership-disclosure thresholds from takeover-control thresholds, mandatory-bid thresholds, antitrust/HSR filing thresholds, and institutional portfolio-disclosure rules.
- Flag papers or sources that are paywalled or require institutional access.
- Be adversarial. If the project is too broad, say exactly how to narrow it.
- Do not anchor the proposal to any existing theory draft. This should read like a fresh, standalone project.
- Prioritize a project that is genuinely ambitious as a JMP, not merely incremental.
- The student can write models, code large data pipelines, and do structural estimation. Use that skill set as part of the design.

## Starting Intuition

Ownership-disclosure rules across jurisdictions look economically unsystematic. Legal regimes impose thresholds such as 3 percent, 5 percent, 10 percent, 15 percent, 30 percent, 50 percent, and 75 percent, with different deadlines, exemptions, aggregation rules, derivative-coverage rules, passive-investor categories, and enforcement mechanisms. These rules are often justified with legal language about transparency, market fairness, control, and investor protection. But it is not obvious that they are calibrated to the underlying economic primitives that matter for shareholder activism and corporate governance:

- How costly is activist intervention?
- How much value does activism create?
- How much hidden accumulation rent is needed to make activism privately incentive-compatible?
- How much do uninformed shareholders lose from trading against privately informed activists?
- How much does earlier disclosure change market prices, target resistance, bidder behavior, settlement bargaining, and real outcomes?
- Should the optimal disclosure threshold depend on liquidity, ownership dispersion, market capitalization, industry, activist reputation, or likely value creation?

The core hunch is that disclosure law is a form of market design, but existing legal thresholds are not designed as if they solve a formal economic mechanism-design problem.

The academically defensible version is not "lawyers designed random rules because they do not know finance." The defensible version is:

> Existing disclosure regimes encode legal intuitions about transparency and control, but they are not calibrated to the economic primitives they regulate: liquidity, information asymmetry, activist entry costs, target resistance, and expected value creation. A structural model can estimate these primitives and evaluate counterfactual disclosure rules.

## Candidate Big Thesis

Disclosure rules allocate the surplus from shareholder activism. Earlier or lower-threshold disclosure protects uninformed investors and helps the market learn who owns the firm, but it can also destroy the private accumulation rents that make costly activist intervention worthwhile. Later or higher-threshold disclosure gives activists more room to profit from private information and governance improvements, but it imposes adverse-selection costs on uninformed investors and may distort corporate-control outcomes.

The paper should ask:

> What ownership-disclosure rule maximizes shareholder value, or total welfare, when activism requires private rents to be incentive-compatible?

The answer is unlikely to be a uniform 3 percent or 5 percent rule. A potentially groundbreaking result would be:

> Uniform percentage thresholds are inefficient. Optimal disclosure should vary with firm liquidity, ownership dispersion, market capitalization, activist campaign costs, and expected value creation.

This would make the paper both a finance paper and a law-and-economics design paper.

## Project Identity

Working titles:

- "The Market Design of Blockholder Disclosure"
- "Designing Disclosure Rules for Shareholder Activism"
- "Who Should Know When? Ownership Disclosure, Activist Entry, and Market Design"
- "Optimal Ownership Disclosure in Shareholder Activism"
- "Disclosure Law as Market Design: Structural Evidence from Shareholder Activism"

One-sentence version:

> I estimate a structural model of activist entry, hidden accumulation, and disclosure to quantify the welfare effects of ownership-disclosure rules and compute optimal counterfactual thresholds and deadlines.

More aggressive version:

> This paper treats blockholder disclosure law as a market-design problem and shows that existing one-size-fits-all thresholds are not generally optimal once activist incentives, liquidity, and information asymmetry are jointly modeled.

## Why This Could Be a Groundbreaking JMP

The project can combine four strengths:

1. Law-and-finance institutional richness:
   Ownership-disclosure rules differ sharply across the United States, United Kingdom, European Union member states, and antitrust regimes such as HSR. The legal variation is economically meaningful and under-modeled.

2. Finance theory:
   Disclosure is not merely a transparency rule. It changes activist entry, accumulation, price discovery, target resistance, and corporate-control bargaining.

3. Structural estimation:
   Reduced form can show rules matter, but structural estimation can estimate counterfactual optimal rules and welfare. This is where the student can showcase both modeling and data-science skill.

4. Policy relevance:
   Regulators actively debate 13D deadlines, passive-investor classification, derivatives, group formation, HSR exemptions, and cross-market transparency. A paper that gives quantitative policy guidance can speak to finance academics, legal scholars, regulators, and practitioners.

## Legal and Regulatory Objects to Distinguish

The paper must be precise about different types of disclosure and control rules.

### 1. Beneficial ownership / activist disclosure

United States:

- Schedule 13D/13G applies to beneficial ownership of more than 5 percent of a covered equity class.
- Schedule 13D is the active/control-intent disclosure.
- Schedule 13G is a shorter-form disclosure for certain passive or exempt holders.
- SEC modernization amendments changed Schedule 13D timing from the older 10-day window to five business days after the triggering acquisition. Verify details against current SEC sources.

Important source seeds:

- SEC beneficial ownership reporting C&DIs: https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/exchange-act-sections-13d-13g-regulation-13d-g-beneficial-ownership-reporting
- SEC final rule, Modernization of Beneficial Ownership Reporting: https://www.sec.gov/file/33-11253

### 2. Institutional portfolio disclosure

United States:

- Form 13F is a quarterly institutional holdings report for institutional investment managers that meet the $100 million threshold in Section 13(f) securities.
- 13F is delayed, broad institutional portfolio disclosure, not the same as 13D activist/control disclosure.

Important source seed:

- SEC Form 13F FAQ: https://www.sec.gov/rules-regulations/staff-guidance/frequently-asked-questions-about-form-13f

### 3. UK major shareholding disclosure

United Kingdom:

- FCA DTR 5 governs major shareholding notifications.
- For UK issuers, DTR 5.1.2R includes thresholds at 3 percent, 4 percent, 5 percent, 6 percent, 7 percent, 8 percent, 9 percent, 10 percent, and each 1 percent threshold thereafter up to 100 percent.
- For non-UK issuers, the threshold schedule differs and includes 5 percent, 10 percent, 15 percent, 20 percent, 25 percent, 30 percent, 50 percent, and 75 percent.
- The UK TR-1 notification process is a major institutional source for data construction.

Important source seeds:

- FCA DTR 5 shareholding notification page: https://www.fca.org.uk/cy/node/8461
- FCA Primary Market Bulletin 33 with DTR 5.1.2R threshold summary: https://www.fca.org.uk/publications/newsletters/primary-market-bulletin-33

### 4. EU major holdings

European Union:

- The Transparency Directive baseline thresholds include 5 percent, 10 percent, 15 percent, 20 percent, 25 percent, 30 percent, 50 percent, and 75 percent.
- Member states can vary in national implementation, additional thresholds, filing mechanics, deadlines, exemptions, and treatment of financial instruments.
- ESMA provides a practical guide summarizing rules across EEA jurisdictions. This can become a key source for a cross-country law-as-data panel.

Important source seeds:

- ESMA major shareholdings page: https://www.esma.europa.eu/issuer-disclosure/major-shareholdings
- ESMA Transparency Directive Article 9: https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/transparency-directive/article-9-notification
- ESMA practical guide, major holdings notifications: https://www.esma.europa.eu/sites/default/files/library/practical_guide_major_holdings_notifications_under_transparency_directive.pdf

### 5. HSR / antitrust premerger notification

United States:

- Hart-Scott-Rodino premerger notification is not a shareholder activism disclosure rule in the same sense as Schedule 13D.
- But HSR can force disclosure or regulatory filing around large toehold acquisitions, creating a separate threshold that may bind activist stake-building before a 13D filing.
- This can create useful identification because HSR thresholds are dollar-value thresholds rather than percentage thresholds and are adjusted over time.
- For 2026, the FTC announced that the minimum size-of-transaction threshold is $133.9 million, effective February 17, 2026. This changes annually, so it must be treated as time-varying.

Important source seeds:

- FTC current HSR thresholds: https://www.ftc.gov/enforcement/premerger-notification-program/current-thresholds
- FTC 2026 threshold update: https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-announces-2026-update-jurisdictional-fee-thresholds-premerger-notification-filings

### 6. Mandatory bid / takeover-control thresholds

These are distinct from ownership disclosure. For example, thresholds around 30 percent, 33 percent, 40 percent, or similar levels may relate to mandatory offer, control, takeover-code, or change-in-control rules in some jurisdictions. Do not conflate these with first ownership-disclosure thresholds.

The paper can still use them as separate legal instruments, but they belong in a different column of the law taxonomy:

- ownership-disclosure threshold,
- intent-disclosure threshold,
- portfolio-disclosure threshold,
- antitrust/toehold notification threshold,
- control or mandatory-bid threshold.

## Research Contributions to Aim For

### Contribution 1: Law as data

Construct a global or multi-jurisdictional dataset of ownership-disclosure law.

Possible variables:

- first ownership threshold,
- subsequent thresholds,
- filing deadline,
- whether deadline is business days or calendar days,
- whether active intent must be disclosed,
- passive-investor categories,
- switch rules from passive to active status,
- derivative coverage,
- cash-settled derivative treatment,
- voting-rights vs economic-exposure definition,
- group aggregation rules,
- wolf-pack or concert-party treatment,
- exemptions for market makers, custodians, index funds, banks, or passive managers,
- public dissemination mechanism,
- machine readability,
- enforcement intensity,
- sanctions,
- whether issuer also has to disseminate notice,
- whether filings are centralized in a searchable public database.

This law dataset is itself a contribution if done carefully. It turns legal heterogeneity into measurable treatment variables.

### Contribution 2: Reduced-form evidence

Show that disclosure law affects economically important outcomes:

- activist target selection,
- stake size at first disclosure,
- pre-disclosure price run-up,
- announcement returns,
- 13D vs 13G filing choice,
- 13G to 13D switches,
- campaign escalation,
- settlements,
- proxy contests,
- sale demands,
- takeover probability,
- takeover premia,
- liquidity and adverse-selection measures around filing,
- long-run operating outcomes.

Reduced form should not be the whole paper, but it should discipline the structural model and persuade skeptical readers that the legal variation is real.

### Contribution 3: Structural estimation

Estimate the primitives behind activist entry and disclosure:

- distribution of activist private information,
- distribution of activist treatment/value-creation ability,
- cost of campaign launch,
- cost of escalation,
- cost of rapid accumulation,
- price-impact or liquidity cost,
- target resistance probability,
- probability of settlement,
- probability of sale/takeover,
- market inference before and after disclosure,
- fraction of value captured by activist vs incumbent shareholders.

Use the model to recover unobserved quantities and run counterfactual disclosure policies.

### Contribution 4: Optimal disclosure design

Use the estimated model to ask:

- What threshold maximizes target shareholder value?
- What threshold maximizes total welfare?
- Should thresholds be uniform across firms?
- Should deadlines be shorter for liquid firms?
- Should small illiquid firms have higher thresholds because activists need larger private rents?
- Should derivatives count toward beneficial ownership?
- Should passive investors face stricter intent-switch rules?
- Should 13F-style portfolio disclosure be more frequent or more targeted?
- Should HSR investment-only exemptions be changed for activists?

The headline result should be a policy-design statement, not just an estimate.

## Core Economic Mechanism

Disclosure has two opposing effects.

### Transparency effect

Earlier or lower-threshold disclosure:

- reduces adverse-selection losses borne by uninformed investors,
- improves price discovery,
- alerts the target board and other shareholders earlier,
- can reduce stealth accumulation and informed trading rents,
- may reduce inefficient overinvestment in private information acquisition.

### Incentive effect

Earlier or lower-threshold disclosure also:

- reduces the activist's ability to build a large position before the price adjusts,
- lowers private returns from costly activism,
- may deter positive-NPV campaigns,
- may cause activists to choose passive filings or avoid targets,
- may shift activism toward only the highest-value or lowest-cost campaigns,
- may induce alternative hidden channels such as derivatives, wolf packs, or coordination.

The structural model should quantify this tradeoff.

## Possible Model Architecture

### Baseline timing

1. Target firm has observable state `X_i`: size, liquidity, valuation, ownership dispersion, institutional ownership, industry, governance, prior performance.
2. Potential activist draws private opportunity `theta_i`, combining stock-picking value and governance-treatment value.
3. Activist chooses whether to enter.
4. Conditional on entry, activist chooses accumulation intensity and intended ownership stake.
5. Disclosure rule `R_jt` determines when ownership or intent becomes public.
6. Market updates prices upon pre-filing trading signals and formal disclosure.
7. Target responds: ignore, negotiate, settle, resist, proxy fight, sale process.
8. Real outcome realizes: operating change, payout, board seat, proxy contest, takeover, or exit.

### Key choices

Activist choice set could include:

- no campaign,
- passive stake / 13G-style filing,
- active stake / 13D-style filing,
- hidden below-threshold accumulation,
- quiet engagement,
- public campaign,
- escalation to proxy fight,
- sale-demand / takeover-oriented campaign.

Start simple. A feasible first structural model might use:

- no entry,
- passive filing,
- active filing.

Then add escalation or takeover as outcome moments rather than choices in the first version.

### Activist payoff

A generic activist payoff could be:

```text
Activist payoff =
    stake * expected value creation
  + pre-disclosure trading rent
  - accumulation cost
  - campaign cost
  - disclosure/regulatory/compliance cost
  - expected resistance cost.
```

More formally:

```text
U_A(a, s, R) =
    alpha(a, R, L_i) * DeltaV(theta_i)
  + TradingRent(alpha, R, L_i, sigma_i)
  - C_entry
  - C_campaign(a, X_i)
  - C_accumulation(alpha, L_i)
  - C_disclosure(R, a)
  + epsilon_a.
```

Where:

- `alpha` is the activist's stake,
- `R` is the disclosure rule,
- `L_i` is liquidity,
- `sigma_i` captures information asymmetry or volatility,
- `DeltaV` is value creation,
- `TradingRent` is rent from buying before market fully learns,
- `C_campaign` is intervention cost,
- `epsilon_a` is a choice shock.

### Market reaction

Market price response should distinguish:

- stock-picking component,
- governance-treatment component,
- selection component,
- disclosure-timing component.

This mirrors and extends Albuquerque, Fos, and Schroth's structural decomposition, but the new policy object is the disclosure rule itself.

### Target and bidder response

Do not make takeover the whole model initially. Use takeover as one high-value outcome channel:

- probability of subsequent takeover,
- time to bid,
- takeover premium,
- sale-demand campaigns,
- target resistance,
- settlement vs escalation.

This keeps the model feasible but still allows the paper to speak to corporate control.

## Estimation Strategy

### Observables

Possible observable data moments:

- whether a campaign occurs,
- 13D vs 13G filing type,
- ownership stake at initial filing,
- time between trading window and disclosure if reconstructable,
- announcement CAR around 13D/13G/TR-1 filings,
- pre-filing abnormal returns and abnormal volume,
- liquidity before and after disclosure,
- switch from 13G to 13D,
- amendments and stake changes,
- campaign objective,
- campaign success,
- settlement,
- proxy contest,
- board representation,
- takeover bid,
- takeover premium,
- long-run operating changes.

### Moments for structural estimation

Candidate moments:

- share of eligible firms targeted by activists,
- target characteristics conditional on campaign,
- distribution of reported stakes at disclosure,
- distribution of announcement returns by filing type,
- pre-filing run-up by liquidity and threshold distance,
- 13D vs 13G filing shares,
- frequency of 13G-to-13D switches,
- post-filing escalation rates,
- bid hazard after filing,
- takeover premium conditional on bid,
- heterogeneity by liquidity, size, institutional ownership, and legal regime.

### Identification intuition

- Filing choice identifies relative payoffs from passive vs active investing.
- Announcement returns identify market beliefs about value creation and stock-picking.
- Stake size at filing identifies accumulation incentives and disclosure-threshold constraints.
- Pre-filing run-up identifies hidden accumulation and market leakage.
- Liquidity interactions identify accumulation costs and price impact.
- Cross-jurisdiction law variation identifies how thresholds and deadlines affect choices.
- HSR thresholds identify exogenous dollar-value constraints on large toehold accumulation.
- Rule changes identify timing effects if event windows are credible.

## Reduced-Form Identification Angles

### 1. US 13D deadline modernization

The SEC moved Schedule 13D filing timing from the older 10-day regime to five business days. This can provide a regulatory shock, but the post-change sample is short as of 2026, so it may be more useful as suggestive evidence unless enough time passes.

Questions:

- Did initial reported stakes fall after the deadline shortened?
- Did announcement CARs change?
- Did pre-filing run-ups shrink?
- Did campaign incidence fall for illiquid firms?
- Did activists shift toward 13G, derivatives, or smaller positions?

### 2. HSR threshold discontinuities

HSR thresholds can bind when a toehold's dollar value crosses reportability thresholds. Bishop, Fos, Jiang, and Partnoy use this angle in "Antitrust, Anti-Activism." This is likely a direct competitor but also an identification template.

Questions:

- Are activists less likely to target firms where a meaningful toehold triggers HSR before 13D?
- Does the effect vary by liquidity and expected campaign value?
- Can HSR threshold variation identify the value of hidden accumulation?

### 3. Cross-country threshold heterogeneity

Use differences across US, UK, EU member states, and possibly other markets.

Challenges:

- Country differences are not randomly assigned.
- Legal thresholds correlate with market structure, enforcement, investor base, and takeover law.
- Need fixed effects, matched samples, or within-country reforms.

Potential approach:

- Build law variables.
- Compare marginal response to threshold distance within country-year-industry cells.
- Use country law as one source of variation in structural estimation rather than pretending it is clean reduced-form randomization.

### 4. Threshold bunching

Activists may bunch just below or just above thresholds.

Questions:

- Do positions cluster below 5 percent in the US?
- Do UK positions cluster around 3 percent or subsequent 1 percent thresholds?
- Does bunching vary with liquidity, activist reputation, campaign type, or expected gains?

### 5. 13G to 13D switches

Switches reveal changes from passive to active intent or loss of passive eligibility.

Questions:

- What predicts switching?
- Does the market response to switching identify the value of revealed activism?
- Are switches more frequent when thresholds are high or disclosure is delayed?

## Data Construction Plan

### Core data

- SEC EDGAR Schedule 13D, 13D/A, 13G, 13G/A.
- Form 13F holdings.
- CRSP prices, returns, volume, bid-ask spreads.
- Compustat accounting variables.
- M&A data from SDC, Refinitiv, LSEG, or similar.
- Activist campaign data from SharkRepellent, FactSet SharkWatch, Activist Insight, or 13D Monitor.
- Board/proxy/settlement data from FactSet, ISS, proxy filings, or hand-collected sources.
- UK TR-1 major shareholding notifications via FCA/LSE/RNS/NSM.
- EU national competent authority filings where feasible.
- ESMA practical guide for legal rule taxonomy.
- HSR thresholds from FTC annual updates.

### Law-as-data table

Create a panel:

```text
country | year | issuer_scope | first_threshold | subsequent_thresholds
deadline_days | business_or_calendar | active_intent_required
passive_short_form | derivatives_covered | cash_settled_derivatives_covered
group_aggregation | wolf_pack_rule | market_maker_exemption
index_fund_exemption | filing_destination | public_database
machine_readable | enforcement_proxy | sanctions | source_url
```

### Firm-event panel

```text
firm | date | country | legal_regime | activist | filing_type
reported_stake | filing_delay_proxy | prefiling_return | filing_CAR
volume_runup | liquidity | ownership_dispersion | market_cap
campaign_objective | settlement | proxy_fight | takeover_bid
takeover_premium | outcome_success | source
```

## Direct Competitors and Must-Read Literature

GPT Pro should expand this list, verify citations, and flag paywalled items.

### Structural activism and value creation

- Albuquerque, Rui, Vyacheslav Fos, and Enrique Schroth, "Value Creation in Shareholder Activism: A Structural Approach." This is essential because it structurally estimates 13D vs 13G filing choice and decomposes activist announcement returns. Source seed: https://www.sciencedirect.com/science/article/pii/S0304405X21003950 and CEPR page https://cepr.org/publications/dp14995
- Gantchev, Nickolay, "The Costs of Shareholder Activism: Evidence from a Sequential Decision Model." Essential for sequential campaign costs.
- Reputation and investor activism: structural approach. Relevant if activist reputation becomes a dynamic state variable.

### Disclosure threshold theory

- Ordonez-Calafi and Bernhardt, "Blockholder Disclosure Thresholds and Hedge Fund Activism." Essential direct competitor on threshold design. Source seed: https://research-information.bris.ac.uk/files/345988398/blockholder_disclosure_thresholds_and_hedge_fund_activism.pdf
- Bebchuk and Jackson on blockholder disclosure. Important legal-theory and law-and-economics background.

### International activism

- Becht, Franks, Grant, and Wagner, "Returns to Hedge Fund Activism: An International Study." Essential for cross-country activism and regulatory threshold variation. Source seed: https://academic.oup.com/rfs/article/30/9/2933/3852480

### HSR and law-finance identification

- Bishop, Fos, Jiang, and Partnoy, "Antitrust, Anti-Activism." Very important and recent. Uses HSR notification thresholds as identification for activist deterrence. Source seed: https://papers.ssrn.com/sol3/Delivery.cfm/6061814.pdf?abstractid=6061814&mirid=1

### Classic activism, liquidity, and governance

- Brav, Jiang, Partnoy, and Thomas, hedge fund activism.
- Edmans, Fang, and Zur, liquidity and governance.
- Maug, liquidity and control.
- Kahn and Winton, ownership and intervention.
- Back, Collin-Dufresne, Fos, Li, and Ljungqvist, activism, strategic trading, and liquidity.

### Activism and takeovers

- Greenwood and Schor, investor activism and takeovers.
- Burkart and Lee, activism and takeovers.
- Corum and Levit, corporate control activism.
- Bulow, Huang, and Klemperer, toeholds and takeovers.

## What Makes This Different From Existing Work

The new paper should not merely replicate structural 13D/13G valuation or theoretical threshold design.

Possible novelty claims:

1. First structural estimation of ownership-disclosure law as a policy design problem.
2. First global or multi-jurisdictional law-as-data map of activist/blockholder disclosure rules tied to campaign outcomes.
3. Quantifies the tradeoff between transparency and activist incentive provision.
4. Shows optimal thresholds are state-contingent, not uniform.
5. Integrates securities disclosure, antitrust thresholds, passive ownership disclosure, and activist campaign outcomes in one empirical framework.
6. Uses structural estimation to evaluate counterfactual legal regimes, such as US 3 percent threshold, EU harmonization, shorter 13D deadlines, and HSR investment-only exemptions.

## Candidate Paper Architectures

Ask GPT Pro to develop and rank these.

### Architecture A: Optimal ownership disclosure, structural core

Main question:

> What ownership-disclosure threshold and deadline maximize shareholder value when activists need hidden accumulation rents?

Core:

- Build model of activist entry, accumulation, filing choice.
- Estimate on US 13D/13G plus event returns.
- Use cross-country and HSR variation to discipline counterfactuals.
- Main output is optimal threshold/deadline by firm type.

Pros:

- Cleanest structural JMP.
- Strong use of modeling and data skills.
- Direct law-and-finance policy contribution.

Cons:

- Requires careful identification.
- Legal data construction is heavy.

### Architecture B: Disclosure law and activist deterrence, reduced form plus structure

Main question:

> Do stricter disclosure rules deter activism, and is that deterrence good or bad?

Core:

- Reduced-form law shocks and threshold discontinuities first.
- Structural model second to translate deterrence into welfare.

Pros:

- Easier to sell empirically.
- Stronger causal evidence.

Cons:

- May look less like a structural JMP if not integrated carefully.

### Architecture C: Disclosure, activism, and corporate control

Main question:

> How do disclosure thresholds affect the probability and terms of takeovers following activist entry?

Core:

- Activist entry and filing choice with takeover as central outcome.
- Estimate effect on bid hazard and takeover premium.

Pros:

- Very finance-rich.
- Connects activism to M&A and control.

Cons:

- Harder model.
- More moving parts.
- Risk of becoming narrower than the bigger law-design idea.

Recommended starting point:

- Use Architecture A as the main JMP.
- Include B for identification.
- Keep C as an important outcome extension rather than the whole paper.

## Potential Headline Results

The paper should aim for results of this form:

1. Activists require economically meaningful hidden accumulation rents to enter campaigns, especially in illiquid firms.
2. Lower thresholds reduce adverse-selection losses but deter marginal campaigns.
3. The welfare-maximizing threshold is not uniform.
4. A 3 percent threshold is beneficial for liquid firms with low accumulation costs, but harmful for illiquid firms where activist entry is fragile.
5. Shorter deadlines reduce pre-filing run-ups, but they also reduce campaign incidence among high-cost targets.
6. Passive disclosure and active disclosure interact: 13F and 13G do not substitute cleanly for 13D because they reveal different economic objects.
7. HSR-like thresholds can unintentionally deter activism in firms where a meaningful toehold is dollar-large relative to reportability thresholds.
8. Existing regimes protect transparency but fail to condition on the economic primitives that determine activist incentive compatibility.

## Referee Concerns to Preempt

### Concern 1: Legal rules are endogenous to country institutions

Response:

- Do not rely only on cross-country variation.
- Use within-country changes, HSR thresholds, bunching, and structural moments.
- Treat country law as part of the policy environment, not a clean randomized treatment.

### Concern 2: Structural model is too ambitious

Response:

- Start with a parsimonious model: no entry, passive filing, active filing.
- Add escalation/takeover as outcome moments or extensions.
- Make counterfactuals directly tied to estimated parameters.

### Concern 3: 13D/13G selection is already studied

Response:

- Acknowledge Albuquerque, Fos, and Schroth.
- Differentiate clearly: their object is value creation and filing choice; this paper's object is optimal disclosure-law design across thresholds, deadlines, and jurisdictions.

### Concern 4: Cross-country activism data is messy

Response:

- Use cross-country data initially to construct law taxonomy and external validity.
- Keep the primary structural estimation in the cleanest data environment, likely US EDGAR plus CRSP/Compustat.
- Add UK/EU as validation/counterfactual discipline if full harmonized panel is too costly.

### Concern 5: Policy counterfactuals require welfare assumptions

Response:

- Report multiple welfare objects:
  - activist private surplus,
  - target shareholder value,
  - uninformed shareholder trading losses,
  - total target-firm value,
  - bidder surplus where observable,
  - total surplus under explicit assumptions.
- Make distributional implications transparent.

### Concern 6: Legal scholars will reject "random law" framing

Response:

- Do not claim lawmakers are random.
- Claim legal rules are historically and administratively motivated, but their quantitative calibration to finance primitives is underdeveloped.
- Frame the paper as complementing legal reasoning with estimated economic design.

## What GPT Pro Should Produce Next

Please produce an expanded research-development memo with the following exact structure:

```markdown
# Proposed JMP: [Best Title]

## 1. Core Thesis

## 2. Why This Is a Big Paper

## 3. Precise Research Questions

## 4. Legal-Regime Taxonomy

## 5. Literature Map and Direct Competitors

## 6. Preferred Paper Architecture

## 7. Alternative Architectures

## 8. Structural Model
### 8.1 Timing
### 8.2 Agents
### 8.3 State Variables
### 8.4 Choices
### 8.5 Payoffs
### 8.6 Equilibrium Concept
### 8.7 Estimation Strategy
### 8.8 Identification
### 8.9 Counterfactuals

## 9. Reduced-Form Evidence

## 10. Data Plan

## 11. Expected Results and Falsification Tests

## 12. Referee Risks and Responses

## 13. Six-Month Roadmap

## 14. Twelve-Month Roadmap

## 15. Draft Abstract

## 16. Draft Introduction Skeleton

## 17. Reading List
Flag each source as open access, likely paywalled, or needs verification.
```

## Calibration of Tone for GPT Pro

Be serious and demanding. The goal is not to produce a cute idea. The goal is to decide whether this can become a top-field or general-interest finance JMP.

The output should feel like something a strong advisor at LSE, UCL, LBS, Wharton, Columbia, NYU, or Chicago would take seriously.

Do not hide weaknesses. The student wants the most ambitious viable version, not the easiest version.

## Non-Negotiable Distinctions

GPT Pro must explicitly distinguish:

- 13D active/control-intent disclosure vs 13G passive disclosure.
- 13D/13G ownership disclosure vs 13F institutional portfolio disclosure.
- Ownership-disclosure thresholds vs mandatory-bid/control thresholds.
- Securities disclosure vs antitrust/HSR notification.
- Percentage thresholds vs dollar-value thresholds.
- Disclosure timing vs disclosure scope.
- Target shareholder value vs activist private profit vs total welfare.

## Minimal Viable First Paper

If the full global project is too broad, propose a minimal viable JMP:

1. US-only structural model of 13D/13G filing choice and hidden accumulation.
2. Reduced-form evidence from the 2024 13D deadline change and HSR threshold variation.
3. Counterfactual disclosure thresholds and deadlines.
4. UK/EU legal-rule map as external validity and future extension.

This MVP still has a big claim:

> Disclosure law should be designed as a function of economic primitives, not fixed as a uniform percentage threshold.

## Possible Final Abstract Direction

This paper studies ownership-disclosure law as a market-design problem. Disclosure rules require investors to reveal large positions once ownership crosses regulatory thresholds, but these thresholds vary widely across jurisdictions and are rarely calibrated to the economic primitives that determine activist entry. I estimate a structural model in which an activist privately observes a value-creation opportunity, chooses whether and how much to accumulate before disclosure, and decides whether to pursue passive or active engagement. Earlier disclosure protects uninformed investors and improves transparency, but it also reduces the private rents that make costly activism incentive-compatible. Using activist filings, ownership stakes, event returns, liquidity, campaign outcomes, and variation in disclosure regimes, I estimate the tradeoff between transparency and activist incentives. Counterfactuals show that uniform thresholds are generally inefficient: optimal disclosure is lower for liquid firms where accumulation rents are less necessary and higher for illiquid firms where early disclosure deters value-creating campaigns. The results quantify how securities law allocates the surplus from shareholder activism and provide a framework for designing disclosure rules.

