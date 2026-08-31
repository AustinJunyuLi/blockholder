# Legal regime portability

**Status:** Non-authoritative research note. The United States and United Kingdom rows were checked against official sources as of 2026-08-29. The Germany, France, Netherlands, and Italy rows were not checked, and the Italy Form 120 claim is unsourced. This note was prepared against the 2026-08-28 `MODEL_CARD.md` stamp at `59c0dfc`; the frozen card is now dated 2026-08-30 at `65b8db3`. It does not amend `MODEL_CARD.md`, `LABEL_LEDGER.md`, or `CONTEXT.md`, and it changes no honesty label.

## Bottom line

The abstract idea that law induces a partition is broadly portable. The current binary purpose-revealing theorem stack is not universal and does not directly model UK or EU ladders.

Every legal disclosure technology maps underlying holdings, instruments, attribution rules, crossing events, delays, and report content into a public history. That mapping partitions the histories the market can distinguish. This is a useful common framework for the United States, the United Kingdom, and European regimes.

The current v4 implementation is narrower. It is best read as a stylized model of a purpose-revealing first Schedule 13D filing. It is not a general model of major-holdings law. It is not even a literal model of all US beneficial-ownership reporting because Schedule 13G can apply, a Schedule 13D may be filed before the deadline, and later Schedule 13D amendments create repeated notifications.

## Current model baseline

This assessment uses the `MODEL_CARD.md` stamp dated 2026-08-28, commit `59c0dfc` (`MODEL_CARD.md`, lines 1-29).

The card defines one stake threshold, one filing window, and two top-level cells. A history is flagged only when an engaging plan crosses the threshold and the filing lands by the control horizon. Otherwise it remains pooled (`MODEL_CARD.md`, lines 31-60). The symbol table makes the same reduction precise: one threshold `tau`, one window `T`, one crossing date, one filing date, one indicator `D`, and a filing message consisting of exact stake plus `a = 1` (`MODEL_CARD.md`, lines 88-125).

Four assumptions are decisive for legal portability:

1. The filing lands exactly at the crossing date plus `T`, rather than at any time up to an outer deadline.
2. `D = 1` implies engagement, and the filing truthfully reveals both stake and purpose.
3. Only Voice plans cross in the core.
4. The flag terminates pooled trading, after which there is one flagged round and then the bidder decision.

The timing and first three restrictions appear in A4 (`MODEL_CARD.md`, lines 230-231) and in the timing and table sections cited above. A7 then requires the flagged tuple to identify the informed component, with the separate A7′ on-path and A7-J joint injectivity forms (`MODEL_CARD.md`, lines 335-362). A(tau) imposes a separate three-atom posterior representation and related restrictions. The card records that this representation is conditional and fails at the implemented calibration, without moving any result label (`MODEL_CARD.md`, lines 365-475).

The current result statements and their honesty labels remain exactly as recorded in the result ledger (`MODEL_CARD.md`, lines 526-559). The card also already declines to claim endogenous filing before a deadline, partially revealing flagged trading, and several broader results (`MODEL_CARD.md`, lines 593-657). Nothing in this note changes those boundaries.

## Terms that must remain distinct

These terms are proposed for this research note and any later extension. No glossary edit is made here.

- **Notification ladder:** Repeated ownership or voting-right reporting rungs. A ladder can require reports on upward and downward crossings and can use different rungs for different issuers or holder categories.
- **Purpose-revealing trigger:** A filing obligation whose content discloses strategic intent or plans. Schedule 13D Item 4 is the leading example, although its actual narrative content is richer and less categorical than the model's `a = 1` message.
- **Control trigger:** A rule that requires or constrains a control transaction, such as the UK mandatory-offer rule at 30 percent. It is not an ownership-notification rule and not a purpose-revealing trigger.

The terms should not be substituted for one another. A notification ladder can operate without revealing purpose. A purpose-revealing trigger need not be a control trigger. A control trigger can apply after several notification rungs have already been crossed.

## Jurisdiction comparison

The table is a portability map, not a compliance guide. The European national rows are deliberately short. Issuer scope, home state, exemptions, aggregation, instruments, acting-in-concert rules, and current national procedure must be checked separately.

