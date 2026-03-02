# ============================================================================
# Figure 2: Non-Monotonic Effect of Liquidity on Takeover Gains
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig02 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "baseline_series.csv"),
                 show_col_types = FALSE)

  # Find the peak (kappa-dagger)
  peak_idx <- which.max(df$Delta_min)
  kappa_peak <- df$kappa[peak_idx]

  p <- ggplot(df, aes(x = kappa, y = Delta_min)) +
    geom_line(colour = "#4477aa", linewidth = 1.0) +
    # Peak marker
    geom_vline(xintercept = kappa_peak, colour = "gray",
               linetype = "dashed", linewidth = 0.5, alpha = 0.7) +
    annotate("text", x = kappa_peak + 0.015,
             y = max(df$Delta_min, na.rm = TRUE) * 0.98,
             label = TeX("$\\kappa^{\\dagger}$"),
             size = 4, colour = "gray", family = "serif") +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = TeX("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$"),
      title = "Non-Monotonic Effect of Liquidity on Takeover Gains"
    ) +
    theme_evt()

  save_figure(p, file.path(output_dir, "fig_nonmonotone.pdf"))
  p
}

if (sys.nframe() == 0) plot_fig02()
