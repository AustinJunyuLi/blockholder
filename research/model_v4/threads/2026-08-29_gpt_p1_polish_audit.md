# Audit of the GPT Pro P1 polish pass — 2026-08-29

**Date.** 2026-08-29.

**Auditor.** Fresh Opus agent (wrote none of the proof, the prompt, or the response). I wrote none
of the material under audit — not `proofs/P1_proof.md`, not `MODEL_CARD.md`, not
`threads/gpt_p1_polish_prompt_2026-08-29.md`, not the response. My only write is this file. **I ran
no git command.**

**Card stamp verified before starting.** `MODEL_CARD.md` line 3 reads *"Version stamp: 2026-08-28 ·
re-review audit repairs (P1-row A5 clause + §5 A5 evidence note + A($\tau$) lead + §4.4 O-1
parenthetical) · commit `59c0dfc`."* This is the controlling stamp and the stamp the response
declares it was built against (`2026-08-29_gpt_p1_polish.md:12`). **Match.**

**Response audited.** `threads/2026-08-29_gpt_p1_polish.md` (893 lines, filed verbatim at commit
`50d23e8`). Nineteen findings F1–F19 in four declared classes — six WRONG (F1–F6), five GAP
(F7–F11), seven POLISH (F12–F18), one UNCLEAR (F19) — a per-step verdict table at lines 819–869, an
OVERALL JUDGMENT at 870–872, a NOTATION DELTA at 874–886 and a NOT CLAIMED at 888–893.

**Primary records consulted.** `proofs/P1_proof.md` (all 1,489 lines: CLAIM, h.1–h.17, Steps 1–20,
WHERE IT FAILS 1–7, LABEL CLAIMED, NOTATION DELTA, NOT CLAIMED 1–15, the four repair tables);
`MODEL_CARD.md` §2 (timing), §3 (equilibrium notion), §4.1–§4.6 (symbol table), §5 (A1–A8 blocks
with the A3/A5/A6 evidence notes), §6 (the P1 row at `:551`), §8 (standing rules);
`threads/gpt_p1_polish_prompt_2026-08-29.md` §1 (the ask, the four finding classes, the three scope
fences); `threads/2026-08-28_gpt_rereview_audit.md` (format precedent).

**HEADLINE.** **No label moves in this audit, and none is made here.** Sixteen findings are upheld
(three of them with scope), two are narrowed, none is rejected. **One upheld WRONG-class finding —
F5 — survives that the drafted repairs cannot close at wording grade.** Under the terms the lane
sets, the P1 row/label question therefore goes to Austin. **No `LABEL_LEDGER.md` entry results from
this audit**; this file drafts text, it does not edit, and nothing below lands until the
orchestrator applies it.

**Rules in force.** An external review may **demote, never promote**. Every text GPT proposed and
every text I draft below is **CONJECTURE-grade edit text** until the lane's own gate runs over the
proof carrying it. No repair lands before this audit; nothing moves until the orchestrator applies
it. Landed record lines (the P1-R repair tables, NOT CLAIMED items) are **superseded with a dated
amendment, never silently rewritten**. Repairs number from **P1-R36** — `P1-R35` is the file's
current ceiling (`proofs/P1_proof.md:1480`), verified by enumeration.

**Class vocabulary, and one declared extension.** The lane's three classes are **WRONG-class** (the
proof text is actually wrong), **MISCITED** (GPT misquotes or misattributes) and **UNCHECKED** (GPT
flags without demonstrating). Two of GPT's findings fit none of the three, so I add two classes and
say so here rather than forcing them: **STALE** (the text was true at the stamp the file was written
against and is superseded at the controlling stamp) and **POLISH-class** (the text is sound and
rough; no defect). WRONG-class here covers a false statement, an unsupported load-bearing inference,
**and** a citation that does not support what it is cited for. Repair grade is a **separate axis**
from finding class and is stated separately for every repair.

**Quote accuracy, recorded once.** Every quotation in the response resolves against
`proofs/P1_proof.md` at the text GPT anchors it to. **No finding in this pass is MISCITED by
misquotation** — a difference from the 2026-08-28 re-review, where three of fourteen were. Where I
depart from GPT it is on consequence or on repair mechanics, never on what the proof says.

---

## Scorecard

Nineteen rulings. **16 UPHELD (three of them with scope) · 2 NARROWED · 0 REJECTED.**

| # | GPT's finding, in one line | GPT class | Verdict | Lane class | Repair | Grade |
|---|---|---|---|---|---|---|
| F1 | Step 2's filing-stake display evaluates the stake at the crossing date | WRONG | **UPHELD** | WRONG-class | P1-R36 | wording |
| F2 | The flagged family can be empty, so "not finite" is not categorical | WRONG | **UPHELD** | WRONG-class | P1-R37 | wording |
| F3 | Step 9(b)'s limit is not plan-uniform when $\Lambda_k>0$ | WRONG | **UPHELD** | WRONG-class | P1-R38 | wording |
| F4 | Step 9(c)'s "fixed" reference belief uses endogenous $\Pr(a=1)$ | WRONG | **UPHELD** | WRONG-class | P1-R39 | wording |
| F5 | The finite corner code does not represent an empty action region on the Gaussian tails | WRONG | **UPHELD** | WRONG-class | **P1-R40-A / -B** | **SUBSTANCE** |
| F6 | Step 15 asserts cutoff continuity the file does not derive | WRONG | **UPHELD** | WRONG-class | P1-R41 | wording |
| F7 | The proof replaces the card's general ordered polytope by the full box | GAP | **NARROWED** | MISCITED (consequence) | P1-R42 | wording |
| F8 | Continuity of the inner root in $\pi$ is missing | GAP | **UPHELD** | WRONG-class | P1-R43 | **SUBSTANCE** (statement-preserving) |
| F9 | Step 9(b)'s price convergence omits $\pi_n$ | GAP | **UPHELD** | WRONG-class | P1-R44 | **SUBSTANCE** (statement-preserving) |
| F10 | Empty interior does not supply the strict sign pattern used next | GAP | **UPHELD** | WRONG-class (non-consumed condition) | P1-R45 | wording |
| F11 | The Kakutani remark asserts convex values and a closed graph | GAP | **UPHELD-WITH-SCOPE** | WRONG-class (non-load-bearing remark) | P1-R46 | wording |
| F12 | h.12 is stale against the current card | POLISH | **UPHELD-WITH-SCOPE** | STALE | P1-R47 | wording |
| F13 | Step 4's Gaussian-law citation points at h.1 | POLISH | **UPHELD** | WRONG-class (citation) | P1-R48 | wording |
| F14 | Step 5(b) retains an ambiguity the card has resolved | POLISH | **UPHELD-WITH-SCOPE** | STALE | P1-R49 | wording |
| F15 | Step 7(iii)'s uniqueness can be global instead of adjacent-root | POLISH | **UPHELD** | POLISH-class | P1-R50 | wording |
| F16 | The perturbation needs a valid starting index; $\varphi_s$ undeclared | POLISH | **UPHELD** | POLISH-class | P1-R51 | wording |
| F17 | Step 12 opens with repair history, not the mathematical issue | POLISH | **UPHELD** | POLISH-class | P1-R52 | wording |
| F18 | Step 20's threshold equivalence needs extended-real conventions | POLISH | **UPHELD** | POLISH-class | P1-R53 | wording |
| F19 | Step 14's four-action derivation cannot be checked from the paste | UNCLEAR | **NARROWED** | UNCHECKED | none | — |

---

## Finding F1 — Step 2's filing-stake measurability display. UPHELD. WRONG-class.

**What the proof says.** Step 2 defines the filing stake at `proofs/P1_proof.md:287`:

> $B_j^F(s)=B_j(s,f_j(s))$ and $Q_j^F(s)=b_j^*(s)-B_j^F(s)$

and then, at `:297-301`, discharges its measurability:

> and — this is the D1-R2 repair written out —
> $$B_j^F(s)\;=\;\sum_{d=0}^{H-T}\mathbf 1\{f_j(s)=d+T\}\cdot B_j(s,d)$$
> is a finite sum of products of Borel functions, hence Borel, and likewise $Q_j^F$.

**What GPT claims** (response `:27-35`). The indicator selects $d=f_j(s)-T=c_j(s)$ but the summand
returns $B_j(s,d)$, the stake at the **crossing** date, where the definition requires
$B_j(s,f_j(s))=B_j(s,d+T)$ — the stake at the **filing** date. Witness: $c_j=2$, $T=3$ returns
$B_j(s,2)$ for $B_j(s,5)$. Secondary: the display silently assigns $B_j^F=0$ where no filing lands.

