# 06 · Build the campaign table, the price link, and run E1

**Lane:** empirics. **Routing:** opus default; a second agent runs the tests.
**Blocked by:** none (the spec is registered). **Blocks:** 07, 08, 10, 11.

**What to build.** `empirics/fingerprints.py` following `empirics/spec.md` exactly:
the loader over all twenty quarterly indexes and both cache naming schemes (fetch and cache the
missing texts with the throttled fetcher, count them); the campaign collapse; the stake column
from the existing parser; the CUSIP read (XML `issuerCUSIP`, cover-page line otherwise); the CRSP
link and its fallback; the equal-weighted market return from the CRSP file; the reaction-day
rule; R, J, and Amihud; the gates as functions; the E1 run writing `e1_estimate.json`
(with the `clock` block), `e1_campaigns.csv`, `e1_stake.pdf`. `empirics/test_fingerprints.py`
holds gate checks, the number guard (renders every reported number and asserts presence in
`paper.tex`, skipping when the file does not exist yet), and unit checks on the reaction-day and
delay rules against three hand-dated cases. E2 is built but not run in this ticket.

**Acceptance.**
- [ ] `PYTHONPATH=. .venv/bin/python -m empirics.fingerprints build` writes the campaign table
      with coverage counts (evidence: the counts).
- [ ] `... run e1` writes the result file; E1-G1 and E1-G3 evaluated and recorded; E1-G2 left
      for ticket 07.
- [ ] Tests pass; the second agent reruns from the cache and matches the result file exactly.
- [ ] The spec was not edited. Any measurement question is reported, not resolved by editing.

**Status:** done, committed 29cb8e5 on v5 (2026-09-02)

## Comments
