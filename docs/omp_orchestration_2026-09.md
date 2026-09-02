# omp orchestration primitives, September 2026

Research note for moving the v5 delivery session off the Claude Code wrap (kimi-dispatch and glm-dispatch
shell scripts, Opus subagents through the Agent tool) onto omp's native orchestration: can the run book in
`.scratch/v5-paper/orchestration.md` be expressed with omp primitives, and what changes character when it is.
Claims cite `omp://<name>.md` or a path under `~/node_modules/@oh-my-pi/pi-coding-agent/` (abbreviated
`src/`); unknowns are marked.

Referee corrections: refereed by Opus 5 on 2026-09-02 and corrected; findings in the session transcript.

## 1. Model routing

A dispatch lands on a model by precedence: `task.agentModelOverrides[agentName]`, then the agent file's
frontmatter `model` list, then the parent session's active model with its configured fallback
(omp://task-agent-discovery.md, "Model and structured-output precedence"; src/task/structured-subagent.ts:282-295).
Frontmatter `model` accepts one selector, a CSV, or an array, tried in order; `@role` aliases expand through
`modelRoles` (omp://task-agent-discovery.md, "Agent definition shape" and "Role-backed custom agents").
`modelRoles.<role>` values live in `~/.omp/agent/config.yml` or the project `.omp/config.yml` and may carry a
thinking suffix such as `:high` (omp://settings.md:333-359; omp://config-usage.md section 4). A run-book role
becomes `.omp/agents/author.md` with `model: "@author"`; the concrete provider string lives only in
`modelRoles.author`.

After-the-fact proof of which model ran, per message, on disk, and surviving the session:

- `SingleResult.resolvedModel` and `resolvedModelIsFallback` on every task result (omp://tools/task.md,
  Outputs; src/task/executor.ts:2344-2345).
- The child's session file `<id>.jsonl` in the parent's artifacts dir (omp://tools/task.md, "Artifacts and
  side channels"): the session file path minus the `.jsonl` suffix
  (src/session/session-manager.ts:110-113, 2102-2106), under
  `~/.omp/agent/sessions/<encoded-cwd>/<timestamp>_<sessionId>.jsonl` (omp://session.md, "On-Disk Layout").
- Inside that JSONL: `message` entries record `provider` and `model` (omp://session.md, `message` entry),
  `model_change` entries record the active model per role with an optional `resolvedModelIsFallback` flag
  (src/session/session-entries.ts:103-111), `credential_pin` entries record the provider and a hashed account
  identity (omp://session.md, `credential_pin`), and `model_usage` entries record purpose, role, provider,
  model, and token usage for off-transcript calls (src/session/session-entries.ts:78-90).

## 2. Effort per step

Three mechanisms, in increasing exactness:

- Per-item coarse effort. With `task.enableEffort: true` (default false;
  src/config/settings-schema.ts:4983-4986) each task item takes `effort: "lo" | "med" | "hi"`, mapped onto the
  resolved model's supported ladder: `lo` the lowest, `med` the middle (lower of two middles), `hi` the
  highest (src/thinking.ts:284-311; omp://tools/task.md, Inputs). The result is clamped to `task.maxEffort`
  (default `max`; src/config/settings-schema.ts:5107-5110), the ceiling survives retry-fallback model switches
  (src/task/executor.ts:3046-3052), and a model with no supported effort at or below the ceiling fails the
  spawn (omp://task-agent-discovery.md).
- Frontmatter `thinking-level` / `thinking` on the agent file sets an exact selector; a per-item `effort`
  overrides it (omp://task-agent-discovery.md).
- A `:level` suffix on any model selector, e.g. `anthropic/claude-opus-4-8:high`, valid in frontmatter
  `model`, `modelRoles` values, and `task.agentModelOverrides` (omp://settings.md:333;
  src/config/model-resolver.ts:734-746).

The run book names four levels (low, medium, high, xhigh); the coarse `lo|med|hi` triplet is too coarse, so
the exact mechanism is the `:level` suffix or frontmatter `thinking-level`. Thinking ladders are per model:
Kimi K3 (k3, k3-256k) and GLM 5.3 declare low, high, max; Opus 5 declares low, medium, high, xhigh, max; an
undeclared level silently clamps down to the nearest declared one (pi-catalog/src/model-thinking.ts), so
effort-variant agents exist only at declared levels. Eval's `agent()` accepts no effort argument
(src/eval/agent-bridge.ts:24-46), so eval-driven DAGs bake effort into the agent definition.

## 3. Structured output

Each task item takes `outputSchema` (JSON Schema) and `schemaMode` (`permissive` default, or `strict`).
Precedence: per-item schema, then agent frontmatter `output`, then the inherited parent session schema
(omp://tools/task.md, Inputs; src/task/structured-subagent.ts:176-188). The child finishes through a hidden
`yield` tool whose payload is validated against the schema. An invalid yield is a tool error the child sees
and can correct; six consecutive invalid yields stop the run (src/task/executor.ts:965, 1560-1589). A child
that never yields gets up to three reminders, the last forcing `toolChoice = yield`
(src/task/executor.ts:1915, 1982-2006; omp://tools/task.md, Flow step 14). At finalization, `strict` rejects
invalid data with exit code 1 and a `schema_violation` payload; `permissive` rejects a plain validation
failure too and only an agent-overridden or invalid schema downgrades to a warning
(src/task/executor.ts:710-716). The parent receives parsed data as `SingleResult.structuredOutput.data` with
source, mode, and validation status (omp://tools/task.md, Outputs). In a JS cell, `agent()` resolves to the
parsed data itself (the text when no schema); with `handle: true` it resolves to `{ text, output, handle, id,
agent, data }` and carries no model field (src/eval/js/shared/prelude.txt:102-126; omp://tools/eval.md,
`agent()`). The RESULT and VERDICT schemas of the run book map directly onto per-item `outputSchema` with
`schemaMode: "strict"`.

## 4. Failover

A prioritized frontmatter `model` list makes the first resolvable entry the primary and the rest the spawn's
own retry-fallback chain (omp://settings.md, retry section: "Subagents get their own per-spawn chains";
src/task/executor.ts:2987-3032). On a rate limit or quota error the session retries with capped jittered
backoff, rotates credentials, honors provider retry hints, then switches down the fallback chain with zero
delay; defaults are 10 retries and a 5-minute delay ceiling (omp://non-compaction-retry-policy.md). Fallbacks
are visible: `resolvedModelIsFallback` appears on progress, on the result, and on `model_change` entries
(src/task/executor.ts:1756-1763, 2344-2345; src/session/session-entries.ts:109-110), and retry events
(`auto_retry_start`, `retry_fallback_applied`) are emitted and persisted
(omp://non-compaction-retry-policy.md).

Forbidding silent fallback to the parent model is only partly supported; three paths land there.
`retry.modelFallback: false` disables the mid-turn retry fallback (omp://settings.md, retry table). Second,
auth fallback: a subagent model with no working credential silently yields the parent's active model, with
only a log warning and no off switch (src/config/model-resolver.ts:1560-1596;
src/task/executor.ts:3017-3024). Third, an unmapped built-in alias: `@task` is accepted as a role
(src/config/model-roles.ts:22-32, 55-66) even with no `modelRoles` entry, finds no configured, inherited, or
priority default (src/config/model-resolver.ts:1090-1092, 1155-1189), and falls through to the parent's
active model (src/config/model-resolver.ts:1258-1260) with no warning, and `resolvedModelIsFallback` stays
false. The only guard is procedural: compare the requested selector against the child's `model_change` entry
and treat a mismatch as a failed dispatch (the run book's exit-3 rule). A cell reaches that entry through
`handle: true`: keep the returned `id` and match the `model_change` line in the child's session JSONL under
`~/.omp/agent/sessions/`, which records the model as `<provider>/<id>` with no level suffix.

## 5. Concurrency and DAGs

One `task` call with `tasks[]` spawns one subagent per item under a shared required `context`; with
`async.enabled=true` each is a background job whose result self-delivers (omp://tools/task.md). A
session-scoped semaphore resized live from `task.maxConcurrency` (default 32) bounds the total fan-out
(omp://tools/task.md, Limits; omp://tools/eval.md, Limits). An agent with `blocking: true` frontmatter runs
inline while batch siblings stay background (omp://tools/task.md). Inside eval, `agent(prompt, {...})` runs
one subagent, `parallel(thunks)` runs a bounded pool, and `pipeline(items, ...stages)` applies stages as
barriered waves; every item settles, then the lowest-index error is thrown and the results array is discarded
(src/eval/js/shared/prelude.txt:147-166; omp://tools/eval.md). The cancel-siblings pool in
`src/task/parallel.ts` is the task tool's internal pool; eval never calls it. Artifacts pass between parent
and workers through the shared `local://` root (omp://tools/task.md, Notes), and `hub` provides steering
(`send`) and barrier waits (`wait`) against live, idle, or parked agents (omp://tools/hub.md). There is no
general per-provider concurrency cap: the provider semaphore exists only for `ollama-cloud` and brackets the
streaming request, not the agent's lifetime (src/task/provider-concurrency.ts:1-12, 19-21); Kimi, GLM, and
Anthropic fan-out is limited only by `task.maxConcurrency`.

## 6. Worker guardrails

- Tool restriction: agent frontmatter `tools:` fixes the child's tool list (`yield` is added automatically);
  omitting `bash` and `eval` removes the shell, hence git (omp://task-agent-discovery.md).
  `src/task/read-only-policy.ts:10-30` defines the recognized read-only tool set used for read-only tagging.
- Hooks and extensions: a `tool_call` handler can block any call, for example a bash command containing
  `git`, and a throwing handler fails closed (omp://hooks.md; omp://extensions.md).
- Approval mode is not the mechanism for workers: subagents are forced to `tools.approvalMode: yolo` because
  they are headless, while a user `tools.approval.<tool>: deny` stays authoritative and `prompt` rejects
  outright in a headless child (omp://approval-mode.md, Subagents; omp://tools/task.md, Flow step 12).
- Files changed: omp adds no changed-file report beyond artifact paths, so the run book's `files_changed`
  field in the RESULT schema remains the carrier, now schema-enforced (question 3).

## 7. Detached long runs

ADR 0004 requires that no model session waits on a computation: the orchestrator starts the check script
detached, one at a time, and reads its record file later
(docs/adr/0004-check-runs-outside-model-sessions.md). omp fits this with `hub` op `start`: a named,
project-scoped supervised process with readiness matching on log regex or port, log following by cursor, and
`detached: true`, which survives broker shutdown and every omp exit (omp://tools/hub.md, process sections).
The `.rc`-file check maps to the orchestrator reading the log or record file on its next turn; no model
polls. The one-at-a-time rule stays operator discipline: omp has no memory-aware job scheduler (question 5).
`omp -p --mode json --max-time <dur>` runs a bounded headless session (omp://cli-reference.md, "Headless /
print mode"), but a headless omp run is itself a model session, not the vehicle for hours-long check runs.

A gate cell coexists with these detached runs: `eval.autoBackground.enabled` (default false; threshold
`eval.autoBackground.thresholdMs`, default 60000) turns a cell that outlives the threshold into a managed
async job and returns the turn (omp://tools/eval.md); this repo sets it in `.omp/config.yml`.

## 8. Failure and stop semantics

A failed child surfaces as `SingleResult.exitCode = 1` with `error` and `stderr`; a background job is marked
failed while the agent stays registered and interrogable (omp://tools/task.md, Errors). Wall-clock and
activity bounds exist per spawn: `task.maxRuntimeMs` (default off) and `task.softRequestBudget` (default 200
requests, force-stopped at 1.5x with a wrap-up yield) (omp://tools/task.md, Limits). On context overflow a
worker is recovered in place, not failed: child sessions inherit parent settings (omp://tools/task.md, Flow
step 12), `compaction.enabled` defaults true, and overflow triggers context promotion then compaction with
retry (omp://compaction.md). In eval, any subagent failure raises into the cell as an error
(src/eval/agent-bridge.ts:168-174), so "fail twice, stop" is ordinary control flow: catch, count, throw on
the second failure; with task batches the rule lives in the orchestrator across turns. The real gap against
the run book's STOP: eval `parallel`/`pipeline` let every sibling run to completion, but a throw then
discards the entire results array, so each chain must catch and report its own record; task batches match the
run book because each job is independent and the orchestrator simply stops spawning.

## 9. Persistence

Finished subagents go `idle` with the session attached, park after `task.agentIdleTtlMs` (default 7 minutes),
and revive on a `hub` message; transcripts persist as `<id>.jsonl` and render through `history://<id>`
(omp://tools/task.md, Flow steps 15-16). Cold revival after a restart rebuilds the subagent from its
persisted `session_init` entry, which carries tools, system prompt, schema, and spawn policy
(src/task/persisted-revive.ts:41-56); the orchestrator resumes with `--continue` or `--resume`
(omp://cli-reference.md). Lost on restart: in-flight background jobs and their delivery, which are in-process
(omp://tools/hub.md). Unknown: whether a task spawn caught mid-turn lands parked or aborted; the artifact
files persist either way. The run book's idempotence rule ("result.txt with PASS or ABSENT exists, never
rerun") has no native equivalent: the driver reads `runs/<label>/result.txt` before dispatching.

## 10. What omp calls a workflow

There is no first-class workflow or DAG object. `src/task/commands.ts:17-24, 65-125` defines a
`WorkflowCommand` as a markdown file (frontmatter plus a `$@`-expanded body template) discovered from
`.omp`/`.pi`/`.claude` command directories, surfacing as slash commands that expand into prompt text
(omp://slash-command-internals.md, section 6); vibe mode is a director pattern over persistent workers, not a
DAG (omp://vibe-mode.md). The DAG surfaces are eval cells (`agent` + `parallel` + `pipeline`),
orchestrator-driven `task` batches with `hub` waits, an extension registering commands and tools
(omp://extensions.md), or an external driver over the SDK or stdio RPC (omp://sdk.md; omp://rpc.md).

## Mapping

| Run-book concept | omp primitive | Gap |
|---|---|---|
| Role (author, engineer, judge) | Agent file `.omp/agents/<role>.md` with frontmatter `model`, `thinking-level`, `tools` | None |
| Provider per role | Frontmatter `model` list or `@role` alias into `modelRoles`; `task.agentModelOverrides` wins | Auth fallback to the parent model has no off switch (question 4) |
| Effort per step | `:level` suffix or frontmatter `thinking-level` for exact levels; per-item `effort` needs `task.enableEffort: true` and is only `lo\|med\|hi` | Eval `agent()` takes no effort; bake it into the agent file. Undeclared levels clamp down silently, so variants exist only at declared levels |
| Context 256k vs 1m | None per spawn; pick the model id with the larger window. After Kimi expired this session uses `xai-oauth/grok-4.6` (500000 context). `extendedContext` gates premium long-context billing (src/config/settings-schema.ts:2477-2490) | None |
| RESULT / VERDICT schema | Per-item `outputSchema` with `schemaMode: "strict"` | None; validation is enforced, not asked for |
| Attempt with one retry | No native equivalent; eval control flow or orchestrator turns | Carried in code, not in a dispatch flag |
| Two-pass gate | One eval cell sequencing four `agent()` calls, or four sequenced task items | None structural |
| STOP (fail twice) | No native halt; eval: throw after the second failure; batches: orchestrator stops spawning and judges | A `parallel`/`pipeline` throw discards all sibling results; each chain must catch and report |
| Phase barrier | `pipeline` stages, or the orchestrator's turn boundary between batches | None |
| Check run (detached, one at a time) | `hub` op `start` with `detached: true`; record/log files read later | One-at-a-time is discipline; no memory-aware scheduler |
| Provenance in `runs/<label>/result.txt` | Orchestrator or cell writes the file from parsed `data`; model proof from `resolvedModel` plus the child `<id>.jsonl` | The file convention stays ours; omp supplies stronger proof beside it |

## Recommendation

Options:

- (a) Eval-cell DAGs. Composite steps (attempt, two-pass gate) become one cell each; phases become
  `pipeline` waves. The procedure lives in code, schemas are strict, parsed results are variables the cell
  writes to `runs/<label>/result.txt` itself. Costs: no per-call effort (solved in agent frontmatter), eval
  subagents are one-shot so no `hub` follow-up inside a gate (src/eval/agent-bridge.ts:155), a gate cell
  holds the session's exclusive eval slot and blocks the turn unless `eval.autoBackground.enabled` is on
  (omp://tools/eval.md), the cell timeout pauses while bridged work is in flight so it never bounds a
  dispatch (src/eval/bridge-timeout.ts), the only per-dispatch wall-clock bound is `task.maxRuntimeMs`
  (default 0, off), and intermediate work is off-transcript unless the cell writes it, which the result.txt
  files cover.
- (b) Plain task batches, turn by turn. Closest to the prose run book: every dispatch is a visible job,
  per-item `effort` works, parked workers take `hub` follow-ups, and STOP's "let running dispatches finish"
  holds naturally. Costs: the attempt/gate logic is re-performed by the model at every step instead of being
  executed, and each stage burns orchestrator turns and context.
- (c) Extension or custom command. A `/gate` command plus a no-git `tool_call` hook would be the most
  enforcing option, but it is new TypeScript to maintain, and extensions run in-process where a careless
  background throw can tear down the session (omp://extensions.md); over-built for one paper session.
- (d) Keep the prose run book, change only the dispatch line. Zero migration risk and the exit-code
  semantics are proven, but it keeps the wrap's weak provenance and uses nothing native.

Pick (a), with phases, check runs, commits, and the STOP judgment staying with the orchestrator, as they do
under every option. The reasons are the run book's own: delegated steps are bounded to minutes (CLAUDE.md,
docs/adr/0004), so a four-dispatch gate fits one cell; the gate procedure is mechanical, so it belongs in
code rather than in the model's head; and strict schemas plus parsed `data` remove the parse-the-text
failure mode the shell wrap had. Option (b) is the fallback for steps Austin wants to watch or steer between
stages.

Worked example, the two-pass gate as one eval JS cell. The project agent files carry the model alias in
frontmatter because eval's `agent()` has no effort or model knob; the effort-variant agents `grok-xhigh` and
`opus-xhigh` stand in where the gate defaults call for them. `dispatch` takes the expected model
(`xai-oauth/grok-4.6` for grok, `anthropic/claude-opus-5` for opus) and checks it against the child's
recorded `model_change`; a mismatch or a thrown dispatch becomes a FAIL record rather than aborting the
cell. `tool.task` from a cell is asynchronous (it returns a still-running background job), so it is not the
vehicle for this inline model check.

```js
// Two-pass gate for ticket 05, run book schemas verbatim.
const RESULT = {"type":"object","required":["status","summary","files_changed","evidence"],"properties":{
  "status":{"type":"string","enum":["PASS","FAIL","ABSENT","STOP"]},"summary":{"type":"string"},
  "files_changed":{"type":"array","items":{"type":"string"}},"evidence":{"type":"string"},"named_condition":{"type":"string"}}};
const VERDICT = {"type":"object","required":["verdict","reasons"],"properties":{"verdict":{"type":"string","enum":["PASS","FAIL"]},"reasons":{"type":"string"}}};

// One dispatch, one record file. A finished step (PASS or ABSENT) or a recorded verdict is never rerun.
const { statSync } = await import("node:fs");
const runDir = ".scratch/v5-paper/runs";
const SESSIONS = `${process.env.HOME}/.omp/agent/sessions`;

// Resolved model of a finished agent() child, read from the transcript that handle: true retains.
async function resolvedModelOf(id) {
  let best, bestMtime = -1;
  for await (const p of new Bun.Glob(`**/${id}.jsonl`).scan({ cwd: SESSIONS, absolute: true })) {
    const m = statSync(p).mtimeMs;
    if (m > bestMtime) { best = p; bestMtime = m; }
  }
  if (!best) return undefined;
  const txt = await Bun.file(best).text();
  return txt.match(/"type":"model_change"[^\n]*?"model":"([^"]+)"/)?.[1];
}

async function dispatch(agentName, label, prompt, schema, expectedModel) {
  const path = `${runDir}/${label.replaceAll(" ", "-")}/result.txt`;
  try {
    const done = JSON.parse(await read(path));
    if (done.status === "PASS" || done.status === "ABSENT" || done.verdict !== undefined) return done;
  } catch {}
  const fail = (summary) => ({ status: "FAIL", summary, files_changed: [], evidence: "dispatch error" });
  let result;
  try {
    const h = await agent(prompt, { agent: agentName, label, schema, schemaMode: "strict", handle: true });
    const model = await resolvedModelOf(h.id);
    result = model === expectedModel ? h.data : fail(`resolved model ${model}, expected ${expectedModel}`);
  } catch (err) {
    result = fail(String(err?.message ?? err));
  }
  await write(path, JSON.stringify(result, null, 2));
  return result;
}

async function twoPass(ticket, writePrompt, rederivePrompt) {
  // PRE is the block under "Shared prompt texts" in the run book, held in a const of the cell.
  const send = (p) => `${PRE}\n\n${p}`;
  const authored = await dispatch("grok", `${ticket} write`, send(writePrompt), RESULT, "xai-oauth/grok-4.6");
  if (authored.status === "ABSENT") return { status: "ABSENT", authored };
  if (authored.status !== "PASS") return { status: "STOP", stage: "write", authored };
  const rd1 = await dispatch("opus", `${ticket} re-derive`, rederivePrompt, VERDICT, "anthropic/claude-opus-5");
  if (rd1.verdict === "PASS") return { status: "PASS", authored, rederive: rd1 };
  const fixPrompt = `An independent re-deriver returned FAIL with these reasons: ${rd1.reasons}\n\n${writePrompt}`;
  const fix = await dispatch("grok", `${ticket} fix`, send(fixPrompt), RESULT, "xai-oauth/grok-4.6");
  if (fix.status !== "PASS") return { status: "STOP", stage: "fix", authored, rederive: rd1, fix };
  const rd2 = await dispatch("opus", `${ticket} re-derive 2`, rederivePrompt, VERDICT, "anthropic/claude-opus-5");
  if (rd2.verdict === "PASS") return { status: "PASS", authored, rederive: rd1, fix, rederive2: rd2 };
  return { status: "STOP", stage: "re-derive", authored, rederive: rd1, fix, rederive2: rd2 };
}

// The write prompt and the REDERIVE text come from the run book's Phase A section, as consts.
const outcome = await twoPass("05", WRITE_05, REDERIVE_05);
await write(`${runDir}/05/result.txt`, JSON.stringify(outcome, null, 2));
display(outcome.status); // "STOP" ends the phase; the orchestrator writes the judgment
```

Open checks before adopting: decide the no-git enforcement (frontmatter `tools:` restriction per question 6
is enough for workers that need no shell; a hook for the rest). The selector strings are settled and the
resolved-model check now lives inside `dispatch`, so `retry.modelFallback: false` is the only remaining
fallback decision.
