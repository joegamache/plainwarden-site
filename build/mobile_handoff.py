# Phone visitors: the questionnaire takes about 20 minutes, which is hard on a phone.
# On small screens, pages with a questionnaire link show a slim bar at the bottom that opens the
# visitor's own mail app with the (tagged) questionnaire link, so they can finish on a computer.
# Nothing is sent by us and nothing is stored except a "dismissed" flag for the tab.
HANDOFF = ("<script>(function(){try{if(!window.matchMedia||!matchMedia('(max-width: 700px)').matches){return;}"
           "try{if(sessionStorage.getItem('pw_handoff_x')){return;}}catch(e){}"
           "var a=document.querySelector('a[href^=\"https://tally.so/r/bZZkz2\"]');if(!a){return;}"
           "var url=a.href,sub='Finish my PlainWarden security plan',"
           "body='Questionnaire link (about 20 minutes; your answers build the plan):\\n\\n'+url+'\\n';"
           "var bar=document.createElement('div');bar.setAttribute('role','region');bar.setAttribute('aria-label','Finish on a computer');"
           "bar.style.cssText='position:fixed;left:0;right:0;bottom:0;z-index:50;background:#15212C;color:#fff;padding:10px 44px 10px 16px;"
           "font:15px/1.4 -apple-system,Segoe UI,Arial,sans-serif;box-shadow:0 -2px 8px rgba(0,0,0,.2)';"
           "var m=document.createElement('a');m.href='mailto:?subject='+encodeURIComponent(sub)+'&body='+encodeURIComponent(body);"
           "m.style.cssText='color:#7FC4A6;font-weight:700;text-decoration:underline';m.textContent='Email yourself the link';"
           "bar.appendChild(document.createTextNode('On your phone? The questionnaire takes about 20 minutes. '));bar.appendChild(m);"
           "bar.appendChild(document.createTextNode(' to finish on a computer.'));"
           "var x=document.createElement('button');x.type='button';x.setAttribute('aria-label','Close');x.textContent='\\u00d7';"
           "x.style.cssText='position:absolute;right:6px;top:4px;background:none;border:0;color:#fff;font-size:24px;line-height:1;padding:8px;cursor:pointer';"
           "x.onclick=function(){bar.remove();document.body.style.paddingBottom='';try{sessionStorage.setItem('pw_handoff_x','1');}catch(e){}};"
           "bar.appendChild(x);document.body.appendChild(bar);document.body.style.paddingBottom=(bar.offsetHeight+8)+'px';"
           "}catch(e){}})();</script>")
for root, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith('.html'): continue
        p = os.path.join(root, f)
        s = open(p).read()
        if 'pw_handoff_x' in s or 'tally.so/r/bZZkz2' not in s: continue
        # after the attribution script, so the emailed link keeps the channel/partner tags
        open(p, 'w').write(s.replace('</body>', HANDOFF + '\n</body>', 1))
