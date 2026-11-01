---
title: "Made with SSG & Skeletonic CSS | White Collar Boxing Training"
description: "Technical overview of how whitecollarboxingtraining.com is compiled with the Rust Static Site Generator (SSG) and Skeletonic CSS."
layout: "page"
permalink: "https://whitecollarboxingtraining.com/made-with-ssg/"
eyebrow: "Web Engineering"
headline: "Built with Rust SSG and Skeletonic CSS"
lead: "Compiled natively into zero-dependency static HTML, CSS, and structured metadata deployed at the Cloudflare edge."
banner: "https://whitecollarboxingtraining.com/images/banner/banner.webp"
logo: "https://whitecollarboxingtraining.com/images/logo/whitecollarboxingtraining.svg"
date: "2026-11-01T09:00:00Z"
---
## Static-First Architecture

`whitecollarboxingtraining.com` is compiled using the Rust [Static Site Generator (SSG)](https://static-site-generator.com/) and styled with [Skeletonic CSS](https://skeletonic.com/).

- **Compiler**: Rust `ssg` (`ssg build --content _posts --template _layouts --output public`)
- **Edge Delivery**: Cloudflare (`whitecollarboxingtraining.com`) with Post-Quantum TLS 1.3 and strict Content Security Policy headers
- **Accessibility**: Verified against WCAG 2.2 Level AAA contrast ratios (`>= 7.0:1`)
