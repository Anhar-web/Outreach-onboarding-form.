"""Usage: python3 b4/setstep.py <json-patch-file>  — or import set_state(fn). Re-embeds state into b4/dashboard_b4.html."""
import json, os, datetime, sys
here=os.path.dirname(os.path.abspath(__file__)); app=os.path.dirname(here)
def save(s):
    s["updatedAt"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
    json.dump(s,open(os.path.join(app,"state.json"),"w"),ensure_ascii=False,indent=1)
    p=os.path.join(here,"dashboard_b4.html"); h=open(p,encoding="utf-8").read()
    a=h.index("window.__STATE__ = "); b=h.index(";\n",a)+2
    open(p,"w",encoding="utf-8").write(h[:a]+"window.__STATE__ = "+json.dumps(s,ensure_ascii=False).replace("</","<\\/")+";\n"+h[b:])
def load(): return json.load(open(os.path.join(app,"state.json"),encoding="utf-8"))
