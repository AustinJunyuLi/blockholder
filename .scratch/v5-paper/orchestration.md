# Orchestration for the v5 delivery session

This is the run book for the session that delivers the paper. It carries everything the four
phase scripts carried: a reader with only this file runs the session exactly as they would
have. The plan and the phase contents live in `.scratch/v5-paper/spec.md` section 5; the
tickets live under `.scratch/v5-paper/issues/`.

## How to run

Kimi and GLM steps run as background Bash jobs:

```bash
printf '%s' "$TASK" | kimi-dispatch --effort <E> --context <C> --artifact-dir .scratch/v5-paper/runs/<label> --schema .scratch/v5-paper/schemas/<result|verdict>.json
```

`glm-dispatch` for GLM, with no `--context`. `$TASK` is the full task text: PRE, a blank
line, the step prompt (with whatever retry or fix wording the procedure prefixes), a blank
line, then the line `Return JSON matching this schema and nothing else:` followed by the
schema JSON. Exit 0 means success: read `runs/<label>/result.txt`, which holds the JSON
alone. Exit 3 is a provider limit: re-dispatch the same task once to the fallback
provider (kimi to opus, glm to kimi) and do not count it as a failure; the opus fallback of a
kimi step runs as an Opus subagent at the same effort and schema. Exit 1 is a failure.
Background the jobs so the concurrent chains really run at once.

Opus steps run as an Opus subagent from the Agent tool with the stated effort and the prompt
text below, with the instruction to reply with JSON matching the schema and nothing else; the
orchestrator saves that JSON to `runs/<label>/result.txt` itself.

Every table row below is a step with its own label. A dispatch's directory is
`.scratch/v5-paper/runs/<label>`, with spaces in the label written as hyphens (`01 verify`
runs in `runs/01-verify`). A composite step (an attempt with its retry, a two-pass gate)
keeps its sub-dispatches under suffixed labels (`01 retry`, `02 write`, `02 re-derive`,
`02 fix`, `02 re-derive 2`), and when the step ends the orchestrator writes the step's own
outcome JSON to `runs/<label>/result.txt`; for single-dispatch steps the dispatch result is
already that file.

A step whose `runs/<label>/result.txt` exists with status PASS or ABSENT is finished and is
never rerun. Tickets that are already committed on the branch are finished too (check git
log).

## Roles

| Role | Provider | Fallback on exit 3 |
|---|---|---|
| author | kimi-dispatch | opus subagent |
| writer | kimi-dispatch | opus subagent |
| engineer | glm-dispatch | kimi-dispatch |
| auditor | glm-dispatch | kimi-dispatch |
| judge | opus subagent | none |

## Schemas

RESULT, `.scratch/v5-paper/schemas/result.json`:

```json
{"type": "object", "required": ["status", "summary", "files_changed", "evidence"], "properties": {"status": {"type": "string", "enum": ["PASS", "FAIL", "ABSENT", "STOP"]}, "summary": {"type": "string"}, "files_changed": {"type": "array", "items": {"type": "string"}}, "evidence": {"type": "string"}, "named_condition": {"type": "string"}}}
```

VERDICT, `.scratch/v5-paper/schemas/verdict.json`:

```json
{"type": "object", "required": ["verdict", "reasons"], "properties": {"verdict": {"type": "string", "enum": ["PASS", "FAIL"]}, "reasons": {"type": "string"}}}
```

## Shared prompt texts

Every task in the phase tables is sent as PRE, a blank line, then the step prompt, a blank
line, then the schema-return line and the schema JSON.

PRE:

```text
Work in /Users/austinli/Projects/blockholder_v5. Read CLAUDE.md, CONTEXT.md and .scratch/v5-paper/spec.md first, then the ticket named below under .scratch/v5-paper/issues/. Run no git command. Edit only the paths the ticket names and report every file you changed. The paper states positive results only: never write a sentence that refers to the inherited draft, earlier versions, dropped results, or attempts. Prose never promotes an honesty label. If a step fails, report FAIL with the output; do not work around a gate or a spec.
```

