"""Make one tagged QR PNG per post.
Usage: python3 make_qr.py b4p1:outings b4p2:assessment ...
Keys are those in links.md. Output: qr/<post>.png plus qr/index.txt with the encoded URLs."""
import sys, os, qrcode
BASE = "https://madar-albayt.tiiny.site/"
DEST = {"assessment": "", "plan": "plan", "sleep": "focus=sleep", "outings": "focus=outings",
        "communication": "focus=communication", "food": "focus=food",
        "transitions": "focus=transitions", "emotions": "focus=emotions"}
os.makedirs("qr", exist_ok=True)
lines = []
for arg in sys.argv[1:]:
    post, key = arg.split(":")
    q = "&".join(x for x in [DEST[key], "src=qr", f"post={post}"] if x)
    url = f"{BASE}?{q}"
    img = qrcode.make(url, box_size=20, border=2)
    img.save(f"qr/{post}.png")
    lines.append(f"{post}\t{key}\t{url}")
open("qr/index.txt", "a").write("\n".join(lines) + "\n")
print("\n".join(lines))
