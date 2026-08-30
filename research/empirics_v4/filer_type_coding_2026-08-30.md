# Filer-type hand coding (activist_hf / corporate / other) — 2026-08-30

Hand-check component of the filer-type control in SPEC.md §6 (triple-interaction with
filer-type dummy, "activist HF / corporate / other, from filer-name coding, §11 row 16").
Output: `empirics/output/filer_type_overrides.csv` (exactly the columns
`filer_cik, filer_name, filer_type, n_filings`).

## What was coded

- Source: `empirics/data/fact2_parsed.jsonl` (re-parsed 2026-08-30 parser), 4,639 initial
  SC 13D filings, 2022–2025, 3,503 unique filer CIKs.
- Unit: **filer_cik**, filings counted as rows in the jsonl (one row per initial 13D).
  Name shown is each CIK's modal (most frequent) `filer_name` — a few CIKs appear under
  variant names (e.g., BitNile 5 of 7 rows, Brookfield 3 of 5).
- Selection: top 200 CIKs by filing count. 188 filers have n ≥ 3; the n = 2 pool has 273
  filers, so the last 12 slots depend on the tie-break. **Tie-break: ascending CIK**
  (arbitrary but deterministic and reproducible; affects only n = 2 filers). Consequence:
  the n = 2 tail is old-CIK filers (Pfizer, Walmart, Eli Lilly, Mitsui, Loews, Hecla,
  Continental General Insurance, FMR, Barings, TCW, Danske Bank, Ameriprise). Note that
  some tied n = 2 filers that fall outside the cut (e.g., Ancora Advisors, B. Riley
  Financial, Funicular Fund LP) are therefore *not* in the overrides file; any filer not
  in this CSV falls back to the regex rule of the spec, and name-based regexes ("ancora",
  "b. riley", "funicular") should catch them.
- Top-200 filers account for 1,075 of 4,639 filings (23%).

## Distribution

| filer_type | filers | filings | filings share (within top 200) |
|---|---|---|---|
| activist_hf | 65 | 529 | 49.2% |
| corporate | 25 | 82 | 7.6% |
| other | 110 | 464 | 43.2% |
| total | 200 | 1,075 | 100% |

Unweighted by construction (filers): 32.5% activist_hf, 12.5% corporate, 55% other.

## Coding rules used (what was mechanical vs judgment)

Mechanical (rule, applied uniformly):

1. **Individuals** (filer_name is a person, e.g., "Radoff Bradley Louis", "Amster Howard")
   → `other`, *except* individuals who are documented activist investors in their own
   right (Icahn, Stilwell, Radoff) → `activist_hf`.
2. **Banks / custodians / credit unions** (Standard Bank of South Africa, Bank of
   America, JPMorgan, Wells Fargo, Toronto Dominion Investments, Danske Bank, Partner
   Colorado Credit Union) → `other`. Their 13Ds plausibly reflect market-making or
   facilitation, not strategy — spec puts banks in "other".
3. **Pensions / sovereign wealth / state agencies** (OPERS, STRS Ohio, USS, ADIA, QIA,
   Mubadala, Investissement Quebec) → `other`.
4. **Index / traditional long-only asset managers** (BlackRock ×2, Franklin, FMR,
   Ameriprise, Capital World Investors, Neuberger, PIMCO/PGIM, M&G, Royal London AM,
   NY Life IM, Invesco Realty, TCW, Barings, SIT, CI Investments, Bleichroeder,
   Gardner Lewis, Carlyle, Eagle Point Credit) → `other`.
5. **PE / VC / growth funds and their GP/SPV vehicles** (General Atlantic, TPG GP A,
   Blackstone Holdings, Apollo entities, SC US (TTGP) = SoftBank Vision Fund vehicle,
   Atlas Venture X/XI, ARCH XII, 5AM VI, NEA-style funds, Morningside, SR One, Longitude,
   Castle Creek, Patriot Financial, Fairmount Funds, Liberty 77 (Mnuchin's Liberty
   Strategic Capital), Kennedy Lewis) → `other`. Per instructions, "corporate" is
   reserved for operating/strategic parents; standalone financial funds and anonymous
   SPVs/shells go to `other`.
6. **Operating companies / strategic parents** (incl. their holding arms and
   insurer-operating companies) → `corporate`.
7. **Conservative default**: whenever genuinely uncertain between activist_hf and other,
   coded `other`. This is the pre-specified tie-breaker; it biases against false
   positives in the activist_hf cell.

