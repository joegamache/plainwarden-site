# SEO weekly log

Newest first. One entry per run: date, Search Console highlights (clicks, impressions, top queries, new pages indexed), what was proposed (PR link), what's next.

## 2026-11-09 — requested technical, intent and conversion audit
- Existing project retained; production crawl found 24/24 sitemap pages returning 200, working HTTPS/apex redirects and a genuine 404.
- Search Console: unauthenticated landing page only; no verified clicks, impressions, indexing or Core Web Vitals. PageSpeed API returned quota exhaustion (429).
- Proposed: clean canonical/OG/schema/internal/sitemap URLs; remove duplicate social metadata; clearer homepage WISP title/H1 and hub titles; article/guide start/pricing links; real article updated dates; primary source links and precise small-firm/consent wording; one sample-page H1; font preconnects.
- Target intents: WISP for tax preparers, WISP checklist, FTC Safeguards Rule and the fewer-than-5,000-consumers exception.
- Validation: build and build/check_seo.py pass (28 HTML pages / 24 indexable URLs); 390px browser checks pass on homepage, FTC article and sample. Tally entry opens; no forms/payments submitted.
- GitHub connector/direct Git upload were unavailable. Owner signed into the browser; uploaded through GitHub website on a review branch. Updated against main after PR #6 merged and rebuilt to preserve its thank-you-page instructions.
- Full findings and fact-check sources: seo/audit-2026-11-09.md. Netlify configuration, prices, checkout/form destinations, legal source text and tracking unchanged. Owner review/merge required by repository workflow.

## 2026-11-09 — weekly run
- Search Console: not reachable (no browser tools on this scheduled cloud run), so no clicks, impressions or indexing data. Worked from the backlog.
- Open PRs: only #3 (Terms Revision 3, held for attorney), not an SEO PR, so new work went ahead.
- New article: PTIN renewal and the WISP question (`/learn/ptin-renewal-wisp-question.html`). Target query: "ptin renewal wisp" / "form w-12 line 11". Timed for 2027 PTIN renewal season (IR-2026-130, Nov. 4, 2026).
- Inbound link added from "Do tax preparers need a WISP?" (its Form W-12 line 11 mention). Outbound links to the Safeguards Rule, Pub 5708 and checklist articles and the two-step login, vendor security and tabletop guides.
- Checks: build OK, canonical and JSON-LD present, sitemap entry present, no broken relative links, no horizontal scroll at 390px.
- Next: "Do I need a WISP if I work from home?". Read Search Console first if reachable.

## 2026-11-02 — first weekly run (first run of November)
- Search Console: not reachable (no browser tools on this scheduled cloud run), so no clicks, impressions or indexing data. Worked from the backlog.
- New article: IRS Publication 5708 explained (`/learn/irs-publication-5708-explained.html`). Target query: "irs publication 5708" / "pub 5708 wisp".
- Monthly refresh: "Do tax preparers need a WISP?" Added Form W-12 line 11 and IR-2026-92, tightened §314.6 wording and the FTC deadline, replaced an unsourced "usually the owner".
- Internal links: no broken links. The FTC Safeguards article had one inbound link (the Learn index), so it now gets links from the refreshed page and the new article.
- Technical fix: article JSON-LD dates were fixed at 2026-10-31; they now come from each article's META header.
- Outreach draft: `seo/outreach/2026-11-chapter-newsletter-guest-article.md` (the owner sends).
- PR: this pull request.
- Next: "PTIN renewal and the WISP question". Read Search Console first if reachable.

## 2026-10-31 — setup
- Sitemap submitted to Search Console; indexing requested for home, sample plan and "Do tax preparers need a WISP?".
- 3 articles, 15 guides, sample plan live. Structured data, canonical and Open Graph tags added.
