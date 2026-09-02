# CLAUDE.md

## Project

One paper: *Who Gets Caught: Blockholder Disclosure Rules and Market Inference*. A blockholder
disclosure rule has two dials, a stake threshold and a filing clock. The rule splits every
possible history of the blockholder into a flagged cell and a pooled cell. Tightening the
threshold makes prices less noise-driven at fixed policies. Shortening the clock does so only when the
histories it newly catches are the noise-sensitive ones, and the paper says exactly when.

Branch `v5`, worktree `/Users/austinli/Projects/blockholder_v5`. The live manuscript is
`paper.tex` with `appendix.tex` and `paper.bib`; delivered PDFs live in `deliverable/`.

Read `CONTEXT.md` before naming any paper object. Read `.scratch/v5-paper/spec.md` before
starting any ticket.

## Doctrine

The paper is the only record. `inherited/draft_v3/` is starting material, read-only, and is
never cited, quoted, or described in the paper. The paper states what holds. It says nothing
about what was tried, dropped, weakened, or superseded, in any version. A result that fails its
gate is absent, not mentioned.

## Authority by area

| Area | Authority | Rule |
|---|---|---|
| Theory | `paper.tex` statements, `appendix.tex` proofs | Every result carries a label. A result is PROVED only after the two-pass gate (writer, then an independent re-deriver who did not see the proof) passes on v5. This applies to inherited results too. |
| Theory code | `numerical_v4/` (depends on `numerical/`), checks in `numerical_v4/checks/` | Keep the code consistent with the paper's model. `numerical_v4.smoke` is the minimum gate. |
| Empirics | `empirics/spec.md`, `empirics/output/<exercise>_estimate.json` | The spec is registered by the commit that precedes the run. Correct it only by a dated amendment inside the file. One result file per exercise is the single source of every manuscript number. |
| Paper | `paper.tex`, `appendix.tex`, `paper.bib`, `deliverable/` | Edit presentation freely. Trace every theory claim to a labelled statement and every number to a result file. |
| Brief | `docs/brief_2026-09-01_referee.md` | Input for the rewrite. Not a rulebook. |
| Plan | `.scratch/v5-paper/spec.md`, `.scratch/v5-paper/issues/` | The session plan and its tickets. |

## The six rules

1. Honesty labels are PROVED, NUMERICAL (verified on the stated grid), ESTIMATED (an empirical
   estimate with a stated design and a standard error). CONJECTURE is a working label that never
   ships. Prose never promotes a label. A review may demote one.
2. Registration before run. `empirics/spec.md` is committed before any exercise runs. A failed
   gate suppresses the exercise. It never licenses editing the spec.
3. One result file per exercise. Every manuscript number renders from it, and the number-guard
   test asserts that every rendered string appears in `paper.tex`.
4. One independent review and one author fix pass per artifact. A theorem-level defect stops the
   affected section and goes to Austin.
5. Unslop gate before delivery: no em dashes, no chatbot phrases, sentence-case headings in
   markdown, plain words in the paper.
6. The orchestrator owns git. Workers edit only assigned paths, preserve concurrent work, run no
   git, and report every file changed. One concern per commit.

## Operating rules

- Fail twice, stop. An item that fails its check or gate twice stops the whole operation. The
  orchestrator writes a one-page judgment and discusses it with Austin. No third attempt.
- Change assumptions when a proof fails once, if a cleaner assumption is available, and record
  the change in the ticket. A changed assumption counts as the second attempt if it fails.
- Empirics are descriptive. No causal claim, no control group, no identification language.
- Routing: the orchestrating session plans, arbitrates and owns git. Kimi (kimi-dispatch)
  authors, GLM (glm-dispatch) engineers and audits, Opus subagents judge; efforts are set per
  step in .scratch/v5-paper/orchestration.md. No Workflow tool.
- A delegated step is bounded to minutes. Every check script is a check run: the orchestrator
  starts it detached from the client, one at a time, and reads its record file. No model session
  waits on a computation (ADR 0004).
- `H` (the trading horizon) is a calibration parameter, not a speed knob. Do not lower it to make
  a run fit.
- Never use bare `git stash`. Set work aside with a temporary commit.

## Verification

```bash
# theory code
.venv/bin/python -m numerical_v4.smoke

# empirics
PYTHONPATH=. .venv/bin/python -m empirics.test_parse_13d
PYTHONPATH=. .venv/bin/python -m empirics.test_fingerprints   # number guard and gates, created by ticket 06

# paper and appendix (they cross-reference each other; keep this order)
xelatex -interaction=nonstopmode paper.tex
biber paper
xelatex -interaction=nonstopmode appendix.tex
xelatex -interaction=nonstopmode paper.tex
xelatex -interaction=nonstopmode paper.tex
xelatex -interaction=nonstopmode appendix.tex
```

TeX delivery requires zero errors, zero undefined references, zero undefined citations, and
visual inspection of both PDFs.
