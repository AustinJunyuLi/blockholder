# ============================================================================
# theme_pres.R -- Presentation-specific ggplot2 theme
#
# Adapted from the manuscript theme_evt for projection-scale readability.
# Uses the Paul Tol muted palette with larger fonts and bolder lines.
# ============================================================================

library(ggplot2)
library(latex2exp)
library(scales)
library(dplyr)
library(tidyr)
library(readr)

# -- Robust TeX wrapper ------------------------------------------------------

# latex2exp occasionally emits literal "mathr..." fragments on mixed
# text-math labels. Sanitize those commands before parsing.
sanitize_tex <- function(label) {
  label <- gsub("\\\\mathrm\\{([^}]*)\\}", "\\1", label, perl = TRUE)
  label <- gsub("\\\\operatorname\\{([^}]*)\\}", "\\1", label, perl = TRUE)
  label
}

TeX <- function(x, output = "expression", ...) {
  latex2exp::TeX(sanitize_tex(x), output = output, ...)
}

# -- Colour palettes (Paul Tol muted, consistent with manuscript) -----------
COL_EXIT   <- "#cc6677"
COL_HOLD   <- "#ddcc77"
COL_QUIET  <- "#88ccee"
COL_PUBLIC <- "#44aa99"

ACTION_COLORS <- c(
  "Exit"         = COL_EXIT,
  "Hold"         = COL_HOLD,
  "Quiet Voice"  = COL_QUIET,
  "Public Voice" = COL_PUBLIC
)

SENS_COLORS    <- c("#4477aa", "#ee6677", "#228833", "#ccbb44")
SENS_LINETYPES <- c("solid", "dashed", "dotdash", "dotted")
SENS_SHAPES    <- c(16, 15, 17, 18)

# -- Presentation theme (larger fonts for projection) -----------------------
theme_pres <- function(base_size = 14) {
  theme_bw(base_size = base_size, base_family = "serif") %+replace%
    theme(
      panel.background = element_rect(fill = "white", colour = NA),
      plot.background = element_rect(fill = "white", colour = NA),
      panel.border     = element_blank(),
      axis.line        = element_line(colour = "black", linewidth = 0.5),
      axis.line.x      = element_line(colour = "black", linewidth = 0.5),
      axis.line.y      = element_line(colour = "black", linewidth = 0.5),
      panel.grid.major = element_line(colour = "grey88", linewidth = 0.25),
      panel.grid.minor = element_blank(),
      axis.title       = element_text(size = rel(1.1)),
      axis.text        = element_text(size = rel(0.9)),
      plot.title       = element_text(size = rel(1.15), hjust = 0.5, face = "plain"),
      legend.text      = element_text(size = rel(0.9)),
      legend.title     = element_blank(),
      legend.background = element_rect(fill = alpha("white", 0.95),
                                       colour = "grey80", linewidth = 0.3),
      legend.key       = element_rect(fill = "white", colour = NA),
      strip.background = element_rect(fill = "white", colour = NA),
      strip.text       = element_text(size = rel(0.92), face = "bold"),
      plot.margin      = margin(8, 12, 8, 8)
    )
}

# -- Figure dimensions for 16:9 slides --------------------------------------
FIG_WIDTH  <- 6.0
FIG_HEIGHT <- 3.8
FIG_DPI    <- 300

save_pres_figure <- function(plot, filename, width = FIG_WIDTH,
                              height = FIG_HEIGHT) {
  ggsave(filename, plot = plot, width = width, height = height,
         device = cairo_pdf, bg = "white")
  message("  Saved: ", filename)
}

# -- Sensitivity plot helper ------------------------------------------------
plot_sensitivity <- function(df, param_col, param_label,
                              y_label = "Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$",
                              title = NULL,
                              legend_fmt = NULL,
                              output_path = NULL) {

  param_vals <- sort(unique(df[[param_col]]))
  n_vals <- length(param_vals)
  df[[param_col]] <- factor(df[[param_col]], levels = param_vals)

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

  colors <- setNames(SENS_COLORS[seq_len(n_vals)], param_vals)
  ltypes <- setNames(SENS_LINETYPES[seq_len(n_vals)], param_vals)
  shapes <- setNames(SENS_SHAPES[seq_len(n_vals)], param_vals)

  p <- ggplot(df, aes(x = kappa, y = Delta_min,
                       colour = .data[[param_col]],
                       linetype = .data[[param_col]],
                       shape = .data[[param_col]])) +
    geom_line(linewidth = 1.0) +
    geom_point(size = 2.0) +
    scale_colour_manual(values = colors, labels = legend_labels) +
    scale_linetype_manual(values = ltypes, labels = legend_labels) +
    scale_shape_manual(values = shapes, labels = legend_labels) +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = TeX(y_label),
      title = if (!is.null(title)) TeX(title) else NULL
    ) +
    theme_pres() +
    theme(legend.position = "right")

  if (!is.null(output_path)) {
    save_pres_figure(p, output_path)
  }
  p
}

# -- Slope computation (central finite differences) --------------------------
compute_slopes <- function(kappa, y) {
  n <- length(kappa)
  slopes <- numeric(n)
  for (i in seq_len(n)) {
    if (i == 1) {
      slopes[i] <- (y[2] - y[1]) / (kappa[2] - kappa[1])
    } else if (i == n) {
      slopes[i] <- (y[n] - y[n - 1]) / (kappa[n] - kappa[n - 1])
    } else {
      slopes[i] <- (y[i + 1] - y[i - 1]) / (kappa[i + 1] - kappa[i - 1])
    }
  }
  slopes
}

# -- Kappa-dagger annotation helper ------------------------------------------
add_kappa_dagger <- function(p, kappa_peak, peak_y, colour = "#228833",
                              label_y = NULL, hjust = -0.3) {
  if (is.null(label_y)) label_y <- peak_y
  p +
    geom_vline(xintercept = kappa_peak, linetype = "dashed",
               colour = colour, linewidth = 0.5, alpha = 0.7) +
    annotate("point", x = kappa_peak, y = peak_y,
             shape = 18, size = 4, colour = colour) +
    annotate("text", x = kappa_peak, y = label_y,
             label = expression(kappa^dagger),
             size = 4.5, hjust = hjust, colour = colour, family = "serif")
}

message("theme_pres.R loaded successfully")
