#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2015-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Verify every whitecollarboxingtraining.com colour pair meets WCAG 2.2 AAA (>= 7:1).

Run: python3 audit/contrast.py
Exits non-zero if any text/UI pair falls below 7:1.
"""


def _lin(c: float) -> float:
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def _luminance(hex_colour: str) -> float:
    h = hex_colour.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def ratio(fg: str, bg: str) -> float:
    la, lb = _luminance(fg), _luminance(bg)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


PAIRS = [
    # (label, foreground, background)
    ("light body text",      "#090a0f", "#ffffff"),
    ("light secondary/surf", "#1e2028", "#f4f4f6"),
    ("light muted / bg",     "#3b3e4a", "#ffffff"),
    ("light muted / surf",   "#3b3e4a", "#f4f4f6"),
    ("light brand / bg",     "#8a0000", "#ffffff"),
    ("light brand / surf",   "#8a0000", "#f4f4f6"),
    ("light btn text",       "#ffffff", "#8a0000"),
    ("dark body text",       "#ffffff", "#050608"),
    ("dark secondary/surf",  "#d4d8e2", "#0c0e14"),
    ("dark muted / bg",      "#a3aab8", "#050608"),
    ("dark muted / surf",    "#a3aab8", "#0c0e14"),
    ("dark brand / bg",      "#facc15", "#050608"),
    ("dark brand / surf",    "#facc15", "#0c0e14"),
    ("dark btn text",        "#050608", "#facc15"),
]

AAA = 7.0


def main() -> int:
    worst = 99.0
    print(f"{'pair':22} {'fg':9} {'bg':9} ratio  AAA(>=7)")
    for label, fg, bg in PAIRS:
        r = ratio(fg, bg)
        worst = min(worst, r)
        print(f"{label:22} {fg:9} {bg:9} {r:5.2f}  {'PASS' if r >= AAA else 'FAIL'}")
    print(f"\nworst pair: {worst:.2f}:1  ->  {'ALL AAA' if worst >= AAA else 'BELOW AAA'}")
    return 0 if worst >= AAA else 1


if __name__ == "__main__":
    raise SystemExit(main())
