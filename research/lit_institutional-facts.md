# Institutional Facts Dossier — Disclosure Thresholds, Takeover Regulation, and Data Sources

**Strand:** institutional-facts (LitResearcher_InstitutionalFacts)
**Purpose:** Factual grounding for repositioning "Liquidity, Activism Disclosure, and Takeover Premia" toward empirics. For each institution: the exact rule, dates of changes, one line on how it supplies exogenous variation or a cross-sectional split for testing a liquidity–disclosure–premia model, and practical data sources. Sources are primary/regulatory (SEC, FTC, FCA, EU, CSA, case law) plus practitioner surveys; no finance papers are treated as sources of the rules themselves.
**Compiled:** August 2025 (this session); all web sources accessed in-session via search/fetch.

---

## 1. US Schedule 13D / 13G regime (the model's core institution)

### 1.1 Statutory skeleton
- **Williams Act of 1968** (Pub. L. 90-439) added Exchange Act §§13(d), 13(g), 14(d)–(f). Any person or "group" (§13(d)(3)) acquiring **beneficial ownership of more than 5%** of a class of SEC-registered voting equity must publicly file within the statutory window — **originally 10 calendar days** (unchanged 1968–2024).
- **Beneficial ownership** (Rule 13d-3): voting or investment power, plus rights to acquire within 60 days (options, convertible). Cash-settled derivatives generally do *not* confer beneficial ownership unless used with the purpose/effect of evading disclosure (Rule 13d-3(b); *CSX Corp. v. TCI/3G*, S.D.N.Y. 2008).
- **Schedule 13D** = control-intent filers; **Schedule 13G** = short form for three eligible classes: **Exempt Investors** (Rule 13d-1(a); e.g., acquired before the class was registered), **Qualified Institutional Investors (QIIs)** (Rule 13d-1(b): broker-dealers, banks, insurers, registered investment companies/advisers, pensions, etc., holding in the ordinary course without control purpose/effect), **Passive Investors** (Rule 13d-1(c): <20% ownership + Item 10 certification of no control purpose/effect).
- **Item 4 of Schedule 13D ("Purpose of Transaction")** — the intent language the model's "public voice" branch maps to: the filer must describe plans/proposals in enumerated categories (a)–(j): further acquisitions/dispositions; extraordinary corporate transactions (merger, reorganization, liquidation); sale of material assets; changes to the board or management (incl. number/term of directors); changes in capitalization or dividend policy; any other material change in business or corporate structure; charter/bylaw changes impeding control; delisting; deregistration; similar actions. Vague "reserve the right" boilerplate is common but is exactly the signal content empirical work codes.
- Item 6 requires disclosure of contracts/arrangements with respect to the issuer's securities (where derivatives exposure surfaces).

### 1.2 Old deadlines (pre-2024)
| Event | Old deadline |
|---|---|
| Initial 13D (>5%, or loss of 13G eligibility) | 10 calendar days |
| 13D amendment on "material change" (Rule 13d-2(a); ±1% deemed material per guidance) | "Promptly" |
| Initial 13G — QII / Exempt | 45 days after calendar year-end; QII: 10 days after first month-end at which >10% |
| Initial 13G — Passive | 10 days after crossing 5% |
| 13G amendments | Annually, 45 days after year-end (QII >10% or ±5% at month-end: 10 days after month-end) |
| 13G→13D switch (Rule 13d-1(e)) | File 13D within 10 days; "cooling-off" (no voting or further acquisitions) until 10 calendar days after the 13D filing |

