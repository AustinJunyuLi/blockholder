# Backup Slides Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add 7 new theory-focused backup slides to `pres/presentation.tex` and wire bidirectional hyperlinks from relevant main slides.

**Architecture:** All edits are in a single file (`pres/presentation.tex`). New backup frames are inserted at specific line ranges within the existing backup section. Main slides get additional `\backuplink` commands. No new packages, macros, or files needed.

**Tech Stack:** LaTeX/Beamer, XeLaTeX compiler, existing UCL theme

---

### Task 1: Add 3 new Mathematical Foundations backup slides (after Backup 5, before Sensitivity divider)

**Files:**
- Modify: `pres/presentation.tex` — insert after line 826 (end of Backup 5 frame), before line 828 (Sensitivity category divider)

**Step 1: Insert Backup 6b — Decomposition proof**

Insert immediately after `\end{frame}` of Backup 5 (line 826), before the Sensitivity category divider comment (line 828):

```latex
% ── BACKUP 6b: Decomposition derivation ────────────────────────────────
\begin{frame}{How do you derive the $\Delta^{\min}$ decomposition?}
\hypertarget{backup:decomposition_proof}{}
\small
\textbf{Goal:} Prove $\Delta^{\min} = m_0 \cdot \PP(\text{bid}) + (\tilde{m} - m_0)\,\E[\pi(X,D) \cdot \1\{\text{bid}\}]$.

\vspace{0.3em}

\textbf{Step 1: Definition.} $\Delta^{\min}(\kappa) = \E[m^R(a) \cdot \1\{\text{bid}\}]$ where $m^R(a) = m_0 + a(\tilde{m} - m_0)$.

\vspace{0.3em}

\textbf{Step 2: Conditional independence.} Given $(X,D)$, the bid indicator $\1\{\text{bid}\}$ depends on $(P(X,D), D, \xi)$. Since $\xi \perp (v,a)$, the bid indicator is conditionally independent of $(v,a)$:
\[
\E[m^R(a) \cdot \1\{\text{bid}\} \mid X,D] = \bar{m}(X,D) \cdot p(X,D)
\]

\vspace{0.3em}

\textbf{Step 3: Iterated expectations.} Taking $\E$ over $(X,D)$ and substituting $\bar{m} = m_0 + (\tilde{m} - m_0)\pi$:
\[
\Delta^{\min} = m_0 \cdot \PP(\text{bid}) + (\tilde{m} - m_0) \cdot \E[\pi(X,D) \cdot \1\{\text{bid}\}] \qquad \blacksquare
\]

\vspace{0.2em}
{\footnotesize\textbf{Key:} The conditional independence step requires $\xi$ (bidder shock) to be independent of $(v,a)$ --- the bid is determined by public information and idiosyncratic bidder heterogeneity alone.}

\returnlink{main:decomposition}{Slide 10b: Decomposition}
\end{frame}
```

**Step 2: Insert Backup 6c — Endpoint behavior**

Insert immediately after Backup 6b:

```latex
% ── BACKUP 6c: Endpoint behavior (Lemma 1) ─────────────────────────────
\begin{frame}{What are the endpoint limits of minority gains?}
\hypertarget{backup:endpoint_behavior}{}
\small
\begin{block}{Lemma 1 (Endpoint Behavior)}
\vspace{-0.2em}
{\small As $\kappa\uparrow 1$: $\Delta^{\text{act}}(\kappa)\to 0$, $\Delta^{\min}(\kappa)\to m_0\PP(\text{bid})$.\\
As $\kappa\downarrow 0$: $\Delta^{\text{act}}(\kappa) > 0$ but suppressed below interior optimum.}
\vspace{-0.2em}
\end{block}

\begin{columns}[T,onlytextwidth]
\column{0.48\textwidth}
\textbf{Right endpoint ($\kappa \uparrow 1$):}
\begin{itemize}\itemsep0.1em
  \item $\PP(z{=}0) \to 0$: order flow uninformative
  \item $\pi(X,0) \to$ unconditional prior
  \item Engagement return $< C(s)$ for all $s$
  \item Voice regions collapse: $\omega_Q + \omega_P \to 0$
\end{itemize}

\column{0.48\textwidth}
\textbf{Left endpoint ($\kappa \downarrow 0$):}
\begin{itemize}\itemsep0.1em
  \item $\PP(z{=}0) \to 1$: $X \to q$ a.s.
  \item Market perfectly deduces $q = 0$
  \item Engagement benefit bounded below $\Rightarrow$ $\omega_Q > 0$ persists
  \item But full informativeness depresses $p(X,0)$ via bid deterrence
\end{itemize}
\end{columns}

\vspace{0.2em}
{\footnotesize $\Rightarrow$ The global maximum of $\Delta^{\min}(\kappa)$ cannot be at either boundary.}

\returnlink{main:result}{Slide 10: Main Result}
\end{frame}
```

