export const meta = {
  name: 'v5-phase-b',
  description: 'Phase B: E2 run and link audit, figures at order size two',
  phases: [{ title: 'E2' }, { title: 'Figures' }],
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
function isRateLimit(o) {
  const s = o == null ? "" : (typeof o === "string" ? o : String(o.summary || o.reasons || ""))
  return /RATE_LIMIT/.test(s)
}
function parseReply(txt, schema) {
  if (!schema) return txt
  if (txt && typeof txt === "object") return txt
  try { const m = String(txt).match(/\{[\s\S]*\}/); return JSON.parse(m[0]) }
  catch (e) { return schema === VERDICT ? { verdict: "FAIL", reasons: "unparseable dispatcher reply: " + String(txt).slice(0, 500) } : { status: "FAIL", summary: "unparseable dispatcher reply: " + String(txt).slice(0, 500), files_changed: [], evidence: "" } }
}
async function run(role, prompt, o) {
  o = o || {}
  const r = ROLE[role]
  if (!r) throw new Error("unknown role " + role)
  const once = async (target) => {
    if (target === "opus") return agent(prompt, { model: "opus", effort: o.effort, schema: o.schema, label: o.label, phase: o.phase })
    const head = `effort: ${o.effort || "high"}\n` + (target === "kimi" ? `context: ${o.ctx || "256k"}\n` : "")
    const tail = o.schema ? `\n\nReturn JSON matching this schema and nothing else:\n${JSON.stringify(o.schema)}` : ""
    const txt = await agent(head + prompt + tail, { agentType: target, label: o.label, phase: o.phase })
    return parseReply(txt, o.schema)
  }
  let out = await once(r.agentType || "opus")
  if (isRateLimit(out) && r.fallback) {
    log(`${o.label || role}: provider limit on ${r.agentType}, re-dispatching once to ${r.fallback}`)
    out = await once(r.fallback)
  }
  return out
}
const SALVAGED = { status: "PASS", summary: "salvaged from the previous run", files_changed: [], evidence: "args.done" }
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

const results = {}
results.t08 = DONE.has('08') ? SALVAGED : await attempt('engineer', '08', 'Ticket 08-e2-run-and-link-audit.md, the run. Confirm the dated E2 direction note is present in empirics/spec.md before running; if absent, return FAIL. Run e2 and report every gate value.', { phase: 'E2', effort: 'medium', retryEffort: 'high' })
if (results.t08.status === 'PASS') {
  results.t08a = DONE.has('08 audit') ? SALVAGED : await attempt('auditor', '08 audit', 'Ticket 08-e2-run-and-link-audit.md, the audit. You did not write the link. Do the sixty-case link audit and write gate E2-G2 into e2_estimate.json.', { phase: 'E2', effort: 'medium', retryEffort: 'high' })
}
results.t10 = DONE.has('10') ? SALVAGED : await attempt('engineer', '10', 'Ticket 10-figures.md. Regenerate every figure and report the commands.', { phase: 'Figures', effort: 'medium', retryEffort: 'high' })
const stops = Object.values(results).filter(v => v && v.status === 'STOP')
if (stops.length) log('STOP in Phase B. The orchestrator writes a judgment and waits for Austin.')
return { stop: stops.length > 0, results }
