export const meta = {
  name: 'v5-phase-b',
  description: 'Phase B: E2 run and link audit, figures at order size two',
  phases: [{ title: 'E2' }, { title: 'Figures' }],
}
const RESULT = { type: "object", required: ["status", "summary", "files_changed", "evidence"], properties: { status: { type: "string", enum: ["PASS", "FAIL", "ABSENT", "STOP"] }, summary: { type: "string" }, files_changed: { type: "array", items: { type: "string" } }, evidence: { type: "string" }, named_condition: { type: "string" } } }
const VERDICT = { type: "object", required: ["verdict", "reasons"], properties: { verdict: { type: "string", enum: ["PASS", "FAIL"] }, reasons: { type: "string" } } }
const W = "/Users/austinli/Projects/blockholder_v5"
const PRE = `Work in ${W}. Read CLAUDE.md, CONTEXT.md and .scratch/v5-paper/spec.md first, then the ticket named below under .scratch/v5-paper/issues/. Run no git command. Edit only the paths the ticket names and report every file you changed. The paper states positive results only: never write a sentence that refers to the inherited draft, earlier versions, dropped results, or attempts. Prose never promotes an honesty label. If a step fails, report FAIL with the output; do not work around a gate or a spec.`
async function attempt(label, prompt, opts) {
  const o = Object.assign({ model: "opus", schema: RESULT }, opts || {})
  const r1 = await agent(`${PRE}\n\n${prompt}`, Object.assign({}, o, { label }))
  if (r1 && (r1.status === "PASS" || r1.status === "ABSENT")) return r1
  log(`${label}: first attempt ${r1 ? r1.status : "null"}; one retry`)
  const r2 = await agent(`${PRE}\n\nThis is the single retry of ${label}. The first attempt reported: ${JSON.stringify(r1)}. You may change one assumption or one design choice to a cleaner one; say exactly what you changed and why in your summary.\n\n${prompt}`, Object.assign({}, o, { label: `${label} retry` }))
  if (r2 && (r2.status === "PASS" || r2.status === "ABSENT")) return r2
  return { status: "STOP", ticket: label, first: r1, second: r2 }
}
async function twoPass(label, writePrompt, rederivePrompt) {
  let w = await agent(`${PRE}\n\n${writePrompt}`, { model: "opus", effort: "high", schema: RESULT, label: `${label} write` })
  if (!w || w.status !== "PASS") return { status: "STOP", ticket: label, stage: "write", report: w }
  let v = await agent(`${PRE}\n\n${rederivePrompt}`, { model: "opus", effort: "high", schema: VERDICT, label: `${label} re-derive` })
  if (v && v.verdict === "PASS") return { status: "PASS", ticket: label, write: w, verdict: v }
  log(`${label}: re-deriver FAIL; one fix`)
  w = await agent(`${PRE}\n\nAn independent re-deriver returned FAIL with these reasons: ${v ? v.reasons : "no report"}. Fix the proof once. You may replace one assumption with a cleaner one; say so in your summary.\n\n${writePrompt}`, { model: "opus", effort: "high", schema: RESULT, label: `${label} fix` })
  if (!w || w.status !== "PASS") return { status: "STOP", ticket: label, stage: "fix", report: w }
  v = await agent(`${PRE}\n\n${rederivePrompt}`, { model: "opus", effort: "high", schema: VERDICT, label: `${label} re-derive 2` })
  if (v && v.verdict === "PASS") return { status: "PASS", ticket: label, write: w, verdict: v }
  return { status: "STOP", ticket: label, stage: "re-derive", report: v }
}
const REDERIVE = (ticket, what) => `Ticket ${ticket}. You are the independent re-deriver. Read only the model section (the inherited model restated with order size two, as described in .scratch/v5-paper/spec.md section 3) and the statement of ${what} as written in appendix.tex. Do not read the proof. Re-derive the statement from the model. Return PASS if your derivation reaches the statement as written, FAIL with precise reasons otherwise (a missing hypothesis, a step you cannot justify, a counterexample).`

const results = {}
results.t08 = await attempt('08', 'Ticket 08-e2-run-and-link-audit.md, the run. Confirm the dated E2 direction note is present in empirics/spec.md before running; if absent, return FAIL. Run e2 and report every gate value.', { phase: 'E2' })
if (results.t08.status === 'PASS') {
  results.t08a = await attempt('08 audit', 'Ticket 08-e2-run-and-link-audit.md, the audit. You did not write the link. Do the sixty-case link audit and write gate E2-G2 into e2_estimate.json.', { phase: 'E2' })
}
results.t10 = await attempt('10', 'Ticket 10-figures.md. Regenerate every figure and report the commands.', { phase: 'Figures' })
const stops = Object.values(results).filter(v => v && v.status === 'STOP')
if (stops.length) log('STOP in Phase B. The orchestrator writes a judgment and waits for Austin.')
return { stop: stops.length > 0, results }
