# Google Ads conversion tracking (Privacy Policy section 5).
# Tag loads on public site pages only, and never when the browser sends Global Privacy Control.
# Purchase conversion fires on thanks.html with the order value and the Stripe session ID (dedupe).
# Leave ADS_ID empty to ship no tag at all.
ADS_ID = ''            # e.g. 'AW-123456789'
ADS_LABEL = ''         # purchase conversion label, e.g. 'AbCdEfGhIjk'
if ADS_ID:
    base = ("<script>(function(){try{if(navigator.globalPrivacyControl){return;}}catch(e){}"
            "window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments);};"
            "gtag('js',new Date());gtag('set','restricted_data_processing',true);"
            "gtag('config','" + ADS_ID + "',{allow_google_signals:false,allow_ad_personalization_signals:false});"
            "var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id=" + ADS_ID + "';"
            "document.head.appendChild(s);})();</script>")
    conv = ("<script>(function(){try{if(navigator.globalPrivacyControl||!window.gtag){return;}"
            "var q=new URLSearchParams(location.search);var sid=q.get('session_id')||'';if(!sid||sid.indexOf('{')===0){return;}"
            "var v=q.get('product')==='year_one'?149:89;"
            "gtag('event','conversion',{send_to:'" + ADS_ID + "/" + ADS_LABEL + "',value:v,currency:'USD',transaction_id:sid});}catch(e){}})();</script>")
    for root, _, files in os.walk(OUT):
        for f in files:
            if not f.endswith('.html'): continue
            p = os.path.join(root, f)
            s = open(p).read()
            if 'googletagmanager.com/gtag' in s: continue
            s = s.replace('</head>', base + '\n</head>', 1)
            if f == 'thanks.html' and root == OUT and ADS_LABEL:
                s = s.replace('</body>', conv + '\n</body>', 1)
            open(p, 'w').write(s)
