import json, datetime, re, os
H=os.path.dirname(os.path.abspath(__file__))
old=json.load(open(os.path.join(H,'..','state.json')))
sp=os.path.join(H,'state.json')
if os.path.exists(sp):
    s=json.load(open(sp))
else:
    s={"project":"Home Orbit — Batch 3 (Nov 2026)","currentStep":1,"steps":[],"plan":old['plan'],"scorecard":old['scorecard'],"concepts":[],"posts":[],"performance":[]}
    for st in old['steps']:
        st=dict(st); st['status']='idle'; st['report']=''; s['steps'].append(st)
    s['steps'][0]['status']='needs-you'
    s['steps'][0]['subtitle']='The Analyst reads Batches 1–2, then the Strategist turns it into the Batch 3 brief.'
    s['steps'][0]['action']={"label":"Read the Analyst + brief, answer the 4 questions in chat, then confirm.","phrase":"Looks right. Next step."}
    for p in s['plan']['specialists']: p['status']='idle'
    for p in s['plan']['specialists']:
        if p['key'] in('st',):p['status']='needs-you'
        if p['key']=='an':p['status']='done'
    for i in s['scorecard']['items']: i['score']=None
    s['performance']=[dict(r,note=('B1/B2 · '+(r.get('note') or ''))) for r in old.get('performance',[])]
# reports set by step scripts
s['updatedAt']=datetime.datetime.now(datetime.timezone.utc).isoformat()
json.dump(s,open(sp,'w'),ensure_ascii=False,indent=1)
d=open(os.path.join(H,'..','dashboard.html')).read()
d=d.replace('<title>Home Orbit Agency Board</title>','<title>Home Orbit Batch 3 Board</title>')
d=re.sub(r'window\.__STATE__ = .*?;\n','',d,flags=re.S)
d=d.replace('<script>','<script>\nwindow.__STATE__ = '+json.dumps(s,ensure_ascii=False).replace('</','<\\/')+';\n',1)
open(os.path.join(H,'dashboard.html'),'w').write(d)
print('ok',len(s['performance']))
