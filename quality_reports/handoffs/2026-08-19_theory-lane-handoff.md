# Handoff — theory lane (v4), for the other laptop

> **Why this is in the repo.** The `/handoff` skill normally saves to the OS temp directory.
> This one is committed on purpose: it must cross machines via GitHub.

Written 2026-08-19 from branch `v4` (HEAD `1ea05a9`). Vocabulary is `CONTEXT.md` — read it first
and use its words everywhere.

## Purpose

Rebuild the core model in two rounds, prove the partition theorem, publish the window-margin sign
the empirics lane is waiting on. Three to four long GPT Pro threads do the theory; Claude does
everything else. No empirics in this lane.

## Who does what

- **Author + GPT Pro** (chatbot on chatgpt.com — no API, cannot see the repo, reads pasted files)
  — the theorist. Proposes the model, the proofs, the labels.
- **Claude Code on the other laptop** (you) — hands, verifier, repo keeper: bundles inputs, runs
  every check, spawns Opus verifiers, writes the `.tex`, commits, pushes.
- **This session** (empirics lane, `v4`) — convergence owner. Owns `CONTEXT.md`, `docs/adr/`,
  `.scratch/`, `bibliography.bib`; merges `v4-theory` into `v4` at draft_v3.

GPT Pro never touches the repo. Claude never accepts a claim on GPT Pro's word.

## Setup on the other laptop

```sh
git clone https://github.com/AustinJunyuLi/blockholder.git   # or, if you have it: git fetch origin
cd blockholder && git fetch origin
git worktree add ../blockholder_v4_theory v4-theory   # branch exists on origin, cut from v4 at this handoff's commit
cd ../blockholder_v4_theory && make venv
.venv/bin/python -c "import numerical; print('ok')"
```

Commit at the end of every ticket. `git push origin v4-theory` after every ticket **and** the
moment `HANDOFF_sign.md` changes — the empirics lane pulls that file.

## What is decided (pointers; do not re-litigate)

`quality_reports/plans/2026-08-19_v4-two-lane-plan.md` (decisions D1–D10, lane structure);
`docs/adr/0006` (position = P2, the disclosure rule as the market's partition); `docs/adr/0007`
(one theorem, two-round model, two lanes); `docs/adr/0005` (routing); `CONTEXT.md` (glossary).
Ticket bodies are in `.scratch/v4-reposition/issues/` and are not repeated here:

| # | Title | Blocked by |
|---|---|---|
| 04 | T0 · Literature housekeeping: the three open cards | none |
| 05 | T1 · Re-run O-1 and publish the sign handoff | none for the repo model; two-round re-run needs 06 |
| 06 | T2 · Two-round core model and the partition theorem | none — the long pole |
| 07 | T3 · Scoping note: filing-timing game and continuous time | none |
| 08 | T4 · Draft-ready model, theorem and proofs sections | 06 |

## Order of work

1. **Start together, no GPT needed:** T1's repo-model O-1 re-run (one Opus agent writes
   `quality_reports/fixes/t1_o1_rerun_check.py` + JSON, runs it with `.venv/bin/python`, compares
   against the committed referee claim) **and** T0's lit housekeeping (Sonnet fetch, Opus reader,
   separate Opus verifier).
2. Publish `research/model_v4/HANDOFF_sign.md` as soon as that number lands, marked **provisional**,
   and push. The empirics lane stops waiting there.
3. **Thread 1 — BUILD.** The whole theory in one thread: two-round model; partition representation
   and existence; decomposition plus flagged-cell liquidity-invariance; the threshold-margin lemma
   (with the second lemma — the interior κ-motion of E[h] dies as π̄↓0); the window-margin sign
   condition, opened with the O-1 refutation as a fact to respect; the GE region certificate; the
   draft_v2 reuse/simplify/drop map. Output: model note, labels *claimed*, one check request per claim.
4. Claude runs every check, writes `research/model_v4/model_v4.tex` (+ `.md` mirror), updates
   `HANDOFF_sign.md` with the two-round number (earlier one kept visible), pushes.
5. **Thread 2 — ATTACK.** Fresh thread, statements only first — it re-derives independently. Only
   after it answers do you paste the proofs and the raw check output and ask for gaps. Verdict per
   claim: WRONG / MISCITED / UNCHECKED.
6. **Thread 3 — REPAIR + SHIP.** Given verdicts and check output: fix, re-label, produce the model
   section, theorem and proofs in LaTeX.
7. **T4:** Claude writes `sections_v3/model.tex`, `theorem.tex`, `proofs_appendix.tex` from the
   accepted output, compiles with xelatex, commits.
8. **T3 (ticket 07):** Thread 4, or one Opus agent — it commits the paper to nothing.

## The courier loop (how a thread actually runs)

GPT Pro cannot see files and Claude cannot see ChatGPT; the author carries text between them.
Claude must therefore build **every** message as one file, and ingest **every** answer as one file:

1. Claude writes `research/model_v4/threads/thread<N>_msg<k>.md` — the complete message, in
   order, nothing left for the author to assemble. The author opens it, selects all, pastes it
   into the ChatGPT thread (inside the Project). A long bundle may be attached as a file instead,
   but message 1 is pasted, not attached.
2. The author copies GPT's whole answer and pastes it into the Claude Code session with one line
   ("Thread 1 answer, turn 1:"). Claude saves it verbatim to
   `research/model_v4/threads/thread<N>_turn<k>_answer.md`, then: checks NOTATION DELTA, greps
   every lemma/ref/citation name, writes and runs the check scripts, and writes the next
   `thread<N>_msg<k+1>.md` — with the **raw** check output pasted in.
3. Repeat inside the same ChatGPT thread until Claude declares the thread done (every claim has
   a verdict or a check). Expect 4–8 round trips per thread.
4. Threads 2 and 3 start fresh ChatGPT threads; Claude prepares message 1 again. Thread 2's
   message 1 carries statements only — no proofs — until it has re-derived.

One-time ChatGPT setup: create a Project; upload `CONTEXT.md`, and later `MODEL_CARD.md` (replace
it whenever Claude regenerates it); start every thread inside the Project; still paste the card at
the top of message 1. Commit the `threads/` directory — it is the lane's primary-source record.

## The GPT Pro protocol

**The Project.** One ChatGPT Project holding the standing files, re-pasted at the top of every
thread: `CONTEXT.md` verbatim, and `research/model_v4/MODEL_CARD.md` — Claude creates it after
Thread 1's first accepted model design and regenerates it after each accepted answer. The card
holds the symbol table (symbol | meaning | sign restriction), timing, equilibrium notion, a result
ledger (ID | statement | label | evidence path), the standing rules, and a **LABELS** section:
PROVED / NUMERICAL (verified on a grid) / ESTIMATED / CONJECTURE. Region-certified is not a fifth
label — it is PROVED with the region named in the hypothesis; labels are never weakened by
editing. Stamp each version with the date and `git rev-parse --short HEAD`; an answer with a stale
stamp is re-asked, not accepted.

**Message 1 of every thread**, in order: (1) the card; (2) that thread's bundle as one
concatenated file — never "see the repo"; (3) for Threads 1 and 2,
`quality_reports/reports/2026-08-19_framework_v3_referee_report.md` **lines 95–125 verbatim**
(the O-1 finding: window-margin attenuation is false at baseline in the repo model), stated as a
fact to respect, not a question; (4) the answer template; (5) the rules — *you cannot see the
repo; cite only IDs that appear in the card; state what you did NOT claim.*

Bundles. Thread 1: `research/draft_v2_digest.md`, `research/positions/P2_partition_infodesign.md`
§§1–4 and §7, `research/positions/ADVERSARIAL_P2.md` §4, `CONTEXT.md`, ADR-0006/0007. Thread 2:
theorem statements only, until it has re-derived. Thread 3: Thread 2's verdicts plus the raw
stdout and JSON, verbatim.

**Answer template** — every result answers in exactly these headings: `CLAIM` (one sentence) ·
`HYPOTHESES` (numbered, each used) · `PROOF` (numbered steps, each citing a hypothesis or an
earlier step) · `WHERE IT FAILS` (≥2 concrete cases) · `LABEL CLAIMED` + why · `NUMERICAL CHECK
REQUEST` (formula, grid, predicted sign *and* magnitude) · `NOTATION DELTA` (symbols not in the
card) · `NOT CLAIMED`.

**Checks.** Claude turns every check request into `quality_reports/fixes/tN_*_check.py` plus a
JSON output, following the D-series pattern already in that directory (`d7_takeover_game_check.py`
+ `.json`, `d8_ge_dominance_check.py` + `.json`), runs it with `.venv/bin/python`, commits script
and JSON. The **raw** output, not a summary, goes back into the next thread. An Opus agent that
did not write the script re-runs it.

**One retry.** A WRONG claim is retried once, in a **new thread**, message 1 = card + the failing
stdout/JSON verbatim. Old threads defend themselves; new ones do not. Still wrong → demote to
CONJECTURE or drop, and tell the author. Cap three fix rounds.

**Who may move a label.** Only an executed check or Thread 2 — never GPT Pro's prose, never an
edit. Executed check + committed JSON → NUMERICAL. Independent re-derivation PASS + Opus
proof-read PASS → PROVED. Log every move: `ID | old→new | evidence path | who | date | commit`.

**Three failure modes.** (1) *Invents draft_v2 lemma numbers* — grep the repo for every lemma
name, `\ref` and citation it uses; anything not found is stripped and re-asked. (2) *Proof by
assertion* — grep the proof text for "clearly", "it follows", "standard", "obviously" and bounce
those lines with "show the step". (3) *Drift* (κ quietly becomes liquidity rather than
noise-trading intensity, a symbol re-keyed) — NOTATION DELTA is mandatory in every answer, and
re-paste the card past roughly 20 turns.

