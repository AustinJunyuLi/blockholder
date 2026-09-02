# Hunt log

Administered by Prime Agent session 01a062f7-8328-74d1-b3ab-65d6de96840e (Fable), started
2026-09-02T17:42. Handoff: /tmp/blockholder_v5_handoff/theory-hunt-handoff.md.

## Workers spawned

| Candidate | Directory | Worker | Model | Thinking | Child id |
|---|---|---|---|---|---|
| 4.1 erasure regime | 1-erasure-regime | hunt-erasure | openai-codex/gpt-5.6-sol | xhigh | sub-fd74c021 |
| 4.2 one cut identity | 2-one-cut-identity | hunt-cut-identity | openai-codex/gpt-5.6-sol | max | sub-b5ff30e8 |
| 4.3 Blackwell tightening | 3-blackwell-tightening | hunt-blackwell | openai-codex/gpt-5.6-sol | xhigh | sub-3ecbcf51 |
| 4.4 benchmark regret | 4-benchmark-regret | hunt-regret | openai-codex/gpt-5.6-sol | high | sub-8a6cab2a |

## Attacks

Attacker is Opus (`anthropic/claude-opus-5`) for every memo written by Sol.

| Candidate | Memo status | Memo received | Attacker | Child id | Verdict |
|---|---|---|---|---|---|
| 4.1 erasure regime | PASS | 2026-09-02T17:54 | attack-erasure | sub-978fb927 | PASS, five nits (attack.md) |
| 4.4 benchmark regret | PASS | 2026-09-02T17:58 | judge-regret | sub-860e781b | PASS, five nits (attack.md); one-node recompute bit for bit |
| 4.3 Blackwell tightening | PASS | 2026-09-02T18:03 | attack-blackwell | sub-ff4bf664 | PASS, eight nits (attack.md); 13500 kernel cases, 34560 LPs |
| 4.2 one cut identity | PASS (both parts) | 2026-09-02T18:04 | attack-cut-identity | sub-a6883c4c | PASS on both parts, eight nits (attack.md); certificate script byte-identical rerun |

## Verdicts

| Candidate | Writer | Memo | Attacker | Gate | Label the memo would support | My rank |
|---|---|---|---|---|---|---|
| 4.3 Tightening is a Blackwell improvement | Sol xhigh | PASS | Opus 5 | PASS, 8 nits | PROVED after nits | 1 |
| 4.1 Order size two is the erasure regime | Sol xhigh | PASS | Opus 5 | PASS, 5 nits | PROVED after nits | 2 |
| 4.2 One cut identity for both dials | Sol max | PASS (both parts) | Opus 5 | PASS, 8 nits | Part 1 PROVED; Part 2 implication PROVED, calibration NUMERICAL | 3 |
| 4.4 Certified benchmark regret | Sol high | PASS | Opus 5 (judge) | PASS, 5 nits | NUMERICAL, no label change | 4 (record, not a theorem) |

Paths: memo.md, attack.md and the attacker's scripts sit in each candidate directory under
`.scratch/v5-paper/hunt/`. Survivors hand to the writing thread's orchestrator at checkpoint 2 or 3
by path; labels are set there, not here. Nothing under `.scratch/v5-paper/issues/` was touched.

Why this order. 4.3 is a theorem that changes what the paper can say first ("tightening always
improves what the market knows"); its content is the identification hypothesis (S14), which the
attacker confirmed is the only load-bearing addition, and it is strict at T = 5 and an equality at
the corner T = 10. 4.1 is cheap and answers the referee's "why order size two" with a proposition
whose b = 2 half is Lemma g2 verbatim; the attacker corrected one side remark (the 2/3 turn and
"incomparable" are one-round facts). 4.2 unifies the composition legs into one corollary (Part 1
is a transcription) and adds a kappa-interval certificate whose largest root is the exact endpoint
of the Condition D failure; the attacker's nit 8 matters for the reading, since at the threshold
dial the caught leg is dominated by survivor re-pricing (1/phi about 40). 4.4 is a record: it
answers "why care about this benchmark" with one number per node (2.4e-4 at most, about 0.6% of
the payoff level at the cutoff) and belongs in the calibration section, not in a theory pack.

GPT Sol Pro pack 3 (`gpt-sol-pro-pack-3.md`, prompt `gpt-sol-pro-prompt-3.txt`) carries the top
three with the memos' statements and proofs and the attackers' verdicts and nits, and asks for a
ranking and appendix-level proof sketches. Pack 2 (`gpt-sol-pro-pack-2.md`) is the earlier,
pre-memo version and is superseded.
