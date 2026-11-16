import json,sys,re
C={c['id']:c for c in json.load(open('concepts_b3.json'))}
ban=['التوحد','أخصائي','اخصائي','كل أسبوعين','كل اسبوعين','يومه كامل','باقي يومه','ستة جوانب','حسي','تبدئي بخطة','تبدأي','—','الكل يقول','علاج','تشخيص']
for f in sys.argv[1:]:
  for p in json.load(open(f)):
    c=C[p['conceptId']]; issues=[]
    if p['slides_ar'][0]!=c['hook']: issues.append('HOOK MISMATCH')
    for i,s in enumerate(p['slides_ar'],1):
      for ln in s.split('\n'):
        if ln.rstrip().endswith('،'): issues.append(f's{i} line ends with comma')
      for b in ban:
        if b in s: issues.append(f's{i} has {b}')
      if len(s.split())>45: issues.append(f's{i} {len(s.split())} words')
    for sl in p['soft_lines']:
      if not any(sl in s for s in p['slides_ar']): issues.append('soft line not in slides')
    if 'الرابط في البايو' not in p['slides_ar'][-1]: issues.append('last slide no link')
    print(p['id'],c['n'],len(p['slides_ar']),'slides',issues or 'OK')
