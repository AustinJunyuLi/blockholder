# Handoff: v5 detection-frame rewrite, rounds 3 and 4

Written 2026-09-03 by the previous orchestrator. Rounds 1 and 2 are done. Rounds 3 and 4 remain.
Worktree `/Users/austinli/Projects/blockholder_v5`, branch `v5`. Nothing is committed yet.

## Read in this order

1. `CLAUDE.md`. The doctrine. Fail twice, stop. Workers run no git. Every number renders from a record.
2. `CONTEXT.md`. The vocabulary. Use its names for every paper object.
3. `.scratch/v5-paper/issues/16-detection-frame.md`. What the paper says and in what order. It supersedes ticket 15 and inherits the sections it lists from `.scratch/v5-paper/issues/15-theory-upgrade.md`.
4. `.scratch/v5-paper/grok/judgment-standing-conditions-2026-09-03.md`. Why the standing-conditions gate stopped and how Austin resolved it.
5. `~/.ringer/work/v5-detection-frame/round3.json`. The five round-3 briefs live in its `spec` strings: paper writer, figures, three record judges. They are complete and self-contained. Reuse them as the thread prompts, with the compile command and the guard command they embed.
6. `~/.ringer/work/v5-detection-frame/fill.json`. The render strings from the three records, the two fixed abstract phrases, the label of every new statement, and the orchestrator notes on the records' facts.
7. `~/.ringer/work/v5-detection-frame/attack_nits.md`. The 117 wording nits from the attack round, for the round-4 hypothesis audit.
8. `~/.ringer/work/v5-detection-frame/att-*/verdict.json`. The fifteen attack verdicts. All PASS except `att-standing-conditions` and `att-standing-conditions-2`, which the judgment covers.

## Decisions already made

- The standing-conditions repair is applied: (S6) says the filing coordinate is public on every history and the pooled history is visible on the pooled cell; Step 6 of the partition lemma cites it that way. Austin waived the third attack gate on 2026-09-03. Do not re-attack the block. Do not reopen (S6) or (S13).
- Labels: fourteen new statements PROVED, `prop:regret` NUMERICAL. `fill.json` lists them. Prose never promotes one.
- The 3-against-5 clock pair is null at every node. The paper states it as a fact of the calibration, never as a result. T = 3 is a grid extension. T = 10 nodes are one pool.
- Abstract phrase one is `several times higher`. Phrase two is `17.5 to 54.3 percent`, the clock's level effect at kappa 0.85 across nodes.
- The threshold's largest magnitude below kappa 0.45 is the record's `5.99 percent`. Ticket 16's "below 0.3 percent" came from the tightest pair alone and is superseded by the record.
- The records are final. Never rerun a `t6_*` script on the full grid; the three full-grid runs took about fifty minutes and every check passed.

## State of the worktree

Done and gated:

- `proofs/07_detection.tex`, `proofs/08_blackwell.tex` (new), `proofs/02_garbling.tex`, `proofs/03_caught.tex`, `proofs/04_inherited.tex`, `proofs/09_regret.tex` (edited), `appendix.tex` (inputs the fragments, cites (S1) to (S14)).
- `numerical_v4/checks/t6_detection_check.py`, `t6_cut_check.py`, `t6_regret_check.py` and their `.json` records on the full grid.
- `empirics/test_fingerprints.py` gained `GridRecordGuardTest`: every string from each script's `render(record)` must appear in `paper.tex`.

Partial, from the interrupted round 3:

- `paper.tex` carries about 190 lines of an interrupted writer's edits on top of three citation edits from the orchestrator. Revert it in step 0.
- `numerical_v4/checks/figures.py`, `figures/fig4_level_effects.pdf`, `figures/fig2_who_gets_caught.pdf` carry the figures worker's changes. Keep them only if the figures script reruns clean in step 0.

Untracked scratch that is never staged: `prime-agent-session-*.html`, `numerical_v4/checks/t2_l3_check.json`, `.scratch/v5-paper/hunt/gpt-pro-4/*.pdf`.

## Structure