| Jurisdiction and rule | Ladder or trigger | Public clock | Purpose content | Fit to the current binary model |
|---|---|---|---|---|
| United States, Regulation 13D-G | Rule 13d-1 requires an initial Schedule 13D after beneficial ownership exceeds 5 percent, unless a Schedule 13G route or another exception applies. Rule 13d-2 requires amendments for material changes, with a 1 percentage-point acquisition or disposition deemed material and smaller changes potentially material. | Initial Schedule 13D is due no later than five business days after the triggering acquisition. A material Schedule 13D amendment is due no later than two business days. These are maximum deadlines, not exact filing dates. | Schedule 13D Items 3, 4, 5, and 6 cover source of funds, purpose and plans, stake and transactions, and arrangements including relevant derivatives. Schedule 13G does not provide the same purpose-and-plans message. | Closest regime, but still only a stylization. The threshold alone does not imply a purpose-revealing 13D, reports can arrive early, and amendments make the history multi-report. |
| United Kingdom, FCA DTR 5 | For a UK issuer, DTR 5.1.2R uses 3 percent and every 1 percent thereafter through 100 percent. For a non-UK issuer, it uses 5, 10, 15, 20, 25, 30, 50, and 75 percent. Reaching, exceeding, and falling below a rung can trigger a report. Financial-instrument holdings are covered and aggregated under DTR 5. | Holder to issuer is as soon as possible and no later than two trading days for a UK issuer or four trading days for a non-UK issuer. Under DTR 5.8.12R, the issuer publishes as soon as possible and no later than the next trading day for a regulated-market issuer, or the third trading day for specified others. | The TR-1 framework reports voting rights, holder identity, controlled chains, crossing date, and instruments. It does not generally disclose an engagement purpose. | Does not fit. It is a repeated, two-stage, up-and-down notification ladder with reports by passive as well as engaging holders. DTR 5, not Takeover Code Rule 9, is the relevant pre-bid analogue. |
| United Kingdom, Takeover Code Rules 8 and 9 | Rule 8.3 requires 1 percent opening-position and dealing disclosures only after an offer period has begun. Rule 9 uses 30 percent as a mandatory-offer control trigger, with further rules for increases between 30 and 50 percent. | Rule 8 has an offer-period disclosure timetable. Rule 9 triggers an offer obligation rather than a pre-bid public-notification clock. | Neither rule turns the ordinary pre-bid DTR 5 report into a general purpose statement. | Keep outside the DTR 5 analogue. Rule 8 is state-contingent on an offer period. Rule 9 is a control trigger. The separate persons-with-significant-control regime above 25 percent is also not the pre-bid analogue. |
| European Union, Transparency Directive minimum structure | Article 9 uses 5, 10, 15, 20, 25, 30, 50, and 75 percent of voting rights, for reaches, exceeds, and falls below. Articles 13 and 13a cover and aggregate relevant instruments. Article 3 permits home states, within its terms, to add lower or additional rungs and stricter timing or content. | Article 12 gives the holder no later than four trading days for notice to the issuer. The issuer then has no later than three trading days after receipt to make the information public. Both are outer limits in a two-stage process. | Article 12 covers the voting-right situation, controlled chain, crossing date, and identities, not engagement purpose. Directive 2013/50/EU recital 12 confirms that national law may impose stricter content, including shareholders' intentions. | Does not fit. The EU structure is a ladder, its ordinary report is not purpose-revealing, and the public clock is neither one-stage nor exact. |
| Germany | The standard WpHG ladder is 3, 5, 10, 15, 20, 25, 30, 50, and 75 percent, with upward and downward crossings. | WpHG section 33 requires notice to the issuer and BaFin without delay and no later than four trading days. Public dissemination is a separate step under the national implementation. | The standard voting-right notification under WpHG section 33 is not an activist-purpose statement. | Does not fit the binary purpose cell. It is evidence that the EU minimum ladder is nationally expanded. |
| France | The principal rungs are 5, 10, 15, 20, 25, 30, one-third, 50, two-thirds, 90, and 95 percent. French company law can support company-specific thresholds below 5 percent. Separate declarations state intentions for the coming six months at 10, 15, 20, and 25 percent. | The national implementation uses notification and publication procedures within the Transparency Directive architecture, with additional rules for intention declarations. The operative deadline must be checked for the issuer and obligation at issue. | Content changes with the rung. Ordinary major-holding information and higher-rung intention declarations are not one common message. | A useful multi-cell extension, not a binary fit. Higher rungs can change information content, not merely reported quantity. |
| Netherlands | The ladder is 3, 5, 10, 15, 20, 25, 30, 40, 50, 60, 75, and 95 percent, with repeated upward and downward notifications. | The national process operates within the Transparency Directive structure. Case-specific filing and publication deadlines should be read from the operative Dutch rules. | The standard substantial-holding notification is not an activist-purpose statement. | Does not fit. It produces many passive and directional report histories without a purpose-revealing flag. |
| Italy | The first rung is 3 percent for a non-SME issuer and 5 percent for an SME issuer, followed by further rungs. Declarations state intentions for the coming six months at 10, 20, and 25 percent. | The national process operates within the Transparency Directive structure. Holding reports and intention declarations can have distinct procedural requirements. CONSOB introduced a combined Form 120 (TR-1) and new submission process in 2026. | As in France, content changes at specified higher rungs because an intention declaration is added. | A useful multi-cell extension, not a binary fit. Issuer type changes the first rung and higher rungs change content. |

