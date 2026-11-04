# Embeds production.json into production.html as window.__STATE__ so the file works when opened directly.
import json,re,pathlib
d=pathlib.Path(__file__).parent
s=json.loads((d/"production.json").read_text())
h=(d/"production.html").read_text()
blob="/*__STATE__*/window.__STATE__="+json.dumps(s,ensure_ascii=False).replace("</","<\\/")+";/*__END__*/"
h=re.sub(r"/\*__STATE__\*/(.*?/\*__END__\*/)?",lambda m:blob,h,count=1,flags=re.S)
(d/"production.html").write_text(h)
