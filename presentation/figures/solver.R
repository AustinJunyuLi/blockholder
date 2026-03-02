# ============================================================================
# solver.R -- Full equilibrium solver for the Exit-Voice-Takeover model
#
# R port of the Python numerical package (params.py, model.py, solver.py).
# Implements all equilibrium computation needed for standalone figure generation.
# ============================================================================

library(stats)  # for dnorm, pnorm, qnorm, uniroot

# -- Tolerance constants (match Python params.py) ---------------------------
TOL_PROB     <- 1e-10
TOL_CONVERGE <- 1e-6
TOL_RESIDUAL <- 5e-3
TOL_REGION   <- 1e-4

# -- Default parameters (match Python ModelParams) ---------------------------
default_params <- function() {
  p <- list(
    mu        = 1.0,
    sigma_v   = 0.5,
    sigma_eps = 0.5,
    kappa     = 0.5,
    C0        = 0.12,
    chi       = 0.5,
    rho       = 0.9,
    Delta     = 0.25,
    m0        = 0.10,
    m1        = 0.30,
    S_bar     = 1.44,
    K         = 0.15,
    sigma_xi  = 0.40,
    delta     = 0.95
  )
  # Derived quantities
  p$sigma_s     <- sqrt(p$sigma_v^2 + p$sigma_eps^2)
  p$beta        <- p$sigma_v^2 / (p$sigma_v^2 + p$sigma_eps^2)
  p$m_tilde     <- p$m0 + p$rho * (p$m1 - p$m0)
  p$Delta_tilde <- p$rho * p$Delta
  p
}

# Helper: update params and recompute derived quantities
update_params <- function(params, ...) {
  updates <- list(...)
  for (nm in names(updates)) {
    params[[nm]] <- updates[[nm]]
  }
  params$sigma_s     <- sqrt(params$sigma_v^2 + params$sigma_eps^2)
  params$beta        <- params$sigma_v^2 / (params$sigma_v^2 + params$sigma_eps^2)
  params$m_tilde     <- params$m0 + params$rho * (params$m1 - params$m0)
  params$Delta_tilde <- params$rho * params$Delta
  params
}

# ── Section 2: Information Structure ────────────────────────────────────────

engagement_cost <- function(s, params) {
  z <- (s - params$mu) / params$sigma_s
  params$C0 * exp(-params$chi * z)
}

v_hat <- function(s, params) {
  params$mu + params$beta * (s - params$mu)
}

# ── Section 3: Market Microstructure ────────────────────────────────────────

compute_action_probabilities <- function(k1, k0, kD, params) {
  alpha1 <- (k1 - params$mu) / params$sigma_s
  alpha0 <- (k0 - params$mu) / params$sigma_s
  alphaD <- (kD - params$mu) / params$sigma_s

  omega_E <- pnorm(alpha1)
  omega_H <- pnorm(alpha0) - pnorm(alpha1)
  omega_Q <- pnorm(alphaD) - pnorm(alpha0)
  omega_P <- 1 - pnorm(alphaD)

  list(
    omega_E = max(0, omega_E),
    omega_H = max(0, omega_H),
    omega_Q = max(0, omega_Q),
    omega_P = max(0, omega_P)
  )
}

compute_conditional_means <- function(k1, k0, kD, params) {
  alpha1 <- (k1 - params$mu) / params$sigma_s
  alpha0 <- (k0 - params$mu) / params$sigma_s
  alphaD <- (kD - params$mu) / params$sigma_s

  lambda_L <- function(alpha) {
    cdf_val <- pnorm(alpha)
    if (cdf_val < TOL_PROB) return(-alpha)
    dnorm(alpha) / cdf_val
  }

  lambda_U <- function(alpha) {
    ccdf <- 1 - pnorm(alpha)
    if (ccdf < TOL_PROB) return(alpha)
    dnorm(alpha) / ccdf
  }

  mu_E <- params$mu - params$beta * params$sigma_s * lambda_L(alpha1)

  denom_H <- pnorm(alpha0) - pnorm(alpha1)
  if (denom_H > TOL_PROB) {
    mu_H <- params$mu + params$beta * params$sigma_s *
      (dnorm(alpha1) - dnorm(alpha0)) / denom_H
  } else {
    mu_H <- params$mu + params$beta * (k0 + k1) / 2 - params$beta * params$mu
  }

  denom_Q <- pnorm(alphaD) - pnorm(alpha0)
  if (denom_Q > TOL_PROB) {
    mu_Q <- params$mu + params$beta * params$sigma_s *
      (dnorm(alpha0) - dnorm(alphaD)) / denom_Q
  } else {
    mu_Q <- params$mu + params$beta * (kD + k0) / 2 - params$beta * params$mu
  }

  mu_P <- params$mu + params$beta * params$sigma_s * lambda_U(alphaD)

  list(mu_E = mu_E, mu_H = mu_H, mu_Q = mu_Q, mu_P = mu_P)
}

