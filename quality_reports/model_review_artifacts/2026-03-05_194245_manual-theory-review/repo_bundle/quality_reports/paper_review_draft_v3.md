# Manuscript Review: Liquidity, Activism Disclosure, and Takeover Premia

**Date:** 2026-03-05
**Reviewer:** Codex (`review-paper` workflow)
**File:** `/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex`

## Summary Assessment

**Overall recommendation:** Revise & Resubmit

The paper has a real core idea: combining activist mode choice, order-flow inference, and disclosure into a single takeover model is interesting, and the disclosed-versus-nondisclosed split is a potentially useful way to organize the economics. The discrete order-flow setup is tractable, and conditional on a few key assumptions the posterior formulas and price decomposition are coherent.

The main problem is that several central claims currently depend on assumptions stronger than the text admits. In particular, the disclosed branch is treated as if `D=1` reveals activism with certainty, but the model only proves that `(+1,1)` dominates `(+1,0)` for sufficiently high signals, not globally. That gap propagates into the posterior formulas, the disclosed-branch invariance claim, and the disclosure-attenuation mechanism. In addition, the existence proof is not valid as written, the nonmonotonicity result is numerical rather than theorem-level, and the welfare section mixes objects that are not obviously on the same unit basis.

Economically, the paper also needs tighter discipline. The model is motivated by activist intervention in underperforming firms, but the current signal/cost structure makes activism more attractive at higher standalone fundamentals. The takeover mechanism also gets its headline deterrence result by assumption rather than derivation. I think the paper is salvageable, but it needs sharper framing and cleaner theorem statements before the contribution is ready.

## Strengths

1. The disclosed versus inferred activism distinction is genuinely interesting and could produce a useful theoretical contribution.
2. The discrete order-flow environment keeps the inference problem transparent and makes the posteriors interpretable.
3. The paper is ambitious in trying to connect governance choice, liquidity, disclosure, and takeover outcomes in one framework.

## Major Concerns

### MC1: The disclosed branch is not identified as claimed
- **Dimension:** Identification / Econometrics / Argument
- **Issue:** The paper repeatedly uses `D=1 => a=1`, but the model only proves that Public Voice dominates Quiet Accumulation for sufficiently high signals. The stronger global exclusion of `QA=(+1,0)` requires extra Assumption `(A8)`, which is explicitly not part of the standing assumptions.
- **Why it matters:** Proposition `\ref{prop:posteriors}`, the conditional means on the disclosed branch, and the disclosed-branch invariance argument all rely on `D=1` revealing Public Voice. As written, those results do not follow from the model.
- **Suggestion:** Either impose and foreground a stronger assumption that globally eliminates `QA`, or enlarge the disclosed-state posterior system so that `D=1` mixes over `(+1,0)` and `(+1,1)`.
- **Location:** [draft_v3.tex:333](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L333), [draft_v3.tex:977](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L977), [draft_v3.tex:994](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L994), [draft_v3.tex:1052](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L1052), [draft_v3.tex:1102](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L1102)

### MC2: The existence proof is not mathematically valid as written
- **Dimension:** Econometrics / Presentation
- **Issue:** The proof invokes bounded fundamentals even though `v` is Gaussian, and it claims order-flow probabilities are bounded away from zero because noise has full support. That is false when action regions collapse or when an action probability is zero.
- **Why it matters:** Those premises are used to justify continuity and Brouwer. Proposition `\ref{prop:existence}` is therefore not established on the page.
- **Suggestion:** Rewrite the proof using continuity of Bayes objects only on reached states, plus explicit treatment of zero-probability states and degenerate action regions. If existence is only shown under extra restrictions, state them as assumptions rather than proof steps.
- **Location:** [draft_v3.tex:163](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L163), [draft_v3.tex:1325](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L1325), [draft_v3.tex:1327](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L1327)

### MC3: The headline hump result is numerical, not a theorem from primitives
- **Dimension:** Argument / Presentation
- **Issue:** The text says the paper establishes nonmonotonicity from primitives, but the formal proposition only says the hump appears in the baseline calibration, and the proof confirms that the result is established numerically. The Weierstrass remark is also wrong: it guarantees a maximizer on a compact set, not an interior peak.
- **Why it matters:** The abstract and introduction currently oversell robustness. Right now the hump looks like a calibrated pattern, not a general theoretical implication.
- **Suggestion:** Reframe the result honestly as a calibrated comparative static unless you can prove sufficient conditions for an interior maximizer.
- **Location:** [draft_v3.tex:561](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L561), [draft_v3.tex:576](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L576), [draft_v3.tex:594](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L594), [draft_v3.tex:1354](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L1354)

