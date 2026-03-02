#!/usr/bin/env Rscript
# ============================================================================
# render_all.R -- Generate all presentation figures (redesigned)
#
# Usage: Rscript render_all.R [--use-csv]
#
# 13 → 10 figures: consolidated sensitivity panels, new decomposition,
# disclosure slopes, annotated hero + welfare.
# ============================================================================

args <- commandArgs(trailingOnly = TRUE)
USE_CSV <- "--use-csv" %in% args

# Resolve paths robustly for Rscript invocation
get_script_dir <- function() {
  cmd_args <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", cmd_args, value = TRUE)
  if (length(file_arg) > 0) {
    return(normalizePath(dirname(sub("^--file=", "", file_arg[1]))))
  }
  getwd()
}

script_dir <- get_script_dir()
output_dir <- script_dir
csv_dir    <- file.path(dirname(dirname(script_dir)), "numerical_output", "data")

message("=== Presentation Figure Generator (Redesigned) ===")
message("Mode: ", if (USE_CSV) "CSV (reading pre-computed data)" else "Solver (computing from scratch)")
message("Output: ", output_dir)
if (USE_CSV) message("CSV dir: ", csv_dir)

# Source dependencies
source(file.path(script_dir, "theme_pres.R"))
if (!USE_CSV) {
  source(file.path(script_dir, "solver.R"))
}

# ── Helper: load or compute data ──────────────────────────────────────────

load_or_compute <- function(csv_name, compute_fn) {
  if (USE_CSV) {
    csv_path <- file.path(csv_dir, csv_name)
    if (file.exists(csv_path)) {
      message("  Reading: ", csv_path)
      return(read_csv(csv_path, show_col_types = FALSE))
    } else {
      message("  CSV not found, computing: ", csv_name)
    }
  }
  compute_fn()
}

# ── Baseline parameters ──────────────────────────────────────────────────

if (!USE_CSV) {
  params <- default_params()
  message("\nSolving baseline equilibrium...")
  baseline <- solve_equilibrium(params)
  message(sprintf("  Cutoffs: k1=%.3f, k0=%.3f, kD=%.3f",
                  baseline$k1, baseline$k0, baseline$kD))
}

# ============================================================================
# FIGURE A: Cutoff Structure (Number Line) — minor: larger annotations
# ============================================================================

message("\n[A] Cutoff structure...")

fig1_data <- load_or_compute("cutoff_regions.csv", function() {
  k1 <- baseline$k1; k0 <- baseline$k0; kD <- baseline$kD
  x_min <- params$mu - 3 * params$sigma_s
  x_max <- max(params$mu + 4 * params$sigma_s, kD + 0.5 * params$sigma_s)
  has_hold <- (k0 - k1) > TOL_REGION

  regions <- data.frame(
    region = character(), xmin = numeric(), xmax = numeric(),
    stringsAsFactors = FALSE
  )
  regions <- rbind(regions, data.frame(region = "Exit", xmin = x_min, xmax = k1))
  if (has_hold) {
    regions <- rbind(regions, data.frame(region = "Hold", xmin = k1, xmax = k0))
    quiet_left <- k0
  } else {
    quiet_left <- k1
  }
  regions <- rbind(regions, data.frame(region = "Quiet Voice", xmin = quiet_left, xmax = kD))
  regions <- rbind(regions, data.frame(region = "Public Voice", xmin = kD, xmax = x_max))
  regions
})

# Get baseline cutoffs for annotation
if (USE_CSV) {
  bc <- read_csv(file.path(csv_dir, "baseline_cutoffs.csv"), show_col_types = FALSE)
  bl_k1 <- bc$k1[1]; bl_k0 <- bc$k0[1]; bl_kD <- bc$kD[1]; bl_mu <- bc$mu[1]
} else {
  bl_k1 <- baseline$k1; bl_k0 <- baseline$k0; bl_kD <- baseline$kD; bl_mu <- params$mu
}

fig1_data$region <- factor(fig1_data$region,
                            levels = c("Exit", "Hold", "Quiet Voice", "Public Voice"))

