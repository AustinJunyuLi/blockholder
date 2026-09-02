# Spec: the v5 paper in one session

Read `CLAUDE.md` and `CONTEXT.md` first. This file is the plan for the session that delivers
`paper.tex`, `appendix.tex`, and the two PDFs in `deliverable/`. It is self-contained. Nothing
outside this worktree is consulted.

## 1. Deliverable

A finished paper titled *Who Gets Caught: Disclosure Rules, Liquidity and the Undetected
Blockholder* (retitled by ticket 16; the delivered checkpoint-3 paper carries the earlier title),
compiled clean, referee-reviewed once, fixed once, unslop-gated, with every theorem passed
through the attack gate on v5 and every number rendered from a result file. Slides are not
part of this session.

## 2. Headline

Amended 2026-09-02 for batch 4 (ticket 16, superseding 15). A disclosure rule has two dials. The
stake threshold τ and the filing clock T split every blockholder history into a flagged cell (the
filing landed; the market knows the blockholder is engaged and the filing tuple identifies her
signal) and a pooled cell (no filing; the market reads order flow). At fixed policies the
engagement premium equals the premium wedge times the probability that a bidder enters against an
engaged blockholder, and the Voice mass is free of liquidity and of the rule, so every effect in
the paper runs through bidder entry conditional on engagement. Entry is higher when the market has
not yet detected her. The filing and the trading tape are the market's two ways of detecting her:
on the tape at order size two an engaged blockholder is either fully detected by one revealed
building mark or silent, and a type with n building rounds is silent with probability (κ/2)^n; the
rule catches the fast builders, who place the fewest orders, so the two technologies catch opposite
blockholders. The pooled premium therefore rises with liquidity, strictly above a root below 0.15
at every node on the calibration, and a disclosure rule's effect on the premium level grows with
liquidity, from under one percent in thin markets to the record's share in liquid ones.

The second half of the paper is ticket 15's contrast, kept in full: tightening either dial is a
Blackwell improvement of the market's control-node experiment; that order does not settle what
liquidity does to prices; for either dial the tighter rule lowers the liquidity sensitivity of the
engagement premium exactly when the net cut leg lies in a band set by the pool's own sensitivity
and the share removed; the band holds on the whole grid and fails on an open interval below it,
reported as a remark with its magnitudes. The mechanism is inference from silence: the histories
that stay pooled are re-priced because the absence of a filing now says more, and on the record the
re-pricing term is 93 to 98 percent of the clock's net cut leg at every node. Order size two is
the unique integral order size whose order-mark channel is an exact, non-trivial erasure family in
liquidity, and the benchmark policy's interim regret bound is reported at every node.

The headline this replaces (tightening lowers noise sensitivity through the weight effect by
proof and the composition effect on the grid; the clock does so iff its composition ratio is at
most one, characterised by who gets caught) stays true and stays in the paper inside the second
half.

## 3. The model, as the paper states it

The inherited multi-date structure, H = 10 trading dates, one change. The engaged blockholder's order
while building the stake is two noise lumps (ADR 0003). The noise trader trades one lump up or
down with probability κ/2 each and sits out with probability 1 minus κ. Order flow takes five
values; only the value plus one is ambiguous between "blockholder bought, noise sold" and
"blockholder idle, noise bought". Everything else in the model (plans, the Voice and Exit menu,
the bidder, the pricing rule, the calibration) is inherited unchanged and restated in the
paper's own words.

Results the paper carries, each with a label at delivery:

| Tag | Statement | Route | Ticket |
|---|---|---|---|
| Partition and factorisation | The rule partitions histories; S = (1 minus Ω) times S_P | Inherited proof, transcribed and attacked on v5 | 04 |
| Flagged cell is κ-free | The flagged endpoint does not depend on κ | Inherited proof, transcribed and attacked on v5 | 04 |
| Garbling lemma (new) | At order size two, the pooled experiment at higher κ is a garbling of that at lower κ; the pooled expectation of any convex (concave) kernel is monotone in κ | New proof | 02 |
| Threshold dial | At fixed policies a tighter threshold weakly lowers noise sensitivity | Factorisation and weight leg proved; the closed form of S_P in κ proved; the composition leg is Condition D, equivalent to the composition ratio being at most one, verified on the grid (NUMERICAL, κ in [0.15, 0.85]) | 02 |
| Clock dial | At fixed policies a shorter clock lowers noise sensitivity iff W_T times C_T is at most one | Inherited proof, transcribed and attacked on v5 | 04 |
| Who gets caught (new) | C_T is at most one iff the sensitivity of what the shorter clock removes lies weakly between the pool's and (2 minus φ)/φ times it; the paper gives the identity behind it | New proof plus a grid check | 03 |
| Blackwell improvement (batch 4) | Tightening either dial at common κ and fixed policies is a Blackwell improvement of the control-node experiment, under the noise channel and the flagged-tuple decoder; strict on the threshold ladder at T = 5, equivalent at the null T = 10 threshold cuts | New proof from the hunt memo, attacked on v5 | 15 |
| Erasure regime (batch 4) | Order size two is the unique integral order size whose binary order-mark channel is an exact non-trivial erasure family in κ; at one the higher-κ experiment is never a garbling of the lower; three and above decode the mark | New proof from the hunt memo, attacked on v5 | 15 |
| Cut identity, one-crossing lemma and reversal (batch 4) | The who-gets-caught corollary holds at the threshold margin with the clock sets replaced; the net cut leg splits into a caught-only leg and a re-pricing term; one sign change in each pool's coefficients decides the band above a computable cutoff; one crossing at both pools with distinct roots gives a strict reversal of total sensitivity on an open interval around the looser pool's root | Restatement plus three lemmas, attacked on v5; sign lists, intervals, magnitudes and the split NUMERICAL from the cut record | 15 |
| Benchmark regret (batch 4) | Certified upper bound on the largest one-step deviation gain at benchmark prices and beliefs over the computational signal support, at every node | NUMERICAL from a regret record with the convention and a normaliser | 15 |
| Entry identity (batch 4) | The engagement premium is Δm times the Voice mass times bidder entry conditional on engagement, per cell too; the Voice mass is κ-free and rule-free at fixed policies | New one-line proof, attacked on v5 | 16 |
| Detection lemma (batch 4) | At order size two a revealed building mark sets the engagement posterior to one; an engaged type with n building rounds is silent with probability (κ/2)^n | New proof under the noise channel and the menu's mark form, attacked on v5 | 16 |
| Upper set and silence (batch 4) | The flagged set is an upper set in the signal made of the types with the fewest building rounds; on every history that stays pooled the tighter rule lowers the engagement posterior and the fundamental posterior | New proofs under the menu's monotone form, attacked on v5; silence lemma absent if it fails | 16 |
| Entry against the undetected (batch 4) | At the pricing root the price rises in the engagement and fundamental posteriors, so entry falls in both | New proof, attacked on v5; absent if it fails, the entry gap then NUMERICAL | 16 |
| Monotone premium and levels (batch 4) | The pooled premium is strictly increasing in κ above a root below 0.15 at every node; entry by detection state, the silent mass, the level effects of both dials, the level cut split | NUMERICAL from the one-crossing lemma on the record's coefficients and from the detection record, T in {3, 5, 10} | 16 |

The general-equilibrium dominance result is not in the paper. Nothing in the paper says so.

## 4. The empirics, as registered

`empirics/spec.md` is the registered document. Two exercises on all initial Schedule 13D
filings 2021 to 2025, the campaign as the unit, EDGAR's filing date, raw CRSP for prices.
E1 is stake at filing. E2 is run-up versus jump by pre-trigger liquidity. One paragraph
documents that the clock moved. E2's model direction enters the spec by a dated note after the
v5 grid has produced it and before E2 runs; that note is the orchestrator's commit between
phases A and B. A failed gate makes the exercise absent from the paper with no sentence about it.

