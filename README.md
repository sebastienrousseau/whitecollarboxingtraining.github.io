<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

<p align="center">
  <img src="images/logo/whitecollarboxingtraining.svg" alt="White Collar Boxing Training logo" width="128" height="128">
</p>

<h1 align="center">whitecollarboxingtraining.com</h1>

<p align="center">
  <strong>Official static website for White Collar Boxing Training in Barnet, North London &amp; the UK — compiled with Rust SSG, styled with Skeletonic CSS, and served via Cloudflare Edge.</strong>
</p>

<p align="center">
  <a href="https://github.com/sebastienrousseau/whitecollarboxingtraining.github.io/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/sebastienrousseau/whitecollarboxingtraining.github.io/ci.yml?branch=master&style=for-the-badge&label=CI" alt="CI"></a>
  <a href="https://github.com/sebastienrousseau/whitecollarboxingtraining.github.io/releases"><img src="https://img.shields.io/github/v/release/sebastienrousseau/whitecollarboxingtraining.github.io?include_prereleases&style=for-the-badge&color=820000" alt="Release"></a>
  <a href="https://securityscorecards.dev/viewer/?uri=github.com/sebastienrousseau/whitecollarboxingtraining.github.io"><img src="https://img.shields.io/ossf-scorecard/github.com/sebastienrousseau/whitecollarboxingtraining.github.io?style=for-the-badge&label=OpenSSF" alt="OpenSSF Scorecard"></a>
  <a href="LICENSE-APACHE"><img src="https://img.shields.io/badge/License-Apache_2.0_OR_MIT-007ec6?style=for-the-badge" alt="License: Apache-2.0 OR MIT"></a>
</p>

---

**whitecollarboxingtraining.com** is the official web property for **White Collar Boxing Training** (`Anchor Hall, Bulwer Rd, Barnet, London EN5 5EX`). Originally built in 2015 on Google App Engine (Python 2.7 / Jinja2, preserved in `archive/legacy-gae-2015/`), the site is now compiled natively with the Rust `static-site-generator` (`ssg`) and Skeletonic CSS, audited to WCAG 2.2 Level AAA (`>= 7.0:1` contrast), and configured for Cloudflare edge delivery alongside AI/LLM and Google Search discovery.

## Contents

