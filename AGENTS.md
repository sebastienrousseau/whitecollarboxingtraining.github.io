<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->
# AGENTS.md — Repository Instructions for AI Coding Agents

Mandatory instructions for all agents working on `whitecollarboxingtraining.github.io` (`https://whitecollarboxingtraining.com`).

## 1. Build & Compilation Invariant

- **Source of Truth**: Edit content in `_posts/*.md` and templates/styles in `_layouts/*`.
- **Legacy Archive**: Never delete `archive/legacy-gae-2015/`. It preserves the historical 2015 Google App Engine Python 2.7 implementation.
- **Compilation**: Always run `make build` (`ssg build --content _posts --template _layouts --output public` followed by `python3 scripts/post-build.py`) and verify with `make verify`.

## 2. Domain & Fact Accuracy

Never invent trainers, addresses, or phone numbers. Use only verified repository facts:
- **Domain**: `https://whitecollarboxingtraining.com` (`CNAME`, `wrangler.toml`, `ssg.toml`)
- **Address**: White Collar Boxing, Anchor Hall, Bulwer Rd, Barnet, London EN5 5EX (`51.651161, -0.17987`)
- **Head Coach**: Gary Foley — `07749 116927` (`+44 7749 116927`), 20+ years white collar boxing experience in London, 9+ years qualified trainer.
- **Senior Coach**: Sean Murphy — `07729 980677` (`+44 7729 980677`), Commonwealth Games Gold Medallist, British Lonsdale Belt Outright Winner, World Title contender.

## 3. Quality & Accessibility Gates

All changes must pass `make verify` with zero warnings:
1. `make lint` (`verify_release_version.sh`, `validate_readme.py`, `release_notes.py --check`, `validate_spdx_headers.py`)
2. `make test` (`regression-test.py`, `node --test tests/property.test.js`)
3. `make audit` (`audit-contrast.py`, `audit/contrast.py`, `validate-frontmatter.py`, `ssg audit`)
