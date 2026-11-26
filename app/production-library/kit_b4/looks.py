"""Batch 4 "Paper & Light" looks (VISUAL_STYLE_B4_1.md).

One idea: a sheet of paper carries the words; the world is cut paper around it,
lit by one warm light. Five looks share fonts, grain, deckled pearl paper and the
warm light; they differ in ground, depth and amount of art. Art FRAMES the copy
and never sits behind a letter.

    1 Layered Paper Night  night/deep   wave layers + moon/lantern + stars, copy on a deckled pearl card
    2 Cream Page           pearl/sand/tealMist   type-first, gold line arcs, one tealMist circle, one small object
    3 Paper Vignette       deep/night   big pearl hook top, a cut-paper stage set with silhouettes at the bottom
    4 Doorway Light        night/deep   a warm light cone from a doorway, mother + child silhouettes in it
    5 Night Bubble         deep/night   one big deckled pearl speech bubble holds the copy, silhouettes below

A post module is a CONF dict; make(ctx, CONF) builds every slide.
Slide text is never typed here: segments come from build.py (verbatim).
"""
import base64
import math
import os
import random

from kit import C, W, H, MX, MT, paper, torn_rect, torn_poly, torn_circle, avoid, seg_html, P

HERE = os.path.dirname(os.path.abspath(__file__))
QR_DIR = os.path.abspath(os.path.join(HERE, '..', '..', 'b4', 'qr'))
C = dict(C)
C['sand'] = C['sandLight']
DARK = {'deep', 'night'}
_gid = [0]


def uid(p='g'):
    _gid[0] += 1
    return f'{p}{_gid[0]}'


# --------------------------------------------------------------------------- light
def glow(cx, cy, r, op=.55, color=None):
    color = color or C['gold']
    g = uid('gl')
    return (f'<defs><radialGradient id="{g}"><stop offset="0" stop-color="{color}" stop-opacity="{op}"/>'
            f'<stop offset=".4" stop-color="{color}" stop-opacity="{op * .38:.3f}"/>'
            f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient></defs>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{g})"/>')


def star(cx, cy, r, tone, fill=None, rot=0, layer=1):
    pts = []
    for k in range(10):
        a = math.radians(rot - 90 + k * 36)
        rr = r if k % 2 == 0 else r * .45
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return paper(f'<polygon points="{P(pts)}" fill="{fill or C["sand"]}"/>', tone, layer)


def stars(spots, tone, seed=3):
    rng = random.Random(seed)
    return ''.join(star(x, y, r, tone, rot=rng.uniform(-20, 20)) for x, y, r in spots)


def moon(cx, cy, r, tone):
    return (glow(cx, cy, r * 3.2, .5) +
            torn_circle(cx, cy, r, C['sand'], tone, seed=41, layer=2,
                        inner=f'<circle cx="{cx + r * .35}" cy="{cy - r * .2}" r="{r * .82}" fill="{C["pearl"]}" fill-opacity=".35"/>'))


def lantern(cx, cy, s, tone):
    body = (f'<path d="M {cx - s * .32} {cy - s * .55} H {cx + s * .32} L {cx + s * .4} {cy + s * .45} H {cx - s * .4} Z" fill="{C["gold"]}"/>'
            f'<rect x="{cx - s * .2}" y="{cy - s * .38}" width="{s * .4}" height="{s * .66}" rx="{s * .08}" fill="{C["sand"]}"/>'
            f'<path d="M {cx - s * .42} {cy - s * .55} Q {cx} {cy - s * .9} {cx + s * .42} {cy - s * .55} Z" fill="{C["goldDeep"]}"/>'
            f'<rect x="{cx - s * .46}" y="{cy + s * .42}" width="{s * .92}" height="{s * .1}" fill="{C["goldDeep"]}"/>'
            f'<path d="M {cx} {cy - s * .9} V {cy - s * 1.3}" stroke="{C["goldDeep"]}" stroke-width="{s * .05}"/>')
    return glow(cx, cy, s * 2.4, .55) + paper(body, tone, 2)


