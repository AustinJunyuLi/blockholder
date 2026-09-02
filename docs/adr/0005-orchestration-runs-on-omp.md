---
status: superseded by ADR-0006
date: 2026-09-02
---
# Orchestration runs on omp native subagents, not on the Claude Code wrap

From this date the delivery session dispatches its allies as omp agents instead of through
the Claude Code wrap. The wrap put two things between the orchestrator and the worker: a
Claude model, which could answer in the worker's place, and an Anthropic-format shim, which
left the proof of which model answered resting on a usage line the wrap printed. omp spawns
each role as an agent whose process is bound to its provider and logs `model_change` and
`credential_pin` per child, so the model that answered is a fact of the runtime rather than
a claim of the wrapper. Strict output schemas, validated rather than asked for, replace the
wrap's contract of exit codes and text parsing. The roles map to agents: grok authors and
maps, glm engineers and audits, opus judges, with effort carried in the agent files because
eval's `agent()` takes no effort argument. Kimi was dropped when the coding plan expired.

Composite steps run as eval-cell DAGs in the orchestrator session: one cell sequences the
dispatches of an attempt or a two-pass gate, and the chains of a phase are async functions
run together, one cell per phase, except that a chain with a check run in its middle is cut
at that boundary into separate cells so the run is started detached as ADR 0004 requires.
The repo's `.omp/config.yml` turns on `eval.autoBackground`, so a long cell becomes a managed
job and the orchestrator keeps its turn for check runs and commits. Phases, check runs,
commits and the STOP judgment stay with the orchestrator, as they did under the wrap. The
research behind the shape, with the mapping from run-book concepts to omp primitives, is
`docs/omp_orchestration_2026-09.md`.

The dispatch helper carries the guards. A step whose record file already reports PASS or
ABSENT is never rerun. A thrown dispatch error becomes a FAIL report, so a chain that fails
cannot make `parallel` throw away the outcomes of its siblings. The resolved model of each
child is read from the transcript omp retains for it and compared with the model the agent
pins; a mismatch is a failed dispatch. A provider limit is an explicit re-dispatch to the
fallback role by the orchestrator, not a fallback chain in frontmatter, so no silent model
switch. One gap is known: an agent whose model cannot be resolved falls through to the
parent session model, and the resolved-model check is the guard that catches it.