Judgment (knowledge-based, spot-verified): well-known activist funds and hedge funds
were coded `activist_hf from entity recognition, following the spec's inclusion of
"generic multi-strategy HFs with activist 13D filings" (so Magnetar, Farallon, Davidson
Kempner, Angelo Gordon, Highbridge, Viking, D. E. Shaw, Adage, Whitebox, Mudrick count
even where their 13Ds are position-driven rather than campaign-driven). About 20
unfamiliar or ambiguous names were verified against public sources (SEC filings,
Fintel/WhaleWisdom profiles, press) on 2026-08-30; verified cases are noted below.

## Example classifications

Activist HF:
- Saba Capital Management, L.P. (101 filings) — Boaz Weinstein; the dominant CEF activist filer.
- Starboard Value LP (16) — named in spec as archetype activist.
- Galloway Capital Partners, LLC (16) — Bruce Galloway, Miami small-cap activist; investment manager of Galloway Capital LP (verified).
- Funicular Funds, LP (7) — vehicle of Cable Car Capital (Jacob Ma-Weaver); 13Ds on Synlogic etc. (verified).
- Hoak Public Equities, LP (5) — Hoak family partnership; NGS board campaign 2023 (verified).
- Camac Fund, LP (3) — Eric Shahinian; activist positions incl. Cryo-Cell, Forte Bio (verified).
- BML Investment Partners, L.P. (11) — BML Capital Management; all 14 of its tracked positions are 13D activist positions (verified).
- ICAHN CARL C (7) — individual exception: canonical activist.
- Ancora-type funds — see note on tie-break above (Ancora itself fell outside the n=2 cut).

Corporate:
- Uber Technologies, Inc (4) — operating company holding strategic minority stakes.
- GSK PLC (3) — pharma operating parent (e.g., Haleon spin-off stake).
- Tether Holdings, S.A. de C.V. (5) — stablecoin operating company investing strategically.
- Star Equity Fund, LP (4) — judgment: fund is wholly owned by operating company Star Equity Holdings; campaigns read strategic (tender offer for GEE Group).
- Walmart Inc. (2), Eli Lilly & Co (2), Mitsui & Co Ltd (2), NextEra Energy Inc (3) — unambiguous operating-company filers.

Individual person (coded `other` per rule):
- Amster Howard (7 filings) — individual investor; the single largest all-"other" individual filer.
- HELU CARLOS SLIM (3) — individual; strategic acquirer but not an HF, conservative rule → other.
- MALONE JOHN C (7) — individual (Liberty chairman); strategic individual, conservative rule → other.
- EBRAHIMI FARHAD FRED (7), Lazar David E. (5), ROBOTTI ROBERT (3) — serial micro-cap 13D filers as individuals; conservative rule → other despite activist-looking behavior.

Other (institutional):
- Universities Superannuation Scheme Ltd (7) — UK pension trustee.
- Abu Dhabi Investment Authority (5) — sovereign wealth fund.
- Sotirios Vahaviolos ... GRAT (3) — estate/Trust planning vehicle.
- TORO 18 HOLDINGS LLC (3), VNV (Cyprus) Ltd (3) — anonymous holding shells → other, not corporate.

## Names I could not confidently classify (coded, with choice)

Coded `other` (conservative default):
- Baker Bros. Advisors LP (10) — healthcare manager famous for passive long-term stakes; not campaign activists.
- Eagle Point Credit Management LLC (5) — credit/CEF income manager (verified: 20% OXLC preferred 13D is position-taking, not a governance campaign shop).
- Lynrock Lake LP (4) — investment manager of a master fund with large concentrated stakes (17.9% RADCOM); HF vs family office unclear.
- Kennedy Lewis Management LP (3) — private-credit/special-sits manager; filings likely credit-conversion.
- Philotimo Fund, LP (5), Forager Fund, L.P. (3), Altai Capital Management (3), Gate City Capital Management (3), Two Seas Capital LP (3), F9 Investments LLC (3), Maven Investment Partners US Ltd (3), FiveT Investment Management Ltd (3), Flawless Management Inc. (3), Anglo Irish Management LLC (3), GK Partners ApS (3), Abra Marinvest Inc. (3), Phoenix Holdings Ltd. (3), DJ Fund Investments LLC Series E (4), Value Base Ltd. (4), Diveroli Investment Group LLC (4), APO Corp. (3), Panacea Innovation Ltd (3), Lucky Dog Holdings (3), Growth Equity Opportunities 18 VGE (3), VA Partners I (3), Bellevue/Bond/Stephens-type n=2 ties outside cut — unidentifiable or plausibly SPV/family vehicles.
- Oriental Moon Tree Ltd (5) — verified pre-IPO 70% controlling holder of Garden Stage; anonymous HK shell. Plausibly "corporate" (strategic promoter), but per SPV rule → other.
- Cincinnati Cornerstone Investors BWV I, LLC (5) — target-named SPV (>10% of Blue Water Vaccines) → other.
- Fairmount Funds Management LLC (7) — verified long-only healthcare crossover (founder-operator model), not an HF → other.

Coded `activist_hf` on moderate-confidence judgment (flagged):
- 325 Capital LLC (6), Scopia Capital Management (3), Sylebra Capital (4), Adage Capital (3), Viking Global (3), Highbridge (3) — fund/manager identity is HF-type; degree of campaign activism unverified.
- Healthcare-dedicated managers grouped with activist HFs by analogy to OrbiMed/RA/Perceptive: Samsara BioCapital (10), RTW Investments (4), Velan (5, verified), Glendon (3, verified distressed special-sits with board rights), EcoR1 (4), BVF (6).
- Juniper Investment Company, LLC (6) — Michas-family active manager with engaged 13Ds (verified: Allient/Artivion).

Corporate judgment calls: Steel Partners Holdings L.P. (operating holding co despite activist
lineage), Investissement Quebec (state agency — coded `other`, SWF-like, not an operating
parent), B. Riley Asset Management (asset-management arm → `other`) vs B. Riley Financial
(operating parent → corporate, but outside tie-break cut), Continental General Insurance
and Equitable Holdings (insurer operating companies → corporate).

## Reproducibility

- Script (one-off, run 2026-08-30): counts rows per `filer_cik` in fact2_parsed.jsonl,
  modal name per CIK, sorts by (-n_filings, int(filer_cik)), applies the CIK-keyed
  hand coding above, writes the CSV sorted the same way. `filer_cik` written as plain
  integer string (no zero padding).
- This is an **overrides** file for the top 200 only; all remaining 3,303 filers get the
  spec's regex coding. The regression control should be: regex rule, then override by
  CIK where this CSV matches.
