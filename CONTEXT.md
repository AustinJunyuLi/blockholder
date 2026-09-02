# CONTEXT.md

Glossary for the v5 paper. Terms only. No implementation detail, no history.

### The model

**Partition**:
The split of every possible history of the blockholder into a flagged cell and a pooled cell,
induced by the disclosure rule.

**Flagged cell**:
The histories in which the disclosure filing has landed by the trading date. The market knows
the blockholder is engaged.
_Avoid_: disclosed state, revealed state

**Pooled cell**:
The histories in which no filing has landed. The market infers engagement from order flow alone.
_Avoid_: hidden state, undisclosed state

**Threshold margin**:
The stake level at which the filing obligation starts, written τ. One of the two dials.

**Window margin**:
The number of trading rounds between crossing the threshold and the filing landing, written T.
The other dial. The clock.
_Avoid_: deadline (use only for the legal rule), lag

**Liquidity**:
The noise-trading intensity κ: the probability that the noise trader trades in a round. Higher κ
is a noisier, more liquid market.

**Order size**:
The blockholder's per-round order while building the stake, equal to two noise lumps. Fixed by
ADR 0003.

**Two dials**:
The headline. Tightening the threshold lowers the noise sensitivity of prices at fixed
policies, under the condition the theorem states. Shortening the clock does so if and only if the newly caught histories are at least as
noise-sensitive as the pool.

**Weight effect / Composition effect**:
The two halves of what a tighter dial does. The weight effect moves mass from the pooled cell to
the flagged cell and always attenuates. The composition effect changes who is left in the pool,
and its sign depends on the dial.

**Who gets caught**:
The corollary that signs the composition effect of the clock: the composition ratio is at most
one exactly when the histories the shorter clock newly catches are at least as noise-sensitive
as the pooled cell.

**Stake at filing**:
The blockholder's holding on the day the filing lands, written B^F. An object the model produces
and the first exercise measures.

**Run-up / Jump**:
The price move from the trigger to the day before the filing lands (run-up, R) and the move on
the reaction day (jump, J). Their sum is the total revaluation.

**Fixed policies**:
A comparison of two disclosure rules with the blockholder's plan held fixed. Every headline
result is stated this way.

### The empirics

**Exercise**:
One registered descriptive measurement. E1 is stake at filing. E2 is run-up versus jump by
pre-trigger liquidity. Nothing else.

**Campaign**:
The unit of every exercise: one (subject firm, trigger date) pair. Simultaneous group filings
collapse to the earliest acceptance.

**Trigger date**:
The date of the event that requires filing, read from the filing.

**Filing date**:
EDGAR's filing date for the accession.

**Reaction day**:
The first trading day on which the filing can move the price: the filing date if EDGAR accepted
the filing before 16:00 New York time, otherwise the next trading day.

**Pre-trigger liquidity**:
The Amihud illiquidity ratio over the trading days before the trigger, in the span the spec
states. The empirical stand-in for κ.

**Gate**:
A binding check on measurement quality, registered before the run. A failed gate makes the
exercise absent from the paper.

**Result file**:
The one JSON file per exercise from which every manuscript number is rendered.

**Registration**:
The commit of `empirics/spec.md` that precedes the run. Git order is the evidence.

### Labels and process

**Honesty label**:
The tag every result carries: PROVED, NUMERICAL (verified on the stated grid), ESTIMATED (an
empirical estimate with a stated design and a standard error). CONJECTURE is a working label that
never ships.

**Attack gate**:
A proof written by one worker and read by a second worker who did not write it and tries to
break it: a missing hypothesis, a step that does not follow, a counterexample. The only route
from CONJECTURE to PROVED. A blind re-derivation from the statement is not this gate.
_Avoid_: two-pass gate, re-derive

**Batch**:
A group of tickets one implementing session runs to completion before anyone reviews it. It
ends when every step has its result file.

**Checkpoint**:
The review between two batches: the gates only the reviewers may run, the check runs, the
commit, and the note the next batch reads.

**Check run**:
One execution of a check script that writes a record file. The orchestrator starts it and reads
the record. A delegated model never waits on one.

**Brief**:
The referee notes in `docs/` that inform the rewrite. Input, not authority.
