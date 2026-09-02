# Spec: the v5 paper in one session

Read `CLAUDE.md` and `CONTEXT.md` first. This file is the plan for the session that delivers
`paper.tex`, `appendix.tex`, and the two PDFs in `deliverable/`. It is self-contained. Nothing
outside this worktree is consulted.

## 1. Deliverable

A finished paper titled *Who Gets Caught: Blockholder Disclosure Rules and Market Inference*,
compiled clean, referee-reviewed once, fixed once, unslop-gated, with every theorem passed
through the attack gate on v5 and every number rendered from a result file. Slides are not
part of this session.

## 2. Headline

A disclosure rule has two dials. The stake threshold τ and the filing clock T split every
blockholder history into a flagged cell (the filing landed; the market knows) and a pooled cell
(no filing; the market reads order flow). Noise sensitivity of the price factorises as the
pooled share times the pooled sensitivity. Tightening the threshold lowers it at fixed policies.
Shortening the clock lowers it if and only if the newly caught histories are at least as
noise-sensitive as the pooled cell, and the paper states that condition as a corollary.

## 3. The model, as the paper states it

Two rounds of the inherited two-round structure, one change. The engaged blockholder's order
while building the stake is two noise lumps (ADR 0003). The noise trader trades one lump up or
down with probability κ/2 each and sits out with probability 1 minus κ. Order flow takes five
values; only the value plus one is ambiguous between "blockholder bought, noise sold" and
"blockholder idle, noise bought". Everything else in the model (plans, the Voice and Exit menu,
the bidder, the pricing rule, the calibration) is inherited unchanged and restated in the
paper's own words.

Results the paper carries, each with a label at delivery:

| Tag | Statement | Route | Ticket |
|---|---|---|---|
| Partition and factorisation | The rule partitions histories; S = (1 minus Ω) times S_P | Inherited proof re-derived on v5 | 04 |
| Flagged cell is κ-free | The flagged endpoint does not depend on κ | Inherited proof re-derived on v5 | 04 |
| Garbling lemma (new) | At order size two, the pooled experiment at higher κ is a garbling of that at lower κ; the pooled expectation of any convex (concave) kernel is monotone in κ | New proof | 02 |
| Threshold dial | At fixed policies a tighter threshold weakly lowers noise sensitivity | Garbling lemma plus the weight and composition legs; any residual bridge clause becomes one named condition verified on the grid | 02 |
| Clock dial | At fixed policies a shorter clock lowers noise sensitivity iff W_T times C_T is at most one | Inherited proof re-derived on v5 | 04 |
| Who gets caught (new) | C_T is at most one iff the newly caught histories are at least as noise-sensitive as the pooled cell; the paper gives the identity behind it | New proof plus a grid check | 03 |
| Existence (conditional on cleanliness) | An equilibrium exists at the paper's calibration | Only if the proof is clean at the numbers used; otherwise absent | 05 |

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
  caught (03); re-derivation of the inherited results (04); existence attempt (05); empirics
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
