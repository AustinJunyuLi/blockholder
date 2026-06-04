"""Master entry point: generate all manuscript figures from CSV data.

Usage:
    python -m pyfig.render_all [--data-dir DIR] [--output-dir DIR]
"""
from __future__ import annotations

import argparse
import os
import sys

from . import style
from .figures import ALL_FIGURES


def main(argv=None):
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap = argparse.ArgumentParser(description="Generate EVT-model figures (Python).")
    ap.add_argument("--data-dir",
                    default=os.path.join(here, "numerical_output", "data"))
    ap.add_argument("--output-dir",
                    default=os.path.join(here, "numerical_output"))
    args = ap.parse_args(argv)

    os.makedirs(args.output_dir, exist_ok=True)
    style.apply_style()

    print("=== EVT model: generating all Python/matplotlib figures ===")
    print(f"  data dir:   {args.data_dir}")
    print(f"  output dir: {args.output_dir}\n")

    failures = 0
    for fn in ALL_FIGURES:
        print(f"running {fn.__name__} ...")
        try:
            fn(args.data_dir, args.output_dir)
        except Exception as exc:  # report, continue (mirrors old render_all.R)
            failures += 1
            print(f"  ERROR in {fn.__name__}: {exc}")

    print(f"\n=== done: {len(ALL_FIGURES) - failures}/{len(ALL_FIGURES)} "
          f"figures generated ===")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