pA <- ggplot(fig1_data) +
  geom_rect(aes(xmin = xmin, xmax = xmax, ymin = 0, ymax = 1, fill = region),
            alpha = 0.7) +
  scale_fill_manual(values = ACTION_COLORS) +
  geom_vline(xintercept = c(bl_k1, bl_kD), linetype = "dashed", linewidth = 0.5) +
  annotate("text", x = bl_k1, y = 1.08, label = expression(k[1] == k[0]),
           size = 5, hjust = 0.5) +
  annotate("text", x = bl_kD, y = 1.08, label = expression(k[D]),
           size = 5, hjust = 0.5) +
  annotate("text", x = bl_mu, y = -0.12, label = expression(mu),
           size = 5, hjust = 0.5) +
  annotate("point", x = bl_mu, y = 0, shape = 17, size = 3) +
  labs(x = "Signal s", y = NULL, fill = NULL) +
  scale_y_continuous(limits = c(-0.2, 1.2), breaks = NULL) +
  theme_pres() +
  theme(axis.line.y = element_blank(),
        legend.position = "bottom",
        legend.direction = "horizontal")

save_pres_figure(pA, file.path(output_dir, "fig_cutoff_structure.pdf"),
                  width = 7, height = 2.5)

# ============================================================================
# Load baseline series (shared across figures B, C, D, H)
# ============================================================================

baseline_data <- load_or_compute("baseline_series.csv", function() {
  kappa_values <- seq(0.15, 0.85, length.out = 35)
  compute_series_over_kappa(params, kappa_values)
})

# Compute peak location (used across multiple figures)
peak_idx <- which.max(baseline_data$Delta_min)
kappa_dagger <- baseline_data$kappa[peak_idx]
peak_delta   <- baseline_data$Delta_min[peak_idx]
baseline_delta_range <- range(baseline_data$Delta_min, na.rm = TRUE)
baseline_delta_span <- diff(baseline_delta_range)

# ============================================================================
# FIGURE B: Hero Nonmonotone (major redesign)
# ============================================================================

message("[B] Hero nonmonotone (shaded regions, diamond peak)...")

y_range <- baseline_delta_range

pB <- ggplot(baseline_data, aes(x = kappa, y = Delta_min)) +
  # Shaded regions: left of peak (noise cover) and right (inference erosion)
  annotate("rect",
           xmin = min(baseline_data$kappa), xmax = kappa_dagger,
           ymin = y_range[1] - diff(y_range) * 0.02,
           ymax = y_range[2] + diff(y_range) * 0.02,
           fill = "#228833", alpha = 0.06) +
  annotate("rect",
           xmin = kappa_dagger, xmax = max(baseline_data$kappa),
           ymin = y_range[1] - diff(y_range) * 0.02,
           ymax = y_range[2] + diff(y_range) * 0.02,
           fill = "#cc6677", alpha = 0.06) +
  # Region labels
  annotate("text",
           x = (min(baseline_data$kappa) + kappa_dagger) / 2,
           y = y_range[1] + diff(y_range) * 0.08,
           label = "Noise cover \u2191", size = 3.5, colour = "#228833",
           fontface = "italic", family = "serif") +
  annotate("text",
           x = (kappa_dagger + max(baseline_data$kappa)) / 2,
           y = y_range[1] + diff(y_range) * 0.08,
           label = "Inference erosion \u2191", size = 3.5, colour = "#cc6677",
           fontface = "italic", family = "serif") +
  # Main curve (thicker, no points)
  geom_line(colour = "#4477aa", linewidth = 1.5) +
  # Peak diamond + kappa dagger annotation
  geom_vline(xintercept = kappa_dagger, linetype = "dashed",
             colour = "#228833", linewidth = 0.5, alpha = 0.7) +
  annotate("point", x = kappa_dagger, y = peak_delta,
           shape = 18, size = 4, colour = "#228833") +
  annotate("text", x = kappa_dagger + 0.01,
           y = y_range[1] + 0.10 * baseline_delta_span,
           label = expression(kappa^"\u2020"),
           size = 4.5, hjust = 0, vjust = 0.4, colour = "#228833", family = "serif") +
  labs(x = TeX("Liquidity $\\kappa$"),
       y = TeX("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$")) +
  theme_pres()

