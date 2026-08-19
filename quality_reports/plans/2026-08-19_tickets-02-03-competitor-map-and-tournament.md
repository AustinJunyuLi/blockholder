# Plan — Tickets 02 + 03: competitor map → positioning tournament (2026-08-19)

Status: APPROVED for ticket 02 only — Austin (2026-08-19): stop after ticket 02; ticket 03 will be run by a different agent (briefs in research/positions/ are hand-off material)

Doctrine: ADR-0005 — Fable orchestrates only; ≤12 agents/stage; finder ≠ verifier; verifiers refute
(WRONG / MISCITED / UNCHECKED); Opus reads/judges/synthesises, Sonnet searches/fetches/extracts.

## Ticket 02 — competitor map + whitespace
Stage A (parallel, 3 agents)
- S1 sonnet sweep A: Google Scholar + SSRN UI + NBER via ego-browser, 2024–26, queries logged → research/sweep_2024_26_A.md
- S2 sonnet sweep B: journal forthcoming/advance pages (JF, RFS, Econometrica, MS, JFQA, RoF, RAPS), ECGI WP series, arXiv q-fin → research/sweep_2024_26_B.md
- O1 opus builder: research/competitor_map.md from the 11 competitor cards (+ antecedent cards for refutation checks); table columns per ticket; whitespace section with refuter-card per item
Stage B
- DIRECT sweep hits → Opus reader (card) + Opus verifier; builder (SendMessage O1) adds rows
- V-map opus verifier: every row vs card/text; every whitespace item vs named refuter and a search over all cards
- fix in place; commit on v4

## Ticket 03 — tournament
Stage A: 5 Opus proposers, blind to each other, different tool/anchor families → research/positions/P1..P5.md (one-page brief per ticket)
Stage B: 3 Opus judges, blind, score all five on whitespace / fact-anchoring / provability of main result / deliverability by Dec / supervisor continuity → research/positions/JUDGE_1..3.md; Fable aggregates → winner, runner-up
Stage C: fresh Opus adversarial check of winner + runner-up against the cards (each whitespace claim: survives / amend); amendments by proposer, re-check by fresh verifier (≤2 rounds)
Stage D: plain-language brief for the author → research/positions/BRIEF_for_author.md; ticket 03 → ready-for-human; commit; PAUSE for the author's decision (ADR written after)

Verification: card/text-extract greps; map rows sourced; whitespace items each name the refuting card.
