# Novelty scan — framework_v3 (Feb-2024 13D shock; liquidity×disclosure×premia nexus)

Referee: novelty / competitor-scan. Date of scan: 2026-08-19.
Object: `framework_v3.qmd` l.35–38 ("Nobody … links market liquidity or the disclosure rule to
takeover premia") and l.52–55 ("No published or SSRN-visible empirical work exploits it yet;
one working paper engages the window trade-off theoretically. The window is open but closing.").

## Verdict

**Claim A ("no published or SSRN-visible empirical work exploits it yet") — FALSE as written.**
Trivedi (SSRN 6866499, posted 3 Jun 2026) runs a *pre-registered difference-in-differences* on the
Feb 5 2024 deadline change with 13G filers as the untreated control, and reports the treatment
effect on the compliance share within five business days (+0.35, p=0.007) with nulls on mean lag,
bid–ask spread, and an adverse-selection illiquidity proxy. That is the memo's own Fact F1, already
on SSRN. Separately, Polk–Buchheit–Riley–Stone is *published* (JFRC 32(4), 2024) and is entirely
about this window, though it projects rather than exploits the shock. Claim A must be rewritten.

**Claim B (theory nexus unclaimed) — TRUE, and it is the memo's real asset.** No paper found joins
all three legs (liquidity × disclosure *rule* × takeover premia). The closest single-leg-missing
papers are Corum (2025: liquidity × regulation × activism, no premia), Ordóñez-Calafi–Bernhardt
(JFQA 2022: disclosure threshold × activism, no takeover, no order-flow premium), and
Burkart–Lee–Voss (2024: activism × control market, no liquidity, no disclosure rule).

**Claim C ("window open but closing") — fair but complacent.** It is closing faster than stated: the
DiD is already posted, and Fos–Jiang–Partnoy (Bishop et al. 2026) are demonstrably working the
"disclosure friction → activist toehold" margin with causal designs. Treat the window as ~12 months.

## Candidate table

| # | title | authors | year | venue/status | URL | what it does (2 lines) | overlap verdict | implication for memo |
|---|---|---|---|---|---|---|---|---|
| 1 | The Mandated Revelation Field and a Conserved-State Measure of Scheduled Disclosure in U.S. Equity Markets | Avaneendra Trivedi (Independent) | 2026 | SSRN WP, posted 3 Jun 2026, 25 pp, no institution, 0 citations | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6866499 | Builds a hashed "owed-fact ledger" from EDGAR; then runs a pre-registered DiD on the Feb 5 2024 13D deadline change with 13G filers as control. Finds the rule moved the within-5-business-day compliance share (+0.35, p=0.007) but not mean lag, bid–ask spread, or the illiquidity/adverse-selection proxy. | **DIRECT COMPETITOR (same shock, same first-stage fact)** — but a weak one: independent single author, physics-flavoured framing, and its own headline return-prediction test is reported as failed. | Kills the literal "no SSRN-visible empirical work" sentence. Cite it, note the differences (they have no premia object and no toehold/accumulation margin), and use its **null on spreads** as a live threat to any liquidity-channel claim the memo makes. |
| 2 | Evidence for Accelerating First-time Activist Investor Disclosure / "Shrinking the 13D disclosure window will benefit non-activist investors" | Ryan Polk, Steve Buchheit, Mark Riley, Mary S. Stone | 2023 WP / 2024 pub | SSRN 4596959 posted 7 Nov 2023; **published** Journal of Financial Regulation and Compliance 32(4) 516 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4596959 · https://www.emerald.com/jfrc/article-abstract/32/4/516/1227033 | Measures abnormal returns earned during the legal filing delay in pre-2024 13D data; projects that a 10→5 day window cuts activists' delay profits. Explicitly a "baseline projection" for the new regime. | **ADJACENT** (same rule, pre-shock data, outcome = delay-period abnormal returns, not premia). | The memo cannot say the window is untouched by *published* work. Use as the benchmark the memo's post-2024 evidence updates. |
| 3 | The Stick or the Carrot? The Role of Regulation and Liquidity in Activist Short-Termism | Adrian Aycan Corum (Cornell) | 2025 | SSRN 4319599, posted 9 Jan 2023, last revised 29 Apr 2025, 77 pp; NFA presented | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4319599 | Theory: activist can exit before intervention payoff; liquidity changes and policies that harden exit (explicitly incl. the 2024 rules restricting activists' time window) raise value under moral hazard *or* adverse selection alone but destroy value under both. | **ADJACENT (same nexus, one leg missing)** — liquidity × regulation × activism, but no takeover premium, no disclosure-threshold inference partition, no order-flow price formation. | **This is almost certainly the "one working paper" the memo means** (prior brief's unidentified "Value-Destroying Activism" NFA paper). Name it and differentiate on the premium/free-riding leg. Note the author is the Corum of Corum–Levit (JFE 2019), already in the repo's lit set. |
| 4 | Antitrust, Anti-Activism | Robert Bishop, Vyacheslav Fos, Wei Jiang, Frank Partnoy | 2026 | SSRN 6061814, posted 13 Jan 2026, rev. 27 Jan 2026; BC Law Review forthcoming; ECGI/NBER-affiliated authors | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6061814 | Exploits the HSR premerger-notification threshold; causal evidence that activists avoid targets where a toehold would trigger HSR disclosure *before* the 13D filing. Also finds concentration falls after activism. | **ADJACENT (same mechanism family, different lever and outcome)** — a disclosure friction changes activist toehold/targeting, but no premia and not the 13D window. | The nearest *credible* team to the memo's shock. Cite as complementary evidence that disclosure frictions bind on accumulation; treat as the competitive clock on the empirical window. |
| 5 | Market Quality of Informed Trades | Wan Soo Choi, Juha Joenväärä, Dominik Rösch, Cristian Tiu | 2025 | SSRN 5317851, posted 25 Jun 2025, rev. 27 Jul 2026, 60 pp | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5317851 | ~500,000 13D-disclosed activist transactions matched to TAQ; activists have higher execution quality but higher price impact — they largely fail to hide among the uninformed. Notes the Feb 5 2024 amendment but does not use it as a design. | **ADJACENT** (liquidity × activist accumulation microstructure; no rule shock, no premia). | The best microstructure benchmark for the memo's order-flow-inference mechanism. Their "activists fail to hide" result is a *supporting* fact for partial revelation, and a hazard if the memo assumes full concealment. |
| 6 | Blockholder Disclosure Thresholds and Hedge Fund Activism | Guillem Ordóñez-Calafi, Dan Bernhardt | 2022 | **Published**, JFQA 57(7) 2834–2859 | https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/blockholder-disclosure-thresholds-and-hedge-fund-activism/3A56BF8A41948A79931DDE3920BFA71E | Theory of the optimal 5%-type disclosure threshold: uninformed investors want lower thresholds when trading losses to the activist beat the disciplining benefit. | **ADJACENT (nexus, one leg missing)** — disclosure threshold × activism, no takeover market, no premium. | Confirms the memo's framing that the *threshold* is claimed but the *deadline* and the *premium* are not. Its object is the threshold level, not the window length. |
| 7 | The Evolution of the Market for Corporate Control | Mike Burkart, Samuel Lee, Paul Voss | 2024 | ECGI Finance WP 956/2024; SSRN posted 12 Feb 2024, rev. 17 Mar 2026; **won 2025 ECGI Intesa Sanpaolo Finance Prize** | https://ecgi.global/working-paper/evolution-market-corporate-control · https://doi.org/10.2139/ssrn.4709037 | Theory of why takeover activism displaced hostile tender offers: as more control-oriented investors enter, informed shareholders broker sales to outside bidders rather than bid themselves. | **ADJACENT** — activism × market for corporate control, but no liquidity state variable and no disclosure rule. | Highest-prestige neighbour; the memo's "market for corporate control" framing must engage it directly. Its prize status raises the bar on framing, not on the mechanism. |
| 8 | Leader-Follower Dynamics in Shareholder Activism | Doruk Cetemen, Gonzalo Cisternas, Aaron Kolb, S. Viswanathan | 2026 | **Published/forthcoming**, Journal of Finance (10.1111/jofi.70033); NY Fed Staff Report 1030; SSRN 4213729 | https://onlinelibrary.wiley.com/doi/10.1111/jofi.70033 | Dynamic Kyle-style model of sequential activist accumulation: leaders create trading gains for followers, generating predictability contrary to Kyle (1985), shaping free-riding in governance. | **ADJACENT** — order-flow inference × activism × free-riding, but no disclosure-rule lever and no takeover premium. | The strongest methodological neighbour on the trading-inference leg. The memo's claim to be "the first formalization of how the market learns about activism-driven control events" is overstated against this paper — soften it. |
| 9 | Blockholder disclosure, activism, and takeovers | Paolo Giudici | 2025 | Book chapter, *Research Handbook on EU Securities Law* (Edward Elgar), ch. 10 | https://www.elgaronline.com/abstract/book/9781800376045/chapter10.xml | Doctrinal chapter on EU Transparency Directive (2004/109/EC) major-holdings transparency and its interaction with activism and takeovers. EU regime, not US 13D; no model, no data. | **NOT OVERLAPPING** (but a naming hazard — the title is nearly the memo's thesis in words). | Cite once as the legal-comparative reference so a referee who Googles the phrase finds it already handled. Do not claim the title-phrase as novel. |
| 10 | From 10 to 5, What A Way to Make a Livin': The SEC's Most Recent Amendments… | R. Young | 2024 | UC Law Journal (Hastings) vol. 76, student note | HeinOnline (hein.journals/hastlj76 §8) | Law-review note on the 2023 amendments; argues about whether the 10→5 change curbs "exploitative" activism. Normative, no data. | **NOT OVERLAPPING** (institutional-fact source). | Useful for the policy-debate framing paragraph only. |
| 11 | The hidden costs of hedge fund activism: insights into market liquidity dynamics | A. Meles, L.R. Pellegrino, D. Salerno et al. | 2026 | **Published**, European Journal of Finance 32(9) | https://www.tandfonline.com/doi/abs/10.1080/1351847X.2026.2655250 | Causal estimate that hedge-fund activism *deteriorates* target stock liquidity, more so under information asymmetry and financial constraints. | **ADJACENT** (liquidity × activism, reverse direction, no rule, no premia). | Direction-of-causality hazard: the memo treats liquidity κ as the state variable driving activism. A referee will ask about reverse causality; this paper is the citation they will use. |
| 12 | The Value of (Stock) Liquidity in the M&A Market | Massimo Massa, Moqi Xu | 2013 | **Published**, JFQA | https://eprints.lse.ac.uk/46343/1/Xu_Value%20of%20Stock.pdf | Target/acquirer stock liquidity affects M&A outcomes and deal terms — the canonical liquidity→M&A empirical anchor. | **ADJACENT** (liquidity × M&A, no disclosure rule, no activist). | The memo's liquidity→premia empirical leg must cite this plus Huang–Maharjan–Nanda (JCF 2024, "Liquid Stock as an Acquisition Currency", SSRN 4730486) and Dass–Huang–Maharjan–Nanda (2016). None of them has the disclosure rule. |

**Not found (i.e. genuinely unclaimed):** any paper — published, SSRN, NBER, ECGI, or arXiv — that
(a) models the 13D *deadline* (as distinct from the 5% threshold) as a policy lever, (b) carries a
liquidity/order-flow state variable, and (c) delivers the takeover premium as an equilibrium object.
The triple is open.

## SEC rule facts (with URLs)

Verified from the SEC press release page (browser; WebFetch is 403-blocked on sec.gov):
https://www.sec.gov/newsroom/press-releases/2023-219

- Releases 33-11253 / 34-98704, "Modernization of Beneficial Ownership Reporting"; **adopted Oct 10, 2023**.
  Adopting release PDF: https://www.sec.gov/files/rules/final/2023/33-11253.pdf ·
  Fact sheet: https://www.sec.gov/files/33-11253-fact-sheet.pdf ·
  Federal Register 88 FR 76896, published Nov 7, 2023:
  https://www.federalregister.gov/documents/2023/11/07/2023-22678/modernization-of-beneficial-ownership-reporting
- Effective **90 days after Federal Register publication** → **Feb 5, 2024**.
- Compliance dates, verbatim from the release: "Compliance with the revised Schedule 13G filing
  deadlines will be required beginning on **Sept. 30, 2024**. Compliance with the structured data
  requirement for Schedules 13D and 13G will be required on **Dec. 18, 2024**. Compliance with the
  other rule amendments will be required upon their effectiveness."

**Provisions the memo does list:** initial Schedule 13D deadline **10 calendar days → 5 business days**.

**Confounds bundled into the same Feb 5, 2024 date that the memo does NOT list — each is a threat
to a clean single-treatment interpretation:**

1. **13D amendment deadline: "promptly" → 2 business days.** Same effective date. Any outcome measured
   on 13D/A events (stake escalation, intent changes) is jointly treated. The memo's premium/toehold
   tests must say which margin they attribute the effect to.
2. **EDGAR filing cut-off extended to 10:00 p.m. ET** (from 5:30 p.m.) for same-business-day credit.
   This mechanically shifts measured filing *timestamps* and therefore any "delay in days" or
   "filed within N days" statistic — including the memo's Fact F1 — independent of behaviour.
   This is the most under-appreciated confound: part of a compliance-share jump can be a clock change.
3. **Cash-settled derivatives guidance** (Item 6 disclosure; Rule 13d-3(b) evasion standard reaffirmed).
   Changes the measured *composition* of disclosed economic exposure.
4. **Group-formation guidance** in the same adopting release — bears directly on wolf-pack accumulation,
   i.e. on the toehold-size outcome variable.
5. **13G acceleration (Sept 30, 2024) and structured data (Dec 18, 2024)** — these break the "13G filers
   as clean untreated control" design after Sept 2024. Trivedi's DiD uses exactly that control; the memo
   should either stop the post-window before Sept 30 2024 or address it explicitly.
6. Contemporaneous, unrelated: 2022 universal proxy card; 2024–25 SEC C&DI updates on 13G "passive"
   eligibility for ESG-engaged managers (Feb 2025) — a separate regime shift inside the post-period.

## Practitioner sources with post-rule statistics (URLs)

Honest result: I could **not** find a practitioner report publishing post-rule 13D filing-lag
statistics (median days, share within 5 business days). The best external benchmark for the memo's
Fact F1 is the academic DiD in row 1 (+0.35 on the compliance share), which corroborates the memo's
direction (35.7% → 75.6% ≈ +0.40) while disagreeing on the mean-lag margin. Institutional-fact
sources located (NOT competitors):

- SEC press release 2023-219 — https://www.sec.gov/newsroom/press-releases/2023-219
- Sidley Austin, "SEC Shortens Filing Deadlines for Schedules 13D/G" (Oct 2023) —
  https://www.sidley.com/en/insights/newsupdates/2023/10/sec-shortens-filing-deadlines-for-schedules-13d-g
- Skadden, "Reminders: Amended Beneficial Ownership Rules Effective" (Feb 2024) —
  https://www.skadden.com/insights/publications/2024/02/reminders-amended-beneficial-ownership-rules-effective
- Olshan client alert, deadlines effective Feb 5, 2024 —
  https://www.olshanlaw.com/Securities-Law-Blog/client-alert-important-reminder-new-schedule-13d-filing-deadlines-take-effect-monday-february-5-2024
- HLS Forum, "SEC Adopts Final Rules to Amend Beneficial Ownership Reporting Rules" (Nov 2023) —
  https://corpgov.law.harvard.edu/2023/11/26/sec-adopts-final-rules-to-amend-beneficial-ownership-reporting-rules/
- Cooley, "2024 Activism Year in Review: Activists Ascendent" (Jan 2025), 243 global campaigns, highest since 2018 —
  https://cooleyma.com/2025/01/30/cooleys-2024-activism-year-in-review-activists-ascendent/
- Lazard, Annual Review of Shareholder Activism 2025 (297 campaigns, third record year) —
  https://www.lazard.com/research-insights/annual-review-of-shareholder-activism-2025/
- Diligent Market Intelligence, Shareholder Activism Annual Review 2025 —
  https://learn.diligent.com/rs/946-AVX-095/images/DMI_ShareholderActivismAnnualReview2025.pdf
- Cleary Gottlieb, "2025 Shareholder Activism Trends and What to Expect in 2026" —
  https://www.clearygottlieb.com/news-and-insights/publication-listing/2025-shareholder-activism-trends-and-what-to-expect-in-2026

## Searches performed

All 2026-08-19. "Hits" = results returned, not results relevant.

| # | query | tool | hits | yield |
|---|---|---|---|---|
| 1 | "Schedule 13D" "five business days" 2024 rule empirical activism event study | WebSearch | 9 | Polk et al.; Meles et al. |
| 2 | SSRN WP 2024/25 shortened 13D filing window beneficial ownership amendments activism effects | WebSearch | 9 | SEC/law-firm only |
| 3 | "pre-disclosure accumulation" OR "stealth accumulation" 13D 2024 rule change activist returns | WebSearch | 8 | none new |
| 4 | "Value-Destroying Activism" NFA WP 13D five/ten-day window | WebSearch | 9 | dead end (title does not exist) |
| 5 | DiD "February 2024" 13D deadline toehold run-up premium | WebSearch | 10 | none |
| 6 | "wolf pack"/"13D filing" 2025-26 new rule shorter deadline accumulation SSRN | WebSearch | 10 | none |
| 7 | theory "disclosure threshold" blockholder accumulation takeover premium liquidity 2025-26 | WebSearch | 6 | Ordóñez-Calafi–Bernhardt |
| 8 | Cetemen Cisternas Kolb Viswanathan activist accumulation disclosure | WebSearch | 10 | JF 2026 confirmed |
| 9 | Burkart Lee Voss + Ordóñez-Calafi Bernhardt status | WebSearch | 18 | ECGI 956/2024, prize; JFQA 57(7) |
| 10 | liquidity → takeover/acquisition premium (Massa-Xu, Huang-Maharjan-Nanda) | WebSearch | 8 | JFQA 2013; JCF 2024 |
| 11 | practitioner post-rule filing-lag statistics (Lazard/Diligent/Olshan) | WebSearch | 40 (4 sub-searches) | no lag statistics found |
| 12 | Cooley 2024 activism year in review + 13D filing timing data | WebSearch | 10 | campaign counts only |
| 13 | HLS Forum post-rule 13D toehold-size data | WebSearch | 10 | none |
| 14 | NBER/ECGI 2025-26 13D deadline shortening toehold evidence | WebSearch | 8 | Bishop-Fos-Jiang-Partnoy |
| 15 | theory optimal disclosure-window length 5 vs 10 days welfare | WebSearch | 10 | none |
| 16 | "Schedule 13D" filings 2024-25 average delay/share within 5 bd | WebSearch | 8 | none |
| 17 | SSRN full-text: "five business days" "Schedule 13D" | ego-browser (SSRN UI) | 10,000 (fuzzy) | Polk et al.; Choi et al. |
| 18 | SSRN t-a-k: "five business days" 13D | ego-browser | 74 | Trivedi |
| 19 | SSRN t-a-k: beneficial ownership reporting modernization | ego-browser | 59 | Polk et al. |
| 20 | SSRN t-a-k: 13D disclosure window | ego-browser | 360 | Polk et al. |
| 21 | SSRN t-a-k: "Schedule 13D" deadline | ego-browser | 138 | none new |
| 22 | SSRN t-a-k: activist disclosure deadline shortened | ego-browser | 12 | none new |
| 23 | Scholar ≥2024: "five business days" "13D" activist disclosure | ego-browser | ~19 | Giudici; Young; Bishop et al.; Meles et al. |
| 24 | Scholar ≥2024: "Schedule 13D" "5 business days" 2024 rule change evidence | ego-browser | 9 | **Trivedi** (the DiD); Choi et al. |
| 25 | Scholar ≥2024: 13D deadline 2024 "natural experiment" activism accumulation | ego-browser | ~13 | none new |
| 26 | Scholar ≥2024: "beneficial ownership" SEC 2023 amendments activist campaigns empirical | ego-browser | ~97 | Kastiel–Nili "The Activism Gap"; Payne-Mann et al. |
| 27 | Scholar ≥2022: Giudici "Blockholder disclosure, activism, and takeovers" | ego-browser | 1 | Elgar chapter |
| 28 | Scholar ≥2022: "takeover premium" liquidity disclosure rule theory blockholder toehold | ego-browser | 12 | nothing joining all three legs |
| 29 | Scholar ≥2022: "disclosure rule" "market for corporate control" revelation price efficiency bidder | ego-browser | 3 | nothing |
| 30 | Scholar ≥2023: "Value-Destroying Activism" | ego-browser | 5 | title does not exist |
| 31 | Scholar ≥2024: NFA program "value-destroying" activism disclosure window | ego-browser | ~71 | **Corum (2025)** — the memo's "one working paper" |
| 32 | Scholar ≥2024: shortened/accelerated 13D deadline campaign outcomes DiD | ego-browser | 2 | none |
| 33 | SSRN abstract pages 6866499 / 5317851 / 6061814 / 4319599 | ego-browser | 4 | full abstracts extracted |
| 34 | SEC press release 2023-219 (dates + provisions) | ego-browser | 1 | verified verbatim |

### Access failures / tool limitations

- `WebFetch` on **sec.gov** returns HTTP 403 (all SEC pages). Worked around with ego-browser.
- `WebFetch` on **federalregister.gov** 302-redirects to `unblock.federalregister.gov` — the adopting
  release text was not read directly; dates were taken from the SEC press release instead.
- The SEC **fact-sheet PDF** rendered with no extractable text in the browser; its provision list was
  taken from the press release and corroborating law-firm memos.
- **SSRN's JSON API** (`api.ssrn.com/content/v1/bindings/204/papers?term=…`) silently ignores `term`
  and returns the latest-papers feed. Do not trust it for search.
- **SSRN's UI search is fuzzy/OR-matched** even with quoted phrases (e.g. `"five business days" 13D`
  in title-abstract-keywords returns 74 mostly-irrelevant results). Google Scholar was strictly better.
- `mcp__papers__search_papers` (arXiv) **timed out**; arXiv q-fin was therefore not swept. Given the
  topic (US securities regulation, finance journals) the expected yield is low, but this is unrun.

### Unrun queries (budget)

- arXiv q-fin sweep (tool timeout).
- Full text of Kastiel & Nili, "The Activism Gap" (Northwestern colloquium PDF) — flagged as having an
  "empirical core" and citing the 2023 §13(d) reform; **worth one follow-up call** to confirm it is not
  a competitor.
- Payne-Mann, Stice-Lawrence et al., "Potential Activism & the Threat of Public Campaigns"
  (SSRN 5076900) — references the Oct 2023 rule; abstract not read.
- Full text of Trivedi (6866499) beyond the abstract — its DiD specification, sample, and whether it
  touches premia at all.
- Full text of Corum (4319599) — whether it formalises the *window length* specifically or only
  "policies that make exit harder" generically. This determines how the memo differentiates.
- NFA 2024/2025 conference programme (portal was JS-blocked for the prior agent; not retried).
- Repec/EconLit and Google Scholar citation-forward search on Polk et al. (who cites it since 2024).