Three UK distinctions prevent a common category error. First, DTR 5 is the ordinary pre-bid holdings analogue. Second, Rule 8 begins only after an offer period starts. Third, Rule 9 is a 30 percent mandatory-offer control trigger. The persons-with-significant-control regime is a separate corporate-ownership regime. None should be used as a substitute for DTR 5 in a pre-bid comparison.

## Three legal mismatches

### Repeated upward and downward reports

The current model has one crossing and one flag. US Schedule 13D amendments, UK DTR 5, the EU ladder, and national implementations can generate sequences of reports. UK and EU-style reports can be triggered when a holding reaches, exceeds, or falls below a rung. A holder can therefore move through several public states before the control horizon.

A legally faithful public history must record at least the rungs, crossing directions, report times, and contents observed so far. A simple flagged-versus-pooled indicator discards this sequence. The current rule that the first flag terminates pooled trading also prevents later trades and later reports from changing beliefs before the control decision.

### Holdings content is not engagement content

An ordinary UK or EU major-holdings report generally reveals voting-right information, identity, chains of control, crossing date, and covered instruments. It does not establish that the holder is engaging. Passive holders can report. Downward reports can arrive. France and Italy add intention content only at specified higher rungs, so even within one jurisdiction some report cells are holdings-only and others are more purpose-revealing.

The model must therefore separate three objects:

1. **Reportable voting rights:** The legally attributed quantity used to test a notification rung.
2. **Economic stake and exposure:** The holder's payoff stake, including relevant cash and derivative positions. It need not equal reportable voting rights.
3. **Engagement:** The action or plan that can change the control outcome. It cannot generally be inferred from a holdings report.

EU Articles 13 and 13a and UK DTR 5.3 make the distinction concrete. Instrument rules can create and aggregate reportable voting-right equivalents. That legal measure is not automatically the holder's net economic stake and does not reveal engagement.

The United States is closer because Schedule 13D contains purpose and plans. Even there, more than 5 percent does not by itself imply Schedule 13D because qualifying passive and institutional holders can report on Schedule 13G. Item 4 also supplies a narrative purpose-and-plans disclosure, not the model's deterministic statement that engagement equals one.

### Public clocks are staged and bounded

A4 says the filing lands exactly at crossing plus `T`. Real rules generally set a latest permissible time. A filing can arrive earlier. In the UK and EU structures, holder notification and public dissemination are separate stages. The market's flag normally concerns public dissemination, not merely delivery to the issuer.

The smallest faithful clock has an actual holder delay and an actual publication delay, each constrained by the applicable rule. The delays may depend on jurisdiction, issuer type, holder information, and actual filing choice. A deterministic combined clock is a modeling assumption, not a direct reading of the legal deadline.

## Result-by-result portability

This table assesses portability, not validity inside the current model. Every current label remains as stated in `MODEL_CARD.md`, lines 526-559.

