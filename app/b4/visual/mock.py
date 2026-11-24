"""Batch 4 visual system mocks: 5 looks rendered with SVG/CSS (no photos, no AI images).
Copy on the mocks is from Anhar's legacy posts, for layout only."""
import json, sys
C = dict(deep="#005A70", night="#003F4F", ink="#0E2F38", teal="#00A9A5", tealDeep="#007A77",
         tealMist="#DCEEEC", pearl="#F6F3EB", sand="#EBD6BC", gold="#C9935A", goldDeep="#8A5A2B",
         )
FONTS = "https://fonts.googleapis.com/css2?family=El+Messiri:wght@600;700&family=Tajawal:wght@500;700&display=block"
DEFS = """
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="4"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.09 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#00222b" flood-opacity="0.35"/></filter>
<filter id="shs" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="#00222b" flood-opacity="0.25"/></filter>
<filter id="deckle" x="-5%" y="-5%" width="110%" height="115%"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="9" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="9"/><feDropShadow dx="0" dy="12" stdDeviation="14" flood-color="#00222b" flood-opacity="0.35"/></filter>
<radialGradient id="glow"><stop offset="0" stop-color="#F3C98B" stop-opacity="0.85"/><stop offset="1" stop-color="#F3C98B" stop-opacity="0"/></radialGradient>
"""
def wave(y, amp, phase, color, flt="sh", w=1080, h=1350, top=False):
    import math
    pts = []
    for i in range(0, 13):
        x = i * 90
        yy = y + amp * math.sin(i * 0.9 + phase)
        pts.append((x, yy))
    d = f"M -20 {pts[0][1]:.0f} " + " ".join(f"Q {x-45:.0f} {yy-amp*0.6:.0f} {x:.0f} {yy:.0f}" for x, yy in pts[1:]) + " L 1100 " + ("-20" if top else "1370") + " L -20 " + ("-20" if top else "1370") + " Z"
    return f'<path d="{d}" fill="{color}" filter="url(#{flt})"/>'

