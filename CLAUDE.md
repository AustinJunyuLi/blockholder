# CLAUDE.md

## Project overview

Academic research project: **"Liquidity, Activism Disclosure, and Takeover Premia"** — an
economic theory model of blockholder behaviour (exit, voice, corporate control). Two eras
coexist in this repo: the **frozen draft_v2 record** (one-round model, figure pipeline, and the
manuscript the supervisor has seen) and the **live v4 effort** (one theorem, two-round model,
two lanes — ADR-0007). In this worktree the live work is the theory lane; the draft_v2 layers
are reference.

## v4-theory lane — theory record FROZEN 2026-08-30; live work is draft_v3 + code

This checkout is the **`v4-theory` worktree** (branch `v4-theory`), one of three worktrees of
the same repo: `blockholder` (`proposal`), `blockholder_v4` (`v4`, the **empirics lane** — do
no empirics work here), and this one. Read `CONTEXT.md` and `docs/adr/` first.

**The theory record is FROZEN** (2026-08-30, commit `65b8db3`; card stamp `2026-08-30 · F5
route R40-A applied + batched two-pass gate PASS + theory-record freeze`). The R-number
sequence is closed, `threads/` is archive, and no proof repairs, audits of audits, or
label-gate runs happen unless Austin reopens the record. From the freeze, **the only artifacts
under review in this checkout are draft_v3 and code.** The live work is `draft_v3.tex` (+`.bib`,
`.pdf`, and `draft_v3_trace.md`) at the repo root: every claim in the draft traces to a card
row via the trace file; a sentence with no card row behind it is a defect to remove, not an
addition to verify. Empirical results come from the empirics lane into the draft's §6 — still
do no empirics work here.

**Where the theory lives**

- `research/model_v4/` — `MODEL_CARD.md` is the single source of truth; **check its version
  stamp before answering from it** (an answer written against a stale stamp is re-asked).
  Beside it: `model_v4.tex`/`model_v4.md` (mirrors — transcription of the card, never new
  claims), `proofs/`, `rederive/`, `threads/` (GPT Pro courier record, filed verbatim),
  `impl_design.md`, and the two ledgers: `LABEL_LEDGER.md` (every label move:
  `ID | old→new | evidence | who | date | commit`) and `HANDOFF_sign.md` (the empirics lane's
  only hard dependency on this lane — amend it only with a dated marker).
- `numerical_v4/` — the two-round implementation. Its gate is the smoke run:
  `.venv/bin/python -m numerical_v4.smoke` (one baseline equilibrium + one frozen-policy kappa
  sweep; `range M_F < 1e-10` is the L2 assertion). Executed checks land as
  `quality_reports/fixes/t2_*.py` with a JSON verdict beside the script.
- `teach/` — the from-zero curriculum (`MISSION.md`, `lessons/`); prose there follows the
  unslop rules in `MISSION.md`.
- Governing plan: `quality_reports/plans/2026-08-20_theory-lane-agentic.md`. Session logs:
  `quality_reports/session_logs/`.

**Label discipline.** Honesty labels (PROVED / NUMERICAL / ESTIMATED / CONJECTURE) are defined
in `CONTEXT.md`. CONJECTURE → PROVED needs the **two-pass gate**: the writer's proof, an
adversarial proof-read PASS, and a statements-only re-derivation PASS — two fresh agents,
neither of whom wrote the proof, the re-deriver working from the card row alone with `proofs/`,
`threads/`, and `rederive/` unopened. An executed, committed check → NUMERICAL. GPT Pro's end
review can demote, never promote by prose. Never weaken a label in the card, the ledger, or the
draft; supersede a landed record line with a dated amendment, never a silent rewrite. **The gate
ran for the last time on 2026-08-30** (`rederive/P1_gate_2026-08-30.md`); the machinery is closed
with the record.

