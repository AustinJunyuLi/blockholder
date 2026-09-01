"""v4 two-round blockholder disclosure model — numerical implementation.

Built to ``research/model_v4/impl_design.md`` (ticket 25 / T2e), including the
binding rulings of that document's section 13.  The seven ``t2_*`` check
scripts are ticket 28's deliverable and are *not* part of this package; this
package exposes the API they need.

Module order mirrors design section 11:

    params   ParamsV4, tolerances, grids
    menu     plans, Gamma, b*(s), breakpoints, legal clock, a7_certificate
    pooled   history enumeration, int8 exponent array, inner price, P_d^P, R, J
    flagged  b* inversion, flagged posterior, P^F, p, M_F
    premium  pi, h, Omega, omega_a, M_P, Delta^act, S_P, the chord
    policy   Policy, evaluate() [pure in the policy], sweeps
    solver   outer map T(k), damped iteration, brentq bracketing, multi-start
    smoke    the two section-11 smoke items
"""
