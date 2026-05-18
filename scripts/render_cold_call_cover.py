"""
Render 1600x900 cover for the Cold-Call Funnel Analysis case study.

A drawn funnel graphic (not a chart, not a photo): five stacked bands narrow
from 102,007 dials to 362 wins, the collapse to the tiny "Won" band being the
visual point — the leak is after the first conversation, not before it. Dark
theme matches the AI-pipeline and tomato-intel covers for grid coherence.

Self-contained like render_tomato_cover.py: run any time —
    python scripts/render_cold_call_cover.py
"""
from __future__ import annotations

import os

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
from matplotlib import font_manager

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(SITE_ROOT, "assets", "images", "projects",
                   "cold-call-funnel-cover.png")

BG = "#0A0A0A"          # --bg-primary, full-bleed like the pipeline cover
INK = "#E5E7EB"         # primary text
MUTED = "#9AA3AF"       # subtitle / secondary
LIME = "#B5E853"        # --accent-green
LIME_DIM = "#5E8A2E"    # the upper, high-volume bands
ALERT = "#E5484D"       # the Won band: where it collapsed to

W, H = 1600, 900

# (label, value, share-of-calls width fraction, color). Widths are eyeballed
# from the real funnel so the narrowing reads honestly without a log trick:
# 102,007 -> 31,421 -> 5,755 -> 2,829 -> 362.
BANDS = [
    ("Calls",          "102,007", 1.00,  LIME_DIM),
    ("Connected",      "31,421",  0.62,  LIME_DIM),
    ("Meeting booked", "5,755",   0.36,  LIME),
    ("Meeting held",   "2,829",   0.26,  LIME),
    ("Won",            "362",     0.10,  ALERT),
]


def pick_fonts() -> tuple[str, str]:
    available = {f.name for f in font_manager.fontManager.ttflist}
    title = ("Inter" if "Inter" in available
             else "DejaVu Sans" if "DejaVu Sans" in available
             else "sans-serif")
    mono = ("JetBrains Mono" if "JetBrains Mono" in available
            else "DejaVu Sans Mono" if "DejaVu Sans Mono" in available
            else "monospace")
    return title, mono


def main() -> None:
    title_font, mono_font = pick_fonts()
    print(f"Fonts: title={title_font}, mono={mono_font}")

    fig = plt.figure(figsize=(16, 9), facecolor=BG, dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_facecolor(BG)
    ax.axis("off")

    ax.text(70, H - 78, "Cold-Call Funnel Analysis",
            fontsize=34, color=INK, fontname=title_font, fontweight="bold")
    ax.text(70, H - 122,
            "102,007 dials, 362 wins  ·  the leak was after the first "
            "conversation, not before it",
            fontsize=16, color=MUTED, fontname=mono_font)

    # Funnel band geometry: a centred narrowing stack.
    cx = W / 2
    top = H - 190
    band_h = 96
    gap = 16
    max_half = 560  # half-width of the widest band

    for i, (label, value, frac, color) in enumerate(BANDS):
        y_top = top - i * (band_h + gap)
        y_bot = y_top - band_h
        half = max_half * frac
        # next band's half-width, for the connecting taper
        nxt = (max_half * BANDS[i + 1][2]) if i + 1 < len(BANDS) else half * 0.5

        band = FancyBboxPatch(
            (cx - half, y_bot), 2 * half, band_h,
            boxstyle="round,pad=0,rounding_size=10",
            linewidth=0, facecolor=color, zorder=2,
        )
        ax.add_patch(band)

        # taper to the next band so it reads as one funnel collapsing
        if i + 1 < len(BANDS):
            taper = Polygon(
                [(cx - half, y_bot), (cx + half, y_bot),
                 (cx + nxt, y_bot - gap), (cx - nxt, y_bot - gap)],
                closed=True, facecolor="#1A1A1A", linewidth=0, zorder=1,
            )
            ax.add_patch(taper)

        on_dark = "#0A0A0A"
        ax.text(cx, (y_top + y_bot) / 2 + 7, value,
                fontsize=22, color=on_dark, fontname=title_font,
                fontweight="bold", ha="center", va="center", zorder=3)
        ax.text(cx, (y_top + y_bot) / 2 - 20, label,
                fontsize=12, color=on_dark, fontname=mono_font,
                ha="center", va="center", zorder=3)

    # The one-line analytical callout, lime, house style.
    cy = top - len(BANDS) * (band_h + gap) - 18
    ax.plot([70, 104], [cy, cy], color=LIME, linewidth=3,
            solid_capstyle="round")
    ax.text(120, cy,
            "Only 12.8% of held meetings became wins  ·  one company-size "
            "band closed at 37.5%, everyone else at 3.0%",
            fontsize=14, color=LIME, fontname=mono_font, va="center")

    ax.text(W - 70, 42, "Synthetic data, real method",
            fontsize=12, color=MUTED, fontname=mono_font,
            ha="right", va="center")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, facecolor=BG, dpi=100)
    print(f"Wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