save_pres_figure(pB, file.path(output_dir, "fig_nonmonotone.pdf"))

# ============================================================================
# FIGURE C: Decomposition (new core figure — 3 lines)
# ============================================================================

message("[C] Decomposition (total + base + activism)...")

decomp_df <- baseline_data %>%
  select(kappa, Delta_min, base, act) %>%
  pivot_longer(cols = c(Delta_min, base, act),
               names_to = "component", values_to = "value") %>%
  mutate(component = factor(component,
                            levels = c("Delta_min", "base", "act"),
                            labels = c("Total minority gains",
                                       "Base: m0 · Pr(bid)",
                                       "Activism")))

pC <- ggplot(decomp_df, aes(x = kappa, y = value,
                            colour = component, linetype = component)) +
  geom_line(linewidth = 1.1) +
  scale_colour_manual(values = c(
    "Total minority gains" = "#4477aa",
    "Base: m0 · Pr(bid)" = "#228833",
    "Activism" = "#ee6677"
  )) +
  scale_linetype_manual(values = c(
    "Total minority gains" = "solid",
    "Base: m0 · Pr(bid)" = "dashed",
    "Activism" = "dotdash"
  )) +
  labs(x = TeX("Liquidity $\\kappa$"),
       y = TeX("Expected Minority Gains")) +
  theme_pres() +
  theme(legend.position = "bottom",
        legend.direction = "horizontal")

# Add kappa dagger at peak of total
pC <- add_kappa_dagger(pC, kappa_dagger, peak_delta, colour = "#228833",
                        label_y = min(baseline_data$Delta_min, na.rm = TRUE))

save_pres_figure(pC, file.path(output_dir, "fig_decomposition.pdf"))

# ============================================================================
# FIGURE D: Disclosure Slopes (replace level curves with slope curves)
# ============================================================================

message("[D] Disclosure slopes (replacing level curves)...")

disc_data <- load_or_compute("disclosure_attenuation.csv", function() {
  kappa_values <- seq(0.15, 0.85, length.out = 35)
  compute_disclosure_attenuation_series(params, kappa_values,
                                         baseline$k1, baseline$k0, baseline$kD)
})

# Compute slopes via finite differences
disc_data <- disc_data %>%
  filter(!is.na(act_disclosure) & !is.na(act_no_disclosure))

slope_disc    <- compute_slopes(disc_data$kappa, disc_data$act_disclosure)
slope_no_disc <- compute_slopes(disc_data$kappa, disc_data$act_no_disclosure)

# Smooth with loess if noisy (check if range of raw slopes is reasonable)
slope_df <- data.frame(
  kappa = disc_data$kappa,
  slope_disc = slope_disc,
  slope_no_disc = slope_no_disc
)

# Apply loess smoothing for cleaner presentation
if (nrow(slope_df) >= 10) {
  lo_disc    <- loess(slope_disc ~ kappa, data = slope_df, span = 0.3)
  lo_no_disc <- loess(slope_no_disc ~ kappa, data = slope_df, span = 0.3)
  slope_df$slope_disc    <- predict(lo_disc)
  slope_df$slope_no_disc <- predict(lo_no_disc)
}

# Find zero-crossings (approximate peak locations of the level curves)
find_zero_crossing <- function(kappa, slope) {
  sign_changes <- which(diff(sign(slope)) != 0)
  if (length(sign_changes) == 0) return(NA)
  # Linear interpolation at first sign change
  i <- sign_changes[1]
  kappa[i] - slope[i] * (kappa[i + 1] - kappa[i]) / (slope[i + 1] - slope[i])
}

zero_disc    <- find_zero_crossing(slope_df$kappa, slope_df$slope_disc)
zero_no_disc <- find_zero_crossing(slope_df$kappa, slope_df$slope_no_disc)

