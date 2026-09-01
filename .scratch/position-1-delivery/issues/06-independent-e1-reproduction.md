# P1-06: Independently reproduce E1

Status: ready-for-agent
Blocked by: P1-05

## What to build

Have a reviewer who did not implement P1-03 or P1-05 reproduce E1 from a clean worktree and the registered entry point.

## Acceptance

- [ ] Start from the committed protocol, manifest, code, and hashed inputs in a clean environment; record commit, environment, commands, and input hashes
- [ ] Reproduce denominator counts, gate arithmetic, complete-case estimates, worst-case bounds, confidence intervals, MDEs, table, CDF data, and rendered CDF
- [ ] Require exact agreement for deterministic counts and data. Use only tolerances declared in the protocol for floating-point or rendered output and report every comparison
- [ ] Verify that old Fact 1, viewed empirical artifacts, frozen theory trees, and BID12 rules remain unchanged
- [ ] Save an independent reproduction report with a blunt `PASS` or `NO-GO` and its evidence hashes
- [ ] Any unexplained difference blocks P1-07. The reproducer does not tune the estimator or patch the adopted artifact to make it pass

## Comments