# --------------------------------------------------------------------------- paper layers
def wave_layer(base, amp, ph, fill, tone, seed, k=1.0, top=False, layer=1):
    """A torn paper wave. bottom layer: area below the wave; top=True: area above it."""
    xs = [-40 + i * 40 for i in range(30)]
    edge = [(x, base + amp * math.sin(x / 1080 * math.pi * 2 * k + ph) + amp * .35 * math.sin(x / 1080 * math.pi * 5 * k + ph * 1.7))
            for x in xs]
    if top:
        verts = [(1120, -40), (-40, -40)] + edge
        torn = list(range(2, len(verts)))
    else:
        verts = edge + [(1120, H + 40), (-40, H + 40)]
        torn = list(range(0, len(edge) - 1))
    return torn_poly(verts, fill, tone, torn=torn, seed=seed, layer=layer, amp=(4, 9))


def waves(ground, y0, n=4, amp=34, seed=7):
    """4-5 stacked layers rising from the bottom: back (darker) -> tealDeep -> sand -> pearl."""
    tone = 'd'
    back = 'deep' if ground == 'night' else 'night'
    cols = [C[back], C['tealDeep'], C['sand'], C['pearl']][-n:] if n < 4 else [C[back], C['tealDeep'], C['sand'], C['pearl']]
    out = ''
    for i, col in enumerate(cols):
        out += wave_layer(y0 + i * 62, amp - i * 4, 1.1 * i + seed * .3, col, tone, seed + i, k=1 + i * .15, layer=min(3, 1 + i))
    return avoid(out, 'waves')


def sky_layer(ground, y, seed=11):
    col = C['ink'] if ground == 'night' else C['night']
    return wave_layer(y, 26, 2.2, col, 'd', seed, k=.8, top=True)


def arcs(cx, cy, rs, a0, a1, color=None, w=5):
    color = color or C['gold']
    out = ''
    for r in rs:
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        out += f'<path d="M {x0:.0f} {y0:.0f} A {r} {r} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>'
    return paper(out, 'l', 1)


# --------------------------------------------------------------------------- people (flat paper silhouettes, no faces)
def mother(cx, foot, h, col, tone, facing=1, reach=None, bend=0):
    """Mother in hijab + abaya, side/back view: a round covered head flowing into
    rounded shoulders and a long A-line abaya. facing 1 = toward the right.
    reach=(x,y): her arm reaches to that point (a child's hand)."""
    f = facing
    r = h * .085
    hx = cx + f * h * .025 + f * bend
    hy = foot - h + r * 1.05
    sh = hy + r * 2.0
    body = (f'M {hx - r * .95} {hy + r * .35} Q {hx - r * 1.05} {sh - r * .55} {cx - h * .15} {sh} '
            f'Q {cx - h * .19} {sh + h * .25} {cx - h * .22} {foot} L {cx + h * .21} {foot} '
            f'Q {cx + h * .18} {sh + h * .25} {cx + h * .14} {sh} Q {hx + r * 1.05} {sh - r * .55} {hx + r * .95} {hy + r * .35} Z')
    out = f'<path d="{body}" fill="{col}"/><circle cx="{hx}" cy="{hy}" r="{r * 1.08}" fill="{col}"/>'
    if reach:
        rx, ry = reach
        out += (f'<path d="M {cx + f * h * .07} {sh + r * .6} Q {cx + f * h * .12} {(sh + ry) / 2 + h * .07} {rx} {ry}" '
                f'fill="none" stroke="{col}" stroke-width="{h * .055:.0f}" stroke-linecap="round"/>')
    return paper(out, tone, 2)


def child(cx, foot, h, col, tone, facing=1, arm_up=True):
    f = facing
    hr = h * .17
    hy = foot - h + hr
    by0, by1 = hy + hr * .9, foot - h * .3
    out = (f'<circle cx="{cx}" cy="{hy}" r="{hr}" fill="{col}"/>'
           f'<rect x="{cx - h * .17}" y="{by0}" width="{h * .34}" height="{by1 - by0}" rx="{h * .1}" fill="{col}"/>'
           f'<rect x="{cx - h * .14}" y="{by1 - 4}" width="{h * .11}" height="{foot - by1 + 4}" rx="{h * .04}" fill="{col}"/>'
           f'<rect x="{cx + h * .03}" y="{by1 - 4}" width="{h * .11}" height="{foot - by1 + 4}" rx="{h * .04}" fill="{col}"/>')
    if arm_up:
        out += (f'<path d="M {cx + f * h * .12} {by0 + h * .08} Q {cx + f * h * .3} {by0} {cx + f * h * .34} {by0 - h * .16}" '
                f'fill="none" stroke="{col}" stroke-width="{h * .09:.0f}" stroke-linecap="round"/>')
    return paper(out, tone, 2)