**Roles and rules.** Opus agents write proofs, proof-read (never their own), re-derive, and
build/verify `numerical_v4`; Sonnet does search, extraction, LaTeX plumbing, and file moves;
the session model orchestrates and reasons directly only on the hardest bits (writer-vs-verifier
disputes, implementation design review, the final coherence read). Finder ≠ verifier throughout.
Verification vocabulary: WRONG blocks with one retry; MISCITED and UNCHECKED never block.
**Git belongs to the orchestrator alone** — agents never run git; each landed unit is committed
and pushed by the orchestrator with explicit paths; `<pending-orchestrator-hash>` placeholders
in stamps and ledger lines are filled in a follow-up commit. **One card writer at a time** — a
parallel ticket returns its card text and the orchestrator applies it verbatim in a quiet
window.

**Post-freeze review rules (2026-08-30 →).** Each artifact — draft_v3, or code — gets **one
review**, by one fresh agent that wrote none of it, and its author fixes the findings **once**.
A review reads the artifact as its reader would. A finding about another review goes to
Austin's one-pager, never into a new file. If drafting surfaces a theorem-level problem: stop
that section, write it into the one-pager, and ask Austin. Every session ends with a one-page
brief for Austin (proved / at risk / needs me) — the only document written for him.

## Tracker, triage, domain docs

- **Issue tracker**: one file per ticket under `.scratch/<feature>/issues/` — mechanics in
  `docs/agents/issue-tracker.md`. `.scratch/` is git-tracked per branch and the branches have
  diverged: the canonical v4 tracker (tickets 21+) lives on branch `v4` — read it from the
  `~/Projects/blockholder_v4` worktree.
- **Triage labels**: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`,
  `wontfix` — mapping in `docs/agents/triage-labels.md`.
- **Domain docs**: `CONTEXT.md` (the glossary — use its vocabulary, never the terms it avoids)
  and `docs/adr/` — consumption rules in `docs/agents/domain.md`.

## Frozen draft_v2 layer (reference)

`draft_v2.tex` is frozen. Its stack still builds and remains the reference for the one-round
model:

- **Pipeline**: Python → CSV → matplotlib → PDF → LaTeX. `make venv` once (creates `.venv/`
  from `requirements.txt`), then `make all` (or `make data` / `make figures` / `make clean`).
  The CSVs in `numerical_output/data/` are the model↔figure contract — column names match paper
  notation; when the model changes, change `numerical/export_data.py` and the matching function
  in `pyfig/figures.py` together.
- **`numerical/`**: `params.py → model.py → solver.py → export_data.py`; `accel.py` is an
  optional Numba layer (`solver.py` is the reference implementation); `takeover_game.py` is the
  D7 tender game (`params_with_endogenous_wedge` is opt-in; exogenous `(m0, m1)` is the
  default). Conventions: pure functions, full type hints, a `params: ModelParams` argument,
  NamedTuple returns. Tolerance constants live in `params.py` — do not change them without
  understanding downstream effects.
- **`pyfig/`**: `style.py` (house style; the Paul Tol palette's canonical hex values live
  there), `figures.py` (one function per figure; `ALL_FIGURES` is the render list),
  `render_all.py` (`python -m pyfig.render_all`).
- **`empirics/`**: stdlib-only EDGAR pipeline for the de-risk leg; raw data gitignored,
  summaries committed. See `empirics/README.md`.
- **D-series** (`quality_reports/fixes/`): each draft_v2 derivation is `DN_*.tex` plus a paired
  `dN_*_check.py` with JSON output.
- **LaTeX**: `xelatex draft_v2.tex && biber draft_v2 && xelatex draft_v2.tex`; the presentation
  builds the same way in `pres/` (`presentation.tex`, its own `slides.bib`).
- **One-round model**: four actions off a private signal `s` — Exit (`s < k1`), Hold, Quiet
  Voice, Public Voice (`s ≥ kD`); cutoffs solved by damped fixed-point iteration; `kappa`
  (noise-trading intensity) is the comparative-statics variable. The two-round model in
  `research/model_v4/` supersedes this for the live lane.
- **Gotchas**: the solver may return NA rows at extreme `kappa` (expected; figure functions
  drop them). No formal test suite — verification is `make clean && make all` plus visual
  inspection of the PDFs.
