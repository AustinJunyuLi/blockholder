# Independent External Audit — GPT Pro (2026-03-04)

This is the full text of an independent theory audit of draft_v3.tex conducted by GPT Pro.
Every issue identified below has been independently verified against the manuscript and numerical code.

## diagnosis/gptpro/pro_v1.md

According to a document from 2026-03-03, here is a **hard-nosed theory audit** of `draft_v3` focused on (i) mathematical rigor/derivations and (ii) whether the economic mechanism is internally coherent and not propped up by awkward design choices.

I’m going to be blunt where something is “prod-breaking”.

---

## Executive triage

### ✅ What is in good shape (math/structure)

* The **information structure** and **signal-truncation conditional means** are standard and look correctly derived.
* The **Bayesian posteriors** in **Proposition 2** (especially the nondisclosed branch with the new (p_0,p_1)) are correctly computed given the discrete support. In particular the formulas for (\pi(1,0),\pi(-1,0),\pi(0,0)) match the underlying mixture logic. 
* The **feed-forward pricing** step (post-disclosure price equals discounted expected terminal payoff, and pre-disclosure price is the iterated expectation over disclosure states) is algebraically consistent and avoids the old premium-on-premium recursion.

### 🚨 Two “must-fix” theory failures

1. **Lemma 2 right-endpoint argument ((\kappa\uparrow 1)) is mathematically inconsistent with your own posterior formulas** and with the bounded support of (z).

   * Lemma 2’s proof claims order flow becomes “completely uninformative” and that (\pi(X,0)) converges to the unconditional prior across all nondisclosed states. 
   * But **Proposition 2 explicitly implies (\pi(1,0)=\frac{\omega_Q}{\omega_H+\omega_Q}), which is independent of (\kappa)** (and Appendix B.8 reiterates (\partial \pi(1,0)/\partial\kappa=0)). 
     These cannot both be true. This is not cosmetic: it undermines the “high-liquidity collapse” endpoint and anything that leans on it.

2. **Proposition 5 (nonmonotonicity / hump) proof is not rigorous as written because it relies on Lemma 2’s endpoint collapse and then applies Jensen in a way that does not hold cleanly with endogenous cutoffs.** 

Those two items are the core of your “hump” narrative; they have to be repaired.

---

## Mathematical rigor review (by component)

### 1) Liquidity/noise specification and what it actually implies

You define noise as
[
z\in{-1,0,1},\quad \mathbb P(z=0)=1-\tfrac{2}{3}\kappa,\quad \mathbb P(z=\pm 1)=\tfrac{\kappa}{3}.
]


This fixes the earlier parity bug (you now keep mass on (z=0) for (\kappa\in(0,1))), and it’s coherent.

**But**: because the support of (z) is bounded and discrete, **order flow cannot become “completely uninformative” in the limit**. Even at (\kappa\to 1) you still have:

* extreme (X\in{-2,2}) perfectly revealing (q),
* and **within (D=0)**, the event (X=1) rules out exit mechanically (since exit is (q=-1) and (z\le 1)). That is exactly why (\pi(1,0)) is (\kappa)-invariant. 

So the model’s own algebra says: **high (\kappa) weakens inference in some states, but not all, and not “completely.”**

This is the first place where the text/proofs overclaim relative to the discrete structure.

---

### 2) Posterior engagement probabilities (\pi(X,D))

**Proposition 2 is right** given the strategy partition and the new (p_0,p_1). 

Two important implications (that your later endpoint narrative forgets):

* (\pi(1,0)=\frac{\omega_Q}{\omega_H+\omega_Q}) does **not** depend on (\kappa). 
* (\pi(-1,0)) is increasing in (\kappa), (\pi(0,0)) is decreasing in (\kappa) (your Appendix B.8 shows the signs correctly). 

That’s fine.

But it means any “(\kappa\to 1) makes all posteriors converge to the unconditional prior” statement is **false** unless you also impose a nontrivial equilibrium restriction like (\omega_E\to 0) (exit vanishes) — which you do not prove and which is not generally implied. This is the direct contradiction with Lemma 2’s proof. 

---