def child_hand(cx, foot, h, facing=1):
    hr = h * .17
    by0 = foot - h + hr * 1.9
    return (cx + facing * h * .34, by0 - h * .16)


def seated(cx, base, s, col, tone):
    """A seated woman from behind (hijab + abaya on a floor cushion)."""
    hr = s * .11
    hy = base - s * .9
    sy = hy + hr * 1.5
    out = (f'<circle cx="{cx}" cy="{hy}" r="{hr * 1.12}" fill="{col}"/>'
           f'<path d="M {cx - hr * 1.12} {hy + hr * .1} Q {cx - hr * 1.2} {sy} {cx - s * .2} {sy + s * .08} '
           f'Q {cx - s * .34} {sy + s * .2} {cx - s * .38} {base} L {cx + s * .38} {base} '
           f'Q {cx + s * .34} {sy + s * .2} {cx + s * .2} {sy + s * .08} Q {cx + hr * 1.2} {sy} {cx + hr * 1.12} {hy + hr * .1} Z" fill="{col}"/>')
    return paper(out, tone, 2)


def standing_man(cx, foot, h, col, tone):
    hr = h * .07
    hy = foot - h + hr * 1.2
    out = (f'<path d="M {cx - hr * 1.3} {hy + hr * .2} Q {cx} {hy - hr * 2.1} {cx + hr * 1.3} {hy + hr * .2} '
           f'L {cx + h * .13} {hy + h * .2} L {cx - h * .13} {hy + h * .2} Z" fill="{col}"/>'
           f'<path d="M {cx - h * .13} {hy + h * .12} L {cx + h * .13} {hy + h * .12} L {cx + h * .15} {foot} L {cx - h * .15} {foot} Z" fill="{col}"/>')
    return paper(out, tone, 2)


# --------------------------------------------------------------------------- objects
def car(cx, cy, s, tone, body=None):
    body = body or C['tealDeep']
    out = (f'<path d="M {cx - s} {cy} Q {cx - s} {cy - s * .32} {cx - s * .7} {cy - s * .36} L {cx - s * .42} {cy - s * .72} '
           f'L {cx + s * .38} {cy - s * .72} L {cx + s * .7} {cy - s * .36} Q {cx + s} {cy - s * .3} {cx + s} {cy} Z" fill="{body}"/>'
           f'<path d="M {cx - s * .34} {cy - s * .62} L {cx - s * .04} {cy - s * .62} L {cx - s * .04} {cy - s * .38} L {cx - s * .56} {cy - s * .38} Z" fill="{C["tealMist"]}"/>'
           f'<path d="M {cx + s * .04} {cy - s * .62} L {cx + s * .32} {cy - s * .62} L {cx + s * .54} {cy - s * .38} L {cx + s * .04} {cy - s * .38} Z" fill="{C["tealMist"]}"/>')
    wheels = (f'<circle cx="{cx - s * .55}" cy="{cy}" r="{s * .2}" fill="{C["ink"]}"/>'
              f'<circle cx="{cx + s * .55}" cy="{cy}" r="{s * .2}" fill="{C["ink"]}"/>')
    return paper(out, tone, 2) + paper(wheels, tone, 3)


def lift_panel(cx, cy, s, tone):
    plate = f'<rect x="{cx - s * .5}" y="{cy - s}" width="{s}" height="{s * 2}" rx="{s * .12}" fill="{C["tealDeep"]}"/>'
    btn = (f'<circle cx="{cx}" cy="{cy - s * .45}" r="{s * .3}" fill="{C["gold"]}"/>'
           f'<circle cx="{cx}" cy="{cy + s * .45}" r="{s * .3}" fill="{C["pearl"]}"/>'
           f'<path d="M {cx - s * .12} {cy - s * .38} L {cx} {cy - s * .56} L {cx + s * .12} {cy - s * .38} Z" fill="{C["ink"]}"/>'
           f'<path d="M {cx - s * .12} {cy + s * .38} L {cx} {cy + s * .56} L {cx + s * .12} {cy + s * .38} Z" fill="{C["ink"]}"/>')
    return paper(plate, tone, 2) + paper(btn, tone, 3)


