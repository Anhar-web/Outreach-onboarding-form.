"""Batch 4 visual system mocks: 5 looks rendered with SVG/CSS (no photos, no AI images).
Copy on the mocks is from Anhar's legacy posts, for layout only."""
import json, sys
C = dict(deep="#005A70", night="#003F4F", ink="#0E2F38", teal="#00A9A5", tealDeep="#007A77",
         tealMist="#DCEEEC", pearl="#F6F3EB", sand="#EBD6BC", gold="#C9935A", goldDeep="#8A5A2B",
         dusk="#B7CBD6", duskDeep="#7F9DB0")
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
    art = f'<rect width="1080" height="1350" fill="{g}"/>' + "".join(tops) + "".join(layers) + moon + card
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

def look3(ground, hook):
    # Paper Vignette: big hook on top, a small cut-paper scene in the lower 40%.
    g = C[ground]
    floor = f'<rect x="0" y="1060" width="1080" height="290" fill="{C["sand"]}" filter="url(#shs)"/>'
    wall = f'<rect x="0" y="820" width="1080" height="250" fill="{C["pearl"]}" filter="url(#shs)"/>'
    stripes = "".join(f'<rect x="{x}" y="820" width="14" height="250" fill="{C["tealMist"]}"/>' for x in range(40, 1080, 90))
    cushions = "".join(f'<rect x="{x}" y="1000" width="200" height="110" rx="26" fill="{c}" filter="url(#sh)"/>' for x, c in [(60, C['deep']), (270, C['tealDeep']), (480, C['deep']), (690, C['tealDeep'])])
    dallah = (f'<g filter="url(#sh)"><ellipse cx="930" cy="1180" rx="120" ry="34" fill="{C["gold"]}"/>' + "".join(f'<path d="M {x} 1170 l 36 0 l -7 -40 l -22 0 Z" fill="{C["pearl"]}"/>' for x in (860, 912, 964)) + '</g>')
    cups = ''
    art = f'<rect width="1080" height="1350" fill="{g}"/>' + wall + stripes + floor + cushions + dallah + cups
    txt = f'<div class="t" style="top:130px;right:100px;width:880px">{hook}</div>'
    return page(g, art, txt, "h1{font-size:96px} p{font-size:56px}")

def look4(ground, hook):
    # Warm Window Light: golden-hour window panes cast across the ground; one paper object.
    g = C[ground]
    beams = "".join(f'<polygon points="{1080-dx},0 {1080-dx-150},0 {300-dx},1350 {450-dx},1350" fill="#FFF6E6" opacity="0.38"/>' for dx in (0, 230, 460))
    bag = (f'<g filter="url(#sh)"><rect x="110" y="1020" width="250" height="230" rx="40" fill="{C["deep"]}"/>'
           f'<rect x="150" y="1080" width="170" height="90" rx="20" fill="{C["tealDeep"]}"/>'
           f'<path d="M 160 1025 q 75 -110 150 0" stroke="{C["deep"]}" stroke-width="22" fill="none"/></g>')
    clock = (f'<g filter="url(#sh)"><circle cx="900" cy="1200" r="95" fill="{C["pearl"]}"/>'
             f'<path d="M 900 1200 L 900 1130" stroke="{C["ink"]}" stroke-width="12" stroke-linecap="round"/>'
             f'<path d="M 900 1200 L 940 1175" stroke="{C["gold"]}" stroke-width="12" stroke-linecap="round"/></g>')
    art = f'<rect width="1080" height="1350" fill="{g}"/>' + beams + bag + clock
    txt = f'<div class="t" style="top:150px;right:110px;width:860px">{hook}</div>'
    return page(g, art, txt, "h1{font-size:90px} p{font-size:54px}")

def look5(ground, hook):
    # Blue Hour Minimal: one big 3D paper object holds the copy (speech bubble).
    g = C[ground]
    bubble = (f'<g filter="url(#deckle)"><rect x="110" y="250" width="860" height="760" rx="90" fill="{C["pearl"]}"/>'
              f'<path d="M 700 990 L 800 1150 L 820 990 Z" fill="{C["pearl"]}"/></g>')
    heart = f'<path d="M 860 930 c -20 -30 -70 -10 -50 30 l 50 40 l 50 -40 c 20 -40 -30 -60 -50 -30 Z" fill="{C["sand"]}" filter="url(#shs)"/>'
    art = f'<rect width="1080" height="1350" fill="{g}"/>' + f'<circle cx="980" cy="120" r="180" fill="{C["duskDeep"]}" opacity="0.35"/>' + bubble + heart
    txt = f'<div class="t" style="top:330px;right:180px;width:720px;text-align:center">{hook}</div>'
    return page(g, art, txt, "h1{font-size:84px} p{font-size:52px}")

LOOKS = {1: look1, 2: look2, 3: look3, 4: look4, 5: look5}
if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    for name, c in cfg.items():
        fn = LOOKS[c["look"]]
        html = fn(c["ground"], c["hook"], c.get("inner", False)) if c["look"] == 1 else fn(c["ground"], c["hook"])
        open(f"out/{name}.html", "w").write(html)
