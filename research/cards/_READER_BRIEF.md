# Reader brief — Ticket 01 literature cards (2026-08-19)

You are one reader in a team producing verified literature cards for a theory-plus-empirics
finance paper. Repo root: /Users/austinli/Projects/blockholder_v4.

## What our paper is (context only — do not edit it)
A single large shareholder (the "blockholder") with a private signal trades in a market with
noise trading of intensity κ (liquidity), and may engage the firm. A legal disclosure rule
(US Schedule 13D: 5% stake threshold + a filing window, 10 → 5 business days from
2024-02-05) forces public revelation of a stake and its purpose. We study how liquidity and
the disclosure rule shape *control outcomes* (bidder entry, takeover premium, activism
success). Vocabulary: read `CONTEXT.md` (glossary) before writing — use its words
(position, whitespace, competitor set, anchor, threshold margin, window margin, partition,
premium wedge, honesty label). Draft_v2 background if you need it: `research/draft_v2_digest.md`.

## Your job
Read the FULL TEXT of each assigned paper — every page, including appendices — and write one
card per paper to `research/cards/<slug>.md`, following `research/cards/_TEMPLATE.md`
section by section (keep all nine headings). Never work from the abstract or from memory.
The text files are 80–240 KB; read them completely in chunks (Read tool with offset/limit,
or `sed -n`). If a text file lacks page markers, re-extract from the PDF with
`pdftotext -layout <pdf> <newtxt>` (form-feed `\f` separates pages) or per page with
`pdftotext -f N -l N -layout <pdf> -`, so that every quote and result carries a page.

## Rules
- Honesty labels on every result: PROVED (analytical proposition with proof), NUMERICAL
  (shown on a grid/simulation only), ESTIMATED (point estimate with SE/CI), ASSERTED
  (claimed in text without proof or estimate). Do not upgrade a label to make a paper look stronger.
- Quotes verbatim, character for character, 5–12 per card, each with a page number. State
  in the header which page numbering you use (printed journal page of the version named
  under "Full text from", or PDF page index if the version has no printed numbers).
- Section 6 (scope boundary) and section 7 (implications) are the ones the positioning
  stage will lean on hardest: be exact about which OBJECT (e.g. announcement return,
  takeover premium, campaign success), which MARGIN of the disclosure rule (threshold level,
  filing window, none), and which IDENTIFICATION (structural, DiD, event study, theory only)
  the paper occupies — and quote the paper where it declares something out of scope.
- Numbers: report sample sizes, periods, coefficients, standard errors, and grid ranges as
  printed. Do not round beyond the paper's precision.
- Premise you act on: the file paths you were given hold the full text. If a file is missing,
  truncated, image-only, or is a different paper/version than named, say so in your return
  message and stop for that paper — do not substitute another source.
- Do NOT edit any file other than your own cards. Do not commit. Do not read other agents' cards.
- Stop when your cards are written; ~25 turns per paper is plenty.

## Return message (≤ 20 lines, plain text)
For each paper: card path; version read (venue/WP series, date); pages read; page-numbering
convention; anything you could not read; the ONE sentence you would put in an index line
("venue/status · object · margin · identification · so-what").