- [Install](#install)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [The whitecollarboxingtraining.com ecosystem](#the-whitecollarboxingtrainingcom-ecosystem)
- [Capabilities at a glance](#capabilities-at-a-glance)
- [Ecosystem comparison](#ecosystem-comparison)
- [Benchmarks](#benchmarks)
- [Features](#features)
- [Configuration](#configuration)
- [Examples](#examples)
- [When not to use whitecollarboxingtraining.com](#when-not-to-use-whitecollarboxingtrainingcom)
- [Development](#development)
- [Security](#security)
- [Documentation](#documentation)
- [Stability guarantees](#stability-guarantees)
- [License](#license)

## Install

```bash
git clone https://github.com/sebastienrousseau/whitecollarboxingtraining.github.io.git
cd whitecollarboxingtraining.github.io
make build
```

## Requirements

| Tool | Minimum Version | Purpose |
| :--- | :--- | :--- |
| `ssg` | `0.0.69` | Rust Static Site Generator compiler |
| `python3` | `3.11+` | Post-build SEO/AI pipeline and WCAG AAA contrast auditors |
| `node` | `20+` | Property-based fuzz tests and HTML validation |
| `make` | `3.81+` | Single-command build and quality gate orchestration |

## Quick Start

```bash
# Compile Markdown content (_posts/) and templates (_layouts/) into public/ and docs/
make build

# Run the complete verification gate (lint, regression tests, property tests, WCAG AAA audit)
make verify

# Preview locally at http://127.0.0.1:8000
make serve
```

## The whitecollarboxingtraining.com ecosystem

| Component | Path | Responsibility |
| :--- | :--- | :--- |
| Content Source | `_posts/*.md` | Frontmatter-validated Markdown pages for programmes, trainers, classes, and FAQs |
| Theme Layouts | `_layouts/*.html`, `_layouts/styles.css` | WCAG 2.2 AAA Championship Crimson &amp; Obsidian theme built on Skeletonic CSS |
| Edge Config | `ssg.toml`, `wrangler.toml`, `_headers`, `_redirects`, `CNAME` | Cloudflare Pages/Workers routing, HSTS, CSP, and immutable cache policies |
| Legacy Archive | `archive/legacy-gae-2015/` | Complete 2015 Google App Engine Python 2.7 / `webapp2` / Jinja2 source archive |

## Capabilities at a glance

| Capability | Status | Implementation |
| :--- | :--- | :--- |
| Rust SSG Compilation | Verified | `ssg build --content _posts --template _layouts --output public` |
| WCAG 2.2 Level AAA Contrast | Verified | `>= 7.59:1` across all light and dark theme token pairs (`audit/contrast.py`) |
| Google &amp; Local SEO | Verified | Schema.org `@graph` (`ExerciseGym`, `SportsActivityLocation`, `LocalBusiness`, `Person`, `OfferCatalog`) |
| AI Search Readiness | Verified | `llms.txt`, `llms-full.txt`, `agents.txt`, `.well-known/ai-plugin.json`, `.well-known/mcp.json` |
| Legacy URL Continuity | Verified | Both clean directory routes (`/story/`) and 2015 `.html` routes (`/story.html`) emitted |
| Cloudflare Setup | Verified | `wrangler.toml`, `_headers`, `_redirects`, `CNAME` (`whitecollarboxingtraining.com`) |

## Ecosystem comparison

| Metric | Legacy 2015 GAE (`archive/legacy-gae-2015/`) | Modern SSG Port (`v0.0.2`) |
| :--- | :--- | :--- |
| Runtime | Python 2.7 (`webapp2` + `jinja2`, deprecated) | Zero-runtime static HTML/CSS compiled by Rust `ssg` |
| Contrast Ratio | `3.5:1` (`#878787` on `#ffffff` — fails WCAG AA) | `>= 7.59:1` light &amp; dark modes (passes WCAG 2.2 AAA) |
| Third-Party Trackers | Facebook SDK, AddThis, Google+, HTTP Maps v2 | Zero third-party scripts or tracking cookies |
| Structured Data | None | Schema.org `@graph` JSON-LD + `llms.txt` + `agents.txt` |

## Benchmarks

| Gate / Metric | Target | Measured (`v0.0.2`) |
| :--- | :--- | :--- |
| Full `ssg build` + `post-build.py` time | `< 2.0s` | `0.38s` |
| Minimum Text Contrast Ratio (Light / Dark) | `>= 7.0:1` (AAA) | `8.07:1` (Light) / `7.59:1` (Dark) |
| Total First-Load CSS + JS Payload (uncompressed) | `< 50 KB` | `21.4 KB` |

## Features

- **Complete Content Preservation &amp; Enrichment**: Retains all original 2015 pages (`Home`, `Our Story`, `What's Involved`, `Trainers`, `Classes`, `Get in Touch`), trainer biographies (`Gary Foley` — `07749 116927`; `Sean Murphy` — `07729 980677`), and Barnet gym details (`Anchor Hall, Bulwer Rd, Barnet, London EN5 5EX`).
- **Three-State Theme Engine**: Supports `System`, `Light`, and `Dark` modes via `theme-init.js` and `main.js` with zero flash of unstyled content.
- **AI &amp; Search Engine Discovery**: Ships `sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt`, `agents.txt`, `rss.xml`, `atom.xml`, and `feed.json`.

## Configuration

Site-level compilation and Cloudflare edge headers are configured in [`ssg.toml`](ssg.toml) and [`wrangler.toml`](wrangler.toml):

```toml
site_name = "White Collar Boxing Training"
base_url = "https://whitecollarboxingtraining.com"
language = "en-GB"

[edge_headers]
targets = ["netlify", "cloudflare", "vercel"]
```

## Examples

Run individual verification gates during development:

```bash
# Verify WCAG 2.2 Level AAA mathematical contrast ratios
make contrast

# Validate Markdown frontmatter across all pages in _posts/
make validate

# Run static and SEO regression assertions
make test
```

## When not to use whitecollarboxingtraining.com

This repository contains the brand content, gym schedule, and static web templates specific to **White Collar Boxing Training** (`whitecollarboxingtraining.com`). If you are looking for reusable starter themes for your own project, use [ssg-themes.github.io](https://github.com/sebastienrousseau/ssg-themes.github.io) or the [Rust Static Site Generator (`ssg`)](https://static-site-generator.com/).

## Development

See [DEVELOPMENT.md](DEVELOPMENT.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for local toolchain setup, branch naming (`feat/v<next-version>`), and pre-commit quality gates.

## Security

See [SECURITY.md](SECURITY.md) and [`/.well-known/security.txt`](public/.well-known/security.txt) for vulnerability disclosure procedures.

## Documentation

- [AGENTS.md](AGENTS.md) — Agentic workflow and repository architecture standards
- [CHANGELOG.md](CHANGELOG.md) — Release history
- [archive/legacy-gae-2015/README.md](archive/legacy-gae-2015/README.md) — Documentation of the archived 2015 Google App Engine application

## Stability guarantees

All public URLs — including both modern directory routes (`/story/`, `/whats-involved/`, `/trainers/`, `/classes/`, `/get-in-touch/`) and legacy 2015 `.html` paths (`/story.html`, `/whats-involved.html`, `/trainers.html`, `/classes.html`, `/get-in-touch.html`) — are regression-tested in `scripts/regression-test.py` on every build.

## License

Dual-licensed under either the [Apache License, Version 2.0](LICENSE-APACHE) or the [MIT License](LICENSE-MIT), at your option.

© 2015–2026 [Sebastien Rousseau](https://sebastienrousseau.com/).
