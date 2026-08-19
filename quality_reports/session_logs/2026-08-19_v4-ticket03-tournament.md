# Session log — 2026-08-19 — v4 ticket 03: positioning tournament

## What happened

Ticket 03 (`.scratch/v4-reposition/issues/03-positioning-tournament.md`) executed end-to-end:
five independent position proposals, three independent judges, adversarial checks of both
finalists against the cards, and a plain-language author brief. Ticket flips to
`ready-for-human`; the author decides among P2 / P4 / the package.

## Team and routing (author override of ADR-0005)

- Session model orchestrated only. Hands: **5 proposers + 3 judges on Kimi-K3-max**;
  **2 adversarial checkers + 1 brief writer on Grok-4.6-xhigh-fast** ("quick jobs").
- Environment finding (recorded for future routing): the only genuine Kimi subagent
  configuration exposed is `kimi-k3-max`. `kimi-k3-high/medium/low` are rejected; unknown
  `-fast` Kimi slugs were silently fallen back to Composer 2.5 fast (caught by the author,
  who then banned Composer). `cursor-grok-4.6-xhigh-fast` resolves and was used without
  incident.

## Artifacts (all under `research/positions/`)

- Proposals: `P1_window_premium_tendergame.md` (W1+W12), `P2_partition_infodesign.md`
  (W3, +W11), `P3_kyle_deadline.md` (W5+W6), `P4_feb2024_did.md` (W2, fallback W13),
  `P5_purpose_partition_13d13g.md` (W7).
- Judge reports: `JUDGE_1.md`, `JUDGE_2.md`, `JUDGE_3.md` (score tables, reasons,
  refuted-claim lists).
- Adversarial reports: `ADVERSARIAL_P2.md`, `ADVERSARIAL_P4.md` (claim-by-claim tables).
- Author brief: `AUTHOR_BRIEF.md`.

## Outcome

- **Winner: P2** — the disclosure rule as the market's rule-keyed partition (W3, CLEAR);
  first-place votes from Judges 1 and 2, Borda 14, raw total 79/90. Main result: flagged
  cell κ-invariant, pooled cell carries the premium's entire κ-derivative; PROVED at fixed
  cutoffs, region-certified PROVED in GE, NUMERICAL off-region.
- **Runner-up: P4** — Feb-2024 window change × control outcome × matched never-13D DiD
  (W2, CLEAR on occupancy / hard on execution); highest raw total 81/90, Judge 3's winner.
- Both finalists **survived adversarial checking with amendments** (P2: 3; P4: 5). No
  whitespace claim was refuted.
- Judges converged on a third option the brief presents honestly: **P2's model + P4's
  empirics** (Judge 3: P2 and P3 near-identical; "the natural package").
- Orchestrator error caught by the brief writer and corrected in the record: P4 was
  top-two for J2/J3 but third for J1 — not "unanimous top-two".

## Open hazards (author owns)

- Payne-Mann, Stice-Lawrence & Wong (SSRN 5076900) PDF — walled; decides whether P5's
  cell (W7) is open.
- Burkart–Lee–Van-Schepdechen Dec-2025 revision — unobtained; live risk on the wedge.
- Zeng IA Table 2 — size split not yet checked against the appendix.

## Next

Author reads `research/positions/AUTHOR_BRIEF.md` and decides: P2, P4, or the package.
Decision is recorded in the ticket comments + a new ADR (last checkbox), then ticket 04
(clean core model) starts from the chosen position; the theory-ambition checkpoint
(spec user story 7) follows.
