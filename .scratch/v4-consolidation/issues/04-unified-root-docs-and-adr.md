# 04: Unified root instructions + superseding ADR

**What to build:** An agent landing on the integrated branch reads one truthful set of instructions: one active branch, protected theory and empirical areas, no lane-split rules. Must land immediately after the merge — the raw merge installs theory-lane docs ("do no empirics work here") on the canonical branch.

**Blocked by:** 03.

**Status:** ready-for-agent

- [ ] `CLAUDE.md` rewritten: merges the v4 empirics-lane content (v4 CLAUDE.md:141-145) and theory-lane rules (theory CLAUDE.md:9-79) into one authority table per the handoff's "Authority boundaries after consolidation"; the nine false statements listed in `authority_digest.md` all gone
- [ ] `AGENTS.md` rewritten likewise (theory AGENTS.md:9 lane rule removed)
- [ ] `CONTEXT.md`: glossary only — touch only if a term crystallised; no lane rules exist in it
- [ ] `docs/adr/0009-consolidated-single-branch.md`: supersedes ADR-0007 (kept as history), notes ADR-0008:31-33's "two-lane split unchanged" clause retired; records staging-branch merge, frozen/never-touch areas (incl. `bid12_coding_rules.md` hash-stamp), worktree retirement + tag
- [ ] Correct `CONTEXT.md`'s `Timing split` glossary entry: it is the registered overlapping `RUNUP`/`JUMP` return-window contrast, not the model's latent flagged/pooled states and not Position 1's headline
- [ ] Add a separate `docs/adr/0010-position-1-legal-clock-paper.md`: supersede ADR-0006 while retaining it as history; record Position 1, E1 as the sole authorised December headline, H1/H2/dose/stake/placebo/BID12 as viewed appendix evidence, frozen-theory protection, and `NO` causal claim
- [ ] WRDS to-do migrated out of `HANDOFF.md` into the empirical doc(s) citing it (`empirical_feasibility.md:32,106`, `data_inventory.md:85,123`); `data_inventory.md:123` backup claim annotated as stale (two SHA-256 copies per SPEC.md:1448)
- [ ] Follows `mattpocock-skills:writing-for-agents` guidance; root docs in one commit and the two ADRs in a separate commit if cleaner

## Comments