REDERIVE, the re-deriver prompt of the two-pass gate; `<ticket>` is the ticket number and
`<what>` the statement named in the phase table:

```text
Ticket <ticket>. You are the independent re-deriver. Read only the model section of inherited/draft_v3/draft_v3.tex (that section and nothing else of that file), with the blockholder order set to two noise lumps as .scratch/v5-paper/spec.md section 3 says, and the statement of <what> as written at the top of the ticket's file under proofs/. Do not read the proof. Re-derive the statement from the model. Return PASS if your derivation reaches the statement as written, FAIL with precise reasons otherwise (a missing hypothesis, a step you cannot justify, a counterexample).
```

CHECK, the phase C checker prompt:

```text
Ticket 11, checker. Run PYTHONPATH=. .venv/bin/python -m empirics.test_fingerprints and the compile sequence in CLAUDE.md. Then grep paper.tex and appendix.tex for any reference to earlier versions, dropped results, attempts, or the inherited draft, and for any label stronger than the one the result holds. Return PASS only if the number guard is green, both files compile with zero errors, undefined references, or citations, and the grep finds nothing. Otherwise FAIL with the exact lines.
```

The attempt retry wording; `<label>` is the step label and `<first report>` the first report
as JSON:

```text
This is the single retry of <label>. The first attempt reported: <first report>. You may change one assumption or one design choice to a cleaner one; say exactly what you changed and why in your summary.
```

The two-pass fix wording; `<reasons>` is the re-deriver's reasons, or the words `no report`
when there is none:

```text
An independent re-deriver returned FAIL with these reasons: <reasons>. Fix the proof once. You may replace one assumption with a cleaner one; say so in your summary.
```

## Procedures

Attempt. A step whose table row says attempt runs at most two dispatches. First: the step
prompt at the step effort, RESULT schema, label `<label>`. A report of PASS or ABSENT ends
the step. Otherwise one retry, label `<label> retry`: the retry wording with the label and
the first report filled in, a blank line, then the step prompt, at the retry effort the table
names, or the same effort when it names none. PASS or ABSENT ends the step. A second report
that is neither is a STOP: the step outcome in `runs/<label>/result.txt` is STOP carrying
both reports.

Two-pass gate. A step whose table row says twoPass runs at most four dispatches, at the
stage efforts the table names, or the defaults write xhigh, re-derive high, fix xhigh,
re-derive 2 high:

1. Write: the author, label `<label> write`, RESULT schema. ABSENT ends the step cleanly. A
   report that is not PASS is a STOP, stage write.
2. Re-derive: the judge, label `<label> re-derive`, VERDICT schema, REDERIVE filled for this
   ticket. A PASS verdict ends the step PASS.
3. Fix: the author, label `<label> fix`, RESULT schema; the prompt is the fix wording with
   the re-deriver's reasons, a blank line, then the write prompt. A report that is not PASS
   is a STOP, stage fix.
4. Re-derive 2: the judge, label `<label> re-derive 2`, VERDICT schema, the same REDERIVE
   text. PASS ends the step PASS; FAIL is a STOP, stage re-derive.

STOP. A STOP at any step ends its phase. Let the dispatches already running finish and keep
their reports, start nothing new in the phase, and do not open the next phase. The
orchestrator writes a one-page judgment (the two reports or verdicts, what was attempted,
what the ticket needed) and waits for Austin before anything else.

## Phase A

Six chains start at once; nothing in one chain waits on another. The barrier at the end is
real: the orchestrator commits all of Phase A.

- Chain 1: 01, then 01 verify when 01 PASSed.
- Chain 2: 02, a two-pass gate.
- Chain 3: 03, a two-pass gate.
- Chain 4: 04, the pipeline below.
- Chain 5: 06, then 06 rerun, then 07.
- Chain 6: 09.