### MC4: The economic mechanism is not aligned with the paper’s motivation
- **Dimension:** Argument / Literature
- **Issue:** The introduction motivates activism as a response to underperformance, but the model’s signal is about standalone firm value and engagement becomes more attractive as the signal rises because costs fall with `s`.
- **Why it matters:** Low-signal firms are exited and high-signal firms get voice. That is hard to reconcile with the usual economics of activism unless `s` is reinterpreted as mispricing, latent improvement potential, or campaign profitability rather than firm quality.
- **Suggestion:** Reinterpret the signal, or change the primitives so that activism is tied to governance slack rather than high levels of `v`.
- **Location:** [draft_v3.tex:67](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L67), [draft_v3.tex:163](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L163), [draft_v3.tex:217](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L217), [draft_v3.tex:345](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L345)

### MC5: The paper advertises price feedback, but the model strips price from entry
- **Dimension:** Literature / Argument
- **Issue:** The paper motivates itself using price-feedback logic, but the bidder conditions on `(X,D)` directly and the bid rule is explicitly independent of `P_trade` and `P_post`.
- **Why it matters:** The mechanism is really an information-feedback model, not a stock-price-feedback model in the Edmans-Goldstein-Jiang sense. That weakens the novelty claim and the way the paper is positioned in the literature.
- **Suggestion:** Either reintroduce actual price-based bidder entry, or rewrite the contribution around order-flow inference and disclosure rather than price feedback.
- **Location:** [draft_v3.tex:67](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L67), [draft_v3.tex:247](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L247), [draft_v3.tex:299](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L299), [draft_v3.tex:701](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L701)

### MC6: Welfare accounting is not yet defensible
- **Dimension:** Econometrics / Argument
- **Issue:** `W_min` is defined as takeover premia per minority share, `W_B` is expected blockholder utility with 1 or 2 shares plus trading cash flows, and `W_bid` is bidder surplus. These are not obviously on the same scale. The simplified aggregate welfare expression also appears to omit the target’s standalone value in bid states if `\bar S` is incremental synergy.
- **Why it matters:** The policy conclusion that socially optimal liquidity exceeds minority-optimal liquidity is not persuasive until the welfare units and transfer accounting are fully pinned down.
- **Suggestion:** Define total share supply and ownership masses explicitly, distinguish level welfare from gains relative to the standalone benchmark, and then rebuild the welfare section from those primitives.
- **Location:** [draft_v3.tex:748](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L748), [draft_v3.tex:752](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L752)

## Minor Concerns

### mc1: Disclosure attenuation proposition overclaims
- **Issue:** Proposition `\ref{prop:disclosure-attenuation}` claims strict attenuation in `\omega_P`, but the proposition itself holds cutoffs fixed, so `\omega_P` is not varying inside the exercise.
- **Suggestion:** Downgrade this to intuition or prove the comparative static in a properly parameterized family.
- **Location:** [draft_v3.tex:610](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L610), [draft_v3.tex:616](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L616)

### mc2: General-equilibrium disclosure “proposition” is a heuristic
- **Issue:** Proposition `\ref{prop:ge-disclosure}` uses an approximate derivative and the footnote says it is only conceptual.
- **Suggestion:** Relabel it as a discussion paragraph or give a real theorem with conditions and proof.
- **Location:** [draft_v3.tex:810](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L810), [draft_v3.tex:812](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L812)

### mc3: Minority welfare is too narrowly labeled
- **Issue:** Calling takeover premia the “natural welfare object” ignores minority gains from improved standalone value when no bid occurs.
- **Suggestion:** Rename the object to “minority takeover rents” or broaden minority welfare to include continuation payoffs.
- **Location:** [draft_v3.tex:75](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L75), [draft_v3.tex:545](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L545), [draft_v3.tex:748](/home/austinli/Dropbox/Projects/Blockholder/directory/draft_v3.tex#L748)

## Referee Objections

### RO1: Why does disclosure reveal activism with certainty?
**Why it matters:** If `D=1` does not pin down `a=1`, the whole disclosed branch changes.
**How to address it:** Either impose a global dominance condition eliminating passive accumulation, or carry `QA` explicitly through the posterior system.

### RO2: Is the hump a theorem or just a calibration artifact?
**Why it matters:** The main contribution is weaker if the hump can disappear under nearby parameter values.
**How to address it:** State the result as calibrated unless you can prove sufficient conditions for an interior maximum.

### RO3: Is this really a price-feedback model?
**Why it matters:** The literature positioning depends on that claim.
**How to address it:** Either put actual prices back into bidder entry or revise the framing toward public-signal inference.

### RO4: Why should activism be increasing in the signal about firm value?
**Why it matters:** The current ordering conflicts with the paper’s underperformance motivation.
**How to address it:** Reinterpret the signal, or modify the cost technology so the action ordering tracks slack rather than quality.

### RO5: Are the welfare conclusions meaningful given the current accounting?
**Why it matters:** Policy recommendations on disclosure and liquidity require coherent welfare measurement.
**How to address it:** Rebuild the welfare section with explicit shareholder masses, clear transfer accounting, and a precise benchmark.

## Summary Statistics

| Dimension | Rating (1-5) |
|-----------|-------------|
| Argument Structure | 3 |
| Identification | 2 |
| Econometrics / Formal Correctness | 2 |
| Literature Positioning | 3 |
| Writing | 4 |
| Presentation | 3 |
| **Overall** | **2.8** |
