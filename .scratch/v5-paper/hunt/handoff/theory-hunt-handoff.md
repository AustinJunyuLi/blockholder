# Handoff: theory-upgrade hunt for "Who Gets Caught"

Written 2026-09-02 by the batch-2 orchestrator thread (Prime Agent session
`01a0620e-dc3e-7298-8fbb-e817826cb987`, Claude Fable 5.1) for a new Fable thread in the same
worktree. The new thread administers a hunt for stronger theory. It does not touch the paper
build, which the writing thread is finishing in parallel.

## What the new thread is for

Run a bounded hunt for four theory upgrades (section 4), each as a feasibility memo written by a
worker and read by the thread manager, and decide which survive into a batch-3 ticket. Optionally
prepare a second, fresh-context consulting pack for GPT 5.6 Sol Pro (section 8); Austin relays it
by hand.

## 1. Read first, in this order

- `CLAUDE.md`, `CONTEXT.md`, `.scratch/v5-paper/spec.md`: the contract, the domain model, the
  spec. `AGENTS.md` names the three rules (paper is the only record and never refers to earlier
  versions; prose never promotes a label; workers run no git and report every file changed).
- `docs/adr/0003-doubled-order-size-and-existence.md` and
  `docs/adr/0007-briefs-state-objective-and-constraints.md`.
- `.scratch/v5-paper/orchestration.md` (gates, labels, checkpoint duties) and
  `.scratch/v5-paper/grok/checkpoint-1.md` (the label every result holds now).
- The proofs the hunt builds on: `proofs/02_garbling.tex` (Lemma g1 erasure form, Lemma g2
  garbling, Lemma g3 exact liquidity representation, the threshold theorem),
  `proofs/03_caught.tex` (the cut identity for the clock), `proofs/04_inherited.tex` (standing
  conditions (S1) to (S11) at lines 257 to 297, partition, factorisation, weight leg, clock
  theorem). `proofs/05_existence.tex` is the failed conditional route; not assembled, context only.
- `.scratch/v5-paper/external/gpt-sol-existence.md`: GPT Sol Pro's answer on existence. Its
  Theorem 1 (a commitment notion) is correct and rejected (it changes the game). Its section B is
  the source of the framing sentence "disclosure regulation changes what the market learns from
  silence" and of the model-statement defects now being fixed in the paper.
- `/tmp/blockholder_v5_handoff/gpt-sol-pro-existence-handoff.md`: the self-contained problem
  pack sent to GPT. Sections 5 to 7 (model verbatim, standing conditions, calibration with
  functional forms and parameter values) are reusable for a second pack.

## 2. State of the worktree when this was written

Branch `v5`, HEAD `639c886` (checkpoint 1). Uncommitted work belongs to batch 2 and to the
writing thread: `paper.tex`, `appendix.tex`, `paper.bib`, `figures/`,
`numerical_v4/checks/figures.py`, wording edits in `proofs/03_caught.tex` and
`proofs/04_inherited.tex`, record-field edits in `numerical_v4/checks/t5_who_gets_caught.py`,
`empirics/test_fingerprints.py`. Do not edit, stage or revert any of these.

Labels (from `checkpoint-1.md`). PROVED: partition and factorisation, flagged cell κ-free,
garbling lemma, threshold weight leg and closed form of S_P, clock dial, who-gets-caught identity
and characterisation. NUMERICAL: threshold composition leg on κ in [0.15, 0.85] at mark 2, H 10
(it fails just below 0.15); directional who-gets-caught sentences off the five-node record.
ESTIMATED: E1. ABSENT: existence, E2. The calibration's frozen policy is not an equilibrium of
the paper's game (a Hold island of width 1.6e-3, prior mass 4.4e-4, regret 7.0e-5 at node 1); the
paper calls it the benchmark policy and states every result at fixed policies.

## 3. Coordination with the writing thread (binding)

Two orchestrators share one worktree. These rules keep them apart.