def rice_plate(cx, cy, s, tone):
    plate = (f'<ellipse cx="{cx}" cy="{cy}" rx="{s}" ry="{s * .42}" fill="{C["pearl"]}"/>'
             f'<ellipse cx="{cx}" cy="{cy}" rx="{s * .78}" ry="{s * .32}" fill="{C["tealMist"]}"/>')
    rice = f'<path d="M {cx - s * .55} {cy + s * .05} Q {cx - s * .1} {cy - s * .62} {cx + s * .5} {cy + s * .02} Z" fill="{C["pearl"]}"/>'
    grains = ''.join(f'<ellipse cx="{cx + dx * s}" cy="{cy + dy * s}" rx="{s * .045}" ry="{s * .02}" fill="{C["sand"]}"/>'
                     for dx, dy in [(-.3, -.08), (-.12, -.22), (.1, -.15), (.25, -.05), (-.02, -.05), (.05, -.3)])
    return paper(plate, tone, 2) + paper(rice + grains, tone, 3)


def tray(cx, cy, s, tone, n=5):
    out = (f'<ellipse cx="{cx}" cy="{cy}" rx="{s}" ry="{s * .3}" fill="{C["gold"]}"/>'
           f'<ellipse cx="{cx}" cy="{cy - 4}" rx="{s * .86}" ry="{s * .24}" fill="{C["goldDeep"]}" fill-opacity=".35"/>')
    sweets = ''
    cols = [C['pearl'], C['tealMist'], C['sand'], C['teal'], C['pearl'], C['sand']]
    for k in range(n):
        x = cx - s * .6 + k * (s * 1.2 / max(1, n - 1))
        y = cy - s * .08 + (k % 2) * s * .06
        sweets += f'<rect x="{x - s * .1}" y="{y - s * .1}" width="{s * .2}" height="{s * .14}" rx="{s * .05}" fill="{cols[k % 6]}"/>'
    return paper(out, tone, 2) + paper(sweets, tone, 3)


def dallah(cx, base, s, tone):
    out = (f'<path d="M {cx - s * .3} {base} L {cx + s * .3} {base} L {cx + s * .2} {base - s * .5} Q {cx} {base - s * .62} {cx - s * .2} {base - s * .5} Z" fill="{C["gold"]}"/>'
           f'<path d="M {cx - s * .14} {base - s * .58} L {cx + s * .14} {base - s * .58} L {cx + s * .08} {base - s * .85} L {cx - s * .08} {base - s * .85} Z" fill="{C["gold"]}"/>'
           f'<path d="M {cx - s * .2} {base - s * .5} Q {cx - s * .62} {base - s * .62} {cx - s * .66} {base - s * .95}" fill="none" stroke="{C["gold"]}" stroke-width="{s * .08}" stroke-linecap="round"/>'
           f'<circle cx="{cx}" cy="{base - s * .92}" r="{s * .07}" fill="{C["goldDeep"]}"/>')
    return paper(out, tone, 2)


def gift_bag(cx, base, s, tone):
    out = (f'<rect x="{cx - s * .4}" y="{base - s}" width="{s * .8}" height="{s}" fill="{C["sand"]}"/>'
           f'<path d="M {cx - s * .2} {base - s} Q {cx} {base - s * 1.4} {cx + s * .2} {base - s}" fill="none" stroke="{C["goldDeep"]}" stroke-width="{s * .06}"/>'
           f'<rect x="{cx - s * .4}" y="{base - s * .55}" width="{s * .8}" height="{s * .1}" fill="{C["gold"]}"/>')
    return paper(out, tone, 3)


def toy_car(cx, cy, s, tone):
    return car(cx, cy, s, tone, body=C['gold'])


