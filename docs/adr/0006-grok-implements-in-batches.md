---
status: accepted
date: 2026-09-02
---
# Grok 4.6 implements in batches; the orchestrator and Opus review at checkpoints

The omp route of ADR 0005 put three providers behind one dispatcher, and the session went to
the dispatcher instead of the paper. From this date Grok 4.6, under a subscription with no
usage ceiling, implements every remaining ticket in three batches, each an interactive Grok
Build session that Austin starts in the worktree. The orchestrator (Fable) and Opus 5 implement
nothing: at the checkpoint after each batch they attack the proofs, judge the records, start
the check runs, commit, and write the note the next batch reads. Austin relays between the two
sessions, because a Grok workflow cannot host Opus and a pause inside one resumes only in the
same process, so one run per batch to completion is simpler than any pause. The gates are
unchanged: a proof's writer and its attacker are different agents, and the attacker whose
verdict changes a label is Opus. A self-attack inside a batch is a separate subagent from the
writer and is advisory. Effort is set per batch at launch, high by default and xhigh for the
paper writer, since the composite benchmarks put Grok 4.6 high and xhigh within a point of each
other and xhigh's only measured edge is on long agentic runs. Batch briefs and checkpoint notes
live under `.scratch/v5-paper/grok/`. ADR 0005 is superseded.
