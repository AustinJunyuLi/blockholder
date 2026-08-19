# Fact sheet — SEC Release 33-11253, "Modernization of Beneficial Ownership Reporting"

**Not a paper card.** An institutional fact sheet for the empirical-spec ticket: every number and
date below is quoted from the release itself with a page cite, so the spec never has to re-open a
295-page PDF.

**Source:** `research/txt_extracts/sec_release_33_11253.pdf` / `.txt` — Release Nos. **33-11253;
34-98704**, File No. **S7-06-22**, RIN 3235-AM93, adopted **October 2023**, "Conformed to Federal
Register version", **295 pages**. Read by: supplement reader (opus), 2026-08-19.
**Page numbers below are the PDF's own printed page numbers**, which run 1–295 and match the PDF
page index one-for-one (verified on pp. 9, 46, 178, 189, 210, 225).

---

## 1. Effective and compliance dates

| Item | What the release says | Page |
|---|---|---|
| **Effective date of the amendments** | "Effective dates: The amendments are effective on **February 5, 2024**." | p. 1 (DATES caption) |
| **Initial Schedule 13D deadline** | Current: "Within 10 days after acquiring beneficial ownership of more than 5% or losing eligibility to file on Schedule 13G. Rule 13d-1(a), (e), (f), and (g)." → New: "**Within five business days** after acquiring beneficial ownership of more than 5% or losing eligibility to file on Schedule 13G." | p. 10 (summary table) |
| **Schedule 13D amendment (13D/A) deadline** | Current: "**Promptly** after the triggering event. Rule 13d-2(a)." → New: "Within **two business days** after the triggering event. Rule 13d-2(a)." The *triggering event* itself is unchanged: a material change in the facts set forth in the previous Schedule 13D. | pp. 10–11 (summary table) |
| **Schedule 13G — initial** | Current: QIIs & Exempt Investors 45 days after **calendar year**-end; QIIs 10 days after month-end above 10%; Passive Investors within 10 days. → New: 45 days after **calendar quarter**-end; QIIs **five business days** after month-end above 10%; Passive Investors **five business days**. | p. 10 |
| **Schedule 13G — amendments** | New: 45 days after calendar quarter-end in which a **material** change occurred (replacing "any change"); QIIs five business days after month-end; Passive Investors **two business days** after exceeding 10% or a 5% move. | pp. 9, 11 |
| **Schedule 13G compliance date** | "compliance with the revised Schedule 13G filing deadlines under Rules 13d-1 and 13d-2 will not be required before **September 30, 2024**. Thus, notwithstanding the fact that the final amendments will become effective on February 5, 2024, beneficial owners will continue to be required to comply with the current Schedule 13G filing deadlines **through September 29, 2024**." | p. 165 (§ II.G) |
| **Structured-data (XML) requirement** | Voluntary compliance for 13G filers may begin **December 18, 2023**; extended transition period adopted in response to comments. | pp. 164–165 |
| **Major rule** | Designated a "major rule" under the Congressional Review Act, 5 U.S.C. 804(2). | p. 165 |

**One-line version for the spec:** 13D initial 10 calendar days → 5 business days and 13D/A "promptly"
→ 2 business days, both effective **2024-02-05**; all 13G changes bind only from **2024-09-30**.

---

## 2. The old ten-calendar-day rule and the business-day practice around it

- The pre-amendment rule was **ten calendar days**, not business days: "Within 10 days after
  acquiring beneficial ownership of more than 5%…" (p. 10; the operative text is Rule 13d-1(a)).
- **Rule 0-3 rolls a weekend/holiday deadline forward**, which is what makes ten calendar days behave
  like a slightly longer window in the data. The release states this three times, twice quoting the
  rule verbatim: "**if the last day of a filing deadline expressed in 'days' falls on a Saturday,
  Sunday, or Federal holiday, then such filing may be made on the next business day thereafter.
  17 CFR 240.0-3**" (p. 46, and again p. 69 n. 268).
- The same rule is what forces the release's own late/timely split: "By rule, the Commission accepts
  as timely any filing that, if the calendar due date falls on a weekend or holiday, is received by
  the next business day… Therefore, **after accounting for weekends and holidays, we preliminarily
  estimate that about 29% of the filings … were late**." (p. 178, n. 695)