After every chain has ended, when 01 PASSed the grid group runs, its jobs at once: 02 grid
(only when 02 PASSed and the 02 final write report carries a named condition), 03 grid (only
when 03 PASSed), and 05 (always).

The 04 pipeline takes four statements, each handled independently and concurrently; n below
is 1 to 4 in the order of the statement list:

1. `04 re-derive <n>`: the judge derives statement n, VERDICT schema.
2. On FAIL, `04 repair <n>`: the author repairs the proof once, RESULT schema. A report that
   is not PASS is a STOP.
3. `04 re-derive 2 <n>`: a fresh judge re-derives, VERDICT schema. FAIL is a STOP.
4. A statement that passed, at the first or second re-derive, gets `04 transcribe <n>`: the
   engineer transcribes it, RESULT schema.

| Label | Role | Provider | Effort | Context | Schema | Depends on |
|---|---|---|---|---|---|---|
| 01 | engineer | glm-dispatch | high, retry xhigh | none | RESULT | nothing |
| 01 verify | engineer | glm-dispatch | low | none | VERDICT | 01 PASS |
| 02 | author, judge | kimi-dispatch, opus subagent | write max, re-derive xhigh, fix max, re-derive 2 xhigh | 256k | RESULT and VERDICT | nothing |
| 03 | author, judge | kimi-dispatch, opus subagent | write xhigh, re-derive xhigh, fix xhigh, re-derive 2 xhigh | 256k | RESULT and VERDICT | nothing |
| 04 | judge, author, engineer | opus, kimi-dispatch, glm-dispatch | re-derive high, repair xhigh, re-derive 2 high, transcribe medium | 256k for the author | VERDICT and RESULT | nothing |
| 06 | engineer | glm-dispatch | high, retry xhigh | none | RESULT | nothing |
| 06 rerun | auditor | glm-dispatch | low | none | VERDICT | 06 PASS in this session; skipped when 06 was already committed |
| 07 | auditor | glm-dispatch | medium, retry medium | none | RESULT | 06 PASS |
| 09 | author | kimi-dispatch | medium, retry medium | 256k | RESULT | nothing |
| 02 grid | engineer | glm-dispatch | medium, retry high | none | RESULT | 01 PASS, 02 PASS with a named condition |
| 03 grid | engineer | glm-dispatch | medium, retry high | none | RESULT | 01 PASS, 03 PASS |
| 05 | author, judge | kimi-dispatch, opus subagent | write xhigh, re-derive high, fix xhigh, re-derive 2 high | 256k | RESULT and VERDICT | 01 PASS |

01 (attempt):

```text
Ticket 01-mark-parameter-and-timed-smoke.md. Build exactly what the ticket says. Report wall time and peak memory for one node at mark=2, H=10, and the diff at mark=1 against numerical_v4/smoke_output.txt.
```

01 verify; `<01 report>` is the 01 report as JSON:

```text
Ticket 01, verifier. You did not write the change. Rerun .venv/bin/python -m numerical_v4.smoke and one check script at mark=2 and confirm the numbers in this report match: <01 report>. Return PASS or FAIL with reasons.
```