compute_posteriors <- function(omega_E, omega_H, omega_Q, omega_P, kappa) {
  p0 <- 1 - kappa
  p1 <- kappa / 2

  posteriors <- list()

  # Disclosed states: D=1 => pi = 1
  for (X in 0:2) {
    posteriors[[paste(X, 1, sep = ",")]] <- 1.0
  }

  # Non-disclosed: D=0
  posteriors[["-2,0"]] <- 0.0

  # X = 1, D = 0: q=0 with z=+1
  denom_1 <- omega_H + omega_Q
  posteriors[["1,0"]] <- if (denom_1 > TOL_PROB) omega_Q / denom_1 else 0.0

  # X = -1, D = 0
  denom_m1 <- (omega_H + omega_Q) * p1 + omega_E * p0
  posteriors[["-1,0"]] <- if (denom_m1 > TOL_PROB) omega_Q * p1 / denom_m1 else 0.0

  # X = 0, D = 0
  denom_0 <- (omega_H + omega_Q) * p0 + omega_E * p1
  posteriors[["0,0"]] <- if (denom_0 > TOL_PROB) omega_Q * p0 / denom_0 else 0.0

  posteriors
}

compute_E_v_given_XD <- function(X, D, omega_E, omega_H, omega_Q, omega_P,
                                  mu_E, mu_H, mu_Q, mu_P, kappa) {
  p0 <- 1 - kappa
  p1 <- kappa / 2

  if (D == 1) return(mu_P)

  if (X == -2) return(mu_E)

  if (X == 1) {
    denom <- omega_H + omega_Q
    if (denom < TOL_PROB) return((mu_H + mu_Q) / 2)
    return((omega_H * mu_H + omega_Q * mu_Q) / denom)
  }

  if (X == -1) {
    denom <- (omega_H + omega_Q) * p1 + omega_E * p0
    if (denom < TOL_PROB) return((mu_H + mu_Q + mu_E) / 3)
    return(((omega_H * mu_H + omega_Q * mu_Q) * p1 + omega_E * mu_E * p0) / denom)
  }

  # X == 0
  denom <- (omega_H + omega_Q) * p0 + omega_E * p1
  if (denom < TOL_PROB) return((mu_H + mu_Q + mu_E) / 3)
  ((omega_H * mu_H + omega_Q * mu_Q) * p0 + omega_E * mu_E * p1) / denom
}

bid_probability <- function(P, m_XD, params) {
  T_val <- (m_XD + params$K - params$S_bar + P) / params$sigma_xi
  1 - pnorm(T_val)
}

solve_price_fixed_point <- function(E_v_XD, pi_XD, params,
                                     max_iter = 100, tol = 1e-8) {
  V_hat <- E_v_XD + params$Delta_tilde * pi_XD
  m_XD  <- params$m0 + (params$m_tilde - params$m0) * pi_XD

  P <- params$delta * V_hat

  for (i in seq_len(max_iter)) {
    p <- bid_probability(P, m_XD, params)
    P_new <- params$delta * ((1 - p) * V_hat + p * (P + m_XD))

    if (abs(P_new - P) < tol) return(P_new)
    P <- P_new
  }
  P
}

compute_equilibrium_prices <- function(k1, k0, kD, params) {
  omegas <- compute_action_probabilities(k1, k0, kD, params)
  means  <- compute_conditional_means(k1, k0, kD, params)
  posts  <- compute_posteriors(omegas$omega_E, omegas$omega_H,
                               omegas$omega_Q, omegas$omega_P, params$kappa)

  prices <- list()
  # All possible (X, D) pairs
  for (X in -2:2) {
    for (D in 0:1) {
      if (D == 1 && X < 0) next
      key <- paste(X, D, sep = ",")
      if (is.null(posts[[key]])) next

      pi_XD <- posts[[key]]
      E_v_XD <- compute_E_v_given_XD(X, D,
                                      omegas$omega_E, omegas$omega_H,
                                      omegas$omega_Q, omegas$omega_P,
                                      means$mu_E, means$mu_H,
                                      means$mu_Q, means$mu_P,
                                      params$kappa)
      prices[[key]] <- solve_price_fixed_point(E_v_XD, pi_XD, params)
    }
  }
  prices
}

# ── Blockholder payoff ─────────────────────────────────────────────────────

compute_expected_payoff <- function(action, s, prices, posteriors, params) {
  p0 <- 1 - params$kappa
  p1 <- params$kappa / 2
  v_post <- v_hat(s, params)

  get_price <- function(X, D) {
    key <- paste(X, D, sep = ",")
    val <- prices[[key]]
    if (is.null(val)) params$mu else val
  }

  get_m_XD <- function(X, D) {
    key <- paste(X, D, sep = ",")
    pi <- posteriors[[key]]
    if (is.null(pi)) pi <- 0
    params$m0 + (params$m_tilde - params$m0) * pi
  }

  if (action == "EXIT") {
    payoff <- 0
    for (z_info in list(c(-1, p1), c(0, p0), c(1, p1))) {
      z  <- z_info[1]; pz <- z_info[2]
      X  <- -1 + z
      P  <- get_price(X, 0)
      payoff <- payoff + pz * P
    }
    return(payoff)
  }

  if (action == "HOLD") {
    payoff <- 0
    for (z_info in list(c(-1, p1), c(0, p0), c(1, p1))) {
      z  <- z_info[1]; pz <- z_info[2]
      X  <- z
      P  <- get_price(X, 0)
      m_XD <- get_m_XD(X, 0)
      p_bid <- bid_probability(P, m_XD, params)
      expected_terminal <- p_bid * (P + params$m0) + (1 - p_bid) * v_post
      payoff <- payoff + pz * params$delta * expected_terminal
    }
    return(payoff)
  }

  if (action == "QUIET") {
    C <- engagement_cost(s, params)
    payoff <- -C
    for (z_info in list(c(-1, p1), c(0, p0), c(1, p1))) {
      z  <- z_info[1]; pz <- z_info[2]
      X  <- z
      P  <- get_price(X, 0)
      m_XD <- get_m_XD(X, 0)
      p_bid <- bid_probability(P, m_XD, params)
      expected_terminal <- p_bid * (P + params$m_tilde) +
                           (1 - p_bid) * (v_post + params$Delta_tilde)
      payoff <- payoff + pz * params$delta * expected_terminal
    }
    return(payoff)
  }

  if (action == "PUBLIC") {
    C <- engagement_cost(s, params)
    payoff <- -C
    for (z_info in list(c(-1, p1), c(0, p0), c(1, p1))) {
      z  <- z_info[1]; pz <- z_info[2]
      X  <- 1 + z
      P  <- get_price(X, 1)
      m_XD <- params$m_tilde
      p_bid <- bid_probability(P, m_XD, params)
      trading_cf <- -P
      expected_terminal <- p_bid * 2 * (P + params$m_tilde) +
                           (1 - p_bid) * 2 * (v_post + params$Delta_tilde)
      payoff <- payoff + pz * (trading_cf + params$delta * expected_terminal)
    }
    return(payoff)
  }

  stop(paste("Unknown action:", action))
}

