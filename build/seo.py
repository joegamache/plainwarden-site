# Technical SEO pass. Executed at the end of build_site.py: canonical, Open Graph/Twitter tags,
# JSON-LD (Organization/WebSite, FAQPage, Article, BreadcrumbList), related links on guides, share image.
import os, re, json, html as _h
BASE = 'https://www.plainwarden.com/'
OG_IMG = BASE + 'og-image.png'

# Share image (1200x630), rendered once from HTML.
if not os.path.exists(OUT + '/og-image.png'):
    from playwright.sync_api import sync_playwright
    og = ('<html><body style="margin:0;width:1200px;height:630px;background:#1D5C47;font-family:Arial,Helvetica,sans-serif;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 90px;box-sizing:border-box">'
          '<div style="display:flex;align-items:center;gap:22px;font-size:46px;font-weight:800"><svg width="60" height="68" viewBox="0 0 28 32"><path d="M14 1 L26 6 V15 C26 23 20.5 28.5 14 31 C7.5 28.5 2 23 2 15 V6 Z" fill="none" stroke="#fff" stroke-width="2.4" stroke-linejoin="round"/><path d="M9 16 L12.5 19.5 L19.5 12" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>PlainWarden</div>'
          '<div style="font-size:64px;font-weight:800;line-height:1.1;margin-top:40px;max-width:980px">A written security plan built for your tax practice</div>'
          '<div style="font-size:32px;margin-top:28px;color:#CFE6DA">About 20 minutes of questions. Word and PDF by email.</div></body></html>')
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 630})
        pg.set_content(og); pg.screenshot(path=OUT + '/og-image.png'); b.close()

ORG = {'@type': 'Organization', '@id': BASE + '#org', 'name': 'PlainWarden', 'url': BASE, 'logo': BASE + 'favicon.svg', 'email': 'support@plainwarden.com'}

def faq_ld(s):
    qa = re.findall(r'<dt[^>]*>(.*?)</dt><dd[^>]*>(.*?)</dd>', s, re.S)
    strip = lambda x: _h.unescape(re.sub(r'<[^>]+>', '', x)).strip()
    if not qa: return None
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in qa]}

RELATED = {
 'learn': [('../sample-plan.html', 'See a sample plan'), ('../guides/index.html', 'How-to guides'), ('index.html', 'More articles')],
 'guides': [('../learn/wisp-checklist-small-tax-practice.html', 'WISP checklist for a small tax practice'), ('../learn/do-tax-preparers-need-a-wisp.html', 'Do tax preparers need a written security plan?'), ('../sample-plan.html', 'See a sample plan')],
}