### 3) Conditional expectations (E[v\mid X,D]) and (\hat V(X,D))

The conditional mean formulas (mixing (\mu_E,\mu_H,\mu_Q) with the correct Bayes weights depending on (p_0,p_1)) are standard and appear correctly set up. The most delicate case is nondisclosed (X=-1) and (X=0), where you mix (q=0) and (q=-1) contributions using (p_0,p_1); your expressions match the mixture structure.  (same structure as the displayed formulas; your v3 analog is consistent with this block)

I did not find an algebraic inconsistency there.

---

### 4) Bidder entry/bid probability monotonicity

You define the bidder’s bid probability as
[
p(X,D)=\lambda_B(1-\Lambda(T(X,D)))
]
with (T) increasing in inferred engagement under net deterrence; and you show (\partial p/\partial \pi<0) under Assumption (A5).

That derivative and sign logic are correct **conditional on your modelling choice**: bidder uses ((X,D)) and the market’s (\pi(X,D)), and you bundle engagement effects into (\hat V) and (\bar m) in the way you specify.

**However**, note the paper text explicitly says the bidder’s payout is “tied to the market’s Bayesian expectation” because she doesn’t observe (a) when (D=0). 
That’s okay as a reduced form, but you should be careful: it’s not “the market” per se—it’s “the bidder’s belief, which coincides with the market’s under common priors and shared information.” Otherwise a referee will push on why bidders outsource beliefs to market makers.

---

### 5) Pricing: (P_{\text{post}}(X,D)) and (P_{\text{trade}}(X))

The feed-forward pricing identities are coherent:

* post-disclosure: (P_{\text{post}}(X,D)=\delta E[Y\mid X,D]) and your simplification to (\hat V(X,D)+p(X,D)\bar m(X,D)) is correct under your payoff definition.
* pre-disclosure: (P_{\text{trade}}(X)=\sum_d \mathbb P(D=d\mid X),P_{\text{post}}(X,d)), iterated expectations.

I don’t see a math error here.

**But** there is a conceptual consistency issue with how you interpret takeover premia (next section).

---

### 6) Takeover premium definition and decomposition

You define the realized premium wedge as (m_R(a)=m_0+a(\tilde m-m_0)). 

And you define minority takeover gains as
[
\Delta_{\min}(\kappa)=\mathbb E[m_R(a)\mathbf 1{\text{bid}}],
]
then decompose it into baseline plus activism-driven component. 

Two issues:

**(i) Minor math/presentation bug:** Appendix B.11 begins “By definition (\Delta_{\min}(\kappa)=\mathbb E[\bar m(X,D)\mathbf 1{\text{bid}}])” but that is **not** “by definition” if the definition is (m_R(a)). It’s true only after an iterated expectations step using (\mathbb E[m_R(a)\mid X,D]=\bar m(X,D)), plus the fact the bid event is conditionally independent of (a) given ((X,D)) in your setup. This is fixable wording, but you should fix it because it will trip readers.

**(ii) Bigger conceptual inconsistency:** in the engagement technology section you still say

> “I interpret (m_0) and (m_1) as per-share takeover premia above the market price (so the consummated offer satisfies (b=P+m)).” 

But in the bidder entry section you now say the bidder anchors the offer to (\hat V(X,D)) plus inferred premium wedge. 

That’s not just semantics:

* If (b=\hat V+m), then (m) is a premium over a **fundamental benchmark**.
* If (b=P+m), then (m) is premium over the **trading price**, which already includes takeover probability and would generally create a feedback/fixed-point.

You moved the model to the first structure (good for tractability), but the text still explains it as the second (premium over price). This needs to be made consistent.

---

## The biggest failure: Lemma 2 and the (\kappa\uparrow 1) endpoint

### What Lemma 2 currently claims

Lemma 2 asserts that as (\kappa\uparrow 1):

* the activism-driven component (\Delta_{\text{act}}(\kappa)\to 0),
* and (\Delta_{\min}(\kappa)\to m_0\mathbb P(\text{bid})). 

And the proof says:

* order flow becomes completely uninformative about (q),
* (\pi(X,0)) converges to the unconditional prior across all nondisclosed states,
* prices flatten across all (X),
* voice collapses ((\omega_Q+\omega_P\to 0)). 

