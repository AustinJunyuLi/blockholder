export const meta = {
  name: 'v5-phase-a',
  description: 'Phase A: order-size parameter, new proofs, re-derivations, empirics build and E1 run, audit, literature check',
  phases: [
    { title: 'Theory code' },
    { title: 'Proofs' },
    { title: 'Empirics' },
    { title: 'Literature' },
    { title: 'Grid checks' },
  ],
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

// ---- Phase A chains run concurrently; the barrier at the end is real: the orchestrator commits all of it.
const results = {}
const chains = [
  async () => {
    results.t01 = await attempt('01', 'Ticket 01-mark-parameter-and-timed-smoke.md. Build exactly what the ticket says. Report wall time and peak memory for one node at mark=2, H=10, and the diff at mark=1 against numerical_v4/smoke_output.txt.', { phase: 'Theory code' })
    if (results.t01.status !== 'PASS') return
    results.t01v = await agent(`${PRE}\n\nTicket 01, verifier. You did not write the change. Rerun .venv/bin/python -m numerical_v4.smoke and one check script at mark=2 and confirm the numbers in this report match: ${JSON.stringify(results.t01)}. Return PASS or FAIL with reasons.`, { model: 'opus', schema: VERDICT, label: '01 verify', phase: 'Theory code' })
  },
  async () => {
    results.t02 = await twoPass('02',
      'Ticket 02-garbling-lemma-and-threshold-dial.md. Write the garbling lemma and the threshold theorem with their proofs into proofs/02_garbling.tex, statement first. If any bridge clause does not follow from the order-size-two structure, state it as one named condition in the theorem and put its exact mathematical form in the named_condition field of your report; otherwise leave that field empty.',
      REDERIVE('02', 'the garbling lemma and the threshold theorem'))
  },
  async () => {
    results.t03 = await twoPass('03',
      'Ticket 03-who-gets-caught.md. Write the corollary and its proof into proofs/03_caught.tex, statement first. The grid check is a separate agent; do not write it.',
      REDERIVE('03', 'the who-gets-caught corollary'))
  },
  async () => {
    const four = ['the partition and factorisation S = (1 minus Omega) S_P', 'the kappa-invariance of the flagged cell', 'the clock theorem: at fixed policies a shorter clock lowers noise sensitivity iff W_T C_T is at most one', 'the weight leg of the threshold theorem: Omega rises when the threshold tightens at fixed policies']
    results.t04 = await pipeline(four,
      (stmt) => agent(`${PRE}\n\nTicket 04-rederive-inherited-results.md. You are an independent re-deriver who has not read any proof. Derive ${stmt} from the model section of inherited/draft_v3/draft_v3.tex (read only the model section) with the blockholder order set to two noise lumps. Return PASS if you reach the statement, FAIL with reasons otherwise.`, { model: 'opus', effort: 'high', schema: VERDICT, label: '04 re-derive', phase: 'Proofs' }),
      async (v, stmt) => {
        if (v && v.verdict === 'PASS') return { stmt, status: 'PASS', verdict: v }
        const w = await agent(`${PRE}\n\nTicket 04. A re-deriver failed on ${stmt} with reasons: ${v ? v.reasons : 'none'}. Repair the proof once, working from the inherited proof in inherited/draft_v3/ (never cited), and write it into proofs/04_inherited.tex.`, { model: 'opus', effort: 'high', schema: RESULT, label: '04 repair', phase: 'Proofs' })
        if (!w || w.status !== 'PASS') return { stmt, status: 'STOP', report: w }
        const v2 = await agent(`${PRE}\n\nTicket 04. Fresh re-deriver: derive ${stmt} from the model section only. PASS or FAIL with reasons.`, { model: 'opus', effort: 'high', schema: VERDICT, label: '04 re-derive 2', phase: 'Proofs' })
        return { stmt, status: v2 && v2.verdict === 'PASS' ? 'PASS' : 'STOP', verdict: v2 }
      },
      async (r, stmt) => {
        if (!r || r.status !== 'PASS' || r.report) return r
        await agent(`${PRE}\n\nTicket 04. Transcribe the proof of ${stmt} into proofs/04_inherited.tex in the paper's notation, from the inherited proof (never cited), and report the file changed.`, { model: 'opus', schema: RESULT, label: '04 transcribe', phase: 'Proofs' })
        return r
      })
  },
  async () => {
    results.t06 = await attempt('06', 'Ticket 06-empirics-build-and-e1-run.md. Build empirics/fingerprints.py and empirics/test_fingerprints.py to empirics/spec.md exactly, run build and run e1, and report the coverage counts and gate values.', { phase: 'Empirics' })
    if (results.t06.status !== 'PASS') return
    results.t06v = await agent(`${PRE}\n\nTicket 06, second agent. Run the tests and rerun e1 from the cache; confirm e1_estimate.json is byte-identical to the file the builder produced (compare against this report: ${JSON.stringify(results.t06)}). PASS or FAIL.`, { model: 'opus', schema: VERDICT, label: '06 rerun', phase: 'Empirics' })
    results.t07 = await attempt('07', 'Ticket 07-e1-blind-audit.md. You did not write the parser or the loader. Do the sixty-case audit and write gate E1-G2 into e1_estimate.json.', { phase: 'Empirics' })
  },
  async () => {
    results.t09 = await attempt('09', 'Ticket 09-literature-check.md. Answer the three questions with primary sources and write docs/lit_check_2026-09.md.', { phase: 'Literature', agentType: 'general-purpose' })
  },
]
await parallel(chains)
// ---- Grid checks that need the mark-2 code (ticket 01) and the proofs' statements.
if (results.t01 && results.t01.status === 'PASS') {
  const gridJobs = []
  if (results.t02 && results.t02.status === 'PASS' && results.t02.write && results.t02.write.named_condition) {
    gridJobs.push(() => attempt('02 grid', `Ticket 02, grid verification. Write numerical_v4/checks/t5_threshold_condition.py that checks this named condition at every calibration node at mark=2 and writes a JSON record: ${results.t02.write.named_condition}. Report the node count and the verdict per node.`, { phase: 'Grid checks' }))
  }
  if (results.t03 && results.t03.status === 'PASS') {
    gridJobs.push(() => attempt('03 grid', 'Ticket 03-who-gets-caught.md, grid check section. Write numerical_v4/checks/t5_who_gets_caught.py exactly as the ticket describes and report the comparison table against the T1 record.', { phase: 'Grid checks' }))
  }
  gridJobs.push(() => twoPass('05',
    'Ticket 05-existence-if-clean.md. Attempt the existence proof at order size two under grid-checkable conditions; write a check script under numerical_v4/checks/ that verifies the conditions at every calibration node. Write the statement and proof into proofs/05_existence.tex. Return PASS only if the proof is complete and the conditions hold at every node; return ABSENT otherwise with the reason in the summary.',
    REDERIVE('05', 'the existence proposition')))
  const g = await parallel(gridJobs)
  results.grid = g
}
const stops = Object.entries(results).flatMap(([k, v]) => {
  if (!v) return [[k, 'null']]
  if (Array.isArray(v)) return v.filter(x => x && x.status === 'STOP').map(x => [k, x])
  return v.status === 'STOP' ? [[k, v]] : []
})
if (stops.length) log(`STOP on: ${stops.map(s => s[0]).join(', ')}. The orchestrator writes a judgment and waits for Austin.`)
return { stop: stops.length > 0, stops, results }
