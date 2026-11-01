#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2015-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Post-build pipeline for whitecollarboxingtraining.com (Rust SSG + Cloudflare)."""
from __future__ import annotations

import glob
import json
import re
import shutil
import subprocess
from pathlib import Path

BASE_URL = "https://whitecollarboxingtraining.com"
LEGACY_SLUGS = ("story", "whats-involved", "trainers", "classes", "get-in-touch")

LLMS_APPENDIX = """
## Gym & Coaching Quick Reference
- **Address**: Anchor Hall, Bulwer Rd, Barnet, London EN5 5EX, UK
- **GPS Coordinates**: 51.651161, -0.17987
- **Head Coach**: Gary Foley (`07749 116927` / `+44 7749 116927`) — 20+ years London white collar boxing experience, 9+ years qualified trainer.
- **Senior Coach**: Sean Murphy (`07729 980677` / `+44 7729 980677`) — Commonwealth Games Gold Medallist, British Lonsdale Belt Outright Winner, World Title contender.
- **Programmes**: Basic/Beginner Boxing, Amateur/Mid-Level Boxing, Advanced Fight Camp, and 1-to-1 Private Coaching.
"""

ROBOTS_TXT = """User-agent: *
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: https://whitecollarboxingtraining.com/sitemap.xml
"""

SECURITY_TXT = """Contact: https://github.com/sebastienrousseau/whitecollarboxingtraining.github.io/security/advisories
Expires: 2027-11-01T00:00:00.000Z
Preferred-Languages: en
Canonical: https://whitecollarboxingtraining.com/.well-known/security.txt
"""

HUMANS_TXT = """/* TEAM */
Author: Sebastien Rousseau
Site: https://sebastienrousseau.com
Head Coach: Gary Foley (07749 116927)
Senior Coach: Sean Murphy (07729 980677)
Location: Anchor Hall, Bulwer Rd, Barnet, London EN5 5EX, UK

/* SITE */
Last update: 2026-11-01
Language: English (en-GB)
Standards: HTML5, CSS3, WCAG 2.2 AAA, Schema.org JSON-LD, OpenGraph
Components: Rust Static Site Generator (SSG), Skeletonic CSS, Cloudflare Edge
"""


def convert_to_webp(src: Path, dst: Path, dark_grade: bool = False) -> None:
    """Convert a raster image to WebP using cwebp."""
    _ = dark_grade
    cwebp = shutil.which("cwebp")
    if cwebp:
        subprocess.run([cwebp, "-quiet", "-q", "85", str(src), "-o", str(dst)], check=False)
        if dst.exists():
            return
    if not dst.exists():
        shutil.copy2(src, dst)


def ensure_webp_images(root: Path, pub: Path) -> None:
    """Copy images into public/images, stage FightSphere boxing photography, and generate .webp."""
    src_img = root / "images"
    dst_img = pub / "images"
    if src_img.is_dir():
        shutil.copytree(src_img, dst_img, dirs_exist_ok=True)

    for ext in ("*.jpg", "*.jpeg", "*.png"):
        for img_path in dst_img.rglob(ext):
            if img_path.parent.name == "boxing":
                continue
            webp_path = img_path.with_suffix(".webp")
            is_legacy_photo = img_path.parent.name in ("other", "banner")
            convert_to_webp(img_path, webp_path, dark_grade=is_legacy_photo)
            rel = img_path.relative_to(dst_img)
            root_webp = src_img / rel.with_suffix(".webp")
            if webp_path.exists():
                try:
                    root_webp.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(webp_path, root_webp)
                except OSError:
                    pass


def copy_static_assets(root: Path, pub: Path) -> None:
    """Copy CSS, JS, CNAME, Cloudflare configs, videos, and favicons into public/."""
    for name in ("skeletonic.min.css", "styles.css", "theme-init.js", "main.js"):
        src = root / "_layouts" / name
        if not src.is_file():
            src = root / name
        if src.is_file():
            shutil.copy2(src, pub / name)
    for meta in ("CNAME", "_redirects", "wrangler.toml"):
        if (root / meta).is_file():
            shutil.copy2(root / meta, pub / meta)
    headers_path = pub / "_headers"
    if not headers_path.is_file() and (root / "_headers").is_file():
        shutil.copy2(root / "_headers", headers_path)
    if headers_path.is_file():
        hdr = headers_path.read_text(encoding="utf-8")
        old_block = (
            "  X-Content-Type-Options: nosniff\n"
            "  Referrer-Policy: strict-origin-when-cross-origin\n"
            "  Permissions-Policy: camera=(), geolocation=(), microphone=()"
        )
        new_block = (
            "  X-Content-Type-Options: nosniff\n"
            "  X-Frame-Options: DENY\n"
            "  Referrer-Policy: strict-origin-when-cross-origin\n"
            "  Permissions-Policy: accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()\n"
            "  Cross-Origin-Opener-Policy: same-origin\n"
            "  Cross-Origin-Resource-Policy: same-site\n"
            "  X-Permitted-Cross-Domain-Policies: none"
        )
        if old_block in hdr:
            hdr = hdr.replace(old_block, new_block, 1)
            headers_path.write_text(hdr, encoding="utf-8")
        shutil.copy2(headers_path, root / "_headers")
    ensure_webp_images(root, pub)

    vid_src = root / "archive" / "legacy-gae-2015" / "videos"
    if vid_src.is_dir():
        shutil.copytree(vid_src, pub / "videos", dirs_exist_ok=True)

    fav_src = pub / "images" / "favicon" / "favicon-32x32.png"
    if fav_src.is_file():
        shutil.copy2(fav_src, pub / "favicon.ico")


