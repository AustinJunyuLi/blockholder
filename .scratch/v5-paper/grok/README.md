# Grok Build run book for the v5 delivery

Read this file, then the brief named in the paste prompt. `CLAUDE.md`, `CONTEXT.md` and
`.scratch/v5-paper/spec.md` bind; this file adds the step contract and the gates. ADR 0006 is
the routing decision. ADR 0007 fixes what a brief is: it states the objective the batch must
reach and the constraints that hold, and the method is yours.

## Shape

Grok 4.6 implements the remaining tickets in four batches. Each batch is one interactive Grok
Build session that Austin starts in this worktree. A batch ends when every step named in the
brief has its result file and the batch result is written; the session then reports and stops.
At the checkpoint that follows, the orchestrator (Fable, with Opus 5 as attacker and judge)
reads the plan, the result files and the diff, runs the gates only Opus may run, starts the long
check runs, commits, and writes `checkpoint-N.md` next to this file. That note carries the facts
the next brief needs and feedback on how the batch was approached. The next batch begins by
reading it.

| Batch | Steps | Effort | Checkpoint after it |
|---|---|---|---|
| 1 | fixes from checkpoint 0 if any; 03 grid; 05 write, self-attack, fix; 08; 08 audit | high | CP1: Opus attack on 05; the 03 grid and 05 condition runs; 01 verify on the T1 and L4 reruns |
| 2 | step 0 from checkpoint 1; 10; 11 | xhigh | CP2: 11 check; 12 referee (Opus); the who-gets-caught rerun |
| 3 | 13; 14 | xhigh | CP3: attack on the two batch-3 lemmas; final CHECK; page inspection, unslop gate, push |
| 4 | 16 (superseding 15): records, proofs, self-attack, paper, check | xhigh | CP4: Opus attack per new statement; the full-grid record runs at T in {3, 5, 10}; the abstract's brackets chosen from the record; label-and-compile check; one referee read; one author fix; unslop; deliver, push |

Batch 2 was finished by Sol workers after Grok stopped mid-step (checkpoint 2). Batch 3 is run
by Gemini 3.8 Flash in an interactive session Austin starts here, with the same brief, plan and
result shapes and the same rules (no git, every file changed reported); Opus stays the attacker
and checker. The launch section below gives the paste prompt; the command line is the tool's own.

## Launch

From a terminal, with the effort the table gives:

```bash
grok --reasoning-effort high --deny "Bash(git *)"
```

Paste prompt, with N the batch number:

```text
Read .scratch/v5-paper/grok/README.md, then .scratch/v5-paper/grok/batch-N.md. Run batch N to the objective the brief states, and stop where it says.
```

The work happens in this directory, on branch `v5`: launch without `--worktree`, and reach each
step by a route that stays here (`/implement` and `/execute-plan` open a worktree of their own).

## Plan and approach record

Before the first step, write `.scratch/v5-paper/runs/batch-N/plan.md`, at most one page, five
short sections:

- the steps as you see them,
- the order you chose and what forces it,
- what you delegate, and to what kind of agent,
- the risks you see,
- what you check before you call a step done.

The plan is yours and you may depart from it while the batch runs; the batch result records how
it went. The orchestrator reads both and answers with feedback in `checkpoint-N.md`.

## Result files

Each step writes JSON to `.scratch/v5-paper/runs/<label>/result.txt`. A working step writes
RESULT:

```text
{"status": "PASS" | "FAIL" | "ABSENT" | "STOP", "summary": "...", "files_changed": [...], "evidence": "...", "named_condition": "..."}
```

`named_condition` is optional. A verdict step writes VERDICT:

```text
{"verdict": "PASS" | "FAIL", "reasons": "..."}
```

`evidence` quotes the output of the commands the step ran. `files_changed` names every file the
step changed, since the orchestrator commits from it. Add keys where a step has more to say;
these keys stay as they are.

A step whose result file already says PASS or ABSENT is finished: read the record, confirm the
edits it claims are on disk, and move on. A run directory that already exists holds debris from
killed runs: write `result.txt` there and leave the rest of that directory alone.

At the end of the batch, write `.scratch/v5-paper/runs/batch-N/result.txt`:

```text
{"status": "PASS" | "STOP", "steps": {"<label>": "<status>", ...}, "files_changed": [...], "summary": "...", "approach": {"as_planned": "...", "changed": "...", "stuck": "..."}}
```

`approach` holds a few sentences each: what went as the plan had it, what you changed and why,
where you got stuck. End the turn with a one-paragraph report, and leave the next batch to its
own session.

## Gates

- **Git.** The orchestrator owns git and commits at the checkpoint. Report every changed file in
  `files_changed`; run no git command, including status, log and stash.
- **Attempt rule.** One attempt, one retry. The retry may replace one assumption or one design
  choice with a cleaner one, and says so in the summary. A second failure is a STOP record
  carrying both reports; every step that does not depend on it still runs, and the batch ends
  normally.
- **Gates are reported as they came out.** A gate that was not run is a FAIL. A FAIL travels to
  the checkpoint in the result file, with `empirics/spec.md`, `H` and every label as they were.
- **Labels.** A label is set at the checkpoint: PROVED by Opus's attack, NUMERICAL by the grid
  judge on the stated grid, ESTIMATED by the registered gates. A batch carries the label a
  result already holds, and prose states that label as it stands.
- **Attacker rule.** Where a step says self-attack, the attacker is a fresh context that wrote
  none of the proof and ran no earlier step, reading exactly: the statement and the proof file,
  `CONTEXT.md`, `.scratch/v5-paper/spec.md` section 3, `docs/adr/0003`, and the model section of
  `inherited/draft_v3/draft_v3.tex`. Its verdict is advisory; the Opus attack at the checkpoint
  is the gate.
- **Registered spec.** `empirics/spec.md` is registered by the commit that precedes the run and
  stays as committed; a gate it fails makes the exercise absent. `H` keeps its calibration
  value, and a run that does not fit is reported with its wall time and memory.
- **Compute.** `PYTHONPATH=. .venv/bin/python`. One evaluation of the model at order size two
  takes about ten seconds and six gigabytes, so one evaluation runs at a time. Inside a batch a
  check script runs at `--nodes 1`; the full grid and the mark-2 smoke are the orchestrator's
  check runs. A check run the orchestrator started may be running in the background (the T1 and
  L4 reruns during batch 1); leave it to finish.
- **Paths.** Edit the paths the ticket and the brief name.
- **Prose.** Positive results only: every sentence is about what holds now. Plain words, no em
  dashes, sentence-case headings in markdown. The unslop gate applies to every file you write.
- **Records.** The plan, the result files and the diff are what reach the orchestrator; no
  transcript does.