def blocks(x, base, s, tone):
    cols = [C['teal'], C['sand'], C['pearl'], C['gold']]
    out = ''
    for k, (dx, dy) in enumerate([(0, 0), (s * 1.05, 0), (s * .5, -s), (s * 2.3, 0)]):
        out += f'<rect x="{x + dx}" y="{base - s + dy}" width="{s}" height="{s}" rx="{s * .08}" fill="{cols[k]}"/>'
    return paper(out, tone, 2)


def shoe_row(x0, y, n, s, tone):
    out = ''
    cols = [C['sand'], C['tealDeep'], C['pearl'], C['gold'], C['teal'], C['sand'], C['goldDeep']]
    for k in range(n):
        x = x0 + k * s * 1.25
        c = cols[k % len(cols)]
        for d in (0, s * .44):
            out += (f'<path d="M {x + d} {y} L {x + d} {y - s * .5} Q {x + d + s * .2} {y - s * .62} {x + d + s * .3} {y - s * .4} '
                    f'L {x + d + s * .38} {y} Z" fill="{c}"/>')
    return paper(out, tone, 2)


def doorway(x, y, w, h, tone, light=True, frame=None):
    frame = frame or C['goldDeep']
    out = ''
    if light:
        out += glow(x + w / 2, y + h * .55, max(w, h) * .85, .55)
    out += torn_rect(x, y, w, h, C['gold'] if light else C['night'], tone, sides='', seed=61, layer=1,
                     inner=f'<rect x="{x + w * .1:.0f}" y="{y + h * .06:.0f}" width="{w * .8:.0f}" height="{h * .94:.0f}" fill="{C["sand"]}" fill-opacity=".5"/>' if light else '')
    out += paper(f'<path d="M {x - 16} {y + h} V {y - 16} H {x + w + 16} V {y + h}" fill="none" stroke="{frame}" stroke-width="22"/>', tone, 3)
    return out


def light_cone(x_door, y_top, y_bot, spread, side='r'):
    """Warm light falling from a doorway at the edge across the dark floor."""
    if side == 'r':
        pts = [(x_door, y_top), (W + 20, y_top), (W + 20, H + 20), (x_door - spread, H + 20)]
    else:
        pts = [(-20, y_top), (x_door, y_top), (x_door + spread, H + 20), (-20, H + 20)]
    return f'<polygon points="{P(pts)}" fill="{C["gold"]}" fill-opacity=".30"/>'


def floor(y, col, tone, seed=5):
    return torn_rect(-30, y, W + 60, H - y + 40, col, tone, sides='t', seed=seed, layer=1)


def cushions(y, col, tone, n=4, x0=60, w=240):
    out = ''
    for k in range(n):
        out += f'<rect x="{x0 + k * (w + 14)}" y="{y}" width="{w}" height="{70}" rx="22" fill="{col}"/>'
    return paper(out, tone, 1)


def shelf(y, tone):
    out = f'<rect x="-20" y="{y}" width="{W + 40}" height="28" fill="{C["goldDeep"]}"/>'
    boxes = ''
    cols = [C['teal'], C['sand'], C['gold'], C['pearl'], C['tealDeep'], C['sand'], C['teal']]
    x = 30
    rng = random.Random(4)
    k = 0
    while x < W:
        bw, bh = rng.randint(90, 150), rng.randint(110, 200)
        boxes += f'<rect x="{x}" y="{y - bh}" width="{bw}" height="{bh}" rx="6" fill="{cols[k % 7]}"/>'
        x += bw + 14
        k += 1
    return paper(boxes, tone, 2) + paper(out, tone, 1)


# --------------------------------------------------------------------------- text
import re as _re
_Q = _re.compile(r'"[^"]{1,14}"')


def autokeep(segs):
    for s in segs:
        for m in _Q.finditer(s.text):
            if m.group(0) not in s.keep:
                s.keep.append(m.group(0))
        for p in ('ما شاء الله', 'السلام عليكم', 'الله يعطيكي العافية'):
            if p in s.text and p not in s.keep and not any(p in k for k in s.keep):
                s.keep.append(p)


