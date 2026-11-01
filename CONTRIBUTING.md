<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->
# Contributing to whitecollarboxingtraining.com

Thank you for contributing to **White Collar Boxing Training** (`whitecollarboxingtraining.com`).

## Workflow

1. Create a release iteration branch (`feat/v<next-version>`, incrementing by `0.0.1`).
2. Edit Markdown content in `_posts/` or templates in `_layouts/`.
3. Build and verify locally:
   ```bash
   make build
   make verify
   ```
4. Ensure all commits follow Conventional Commits (`<type>: <subject>`, max 50 chars) and pass `make verify`.

## Licensing

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in this repository shall be dual-licensed under `Apache-2.0 OR MIT`, without any additional terms or conditions.
