---
status: accepted
date: 2026-09-02
---
# Briefs state the objective and the constraints; the implementer chooses the method

Batch 1 was handed over as a script: the step order, the subagent split, the per-step recipe and
the prompt texts all came from the orchestrator, and the implementer's own judgment had nowhere
to act. Asked instead to design its own route through the same work, Grok 4.6 wrote
`.grok/workflows/v5-batch-1.rhai`, which sequences the batch, runs the independent step 0 edits
together, carries the gates into every prompt and closes the batch on one result file. From
batch 2 a brief has four parts and nothing else: the objective, meaning what must be true when
the batch ends in terms the orchestrator can check; the inputs, as pointers to tickets, records
and checkpoint notes; the constraints that bind this batch, which are the effort, the paths, the
labels the results carry and the dependencies between steps; and done, the result files that
must exist and what each must show. `.scratch/v5-paper/grok/README.md` carries the standing
gates once, so a brief points at it and restates none of them. Two records make the method
visible in exchange: `runs/batch-N/plan.md`, written before the first step, holds the steps as
the implementer sees them, the order and what forces it, what it delegates, the risks and what
it checks before calling a step done; the `approach` block of `runs/batch-N/result.txt` records
what went as planned, what changed and why, and where it got stuck. The orchestrator reads both
at the checkpoint and writes feedback on the approach in `checkpoint-N.md`, so review covers how
the work was organised as well as what it produced. The gates of ADR 0006 are unchanged.
