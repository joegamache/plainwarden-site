import re, html, os
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(HERE,'src','Main.dc.html')
OUT=os.path.join(HERE,'..','public')
os.makedirs(OUT, exist_ok=True)
s=open(SRC).read()
FORM='https://tally.so/r/bZZkz2'
def sub(old,new,count=1):
    global s
    n=s.count(old); assert n>=count, (old[:60], n)
    s=s.replace(old,new) if count=='all' else s.replace(old,new,count)
# head/body cleanup
head_m=re.search(r'<helmet>(.*?)</helmet>',s,re.S); head=head_m.group(1)
s=s.replace(head_m.group(0),'')
s=re.sub(r'<script src="./support.js"></script>\n','',s)
s=s.replace('<x-dc>\n','').replace('</x-dc>\n','')
s=re.sub(r'<script type="text/x-dc".*?</script>\n','',s,flags=re.S)
meta=('<meta name="viewport" content="width=device-width,initial-scale=1">\n'
 '<meta name="description" content="PlainWarden builds your firm\'s Written Information Security Plan (WISP) from a 20-minute questionnaire: what you do today, what to fix with dates, and what to confirm. Word and PDF, for tax and accounting practices.">\n'
 '<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'
 '<meta property="og:title" content="PlainWarden: your written security plan in about 20 minutes">\n'
 '<meta property="og:description" content="An honest WISP for tax and accounting practices, built from how your firm actually works.">\n')
s=s.replace('<title>PlainWarden home</title>','<title>PlainWarden | Written Information Security Plan for Tax Practices</title>\n'+meta+head.strip()+'\n<style>html{scroll-behavior:smooth}</style>')
# CTAs
s=s.replace('href="#start"','href="'+FORM+'?plan=yearone"')
plan_btn='href="'+FORM+'?plan=yearone" style="margin-top: auto; background: #FFFFFF; color: #15212C'
assert s.count(plan_btn)==1
s=s.replace(plan_btn,'href="'+FORM+'?plan=plan" style="margin-top: auto; background: #FFFFFF; color: #15212C')
# footer links
for a,b in [('#terms','terms.html'),('#privacy','privacy.html'),('#refunds','refunds.html')]:
    sub('href="'+a+'"','href="'+b+'"')
sub('<a href="terms.html" style="color: #B8C2BD">Terms</a>','<a href="sample-plan.html" style="color: #B8C2BD">Sample plan</a>\n<a href="guides/index.html" style="color: #B8C2BD">Guides</a>\n<a href="learn/index.html" style="color: #B8C2BD">Learn</a>\n<a href="terms.html" style="color: #B8C2BD">Terms</a>')
sub('<a href="#pricing" style="background: #FFFFFF; color: #15212C; text-decoration: none; font-weight: 600; font-size: 17px; padding: 15px 26px; border-radius: 6px; border: 1px solid #B9C2BD; min-height: 44px; box-sizing: border-box; display: inline-flex; align-items: center">See pricing</a>','<a href="#pricing" style="background: #FFFFFF; color: #15212C; text-decoration: none; font-weight: 600; font-size: 17px; padding: 15px 26px; border-radius: 6px; border: 1px solid #B9C2BD; min-height: 44px; box-sizing: border-box; display: inline-flex; align-items: center">See pricing</a> <a href="sample-plan.html" style="background: #FFFFFF; color: #15212C; text-decoration: none; font-weight: 600; font-size: 17px; padding: 15px 26px; border-radius: 6px; border: 1px solid #B9C2BD; min-height: 44px; box-sizing: border-box; display: inline-flex; align-items: center">See a sample plan</a>')
sub('<span>support@plainwarden.com</span>','<a href="mailto:support@plainwarden.com" style="color: #B8C2BD">support@plainwarden.com</a>')
sub('© 2026 PlainWarden LLC.','© 2026 PlainWarden.')
# wording fixes
sub('>confirmed in place<','>reported in place<')
sub('>Six, filled in from your answers where possible','>Seven, filled in from your answers where possible')
# merged Year One list
old_list=re.search(r'<li>Your complete plan, Word and PDF</li>\n<li>Plan updates when.*?</li>\n</ul>',s,re.S).group(0)
Q=''
items=['Your complete plan, Word and PDF',
 'Reminders when action items are due, and a tracker for gaps and items to confirm'+Q,
 'Yearly staff security training with sign-off records'+Q,
 'How-to guides for common fixes'+Q,
 'Vendor tracker and quarterly check-in emails'+Q,
 'Plan updates when your practice or the rules change, with an October PTIN-season re-review'+Q,
 'Audit-ready binder'+Q]
s=s.replace(old_list,'\n'.join('<li>'+i+'</li>' for i in items)+'\n</ul>\n<p style="margin: 0; color: #4A5865; font-size: 14px">Everything in Year One is ready when your plan arrives: the links to your tracker and staff training come in the same email.</p>')

