# ============================================================================
# Figure 1: Equilibrium Cutoff Structure on Number Line
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))
library(patchwork)

plot_fig01 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  # Read data
  cutoffs <- read_csv(file.path(data_dir, "baseline_cutoffs.csv"),
                      show_col_types = FALSE)
  regions <- read_csv(file.path(data_dir, "cutoff_regions.csv"),
                      show_col_types = FALSE)

  k1 <- cutoffs$k1
  k0 <- cutoffs$k0
  kD <- cutoffs$kD
  mu <- cutoffs$mu
  sigma_s <- cutoffs$sigma_s

  has_hold <- abs(k0 - k1) > 1e-4
  tol <- 1e-4

  # Main number-line plot
  p_main <- ggplot() +
    # Coloured regions
    geom_rect(data = regions,
              aes(xmin = xmin, xmax = xmax, ymin = -0.2, ymax = 0.2,
                  fill = region),
              alpha = 0.7) +
    scale_fill_manual(
      values = ACTION_COLORS,
      limits = c("Exit", "Hold", "Quiet Voice", "Public Voice"),
      breaks = regions$region
    ) +
    # Region labels (only for wide-enough regions)
    geom_text(data = regions %>% filter((xmax - xmin) >= 0.8),
              aes(x = (xmin + xmax) / 2, y = 0, label = region),
              size = 3, fontface = "bold", family = "serif") +
    # Cutoff lines
    geom_vline(xintercept = k1, linetype = "dashed", linewidth = 0.5, alpha = 0.9) +
    {if (has_hold) geom_vline(xintercept = k0, linetype = "dashed",
                               linewidth = 0.5, alpha = 0.9)} +
    geom_vline(xintercept = kD, linetype = "dashed", linewidth = 0.5, alpha = 0.9) +
    # Number line
    geom_hline(yintercept = -0.32, linewidth = 0.5, alpha = 0.8) +
    # Cutoff points on number line
    annotate("point", x = k1, y = -0.32, size = 2) +
    {if (has_hold) annotate("point", x = k0, y = -0.32, size = 2)} +
    annotate("point", x = kD, y = -0.32, size = 2) +
    # Cutoff labels
    annotate("text", x = k1, y = -0.42,
             label = TeX("$k_1$"), size = 4, family = "serif", vjust = 1) +
    {if (has_hold) {
      annotate("text", x = k0, y = -0.50,
               label = TeX("$k_0$"), size = 4, family = "serif", vjust = 1)
    } else {
      annotate("text", x = k1 + 0.05, y = -0.50,
               label = TeX("$k_1 = k_0$"), size = 3.5, family = "serif", vjust = 1)
    }} +
    annotate("text", x = kD, y = -0.42,
             label = TeX("$k_D$"), size = 4, family = "serif", vjust = 1) +
    # Mu marker
    geom_vline(xintercept = mu, colour = "gray", linetype = "dotted",
               linewidth = 0.5) +
    annotate("text", x = mu, y = 0.35,
             label = TeX("$\\mu$"), size = 4, colour = "gray",
             family = "serif", vjust = 0) +
    # Axes and theme
    labs(x = TeX("Signal $s$")) +
    coord_cartesian(ylim = c(-0.6, 0.5)) +
    theme_evt() +
    theme(
      axis.text.y  = element_blank(),
      axis.ticks.y = element_blank(),
      axis.title.y = element_blank(),
      axis.line.y  = element_blank(),
      legend.position = "top",
      legend.direction = "horizontal",
      legend.justification = "center"
    ) +
    guides(fill = guide_legend(nrow = 1, override.aes = list(alpha = 0.7)))

  # If k1 and k0 are very close but distinct, add a zoom inset
  if (has_hold && abs(k0 - k1) < 0.15) {
    pad <- max(0.08, 8 * abs(k0 - k1))
    zoom_xmin <- k1 - pad
    zoom_xmax <- k0 + pad

    p_zoom <- ggplot() +
      geom_rect(data = regions,
                aes(xmin = xmin, xmax = xmax, ymin = -0.2, ymax = 0.2,
                    fill = region),
                alpha = 0.7) +
      scale_fill_manual(values = ACTION_COLORS, guide = "none") +
      geom_vline(xintercept = k1, linetype = "dashed", linewidth = 0.5) +
      geom_vline(xintercept = k0, linetype = "dashed", linewidth = 0.5) +
      coord_cartesian(xlim = c(zoom_xmin, zoom_xmax),
                      ylim = c(-0.25, 0.25)) +
      theme_evt() +
      theme(
        axis.text  = element_blank(),
        axis.ticks = element_blank(),
        axis.title = element_blank(),
        axis.line  = element_blank(),
        panel.border = element_rect(fill = NA, colour = "grey40", linewidth = 0.5)
      )

    p_final <- p_main + inset_element(p_zoom, left = 0.02, bottom = 0.02,
                                       right = 0.35, top = 0.45)
  } else {
    p_final <- p_main
  }

  save_figure(p_final, file.path(output_dir, "fig_cutoff_structure.pdf"),
              width = 8, height = 2.5)

  p_final
}

# Run if sourced directly
if (sys.nframe() == 0) plot_fig01()