02, write prompt of the two-pass gate (re-derive prompt is REDERIVE with ticket 02 and "the
garbling lemma and the threshold theorem"):

```text
Ticket 02-garbling-lemma-and-threshold-dial.md. Write the garbling lemma and the threshold theorem with their proofs into proofs/02_garbling.tex, statement first. If any bridge clause does not follow from the order-size-two structure, state it as one named condition in the theorem and put its exact mathematical form in the named_condition field of your report; otherwise leave that field empty.
```

03, write prompt of the two-pass gate (re-derive prompt is REDERIVE with ticket 03 and "the
who-gets-caught corollary"):

```text
Ticket 03-who-gets-caught.md. Write the corollary and its proof into proofs/03_caught.tex, statement first. The grid check is a separate agent; do not write it.
```

04, the four statements, in order:

```text
the partition and factorisation S = (1 minus Omega) S_P
the kappa-invariance of the flagged cell
the clock theorem: at fixed policies a shorter clock lowers noise sensitivity iff W_T C_T is at most one
the weight leg of the threshold theorem: Omega rises when the threshold tightens at fixed policies
```

04 re-derive `<n>`; `<statement>` is statement n from the list:

```text
Ticket 04-rederive-inherited-results.md. You are an independent re-deriver who has not read any proof. Derive <statement> from the model section of inherited/draft_v3/draft_v3.tex (read only the model section) with the blockholder order set to two noise lumps. Return PASS if you reach the statement, FAIL with reasons otherwise.
```

04 repair `<n>`; `<statement>` is statement n, and `<reasons>` the re-deriver's reasons or
the word `none`:

```text
Ticket 04. A re-deriver failed on <statement> with reasons: <reasons>. Repair the proof once, working from the inherited proof in inherited/draft_v3/ (never cited), and write it into proofs/04_inherited.tex.
```

04 re-derive 2 `<n>`; `<statement>` is statement n:

```text
Ticket 04. Fresh re-deriver: derive <statement> from the model section only. PASS or FAIL with reasons.
```

04 transcribe `<n>`; `<statement>` is statement n:

```text
Ticket 04. Transcribe the proof of <statement> into proofs/04_inherited.tex in the paper's notation, from the inherited proof (never cited), and report the file changed.
```

06 (attempt):

```text
Ticket 06-empirics-build-and-e1-run.md. Build empirics/fingerprints.py and empirics/test_fingerprints.py to empirics/spec.md exactly, run build and run e1, and report the coverage counts and gate values.
```

06 rerun; `<06 report>` is the 06 report as JSON:

```text
Ticket 06, second agent. Run the tests and rerun e1 from the cache; confirm e1_estimate.json is byte-identical to the file the builder produced (compare against this report: <06 report>). PASS or FAIL.
```

07 (attempt):

```text
Ticket 07-e1-blind-audit.md. You did not write the parser or the loader. Do the sixty-case audit and write gate E1-G2 into e1_estimate.json.
```

09 (attempt):

```text
Ticket 09-literature-check.md. Answer the three questions with primary sources and write docs/lit_check_2026-09.md. Use the WebSearch tool for primary sources and the ego-browser skill for pages WebSearch cannot open.
```

02 grid (attempt); `<named condition>` is the named_condition field of the 02 final write
report:

```text
Ticket 02, grid verification. Write numerical_v4/checks/t5_threshold_condition.py that checks this named condition at every calibration node at mark=2 and writes a JSON record: <named condition>. Report the node count and the verdict per node.
```

03 grid (attempt):

```text
Ticket 03-who-gets-caught.md, grid check section. Write numerical_v4/checks/t5_who_gets_caught.py exactly as the ticket describes and report the comparison table against the T1 record.
```

05, write prompt of the two-pass gate (re-derive prompt is REDERIVE with ticket 05 and "the
existence proposition"):

```text
Ticket 05-existence-if-clean.md. Attempt the existence proof at order size two under grid-checkable conditions; write a check script under numerical_v4/checks/ that verifies the conditions at every calibration node. Write the statement and proof into proofs/05_existence.tex. Return PASS only if the proof is complete and the conditions hold at every node; return ABSENT otherwise with the reason in the summary.
```

## Phase B

One sequence: 08, then 08 audit when 08 PASSed, then 10, unless the phase has stopped.

| Label | Role | Provider | Effort | Context | Schema | Depends on |
|---|---|---|---|---|---|---|
| 08 | engineer | glm-dispatch | medium, retry high | none | RESULT | nothing |
| 08 audit | auditor | glm-dispatch | medium, retry high | none | RESULT | 08 PASS |
| 10 | engineer | glm-dispatch | medium, retry high | none | RESULT | after 08 and 08 audit, unless the phase stopped |

08 (attempt):

```text
Ticket 08-e2-run-and-link-audit.md, the run. Confirm the dated E2 direction note is present in empirics/spec.md before running; if absent, return FAIL. Run e2 and report every gate value.
```

08 audit (attempt):

```text
Ticket 08-e2-run-and-link-audit.md, the audit. You did not write the link. Do the sixty-case link audit and write gate E2-G2 into e2_estimate.json.
```

10 (attempt):

```text
Ticket 10-figures.md. Regenerate every figure and report the commands.
```

## Phase C

11 first, as an attempt. When it PASSed, 11 check runs. When the check verdict is not PASS,
one fix: 11 fix (a single run, not an attempt), then 11 check 2 whatever the fix returned,
with the same CHECK prompt. The phase is clean only when the last write report (11, or 11
fix when there was one) is PASS and the last check verdict is PASS; anything else is a STOP.

| Label | Role | Provider | Effort | Context | Schema | Depends on |
|---|---|---|---|---|---|---|
| 11 | writer | kimi-dispatch | xhigh, retry max | 1m | RESULT | nothing |
| 11 check | engineer | glm-dispatch | low | none | VERDICT | 11 PASS |
| 11 fix | writer | kimi-dispatch | high | 1m | RESULT | 11 check not PASS |
| 11 check 2 | engineer | glm-dispatch | low | none | VERDICT | 11 fix |

11 (attempt):

```text
Ticket 11-paper-writer.md. Write paper.tex, appendix.tex and paper.bib as the ticket says. Apply the unslop rules to the prose.
```

11 check and 11 check 2: the CHECK prompt in Shared prompt texts, unchanged.

11 fix; `<reasons>` is the checker's reasons, or the words `no report` when there is none:

```text
Ticket 11, fix pass. The checker reported: <reasons>. Fix exactly those items in paper.tex, appendix.tex, paper.bib.
```

## Phase D

One sequence: 12 referee, then 13 fix whatever 12 returned, then 14 when 13 fix PASSed. The
phase stops unless 13 fix PASSed and 14 PASSed.

| Label | Role | Provider | Effort | Context | Schema | Depends on |
|---|---|---|---|---|---|---|
| 12 referee | judge | opus subagent | high | none | RESULT | nothing |
| 13 fix | judge | opus subagent | high | none | RESULT | 12 referee, whatever it returned |
| 14 | engineer | glm-dispatch | medium, retry high | none | RESULT | 13 fix PASS |

12 referee:

```text
Ticket 12-referee.md. You wrote nothing in this session. Referee deliverable-quality: read paper.pdf and appendix.pdf (render pages to images if needed), write .scratch/v5-paper/referee_report.md with blocking and minor lists, each with a location. Do not edit the paper.
```

13 fix:

```text
Ticket 13-author-fix.md. Fix every blocking item and every minor item in .scratch/v5-paper/referee_report.md that needs no new result. Mark each item fixed or STOP with the reason, in the report file. Rerun the number guard. Return STOP if any blocking item needs a new theorem or a new run.
```

14 (attempt):

```text
Ticket 14-compile-and-deliver.md. Compile, inspect every page, apply the unslop gate, copy the PDFs to deliverable/.
```

## Between phases

What the orchestrator does between phases:

1. After A: read the mark-2 T1 record under `numerical_v4/checks/` for the sign of the
   run-up share across the κ grid; append a dated note to the E2 section of
   `empirics/spec.md` stating that direction; commit Phase A files one concern per commit
   (code, proofs, empirics, lit, spec note); update ticket statuses.
2. After B: commit results and figures.
3. After C: commit the paper.
4. After D: commit, push `v5`, write `.scratch/v5-paper/session_note.md`.