def segs_html(segs, look, tool_fill):
    """Body flow. A «الافتراض…:» / «الخطوة …:» label becomes a gold paper tag; a short
    'جربي …' line naming the tool gets a small paper tag (gold on look 1, tealMist else)."""
    out = ''
    autokeep(segs)
    for s in segs:
        if s.role == 'label':
            out += f'<div class="ltag torn" data-fill="{C["gold"]}" data-seed="5" data-sides="lr">{seg_html(s, "label", "span")}</div>'
        elif s.role in ('lead', 'support') and s.text.startswith('جربي') and len(s.text) <= 60:
            out += f'<div class="tooltag torn" data-fill="{tool_fill}" data-seed="8" data-sides="lr">{seg_html(s, "tool", "div")}</div>'
        else:
            out += seg_html(s)
    return out


def box(segs, x, y, w, color, look, tool_fill=None, cls='', size=None, style='', maxh=None, minfs=50):
    inner = segs_html(segs, look, tool_fill or C['tealMist'])
    sz = f'--fs:{size}px;' if size else ''
    mh = f' data-maxh="{maxh}" data-minfs="{minfs}"' if maxh else ''
    return (f'<div class="tx c-{color} {cls}"{mh} style="left:{x}px;top:{y}px;width:{w}px;{sz}{style}">{inner}</div>')


def card(segs, x, y, w, look, tool_fill=None, cls='', size=None, pad=56, kind='card', seed=21, maxh=None, minfs=50, shape='', tail='l'):
    """Opaque deckled pearl paper card (never translucent) holding ink text."""
    inner = segs_html(segs, look, tool_fill or C['tealMist'])
    sz = f'--fs:{size}px;' if size else ''
    mh = f' data-maxh="{maxh}" data-minfs="{minfs}"' if maxh else ''
    sh = f' data-shape="{shape}" data-tail="{tail}"' if shape else ''
    return (f'<div class="tx c-ink {kind} torn {cls}"{mh}{sh} data-fill="{C["pearl"]}" data-seed="{seed}" data-sides="tblr" '
            f'style="left:{x}px;top:{y}px;width:{w}px;padding:{pad}px {pad}px {pad + 6}px;{sz}">{inner}</div>')


def est_lines(text, px, width, face='body'):
    k = .56 if face == 'hook' else .47
    cpl = max(8, int(width / (px * k)))
    return max(1, math.ceil(len(text) / cpl))


def fit_hook(ctx, width, budget, lo=72, hi=96):
    """Pick the hook size so slide 1 fits its budget; demote trailing lines to the
    Tajawal clause style if even 80px is too tall. Returns (segs, size)."""
    segs = ctx.t.body()
    for px in range(hi, lo - 1, -4):
        hgt = sum(est_lines(s.text, px, width, 'hook') for s in segs) * px * 1.32
        if hgt <= budget:
            return segs, px
    px = lo
    k = len(segs)
    while k > 1:
        k -= 1
        for s in segs[k:]:
            s.role = 'clause'
        hgt = (sum(est_lines(s.text, px, width, 'hook') for s in segs[:k]) * px * 1.32 +
               sum(est_lines(s.text, 58, width) for s in segs[k:]) * 58 * 1.5 + 20)
        if hgt <= budget:
            break
    return segs, px


def body_size(ctx, width, budget):
    segs = ctx.t.body()
    for px in (72, 68, 66, 62, 60, 58, 56, 54, 52, 50):
        hgt = sum(est_lines(s.text, px, width) for s in segs) * px * 1.5 + 18 * len(segs) + (95 if ctx.t.label() else 0)
        if hgt <= budget:
            return px
    return 50


def qr_card(post_id, x, y, s=290, tone='d', extra_segs=None, look=1):
    data = base64.b64encode(open(os.path.join(QR_DIR, f'{post_id}.png'), 'rb').read()).decode()
    pad = 26
    hh = s + pad * 2
    svg = torn_rect(x, y, s + pad * 2, hh, C['pearl'], tone, sides='tblr', seed=77, layer=3,
                    inner=f'<image x="{x + pad}" y="{y + pad}" width="{s}" height="{s}" href="data:image/png;base64,{data}"/>')
    return avoid(svg, 'qr'), hh


# --------------------------------------------------------------------------- the looks
def text_col(ground):
    return 'pearl' if ground in DARK else 'ink'


