"""b3p6 Sibling and the tower. Deep ground. Composition: VERTICAL STACK HERO.

One tall tower of coloured paper blocks stands centre-frame. s1 it topples
(blocks mid-fall) as mum's abaya knees rise at the right edge. s2 the tower
whole, a small sister's hand reaching from the left, a pot steaming far right.
s3 blocks scattered, two small figures from behind. s4 the half tower, its top
blocks lying on the floor. s5 a wide shallow box with raised torn edges, the
tower standing inside. s6 the box in the room's corner, a clear pearl path of
floor running past it. CTA end: gold, a mini box with blocks bottom-right.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_rect, torn_strip, torn_poly, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'deep'
T = 'd'
COLS = ['gold', 'teal', 'pearl', 'sandLight', 'tealMist', 'goldDeep']
MARK = {'gold': 'goldDeep', 'teal': 'tealMist', 'pearl': 'teal', 'sandLight': 'gold', 'tealMist': 'teal', 'goldDeep': 'gold'}


def block(cx, cy, sz, k, rot=0):
    """One cube, front face + a thin lighter top band, with a simple cut shape
    (circle / triangle / square, never letters) on the front."""
    col = COLS[k % len(COLS)]
    mk = C[MARK[col]]
    h = sz / 2
    shape = k % 3
    if shape == 0:
        m = f'<circle cx="0" cy="4" r="{sz * .22:.1f}" fill="{mk}"/>'
    elif shape == 1:
        r = sz * .26
        m = f'<path d="M 0 {4 - r:.1f} L {r:.1f} {4 + r * .8:.1f} L {-r:.1f} {4 + r * .8:.1f} Z" fill="{mk}"/>'
    else:
        r = sz * .2
        m = f'<rect x="{-r:.1f}" y="{4 - r:.1f}" width="{2 * r:.1f}" height="{2 * r:.1f}" fill="{mk}"/>'
    g = (f'<g transform="translate({cx:.1f} {cy:.1f}) rotate({rot:.1f})">'
         f'<rect x="{-h}" y="{-h}" width="{sz}" height="{sz}" rx="6" fill="{C[col]}"/>'
         f'<rect x="{-h}" y="{-h}" width="{sz}" height="{sz * .14:.1f}" rx="5" fill="{C["pearl"]}" fill-opacity=".45"/>'
         f'{m}</g>')
    return paper(g, T, 2)


def tower(cx, base, n, sz=104, k0=0, sway=6):
    out = ''
    for k in range(n):
        dx = sway * math.sin(k * 1.7)
        out += block(cx + dx, base - sz / 2 - k * sz, sz, k0 + k, rot=(k % 2) * 2 - 1)
    return out


def toppling(px, base, n, sz=100, k0=0):
    """The tower falling to the left about its base: each block higher up has
    turned further and flies a little apart."""
    out = ''
    for k in range(n):
        a = math.radians(4 + k * 6)
        r = sz / 2 + k * sz * (1 + .04 * k)
        x = px - r * math.sin(a) - (k * k * 1.6)
        y = base - r * math.cos(a) + (k * k * 2.6)
        out += block(x, y, sz, k0 + k, rot=-(8 + k * 10))
    return out


def floor(y, seed=3, x0=80, x1=1000, h=150):
    """A majlis floor rug (tealDeep, gold border lines), its fringed ends torn."""
    inner = (f'<rect x="{x0 + 18}" y="{y + 16}" width="{x1 - x0 - 36}" height="8" fill="{C["gold"]}"/>'
             f'<rect x="{x0 + 18}" y="{y + h - 24}" width="{x1 - x0 - 36}" height="8" fill="{C["gold"]}"/>')
    return torn_rect(x0, y, x1 - x0, h, C['tealDeep'], T, sides='lr', seed=seed, layer=1, inner=inner)


def knees(x, y, s=1.0):
    """mum getting up from the floor at the right edge, seen from the side: the
    abaya over a bent knee (knee at (x, y)), thigh rising off-canvas to the
    right, gold hem along the floor, a hand pressing on the knee, rising lines."""
    g = (f'<g transform="translate({x} {y}) scale({s})">'
         f'<path d="M -40 230 L -40 40 Q -40 -40 40 -40 L 400 -300 L 400 230 Z" fill="{C["ink"]}"/>'
         f'<rect x="-50" y="212" width="460" height="20" fill="{C["gold"]}"/>'
         f'<path d="M 20 -70 Q -30 -90 -60 -60 Q -78 -40 -60 -22 L 0 -10 L 70 -30 Z" fill="{C["sandLight"]}"/>'
         f'<rect x="20" y="-110" width="300" height="90" rx="30" fill="{C["ink"]}" transform="rotate(-38 20 -60)"/>'
         f'<rect x="12" y="-112" width="22" height="94" fill="{C["gold"]}" transform="rotate(-38 20 -60)"/></g>')
    out = paper(g, T, 3)
    for k in range(3):
        xx = x - 110 * s - k * 40 * s
        out += torn_strip([(xx, y + 60 * s - k * 30), (xx, y - 60 * s - k * 30)], 9, C['pearl'], T, seed=40 + k, layer=1)
    return out


def small_hand(x, y, s=1.0, rot=0, cuff='gold'):
    """A small hand reaching (fingers to local -y), sleeve behind."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    g = f'<rect x="-52" y="-4" width="104" height="400" rx="16" fill="{C[cuff]}"/>'
    g += f'<rect x="-46" y="-120" width="92" height="126" rx="36" fill="{C["sandLight"]}"/>'
    for fx, L, a in ((-31, 64, -12), (-10, 78, -4), (11, 74, 4), (32, 58, 12)):
        g += f'<rect x="{fx - 10}" y="{-110 - L}" width="20" height="{L + 20}" rx="10" fill="{C["sandLight"]}" transform="rotate({a} {fx} -110)"/>'
    g += f'<rect x="32" y="-110" width="24" height="76" rx="12" fill="{C["sandLight"]}" transform="rotate(48 44 -40)"/>'
    return paper(f'<g transform="{tr}">{g}</g>', T, 3)


