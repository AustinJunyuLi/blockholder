# Rules for hunt workers

You are a worker in the theory-upgrade hunt for the paper *Who Gets Caught: Blockholder
Disclosure Rules and Market Inference*. Your brief is `brief.md` in your hunt directory. This
file holds the rules every worker follows. Read it once, then the brief.

## Read first, in this order

1. `CLAUDE.md`, `CONTEXT.md`, `.scratch/v5-paper/spec.md` (the contract, the glossary, the plan).
2. `docs/adr/0003-doubled-order-size-and-existence.md` and
   `docs/adr/0007-briefs-state-objective-and-constraints.md`.
3. `.scratch/v5-paper/grok/checkpoint-1.md`, section "Labels at this moment".
4. The proofs your brief names. The standing conditions (S1) to (S11) are in
   `proofs/04_inherited.tex` at lines 257 to 297; every statement you write numbers its
   hypotheses in that scheme and adds any hypothesis the standing conditions do not carry.

Every path in this file and in your brief is relative to the repository root
`/Users/austinli/Projects/blockholder_v5`. Work from there.

## Paths

Write only inside your own hunt directory, `.scratch/v5-paper/hunt/<n>-<slug>/`, and the OS
temp directory. Everything else in the worktree is read-only. In particular do not touch
`paper.tex`, `appendix.tex`, `paper.bib`, `proofs/`, `figures/`, `numerical_v4/`, `empirics/`,
`docs/`, `.scratch/v5-paper/grok/`, `.scratch/v5-paper/issues/`, `.scratch/v5-paper/runs/`
(except the compute lock file named below), or any other hunt directory. A second orchestrator
is editing the paper in this worktree at the same time; a stray write costs both threads.

## Git

Run no git command. None. Not `git status`, not `git diff`, not `git log`. Read files directly.

## Compute

Model evaluations are heavy: one pooled pass is about 10 seconds and 6 GB; a cold policy solve
is 4 to 5 minutes and 8 GB; the machine has 24 GB and two orchestrators share it. Rules:

- One heavy run at a time on the machine. Before any pooled pass or solve, check that
  `.scratch/v5-paper/runs/COMPUTE_LOCK` does not exist and that `pgrep -f numerical_v4` prints
  nothing. Then write the lock as a JSON file with keys `pid`, `what`, `started` (ISO time) and
  `owner` (your hunt directory name). Delete it as soon as your run ends, including on error.
- If the lock exists or a process is running, do other work and try again later. Do not wait
  in a loop for more than a few minutes; if you cannot get the machine within your work, write
  the memo without the computation and say so.
- Never run a script under `numerical_v4/checks/` (each rewrites a record file), never run
  `numerical_v4.smoke`, and never start a cold solve unless your brief says you may. Never lower
  `H`.
- A hunt script lives beside your memo and runs from the repository root as
  `PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/<n>-<slug>/<script>.py`. It writes its
  record beside itself, never under `numerical_v4/`.
- Frozen calibration inputs (the benchmark cutoffs `frozen_k`, the threshold ladder
  `tau_ladder`, the parameter hash) are in the `provenance` block of
  `numerical_v4/checks/t2_threshold_revelation_check.json` at full precision. Read them; do not
  re-solve.

## What the memo is

Write `memo.md` in your hunt directory with these parts, in this order:

1. The statement, as you would put it in the paper, with the full hypothesis list numbered in
   the standing-condition scheme (S1) to (S11) plus any added hypothesis, each named.
2. The proof, or the counterexample, or the honest "open" with what blocks it. A proof is
   complete at the level of a journal appendix. A counterexample is explicit and checkable.
3. What a script must compute at a calibration node, if anything, with tolerances.
4. The cost of carrying the result into the paper: which theorems it touches, which labels it
   could change, which sections move.
5. A `RESULT` JSON block in this schema:
   `{"status": "PASS" | "FAIL" | "STOP", "summary": str, "files_changed": [str], "evidence": str}`.
   PASS means "proved as stated in part 1", FAIL means "false, with the counterexample in
   part 2", STOP means "open, with the blocker in part 2".

LaTeX for the statement and proof is welcome in a separate `statement.tex` beside the memo,
following the conventions of the files in `proofs/`.

## Rules on content

- The paper is the only record. The memo may discuss the model, the proofs and the records.
  It never cites the inherited draft (`inherited/`), earlier versions of the paper, or failed
  attempts as authority. The failed existence route may be discussed as context, never as
  authority.
- Labels (PROVED, NUMERICAL, ESTIMATED) are set by the orchestrator at a checkpoint. The memo
  says which label the result would support and awards none. Prose never promotes a label.
- Positive claims only where you have them. Where a step is unproved, say so in the step.
- Writing rules: no em dashes, sentence-case headings, plain words, no chatbot phrasing, no
  filler. Short sentences.
- You are the writer. An independent attacker from another model family will read your memo
  and try to break it. Write so that the attacker can check every step.

## When you finish

Reply to the parent once with `await agent_message.send(message, receiver_role='parent')`.
The message holds, in this order: the status (PASS, FAIL or STOP), the memo path, every file
you created or changed, and a summary of the evidence in at most ten lines. Send nothing else
to the parent unless you are blocked on a path or the compute lock.
