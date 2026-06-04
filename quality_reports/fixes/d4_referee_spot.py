import json, math, random
out = {}
try:
    from scipy.stats import norm
    Phi = lambda x: float(norm.cdf(x))
    out["have_scipy"] = True
except Exception:
    out["have_scipy"] = False
    Phi = lambda x: 0.5*(1.0+math.erf(x/math.sqrt(2.0)))

# A: event coincidence is an algebraic identity. Confirm 0 mismatch + boundary.
Sbar,K,P,sig = 1.44,0.15,1.216,0.40
random.seed(1)
mism=0
for _ in range(300000):
    xi=random.gauss(0.0,sig)*4
    for mbar in (0.0,0.10,0.30,0.375):
        if ((Sbar+xi-K-P-mbar)>=0)!=((xi-(mbar+K-Sbar+P))>=0):
            mism+=1
out["A_mismatch"]=mism
out["A_anchor_p"]={}
for mbar in (0.10,0.30):
    thr=mbar+K-Sbar+P
    out["A_anchor_p"][mbar]=[round(thr,4),round(1-Phi(thr/sig),4)]

# B/C: premia closed form m^R(a)=d(a)+theta*(R-d(a))^+, d(a)=beta0+a*Dt
beta0,Dt,rho=0.10,0.20,0.9
def mR(a,R,th):
    d=beta0+a*Dt; return d+th*max(R-d,0.0)
# pass-through R<=beta0 -> constant pair for any theta
pt=all(abs(mR(0,R,th)-beta0)<1e-12 and abs(mR(1,R,th)-(beta0+Dt))<1e-12
       for R in (-0.5,0.0,0.05,0.10) for th in (0.05,0.2,0.5,0.95))
out["BC_passthrough_constant_pair"]=pt
out["BC_pair"]=[beta0,beta0+Dt]
# band wedges (rem:bg-band) at theta=0.5
out["bands_theta0.5"]={}
for R in (0.05,0.20,0.40,1.0,5.0):
    th=0.5; w=mR(1,R,th)-mR(0,R,th)
    out["bands_theta0.5"][R]=[round(mR(0,R,th),4),round(mR(1,R,th),4),round(w,4),w>0]
# claimed band formulas:
# R<=b0: Dt ; b0<R<=b0+Dt: Dt-theta(R-b0) ; R>b0+Dt: (1-theta)Dt
def band_formula(R,th):
    if R<=beta0: return Dt
    if R<=beta0+Dt: return Dt-th*(R-beta0)
    return (1-th)*Dt
out["band_formula_matches_mR"]=all(
    abs((mR(1,R,th)-mR(0,R,th))-band_formula(R,th))<1e-12
    for R in (0.0,0.12,0.15,0.20,0.30,0.5,2.0) for th in (0.1,0.5,0.9))

# D: rho non-id
def dn(rho,Delta):
    Dt_=rho*Delta; return Dt_, rho*Dt_
w1,a1=dn(0.9,0.20/0.9); w2,a2=dn(0.45,0.20/0.45)
out["D_wedge"]=[round(w1,4),round(w2,4)]
out["D_act_rho2Delta"]=[round(a1,4),round(a2,4)]

# === REFEREE PROBE: TIOLI vs Nash. A pure TIOLI acquirer offers the target
# exactly its reservation d(a) (theta=0 on the rent). The split formula gives
# the target theta>0 of (R-d(a))^+. So outside pass-through the prose ("TIOLI")
# and the formula (Nash, theta>0) DISAGREE. Inside pass-through (R<=d(0)) the
# (.)^+ is 0 so offer=d(a) for ALL theta -> the two agree only where theta is
# irrelevant. Quantify the disagreement.
th=0.5
out["TIOLI_vs_Nash_gap"]={}
for R in (0.05,0.20,0.40,1.0):
    tioli_offer=beta0+0*Dt   # a=0: TIOLI offers reservation d(0)=beta0
    nash_offer=mR(0,R,th)
    out["TIOLI_vs_Nash_gap"][R]=[round(tioli_offer,4),round(nash_offer,4),
                                 round(nash_offer-tioli_offer,4)]

# === REFEREE PROBE: circularity. The "coincidence" is forced because the
# protocol FIXES mbar(a)=m^R(a). Demonstrate it holds for an ARBITRARY rent
# (any constant c), proving the lemma uses nothing about the bargaining:
random.seed(2); arb=0
for _ in range(50000):
    xi=random.gauss(0.0,sig)*4
    for c in (-0.7, 0.123, 0.9):
        if ((Sbar+xi-K-P-c)>=0)!=((xi-(c+K-Sbar+P))>=0): arb+=1
out["circularity_holds_for_any_constant_rent_mismatch"]=arb  # should be 0

print(json.dumps(out,indent=2))
with open("/tmp/d4_spot_result.json","w") as f: json.dump(out,f,indent=2)