def pot(x, y, s=1.0, steam=True):
    """A cooking pot (gold), lid with knob, two handles, steam as pearl wavy strips."""
    g = (f'<g transform="translate({x} {y}) scale({s})">'
         f'<rect x="-150" y="-30" width="40" height="22" rx="10" fill="{C["goldDeep"]}"/>'
         f'<rect x="110" y="-30" width="40" height="22" rx="10" fill="{C["goldDeep"]}"/>'
         f'<path d="M -120 -40 L 120 -40 L 110 120 Q 0 134 -110 120 Z" fill="{C["gold"]}"/>'
         f'<rect x="-120" y="-40" width="240" height="18" fill="{C["goldDeep"]}"/>'
         f'<path d="M -130 -42 Q 0 -100 130 -42 Z" fill="{C["sandLight"]}"/>'
         f'<rect x="-16" y="-90" width="32" height="22" rx="10" fill="{C["goldDeep"]}"/></g>')
    out = paper(g, T, 2)
    if steam:
        for k, dx in enumerate((-60, 0, 60)):
            pts = [(x + dx * s + 18 * math.sin(j * 1.3 + k) * s, y - 110 * s - j * 34 * s) for j in range(7)]
            out += torn_strip(pts, 14 * s, C['pearl'], T, seed=60 + k, layer=1)
    return out


def child_back(cx, cy, r=80, body='tealDeep', hair='goldDeep'):
    """A small child seen from behind: shoulders, neck, ears, round back of the head (no face)."""
    out = paper(f'<path d="M {cx - r * 1.7} {cy + r * 2.6} Q {cx - r * 1.6} {cy + r * 1.05} {cx} {cy + r} '
                f'Q {cx + r * 1.6} {cy + r * 1.05} {cx + r * 1.7} {cy + r * 2.6} Z" fill="{C[body]}"/>'
                f'<rect x="{cx - r * .32}" y="{cy + r * .55}" width="{r * .64}" height="{r * .6}" rx="{r * .2}" fill="{C["sandLight"]}"/>'
                f'<ellipse cx="{cx - r * .98}" cy="{cy + r * .1}" rx="{r * .16}" ry="{r * .26}" fill="{C["sandLight"]}"/>'
                f'<ellipse cx="{cx + r * .98}" cy="{cy + r * .1}" rx="{r * .16}" ry="{r * .26}" fill="{C["sandLight"]}"/>', T, 1)
    out += paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C[hair]}"/>', T, 2)
    return out


