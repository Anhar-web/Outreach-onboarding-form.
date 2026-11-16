import json,os,re,html,datetime
from PIL import Image
APP=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H=os.path.join(APP,'prod_b3')
F=json.load(open(os.path.join(APP,'posts_b3_final.json')))
S=json.load(open(os.path.join(H,'state.json')))
dash=open(os.path.join(APP,'dashboard.html')).read()
css=re.search(r'<style>(.*?)</style>',dash,re.S).group(1)
css=css.replace('repeat(9,1fr)','repeat(7,1fr)').replace('repeat(9,64px)','repeat(7,64px)')
css+='.thumb{width:100%;border-radius:8px;border:1px solid var(--line);background:#000}.grp{font:600 11px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:6px 0}'
ev=lambda o:f"Evening {(o+1)//2} · {'7:15' if o%2 else '8:15'} PM"
files={}
cards=''
for p in sorted(F,key=lambda p:p['posting_order']):
    pid=p['id']; d=os.path.join(APP,'output_b3',pid); c=os.path.join(d,'contact.png')
    pc=S['pieces'].get(pid,{})
    st=pc.get('status','qa passed' if os.path.exists(os.path.join(APP,'output_b3','zips')) else 'building')
    img=''
    if os.path.exists(c):
        im=Image.open(c).convert('RGB'); im.thumbnail((1000,1000)); out=os.path.join(H,f'thumb-{pid}.jpg'); im.save(out,quality=78)
        files[f'thumb-{pid}.jpg']=out
        img=f'<img class="thumb" src="thumb-{pid}.jpg" alt="Contact sheet for {html.escape(p["title"])}, slide 1 at top-right">'
    else: img='<p class="empty">Not rendered yet.</p>'
    cards+=f'''<div class="cc"><div class="tags"><span class="tag acc">A · Static</span><span class="tag">{html.escape(p['label'])}</span><span class="tag">{html.escape(ev(p['posting_order']))}</span><span class="tag gold">{html.escape(st)}</span></div>
<b>{html.escape(p['title'])}</b><div class="hook ar" dir="rtl">{html.escape(p['slides_ar'][0])}</div>
<div class="note">{html.escape(pc.get('composition',''))}</div>{img}<div class="note">{html.escape(pc.get('notes',''))}</div></div>'''
steps=''
for s in S['stages']:
    steps+=f'<div class="st{" cur" if s["n"]==S["currentStage"] else ""}" data-s="{s["status"]}"><span class="dot">{"✓" if s["status"]=="done" else s["n"]}</span><span class="lbl">{html.escape(s["title"])}</span></div>'
def md(t):
    out=[];inl=False
    for ln in t.split('\n'):
        e=html.escape(ln); e=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',e); e=re.sub(r'`(.+?)`',r'<code>\1</code>',e)
        if ln.startswith('- '):
            if not inl: out.append('<ul>'); inl=True
            out.append('<li>'+e[2:]+'</li>'); continue
        if inl: out.append('</ul>'); inl=False
        if ln.startswith('### '): out.append('<h3>'+e[4:]+'</h3>')
        elif ln.strip(): out.append('<p>'+e+'</p>')
    if inl: out.append('</ul>')
    return '\n'.join(out)
cur=[s for s in S['stages'] if s['n']==S['currentStage']][0]
team=''.join(f'<div class="mem"><span class="av" data-s="{m["status"]}">{m["name"][:2].upper()}</span><div><b>{html.escape(m["name"])}</b><span>{html.escape(m["role"])}</span></div></div>' for m in S['team'])
sc=''.join(f'<div class="sc"><span>{html.escape(n)}</span><span class="bar"><i style="width:0"></i></span><span class="v">{w}</span></div>' for n,w in [("Attention — first frame",22),("Visual clarity",16),("Brand recognizability",10),("Freshness — not more of the same",10),("Storytelling",12),("Retention",12),("Production quality",10),("Conversion support",8)])
page=f'''<title>Home Orbit Production Board B3</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&family=El+Messiri:wght@600;700&display=swap">
<style>{css}</style>
<div class="wrap">
<header><div class="logo">مدار</div><div class="hgroup"><div class="k">Creative Production</div><h1>Home Orbit · Batch 3 production (12 static carousels)</h1></div><span class="chip">Updated {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime('%b %d, %H:%M')} (Saudi)</span><button class="tbtn" id="tt" type="button">Theme</button></header>
<nav class="stepper">{steps}</nav>
<section class="card"><div class="eyebrow">Stage {cur["n"]} of 7 <span class="pill" data-s="{cur["status"]}">{cur["status"]}</span></div><h2>{html.escape(cur["title"])}</h2><p class="sub">{html.escape(cur["subtitle"])}</p>
<div class="action"><div class="row"><span class="k">YOUR ACTION</span></div><div>{html.escape(cur["action"])}</div></div>
<div class="md">{md(cur["report"])}</div></section>
<section><h3 class="sec">The department</h3><div class="team">{team}</div></section>
<section><h3 class="sec">The production scorecard</h3>{sc}<p class="note">Creative QA scores each post once the build is done. Arabic legibility is a gate.</p></section>
<section><h3 class="sec">The pieces (posting order)</h3><div class="grp">Branch A · Static carousels (all 12). No video this batch.</div><div class="grid">{cards}</div></section>
<p class="note">The department proposes. You decide at every checkpoint.</p>
</div>
<script>try{{const t=localStorage.getItem('ho-theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}
document.getElementById('tt').onclick=()=>{{const r=document.documentElement;const dark=r.dataset.theme?r.dataset.theme==="dark":matchMedia('(prefers-color-scheme: dark)').matches;r.dataset.theme=dark?"light":"dark";try{{localStorage.setItem('ho-theme',r.dataset.theme)}}catch(e){{}}}};</script>'''
open(os.path.join(H,'production_board.html'),'w').write(page)
json.dump(files,open(os.path.join(H,'files.json'),'w'))
print(len(files),'thumbs')
