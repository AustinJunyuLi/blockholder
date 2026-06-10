# Bloomberg Terminal Inventory Checklist (decision-report open item 2d)

**For the author, at the terminal.** Goal: confirm what the terminal can deliver for the structural leg before committing it (9–24mo). Tick each line and note export caps.

## Ownership / filings
- [ ] `OWN` / `HDS` — holder history for a sample target: how far back, point-in-time?
- [ ] `13F` / filing functions — can you pull *13D/G filing histories* (filer-level campaign lists), or only current holders?
- [ ] `CACS` — corporate-action history export (for event-study adjustments).
- [ ] Activist-specific screens (e.g., `SI` / `ACT` activism screens if licensed): campaign lists with dates?

## M&A / premia
- [ ] `MA <GO>` — deal database: announced/completed, premia fields (1-day, 1-week, 4-week), bidder type (strategic vs financial — the γ proxy from D7), toehold field?
- [ ] Export caps: rows per pull, monthly download quota; can MA results be exported with deal premia + acquirer classification?

## Market data
- [ ] Daily price/volume history depth for delisted names (survivorship)?
- [ ] Tick/intraday history (`QR` / Data License): export limits — needed only if Amihud from daily is insufficient.
- [ ] Amihud illiquidity ingredients: daily |ret|/volume exportable in bulk?

## Practical
- [ ] Excel API (`BDH`/`BDS`) bulk limits per day.
- [ ] Terms-of-use: can extracted premia/ownership series be used in a published academic paper (cite policy)?

**Decision input:** if MA premia + acquirer-type + ownership history export cleanly, Bloomberg substitutes for SDC and (partly) for CRSP in Fact 2's fallback; if caps are tight, WRDS/CRSP is the primary and Bloomberg is validation only.
