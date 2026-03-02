# ============================================================================
# Figure 3: Decomposition of Minority Takeover Gains
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig03 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "baseline_series.csv"),
                 show_col_types = FALSE)

  df$total <- df$base + df$act

  # Find the peak
  peak_idx <- which.max(df$total)
  kappa_peak <- df$kappa[peak_idx]

  p <- ggplot(df, aes(x = kappa)) +
    # Base component: cyan fill from 0
    geom_ribbon(aes(ymin = 0, ymax = base),
                fill = COL_QUIET, alpha = 0.5) +
    # Activism component: rose fill stacked
    geom_ribbon(aes(ymin = base, ymax = total),
                fill = COL_EXIT, alpha = 0.5) +
    # Total line on top
    geom_line(aes(y = total), colour = "black", linewidth = 0.7) +
    # Peak marker
    geom_vline(xintercept = kappa_peak, colour = "gray",
               linetype = "dashed", linewidth = 0.5, alpha = 0.7) +
    annotate("text", x = kappa_peak + 0.015,
             y = max(df$total, na.rm = TRUE) * 0.98,
             label = TeX("$\\kappa^{\\dagger}$"),
             size = 4, colour = "gray", family = "serif") +
    # Manual legend via annotate (matching stacked area style)
    annotate("rect", xmin = 0.17, xmax = 0.20, ymin = max(df$total) * 0.88,
             ymax = max(df$total) * 0.92,
             fill = COL_QUIET, alpha = 0.5) +
    annotate("text", x = 0.21, y = max(df$total) * 0.90,
             label = TeX("Base: $m_0 \\cdot P(\\mathrm{bid})$"),
             size = 3, hjust = 0, family = "serif") +
    annotate("rect", xmin = 0.17, xmax = 0.20, ymin = max(df$total) * 0.80,
             ymax = max(df$total) * 0.84,
             fill = COL_EXIT, alpha = 0.5) +
    annotate("text", x = 0.21, y = max(df$total) * 0.82,
             label = TeX("Activism: $\\Delta^{\\mathrm{act}}(\\kappa)$"),
             size = 3, hjust = 0, family = "serif") +
    annotate("segment", x = 0.17, xend = 0.20, y = max(df$total) * 0.74,
             yend = max(df$total) * 0.74, linewidth = 0.5) +
    annotate("text", x = 0.21, y = max(df$total) * 0.74,
             label = TeX("Total $\\Delta^{\\mathrm{min}}$"),
             size = 3, hjust = 0, family = "serif") +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = TeX("Expected Minority Takeover Gains"),
      title = "Decomposition of Minority Takeover Gains"
    ) +
    theme_evt()

  save_figure(p, file.path(output_dir, "fig_decomposition.pdf"))
  p
}

if (sys.nframe() == 0) plot_fig03()
