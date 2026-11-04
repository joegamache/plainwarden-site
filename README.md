# plainwarden.com

Static site for PlainWarden, deployed by Netlify from the `public/` folder on the `main` branch.

## Build
```
pip install playwright   # only needed the first time an og-image must be rendered
python3 build/build_site.py
```
The build rewrites `public/`. Commit both the source change and the rebuilt `public/`.

## Layout
- `build/build_site.py` — builds the home page from `build/src/Main.dc.html`, then runs the modules below.
- `build/legal_v2.py` — Terms, Privacy, Refunds (attorney-reviewed text; don't edit without the owner).
- `build/guides.py` — the 15 how-to guides.
- `build/content.py` — sample plan page, `/learn/` articles, thank-you page.
- `build/articles/<slug>.html` — one article per file, with a JSON META header.
- `build/seo.py` — canonical, Open Graph, JSON-LD, related links, share image.
- `seo/` — SEO backlog and weekly log for the SEO agent (see SEO_AGENT.md).

## Publishing
Changes go through pull requests. Netlify builds a deploy preview for each PR; merging to `main` publishes.