def enhance_html_file(html_path: Path) -> None:
    """Ensure responsive tables and explicit image attributes on compiled HTML."""
    content = html_path.read_text(encoding="utf-8")
    content = content.replace("<table>", '<div class="table-responsive"><table>').replace(
        "</table>", "</table></div>"
    )
    content = content.replace(
        '<div class="table-responsive"><div class="table-responsive"><table>',
        '<div class="table-responsive"><table>',
    ).replace("</table></div></div>", "</table></div>")

    def fix_img(match: re.Match[str]) -> str:
        tag = match.group(0)
        if "width=" not in tag:
            tag = tag[:-1] + ' width="1280" height="720" loading="lazy">'
        return tag

    content = re.sub(r"<img\b[^>]*>", fix_img, content)
    html_path.write_text(content, encoding="utf-8")


def emit_legacy_html_aliases(pub: Path) -> None:
    """Emit /404.html and /<slug>.html copies so all 2015 URLs resolve with HTTP 200."""
    err_idx = pub / "404" / "index.html"
    if err_idx.is_file():
        shutil.copy2(err_idx, pub / "404.html")
    for slug in LEGACY_SLUGS:
        idx = pub / slug / "index.html"
        if idx.is_file():
            shutil.copy2(idx, pub / f"{slug}.html")


def write_seo_and_ai_files(pub: Path) -> None:
    """Enrich sitemap.xml, robots.txt, llms.txt, llms-full.txt, agents.txt, and .well-known."""
    skip_dirs = {"404", "offline", "thanks"}
    urls: list[str] = []
    for page in sorted(pub.rglob("index.html")):
        rel_dir = page.parent.relative_to(pub)
        top = rel_dir.parts[0] if rel_dir.parts else ""
        if top in skip_dirs:
            continue
        loc = f"{BASE_URL}/" if str(rel_dir) == "." else f"{BASE_URL}/{rel_dir.as_posix()}/"
        urls.append(
            f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>2026-11-01</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
        )
    (pub / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(urls)
        + "</urlset>\n",
        encoding="utf-8",
    )
    (pub / "robots.txt").write_text(ROBOTS_TXT, encoding="utf-8")
    for llm_file in ("llms.txt", "llms-full.txt", "agents.txt"):
        p = pub / llm_file
        existing = p.read_text(encoding="utf-8") if p.is_file() else "# White Collar Boxing Training\n"
        if "51.651161, -0.17987" not in existing:
            p.write_text(existing.rstrip() + "\n" + LLMS_APPENDIX, encoding="utf-8")
    (pub / "humans.txt").write_text(HUMANS_TXT, encoding="utf-8")
    (pub / "security.txt").write_text(SECURITY_TXT, encoding="utf-8")

    wk = pub / ".well-known"
    wk.mkdir(parents=True, exist_ok=True)
    (wk / "security.txt").write_text(SECURITY_TXT, encoding="utf-8")
    if not (wk / "ai-plugin.json").is_file():
        (wk / "ai-plugin.json").write_text(json.dumps({
            "schema_version": "v1",
            "name_for_human": "White Collar Boxing Training",
            "name_for_model": "whitecollarboxingtraining",
            "description_for_human": "White Collar Boxing Training in Barnet, London & the UK.",
            "description_for_model": "Official information for White Collar Boxing Training at Anchor Hall, Bulwer Rd, Barnet, London EN5 5EX, UK. Coaches: Gary Foley (07749 116927) and Sean Murphy (07729 980677).",
            "auth": {"type": "none"},
            "url": BASE_URL,
            "logo_url": f"{BASE_URL}/images/logo/whitecollarboxingtraining.svg",
        }, indent=2) + "\n", encoding="utf-8")
    if not (wk / "mcp.json").is_file():
        (wk / "mcp.json").write_text(json.dumps({
            "name": "whitecollarboxingtraining",
            "version": "0.0.2",
            "url": BASE_URL,
            "llms_txt": f"{BASE_URL}/llms.txt",
        }, indent=2) + "\n", encoding="utf-8")


def sync_docs(root: Path, pub: Path) -> None:
    """Mirror public/ into docs/ while preserving docs/releases/."""
    docs = root / "docs"
    releases_backup: dict[str, str] = {}
    rel_dir = docs / "releases"
    if rel_dir.is_dir():
        for p in rel_dir.glob("*.md"):
            releases_backup[p.name] = p.read_text(encoding="utf-8")
    if docs.exists():
        shutil.rmtree(docs)
    shutil.copytree(pub, docs)
    rel_dir.mkdir(parents=True, exist_ok=True)
    for name, text in releases_backup.items():
        (rel_dir / name).write_text(text, encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    pub = root / "public"
    pub.mkdir(parents=True, exist_ok=True)
    copy_static_assets(root, pub)
    for html_str in glob.glob(str(pub / "**" / "*.html"), recursive=True):
        enhance_html_file(Path(html_str))
    emit_legacy_html_aliases(pub)
    write_seo_and_ai_files(pub)
    sync_docs(root, pub)
    print("Post-build completed successfully for whitecollarboxingtraining.com.")


if __name__ == "__main__":
    main()