pD <- ggplot(slope_df, aes(x = kappa)) +
  # Ribbon between the two slope curves (pmin/pmax handles crossing)
  geom_ribbon(aes(ymin = pmin(slope_disc, slope_no_disc),
                  ymax = pmax(slope_disc, slope_no_disc)),
              fill = "#4477aa", alpha = 0.12) +
  # Slope curves
  geom_line(aes(y = slope_disc), colour = "#4477aa", linewidth = 1.1,
            linetype = "solid") +
  geom_line(aes(y = slope_no_disc), colour = "#ee6677", linewidth = 1.1,
            linetype = "dashed") +
  # Zero reference line
  geom_hline(yintercept = 0, linetype = "dotted", colour = "grey50",
             linewidth = 0.4) +
  labs(x = TeX("Liquidity $\\kappa$"),
       y = TeX("Slope $\\partial\\Delta^{\\mathrm{act}} / \\partial\\kappa$")) +
  theme_pres()

# Mark zero-crossing points
if (!is.na(zero_disc)) {
  pD <- pD + annotate("point", x = zero_disc, y = 0,
                       shape = 16, size = 3, colour = "#4477aa")
}
if (!is.na(zero_no_disc)) {
  pD <- pD + annotate("point", x = zero_no_disc, y = 0,
                       shape = 16, size = 3, colour = "#ee6677")
}

# Attenuation label in ribbon region
ribbon_mid_x <- mean(slope_df$kappa)
ribbon_mid_y <- mean(c(
  slope_df$slope_disc[which.min(abs(slope_df$kappa - ribbon_mid_x))],
  slope_df$slope_no_disc[which.min(abs(slope_df$kappa - ribbon_mid_x))]
))

pD <- pD +
  annotate("text", x = ribbon_mid_x, y = ribbon_mid_y,
           label = "Attenuation", size = 3.5, colour = "#4477aa",
           fontface = "italic", family = "serif", alpha = 0.8)

# Manual legend at bottom
slope_y_range <- range(c(slope_df$slope_disc, slope_df$slope_no_disc), na.rm = TRUE)
leg_y <- slope_y_range[1] + diff(slope_y_range) * 0.05
leg_x <- min(slope_df$kappa) + diff(range(slope_df$kappa)) * 0.03

pD <- pD +
  annotate("segment", x = leg_x, xend = leg_x + 0.06,
           y = leg_y, yend = leg_y,
           colour = "#4477aa", linewidth = 0.8) +
  annotate("text", x = leg_x + 0.07, y = leg_y,
           label = "Baseline (disclosure)", hjust = 0, size = 3.2,
           family = "serif") +
  annotate("segment", x = leg_x, xend = leg_x + 0.06,
           y = leg_y - diff(slope_y_range) * 0.1,
           yend = leg_y - diff(slope_y_range) * 0.1,
           colour = "#ee6677", linewidth = 0.8, linetype = "dashed") +
  annotate("text", x = leg_x + 0.07,
           y = leg_y - diff(slope_y_range) * 0.1,
           label = "No disclosure", hjust = 0, size = 3.2,
           family = "serif")

save_pres_figure(pD, file.path(output_dir, "fig_disclosure_slopes.pdf"))

# ============================================================================
# FIGURES E & F: Consolidated Sensitivity Panels
# ============================================================================

kappa_sens <- seq(0.25, 0.85, length.out = 21)

# Load all sensitivity data
message("[E] Sensitivity panel 1 (delta + sigma_xi)...")

sens_delta <- load_or_compute("sensitivity_delta.csv", function() {
  compute_sensitivity(params, "delta", c(0.85, 0.90, 0.95), kappa_sens)
})

sens_sigma_xi <- load_or_compute("sensitivity_sigma_xi.csv", function() {
  compute_sensitivity(params, "sigma_xi", c(0.25, 0.40, 0.60), kappa_sens)
})

# Build panel 1: delta + sigma_xi
# Use ordinal rank within each parameter group for color mapping
panel1_delta <- sens_delta %>%
  mutate(parameter = "Discount factor \u03b4",
         param_rank = as.factor(as.integer(factor(delta)))) %>%
  select(kappa, Delta_min, parameter, param_rank)