def page(bg, svg_art, html_text, extra_css=""):
    return f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><link rel="stylesheet" href="{FONTS}">
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;background:{bg};position:relative;font-family:Tajawal}}
svg.art{{position:absolute;inset:0}} .t{{position:absolute;color:{C['ink']}}}
h1{{font-family:'El Messiri';font-weight:700;line-height:1.35}} p{{font-weight:500;line-height:1.55}} b{{font-weight:700}}
.hl{{color:{C['tealDeep']}}} {extra_css}</style></head><body>
<svg class="art" width="1080" height="1350" viewBox="0 0 1080 1350"><defs>{DEFS}</defs>{svg_art}<rect width="1080" height="1350" fill="#fff" filter="url(#grain)" opacity="0.9"/></svg>
{html_text}</body></html>"""

def look1(ground, hook, inner=False):
    # Layered Paper Night: paper waves frame a deckled pearl card; one warm light.
    g = C[ground]
    layers = [wave(1060, 45, 0.3, "#0B4D5E"), wave(1120, 40, 1.9, C['deep']), wave(1185, 34, 0.8, C['tealDeep']), wave(1245, 28, 2.6, C['sand']), wave(1300, 20, 1.2, C['pearl'])]
    tops = [wave(150, 35, 2.0, C['deep'], top=True), wave(95, 28, 0.4, "#0B4D5E", top=True)]
    if inner:
        layers = layers[2:]; tops = tops[1:]
    moon = '' if inner else f'<circle cx="190" cy="120" r="120" fill="url(#glow)"/><path d="M 210 70 a 55 55 0 1 0 0 110 a 42 42 0 1 1 0 -110 Z" fill="{C["gold"]}" filter="url(#shs)"/>'
    stars = '' if inner else "".join(f'<path d="M {x} {y} l 6 14 l 15 2 l -11 10 l 3 15 l -13 -8 l -13 8 l 3 -15 l -11 -10 l 15 -2 Z" fill="{C["pearl"]}" opacity="0.8"/>' for x, y in [(900, 120), (980, 210), (760, 70), (430, 60)])
    card = stars + f'<rect x="110" y="{250 if not inner else 150}" width="860" height="{720 if not inner else 960}" rx="6" fill="{C["pearl"]}" filter="url(#deckle)"/>'
    sil = '' if inner else mother(860, 1150, 0.55, C['night']) + child(960, 1160, 0.7, C['night'], flip=True)
    art = f'<rect width="1080" height="1350" fill="{g}"/>' + "".join(tops) + "".join(layers) + sil + moon + card
    txt = f'<div class="t" style="top:{320 if not inner else 210}px;right:170px;width:740px">{hook}</div>'
    return page(g, art, txt, "h1{font-size:80px} p{font-size:52px}")

def look2(ground, hook):
    # Cream Page: type-first; thin line motifs at the edges, one small paper cut-out.
    g = C[ground]
    art = (f'<rect width="1080" height="1350" fill="{g}"/>'
           f'<circle cx="60" cy="1250" r="190" fill="{C["tealMist"]}"/>'
           f'<circle cx="1050" cy="560" r="70" fill="{C["tealMist"]}"/>'
           f'<path d="M 860 40 C 980 60 1040 140 1050 260" stroke="{C["gold"]}" stroke-width="4" fill="none"/>'
           f'<path d="M 820 30 C 960 40 1060 120 1070 300" stroke="{C["gold"]}" stroke-width="2" fill="none" opacity="0.6"/>'
           f'<g filter="url(#shs)"><path d="M 140 1100 l 26 52 l 58 8 l -42 40 l 10 58 l -52 -27 l -52 27 l 10 -58 l -42 -40 l 58 -8 Z" fill="{C["gold"]}"/></g>')
    txt = f'<div class="t" style="top:170px;right:110px;width:860px">{hook}</div>'
    return page(g, art, txt, "h1{font-size:92px;color:%s} p{font-size:54px}" % C['tealDeep'])

DARK = ("night", "deep")
def mother(x, y, k, col, flip=False):
    # paper silhouette: hijab + abaya, side view, no features
    t = f'translate({x},{y}) scale({-k if flip else k},{k})'
    return (f'<g transform="{t}" filter="url(#shs)"><path d="M0,-300 c28,0 48,22 48,52 c0,22 -10,38 -22,46 '
            f'c40,14 66,60 74,120 l34,250 c4,30 -10,32 -40,32 l-190,0 c-30,0 -40,-4 -36,-32 l30,-250 '
            f'c8,-58 34,-104 70,-120 c-14,-8 -24,-24 -24,-46 c0,-30 20,-52 46,-52 Z" fill="{col}"/></g>')
def child(x, y, k, col, flip=False, arm=False):
    t = f'translate({x},{y}) scale({-k if flip else k},{k})'
    a = f'<path d="M18,-120 q40,-30 60,-70" stroke="{col}" stroke-width="20" stroke-linecap="round" fill="none"/>' if arm else ''
    return (f'<g transform="{t}" filter="url(#shs)"><circle cx="0" cy="-160" r="34" fill="{col}"/>'
            f'<path d="M-34,-118 q34,-14 68,0 l8,80 l-18,0 l0,38 l-16,0 l-4,-36 l-4,36 l-16,0 l0,-38 l-18,0 Z" fill="{col}"/>{a}</g>')
def stars(pts, col):
    return "".join(f'<path d="M {x} {y} l 6 14 l 15 2 l -11 10 l 3 15 l -13 -8 l -13 8 l 3 -15 l -11 -10 l 15 -2 Z" fill="{col}" opacity="0.8"/>' for x, y in pts)
DCSS = "h1{color:%s} p{color:%s} .hl{color:%s}" % ("#F6F3EB", "#F6F3EB", "#EBD6BC")

def look3(ground, hook):
    # Paper Vignette: big hook on top, a cut-paper stage set below with seated silhouettes (witnesses).
    g = C[ground]; dark = ground in DARK
    wallc = "#0B4D5E" if dark else C["pearl"]; floorc = C["night"] if ground == "deep" else (C["ink"] if dark else C["sand"])
    glow = '<circle cx="540" cy="900" r="420" fill="url(#glow)" opacity="0.55"/>' if dark else ''
    wall = f'<rect x="0" y="820" width="1080" height="250" fill="{wallc}" filter="url(#shs)"/>'
    stripes = "".join(f'<rect x="{x}" y="820" width="12" height="250" fill="{C["deep"] if dark else C["tealMist"]}" opacity="0.7"/>' for x in range(40, 1080, 90))
    floor = f'<rect x="0" y="1060" width="1080" height="290" fill="{floorc}" filter="url(#shs)"/>'
    cush = "".join(f'<rect x="{x}" y="1000" width="200" height="110" rx="26" fill="{c}" filter="url(#sh)"/>' for x, c in [(60, C['tealDeep']), (270, C['gold']), (480, C['tealDeep']), (690, C['gold'])])
    silc = C["night"] if dark else C["deep"]
    people = mother(170, 1030, 0.62, silc) + mother(390, 1030, 0.6, silc, flip=True) + mother(600, 1030, 0.64, silc)
    kid = child(860, 1060, 0.9, silc, arm=True)
    tray = f'<g filter="url(#sh)"><ellipse cx="900" cy="1190" rx="110" ry="30" fill="{C["gold"]}"/></g>'
    art = f'<rect width="1080" height="1350" fill="{g}"/>' + glow + wall + stripes + floor + cush + people + kid + tray
    txt = f'<div class="t" style="top:130px;right:100px;width:880px">{hook}</div>'
    return page(g, art, txt, "h1{font-size:96px} p{font-size:56px}" + (DCSS if dark else ""))

def look4(ground, hook):
    # Doorway / window light: a warm light cone falls across the ground; a child silhouette stands in it.
    g = C[ground]; dark = ground in DARK
    if dark:
        beam = f'<polygon points="1080,760 1080,1120 300,1350 820,1350" fill="#F3C98B" opacity="0.28"/><polygon points="1080,800 1080,1080 450,1350 680,1350" fill="#F3C98B" opacity="0.25"/>'
        door = f'<rect x="1010" y="740" width="70" height="400" fill="#F3C98B" opacity="0.9" filter="url(#shs)"/>'
        art = f'<rect width="1080" height="1350" fill="{g}"/>' + beam + door + mother(250, 1300, 0.9, C["night"] if ground=="deep" else C["ink"]) + child(560, 1290, 1.15, C["night"] if ground=="deep" else C["ink"], flip=True)
    else:
        beams = "".join(f'<polygon points="{1080-dx},0 {1080-dx-150},0 {300-dx},1350 {450-dx},1350" fill="#FFF6E6" opacity="0.38"/>' for dx in (0, 230, 460))
        art = f'<rect width="1080" height="1350" fill="{g}"/>' + beams + child(560, 1290, 1.15, C["deep"], flip=True)
    txt = f'<div class="t" style="top:150px;right:110px;width:860px">{hook}</div>'
    return page(g, art, txt, "h1{font-size:90px} p{font-size:54px}" + (DCSS if dark else ""))

def look5(ground, hook):
    # Night Bubble: one big pearl paper speech bubble holds the copy; two small silhouettes talking below.
    g = C[ground]; dark = ground in DARK
    bubble = (f'<g filter="url(#deckle)"><rect x="110" y="200" width="860" height="720" rx="90" fill="{C["pearl"]}"/>'
              f'<path d="M 640 900 L 560 1060 L 760 905 Z" fill="{C["pearl"]}"/></g>')
    silc = C["ink"] if dark else C["deep"]
    people = mother(470, 1320, 0.75, silc) + mother(720, 1320, 0.75, silc, flip=True)
    art = (f'<rect width="1080" height="1350" fill="{g}"/>' + stars([(120, 120), (960, 90), (880, 1080), (170, 1060)], C["sand"])
           + '<circle cx="980" cy="1200" r="260" fill="url(#glow)" opacity="0.5"/>' + bubble + people)
    txt = f'<div class="t" style="top:280px;right:180px;width:720px;text-align:center">{hook}</div>'
    return page(g, art, txt, "h1{font-size:84px} p{font-size:52px}")

LOOKS = {1: look1, 2: look2, 3: look3, 4: look4, 5: look5}
if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    for name, c in cfg.items():
        fn = LOOKS[c["look"]]
        html = fn(c["ground"], c["hook"], c.get("inner", False)) if c["look"] == 1 else fn(c["ground"], c["hook"])
        open(f"out/{name}.html", "w").write(html)