**Step 3: Insert Backup 6d — Nonmonotonicity proof**

Insert immediately after Backup 6c:

```latex
% ── BACKUP 6d: Nonmonotonicity proof (Prop 5) ──────────────────────────
\begin{frame}{How do you know the hump is strict?}
\hypertarget{backup:nonmonotonicity_proof}{}
\small
\textbf{Proof of Proposition 5 (Nonmonotonic Liquidity Effect):}

\vspace{0.3em}

\textbf{Step 1: Continuity.} $\Delta^{\min}(\kappa)$ is continuous on $[0,1]$ (normal probabilities, Bayesian posteriors, and pricing are all continuous in $\kappa$).

\vspace{0.3em}

\textbf{Step 2: Weierstrass.} Continuous on compact $\Rightarrow$ attains a global maximum $\kappa^{\dagger} = \arg\max_{\kappa \in [0,1]} \Delta^{\min}(\kappa)$.

\vspace{0.3em}

\textbf{Step 3: Interior maximizer.} By Lemma 1, neither endpoint achieves the maximum:
\[
\Delta^{\min}(\tilde{\kappa}) > \lim_{\kappa \downarrow 0} \Delta^{\min}(\kappa) \quad \text{and} \quad \lim_{\kappa \uparrow 1} \Delta^{\min}(\kappa) = m_0 \PP(\text{bid})
\]
$\Rightarrow$ $\kappa^{\dagger} \in (0,1)$: the hump is \textbf{strict} with an interior peak. $\blacksquare$

\vspace{0.3em}

{\footnotesize\textbf{Note on shape:} The Weierstrass argument guarantees at least one interior peak but does not rule out multiple local maxima (W-shape). The baseline calibration confirms a well-behaved single-peaked hump, demonstrating that the fundamental economic trade-off dominates.}

\returnlink{main:result}{Slide 10: Main Result}
\end{frame}
```

**Step 4: Compile and verify**

Run: `cd /home/austinli/Dropbox/Projects/Blockholder/directory/pres && xelatex presentation.tex`
Expected: Compiles with no errors; new backup slides appear after Backup 5

**Step 5: Commit**

```bash
git add pres/presentation.tex
git commit -m "feat(pres): add 3 Mathematical Foundations backup slides (6b-6d)

Add decomposition proof, endpoint behavior (Lemma 1), and
nonmonotonicity proof (Prop 5) backup slides."
```

---

### Task 2: Add 2 new Sensitivity & Comparative Statics backup slides (after Backup 7, before Backup 11)

**Files:**
- Modify: `pres/presentation.tex` — insert after the end of Backup 7 frame (line 859), before Backup 11 comment (line 861)

**Step 1: Insert Backup 8 — Bid probability monotonicity**

Insert after `\end{frame}` of Backup 7 (line 859), before the Backup 11 comment (line 861):