- **Note for the spec:** the release does *not* cite a Compliance & Disclosure Interpretation for a
  "business-day practice" under the old rule. The mechanism it names is **Rule 0-3** and only Rule
  0-3. If the draft has been asserting a C&DI, that attribution needs a separate source — it is not
  in 33-11253. The proposal's own "ten calendar days ≈ seven business days" mapping (`model.tex:48-49`)
  is an **author calculation**, not a statement in the release.
- Related definitional change: "business day" in Regulation 13D-G is defined as "any day, other than
  Saturday, Sunday, or a Federal holiday, **from 12:00 a.m. to 11:59 p.m. Eastern Time**" — the
  Commission adopted a commenter's request for a full 24-hour day rather than the proposed 6 a.m.–10
  p.m. window (p. 37).

---

## 3. EDGAR filing cut-off change

- **5:30 p.m. ET → 10 p.m. ET**, for Schedules 13D and 13G and their amendments: the release amends
  Rule 13(a) of Regulation S-T "to permit Schedules 13D and 13G, and any amendments thereto, that are
  submitted by direct transmission **commencing on or before 10 p.m. Eastern Time** on a given
  business day to be deemed to have been filed on the same business day. This amendment should
  provide additional time for beneficial owners to prepare and submit their Schedule 13D or 13G
  filings." (p. 9)
- Summary-table row: Filing "Cut-Off" Time — Current 13D **5:30 p.m. ET** (Rule 13(a)(2) of Reg. S-T)
  → New 13D **10 p.m. ET** (Rule 13(a)(4)); same change for all 13G filers (p. 11).
- Also at p. 39 n. 137: "our amendment to Rule 13(a)(4) of Regulation S-T, which **extends the filing
  'cut-off' time for Schedules 13D and 13G from 5:30 p.m. Eastern Time to 10 p.m. Eastern Time**."
- **Why this matters to the design:** the cut-off change lands on **the same date** as the deadline
  change (2024-02-05). It shifts the *timestamp distribution within* the last day, so any
  filing-time or same-day-vs-next-day outcome is jointly treated. This is the "EDGAR cut-off"
  confound already on the referee checklist in `CONTEXT.md`, and the release is the citation for it.
- Hardship escape closed at the same time: the temporary hardship exemption in Rule 201(a) of Reg.
  S-T is made **unavailable** to Schedules 13D and 13G (p. 9 n. 19).

---

## 4. Filing-delay and accumulation statistics (the release's own numbers)

### 4.1 Delay distribution, initial Schedule 13D, calendar 2022 (Figure 1, discussed p. 178)

| Statistic | Value | Page |
|---|---|---|
| Filed within the existing 10-day window | **about 71%** | p. 178 |
| Filed **on** the filing deadline | **about 34%** | p. 178 |
| Filed on the 10th day after the trigger date | **20.7%** | p. 178 n. 696 |
| Filed **after** the tenth day | **approximately 42%** | p. 178 n. 695 |
| **Late** after applying Rule 0-3 (weekends/holidays) | **about 29%** | p. 178 n. 695 |
| Would already have met the new deadline | "**Approximately 29 percent** of the initial Schedule 13D filings [in 2022], representing about **41 percent** of all of the initial Schedule 13D filings that were filed by the current filing deadline, were filed within the amended five-business day deadline." | p. 178 (quoted again at p. 46 n. 166 and p. 193) |
| Implied: filings that must move earlier | "The final amendments may thus result in earlier filing for about **59 percent** of timely Schedule 13D reports." | p. 193 |

### 4.2 Median delay by filer type, initial 13D, 2022 (Table 1, p. 177)

| | Prominent Activists | Other Institutions | Other Individuals | All filings |
|---|---|---|---|---|
| Unique lead filers | 22 | 720 | 252 | 994 |
| Initial filings | 60 | 843 | 258 | 1,161 |
| **Median calendar days, trigger → filing** | **9** | **10** | **11** | **10** |
| Median ownership reported | 6.6% | 15.0% | 10.5% | 13.0% |