# ── Section 4: Minority Gains ──────────────────────────────────────────────

compute_minority_gains <- function(k1, k0, kD, params) {
  omegas <- compute_action_probabilities(k1, k0, kD, params)
  posts  <- compute_posteriors(omegas$omega_E, omegas$omega_H,
                               omegas$omega_Q, omegas$omega_P, params$kappa)
  prices <- compute_equilibrium_prices(k1, k0, kD, params)

  p0 <- 1 - params$kappa
  p1 <- params$kappa / 2

  total_gains    <- 0
  base_gains     <- 0
  activism_gains <- 0

  actions <- list(
    list(action = "EXIT",   q = -1, a = 0, omega = omegas$omega_E),
    list(action = "HOLD",   q =  0, a = 0, omega = omegas$omega_H),
    list(action = "QUIET",  q =  0, a = 1, omega = omegas$omega_Q),
    list(action = "PUBLIC", q =  1, a = 1, omega = omegas$omega_P)
  )

  for (act_info in actions) {
    if (act_info$omega < TOL_PROB) next
    D <- if (act_info$action == "PUBLIC") 1 else 0

    for (z_info in list(c(-1, p1), c(0, p0), c(1, p1))) {
      z  <- z_info[1]; pz <- z_info[2]
      X  <- act_info$q + z
      key <- paste(X, D, sep = ",")

      P <- prices[[key]]
      if (is.null(P)) next
      pi_XD <- posts[[key]]
      if (is.null(pi_XD)) pi_XD <- 0
      m_XD <- params$m0 + (params$m_tilde - params$m0) * pi_XD
      p_bid <- bid_probability(P, m_XD, params)
      m_realized <- if (act_info$a == 1) params$m_tilde else params$m0

      weight <- act_info$omega * pz
      total_gains    <- total_gains + weight * p_bid * m_realized
      base_gains     <- base_gains + weight * p_bid * params$m0
      activism_gains <- activism_gains + weight * p_bid * (m_realized - params$m0)
    }
  }

  list(total = total_gains, base = base_gains, activism = activism_gains)
}

# ── Equilibrium Solver ─────────────────────────────────────────────────────

