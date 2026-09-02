# Orchestration for the v5 delivery session

The orchestrator's run book. Grok 4.6 implements in batches from the briefs under `grok/`; this
file holds what the orchestrator does at each checkpoint, the gates only the reviewers run, the
check runs, and the orchestrator's own prompt texts and procedures (ADR 0006). A brief states
the objective the batch must reach and the constraints that hold, and leaves the method to Grok
(ADR 0007). Phase contents are in `spec.md` section 5; tickets are under `issues/`.

## Sessions and records

- The implementing session is Grok Build, one per batch, started by Austin with the launch line
  in `grok/README.md`. Its briefs are `grok/batch-N.md`; its step contract is the README. A
  brief carries the objective, the inputs, the constraints that bind the batch, and what must
  exist when it ends. Grok organises the work.
- The orchestrating session is Fable in Claude Code (`KICKOFF.md`). At a checkpoint it reads
  the batch plan, the batch result and the diff, runs the Opus subagents listed below, starts
  the check runs, commits one concern per commit, writes `grok/checkpoint-N.md` with feedback on
  the approach, and writes the next brief.
- Every step has a label and writes `runs/<label>/result.txt` in the RESULT or VERDICT schema
  (`schemas/result.json`, `schemas/verdict.json`). A step whose record holds PASS or ABSENT is
  finished and never rerun; a recorded verdict is never rerun; a ticket committed on the branch
  is finished. Directories under `runs/` without a `result.txt` are debris from killed runs.
- The orchestrator reads the batch plan, the result files and diffs, never transcripts.
- Opus subagents run from the orchestrating session through the Agent tool at model `opus`.
  The tool sets no effort tier, so each prompt states the depth it wants: a judge that reads
  records and recomputes one node is told to do exactly that; an attacker is told to try to
  break the proof and to recompute what it doubts.

## Schemas

RESULT:

```json
{"type": "object", "required": ["status", "summary", "files_changed", "evidence"], "properties": {"status": {"type": "string", "enum": ["PASS", "FAIL", "ABSENT", "STOP"]}, "summary": {"type": "string"}, "files_changed": {"type": "array", "items": {"type": "string"}}, "evidence": {"type": "string"}, "named_condition": {"type": "string"}}}
```

VERDICT:

```json
{"type": "object", "required": ["verdict", "reasons"], "properties": {"verdict": {"type": "string", "enum": ["PASS", "FAIL"]}, "reasons": {"type": "string"}}}
```

## Shared prompt texts

ATTACK, the attacker prompt; `<ticket>` is the ticket number, `<what>` the statement, `<proof>`
the proof file:

```text
Ticket <ticket>. You are the independent attacker. You did not write this proof. Read CLAUDE.md, CONTEXT.md, .scratch/v5-paper/spec.md section 3, docs/adr/0003, the model section only of inherited/draft_v3/draft_v3.tex (never cited), then the statement of <what> at the top of <proof> and the proof that follows. Try to break the proof: a missing hypothesis, a step that does not follow, a counterexample, a hidden use of a dropped assumption (the order-size-one ternary pooled law, any support assumption on the pooled posterior). Where you doubt an inequality or identity, recompute it at one node with a short script (PYTHONPATH=. .venv/bin/python; one evaluation at order size two takes ten seconds and six gigabytes; run no check script and not the smoke). Return PASS only if you cannot break it; FAIL with the precise hole otherwise; nits that are not holes after the word "Nits:". Do not rewrite the proof. Run no git command. Edit no file except the verdict: write the VERDICT JSON to .scratch/v5-paper/runs/<ticket>-attack/result.txt and return it.
```

CHECK, the paper checker prompt (11 check, 11 check 2):

```text
Ticket 11, checker. Run PYTHONPATH=. .venv/bin/python -m empirics.test_fingerprints and the compile sequence in CLAUDE.md. Then grep paper.tex and appendix.tex for any reference to earlier versions, dropped results, attempts, or the inherited draft, and for any label stronger than the one the result holds (the labels are listed in grok/checkpoint-1.md). Return PASS only if the number guard is green, both files compile with zero errors, undefined references, or citations, and the grep finds nothing. Otherwise FAIL with the exact lines. Run no git command; edit nothing; write the VERDICT JSON to .scratch/v5-paper/runs/11-check/result.txt.
```

The fix wording, which the orchestrator carries into a fix brief as its input; `<reasons>` is
the attacker's or the checker's reasons:

```text
An independent attacker returned FAIL with these reasons: <reasons>. Fix the proof once. You may replace one assumption with a cleaner one; say so in your summary.
```

## Procedures