panel1_sigma <- sens_sigma_xi %>%
  mutate(parameter = "Bidder shock \u03c3_\u03be",
         param_rank = as.factor(as.integer(factor(sigma_xi)))) %>%
  select(kappa, Delta_min, parameter, param_rank)

panel1_data <- bind_rows(panel1_delta, panel1_sigma) %>%
  filter(!is.na(Delta_min))

pE <- ggplot(panel1_data, aes(x = kappa, y = Delta_min,
                                colour = param_rank,
                                linetype = param_rank)) +
  geom_line(linewidth = 0.9) +
  scale_colour_manual(values = SENS_COLORS[1:3]) +
  scale_linetype_manual(values = SENS_LINETYPES[1:3]) +
  facet_wrap(~parameter, ncol = 2, scales = "free_y") +
  # Add kappa dagger reference in each panel
  geom_vline(xintercept = kappa_dagger, linetype = "dotted",
             colour = "#228833", linewidth = 0.4, alpha = 0.6) +
  labs(x = TeX("Liquidity $\\kappa$"),
       y = TeX("$\\Delta^{\\mathrm{min}}$")) +
  theme_pres() +
  theme(legend.position = "none",
        strip.text = element_text(size = 11))

save_pres_figure(pE, file.path(output_dir, "fig_sensitivity_panel1.pdf"),
                  width = 8.0, height = 3.8)

# Panel 2: C0 + wedge + rho
message("[F] Sensitivity panel 2 (C0 + wedge + rho)...")

sens_C0 <- load_or_compute("sensitivity_C0.csv", function() {
  compute_sensitivity(params, "C0", c(0.06, 0.12, 0.21, 0.24), kappa_sens)
})

sens_wedge <- load_or_compute("sensitivity_wedge.csv", function() {
  compute_sensitivity(params, "wedge", c(0.10, 0.20, 0.30), kappa_sens,
                       replace_fn = function(bp, k, w) {
                         update_params(bp, kappa = k, m1 = bp$m0 + w)
                       })
})

sens_rho <- load_or_compute("sensitivity_rho.csv", function() {
  compute_sensitivity(params, "rho", c(0.5, 0.7, 0.9), kappa_sens)
})

# Use ordinal rank within each parameter group (max 4 per group)
panel2_C0 <- sens_C0 %>%
  mutate(parameter = "Engagement cost C\u2080",
         param_rank = as.factor(as.integer(factor(C0)))) %>%
  select(kappa, Delta_min, parameter, param_rank)

panel2_wedge <- sens_wedge %>%
  mutate(parameter = "Premium wedge m\u2081\u2212m\u2080",
         param_rank = as.factor(as.integer(factor(wedge)))) %>%
  select(kappa, Delta_min, parameter, param_rank)

panel2_rho <- sens_rho %>%
  mutate(parameter = "Success prob. \u03c1",
         param_rank = as.factor(as.integer(factor(rho)))) %>%
  select(kappa, Delta_min, parameter, param_rank)

panel2_data <- bind_rows(panel2_C0, panel2_wedge, panel2_rho) %>%
  filter(!is.na(Delta_min))

pF <- ggplot(panel2_data, aes(x = kappa, y = Delta_min,
                                colour = param_rank,
                                linetype = param_rank)) +
  geom_line(linewidth = 0.9) +
  scale_colour_manual(values = SENS_COLORS[1:4]) +
  scale_linetype_manual(values = SENS_LINETYPES[1:4]) +
  facet_wrap(~parameter, ncol = 3, scales = "free_y") +
  geom_vline(xintercept = kappa_dagger, linetype = "dotted",
             colour = "#228833", linewidth = 0.4, alpha = 0.6) +
  labs(x = TeX("Liquidity $\\kappa$"),
       y = TeX("$\\Delta^{\\mathrm{min}}$")) +
  theme_pres() +
  theme(legend.position = "none",
        strip.text = element_text(size = 11))

save_pres_figure(pF, file.path(output_dir, "fig_sensitivity_panel2.pdf"),
                  width = 9.0, height = 3.5)

