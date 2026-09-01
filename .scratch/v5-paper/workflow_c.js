export const meta = {
  name: 'v5-phase-c',
  description: 'Phase C: write the paper, number guard and compile check',
  phases: [{ title: 'Write' }, { title: 'Check' }],
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
const RUNS = `/Users/austinli/.claude/ally-runs/${(args && args.run) || "r0"}/c`
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
    const raw = await agent(head + prompt + tail, { agentType: target, label: o.label, phase: o.phase })
    let out = parseReply(raw, o.schema)
    if (!hasProvenance(out, o.schema) && !isRateLimit(out) && !/^\s*DISPATCH FAIL/.test(String(raw == null ? "" : raw))) {
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

const CHECK = 'Ticket 11, checker. Run PYTHONPATH=. .venv/bin/python -m empirics.test_fingerprints and the compile sequence in CLAUDE.md. Then grep paper.tex and appendix.tex for any reference to earlier versions, dropped results, attempts, or the inherited draft, and for any label stronger than the one the result holds. Return PASS only if the number guard is green, both files compile with zero errors, undefined references, or citations, and the grep finds nothing. Otherwise FAIL with the exact lines.'
let w = await attempt('writer', '11', 'Ticket 11-paper-writer.md. Write paper.tex, appendix.tex and paper.bib as the ticket says. Apply the unslop rules to the prose.', { phase: 'Write', effort: 'xhigh', retryEffort: 'max', ctx: '1m' })
let c = null
if (w.status === 'PASS') {
  c = await run('engineer', `${PRE}\n\n${CHECK}`, { effort: 'low', schema: VERDICT, label: '11 check', phase: 'Check' })
  if (!(c && c.verdict === 'PASS')) {
    log('11: checker FAIL; one fix')
    w = await run('writer', `${PRE}\n\nTicket 11, fix pass. The checker reported: ${c ? c.reasons : 'no report'}. Fix exactly those items in paper.tex, appendix.tex, paper.bib.`, { effort: 'high', schema: RESULT, label: '11 fix', phase: 'Write', ctx: '1m' })
    c = await run('engineer', `${PRE}\n\n${CHECK}`, { effort: 'low', schema: VERDICT, label: '11 check 2', phase: 'Check' })
  }
}
const ok = w && w.status === 'PASS' && c && c.verdict === 'PASS'
if (!ok) log('STOP in Phase C. The orchestrator writes a judgment and waits for Austin.')
return { stop: !ok, write: w, check: c }
