import json,sys,datetime
s=json.load(open("state.json"))
def save():
    s["updatedAt"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
    json.dump(s,open("state.json","w"),ensure_ascii=False,indent=1)