**Verdict: UPHELD, WRONG-class.** The arithmetic is exact. On the summand indexed $d$, the indicator
$\mathbf 1\{f_j(s)=d+T\}$ fires precisely when $c_j(s)=d$, and the factor multiplied in is
$B_j(s,d)=B_j(s,c_j(s))$. Card §4.2's rows give $\partial_dB_j\ge0$ on Voice, so $B_j(s,c_j)\le
B_j(s,c_j+T)$ with the inequality strict on any plan that keeps accumulating inside the window —
which is the generic case, and is exactly what card §4.2's $B^F$ row ("$T'<T\Rightarrow
B^F(T')\le B^F(T)$ at fixed policies") records as varying with $T$. The display therefore computes
the wrong object. The step's **conclusion** — that $B_j^F$ and $Q_j^F$ are Borel — is untouched: the
corrected display is a finite sum of products of the same Borel functions.

The secondary point is correct and benign. Off $\{D_j=1\}$ every indicator vanishes and the sum
returns $0$, so the display extends $B_j^F$ by zero and $Q_j^F$ by $b_j^*$. Card §4.2 defines both
on the flagged set; Steps 6, 10, 11 and 12 read them only there. The extension is a convention that
should be named, not a defect.

### DRAFTED REPAIR — P1-R36 (Step 2, replacing `:297-301`). Grade: **WORDING-ONLY.**

> and — this is the D1-R2 repair written out — the filing objects are Borel through the finite
> decomposition
> $$\widetilde B_j^F(s)\;=\;\sum_{\ell=T}^{H}\mathbf 1\{f_j(s)=\ell\}\cdot B_j(s,\ell),
> \qquad \widetilde Q_j^F(s)\;=\;b_j^*(s)-\widetilde B_j^F(s),$$
> each a finite sum of products of Borel functions, hence Borel. On $\{D_j=1\}$ one has
> $f_j(s)\in\{T,\dots,H\}$ by h.9, so $\widetilde B_j^F(s)=B_j(s,f_j(s))=B_j^F(s)$ and
> $\widetilde Q_j^F(s)=Q_j^F(s)$ there. Off $\{D_j=1\}$ every indicator vanishes and the tildes are
> a conventional extension by $\widetilde B_j^F:=0$; card §4.2 defines $B_j^F$ and $Q_j^F$ on the
> flagged set and no step reads them elsewhere, so the extension is never consumed. Suppressing the
> tildes on the flagged set, $B_j^F$ and $Q_j^F$ are Borel there.
>
> *Corrected 2026-08-29 (**P1-R36**, polish-pass finding F1). The pre-repair display summed
> $\mathbf 1\{f_j(s)=d+T\}\cdot B_j(s,d)$ over $d=0,\dots,H-T$, whose surviving factor is
> $B_j(s,c_j(s))$ — the stake at the **crossing** date — where this step's own definition three
> lines above requires $B_j(s,f_j(s))$, the stake at the **filing** date; at $c_j=2$ and $T=3$ the
> old display returned $B_j(s,2)$ for $B_j(s,5)$, and card §4.2's $\partial_dB_j\ge0$ on Voice makes
> the two differ on any plan still accumulating inside the window. The index is now the filing date
> itself over its whole admissible range. The step's conclusion is unchanged.*

**Why the grade is wording.** The corrected display is a transcription of the step's own definition
at `:287`; the step's conclusion (Borel) is what it was; no hypothesis moves and no downstream step
reads the display rather than the definition.

---

## Finding F2 — the flagged family need not exist. UPHELD. WRONG-class.

**What the proof says.** The Step 3 heading, `proofs/P1_proof.md:306`:

> **Step 3 (the pooled public-history family is finite; the flagged family is not).**

and `:311-315`:

> By Step 2 the flagged tuple $\sigma_F:=(B^F,Q^F,a=1)$ — card §4.6's $\mathsf S_F$, the filing
> message $F$ augmented by the flagged order $Q^F$ — is Borel but takes values in
> $[0,\bar b]^2\times\{1\}$, a continuum

and the Step 6 opening, `:387-388`:

> By Step 3 the flagged information sets are indexed by the continuum
> $\sigma_F\in[0,\bar b]^2\times\{1\}$.

**What GPT claims** (response `:74-79`). A8 is not assumed for the existence half, so no plan need
flag — the proof's own WHERE IT FAILS 6 sets $\tau>\bar b$ — and then the flagged image is empty,
hence finite. A continuum **codomain** does not make the **image** a continuum. When the flagged set
is nonempty the intended conclusion is recoverable: a Voice plan's flagged signal set is an upper
ray, uncountable, and h.7 maps it injectively.

**Verdict: UPHELD, WRONG-class.** Three checks.

1. **The empty case is admissible.** The CLAIM (`:47-49`) says "A8 is used for that addendum and for
   nothing in the existence half", and h.8's *Used* line reads "Step 19 only" (`:130`). WHERE IT
   FAILS 6 (`:1072-1076`) realises it: "Set $\tau>\bar b$. No plan can cross, so $D\equiv0$,
   $\Omega(k^\star)=0$ … and Steps 6, 10 and 12 are vacuous."
2. **The heading is then false.** Empty is finite. The heading's contrast — pooled finite, flagged
   not — does not hold at every admissible parameter.
3. **GPT's positive half checks out.** $D_j(s;\tau,T)=\mathbf 1\{a_j=1\}\cdot\mathbf
   1\{B_j(s,H-T)\ge\tau\}$ (`:302`), and card §4.2 gives $\partial_sB_j\ge0$ on Voice (h.17-c), so
   $\{s:D_j(s)=1\}$ is an up-set of $\mathbb R$; a nonempty up-set of $\mathbb R$ contains a
   half-line and is uncountable; h.7 (A7-J) is injective on the flagged-**pair** set, so the image
   is uncountable. The dichotomy — empty or uncountable, never finite-and-nonempty — is right.

**No downstream step is disturbed.** Step 6 builds its family *on the image*, and (a)–(d) are
vacuous when the image is empty; Step 10 pins beliefs at image tuples; Step 12 quantifies over
flagged pairs. WHERE IT FAILS 6 already carries the vacuity. The defect is an over-categorical
heading and opening sentence, not a broken construction.

### DRAFTED REPAIR — P1-R37, three sites. Grade: **WORDING-ONLY.**

**(a) Step 3 heading (`:306`).**

> **Step 3 (the pooled public-history family is finite; the flagged family is empty or uncountable,
> and in neither case a finite nonempty indexed family).**

**(b) Step 3, replacing `:311-315`.**

> By Step 2 the flagged tuple $\sigma_F:=(B^F,Q^F,a=1)$ — card §4.6's $\mathsf S_F$, the filing
> message $F$ augmented by the flagged order $Q^F$ — is Borel with **codomain**
> $[0,\bar b]^2\times\{1\}$, a continuum: card §4.2 puts $B_j(s,d)\in[0,\bar b]$ with $s$ Gaussian
> and imposes monotonicity only, and no card row discretises the stake level. What the construction
> below runs on is the **image** of the flagged-pair map $(j,s)\mapsto(B_j^F(s),Q_j^F(s),1)$ on
> $\{(j,s):D_j(s;\tau,T)=1\}$, and that image obeys a dichotomy. **If no plan flags** — A8 is not
> assumed in the existence half, and WHERE IT FAILS 6's $\tau>\bar b$ realises this — the
> flagged-pair set and its image are empty, and Steps 6, 10 and 12 are vacuous, as WHERE IT FAILS 6
> already records. **If some plan flags at one signal**, that plan is Voice (h.4), and with
> $D_j(s)=\mathbf 1\{a_j=1\}\mathbf 1\{B_j(s,H-T)\ge\tau\}$ (h.9) and $\partial_sB_j\ge0$ on Voice
> (h.17-c) its flagged signal set is a nonempty up-set of $\mathbb R$, hence contains a half-line
> and is uncountable; h.7 maps it injectively, so the image is uncountable. **Either way the flagged
> layer cannot be handled as a finite nonempty indexed family**, and that is what forces the two
> layers of Part B to be treated differently. This is exactly the D1-R2 finding.
>
> *Corrected 2026-08-29 (**P1-R37**, polish-pass finding F2): the pre-repair heading and paragraph
> said the flagged family "is not" finite, categorically, and read a continuum codomain as a
> continuum index set. The empty case is admissible because A8 is not assumed for existence, and
> empty is finite. The step's use is unchanged — Step 6 constructs on the image, whatever the image
> is.*

**(c) Step 6 opening (`:387-388`).**

> Work on the image of the flagged-pair map (Step 3). If that image is empty, parts (a)–(d) below
> are vacuous and no flagged price is constructed or needed. Otherwise Step 3 makes it uncountable,
> its elements written $\sigma_F\in[0,\bar b]^2\times\{1\}$, and the construction applies.

**Why the grade is wording.** No step consumes nonemptiness or uncountability of the flagged image;
Step 6 is a construction on the image and is vacuous when the image is empty; the file's own WHERE
IT FAILS 6 already states that vacuity. The scoping corrects a claim, adds no hypothesis and changes
no step conclusion.

---

## Finding F3 — Step 9(b)'s limit characterisation. UPHELD. WRONG-class.

This is the finding the intake flagged for a discriminating check. Per the task, the text is quoted
exactly wherever the ruling rests on it, because a second agent is adjudicating the same lines for a
different purpose.

**What the proof says — the attacked clause, `proofs/P1_proof.md:514-518`, verbatim:**

> A ratio of polynomials in $1/n$ with a denominator that is nonzero
> for all large $n$ converges as $n\to\infty$, **pointwise in $(j,s)$**, and the limit is the
> plan-uniform-weighted joint law restricted to the history. This is where h.2's
> finiteness pays: with a continuum of pooled histories the limit would need a separate argument.

**The case split that follows, `:526-540`, verbatim:**

> **The envelope needs a case split on the denominator $Z_n$, and
> here it is (retry finding 4):** write $Z_n=(1-t_n)\Lambda_k+(t_n/J)\Lambda_u$ for
> the denominator — the display above with $w_n$ expanded — where
> $\Lambda_k=\int L_{j_k(s')}(\mathcal H_d^P\mid s')\varphi_s(s')\,\mathrm ds'$ is the unperturbed
> aggregate, $\Lambda_u=\sum_{j'}\int L_{j'}(\mathcal H_d^P\mid s')\varphi_s(s')\,\mathrm ds'$ the
> plan-uniform one, and $t_n=J/n$ the perturbation mass. *If $\Lambda_k>0$* — the history is on path under
> $k$ — then $Z_n\ge\Lambda_k/2$ for all large $n$, and $2\lvert\mu_v+\beta(s-\mu_v)\rvert\varphi_s
> L_j/\Lambda_k$ is an integrable envelope by h.17-d's Gaussian tail and h.2's integrability clause, so
> dominated convergence applies. *If $\Lambda_k=0$* — the $k$-null case — the $(1-t_n)$ term
> vanishes $\Phi_s$-a.e. in numerator and denominator alike, so $\mu_n=L_j\varphi_s/\Lambda_u$ **exactly
> and $n$-free**, and there is nothing to pass to the limit. (Without the split the bare claim would be
> false as stated: $\mu_n\le\varphi_sL_j/Z_n$ with $Z_n\downarrow0$ is not a uniform envelope.) Either
> way $\hat v_n\to\hat v_\infty$ and, by Step 8's 1-Lipschitz bound, the prices converge
> with them. Hence the limiting belief **and the limiting price** exist at every reachable
> pooled history, on path and off, and on path the belief agrees with the Bayes posterior.

**The mixing weight, `:496`, verbatim:**

> $$w_n(j\mid s)=(1-t_n)\,\mathbf 1\{j=j_k(s)\}+\tfrac{t_n}{J},\qquad t_n:=\tfrac Jn\downarrow0,$$

**What GPT claims** (response `:119-121`): the characterisation "is false whenever $\Lambda_k>0$. At
an on-path history, the uniform tremble vanishes and the limiting posterior is the ordinary
posterior generated by the conjectured strategy $j_k$, not the posterior generated by uniform plan
weights. The later denominator case split implicitly recognizes the distinction, so the step
currently contains two incompatible descriptions of the same limit."

**Verdict: UPHELD, WRONG-class.**

**The evaluation.** From `:504-506`, $\mu_n(j,s)=w_n(j\mid s)L_j(\mathcal H_d^P\mid
s)\varphi_s(s)/Z_n$. As $n\to\infty$, $t_n=J/n\downarrow0$, so $w_n(j\mid s)\to\mathbf
1\{j=j_k(s)\}$ pointwise and $Z_n=(1-t_n)\Lambda_k+(t_n/J)\Lambda_u\to\Lambda_k$. Hence when
$\Lambda_k>0$,
$$\mu_\infty(j,s)=\frac{\mathbf 1\{j=j_k(s)\}\,L_j(\mathcal H_d^P\mid s)\,\varphi_s(s)}{\Lambda_k},$$
the Bayes posterior generated by $j_k$ — a law concentrated on the graph of $j_k$. The plan-uniform
law $L_j\varphi_s/\Lambda_u$ charges every $j\in\mathcal J$ at every $s$. The two coincide only in
the degenerate case $J=1$. So the clause at `:516-517` is false at every reachable history with
$\Lambda_k>0$.

**Is `:516-517` scoped by its context?** No. It sits at the close of the paragraph running from
`:507`, whose subject is the positivity of the denominator **at a reachable history** — a class that
by the step's own definition (`:483-492`) contains both $\Lambda_k>0$ and $\Lambda_k=0$ histories.
Nothing between `:509` and `:518` restricts it to the $k$-null case, and the case split that would
scope it does not begin until `:526`, eight lines later, introduced as an *envelope* matter ("The
envelope needs a case split on the denominator $Z_n$") rather than as a correction of the
characterisation. The clause is unconditional as printed. **This is exactly the conflation GPT
names**, and the step's own closing sentence at `:540` — "on path the belief agrees with the Bayes
posterior" — is the second, incompatible description.

**Two independent confirmations that the two-case reading is the lane's.** (i) Card §5's A6 evidence
note, `MODEL_CARD.md:273-275`: "Step 9(b) gives Bayes where $\Lambda_k(h) > 0$ but a $k$-free
plan-uniform posterior on the frontier, so the price system can be discontinuous exactly on
$\bigcup_h \partial\{k : \Lambda_k(h) > 0\}$." The card's landed record already attributes the
two-case reading to this step, and the A6 finding is *built on* the two cases being different laws.
(ii) Step 17(iii) (`:939-941`) assigns "Step 9 for pooled histories of positive probability under
$k^\star$" to card §3(iii) *Bayes-consistent on-path beliefs* — which is true only under the
$\Lambda_k>0$ branch giving Bayes. Under the printed clause at `:516-517`, §3(iii) would fail.

**Does the case split below already carry both cases?** Partly, and that is what fixes the repair
grade. The $\Lambda_k=0$ branch **displays** its limit verbatim at `:535` ($\mu_n=L_j\varphi_s/
\Lambda_u$, exactly and $n$-free). The $\Lambda_k>0$ branch supplies an envelope and invokes
dominated convergence but **does not display** $\mu_\infty$; the only place the limit is
characterised is the false clause. So the repair is: delete the false characterisation, and display
the $\Lambda_k>0$ limit where the split already handles that case.

### DRAFTED REPAIR — P1-R38, two sites in Step 9(b). Grade: **WORDING-ONLY.**

**(a) Replacing `:514-518`.**

> A ratio of polynomials in $1/n$ with a denominator that is nonzero for all large $n$ converges as
> $n\to\infty$, **pointwise in $(j,s)$**. Write $\mu_\infty$ for that limit. **Which law it is
> depends on the same denominator split the envelope below needs, and the two cases are not the same
> law**; both are displayed there. This is where h.2's finiteness pays: with a continuum of pooled
> histories the limit would need a separate argument.

**(b) Replacing the two case sentences at `:531-537`, leaving the surrounding text as printed.**

> *If $\Lambda_k>0$* — the history is on path under $k$ — then $Z_n\ge\Lambda_k/2$ for all large
> $n$, and $2\lvert\mu_v+\beta(s-\mu_v)\rvert\varphi_sL_j/\Lambda_k$ is an integrable envelope by
> h.17-d's Gaussian tail and h.2's integrability clause, so dominated convergence applies; and since
> $w_n(j\mid s)\to\mathbf 1\{j=j_k(s)\}$ pointwise and $Z_n\to\Lambda_k$,
> $$\mu_\infty(j,s)=\frac{\mathbf 1\{j=j_k(s)\}\,L_j(\mathcal H_d^P\mid s)\,\varphi_s(s)}{\Lambda_k},$$
> **the ordinary Bayes posterior generated by the conjectured map $j_k$** — the uniform tremble
> washes out and the limit is *not* the plan-uniform law. *If $\Lambda_k=0$* — the $k$-null case —
> the $(1-t_n)$ term vanishes $\Phi_s$-a.e. in numerator and denominator alike, so
> $$\mu_n(j,s)=\mu_\infty(j,s)=\frac{L_j(\mathcal H_d^P\mid s)\,\varphi_s(s)}{\Lambda_u}$$
> **exactly and $n$-free** — the plan-uniform posterior restricted to the history — and there is
> nothing to pass to the limit. (Without the split the bare claim would be false as stated:
> $\mu_n\le\varphi_sL_j/Z_n$ with $Z_n\downarrow0$ is not a uniform envelope.) In both cases the
> displayed density is a probability density at the history.
>
> *Corrected 2026-08-29 (**P1-R38**, polish-pass finding F3). The pre-repair text characterised the
> limit, unconditionally at every reachable history, as "the plan-uniform-weighted joint law
> restricted to the history". That is false whenever $\Lambda_k>0$, and it contradicted this step's
> own closing sentence that on path the belief agrees with the Bayes posterior. The two-case reading
> is the one card §5's A6 evidence note already attributes to this step and the one Step 17(iii)
> and 17(iv) consume.*

**Why the grade is wording — stated in the terms the orchestrator can overrule.** The $\Lambda_k=0$
display is **already in the step's own case split verbatim** (`:535`). The $\Lambda_k>0$ display is
the elementary evaluation of a limit the step **already proves exists** (`:514-515`) and that the
step's **own closing sentence already asserts is the Bayes posterior** (`:540`). Every downstream
consumer — Step 17(iii), Step 17(iv), and card §5's A6 evidence note — already reads the step the
corrected way. No hypothesis moves; no step conclusion changes; the corrected text proves neither
more nor less than the step's stated conclusions. **If the orchestrator judges that displaying
$\mu_\infty$ in the $\Lambda_k>0$ branch is new mathematical content rather than a corrected
description, P1-R38 reclassifies to SUBSTANCE (statement-preserving) and rides the same re-gate as
P1-R43 and P1-R44.** I record the alternative rather than resolve it, because the boundary is a
judgement the lane owns.

---

## Finding F4 — Step 9(c)'s reference belief. UPHELD. WRONG-class.

**What the proof says**, `proofs/P1_proof.md:560-565`:

> **Convention adopted
> here:** fix once and for all a **reference belief** $(\hat v_\circ,\pi_\circ)$ — for definiteness the
> prior pair $\bigl(\mu_v,\Pr(a=1)\bigr)$, and any other admissible pair does equally — and assign to
> every unreachable pooled history the **inner root at that belief**

**What GPT claims** (response `:171-180`): $\Pr(a=1)$ is not a fixed primitive; engagement is
attached to the selected plan, so under conjecture $k$ it is $\Pr(a_{j_k(s)}=1)$, varying with $k$;
the displayed choice therefore does not define a convention fixed once across the price systems used
to build $\mathcal T(k)$, and the proof itself acknowledges that the convention can move the
best-response cutoff.

**Verdict: UPHELD, WRONG-class.** Card §4.2's $a_j$ row attaches engagement to the plan
($a_j\in\{0,1\}$; $a_j=1$ for Voice, $0$ for Exit/Hold), and the model has **no prior over plans** —
the blockholder chooses one at date 0 (card §2 item 1). So the unconditional $\Pr(a=1)$ is not
defined at all without a strategy, and once a strategy is supplied it is $\Pr(a_{j_k(s)}=1)$, a
functional of $k$. $\mu_v$ is card §4.1's prior mean and is a genuine primitive; its partner is not.
The pair as instantiated is not $k$-independent, so "fixed once and for all" is false of it.

**Why it matters, in the file's own words.** Step 9(c) at `:576-581`: "The choice is not innocuous in
one narrow respect and the file does not pretend otherwise: it can change $U_j(s;k)$ on a
$\Phi_s$-null set of signals, hence can move $\mathcal T_i(k)$". And the card's P1 row
(`MODEL_CARD.md:551`) requires "**one** full-support perturbation family over **plans — fixed once
and used to define the price system at every $k\in\Theta$, not only at $k^\star$**". A convention
computed from the conjectured plan distribution is exactly what that clause is written against.

**What survives.** The substantive content of Step 9(c) — that a reference belief is fixed, that the
price at unreachable histories is the inner root at it (so that every price in the object is an
inner fixed point, which is P1-R30's whole point), and NOT CLAIMED 13's rider that the theorem is
about the object built from that convention — is untouched. Only the "for definiteness"
instantiation is wrong, and the step's own "any other admissible pair does equally" licenses the
swap.

### DRAFTED REPAIR — P1-R39, three sites. Grade: **WORDING-ONLY.**

**(a) Step 9(c), replacing the parenthetical at `:561-562`.**

> **Convention adopted here:** fix once and for all a **$k$-independent reference belief**
> $(\hat v_\circ,\pi_\circ)\in\mathbb R\times[0,1]$ — for definiteness $(\mu_v,1)$, card §4.1's
> prior mean of $v$ paired with certain engagement, and any other pair fixed independently of $k$
> does equally — and assign to every unreachable pooled history the **inner root at that belief**
>
> *Corrected 2026-08-29 (**P1-R39**, polish-pass finding F4). The pre-repair instantiation was
> $(\mu_v,\Pr(a=1))$. $\mu_v$ is a card §4.1 primitive; $\Pr(a=1)$ is not. Engagement is attached to
> the plan (card §4.2's $a_j$ row) and the model carries no prior over plans, so the unconditional
> engagement probability is undefined without a strategy and, once one is supplied, equals
> $\Pr(a_{j_k(s)}=1)$ — a functional of the conjecture. The convention has to be $k$-independent,
> both because this step's own rider records that the reference belief can move $\mathcal T_i(k)$
> through a $\Phi_s$-null signal set and because the card's P1 row requires one price system fixed
> once and used at every $k\in\Theta$. The scalar $1$ is not substantive; what is essential is that
> $\pi_\circ$ not be computed from the conjectured plan distribution.*

**(b) NOTATION DELTA, the $(\hat v_\circ,\pi_\circ)$ row (`:1233`).** Replace "for definiteness the
prior pair $(\mu_v,\Pr(a{=}1))$" with "for definiteness the $k$-independent pair $(\mu_v,1)$
(**P1-R39**, 2026-08-29)". The rest of the row stands.

**(c) The P1-R30 repair-table row (`:1474`) — dated annotation, NOT a rewrite.** Append:

> *Amended 2026-08-29 by **P1-R39** (polish-pass finding F4): the instantiation this row names,
> $(\mu_v,\Pr(a{=}1))$, is not $k$-independent — $\Pr(a=1)$ is a functional of the conjectured plan
> map — and is replaced by $(\mu_v,1)$. **The change of convention this row records — from
> $\mathbb E[Y]$ to the inner root at a fixed reference belief — stands unchanged**, together with
> its reason.*

**Why the grade is wording.** One instantiation is exchanged for another that the step's own text
already declares equivalent-in-kind; the convention's role, the inner-root property, the rider and
NOT CLAIMED 13 are all unchanged.

---

## Finding F5 — the finite corner convention on the Gaussian tails. UPHELD. WRONG-class. **This is the survivor.**

**What the proof says.** Step 1's coding, `proofs/P1_proof.md:275-277`:

> $$
> j_k(s)\;=\;1+\#\{i\in\{1,\dots,J-1\}:k_i\le s\}.
> $$

Step 13's construction and its corner clause, `:811-824`:

> $$
> \mathcal T_i(k;\vartheta)\;=\;\inf\bigl\{s\in[\underline s,\overline s]:j^\star(s;k)\ge i+1\bigr\},
> \qquad i=1,\dots,J-1,\qquad \inf\emptyset:=\overline s .
> $$
> Since $\{s:j^\star\ge i+2\}\subseteq\{s:j^\star\ge i+1\}$, the infima satisfy
> $\mathcal T_1(k)\le\mathcal T_2(k)\le\cdots\le\mathcal T_{J-1}(k)$, and every component lies in
> $[\underline s,\overline s]$ by construction. The **corner convention** is the display's
> $\inf\emptyset:=\overline s$: a plan that is optimal nowhere contributes an empty up-set and its
> cutoff sits at the top of the bracket, so it simply never appears in the range of $j^\star$ (pass-2
> N8's second half). Because $j^\star(\cdot;k)$ is weakly increasing, each $\{s:j^\star\ge i+1\}$ **is**
> an up-set, so these infima genuinely represent it: $j^\star(\cdot;k)$ agrees with Step 1's
> $j_{\mathcal T(k)}$ at every $s$ except possibly the finitely many $\mathcal T_i(k)$ at which the
> up-set fails to contain its own infimum, where the two differ by the boundary convention alone —
> card §3(i) pins no convention there.

Step 17(i)'s consistency clause, `:924-929`:

> **Consistency with the conjecture the prices are
> built on:** Steps 5, 6 and 9 price against the conjecture $k^\star$, whose induced map is Step 1's
> $j_{k^\star}$; that map and $j^\star(\cdot;k^\star)$ agree off the finitely many cutoff points, hence
> $\Phi_s$-almost surely, so every conditional probability, posterior and price is the same under
> either — the disagreement is invisible to (iii), (iv) and (v), which are statements about
> probabilities.

Step 19's parenthetical, `:973-975`:

> *(symbol updated 2026-08-25 round 2 with P1-R23; $\Omega$ is unaffected by the change, since
> $j^\star(\cdot;k^\star)$ and Step 1's $j_{k^\star}$ can differ only at the finitely many cutoff
> points, a $\Phi_s$-null set)*

**What GPT claims** (response `:228-276`): setting $k_i=\overline s$ does not encode "never" — under
Step 1's coding it activates plan $i+1$ at every $s\ge\overline s$. Witness $J=2$,
$j^\star(s;k)\equiv1$: empty upper level set, $\mathcal T_1(k)=\overline s$, but
$j_{\mathcal T(k)}(s)=2$ for every $s\ge\overline s$; $s$ is Gaussian and $\overline s$ is finite, so
$\Pr(s\ge\overline s)>0$ and the two maps disagree on a positive-probability tail. Consequently the
representation claim is false, the conjectured population need not agree a.s. with the proposed
equilibrium strategy, Step 17(i) does not establish card §3(i), and Step 19's parenthetical need not
hold. GPT adds: "There is no statement-preserving prose-only repair", and offers two options —
tail conditions on h.6 and the P1 row, or a sentinel re-parameterisation used consistently in Step
1, the price system, $\mathcal T$ and card §3.

**Verdict: UPHELD, WRONG-class, at theorem level under the printed coding.** Five checks.

1. **The coding claim is arithmetic.** With $k_1=\overline s$ and $J=2$,
   $j_{\mathcal T(k)}(s)=1+\mathbf 1\{\overline s\le s\}$, which is $2$ on $[\overline s,\infty)$.
   The corner value activates the plan; it does not retire it.
2. **The domain is $\mathbb R$, not the bracket.** Step 13 (`:780-781`) says Step 11 "determines
   $U_j(s;k)$ for every $j$ and $s$ — at **every** $s$, by Step 9(c)'s convention"; Step 17(ii)
   (`:934`) says $j^\star(s;k^\star)\in\arg\max_jU_j(s;k^\star)$ "at **every** $s$"; Step 20 works
   with $\Omega=1-\Phi_s(s_F)$ over the signal line; card §4.1 makes $s=v+\varepsilon$ Gaussian with
   full support. Only the **cutoffs** are confined to $[\underline s,\overline s]$ — the NOTATION
   DELTA row (`:1244`) calls it "the common signal bracket underlying $\Theta$". So
   $\Pr(s\ge\overline s)>0$ with $\overline s$ finite by compactness of $\Theta$.
3. **The witness is card-legal and sharper than GPT states it.** Take $J=2$ on a menu whose plan 2
   is dominated, so $j^\star(\cdot;k)\equiv1$ at every $k\in\Theta$. h.3 holds on both clauses
   ($U_2-U_1<0$ everywhere: zero crossings; the constant selection is weakly increasing). h.7,
   h.9–h.17 are untouched. Then $\mathcal T_1(k)\equiv\overline s$, so **$\mathcal T$ is constant —
   hence continuous, hence a self-map — and h.6's continuity and self-map halves both hold**. Brouwer
   returns $k^\star=\overline s$ immediately. At that fixed point $j_{k^\star}(s)=2$ for all
   $s\ge\overline s$ while $j^\star(s;k^\star)=1$ there. The failure is therefore isolated in the
   **bracket** half of h.6 and in the **representation**, not in continuity or self-mapping.
4. **The file's own counterexample instantiates it.** Step 13's "Why not the largest maximiser"
   (`:801-808`) constructs, explicitly *inside* h.3, a configuration with "$U_2-U_1\le0$ everywhere
   with equality at exactly one point $s_0$ — a tangential touch, so zero crossings … and the
   constant selection $j\equiv1$ is weakly increasing"; it then concludes "The largest **weakly
   increasing** selection is $j\equiv1$ there, as it should be." That is $j^\star\equiv1$ with
   $\{s:j^\star\ge2\}=\emptyset$: the proof exhibits the corner case as an admissible configuration
   two paragraphs before the sentence that mishandles it.
5. **The consequence bites where GPT says.** Under the witness, Step 17(i)'s "$\Phi_s$-almost
   surely" is false and Step 19's parenthetical is false. Neither assembly repairs it: taking the
   equilibrium plan map to be $j^\star$ leaves the prices, posteriors and entry probabilities of
   §3(iii)–(v) computed against a **different** population on a positive-probability set; taking it
   to be $j_{k^\star}$ restores §3(iii)–(v) but breaks §3(ii), since $j_{k^\star}=2$ on
   $[\overline s,\infty)$ where plan 2 is not optimal — which is precisely the defect P1-R23 and
   P1-R28 moved to $j^\star$ in order to avoid.

**The one defence, and why it does not close at wording grade.** h.6 reads "All best-response
cutoffs lie in a common compact ordered polytope $\Theta$" (`proofs/P1_proof.md:111-112`; card §5's
A6 block, `MODEL_CARD.md:267-268`). Read as *"for every $k$ and every adjacent pair the
best-response cutoff exists and lies in the bracket"*, the witness is outside the theorem and the
finding dissolves. That reading is available — it is exactly what Step 14 (`:833-850`) proves in the
four-action specialisation ("every indifference signal is finite and bounded uniformly in the
conjecture") and calls "the first of the two things h.6 is doing". **But the proof's own text
contradicts it**, and so does the card's:

- Step 13 states the corner convention as a **live** code for "a plan that is optimal nowhere",
  which the strong reading of h.6 would make impossible;
- Step 16 (`:900-905`) reads h.6 as applying "under the named largest-weakly-increasing-selection
  tie-break and the $\inf\emptyset:=\overline s$ **corner convention**";
- the card's P1 row (`MODEL_CARD.md:551`) reads A6 as asserting that $\mathcal T$ — "**under a named
  tie-break-and-corner selection**, without which a correspondence cannot be called continuous" — is
  a well-defined single-valued continuous self-map of $\Theta$.

So the controlling record contemplates corners **arising**, and the strong reading is not simply
what h.6 already says — adopting it **removes configurations the proof and the card currently
present as covered**. That is a change in the antecedent's content, not a correction of prose.

**Grade: SUBSTANCE.** Both available routes change either the antecedent or the parameterisation.
Neither is a wording repair. Two packages are drafted; **the choice between them is not this audit's
to make.**

### DRAFTED REPAIR — P1-R40-A (Package A: name what h.6's bracket clause delivers). Grade: **SUBSTANCE.**

**(A1) Step 13, replacing the corner clause at `:817-824`.**

> The display's $\inf\emptyset:=\overline s$ is a **totalisation, not a code for "never"**: it makes
> $\mathcal T_i$ defined at every $k$, and under h.6 it is never triggered. **What h.6's bracket
> clause is assumed to deliver, written out.** h.6 asserts that all best-response cutoffs lie in the
> common compact ordered polytope $\Theta$; read at the level Step 14 consumes it, that is: *for
> every $k\in\Theta$ and every $i\in\{1,\dots,J-1\}$ the set $\{s\in\mathbb R:j^\star(s;k)\ge i+1\}$
> is a **nonempty** up-set whose infimum lies in $[\underline s,\overline s]$.* Under that clause,
> and because $j^\star(\cdot;k)$ is weakly increasing so each such set **is** an up-set, the infima
> genuinely represent $j^\star$ on **all of $\mathbb R$**: $j^\star(\cdot;k)$ agrees with Step 1's
> $j_{\mathcal T(k)}$ at every $s$ except possibly the finitely many $\mathcal T_i(k)$ at which the
> up-set fails to contain its own infimum, where the two differ by the boundary convention alone —
> card §3(i) pins no convention there.
>
> *Corrected 2026-08-29 (**P1-R40-A**, polish-pass finding F5). The pre-repair text read
> $\inf\emptyset:=\overline s$ as a live corner code — "a plan that is optimal nowhere contributes an
> empty up-set and its cutoff sits at the top of the bracket, so it simply never appears in the range
> of $j^\star$" — and **that reading is false as a representation claim**. Step 1 codes
> $j_k(s)=1+\#\{i:k_i\le s\}$, so $k_i=\overline s$ does not retire plan $i+1$: it activates it at
> every $s\ge\overline s$. Take $J=2$ on a menu whose plan 2 is dominated, so $j^\star(\cdot;k)\equiv1$
> at every $k$ — admissible under h.3, and the same configuration this step's own tangency
> counterexample below produces. Then $\{s:j^\star\ge2\}=\emptyset$, $\mathcal T_1\equiv\overline s$,
> $\mathcal T$ is constant (so h.6's continuity and self-map halves both hold) and Brouwer returns
> $k^\star=\overline s$, while $j_{k^\star}(s)=2$ for every $s\ge\overline s$. The signal is Gaussian
> (h.17-d) and $\overline s$ is finite, so $\Pr(s\ge\overline s)>0$: the two maps disagree on a
> **positive-probability** tail rather than at finitely many points, and Step 17(i)'s
> $\Phi_s$-almost-sure consistency clause and Step 19's "$\Omega$ is unaffected" parenthetical both
> fail there. The mirror case is the lower endpoint: if $j^\star\ge i+1$ at some $s<\underline s$,
> the infimum over $[\underline s,\overline s]$ returns $\underline s$ and the two maps disagree on
> $(-\infty,\underline s)$. The bracket clause as now stated excludes both.*

**(A2) Step 14, appended after "…the first of the two things h.6 is doing." (`:849-850`).**

> Said in the form Step 13 consumes: what h.6's bracket clause supplies is that **every** adjacent-pair
> indifference signal **exists** and lies in $[\underline s,\overline s]$ — which is exactly what the
> four-action argument above establishes in its specialisation, and exactly what excludes both an
> adjacent pair with no crossing anywhere (a plan optimal nowhere, and with it every plan above it)
> and an adjacent pair whose crossing sits outside the bracket. A menu with a dominated top plan
> satisfies h.1–h.4, h.7 and h.9–h.17 and **fails this clause**; on such a menu P1 asserts nothing.

**(A3) NOT CLAIMED gains item 16 (appended, so no cross-reference renumbers).**

> 16. That P1 covers menus on which some adjacent plan pair has no indifference signal in the common
>     bracket — in particular menus with a dominated top plan, where $\{s:j^\star(s;k)\ge i+1\}$ is
>     empty. h.6's bracket clause as Steps 13–14 consume it excludes them, and Step 13's corrected
>     corner note records why: under Step 1's coding the finite cutoff vector cannot represent
>     $j^\star$ on the Gaussian tails there. *Added 2026-08-29, P1-R40-A, polish-pass finding F5.*

**(A4) Card-side follow-on — DRAFTED, NOT APPLIED, and outside this audit's edit surface.** The P1
row's "**A6 is read**" sentence (`MODEL_CARD.md:551`) should carry the same clause, since it is the
statement of record the re-derivation works from. Draft, for the orchestrator and Austin:

> after "with $\Theta$ nonempty per §4.5", add: "— and, in the **bracket** half, that for every
> $k\in\Theta$ and every adjacent plan pair the best-response indifference signal **exists** and lies
> in the common bracket, which is what makes the finite cutoff vector represent the best-response
> plan map on the whole Gaussian signal line and not merely inside the bracket
> (`proofs/P1_proof.md` Steps 13–14; polish-pass audit 2026-08-29, P1-R40-A)."

### DRAFTED REPAIR — P1-R40-B (Package B: sentinel re-parameterisation). Grade: **SUBSTANCE.** Sketched, not drafted in full.

GPT's option 2. Redefine the cutoff parameterisation so that boundary values are genuine
always/never sentinels, and use that coding identically in Step 1's $j_k$, in $\mathcal T$, in the
price system and in card §3(i). **Recorded with three costs, which is why Package A is drafted in
full and this one is not.** (i) It edits **card §3**, the equilibrium notion — the highest-cost edit
surface in the lane, and one no proof-side repair may make. (ii) A genuine cutoff sitting **at** an
endpoint is then mis-coded as a sentinel, so the bracket must first be enlarged strictly beyond
h.6's, which reopens the bracket clause anyway. (iii) The lower sentinel ("always $\ge i+1$") cannot
be expressed by $j_k(s)=1+\#\{i:k_i\le s\}$ at all and needs a second coding change. Package A
reaches the same representation-faithfulness by naming what h.6 was already being read as supplying.

**Note on the lane's no-weakening rule.** Package A narrows the class of menus Step 13 currently
claims to cover. That is **not** a weakening of an established conclusion: the coverage as printed
rests on a representation claim that is false, and correcting a false claim is not retreat from a
true one — the same distinction the file itself draws at Step 9(d) (`:591-593`) and at P1-R12.

---

## Finding F6 — Step 15 asserts cutoff continuity the file does not derive. UPHELD. WRONG-class.

**What the proof says**, `proofs/P1_proof.md:854-865`:

> $U_j(s;k)$ is continuous in $k$ for each fixed $(j,s)$: the pooled and flagged inner prices
> are continuous in the cutoffs — *commentary, not a consumed hypothesis (pass-1 finding 3): this
> clause read "by h.5", but h.5 is struck and this step's actual route to continuity of $\mathcal T$ is
> h.6 asserting it outright at Step 16; …* — and by Step 4 they enter $U_j$ only through $(\hat v,\pi)$, which are
> ratios of integrals over signal intervals with endpoints $k$ and are continuous in $k$ wherever the
> conditioning event has probability bounded away from zero; at histories of vanishing probability
> the Step 9 perturbation limit supplies the value. **That is continuity in $k$ at fixed $(j,s)$, and it
> is not enough**

**What GPT claims** (response `:296-309`): supplying a value at a zero-probability history does not
show the value equals the limit from nearby conjectures at which the history has positive
probability; Step 9 uses two different posterior formulas and nothing shows they agree as
$\Lambda_k\downarrow0$; the card's A5/A6 record identifies this composition-through-conditioning as
the discontinuous object; Step 8 gives continuity of the root **given** $(\hat v,\pi)$, not of
$k\mapsto(\hat v,\pi)\mapsto P$.

**Verdict: UPHELD, WRONG-class.** The inline italic marks only the sub-clause about inner prices as
commentary; the sentence's **subject claim** — "$U_j(s;k)$ is continuous in $k$ for each fixed
$(j,s)$" — is asserted flatly, and the paragraph then reasons *from* it ("**That is** continuity in
$k$ at fixed $(j,s)$, and it is not enough"), treating it as established before naming the two
further conditions. It is not established anywhere in the file, and the controlling card says so
twice:

- A5 evidence note, `MODEL_CARD.md:252-257`: "(i) Continuity of the inner root **in its belief
  summaries** $(\hat v,\pi)$ follows from $m_0\ge0$ … (ii) Continuity of the **composition**
  $k\mapsto(\hat v,\pi)\mapsto P$ **in the cutoff vector** is what the clause above retains, and **no
  step derives it**".
- A6 evidence note, `MODEL_CARD.md:291-296`: "the failure is live at the **interior $n(s)$ cell
  edges** … measured $\mathcal T_2$ jumps of $6.33\times10^{-3}$ / $1.09\times10^{-2}$ /
  $2.83\times10^{-2}$ across $\le2\times10^{-9}$ steps in $k_2$", curated as executed t2 checks.

And the P1 row itself (`MODEL_CARD.md:551`) already names Step 15's cutoff-continuity citation as
non-load-bearing. So the proof text claims more than the record supports — which is the one place
the prompt's scope fence 1 authorises applicability commentary ("where the proof text itself claims
more than that record supports").

GPT's supporting point about the two posterior formulas is correct and is now sharper after F3: the
$\Lambda_k>0$ branch converges to the $j_k$-concentrated Bayes law and the $\Lambda_k=0$ branch to
the plan-uniform law, and these are different laws, so the value supplied at a $k$-null history is
in general **not** the one-sided limit of the values at nearby $k$ with $\Lambda_k>0$. That is the
mechanism the A6 note measures.

**A second site of the same overclaim**, which GPT reaches through F14 and I fold in here. Step 5's
closing sentence, `:378-383`: "the pooled price family $k\mapsto(P_d^P(\mathcal H_d^P;k))_{\mathcal
H_d^P}$ is a finite vector of **continuous functions of $k$** — at the control-node cell by (a) with
Steps 7–8, and at $d<H$ by (b) as a finite-sum conditional expectation of continuous functions — on
those histories that carry positive probability under the conjecture $k$." The final qualifier
narrows it but does not establish it: continuity in $k$ still requires $k\mapsto(\hat v,\pi)$ to be
continuous on that set, which Steps 7–8 do not give. The parenthetical "finite-sum conditional
expectation" is separately loose — the conditional expectation integrates over the continuous signal
and, on flagged branches, the flagged-tuple law.

### DRAFTED REPAIR — P1-R41, two sites. Grade: **WORDING-ONLY.**

**(a) Step 15, replacing the opening at `:854-866` up to and including "…needs two more things that
the card does not supply:".**

> **Nothing in Steps 4–10 derives continuity of $k\mapsto U_j(s;k)$ at fixed $(j,s)$, and this step
> does not assert it.** One link of the chain is derived: Step 7(iii) and Step 8 make the inner root
> exist, be unique and be continuous in its **belief summaries** $(\hat v,\pi)$, and by Step 4 those
> summaries are the only channel through which the information set enters the price. The other link
> is not. The $k$-dependence runs through the **conditioning**: $(\hat v,\pi)$ are ratios of
> integrals over signal intervals with endpoints $k$, continuous in $k$ only while the conditioning
> event's probability stays bounded away from zero, and at a history whose probability vanishes as
> $k$ moves it is Step 9's **construction**, not a continuity argument, that supplies the value —
> and Step 9(b)'s two branches are *different laws* (the $j_k$-concentrated Bayes posterior where
> $\Lambda_k>0$, the plan-uniform posterior where $\Lambda_k=0$), with no step here showing they
> agree as $\Lambda_k\downarrow0$. Card §5's A5 evidence note draws exactly this distinction and
> records the composition $k\mapsto(\hat v,\pi)\mapsto P$ as the underived one; card §5's A6 evidence
> note records it **measured to jump**, on $\bigcup_h\partial\{k:\Lambda_k(h)>0\}$, at the implemented
> calibration. **P1 therefore consumes h.6 as an assumption at precisely this point**: for the named
> largest-weakly-increasing-selection tie-break, the $\inf\emptyset$ totalisation and Step 9(c)'s
> reference-belief convention, $\mathcal T$ is a continuous self-map of $\Theta$ (Step 16).
> Conditions (i) and (ii) below are **candidate primitive sufficient conditions** for that
> assumption — the weakest pair this file can name — and are not consequences of the preceding steps:
>
> *Corrected 2026-08-29 (**P1-R41**, polish-pass finding F6). The pre-repair opening asserted flatly
> that "$U_j(s;k)$ is continuous in $k$ for each fixed $(j,s)$", carried a struck-h.5 clause marked
> as commentary inside that assertion, and then reasoned from it ("**That is** continuity in $k$ at
> fixed $(j,s)$, and it is not enough"). The assertion is derived nowhere in this file and the card's
> A5 and A6 evidence notes record the composed object as measured to fail. Nothing downstream is
> lost: this step's route to continuity of $\mathcal T$ was already h.6 asserting it outright at Step
> 16, as the struck h.5(c) records.*

**(b) Step 5, replacing the closing sentence at `:378-383`.**

> the pooled price family $k\mapsto(P_d^P(\mathcal H_d^P;k))_{\mathcal H_d^P}$ is a **finite**
> vector, indexed by Step 3's finite pooled alphabet — each entry an inner root at the belief
> summaries carried at its own history by (a) with Steps 7–8 at the control-node cell, and at $d<H$
> by (b) a conditional expectation of already-solved control-node values, which integrates over the
> continuous signal law and, on flagged branches, over the flagged-tuple law, and is **not** a finite
> sum over terminal states. **No continuity of this family in the conjecture $k$ is claimed here**:
> continuity in the belief summaries is Steps 7–8; continuity of the composition through the
> conditioning is not derived (Step 15) and enters only through h.6. Histories of zero probability
> under $k$, and histories of zero probability under every profile, are handled in Step 9(b) and
> 9(c) respectively. *(Amended 2026-08-29, **P1-R41**, polish-pass findings F6 and F14.)*

**Why the grade is wording.** The repair deletes assertions the file never derives and the card
records as measured false. The route the proof actually takes — h.6 asserting continuity of
$\mathcal T$ at Step 16 — is untouched, so the conditional Brouwer argument runs exactly as printed.
Nothing that any later step reads is removed.

---

## Finding F7 — the ordered polytope. NARROWED. GPT's consequence is misattributed.

**What the proof says**, `proofs/P1_proof.md:271-274`:

> Fix $k=(k_1\le\cdots\le k_{J-1})\in\Theta$, where
> $\Theta=\{k\in[\underline s,\overline s]^{J-1}:\underline s\le k_1\le\cdots\le k_{J-1}\le\overline s\}$
> is card §4.5's compact ordered polytope, nonempty, compact and convex as the intersection of a cube
> with the $J-2$ half-spaces $\{k_i\le k_{i+1}\}$.

**What the card says**, `MODEL_CARD.md:150`: "$\Theta$, $\vartheta$ | compact ordered cutoff
polytope; parameter vector | $\Theta$ nonempty, compact, convex".

**What GPT claims** (response `:339-347`): the card does not identify $\Theta$ with the whole
box-∩-ordering set, and for a proper ordered polytope Step 13's inequalities do not imply
$\mathcal T(k)\in\Theta$; the membership should be supplied by h.6's self-map clause.

**Verdict: NARROWED.** The premise is right and the consequence is misattributed.

- **Premise, upheld.** Card §4.5 states properties $\Theta$ must have; it names no particular set.
  The proof's "**is** card §4.5's compact ordered polytope" over-identifies a description with an
  instance. That is a citation nit worth fixing.
- **Consequence, rejected.** The proof does not import a possibly proper card-given polytope — it
  **defines** $\Theta$ as the ordered box on h.6's bracket, in the same sentence. On the ordered
  box, the nesting and bracket inequalities Step 13 establishes (`:815-816`) *do* imply membership.
  So Step 13's derivation is sound as it stands.
- **GPT's proposed closing sentence is refused.** It would replace Step 13's derived conclusion with
  "Membership in the possibly proper polytope $\Theta$ is the self-map content of h.6." That
  converts a **derived** result into an assumption. The lane's discipline forbids weakening a step
  conclusion, and Step 13's own summary (`:826-829`) names the self-map and weak-ordering halves as
  derived from h.3 — a claim the 2026-08-25 gate covered. Independently, card §5's A6 evidence note
  (`MODEL_CARD.md:298-301`) confirms the lane's reading that "Steps 13–14 … build from the bracket
  $[s_{lo},s_{hi}]$".

### DRAFTED REPAIR — P1-R42 (Step 1, replacing `:271-274`). Grade: **WORDING-ONLY.**

> Fix $k=(k_1\le\cdots\le k_{J-1})\in\Theta$, where
> $$\Theta\;:=\;\{k\in[\underline s,\overline s]^{J-1}:\underline s\le k_1\le\cdots\le k_{J-1}\le\overline s\}$$
> is the ordered box built on h.6's common bracket. It is **a** polytope of the kind card §4.5
> requires — nonempty, compact and convex as the intersection of a cube with the $J-2$ half-spaces
> $\{k_i\le k_{i+1}\}$ — and this proof fixes it as **the** $\Theta$ throughout. Card §4.5 states the
> properties $\Theta$ must have and names no particular set, so the choice is this file's and is made
> here, once.
>
> *Clarified 2026-08-29 (**P1-R42**, polish-pass finding F7), which read the pre-repair "is card
> §4.5's compact ordered polytope" as importing a possibly proper card-given polytope. **The
> finding's proposed consequence is not adopted**: it would move Step 13's derived
> $\mathcal T(k)\in\Theta$ into h.6's self-map clause, and on the ordered box the ordering and
> bracket inequalities of Step 13 do imply membership, so the derivation stands and is not weakened
> into an assumption.*

---

## Finding F8 — continuity of the inner root in $\pi$. UPHELD. WRONG-class.

**What the proof says.** Step 5(a), `proofs/P1_proof.md:359-360`: "**Step 7 supplies a unique fixed
point** of $\mathcal P_{\mathcal I}$ from h.12 ($m_0\ge0$), **with continuity in the belief from Step
8**." Step 6(b), `:401-402`: "**Step 8 makes it continuous** in the belief — indeed 1-Lipschitz,
since $\partial P/\partial\hat v\in(0,1]$ there." And Step 8 in full, `:458-465`:

> At the root, $\varrho'<0$ (Step 7(iii)), so the implicit function theorem applies to
> $\varrho(P;\hat v)=0$ and yields
> $$
> \frac{\partial P}{\partial\hat v}
> =\frac{1-p}{\,1-p+|p'(P)|\,(P+\bar m-A)\,}\;\in\;(0,1],
> $$

**What GPT claims** (response `:395-401`): the pooled belief varies in both $(\hat v,\pi)$; Step 8
varies $\hat v$ with $\pi$ held fixed and neither differentiates in $\pi$ nor proves joint
continuity; that missing continuity is used at Step 5(a) and Step 9(b).

**Verdict: UPHELD, WRONG-class (a citation that does not support what it is cited for).** Step 8 is
written in one argument, $\varrho(P;\hat v)$, and delivers one partial derivative. On the **flagged**
layer that suffices — Step 6(a) fixes $\pi\equiv1$, so $\hat v$ is the only moving summand, and
Step 6(b)'s citation is exact. On the **pooled** layer it does not: Step 4's own conclusion
(`:349-350`) is that the map "depends on $\mathcal I$ only through the two scalars
$(\hat v(\mathcal I),\pi(\mathcal I))$", and Step 5(a) is a pooled control node where both move.
Step 17(iv) then rests on the same citation at reachable $k$-null histories. So the gap is real and
load-bearing.

The repair is routine and uses nothing beyond what Step 7 already supplies, sharpened by P1-R50.

### DRAFTED REPAIR — P1-R43. Grade: **SUBSTANCE (statement-preserving).**

**(a) Step 8, appended after the displayed derivative.**

> **Continuity in the full belief pair.** The pooled layer moves both summaries, so the root is
> needed as a function of $(\hat v,\pi)$ and not of $\hat v$ alone. Write the residual with both
> arguments,
> $$\varrho(P;\hat v,\pi)=\bigl(1-p(P;\pi)\bigr)\bigl(A(\hat v,\pi)-P\bigr)+p(P;\pi)\,\bar m(\pi),$$
> $$A=\hat v+\pi\Delta_V,\qquad \bar m=m_0+\pi\Delta_m,\qquad
> p(P;\pi)=1-\Phi\!\Bigl(\tfrac{P+K+\bar m(\pi)-\bar S}{\sigma_\xi}\Bigr).$$
> $A$ and $\bar m$ are affine in $(\hat v,\pi)$ by card §4.1 and h.12, and $\Phi$ is smooth, so
> $\varrho$ is $C^1$ jointly in $(P,\hat v,\pi)$ on $\mathbb R\times\mathbb R\times[0,1]$. By Step
> 7(iii) in its sharpened form, $\partial_P\varrho<0$ at every $P\ge A$, hence at every root. The
> implicit function theorem therefore gives a locally $C^1$ root $P=P(\hat v,\pi)$ around every
> belief pair, and Step 7(ii)–(iii)'s global existence and uniqueness make those local root functions
> agree wherever their domains overlap. **Hence the unique inner root is a single-valued continuous
> function of $(\hat v,\pi)$ jointly on $\mathbb R\times[0,1]$.** The displayed
> $\partial P/\partial\hat v\in(0,1]$ is the non-expansiveness bound in the $\hat v$ direction at
> fixed $\pi$, which is what Step 6(b) consumes on the flagged cell, where $\pi\equiv1$ by Step 6(a).
>
> *Added 2026-08-29 (**P1-R43**, polish-pass finding F8): Step 5(a) cited "continuity in the belief
> from Step 8" and Step 9(b) invoked "Step 8's 1-Lipschitz bound" at pooled histories where $\pi$
> varies, while the pre-repair Step 8 differentiated in $\hat v$ at fixed $\pi$ only. This appendix
> supplies the joint statement those citations consume. **No hypothesis is added** — the argument
> runs on h.12, Step 4's reduction and Step 7 alone — and no step conclusion changes.*

**(b) Step 5(a), `:360`.** Replace "with continuity in the belief from Step 8" with "with **joint**
continuity in the belief pair $(\hat v,\pi)$ from Step 8".

**Why the grade is substance.** This is new mathematical content that Steps 5(a), 9(b) and 17(iv)
consume. It is **statement-preserving** — no hypothesis added, no conclusion changed, no
parameterisation touched — but a proof carrying it must clear the two-pass gate before the row can
rest on it.

---

## Finding F9 — Step 9(b)'s price convergence omits $\pi_n$. UPHELD. WRONG-class.

**What the proof says**, `proofs/P1_proof.md:537-540`:

> Either
> way $\hat v_n\to\hat v_\infty$ and, by Step 8's 1-Lipschitz bound, the prices converge
> with them. Hence the limiting belief **and the limiting price** exist at every reachable
> pooled history, on path and off

**What GPT claims** (response `:441-443`): the price is a function of both $\hat v_n$ and $\pi_n$;
Step 8's bound controls only $\hat v$ at fixed $\pi$; the step never defines $\pi_n$, proves
$\pi_n\to\pi_\infty$, or invokes joint continuity.

**Verdict: UPHELD, WRONG-class.** Step 4 (`:349-350`) makes the pricing map a function of
$(\hat v,\pi)$; Step 9(b) tracks only $\hat v_n$ (`:524-525`); no $\pi_n$ appears anywhere in the
step or in the NOTATION DELTA. The inference "the prices converge with them" therefore does not go
through as written, and Step 17(iv) (`:944-947`) reads exactly this limiting price at reachable
$k$-null pooled histories, which the step itself flags as load-bearing where it is least obvious
(`:541-544`).

### DRAFTED REPAIR — P1-R44 (Step 9(b), replacing `:537-539`). Grade: **SUBSTANCE (statement-preserving).**

> Both belief summaries have to be carried, because Step 4's pricing map depends on the information
> set through the pair. Alongside $\hat v_n$ define the stage-$n$ engagement posterior
> $$\pi_n\;:=\;\sum_{j\in\mathcal J}a_j\int\mu_n(j,s)\,\mathrm ds\;\in[0,1],$$
> card §4.3's $\pi(\mathcal I)$ evaluated at $\mu_n$. If $\Lambda_k>0$, then $a_j\in\{0,1\}$ (card
> §4.2) makes $a_j\mu_n(j,s)\le\mu_n(j,s)$, so the same denominator bound gives the integrable
> envelope $2\varphi_sL_j/\Lambda_k$ and dominated convergence yields $\pi_n\to\pi_\infty$; if
> $\Lambda_k=0$, then $\mu_n$ is $n$-free by the display above, so $\pi_n$ is constant and the
> convergence is immediate. The same two cases give $\hat v_n\to\hat v_\infty$. Hence
> $(\hat v_n,\pi_n)\to(\hat v_\infty,\pi_\infty)$, and by **Step 8's joint continuity of the unique
> inner root in $(\hat v,\pi)$** the prices converge with them: $P_n\to P_\infty$. Step 8's bound
> $\partial P/\partial\hat v\in(0,1]$ remains available for comparisons at fixed $\pi$.
>
> *Added 2026-08-29 (**P1-R44**, polish-pass finding F9): the pre-repair sentence inferred price
> convergence from $\hat v_n\to\hat v_\infty$ together with Step 8's 1-Lipschitz bound alone. The
> price is a function of both summaries; $\pi_n$ was never defined, never shown to converge, and the
> 1-Lipschitz bound is a $\hat v$-direction bound at fixed $\pi$. **Depends on P1-R43.**
> No hypothesis is added and no step conclusion changes.*

**Also required by this repair.** The NOTATION DELTA gains $\pi_n$ (it is a new proof-local symbol,
card §8 rule 3):

> | $\pi_n$ | the stage-$n$ engagement posterior at a pooled history, $\sum_ja_j\int\mu_n(j,s)\,\mathrm ds$ (Step 9(b)) | card §4.3's $\pi(\mathcal I)$ evaluated at $\mu_n$, not a new object; the subscript $n$ matches $\mu_n$, $w_n$, $t_n$ and $Z_n$ and keeps it clear of $\pi_\circ$, the reference-belief scalar of Step 9(c). Declared 2026-08-29, **P1-R44** |

---

## Finding F10 — empty interior does not supply the strict sign pattern. UPHELD. WRONG-class, on a condition no step consumes.

**What the proof says**, `proofs/P1_proof.md:880-890`:

> (ii) *transversality*: for every adjacent pair $(i,i+1)$ and every $k\in\Theta$, the indifference
> set $\{s:U_{i+1}(s;k)=U_i(s;k)\}$ has empty interior. h.3 says the difference crosses zero "at
> most once", which does not exclude an interval on which it is identically zero; …
>
> **Under (i) and (ii), continuity of $\mathcal T$ follows from (i)'s joint continuity together
> with the strict sign change of $U_{i+1}-U_i$ at each crossing: the sign change locates the crossing
> and the joint continuity moves it continuously with $k$.**

**What GPT claims** (response `:487-494`): empty interior excludes a tie interval but does not
establish a unique threshold, strict signs either side, corner behaviour when a plan is absent, or
continuity of the selected threshold; the strict-sign conclusion is not part of (ii) and is not
derived from h.3 plus empty interior.

**Verdict: UPHELD, WRONG-class.** The gap is exhibited by the file's own text. h.3 says the
difference **crosses** zero at most once (`:89-91`); a **tangency** — $d_i:=U_{i+1}-U_i\le0$
everywhere with a single zero at $s_0$ — has zero crossings, so h.3 holds, and the tie set
$\{s_0\}$ has empty interior, so (ii) holds. There is then no crossing, no strict sign change and no
threshold, and the boxed argument has nothing to locate. This is precisely the configuration Step 13
constructs at `:801-808` to justify the largest-weakly-increasing tie-break, and it is inside h.3 by
that step's own words.

**Non-blocking for the theorem.** (i) and (ii) are named as candidate sufficient conditions that
would *replace* h.6, not as hypotheses: `:891-893` reads "h.6 assumes the conclusion instead: it
asserts continuity of $\mathcal T$ directly", and NOT CLAIMED 2 and 11 record the same. So no step
consumes (ii), and the repair touches an optional route only.

**Cross-finding tension, recorded.** GPT's own replacement condition permits "$c_i(k)=\overline s$
… to encode an upper plan that is never preferred within the bracket" (response `:513-516`). That is
exactly the corner encoding F5 shows the finite cutoff vector cannot carry. The permission is **not
adopted**; the drafted (ii) below requires a genuine sign change inside the bracket, consistent with
P1-R40-A.

### DRAFTED REPAIR — P1-R45 (Step 15, replacing (ii) at `:880-884` and the boxed sentence at `:886-890`). Grade: **WORDING-ONLY.** Conditional on P1-R40's route.

> (ii) *Robust threshold identification.* For each adjacent pair write
> $d_i(s,k):=U_{i+1}(s;k)-U_i(s;k)$. The condition is: for every $k\in\Theta$ there is a **unique**
> $c_i(k)\in[\underline s,\overline s]$ with
> $$d_i(s,k)<0\ \text{ for } s<c_i(k),\qquad d_i(s,k)>0\ \text{ for } s>c_i(k).$$
> This asks strictly more than h.3 plus a tie set of empty interior. h.3 says the difference
> **crosses** zero at most once, which admits two failures: an interval of ties — which the
> pre-repair (ii) excluded, and which is all it excluded — and an isolated **tangency**, at which
> $d_i\le0$ everywhere with one zero, so that there is no crossing, no sign change and no threshold
> at all. Step 13's own "Why not the largest maximiser" counterexample is that tangency, and it sits
> inside h.3.
>
> **Under (i) and (ii), each $\mathcal T_i=c_i$ is continuous, by the following topological argument
> — the implicit function theorem is the wrong tool here, since it would need $U$ differentiable in
> $(s,k)$ and no hypothesis supplies that (batch-1 audit P1-R4).** Let $k_n\to k$ in $\Theta$ and
> take any convergent subsequence $c_i(k_{n'})\to c$, which exists because $[\underline s,\overline
> s]$ is compact. For every $s<c$ one eventually has $s<c_i(k_{n'})$, so $d_i(s,k_{n'})<0$, and (i)'s
> joint continuity gives $d_i(s,k)\le0$; symmetrically $d_i(s,k)\ge0$ for every $s>c$. Uniqueness of
> the sign threshold at $k$ forces $c=c_i(k)$. Every convergent subsequence has the same limit, so
> $c_i(k_n)\to c_i(k)$ and each component of $\mathcal T$ is continuous. These conditions are
> sufficient and are **not** claimed weakest; P1 continues to assume their conclusion through h.6,
> and (i)+(ii) is the weakest pair this file can name that would replace it.
>
> *Corrected 2026-08-29 (**P1-R45**, polish-pass finding F10): the pre-repair (ii) asked only that
> the indifference set have empty interior, and the boxed conclusion then ran on "the strict sign
> change of $U_{i+1}-U_i$ at each crossing", which empty interior does not supply — the tangency case
> satisfies h.3 and empty interior and has no crossing. **Note against P1-R40:** the finding's own
> proposed condition additionally permitted $c_i(k)=\overline s$ to encode an upper plan never
> preferred within the bracket, which is precisely the corner encoding finding F5 shows the finite
> cutoff vector cannot carry; that permission is not adopted.*

**Cross-references checked.** WHERE IT FAILS 3 (`:1043-1059`) turns on a plateau interval, which
violates the new (ii) as it violated the old one, so both its statement and P1-R32's plateau note
still resolve. Card §5's A3 note's citation of "Step 15(i) / WHERE IT FAILS 4" is untouched.

---

## Finding F11 — the Kakutani remark. UPHELD-WITH-SCOPE. WRONG-class in a non-load-bearing remark.

**What the proof says**, `proofs/P1_proof.md:956-965`:

> It is nonempty by h.3; its values are convex, because at an indifference plateau the
> admissible values of a component form an interval and the ordering constraints cut the product of
> those intervals by half-spaces; its values are compact, being closed subsets of the compact
> $\Theta$; and its graph is closed by the maximum theorem, given that $U_j(s;k)$ is jointly
> continuous in $(s,k)$ … Kakutani's theorem then gives a fixed point without
> Step 15(ii) and without h.6's continuity clause.

**What GPT claims** (response `:545-552`): the paragraph does not establish that every admissible
cutoff vector is an independent component-wise choice from intervals, that skipped plans and
non-adjacent ties cannot make the value a non-convex union of faces, that limits of represented
monotone selections stay represented under the corner convention, or that the ordinary maximum
theorem supplies a closed graph for a selection-valued problem; and F5's corner problem propagates
to $\mathfrak T$.

**Verdict: UPHELD-WITH-SCOPE.** The assertions are genuinely unsupported at the level card §8 rule 7
requires ("No 'clearly', 'it follows', 'standard', 'obviously' in a proof step" — "by the maximum
theorem" here stands in for an unshown step in a non-standard, selection-valued setting). The
**scope** is that Step 18 is explicitly outside the claim: its own heading calls it "a strengthening
that is not part of the claim", `:964-965` says "Card §3 fixes the Brouwer route for P1, so this is
recorded as a remark", and NOT CLAIMED 3 disclaims it. No step in 1–17 or 19–20 reads it. So the
finding does not touch the theorem; it corrects an over-assertion in a remark.

### DRAFTED REPAIR — P1-R46 (Step 18, replacing `:956-965`). Grade: **WORDING-ONLY.**

> Define instead the best-response correspondence
> $\mathfrak T(k)=\{k'\in\Theta:k'\text{ represents some optimal weakly increasing plan selection at
> }k\}$. It is nonempty by h.3, and its values are compact as closed subsets of the compact $\Theta$.
> A Kakutani argument would additionally need a lemma that, **under this file's cutoff encoding**,
> $\mathfrak T$ has **convex** values and a **closed graph**, and no such lemma is proved here. The
> plateau picture — at an indifference plateau the admissible values of a component form an interval
> and the ordering constraints cut the product by half-spaces — does not by itself show that every
> admissible cutoff vector is an independent component-wise choice, and it does not cover skipped
> plans or non-adjacent ties; and the maximum theorem, which concerns choice from a fixed set at a
> parameter, does not by itself deliver a closed graph for a **selection-valued** problem whose
> limits must remain *represented* under the corner conventions of Step 13 — conventions that
> P1-R40's finding shows are not representation-faithful in general. **No Kakutani conclusion is
> therefore drawn here.** Card §3 fixes the Brouwer route for P1, so this stays a remark; see NOT
> CLAIMED 3.
>
> *Scoped 2026-08-29 (**P1-R46**, polish-pass finding F11): the pre-repair text asserted convex
> values and a closed graph outright and concluded that "Kakutani's theorem then gives a fixed point
> without Step 15(ii) and without h.6's continuity clause". That conclusion is withdrawn as
> unestablished. It is outside the claim (NOT CLAIMED 3) and no step reads it, so nothing the theorem
> rests on changes.*

**CARD-SIDE FOLLOW-ON — flagged, not resolved.** Card §5's A6 evidence note (`MODEL_CARD.md:306-308`)
lists among "Repairs on file, both outside §3's declared Brouwer-with-one-fixed-family route: the
$t$-constrained game + Kakutani + $t\downarrow0$ (`proofs/P1_proof.md` Step 18)". That is a
**different construction** from Step 18's plain-Kakutani remark — Step 18 carries no $t$-constrained
game and no $t\downarrow0$ limit. Whether the pointer is loose, or names a construction that lives
elsewhere, is not this audit's to settle; the orchestrator should check it against whatever text
lands at Step 18. **No card edit is drafted here.**

---

## Finding F12 — h.12's card status. UPHELD-WITH-SCOPE. STALE.

**What the proof says**, `proofs/P1_proof.md:167-169`:

> 12. **h.12 [ADDITION] — nonnegative premia.** $m_0\ge 0$. Card §4.1 restricts only $m_1>m_0$ and
>     $\Delta_m>0$; it does not sign $m_0$. With $\Delta_m>0$ and $\pi\in[0,1]$ this gives
>     $\bar m(\mathcal I):=m_0+\pi(\mathcal I)\Delta_m\ge 0$. *Used: Steps 7, 8.*

**What the card says**, `MODEL_CARD.md:83`: "$m_1 > m_0$; **and $m_0 \ge 0$** — adopted from P1's
h.12".

**Verdict: UPHELD-WITH-SCOPE, STALE.** The sentence "it does not sign $m_0$" was true at the
2026-08-20 stamp this file was written against (`:3`) and is false at the controlling stamp. The
**scope** is that the file already records the absorption twice — LABEL CLAIMED reason 2
(`:1125-1127`: "h.12 ($m_0\ge0$) is now card §4.1's sign restriction … so those two are discharged")
and P1-R15 (`:1397`) — so this is a single un-swept site, not an unrecorded fact. The inconsistency
is internal: h.14 carries exactly such a status marker ("[ADDITION, card gap closed 2026-08-23]",
`:174`) and h.12 does not.

### DRAFTED REPAIR — P1-R47 (replacing h.12 at `:167-169`). Grade: **WORDING-ONLY.**

> 12. **h.12 = card §4.1's nonnegative-premium restriction** *(was [ADDITION]; card gap closed —
>     see the status note)*. $m_0\ge0$. With $\Delta_m>0$ and $\pi\in[0,1]$ this gives
>     $\bar m(\mathcal I):=m_0+\pi(\mathcal I)\Delta_m\ge0$.
>     *Status corrected 2026-08-29 (**P1-R47**, polish-pass finding F12): the pre-repair item was
>     marked [ADDITION] and read "Card §4.1 restricts only $m_1>m_0$ and $\Delta_m>0$; it does not
>     sign $m_0$", which was true at the 2026-08-20 stamp this file was written against and is stale
>     at the controlling stamp — card §4.1's $m_0,m_1$ row now carries "**and $m_0\ge0$** — adopted
>     from P1's h.12". The restriction originated in this proof and has been absorbed into the card;
>     it is no longer an addition outside it. LABEL CLAIMED reason 2 and P1-R15 already record the
>     absorption, and this item now records it too, on the pattern h.14 already uses.*
>     *Used: Steps 7, 8.*

---

## Finding F13 — Step 4's Gaussian-law citation. UPHELD. WRONG-class (citation).

**What the proof says**, `proofs/P1_proof.md:340`: "With $\xi\sim N(0,\sigma_\xi^2)$ (h.1),
$p=1-\Phi\bigl((P+K+\bar m-\bar S)/\sigma_\xi\bigr)$".

**Verdict: UPHELD.** h.1 = A1 is "independent primitives … all variances strictly positive"
(`:75-76`; card §5 A1 at `MODEL_CARD.md:172-173`) — independence and positive variance, not a
distributional form. The Gaussian law is card §4.1's, carried into the hypothesis list as h.17-d
("§4.1's distributional forms — $v,\varepsilon,\xi$ Gaussian with the projection $\beta$", `:258`).
The step's own preceding sentences use h.1 correctly, for independence (`:331-333`); only the
distributional citation misattributes. Non-blocking, and the computation is unchanged.

### DRAFTED REPAIR — P1-R48 (Step 4, replacing the clause at `:340`). Grade: **WORDING-ONLY.**

> With $\xi\sim N(0,\sigma_\xi^2)$ by **h.17-d** — card §4.1's distributional forms; h.1 supplies
> $\xi$'s independence from $(v,\varepsilon,z_{0:H})$, which is what the previous sentence used, and
> the strict positivity of its variance, not the Gaussian law itself —
> $p=1-\Phi\bigl((P+K+\bar m-\bar S)/\sigma_\xi\bigr)$, which is card §4.3's entry row verbatim and
> lies in $(0,1)$ for every finite $P$. *(Citation corrected 2026-08-29, **P1-R48**, polish-pass
> finding F13.)*

---

## Finding F14 — Step 5(b)'s card ambiguity. UPHELD-WITH-SCOPE. STALE.

**What the proof says**, `proofs/P1_proof.md:372-375`:

> Under the other reading of §4.3's $Y$ row (the $P$ inside $Y$ is
> the price at whichever information set is conditioning) part (a)'s fixed-point argument applies at
> these dates too. **Card ambiguity, regeneration item: card §4.3's $Y$ row should pin which $P$ it
> means** (batch-1 audit P1-R8).

and NOT CLAIMED 12 (`:1310-1312`): "That card §4.3's $Y$ row has been disambiguated."

**What the card says**, `MODEL_CARD.md:121`, the $P_d^P$/$P^F$ row: "**The genuine fixed point sits
at control nodes.** At an earlier pooled date $d<H$ the price is a *tower expectation* of
already-solved control-node values, with no self-reference; only the control-node map is a fixed
point to be solved (batch-1 audit P1-R8, `proofs/P1_proof.md` Step 5, split (a)/(b))."

**Verdict: UPHELD-WITH-SCOPE, STALE.** The card has pinned the reading, and it pins it by citing
this very split. Reading (b) is the card's, not one of two live readings, and the regeneration item
is discharged. **Two scopings.** (i) The card resolves it in the $P_d^P$ row rather than by editing
the $Y$ row's symbol; the substance is settled either way, and this audit records that rather than
asking for a further card edit. (ii) GPT's instruction "Delete NOT CLAIMED 12" is **not adopted** —
lane discipline supersedes a landed record line with a dated amendment and never deletes it. GPT's
"finite-sum" correction and its "no continuity in $k$ is claimed" clause are carried by P1-R41(b),
not here.

### DRAFTED REPAIR — P1-R49, two sites. Grade: **WORDING-ONLY.**

**(a) Step 5(b), appended after the "Card ambiguity, regeneration item" sentence at `:374-375`. The
existing two-reading text stays as printed.**

> *Superseded 2026-08-29 (**P1-R49**, polish-pass finding F14). The ambiguity is resolved on the card
> at the controlling stamp: card §4.3's $P_d^P$ row reads "**The genuine fixed point sits at control
> nodes.** At an earlier pooled date $d<H$ the price is a *tower expectation* of already-solved
> control-node values, with no self-reference; only the control-node map is a fixed point to be
> solved", and cites this split by name. Reading (b) is therefore the card's, the regeneration item
> is discharged, and the two-reading text above stands as the record of why this step was written to
> survive either.*

**(b) NOT CLAIMED 12, appended (not replaced).**

> *Amended 2026-08-29 (**P1-R49**): **discharged.** Card §4.3's $P_d^P$ row pins the reading at the
> controlling stamp — earlier pooled dates are tower expectations of solved control-node values, with
> no self-reference — so this item no longer disclaims a live ambiguity. What it now records is that
> the disambiguation is the card's and that this file's step was written to survive either reading.*

---

## Finding F15 — Step 7(iii)'s uniqueness argument. UPHELD. POLISH-class.

**What the proof says**, `proofs/P1_proof.md:441-448`:

> At any root, (i) gives $P\ge A$, so
> $P+\bar m-A\ge\bar m\ge 0$ and the first term is $\le 0$; the second is $<0$ since $p<1$. Hence
> $\varrho'<0$ **strictly at every root**. Suppose two roots $P_1<P_2$ with no root between them.
> …The two conclusions contradict each other, so there is at most one root.

**Verdict: UPHELD, POLISH-class.** The argument is valid; it is also unnecessary. The three facts it
uses — $p'(P)<0$, $P+\bar m-A\ge\bar m\ge0$ by h.12, and $p(P)-1<0$ — hold at **every** $P\ge A$,
not only at roots, so $\varrho'(P)<0$ on all of $[A,\infty)$ and a strictly decreasing function has
at most one zero there. The global statement is shorter, strictly stronger, and is what P1-R43's
implicit-function appendix wants anyway.

### DRAFTED REPAIR — P1-R50 (Step 7(iii), replacing `:441-448`). Grade: **WORDING-ONLY.** Strictly strengthening; nothing is weakened.

> (iii) *The root is unique.* $\varrho$ is differentiable with
> $\varrho'(P)=p'(P)\bigl(P+\bar m-A\bigr)+p(P)-1$, and
> $p'(P)=-\phi\bigl((P+K+\bar m-\bar S)/\sigma_\xi\bigr)/\sigma_\xi<0$. Take any $P\ge A$. Then
> $P+\bar m-A\ge\bar m\ge0$ by h.12, so the first term is $\le0$; and $p(P)-1<0$ since $p<1$ (Step
> 4). Hence
> $$\varrho'(P)<0\qquad\text{for every }P\ge A,$$
> not merely at roots. By (i) every root lies in $[A,\infty)$, and a strictly decreasing function has
> at most one zero on an interval, so there is at most one root; (ii) supplies existence, so the root
> is unique. *Replaced 2026-08-29 (**P1-R50**, polish-pass finding F15): the pre-repair argument
> established $\varrho'<0$ at roots only and then ran a two-adjacent-roots contradiction. The global
> statement follows from the same three facts, is shorter, and is the form Step 8's
> implicit-function argument consumes.*

---

## Finding F16 — the perturbation's starting index, and $\varphi_s$. UPHELD. POLISH-class.

**What the proof says.** `proofs/P1_proof.md:472-474`: "at stage $n$ every signal type plays every
plan $j\in\mathcal J$ with weight at least $1/n$"; and `:496`:

> $$w_n(j\mid s)=(1-t_n)\,\mathbf 1\{j=j_k(s)\}+\tfrac{t_n}{J},\qquad t_n:=\tfrac Jn\downarrow0,$$

**Verdict: UPHELD, POLISH-class.** For $n<J$ the display is not a probability distribution:
$t_n=J/n>1$, so $1-t_n<0$ and $w_n(j_k(s)\mid s)<0$; the step's own "$J$ plans each with weight at
least $1/n$" is infeasible for the same reason ($J/n>1$). No inference in the file depends on small
$n$ — everything is "for all large $n$" or a limit — so nothing is wrong downstream; the sequence
simply needs its index range said. **The $\varphi_s$ half is upheld separately and is a card §8 rule
3 matter:** $\varphi_s$ is used at `:500, 504, 505, 511, 529, 530, 532, 535, 537`, is not a card §4
symbol, and has **no row of its own** in the NOTATION DELTA — it is named only inside the gloss of
the $t_n$/$Z_n$/$\Lambda$ row (`:1231`), which rule 3 ("list every symbol used that is not in §4")
does not satisfy.

### DRAFTED REPAIR — P1-R51, two sites. Grade: **WORDING-ONLY.**

**(a) Step 9(b), replacing `:495-497`.**

> For integers $n\ge J$ write
> $$w_n(j\mid s)=(1-t_n)\,\mathbf 1\{j=j_k(s)\}+\tfrac{t_n}{J},\qquad t_n:=\tfrac Jn\in(0,1],\quad
> t_n\downarrow0,$$
> for the stage-$n$ mixing weight: the weights are nonnegative, sum to one, and give every plan at
> least $t_n/J=1/n>0$, which is Step 9's own parameterisation of the perturbation. (For $n<J$ the
> display is not a probability distribution — $t_n>1$ makes $1-t_n<0$ — and Step 9's "every plan with
> weight at least $1/n$" is infeasible there, since $J/n>1$; the limit is unaffected by dropping
> finitely many initial indices.) *(Index range stated 2026-08-29, **P1-R51**, polish-pass finding
> F16.)*

**(b) NOTATION DELTA gains a row.**

> | $\varphi_s$ | density of the Gaussian signal $s$ (Step 9(b)) | distinct from $\phi$, the unit-normal density, which appears only inside $p'(P)$ at Step 7(iii), and from $\Phi_s$, this table's signal c.d.f. Declared 2026-08-29 (**P1-R51**): the symbol was in use at Step 9(b) and named only inside the $t_n$ row's gloss, which card §8 rule 3 does not satisfy |

---

## Finding F17 — Step 12's opening. UPHELD. POLISH-class.

**What the proof says**, `proofs/P1_proof.md:661-666`, is a five-line italic block of repair
chronology ("*Restructured 2026-08-25 (round 2) on pass-1 finding 1 and pass-2 R16–R17. The
pre-round-2 argument ran the deviation back to date-0 optimality…*") standing where the step's
quantifier and strategy belong.

**Verdict: UPHELD, POLISH-class.** The mathematical content of the block — that §3(ii) binds at
every flagged pair including non-selected ones, and that the argument therefore cannot run through
date-0 optimality — is load-bearing and is buried in a provenance note. The chronology itself is
already carried by P1-R17 (`:1441`) and by the round-2 FAIL narrative (`:1418-1431`).

### DRAFTED REPAIR — P1-R52 (Step 12, replacing `:661-666`). Grade: **WORDING-ONLY.**

> The requirement to be discharged is card §3(ii) at **every** flagged pair, including pairs the
> date-0 cutoff policy does not select — h.11 defines an action set $\mathcal Q_j(s)$ at every
> flagged pair, and a date-0 deviation to a non-selected plan that flags creates a genuine round-2
> information set carrying §3(ii). The argument therefore **cannot** run through date-0 optimality:
> at a non-selected pair there is none to appeal to, and that is exactly what lets the argument below
> reach those nodes. Fix an arbitrary flagged pair $(j,s)$, with no assumption that $j=j_k(s)$, and
> let $j'$ range over the menu elements generating h.11's action set $\mathcal Q_j(s)$.
> *(Restructured 2026-08-25, round 2 — **P1-R17**, on pass-1 finding 1 and pass-2 R16–R17; the
> chronology is in the repair table at the foot of this file. Opening rewritten 2026-08-29,
> **P1-R52**, polish-pass finding F17, to lead with the quantifier and the strategy rather than the
> repair history. Parts (a)–(d) are unchanged.)*

---

## Finding F18 — Step 20's threshold equivalence. UPHELD. POLISH-class.

**What the proof says**, `proofs/P1_proof.md:999-1001`:

> Writing $s_F(k^\star)$ for the infimum of that upper interval,
> $\Omega=1-\Phi_s\bigl(s_F(k^\star)\bigr)$ with $\Phi_s$ the signal c.d.f., and h.8 is equivalent to
> $s_F(k^\star)$ being finite and strictly above $-\infty$.

**Verdict: UPHELD, POLISH-class.** "finite **and** strictly above $-\infty$" is redundant on its
face, and the two degenerate flagged sets the file itself names in WHERE IT FAILS 6 — empty at
$\tau>\bar b$, full on an all-Voice crossing menu — are left without a stated value for $s_F$.
GPT's tightening is right. **One collision must be marked**, and GPT does not mark it: Step 13
already fixes $\inf\emptyset:=\overline s$ for a different object, so Step 20's $\pm\infty$
conventions have to be declared Step-20-local or the two codes read as one.

### DRAFTED REPAIR — P1-R53 (Step 20, replacing `:999-1001`). Grade: **WORDING-ONLY.**

> Writing $s_F(k^\star)$ for the infimum of that upper interval, and adopting **for this step alone**
> the extended-real conventions
> $$\inf\emptyset:=+\infty,\qquad \inf\mathbb R:=-\infty$$
> — **not** Step 13's $\inf\emptyset:=\overline s$, which totalises $\mathcal T_i$ inside the bracket
> and is a different convention for a different object —
> $$\Omega\;=\;1-\Phi_s\bigl(s_F(k^\star)\bigr)\;\in[0,1],$$
> with endpoint values $\Omega=0$ at $s_F=+\infty$ (nothing flags — WHERE IT FAILS 6's $\tau>\bar b$)
> and $\Omega=1$ at $s_F=-\infty$ (everything flags — the symmetric case named in the same item).
> Hence
> $$0<\Omega<1\quad\Longleftrightarrow\quad s_F(k^\star)\in\mathbb R,$$
> which is h.8 restated as a single signal threshold. *(Tightened 2026-08-29, **P1-R53**, polish-pass
> finding F18: the pre-repair sentence read "h.8 is equivalent to $s_F(k^\star)$ being finite and
> strictly above $-\infty$", redundant on its face, and left the two degenerate flagged sets without
> a stated $s_F$.)*

---

## Finding F19 — Step 14's four-action derivation. NARROWED. UNCHECKED.

**What the proof says**, `proofs/P1_proof.md:833-839`: the four-action bracket derivation, with
affine payoffs, ordered slopes and a strictly decreasing engagement cost, attributed to "the frozen
manuscript" without a locator.

**What GPT claims** (response `:804-813`): the paste supplies none of the payoff formulas, slope
coefficients, intercept bounds, cost function, existence argument for each adjacent indifference, or
the source passage, so the first paragraph of Step 14 cannot be verified from the stipulated record.

**Verdict: NARROWED. UNCHECKED, non-blocking, and it reduces to agreement with the file's own
disclaimer.** GPT demonstrates no defect; it reports that a paragraph is unverifiable from the
materials it was given. That is what the lane calls UNCHECKED, and it never blocks. Three scopings:

1. The material GPT wants is the **frozen manuscript**, which the prompt's scope fence 3 places
   outside this pass ("the other seven proofs and the numerical implementation are other threads'
   objects"); the paste was the complete proof file, so nothing was withheld in error.
2. The file already disclaims exactly this. NOT CLAIMED 10 (`:1302-1304`): "That the frozen
   manuscript's four-action results transfer to the $J$-plan menu. Step 14 borrows an *argument
   shape* from it and says explicitly that the shape needs a payoff form the card does not impose."
3. GPT itself records the paragraph as non-load-bearing (`:815`), and Step 14's conclusion — the
   bracket is **assumed** at the card's level of generality — does not rest on it. That conclusion
   is, however, exactly the clause F5/P1-R40-A now asks to be stated in the form Step 13 consumes.

**No repair drafted.** A locator for the frozen-manuscript passage would be a courtesy and is
recorded as optional in the repair queue's no-action table, not as a finding.

---

# REPAIR QUEUE

Repairs number from **P1-R36**; `P1-R35` is the file's ceiling. **All texts are CONJECTURE-grade
edit text.** Nothing below is applied by this audit.

## (i) Wording-grade batch — landable in one quiet window, no re-gating implied

| ID | Finding | Site(s) in `proofs/P1_proof.md` | What |
|---|---|---|---|
| **P1-R36** | F1 | Step 2, `:297-301` | filing-stake display re-indexed to the filing date; extension off the flagged set named |
| **P1-R37** | F2 | Step 3 heading `:306`, Step 3 `:311-315`, Step 6 opening `:387-388` | flagged image: empty-or-uncountable dichotomy replaces the categorical "not finite" |
| **P1-R38** | F3 | Step 9(b) `:514-518` and `:531-537` | the two-case limit displayed; the unconditional plan-uniform characterisation withdrawn |
| **P1-R39** | F4 | Step 9(c) `:561-562`, NOTATION DELTA `:1233`, **dated annotation** on P1-R30 `:1474` | $k$-independent reference belief $(\mu_v,1)$ replaces $(\mu_v,\Pr(a{=}1))$ |
| **P1-R41** | F6 (+F14's continuity half) | Step 15 opening `:854-866`, Step 5 closing `:378-383` | the underived cutoff continuity de-asserted; h.6 named as the assumption at that point |
| **P1-R42** | F7 | Step 1 `:271-274` | $\Theta$ declared as this file's ordered box on h.6's bracket; GPT's weakening refused |
| **P1-R45** | F10 | Step 15(ii) `:880-884`, boxed sentence `:886-890` | robust sign-threshold condition replaces empty interior; continuity argument written out |
| **P1-R46** | F11 | Step 18 `:956-965` | Kakutani conclusion withdrawn as unestablished; remark scoped |
| **P1-R47** | F12 | h.12 `:167-169` | card-status corrected; [ADDITION] retired |
| **P1-R48** | F13 | Step 4 `:340` | Gaussian law cited to h.17-d, independence to h.1 |
| **P1-R49** | F14 | Step 5(b) `:374-375`, NOT CLAIMED 12 | dated supersession: the card has pinned the reading |
| **P1-R50** | F15 | Step 7(iii) `:441-448` | global $\varrho'<0$ on $[A,\infty)$ replaces the adjacent-root argument |
| **P1-R51** | F16 | Step 9(b) `:495-497`, NOTATION DELTA | index range $n\ge J$; $\varphi_s$ declared |
| **P1-R52** | F17 | Step 12 opening `:661-666` | leads with the quantifier and strategy; provenance pointer kept |
| **P1-R53** | F18 | Step 20 `:999-1001` | Step-20-local $\pm\infty$ conventions; the equivalence stated |

**Ordering note.** P1-R45 is drafted consistently with P1-R40-A and should land after the F5 route is
chosen; if Package B is taken instead, P1-R45's corner paragraph needs a matching rewrite. P1-R38's
grade carries a declared alternative (see **F3**, "Why the grade is wording"): if the orchestrator
judges the $\Lambda_k>0$ display to be new content, P1-R38 moves to group (ii).

## (ii) Gated batch — statement-preserving, but new derivation; needs re-gating before the row rests on it

| ID | Finding | Site(s) | What | Dependency |
|---|---|---|---|---|
| **P1-R43** | F8 | Step 8 (append), Step 5(a) `:360` | joint continuity of the inner root in $(\hat v,\pi)$ by IFT + Step 7's global uniqueness | uses P1-R50's sharpened $\varrho'<0$ on $[A,\infty)$ |
| **P1-R44** | F9 | Step 9(b) `:537-539`, NOTATION DELTA | $\pi_n$ defined, shown to converge in both branches; prices converge by joint continuity | **depends on P1-R43** |

Neither adds a hypothesis, changes a step conclusion, or touches the parameterisation. Both are
consumed by Step 17(iv). A proof carrying them needs an adversarial proof-read and a statements-only
re-derivation before the P1 row rests on the amended text.

## (iii) Gated and antecedent-touching — **Austin's call, not the orchestrator's**

| ID | Finding | What | Reach |
|---|---|---|---|
| **P1-R40-A** | F5 | state that h.6's bracket clause delivers, for every $k\in\Theta$ and every adjacent pair, a **nonempty** up-set with infimum in $[\underline s,\overline s]$; retire the corner code as a totalisation; add NOT CLAIMED 16 | Step 13, Step 14, NOT CLAIMED; **plus a drafted card-side clause on the P1 row's "A6 is read" sentence, not applied** |
| **P1-R40-B** | F5 | sentinel re-parameterisation, coded identically in Step 1, $\mathcal T$, the price system and card §3(i) | sketched only; edits **card §3**, needs a strictly enlarged bracket, and cannot express the lower sentinel under the current $j_k$ |

## (iv) No-action items, with reasons

| Item | Reason |
|---|---|
| GPT's F7 closing sentence ("Membership in the possibly proper polytope $\Theta$ is the self-map content of h.6") | would convert Step 13's **derived** self-map conclusion into an assumption; the lane does not weaken a step conclusion, and on the ordered box the derivation is sound |
| GPT's F10 permission for $c_i(k)=\overline s$ to encode "an upper plan never preferred within the bracket" | re-admits precisely the corner encoding its own F5 shows is not representation-faithful |
| GPT's F14 instruction "Delete NOT CLAIMED 12" | landed record is superseded with a dated amendment, never deleted; P1-R49(b) does that instead |
| GPT's F19 request for the four-action payoff formulas | frozen manuscript is outside the pass's scope fence 3; NOT CLAIMED 10 already disclaims the transfer. *Optional courtesy, not a finding:* a locator at Step 14 for the manuscript passage |
| The card's A6-note pointer to Step 18 as "$t$-constrained game + Kakutani + $t\downarrow0$" | **flagged, not resolved** (F11); a card-side check for the orchestrator, no edit drafted |
| Any numerical check | none is requested by this audit and none is executed; no `t2_*` script results from it |
| `LABEL_LEDGER.md` | **no entry results from this audit** |

---

# Demotion question

**YES. One upheld WRONG-class finding survives that the drafted repairs CANNOT close at wording
grade: F5.** The P1 row/label question therefore goes to Austin.

**F5, stated plainly.** Under the printed cutoff coding, Step 13's representation sentence is false.
Step 1 codes $j_k(s)=1+\#\{i:k_i\le s\}$, so the corner value $k_i=\overline s$ does not retire plan
$i+1$ — it activates it at every $s\ge\overline s$. On a card-legal menu with a dominated top plan,
$j^\star(\cdot;k)\equiv1$ at every $k$, so $\{s:j^\star\ge2\}=\emptyset$,
$\mathcal T_1\equiv\overline s$, $\mathcal T$ is constant (h.6's continuity and self-map halves both
hold), Brouwer returns $k^\star=\overline s$, and $j_{k^\star}(s)=2$ on $[\overline s,\infty)$, a set
of strictly positive Gaussian probability with $\overline s$ finite. Step 17(i)'s
"$\Phi_s$-almost surely" consistency clause and Step 19's "$\Omega$ is unaffected" parenthetical are
both false there, and neither choice of equilibrium plan map repairs it: $j^\star$ leaves card
§3(iii)–(v) computed against a different population on a positive-probability set, and $j_{k^\star}$
breaks §3(ii) on the same set. The proof's own tangency counterexample at Step 13 constructs this
configuration inside h.3, two paragraphs above the sentence that mishandles it.

**Why the repairs cannot close it at wording grade.** The one defence — reading h.6's bracket clause
as asserting that every adjacent-pair best-response cutoff **exists** and lies in the bracket — is
available and is what Step 14 proves in its four-action specialisation. But adopting it removes
configurations that the proof text (Step 13's corner gloss, Step 16's reading of h.6) and the card's
own P1 row ("A6 is read … **under a named tie-break-and-corner selection**") currently present as
covered. That is a change in the antecedent's content, not a correction of prose, and it is drafted
as **P1-R40-A** together with a card-side clause on the P1 row. The alternative, **P1-R40-B**, edits
the equilibrium parameterisation and card §3 itself. Both are SUBSTANCE; both need the two-pass gate
(adversarial proof-read plus statements-only re-derivation) run over the amended proof; and the
choice between them, together with the card edit either implies, is Austin's.

**A second, distinct category, which must not be collapsed into the first.** F8 and F9 are also
upheld WRONG-class, and their repairs (P1-R43, P1-R44) are also SUBSTANCE — they supply new
derivations that Steps 5(a), 9(b) and 17(iv) consume. But they are **statement-preserving**: routine
implicit-function and dominated-convergence work using only h.12, Step 4's reduction and Step 7's own
facts, adding no hypothesis and changing no conclusion. They say the proof text is incomplete, not
that the statement is unestablished. They require re-gating of the amended proof; they do not by
themselves put the row's statement in question. Reporting them as label-threatening, or reporting F5
as merely needing re-gating, would misreport in opposite directions.

**Why each remaining upheld WRONG-class finding does close at wording grade.**

- **F1** — the corrected display is a transcription of the step's own definition three lines above;
  the step's conclusion (Borel) is unchanged and nothing downstream reads the display.
- **F2** — no step consumes nonemptiness or uncountability of the flagged image; Step 6 constructs on
  the image and is vacuous when it is empty, which WHERE IT FAILS 6 already records.
- **F3** — the $\Lambda_k=0$ display is already in the step's own case split verbatim, the
  $\Lambda_k>0$ display is the elementary evaluation of a limit the step already proves exists and
  its own closing sentence already calls Bayes, and every downstream consumer plus card §5's A6 note
  already reads it the corrected way. *(Declared alternative: if the orchestrator judges the display
  to be new content, P1-R38 moves to the gated batch with P1-R43/R44 — still statement-preserving,
  still not label-threatening.)*
- **F4** — one "for definiteness" instantiation is exchanged for another the step's own text already
  declares equivalent-in-kind; the convention's role, the inner-root property and NOT CLAIMED 13 are
  unchanged.
- **F6** — the repair deletes an assertion the file never derives and the card records as measured
  false; the route the proof actually takes (h.6 asserting $\mathcal T$-continuity at Step 16) is
  untouched, so the conditional Brouwer argument runs exactly as printed.
- **F10** — (i) and (ii) are named candidate sufficient conditions that no step consumes; h.6 is
  assumed outright, so repairing the optional route touches nothing the theorem rests on.
- **F11** — Step 18 is outside the claim by its own heading and by NOT CLAIMED 3, and no step reads
  it; withdrawing an unestablished conclusion from a remark changes nothing the theorem rests on.
- **F13** — the computation is unchanged; only the hypothesis pointer moves from h.1 to h.17-d.

**What this audit does not do.** It does not move the P1 label, does not write to
`LABEL_LEDGER.md`, does not edit `MODEL_CARD.md`, the mirrors, or `proofs/P1_proof.md`, and does not
run any numerical check. GPT's OVERALL JUDGMENT (`:872`) writes that "without the first one, the P1
row should not remain PROVED on the strength of this proof." I uphold the **finding** it rests on and
record its reach precisely; the **label call** is Austin's, on the record above.

---

## Where I differ from GPT's own classification

| # | GPT's class | My class | Why |
|---|---|---|---|
| F7 | GAP | consequence misattributed; premise upheld as a citation nit | the proof defines $\Theta$ as the ordered box in the same sentence, so Step 13's derivation is sound; GPT's fix would weaken a derived conclusion |
| F8, F9 | GAP | **WRONG-class** | a load-bearing inference that is not supported is not a stylistic gap; both are consumed by Step 17(iv) |
| F10 | GAP | **WRONG-class**, on a condition no step consumes | the boxed conclusion runs on a strict sign change that (ii) does not supply — the tangency case satisfies h.3 and (ii) and has no crossing |
| F11 | GAP | **WRONG-class in a non-load-bearing remark** (UPHELD-WITH-SCOPE) | the assertions fail card §8 rule 7; the remark is outside the claim, so the reach is nil |
| F12, F14 | POLISH | **STALE** | record staleness against a stamp the file was not written at, not roughness; both are already recorded elsewhere in the file or on the card |
| F13 | POLISH | **WRONG-class (citation)** | a citation that does not support what it is cited for; non-blocking, but not a matter of style |
| F19 | UNCLEAR | **UNCHECKED** | GPT demonstrates no defect; the material it wants is outside the pass's scope fence 3 and NOT CLAIMED 10 already disclaims the transfer |
| F5 | WRONG, "no statement-preserving prose-only repair" | **UPHELD**, with a sharper witness and a defence disposed of | GPT's witness is right; the constant-$\mathcal T$ version isolates the failure in h.6's **bracket** half with continuity and self-mapping intact, and the file's own tangency counterexample instantiates it |

**Recorded once, in GPT's favour.** Every quotation in the response resolves against the proof at the
text it is anchored to; no finding in this pass is MISCITED by misquotation. Against the 2026-08-28
re-review, where three of fourteen were, that is a clean pass on localisation, and every finding was
actionable at the step level the prompt required.
