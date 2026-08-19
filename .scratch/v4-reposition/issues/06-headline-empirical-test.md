# 06 — Run the headline empirical test

**What to build:** The one clean result from the spec, estimated on data on disk (CRSP snapshot, parsed 13D universe, EDGAR pulls via the existing pipeline), with the script and a data manifest committed and re-run by a verifier. Parser bugs on the path get fixed with an assert-based check. If a fresh WRDS pull is genuinely required, the author is asked to log in first — nothing else waits on it.

**Blocked by:** 05.

**Status:** ready-for-agent

- [ ] Estimate, standard errors, and the pre-specified robustness table produced by a committed script
- [ ] Verifier re-runs the script from the manifest and matches the numbers
- [ ] Parser fixes with checks (if touched)
- [ ] Plain-language result note (supportive / against / bounded null) — no spin
- [ ] Commit on `v4`

## Comments
