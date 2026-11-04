# Per post: a PDF (one slide per page, in order) and a ZIP of the full-size PNGs.
import glob,os,re,sys,zipfile
from PIL import Image
key=lambda x:[int(n) if n.isdigit() else n for n in re.split(r"(\d+)",x)]
names={"p5":"vacuum","p7":"ipad","p2":"azeema","p10":"cries","p3":"bedtime","p6":"shoes","p4":"plate","p9":"name","p1":"park","p8":"aunt-bedtime"}
os.makedirs("downloads",exist_ok=True)
for k in sys.argv[1:]:
    files=sorted(glob.glob(f"output/{k}/slide-*.png"),key=key)
    base=f"downloads/{k}-{names.get(k,k)}"
    ims=[Image.open(f).convert("RGB") for f in files]
    ims[0].save(base+".pdf",save_all=True,append_images=ims[1:],resolution=144)
    with zipfile.ZipFile(base+"-png.zip","w",zipfile.ZIP_DEFLATED) as z:
        for i,f in enumerate(files,1): z.write(f,f"{k}-{names.get(k,k)}/{i:02d}-{os.path.basename(f)}")
    print(base,len(files),"slides")