| Result | Portability assessment | Required change |
|---|---|---|
| D1 | The generic partition idea and price telescoping survive. The current one-indicator statement, exact clock equivalence, and two-cell map do not. | State and prove a new multi-report result. A measurable legal technology should map each underlying path into one public report history. Price changes can still telescope across trading and report events, but the event sequence and staged clocks must enter the statement. |
| L1 | Generalizes mechanically. | Replace the binary weighted average with a finite sum over report-history cells, treating null cells as undefined rather than imputing their conditional means. If exact reported quantities remain continuous, integrate them within the relevant top-level legal-history cell. |
| L2 | Fails as a legal implication unless every report history used as a disclosed cell is sufficient for both engagement and informed type. | Prove a cell-specific sufficiency result, if available. Ordinary UK and EU holdings reports do not imply engagement. A purpose statement at a higher French or Italian rung may still fail to identify the informed type or make prior order flow irrelevant. |
| L3 | The three-atom assumption does not travel. Law supplies report rules, not a symmetric three-point posterior support or a kernel that depends only on the engagement posterior. | Derive a new finite-cell or general-distribution result. L3 remains PROVED under A(tau) in the current model, but A(tau) is not established by a UK, EU, or US legal ladder. The card already records its separate applicability limits. |
| L4 | Set nesting survives only for a carefully defined additive and upward reform. The pooled engagement-share result does not survive passive or downward notifications. | Define tightening as a carefully coupled upward reform, such as adding a lower upward rung while retaining every old rung and holding holder scope, content, attribution, clocks, and policies fixed. Even then, newly reported histories need not be engaging histories. Leg 2 can reverse, and leg 3 needs new restrictions rather than the current A(br) bridge. |
| T1 | Needs a new proof and has no universal sign in a multi-cell regime. | Work with the absolute value of a signed sum of cell derivatives. Multiple moving cells can reinforce or cancel one another. More disclosure can remove cancellation and increase aggregate absolute sensitivity. There is no general replacement of the current chord-based scalar `W times C` formula. A multi-cell analogue requires a signed-sum or vector factorization. |
| P1 | Needs a new game and proof. | Permit several report nodes, trading after reports, actual timing choices within legal maxima, content that varies by rung, and reports by passive or downward-moving holders. Rebuild sequential optimality and beliefs. The current flag-terminates-pooling game cannot simply be relabeled. |
| C1 | The dominance-and-contraction method may be reusable, but the present scalar statement and numerical evidence are not portable. | First prove a new fixed-policy multi-cell result. Then formulate legal reforms as vector parameters and bound the equilibrium feedback for that new game. The current threshold-coordinate statement, direct sign, and node evidence are tied to the current scalar model and calibration. |

## Multi-cell decomposition

Use `q` as the legal-history index here to avoid collision with the card's engagement-premium kernel `h(I)`.

```text
Delta = sum over report histories q of weight(q) times premium(q).
```

At fixed policies, the general derivative is:

```text
dDelta/dkappa = sum over q of [dWeight(q)/dkappa times premium(q)
                               + weight(q) times dPremium(q)/dkappa].
```

If the cell weights are invariant to `kappa` at fixed policies, this reduces to:

```text
dDelta/dkappa = sum over q of weight(q) times dPremium(q)/dkappa.
```

Aggregate sensitivity is the absolute value of this signed sum. It is not generally the sum of the cells' absolute sensitivities. This blocks a universal `W times C` formula. Such a factorization requires the legal reform to isolate one moving residual cell or requires strong common-sign and proportional-scaling restrictions across all moving cells.

## Passive-holder counterexample

Before tightening, suppose the pooled population at the control horizon consists of three equally weighted types: one active type and two passive types. The active share of the pool is 1 divided by 3.

Now add a lower reporting rung. One passive type crosses it and reports fast enough for the report to be public before the horizon. The active type's slower report arrives after the horizon. The second passive type also remains pooled. The post-tightening pool therefore contains one active type and one passive type, so its active share is 1 divided by 2.

The pooled engagement share rises from 1/3 to 1/2. This reverses current L4 leg 2. The current proof avoids the counterexample by assuming that every newly flagged history is generated by Voice. UK and EU notification ladders do not supply that assumption because passive holders report too. Downward reports create further non-nested composition changes.