## Coupling with the empirics lane

`research/model_v4/HANDOFF_sign.md` is the **only** hard dependency. Required fields: **sign**
(does a tighter filing window raise or lower how much the control outcome moves with liquidity),
**magnitude** with units, **condition** under which it holds (region named), **which model**
produced it (repo or two-round), **date**, **commit hash**. Publish provisionally and early; when
the two-round number arrives, add it and keep the earlier one visible. Push the moment it changes.

Everything else stays uncoupled by disjoint writes. The theory lane writes only
`research/model_v4/`, `quality_reports/fixes/`,
`sections_v3/model.tex|theorem.tex|proofs_appendix.tex`, `research/cards/`, and its session log.
Do **not** edit `CONTEXT.md`, `docs/adr/`, `.scratch/` or `bibliography.bib`. New glossary terms
and bibliography entries are *proposals*: `research/model_v4/PROPOSED_TERMS.md` plus a session-log
note; the convergence owner merges them. (Ticket 08's bibliography entries go in a lane-local
`sections_v3/theory_refs.bib`.)

## Routing (ADR-0005; `~/.claude/rules/native-workflow.md` §Verification)

- **Opus** — model writer, independent re-deriver, judges, final referee, every paper reading, and
  every re-run of a check script someone else wrote.
- **Sonnet** — search, fetch, extraction, LaTeX plumbing, formatting, file moves. Effort `low` for
  mechanical stages, `medium` otherwise.
- **Fable is never spawned as a subagent.** Every Agent call sets model and effort explicitly.
- Finder ≠ verifier; verifiers prompted to refute; three outcomes only (WRONG blocks and triggers
  the one retry, MISCITED and UNCHECKED never block); executed checks wherever one exists;
  re-verify a fix with a checker who did not write it.
- **Ticket-03 environment finding**
  (`quality_reports/session_logs/2026-08-19_v4-ticket03-tournament.md`): the only genuine Kimi
  configuration exposed is `kimi-k3-max`. `kimi-k3-high/medium/low` are rejected, and unknown
  `-fast` Kimi slugs silently fall back to Composer 2.5 fast. The author has **banned Composer**.

## Hazards to carry

- **Interior-crossing condition.** draft_v2's baseline collapses Hold. If the crossing region
  collapses at some κ, the partition is a property of the information structure, not of positive
  cell mass. It belongs in the theorem's hypothesis, grid-verified (P2 §4; ADVERSARIAL_P2 §4).
- **The GE sign can flip off-region** (D8's counterexample logic). Certify a region, claim no
  global sign; empty region → ship fixed-cutoff only.
- **Chabakauri et al. (2022) is uncarded** and is the named live refuter of the partition
  whitespace. T0's first job; answer in one plain sentence whether it refutes.
- **Burkart–Lee–Van Schepdechen's December-2025 revision is unread** — a live risk to the
  appropriability coefficient λ = 1 − q(1−γ)ψ from D7.
- **Calibration must be re-anchored.** At the paper's own baseline ω_P ≈ 0.037, which made the old
  disclosure-attenuation effect under 1% (curve ranges 0.01107 vs 0.01117). Anchor the flagged
  share to the share of engagements that get disclosed before reporting any magnitude.

## Session logging

`quality_reports/session_logs/YYYY-MM-DD_<description>_theory.md`. Three triggers, all proactive:
**post-plan** (goal, approach, rationale, key context); **incremental** — 1–3 lines whenever a
decision is made, a problem solved, the author corrects something, or the approach changes, never
batched; **end of session** (summary, open questions, blockers). One line per GPT thread: which
thread, what came back, what the checks said, which labels moved.

## Suggested skills

`mattpocock-skills:domain-modeling` (read-only use of the glossary — propose terms, do not edit);
`mattpocock-skills:research` (T0 fetches); `mattpocock-skills:code-review` (the check scripts);
`anthropic-skills:pdf` (reading papers); `ego-browser` (paywalled papers — the author logs in).

## First message for the other Claude session

> Read `quality_reports/handoffs/2026-08-19_theory-lane-handoff.md` in this repo — it is the full
> brief for the theory lane of the v4 blockholder paper and it covers setup, ticket order, the GPT
> Pro protocol and the house rules. Then read `CONTEXT.md` and `docs/adr/0005`, `0006`, `0007`.
> Start two things in parallel, neither of which needs GPT Pro: ticket 05 (T1) — reproduce the
> referee's O-1 experiment in the current repo model with a committed check script under
> `quality_reports/fixes/`, run with `.venv/bin/python`, and publish a provisional
> `research/model_v4/HANDOFF_sign.md` — and ticket 04 (T0) — the three open literature cards,
> Chabakauri et al. (2022) first. Commit and push `v4-theory` after each. Do not edit
> `CONTEXT.md`, `docs/adr/`, `.scratch/` or `bibliography.bib`.