solve_equilibrium <- function(params, k1_init = NULL, k0_init = NULL,
                               kD_init = NULL, max_iter = 60,
                               tol = TOL_CONVERGE) {
  s_min <- params$mu - 6 * params$sigma_s
  s_max <- params$mu + 6 * params$sigma_s

  k1 <- if (is.null(k1_init)) params$mu - 1.0 * params$sigma_s else k1_init
  k0 <- if (is.null(k0_init)) params$mu - 0.5 * params$sigma_s else k0_init
  kD <- if (is.null(kD_init)) params$mu + 0.5 * params$sigma_s else kD_init

  s_grid <- seq(s_min, s_max, length.out = 61)

  bracket_root <- function(func, low = NULL, high = NULL, target = NULL) {
    grid <- s_grid
    if (!is.null(low))  grid <- grid[grid >= low]
    if (!is.null(high)) grid <- grid[grid <= high]
    if (length(grid) < 2) return(NULL)

    vals <- sapply(grid, func)
    if (any(is.na(vals) | !is.finite(vals))) return(NULL)

    brackets <- list()
    for (i in seq_len(length(grid) - 1)) {
      if (vals[i] == 0) {
        brackets[[length(brackets) + 1]] <- c(grid[i], grid[i])
      } else if (vals[i] * vals[i + 1] < 0) {
        brackets[[length(brackets) + 1]] <- c(grid[i], grid[i + 1])
      }
    }

    if (length(brackets) == 0) return(NULL)
    if (is.null(target) || !is.finite(target)) return(brackets[[1]])

    # Prefer bracket closest to current iterate
    dists <- sapply(brackets, function(ab) abs((ab[1] + ab[2]) / 2 - target))
    brackets[[which.min(dists)]]
  }

  for (iter in seq_len(max_iter)) {
    k0 <- max(k0, k1)
    kD <- max(kD, k0)

    omegas <- compute_action_probabilities(k1, k0, kD, params)
    posteriors <- compute_posteriors(omegas$omega_E, omegas$omega_H,
                                     omegas$omega_Q, omegas$omega_P,
                                     params$kappa)
    prices <- compute_equilibrium_prices(k1, k0, kD, params)

    U <- function(action, s) {
      compute_expected_payoff(action, s, prices, posteriors, params)
    }

    # k1: Exit vs best q=0 option
    diff_E_best0 <- function(s) {
      U("EXIT", s) - max(U("HOLD", s), U("QUIET", s))
    }

    bracket <- bracket_root(diff_E_best0, target = k1)
    if (is.null(bracket)) {
      k1_new <- if (diff_E_best0(s_min) >= 0) s_max else s_min
    } else if (bracket[1] == bracket[2]) {
      k1_new <- bracket[1]
    } else {
      res <- tryCatch(
        uniroot(diff_E_best0, interval = bracket, tol = 1e-8),
        error = function(e) NULL
      )
      k1_new <- if (!is.null(res)) res$root else (bracket[1] + bracket[2]) / 2
    }

    # k0: Hold vs Quiet Voice
    diff_H_Q <- function(s) U("HOLD", s) - U("QUIET", s)

    eps <- 1e-4
    s0 <- min(k1_new + eps, s_max)
    bracket <- bracket_root(diff_H_Q, low = k1_new, high = s_max, target = k0)
    if (is.null(bracket)) {
      k0_new <- if (diff_H_Q(s0) <= 0) k1_new else s_max
    } else if (bracket[1] == bracket[2]) {
      k0_new <- bracket[1]
    } else {
      res <- tryCatch(
        uniroot(diff_H_Q, interval = bracket, tol = 1e-8),
        error = function(e) NULL
      )
      k0_new <- if (!is.null(res)) res$root else (bracket[1] + bracket[2]) / 2
    }

    # kD: (Quiet or Hold) vs Public Voice
    lower_action <- if (k0_new < s_max - 1e-6) "QUIET" else "HOLD"
    diff_lower_P <- function(s) U(lower_action, s) - U("PUBLIC", s)

    start <- min(k0_new, s_max)
    bracket <- bracket_root(diff_lower_P, low = start, high = s_max, target = kD)
    if (is.null(bracket)) {
      kD_new <- if (diff_lower_P(start + eps) <= 0) start else s_max
    } else if (bracket[1] == bracket[2]) {
      kD_new <- bracket[1]
    } else {
      res <- tryCatch(
        uniroot(diff_lower_P, interval = bracket, tol = 1e-8),
        error = function(e) NULL
      )
      kD_new <- if (!is.null(res)) res$root else (bracket[1] + bracket[2]) / 2
    }

    # Enforce ordering
    k0_new <- max(k0_new, k1_new)
    kD_new <- max(kD_new, k0_new)

    # Check convergence
    if (abs(k1_new - k1) < tol &&
        abs(k0_new - k0) < tol &&
        abs(kD_new - kD) < tol) {
      return(list(k1 = k1_new, k0 = k0_new, kD = kD_new))
    }

    # Damped update
    alpha <- 0.75
    k1 <- alpha * k1_new + (1 - alpha) * k1
    k0 <- alpha * k0_new + (1 - alpha) * k0
    kD <- alpha * kD_new + (1 - alpha) * kD
  }

  list(k1 = k1, k0 = k0, kD = kD)
}

# ── Multi-start solver ─────────────────────────────────────────────────────

equilibrium_residual <- function(k1, k0, kD, params) {
  omegas <- compute_action_probabilities(k1, k0, kD, params)
  posts  <- compute_posteriors(omegas$omega_E, omegas$omega_H,
                               omegas$omega_Q, omegas$omega_P, params$kappa)
  prices <- compute_equilibrium_prices(k1, k0, kD, params)

  U <- function(action, s) {
    compute_expected_payoff(action, s, prices, posts, params)
  }

  s_min <- params$mu - 6 * params$sigma_s
  s_max <- params$mu + 6 * params$sigma_s

  diff1 <- U("EXIT", k1) - max(U("HOLD", k1), U("QUIET", k1))
  r1 <- if (k1 <= s_min + TOL_REGION || k1 >= s_max - TOL_REGION) {
    if (k1 >= s_max - TOL_REGION) max(0, -diff1) else max(0, diff1)
  } else {
    abs(diff1)
  }

  if ((k0 - k1) > TOL_REGION) {
    r0 <- abs(U("HOLD", k0) - U("QUIET", k0))
  } else {
    s_test <- min(k1 + TOL_REGION, s_max)
    r0 <- max(0, U("HOLD", s_test) - U("QUIET", s_test))
  }

  lower <- if (k0 < s_max - TOL_REGION) "QUIET" else "HOLD"
  if (kD >= s_max - TOL_REGION) {
    rD <- max(0, U("PUBLIC", s_max) - U(lower, s_max))
  } else {
    rD <- abs(U(lower, kD) - U("PUBLIC", kD))
  }

  max(r1, r0, rD)
}

