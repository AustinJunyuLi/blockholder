export const meta = {
  name: 'v5-phase-d',
  description: 'Phase D: one referee pass, one author fix pass, compile and deliver',
  phases: [{ title: 'Referee' }, { title: 'Fix' }, { title: 'Deliver' }],
}
const RESULT = { type: "object", required: ["status", "summary", "files_changed", "evidence"], properties: { status: { type: "string", enum: ["PASS", "FAIL", "ABSENT", "STOP"] }, summary: { type: "string" }, files_changed: { type: "array", items: { type: "string" } }, evidence: { type: "string" }, named_condition: { type: "string" } } }
const VERDICT = { type: "object", required: ["verdict", "reasons"], properties: { verdict: { type: "string", enum: ["PASS", "FAIL"] }, reasons: { type: "string" } } }
const ROLE = {
  author:   { agentType: "kimi", fallback: "opus" },
  writer:   { agentType: "kimi", fallback: "opus" },
  engineer: { agentType: "glm",  fallback: "kimi" },
  auditor:  { agentType: "glm",  fallback: "kimi" },
  judge:    { model: "opus" },
}
const DONE = new Set(((args && args.done) || []).map(String))
// Every ally dispatch writes into a fixed directory named by run tag, phase and label. The
// worker runs detached there, so a dead dispatcher never loses an answer: a reader agent picks
// it up from disk. Pass a fresh args.run on every launch so no stale answer can be read.
const RUNS = `/Users/austinli/.claude/ally-runs/${(args && args.run) || "r0"}/d`
const SEQ = {}
function slug(s) { return String(s).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") }
function isRateLimit(o) {
  const s = o == null ? "" : (typeof o === "string" ? o : String(o.summary || o.reasons || ""))
  return /RATE_LIMIT/.test(s)
}
function hasProvenance(o, schema) {
  if (schema) return !!(o && typeof o === "object" && o.dispatch && o.dispatch.model)
  return /\[dispatch model=\S+ rc=0/.test(String(o == null ? "" : o))
}
function parseReply(txt, schema) {
  if (!schema) return txt
  if (txt && typeof txt === "object") return txt
  try { const m = String(txt).match(/\{[\s\S]*\}/); return JSON.parse(m[0]) }
  catch (e) { return schema === VERDICT ? { verdict: "FAIL", reasons: "unparseable dispatcher reply: " + String(txt).slice(0, 500) } : { status: "FAIL", summary: "unparseable dispatcher reply: " + String(txt).slice(0, 500), files_changed: [], evidence: "" } }
}
const READER = (dir) => `You are a reader, not a worker. Do not think about any task and do not read any project file. A detached worker writes its answer into ${dir}. First run: test -f "${dir}/task.txt" && echo started || echo never-started . If it prints never-started, your final message is: DISPATCH FAIL: worker never started in ${dir}. Otherwise wait with one Bash call at a time, timeout parameter 600000: until [ -f "${dir}/done.txt" ]; do sleep 15; done; cat "${dir}/done.txt" . Run that call again each time it returns without a number, at most 30 times. When it prints 0, your final message is the entire contents of ${dir}/stdout.txt, verbatim, nothing added or removed. When it prints 3, return DISPATCH RATE_LIMIT followed by the contents of ${dir}/stderr.txt. Any other number: DISPATCH FAIL followed by the contents of ${dir}/stderr.txt. If done.txt never appears, return: DISPATCH FAIL: no done.txt in ${dir}.`
async function run(role, prompt, o) {
  o = o || {}
  const r = ROLE[role]
  if (!r) throw new Error("unknown role " + role)
  const once = async (target) => {
    if (target === "opus") return agent(prompt, { model: "opus", effort: o.effort, schema: o.schema, label: o.label, phase: o.phase })
    const key = `${slug(o.label || role)}-${target}`
    SEQ[key] = (SEQ[key] || 0) + 1
    const dir = `${RUNS}/${key}-${SEQ[key]}`
    const head = `effort: ${o.effort || "high"}\n` + (target === "kimi" ? `context: ${o.ctx || "256k"}\n` : "") + `artifact-dir: ${dir}\n`
    const tail = o.schema ? `\n\nReturn JSON matching this schema and nothing else:\n${JSON.stringify(o.schema)}` : ""
    let out = parseReply(await agent(head + prompt + tail, { agentType: target, label: o.label, phase: o.phase }), o.schema)
    if (!hasProvenance(out, o.schema) && !isRateLimit(out)) {
      log(`${o.label || role}: no ${target} provenance in the dispatcher reply; a reader collects ${dir}`)
      out = parseReply(await agent(READER(dir), { model: "sonnet", effort: "low", label: `${o.label || role} reader`, phase: o.phase }), o.schema)
    }
    return out
  }
  let out = await once(r.agentType || "opus")
  if (isRateLimit(out) && r.fallback) {
    log(`${o.label || role}: provider limit on ${r.agentType}, re-dispatching once to ${r.fallback}`)
    out = await once(r.fallback)
  }
  return out
}
const W = "/Users/austinli/Projects/blockholder_v5"
const PRE = `Work in ${W}. Read CLAUDE.md, CONTEXT.md and .scratch/v5-paper/spec.md first, then the ticket named below under .scratch/v5-paper/issues/. Run no git command. Edit only the paths the ticket names and report every file you changed. The paper states positive results only: never write a sentence that refers to the inherited draft, earlier versions, dropped results, or attempts. Prose never promotes an honesty label. If a step fails, report FAIL with the output; do not work around a gate or a spec.`
async function attempt(role, label, prompt, opts) {
  const o = Object.assign({ schema: RESULT }, opts || {})
  const re = o.retryEffort; delete o.retryEffort
  const r1 = await run(role, `${PRE}\n\n${prompt}`, Object.assign({}, o, { label }))
  if (r1 && (r1.status === "PASS" || r1.status === "ABSENT")) return r1
  log(`${label}: first attempt ${r1 ? r1.status : "null"}; one retry`)
  const r2 = await run(role, `${PRE}\n\nThis is the single retry of ${label}. The first attempt reported: ${JSON.stringify(r1)}. You may change one assumption or one design choice to a cleaner one; say exactly what you changed and why in your summary.\n\n${prompt}`, Object.assign({}, o, { label: `${label} retry` }, re ? { effort: re } : {}))
  if (r2 && (r2.status === "PASS" || r2.status === "ABSENT")) return r2
  return { status: "STOP", ticket: label, first: r1, second: r2 }
}

const ref = await run('judge', `${PRE}\n\nTicket 12-referee.md. You wrote nothing in this session. Referee deliverable-quality: read paper.pdf and appendix.pdf (render pages to images if needed), write .scratch/v5-paper/referee_report.md with blocking and minor lists, each with a location. Do not edit the paper.`, { effort: 'high', schema: RESULT, label: '12 referee', phase: 'Referee' })
const fix = await run('judge', `${PRE}\n\nTicket 13-author-fix.md. Fix every blocking item and every minor item in .scratch/v5-paper/referee_report.md that needs no new result. Mark each item fixed or STOP with the reason, in the report file. Rerun the number guard. Return STOP if any blocking item needs a new theorem or a new run.`, { effort: 'high', schema: RESULT, label: '13 fix', phase: 'Fix' })
let deliver = null
if (fix && fix.status === 'PASS') {
  deliver = await attempt('engineer', '14', 'Ticket 14-compile-and-deliver.md. Compile, inspect every page, apply the unslop gate, copy the PDFs to deliverable/.', { phase: 'Deliver', effort: 'medium', retryEffort: 'high' })
}
const ok = fix && fix.status === 'PASS' && deliver && deliver.status === 'PASS'
if (!ok) log('STOP in Phase D. The orchestrator writes a judgment and waits for Austin.')
return { stop: !ok, referee: ref, fix, deliver }