```latex
% ── BACKUP 8: Bid probability monotonicity ──────────────────────────────
\begin{frame}{Does engagement deter bids?}
\hypertarget{backup:bid_monotonicity}{}
\small
\textbf{Bid probability:} $p(X,D) = 1 - \Phi\!\left(\frac{\bar{m}(X,D) + K - \bar{S} + P}{\sigma_\xi}\right)$ where $T \equiv \frac{\bar{m} + K - \bar{S} + P}{\sigma_\xi}$.

\vspace{0.3em}

\textbf{Result 1: Higher prices deter bids.}
\[
\frac{\partial p}{\partial P} = -\frac{\phi(T)}{\sigma_\xi} < 0
\]
The supremum $\sup_P |\partial p / \partial P| = \phi(0)/\sigma_\xi$ is the binding term in Assumption A5.

\vspace{0.3em}

\textbf{Result 2: Higher inferred engagement deters bids} (when $\tilde{m} > m_0$).
\[
\frac{\partial p}{\partial \pi} = -\frac{(\tilde{m} - m_0)\,\phi(T)}{\sigma_\xi} < 0
\]

\vspace{0.2em}

{\footnotesize\textbf{Policy implication:} Disclosed activism ($\pi = 1$) deters bids more strongly than inferred activism ($\pi < 1$), since the full premium $\tilde{m}$ enters the bidder's cost.  This is why $p(X,1) < p(X,0)$ in the baseline table.}

\returnlink{main:engagement}{Slide 6: Engagement \& Bidder Entry}
\end{frame}
```

**Step 2: Insert Backup 9 — Takeover comparative statics**

Insert immediately after Backup 8:

```latex
% ── BACKUP 9: Takeover comparative statics ──────────────────────────────
\begin{frame}{How do synergies and entry costs affect bid incidence?}
\hypertarget{backup:takeover_comps}{}
\small
Fix any $(X,D)$. Define $T \equiv (\bar{m} + K - \bar{S} + P)/\sigma_\xi$, so $p = 1 - \Phi(T)$.

\vspace{0.3em}

\textbf{Result (a): Higher synergies increase bids.}
\[
\frac{\partial p}{\partial \bar{S}} = \frac{\phi(T)}{\sigma_\xi} > 0 \qquad (\text{since } \partial T / \partial \bar{S} = -1/\sigma_\xi)
\]

\vspace{0.3em}

\textbf{Result (b): Higher entry costs reduce bids.}
\[
\frac{\partial p}{\partial K} = -\frac{\phi(T)}{\sigma_\xi} < 0 \qquad (\text{since } \partial T / \partial K = +1/\sigma_\xi)
\]

\vspace{0.3em}

{\footnotesize\textbf{Unified structure:} All three derivatives ($\bar{S}$, $K$, $P$) share the same $\phi(T)/\sigma_\xi$ factor. Differences are purely in sign, driven by how each parameter enters the bidder's standardized threshold $T$.}

\vspace{0.2em}

{\footnotesize\textbf{Note:} These are partial equilibrium results (equilibrium prices held fixed). In GE, higher $\bar{S}$ also raises equilibrium prices, partially offsetting the direct effect through the price-entry feedback loop.}

\returnlink{main:engagement}{Slide 6: Engagement \& Bidder Entry}
\end{frame}
```

**Step 3: Compile and verify**

Run: `cd /home/austinli/Dropbox/Projects/Blockholder/directory/pres && xelatex presentation.tex`
Expected: Compiles with no errors; Backups 8-9 appear between Backup 7 and Backup 11

**Step 4: Commit**

```bash
git add pres/presentation.tex
git commit -m "feat(pres): add 2 Sensitivity backup slides (8-9)

Add bid monotonicity and takeover comparative statics backups,
filling the gap between Backup 7 and Backup 11."
```

---

### Task 3: Add 2 new Disclosure Extensions backup slides

**Files:**
- Modify: `pres/presentation.tex`
  - Backup 10: insert after Backup 9 (just added) and before Backup 11 (cutoffs vs kappa)
  - Backup 12b: insert after Backup 14 (GE disclosure), before the Welfare category divider

**Step 1: Insert Backup 10 — Disclosed-branch invariance**

Insert after Backup 9's `\end{frame}`, before the Backup 11 comment:

```latex
% ── BACKUP 10: Disclosed-branch invariance ──────────────────────────────
\begin{frame}{Why are prices flat on the disclosed branch?}
\hypertarget{backup:disclosed_invariance}{}
\small
\textbf{Claim:} $P^*(x,1) = P^*(x',1)$ and $p(x,1) = p(x',1)$ for all $x, x' \in \{0,1,2\}$.

\vspace{0.3em}

\textbf{Step 1: Identification.} $D = 1 \Leftrightarrow$ Public Voice: $a = 1$ a.s.\ and $X = 1 + z$ with $z \in \{-1, 0, 1\}$.

\vspace{0.3em}

\textbf{Step 2: Independence.} Since $z \perp (v, s, \xi)$, conditioning on $X = x$ given $D = 1$ only reveals $z = x - 1$ --- no information about $v$ beyond what $D = 1$ already implies:
\[
\PP(v \in B \mid X{=}x, D{=}1) = \PP(v \in B \mid D{=}1) \quad \forall\, x \in \{0,1,2\}
\]
$\Rightarrow$ $\pi(x,1) = 1$, $\E[v \mid x, 1] = \mu_P$ for all $x$.

\vspace{0.3em}

\textbf{Step 3: Fixed-point uniqueness.} Since $\hat{V}(x,1)$ and $\bar{m}(x,1) = \tilde{m}$ are constant, the pricing fixed point has the same RHS for all $x$. By A5, $P^*(x,1) = P^*(x',1)$. $\blacksquare$

\vspace{0.2em}

{\footnotesize\textbf{Consequence:} The disclosed component of $\Delta^{\text{act}}$ is $\kappa$-invariant --- this is the foundation of Proposition 6 (disclosure attenuation).}

\returnlink{main:prop2}{Slide 8: Bayesian Inference}
\end{frame}
```

**Step 2: Insert Backup 12b — PE vs GE disclosure**

Insert after the `\end{frame}` of Backup 14 (GE disclosure, line 980), before the Welfare category divider (line 982):

```latex
% ── BACKUP 12b: PE vs GE disclosure distinction ────────────────────────
\begin{frame}{How does partial vs.\ general equilibrium change the disclosure story?}
\hypertarget{backup:PE_vs_GE}{}
\small
\begin{columns}[T,onlytextwidth]
\column{0.48\textwidth}
\textbf{Proposition 6 (Partial Equilibrium):}
\begin{itemize}\itemsep0.1em
  \item \textbf{Fix} cutoffs $(k_1, k_0, k_D)$
  \item Vary $\kappa$ through inference only
  \item Disclosed component ($D{=}1$): $\kappa$-invariant (by Disclosed-Branch Invariance)
  \item Inferred component ($D{=}0$): weighted by $\PP(D{=}0) = 1 - \omega_P$
\end{itemize}
$\Rightarrow$ $|\partial\Delta^{\text{act}}/\partial\kappa|$ \textbf{decreases} as $\omega_P$ rises.

\column{0.48\textwidth}
\textbf{Proposition 7 (General Equilibrium):}
\begin{itemize}\itemsep0.1em
  \item \textbf{Allow} $k_D = k_D(\tau)$ to adjust
  \item Total derivative decomposes:
\end{itemize}
\vspace{-0.3em}
\[
\frac{d\Delta^{\text{act}}}{d\tau} \approx \underbrace{(+)}_{\text{transp.}} + \underbrace{(-)}_{\text{deter.}}
\]
\vspace{-0.3em}
\begin{itemize}\itemsep0.1em
  \item Stricter $\tau$ destroys Quiet Voice
  \item Blockholder may exit rather than disclose
\end{itemize}
\end{columns}

\vspace{0.3em}

{\footnotesize\textbf{Key distinction:} PE shows \emph{why} disclosure attenuates (mechanical: $D{=}1$ states are $\kappa$-free). GE shows \emph{whether} stricter disclosure helps (ambiguous: transparency vs.\ deterrence). Low $C_0$ + moderate $\kappa$: transparency dominates. High $C_0$: deterrence dominates.}

\returnlink{main:attenuation}{Slide 11: Disclosure Attenuation}
\end{frame}
```

**Step 3: Compile and verify**

Run: `cd /home/austinli/Dropbox/Projects/Blockholder/directory/pres && xelatex presentation.tex`
Expected: Compiles with no errors; Backup 10 appears before Backup 11; Backup 12b appears after Backup 14

**Step 4: Commit**

```bash
git add pres/presentation.tex
git commit -m "feat(pres): add 2 Disclosure backup slides (10, 12b)

Add disclosed-branch invariance proof and PE vs GE
disclosure distinction backup slides."
```

---

### Task 4: Add bidirectional backlinks from main slides to new backups

**Files:**
- Modify: `pres/presentation.tex` — add `\backuplink` commands to 7 main slides

