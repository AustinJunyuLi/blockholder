# ============================================================================
# Figure 13: Welfare Decomposition and Optimal Liquidity
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig13 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "welfare.csv"), show_col_types = FALSE)

  # Find optima
  idx_min <- which.max(df$W_min)
  idx_tot <- which.max(df$W_tot)
  kappa_dagger <- df$kappa[idx_min]
  kappa_star   <- df$kappa[idx_tot]

  p <- ggplot(df, aes(x = kappa)) +
    geom_line(aes(y = W_tot), colour = "#4477aa",
              linewidth = 0.9, linetype = "solid") +
    geom_line(aes(y = W_bid), colour = "#ee6677",
              linewidth = 0.9, linetype = "dashed") +
    geom_line(aes(y = W_min), colour = "#228833",
              linewidth = 0.9, linetype = "dotdash") +
    # Optimal kappa for minority gains
    geom_vline(xintercept = kappa_dagger, colour = "#228833",
               linetype = "dotted", linewidth = 0.5, alpha = 0.7) +
    annotate("text", x = kappa_dagger + 0.015,
             y = min(df$W_min, na.rm = TRUE),
             label = TeX("$\\kappa^{\\dagger}$"),
             colour = "#228833", size = 4, family = "serif") +
    # Optimal kappa for total surplus
    geom_vline(xintercept = kappa_star, colour = "#4477aa",
               linetype = "dotted", linewidth = 0.5, alpha = 0.7) +
    annotate("text", x = kappa_star - 0.015,
             y = max(df$W_tot, na.rm = TRUE) * 0.95,
             label = TeX("$\\kappa^{*}$"),
             colour = "#4477aa", size = 4, family = "serif", hjust = 1) +
    # Manual legend
    annotate("segment", x = 0.68, xend = 0.72,
             y = max(df$W_tot) * 0.35,
             yend = max(df$W_tot) * 0.35,
             colour = "#4477aa", linewidth = 0.7) +
    annotate("text", x = 0.73, y = max(df$W_tot) * 0.35,
             label = TeX("Total Surplus $W$"),
             hjust = 0, size = 3, family = "serif") +
    annotate("segment", x = 0.68, xend = 0.72,
             y = max(df$W_tot) * 0.30,
             yend = max(df$W_tot) * 0.30,
             colour = "#ee6677", linewidth = 0.7, linetype = "dashed") +
    annotate("text", x = 0.73, y = max(df$W_tot) * 0.30,
             label = TeX("Bidder Surplus $W_{\\mathrm{bid}}$"),
             hjust = 0, size = 3, family = "serif") +
    annotate("segment", x = 0.68, xend = 0.72,
             y = max(df$W_tot) * 0.25,
             yend = max(df$W_tot) * 0.25,
             colour = "#228833", linewidth = 0.7, linetype = "dotdash") +
    annotate("text", x = 0.73, y = max(df$W_tot) * 0.25,
             label = TeX("Minority Gains $W_{\\mathrm{min}}$"),
             hjust = 0, size = 3, family = "serif") +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = "Expected Welfare / Surplus",
      title = "Welfare Decomposition"
    ) +
    theme_evt()

  save_figure(p, file.path(output_dir, "fig_welfare.pdf"))
  p
}

if (sys.nframe() == 0) plot_fig13()
