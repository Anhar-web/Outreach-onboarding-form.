"""b3p12 Winter jacket, two voices. Deep ground. Composition: COAT-HOOK RAIL.

A wooden rail with pearl hooks runs across the art; a small teal puffer jacket
moves around it. s1 the jacket carried over mum's pearl sleeve, the hooks
empty. s2 two wordless torn bubbles: grandma's (right) holds a pushing hand on
the jacket, mum's inner thought (left) holds crying arcs. s3 a bare small hand
with frost flakes, the jacket still on mum's arm. s4 the jacket alone on a
hook. s5 a second, LOW rail with the jacket on it and a small hand reaching it.
s6 the hooks empty, an abaya sleeve and the small puffer sleeve going on side
by side. s7 the jacket dropped on the floor under the low rail.
CTA end: gold, a mini rail with the jacket in the bottom-right, tag on the left.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_rect, torn_poly, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'deep'
T = 'd'


def rail(x0, x1, y, hooks=(), s=1.0):
    """Wooden rail (goldDeep, gold top band) with pearl J hooks at the given x's."""
    h = 44 * s
    out = paper(f'<rect x="{x0}" y="{y - h / 2}" width="{x1 - x0}" height="{h}" rx="{8 * s}" fill="{C["goldDeep"]}"/>'
                f'<rect x="{x0}" y="{y - h / 2}" width="{x1 - x0}" height="{h * .28}" rx="{6 * s}" fill="{C["gold"]}"/>'
                f'<circle cx="{x0 + 30 * s}" cy="{y}" r="{6 * s}" fill="{C["ink"]}" fill-opacity=".5"/>'
                f'<circle cx="{x1 - 30 * s}" cy="{y}" r="{6 * s}" fill="{C["ink"]}" fill-opacity=".5"/>', T, 1)
    for hx in hooks:
        out += hook(hx, y, s)
    return avoid(out, 'rail')


def hook(x, y, s=1.0):
    return paper(f'<g transform="translate({x} {y}) scale({s})">'
                 f'<circle cx="0" cy="0" r="14" fill="{C["tealMist"]}"/>'
                 f'<path d="M 0 0 V 62 Q 0 100 36 92 Q 52 86 50 66" fill="none" stroke="{C["pearl"]}" stroke-width="15" stroke-linecap="round"/>'
                 f'<circle cx="50" cy="62" r="11" fill="{C["pearl"]}"/></g>', T, 2)


def jacket(x, y, s=1.0, rot=0, splay=8, layer=2):
    """Small teal puffer jacket, front view. Local frame: the hanging loop at
    (0,0), the jacket hangs down. Quilted bands, pearl zip, gold zip pull,
    tealDeep collar and folded hood. splay = sleeve angle."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    q = C['tealDeep']
    out = (f'<path d="M -12 -2 Q 0 -26 12 -2" fill="none" stroke="{q}" stroke-width="8"/>'
           f'<ellipse cx="0" cy="22" rx="78" ry="38" fill="{q}"/>')
    for sd in (-1, 1):
        # sleeves hang from the shoulder corners and splay outwards
        g = f'<g transform="rotate({sd * splay} {sd * 112} 52)">'
        g += f'<rect x="{sd * 148 - 38}" y="40" width="76" height="236" rx="34" fill="{C["teal"]}"/>'
        g += ''.join(f'<path d="M {sd * 148 - 36} {100 + k * 52} Q {sd * 148} {108 + k * 52} {sd * 148 + 36} {100 + k * 52}" fill="none" stroke="{q}" stroke-width="6"/>' for k in range(3))
        g += f'<rect x="{sd * 148 - 34}" y="248" width="68" height="30" rx="12" fill="{q}"/></g>'
        out += g
    out += f'<path d="M -112 40 Q 0 30 112 40 L 128 300 Q 0 322 -128 300 Z" fill="{C["teal"]}"/>'
    out += ''.join(f'<path d="M {-118 - k * 2} {96 + k * 52} Q 0 {108 + k * 52} {118 + k * 2} {96 + k * 52}" fill="none" stroke="{q}" stroke-width="6"/>' for k in range(4))
    out += f'<rect x="-64" y="28" width="128" height="36" rx="14" fill="{q}"/>'
    out += f'<path d="M 0 62 V 308" stroke="{C["pearl"]}" stroke-width="7"/><rect x="-8" y="62" width="16" height="30" rx="5" fill="{C["gold"]}"/>'
    return paper(f'<g transform="{tr}">{out}</g>', T, layer)


ARM_HAND = ('<path d="M 6 -48 Q -60 -60 -110 -38 Q -140 -20 -130 6 Q -120 26 -90 22 L -40 30 Q -10 52 6 48 Z" fill="{sk}"/>'
            '<path d="M -100 -30 Q -150 -12 -126 18" fill="none" stroke="{gd}" stroke-opacity=".35" stroke-width="4"/>')


def arm(x, y, rot=0, s=1.0, sleeve='pearl', length=520, hand=True, layer=3, band=None):
    """A forearm: sleeve running off to local +x from (x,y), hand beyond it to -x."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    g = f'<rect x="0" y="-62" width="{length}" height="124" rx="30" fill="{C[sleeve]}"/>'
    if band:
        g += f'<rect x="0" y="-62" width="26" height="124" fill="{C[band]}"/>'
    if hand:
        g += ARM_HAND.format(sk=C['sandLight'], gd=C['goldDeep'])
    return paper(f'<g transform="{tr}">{g}</g>', T, layer)


