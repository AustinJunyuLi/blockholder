# P1-09: Independently verify the clean final delivery

Status: ready-for-agent
Blocked by: P1-08

## What to build

Use a fresh reviewer who did not write P1-07 or P1-08 to give the complete repository and paper a final `GO` or `NO-GO`.

## Acceptance

- [ ] From the final commit, rerun the registered E1 reproduction and both document builds; verify artifact, table, CDF, PDF, and source hashes
- [ ] Check every manuscript E1 number against `e1_estimate.json` and every appendix exercise against its preserved viewed artifact
- [ ] Recheck all Position 1 claims against the review, Position 1 ADR, frozen theory card, and empirical labels. Confirm no causal claim, no unconditional window sign, and no promotion of `NOT ESTIMATED`
- [ ] Verify frozen tree hashes, BID12 rules hash, old Fact 1 hashes, and all viewed-result hashes are unchanged
- [ ] Inspect the final PDFs independently for prose and visual defects; reopen P1-08 for any material defect
- [ ] Run the repository verification gates and record exact commands. `git status --short` is empty apart from documented ignored local dependencies, with no undeclared untracked files
- [ ] Save `quality_reports/verification/YYYY-MM-DD_position_1_final_delivery.md` with the commit, hashes, checks, remaining limitations, and blunt `GO` or `NO-GO`
- [ ] Mark delivery complete only on `GO`; otherwise preserve all evidence and leave the failed gate explicit

## Comments
