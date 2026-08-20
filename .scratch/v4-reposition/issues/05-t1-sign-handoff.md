# 05 — T1 · Re-run O-1 and publish the sign handoff

**Lane:** theory (`v4-theory`, other machine)

**Routing:** per ADR-0005 — an Opus agent runs and reads the experiment; Sonnet for file plumbing; a separate Opus verifier who did not write the script re-runs it and reports WRONG / MISCITED / UNCHECKED.

**What to build:** The theory lane's first milestone and the empirics lane's only dependency. Reproduce the referee's O-1 experiment — the window margin, public buy flagged versus pooled, at fixed cutoffs — in the current repo model, starting from the committed claim, and confirm or refute that window-margin attenuation is false at baseline. Then re-run the same experiment in the two-round model as soon as that model exists. Separately, find a data anchor for the flagged share (the share of engagements that get disclosed) so the calibration is an empirically meaningful number. Publish the answer to `research/model_v4/HANDOFF_sign.md`: sign, magnitude, the condition under which it holds, and the date. Publish an honest placeholder early rather than making the empirics lane wait.

**Blocked by:** None for the repo-model re-run. The two-round re-run needs 06 (T2).

**Status:** ready-for-agent

- [ ] O-1 reproduced in the repo model by a committed check script under `quality_reports/fixes/`, run with the project virtualenv; numbers match the committed referee claim or the difference is explained
- [ ] `research/model_v4/HANDOFF_sign.md` written with sign, magnitude, condition and date — a placeholder version published early and marked as provisional if the two-round re-run is not yet possible
- [ ] The two-round re-run added to the same file once 06 lands, with the earlier number kept visible rather than overwritten
- [ ] A flagged-share data anchor named with its source, or its absence stated plainly
- [ ] A verifier who did not write the script re-runs it and matches the numbers
- [ ] Session log entry and commit on `v4-theory`; the branch pushed so the empirics lane can pull the handoff

## Comments

2026-08-20: a wave-1 agent for this ticket was launched and killed by a session restart before producing any output. Ticket stands ready; re-run under the lane-v2 protocol (quality_reports/plans/2026-08-20_theory-lane-agentic.md).
