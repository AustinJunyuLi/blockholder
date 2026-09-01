# Kickoff for the delivery session

Paste this as the first message of a fresh Claude Code session started in
`/Users/austinli/Projects/blockholder_v5` with Fable 5.1 as the model.

> Use a workflow. Read CLAUDE.md, CONTEXT.md and .scratch/v5-paper/spec.md. Workers run on three
> providers through agent types kimi, glm and opus; the role table at the top of each script
> decides which. First, commit the rewritten workflow scripts and KICKOFF.md as one commit. Then
> salvage: the killed run lives in ~/.claude/projects/-Users-austinli-Projects-
> blockholder-v4/fa1ebbf1-9665-45cb-b8ab-f623d293f851/subagents/workflows/wf_d074b870-c81/. If it
> has a journal.jsonl read that; otherwise read each agent-*.jsonl there and take the input of its
> last StructuredOutput call (the ticket is named in the first user message). Tickets 04, 06, 07
> and 09 ended PASS there; confirm, commit their files from the working tree one concern per
> commit, and pass those labels as args.done when you launch workflow_a.js. A ticket without a
> PASS record runs again. Then run .scratch/v5-paper/workflow_a.js to workflow_d.js in order with
> the Workflow tool (scriptPath, absolute), committing between phases as the spec says. Load the
> workflow-authoring skill before the first run. You own git; workers run none. If any phase
> returns stop: true, write the one-page judgment and wait for me. Deliver paper.pdf and
> appendix.pdf.

Before sending it: open `/config` and raise "Dynamic workflow size" above the default guideline
of fifteen agents (Phase A alone spawns about fifteen).
Start this session only after ~/.claude/agents/kimi.md and glm.md exist; agent types load at
session start.

Launch every phase with two args: `done`, the salvaged labels, and `run`, a fresh tag for that
launch (for example `a2`). Each ally dispatch writes to
`~/.claude/ally-runs/<run>/<phase>/<label>-<provider>-<n>/`; the worker runs detached there,
so a dead dispatcher loses nothing, and a reader agent collects the answer from disk. A reused
tag could hand a reader a stale answer, so never reuse one.

What the orchestrator does between phases:

1. After A: read the mark-2 T1 record under `numerical_v4/checks/` for the sign of the run-up
   share across the κ grid; append a dated note to the E2 section of `empirics/spec.md` stating
   that direction; commit Phase A files one concern per commit (code, proofs, empirics, lit,
   spec note); update ticket statuses.
2. After B: commit results and figures.
3. After C: commit the paper.
4. After D: commit, push `v5`, write `.scratch/v5-paper/session_note.md`.

Any `stop: true` ends the session's build. The judgment goes to Austin before anything else.