## Sign-cancellation counterexample

Suppose two legal cells have equal weights. Their local liquidity derivatives are `+1` and `-1`. The aggregate derivative is:

```text
0.5 times (+1) + 0.5 times (-1) = 0.
```

Consider a local content reform that leaves the cell weights unchanged but makes the negative-derivative cell fully revealing, so its derivative becomes `0`. The positive-derivative cell remains unchanged. The new aggregate derivative is:

```text
0.5 times (+1) + 0.5 times 0 = 0.5.
```

Absolute aggregate sensitivity rises from `0` to `0.5`. More disclosure has increased the absolute aggregate derivative by removing cancellation. These can be local derivatives around positive premium levels, so the example does not require a negative premium. This rules out a universal multi-cell attenuation sign for local content reforms that leave cell weights unchanged. A threshold or window reform requires an additional weight-transfer analysis before the same conclusion can be drawn.

## Smallest general model

The smallest useful extension is a finite report-history partition generated by a legal disclosure technology. It should contain:

1. A vector of notification rungs rather than one threshold.
2. Crossing directions, including upward and downward events.
3. A holder-notification delay and a separate public-release delay, each subject to legal upper bounds.
4. A content map by rung, direction, holder category, and legal route. The map can distinguish holdings-only reports, instrument reports, and purpose or intention declarations.
5. Attribution and aggregation rules for direct holdings, controlled entities, concert parties, proxies, and instruments.
6. Separate state variables for reportable voting rights, economic stake and exposure, and engagement.
7. A separate control trigger, such as a mandatory-bid threshold, that affects the control game but is not treated as another notification rung.
8. A public history through the control horizon that records no report or the ordered sequence of public reports and their contents.

With finitely many rungs, crossing directions, legal routes, and dates, the top-level legal-event histories are finite. Exact percentages and other continuous report fields can remain message coordinates inside a top-level cell, as exact stake does in the current flagged cell. Conditional premiums then average over those coordinates. If every distinct continuous message is instead treated as its own cell, the exact information partition is not finite and the sum becomes an integral. That distinction should be stated rather than hidden.

A reform is then a change in the legal technology, not automatically a scalar movement in one threshold. Lowering a rung, adding a rung, shortening a holder deadline, shortening an issuer-publication deadline, adding instrument attribution, and adding an intention statement are different reforms and can move different cells.

## Conditions for an honest binary collapse

A notification ladder can be collapsed to the current binary information structure only under the following restrictions:

1. There is only one payoff-relevant first report before the control horizon.
2. Every disclosed cell being aggregated into the flag fully reveals engagement and the informed type. It must satisfy the on-path sufficiency needed for an L2 analogue, corresponding to A7′, and any equilibrium proof that pins off-path flagged beliefs must separately satisfy the joint condition corresponding to A7-J.
3. Passive-holder and downward-crossing reports are irrelevant to payoffs or are outside the modeled population.
4. Later reports add no payoff-relevant information before the control horizon.
5. Holder and publication delays can be represented by one deterministic public clock.
6. All no-report histories can be aggregated into one residual opaque cell.

Importing the current threshold-comparative-static results into that collapsed model requires four further restrictions:

1. Plan and execution policies are fixed for the comparative static.
2. Cell derivatives do not create sign cancellation when an attenuation ratio is claimed.
3. The reform moves the one payoff-relevant threshold or clock without also changing attribution, holder scope, report content, or the control trigger.
4. A(tau) and A(br) are assumed for the current threshold theorem. A legal binary collapse does not establish either assumption.

The six collapse conditions can be plausible as a deliberate US Schedule 13D abstraction after restricting attention to purpose-revealing 13D filers and treating later amendments as irrelevant before the horizon. The extra four conditions are needed only to import the current comparative-static theorem stack. Neither set is a direct description of UK DTR 5 or an EU voting-right ladder. France and Italy particularly resist collapse because the information content itself changes at higher rungs.

## Practical recommendation

Keep the December paper explicitly US Schedule 13D-specific. Present current US law as a stylized purpose-revealing first-filing model. State that the model abstracts from Schedule 13G eligibility, filing before the maximum deadline, later Schedule 13D amendments, and richer Item 4 narratives.

