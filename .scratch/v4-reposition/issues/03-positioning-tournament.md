# 03 — Positioning tournament, then the author decides

**What to build:** Several independent position proposals (different tools and anchors), each a one-page brief: object, margin, anchor, main result to be proved, empirical design, what is new vs the competitor map, deliverability by December, supervisor continuity. Judged by independent judges on those criteria; the winner and runner-up adversarially checked against the cards. Ends with a plain-language brief to the author and a pause.

**Blocked by:** 01, 02.

**Status:** ready-for-human (tournament done 2026-08-19; awaiting the author's position decision — see research/positions/AUTHOR_BRIEF.md)

- [x] ≥ 4 independent proposals, each from a different tool/anchor family
- [x] Judge scores with reasons; winner and runner-up named
- [x] Adversarial check of the winner: every whitespace claim survives or the proposal is amended
- [x] Brief for the author written in plain language; ticket flips to `ready-for-human` and waits for the decision
- [ ] Decision recorded here under Comments and in an ADR; commit on `v4`

## Comments

- 2026-08-19 (ticket-03 session; author override of ADR-0005 routing: Kimi-K3-max proposers/judges, Grok-4.6-xhigh-fast checkers/writer; Composer banned after the harness was caught silently falling back to it on unknown Kimi slugs — only `kimi-k3-max` is genuine Kimi here). **Stage A:** 5 independent proposals, one per tool/anchor family — P1 tender-game × window→premium (W1+W12), P2 information-design × rule-keyed partition (W3, +W11), P3 Kyle-deadline MCS (W5+W6), P4 Feb-2024 × control-outcome matched DiD (W2, fallback W13), P5 13D/13G purpose partition (W7). **Stage B:** 3 independent judges, citations checked against cards. Totals /30: J1 P2 27 · P3 27 · P4 26 · P1 25 · P5 23; J2 P2 27 · P4 27 · P1 26 · P3 26 · P5 21; J3 P4 28 · P2 25 · P1 25 · P3 25 · P5 22. **Winner: P2** (2 of 3 first-place votes, Borda 14). **Runner-up: P4** (highest raw total 81/90; top-two for J2/J3, third for J1). **Stage C:** both finalists adversarially checked against the cards — both **SURVIVE WITH AMENDMENTS** (P2: 3, incl. CCKV gloss-as-quote and Thm-1 mischaracterization; P4: 5, incl. Trivedi t = 2.69 not ">3" and the ≤3 pp bound scoped to the accumulation channel only); every whitespace claim survived. **Stage D:** plain-language brief at `research/positions/AUTHOR_BRIEF.md` presenting P2, P4, and the judges' convergent third option (P2's model + P4's empirics). Open hazards owned by the author: Payne-Mann SSRN 5076900 PDF (decides P5's cell), BLV Dec-2025 revision, Zeng IA Table 2. **Pause: awaiting the author's decision among P2 / P4 / package; then the last checkbox (decision + ADR) completes.**
