"""Validate built crawl targets, metadata, schema, anchors and purchase links (stdlib only)."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent / 'public'
BASE = 'https://www.plainwarden.com/'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []; self.ids = set(); self.schema = []; self.script = None
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs); self.tags.append((tag, attrs))
        if attrs.get('id'): self.ids.add(attrs['id'])
        if tag == 'script' and attrs.get('type') == 'application/ld+json': self.script = ''
    def handle_data(self, data):
        if self.script is not None: self.script += data
    def handle_endtag(self, tag):
        if tag == 'script' and self.script is not None:
            self.schema.append(json.loads(self.script)); self.script = None
    def attr(self, tag, key, value, result):
        return [a.get(result, '') for t, a in self.tags if t == tag and a.get(key) == value]

def resolve(url):
    path = ROOT / unquote(urlsplit(url).path).lstrip('/')
    if path.is_dir(): return path / 'index.html'
    return path if path.exists() else path.with_suffix('.html')

pages = {p: Page(p.read_text()) for p in ROOT.rglob('*.html')}
urls = [n.text for n in ET.parse(ROOT / 'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(urls) == len(set(urls)), 'Duplicate sitemap URLs'
indexable = set()
for path, page in pages.items():
    rel = path.relative_to(ROOT).as_posix()
    url = BASE + (rel[:-10] if rel.endswith('index.html') else rel[:-5])
    assert page.attr('link', 'rel', 'canonical', 'href') == [url], rel
    assert len(page.attr('meta', 'name', 'description', 'content')) == 1, rel
    assert len(page.attr('meta', 'property', 'og:title', 'content')) == 1, rel
    assert page.attr('meta', 'property', 'og:url', 'content') == [url], rel
    assert sum(t == 'h1' for t, _ in page.tags) == 1, rel
    noindex = any('noindex' in v for v in page.attr('meta', 'name', 'robots', 'content'))
    if not noindex:
        indexable.add(url)
        assert page.schema, rel
        graph = page.schema[0]['@graph']
        assert any(n['@type'] == 'WebPage' and n['url'] == url for n in graph), rel
        for node in graph:
            if node['@type'] == 'Article':
                assert node['url'] == url and node['dateModified'] >= node['datePublished'], rel
        if rel.startswith(('learn/', 'guides/')) and not rel.endswith('index.html'):
            assert 'https://tally.so/r/bZZkz2?plan=yearone' in page.attr('a', 'href', 'https://tally.so/r/bZZkz2?plan=yearone', 'href'), rel
    else:
        assert url not in urls and not page.schema, rel
    for tag, attrs in page.tags:
        target = attrs.get('href') if tag in ('a', 'link') else attrs.get('src') if tag in ('img', 'script') else None
        if not target: continue
        absolute = urljoin(url, target)
        if urlsplit(absolute).netloc != urlsplit(BASE).netloc: continue
        dest = resolve(absolute)
        assert dest.is_file(), (rel, target)
        fragment = urlsplit(absolute).fragment
        if fragment and dest in pages: assert unquote(fragment) in pages[dest].ids, (rel, target)
assert set(urls) == indexable, (set(urls) ^ indexable)
assert 'Sitemap: ' + BASE + 'sitemap.xml' in (ROOT / 'robots.txt').read_text()
print(f'PASS: {len(pages)} HTML pages; {len(urls)} indexable sitemap URLs; canonical/social metadata, JSON-LD, local links/anchors, noindex exclusions and article CTAs.')