**Step 1: Add backlinks to Slide 6 (Engagement & Bidder Entry)**

After the existing `\backuplink{backup:fixed_point}{Fixed-point derivation}` on line 391, add:
```latex
\backuplink{backup:bid_monotonicity}{Bid deterrence}
\backuplink{backup:takeover_comps}{Takeover comparative statics}
```

**Step 2: Add backlink to Slide 8 (Bayesian Inference)**

After the existing `\backuplink{backup:full_posteriors}{Full posterior formulas}` on line 453, add:
```latex
\backuplink{backup:disclosed_invariance}{Disclosed-branch invariance}
```

**Step 3: Add backlink to Slide 9 (Price Decomposition)**

After the existing `\backuplink{backup:fixed_point}{Pricing derivation}` on line 485, add:
```latex
\backuplink{backup:disclosed_invariance}{Disclosed-branch invariance}
```

**Step 4: Add backlinks to Slide 10 (Main Result)**

After the existing `\backuplink{backup:sensitivity}{Sensitivity analyses}` on line 519, add:
```latex
\backuplink{backup:endpoint_behavior}{Endpoint limits}
\backuplink{backup:nonmonotonicity_proof}{Nonmonotonicity proof}
```

**Step 5: Add backlink to Slide 10b (Decomposition)**

After the existing `\backuplink{backup:sensitivity}{Sensitivity analyses}` on line 552, add:
```latex
\backuplink{backup:decomposition_proof}{Decomposition proof}
```

**Step 6: Add backlink to Slide 11 (Disclosure Attenuation)**

After the existing `\backuplink{backup:noisy_rumor}{Noisy rumors}` on line 580, add:
```latex
\backuplink{backup:PE_vs_GE}{PE vs GE distinction}
```

**Step 7: Add backlink to Slide 12 (Policy Implications)**

After the existing `\backuplink{backup:welfare}{Welfare decomposition}` on line 618, add:
```latex
\backuplink{backup:PE_vs_GE}{PE vs GE distinction}
```

**Step 8: Compile and verify**

Run: `cd /home/austinli/Dropbox/Projects/Blockholder/directory/pres && xelatex presentation.tex`
Expected: Compiles with no errors; all new hyperlinks resolve (no "undefined reference" warnings)

**Step 9: Update header comment**

Change line 4 from:
```latex
% 14 core slides + 17 backup slides with bidirectional hyperlinks
```
to:
```latex
% 14 core slides + 27 backup slides with bidirectional hyperlinks
```

**Step 10: Commit**

```bash
git add pres/presentation.tex
git commit -m "feat(pres): wire bidirectional links for 7 new backup slides

Add backuplinks from Slides 6, 8, 9, 10, 10b, 11, 12 to new
backup targets. Update header comment to reflect 27 total backups."
```

---

### Task 5: Final verification

**Step 1: Full compile (2 passes for hyperlinks)**

Run:
```bash
cd /home/austinli/Dropbox/Projects/Blockholder/directory/pres && xelatex presentation.tex && biber presentation && xelatex presentation.tex
```
Expected: No errors, no undefined reference warnings

**Step 2: Verify slide count**

Run:
```bash
grep -c '\\begin{frame}' /home/austinli/Dropbox/Projects/Blockholder/directory/pres/presentation.tex
```
Expected: ~47 frames (14 core + 5 category dividers + 27 backup + 1 references = 47, though some may be `allowframebreaks`)

**Step 3: Verify all hypertargets resolve**

Run:
```bash
grep -o 'hypertarget{[^}]*}' /home/austinli/Dropbox/Projects/Blockholder/directory/pres/presentation.tex | sort
grep -o 'hyperlink{[^}]*}' /home/austinli/Dropbox/Projects/Blockholder/directory/pres/presentation.tex | sort
```
Expected: Every `hyperlink` target has a corresponding `hypertarget`

**Step 4: Visual spot-check**

Open `pres/presentation.pdf` and verify:
- New backups appear in correct category sections
- Backlinks on main slides are visible and clickable
- Return links on backup slides point to correct main slides
- Mathematical notation renders correctly

**Step 5: Commit final**

```bash
git add pres/presentation.tex
git commit -m "verify: full compile passes, all 27 backup slides with bidirectional links"
```