# ============================================================================
# FIGURE G: Welfare (major — dual-optimum markers)
# ============================================================================

message("[G] Welfare (dual-optimum markers)...")

welfare_data <- load_or_compute("welfare.csv", function() {
  compute_welfare_series(params, kappa_sens)
})

# Find optima
idx_min <- which.max(welfare_data$W_min)
idx_tot <- which.max(welfare_data$W_tot)
kd_welfare <- welfare_data$kappa[idx_min]
ks_welfare <- welfare_data$kappa[idx_tot]
welfare_y_min <- min(welfare_data$W_min, na.rm = TRUE)
welfare_y_range <- diff(range(welfare_data$W_tot, welfare_data$W_bid,
                              welfare_data$W_min, na.rm = TRUE))

pG <- ggplot(welfare_data, aes(x = kappa)) +
  geom_line(aes(y = W_tot), colour = "#4477aa", linewidth = 1.1,
            linetype = "solid") +
  geom_line(aes(y = W_bid), colour = "#ee6677", linewidth = 1.1,
            linetype = "dashed") +
  geom_line(aes(y = W_min), colour = "#228833", linewidth = 1.1,
            linetype = "dotdash") +
  # kappa dagger (minority optimum)
  geom_vline(xintercept = kd_welfare, colour = "#228833",
             linetype = "dotted", linewidth = 0.5, alpha = 0.7) +
  annotate("text", x = kd_welfare + 0.015,
           y = welfare_y_min + 0.08 * welfare_y_range,
           label = TeX("$\\kappa^{\\dagger}$"),
           colour = "#228833", size = 4.5, vjust = 0.4, family = "serif") +
  # kappa star (total surplus optimum)
  geom_vline(xintercept = ks_welfare, colour = "#4477aa",
             linetype = "dotted", linewidth = 0.5, alpha = 0.7) +
  annotate("text", x = ks_welfare - 0.015,
           y = max(welfare_data$W_tot, na.rm = TRUE) * 0.95,
           label = TeX("$\\kappa^{*}$"),
           colour = "#4477aa", size = 4.5, family = "serif", hjust = 1) +
  labs(x = TeX("Liquidity $\\kappa$"),
       y = "Expected Welfare") +
  theme_pres() +
  theme(legend.position = "none")

# Manual legend (following manuscript pattern)
w_max <- max(welfare_data$W_tot, na.rm = TRUE)
w_min <- min(welfare_data$W_min, na.rm = TRUE)
leg_x <- 0.68
leg_y_base <- w_min + (w_max - w_min) * 0.35
leg_gap <- (w_max - w_min) * 0.07

pG <- pG +
  annotate("segment", x = leg_x, xend = leg_x + 0.04,
           y = leg_y_base, yend = leg_y_base,
           colour = "#4477aa", linewidth = 0.7) +
  annotate("text", x = leg_x + 0.05, y = leg_y_base,
           label = TeX("Total Surplus $W$"),
           hjust = 0, size = 3.5, family = "serif") +
  annotate("segment", x = leg_x, xend = leg_x + 0.04,
           y = leg_y_base - leg_gap, yend = leg_y_base - leg_gap,
           colour = "#ee6677", linewidth = 0.7, linetype = "dashed") +
  annotate("text", x = leg_x + 0.05, y = leg_y_base - leg_gap,
           label = TeX("Bidder $W_{\\mathrm{bid}}$"),
           hjust = 0, size = 3.5, family = "serif") +
  annotate("segment", x = leg_x, xend = leg_x + 0.04,
           y = leg_y_base - 2 * leg_gap, yend = leg_y_base - 2 * leg_gap,
           colour = "#228833", linewidth = 0.7, linetype = "dotdash") +
  annotate("text", x = leg_x + 0.05, y = leg_y_base - 2 * leg_gap,
           label = TeX("Minority $W_{\\mathrm{min}}$"),
           hjust = 0, size = 3.5, family = "serif")

save_pres_figure(pG, file.path(output_dir, "fig_welfare.pdf"))

