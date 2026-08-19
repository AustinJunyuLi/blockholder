# Blockholder paper (v4)

The economics of one paper: how market liquidity, the legal rule that forces a
large shareholder to reveal itself, and control outcomes (takeovers, activism
success) interact. This glossary fixes the words every agent and draft must use.

## Language

### The paper

**Position**:
The paper's claim to open ground: its object, the margin of the disclosure rule it studies, and how it identifies the effect.
_Avoid_: angle, framing, pitch

**Whitespace**:
An object, margin or identification that no paper in the competitor set has occupied. A position must sit in whitespace.
_Avoid_: gap, novelty

**Competitor set**:
The named papers a position is judged against: Celentano–Levine, Johnson–Swem, Cetemen–Cisternas–Kolb–Viswanathan, Albuquerque–Fos–Schroth, Back et al. 2018, Trivedi, Corum, Polk et al., and the author's own `proposal/` outline.

**Anchor**:
The institutional fact or setting the position rests on (a rule, a threshold, a dated change).
_Avoid_: hook, motivation

**Deliverability**:
Whether the author can robustly finish a piece by the December package without new tools, data or coauthors. A ranking criterion, not a nice-to-have.

**December package**:
The department-review deliverable: a full draft (draft_v3) with a clean core model and one clean empirical result, plus a written empirical spec for the rest. Never described as a job-market paper; never names a journal.

**Clean result**:
One empirical estimate whose design and data survive the referee checklist and that can be re-run from files in hand.

**Honesty label**:
The tag every result carries: PROVED, NUMERICAL (verified on a grid), or CONJECTURE. Labels are never weakened by editing.

### The model

**Blockholder**:
The single large shareholder with a private signal who trades and may engage.
_Avoid_: activist (unless the blockholder has chosen voice), investor, fund

**Core model**:
The minimal set of primitives, timing and equilibrium notion from which the main result is stated. Rebuilt clean for v4; not a patch of draft_v2.

**Disclosure rule**:
The legal rule (a stake threshold plus a filing window) that forces public revelation of a stake and its purpose. In the US: Schedule 13D.
_Avoid_: reporting regime, transparency requirement, 13D filing (when the rule, not the document, is meant)

**Partition**:
The split of what the market observes into a *flagged* state (disclosure has occurred) and a *pooled* state (it has not). The disclosure rule is the market's partition; this is the paper's identity.
_Avoid_: signal, information structure

**Threshold margin**:
The part of the disclosure rule fixing which stake sizes trigger disclosure (5% in the US, 3% in the UK). Moving it changes who is flagged.

**Window margin**:
The part of the disclosure rule fixing how long after crossing the threshold the filing may wait (10 → 5 business days on 2024-02-05). Moving it changes how much trading happens before the flag.

**Liquidity**:
Noise-trading intensity, the model's κ; empirically an Amihud-type illiquidity measure inverted. The paper's driving variable.
_Avoid_: depth, volume, turnover (unless that is the measured proxy)

**Control outcome**:
What the blockholder's engagement changes for shareholders: bidder entry, takeover premium, or campaign success. Broadened from "takeover premium" alone.

**Premium wedge**:
The gap in expected takeover premium between an engaged and an unengaged target (m₁ − m₀ in draft_v2; λ-scaled in the tender game).

**Exit / Hold / Quiet voice / Public voice**:
The blockholder's four actions in draft_v2: sell; stay passive; engage below the disclosure threshold; buy above it and be flagged. Machinery, not identity — the core model may collapse them.

**Disclosure attenuation**:
The claim (draft_v2's T2) that a stricter disclosure rule lowers how much control outcomes move with liquidity. Its sign depends on the margin (threshold vs window).

**Hump**:
The claim (draft_v2's R1) that minority gains from control are non-monotone in liquidity. Certified only on a grid; disposable.

### The empirics

**Feb-2024 acceleration**:
SEC Release 33-11253: 13D window 10 → 5 business days from 2024-02-05; 13D/A 2 business days; 13G changes from 2024-09-30. A candidate anchor, already used by Trivedi, Corum, Polk et al. and the author's `proposal/`.
_Avoid_: the reform, the shock (say which)

**Referee checklist**:
The fixed list a design must pass: control group or bounded null, confound list (EDGAR cut-off, anticipation, T+1), power/MDE, placebo, pre-trend, parser validation.
