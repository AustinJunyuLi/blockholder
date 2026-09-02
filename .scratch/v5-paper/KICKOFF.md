# Kickoff for the delivery session

Two sessions share the work from 2026-09-02 (ADR 0006). Austin relays between them.

**The implementing session** is Grok Build, started by Austin per batch. Launch line and paste
prompt: `.scratch/v5-paper/grok/README.md`. Its brief states the objective and the constraints;
Grok chooses the method, writes its plan first and reports how the batch went (ADR 0007).

**The orchestrating session** is Fable in Claude Code, started in
`/Users/austinli/Projects/blockholder_v5`. Paste this as its first message:

> Read CLAUDE.md, CONTEXT.md, .scratch/v5-paper/spec.md, .scratch/v5-paper/orchestration.md
> and .scratch/v5-paper/grok/README.md. You are the orchestrator at the checkpoints: when
> Austin says a batch is done, read runs/batch-N/plan.md, runs/batch-N/result.txt and the diff,
> run the Opus attacks and judge calls orchestration.md lists for that checkpoint, start the
> check runs detached one at a time (ADR 0004), commit one concern per commit, write
> grok/checkpoint-N.md with every label and your feedback on the approach, and write
> grok/batch-(N+1).md as an objective with its constraints (ADR 0007). A STOP ends the build:
> write the one-page judgment and wait for Austin. You own git; no worker runs any.

Run records land under `.scratch/v5-paper/runs/`; a step whose `result.txt` shows PASS or
ABSENT, or whose ticket is already committed on `v5`, is done.

State at 2026-09-02 12:30: tickets 04, 06, 07, 09 committed and done; 01 code committed with
the judge verify pending; proofs 02 and 03 committed and under Opus attack (checkpoint 0);
the T1 then L4 reruns started detached at 12:22; batch 1 brief written.
