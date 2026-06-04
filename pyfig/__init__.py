"""Python figure package for the Exit-Voice-Takeover model.

Replaces the former R/ggplot2 visualization layer. The pipeline is now
Python end-to-end: numerical.export_data -> CSV -> pyfig -> PDF figures.

Public entry point: ``python -m pyfig.render_all --data-dir DIR --output-dir DIR``.
"""