# ============================================================================
# FIGURE H: Cutoffs vs Liquidity (minor — add kappa dagger)
# ============================================================================

message("[H] Cutoffs vs liquidity...")

fig_h_long <- baseline_data %>%
  select(kappa, k1, k0, kD) %>%
  tidyr::pivot_longer(cols = c(k1, k0, kD),
                       names_to = "cutoff", values_to = "value") %>%
  mutate(cutoff = factor(cutoff, levels = c("k1", "k0", "kD"),
                          labels = c("k1 (Exit/Hold)", "k0 (Hold/Quiet)",
                                     "kD (Quiet/Public)")))

fig_h_y_min <- min(fig_h_long$value, na.rm = TRUE)
fig_h_y_range <- diff(range(fig_h_long$value, na.rm = TRUE))

pH <- ggplot(fig_h_long, aes(x = kappa, y = value, colour = cutoff,
                              linetype = cutoff)) +
  geom_line(linewidth = 1.0) +
  geom_hline(yintercept = bl_mu, linetype = "dotted", colour = "grey50") +
  annotate("text", x = 0.16, y = bl_mu + 0.05, label = expression(mu),
           size = 4, colour = "grey50") +
  # Add kappa dagger vline
  geom_vline(xintercept = kappa_dagger, linetype = "dashed",
             colour = "#228833", linewidth = 0.4, alpha = 0.6) +
  annotate("text", x = kappa_dagger + 0.01,
           y = fig_h_y_min + 0.08 * fig_h_y_range,
           label = expression(kappa^"\u2020"),
           size = 4, colour = "#228833", hjust = 0, vjust = 0.4, family = "serif") +
  scale_colour_manual(values = c("k1 (Exit/Hold)" = COL_EXIT,
                                  "k0 (Hold/Quiet)" = COL_HOLD,
                                  "kD (Quiet/Public)" = COL_PUBLIC)) +
  scale_linetype_manual(values = c("k1 (Exit/Hold)" = "solid",
                                    "k0 (Hold/Quiet)" = "dashed",
                                    "kD (Quiet/Public)" = "dotdash")) +
  labs(x = TeX("Liquidity $\\kappa$"),
       y = "Signal Cutoff Value") +
  theme_pres() +
  theme(legend.position = "bottom",
        legend.direction = "horizontal")

save_pres_figure(pH, file.path(output_dir, "fig_cutoffs_kappa.pdf"))

# ============================================================================
# FIGURE I: Noisy Rumor (minor — legend to bottom, add kappa dagger)
# ============================================================================

message("[I] Noisy rumor...")

rumor_data <- load_or_compute("noisy_rumor.csv", function() {
  rumor_configs <- list(
    list(eta_1 = 0.50, eta_0 = 0.50, label = "Uninformative"),
    list(eta_1 = 0.75, eta_0 = 0.25, label = "Moderate"),
    list(eta_1 = 0.95, eta_0 = 0.05, label = "Precise")
  )
  compute_noisy_rumor_series(params, kappa_sens, rumor_configs)
})

rumor_data$label <- factor(rumor_data$label,
                            levels = c("Uninformative", "Moderate", "Precise"))

n_labels <- length(unique(rumor_data$label))
colors_rumor <- setNames(SENS_COLORS[seq_len(n_labels)], levels(rumor_data$label))

# Find kappa dagger for the uninformative case (= baseline)
uninf <- rumor_data %>% filter(label == "Uninformative")
uninf_peak_idx <- which.max(uninf$Delta_min)
kd_rumor <- uninf$kappa[uninf_peak_idx]
rumor_y_min <- min(rumor_data$Delta_min, na.rm = TRUE)
rumor_y_range <- diff(range(rumor_data$Delta_min, na.rm = TRUE))
kd_label_y <- rumor_y_min + 0.40 * rumor_y_range

