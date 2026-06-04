# D2 Welfare/Planner -- Verified Numerics (attempt 4)

Solver: numerical.solver.solve_valid(params, prev_cutoffs, residual_tol=1e-5).
Welfare: numerical.model.welfare_components -> WelfareComponents(W_B, Dmin, W_bid, total).
Env: /tmp/blk_venv (numpy 2.4.6, scipy 1.17.1). PYTHONPATH=repo.
model.py PATCHED: np.trapz -> np.trapezoid + compat shim (2 call sites; backup .bak_trapz).

## W = W_B + Delta^min + W_bid  (EXACT identity; diff = 0.0e+00 at every kappa)
kappa  W_B        Dmin       W_bid      W_total
0.05   1.339862   0.066968   0.005913   1.412743
0.25   1.346060   0.077015   0.005469   1.428545   (table point; see fine grid)
0.50   1.346060   0.077015   0.005469   1.428545
0.59   1.332947   0.077558   0.005474   1.415779   (Dmin PEAK)
0.75   1.330998   0.074917   0.005371   1.411286
0.95   1.341363   0.067814   0.005854   1.415030

## Fine grid (46 pts, warm-started, residual-filtered <1e-3):
argmax W_total : kappa* = 0.290, W = 1.444248
argmax Dmin    : kappa-dagger = 0.590, Dmin = 0.077558
argmax W_B     : kappa = 0.290, W_B = 1.367268
argmax W_bid   : kappa = 0.050, W_bid = 0.005913

## HEADLINE WEDGE: kappa* (0.29) < kappa-dagger (0.59).  SIGN(kappa*-kappa-dagger) = NEGATIVE.
Mechanism: at kappa-dagger, Dmin'=0 but W_B'<0 dominates (blockholder trading profit
peaks at lower liquidity than minority value creation), and W_bid' is small. So W'(kappa-dagger)<0,
pushing the total-welfare optimum BELOW the minority optimum.

## Endpoint symmetry (limit): Dmin(0.05)=0.066968 ~ Dmin(0.95)=0.067814. Both > 0 (NOT ->0).
Refutes the OLD "value creation collapses at extremes" claim.

## Disclosure wedge probe (partial; (k1,k0) fixed, price FP NOT re-solved -> freezes channel G):
kappa=0.20: kD_eq=2.5034, kD*_W=1.50 (< kD_eq) -> underdisclosure corroborated (channel (i) only).
kD*_Dmin (2.01) != kD*_W (1.50): minority-cutoff != surplus-cutoff; ordering needs (ii).

## Citations verified in draft_v2.tex thebibliography:
levit2024 = Levit, Malenko, Maug (2024), "Trading and Shareholder Democracy," JF 79(1):257-304.
grossman1980 = Grossman & Hart (1980), "Takeover Bids, the Free-Rider Problem...", Bell J Econ 11(1):42-64.

## Host-draft lines to EXCISE/REPLACE (false OLD mechanism):
- line 728: "value creation collapses, and Delta^min -> 0 ... hump ... intrinsic"
- lines 753-757 (Conclusion): "disclosure incentive collapses ... value creation muted"
- line 1416 (fig caption): "inherent hump ... at both extremes value creation falls away"

## Host labels that EXIST (use only these / section names): prop:posteriors,
prop:equilibrium-characterization, prop:cutoffs, sec:payoffs, sec:welfare.
NONE of eq:pricing, eq:bid-prob, eq:price-fp, eq:k1, eq:kD, fn:pv-delta exist.