### Why that is not correct under your own equilibrium objects

1. **Direct contradiction with Proposition 2:**
   (\pi(1,0)=\frac{\omega_Q}{\omega_H+\omega_Q}) does not depend on (\kappa). 
   So it cannot converge to an unconditional prior that depends on (\omega_E) unless (\omega_E\to 0), which you do not prove.

2. **The “completely uninformative” claim is incompatible with bounded support**
   With (z\in{-1,0,1}) and (q\in{-1,0,+1}), even at (\kappa\to 1) extreme order flows remain revealing (e.g., (X=2\Rightarrow q=+1)). So neither “completely uninformative” nor “prices flatten across all (X)” follows mechanically.

3. **Even if inference weakened, the “voice regions collapse” conclusion needs an actual argument that cutoffs diverge**
   Since (C(s)\to 0) as (s\to\infty) by your exponential specification, to get (\omega_Q+\omega_P\to 0) you need the *gross* benefit of engagement to go to 0 so that the engagement cutoff goes to (+\infty). Lemma 2 doesn’t establish that; it asserts collapse via “no rents,” which is not a valid step (and, in standard microstructure logic, more noise typically increases informed trading rents rather than kills them).

### Consequence

* **Lemma 2 is not salvageable by minor editing.** Either the endpoint claim changes, or the liquidity/noise structure changes.

---

## Proposition 5 nonmonotonicity proof: also not rigorous as written

Proposition 5 claims an interior maximizer of (\Delta_{\min}(\kappa)), using:

* Lemma 2 to pin down the right endpoint,
* then a Jensen/concavity argument to make (\kappa\downarrow 0) relatively low. 

Even setting aside Lemma 2, the Jensen step is not tight because:

* the distribution of (\pi(X,D)) is endogenous (cutoffs (\Rightarrow) (\omega)’s (\Rightarrow) (\pi)’s),
* so you can’t cleanly treat changes in (\kappa) as a mean-preserving spread in (\pi) holding the mean fixed.

Right now it reads as a heuristic sketch; it won’t survive a hostile referee.

---

## Economic mechanism audit (are the modeling choices defensible?)

### 1) Bidder observes ((X,D)) directly

You explicitly changed the bidder’s info set to ((X,D)) to “avoid any reliance on price injectivity.” 

This is defensible *if you motivate it properly* (e.g., bidder can observe trading/volume + filings, or can condition on a sufficient statistic that is effectively (X)). Otherwise, a referee will say “bidders observe price, not raw order flow.”

There is a legit precedent in feedback models (Edmans et al.) for letting the real-side actor observe order flow for tractability, but you should cite/justify explicitly (your draft already nods to this style). 

### 2) Premium definition inconsistency

As noted, you still say (b=P+m) (premium over market price). 
But the mechanism now actually uses (b=\hat V+m). 

This mismatch will confuse (and invites “double counting” accusations even though you fixed the recursion). You should pick one interpretation and make *all* text consistent.

My recommendation if you want to keep feed-forward pricing:

* redefine (m_0,m_1) as **control/bargaining premia over estimated standalone value**, not “premium over the market price.”

### 3) Net deterrence assumption (A5)

You impose net deterrence so that higher inferred engagement reduces bid probability (derivative negative).

That’s internally consistent, but it’s economically strong: empirically activism can *increase* takeover likelihood in many samples. If your headline prediction is nonmonotonic minority gains, you should at least:

* acknowledge the alternative case ((\Delta S) big()) where activism **facilitates** bids,
* and explain whether the hump is unique to deterrence or whether you get a different shape.

Right now the model hard-codes the sign.

### 4) “Liquidity kills rents” intuition is opposite standard microstructure

Given your own definition “higher (\kappa) = more noise imbalance = weaker inference”, standard Kyle logic says: more noise typically **increases** informed trading rents (better camouflage), not eliminates them. Your Lemma 2 right endpoint narrative depends on the opposite idea (“stripped of ability to extract rents…”). 

So beyond the math contradiction, the economics as written is not convincing.