For contrast, initial **Schedule 13G** filings in 2022 (p. 190): 8,433 initial filings by 2,633 unique
lead filers; median calendar days trigger → filing **40 (QIIs) / 45 (Exempt) / 10 (Passive) / 39
(total)**; median ownership 6% / 15% / 6% / 7%.

### 4.3 Filing-type split and late rates, 2011–2021 (Table 2, p. 181)

| | Number | % of all | Prominent Activists | Other Institutions | Other Individuals | **Late** |
|---|---|---|---|---|---|---|
| **Non-corporate-action filings** | 3,067 | **20%** | 28% | 65% | 7% | **about 11%** |
| **Corporate-action filings** | 12,657 | **80%** | 3% | 67% | 30% | **about 34%** |

Non-corporate-action = filings from which a tabular transaction history could be extracted, "which we
view as more likely to involve activist campaigns" (p. 181). **This is the release's proxy for an
activist campaign and the population every accumulation statistic below is computed on.**

### 4.4 Accumulation completed by the new deadline (Table 3, p. 189 — non-corporate-action initial 13Ds, 2011–2021)

| Percent of stake accumulated by the amended (5-business-day) deadline | (1) 100% | (2) <100% | (3) <90% | (4) <75% |
|---|---|---|---|---|
| Number of campaigns in sample | 1,907 | 463 | 78 | 16 |
| **Percent of campaigns** | **80%** | **20%** | **3%** | **1%** |
| **Average number of campaigns / year** | **173** | **42** | **7** | **1** |

Columns 3 and 4 are **subsets** of column 2. Supporting text, p. 188: "about **97 percent** of the
filers completed acquiring 90 percent of their reported stake by the amended deadline, while the
remaining **three percent** … continued to accumulate shares constituting 10 percent or more of their
reported stake after the amended deadline… about **99 percent** of the filers completed acquiring 75
percent of their reported stake by the amended deadline, while the remaining **one percent** …
continued to accumulate shares representing 25 percent or more of their reported stake after that
date." Restated at p. 234 ("80 percent of campaigns were completed by the amended deadline, with 97
percent of campaigns having completed 90 percent of their stakes") and p. 238.

### 4.5 Campaign characteristics by degree of accumulation (Table 6, pp. 225–226)

| Row | (1) 100% | (2) <100% | (3) <90% | (4) <75% |
|---|---|---|---|---|
| (1) Avg. campaigns / year | 173 | 42 | 7 | 1 |
| (2) Avg. issuer market cap | **$916M** | $1.5B | **$1.8B** | $1.8B |
| (3) Avg. issuer turnover | 1.2% | 1.2% | 1.5% | 1.5% |
| (4) Avg. **Amihud illiquidity** | **0.13** | 0.11 | **0.09** | 0.08 |
| (5) % issuers in S&P 1500 | 9.7% | 14.3% | 15.6% | 12.5% |
| (6) % by a **Prominent Activist** | **29.8%** | 36.3% | **43.6%** | 56.3% |
| (7) Avg. beneficial ownership reported | 9.1% | 7.3% | 8.7% | 9.5% |
| (8) **Avg. % of reported stake accumulated *after* the amended deadline** | 0% | **5.9%** | 19.2% | 35.3% |
| (9) Avg. % of unrealized gains attributable to post-deadline shares | 0% | 4.1% | 9.1% | 22.6% |
| (10) **Avg. CAR, day −20 to +20 around the filing date** | **5.7%** | 8.1% | **17.2%** | 14.4% |
| (11) Avg. increase in shareholder value **per campaign** | **$36M** | $151M | **$222M** | $208M |
| (12) Avg. **aggregate** increase in shareholder value / year | $6.3B/yr | $6.3B/yr | $1.6B/yr | $302M/yr |

Sample: **2,370** non-corporate-action filings after excluding late filers, filings with no reported
ownership, and same-date duplicates (p. 224). Amihud is computed as in the Gantchev & Jotikasthira
(2018) study, over the **six months before the trigger date** (p. 225 n., p. 224 n. 817). Turnover is
average daily volume as a percent of shares outstanding over the same six months. **Row 10 is a
41-business-day window centred on the filing date — it is not a "filing window" return** (p. 224 n.
817 spells out the −20/+20 business-day construction and notes it differs from the calendar-day
Figures 7a/7b).

