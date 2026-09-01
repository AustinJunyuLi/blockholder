export const meta = {
  name: 'v5-phase-c',
  description: 'Phase C: write the paper, number guard and compile check',
  phases: [{ title: 'Write' }, { title: 'Check' }],
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
  if (w && w.status === "ABSENT") return { status: "ABSENT", ticket: label, write: w }
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
const REDERIVE = (ticket, what) => `Ticket ${ticket}. You are the independent re-deriver. Read only the model section of inherited/draft_v3/draft_v3.tex (that section and nothing else of that file), with the blockholder order set to two noise lumps as .scratch/v5-paper/spec.md section 3 says, and the statement of ${what} as written at the top of the ticket's file under proofs/. Do not read the proof. Re-derive the statement from the model. Return PASS if your derivation reaches the statement as written, FAIL with precise reasons otherwise (a missing hypothesis, a step you cannot justify, a counterexample).`

const CHECK = 'Ticket 11, checker. Run PYTHONPATH=. .venv/bin/python -m empirics.test_fingerprints and the compile sequence in CLAUDE.md. Then grep paper.tex and appendix.tex for any reference to earlier versions, dropped results, attempts, or the inherited draft, and for any label stronger than the one the result holds. Return PASS only if the number guard is green, both files compile with zero errors, undefined references, or citations, and the grep finds nothing. Otherwise FAIL with the exact lines.'
let w = await attempt('11', 'Ticket 11-paper-writer.md. Write paper.tex, appendix.tex and paper.bib as the ticket says. Apply the unslop rules to the prose.', { phase: 'Write', effort: 'high' })
let c = null
if (w.status === 'PASS') {
  c = await agent(`${PRE}\n\n${CHECK}`, { model: 'opus', schema: VERDICT, label: '11 check', phase: 'Check' })
  if (!(c && c.verdict === 'PASS')) {
    log('11: checker FAIL; one fix')
    w = await agent(`${PRE}\n\nTicket 11, fix pass. The checker reported: ${c ? c.reasons : 'no report'}. Fix exactly those items in paper.tex, appendix.tex, paper.bib.`, { model: 'opus', effort: 'high', schema: RESULT, label: '11 fix', phase: 'Write' })
    c = await agent(`${PRE}\n\n${CHECK}`, { model: 'opus', schema: VERDICT, label: '11 check 2', phase: 'Check' })
  }
}
const ok = w && w.status === 'PASS' && c && c.verdict === 'PASS'
if (!ok) log('STOP in Phase C. The orchestrator writes a judgment and waits for Austin.')
return { stop: !ok, write: w, check: c }
