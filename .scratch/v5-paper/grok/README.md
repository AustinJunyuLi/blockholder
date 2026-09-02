# Grok Build run book for the v5 delivery

Read this file, then the batch file named in the paste prompt. `CLAUDE.md`, `CONTEXT.md` and
`.scratch/v5-paper/spec.md` bind; this file adds only what they do not say. ADR 0006 is the
routing decision.

## Shape

Grok 4.6 implements the remaining tickets in three batches. Each batch is one interactive Grok
Build session that Austin starts in this worktree. The batch ends when every step in the batch
file has its result file; the session then reports and stops. At the checkpoint that follows,
the orchestrator (Fable, with Opus 5 as attacker and judge) reads the diff and the result files,
runs the gates only Opus may run, starts the long check runs, commits, and writes
`checkpoint-N.md` next to this file. The next batch begins by reading that note.

| Batch | Steps | Effort | Checkpoint after it |
|---|---|---|---|
| 1 | fixes from checkpoint 0 if any; 03 grid; 05 write, self-attack, fix; 08; 08 audit | high | CP1: Opus attack on 05; the 03 grid and 05 condition runs; 01 verify on the T1 and L4 reruns |
| 2 | 10; 11 | xhigh | CP2: 11 check; 12 referee (Opus) |
| 3 | 13; 14 | high | CP3: page inspection, unslop gate, push |

## Launch

From a terminal, for batches 1 and 3:

```bash
grok --reasoning-effort high --deny "Bash(git *)"
```

For batch 2 the effort is `xhigh`. Never `--worktree`: work happens in this directory, on this
branch, with no worktree isolation and no new branch.

Paste prompt, with N the batch number:

```text
Read .scratch/v5-paper/grok/README.md, then .scratch/v5-paper/grok/batch-N.md. Run batch N as the brief says, in order, and stop where it says.
```

## Contract for every step

- **Result file.** Each step writes JSON to `.scratch/v5-paper/runs/<label>/result.txt`:
  `{"status": "PASS" | "FAIL" | "ABSENT" | "STOP", "summary": "...", "files_changed": [...],
  "evidence": "...", "named_condition": "..." (optional)}`. A verdict step writes
  `{"verdict": "PASS" | "FAIL", "reasons": "..."}`. A run directory that already exists holds
  debris from killed runs: write `result.txt` there and touch nothing else in it.
- **Finished means finished.** A step whose `result.txt` says PASS or ABSENT is not redone.
- **No git.** No git command of any kind, including status, log and stash. The orchestrator
  owns git and commits at the checkpoint. Report every file changed in `files_changed`.
- **Paths.** Edit only the paths the ticket and the batch file name.
- **Attempt rule.** One attempt, one retry. The retry may change one assumption or one design
  choice to a cleaner one and says so in the summary. A second failure is STOP: write the STOP
  result carrying both reports, then go on to the next step that does not depend on it. The
  batch still ends normally.
- **On FAIL, report.** Never work around a gate, edit `empirics/spec.md`, lower `H`, or change a
  label. A gate that was not run is a FAIL, not a PASS.
- **Compute.** `PYTHONPATH=. .venv/bin/python`, never system python. One evaluation of the model
  at order size two takes about ten seconds and six gigabytes. Run at most one at a time inside
  the batch, and run a check script only with `--nodes 1`. Never the smoke at mark 2, never a
  full grid. A check run the orchestrator started may be running in the background (the T1 and
  L4 reruns during batch 1); that is expected and is not a reason to wait or to kill anything.
- **Subagents.** Use fresh subagents freely, in this directory. Skip `/implement` and
  `/execute-plan`: they default to worktrees and to open-ended review loops. A step gets one
  review round at most.
- **Attacker rule.** Where a step says self-attack, the attacker is a fresh subagent that did
  not write the proof and did not run any earlier step, given only: the statement and proof
  file, `CONTEXT.md`, `.scratch/v5-paper/spec.md` section 3, `docs/adr/0003`, and the model
  section of `inherited/draft_v3/draft_v3.tex`. No resumed session, no shared transcript with
  the writer. Its verdict changes no label; the Opus attack at the checkpoint is the gate.
- **Prose rules.** Positive results only: never a sentence about earlier versions, attempts, or
  the inherited draft. Prose never promotes a label. No em dashes, plain words.
- **Tool use.** Read the ticket file in full before acting. Run the acceptance commands and
  paste their output into `evidence`. Answer nothing from memory that a file can answer.

## End of a batch

When every step listed has its `result.txt`, write `.scratch/v5-paper/runs/batch-N/result.txt`:
`{"status": "PASS" | "STOP", "steps": {"<label>": "<status>", ...}, "files_changed": [...],
"summary": "..."}`. End the turn with a one-paragraph report. Do not start the next batch.
