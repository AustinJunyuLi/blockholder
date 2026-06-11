"""Business-format slidepack: Liquidity, Activism Disclosure, and Takeover Premia.

Generates pres/blockholder_seminar_40min.pptx — a 40-minute business-styled
deck (decision-oriented headlines, figure-led, technical material in backups)
sharing its narrative spine with the academic Beamer deck
(quality_reports/plans/2026-06-11_slidepack-40min-design.md).

Figures are rasterized from the canonical PDFs (pres/figures + empirics/output)
to 300-dpi PNGs in pres/pptx_assets/ via pdftocairo. Fact 1/2 numbers are read
from empirics/output/*.csv at build time, so re-running after the event-study
refresh updates the evidence slides automatically.

Usage:
    .venv/bin/python pres/make_pptx.py
"""

from __future__ import annotations

import csv
import os
import subprocess

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = os.path.join(HERE, "pptx_assets")
OUT_PPTX = os.path.join(HERE, "blockholder_seminar_40min.pptx")

SLIDE_W, SLIDE_H = Inches(13.333), Inches(7.5)

# ── palette: strategy-consulting navy/charcoal chrome; Paul Tol muted
#    accents retained where they key to the figure layer ────────────────────
INK = RGBColor(0x21, 0x21, 0x21)     # charcoal body text
GREY = RGBColor(0x5A, 0x5A, 0x5A)    # support text
FAINT = RGBColor(0xF3, 0xF4, 0xF6)   # panel fill (cool light grey)
HAIR = RGBColor(0xC9, 0xCD, 0xD2)    # hairline rules
NAVY = RGBColor(0x1F, 0x3A, 0x5F)    # primary accent (kickers, bars, chips)
BLUE = NAVY                          # structural accent alias (legacy name)
DATABLUE = RGBColor(0x44, 0x77, 0xAA)  # series blue used inside figures
ROSE = RGBColor(0xEE, 0x66, 0x77)
TEAL = RGBColor(0x44, 0xAA, 0x99)
SAND = RGBColor(0xDD, 0xCC, 0x77)
CYAN = RGBColor(0x88, 0xCC, 0xEE)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "Helvetica Neue"

# figure PDFs to rasterize: (source path relative to ROOT, asset name)
# Shared manuscript figures come from numerical_output/ (canonical); the four
# slide-only variants from pres/figures/ (pyfig.slide_figures).
FIGS = [
    ("numerical_output/fig_nonmonotone.pdf", "nonmonotone"),
    ("numerical_output/fig_decomposition.pdf", "decomposition"),
    ("numerical_output/fig_wedge_primitives.pdf", "wedge"),
    ("numerical_output/fig_ge_decomposition.pdf", "ge_decomp"),
    ("pres/figures/fig_disclosure_slopes.pdf", "slopes"),
    ("numerical_output/fig_welfare.pdf", "welfare"),
    ("numerical_output/fig_cutoff_structure.pdf", "cutoffs"),
    ("numerical_output/fig_cutoffs_kappa.pdf", "cutoffs_kappa"),
    ("pres/figures/fig_sensitivity_panel1.pdf", "sens1"),
    ("pres/figures/fig_sensitivity_panel2.pdf", "sens2"),
    ("pres/figures/fig_noisy_rumor.pdf", "rumor"),
    ("empirics/output/fact1_delay.pdf", "fact1"),
    ("empirics/output/fact2_car.pdf", "fact2"),
]


def build_assets() -> None:
    os.makedirs(ASSETS, exist_ok=True)
    for rel, name in FIGS:
        src = os.path.join(ROOT, rel)
        dst = os.path.join(ASSETS, name)
        if not os.path.exists(src):
            print(f"  !! missing {rel} (slide will show a placeholder)")
            continue
        subprocess.run(
            ["pdftocairo", "-png", "-r", "300", "-singlefile", src, dst],
            check=True,
        )
    print(f"assets -> {ASSETS}")


# ── data hooks: evidence numbers read from the empirics outputs ─────────────

def fact1_numbers() -> dict:
    path = os.path.join(ROOT, "empirics/output/fact1_summary.csv")
    out = {"pre_med": "7", "post_med": "5", "pre_5bd": "36%", "post_5bd": "76%"}
    try:
        with open(path) as fh:
            for row in csv.DictReader(fh):
                if row["window"].startswith("pre"):
                    out["pre_med"] = f"{float(row['median']):.0f}"
                    out["pre_5bd"] = f"{100 * float(row['share_within_5bd']):.0f}%"
                else:
                    out["post_med"] = f"{float(row['median']):.0f}"
                    out["post_5bd"] = f"{100 * float(row['share_within_5bd']):.0f}%"
    except OSError:
        pass
    return out


def fact2_numbers() -> dict:
    """Headline coefficients from spec 2 on CAR[-1,+1]; em-dash until run."""
    path = os.path.join(ROOT, "empirics/output/fact2_regressions.csv")
    out = {"beta": "—", "beta_t": "—", "delta": "—", "delta_t": "—",
           "amihud": "—", "amihud_t": "—", "n": "—"}
    try:
        with open(path) as fh:
            for row in csv.DictReader(fh):
                if (row["spec"] == "2_interaction"
                        and row["depvar"] == "car_m1_p1"):
                    if row["param"] == "post":
                        out["beta"] = f"{float(row['coef']) * 100:+.2f}pp"
                        out["beta_t"] = f"t={float(row['t']):.2f}"
                        out["n"] = row["n"]
                    if row["param"] == "post_x_lnamihud":
                        out["delta"] = f"{float(row['coef']) * 100:+.2f}pp"
                        out["delta_t"] = f"t={float(row['t']):.2f}"
                    if row["param"] == "ln_amihud":
                        out["amihud"] = f"{float(row['coef']) * 100:+.2f}pp"
                        out["amihud_t"] = f"t={float(row['t']):.2f}"
    except OSError:
        pass
    return out


# ── slide toolkit ───────────────────────────────────────────────────────────

