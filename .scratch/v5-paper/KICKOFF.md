# Kickoff for the delivery session

Paste this as the first message of a fresh Claude Code session started in
`/Users/austinli/Projects/blockholder_v5` with Fable 5.1 as the model.

> Use a workflow. Read CLAUDE.md, CONTEXT.md and .scratch/v5-paper/spec.md, then run the four
> phases in .scratch/v5-paper/workflow_a.js to workflow_d.js in order with the Workflow tool
> (scriptPath, absolute), committing between phases as the spec says. Load the workflow-authoring
> skill before the first run. You own git; workers run none. If any phase returns stop: true,
> write the one-page judgment and wait for me. Deliver paper.pdf and appendix.pdf.

Before sending it: open `/config` and raise "Dynamic workflow size" above the default guideline
of fifteen agents (Phase A alone spawns about fifteen).

What the orchestrator does between phases:

1. After A: read the mark-2 T1 record under `numerical_v4/checks/` for the sign of the run-up
   share across the κ grid; append a dated note to the E2 section of `empirics/spec.md` stating
   that direction; commit Phase A files one concern per commit (code, proofs, empirics, lit,
   spec note); update ticket statuses.
2. After B: commit results and figures.
3. After C: commit the paper.
4. After D: commit, push `v5`, write `.scratch/v5-paper/session_note.md`.

Any `stop: true` ends the session's build. The judgment goes to Austin before anything else.
