# Channel and referral tagging (no cookies, nothing personal).
# A visit tagged ?ref=<partner> or ?utm_source=<channel> (or a Google Ads click, gclid) keeps that tag
# for the browser tab (sessionStorage) and adds it to the questionnaire link, so Tally's hidden fields
# record where the order came from. The order pipeline uses it for partner commissions and channel reports.
# A partner code (ref) is also remembered in localStorage for 60 days (key pw_ref: code + time), so a
# visitor who comes back later still counts for the partner. A newer partner link replaces it.
# Disclosed in the Privacy Policy, section 5.
ATTR = ("<script>(function(){try{var K=['ref','utm_source','utm_campaign'],q=new URLSearchParams(location.search),s={};"
        "try{s=JSON.parse(sessionStorage.getItem('pw_attr')||'{}')||{};}catch(e){s={};}"
        "var c=function(v){return String(v||'').toLowerCase().replace(/[^a-z0-9_-]/g,'').slice(0,40);};"
        "K.forEach(function(k){var v=c(q.get(k));if(v){s[k]=v;}});"
        "var D=5184e6,r=null;try{r=JSON.parse(localStorage.getItem('pw_ref')||'null');}catch(e){r=null;}"
        "if(s.ref&&c(q.get('ref'))){try{localStorage.setItem('pw_ref',JSON.stringify({v:s.ref,t:Date.now()}));}catch(e){}}"
        "else if(r&&r.v&&r.t&&Date.now()-r.t<D){if(!s.ref){s.ref=c(r.v);}}"
        "else if(r){try{localStorage.removeItem('pw_ref');}catch(e){}}"
        "if(q.get('gclid')&&!q.get('utm_source')){s.utm_source='google-ads';}"
        "try{sessionStorage.setItem('pw_attr',JSON.stringify(s));}catch(e){}"
        "if(!Object.keys(s).length){return;}"
        "var a=document.querySelectorAll('a[href^=\"https://tally.so/r/bZZkz2\"]');"
        "for(var i=0;i<a.length;i++){var u=new URL(a[i].href);K.forEach(function(k){if(s[k]&&!u.searchParams.get(k)){u.searchParams.set(k,s[k]);}});a[i].href=u.toString();}"
        "}catch(e){}})();</script>")
for root, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith('.html'): continue
        p = os.path.join(root, f)
        s = open(p).read()
        if 'pw_attr' in s or '</body>' not in s: continue
        open(p, 'w').write(s.replace('</body>', ATTR + '\n</body>', 1))