### 4.6 Wealth transfers to "informed bystanders" (Table 5, p. 210; discussion p. 211)

| Row | (1) 100% | (2) <100% | (3) <90% | (4) <75% |
|---|---|---|---|---|
| Avg. campaigns/year with potential transfers between amended deadline and filing date | 54 | 41 | 7 | 1 |
| Median abnormal return, amended deadline → day after filing | .5% | 1.9% | 3.1% | 6.9% |
| Avg. abnormal volume other than the filer's trades (% shares o/s) | .8% | .7% | 1.5% | 2.6% |
| Avg. transfers per campaign | $425K | $640K | $1.8M | $5.1M |
| **Aggregate transfers per year** | **$23M** | **$26M** | **$13M** | **$7M** |

Headline sentences (p. 211): the transfers "that could be avoided by shortening the filing deadline to
five business days if no filers forgo campaigns … is about **$49 million per year** ($23 million from
Column 1 plus $26 million from Column 2)"; **$42 million per year** if filers accumulating ≥25% after
the deadline forgo their campaigns; **$36 million per year** if filers accumulating ≥10% after the
deadline forgo theirs (n. 773). The Commission explicitly disclaims these as benefit estimates: "the
wealth transfer estimates in Table 5 **do not represent estimates of the benefit** of the final rule
amendments."

**These three numbers — $49M / $42M / $36M per year — are the only annualised "foregone value"
figures in the entire release.** A full inventory of every `$N million|billion` token in the 295 pages
returns no figure between $128 million and $1.5 billion. See §5.

---

## 5. Two things the release does NOT contain (checked, so nobody re-checks)

1. **There is no "$810 million" figure anywhere in Release 33-11253.** A regex sweep for `810`
   returns exactly two hits, both footnote numbers on p. 222. A full inventory of dollar amounts in
   the release yields: $100M, $6.3B/yr ×2, $49M ×2, $1.8B ×2, $916M, $7M ×2, $50M, $5.1M, $5M, $42M,
   $36M ×2, $302M/yr, $26M, $23M ×2, $222M, $208M, $151M, $13M ×2, $128M, $12M, $1.8M, $1.6B/yr,
   $1.5B — and nothing else. If the draft needs an annual foregone-value number sourced to the SEC,
   it is **$49 million** (or $42M / $36M under the adaptation assumptions), from Table 5.
2. **No Compliance & Disclosure Interpretation is cited for a business-day reading of the old
   ten-day rule.** The only mechanism named is **Rule 0-3** (pp. 46, 69 n. 268, 178 n. 695).

---

## 6. Useful qualifications the release volunteers (worth one sentence each in the spec)

- **Selling shareholders mostly gained.** "we acknowledge, as mentioned by commenters, that **most
  investors selling shares during the filing window seem to benefit** from the impending activist
  campaign" (p. 213). The "harm" framing is about trades with *informed bystanders*, never with the
  filer itself.
- **Accumulation is timed to institutional selling.** The release cites Gantchev & Jotikasthira
  (2018) for the finding "that the timing of Schedule 13D share accumulations is closely tied to
  institutional liquidity shocks, in that activist purchases closely track institutional sales at the
  daily frequency" (p. 212 n. 775) — i.e. the SEC's own record already contains the
  liquidity-timing channel.
- **Abnormal volume may not be bystanders.** "It is possible that the abnormal trading volume
  represents other traders' reactions to similar news, market conditions, and trends" (p. 212).
- **Pre-filing press releases are rare.** Staff full-text-searched 2021 initial 13Ds and found
  **three** filings where the filer disclosed the campaign by press release between trigger and
  filing date, none of which entered the Table 5 sample (p. 212 n. 774). Useful for ruling out a
  voluntary-disclosure confound.
- **Measurement caveat the Commission states about its own tail.** Of the filings in Table 6
  column 4 (<75%), manual review found **6%** would not have been categorised there had the
  ownership-extraction algorithm been as precise as the manual read (p. 224 n. 817). Every statistic
  in Table 6 "reflects data for at least 81% of the respective sample."
