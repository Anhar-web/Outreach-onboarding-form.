# Makes small JPG previews (540px wide) of rendered slides for the dashboard.
import glob,os,re,sys,json
from PIL import Image
ids=sys.argv[1:]
for k in ids:
    os.makedirs(f"preview/{k}",exist_ok=True)
    for f in glob.glob(f"output/{k}/slide-*.png"):
        im=Image.open(f).convert("RGB"); im=im.resize((540,675),Image.LANCZOS)
        im.save(f"preview/{k}/"+os.path.basename(f).replace(".png",".jpg"),quality=82,optimize=True)
s=json.load(open("production.json"))
key=lambda x:[int(n) if n.isdigit() else n for n in re.split(r"(\d+)",x)]
for pc in s["pieces"]:
    if pc["postId"] in ids:
        pc["assets"]=sorted(glob.glob(f"preview/{pc['postId']}/slide-*.jpg"),key=key)
json.dump(s,open("production.json","w"),ensure_ascii=False,indent=2)