# --- legal review (2026-10-30): soften or substantiate marketing claims ---
CLAIMS=[
 ('Your written security plan in about 20 minutes, kept current all year.','About 20 minutes of questions. A written security plan built for your practice.'),
 ('Every paid tax preparer needs a Written Information Security Plan.','The IRS and FTC expect paid tax preparers to keep a Written Information Security Plan.'),
 ('When you renew your PTIN, you confirm you have a data security plan.','PTIN renewal reminds every preparer: you need a written data security plan.'),
 ('The IRS sample is a 29-page fill-in-the-blanks document. Here is why it is worth 15 minutes now.','The IRS sample is a long fill-in-the-blanks document. Here is why it is worth doing now.'),
 ('It is the first thing asked for after a breach','It is what people ask to see after a breach'),
 ('Regulators, insurers and your own clients will want to see the plan you had in place, and whether you followed it.','Regulators, insurers and your own clients may ask for the plan you had in place, and whether you followed it.'),
 ('with every requirement traced to the rule it comes from.','with regulatory references for the requirements it covers.'),
 ('Free templates make you claim everything. Your plan should match your practice.','A plan that claims everything helps no one. Yours should match your practice.'),
 ("Many free plan builders require you to check every box to continue, so the finished document says you do things you don't. After a breach, a plan you didn't follow can hurt more than help.","A template that makes you check every box can leave you with a plan that says you do things you don't. After a breach, a plan you didn't follow can hurt more than help."),
 ('>Same 30+ steps for every firm<','>Same steps for every firm<'),
 ('>Typical free template<','>Check-every-box template<'),
 ('>Under 5,000 clients<','>Fewer than 5,000 consumers<'),
 ('>Applies the 16 CFR 314.6 exemption<','>Accounts for the 16 CFR 314.6 exceptions<'),
]
for a,b in CLAIMS:
    assert s.count(a)==1,(a,s.count(a)); s=s.replace(a,b)
import re as _re
for label in ['Sales call before download','Attachments']:
    pat=_re.compile(r'<tr>(?:(?!</tr>).)*?'+label+r'(?:(?!</tr>).)*?</tr>\n?',_re.S)
    assert len(pat.findall(s))==1,(label,len(pat.findall(s))); s=pat.sub('',s)
open(OUT+'/index.html','w').write(s)

# ---------- legal pages ----------
FAV='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M14 1 L26 6 V15 C26 23 20.5 28.5 14 31 C7.5 28.5 2 23 2 15 V6 Z" fill="#1D5C47"/><path d="M9 16 L12.5 19.5 L19.5 12" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
open(OUT+'/favicon.svg','w').write(FAV)
def page(fname,title,body):
    doc=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | PlainWarden</title><meta name="robots" content="noindex"><link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;600;700;800&amp;display=swap">
<style>
body{{margin:0;background:#F5F6F3;color:#15212C;font-family:'Public Sans',system-ui,-apple-system,'Segoe UI',sans-serif;font-size:17px;line-height:1.65}}
a{{color:#1D5C47}} header{{background:#fff;border-bottom:1px solid #D5DAD6;padding:18px 16px}}
.wrap{{max-width:760px;margin:0 auto}} .brand{{display:inline-flex;align-items:center;gap:10px;text-decoration:none;color:#15212C;font-weight:800;font-size:21px}}
main{{padding:40px 16px 64px}} h1{{font-size:32px;line-height:1.2;margin:0 0 8px}} h2{{font-size:19px;margin:28px 0 6px}}
.draft{{background:#FFF6E0;border:1px solid #E7C66B;border-radius:6px;padding:12px 16px;margin:0 0 28px;font-size:15px}}
.muted{{color:#4A5865;font-size:15px}} table{{border-collapse:collapse;width:100%;font-size:15px;margin:8px 0}} td,th{{border:1px solid #D5DAD6;padding:8px 10px;text-align:left;vertical-align:top}} th{{background:#EAF2EE}}
.tw{{overflow-x:auto}} .box{{background:#fff;border:1px solid #D5DAD6;border-radius:6px;padding:4px 20px}}
footer{{border-top:1px solid #D5DAD6;padding:24px 16px;font-size:14px;color:#4A5865}} footer a{{margin-right:16px;display:inline-block;overflow-wrap:anywhere}}
</style></head><body>
<header><div class="wrap"><a class="brand" href="index.html"><svg width="24" height="28" viewBox="0 0 28 32" aria-hidden="true"><path d="M14 1 L26 6 V15 C26 23 20.5 28.5 14 31 C7.5 28.5 2 23 2 15 V6 Z" fill="none" stroke="#1D5C47" stroke-width="2.4" stroke-linejoin="round"/><path d="M9 16 L12.5 19.5 L19.5 12" fill="none" stroke="#1D5C47" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>PlainWarden</a></div></header>
<main><div class="wrap">
<h1>{title}</h1>
<p class="draft"><strong>Draft, under legal review.</strong> This page is a working draft and may change before PlainWarden opens for general sale. Questions: <a href="mailto:support@plainwarden.com">support@plainwarden.com</a>.</p>
{body}
</div></main>
<footer><div class="wrap"><a href="index.html">Home</a><a href="terms.html">Terms</a><a href="privacy.html">Privacy</a><a href="refunds.html">Refunds</a><a href="mailto:support@plainwarden.com">support@plainwarden.com</a><p>PlainWarden is a tool to help tax and accounting firms create and maintain a Written Information Security Plan. It is not legal advice and does not certify compliance.</p></div></footer>
</body></html>'''
    open(OUT+'/'+fname,'w').write(doc)
def P(head,txt): return f'<h2>{head}</h2><p>{txt}</p>'
E='<a href="mailto:support@plainwarden.com">support@plainwarden.com</a>'
exec(open(os.path.join(HERE,'legal_v2.py')).read())
exec(open(os.path.join(HERE,'guides.py')).read())
exec(open(os.path.join(HERE,'content.py')).read())
open(OUT+'/robots.txt','w').write('User-agent: *\nAllow: /\nSitemap: https://www.plainwarden.com/sitemap.xml\n')
URLS=['', 'guides/', 'sample-plan.html', 'learn/']+['guides/'+x+'.html' for x in GUIDE_SLUGS]+['learn/'+x+'.html' for x in ARTICLE_SLUGS]
open(OUT+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://www.plainwarden.com/'+u+'</loc></url>' for u in URLS)+'</urlset>\n')
print(os.listdir(OUT))
exec(open(os.path.join(HERE,'seo.py')).read())