Writing a brief. `grok/batch-N.md` has four parts and nothing else (ADR 0007). The objective:
what must be true when the batch ends, in terms the orchestrator can check. The inputs: pointers
to the tickets, records and checkpoint notes the batch reads, with no restatement of what they
hold. The constraints that bind this batch: the effort, the paths, the labels the results carry,
the dependencies between steps. Done: the result files that must exist and what each must show.
The README carries every standing gate once, so a brief points at it and states no gate of its
own. How the work is organised, what Grok delegates, and the order of steps that no dependency
fixes, stay with Grok. Facts a checkpoint supplies sit in angle brackets while the brief is a
skeleton, and the brief is final when none is left. A fix brief (`grok/batch-N-fix.md`) has the
same four parts, with the attacker's or the checker's reasons among its inputs.

Attempt. One attempt, one retry, as the README says. A second failure is a STOP record
carrying both reports.

Attack gate. Write (Grok, in a batch); attack (Opus, at the checkpoint, ATTACK); on FAIL one
fix (Grok) and one attack 2 (Opus). The fix runs as step 0 of the next batch and attack 2 at the
next checkpoint, unless a later step of that batch depends on the result's label (11 depends on
05); then the fix is its own brief, `grok/batch-N-fix.md`, and attack 2 its own checkpoint.
A second FAIL is a STOP. An attacker PASS with nits: wording nits are applied by Grok as a
step 0 with no label change, and the checkpoint diff confirms that only wording moved.

STOP. A STOP at any step ends the build. Nothing new starts. The orchestrator writes a
one-page judgment (the two reports or verdicts, what was attempted, what the ticket needed) in
the checkpoint note and waits for Austin before anything else.

## Check runs

A check run is one execution of a check script that writes its record file. The orchestrator
starts it, never a worker, detached from the client so that an interrupt cannot reach it, from
a plain Bash call (not a tracked background job):

```bash
python3 - <<'PY'
import subprocess, os
root = "/Users/austinli/Projects/blockholder_v5"
name = "t2_t1_check"                      # the script's stem
log = f"{root}/.scratch/v5-paper/runs/checks/{name}.log"
os.makedirs(os.path.dirname(log), exist_ok=True)
cmd = (f"cd {root} && PYTHONPATH=. .venv/bin/python numerical_v4/checks/{name}.py "
       f"> {log} 2>&1; echo $? > {log[:-4]}.rc")
subprocess.Popen(["/bin/sh", "-c", cmd], start_new_session=True,
                 stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
PY
```

One run at a time on this machine: one evaluation at order size two peaks near 6 GiB and a
cold solve near 8 GiB, and the work is bound by memory bandwidth, so concurrent runs thrash.
Several scripts in sequence may share one detached shell. A run is finished when
`runs/checks/<name>.rc` exists; its record is the JSON next to the script. The orchestrator
checks the `.rc` file when it next acts; no model polls a log. Verification of a run is a judge
reading the record and recomputing one node; it never repeats the run.

| Run | Script | Needs | Cost alone | Feeds |
|---|---|---|---|---|
| T1 rerun | `t2_t1_check.py` | 01 code (committed) | about 3.5 h | 01 verify, 03 grid comparison, 10 |
| L4 rerun | `t2_l4_check.py` | 01 code | about 2.3 h | 01 verify, the weight leg of the threshold theorem |
| Condition D | `t2_threshold_revelation_check.py` | present (hash `fbacc963f39422c3`, mark 2, H 10); rerun only if the code changes | 17 min | 02's named condition |
| who gets caught | `t5_who_gets_caught.py` | 03 grid PASS in batch 1 | sized by its author's report | 03's grid record, 10 |
| existence conditions | `t5_existence_conditions.py` | 05 write PASS in batch 1 | sized by its author's report | 05's label |

The T1 then L4 chain was started 2026-09-02 12:22 (`runs/checks/t1_l4_chain.pid`).

## Checkpoints

At a checkpoint the orchestrator reads `runs/batch-N/plan.md`, where the batch wrote one, and
the `approach` block of `runs/batch-N/result.txt`, then writes a section "Feedback on the
approach" in `grok/checkpoint-N.md`: what the plan got right, where another order, another
split of the work or another check before calling a step done would have cost less, and what to
carry into the next batch. That section is about how the batch was organised; the gates below
decide the results. Batch 1 ran before this rule, so its plan is `.grok/workflows/v5-batch-1.rhai`.

Checkpoint 0 (before batch 1). Opus attacks on the committed proofs: `02-attack` (the garbling
lemma and the threshold theorem, `proofs/02_garbling.tex`), `03-attack` (the who-gets-caught
corollary, `proofs/03_caught.tex`), `04-attack` (the four inherited results,
`proofs/04_inherited.tex`). Then: `runs/02/result.txt` and `runs/03/result.txt` rewritten as
attack-gate outcomes; the Condition D script and record committed with 02's PASS; ticket
statuses; `grok/checkpoint-0.md` with the verdicts, the nits for step 0 of batch 1, and the
label scope each attacker set; `grok/batch-1.md` step 0 finalised.

