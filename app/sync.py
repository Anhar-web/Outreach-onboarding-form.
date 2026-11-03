# Embeds state.json into dashboard.html as window.__STATE__ so the file works when opened directly.
import json,re,pathlib
d=pathlib.Path(__file__).parent
s=json.loads((d/"state.json").read_text())
h=(d/"dashboard.html").read_text()
blob="/*__STATE__*/window.__STATE__="+json.dumps(s,ensure_ascii=False).replace("</","<\\/")+";/*__END__*/"
h=re.sub(r"/\*__STATE__\*/(.*?/\*__END__\*/)?",lambda m:blob,h,count=1,flags=re.S)
(d/"dashboard.html").write_text(h)