- Paths. The hunt thread and its workers write only under `.scratch/v5-paper/hunt/` and the OS
  temp directory. Everything else is read-only: no edits to `paper.tex`, `appendix.tex`,
  `paper.bib`, `proofs/`, `figures/`, `numerical_v4/`, `empirics/`, `docs/`, `.scratch/v5-paper/grok/`,
  `.scratch/v5-paper/issues/`, records under `numerical_v4/checks/`. A worker that needs a script
  writes it under `.scratch/v5-paper/hunt/<n>-<slug>/` and runs it from the repo root with
  `PYTHONPATH=. .venv/bin/python`.
- Git. The writing thread owns commits for batch 2 and checkpoint 2. The hunt thread may commit
  only with explicit paths under `.scratch/v5-paper/hunt/` (`git add .scratch/v5-paper/hunt/...`
  then `git commit`), never `git add -A`, `git commit -a`, `stash`, `reset`, `checkout`, `rebase`
  or `push`. Workers run no git at all.
- Compute. One heavy run at a time on this machine (a pooled pass is about 10 s and 6 GB; a cold
  solve about 4 to 5 min and 8 GB; the machine has 24 GB). Before any pooled pass or solve, check
  that `.scratch/v5-paper/runs/COMPUTE_LOCK` does not exist and that `pgrep -f numerical_v4`
  is empty; then write the lock (pid, what, started) and delete it when done. The writing thread
  follows the same rule. Never run a check script that rewrites a record under
  `numerical_v4/checks/`; hunt scripts write their own records under `hunt/`.
- Messaging. The writing thread is a sibling root agent, id
  `01a0620e-dc3e-7298-8fbb-e817826cb987`; `await agent_message.list_agents()` shows it. Use it
  only for a conflict (a path both threads need, a lock held too long). Austin is the relay for
  decisions.

## 4. The hunt: four candidates, ranked

Each candidate below is stated as the objective a worker receives. Per ADR 0007 the brief states
objective and constraints and leaves the method to the worker. The statements are conjectures by
the batch-2 orchestrator; the worker's job is to prove, disprove, or sharpen them.

### 4.1 Order size two is the erasure regime

Conjecture. With a ternary noise lump of size one and a building order of b lumps, the pooled
experiment at liquidity κ is a garbling of the one at κ' < κ for every pair (monotone in κ) if
and only if b = 2. At b = 1 informativeness is non-monotone in κ (the flow reveals the mark at
κ = 0 and again at κ = 1 by parity; the ambiguous values 0 and 1 carry likelihood ratios
(κ/2)/(1−κ) and its inverse). At b ≥ 3 the two flow supports are disjoint and the pool hides
nothing. So b = 2 is the only ratio at which noise garbles building without confounding it.

Why it matters. It turns the one primitive change (ADR 0003, defended today by a paragraph) into
a proposition, and answers the referee objection that the order size was chosen to make the
theorem work. Lemma g1 in `proofs/02_garbling.tex` already carries most of the b = 2 half.

Expected cost: low. Expected outcome: true, with a short proof and a two-line counterexample at
b = 1 (a finite Blackwell comparison, checkable by a linear program).

### 4.2 One cut identity for both dials

