# Link-map defect and repair — the NaN-ticker collision (2026-08-30, evening)

Dated note under §0 rule 1. **No SPEC object changes.** This records a defect in
a committed unit (`906128b`, the CIK↔PERMNO link rebuild), its repair, and the
consequence the repair exposes — which is a decision for Austin, not for this
session.

## 1. The defect

`empirics/link_cik_cusip.py`'s `norm_ticker` normalised a missing CRSP ticker to
the string `"NAN"`:

- CRSP blanks `Ticker` when a security delists;
- pandas reads a blank as float `NaN`;
- `str(nan).upper().strip()` is `"NAN"`;
- **NAN is a real NYSE ticker** — Nuveen New York Quality Municipal Income Fund,
  CIK 1074769.

So every delisted PERMNO with no ticker matched that fund's ticker, passed the
"no still-listed PERMNO claims this ticker" guard (none does — the fund is a
delisted-ticker check, not a live one, and NAN's own PERMNO is a separate row),
and was written out with CIK 1074769 under route `ticker_delisted`.

**1,607 of the 5,443 common-US PERMNOs carried that CIK** — 1,607 of the 1,607
delisted ones, i.e. all of them. In `permno_cik_map.csv` as committed, one CIK
served 1,607 PERMNOs while the next-largest served 2.

The bug was silent in the worst way. It *raised* the reported link rate (95.7%
of delisted PERMNOs "mapped"), and the build's own survivorship warning —
already written, and correct in spirit — printed the reassuring branch.

**How it surfaced.** Not by looking for it. The stage-M smoke run reported 1,122
control PERMNOs with a blank SIC in EDGAR. The first reading was that these were
closed-end funds and trusts, and that excluding them was the exact-SIC match
doing the universe screen's job. That reading was wrong, and it was wrong in a
comfortable direction. CRSP classifies the same 1,122 as `IssuerType` CORP or
REIT with `SecuritySubType` COM: ordinary corporations. They looked like one
fund because they *were pointed at* one fund. Checking the CRSP classification
against the EDGAR one is what broke it open.

## 2. The repair

`norm_ticker` now returns `""` for any missing value (`None`, float NaN, numpy
NaN, `pd.NA`) before the regex runs. The literal ticker string `"nan"` still
normalises to `"NAN"`, so the firm that genuinely trades as NAN keeps its CIK:
the guard keys on the missing value, not on the letters.

`empirics/test_link_cik_cusip.py` (19 checks) covers the repair, the reuse
guard, ambiguous tickers, and one check that no CIK absorbs a crowd of PERMNOs —
the shape of the failure, not just its instance.

`--reverse-map-only` was added to the link build so the map could be rebuilt
from files already on disk while two extraction lanes held the SEC lock. It does
no fetching and takes no lock; a full run reproduces the same file.

**The rebuilt map differs from the committed one on exactly 1,607 rows**, every
one of them a `ticker_delisted` → `no_edgar_ticker` flip losing CIK 1074769. No
row gained or altered a CIK. Every identity column is unchanged.

| | before | after |
|---|---|---|
| PERMNOs mapped to a CIK | 5,212 (95.8%) | 3,605 (66.2%) |
| routes | ticker 3,605 · ticker_delisted 1,607 | ticker 3,605 · no_edgar_ticker 1,835 · ambiguous_ticker 3 |
| delisted PERMNOs carrying a CIK | 1,607 | **0** |
| control-universe PERMNOs linked | 3,464 | 2,344 |
| control-universe PERMNOs with a usable SIC | 752 of 3,464 linked, 1,122 blank | 752 of 2,344 linked, **2** blank (1,590 still awaiting their submissions fetch) |

The blank-SIC finding of the earlier session-log entry therefore **dissolves**:
it was an artefact of this bug, not a property of the control universe. Blank
SIC collapses from 1,122 to 2.

## 3. What the repair does *not* change

- **Control-universe membership is unchanged.** CIK 1074769 is not among the
  2,735 13D subject CIKs, so exclusion route E6 (reverse map ∩ subject CIKs)
  never excluded a PERMNO *because of* the bogus link. The 3,600-PERMNO universe
  in `never13d_control_universe.csv` stands as built.
- **No running process needs restarting.** Both extraction lanes loaded their
  CIK lists at startup, and the chain reads `fact2_parsed.jsonl`, not this map.
  The control lane's list loses exactly one CIK (the Nuveen fund) on a future
  run; nothing already fetched is wasted.
- **The treated side is untouched.** Treated firms link through 13D cover-page
  CUSIPs and the header CIK, not through this reverse map.

## 4. The consequence — reported, not resolved (for Austin)

**No delisted control firm can be coded for BID12 any more.** All 1,120 delisted
PERMNOs in the control universe are now unlinked, so they carry no CIK, so the
coder has no filings to read for them.

Before the repair they were not really coded either — they were coded from a
municipal bond fund's filings, which is worse. The repair converts 1,120 silent
wrong zeros into 1,120 honest missings. That is strictly better, and it makes
the design problem visible instead of burying it in the control rate.

The design problem is survivorship, and it is asymmetric:

- the **treated** sample keeps its delisted firms (CUSIP-linked), and a delisted
  13D target is very often a target that was *acquired*;
- the **control** sample now keeps only survivors, and a control that was
  acquired inside its window delisted and is therefore absent.

A control group conditioned on survival under-counts exactly the outcome BID12
measures. The control bid rate biases **down**, and γ (the Treat level effect,
Greenwood–Schor's 11 pp analogue) biases **up**. β, the reform effect, is
affected only if the asymmetry differs pre/post — which it may, since the post
window is shorter and gives less time to delist.

**Options, none taken here.**

1. Report the leg with the survivorship asymmetry stated and signed, as SPEC
   §8.5 row x already does for delisting. Cheapest, and consistent with how the
   amendment-orphan caveat is handled.
2. Recover the delisted controls with a CUSIP→CIK route that does not depend on
   current tickers. **Costed, not built** — see §5. Cheaper than it sounds.
3. Restrict both sides to survivors, which trades the asymmetry for a bias of
   known direction on both sides but throws away the acquired treated firms that
   §2.3 filter 3 was written to keep.

This belongs beside the amendment-orphan caveat (SPEC §8.2) as a live limitation
of the control group.

## 5. Costing the recovery route (measured 2026-08-30, not built)

Two cheaper routes were tested first and one of them is dead, which is worth
recording so nobody re-tries it.

**Dead: the historical-ticker route.** CRSP carries ticker *history*, and the
map used only each PERMNO's last row, which delisting blanks. Rebuilding from
the last **non-blank** ticker in `crsp.ticker_spans` recovers **110 of 1,607**
delisted PERMNOs. The rest fail for a structural reason, not a fixable one:
`company_tickers.json` lists **current** registrants only, so 1,463 delisted
tickers are simply absent from it and 34 now belong to a live security. Any
ticker-based route fails for delisted firms by construction. There is also no
name route inside the repo: the CRSP daily snapshot carries no company name
column, and neither WRDS extract does.

**Viable: CUSIP → issuer name → CIK, through 13F holdings.** A 13F information
table lists `cusip` beside `nameOfIssuer`, and the quarterly EDGAR indexes
already on disk give company name → CIK for every filer 2021–2025, delisted
firms included. Measured on **one** filing (Geode Capital Management, 2023Q1,
`0001214717-23-000010`, 2.7 MB, 4,803 distinct CUSIPs):

| step | count | of |
|---|---|---|
| delisted control PERMNOs | 1,120 | — |
| CUSIP present in that single 13F | 370 | 33.0% |
| of those, name resolves to exactly one CIK in the on-disk indexes | 261 | 70.5% |
| name matched more than one CIK | 15 | 4.1% |
| name absent from the indexes (13F abbreviations such as "10X CAPITAL VENTURE ACQUIS-A") | 94 | 25.4% |

The 33% CUSIP ceiling is an artefact of using one quarter: a 2023Q1 holdings
table cannot contain a firm that delisted in 2021, and 447 of the 1,120
delisted before 2023. One 13F per year from the same filer (five filings, about
14 MB, five requests) should lift CUSIP coverage well above that, and the
name→CIK step is local.

**So the realistic cost is minutes of lane time, not a new data project:** five
13F fetches, local name matching, and one submissions fetch per recovered CIK
to validate (many are already cached). The validation rule writes itself: a
recovered CIK whose filings continue well past the CRSP delisting date is the
wrong company, and the 15 ambiguous names are held out rather than guessed.

**Still not built, and not a decision this session may take.** It would add a
linkage route the SPEC's control universe was not built on, and it needs its own
gate before any control it recovers enters the sample. What changes with this
measurement is only Austin's menu: option 2 is cheap, not expensive, and worth
weighing against simply signing the survivorship bias in the text.
