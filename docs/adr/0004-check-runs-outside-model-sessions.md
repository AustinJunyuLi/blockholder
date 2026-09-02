---
status: accepted
date: 2026-09-02
---
# A check run is a detached job the orchestrator owns, never a model session's wait

At order size two one evaluation of the model takes about six seconds and six gigabytes of
memory, so a check script that visits hundreds of nodes runs for hours and the machine holds at
most two or three such processes at once. Ticket 01 placed those runs inside the session of the
model that had written the code. Four such sessions were stopped or timed out before any of
them reported, while every record they had computed survived on disk. From this date a delegated
step is bounded to minutes: it writes code, runs the quick test, and reports. Each check script
runs as a check run: a background job the orchestrator starts outside the Claude Code client, so
that the client cannot stop it, one at a time on this machine because memory rather than
processor count is the limit, each writing its own log and its own record file. The orchestrator
reads record files. No model waits on a computation. Verification of a run reads its record and
recomputes one node; it never repeats the run.

The suite carries only the records the paper cites. A block whose premise holds at order size one
only, the chord route through the ternary pooled law that ADR 0003 retired, reports not
applicable at order size two instead of failing. The thirty-seed existence check is out of the
suite: nothing the paper states cites it, and the existence attempt of ticket 05 carries its own
condition check. A parallel process pool and a remote machine were considered and deferred: the
two runs the paper needs cost under two hours in sequence.