---

## Concrete fix list (in priority order)

### P0 — Fix Lemma 2 / right endpoint and anything that depends on it

You have two viable routes:

**Route A (minimal structural change): keep discrete (z), but change the claim.**

* Do **not** claim order flow becomes “completely uninformative” or that (\pi(X,0)) converges to a single prior across all nondisclosed states. That’s false given (\pi(1,0)). 
* Re-derive the correct (\kappa\uparrow 1) limiting posteriors: at (\kappa=1), (p_0=p_1=1/3), so (\pi(-1,0)) and (\pi(0,0)) collapse to the same expression, but (\pi(1,0)) generally does not. 
* Then restate Lemma 2 as a weaker endpoint statement (e.g., certain posteriors compress; bid probability effects attenuate) **without** asserting (\Delta_{\text{act}}\to 0) unless you can actually prove cutoffs diverge.

**Route B (structural but “clean”): change the noise process so an uninformative limit exists.**
If you *need* a theorem that as liquidity rises inference dies, you need noise with increasing support/variance, not bounded ({-1,0,1}). E.g.:

* (z\sim \mathcal N(0,\sigma_z^2(\kappa))) with (\sigma_z(\kappa)\to\infty) as (\kappa\uparrow 1), or
* a discrete (z) with support expanding in (\kappa).

Then you can legitimately say the likelihood ratio between (q=0) and (q=-1) tends to 1 and posteriors converge to priors. With current bounded support, you cannot.

Either way: **Proposition 5 proof must be rewritten** after you settle the endpoint.

---

### P1 — Tighten Lemma 1 (eliminate “Quiet Accumulation” (QA)) so it’s actually watertight

Right now the lemma statement is intuitive (“if you buy an extra share, you should also engage”) but the proof sketch needs to pin down that **for any type that would ever choose (q=+1), engagement is strictly optimal**. 

If you want a clean solution, add a simple assumption:

* For all (s\ge k_D), (U(+1,1\mid s)>U(+1,0\mid s)).
  Or prove (k_D) must lie above the point where (PV-QA) flips sign.

Otherwise a referee can argue there may exist a “buy-but-don’t-engage” region, breaking (\pi(X,1)=1).

---

### P2 — Make the takeover premium interpretation consistent everywhere

* Remove/replace the sentence interpreting (m_0,m_1) as “premia above the market price (b=P+m)” unless you reintroduce the price-linked offer and deal with its fixed-point.
* Align language with the new mechanism: offer anchored to (\hat V(X,D)) plus a bargaining/control wedge. 

---

### P3 — Promote the hidden (\lambda_B<1/2) restriction into an explicit assumption (or relax it properly)

Your single-crossing / monotone cutoff ordering between Quiet Voice and Public Voice uses that (2p(X,1)<1) and notes this holds if (\lambda_B<0.5). 

Right now it’s a “calibration fact” inside the proof. In theory land, this should be an assumption or replaced with a more general sufficient condition.

---

### P4 — Fix minor “rigor leaks” (won’t kill you, but looks sloppy)

* In B.11 don’t say “by definition” when using iterated expectations to swap (m_R) for (\bar m). 
* If you’re going to rely on (\mathbb P(D=d\mid X)) in (P_{\text{trade}}(X)), either give explicit formulas (at least for (X\in{0,1}) where both (D) possible) or add a short appendix line.

---

## Bottom line

* The core **microstructure + disclosure + engagement** scaffold is much cleaner than v2 (feed-forward pricing and bidder observing ((X,D)) are meaningful improvements).
* But the current **high-liquidity endpoint** and thus the claimed **theorem-level hump** are **not correct as written** (direct contradiction between Lemma 2’s proof and Proposition 2/Appendix B.8). 
* If you fix only one thing before moving forward: **repair Lemma 2 + rewrite Proposition 5 proof**. Everything else is second-order compared to that.

If you want, I can propose a **drop-in replacement for Lemma 2** under your *current* discrete (z) that is true (weaker, but correct), and then suggest how to restate Proposition 5 as a **“numerically verified + analytically supported”** result rather than a fully closed-form theorem—*without* another full overhaul.

