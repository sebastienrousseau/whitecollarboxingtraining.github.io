<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->
# Development Guide

## Prerequisites

- Rust `ssg` (`0.0.69` or newer)
- Python `3.11+` (`Pillow` optional for `.webp` generation)
- Node.js `20+`

## Local Build & Verification

```bash
# Compile _posts/ and _layouts/ into public/ and docs/
make build

# Run full lint, test, contrast, and ssg audit suite
make verify

# Serve locally on http://127.0.0.1:8000
make serve
```

## Directory Structure

- `_posts/` — Markdown content pages with YAML frontmatter
- `_layouts/` — Handlebars/SSG HTML templates, `styles.css`, `skeletonic.min.css`, `theme-init.js`, and `main.js`
- `scripts/` — Post-build SEO/AI generator (`post-build.py`), regression suite (`regression-test.py`), and validators
- `audit/` — Mathematical WCAG 2.2 Level AAA contrast auditor (`contrast.py`)
- `archive/legacy-gae-2015/` — Archived 2015 Google App Engine Python 2.7 codebase
- `public/` & `docs/` — Compiled static output and Cloudflare edge configuration artifacts