Do not claim cross-country universality for the current theorem stack. Present the general claim at the correct level: disclosure law creates a market partition. Name the UK and EU notification ladder as an extension, not as an application of the existing binary theorem.

France and Italy are especially useful future cases because information content changes at higher rungs. They could identify the effect of adding intention content separately from the effect of reporting voting rights. A universal multi-cell attenuation theorem is a separate project, not a small robustness check.

## Official sources

### European Union

- [Transparency Directive 2004/109/EC, consolidated text dated 2024-01-09](https://eur-lex.europa.eu/eli/dir/2004/109/2024-01-09/eng), especially Articles 3, 9, 12, 13, and 13a.
- [Directive 2013/50/EU](https://eur-lex.europa.eu/eli/dir/2013/50/oj), recital 12 on national lower or additional thresholds and stricter content, process, and timing, including disclosure of shareholders' intentions.
- [ESMA, Practical guide on notifications of major holdings under the Transparency Directive, 2025](https://www.esma.europa.eu/document/practical-guide-notifications-major-holdings-under-transparency-directive).

### United Kingdom

- [FCA DTR 5.1](https://handbook.fca.org.uk/handbook/dtr5/dtr5s1), especially DTR 5.1.2R.
- [FCA DTR 5.8](https://handbook.fca.org.uk/handbook/dtr5/dtr5s7), especially DTR 5.8.3R and DTR 5.8.12R, and the TR-1 content framework.
- [FCA DTR 5.3 financial-instrument rules](https://handbook.fca.org.uk/handbook/dtr5/dtr5s11).
- [Takeover Code Rule 8.3](https://code.thetakeoverpanel.org.uk/tp/rules/rule-8/rule-8-3.html).
- [Takeover Code Rule 9.1](https://code.thetakeoverpanel.org.uk/tp/rules/rule-9/rule-9-1.html).

### Selected national implementations

- Germany: [BaFin voting-right notification materials](https://www.bafin.de/EN/unternehmen-maerkte/mvp-portal/stimmrechtsmitteilungen/) and [WpHG section 33](https://www.gesetze-im-internet.de/wphg/__33.html).
- France: [AMF major-holding notifications and intentions](https://www.amf-france.org/en/forms-and-declarations/listed-companies-and-corporate-financing/major-holding-notifications-intentions).
- Netherlands: [AFM substantial-holdings register and threshold summary](https://www.afm.nl/en/sector/registers/meldingenregisters/substantiele-deelnemingen).
- Italy: [CONSOB major-holding notification procedures](https://www.consob.it/web/consob-and-its-activities/how-to-submit-major-holding-notifications1).

### United States

- [SEC Release No. 33-11253, Modernization of Beneficial Ownership Reporting](https://www.sec.gov/files/rules/final/2023/33-11253.pdf).
- [Current eCFR Regulation 13D-G table and rules](https://www.ecfr.gov/current/title-17/chapter-II/part-240/subpart-A/subject-group-ECFR7ce825ff9acf140?toc=1), especially Rules 13d-1 and 13d-2 and Schedule 13D Items 3 through 6.
- [SEC Division of Corporation Finance interpretations on Sections 13(d) and 13(g) and Regulation 13D-G](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/exchange-act-sections-13d-13g-regulation-13d-g-beneficial-ownership-reporting). These are staff interpretations, not a substitute for the rules.

## Source limits and legal caution

The legal facts in this note were verified by the research team as of 2026-08-29. Official web pages and handbooks can change. The EUR-Lex consolidated text is a documentation tool, and authentic Official Journal texts control. ESMA's practical guide and regulator summaries assist navigation but do not replace legislation, binding rules, or case-specific advice.

The national table does not resolve issuer home state, market scope, exemptions, attribution, group or concert-party treatment, instrument classification, form requirements, or the interaction with takeover and company law. It does not replace national legal analysis. This note is not legal advice.

## Not claimed

This note does not claim that any current result is false within its stated hypotheses. It does not demote D1, L1, L2, L3, L4, T1, P1, or C1. It does not amend A4, A7′, A7-J, A(tau), A(br), the result ledger, or the card's not-claimed list. It does not claim a universal sign for disclosure attenuation under a notification ladder. It does not claim that the short national comparison is complete.