One orchestrator thread owns git, runs every gate, and writes no prose. One fresh thread per job. A thread never reviews what it wrote. Every gate is a script that exits 0; the scripts are in `~/.ringer/work/v5-detection-frame/checks/` and run without Ringer. Effort: writer and author fix at max, judges and referee and nits editor at high, orchestrator at high, unslop and delivery at low.

## Steps

### Step 0. Clean base

```bash
cd /Users/austinli/Projects/blockholder_v5
git checkout -- paper.tex
sed -i '' 's/(S1) to (S11)/(S1) to (S14)/g; s/^(S11) in the appendix/(S14) in the appendix/' paper.tex
PYTHONPATH=. .venv/bin/python numerical_v4/checks/figures.py
```

Done when: `paper.tex` has no `(S11)`; the figures script exits 0 (else `git checkout -- numerical_v4/checks/figures.py figures/fig2_who_gets_caught.pdf` and delete `figures/fig4_level_effects.pdf`); the six-command compile order in `CLAUDE.md` runs with zero errors in `paper.log` and `appendix.log`; the number guard fails only in `GridRecordGuardTest`, which the writer will satisfy.

### Step 1. Round 3, five threads in parallel

Prompts: the five `spec` strings in `round3.json`, verbatim. Each thread works in its own scratch directory for `notes.md` or `verdict.json` and edits only its owned paths in the worktree.

Done when: `check_paper.py --repo <worktree> --notes <writer notes>` prints PASS; the figures gate in `round3.json` passes; each `verdict.json` passes `check_verdict.py` and reads PASS. The judges' recomputations take the compute lock themselves, so they serialise. A judge FAIL on any record stops the operation and goes to Austin.

### Step 2. Round 4, serial

1. Appendix nits editor. Owns `proofs/` and `appendix.tex`. Applies `attack_nits.md` and the six wording nits in `att-standing-conditions-2/verdict.json`: the dead hook pair around (S12) to (S14) in `04_inherited.tex`, (S12)'s notation, (S13) saying cells at depth d, (S12) stating the mark support, `03_caught.tex` citing the two-cell lemma beside (S9). Wording only: no new statement, no changed hypothesis. Done when `check_proofs.py` passes and the compile order runs clean.
2. Referee. Read-only, fresh thread, on the compiled `paper.pdf` and `appendix.pdf` against ticket 16 and the label rules. Output is a fix list with a severity per item. A theorem-level finding stops the operation and goes to Austin.
3. Author fix. Owns `paper.tex`. Applies the list in one pass. Done when `check_paper.py` passes again.
4. Unslop. No em dashes, no chatbot phrases, plain words, sentence-case markdown headings. Done when `grep -c '—' paper.tex appendix.tex proofs/*.tex` prints zero on every file and one read of the abstract and introduction finds nothing to cut.
5. Compile in the project order. Open both PDFs and look at every page: figures render, tables fit, no overfull boxes in the margins, labels print on every statement. Copy `paper.pdf` and `appendix.pdf` to `deliverable/`.

### Step 3. Commit and push

One concern per commit, in this order, staging named paths only:

1. Records: the three `t6_*` scripts and `.json` files, the guard test.
2. Proofs: `proofs/`, `appendix.tex`.
3. Figures: `figures.py`, the figure PDFs.
4. Paper: `paper.tex`, `paper.bib`.
5. Deliverable: `deliverable/`.
6. Scratch: the judgment and this handoff under `.scratch/v5-paper/grok/`.

Then `git push origin v5`. Done when the push succeeds and the commit list is reported to Austin.

## Hazards seen in rounds 1 and 2

- The `t6_*` scripts acquire and release the compute lock themselves. Writing the lock for them deadlocks them; the detection run sat idle for twenty minutes that way.
- `check_record.py` requires a `notes.md` beside the record. That is a task artifact, not a property of the record.
- The cut record's rendered share ranges are the strings to print. The raw share on a single clock pair runs wider at individual kappa values, and inside a threshold pair's reversal interval the net cut leg crosses zero and the share is undefined. The paper never quotes a share from the raw rows.
- `paper.tex` and `appendix.tex` cross-reference through `xr` with prefix `app:`. Out-of-order compiles leave undefined references that look like missing labels.
- Bare `git stash` is forbidden; the stash is shared across worktrees.