solve_valid <- function(params, prev_cutoffs = NULL,
                         residual_tol = TOL_RESIDUAL) {
  attempt <- function(k1i, k0i, kDi) {
    cut <- solve_equilibrium(params, k1_init = k1i, k0_init = k0i,
                              kD_init = kDi, max_iter = 90)
    res <- equilibrium_residual(cut$k1, cut$k0, cut$kD, params)
    list(cut = cut, res = res)
  }

  if (!is.null(prev_cutoffs)) {
    result <- attempt(prev_cutoffs$k1, prev_cutoffs$k0, prev_cutoffs$kD)
    if (is.finite(result$res) && result$res <= residual_tol) {
      return(result)
    }
    # Try collapsed hold
    alt <- attempt(prev_cutoffs$k1, prev_cutoffs$k1, prev_cutoffs$kD)
    if (alt$res < result$res) result <- alt
    return(result)
  }

  # Generic starts
  starts <- list(
    list(k1 = params$mu - 1.0 * params$sigma_s,
         k0 = params$mu - 1.0 * params$sigma_s,
         kD = params$mu + 0.5 * params$sigma_s),
    list(k1 = params$mu - 1.0 * params$sigma_s,
         k0 = params$mu - 0.5 * params$sigma_s,
         kD = params$mu + 0.5 * params$sigma_s)
  )

  best <- list(cut = NULL, res = Inf)
  for (st in starts) {
    result <- attempt(st$k1, st$k0, st$kD)
    if (result$res < best$res) best <- result
  }
  best
}

# ── Series over kappa ──────────────────────────────────────────────────────

compute_series_over_kappa <- function(base_params, kappa_values) {
  n <- length(kappa_values)
  k1_vals <- rep(NA_real_, n)
  k0_vals <- rep(NA_real_, n)
  kD_vals <- rep(NA_real_, n)
  Delta_min_vals <- rep(NA_real_, n)
  base_vals <- rep(NA_real_, n)
  act_vals  <- rep(NA_real_, n)

  prev_cutoffs <- NULL

  for (i in seq_len(n)) {
    kap <- kappa_values[i]
    p <- update_params(base_params, kappa = kap)

    result <- tryCatch({
      if (!is.null(prev_cutoffs)) {
        cut <- solve_equilibrium(p, k1_init = prev_cutoffs$k1,
                                  k0_init = prev_cutoffs$k0,
                                  kD_init = prev_cutoffs$kD)
      } else {
        cut <- solve_equilibrium(p)
      }
      gains <- compute_minority_gains(cut$k1, cut$k0, cut$kD, p)
      list(cut = cut, gains = gains)
    }, error = function(e) NULL)

    if (!is.null(result)) {
      prev_cutoffs <- result$cut
      k1_vals[i] <- result$cut$k1
      k0_vals[i] <- result$cut$k0
      kD_vals[i] <- result$cut$kD
      Delta_min_vals[i] <- result$gains$total
      base_vals[i] <- result$gains$base
      act_vals[i]  <- result$gains$activism
    } else {
      prev_cutoffs <- NULL
    }
  }

  data.frame(
    kappa     = kappa_values,
    k1        = k1_vals,
    k0        = k0_vals,
    kD        = kD_vals,
    Delta_min = Delta_min_vals,
    base      = base_vals,
    act       = act_vals
  )
}

# ── Counterfactual: No Disclosure ──────────────────────────────────────────

compute_posteriors_no_disclosure <- function(omega_E, omega_H, omega_Q,
                                             omega_P, kappa) {
  p0 <- 1 - kappa
  p1 <- kappa / 2

  prob_z <- function(z) {
    if (z == 0) p0 else if (z %in% c(-1, 1)) p1 else 0
  }

  actions <- list(
    list(q = -1, a = 0, omega = omega_E),
    list(q =  0, a = 0, omega = omega_H),
    list(q =  0, a = 1, omega = omega_Q),
    list(q =  1, a = 1, omega = omega_P)
  )

  posteriors <- list()
  for (X in -2:2) {
    denom <- 0; numer <- 0
    for (act in actions) {
      pz <- prob_z(X - act$q)
      if (pz == 0 || act$omega < TOL_PROB) next
      w <- act$omega * pz
      denom <- denom + w
      if (act$a == 1) numer <- numer + w
    }
    posteriors[[as.character(X)]] <- if (denom > TOL_PROB) numer / denom else 0
  }
  posteriors
}

compute_E_v_given_X_no_disclosure <- function(X, omega_E, omega_H, omega_Q,
                                               omega_P, mu_E, mu_H, mu_Q,
                                               mu_P, kappa) {
  p0 <- 1 - kappa
  p1 <- kappa / 2

  prob_z <- function(z) {
    if (z == 0) p0 else if (z %in% c(-1, 1)) p1 else 0
  }

  actions <- list(
    list(q = -1, mu = mu_E, omega = omega_E),
    list(q =  0, mu = mu_H, omega = omega_H),
    list(q =  0, mu = mu_Q, omega = omega_Q),
    list(q =  1, mu = mu_P, omega = omega_P)
  )

  denom <- 0; numer <- 0
  for (act in actions) {
    pz <- prob_z(X - act$q)
    if (pz == 0 || act$omega < TOL_PROB) next
    w <- act$omega * pz
    denom <- denom + w
    numer <- numer + w * act$mu
  }

  if (denom < TOL_PROB) return(mean(c(mu_E, mu_H, mu_Q, mu_P)))
  numer / denom
}

