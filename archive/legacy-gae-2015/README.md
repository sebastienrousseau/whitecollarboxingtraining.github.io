# Legacy Google App Engine Codebase (2015 Archive)

This directory (`archive/legacy-gae-2015/`) preserves the original 2015 Google App Engine (Python 2.7, `webapp2`, and `jinja2`) implementation of **White Collar Boxing Training** (`whitecollarboxingtraining.com`).

In `v0.0.2`, the site was ported to the Rust `static-site-generator` (`ssg`) and Skeletonic CSS while retaining and expanding all original content, trainer profiles, Barnet London gym location details, and URLs.

## Archived Contents

- `app.yaml` — Google App Engine Python 2.7 runtime and static asset routing configuration
- `main.py` — `webapp2` request handlers for `/`, `/story.html`, `/whats-involved.html`, `/trainers.html`, `/classes.html`, and `/get-in-touch.html`
- `templates/` — Jinja2 HTML templates and partial views (`templates/src/`)
- `stylesheets/` — Legacy Skeleton 1.2 CSS (`skeleton.css`, `normalize.css`, `custom.css`, `print.css`, `wcbt-min.css`)
- `javascripts/` — Legacy jQuery 1.10.1 and HTML5 shim scripts (`app.js`, `wcbt.min.js`)
- `images/` — Original raster/SVG banners, icons, favicons, and trainer photographs (`gary.jpg`, `sean.jpg`)
- `videos/` — Original training video (`gary.mp4`, `gary.ogv`)
- `humans.txt`, `robots.txt`, `sitemap.xml` — Original 2015 metadata files