pI <- ggplot(rumor_data, aes(x = kappa, y = Delta_min, colour = label,
                                linetype = label)) +
  geom_line(linewidth = 1.0) +
  # Add kappa dagger for uninformative case
  geom_vline(xintercept = kd_rumor, linetype = "dashed",
             colour = "#228833", linewidth = 0.4, alpha = 0.6) +
  annotate("text", x = kd_rumor + 0.01,
           y = kd_label_y,
           label = expression(kappa^"\u2020"),
           size = 4, colour = "#228833", hjust = 0, vjust = 0.5, family = "serif") +
  scale_colour_manual(values = colors_rumor) +
  scale_linetype_manual(values = setNames(SENS_LINETYPES[seq_len(n_labels)],
                                           levels(rumor_data$label))) +
  labs(x = TeX("Liquidity $\\kappa$"),
       y = TeX("$\\Delta^{\\mathrm{min}}$"),
       colour = "Rumor Precision", linetype = "Rumor Precision") +
  theme_pres() +
  theme(legend.position = "bottom")

save_pres_figure(pI, file.path(output_dir, "fig_noisy_rumor.pdf"))

# ============================================================================
# FIGURE J: Prices (keep generated, not on any slide)
# ============================================================================

message("[J] Prices by state (kept for completeness)...")

fig_j_data <- load_or_compute("prices.csv", function() {
  prices <- compute_equilibrium_prices(baseline$k1, baseline$k0, baseline$kD, params)
  omegas <- compute_action_probabilities(baseline$k1, baseline$k0, baseline$kD, params)
  posts  <- compute_posteriors(omegas$omega_E, omegas$omega_H,
                               omegas$omega_Q, omegas$omega_P, params$kappa)

  rows <- list()
  for (X in -2:1) {
    key <- paste(X, 0, sep = ",")
    P <- prices[[key]]; if (is.null(P)) P <- NA
    pi_val <- posts[[key]]; if (is.null(pi_val)) pi_val <- 0
    m_XD <- params$m0 + (params$m_tilde - params$m0) * pi_val
    p_bid <- if (!is.na(P)) bid_probability(P, m_XD, params) else NA
    rows[[length(rows) + 1]] <- data.frame(
      X = X, D = 0, price = P, pi = pi_val, p_bid = p_bid, m_XD = m_XD
    )
  }
  for (X in 0:2) {
    key <- paste(X, 1, sep = ",")
    P <- prices[[key]]; if (is.null(P)) P <- NA
    rows[[length(rows) + 1]] <- data.frame(
      X = X, D = 1, price = P, pi = 1.0, p_bid = if (!is.na(P))
        bid_probability(P, params$m_tilde, params) else NA, m_XD = params$m_tilde
    )
  }
  do.call(rbind, rows)
})

fig_j_data <- fig_j_data %>%
  mutate(D_label = ifelse(D == 0, "D = 0 (Inferred)", "D = 1 (Observed)"),
         X_label = as.factor(X))

pJ <- ggplot(fig_j_data, aes(x = X_label, y = price, fill = D_label)) +
  geom_col(position = "dodge", width = 0.6) +
  geom_text(aes(label = sprintf("%.2f", pi)), vjust = -0.5, size = 3.2,
            position = position_dodge(width = 0.6)) +
  scale_fill_manual(values = c("D = 0 (Inferred)" = "#4477aa",
                                "D = 1 (Observed)" = "#44aa99")) +
  labs(x = "Order Flow X", y = "Equilibrium Price P(X,D)",
       fill = NULL) +
  theme_pres() +
  theme(legend.position = "top")

save_pres_figure(pJ, file.path(output_dir, "fig_prices.pdf"))

# ============================================================================
# Summary
# ============================================================================

message("\n=== All 10 presentation figures generated ===")
message("  A: fig_cutoff_structure.pdf")
message("  B: fig_nonmonotone.pdf")
message("  C: fig_decomposition.pdf")
message("  D: fig_disclosure_slopes.pdf")
message("  E: fig_sensitivity_panel1.pdf")
message("  F: fig_sensitivity_panel2.pdf")
message("  G: fig_welfare.pdf")
message("  H: fig_cutoffs_kappa.pdf")
message("  I: fig_noisy_rumor.pdf")
message("  J: fig_prices.pdf (not on slides)")
message("Output directory: ", output_dir)