compute_minority_gains_no_disclosure <- function(k1, k0, kD, params) {
  omegas <- compute_action_probabilities(k1, k0, kD, params)
  means  <- compute_conditional_means(k1, k0, kD, params)
  post_X <- compute_posteriors_no_disclosure(omegas$omega_E, omegas$omega_H,
                                              omegas$omega_Q, omegas$omega_P,
                                              params$kappa)

  prices_X <- list()
  for (X in -2:2) {
    pi_X <- post_X[[as.character(X)]]
    if (is.null(pi_X)) pi_X <- 0
    E_v_X <- compute_E_v_given_X_no_disclosure(X,
                                                omegas$omega_E, omegas$omega_H,
                                                omegas$omega_Q, omegas$omega_P,
                                                means$mu_E, means$mu_H,
                                                means$mu_Q, means$mu_P,
                                                params$kappa)
    prices_X[[as.character(X)]] <- solve_price_fixed_point(E_v_X, pi_X, params)
  }

  p0 <- 1 - params$kappa
  p1 <- params$kappa / 2

  total_gains <- 0; base_gains <- 0; activism_gains <- 0

  actions <- list(
    list(action = "EXIT",   q = -1, a = 0, omega = omegas$omega_E),
    list(action = "HOLD",   q =  0, a = 0, omega = omegas$omega_H),
    list(action = "QUIET",  q =  0, a = 1, omega = omegas$omega_Q),
    list(action = "PUBLIC", q =  1, a = 1, omega = omegas$omega_P)
  )

  for (act_info in actions) {
    if (act_info$omega < TOL_PROB) next
    m_realized <- if (act_info$a == 1) params$m_tilde else params$m0

    for (z_info in list(c(-1, p1), c(0, p0), c(1, p1))) {
      z <- z_info[1]; pz <- z_info[2]
      X <- act_info$q + z
      P <- prices_X[[as.character(X)]]
      if (is.null(P)) next
      pi_X <- post_X[[as.character(X)]]
      if (is.null(pi_X)) pi_X <- 0
      m_X <- params$m0 + (params$m_tilde - params$m0) * pi_X
      p_bid <- bid_probability(P, m_X, params)
      weight <- act_info$omega * pz
      total_gains    <- total_gains + weight * p_bid * m_realized
      base_gains     <- base_gains + weight * p_bid * params$m0
      activism_gains <- activism_gains + weight * p_bid * (m_realized - params$m0)
    }
  }

  list(total = total_gains, base = base_gains, activism = activism_gains)
}

# ── Counterfactual: Noisy Rumor ────────────────────────────────────────────

compute_posteriors_noisy_rumor <- function(omega_E, omega_H, omega_Q,
                                            omega_P, kappa, eta_1, eta_0) {
  p0 <- 1 - kappa
  p1 <- kappa / 2
  posteriors <- list()

  # Disclosed branch
  for (X in 0:2) {
    for (R in 0:1) {
      posteriors[[paste(X, 1, R, sep = ",")]] <- 1.0
    }
  }
  for (R in 0:1) posteriors[[paste(-2, 0, R, sep = ",")]] <- 0.0

  # X=1, D=0
  d_r1 <- omega_Q * eta_1 + omega_H * eta_0
  d_r0 <- omega_Q * (1 - eta_1) + omega_H * (1 - eta_0)
  posteriors[["1,0,1"]] <- if (d_r1 > TOL_PROB) omega_Q * eta_1 / d_r1 else 0
  posteriors[["1,0,0"]] <- if (d_r0 > TOL_PROB) omega_Q * (1 - eta_1) / d_r0 else 0

  # X=-1, D=0
  d_m1_r1 <- (omega_H * p1 + omega_E * p0) * eta_0 + omega_Q * p1 * eta_1
  d_m1_r0 <- (omega_H * p1 + omega_E * p0) * (1 - eta_0) + omega_Q * p1 * (1 - eta_1)
  posteriors[["-1,0,1"]] <- if (d_m1_r1 > TOL_PROB) omega_Q * p1 * eta_1 / d_m1_r1 else 0
  posteriors[["-1,0,0"]] <- if (d_m1_r0 > TOL_PROB) omega_Q * p1 * (1 - eta_1) / d_m1_r0 else 0

  # X=0, D=0
  d_0_r1 <- (omega_H * p0 + omega_E * p1) * eta_0 + omega_Q * p0 * eta_1
  d_0_r0 <- (omega_H * p0 + omega_E * p1) * (1 - eta_0) + omega_Q * p0 * (1 - eta_1)
  posteriors[["0,0,1"]] <- if (d_0_r1 > TOL_PROB) omega_Q * p0 * eta_1 / d_0_r1 else 0
  posteriors[["0,0,0"]] <- if (d_0_r0 > TOL_PROB) omega_Q * p0 * (1 - eta_1) / d_0_r0 else 0

  posteriors
}