def allsegs(ctx):
    return [s for s in ctx.t.segs if s.role != 'soft']


def make(ctx, K):
    look, g = K['look'], K['ground']
    tone = 'd' if g in DARK else 'l'
    first, last = ctx.first, ctx.last
    tool_fill = C['gold'] if look == 1 else C['tealMist']
    art, html = '', ''

    # ---------------------------------------------------------------- LOOK 1: layered paper night
    if look == 1:
        if first:
            art += sky_layer(g, 150)
            art += moon(K.get('moon_x', 860), 250, 58, tone) if K.get('light', 'moon') == 'moon' else lantern(K.get('moon_x', 860), 270, 90, tone)
            art += stars([(130, 120, 16), (300, 210, 11), (560, 140, 13), (980, 420, 10)], tone)
            art += waves(g, 1080)
            art += glow(860, 1010, 300, .45)
            art += avoid(K['figs'](g, tone), 'people')
            segs, px = fit_hook(ctx, 708, 760)
            html += card(segs, 130, 140, 820, 1, cls='hookcard', size=96, seed=31, maxh=K.get('hook_maxh', 640), minfs=72)
        elif last:
            art += waves(g, 1210, n=2)
            art += star(140, 140, 14, tone) + star(960, 230, 10, tone)
            art += moon(940, 1110, 34, tone) if K.get('light', 'moon') == 'moon' else lantern(950, 1120, 60, tone)
            q, qh = qr_card(ctx.post_id, 110, 900, tone=tone)
            art += q
            html += card(allsegs(ctx), 110, 110, 860, 1, size=72, seed=33, cls='endcard', maxh=770)
        else:
            art += waves(g, 1170 + (ctx.i % 2) * 30, n=2, seed=7 + ctx.i)
            art += stars([(120 + 40 * (ctx.i % 3), 110, 13), (980, 160 + 30 * (ctx.i % 2), 10)], tone, seed=ctx.i)
            art += glow(1000 if ctx.i % 2 else 80, 1180, 220, .3)
            px = body_size(ctx, 748, 900)
            html += card(allsegs(ctx), 110, 130, 860, 1, tool_fill=tool_fill, size=72, seed=40 + ctx.i, maxh=1010)

    # ---------------------------------------------------------------- LOOK 2: cream page (the one light look)
    elif look == 2:
        corner = K.get('corner', 'bl')
        obj = K['object']
        if first:
            art += arcs(1080, 1350, [170, 215, 260], 180, 270)
            art += torn_circle(-40, 1180, 230, C['tealMist'] if g != 'tealMist' else C['pearl'], 'l', seed=12, layer=1)
            art += avoid(obj(250, 1110, 1.0, 'l'), 'object')
            segs, px = fit_hook(ctx, 888, 820)
            html += box(segs, MX, 140, 888, 'deep' if g == 'sandLight' else 'tealDeep', 2, size=96, cls='hookplain', maxh=K.get('hook_maxh', 820), minfs=72)
        elif last:
            art += arcs(0, 1350, [150, 190], 270, 360)
            art += avoid(obj(860, 1180, .55, 'l'), 'object')
            q, qh = qr_card(ctx.post_id, 96, 900, tone='l')
            art += q
            html += box(allsegs(ctx), MX, 120, 888, 'ink', 2, size=72, maxh=760)
        else:
            k = ctx.i
            if k % 2:
                art += arcs(0, 0, [140, 180], 0, 90)
                art += torn_circle(1120, 1300, 170, C['tealMist'] if g != 'tealMist' else C['pearl'], 'l', seed=13 + k, layer=1)
            else:
                art += arcs(1080, 1350, [140, 180], 180, 270)
                art += torn_circle(-30, 140, 120, C['tealMist'] if g != 'tealMist' else C['pearl'], 'l', seed=13 + k, layer=1)
            px = body_size(ctx, 888, 980)
            html += box(allsegs(ctx), MX, 130, 888, 'ink', 2, tool_fill=C['tealMist'] if g != 'tealMist' else C['pearl'], size=72, maxh=1050)

    # ---------------------------------------------------------------- LOOK 3: paper vignette
    elif look == 3:
        scene = K['scene']
        if first:
            art += scene(g, tone, full=True)
            segs, px = fit_hook(ctx, 888, 860)
            html += box(segs, MX, 120, 888, 'pearl', 3, size=96, cls='hookplain', maxh=K.get('hook_maxh', 660), minfs=72)
        elif last:
            art += K['prop'](g, tone, 'corner_r')
            q, qh = qr_card(ctx.post_id, 96, 900, tone=tone)
            art += q
            html += box(allsegs(ctx), MX, 120, 888, 'pearl', 3, size=72, maxh=760)
        else:
            art += K['prop'](g, tone, 'corner_l' if ctx.i % 2 else 'corner_r')
            px = body_size(ctx, 888, 900)
            html += box(allsegs(ctx), MX, 130, 888, 'pearl', 3, tool_fill=C['tealMist'], size=72, maxh=980)

    # ---------------------------------------------------------------- LOOK 4: doorway light
    elif look == 4:
        if first:
            art += doorway(70, 680, 210, 520, tone)
            art += floor(1200, C['ink'] if g == 'night' else C['night'], tone)
            art += f'<polygon points="70,1200 280,1200 1100,1370 -20,1370" fill="{C["gold"]}" fill-opacity=".32"/>'
            art += stars([(980, 760, 12), (860, 700, 9)], tone)
            art += avoid(K['figs'](g, tone), 'people')
            segs, px = fit_hook(ctx, 860, 720)
            html += box(segs, MX, 120, 888, 'pearl', 4, size=96, cls='hookplain', maxh=K.get('hook_maxh', 520), minfs=72)
        elif last:
            art += doorway(960, 1040, 130, 330, tone) + light_cone(960, 1350, 1350, 300)
            q, qh = qr_card(ctx.post_id, 96, 900, tone=tone)
            art += q
            html += box(allsegs(ctx), MX, 120, 888, 'pearl', 4, size=72, maxh=760)
        else:
            side = 'r' if ctx.i % 2 else 'l'
            if side == 'r':
                art += f'<polygon points="1080,0 1080,1350 860,1350 1000,0" fill="{C["gold"]}" fill-opacity=".16"/>'
            else:
                art += f'<polygon points="0,0 80,0 220,1350 0,1350" fill="{C["gold"]}" fill-opacity=".16"/>'
            art += star(150 if side == 'r' else 930, 1200, 12, tone)
            px = body_size(ctx, 888, 980)
            html += box(allsegs(ctx), MX, 130, 888, 'pearl', 4, tool_fill=C['tealMist'], size=72, maxh=1050)

    # ---------------------------------------------------------------- LOOK 5: night bubble
    elif look == 5:
        people = K['people']
        if first:
            art += glow(980, 140, 300, .45)
            art += stars([(110, 130, 14), (250, 230, 9), (980, 1000, 10)], tone)
            art += people(g, tone)
            segs, px = fit_hook(ctx, 790, 900)
            html += card(segs, 80, 110, 920, 5, cls='bubble hookcard', size=96, seed=51, kind='card', maxh=K.get('hook_maxh', 700), minfs=72, shape='bubble', tail='r', pad=64)
        elif last:
            art += glow(90, 1250, 260, .4)
            art += stars([(980, 1240, 12), (120, 120, 11)], tone)
            q, qh = qr_card(ctx.post_id, 110, 900, tone=tone)
            art += q
            html += card(allsegs(ctx), 100, 90, 880, 5, size=72, seed=53, cls='bubble endcard', maxh=760, shape='bubble', tail='none', pad=48)
        else:
            art += glow(90 if ctx.i % 2 else 990, 1240, 240, .35)
            art += stars([(980 if ctx.i % 2 else 120, 1220, 12)], tone, seed=ctx.i)
            px = body_size(ctx, 748, 920)
            html += card(allsegs(ctx), 110, 130, 860, 5, tool_fill=C['tealMist'], size=72, seed=55 + ctx.i, cls='bubble', maxh=930, shape='bubble', tail='l' if ctx.i % 2 else 'r', pad=60)

    return {'ground': g, 'art': art, 'html': html,
            'dots_theme': 'dark' if g in DARK else 'light'}
