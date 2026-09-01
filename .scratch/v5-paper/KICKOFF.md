# Kickoff for the delivery session

Paste this as the first message of a fresh Claude Code session started in
`/Users/austinli/Projects/blockholder_v5` with Fable 5.1 as the model.

> Read CLAUDE.md, CONTEXT.md, .scratch/v5-paper/spec.md and .scratch/v5-paper/orchestration.md.
> Run the steps in orchestration.md phase by phase yourself: Kimi and GLM steps through
> kimi-dispatch and glm-dispatch as background Bash jobs, Opus steps as opus subagents. A step
> whose runs/<label>/result.txt shows PASS or ABSENT, or whose ticket is already committed on v5,
> is done. Commit between phases as the spec says; you own git, workers run none. A STOP ends the
> build: write the one-page judgment and wait for me. Deliver paper.pdf and appendix.pdf.

Every step, effort, dependency and prompt text is in `.scratch/v5-paper/orchestration.md`; the
run records land under `.scratch/v5-paper/runs/` and are the record of what has already run.

State at handover (2026-09-02): tickets 04, 06, 07 and 09 are committed and done. The uncommitted
changes under `numerical_v4/` and the files `proofs/02_garbling.tex`, `proofs/03_caught.tex` and
`numerical_v4/checks/t2_threshold_revelation_check.*` are unfinished work of the killed runs on
tickets 01, 02 and 03, with no PASS record. Those tickets run again from their steps; a worker may
read what is there but the step's own gate decides what stays.

What the orchestrator does between phases:

1. After A: read the mark-2 T1 record under `numerical_v4/checks/` for the sign of the run-up
   share across the κ grid; append a dated note to the E2 section of `empirics/spec.md` stating
   that direction; commit Phase A files one concern per commit (code, proofs, empirics, lit,
   spec note); update ticket statuses.
2. After B: commit results and figures.
3. After C: commit the paper.
4. After D: commit, push `v5`, write `.scratch/v5-paper/session_note.md`.

Any STOP ends the session's build. The judgment goes to Austin before anything else.
