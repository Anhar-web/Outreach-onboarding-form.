import json,re
t=open('anhar/Batch_3_anhar_edits.txt').read()
ids=[(m.start(),m.group(1)) for m in re.finditer(r'id (b3p\d+)',t)]
E=json.load(open('posts_b3_edited.json')); D={p['id']:p for p in E}
out=[]
for k,(pos,pid) in enumerate(ids):
    end=ids[k+1][0] if k+1<len(ids) else len(t)
    # cut back to the header line start for next
    chunk=t[pos:end]
    lines=chunk.split('\n')[1:]
    sec=None; cur=[]; slides=[]; cap=[]; pin=[]; note=[]
    def flush():
        global cur
    buf={'slides':[], 'cap':[], 'pin':[], 'note':[]}
    for ln in lines:
        s=ln.strip()
        if re.match(r'^=+$',s) or re.match(r'^POST \d+ of 12',s) or re.match(r'^Evening \d',s): continue
        m=re.match(r'^\[?شريحة\s*(\d+)\]?$',s)
        if m: buf['slides'].append([]); sec='s'; continue
        if re.match(r'^\[?الكابشن\]?$',s): sec='c'; continue
        if re.match(r'^\[?التعليق المثبت\]?$',s): sec='p'; continue
        if s.startswith('(') and s.endswith(')') and re.search('[A-Za-z]',s): buf['note'].append(s[1:-1]); sec=None; continue
        if sec=='s': buf['slides'][-1].append(ln.rstrip())
        elif sec=='c': buf['cap'].append(ln.rstrip())
        elif sec=='p': buf['pin'].append(ln.rstrip())
    clean=lambda L:'\n'.join(x for x in L if x.strip()).strip()
    slides=[re.sub(r'  +',' ',clean(L)) for L in buf['slides']]
    p=dict(D[pid]); 
    p['slides_ar']=slides
    p['caption_ar']=re.sub(r'  +',' ',clean(buf['cap']))
    if buf['pin']: p['pinned_ar']=re.sub(r'  +',' ',clean(buf['pin']))
    else: p['pinned_ar_missing']=True
    p['anhar_note']=' '.join(buf['note'])
    p['status']='final'
    out.append(p)
for p in out:
    print(p['id'],len(p['slides_ar']),'pin' if not p.get('pinned_ar_missing') else 'NO PIN','|',p['slides_ar'][0][:60])
json.dump(out,open('posts_b3_anhar_raw.json','w'),ensure_ascii=False,indent=1)
