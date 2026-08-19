# Trivedi (2026) — "The Mandated Revelation Field and a Conserved-State Measure of Scheduled Disclosure in U.S. Equity Markets"

**Venue / status:** SSRN working paper 6866499 *(the abstract ID is **not** printed anywhere in the PDF — it comes from `research/txt_extracts/FETCH_LOG_B.md`, which records the SSRN URL the author's copy was fetched from; verified by verifier as provenance, not as a claim of the document)*, dated "June 2026" on the title page (PDF CreationDate 2026-06-02); independent researcher (Avaneendra Trivedi, no institutional affiliation); no journal, no R&R, self-disseminated ("We disseminate through zero-fee venues", p. 16). Not peer reviewed.
**Full text from:** `research/txt_extracts/trivedi_2026_ssrn.pdf` (25 pp) and `research/txt_extracts/trivedi_2026_ssrn.txt` (`pdftotext -layout`) · **Reader:** opus · **Read:** full text, 25 pages (all 12 sections + Appendices A–G)
**Page numbering:** printed page number in the running header ("Trivedi (2026) | Mandated Revelation Field — N"), which is identical to the PDF page index (1–25). Quotes are character-for-character; line-break hyphenation rejoined and multi-space `-layout` padding collapsed to single spaces, nothing else changed.
**Type:** empirical (measurement + reduced-form) **Role for us:** competitor (shares our anchor, the 2024-02-05 window change) — and, on one narrow point, a usable first-stage citation

## 1. Question

Can the *stock of facts that are legally true, legally owed, but not yet published* be defined and measured as a market-state object in its own right, rather than being studied one filing at a time after each filing lands? Trivedi defines the "Mandated Revelation Field" (MRF) — a dated, cross-statute inventory of owed-but-unpublished facts across four statute families (13F, Form 4, Schedule 13D/13G, N-PORT) — builds a hashed, reproducible pipeline that reconstructs it from EDGAR, and then asks two empirical questions of it. First, did the February 5, 2024 shortening of the initial Schedule 13D deadline actually change realized disclosure timing (and did it move spreads or illiquidity)? Second, does the aggregate "Disclosure Debt" density predict abnormal returns out of sample? The paper answers the first with a mixed finding and the second, by its own locked decision rule, with a self-declared failure.

The relevance to us is narrow but sharp: Section 7 (pp. 10–11) is a pre-registered difference-in-differences on our anchor date, with Schedule 13G filers as the control group. To our knowledge this is the only paper we hold that runs a design on post-2024 13D outcomes.

## 2. Model / data and method

**Object (Sections 3–6, pp. 4–9).** `MRF(t) = ∑_{f ∈ owed(t)} m_f · δ(filer, security, type, release)_f` (eq. 1, p. 4) — a marked measure over owed facts. Timing and existence are computed exactly from a versioned, content-hashed "rule lattice" of eleven branches across four statute families (Appendix A, p. 19); dollar magnitudes are *set*-identified as Manski intervals from a second-order-cone feasibility program (eq. 3, p. 9; Appendix C, p. 21), never point-estimated. Scalar contractions: Disclosure Debt `D(t)` (owed-fact count / bounded backlog), the surfacing-window density `g(t,h)` at the statutory 45-day horizon, and the drain rate (p. 4). A four-state conservation identity `N_owed = N_surf + N_pend + N_cloak + N_restate` (eq. 2, p. 4) is enforced as a test gate.

**Exact-layer sample (p. 6).** A deliberately small, *declared* filer universe: five 13F managers (Berkshire, Renaissance, Bridgewater, Scion, Pershing Square) and six Form 4 issuers (AAPL, MSFT, TSLA, JPM, NVDA, KO), CIKs in Table D.1 (p. 22). Ingest: 1,132 content-hashed raw files = 44 Form 13F filings (39,541 holdings rows) + 913 Form 4 filings (2,541 transaction rows), producing a ledger of 2,583 owed facts over a 2022–2023 backtest with 428 evaluation dates.

**The natural experiment (Section 7, pp. 10–11) — the part that matters to us.**
- *Treatment:* the 2024-02-05 shortening of the initial Schedule 13D deadline from ten calendar days to five business days (SEC Release 33-11253, cited p. 18).
- *Control:* Schedule 13G filers, on the argument that 13G deadlines did not change until 2024-09-30, so the post window can end before that date (p. 10).
- *Unit and outcome:* the filing, with the realized filing lag = filing date − event date, read from real EDGAR cover pages.
- *Window:* pre and post windows of 180 days each, fixed in the locked spec (p. 25).
- *Panel:* 333 filings — 148 Schedule 13D (treated), 185 Schedule 13G (control) — across 133 event-date clusters (p. 10). Standard errors clustered by event date throughout, citing Petersen (2009).
- *Outcomes:* primary = mean calendar-day lag; secondary = share of filings made within five business days; plus two microstructure outcomes on **daily** proxies (change in Corwin–Schultz high-low spread, change in Amihud illiquidity), resolvable for 234 of 333 filings (70% coverage).
- *Pre-registration:* the design was serialized canonically and SHA-256 hashed (`9ba37e1d`, full `9ba37e1db012c973`, Table F.1 p. 24) and written to an immutable file in the author's own version control before the post period was opened. **It is not lodged at any third-party registry** — no AEA RCT registry, no OSF, no repository URL appears anywhere in the 25 pages (verified: zero occurrences of "registry", "OSF", "AEA", "github", "zenodo", "repositor" in the full text).
- *Data-quality caveats stated:* cover-page event-date extraction ~90% reliable; subject-company resolution 70%; gaps flagged, not imputed (p. 16).

**The flagship return test (Section 8, pp. 12–14).** Separately pre-registered (`3b0732ed`). Monthly panel of 374 securities / 8,976 observations (4,488 out of sample in 2023), built by exploding portfolio-grain 13F facts to security level through an OpenFIGI CUSIP→ticker bridge (5,028 of 6,401 CUSIPs resolve; universe capped at top 400 by surfacing-event count, 859 candidates dropped and logged). Three nulls (seeded calendar permutation, Coval–Stafford flow null, 13F-only null), Harvey–Liu–Zhu t-hurdle of 3, Benjamini–Hochberg FDR at 5%, and a locked three-way decision rule.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | DiD on the **mean filing lag** is **+1.89 calendar days, SE 3.94, t = 0.48, p = 0.63** — a null | ESTIMATED | p. 11, Table 2 (text p. 10) |
| R2 | DiD on the **share filing within five business days** is **+0.348, SE 0.130, t = 2.69, p = 0.007** — the headline positive. **The author's own caveat, which must travel with any citation of this number:** "the secondary effect is significant at conventional clustered levels but does not clear the Harvey, Liu, and Zhu (2016) hurdle of three, which governs the cross-sectional return-factor test of Section 8 rather than a policy treatment effect" (p. 11) *(caveat added by verifier)* | ESTIMATED | p. 11, Table 2 (text p. 10; caveat p. 11) |
| R3 | Raw means behind R2: 13D compliance share 0.39 → 0.80; 13G control share 0.27 → 0.34; median 13D lag 10 → 7 calendar days | ESTIMATED (descriptive, no SE) | p. 10 |
| R4 | DiD on the **change in Corwin–Schultz bid-ask spread** is **+0.0013, SE 0.0051, t = 0.26, p = 0.80** — null | ESTIMATED | p. 11, Table 2 |
| R5 | DiD on the **change in Amihud illiquidity** (the adverse-selection proxy) is **+0.41, SE 0.81, t = 0.50, p = 0.62** — null | ESTIMATED | p. 11, Table 2 |
| R6 | Own interpretation: the constraint "binds in the right tail and on the compliance rate, not on the mean, because most filers already filed well inside the old window" | ASSERTED | p. 11 |
| R7 | **Flagship return-prediction test fails on the author's own locked rule.** Raw MRF density OOS coefficient 0.00124, t = 0.40, p = 0.69; the seeded calendar null carries a comparable t = 0.83. Committed verdict `beats_neither` | ESTIMATED | p. 13, Table 3 |
| R8 | The one survivor: cross-statute increment orthogonalized on the 13F-only signal, OOS coefficient 0.00373, **t = 3.09, p = 0.002**, FDR-reject = yes. Author states it does **not** rescue the claim | ESTIMATED | p. 13, Table 3 |
| R9 | Other flagship rows: Coval–Stafford flow null 5.3e-11 (t = 1.95, p = 0.051); 13F-only null −7.9e-06 (t = 0.00, p = 1.00); neither FDR-rejects | ESTIMATED | p. 13, Table 3 |
| R10 | Conservation identity (eq. 2) balances at all **428** evaluation dates; a deliberately corrupted input (a fact surfacing before it triggers) turns the gate red | NUMERICAL | pp. 4, 6; Fig. 1 p. 7 |
| R11 | Magnitude bounds contain the true reported transaction value for **1,535 of 1,536** real Form 4 facts (99.9%); median interval width ≈ $4bn | NUMERICAL | p. 9; Fig. 5 p. 10 |
| R12 | Determinism: canonical ledger hash `f3821ab3` byte-identical across clean rebuilds; lattice manifest hash `376cba1788ed5561` stable | NUMERICAL | pp. 6, 19, 24 |
| R13 | Disclosure Debt peaks at 150 owed facts on 2022-04-27 and drains in pulses synchronized to the statutory release calendar | NUMERICAL | p. 7, Fig. 2 |
| R14 | Novelty claim: no prior object aggregates pending mandated disclosures across filing types into a conserved dated market-state object; and no prior paper uses the Feb-2024 13D change as a natural experiment | ASSERTED (explicitly on a **bounded** search, correction invited) | pp. 3–4, 10, 24 |
| R15 | The conservation identity itself: stated and imposed by construction, enforced as a test — no proposition, no proof | ASSERTED | p. 4, eq. (2) |
| R16 | Eight-episode stress replay reports realized mean ΔAmihud per crisis episode (e.g. Lehman +5.96e-05, COVID-19 +2.36e-05, SVB −9.49e-06 flagged partial); the link from MRF density to realized asymmetry is **flagged pending** | ESTIMATED (descriptive) / NOT DONE | p. 14; Table E.1 p. 23 |

## 4. Institutional facts used

- **Schedule 13D initial deadline: ten calendar days → five business days, effective 2024-02-05** (p. 5, p. 10); SEC Release Nos. 33-11253; 34-98704; 88 FR 76896 (p. 18). Encoded as two dated lattice branches, `rule_13d_initial_pre2024` (to 2024-02-04) and `rule_13d_initial_post2024` (Table A.1, p. 19).
- **Schedule 13D/A amendment deadline: two business days, from 2024-02-05** (`rule_13d_amendment_post2024`, 17 CFR 240.13d-2(a), Table A.1 p. 19).
- **Schedule 13G deadline changes: 2024-09-30**, encoded as `rule_13g_qii_post` and `rule_13g_passive_post` (17 CFR 240.13d-1(b), (c)) — used to bound the post window rather than studied (pp. 5, 10, 19).
- Beneficial ownership trigger: crossing the five percent threshold (p. 2). The 5% level is *described*, never varied or studied.
- Form 4: two business days, SOX §403, effective 2002-08-29 (p. 5). Form 13F: $100m threshold, 45-day lag; value units changed from thousands to whole dollars effective 2023-01-03 (p. 5). N-PORT: three branches, 2024 amendments delayed to 2027-11-17 / 2028-05-18, tier threshold $1bn per FR Doc 2025-06861 (p. 5).
- All statutory parameters verified against eCFR and the Federal Register on 2026-05-31 (pp. 5, 24).
- **Data sources:** EDGAR structured submission feeds and cover pages (free, throttled, descriptive User-Agent); daily OHLCV from **Yahoo Finance**, cached and content-hashed because Yahoo adjusted prices are mutable (p. 22). No CRSP, no TAQ, no Compustat, no SDC.
- Microstructure estimators defined explicitly: Corwin–Schultz (2012) high-low spread with negative estimates truncated to zero; Amihud (2002) `|r_t| / DVOL_t × 10^6` with 20-day trailing mean; Roll (1984) as robustness only, not in the primary regressions (Appendix D.1, p. 22).

## 5. Referee-facing strengths / weaknesses

**Strengths**
- **Pre-registration honoured against the author's own interest.** The flagship verdict is `beats_neither` and is reported verbatim in the abstract, in Section 8, and in the conclusion. A locked three-way decision rule was written before the OOS window opened and was obeyed when it killed the headline claim. This is rarer than it should be and a referee will say so.
- **The right bite variable.** Choosing the compliance share within five business days as a secondary outcome, and finding the effect there while the mean is null, is a genuinely useful design lesson: when a deadline binds only for late filers, the mean is the wrong moment. R6 states this explicitly.
- **Institutional detail is correct and dated.** The rule lattice pins effective dates per branch and refuses to apply a regime before its compliance date. Statutory parameters verified against primary sources on a stated date, with one correction recorded ($1bn not $10bn N-PORT tier, p. 24).
- **Reproducibility machinery is unusually complete:** content-addressed lineage, 94-test suite (Appendix B, p. 20), pinned 176-package lockfile, seeded stochastics only in the permutation null and the sensitivity sweep.
- **Epistemic discipline on magnitudes:** a gate that *fails the build* if any owed dollar magnitude is emitted as a point rather than an interval.
- **Bounded claims labelled as bounded.** The novelty and first-use claims are explicitly "surviving a bounded adversarial search rather than proven" (Q11).

**Weaknesses / open flanks**
- **The parallel-trends assumption is never examined.** Verified by full-text search: the words "parallel", "trend", "pre-trend", "anticipat", "placebo" appear **zero times** in all 25 pages. No dynamic event-study plot, no pre-period leads, no placebo date, no test of whether 13D and 13G lags were moving together before 2024-02-05. For a paper whose only positive result is a DiD, this is the first thing a referee will ask for and the paper does not have it.
- **Anticipation is unaddressed.** The rule was adopted in October 2023 and effective 2024-02-05; a 180-day pre-window therefore straddles the adoption announcement. Filers could plausibly have adjusted before the effective date, which biases the DiD toward zero on the pre side. Not mentioned.
- **The EDGAR filing-cut-off / T+1 confound is unaddressed.** Filings submitted after the daily cut-off are stamped the next business day, which mechanically shifts a *business-day* compliance measure. Verified absent: "cut-off", "5:30", "same-day" do not appear. *(Two verifier caveats. First, the unhyphenated string "cutoff" does appear twice, pp. 12 and 25, but both are the top-decile **density** cutoff in the flagship test — nothing to do with EDGAR filing times, so the criticism stands. Second, the paper does validate the underlying **business-day arithmetic**: Appendix B's `test_calendars` module, 10 tests, asserts "US federal business-day arithmetic; weekend and holiday roll for the Form 4 two-day and 13D five-day deadlines, cross-checked against numpy busday" (p. 20). What is missing is the intraday **timestamp** question — whether a filing accepted after the daily cut-off is stamped the next day — not the calendar mechanics.)*
- **No power calculation, no MDE.** "Powered" is used rhetorically about the flagship panel's size, never as a computed minimum detectable effect. With SE = 3.94 days on the mean lag, the design cannot reject a five-day change; with SE = 0.0051 on a spread change and 0.81 on an Amihud change, the two microstructure nulls are **uninformative**, not evidence of no effect. The paper repeatedly calls them "null" without bounding what it could have detected.
- **The 13G control group is not defended.** 13G is filed by passive and qualified institutional investors who by construction disclaim control intent; 13D filers are the opposite population. Whether their filing-lag behaviour would have evolved in parallel absent the rule is asserted only via "13G deadlines did not change until September 30, 2024" — a statement about *treatment*, not about *comparability*. Worse, selection into 13D-vs-13G is itself plausibly responsive to the rule change (a tighter 13D window raises the relative attractiveness of qualifying for 13G), so the control group's composition may be treated too. Not discussed anywhere.
- **The microstructure outcomes were not truly pre-registered.** Appendix G.2 (Q10) concedes they "were flagged data-pending in the locked file and added on real daily proxies once the microstructure adapter was wired; the lag and compliance outcomes remained the locked headline." So the two nulls a reader might cite as pre-committed evidence are, on the author's own account, added after the lock.
- **Pre-registration is self-hosted.** "Committed to version control" with a SHA-256 hash is auditable only if someone can see the repository; no repository, DOI, or registry link appears in the paper. A referee will treat the hash as a claim, not as a verifiable pre-commitment.
- **Sample is small and coverage partial:** 333 filings / 148 treated / 133 clusters; event-date extraction ~90%; subject-company resolution 70% (234/333). Missingness on cover-page parsing is very unlikely to be random across 13D and 13G filers, whose cover pages differ.
- **The sampling frame for those 333 filings is never stated anywhere in the 25 pages (added by verifier).** Section 7.1 (p. 10) says only "The panel has 333 filings, 148 Schedule 13D treatment and 185 Schedule 13G control, across 133 event-date clusters." It never says whether that is the complete EDGAR population of 13D/13G filings in the two 180-day windows, a random draw, or simply the subset whose cover pages parsed. 148 initial 13Ds across a full 360-day span is far below the true US 13D flow, so it is plainly a subsample of unstated provenance — and if it is the parse-successful subset, then the "~90% extraction rate" caveat is not a reliability figure but a selection rule, and the DiD is estimated on selected filings. Appendix G.2's locked spec (p. 25) fixes the event date, the groups, the window and the outcomes, but not the universe. **This is the first question a referee asks and the paper cannot answer it. It also bears directly on us: it means R2 is a defensible first-stage *citation* but not yet a replicable first-stage *design*.**
- **Daily proxies, not TAQ**, for every microstructure outcome — conceded (Q7). Yahoo Finance as the price source, with mutable adjusted prices, is below the bar most finance referees hold.
- **Framing.** "Mandated Revelation Field", "conserved-state", "drain calendar", a four-state automaton, a conic program, and physics vocabulary throughout will read to a finance referee as apparatus disproportionate to the two regressions it supports. The two self-cited companion papers ("Gyral Covariance Decomposition", "Irreversibility Field Anatomy", p. 18) reinforce that impression.
- **Single independent author, no affiliation, no peer review, no acknowledgements, no seminar trail.** The paper is candid about this (declared filer universe, invited correction) but it means nothing here has been externally checked.
- **The headline empirical contribution is a self-declared failure.** R7. Only R2 survives as a positive finding, and R2 is a first-stage compliance fact, not an economic result.

## 6. What they do NOT do (scope boundary)

**Object.** No takeover, premium, bidder-entry, control-contest, campaign-success, activism, toehold, stake-size, or accumulation-margin outcome appears anywhere. Verified by full-text search across all 25 pages: **"takeover" = 0, "premium" = 0, "toehold" = 0, "stake" = 0, "activis*" = 0, "block*" = 0** occurrences. "Accumulat*" appears six times, and never as an outcome: twice describing Collin-Dufresne–Fos's pre-filing window (pp. 2–3) and four times as the decision variable of the bounds program (pp. 9, 20, 21). The measured objects are exactly: owed-fact counts / Disclosure Debt, realized filing lag, compliance share within five business days, change in Corwin–Schultz spread, change in Amihud illiquidity, and forward abnormal monthly return. There is no announcement return around the 13D itself.

**Margin.** The **window margin only**. The 5% threshold is mentioned once, descriptively (p. 2), and is never varied, never estimated around, never used for a bunching or regression-discontinuity design. The 13G September-2024 change is used only to bound the post window. No cross-country margin (no UK 3%).

**Identification.** One DiD with an intact-by-assumption control group, plus an out-of-sample predictive regression with permutation nulls. No structural estimation, no model, no theory. There is no economic model of *why* a filer chooses a lag, so the paper cannot distinguish mechanisms behind R6.

**Mechanism, declared open.** "This is an honest mixed finding: the 2024 rule moved timing compliance at the margin without detectable repricing, **which raises a mechanism question** and is more interesting than a clean positive" (Q5, p. 11) — the mechanism question is raised and left standing.

**Explicitly deferred by the author:**
- Intraday replication: "the daily-proxy limitation applies and replication with intraday TAQ is recommended" (Q6, p. 11; repeated p. 16).
- The link from MRF density to realized asymmetry across crisis episodes: "requires the historical owed-fact ingest for each era, which is outside the 2022-2023 ingested window, and is flagged as pending" (Q12, p. 14).
- The full EDGAR corpus: "the exact layer is run on a documented filer universe rather than the full corpus" (p. 16).
- Novelty and first-use: bounded, correction invited (Q11, p. 24).

## 7. Implications for our position

**Where they sit, precisely.**
- **OBJECT:** disclosure-timing compliance (share filed within five business days; mean lag), plus two generic target-level microstructure levels (Corwin–Schultz spread change, Amihud illiquidity change), plus a monthly forward abnormal return. **Not a control outcome.**
- **MARGIN:** the **window margin** (10 calendar days → 5 business days, 2024-02-05). Not the threshold margin.
- **IDENTIFICATION:** DiD, 13D treated vs 13G control, ±180 days, event-date-clustered SEs, self-hosted pre-registration. Plus a separate OOS predictive test.

**What this does to our whitespace.**

*Object: intact, and confirmed by a hostile search.* A direct competitor working on our exact anchor produced zero takeover, premium, bidder-entry, campaign-success, toehold or stake-size outcomes. Our object — liquidity × disclosure rule → **control outcome** — is untouched by the one paper that had the best opportunity to touch it.

*Margin: shared, and this is the real collision.* We are on their margin if we anchor on Feb-2024. But the collision is a stage collision, not an object collision: **they estimate the first stage (did the window bite on timing?), we would estimate the second (what does the bite do to control outcomes?).** Their R2 is therefore a *resource*, not only a rival: it is the best evidence we have that the window margin actually binds — the treated compliance share rises 0.39 → 0.80 against a control moving 0.27 → 0.34 (Q3), a DiD of +0.348 (p = 0.007). Any design of ours that assumes the 2024 change was real can cite this instead of assuming it. We should cite it that way and say so plainly — **but cite it with its two attached qualifications (added by verifier): the author himself notes it does not clear his own Harvey–Liu–Zhu t > 3 hurdle (p. 11), and the paper never states the sampling frame behind the 333 filings (§5). Cited as "a working paper reports the window bit on compliance" it is fine; cited as "the window bite is established" it is a hostage.**

*The economic content of the window margin is named by their own related-work section, and we should take it (added by verifier).* Section 2.2 (p. 3) positions the paper against Collin-Dufresne and Fos (2015): "Collin-Dufresne and Fos (2015) study Schedule 13D filers and exploit the pre-filing accumulation window as the period during which informed trading occurs, under the old ten-calendar-day regime. Their object is the window before a single filing type; ours is the aggregate owed queue across filing types, and our Schedule 13D analysis exploits the 2024 deadline change itself as a natural experiment on the timing of the drain, which their pre-2024 sample cannot address." That sentence is the bridge our position needs, written by a competitor: **CDF establishes that the pre-flag window is where informed accumulation happens; Trivedi establishes that the 2024 rule shortened that window in practice; neither asks what the shortening does to a control outcome.** The chain CDF (mechanism, pre-2024) → Trivedi (first stage, 2024) → us (control outcome) is the cleanest way to state our contribution, and it also shows the anchor is not virgin territory — Trivedi's own first-use claim (Q9) already concedes CDF is adjacent, and our competitor set adds Corum and Polk et al.

*Liquidity: driver vs outcome — the sharpest distinction available to us.* In Trivedi, liquidity is **only ever an outcome or a nuisance parameter**: an Amihud change as a DiD outcome (R5), an Amihud change per crisis episode in the stress replay (R16), and a participation ceiling κ = 10% inside the bounds program (p. 9, p. 21). It is **never a driver of behaviour** — there is no cross-sectional split by liquidity, no interaction, no conditioning. In our model liquidity (noise-trading intensity κ) is the *driving variable*, an ex-ante state of the security, and the object of interest is the **slope** — how much control outcomes move with liquidity, and how the disclosure rule attenuates that slope (draft_v2's T2). Trivedi never estimates any interaction of any kind. This is clean whitespace and we should state it in exactly these words: they measure a **level** effect of the rule **on** liquidity; we measure the **slope** of control outcomes **in** liquidity, and how the rule moves that slope.

*Do their nulls on spreads threaten a liquidity channel?* **No — but we must pre-empt the question, because a referee will ask it.** Three reasons, in decreasing order of strength:
1. **They are uninformative, not zero.** SE 0.0051 on the spread change and 0.81 on the Amihud change, on 234 filings of daily Yahoo data. No MDE is reported. A null with an unreported and almost certainly enormous confidence interval bounds nothing.
2. **Wrong variable.** They test whether the rule *changed* target liquidity around the surfacing window. We use pre-existing cross-sectional liquidity as a *conditioning* variable. A zero average effect of the rule on liquidity is entirely consistent with — indeed convenient for — a design that uses liquidity as an ex-ante moderator, because it means liquidity is not itself treated.
3. **Wrong estimand.** Our claim is about an interaction (attenuation of a liquidity slope), which no specification in the paper estimates. Their Table 2 has four rows and none is an interaction.
Note the direction of the favour: their null on liquidity as an *outcome* actually **protects** our use of liquidity as a **pre-treatment moderator** from the objection that the rule moved the moderator. We should say that.

*Can we reuse the 13G control group?* **For a first stage, yes with repairs. For our object, no — and we should say why, loudly.**
- For a **timing/compliance** first stage, 13G-as-control is defensible and we could replicate it — but only after adding what Trivedi did not: a pre-trend/event-study plot, a placebo date, an anticipation window around the October-2023 adoption, the EDGAR cut-off / T+1 check, a stated MDE, and — added by verifier — **a stated sampling frame**, which his paper never gives (§5). Our own referee checklist (CONTEXT.md) names every one of these, and Trivedi's Section 7 fails all of them. His design is a template for the outcome variable, not for the credibility work.
- For a **control outcome** (bidder entry, takeover premium, campaign success) 13G is structurally unusable as a control: 13G filers disclaim control intent by definition, so the counterfactual outcome is not merely unobserved, it does not exist. Worse, selection into 13D vs 13G is itself plausibly responsive to the window change, so the control group is contaminated on the very margin we would study. **We must distinguish ourselves here, not borrow.** Our comparison has to come from somewhere else — within-13D dose (pre-filing accumulation length, liquidity of the target), a never-13D benchmark of comparable targets, the threshold margin, or a cross-country contrast — and the card's contribution to the positioning stage is that the obvious control group is closed to us.

*The mean-vs-tail lesson is directly actionable.* R6 says the constraint binds in the right tail, not at the mean. If our theory's window margin works through *how much trading happens before the flag*, then the treated moment is the tail of the lag distribution, and treatment intensity should be defined on it (share of the pre-flag accumulation window removed for filers who were previously slow), not on a mean shift. Trivedi's null on the mean is a warning about how to define our treatment, not evidence against the window margin.

*Their first-use claim is contestable and we should not repeat it.* Trivedi states (Q9, p. 10) that a bounded search found no prior work using the Feb-2024 change as a natural experiment. Our own competitor set already includes Corum and Polk et al. on this anchor. The claim is honestly hedged as bounded, but it means (a) the anchor is more crowded than this paper thinks, and (b) our positioning cannot rest on being first to the date — only on being first to the *object*.

*Deliverability read.* This paper is a demonstration that the 13D/13G lag panel is buildable from free EDGAR cover pages by one person — 333 filings, event dates parsed at ~90%. That is a real signal for our December-package feasibility on a timing first stage. It is equally a demonstration that a free-data microstructure leg (Yahoo daily, Corwin–Schultz, Amihud) will not carry a clean result; if we need a liquidity measure, our `empirics/` layer must plan for something better or accept it as a moderator only.

*Bottom line for the positioning stage.* Trivedi occupies **{timing-compliance object} × {window margin} × {13D-vs-13G DiD}**. We should occupy **{control outcome} × {window margin, and ideally the threshold margin too} × {a design whose control group is not 13G}**, cite R2 as an established first stage, and pre-empt R4–R5 by naming them as underpowered level tests of the wrong variable.

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "On February 5, 2024 the initial Schedule 13D deadline shortened from ten calendar days to five business days. Schedule 13G deadlines did not change until September 30, 2024, so 13G filers are an untreated comparison group throughout a post window that ends before that date." | p. 10 | The design in their own words; the entire defence of the control group |
| Q2 | "This yields a clean difference-in-differences design on the realized filing lag, the date of filing minus the date of the event requiring filing, which is the timing outcome the rule directly governs and which is computable from free EDGAR cover pages." | p. 10 | Their object and margin, stated; free-data feasibility |
| Q3 | "The 13D compliance share rose from 0.39 to 0.80 across the event while the 13G control share moved only from 0.27 to 0.34, and the median 13D lag fell from ten to seven calendar days." | p. 10 | The first stage we can cite: the window margin bit |
| Q4 | "The pre-registered primary outcome, the mean calendar-day lag, does not move: the difference-in-differences estimate is plus 1.89 days, with a t-statistic of 0.48 and p of 0.63, a null reported verbatim." | p. 10 | The mean-vs-tail lesson; how to define our treatment intensity |
| Q5 | "Both asymmetry outcomes are null: the change in the Corwin-Schultz spread across the surfacing window has a difference-in-differences of plus 0.0013 (t = 0.26), and the change in Amihud illiquidity has a difference-in-differences of plus 0.41 (t = 0.50)." | p. 11 | The nulls we must pre-empt; note SEs 0.0051 and 0.81 in Table 2 |
| Q6 | "the 2024 rule moved timing compliance at the margin without detectable repricing, which raises a mechanism question and is more interesting than a clean positive" | p. 11 | They leave the mechanism open — our opening |
| Q7 | "the daily-proxy limitation applies and replication with intraday TAQ is recommended" | p. 11 | Their own concession that the microstructure leg is weak |
| Q8 | "the constraint binds in the right tail and on the compliance rate, not on the mean, because most filers already filed well inside the old window" | p. 11 | Design lesson: define treatment on the tail |
| Q9 | "A dedicated search on 2026-05-31 found no prior published or working paper using this change as a natural experiment; the closest located work, Collin-Dufresne and Fos (2015), studies the pre-filing window under the old regime and does not exploit the 2024 change." | p. 10 | Their first-use claim — contestable given Corum / Polk et al. |
| Q10 | "The proposal named microstructure asymmetry outcomes, the change in Corwin-Schultz spread and the change in Amihud illiquidity, were flagged data-pending in the locked file and added on real daily proxies once the microstructure adapter was wired; the lag and compliance outcomes remained the locked headline." | p. 25 | The spread/illiquidity nulls are NOT strictly pre-registered — by the author's own account |
| Q11 | "Both searches are bounded rather than exhaustive gated full-text sweeps, so the first-use and novelty claims are stated as surviving a bounded adversarial search rather than proven, and correction is invited." | p. 24 | Honest hedging; licenses us to contest the first-use claim |
| Q12 | "The owed-fact queue reconstruction that would link MRF surfacing density to the realized asymmetry resolution requires the historical owed-fact ingest for each era, which is outside the 2022-2023 ingested window, and is flagged as pending." | p. 14 | Explicit scope boundary: the density→liquidity link is not done |

Additional verbatim strings verified against the full text and available if needed: "The committed verdict is beats_neither." (pp. 13, 25); "The panel has 333 filings, 148 Schedule 13D treatment and 185 Schedule 13G control, across 133 event-date clusters." (p. 10); "Standard errors are clustered by event date throughout, following the panel-clustering guidance of Petersen (2009)." (p. 10); "Event dates were extracted from the real cover pages with an approximately ninety percent extraction rate, and unresolved subjects are flagged rather than imputed." (p. 10); "We add the proposal named microstructure outcomes on real daily proxies, resolving the subject company from the EDGAR header for 234 of 333 filings, a 70 percent coverage." (p. 11); "Their object is the window before a single filing type; ours is the aggregate owed queue across filing types, and our Schedule 13D analysis exploits the 2024 deadline change itself as a natural experiment on the timing of the drain, which their pre-2024 sample cannot address." (p. 3); "the exact layer is run on a documented filer universe rather than the full corpus" (p. 16); "the cover-page event-date extraction is approximately ninety percent reliable and the subject-company asymmetry coverage is about seventy percent, both carried as data-quality caveats with the gaps flagged, not imputed" (p. 16).

## 9. Verification log

**Verified 2026-08-19 (adversarial verifier, opus). Method:** whole paper re-read, all 25 pages, re-extracted per page with `pdftotext -f N -l N -layout` into a page-marked file, so every page attribution below was checked against the page the text actually sits on rather than against a whole-document extract. All absence claims re-run as case-insensitive regexes over the 25 per-page extracts. Front matter checked against `pdfinfo` and printed p. 1.

**Counts: 41 OK · 0 WRONG · 1 MISCITED · 1 UNCHECKED · 5 omissions added.**

### Header / venue
| Item | Verdict | Checked against |
|---|---|---|
| Title-page date "June 2026" | OK | p. 1, under the affiliation line, verbatim |
| PDF CreationDate 2026-06-02 | OK | `pdfinfo`: "CreationDate: Tue Jun 2 14:24:13 2026 CST" |
| 25 pages, printed page = PDF index | OK | `pdfinfo` Pages: 25; running header "Trivedi (2026) \| Mandated Revelation Field — N" checked on every page |
| Independent researcher, no affiliation, no acknowledgements, no peer review | OK | p. 1 ("Independent Researcher", avaneendra22@gmail.com); "acknowledg" = 0 hits in 25 pages |
| "We disseminate through zero-fee venues" (p. 16) | OK | p. 16, conclusion, verbatim |
| **SSRN 6866499** | **MISCITED (fixed in header)** | The abstract ID appears nowhere in the PDF — no SSRN stamp, no version number. It is provenance from `FETCH_LOG_B.md`, which records the URL and an author-supplied `ssrn-6866499.pdf`. Header now says so |

### Quotes (§8) — all twelve
| # | Verdict | Checked against |
|---|---|---|
| Q1 | OK, verbatim, **p. 10** | §7.1 opening, first two sentences |
| Q2 | OK, verbatim, **p. 10** | §7.1, third sentence |
| Q3 | OK, verbatim, **p. 10** | §7.2, third sentence. 0.39 → 0.80, 0.27 → 0.34, median ten → seven all confirmed |
| Q4 | OK, verbatim, **p. 10** | §7.2, first sentence |
| Q5 | OK, verbatim, **p. 11** | §7.2 second paragraph. Both the +0.0013 (t = 0.26) and +0.41 (t = 0.50) match Table 2 |
| Q6 | OK, verbatim, **p. 11** | §7.2 second paragraph, closing |
| Q7 | OK, verbatim, **p. 11** | §7.2 final clause |
| Q8 | OK, verbatim, **p. 11** | First line of p. 11 (the sentence begins on p. 10 and completes on p. 11; the quoted fragment is entirely on p. 11, so the citation is right) |
| Q9 | OK, verbatim, **p. 10** | §7.1, fourth and fifth sentences |
| Q10 | OK, verbatim, **p. 25** | Appendix G.2, second paragraph. **Confirms the decision-critical claim that the two microstructure outcomes were flagged data-pending in the locked file and added after the lock** |
| Q11 | OK, verbatim, **p. 24** | Appendix F.1, closing sentence |
| Q12 | OK, verbatim, **p. 14** | §9, penultimate sentence |
| The eight "additional verbatim strings" (§8 tail) | OK, all eight, all on the pages cited | Checked one at a time; "The committed verdict is beats_neither." confirmed on both p. 13 (§8.3) and p. 25 (Appendix G.1) |

### Results (§3) — every number re-read off the printed tables
| # | Verdict | Checked against |
|---|---|---|
| R1 | OK | **Table 2, p. 11**, row 1: +1.89 / 3.94 / 0.48 / 0.63. Text statement on p. 10. Card's "(text p. 10)" is right |
| R2 | OK | Table 2 row 2: +0.348 / 0.130 / 2.69 / 0.007. **Author's own t > 3 caveat found on p. 11 and added to the row** — see omissions |
| R3 | OK | p. 10, §7.2, all three descriptive figures |
| R4 | OK | Table 2 row 3: +0.0013 / 0.0051 / 0.26 / **0.80** |
| R5 | OK | Table 2 row 4: +0.41 / 0.81 / 0.50 / **0.62**. (The card's "p = 0.62" matches the table; note the abstract does not report p-values for these) |
| R6 | OK, ASSERTED label correct | p. 11, first sentence, verbatim |
| R7 | OK | **Table 3, p. 13**: MRF aggregate raw 0.00124, t 0.40, p 0.69, FDR no; calendar null 0.00144, t 0.83, p 0.41. Verdict `beats_neither` at §8.3 p. 13 and again p. 25 |
| R8 | OK | Table 3 last row: 0.00373, t 3.09, p 0.002, FDR reject **yes**. The "does not rescue the claim" statement is on p. 13, verbatim |
| R9 | OK | Table 3 rows 3–4: Coval-Stafford 5.3e-11 / 1.95 / 0.051 / no; 13F-only −7.9e-06 / 0.00 / 1.00 / no |
| R10 | OK | 428 evaluation dates confirmed on pp. 1, 4, 6, 7 and 16; corrupted-input red test pp. 4, 6, Fig. 1 caption p. 7 |
| R11 | OK | p. 9 §6.2 text (1,536 facts, 1,535 contained, 99.9%, median width "about four billion dollars", exception ticker RBBN) and Fig. 5 caption p. 10 |
| R12 | OK | f3821ab3 on p. 6 and Table F.1 p. 24; 376cba1788ed5561 on pp. 19 (twice) and 24 |
| R13 | OK | p. 7, twice — body text and Fig. 2 caption. 150 owed facts, 2022-04-27 |
| R14 | OK, and the "bounded" hedge is real | pp. 3–4 (§2.4 sweep), p. 10 (§7.1), p. 24 (Appendix F.1) |
| R15 | OK | p. 4, Eq. (2), stated and imposed as a gate; no proposition, no proof anywhere |
| R16 | OK | **Table E.1, p. 23**: Lehman +5.96e-05, COVID-19 +2.36e-05, SVB −9.49e-06 "partial". Pending flag on p. 14 |
| Panel counts (§2) | OK | 333 / 148 / 185 / 133 clusters, p. 10; 234 of 333 at 70%, p. 11; ±180 days, p. 25; SHA `9ba37e1d`, full `9ba37e1db012c973`, Table F.1 p. 24; 374 securities / 8,976 obs / 4,488 OOS, p. 12; 5,028 of 6,401 CUSIPs and the 859-dropped cap, p. 12 |

### Scope claims (§6) — every absence re-run
| Term | Card says | Verifier finds | Verdict |
|---|---|---|---|
| takeover, premium, toehold, stake, activis*, block* | 0 each | **0 each across all 25 pages** | OK |
| parallel, trend, pre-trend, anticipat*, placebo | 0 each | **0 each** | OK |
| MDE, "minimum detectable" | 0 | **0** | OK |
| registry, OSF, AEA, github, zenodo, repositor* | 0 each | **0 each** — confirming the pre-registration is self-hosted and unverifiable from the paper | OK |
| "cut-off", "5:30", "same-day" | 0 each | **0 each** — but unhyphenated **"cutoff" = 2 hits (pp. 12, 25)**, both the top-decile *density* cutoff of the flagship spec. Substantively irrelevant to the EDGAR-timestamp criticism, but a reader re-running the grep would trip on it | OK, caveat added to §5 |
| accumulat* | 6, never as an outcome | **6 hits: pp. 2, 3, 9, 20, 21** — p. 2 and p. 3 describe Collin-Dufresne–Fos's pre-filing window, pp. 9/20/21 are the bounds program's decision variable. Exactly as the card says | OK |
| 13G | (used only to bound the post window) | 16 hits, pp. 1, 5, 10, 11, 19, 25 — all as control group or as a dated lattice branch; no 13G *outcome* anywhere | OK |
| "power"/"powered" used rhetorically, never as an MDE | — | 13 hits, pp. 1, 2, 6, 12, 13, 16, 17; every one is "powered test"/"powered universe"/"powerful", never a computed minimum detectable effect. The §5 criticism stands exactly as written | OK |

### UNCHECKED
- **The pre-registration itself.** The SHA-256 hashes `9ba37e1d` / `3b0732ed` and the claim that the specs were written to immutable files before the post period opened cannot be checked from the document — there is no repository, DOI or registry link, and the grep confirms none exists. The card already treats this as a claim rather than a verified pre-commitment (§5, Q10). Left in place, marked. **Decision-critical for how much weight we put on R2**: if we cite R2 as an established first stage, we are relying on an unverifiable pre-commitment plus an unstated sampling frame. Name both when citing.

### Omissions added (§ where added)
1. **§3 R2 and §7 — the author's own hurdle caveat on the one positive result.** p. 11: "the secondary effect is significant at conventional clustered levels but does not clear the Harvey, Liu, and Zhu (2016) hurdle of three, which governs the cross-sectional return-factor test of Section 8 rather than a policy treatment effect." The card recommended citing R2 as an established first stage without carrying the caveat the author himself attaches to it. Now attached in both places.
2. **§5 and §7 — the sampling frame for the 333 filings is never stated.** New bullet in Weaknesses. Nowhere in 25 pages does the paper say whether the panel is the full EDGAR population in the two windows, a random draw, or the parse-successful subset; 148 initial 13Ds over 360 days is well below the true flow. Appendix G.2's locked spec (p. 25) fixes date, groups, window and outcomes but not the universe. This is the single largest hole in Section 7 and the card had it nowhere.
3. **§7 — the Collin-Dufresne–Fos bridge, in Trivedi's own words.** §2.2 (p. 3) names the pre-filing accumulation window as where informed trading happens under the old ten-day regime and concedes CDF's pre-2024 sample cannot address the 2024 change. That gives us the three-link chain — CDF (mechanism) → Trivedi (first stage) → us (control outcome) — for stating our contribution, and it is the economic content of the window margin, which the card previously left implicit.
4. **§5 — the business-day arithmetic *is* validated.** Appendix B's `test_calendars` (10 tests, p. 20) asserts weekend/holiday roll for the Form 4 two-day and 13D five-day deadlines against `numpy busday`. The card's T+1 criticism was slightly overstated as written; it now distinguishes calendar mechanics (done) from the intraday EDGAR timestamp question (not done). Keeping this precise matters because we will make the same criticism in writing.
5. **§5 — the "cutoff" grep caveat** (see the scope table above), so nobody re-running the check thinks the card was wrong.

### Overall verdict
**Unusually clean. Not one number, quote, page attribution or absence claim was refuted — 41 checks OK, zero WRONG.** The only header correction is the SSRN ID, which is provenance rather than a document claim. The five omissions are all in the same direction: the card was slightly too generous to Section 7 as a *design* (no sampling frame, an unverifiable pre-registration, a headline that misses the author's own hurdle) while being correctly hostile to it as *evidence*. The card's central competitive reading — Trivedi occupies {timing-compliance object} × {window margin} × {13D-vs-13G DiD}, touches no control outcome, and never uses liquidity as a driver — survives every check, including a re-run of all six object greps at zero hits.

---

**Reader's notes for the verifier** *(retained; every item below was re-run and confirmed — see the tables above)*. (a) Quotes were checked programmatically against `research/txt_extracts/trivedi_2026_ssrn.txt` with whitespace normalised and line-break hyphenation rejoined (`difference-in-\ndifferences` → `difference-in-differences`, `pre-\ncommitment` → `pre-commitment`); all twelve Q-quotes and the eight additional strings matched on the page cited. (b) The absence claims in §6 rest on case-insensitive full-text counts over all 25 pages: takeover 0, premium 0, toehold 0, stake 0, activis* 0, block* 0, parallel 0, trend 0, pre-trend 0, anticipat* 0, placebo 0, "minimum detectable" 0, MDE 0, registry 0, OSF 0, AEA 0, github 0, zenodo 0, repositor* 0, "cut-off" 0, "5:30" 0. These are worth re-running. (c) Table 2 (p. 11) and Table 3 (p. 13) are the sources for every ESTIMATED number; the abstract rounds the compliance-share DiD to "plus 0.35" while Table 2 prints +0.348 — both are the same estimate. (d) The June-2026 date is from the title page ("June 2026"); `pdfinfo` reports CreationDate 2026-06-02, consistent with our note of a 3 June 2026 SSRN posting but one day earlier — the PDF carries no version number and no SSRN abstract-ID stamp inside the document.