compute_minority_gains_noisy_rumor <- function(k1, k0, kD, params,
                                                eta_1, eta_0) {
  omegas <- compute_action_probabilities(k1, k0, kD, params)
  means  <- compute_conditional_means(k1, k0, kD, params)
  post_R <- compute_posteriors_noisy_rumor(omegas$omega_E, omegas$omega_H,
                                            omegas$omega_Q, omegas$omega_P,
                                            params$kappa, eta_1, eta_0)

  # Compute prices P(X, D, R)
  prices_R <- list()
  p0 <- 1 - params$kappa; p1 <- params$kappa / 2

  for (X in -2:2) {
    for (D in 0:1) {
      if (D == 1 && X < 0) next
      for (R in 0:1) {
        key <- paste(X, D, R, sep = ",")
        pi_XDR <- post_R[[key]]
        if (is.null(pi_XDR)) next

        if (D == 1) {
          E_v <- means$mu_P
        } else if (X == -2) {
          E_v <- means$mu_E
        } else if (X == 1) {
          wH <- omegas$omega_H * (if (R == 1) eta_0 else 1 - eta_0)
          wQ <- omegas$omega_Q * (if (R == 1) eta_1 else 1 - eta_1)
          d <- wH + wQ
          E_v <- if (d > TOL_PROB) (wH * means$mu_H + wQ * means$mu_Q) / d else
                   (means$mu_H + means$mu_Q) / 2
        } else if (X == -1) {
          wE <- omegas$omega_E * p0 * (if (R == 1) eta_0 else 1 - eta_0)
          wH <- omegas$omega_H * p1 * (if (R == 1) eta_0 else 1 - eta_0)
          wQ <- omegas$omega_Q * p1 * (if (R == 1) eta_1 else 1 - eta_1)
          d <- wE + wH + wQ
          E_v <- if (d > TOL_PROB) (wE * means$mu_E + wH * means$mu_H + wQ * means$mu_Q) / d else
                   (means$mu_E + means$mu_H + means$mu_Q) / 3
        } else {
          wE <- omegas$omega_E * p1 * (if (R == 1) eta_0 else 1 - eta_0)
          wH <- omegas$omega_H * p0 * (if (R == 1) eta_0 else 1 - eta_0)
          wQ <- omegas$omega_Q * p0 * (if (R == 1) eta_1 else 1 - eta_1)
          d <- wE + wH + wQ
          E_v <- if (d > TOL_PROB) (wE * means$mu_E + wH * means$mu_H + wQ * means$mu_Q) / d else
                   (means$mu_E + means$mu_H + means$mu_Q) / 3
        }
        prices_R[[key]] <- solve_price_fixed_point(E_v, pi_XDR, params)
      }
    }
  }

  # Enumerate gains
  total_gains <- 0; base_gains <- 0; activism_gains <- 0

  actions <- list(
    list(q = -1, a = 0, omega = omegas$omega_E, D = 0),
    list(q =  0, a = 0, omega = omegas$omega_H, D = 0),
    list(q =  0, a = 1, omega = omegas$omega_Q, D = 0),
    list(q =  1, a = 1, omega = omegas$omega_P, D = 1)
  )

  for (act in actions) {
    if (act$omega < TOL_PROB) next
    m_realized <- if (act$a == 1) params$m_tilde else params$m0

    for (z_info in list(c(-1, p1), c(0, p0), c(1, p1))) {
      z <- z_info[1]; pz <- z_info[2]
      X <- act$q + z

      for (R in 0:1) {
        if (act$D == 1) {
          pR <- if (R == 1) 1.0 else 0.0
        } else {
          pR <- if (act$a == 1) {
            if (R == 1) eta_1 else 1 - eta_1
          } else {
            if (R == 1) eta_0 else 1 - eta_0
          }
        }
        if (pR < TOL_PROB) next

        key <- paste(X, act$D, R, sep = ",")
        P <- prices_R[[key]]
        if (is.null(P)) next
        pi_XDR <- post_R[[key]]
        if (is.null(pi_XDR)) pi_XDR <- 0
        m_XDR <- params$m0 + (params$m_tilde - params$m0) * pi_XDR
        p_bid <- bid_probability(P, m_XDR, params)

        weight <- act$omega * pz * pR
        total_gains    <- total_gains + weight * p_bid * m_realized
        base_gains     <- base_gains + weight * p_bid * params$m0
        activism_gains <- activism_gains + weight * p_bid * (m_realized - params$m0)
      }
    }
  }

  list(total = total_gains, base = base_gains, activism = activism_gains)
}

# ── Welfare ────────────────────────────────────────────────────────────────

compute_bidder_surplus_state <- function(P, m_XD, params) {
  T_val <- (m_XD + params$K - params$S_bar + P) / params$sigma_xi
  params$sigma_xi * dnorm(T_val) - T_val * params$sigma_xi * (1 - pnorm(T_val))
}

compute_welfare <- function(k1, k0, kD, params) {
  omegas <- compute_action_probabilities(k1, k0, kD, params)
  posts  <- compute_posteriors(omegas$omega_E, omegas$omega_H,
                               omegas$omega_Q, omegas$omega_P, params$kappa)
  prices <- compute_equilibrium_prices(k1, k0, kD, params)

  p0 <- 1 - params$kappa
  p1 <- params$kappa / 2

  W_bid <- 0
  actions <- list(
    list(q = -1, D = 0, omega = omegas$omega_E),
    list(q =  0, D = 0, omega = omegas$omega_H),
    list(q =  0, D = 0, omega = omegas$omega_Q),
    list(q =  1, D = 1, omega = omegas$omega_P)
  )

  for (act in actions) {
    if (act$omega < TOL_PROB) next
    for (z_info in list(c(-1, p1), c(0, p0), c(1, p1))) {
      z <- z_info[1]; pz <- z_info[2]
      X <- act$q + z
      key <- paste(X, act$D, sep = ",")
      P <- prices[[key]]
      if (is.null(P)) next
      pi_XD <- posts[[key]]
      if (is.null(pi_XD)) pi_XD <- 0
      m_XD <- params$m0 + (params$m_tilde - params$m0) * pi_XD
      surplus <- compute_bidder_surplus_state(P, m_XD, params)
      W_bid <- W_bid + act$omega * pz * surplus
    }
  }

  gains <- compute_minority_gains(k1, k0, kD, params)
  W_min <- gains$total
  W_tot <- W_min + W_bid

  list(W_min = W_min, W_bid = W_bid, W_tot = W_tot)
}

