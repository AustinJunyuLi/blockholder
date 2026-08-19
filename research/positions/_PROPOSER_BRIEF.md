# Proposer brief — Ticket 03 positioning tournament (2026-08-19)

You are ONE of several independent proposers. You do not see the other proposals. You are
assigned a tool/anchor family (in your prompt) and must build the best position you can from
inside it. Repo root: /Users/austinli/Projects/blockholder_v4.

## Read first (do not edit)
- CONTEXT.md (glossary — use its words), docs/adr/0001–0005, .scratch/v4-reposition/spec.md
- research/competitor_map.md (the verified map: competitor table, occupied cells, whitespace)
- research/cards/INDEX.md (§1 tables, §4 cross-cutting facts, hazards, whitespace quotes)
- research/draft_v2_digest.md (what the current paper is), research/empirical_feasibility.md
  (what data is on disk), research/cards/_institutional_sec_33_11253.md (the rule's facts)
- Any card in research/cards/ you lean on: open it and cite its section/page.

## Hard constraints (from the spec and ADRs)
- Identity must stay: liquidity × the disclosure rule as the market's partition × control
  outcomes (ADR-0004). Any draft_v2 component may be dropped.
- The position must sit in whitespace: name the competitor_map.md whitespace cell(s) it
  occupies and the row(s) it sidesteps. A cell rated NARROW/CONTESTED may be used only with
  the named card disposed of explicitly.
- The Feb-2024 acceleration earns no bonus for existing (ADR-0003); a calibrated/quantified
  empirical leg is acceptable; a causal design is preferred when one exists.
- Deliverability by December 2026 is a first-class criterion: no new data sources beyond
  the spec's caps (on-disk CRSP 2021–25, parsed 13D universe, EDGAR pipeline; WRDS pulls
  limited to CRSP/Compustat/13F/SDC < ~2 GB each; ≤ ~300 hand-collected offer prices),
  no coauthors, no continuous-time unless flagged as optional extension.
- Honesty labels: the main result is stated with the label you expect to earn
  (PROVED / NUMERICAL / CONJECTURE) and a proof route. Never overclaim.
- Never say "job-market paper"; never name a journal.

## Deliverable: ONE page (≤ 900 words) at research/positions/P<n>_<slug>.md with these
headings, in this order:
1. Object — the control outcome(s) studied, in one sentence.
2. Margin — which margin of the disclosure rule (threshold / window / partition / 13D-vs-13G),
   as LEVEL or CHANGE.
3. Anchor — the institutional fact the position rests on, with the card/page.
4. Main result to be proved — one statement; the tool; the proof route in 3–6 lines; the
   expected honesty label; the single biggest technical risk.
5. Empirical design — object, sample, identification, control group or bounded null,
   the confound list (EDGAR cut-off, anticipation, T+1, …), power/MDE sketch, placebo; what
   is run by December on data in hand and what is only specified.
6. What is new vs the competitor map — the whitespace cell(s) occupied (quote the map's
   rating), the nearest rows and why each does not occupy it (card + page).
7. Deliverability by December — weeks of work per piece; what could fail; fallback.
8. Supervisor continuity — what a reader of draft_v2 recognises; what is dropped and why.
9. Self-assessed weakest point — one paragraph, honest.

## Rules
- Every factual claim about a paper cites a card (file + section/page). No memory.
- Do not read other proposers' files. Do not edit anything but your own file. No commit.
- Stop when the page is written (~30–40 turns).

## Return (≤ 12 lines)
File path; object · margin · anchor · tool; the main result in one sentence with its
expected label; the whitespace cell(s) claimed; your own deliverability verdict.
