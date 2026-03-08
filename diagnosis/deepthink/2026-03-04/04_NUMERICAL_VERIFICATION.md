# Numerical Verification Data

This file contains independent numerical verification of the issues identified in the GPT Pro audit.
All data was generated from the current codebase (post-Anonymous Accumulation implementation).

## 1. Voice Survival at High κ

The following table shows that voice does NOT collapse at κ→1. Public Voice GROWS while Quiet Voice shrinks.
This directly contradicts Lemma 2's claim that "voice regions collapse (ω_Q+ω_P→0)."

```
kappa    k1      k0      kD      omegaE   omegaH   omegaQ   omegaP     resid
0.050  -0.112   1.236   1.999   0.2904   0.1407   0.2904   0.0789   8.17e-08
0.115   0.087   1.238   1.781   0.2336   0.1571   0.2336   0.1348   9.67e-08
0.180   0.188   1.239   1.651   0.1888   0.1588   0.1888   0.1788   1.59e-07
0.244   0.250   1.241   1.552   0.1490   0.1533   0.1490   0.2176   1.74e-07
0.309   0.291   1.243   1.468   0.1116   0.1450   0.1116   0.2539   2.16e-07
0.374   0.317   1.245   1.393   0.0753   0.1362   0.0753   0.2890   2.79e-07
0.439   0.333   1.248   1.325   0.0399   0.1268   0.0399   0.3231   2.57e-07
0.504   0.400   1.247   1.311   0.0332   0.1378   0.0332   0.3302   7.93e-03
0.633   0.432   1.251   1.251   0.0000   0.1466   0.0000   0.3615   5.17e-08
0.763   0.519   1.251   1.251   0.0000   0.1492   0.0000   0.3615   6.21e-08
0.925   0.615   1.250   1.250   0.0000   0.1516   0.0000   0.3616   5.32e-08
0.990   0.647   1.250   1.250   0.0000   0.1524   0.0000   0.3618   9.30e-08
```

Key observations:
- ω_P INCREASES from 0.079 → 0.362 as κ rises (Public Voice becomes MORE attractive)
- ω_Q DECREASES from 0.290 → 0.000 (Quiet Voice collapses around κ=0.63)
- Total voice (ω_Q+ω_P) stays roughly constant at ~36%
- For κ ≥ 0.63: Quiet Voice collapses (k₀ = k_D), producing a TWO-cutoff equilibrium (Exit/Hold/Public)

## 2. Posterior π(1,0) Does NOT Converge to Unconditional Prior

```
kappa   pi(1,0)   pi(-1,0)   pi(0,0)   uncond_prior   pi(1,0)==uncond?
0.50    0.2954    0.0859     0.2563    0.1835          NO (0.295 ≠ 0.184)
0.70    0.2368    0.0803     0.1724    0.1278          NO (0.237 ≠ 0.128)
0.85    0.2357    0.0892     0.1384    0.1136          NO (0.236 ≠ 0.114)
0.90    0.2269    0.0902     0.1224    0.1062          NO (0.227 ≠ 0.106)
0.95    0.2147    0.0902     0.1058    0.0980          NO (0.215 ≠ 0.098)
0.99    0.0000    0.0000     0.0000    0.0000          N/A (ω_Q=0, trivial)
```

At κ=1 with p₀=p₁=1/3:
- π(-1,0) = ω_Q/(ω_E+ω_H+ω_Q) ← converges to unconditional D=0 prior ✓
- π(0,0) = ω_Q/(ω_E+ω_H+ω_Q) ← same ✓
- π(1,0) = ω_Q/(ω_H+ω_Q) ← DOES NOT converge ✗

The reason: at X=1, D=0, the market KNOWS q=0 (Exit q=-1 cannot produce X=1 with bounded z∈{-1,0,+1}). The noise distribution is irrelevant for this state.

## 3. Δ_min Hump Shape — Decomposition

```
kappa   Delta_min   Delta_base   Delta_act   base_trend   act_trend
0.050   0.00810     0.00545      0.00265     ↑            ↓
0.115   0.00844     0.00605      0.00239     ↑            ↓
0.180   0.00860     0.00644      0.00216     ↑            ↓
0.244   0.00864     0.00673      0.00190     ← PEAK →     ↓
0.309   0.00857     0.00696      0.00161     ↑            ↓
0.374   0.00840     0.00715      0.00125     ↑            ↓
0.439   0.00812     0.00731      0.00081     ↑            ↓
0.633   0.00770     0.00750      0.00020     ↑            ↓
0.925   0.00777     0.00757      0.00020     ↑            ≈flat
0.990   0.00778     0.00758      0.00020     ↑            ≈flat
```

Key findings:
- Δ_base is MONOTONICALLY INCREASING (more noise → more bids → higher base premium)
- Δ_act is MONOTONICALLY DECREASING (more noise → quiet voice shrinks → less inference premium)
- Hump in Δ_min arises from SUM of opposing monotone forces
- Peak at κ ≈ 0.24, amplitude ~10% above endpoints
- Right-endpoint: Δ_min ≈ 0.00778, NOT m₀·P(bid) as Lemma 2 claims
- Δ_act → 0.00020 (positive, NOT zero) — driven by disclosed component at D=1

## 4. Equilibrium at Baseline κ = 0.50

Cutoffs: k₁ = 0.615, k₀ = 1.237, k_D = 1.529
Action probabilities: ω_E = 0.293, ω_H = 0.338, ω_Q = 0.142, ω_P = 0.227
Minority gains: Δ_min = 0.00807, Δ_base = 0.00736, Δ_act = 0.00071

## 5. Why Quiet Voice Collapses but Public Voice Survives

At high κ, noise camouflages all trades (including the buy order q=+1 of Public Voice).
The stealth advantage of Quiet Voice (avoiding disclosure) diminishes because the
Public Voice trade is also increasingly hidden. Meanwhile, Public Voice has the
fundamental advantage of doubling the stake (h=2 vs h=1), amplifying engagement gains.
So the blockholder rationally shifts from quiet to public engagement.

This is CONSISTENT with standard Kyle (1985) microstructure intuition: more noise
INCREASES informed trading rents. The paper's current narrative — "stripped of
ability to extract adverse-selection rents" at high κ — runs against this logic.
