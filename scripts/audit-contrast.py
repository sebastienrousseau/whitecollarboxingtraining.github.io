#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2015-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
# WCAG 2.2 Level AAA Mathematical Contrast Ratio Validator
import sys

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip("#")
    if len(hex_str) == 3:
        hex_str = "".join([c*2 for c in hex_str])
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def relative_luminance(rgb):
    def channel_lum(val):
        s = val / 255.0
        return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * channel_lum(r) + 0.7152 * channel_lum(g) + 0.0722 * channel_lum(b)

def contrast_ratio(hex1, hex2):
    l1 = relative_luminance(hex_to_rgb(hex1))
    l2 = relative_luminance(hex_to_rgb(hex2))
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

tokens = [
    ("Light Mode Body Text", "#090a0f", "#ffffff", 7.0),
    ("Light Mode Headings", "#050608", "#ffffff", 4.5),
    ("Light Mode Links", "#8a0000", "#ffffff", 7.0),
    ("Light Mode Focus Ring", "#8a0000", "#f4f4f6", 3.0),
    ("Dark Mode Body Text", "#ffffff", "#050608", 7.0),
    ("Dark Mode Headings", "#ffffff", "#050608", 4.5),
    ("Dark Mode Links", "#facc15", "#050608", 7.0),
    ("Dark Mode Focus Ring", "#facc15", "#0c0e14", 3.0),
]

all_pass = True
print("=== WCAG 2.2 Level AAA Color Contrast Audit ===")
for name, fg, bg, threshold in tokens:
    ratio = contrast_ratio(fg, bg)
    status = "PASS" if ratio >= threshold else "FAIL"
    print(f"[{status}] {name:25s} | FG:{fg} BG:{bg} | Ratio:{ratio:5.2f}:1 (Target: >={threshold}:1)")
    if ratio < threshold:
        all_pass = False

sys.exit(0 if all_pass else 1)
