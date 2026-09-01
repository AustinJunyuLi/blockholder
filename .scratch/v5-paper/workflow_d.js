export const meta = {
  name: 'v5-phase-d',
  description: 'Phase D: one referee pass, one author fix pass, compile and deliver',
  phases: [{ title: 'Referee' }, { title: 'Fix' }, { title: 'Deliver' }],
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

const ref = await agent(`${PRE}\n\nTicket 12-referee.md. You wrote nothing in this session. Referee deliverable-quality: read paper.pdf and appendix.pdf (render pages to images if needed), write .scratch/v5-paper/referee_report.md with blocking and minor lists, each with a location. Do not edit the paper.`, { model: 'opus', effort: 'medium', schema: RESULT, label: '12 referee', phase: 'Referee' })
const fix = await agent(`${PRE}\n\nTicket 13-author-fix.md. Fix every blocking item and every minor item in .scratch/v5-paper/referee_report.md that needs no new result. Mark each item fixed or STOP with the reason, in the report file. Rerun the number guard. Return STOP if any blocking item needs a new theorem or a new run.`, { model: 'opus', effort: 'high', schema: RESULT, label: '13 fix', phase: 'Fix' })
let deliver = null
if (fix && fix.status === 'PASS') {
  deliver = await attempt('14', 'Ticket 14-compile-and-deliver.md. Compile, inspect every page, apply the unslop gate, copy the PDFs to deliverable/.', { phase: 'Deliver' })
}
const ok = fix && fix.status === 'PASS' && deliver && deliver.status === 'PASS'
if (!ok) log('STOP in Phase D. The orchestrator writes a judgment and waits for Austin.')
return { stop: !ok, referee: ref, fix, deliver }