### 1.3 The 2023–2024 SEC amendments ("Modernization of Beneficial Ownership Reporting")
Proposed **Feb 10, 2022** (Release 33-11030, File S7-06-22; Dodd-Frank 2010 §766 had given the SEC authority to shorten the 10-day window; Wachtell Lipton petitioned for shortening in 2011); adopted **Oct 10, 2023** (Releases **33-11253 / 34-98704**, 88 FR 76896, Nov 7, 2023); **effective Feb 5, 2024**; 13G deadline compliance **Sept 30, 2024**; structured-data (machine-readable) compliance **Dec 18, 2024**. ([SEC press release 2023-219](https://www.sec.gov/newsroom/press-releases/2023-219); [SEC final rule page](https://www.sec.gov/rules-regulations/2023/10/33-11180))

New deadlines (per final rule; 13G table confirmed by [Sheppard Mullin/NLR summary](https://natlawreview.com/article/revised-schedule-13g-filing-deadlines-effective-september-30-2024-what-you-need)):

| Event | New deadline |
|---|---|
| Initial **13D** | **5 business days** after crossing 5% or losing 13G eligibility |
| 13D amendment (material change) | **2 business days** |
| Initial 13G — QII/Exempt | 45 days after **quarter**-end of crossing (QII: unless >10% at a month-end) |
| Initial 13G — QII >10% at month-end | **5 business days** after that month-end |
| Initial 13G — Passive | **5 business days** after crossing 5% |
| 13G amendment — any material change (guidance: ±1% = material) | 45 days after **quarter**-end |
| 13G amendment — QII >10% or ±5% at month-end | 5 business days after month-end |
| 13G amendment — Passive >10% or ±5% | **2 business days** after the trade |
| 13G→13D switch | 13D within **5 business days**; cooling-off (no voting/acquisitions) until **5 business days after** the 13D filing (shortened from 10 calendar days) |

Other substantive content:
- **Cash-settled derivatives guidance** (adopting release, not a new rule): the SEC declined to adopt its proposed deemed-beneficial-ownership rule for cash-settled swaps, but reaffirmed that such instruments can (i) confer beneficial ownership under Rule 13d-3(b) if used as part of a plan to evade disclosure or to prevent the vesting of ownership, and (ii) may require Item 6 disclosure. 
- **Group formation guidance** under §13(d)(3): the SEC did *not* adopt its proposed "acting in concert" rule changes but gave guidance that two or more persons who *agree* to act together form a group (agreement is the touchstone), and that ordinary investor–issuer engagement (e.g., discussing executive comp or ESG without pressuring on specific votes) generally does not create a group or destroy 13G eligibility.
- Filing cut-off extended to 10 p.m. ET.

**Exogenous variation for our model:** (i) the Feb 5, 2024 shortening of the stealth-accumulation window 10 days → 5 business days is a clean, dated, plausibly exogenous shock to the *disclosure friction* parameter — usable as an event/DiD on toehold sizes, pre-announcement run-ups, and premia; (ii) 13G eligibility (passive <20%, QII, no control intent) splits identical-sized stakes into disclosed vs non-disclosed by *investor type*, not by choice; (iii) 20% passive cap and intent flips generate forced 13D events; (iv) structured data from Dec 18, 2024 lowers measurement cost of intent coding.

**Related institution for the "voice" channel:** SEC **universal proxy Rule 14a-19** (adopted Nov 17, 2021; mandatory universal proxy cards in contested elections for meetings after Aug 31, 2022) — lowered the cost of proxy contests, shifting the exit/voice margin. ([SEC Release 34-93596](https://www.sec.gov/files/rules/final/2021/34-93596.pdf))

**Data:** EDGAR (SC 13D/13G + /A amendments; full-text search back to 2001; submissions API; XBRL-structured 13D/G from Dec 2024); hand-collected academic 13D samples (Brav–Jiang–Partnoy–Thomas 2008; Gantchev 2013; Bebchuk et al. 2015; Collin-Dufresne–Fos); FactSet SharkRepellent/SharkWatch (campaign-level activism keyed to 13D events); Activist Insight (available via WRDS); LSEG/Refinitiv ownership and activism modules.

---

## 2. Hart–Scott–Rodino (HSR) premerger notification

- **HSR Act of 1976** (15 U.S.C. §18a): parties to reportable acquisitions must notify FTC/DOJ and observe a waiting period (**30 days**; **15 days** for cash tender offers) before closing. Applies to voting-securities acquisitions — i.e., it is a *second* disclosure/timing regime binding on stake-builders beyond 13D.
- **Thresholds** (indexed annually to GNP since the 2000 amendments, effective 2005): minimum size-of-transaction threshold **$50M (2000) → $119.5M (2024) → $126.4M (2025, effective Feb 2025) → $133.9M (2026, effective Feb 17, 2026)**; size-of-person test $26.8M/$267.8M (2026); $200M test → $535.5M (2026). Above the upper size-of-transaction tier ($535.5M in 2026) the size-of-person test drops out. Notification *thresholds* for subsequent filings at $50M/$100M/$500M/25%/50% (indexed). ([Dechert 2026 table](https://www.dechert.com/knowledge/onpoint/2026/1/minimum-hsr-reporting-threshold-rises-to-us-133-9-million--inter.html); [Foley](https://www.foley.com/insights/publications/2026/01/hart-scott-rodino-reporting-threshold-increases-by-7-5-million-after-latest-yearly-adjustment/))
- **"Investment-only" exemption** (statutory §7A(c)(9); **16 C.F.R. §802.9**): acquisitions made **"solely for the purpose of investment"** are exempt if the acquirer holds **≤10% of voting securities** afterward, *regardless of dollar size*. FTC/DOJ interpret "investment only" narrowly — any intent to influence basic business decisions (seeking a board seat, advocating strategic change, talking to management about operations) can void it. Enforcement: DOJ's 2016 settlement with **ValueAct** ($11M civil penalty) for relying on §802.9 while intending to influence; also 2015 Third Point-related scrutiny. 
- **§802.64**: ordinary-course acquisitions by certain institutional investors of ≤15% can be exempt.
- FTC proposed (Sept 2020) narrowing §802.9 (new de minimis rule + "associate" aggregation); **never adopted**.

**Exogenous variation:** (i) annual GNP indexation moves the *real* filing threshold mechanically — bunching/RD around it; (ii) the 10% investment-only cap is a hard kink: activists above 10% must pre-clear and wait (15 days for cash tender offers), so the cap co-moves with neither firm liquidity nor fundamentals — cross-sectional split on whether a stake of a given size triggers a second disclosure/waiting regime; (iii) §802.9 vs 13G "passive" definitions differ (10% vs 20%), creating a 10–20% band where 13G is available but HSR is not.

**Data:** FTC/DOJ annual HSR reports (counts by size band); SDC Platinum for transaction values; academic use of HSR bunching (e.g., Wollmann on stealth consolidation).

---

## 3. Poison pills / NOL pills

- **Flip-over rights plan** invented by Wachtell (1982); upheld in ***Moran v. Household Int'l***, 500 A.2d 1346 (Del. 1985). Modern **flip-in** pill: if any person crosses the trigger, all *other* shareholders buy shares at a steep discount, diluting the acquirer; the board retains redemption power (the pill is a *bid-delaying/negotiating* device, not an absolute bar).
- **Typical triggers:** standard rights plans **10–20%** (15% most common historically; 10% common in anti-activist pills), often with a higher carve-out (~20%) for passive 13G filers. **NOL (§382) pills: 4.9–4.99%** — set just below 5% because IRC §382 defines an "ownership change" as 5-percent shareholders collectively increasing ownership by >50pp over a rolling 3-year period (limiting NOL usage); blessed by Rev. Rul. 90-11. ([Morrison Foerster NOL plan guide](https://www.mofo.com/resources/insights/230724-protecting-tax-assets-considering-an-nol-rights-plan); [deallawyers.com](https://www.deallawyers.com/blog/2020/06/poison-pills-overview-of-nol-rights-plans.html))
- **Key case law on keeping the pill in place:** *City Capital v. Interco* (Del. Ch. 1988) and *Paramount v. Time* (1989); *Unitrin* (Del. 1995, "coercive/preclusive" standard); ***Air Products v. Airgas*** (Del. Ch. Feb 15, 2011) — pill sustained against a fully financed all-cash bid at a ~70% premium (pillar of "just say no" in Delaware); ***The Williams Cos. Stockholder Litig.*** (Del. Ch. Feb 26, 2021) — a **5% trigger** anti-activist pill struck down as unprecedented outside the NOL context (establishes the de facto floor for activist pills ≈10%). Dead-hand/no-hand pills invalid (*Carmody v. Toll Bros.* 1998; *Quickturn v. Mentor Graphics* 1998). Twitter adopted a 15% pill vs. Musk (Apr 15, 2022).
- **Prevalence:** ~2,000+ pills in force in the early 2000s; secular decline under proxy-advisor pressure (ISS/Glass Lewis oppose pills >1 year without shareholder ratification) to a few dozen standing pills by early 2020 — most boards now keep pills "on the shelf." **COVID wave:** >50 adoptions by end-April 2020 ([Thompson Hine](https://www.thompsonhine.com/insights/pandemic-poison-pill-wave-crashes/)); Eldar & coauthors document the "crisis pill" phenomenon and the rise of anti-activist pills ([ECGI WP](https://www.ecgi.global/sites/default/files/Paper%3A%20The%20Rise%20of%20Anti-Activist%20Poison%20Pills%09.pdf)).

**Exogenous variation:** pill triggers are firm-specific hard ceilings on stealth accumulation — a ready-made cross-sectional split on the maximum feasible undisclosed toehold, with the **4.99% NOL pill vs 10–20% standard pill** contrast orthogonal to liquidity; adoptions are 8-K events (event studies); *Williams* (2021) and the COVID wave give time-series shifts in trigger levels.

**Data:** FactSet **SharkRepellent** (all US in-force pills, triggers, terms, carve-outs); SDC Platinum's poison-pill module (US/Canada/Japan); 8-K Item 1.01/3.03 filings on EDGAR; ISS takeover-defense data (IRRC legacy on WRDS).

---

## 4. United Kingdom

- **Disclosure — DTR 5 (FCA Handbook):** for **UK issuers**, notify at **3%** and **each 1% above 3% up to 100%**, within **2 trading days**; for non-UK issuers the EU Transparency Directive ladder (5/10/15/20/25/30/50/75%) applies. The 3% level dates to the Companies Act legislation of the early 1980s (CA 1985 Part VI), carried into DTR 5 in 2007 when the TD was implemented; the UK kept its stricter ladder post-Brexit. ([Ogilvy summary](https://ogilvy-wachtel.com/2021/04/disclosure-requirements-for-an-interest-in-uk-listed-shares/); [DTR 5.1.2 text](https://service.betterregulation.com/document/122893))
- **Mandatory bid — Takeover Code Rule 9.1:** any person (with concert parties) acquiring **≥30% of voting rights**, or a holder of 30–50% acquiring *any* more, must make a **mandatory cash offer to all shareholders at the highest price paid in the prior 12 months**. "Whitewash" dispensation via independent-shareholder vote. During offer periods, Rule 8 requires disclosures from 1% holders. The Panel on Takeovers and Mergers dates to 1968; statutory basis since Companies Act 2006 Part 28 (implementing the Takeover Directive). Code changes effective 2024–2026 (e.g., Feb 2026 update) do not move the 30% trigger. ([Baker McKenzie UK guide](https://resourcehub.bakermckenzie.com/en/resources/global-public-ma-guide/europe-middle-east-and-africa/united-kingdom/topics/before-a-public-takeover-bid); [Wedlake Bell 2026 update](https://wedlakebell.com/insights/articles/navigating-the-takeover-code-key-changes-effective-february-2026/))

**Exogenous variation:** 3% + 1%-rungs vs the US 5%/13D regime is a clean cross-country contrast in disclosure *intensity*; the 30% mandatory-bid cliff predicts **bunching of stakes at 29.9%** (empirically documented in UK/EU stake data) — a direct testable implication for any model where disclosure/control thresholds shape accumulation; 2-trading-day deadline vs the US 5-business-day window gives timing variation.

**Data:** RNS filings (LSE regulatory news), the Takeover Panel's daily disclosure table, LSEG/Refinitiv and SDC for UK bids and premia.

---

## 5. EU Transparency Directive and other jurisdictions

### 5.1 EU baseline
- **Directive 2004/109/EC** (Dec 15, 2004; transposition by Jan 2007), Art. 9: notify when holdings reach/exceed/fall below **5%, 10%, 15%, 20%, 25%, 30%, 50%, 75%** of voting rights (member states may substitute ⅓/⅔ style thresholds — e.g., Luxembourg uses 5/10/15/20/25/33⅓/50/66⅔ per [CSSF](https://www.cssf.lu/en/information-requirements-issuers-of-securities/)). Deadline: **4 trading days** (tightened from 7 calendar days by **Directive 2013/50/EU**, which also extended Art. 13 to cash-settled instruments of "similar economic effect" — the EU's answer to hidden-stake decoupling). Member states may impose stricter regimes ([ESMA mapping of gold-plating](https://www.esma.europa.eu/sites/default/files/library/2015/11/2011_194.pdf)).

### 5.2 Stricter member states (initial threshold and ladder)
| Jurisdiction | Thresholds (initial + rungs) |
|---|---|
| Germany (WpHG §33) | **3**, 5, 10, 15, 20, 25, 30, 50, 75% |
| France (AMF) | **5**, 10, 15, 20, 25, 30, ⅓, 50, ⅔, 90, 95% + bylaws may add **0.5%** steps ([AMF](https://www.amf-france.org/en/professionals/professional-investors/my-relations-amf/major-holding)) |
| Italy (Consob) | **3%** (5% for SMEs), then 10/15/20/25/30/50/66.6/90% |
| Spain (CNMV) | **3**, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 75, 80, 90% |
| Netherlands (AFM) | **3**, 5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 95% ([AFM](https://www.afm.nl/en/sector/registers/meldingenregisters/substantiele-deelnemingen)) |

### 5.3 Mandatory-bid thresholds (Takeover Directive 2004/25/EC, Art. 5 — level set nationally)
UK 30%, France 30%, Germany 30%, Italy 30%, Spain 30%; **Switzerland (non-EU) 33⅓%** with statutory opt-up (to 49%) / opt-out (FMIA Art. 135).

### 5.4 Other meaningfully different jurisdictions
| Jurisdiction | Disclosure | Control trigger |
|---|---|---|
| **Switzerland** (FMIA Art. 120) | **3, 5, 10, 15, 20, 25, 33⅓, 50, 66⅔%**, 4 trading days | Mandatory offer at **33⅓%** |
| **Canada** (NI 62-103/62-104) | **10% early warning** + every ±2% (news release promptly, report in 2 business days) | Take-over bid regime at **20%**; 2016 amendments (eff. **May 9, 2016**): 105-day minimum deposit period, >50% minimum tender, mandatory 10-day extension ([OSC](https://www.osc.ca/en/industry/companies/mergers-and-acquisitions/early-warning-system-and-alternative-monthly-reporting-system)) |
| **Australia** | **5%** substantial-holder notice (2 business days), ±1% updates | **20%** acquisition prohibition (s.606) + **3%/6-month creep** exception |
| **Japan** (FIEA Art. 27-23) | **5%** large-shareholding report within **5 business days**, ±1% amendments | Mandatory tender offer for off-market purchases crossing **⅓** ([FSA working group](https://www.fsa.go.jp/en/refer/councils/singie_kinyu/20240130/01.pdf); 2024–26 reform debate on lowering the TOB threshold to 30%) |
| **Hong Kong** (SFO Part XV) | **5%** + each whole-% crossing, 3 business days | Takeovers Code Rule 26: **30%** mandatory bid; **2%/12-month creeper** (30–50%) |
| **China** (Securities Law 2019, eff. Mar 1, 2020) | **5%** report within 3 days (trading frozen until announced) + **every 1%** announcement | **30%** → mandatory tender offer |
| **India** (SEBI SAST 2011) | **5%** initial; every ±2% change | Open-offer trigger **25%**; **5%/year creeper** (25–75%) |

**Exogenous variation:** the EU is a ready-made panel for the paper's R2 comparative static (disclosure strictness × liquidity): initial thresholds of 3% (UK/DE/ES/IT/NL) vs 5% (FR) vs 10% (CA), plus different rung densities; **Directive 2013/50/EU** is a dated EU-wide shock to hidden-stake (cash-settled) strategies; mandatory-bid thresholds (25/30/33⅓%) generate stake bunching at different levels across countries; Canada's 2016 bid-regime reform is a dated regime break.

**Data:** national OAM registers (BaFin, AMF, Consob, CNMV, AFM, FINMA); ESMA practical guide to major-holdings notifications; SEDAR+ (Canada), ASIC substantial-holder notices (Australia), EDINET (Japan), HKEXnews, CSRC disclosures.

---

## 6. US state antitakeover statutes

- **First generation** (1970s–82): state takeover-disclosure/fairness acts applying to out-of-state incorporations — struck in ***Edgar v. MITE Corp.***, 457 U.S. 624 (1982) (dormant Commerce Clause; plurality also found Williams Act preemption).
- **Second generation — control share acquisition statutes:** upheld in ***CTS Corp. v. Dynamics Corp.***, 481 U.S. 69 (1987). Indiana model (IBCL Ch. 42, signed Mar 4, 1986, effective Aug 1, 1987): shares acquired crossing **20%, 33⅓%, or 50%** of voting power lose voting rights unless a **majority of disinterested shares** approve at a special meeting (50-day clock; acquirer pays). Adopted in ~25+ states (Ohio pioneered in 1982); opt-out generally available. ([FindLaw text](https://caselaw.findlaw.com/court/us-supreme-court/481/69.html))
- **Third generation — business combination ("moratorium") statutes:** upheld in ***Amanda Acquisition v. Universal Foods***, 877 F.2d 496 (7th Cir. 1989). **Delaware §203 (enacted 1988):** no business combination with an **≥15% "interested stockholder"** for **3 years** unless (i) the board pre-approved the crossing or the combination, (ii) the acquirer reaches **85%** in one step (excluding directors/officers and certain ESOP shares), or (iii) post-crossing approval by the board plus **⅔ of disinterested shares**. **New York BCL §912:** **5-year** freeze at **20%**. ~**33 states** had BC statutes by 1991 (Bertrand–Mullainathan 2003 list of 30 adopters 1985–1991, plus IA/OR/TX per Pinnell 2000). Staggered adoption years = the canonical governance DiD design.
- **Fair price statutes** (older wave, ~30 states at peak): supermajority (e.g., 80%, or ⅔ disinterested) or a fair-price test for back-end mergers. Many later folded into BC statutes.
- **Other constituency statutes** (~40+ states, 1986–1991): boards may weigh stakeholder interests when responding to bids. **Pill-validation statutes** (~24 states) explicitly authorize rights plans. **Disgorgement:** Pennsylvania Act 36 of 1990 (15 Pa.C.S. Subch. 25G) lets target firms recapture short-swing profits of failed bidders.

**Exogenous variation:** staggered state adoptions (1985–1991) provide DiD; the statute-type × threshold matrix (DE 15% + 3-year freeze vs IN 20/33⅓/50% voting-stripping vs NY 20% + 5-year freeze) is a cross-sectional split on *when a disclosed stake becomes strategically blocked* — interacting disclosure (13D) with the binding constraint a bidder actually faces. CTS (1987) and MITE (1982) are judicial regime breaks.

**Data:** state statutes via legal databases; ISS/IRRC takeover-defense datasets (WRDS) flag state-law coverage per firm; legal surveys (e.g., Karpoff's state-antitakeover-law chronologies).

---

## 7. Consolidated data-source catalog

| Source | What it gives | Notes |
|---|---|---|
| **SEC EDGAR** | SC 13D/13G (+/A), 8-K (pill adoptions, Item 4 intent exhibits), DEFA14A (campaigns), Schedule TO / 14D-9 (tender offers), 13E-3 (going-private) | Full-text search 2001+; **structured/machine-readable 13D/G from Dec 18, 2024**; free bulk data & submissions API; the project's `empirics/` EDGAR pipeline already targets this |
| **WRDS** | Activist Insight (campaign-level activism); Refinitiv/LSEG ownership (s34 13F); FactSet feeds; BoardEx; ISS (incl. IRRC takeover defenses) | 13D raw text itself is best taken from EDGAR; WRDS supplies the cleaned campaign/defense layers |
| **LSEG / SDC Platinum** | M&A deals with premia over unaffected prices (1-day, 4-week), toeholds, deal terms; shareholder-activism module; poison-pill module (US/Canada/Japan) | Standard source for the *premium* outcome variable |
| **FactSet SharkRepellent / SharkWatch** | In-force poison pills (triggers, carve-outs), takeover defenses, activism campaigns, 13D monitoring | The standard pill/defense source; also available via Databricks marketplace |
| **Activist Insight** | Global activist campaign data | Available through WRDS subscription |
| **Hand-collected academic 13D samples** | Brav–Jiang–Partnoy–Thomas (2008, hedge-fund activism 2001–06); Gantchev (2013); Bebchuk et al. (2015, 13Ds 2000–07); Collin-Dufresne–Fos | Benchmark coding of Item 4 intent, sequences, outcomes |
| **Non-US registers** | RNS/Panel table (UK); BaFin/AMF/Consob/CNMV/AFM/FINMA registers (EU/CH); SEDAR+ (CA); ASIC (AU); EDINET (JP); HKEXnews; CSRC | Each publishes threshold-crossing notices usable as event-level disclosure data |

---

## 8. Referee-facing cautions (institutional measurement)

1. **Thresholds are in voting rights / beneficial ownership, not economic exposure.** Rule 13d-3 counts 60-day rights (options) but generally not cash-settled swaps; DTR 5 and post-2013 EU rules count more instruments. Stake measures must specify which instrument set is being summed, or hidden-stake measurement error (CSX/TCI-style decoupling) will be attacked.
2. **13D Item 4 is intent-revealing but cheap-talk-prone**; coding "public voice" from boilerplate vs concrete proposals is the key empirical discipline (precedent: BJPT 2008's schedule-of-demands coding).
3. **Deadlines ≠ disclosure dates.** The economically relevant object is the *filings-made* date; late filings are common and the 2024 regime change altered both the deadline and the bunching point.
4. **Eligibility (13G) is a choice-type variable, not random.** The passive/QII split must be handled as selection (instrument via index membership / 13F institution type), or referees will reject it as exogenous.
5. **Mandatory-bid bunching (30%/29.9%) is documented anecdotally**; a formal bunching test needs care with concert-party aggregation rules.

## 9. Implications for repositioning (institutional strand)

- **R2 (disclosure attenuation) is directly testable three ways:** (a) the Feb 5, 2024 SEC window shortening (event/DiD: premia-to-liquidity sensitivity pre/post, with non-US targets as controls); (b) cross-country initial-threshold variation (3% UK/DE/ES/IT/NL vs 5% US/FR vs 10% Canada); (c) within-firm pill-trigger variation (4.99% NOL vs 10–20%) capping feasible undisclosed toeholds.
- **R1 (hump in κ) outcome data:** premia from SDC + liquidity measures, split by disclosure regime (13D-window era, 13G eligibility, mandatory-bid jurisdictions) — institutions supply the splits; the paper should *not* rest on numerical comparative statics alone.
- **Framing asset:** the 1968→2024 acceleration of 13D, the 2013/50/EU derivatives inclusion, and universal proxy (2022) are all instances of regulators *compressing stealth accumulation* — a policy hook that makes the model's disclosure parameter the object of live policy debate.
- **Borrow the mandatory-bid cliff** as a sharp prediction: if disclosure raises premia through bidder inference, stakes should bunch just below control triggers (30% UK/EU; 20% Australia/Canada; 15% DGCL §203) — a falsifiable, data-light empirical test distinct from the activism literature.
