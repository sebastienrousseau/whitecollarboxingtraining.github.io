#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2015-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Automated regression test suite for whitecollarboxingtraining.com."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
BASE_URL = "https://whitecollarboxingtraining.com"


def assert_true(cond: bool, msg: str) -> None:
    if not cond:
        print(f"[FAIL] {msg}", file=sys.stderr)
        sys.exit(1)


def check_required_files() -> None:
    required = [
        "index.html",
        "404.html",
        "story/index.html",
        "whats-involved/index.html",
        "trainers/index.html",
        "classes/index.html",
        "get-in-touch/index.html",
        "contact/index.html",
        "faqs/index.html",
        "story.html",
        "whats-involved.html",
        "trainers.html",
        "classes.html",
        "get-in-touch.html",
        "CNAME",
        "_headers",
        "_redirects",
        "wrangler.toml",
        "sitemap.xml",
        "robots.txt",
        "llms.txt",
        "llms-full.txt",
        "agents.txt",
        "manifest.json",
        "skeletonic.min.css",
        "styles.css",
        "main.js",
        "theme-init.js",
        ".well-known/security.txt",
        ".well-known/ai-plugin.json",
        ".well-known/mcp.json",
    ]
    for rel in required:
        assert_true((PUBLIC / rel).is_file(), f"Missing required build output: public/{rel}")


def check_content_and_seo() -> None:
    cname = (PUBLIC / "CNAME").read_text(encoding="utf-8").strip()
    assert_true(cname == "whitecollarboxingtraining.com", f"Unexpected CNAME: {cname}")

    home = (PUBLIC / "index.html").read_text(encoding="utf-8")
    for fact in (
        "Gary Foley",
        "Sean Murphy",
        "07749 116927",
        "07729 980677",
        "Anchor Hall",
        "EN5 5EX",
        "application/ld+json",
        "ExerciseGym",
        "https://sebastienrousseau.com/",
    ):
        assert_true(fact in home, f"Homepage missing expected content or schema token: {fact}")

    trainers = (PUBLIC / "trainers" / "index.html").read_text(encoding="utf-8")
    assert_true("Commonwealth Games Gold" in trainers, "Trainers page missing Commonwealth Games Gold")
    assert_true("Lonsdale Belt" in trainers, "Trainers page missing Lonsdale Belt")

    llms = (PUBLIC / "llms.txt").read_text(encoding="utf-8")
    assert_true("51.651161, -0.17987" in llms, "llms.txt missing Barnet GPS coordinates")

    headers = (PUBLIC / "_headers").read_text(encoding="utf-8")
    for h in (
        "X-Frame-Options: DENY",
        "Referrer-Policy: strict-origin-when-cross-origin",
        "Cross-Origin-Opener-Policy: same-origin",
        "Cross-Origin-Resource-Policy: same-site",
        "X-Permitted-Cross-Domain-Policies: none",
    ):
        assert_true(h in headers, f"_headers missing Cloudflare security header: {h}")

    wrangler = (PUBLIC / "wrangler.toml").read_text(encoding="utf-8")
    assert_true('"Cross-Origin-Resource-Policy" = "same-site"' in wrangler, "wrangler.toml missing CORP same-site")
    assert_true('"X-Permitted-Cross-Domain-Policies" = "none"' in wrangler, "wrangler.toml missing XPCDP none")


def main() -> int:
    check_required_files()
    check_content_and_seo()
    print("[regression-test] All static, SEO, AI search, and Cloudflare checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