def box(cx, base, w=720, h=170, s=1.0, inner=''):
    """A wide shallow box with raised torn walls, seen from the front and a little
    above: back wall (sandLight, torn top), gold inside floor, gold side walls in
    perspective, front wall (pearl, torn top). `inner` is drawn inside."""
    w, h = w * s, h * s
    d = 70 * s
    x0, x1 = cx - w / 2, cx + w / 2
    top = base - h
    back = torn_rect(x0 + 50 * s, top - d - h * .55, w - 100 * s, h * .55 + d, C['sandLight'], T, sides='t', seed=12, layer=1)
    bottom = paper(f'<polygon points="{x0 + 50 * s},{top - d} {x1 - 50 * s},{top - d} {x1},{top} {x0},{top}" fill="{C["gold"]}"/>', T, 1)
    sides = (torn_poly([(x0, top), (x0 + 50 * s, top - d), (x0 + 50 * s, top - d - h * .55), (x0, top - h * .25)], C['goldDeep'], T, seed=14, layer=1, torn=[2, 3])
             + torn_poly([(x1, top), (x1 - 50 * s, top - d), (x1 - 50 * s, top - d - h * .55), (x1, top - h * .25)], C['goldDeep'], T, seed=15, layer=1, torn=[2, 3]))
    front = torn_rect(x0, top - h * .25, w, h * 1.25, C['pearl'], T, sides='t', seed=13, layer=3,
                      inner=f'<rect x="{x0}" y="{top + h * .5}" width="{w}" height="{10 * s}" fill="{C["gold"]}"/>')
    return back + bottom + sides + inner + front


def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = box(800, 1230, 380, 90, 1.0, inner=tower(800, 1180, 4, 64, sway=3))
        return cta_end(ctx, mini_art=mini, tag_y=890, tag_x=120)
    art, html = '', ''
    if s == 1:
        art = floor(1120, x0=60, x1=760)
        art += avoid(toppling(520, 1190, 6, sz=104), 'tower')
        art += avoid(knees(860, 1050, 1.0), 'mum')
        html = hook_box(ctx, G, y=MT - 10, size=94)
    elif s == 2:
        art = floor(1120, x0=200, x1=760)
        art += avoid(tower(480, 1200, 5, sz=110), 'tower')
        art += avoid(small_hand(200, 1010, 1.2, rot=62), 'sister')
        art += avoid(pot(900, 1100, .75), 'pot')
        html = body_box(ctx, G)
    elif s == 3:
        art = floor(1080, x0=40, x1=1040, h=200)
        for k, (x, y, r) in enumerate(((140, 1110, 20), (300, 1210, -30), (880, 1110, 12), (990, 1240, -14), (90, 1270, 40),
                                       (640, 1010, 35), (430, 800, -40), (820, 760, 60), (560, 680, 20))):
            art += block(x, y, 96, k, rot=r)
        art += avoid(child_back(380, 1160, r=100, body='tealDeep') + child_back(730, 1210, r=76, body='gold', hair='ink'), 'kids')
        html = body_box(ctx, G)
    elif s == 4:
        art = floor(1120, x0=100, x1=980)
        art += avoid(tower(520, 1200, 3, sz=118), 'tower')
        art += avoid(block(770, 1140, 108, 3, rot=24) + block(900, 1170, 108, 4, rot=-12) + block(250, 1150, 108, 5, rot=38), 'fallen')
        html = body_box(ctx, G) + soft_cta(ctx, y=440)
    elif s == 5:
        art = avoid(box(540, 1250, 800, 170, 1.0, inner=tower(540, 1080, 4, sz=104, sway=4)), 'box')
        html = body_box(ctx, G)
    elif s == 6:
        # the room corner: wall seam, the box tucked in the corner, a clear pearl path of floor
        art = torn_poly([(-20, 900), (1100, 800), (1100, 1370), (-20, 1370)], C['night'], T, seed=21, layer=1, torn=[])
        art += paper(f'<path d="M 830 560 V 808" stroke="{C["tealDeep"]}" stroke-width="10"/>', T, 1)
        art += avoid(box(840, 1010, 400, 100, 1.0, inner=tower(840, 935, 4, sz=66, sway=3)), 'box')
        art += torn_strip([(-20, 1250), (200, 1200), (380, 1150), (520, 1080), (600, 1000), (620, 920)], 80, C['pearl'], T, seed=31, layer=1)
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
