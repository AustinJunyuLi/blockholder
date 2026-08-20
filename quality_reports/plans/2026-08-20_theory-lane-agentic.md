# Theory lane v2 — agentic (2026-08-20)

**Status:** APPROVED (2026-08-20)

## Context

The courier loop (author hand-carries every message between GPT Pro and the repo)
produced two good turns but is extremely slow — each round trip needs Austin at
the keyboard. Austin's decision: move the theory work into an agentic
environment run from this session; GPT Pro is consulted only at pivotal
moments. Austin also granted a scoped change to the routing rule: **Fable may
reason through the hardest theory bits directly** (not just orchestrate), with
Opus doing the bulk derivation/verification, Sonnet the mechanical work, and
Fable managing its own context tightly.

Current state (all committed on `v4-theory`, HEAD `d40f113`): model card v4.0;
eight results D1, P1, L1–L4, T1, C1, all CONJECTURE; D1/L1/L2 proofs on file
with Opus proof-read PASS; msg3 drafted (asks GPT for L3/L4 + the A7
construction). The stack's biggest open risk: whether injective A7 is
satisfiable on an actual plan menu. No two-round numerical implementation
exists yet; `HANDOFF_sign.md` (the empirics lane's only hard dependency) is
still unpublished.

## The new protocol (replaces the courier sections of the 08-19 handoff)

**Roles**
- **Opus agents** — proof writers (one per result); adversarial proof-readers
  (never the writer); independent re-derivers (statements-only input, never see
  the writer's proof); check-script writers and re-runners; implementation
  builder.
- **Sonnet agents** — search, extraction, LaTeX plumbing, file moves
  (effort low/medium).
- **Fable (this session)** — orchestrates; personally reasons only on the most
  challenging bits: (a) the A7 satisfiability construction, (b) adjudicating
  writer-vs-re-deriver disagreements, (c) design review of the two-round
  implementation architecture, (d) final coherence read of the stack before the
  GPT bundle. Everything bulky stays delegated.
- **GPT Pro** — exactly one courier moment plus escalation: one end-of-stack
  review of the complete bundle (card + proofs + raw check output). Escalation
  to GPT only when a claim fails twice in-house. **msg3 is NOT pasted**
  (Austin's decision): Thread 1 retires now with turns 1–2 as its record, and
  msg3 stays on file re-purposed as the spec for the local L3/L4 writers and
  the A7 work — its proof requirements are exactly the brief those agents get.

**Label discipline (unchanged in substance)**
CONJECTURE → PROVED needs: writer's proof + adversarial Opus proof-read PASS +
independent re-derivation PASS by an agent who never saw the proof. Executed,
committed check → NUMERICAL. GPT Pro's end review can demote, never promote by
prose. Every move logged `ID | old→new | evidence | who | date | commit`.
Finder ≠ verifier throughout; WRONG blocks with one retry; MISCITED/UNCHECKED
never block.

## Work plan

**Wave 1 — launch immediately, parallel (6 agents + Fable):**
1. Opus writer: **L3** proof (mean-value chord form 𝒞(π̄)=¼π̄²g″(ζ); C_h=0 case;
   A(τ) domain named with a satisfying and a non-satisfying structure).
2. Opus writer: **L4** proof (each nestedness hypothesis used; the
   "newly flagged is Voice" step identified).
3. Opus writer: **P1** existence proof (Brouwer route; adapt draft_v2's
   `prop:existence` architecture to the plan menu).
4. Opus builder: **two-round numerical implementation** design doc + skeleton
   (`numerical_v4/`: calendar, finite plan menu, pooled pricing on histories,
   flagged round, solver). Design reviewed by Fable before the build continues.
5. Opus: **ticket 05** — repo-model O-1 re-run
   (`quality_reports/fixes/t1_o1_rerun_check.py` + JSON) and publish
   **provisional `research/model_v4/HANDOFF_sign.md`** — unblocks the empirics
   lane.
6. Sonnet+Opus: **ticket 04** — the three literature cards, Chabakauri et
   al. (2022) first (the named live refuter).
- **Fable: the A7 satisfiability construction** — exhibit a plan menu on which
  injective A7 holds, or the weakest menu condition that delivers it; one Opus
  agent then attacks the construction.

**Wave 2 — as wave-1 proofs land:** adversarial proof-reads (fresh Opus,
batched); **T1** proof (needs L3/L4); C1 bounds + region-certification script
(needs the implementation).

**Wave 3:** independent re-derivations (statements-only) for everything that
passed proof-read → PROVED; check scripts for D1/L1/L2/L3/L4/T1 → run → commit
raw output → NUMERICAL where applicable.

**Wave 4:** `model_v4.tex` + md mirror (ticket 06 deliverable); update
`HANDOFF_sign.md` with the two-round number (earlier one kept visible);
assemble the **GPT Pro end bundle** (card + proofs + raw check output) as one
paste-ready file; Austin couriers it once.

## Files to write in the execution phase

- `quality_reports/handoffs/2026-08-20_theory-lane-v2-agentic.md` (v4-theory) —
  the protocol above; marks the courier sections of the 08-19 handoff
  superseded.
- `docs/adr/0008-agentic-theory-lane.md` (on `v4`, this checkout — the
  convergence owner owns `docs/adr/`) — short record of the restructure and the
  scoped Fable-may-reason grant.
- `quality_reports/plans/2026-08-20_theory-lane-agentic.md` (v4-theory) — this
  plan, per the plan-first rule.
- Memory update: `fable-orchestrates-only.md` gets the scoped exception
  (v4 theory lane: hardest bits only, context managed).
- Session log entries as work proceeds; commits + pushes on `v4-theory`
  (and one on `v4` for the ADR) per the existing discipline.

## Sizing and routing

Per `~/.claude/rules/native-workflow.md`: waves stay ≤ 12 agents (wave 1 is 6);
writers opus, proof-readers/judges opus, mechanical sonnet low; abort a wave
after 3 consecutive agent failures; every agent gets a stopping condition and
the premise it acts on; one retry with evidence, then escalate (ultimately to
GPT Pro per the failure rule).

## Verification

- Wave 1 ends with: three proofs on file + proof-read verdicts, an implementation
  design Fable has reviewed, a committed O-1 check JSON, and a pushed
  provisional `HANDOFF_sign.md` (the empirics lane can see it).
- The transformation itself is verified by the ledger: labels move only through
  the two-pass rule, every move logged, zero courier rounds consumed except the
  two planned ones.
- End state: all eight results labelled per their evidence, `make`-runnable
  check scripts committed with raw JSON, and one paste-ready GPT bundle.