Checkpoint 1 (after batch 1). `05-attack` (Opus, ATTACK, `proofs/05_existence.tex`) unless 05
returned ABSENT. `01-verify` (Opus) once the T1 and L4 reruns have landed. The who-gets-caught
run, then the existence conditions run if 05 wrote a script, one detached shell in sequence.
When their records land: `03-grid-judge` (Opus) reads the who-gets-caught record, compares its
C_T verdicts with the T1 record's at the same nodes under the point-derivative convention, and
recomputes one node; `05-grid-judge` likewise decides 05's label from its record (a condition
that fails at any node makes the result ABSENT). Commit the batch, the records, the results.
Write `grok/checkpoint-1.md` with every result's label at that moment; fill the placeholders in
`grok/batch-2.md`.

Checkpoint 2 (after batch 2). The who-gets-caught rerun on the step-0 script, detached, so the committed record carries the added fields. `11-check` (Opus, CHECK). On FAIL, a fix-only brief `batch-2-fix.md`
(11 fix), then `11-check-2`; a second FAIL is a STOP. On PASS, `12-referee` (Opus). Commit the
paper. Write `grok/checkpoint-2.md`; fill the placeholders in `grok/batch-3.md` from the referee
report.

Checkpoint 3 (after batch 3). The orchestrator renders every page of both PDFs and inspects
them, runs the unslop gate over the prose, confirms `deliverable/` holds both PDFs, commits,
pushes `v5`, and writes `session_note.md` (what shipped, every label, any STOP).

## Checkpoint prompts

These prompts are the orchestrator's own, sent to Opus subagents at a checkpoint. What Grok does
in a batch is in the brief, as an objective and the constraints that bind it.

01 verify; `<01 report>` is `runs/01-rewrite/result.txt`:

```text
Ticket 01, judge. You did not write the change. Read numerical_v4/smoke_output_mark2.txt, numerical_v4/checks/t2_t1_check.json and numerical_v4/checks/t2_l4_check.json. Confirm each record's provenance says mark = 2 and H = 10 and that the not-applicable blocks are so labelled and counted in neither n_fail nor the pass count. Then recompute one node at mark = 2 with a short PYTHONPATH=. .venv/bin/python -c script that solves the baseline policy at the frozen tau, evaluates at kappa = 0.5, and compares M_F and M_P with the T1 record's baseline node to 1e-10 (a cold solve plus one evaluation; run nothing longer). Return PASS or FAIL with reasons as the VERDICT JSON in .scratch/v5-paper/runs/01-verify/result.txt. Run no git command; edit nothing else. The 01 report for reference: <01 report>.
```

03 grid judge:

```text
Ticket 03, judge of the grid record. Read numerical_v4/checks/t5_who_gets_caught.json and t2_t1_check.json. Confirm the provenance block (mark 2, H 10, the params hash equal to the T1 record's). Build the comparison table: at every node, the who-gets-caught record's C_T <= 1 verdict against the T1 record's under the point-derivative convention; any disagreement is a FAIL with the nodes listed. Recompute s_A and s_B at one node with a short script (one evaluation; run nothing longer). Write the VERDICT JSON with the table in reasons to .scratch/v5-paper/runs/03-grid-judge/result.txt. Run no git command; edit nothing else.
```

05 grid judge:

```text
Ticket 05, judge of the condition record. Read proofs/05_existence.tex (the conditions the statement names) and numerical_v4/checks/t5_existence_conditions.json. Confirm the provenance block and that every condition the statement names is checked at every calibration node. PASS if every condition holds at every node; FAIL with the failing nodes and conditions otherwise (FAIL makes the result ABSENT from the paper). Recompute one condition at one node with a short script. Write the VERDICT JSON to .scratch/v5-paper/runs/05-grid-judge/result.txt. Run no git command; edit nothing else.
```

12 referee (Opus):

```text
Ticket 12-referee.md. You wrote nothing in this session. Referee at deliverable quality: read paper.pdf and appendix.pdf (render pages to images if needed) and write .scratch/v5-paper/referee_report.md with blocking and minor lists, each item with a location. Do not edit the paper. Run no git command. Write the RESULT JSON to .scratch/v5-paper/runs/12-referee/result.txt.
```

## Commit points

1. Checkpoint 0: the Condition D script and record with 02's verdict; the two run records
   rewritten; the checkpoint note and batch 1 brief.
2. Checkpoint 1: batch 1 files one concern per commit (grid scripts, the existence proof,
   E2 results and audit), the T1 and L4 records, the grid records, the checkpoint note.
3. Checkpoint 2: figures and the paper.
4. Checkpoint 3: the fixes and the deliverables; push `v5`; `session_note.md`.