for root, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith('.html'): continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, OUT).replace(os.sep, '/')
        s = open(path).read()
        if 'rel="canonical"' in s: continue
        url = BASE + (rel[:-len('index.html')] if rel.endswith('index.html') else rel[:-len('.html')])
        title = _h.unescape((re.search(r'<title>(.*?)</title>', s, re.S) or [None, 'PlainWarden'])[1]).strip()
        index_titles = {'learn/index.html': 'WISP Resources for Tax Preparers | PlainWarden',
                        'guides/index.html': 'Tax Practice Security How-To Guides | PlainWarden'}
        if rel in index_titles:
            title = index_titles[rel]
            s = re.sub(r'<title>.*?</title>', '<title>' + title + '</title>', s, count=1, flags=re.S)
        dm = re.search(r'<meta name="description" content="([^"]*)"', s)
        desc = _h.unescape(dm.group(1)) if dm else 'Written Information Security Plan generator for tax and accounting practices.'
        noindex = 'name="robots" content="noindex"' in s
        tags = ['<link rel="canonical" href="%s">' % url]
        if not dm: tags.append('<meta name="description" content="%s">' % _h.escape(desc))
        tags += ['<meta property="og:type" content="%s">' % ('article' if rel.startswith(('learn/', 'guides/')) and not rel.endswith('index.html') else 'website'),
                 '<meta property="og:site_name" content="PlainWarden">',
                 '<meta property="og:title" content="%s">' % _h.escape(title),
                 '<meta property="og:description" content="%s">' % _h.escape(desc),
                 '<meta property="og:url" content="%s">' % url,
                 '<meta property="og:image" content="%s">' % OG_IMG,
                 '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
                 '<meta property="og:image:alt" content="PlainWarden: a written security plan built for your tax practice">',
                 '<meta name="twitter:card" content="summary_large_image">']
        graph = [ORG] if not noindex else []
        if not noindex:
            if rel == 'index.html':
                graph += [{'@type': 'WebSite', 'name': 'PlainWarden', 'url': BASE, 'publisher': {'@id': BASE + '#org'}}]
                fq = faq_ld(s)
                if fq: graph.append(fq)
            elif rel.startswith(('learn/', 'guides/')) and not rel.endswith('index.html'):
                head = re.sub(r'\s*\|\s*PlainWarden$', '', title)
                # Article dates come from the META header; guides keep their review date.
                _am = ARTICLE_META.get(rel[len('learn/'):-len('.html')], {}) if rel.startswith('learn/') else {}
                graph.append({'@type': 'Article', 'headline': head, 'description': desc, 'url': url, 'image': OG_IMG,
                              'datePublished': _am.get('published', '2026-10-31'), 'dateModified': _am.get('updated', '2026-10-31'), 'inLanguage': 'en-US',
                              'author': {'@id': BASE + '#org'}, 'publisher': ORG, 'mainEntityOfPage': url})
                sec = 'Learn' if rel.startswith('learn/') else 'How-to guides'
                graph.append({'@type': 'BreadcrumbList', 'itemListElement': [
                    {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': BASE},
                    {'@type': 'ListItem', 'position': 2, 'name': sec, 'item': BASE + rel.split('/')[0] + '/'},
                    {'@type': 'ListItem', 'position': 3, 'name': head, 'item': url}]})
        if not noindex:
            graph.append({'@type': 'WebPage', '@id': url + '#webpage', 'url': url,
                          'name': title, 'description': desc, 'inLanguage': 'en-US',
                          'publisher': {'@id': BASE + '#org'}})
            tags.append('<script type="application/ld+json">%s</script>' % json.dumps(
                {'@context': 'https://schema.org', '@graph': graph}, separators=(',', ':')).replace('</', '<\\/'))
        s = s.replace('</head>', '\n'.join(tags) + '\n</head>', 1)
        # Related reading on articles and guides (not on index pages).
        sec = rel.split('/')[0]
        if sec in RELATED and not rel.endswith('index.html') and 'class="related"' not in s:
            links = ''.join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in RELATED[sec] if not h.endswith(f))
            box = '<div class="box related"><h2 style="margin-top:12px">Related</h2><ul>%s</ul></div>' % links
            s = s.replace('<p class="muted">General guidance', box + '<p class="muted">General guidance', 1)
        # Give informational visitors an immediate, clearly labelled next step.
        if sec in RELATED and not rel.endswith('index.html'):
            cta = ('<aside class="box" aria-label="Create your WISP"><h2>Build your practice’s WISP</h2>'
                   '<p>Turn your answers into an editable Word plan, a PDF and an action plan. '
                   'Review the result and implement the safeguards for your firm.</p>'
                   '<p><a href="https://tally.so/r/bZZkz2?plan=yearone">Start your plan</a> · '
                   '<a href="/#pricing">See pricing</a> · <a href="/sample-plan">See a sample WISP</a></p></aside>')
            s = s.replace('<div class="box related">', cta + '<div class="box related">', 1)
        # Use the same clean URL format as Netlify Pretty URLs, including in schema.
        def clean_link(match):
            href = match.group(1)
            if not href.startswith(('https:', 'http:', 'mailto:', '#')):
                if href.startswith('index.html'):
                    href = './' + href[len('index.html'):]
                else:
                    href = re.sub(r'index\.html(?=[?#]|$)', '', href)
                href = re.sub(r'\.html(?=[?#]|$)', '', href)
            return 'href="' + (href or './') + '"'
        s = re.sub(r'href="([^"]*)"', clean_link, s)
        # Articles show their actual editorial dates instead of the guide template date.
        if rel.startswith('learn/') and not rel.endswith('index.html'):
            am = ARTICLE_META[rel[len('learn/'):-len('.html')]]
            s = s.replace('last reviewed ' + GUIDES_REVIEWED,
                          'updated <time datetime="' + am['updated'] + '">' + am['updated'] + '</time>')
        s = s.replace('<link rel="stylesheet" href="https://fonts.googleapis.com',
                      '<link rel="preconnect" href="https://fonts.googleapis.com">'
                      '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">'
                      '<link rel="stylesheet" href="https://fonts.googleapis.com') if 'rel="preconnect"' not in s else s
        open(path, 'w').write(s)