class Deck:
    def __init__(self):
        self.prs = Presentation()
        self.prs.slide_width = SLIDE_W
        self.prs.slide_height = SLIDE_H
        self.blank = self.prs.slide_layouts[6]
        self.n = 0

    def slide(self, kicker: str = "", headline: str = "", footer: bool = True):
        s = self.prs.slides.add_slide(self.blank)
        self.n += 1
        if kicker:
            tb = self._text(s, Inches(0.55), Inches(0.34), Inches(11), Inches(0.3))
            p = tb.paragraphs[0]
            r = p.add_run(); r.text = kicker.upper()
            f = r.font; f.name = FONT; f.size = Pt(12); f.bold = True
            f.color.rgb = NAVY
        if headline:
            tb = self._text(s, Inches(0.52), Inches(0.64), Inches(12.3), Inches(1.0))
            p = tb.paragraphs[0]
            r = p.add_run(); r.text = headline
            f = r.font; f.name = FONT; f.size = Pt(27); f.bold = True
            f.color.rgb = INK
        if kicker or headline:
            self.hairline(s, Inches(0.55), Inches(1.68), Inches(12.23))
        if footer:
            self.hairline(s, Inches(0.55), Inches(7.02), Inches(12.23))
            tb = self._text(s, Inches(0.55), Inches(7.08), Inches(9), Inches(0.3))
            p = tb.paragraphs[0]
            r = p.add_run()
            r.text = "Liquidity, Activism Disclosure, and Takeover Premia"
            f = r.font; f.name = FONT; f.size = Pt(8.5); f.color.rgb = GREY
            tb = self._text(s, Inches(12.45), Inches(7.08), Inches(0.6), Inches(0.3))
            p = tb.paragraphs[0]; p.alignment = PP_ALIGN.RIGHT
            r = p.add_run(); r.text = str(self.n)
            f = r.font; f.name = FONT; f.size = Pt(10); f.color.rgb = GREY
        return s

    def hairline(self, s, x, y, w, color=HAIR):
        # thin filled rectangle (not a connector: shadow-proof in all renderers)
        ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, Pt(0.75))
        ln.fill.solid(); ln.fill.fore_color.rgb = color
        ln.line.fill.background()
        ln.shadow.inherit = False
        return ln

    @staticmethod
    def _text(s, x, y, w, h):
        box = s.shapes.add_textbox(x, y, w, h)
        box.text_frame.word_wrap = True
        return box.text_frame

    def body(self, s, x, y, w, h, items, size=17, gap=6, color=INK):
        """items: list of str or (str, dict) with bold/color/size/level/space."""
        tf = self._text(s, x, y, w, h)
        first = True
        for it in items:
            txt, opt = (it, {}) if isinstance(it, str) else it
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            first = False
            p.space_after = Pt(opt.get("space", gap))
            p.level = opt.get("level", 0)
            for seg_txt, seg_bold, seg_col in _segments(txt, opt):
                r = p.add_run(); r.text = seg_txt
                f = r.font; f.name = FONT
                f.size = Pt(opt.get("size", size))
                f.bold = seg_bold
                f.color.rgb = seg_col if seg_col else opt.get("color", color)
        return tf

    def panel(self, s, x, y, w, h, fill=FAINT, line=None):
        shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        shp.adjustments[0] = 0.045
        shp.fill.solid(); shp.fill.fore_color.rgb = fill
        if line is None:
            shp.line.fill.background()
        else:
            shp.line.color.rgb = line; shp.line.width = Pt(1.0)
        shp.shadow.inherit = False
        return shp

    def chip(self, s, x, y, w, h, text, fill=BLUE, color=WHITE, size=14,
             bold=True, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
        shp = s.shapes.add_shape(shape, x, y, w, h)
        if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
            shp.adjustments[0] = 0.18
        shp.fill.solid(); shp.fill.fore_color.rgb = fill
        shp.line.fill.background(); shp.shadow.inherit = False
        tf = shp.text_frame; tf.word_wrap = True
        tf.margin_left = tf.margin_right = Pt(6)
        tf.margin_top = tf.margin_bottom = Pt(3)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        for i, line_txt in enumerate(text.split("\n")):
            pp = p if i == 0 else tf.add_paragraph()
            pp.alignment = PP_ALIGN.CENTER
            r = pp.add_run(); r.text = line_txt
            f = r.font; f.name = FONT; f.size = Pt(size); f.bold = bold
            f.color.rgb = color
        return shp

    def arrow(self, s, x1, y1, x2, y2, color=GREY, w=Pt(2.2)):
        conn = s.shapes.add_connector(2, x1, y1, x2, y2)  # straight
        conn.line.color.rgb = color; conn.line.width = w
        le = conn.line._get_or_add_ln()
        import copy
        from pptx.oxml.ns import qn
        head = le.makeelement(qn("a:tailEnd"), {"type": "triangle", "w": "med",
                                                "len": "med"})
        le.append(copy.deepcopy(head))
        return conn

    def picture(self, s, name, x, y, w=None, h=None):
        path = os.path.join(ASSETS, f"{name}.png")
        if not os.path.exists(path):
            ph = self.panel(s, x, y, w or Inches(6), h or Inches(4), fill=FAINT)
            tf = ph.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
            r = p.add_run(); r.text = f"[figure: {name}]"
            r.font.name = FONT; r.font.size = Pt(14); r.font.color.rgb = GREY
            return ph
        return s.shapes.add_picture(path, x, y, width=w, height=h)

    def caption(self, s, x, y, w, text, size=12):
        tf = self._text(s, x, y, w, Inches(0.5))
        p = tf.paragraphs[0]
        r = p.add_run(); r.text = text
        f = r.font; f.name = FONT; f.size = Pt(size); f.color.rgb = GREY


def _segments(txt: str, opt: dict):
    """'**bold**' segments inside a string; returns (text, bold, color)."""
    base_bold = opt.get("bold", False)
    parts = txt.split("**")
    out = []
    for i, seg in enumerate(parts):
        if seg == "":
            continue
        out.append((seg, base_bold or (i % 2 == 1), None))
    return out or [("", base_bold, None)]


# ── deck assembly ───────────────────────────────────────────────────────────

def build() -> None:
    d = Deck()
    f1 = fact1_numbers()
    f2 = fact2_numbers()

    # 1 ── title ────────────────────────────────────────────────────────────
    s = d.slide(footer=False)
    bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(2.10),
                             Inches(0.18), Inches(2.6))
    bar.fill.solid(); bar.fill.fore_color.rgb = BLUE
    bar.line.fill.background(); bar.shadow.inherit = False
    tf = d._text(s, Inches(0.75), Inches(2.15), Inches(11.8), Inches(1.9))
    p = tf.paragraphs[0]
    r = p.add_run(); r.text = "Liquidity, Activism Disclosure,"
    r.font.name = FONT; r.font.size = Pt(44); r.font.bold = True
    r.font.color.rgb = INK
    p2 = tf.add_paragraph()
    r = p2.add_run(); r.text = "and Takeover Premia"
    r.font.name = FONT; r.font.size = Pt(44); r.font.bold = True
    r.font.color.rgb = INK
    p3 = tf.add_paragraph(); p3.space_before = Pt(16)
    r = p3.add_run()
    r.text = "When can the market see an activist coming — and who pockets the premium?"
    r.font.name = FONT; r.font.size = Pt(20); r.font.color.rgb = GREY
    tf = d._text(s, Inches(0.75), Inches(5.6), Inches(10), Inches(0.8))
    p = tf.paragraphs[0]
    r = p.add_run(); r.text = "Austin Li   ·   University College London"
    r.font.name = FONT; r.font.size = Pt(16); r.font.color.rgb = INK

    # 2 ── the takeaway up front ────────────────────────────────────────────
    s = d.slide("Executive summary", "Three things to take away")
    claims = [
        ("1", "Liquidity has a sweet spot",
         "Takeover gains for minority shareholders are **hump-shaped** in market "
         "liquidity: noise lets bidders in, but too much noise destroys the "
         "market's ability to price activism.", BLUE),
        ("2", "Who pockets the premium is tender mechanics",
         "The activist premium is pinned by a free-rider tender game: "
         "appropriability λ = 1 − q(1−γ)ψ. Low λ explains why estimated "
         "premia can **fall** when activists show up.", TEAL),
        ("3", "Disclosure law is a market-design lever",
         "Stake-triggered disclosure attenuates the liquidity effect — and "
         "stricter rules can **backfire** by killing quiet engagement. The 2024 "
         "SEC acceleration moved exactly this margin.", ROSE),
    ]
    x = Inches(0.55)
    for num, head, body, col in claims:
        d.panel(s, x, Inches(1.85), Inches(4.0), Inches(4.6))
        d.chip(s, x + Inches(0.25), Inches(2.10), Inches(0.55), Inches(0.55),
               num, fill=col, size=20, shape=MSO_SHAPE.OVAL)
        d.body(s, x + Inches(0.22), Inches(2.80), Inches(3.6), Inches(1.15),
               [(head, {"bold": True, "size": 16.5})])
        d.body(s, x + Inches(0.22), Inches(3.95), Inches(3.6), Inches(2.35),
               [(body, {"size": 13.5})], color=INK)
        x += Inches(4.22)

    # 3 ── why care ─────────────────────────────────────────────────────────
    s = d.slide("Motivation", "Activist returns ride the takeover channel")
    d.panel(s, Inches(0.55), Inches(1.9), Inches(5.7), Inches(4.5), fill=FAINT)
    tf = d._text(s, Inches(0.85), Inches(2.3), Inches(5.1), Inches(2.2))
    p = tf.paragraphs[0]
    r = p.add_run(); r.text = "~65%"
    r.font.name = FONT; r.font.size = Pt(60); r.font.bold = True
    r.font.color.rgb = BLUE
    d.body(s, Inches(0.85), Inches(3.6), Inches(5.1), Inches(2.5), [
        ("of activist hedge-fund returns are tied to M&A outcomes "
         "(Brav–Jiang–Partnoy–Thomas 2008).", {"size": 16}),
        ("Targets are acquired at significant premia; activists profit "
         "primarily through the takeover exit (Greenwood–Schor 2009).",
         {"size": 16}),
    ])
    d.body(s, Inches(6.7), Inches(2.0), Inches(6.1), Inches(4.6), [
        ("So the question that prices an activist position is:",
         {"size": 17, "space": 10}),
        ("does a takeover arrive, and at what premium?",
         {"bold": True, "size": 22, "space": 14}),
        ("Both depend on what the market can infer about engagement "
         "before anything is announced — i.e., on **trading conditions** "
         "and **disclosure rules**.", {"size": 17, "space": 10}),
        ("Informed trading moves prices ahead of 13D filings "
         "(Collin-Dufresne–Fos 2015): the market is watching order flow.",
         {"size": 15, "color": GREY}),
    ])

    # 4 ── the two levers ───────────────────────────────────────────────────
    s = d.slide("Motivation", "Two policy levers, one information problem")
    d.chip(s, Inches(0.8), Inches(2.0), Inches(5.6), Inches(0.62),
           "LIQUIDITY — can you trade unseen?", fill=BLUE, size=16)
    d.body(s, Inches(0.8), Inches(2.8), Inches(5.6), Inches(3.4), [
        ("Noise trading is **camouflage**: it lets a blockholder accumulate "
         "or exit without moving the price.", {"size": 16}),
        ("But camouflage cuts both ways — it also stops the market from "
         "**seeing value being created**.", {"size": 16}),
        ("Tick sizes, dark pools, retail flow, index churn: all shift this "
         "dial. Regulators move it constantly.", {"size": 15, "color": GREY}),
    ])
    d.chip(s, Inches(6.95), Inches(2.0), Inches(5.6), Inches(0.62),
           "DISCLOSURE — when must you show your hand?", fill=TEAL, size=16)
    d.body(s, Inches(6.95), Inches(2.8), Inches(5.6), Inches(3.4), [
        ("Schedule 13D: crossing **5%** with intent forces a public filing — "
         "engagement becomes observable.", {"size": 16}),
        ("Below the trigger, engagement can only be **inferred** from order "
         "flow. The rule partitions the information regime.", {"size": 16}),
        ("US window: 10 calendar days → **5 business days** (Feb 2024). "
         "UK: 3% / 2 days. The lever is live.", {"size": 15, "color": GREY}),
    ])

    # 5 ── 2024 timeline ────────────────────────────────────────────────────
    s = d.slide("Motivation", "2024: the SEC halved the clock")
    y = Inches(3.0)
    d.arrow(s, Inches(0.9), y, Inches(12.4), y, color=GREY, w=Pt(2.5))
    marks = [
        (Inches(1.6), "1968", "Williams Act:\n13D regime born", FAINT, INK),
        (Inches(4.6), "2011–22", "Petitions & debate:\n10-day gap criticized", FAINT, INK),
        (Inches(7.6), "Oct 2023", "Rule 33-11253 adopted", CYAN, INK),
        (Inches(10.6), "Feb 5, 2024", "5 business days\nin force", BLUE, WHITE),
    ]
    for x, when, what, fill, txtcol in marks:
        tick = s.shapes.add_shape(MSO_SHAPE.OVAL, x - Inches(0.07),
                                  y - Inches(0.07), Inches(0.14), Inches(0.14))
        tick.fill.solid(); tick.fill.fore_color.rgb = INK
        tick.line.fill.background(); tick.shadow.inherit = False
        d.body(s, x - Inches(0.9), y - Inches(0.75), Inches(1.9), Inches(0.4),
               [(when, {"bold": True, "size": 14})])
        d.chip(s, x - Inches(1.05), y + Inches(0.25), Inches(2.1), Inches(0.95),
               what, fill=fill, color=txtcol, size=12, bold=False)
    d.body(s, Inches(0.9), Inches(5.1), Inches(11.6), Inches(1.6), [
        ("A regulator just compressed the **pre-disclosure accumulation "
         "window** — the exact margin this framework prices.",
         {"size": 18, "bold": False}),
        ("That makes the theory testable now: filings, returns, and "
         "liquidity around 2024-02-05 are the natural experiment.",
         {"size": 16, "color": GREY}),
    ])

    # 6 ── the question ─────────────────────────────────────────────────────
    s = d.slide("Motivation", "", footer=True)
    d.panel(s, Inches(1.1), Inches(2.3), Inches(11.1), Inches(2.6), fill=FAINT)
    tf = d._text(s, Inches(1.6), Inches(2.8), Inches(10.1), Inches(1.8))
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = ("How do market liquidity and disclosure rules shape the takeover "
              "premia that minority shareholders receive?")
    r.font.name = FONT; r.font.size = Pt(28); r.font.bold = True
    r.font.color.rgb = INK
    d.body(s, Inches(1.6), Inches(5.3), Inches(10.4), Inches(1.2), [
        ("A single equilibrium framework: a blockholder who can exit, hold, or "
         "engage — quietly or publicly — a market pricing order flow, and a "
         "bidder reading both.", {"size": 16, "color": GREY}),
    ])

    # 6b ── positioning vs the literature (mirrors the Beamer positioning
    #       frames: three strands + the structural activism trio) ───────────
    s = d.slide("Positioning", "Three literatures, one missing piece")
    cols = [
        ("EXIT vs VOICE", "Blockholder governance: liquidity both "
         "disciplines (cheap accumulation) and tempts exit.\n"
         "Hirschman 1970; Maug 1998; Edmans 2009", ROSE),
        ("INFORMED TRADING", "Microstructure: order flow moves prices; "
         "noise is camouflage.\nKyle 1985; Glosten–Milgrom 1985", CYAN),
        ("TAKEOVER FEEDBACK", "Prices feed back into real decisions — "
         "including bids.\nGrossman–Hart 1980; Edmans–Goldstein–Jiang 2015",
         TEAL),
    ]
    x = Inches(0.7)
    for head, body_txt, col in cols:
        d.chip(s, x, Inches(2.0), Inches(3.9), Inches(0.55), head, fill=col,
               color=INK if col in (SAND, CYAN) else WHITE, size=14)
        main, _, cites = body_txt.partition("\n")
        d.body(s, x + Inches(0.05), Inches(2.75), Inches(3.8), Inches(2.2), [
            (main, {"size": 14.5, "space": 8}),
            (cites, {"size": 11.5, "color": GREY}),
        ])
        x += Inches(4.05)
    d.panel(s, Inches(0.7), Inches(5.15), Inches(12.0), Inches(1.5), fill=FAINT)
    d.body(s, Inches(0.95), Inches(5.35), Inches(11.5), Inches(1.2), [
        ("Closest trio: Ordóñez-Calafí & Bernhardt 2022 (threshold design), "
         "Corum & Levit 2019 (activists as bidder catalysts), Cetemen et al. "
         "2026 (dynamic trade timing).", {"size": 14, "color": GREY,
                                          "space": 6}),
        ("**This paper:** stake-triggered disclosure partitions order-flow "
         "inference into disclosed and nondisclosed branches — and that "
         "inference feeds endogenous bidder entry.", {"size": 15.5}),
    ])

    # 7 ── framework in one picture ─────────────────────────────────────────
    s = d.slide("Framework", "The model in one picture")
    stages = [
        ("NATURE", "Value v drawn;\nblockholder sees\nprivate signal s", FAINT, INK),
        ("TRADING", "Chooses action;\nnoise traders mix in;\nmarket prices order flow", BLUE, WHITE),
        ("ENTRY", "Bidder reads price &\ndisclosure, decides\nwhether to bid", TEAL, WHITE),
        ("PAYOFFS", "Takeover premium\nor standalone value", FAINT, INK),
    ]
    x = Inches(0.7)
    for i, (head, body, fill, col) in enumerate(stages):
        d.chip(s, x, Inches(2.2), Inches(2.55), Inches(0.55), head,
               fill=INK if fill is FAINT else fill, color=WHITE, size=14)
        d.chip(s, x, Inches(2.95), Inches(2.55), Inches(1.7), body,
               fill=FAINT, color=INK, size=13, bold=False)
        if i < 3:
            d.arrow(s, x + Inches(2.62), Inches(3.05), x + Inches(3.02),
                    Inches(3.05), color=GREY)
        x += Inches(3.1)
    d.body(s, Inches(0.7), Inches(5.2), Inches(12), Inches(1.6), [
        ("One round of trading, one potential bidder — the cleanest lab for the "
         "question. κ = share of noise trades (the liquidity dial).",
         {"size": 16}),
        ("Crucially, the bidder **conditions on the price**: information flows "
         "from trading to takeover entry. That feedback loop is the engine.",
         {"size": 16}),
    ])

    # 8 ── the four plays ───────────────────────────────────────────────────
    s = d.slide("Framework", "The blockholder's four plays")
    plays = [
        ("EXIT", "Sell the stake", "Weakest signals:\ncash out before bad news",
         ROSE, Inches(0.7)),
        ("HOLD", "Stay passive", "Middling signals:\nnot worth the\nengagement cost",
         SAND, Inches(3.85)),
        ("QUIET VOICE", "Engage privately", "Good signals:\nimprove the firm\nbelow the radar",
         CYAN, Inches(7.0)),
        ("PUBLIC VOICE", "Buy + engage + file", "Best signals:\nscale up and\ntrigger disclosure",
         TEAL, Inches(10.15)),
    ]
    for head, sub, body, col, x in plays:
        d.panel(s, x, Inches(1.95), Inches(2.85), Inches(3.5), fill=FAINT)
        d.chip(s, x + Inches(0.18), Inches(2.15), Inches(2.5), Inches(0.55),
               head, fill=col, color=INK if col in (SAND, CYAN) else WHITE,
               size=14)
        d.body(s, x + Inches(0.18), Inches(2.85), Inches(2.5), Inches(0.5),
               [(sub, {"bold": True, "size": 14})])
        d.body(s, x + Inches(0.18), Inches(3.35), Inches(2.5), Inches(1.9),
               [(body, {"size": 13})], color=INK)
    d.arrow(s, Inches(1.2), Inches(5.85), Inches(12.2), Inches(5.85),
            color=GREY, w=Pt(2.0))
    d.body(s, Inches(0.7), Inches(6.0), Inches(11.5), Inches(0.5), [
        ("private signal s →  the equilibrium is a ladder of cutoffs "
         "k₁ ≤ k₀ ≤ k_D  (a theorem, not an assumption)", {"size": 14,
         "color": GREY}),
    ])

    # 9 ── the feedback loop ────────────────────────────────────────────────
    s = d.slide("Framework", "Why liquidity matters twice")
    nodes = [
        ("Order flow X", Inches(0.8), BLUE, WHITE),
        ("Market belief\nπ(X, D)", Inches(3.95), CYAN, INK),
        ("Price P(X, D)", Inches(7.1), SAND, INK),
        ("Bid entry p", Inches(10.25), TEAL, WHITE),
    ]
    for txt, x, fill, col in nodes:
        d.chip(s, x, Inches(2.6), Inches(2.4), Inches(1.0), txt, fill=fill,
               color=col, size=15)
        if x < Inches(10):
            d.arrow(s, x + Inches(2.47), Inches(3.1), x + Inches(3.88),
                    Inches(3.1), color=GREY)
    d.body(s, Inches(0.8), Inches(4.1), Inches(12), Inches(2.6), [
        ("**Noise as cover (+):** more noise → lower prices on average → "
         "takeovers get cheaper → more bids arrive.", {"size": 16.5,
         "space": 8}),
        ("**Noise as fog (−):** more noise → order flow says less about "
         "engagement → the activism premium the market can price **erodes**.",
         {"size": 16.5, "space": 8}),
        ("Disclosure (D = 1) bypasses the fog entirely — engagement is "
         "observed, not inferred. That asymmetry drives the policy results.",
         {"size": 15, "color": GREY}),
    ])

    # 10 ── two regimes ─────────────────────────────────────────────────────
    s = d.slide("Framework", "What the market sees: two information regimes")
    d.chip(s, Inches(0.8), Inches(2.0), Inches(5.7), Inches(0.6),
           "QUIET (D = 0) — inference", fill=CYAN, color=INK, size=15)
    d.body(s, Inches(0.8), Inches(2.8), Inches(5.7), Inches(3.2), [
        ("Engagement is **guessed from order flow**.", {"size": 16}),
        ("Liquidity κ governs how good the guess is.", {"size": 16}),
        ("Hold and quiet voice look identical in the tape — by design.",
         {"size": 15, "color": GREY}),
    ])
    d.chip(s, Inches(6.95), Inches(2.0), Inches(5.7), Inches(0.6),
           "PUBLIC (D = 1) — observation", fill=TEAL, size=15)
    d.body(s, Inches(6.95), Inches(2.8), Inches(5.7), Inches(3.2), [
        ("The 13D filing makes engagement **public**.", {"size": 16}),
        ("Prices stop depending on κ at all.", {"size": 16}),
        ("Disclosure is an information-regime switch, not just paperwork.",
         {"size": 15, "color": GREY}),
    ])
    d.body(s, Inches(0.8), Inches(6.1), Inches(11.8), Inches(0.6), [
        ("The disclosure rule decides **how much of the market lives in each "
         "regime** — that is what makes it a design object.", {"size": 16}),
    ])

    # 11 ── result 1: the hump ──────────────────────────────────────────────
    s = d.slide("Results · 1", "Liquidity has a sweet spot")
    d.picture(s, "nonmonotone", Inches(0.55), Inches(1.9), w=Inches(6.2))
    d.body(s, Inches(7.9), Inches(2.0), Inches(4.9), Inches(4.4), [
        ("Expected takeover gains to minority shareholders are "
         "**hump-shaped** in liquidity.", {"size": 17, "space": 10}),
        ("Too little noise: bidders stay away — prices are too informative, "
         "deals too expensive.", {"size": 15.5}),
        ("Too much noise: bids come, but the **activism premium** the market "
         "can price has evaporated.", {"size": 15.5}),
        ("The peak κ† ≈ 0.59: cover and visibility in balance.",
         {"size": 15.5, "bold": False}),
    ])
    d.caption(s, Inches(0.55), Inches(6.55), Inches(7),
              "Minority takeover gains Δ-min vs noise-trading intensity κ; baseline calibration.")

    # 12 ── why: decomposition ──────────────────────────────────────────────
    s = d.slide("Results · 1", "Why: cover vs camouflage, in one split")
    d.picture(s, "decomposition", Inches(0.55), Inches(1.9), w=Inches(6.2))
    d.body(s, Inches(7.9), Inches(2.0), Inches(4.9), Inches(4.4), [
        ("Split the gains into two books:", {"size": 16, "space": 8}),
        ("**Base book** — premium that arrives regardless of activism. "
         "Rises with noise: cover brings bids.", {"size": 15.5}),
        ("**Activism book** — premium tied to the market believing engagement "
         "is happening. Hump-shaped: inference dies with noise.",
         {"size": 15.5}),
        ("The activism book's peak sets the overall sweet spot.",
         {"size": 15.5}),
    ])
    d.caption(s, Inches(0.55), Inches(6.55), Inches(7),
              "Decomposition of Δ-min into base and activism components across κ.")

    # 13 ── result 2: the wedge ─────────────────────────────────────────────
    s = d.slide("Results · 2", "Who captures the prize: tender-game arithmetic")
    d.picture(s, "wedge", Inches(0.55), Inches(1.9), w=Inches(7.0))
    d.panel(s, Inches(7.9), Inches(1.95), Inches(4.9), Inches(1.5), fill=FAINT)
    tf = d._text(s, Inches(8.15), Inches(2.18), Inches(4.4), Inches(1.1))
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = "λ = 1 − q(1−γ)ψ"
    r.font.name = FONT; r.font.size = Pt(26); r.font.bold = True
    r.font.color.rgb = INK
    p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER
    r = p2.add_run()
    r.text = "how much of the improvement the activist's side keeps"
    r.font.name = FONT; r.font.size = Pt(12); r.font.color.rgb = GREY
    d.body(s, Inches(7.9), Inches(3.7), Inches(4.9), Inches(2.9), [
        ("q — chance a rival raider shows up", {"size": 14.5}),
        ("γ — does the improvement survive a change of control?",
         {"size": 14.5}),
        ("ψ — can the bloc's stake block the raid?", {"size": 14.5}),
        ("Derived from a free-rider tender game — not assumed. "
         "Premium wedge: m₁ − m₀ = (1−θ)λρΔ.", {"size": 14.5,
         "color": GREY, "space": 4}),
    ])
    d.caption(s, Inches(0.55), Inches(6.55), Inches(7),
              "Appropriability λ across game primitives (q, γ, ψ).")

    # 14 ── result 2b: negative premia reconciled ───────────────────────────
    s = d.slide("Results · 2", "The puzzle this solves: premia that fall on arrival")
    d.body(s, Inches(0.7), Inches(1.95), Inches(5.9), Inches(4.4), [
        ("Structural estimates (Celentano–Levine 2025) find bid premia "
         "**13.7% lower** with an activist in the deal.", {"size": 17,
         "space": 10}),
        ("Contradiction with 'activism creates value'? No.", {"size": 16,
         "space": 8}),
        ("The measured premium divides the offer by a market price that "
         "**already banks** the activist's work (AFS 2022: 13D returns are "
         "~3/4 anticipated treatment).", {"size": 16, "space": 8}),
        ("When appropriability λ is low, the denominator outruns the "
         "numerator: measured premia fall even though the true wedge "
         "m₁ ≥ m₀ never flips.", {"size": 16}),
    ])
    d.panel(s, Inches(7.0), Inches(2.0), Inches(5.6), Inches(4.2), fill=FAINT)
    d.body(s, Inches(7.3), Inches(2.25), Inches(5.0), Inches(3.8), [
        ("What our wedge adds vs the board-bargaining story:",
         {"bold": True, "size": 15, "space": 8}),
        ("Their effect moves only with activist **presence**.", {"size": 14.5}),
        ("Ours is indexed by **observables**: acquirer type (γ), rival "
         "pressure (q), stake pivotality (ψ), liquidity (κ).", {"size": 14.5}),
        ("→ It predicts **where the sign flips**: portable improvements, "
         "pivotal blocs, cold fringe markets.", {"size": 14.5, "space": 4}),
        ("Different cross-sections, testable against each other.",
         {"size": 14, "color": GREY}),
    ])

    # 15 ── result 3: when a theorem ────────────────────────────────────────
    s = d.slide("Results · 3", "How robust is the sweet spot? Now a theorem — with edges")
    d.picture(s, "ge_decomp", Inches(0.55), Inches(1.9), w=Inches(7.0))
    d.body(s, Inches(7.9), Inches(2.0), Inches(4.9), Inches(4.5), [
        ("On a **certified range** of the liquidity dial (κ from 0.35 to "
         "0.825), the hump is a theorem: equilibrium feedback provably "
         "cannot overturn it.", {"size": 15.5, "space": 8}),
        ("Outside it, the warning is real: when bidders barely react to "
         "premia (σ_ξ = 0.60), the hump **inverts into a trough** — "
         "certified, not hypothetical.", {"size": 15.5, "space": 8}),
        ("Practical read: the liquidity sweet spot is strongest where "
         "takeover entry is most sensitive to expected resistance.",
         {"size": 15, "color": GREY}),
    ])
    d.caption(s, Inches(0.55), Inches(6.55), Inches(7),
              "GE channel decomposition; certified region and the σ_ξ = 0.60 inversion.")

    # 16 ── disclosure attenuates ───────────────────────────────────────────
    s = d.slide("Results · 4", "Disclosure turns the liquidity dial down")
    d.picture(s, "slopes", Inches(0.55), Inches(1.9), w=Inches(7.0))
    d.body(s, Inches(7.9), Inches(2.0), Inches(4.9), Inches(4.4), [
        ("Disclosed states don't depend on liquidity — so the more "
         "engagement happens in public, the **flatter** the "
         "liquidity–premium relationship.", {"size": 16, "space": 10}),
        ("Disclosure and liquidity are **substitute** information channels.",
         {"size": 16, "space": 10}),
        ("Cross-market prediction: tighter regimes (UK 3%/2-day) should show "
         "**muted** liquidity sensitivity vs the US.", {"size": 15.5}),
    ])
    d.caption(s, Inches(0.55), Inches(6.55), Inches(7),
              "Sensitivity of activism gains to κ under baseline vs stricter disclosure.")

    # 17 ── the policy paradox ──────────────────────────────────────────────
    s = d.slide("Results · 4", "The transparency paradox")
    d.chip(s, Inches(0.8), Inches(2.1), Inches(5.7), Inches(0.6),
           "TRANSPARENCY (+)", fill=TEAL, size=15)
    d.body(s, Inches(0.8), Inches(2.9), Inches(5.7), Inches(2.9), [
        ("Stricter disclosure reveals engagement → market prices activism "
         "→ minorities share the gains.", {"size": 16}),
        ("Dominates when engagement is cheap and liquidity moderate.",
         {"size": 15, "color": GREY}),
    ])
    d.chip(s, Inches(6.95), Inches(2.1), Inches(5.7), Inches(0.6),
           "DETERRENCE (−)", fill=ROSE, size=15)
    d.body(s, Inches(6.95), Inches(2.9), Inches(5.7), Inches(2.9), [
        ("Forced visibility kills **quiet voice**: the blockholder exits "
         "rather than tip a bidder-deterring hand.", {"size": 16}),
        ("Dominates when engagement is costly — minorities end up worse off.",
         {"size": 15, "color": GREY}),
    ])
    d.panel(s, Inches(0.8), Inches(5.45), Inches(11.85), Inches(1.15),
            fill=FAINT)
    d.body(s, Inches(1.05), Inches(5.7), Inches(11.4), Inches(0.8), [
        ("Disclosure reform that ignores deterrence can **destroy the channel "
         "it is trying to illuminate** — the model says when.",
         {"size": 17, "bold": False}),
    ])

    # 18 ── evidence 1 ──────────────────────────────────────────────────────
    s = d.slide("Evidence · 1", "The clock bit: filings sped up immediately")
    d.picture(s, "fact1", Inches(0.55), Inches(1.9), w=Inches(7.0))
    d.panel(s, Inches(7.9), Inches(2.0), Inches(4.9), Inches(2.5), fill=FAINT)
    tf = d._text(s, Inches(8.15), Inches(2.25), Inches(4.4), Inches(2.0))
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = f"median {f1['pre_med']} → {f1['post_med']} days"
    r.font.name = FONT; r.font.size = Pt(24); r.font.bold = True
    r.font.color.rgb = BLUE
    p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(10)
    r = p2.add_run()
    r.text = f"filed within 5 business days:\n{f1['pre_5bd']} → {f1['post_5bd']}"
    r.font.name = FONT; r.font.size = Pt(17); r.font.color.rgb = INK
    d.body(s, Inches(7.9), Inches(4.8), Inches(4.9), Inches(1.7), [
        ("Universe of original 13Ds on EDGAR, windows straddling the "
         "2024-02-05 compliance date.", {"size": 14, "color": GREY}),
        ("The accumulation window — the model's quiet-trading cover — "
         "shrank by force of law.", {"size": 14.5}),
    ])

    # 19 ── evidence 2 ──────────────────────────────────────────────────────
    s = d.slide("Evidence · 2", "The market noticed: announcement returns moved")
    d.picture(s, "fact2", Inches(0.55), Inches(1.9), w=Inches(7.0))
    d.body(s, Inches(7.9), Inches(2.0), Inches(4.9), Inches(2.2), [
        ("Market-model CARs around 1,513 original 13D filings, 2022–2025; "
         "Post = filed under the 5-day rule.", {"size": 14.5, "space": 8}),
        ("Mean CAR[−1,+1] **doubles** post-rule (0.85% → 1.71%; sign as "
         "predicted, not significant). Surprises concentrate in **liquid** "
         "names — the camouflage margin is first-order. The Post×illiquidity "
         "interaction is a precise null.", {"size": 15}),
    ])
    d.panel(s, Inches(7.9), Inches(4.35), Inches(4.9), Inches(2.05), fill=FAINT)
    d.body(s, Inches(8.15), Inches(4.55), Inches(4.4), Inches(1.7), [
        (f"β (Post): {f2['beta']}   ({f2['beta_t']})", {"size": 15.5,
         "bold": True}),
        (f"ln Amihud: {f2['amihud']}   ({f2['amihud_t']})",
         {"size": 15.5, "bold": True}),
        (f"δ (Post × ln Amihud): {f2['delta']}   ({f2['delta_t']})",
         {"size": 15.5, "bold": True}),
        (f"n = {f2['n']} events · two-way clustered SEs",
         {"size": 12.5, "color": GREY}),
    ])

    # 20 ── policy meaning ──────────────────────────────────────────────────
    s = d.slide("Implications", "For policy: liquidity regulation is governance policy")
    d.body(s, Inches(0.7), Inches(2.0), Inches(11.9), Inches(4.4), [
        ("Anything that moves noise trading — tick size regimes, dark-pool "
         "rules, PFOF, index flows — **also moves takeover discipline**. The "
         "two rulebooks are one.", {"size": 18, "space": 12}),
        ("Disclosure thresholds and windows are not transparency knobs alone: "
         "they reallocate engagement between quiet and public — and can "
         "**deter it outright**.", {"size": 18, "space": 12}),
        ("The 2024 acceleration traded camouflage for visibility. The model "
         "prices that trade; the early data move the predicted way.",
         {"size": 18, "space": 12}),
        ("Welfare caveat: the κ that maximizes minority gains is **not** the "
         "social optimum — extraction deters some efficient deals.",
         {"size": 15, "color": GREY}),
    ])

    # 21 ── investor meaning ────────────────────────────────────────────────
    s = d.slide("Implications", "For investors: where activism pays")
    rows = [
        ("Screen on liquidity", "Activist targets in **mid-liquidity** names "
         "carry the largest expected takeover kicker — both tails are weak.",
         BLUE),
        ("Read the wedge", "Premium capture is largest with portable "
         "improvements (high γ), pivotal blocs (ψ), and few rival raiders "
         "(low q).", TEAL),
        ("Mind the regime", "Post-2024, filing-day surprises are larger on "
         "average — and they are largest in liquid names, where quiet "
         "accumulation hides best.", ROSE),
    ]
    y = Inches(2.0)
    for head, body, col in rows:
        d.chip(s, Inches(0.8), y, Inches(3.1), Inches(0.95), head, fill=col,
               color=WHITE, size=15)
        d.body(s, Inches(4.2), y + Inches(0.06), Inches(8.4), Inches(1.2),
               [(body, {"size": 16})])
        y += Inches(1.45)
    d.body(s, Inches(0.8), Inches(6.35), Inches(11.5), Inches(0.5), [
        ("All three are cross-sectional, sign-testable statements — not "
         "calibration folklore.", {"size": 14, "color": GREY}),
    ])

    # 22 ── where this goes ─────────────────────────────────────────────────
    s = d.slide("Roadmap", "Where this goes next")
    steps = [
        ("Now", "Theory + certified numerics + two facts from the 2024 "
         "natural experiment", BLUE),
        ("Next", "Full event-study cross-sections: premia, bid hazards, and "
         "liquidity interactions on the 13D universe", TEAL),
        ("Then", "Structural leg: estimate the engagement-cost distribution "
         "from 13D XML microdata — the white space the structural trio "
         "left open", ROSE),
    ]
    x = Inches(0.7)
    for when, what, col in steps:
        d.panel(s, x, Inches(2.1), Inches(3.95), Inches(3.4), fill=FAINT)
        d.chip(s, x + Inches(0.25), Inches(2.35), Inches(1.3), Inches(0.5),
               when, fill=col, size=14)
        d.body(s, x + Inches(0.25), Inches(3.05), Inches(3.45), Inches(2.3),
               [(what, {"size": 15})])
        x += Inches(4.17)
    d.body(s, Inches(0.7), Inches(5.9), Inches(11.9), Inches(0.8), [
        ("The framework is built so each leg sharpens the same objects: "
         "κ, the disclosure rule, and λ.", {"size": 15, "color": GREY}),
    ])

    # 23 ── takeaways ───────────────────────────────────────────────────────
    s = d.slide("Close", "Three things to remember")
    msgs = [
        ("Liquidity has a sweet spot", "minority takeover gains peak at "
         "moderate noise — and we certified when that's a theorem.", BLUE),
        ("Premia follow tender mechanics", "λ = 1 − q(1−γ)ψ prices who keeps "
         "the improvement — and why measured premia can fall.", TEAL),
        ("Disclosure is market design", "it substitutes for liquidity in "
         "pricing activism, and stricter isn't always better.", ROSE),
    ]
    y = Inches(2.1)
    for i, (head, body, col) in enumerate(msgs, 1):
        d.chip(s, Inches(0.85), y, Inches(0.55), Inches(0.55), str(i),
               fill=col, size=18, shape=MSO_SHAPE.OVAL)
        d.body(s, Inches(1.7), y - Inches(0.02), Inches(11), Inches(1.2), [
            (f"**{head}** — {body}", {"size": 19}),
        ])
        y += Inches(1.25)
    d.body(s, Inches(0.85), Inches(6.2), Inches(11), Inches(0.6), [
        ("Thank you  ·  junyu.li.24@ucl.ac.uk", {"size": 16, "color": GREY}),
    ])

    # ── BACKUPS ─────────────────────────────────────────────────────────────
    s = d.slide(footer=False)
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    band.fill.solid(); band.fill.fore_color.rgb = NAVY
    band.line.fill.background(); band.shadow.inherit = False
    tf = d._text(s, Inches(0.9), Inches(3.3), Inches(11.5), Inches(1.2))
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = "Backup"
    r.font.name = FONT; r.font.size = Pt(40); r.font.bold = True
    r.font.color.rgb = WHITE

    # B1 calibration
    s = d.slide("Backup", "Baseline calibration")
    cal = [
        ("Prior mean μ / value vol σ_v", "1.00 / 0.50", "normalization; moderate uncertainty"),
        ("Signal noise σ_ε", "0.50", "signal weight β = 0.5"),
        ("Discount δ", "0.95", "near-term horizon"),
        ("Liquidity κ (baseline)", "0.50", "interior"),
        ("Engagement cost C₀, slope χ", "0.12, 0.50", "moderate, strong-thesis decay"),
        ("Success prob ρ / value-add Δ", "0.90 / 0.25", "selective activists"),
        ("Premia m₀ / m₁", "0.10 / 0.30", "10% base, 30% on success"),
        ("Synergy S̄ / entry cost K / σ_ξ", "1.44 / 0.15 / 0.40", "interior bid probability"),
    ]
    y = Inches(1.95)
    for name, val, why in cal:
        d.body(s, Inches(0.8), y, Inches(5.4), Inches(0.45),
               [(name, {"size": 14.5})])
        d.body(s, Inches(6.3), y, Inches(2.0), Inches(0.45),
               [(val, {"size": 14.5, "bold": True})])
        d.body(s, Inches(8.5), y, Inches(4.3), Inches(0.45),
               [(why, {"size": 13, "color": GREY})])
        y += Inches(0.55)
    d.body(s, Inches(0.8), y + Inches(0.1), Inches(11.5), Inches(0.5), [
        ("Regularity (A5): δφ(0)/σ_ξ = 0.947 < 1 — unique pricing fixed "
         "point.", {"size": 13.5, "color": GREY}),
    ])

    # B2 baseline equilibrium table
    s = d.slide("Backup", "Baseline equilibrium outcomes")
    hdr = ["D", "X", "Price P", "Belief π", "Bid prob p", "Premium m̄"]
    data = [
        ("0", "−2", "0.84", "0.00", "0.81", "0.10"),
        ("0", "−1", "1.06", "0.41", "0.55", "0.17"),
        ("0", "0", "1.23", "0.74", "0.33", "0.23"),
        ("0", "+1", "1.39", "1.00", "0.17", "0.28"),
        ("1", "0/1/2", "1.90", "1.00", "0.01", "0.28"),
    ]
    xcols = [Inches(0.9), Inches(2.1), Inches(3.7), Inches(5.7), Inches(7.7),
             Inches(9.9)]
    for x, htxt in zip(xcols, hdr):
        d.body(s, x, Inches(2.0), Inches(1.9), Inches(0.4),
               [(htxt, {"bold": True, "size": 15})])
    y = Inches(2.55)
    for row in data:
        for x, cell in zip(xcols, row):
            d.body(s, x, y, Inches(1.9), Inches(0.4), [(cell, {"size": 14.5})])
        y += Inches(0.52)
    d.body(s, Inches(0.9), y + Inches(0.2), Inches(11.6), Inches(1.4), [
        ("Cutoffs: k₁ = k₀ ≈ 0.82, k_D ≈ 2.26 (hold region collapsed at "
         "baseline).", {"size": 14}),
        ("Disclosed branch: flat price, belief 1, bid probability collapses "
         "to 1% — public activism strongly deters bidders (price run-up plus "
         "the full premium m̃ = 0.28).", {"size": 14}),
    ])

    # B3 posteriors
    s = d.slide("Backup", "Where κ enters: the posterior algebra")
    d.body(s, Inches(0.8), Inches(2.0), Inches(11.8), Inches(4.4), [
        ("Noise: z = 0 w.p. 1 − κ; z = ±1 w.p. κ/2 each.  Order flow "
         "X = q + z; disclosure D = 1{q = +1}.", {"size": 16, "space": 10}),
        ("π(1, 0) = ω_Q / (ω_H + ω_Q) — κ-free (X = 1 pins q = 0).",
         {"size": 16}),
        ("π(0, 0) = ω_Q(1−κ) / [(ω_H + ω_Q)(1−κ) + ω_E κ/2] — falls in κ.",
         {"size": 16}),
        ("π(−1, 0) = ω_Q(κ/2) / [(ω_H + ω_Q)(κ/2) + ω_E(1−κ)] — rises in κ.",
         {"size": 16, "space": 10}),
        ("Rising κ compresses posteriors toward the prior: the inference "
         "channel of the hump. On D = 1, π ≡ 1 regardless of κ.",
         {"size": 15, "color": GREY}),
    ])

    # B4 existence/uniqueness
    s = d.slide("Backup", "Existence and uniqueness")
    d.body(s, Inches(0.8), Inches(2.0), Inches(11.8), Inches(4.4), [
        ("Existence: Brouwer on the compact cutoff simplex — unconditional.",
         {"size": 16, "space": 8}),
        ("Pricing layer: A5 (δφ(0)/σ_ξ < 1) makes the price map a "
         "contraction — unique P* per information set.", {"size": 16,
         "space": 8}),
        ("Cutoff layer: contraction verified numerically (A6); multi-start "
         "search from 4+ initial conditions converges to identical cutoffs; "
         "modulus L ≤ 0.836 along the κ path.", {"size": 16, "space": 8}),
        ("The same modulus L powers the inversion-free certification of the "
         "hump region (next backup).", {"size": 15, "color": GREY}),
    ])

    # B5 certification method
    s = d.slide("Backup", "Certifying the hump region without inverting a Jacobian")
    d.body(s, Inches(0.8), Inches(2.0), Inches(11.8), Inches(4.6), [
        ("Threat: equilibrium cutoffs move with κ (GE channel B) and could "
         "overturn the fixed-cutoff hump (channel A).", {"size": 16,
         "space": 8}),
        ("Standard bound needs ‖dk/dκ‖ — the unknown path derivative.",
         {"size": 16, "space": 8}),
        ("Trick: F = I − T inherits the contraction modulus L of the "
         "best-response map, so ‖(I − D_kT)⁻¹‖ ≤ 1/(1−L) by Neumann series — "
         "computable from **one solve plus one finite difference**.",
         {"size": 16, "space": 8}),
        ("Result: |B| bounded below channel A's amplitude on κ ∈ "
         "[0.35, 0.825] (inversion-free; [0.30, 0.85] with exact IFT). "
         "Margins: ball integral 2.5×10⁻⁵ vs 4.7×10⁻³.", {"size": 16,
         "space": 8}),
        ("At σ_ξ = 0.60 the same machinery certifies the **failure**: "
         "∫|B| = 0.021 vs A-amplitude 0.0069 → trough.", {"size": 15,
         "color": GREY}),
    ])

    # B6 tender game
    s = d.slide("Backup", "The tender game behind λ")
    d.body(s, Inches(0.8), Inches(2.0), Inches(11.8), Inches(4.6), [
        ("At the bargaining disagreement node: fringe raider (cost c_F ~ H, "
         "synergy S_F ~ G) posts a uniform tender for control share τ; "
         "atomistic float free-rides; charter allows dilution φ of "
         "non-tendering holders (Grossman–Hart).", {"size": 15.5,
         "space": 8}),
        ("Free-rider floor: b̂* = w + γaΔ + S_F − φ. Raid pays iff entry "
         "cost is covered by dilution on acquired shares.", {"size": 15.5,
         "space": 8}),
        ("Pivotal bloc (1 − α < τ) can block: raid additionally needs "
         "S_F − φ ≥ (1−γ)aΔ → the ψ factor.", {"size": 15.5, "space": 8}),
        ("λ = 1 − q(1−γ)ψ emerges as the equilibrium share of the "
         "improvement the activist's side keeps; λ > 0 fails only if raids "
         "are certain, fully superseding, and unblockable — so the wedge "
         "m₁ > m₀ is a theorem on the rest of the parameter space.",
         {"size": 15.5}),
    ])

    # B7 sensitivity
    s = d.slide("Backup", "Sensitivity: the hump survives")
    d.picture(s, "sens1", Inches(0.55), Inches(2.0), w=Inches(6.1))
    d.picture(s, "sens2", Inches(6.85), Inches(2.0), w=Inches(6.1))
    d.caption(s, Inches(0.55), Inches(6.4), Inches(12),
              "Left: discount factor δ and bidder vol σ_ξ. Right: engagement cost C₀, "
              "premium wedge m₁−m₀, success probability ρ. Peak location κ† marked.")

    # B8 welfare
    s = d.slide("Backup", "Welfare vs minority gains")
    d.picture(s, "welfare", Inches(0.55), Inches(1.9), w=Inches(6.6))
    d.body(s, Inches(7.5), Inches(2.0), Inches(5.2), Inches(4.4), [
        ("Total surplus = synergies + improvements − costs; prices and "
         "premia are transfers.", {"size": 15.5, "space": 8}),
        ("The κ that maximizes minority extraction deters marginal "
         "efficient takeovers → κ* ≠ κ†.", {"size": 15.5, "space": 8}),
        ("Policy read: \"more liquidity is good for governance\" and \"good "
         "for welfare\" are different claims; the model separates them.",
         {"size": 15, "color": GREY}),
    ])

    # B9 disclosure benchmarks
    s = d.slide("Backup", "Disclosure benchmarks and rumors")
    d.picture(s, "rumor", Inches(0.55), Inches(1.9), w=Inches(6.6))
    d.body(s, Inches(7.5), Inches(2.0), Inches(5.2), Inches(4.4), [
        ("Bounds: full information (κ-invariant) and no disclosure "
         "(maximally κ-sensitive) bracket the baseline regime.",
         {"size": 15.5, "space": 8}),
        ("Noisy rumors (wolf-pack chatter) interpolate: as rumor precision "
         "rises, inference converges to full information and the liquidity "
         "effect flattens further.", {"size": 15.5, "space": 8}),
        ("Same comparative static as tightening the disclosure rule — "
         "information substitutes are interchangeable here.", {"size": 15,
         "color": GREY}),
    ])

    # B10 cutoffs vs kappa
    s = d.slide("Backup", "Equilibrium cutoffs across the liquidity dial")
    d.picture(s, "cutoffs_kappa", Inches(0.85), Inches(1.9), h=Inches(4.1))
    d.body(s, Inches(7.5), Inches(2.0), Inches(5.2), Inches(4.2), [
        ("Exit/hold boundary k₁ = k₀ throughout (hold collapsed); public "
         "threshold k_D tracks the quiet/public margin.", {"size": 15.5,
         "space": 8}),
        ("Ordering k₁ ≤ k₀ ≤ k_D preserved across all κ — the GE channel "
         "moves cutoffs smoothly, no regime jumps.", {"size": 15.5}),
    ])

    # B11 fact 2 methods
    s = d.slide("Backup", "Evidence: data & methods")
    d.body(s, Inches(0.8), Inches(2.0), Inches(11.8), Inches(4.6), [
        ("Universe: every original Schedule 13D on EDGAR 2022Q1–2025Q4 "
         "(amendments excluded; boundary-aware form matching — EDGAR renamed "
         "the form \"SCHEDULE 13D\" in Dec 2024).", {"size": 15, "space": 8}),
        ("CUSIPs parsed from cover pages with check-digit validation "
         "(~80–90% coverage); after-16:00 ET acceptances shifted to the next "
         "trading day.", {"size": 15, "space": 8}),
        ("CARs: market model, estimation 220 trading days ending 30 before "
         "the event (min 100 obs), windows [−1,+1] and [−10,+1].",
         {"size": 15, "space": 8}),
        ("Covariates: Amihud illiquidity [−250,−30], run-up [−60,−11], "
         "ln market cap at −30; US common stock only; two-way clustered SEs "
         "(firm × month); year-quarter FE absorb Post in the saturated spec.",
         {"size": 15}),
    ])

    d.prs.save(OUT_PPTX)
    print(f"wrote {OUT_PPTX}: {d.n} numbered slides "
          f"({len(d.prs.slides.__iter__.__self__._sldIdLst)} total)")


if __name__ == "__main__":
    build_assets()
    build()