# ── Disclosure attenuation series ──────────────────────────────────────────

compute_disclosure_attenuation_series <- function(base_params, kappa_values,
                                                    k1_ref, k0_ref, kD_ref) {
  n <- length(kappa_values)
  act_disc    <- rep(NA_real_, n)
  act_no_disc <- rep(NA_real_, n)

  for (i in seq_len(n)) {
    p <- update_params(base_params, kappa = kappa_values[i])
    g1 <- compute_minority_gains(k1_ref, k0_ref, kD_ref, p)
    g2 <- compute_minority_gains_no_disclosure(k1_ref, k0_ref, kD_ref, p)
    act_disc[i]    <- g1$activism
    act_no_disc[i] <- g2$activism
  }

  data.frame(
    kappa            = kappa_values,
    act_disclosure   = act_disc,
    act_no_disclosure = act_no_disc
  )
}

# ── Sensitivity sweep ─────────────────────────────────────────────────────

compute_sensitivity <- function(base_params, param_name, param_values,
                                 kappa_values, replace_fn = NULL) {
  results <- data.frame()

  for (pval in param_values) {
    prev_cutoffs <- NULL
    for (kap in kappa_values) {
      p <- if (!is.null(replace_fn)) {
        replace_fn(base_params, kap, pval)
      } else {
        args <- list(kappa = kap)
        args[[param_name]] <- pval
        do.call(update_params, c(list(base_params), args))
      }

      result <- tryCatch({
        sv <- solve_valid(p, prev_cutoffs)
        if (is.null(sv$cut) || !is.finite(sv$res) || sv$res > TOL_RESIDUAL) {
          prev_cutoffs <- NULL
          NA_real_
        } else {
          prev_cutoffs <- sv$cut
          compute_minority_gains(sv$cut$k1, sv$cut$k0, sv$cut$kD, p)$total
        }
      }, error = function(e) { prev_cutoffs <<- NULL; NA_real_ })

      results <- rbind(results, data.frame(
        kappa     = kap,
        param_val = pval,
        Delta_min = result
      ))
    }
  }

  names(results)[2] <- param_name
  results
}

# ── Noisy rumor series ─────────────────────────────────────────────────────

compute_noisy_rumor_series <- function(base_params, kappa_values,
                                        rumor_configs) {
  results <- data.frame()

  for (cfg in rumor_configs) {
    eta_1 <- cfg$eta_1
    eta_0 <- cfg$eta_0
    label <- cfg$label
    prev_cutoffs <- NULL

    for (kap in kappa_values) {
      p <- update_params(base_params, kappa = kap)

      result <- tryCatch({
        sv <- solve_valid(p, prev_cutoffs)
        if (is.null(sv$cut) || !is.finite(sv$res) || sv$res > TOL_RESIDUAL) {
          prev_cutoffs <<- NULL
          NA_real_
        } else {
          prev_cutoffs <<- sv$cut
          g <- compute_minority_gains_noisy_rumor(
            sv$cut$k1, sv$cut$k0, sv$cut$kD, p, eta_1, eta_0)
          g$total
        }
      }, error = function(e) { prev_cutoffs <<- NULL; NA_real_ })

      results <- rbind(results, data.frame(
        kappa     = kap,
        eta_1     = eta_1,
        eta_0     = eta_0,
        label     = label,
        Delta_min = result,
        stringsAsFactors = FALSE
      ))
    }
  }
  results
}

# ── Welfare series ─────────────────────────────────────────────────────────

compute_welfare_series <- function(base_params, kappa_values) {
  n <- length(kappa_values)
  W_min_vals <- rep(NA_real_, n)
  W_bid_vals <- rep(NA_real_, n)
  W_tot_vals <- rep(NA_real_, n)

  prev_cutoffs <- NULL
  for (i in seq_len(n)) {
    p <- update_params(base_params, kappa = kappa_values[i])

    result <- tryCatch({
      sv <- solve_valid(p, prev_cutoffs)
      if (is.null(sv$cut) || !is.finite(sv$res) || sv$res > TOL_RESIDUAL) {
        prev_cutoffs <<- NULL
        NULL
      } else {
        prev_cutoffs <<- sv$cut
        compute_welfare(sv$cut$k1, sv$cut$k0, sv$cut$kD, p)
      }
    }, error = function(e) { prev_cutoffs <<- NULL; NULL })

    if (!is.null(result)) {
      W_min_vals[i] <- result$W_min
      W_bid_vals[i] <- result$W_bid
      W_tot_vals[i] <- result$W_tot
    }
  }

  data.frame(
    kappa = kappa_values,
    W_min = W_min_vals,
    W_bid = W_bid_vals,
    W_tot = W_tot_vals
  )
}

message("solver.R loaded successfully")