def small_hand(x, y, s=1.0, rot=0, cuff='tealDeep'):
    """A small hand reaching up (fingers to -y), cuff below."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    g = f'<rect x="-52" y="-4" width="104" height="220" rx="16" fill="{C[cuff]}"/>'
    g += f'<rect x="-46" y="-120" width="92" height="126" rx="36" fill="{C["sandLight"]}"/>'
    for fx, L, a in ((-31, 64, -12), (-10, 78, -4), (11, 74, 4), (32, 58, 12)):
        g += f'<rect x="{fx - 10}" y="{-110 - L}" width="20" height="{L + 20}" rx="10" fill="{C["sandLight"]}" transform="rotate({a} {fx} -110)"/>'
    g += f'<rect x="32" y="-110" width="24" height="76" rx="12" fill="{C["sandLight"]}" transform="rotate(48 44 -40)"/>'
    return paper(f'<g transform="{tr}">{g}</g>', T, 3)


def bubble(x, y, w, h, tail, fill='pearl', seed=5):
    """A torn speech bubble with a tail ending at `tail`."""
    tx, ty = tail
    bx = min(max(tx, x + 70), x + w - 70)
    pts = [(x, y), (x + w, y), (x + w, y + h), (bx + 40, y + h), (tx, ty), (bx - 40, y + h), (x, y + h)]
    return torn_poly(pts, C[fill], T, seed=seed, layer=2)


def thought(x, y, w, h, trail, fill='tealMist', inner=''):
    """mum's inner voice: a cloud of overlapping circles + a trail of small circles."""
    cx, cy = x + w / 2, y + h / 2
    blobs = [(cx, cy, h * .5), (cx - w * .3, cy + 6, h * .42), (cx + w * .3, cy + 4, h * .42),
             (cx - w * .14, cy - h * .2, h * .4), (cx + w * .16, cy - h * .18, h * .38)]
    shapes = ''.join(f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="{r:.0f}" fill="{C[fill]}"/>' for bx, by, r in blobs)
    out = paper(shapes, T, 2) + paper(inner, T, 3)
    for tx, ty, r in trail:
        out += paper(f'<circle cx="{tx}" cy="{ty}" r="{r}" fill="{C[fill]}"/>', T, 2)
    return out


def cry_arcs(x, y, s=1.0):
    """Crying as gold zig-zag bursts (no face)."""
    out = ''
    for a in (-160, -120, -60, -20):
        r0, r1 = 34 * s, 92 * s
        ar = math.radians(a)
        p = [(x + r0 * math.cos(ar), y + r0 * math.sin(ar))]
        for j in range(1, 4):
            rr = r0 + (r1 - r0) * j / 3
            off = (12 * s) * (1 if j % 2 else -1)
            p.append((x + rr * math.cos(ar) - off * math.sin(ar), y + rr * math.sin(ar) + off * math.cos(ar)))
        d = 'M ' + ' L '.join(f'{px:.0f} {py:.0f}' for px, py in p)
        out += f'<path d="{d}" fill="none" stroke="{C["gold"]}" stroke-width="{10 * s}" stroke-linecap="round" stroke-linejoin="round"/>'
    return out


def flake(x, y, r=16):
    d = ''.join(f'M {x} {y} L {x + r * math.cos(math.radians(a)):.1f} {y + r * math.sin(math.radians(a)):.1f} ' for a in range(0, 360, 60))
    return paper(f'<path d="{d}" stroke="{C["pearl"]}" stroke-width="5" stroke-linecap="round"/>', T, 2)


def floor(y, seed=3):
    return torn_rect(-20, y, W + 40, H - y + 20, C['night'], T, sides='t', seed=seed, layer=1)


def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = (rail(600, 1010, 980, hooks=(700, 900), s=.7) + jacket(700 + 35 * .7, 980 + 64 * .7, .55))
        return cta_end(ctx, mini_art=mini, tag_y=1040, tag_x=110)
    art, html = '', ''
    if s == 1:
        art = rail(60, 1020, 760, hooks=(250, 540, 830))
        art += avoid(jacket(520, 930, 1.05, rot=-4, splay=10) + arm(640, 990, rot=-4, length=520), 'jacket')
        html = hook_box(ctx, G, y=MT - 10, size=96)
    elif s == 2:
        art = avoid(bubble(590, 610, 400, 260, (960, 960), seed=5)
                    + jacket(790, 640, .5, splay=8)
                    + paper(f'<g transform="translate(930 790) rotate(200) scale(.55)"><rect x="0" y="-62" width="200" height="124" rx="30" fill="{C["goldDeep"]}"/>'
                            + ARM_HAND.format(sk=C['sandLight'], gd=C['goldDeep']) + '</g>', T, 3), 'gran')
        art += avoid(thought(90, 830, 380, 220, [(420, 1070, 18), (470, 1100, 12)], inner=cry_arcs(280, 950, 1.0)), 'mum')
        art += avoid(jacket(560, 1080, .6, rot=-4, splay=10) + arm(640, 1115, rot=-4, length=520, s=.7), 'carry')
        html = body_box(ctx, G)
    elif s == 3:
        art = avoid(small_hand(260, 1240, 1.6, rot=10), 'small')
        for (fx, fy, r) in ((120, 720, 18), (330, 640, 14), (430, 790, 20), (110, 950, 14), (470, 980, 12), (200, 600, 10)):
            art += flake(fx, fy, r)
        art += avoid(jacket(700, 850, .95, rot=-4, splay=10) + arm(800, 905, rot=-4, length=500), 'jacket')
        html = body_box(ctx, G)
    elif s == 4:
        art = rail(60, 1020, 470, hooks=(250, 540, 830))
        art += avoid(jacket(540 + 36, 470 + 72, 1.25, splay=6), 'jacket')
        html = body_box(ctx, G) + soft_cta(ctx, y=1060)
    elif s == 5:
        art = rail(60, 1020, 600, hooks=(300, 800))
        art += paper(f'<path d="M 800 668 Q 760 668 720 700 L 690 1180 L 910 1180 L 880 700 Q 840 668 800 668 Z" fill="{C["ink"]}"/>'
                     f'<path d="M 800 690 V 1180" stroke="{C["gold"]}" stroke-width="8"/>', T, 1)
        art += floor(1250)
        art += rail(60, 600, 900, hooks=(330,), s=.9)
        art += avoid(jacket(330 + 32, 900 + 64, .9, splay=6), 'jacket')
        art += avoid(small_hand(640, 1340, 1.25, rot=-28), 'small')
        html = body_box(ctx, G)
    elif s == 6:
        art = rail(60, 1020, 560, hooks=(300, 760))
        arms = arm(330, 880, rot=-12, s=1.0, sleeve='ink', length=900, band='gold')
        arms += paper(f'<g transform="translate(420 1150) rotate(-12) scale(.78)"><rect x="0" y="-62" width="900" height="124" rx="44" fill="{C["teal"]}"/>'
                      + ''.join(f'<path d="M {80 + k * 100} -60 Q {94 + k * 100} 0 {80 + k * 100} 60" fill="none" stroke="{C["tealDeep"]}" stroke-width="8"/>' for k in range(7))
                      + f'<rect x="0" y="-62" width="34" height="124" rx="12" fill="{C["tealDeep"]}"/>'
                      + ARM_HAND.format(sk=C['sandLight'], gd=C['goldDeep']) + '</g>', T, 3)
        art += avoid(arms, 'arms')
        html = body_box(ctx, G)
    elif s == 7:
        art = rail(60, 640, 720, hooks=(360,), s=.9)
        art += floor(1130, seed=8)
        art += avoid(jacket(620, 1060, .95, rot=-96, splay=34), 'jacket')
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