Conjecture. The cut identity of `cor:caught` (`proofs/03_caught.tex`, part (iii): the looser
rule's pooled sensitivity is the mass-weighted average of what the tighter rule leaves in the
pool and what it removes, with the survivors' re-pricing term) holds verbatim for the threshold
margin, because tightening the threshold also produces nested flagged cells
C_F(τ,T) ⊆ C_F(τ',T) for τ' < τ (crossing dates are weakly earlier and monotone in the signal,
standing conditions (S4) and (S5)). Under both dials the removed set is the top slice of the
silent pool's Voice types. Condition D (C_τ ≤ 1) is then the same band condition on the removed
set's sensitivity as (iv) of the corollary.

Second, harder part. A sufficient condition on primitives for the band condition, for instance
that a type-level sensitivity contribution is monotone in the signal on the pool's Voice region.
Any such condition will be conditional: the grid record
`numerical_v4/checks/t2_threshold_revelation_check.json` shows Condition D failing just below
κ = 0.15, so a universal claim is false. A condition that holds where the grid holds and is
checkable at a node is the target.

Why it matters. One identity, two dials, one question ("is what gets caught more noise-sensitive
than what stays"), instead of a Condition D for the threshold and a separate corollary for the
clock. The first part is close to transcription; the second is the real mathematics.

### 4.3 Tightening is a Blackwell improvement

Conjecture. At fixed policies, for τ' < τ at a common window, or T' < T at a common threshold,
the market's control-node experiment about the blockholder's type under the tighter rule is
Blackwell more informative than under the looser one. Sketch that the worker may ignore:
flagged sets are nested; a flagged type is identified exactly since b* is strictly increasing
(S6 of the calibration; standing condition (S4) gives monotone paths); from the tighter rule's
output one can simulate the looser rule's output by drawing fresh noise for types flagged only
under the tighter rule, because no-feedback timing (S7) makes the mark path a function of the
type alone.

Corollaries to state if it holds: expected posterior variance of engagement falls in tightness
unconditionally; the expected premium level rises when the kernel 𝗁 of Lemma g3 is convex on
the hull the pooled cell generates.

Why it matters. It gives the paper a first theorem under the framing "tightening always
improves what the market knows; the sensitivity results say how the improvement is composed,
into a κ-free flag part and a silence part". Risk: a referee may find it obvious; it is a spine,
not a headline.

### 4.4 A stated maximal regret for the benchmark policy (numerical, not theory)

Objective. A record giving, at each of the ten calibration nodes (T in {5, 10}, five thresholds
in the ladder of `numerical_v4/checks/t5_who_gets_caught.json` provenance), a rigorous upper bound
on the benchmark policy's maximal interim regret, ess sup over signals of the best plan's payoff
minus the assigned plan's payoff. The bound must come from a breakpoint-aware method (the free
breakpoints of n(s) and the legal clock are computable in closed form; see
`numerical_v4/menu.py` `breakpoints`), not from a uniform signal grid; the 241-point grid missed
the node-1 island. Reference numbers at node 1: regret 7.0e-5 on the island (1.8608, 1.8625),
zero elsewhere to solver tolerance; see `.scratch/v5-paper/runs/05-condition-judge/result.txt`
and `/tmp/judge05_gap.json` (plateau table, crossings).

Why it matters. It answers "why should the reader care about comparative statics at this
policy" with one number per node, at the cost of about ten pooled passes. It changes no label.

### Not worth chasing

Existence or any equilibrium result under the paper's notion (the integer building count makes
the best-response correspondence non-monotone; no theorem edit fixes it short of a menu change,
which is a calibration change out of scope). A general-equilibrium comparative static (dropped
in ADR 0003). A Kyle-style "tighter rules lower informed profits" result (the cross-moment it
needs is not Blackwell-monotone in general).

## 5. Deliverable shape for each candidate

A memo at `.scratch/v5-paper/hunt/<n>-<slug>/memo.md` with, in this order: the statement as the
worker would put it in the paper, with the full hypothesis list in the numbering of the standing
conditions; the proof, or the counterexample, or the honest "open" with what blocks it; what a
script must compute at a node, if anything, with tolerances; the cost of carrying it into the
paper (which theorems it touches, which labels it could change, which sections move); and a
`RESULT` JSON block in the shape `.scratch/v5-paper/schemas/` gives, status PASS for "proved",
FAIL for "false", STOP for "open". Any script and its record sit beside the memo. LaTeX for the
statement and proof is welcome and should follow the conventions of the existing `proofs/` files.

## 6. Gates before anything reaches batch 3

- Writer and attacker are different agents. A memo that claims PROVED gets an attack from a
  different model family than the writer (Opus if the writer was Sol; Sol xhigh if the writer was
  Opus). The attacker writes `.scratch/v5-paper/hunt/<n>-<slug>/attack.md` with a VERDICT JSON.
- Labels are set at checkpoints by the writing thread's orchestrator, never in a memo or in prose.
  A memo says what label it would support; it does not award it.
- The paper is the only record. Nothing in a memo cites the inherited draft, earlier versions,
  or failed attempts as authority; the failed existence route may be discussed in a memo, never
  in paper text.
- Unslop rules apply to memos: no em dashes, sentence-case headings, plain words, no chatbot
  phrasing.
- Survivors become tickets under `.scratch/v5-paper/issues/` only through the writing thread's
  orchestrator at checkpoint 2 or 3 (that thread owns the issues directory and the batch-3
  brief). Hand it the memo paths and your verdict; Austin decides what enters.

## 7. Model roster and spawn form

Austin's instruction (2026-09-02): default to GPT 5.6 Sol at medium or high, escalate to xhigh
for hard work, max for the most intricate; a little Opus; no Sonnet. Sol's mathematics is on a
par with Fable 5.1 but it is slow. Spawn form in the Prime Agent REPL:

    h = await rlm(brief, name='hunt-erasure', model='openai-codex/gpt-5.6-sol', thinking='xhigh')

`thinking='high'` and `'xhigh'` are confirmed to work for `openai-codex/gpt-5.6-sol`; `'max'` is
untested (an unsupported level fails the spawn, so try it once and fall back). Opus is
`anthropic/claude-opus-5`. Children reply with
`await agent_message.send(message, receiver_role='parent')`; delete with
`await rlm.delete_subagent(h.rlm_child_id)` (passing the handle raises TypeError). Recover handles
after a restart with `await rlm.list_subagents()`. If a child goes silent, read its session jsonl
under `~/.prime/agent/session-artifacts/<your-session>/<child-id>/`.

Suggested assignment: 4.1 Sol xhigh; 4.2 Sol max (or xhigh if max fails), the two parts to one
worker so the identity informs the sufficient condition; 4.3 Sol xhigh; 4.4 Sol high (it is code
and a record, not a proof). Attacks: Opus for 4.1 to 4.3. All four can run in parallel; 4.4 is
the only one that needs the compute lock.

Brief every worker with the preamble the writing thread uses: read the contract files first;
no git; paths limited to its hunt directory; the paper is the only record; unslop; compute
rules; reply to the parent with files changed and the memo path. State the objective and the
constraints; do not prescribe the proof.

## 8. Optional: a second GPT 5.6 Sol Pro consulting pack

GPT Sol Pro (web) has no filesystem; Austin pastes a pack and relays the answer into
`.scratch/v5-paper/external/`. The first pack and prompt are at
`/tmp/blockholder_v5_handoff/gpt-sol-pro-existence-handoff.md` and
`/tmp/blockholder_v5_handoff/gpt-sol-pro-prompt.txt` (copy them somewhere durable; `/tmp` is
cleared on reboot). Reuse their sections 5 to 7 verbatim for the model, the standing conditions
and the calibration.

A second pack should state the four candidates of section 4 as objectives and ask for proofs or
counterexamples plus holistic comments, in a fresh context (do not include GPT's first answer;
do include the fact that the paper is now a fixed-policy paper with a benchmark policy). Include
`proofs/02_garbling.tex` and `proofs/03_caught.tex` verbatim so GPT sees the erasure form and
the cut identity; the first pack did not carry them. Same output constraints as the first pack:
every hypothesis in the statement, anything checkable at a node stated as a computation with a
tolerance, unproved parts labelled. GPT's answer is input, not authority: it goes through the
same attack gate as a worker memo.

## 9. Suggested skills

- `writing-for-agents` when writing the worker briefs and the memo template.
- `unslop` on every memo and brief before it is saved.
- `code-review` if 4.4 produces a script that might later move into `numerical_v4/checks/`.
- `subagents` for the delegation shape (bounded workers, explicit reply).
- `research` only if a candidate needs a literature check (Blackwell garbling of finite
  experiments for 4.1 and 4.3); the existing literature ticket is
  `.scratch/v5-paper/issues/09-literature-check.md`.

## 10. What the writing thread is doing meanwhile

Finishing batch 2: a Sol worker is bringing `paper.tex`, `appendix.tex`, `paper.bib` to the
Done list of `.scratch/v5-paper/grok/batch-2.md` plus seven model-statement constraints taken
from GPT's review (signal truncation stated; mark versus order size; Exit's sale leaves no mark,
with its reason; filing-date timing; "benchmark policy", never "equilibrium"; an economic scale
argument in the order-size paragraph; almost-sure optimality if an equilibrium is defined). Then
an Opus CHECK, a Sol referee, commits one concern per commit, `grok/checkpoint-2.md`, and the
batch-3 brief. The who-gets-caught record rerun holds the compute lock until it finishes.
