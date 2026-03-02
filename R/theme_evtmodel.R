# ============================================================================
# theme_evtmodel.R -- Shared ggplot2 theme, palettes, and helpers
#
# Replicates the matplotlib style from figures.py for publication-quality
# figures using the Paul Tol colourblind-friendly muted palette.
# ============================================================================

library(ggplot2)
library(latex2exp)
library(scales)
library(dplyr)
library(readr)

# -- Colour palettes ---------------------------------------------------------

# Action colours (Paul Tol muted)
COL_EXIT   <- "#cc6677"   # muted rose
COL_HOLD   <- "#ddcc77"   # muted sand
COL_QUIET  <- "#88ccee"   # muted cyan
COL_PUBLIC <- "#44aa99"   # muted teal

ACTION_COLORS <- c(
  "Exit"         = COL_EXIT,
  "Hold"         = COL_HOLD,
  "Quiet Voice"  = COL_QUIET,
  "Public Voice" = COL_PUBLIC
)

# Sensitivity analysis palette
SENS_COLORS <- c("#4477aa", "#ee6677", "#228833", "#ccbb44")

# Named line types and shapes for sensitivity
SENS_LINETYPES <- c("solid", "dashed", "dotdash", "dotted")
SENS_SHAPES    <- c(16, 15, 17, 18)  # circle, square, triangle, diamond

# -- Custom ggplot2 theme ----------------------------------------------------

theme_evt <- function(base_size = 11) {
  theme_bw(base_size = base_size, base_family = "serif") %+replace%
    theme(
      # Remove top and right spines (matching matplotlib)
      panel.border     = element_blank(),
      axis.line        = element_line(colour = "black", linewidth = 0.4),
      axis.line.x      = element_line(colour = "black", linewidth = 0.4),
      axis.line.y      = element_line(colour = "black", linewidth = 0.4),

      # Grid: subtle like matplotlib grid.alpha = 0.15
      panel.grid.major = element_line(colour = "grey85", linewidth = 0.3),
      panel.grid.minor = element_blank(),

      # Font sizes matching matplotlib rcParams
      axis.title       = element_text(size = rel(1.09)),   # 12/11
      axis.text        = element_text(size = rel(0.91)),   # 10/11
      plot.title       = element_text(size = rel(1.09), hjust = 0.5, face = "plain"),
      legend.text      = element_text(size = rel(0.91)),
      legend.title     = element_blank(),
      legend.background = element_rect(fill = "white", colour = "grey80",
                                        linewidth = 0.3),
      legend.key       = element_rect(fill = "white", colour = NA),

      # Tight layout
      plot.margin      = margin(5, 10, 5, 5)
    )
}

# -- Default figure dimensions ------------------------------------------------

FIG_WIDTH  <- 5.5
FIG_HEIGHT <- 3.8
FIG_DPI    <- 300

# -- Save helper --------------------------------------------------------------

save_figure <- function(plot, filename, width = FIG_WIDTH, height = FIG_HEIGHT,
                        dpi = FIG_DPI, device = cairo_pdf) {
  ggsave(filename, plot = plot, width = width, height = height,
         dpi = dpi, device = device)
  message("  Saved: ", filename)
}

# -- Sensitivity plot helper --------------------------------------------------

#' Plot sensitivity analysis: Delta_min vs kappa for multiple parameter values.
#'
#' @param df         Data frame with columns: kappa, <param_col>, Delta_min
#' @param param_col  Name of the parameter column (string)
#' @param param_label LaTeX label for the parameter (passed to TeX())
#' @param y_label    LaTeX label for the y-axis
#' @param title      Plot title (LaTeX or plain text)
#' @param legend_fmt Format function for legend labels (e.g., function(x) sprintf("$C_0 = %.2f$", x))
#' @param output_path File path for saving (optional)
#' @return ggplot object
plot_sensitivity <- function(df, param_col, param_label,
                             y_label = "Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$",
                             title = NULL,
                             legend_fmt = NULL,
                             output_path = NULL) {

  # Ensure param_col is a factor for consistent styling
  param_vals <- sort(unique(df[[param_col]]))
  n_vals <- length(param_vals)
  df[[param_col]] <- factor(df[[param_col]], levels = param_vals)

  # Build legend labels
  if (is.null(legend_fmt)) {
    legend_labels <- setNames(
      sapply(param_vals, function(v) TeX(sprintf("%s = %s", param_label, v))),
      param_vals
    )
  } else {
    legend_labels <- setNames(
      sapply(param_vals, function(v) TeX(legend_fmt(v))),
      param_vals
    )
  }

  # Assign colours/linetypes/shapes
  colors <- setNames(SENS_COLORS[seq_len(n_vals)], param_vals)
  ltypes <- setNames(SENS_LINETYPES[seq_len(n_vals)], param_vals)
  shapes <- setNames(SENS_SHAPES[seq_len(n_vals)], param_vals)

  p <- ggplot(df, aes(x = kappa, y = Delta_min,
                       colour = .data[[param_col]],
                       linetype = .data[[param_col]],
                       shape = .data[[param_col]])) +
    geom_line(linewidth = 0.9) +
    geom_point(size = 1.8) +
    scale_colour_manual(values = colors, labels = legend_labels) +
    scale_linetype_manual(values = ltypes, labels = legend_labels) +
    scale_shape_manual(values = shapes, labels = legend_labels) +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = TeX(y_label),
      title = if (!is.null(title)) TeX(title) else NULL
    ) +
    theme_evt() +
    theme(legend.position = "right")

  if (!is.null(output_path)) {
    save_figure(p, output_path)
  }

  p
}
