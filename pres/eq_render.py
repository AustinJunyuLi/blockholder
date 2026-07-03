"""LaTeX equation rasterizer for the PPTX deck.

Renders every display equation used by make_pptx.py with the manuscript's
Computer Modern math (one xelatex + preview compile, then pdftocairo) into
transparent 600-dpi PNGs under pres/pptx_assets/eq/.

Sizing contract: equations are typeset at a 10pt base, so a PNG placed at
(pixel_size / 600) * (target_pt / 10) inches reproduces the equation at
target_pt on the slide. make_pptx.Deck.eq() applies this rule.

A manifest hash skips recompilation when the equation set is unchanged.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile

DPI = 600
BASE_PT = 10.0

# color name -> hex used inside the LaTeX doc
COLORS = {
    "ink": "212121",
    "grey": "5A5A5A",
    "navy": "1F3A5F",
    "white": "FFFFFF",
    "ice": "C9D6E8",
}

# key -> (color, latex math body). Notation mirrors pres/presentation.tex.
EQS: dict[str, tuple[str, str]] = {
    # headline objects
    "lam_white": ("white", r"\lambda \;=\; 1 \,-\, q\,(1-\gamma)\,\psi"),
    "lam": ("ink", r"\lambda \;=\; 1 \,-\, q\,(1-\gamma)\,\psi"),
    "wedge": ("ink", r"m_1 - m_0 \;=\; (1-\theta)\,\lambda\,\rho\,\Delta"),
    "ladder": ("ink", r"k_1 \;\le\; k_0 \;\le\; k_D"),
    "kdagger": ("navy", r"\kappa^{\dagger} \approx 0.59"),
    "range_cert": ("navy", r"\kappa \in [\,0.35,\;0.825\,]"),
    "sigxi": ("navy", r"\sigma_\xi = 0.60"),
    # feedback-loop nodes (slide 9)
    "node_X": ("white", r"X"),
    "node_belief": ("ink", r"\pi(X, D)"),
    "node_price": ("ink", r"P(X, D)"),
    "node_p": ("white", r"p"),
    # wedge legend symbols (slide 13)
    "sym_q": ("ink", r"q"),
    "sym_gamma": ("ink", r"\gamma"),
    "sym_psi": ("ink", r"\psi"),
    # posterior algebra (backup B3)
    "noise_cases": (
        "ink",
        r"z \;=\; \begin{cases} \;0 & \text{w.p. } 1-\kappa"
        r"\\[2pt] \pm 1 & \text{w.p. } \kappa/2 \text{ each}\end{cases}",
    ),
    "flow": ("ink", r"X \;=\; q + z, \qquad D \;=\; \mathbf{1}\{\,q = +1\,\}"),
    "post_p1": ("ink", r"\pi(1,0) \;=\; \frac{\omega_Q}{\omega_H + \omega_Q}"),
    "post_0": (
        "ink",
        r"\pi(0,0) \;=\; \frac{\omega_Q\,(1-\kappa)}"
        r"{(\omega_H + \omega_Q)\,(1-\kappa) \;+\; \omega_E\,\kappa/2}",
    ),
    "post_m1": (
        "ink",
        r"\pi(-1,0) \;=\; \frac{\omega_Q\,\kappa/2}"
        r"{(\omega_H + \omega_Q)\,\kappa/2 \;+\; \omega_E\,(1-\kappa)}",
    ),
    # regularity / certification (backups B1, B4, B5)
    "a5": ("ink", r"\delta\,\varphi(0)/\sigma_\xi \;=\; 0.947 \;<\; 1"),
    "neumann": (
        "ink",
        r"\bigl\|\,(I - D_k T)^{-1}\bigr\|_\infty \;\le\; \frac{1}{1-L}",
    ),
    # tender game (backup B6)
    "freerider": ("ink", r"\hat b^{\,*} \;=\; w + \gamma\,a\,\Delta + S_F - \varphi"),
    "block": ("ink", r"S_F - \varphi \;\ge\; (1-\gamma)\,a\,\Delta"),
    # calibration table symbols (backup B1)
    "cal_prior": ("ink", r"\mu,\ \sigma_v"),
    "cal_eps": ("ink", r"\sigma_\varepsilon"),
    "cal_delta": ("ink", r"\delta"),
    "cal_kappa": ("ink", r"\kappa"),
    "cal_cost": ("ink", r"C_0,\ \chi"),
    "cal_rho": ("ink", r"\rho,\ \Delta"),
    "cal_m": ("ink", r"m_0,\ m_1"),
    "cal_syn": ("ink", r"\bar S,\ K,\ \sigma_\xi"),
    # equilibrium table headers (backup B2)
    "th_D": ("ink", r"D"),
    "th_X": ("ink", r"X"),
    "th_P": ("ink", r"P"),
    "th_pi": ("ink", r"\pi"),
    "th_p": ("ink", r"p"),
    "th_mbar": ("ink", r"\bar m"),
}

_PREAMBLE = r"""\documentclass[10pt]{article}
\usepackage[active,tightpage]{preview}
\setlength\PreviewBorder{1.5pt}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
%s
\pagestyle{empty}
\begin{document}
"""


def _doc() -> str:
    defs = "\n".join(
        rf"\definecolor{{{n}}}{{HTML}}{{{h}}}" for n, h in COLORS.items()
    )
    lines = [_PREAMBLE % defs]
    for _, (color, body) in EQS.items():
        lines.append(
            "\\begin{preview}%\n"
            f"{{\\color{{{color}}}$\\displaystyle {body}$}}%\n"
            "\\end{preview}"
        )
    lines.append(r"\end{document}")
    return "\n".join(lines)


def _digest() -> str:
    payload = json.dumps({"eqs": EQS, "dpi": DPI}, sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()


def ensure_equations(assets_dir: str) -> dict[str, str]:
    """Render (or reuse) all equation PNGs; return key -> png path."""
    eq_dir = os.path.join(assets_dir, "eq")
    manifest = os.path.join(eq_dir, "manifest.json")
    paths = {k: os.path.join(eq_dir, f"{k}.png") for k in EQS}

    if os.path.exists(manifest):
        try:
            with open(manifest) as fh:
                if (json.load(fh).get("digest") == _digest()
                        and all(os.path.exists(p) for p in paths.values())):
                    return paths
        except (OSError, json.JSONDecodeError):
            pass

    os.makedirs(eq_dir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tex = os.path.join(tmp, "eqs.tex")
        with open(tex, "w") as fh:
            fh.write(_doc())
        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error",
             "-output-directory", tmp, tex],
            check=True, capture_output=True,
        )
        subprocess.run(
            ["pdftocairo", "-png", "-transp", "-r", str(DPI),
             os.path.join(tmp, "eqs.pdf"), os.path.join(tmp, "eq")],
            check=True,
        )
        # pdftocairo zero-pads page numbers based on page count
        pages = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
        if len(pages) != len(EQS):
            raise RuntimeError(
                f"equation render mismatch: {len(pages)} pages, {len(EQS)} keys")
        for page, key in zip(pages, EQS):
            shutil.move(os.path.join(tmp, page), paths[key])

    with open(manifest, "w") as fh:
        json.dump({"digest": _digest()}, fh)
    print(f"equations -> {eq_dir} ({len(EQS)} rendered)")
    return paths


_size_cache: dict[str, tuple[int, int]] = {}


def png_size(path: str) -> tuple[int, int]:
    """(width, height) in pixels, cached."""
    if path not in _size_cache:
        from PIL import Image

        with Image.open(path) as im:
            _size_cache[path] = im.size
    return _size_cache[path]


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    ensure_equations(os.path.join(here, "pptx_assets"))
