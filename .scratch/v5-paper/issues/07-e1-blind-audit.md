# 07 · E1 blind audit (E1-G2)

**Lane:** empirics. **Routing:** opus default; must not be the agent that wrote the parser or
the loader. **Blocked by:** 06. **Blocks:** 11.

**What to do.** Draw sixty campaigns at random (seed 5), stratified by year and parser route,
from `e1_campaigns.csv`. Read each filing's cover page and Item 4, record the stake and trigger
date by hand into `empirics/output/e1_audit.csv`, and count material errors against the parsed
values. Write the count into `e1_estimate.json` under `gates.E1-G2` with PASS or NO-GO.

**Acceptance.**
- [ ] Sixty hand-coded rows with the excerpt that supports each reading.
- [ ] Gate evaluated and written; a NO-GO suppresses every E1 number.

**Status:** done, committed 16292f9 on v5 (2026-09-02)

## Comments
