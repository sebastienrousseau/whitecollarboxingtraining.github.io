<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->
# Changelog

All notable changes to `whitecollarboxingtraining.com` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to strict `+0.0.1` Semantic Versioning increments.

## [0.0.2] - 2026-11-01

### Added
- **Rust SSG & Skeletonic CSS Architecture**: Added `ssg.toml`, `_layouts/` (`base.html`, `header.html`, `footer.html`, `index.html`, `page.html`, `contact.html`, `404.html`, `styles.css`, `skeletonic.min.css`, `theme-init.js`, `main.js`), and `_posts/*.md`.
- **Legacy Code Archive**: Archived the 2015 Google App Engine Python 2.7 (`webapp2` + `jinja2`) application in `archive/legacy-gae-2015/`.
- **SEO, Google Search & AI Search Discovery**: Added Schema.org `@graph` JSON-LD (`ExerciseGym`, `SportsActivityLocation`, `LocalBusiness`, `Person` for Gary Foley and Sean Murphy, `OfferCatalog`), `llms.txt`, `llms-full.txt`, `agents.txt`, `.well-known/ai-plugin.json`, and `.well-known/mcp.json`.
- **Cloudflare Configuration**: Added `wrangler.toml`, `_headers`, `_redirects`, and `CNAME` (`whitecollarboxingtraining.com`).
- **Quality Gates**: Added `Makefile`, `audit/contrast.py`, `scripts/audit-contrast.py`, `scripts/validate-frontmatter.py`, `scripts/regression-test.py`, `tests/property.test.js`, and GitHub Actions CI workflows.

### Changed
- Upgraded visual contrast from legacy `#878787` (`3.5:1`) to WCAG 2.2 Level AAA (`>= 7.59:1`) across light and dark modes.
- Replaced deprecated third-party embeds (Facebook Login SDK, AddThis, Google+, HTTP Google Maps v2, and external Google Calendar iframe) with privacy-first, zero-cookie static components.

## [0.0.1] - 2026-11-01

### Fixed
- Enforced `https://whitecollarboxingtraining.com` in `sitemap.xml` and `robots.txt`.
- Added dual `Apache-2.0 OR MIT` license files.
