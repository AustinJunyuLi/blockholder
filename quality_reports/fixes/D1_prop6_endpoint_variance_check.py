#!/usr/bin/env python3
"""
Self-contained numerical/symbolic verification for D1_prop6_endpoint_variance.tex
(Lemma A endpoint symmetry; Lemma B kappa-invariant conditional mean and strictly
U-shaped conditional variance at fixed masses).

Run with any python that has sympy + numpy.  No dependence on the paper's solver:
this verifies the CLOSED-FORM algebra of the manuscript proof at FIXED masses
(A,B,Q) = (omega_E, omega_H+omega_Q, omega_Q).  Equilibrium (moving-mass)
behaviour is verified separately by the phase-0 driver and is NOT claimed here.

Notation:  a = omega_E, b = omega_H + omega_Q, c = omega_Q,  0 < c <= b,  a,b > 0.
           x = kappa/2 in [0, 1/2],  y = 1 - kappa = 1 - 2x.
           P(D=0) = a + b  (fixed masses).
"""
import sympy as sp

a, b, c, x = sp.symbols('a b c x', positive=True)
y = 1 - 2*x

# ---- Realized D=0 atoms (Bayes), masses and posteriors --------------------
P_m2 = a*x;            pi_m2 = sp.Integer(0)
P_m1 = a*y + b*x;      pi_m1 = c*x/(a*y + b*x)
P_0  = a*x + b*y;      pi_0  = c*y/(a*x + b*y)
P_p1 = b*x;            pi_p1 = c/b
P = [P_m2, P_m1, P_0, P_p1]
PI = [pi_m2, pi_m1, pi_0, pi_p1]

# total D=0 mass
print("P(D=0) - (a+b) =", sp.simplify(sum(P) - (a+b)))     # expect 0

# ---- First conditional moment: E[pi 1{D=0}] = c (kappa-invariant) ---------
E_pi_ind = sp.simplify(sum(Pj*PIj for Pj, PIj in zip(P, PI)))
print("E[pi*1{D=0}] simplified =", E_pi_ind)                # expect c
print("d/dkappa E[pi*1{D=0}] =", sp.simplify(sp.diff(E_pi_ind, x)))  # expect 0

# ---- Second conditional moment and g(x) = E[pi^2 1{D=0}]/c^2 --------------
E_pi2_ind = sum(Pj*PIj**2 for Pj, PIj in zip(P, PI))
g = sp.simplify(E_pi2_ind/c**2)
g_expected = x**2/(a*y+b*x) + y**2/(a*x+b*y) + x/b
print("g - g_expected =", sp.simplify(g - g_expected))      # expect 0

# ---- Endpoints g(0)=g(1/2)=1/b  =>  E[pi^2 1{D=0}](0)=(1)=c^2/b ----------
print("g(0)   =", sp.simplify(g.subs(x, 0)))                # expect 1/b
print("g(1/2) =", sp.simplify(g.subs(x, sp.Rational(1, 2))))# expect 1/b

# ---- Strict convexity of g in x:  the two fractional pieces ---------------
u = a*y + b*x          # = a + (b-2a)x
w = a*x + b*y          # = b + (a-2b)x
h1 = x**2/u
h2 = y**2/w
# manuscript claim:  h1'' = 2 a^2 / u^3,  h2'' = 2 a^2 / w^3   (both > 0)
print("h1'' - 2a^2/u^3 =", sp.simplify(sp.diff(h1, x, 2) - 2*a**2/u**3))  # 0
print("h2'' - 2a^2/w^3 =", sp.simplify(sp.diff(h2, x, 2) - 2*a**2/w**3))  # 0
# x/b is linear => g'' = 2a^2/u^3 + 2a^2/w^3 > 0  strictly  =>  g strictly convex
gpp = sp.simplify(sp.diff(g, x, 2) - (2*a**2/u**3 + 2*a**2/w**3))
print("g'' - (2a^2/u^3 + 2a^2/w^3) =", gpp)                 # expect 0

# ---- Strict convex + equal endpoints => unique interior minimizer, U-shape
# Variance is an increasing affine transform of g (mean is invariant):
#   Var[pi|D=0] = c^2 g(x)/(a+b) - c^2/(a+b)^2.
# So Var inherits the strict U-shape of g exactly.  Confirm numerically:
import numpy as np
for (aa, bb, cc) in [(0.30, 0.60, 0.30), (0.50, 0.45, 0.20),
                     (0.10, 0.85, 0.40), (0.45, 0.50, 0.50)]:
    gnum = sp.lambdify(x, g.subs({a: aa, b: bb, c: cc}), 'numpy')
    xs = np.linspace(0, 0.5, 20001)
    gv = gnum(xs)
    var = cc**2*gv/(aa+bb) - cc**2/(aa+bb)**2
    imin = int(np.argmin(var))
    # second difference >= 0 everywhere (discrete convexity)
    d2 = np.diff(var, 2)
    print(f"(a,b,c)=({aa},{bb},{cc}): argmin x*={xs[imin]:.4f}, "
          f"endpoints var(0)={var[0]:.6e} var(.5)={var[-1]:.6e} "
          f"min={var[imin]:.6e}  convex(min d2)={d2.min():.3e}")

# ---- Endpoint symmetry of the realized D=0 LAW (Lemma A core) -------------
# At x=0: atoms {0 (mass a), pi_V=c/b (mass b)}.
# At x=1/2 (y=0): pi_m2=0 (mass a/2), pi_m1=c/b... check pi_m1 at x=1/2:
print("pi(-1) at x=1/2 =", sp.simplify(pi_m1.subs(x, sp.Rational(1,2))))   # c/b
print("pi(0)  at x=1/2 =", sp.simplify(pi_0.subs(x, sp.Rational(1,2))))    # 0
print("masses at x=1/2: P(-2),P(-1),P(0),P(+1) =",
      [sp.simplify(Pj.subs(x, sp.Rational(1,2))) for Pj in P])
# => {0: a/2 + a/2 = a, c/b: b/2 + b/2 = b}  identical two-point law to x=0.