## 5. Phases and the commit points

Registration is a commit and workers run no git, so the work runs as phases from
`.scratch/v5-paper/orchestration.md`, the orchestrator committing between them. Since
2026-09-02 the remaining phases run as the three batches of section 7.

- Phase A: mark parameter and timed smoke (01); garbling lemma and threshold dial (02); who gets
  caught (03); the inherited results (04); existence attempt (05); empirics
  build and the E1 run (06); E1 blind audit (07); literature check (09). Orchestrator then:
  reads the mark-2 grid record for the run-up share direction in κ, appends the dated E2
  direction note to `empirics/spec.md`, commits all Phase A files, one concern per commit.
- Phase B: E2 run (08); E2 link audit (08); grid figures at order size two and the two exercise
  figures (10). Orchestrator commits.
- Phase C: the paper writer (11) produces `paper.tex`, `appendix.tex`, `paper.bib` from the v5
  proofs, the result files, the brief, and the inherited draft's prose where it survives; number
  guard and compile check (11). Orchestrator commits.
- Phase D: one referee pass (12); one author fix pass (13); compile, visual inspection, PDFs to
  `deliverable/` (14). Orchestrator commits and pushes.
- Phase E (batch 4, ticket 16 superseding 15, after the v5 delivery at checkpoint 3): the
  detection record (T in {3, 5, 10}), the cut record and the regret record; the entry identity,
  the detection lemma, the upper-set lemma, the silence lemma, entry against the undetected, the
  Blackwell theorem, the trichotomy, the threshold-margin restatement, the split identity, the
  one-crossing lemma and the reversal lemma in the appendix; the attack gate per statement; the
  title, abstract, introduction, results placement and conclusion rewritten around section 2;
  label-and-compile check; one referee read; one author fix; unslop; compile, inspect, deliver.
  Orchestrator commits and pushes.

## 6. Policies every worker follows

- Attack gate: the writer of a proof and its attacker are different agents; the attacker
  reads the statement, the model, and the proof, and tries to break it. The label becomes
  PROVED only on the attacker's PASS. Grid claims are NUMERICAL with the grid named.
- Fail twice, stop. Each ticket gets one retry. On a proof failure the retry may change an
  assumption to a cleaner one and must say so in its report. A second failure returns STOP; the
  script ends; the orchestrator writes a one-page judgment for Austin and waits.
- Positive results only. No worker writes text about attempts, fallbacks, prior versions, or
  results that are not in the paper. The inherited draft is never cited.
- Labels never promoted by prose. The writer cites the label a result holds at write time.
- Every number in the paper renders from `e1_estimate.json` or `e2_estimate.json` or a grid
  record under `numerical_v4/checks/`; the number-guard test enforces the first two.
- Compute: `H` stays at its calibration value. A worker that cannot fit a run reports the wall
  time and memory and stops; it does not lower `H`.
- Reports are structured: status, files changed, evidence. The orchestrator reads reports, not
  transcripts.

## 7. Routing and budget

Grok 4.6 implements the remaining tickets in three batches, each an interactive Grok Build
session Austin starts; Fable orchestrates, owns git and reviews at the checkpoint after each
batch, with Opus 5 as attacker and judge (ADR 0006). The batch contents, efforts and the
step contract are in `.scratch/v5-paper/grok/README.md`. The prompt texts, schemas, procedures
and check-run rules of `.scratch/v5-paper/orchestration.md` still bind; its dispatch mechanics
are superseded.

## 8. Done

`paper.pdf` and `appendix.pdf` in `deliverable/`, zero TeX errors or undefined references,
number guard green, every result labelled, the referee's blocking items fixed, the unslop gate
passed, all commits on `v5` pushed, and a one-page session note at
`.scratch/v5-paper/session_note.md` listing what shipped and any STOP.
