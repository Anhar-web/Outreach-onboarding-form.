"""p10 Hair wash. Deep ground. Composition: VERTICAL CASCADE.

A shower head sits high on the left; torn teal water strips fall diagonally to
the right, over a small head seen from behind (never a face). Mum is a wet pearl
sleeve. Across the slides the water changes state: pouring (s1), splashing (s2),
cut at ten (s5), gentle from a hand shower (s6), all three tools together (s7).
CTA end: gold, the towel + hand shower small in the bottom-left.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'deep'
T = 'd'


def shower_head(x, y, s=1.0, tone=T):
    tr = f'translate({x} {y}) scale({s})'
    pipe = paper(f'<path d="M -260 -40 H -40 Q 0 -40 0 0 V 30" fill="none" stroke="{C["pearl"]}" stroke-width="34" stroke-linecap="round"/>', tone, 1, T=tr)
    head = paper(f'<path d="M -110 30 H 110 Q 120 30 110 70 L 90 110 H -90 L -110 70 Q -120 30 -110 30 Z" fill="{C["gold"]}"/>'
                 + ''.join(f'<circle cx="{-60 + k * 30}" cy="96" r="6" fill="{C["goldDeep"]}"/>' for k in range(5)), tone, 2, T=tr)
    return head and (pipe + head)


def water(x0, y0, n=7, length=520, spread=26, angle=72, seed=1, width=22, cols=('teal', 'pearl'), gaps=False):
    """Torn strips falling from (x0, y0) at `angle` degrees (90 = straight down)."""
    out = ''
    for k in range(n):
        a = math.radians(angle + (k - n / 2) * 3)
        sx = x0 + (k - n / 2) * spread
        L = length * (0.85 + 0.3 * ((k * 37) % 7) / 7)
        p0 = (sx, y0)
        p1 = (sx + L * math.cos(a), y0 + L * math.sin(a))
        if gaps:  # cut water: a short stub only
            p1 = (sx + L * .25 * math.cos(a), y0 + L * .25 * math.sin(a))
        out += torn_strip([p0, p1], width, C[cols[k % len(cols)]], T, seed=seed + k, layer=2)
    return out


def drops(pts, r=14, col='teal', seed=40):
    out = ''
    for i, (x, y) in enumerate(pts):
        out += paper(f'<path d="M {x} {y - r * 1.6} Q {x + r} {y - r * .2} {x} {y + r} Q {x - r} {y - r * .2} {x} {y - r * 1.6} Z" fill="{C[col]}"/>', T, 1)
    return out


def small_head(cx, cy, r=150, foam=True):
    """Back of a small head (no face): mostly goldDeep hair, two sandLight ears,
    a neck and shoulders below; pearl shampoo foam on top."""
    out = paper(f'<path d="M {cx - r * 1.7} {cy + r * 2.4} Q {cx - r * 1.6} {cy + r * 1.05} {cx} {cy + r} Q {cx + r * 1.6} {cy + r * 1.05} {cx + r * 1.7} {cy + r * 2.4} Z" fill="{C["tealDeep"]}"/>', T, 1)
    out += paper(f'<rect x="{cx - r * .32}" y="{cy + r * .55}" width="{r * .64}" height="{r * .6}" rx="{r * .2}" fill="{C["sandLight"]}"/>', T, 1)
    out += paper(f'<ellipse cx="{cx - r * .98}" cy="{cy + r * .1}" rx="{r * .16}" ry="{r * .26}" fill="{C["sandLight"]}"/>'
                 f'<ellipse cx="{cx + r * .98}" cy="{cy + r * .1}" rx="{r * .16}" ry="{r * .26}" fill="{C["sandLight"]}"/>', T, 1)
    out += paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["goldDeep"]}"/>', T, 2)
    if foam:
        for k, (dx, dy, rr) in enumerate(((-.55, -.7, .3), (-.05, -.92, .34), (.5, -.7, .3), (.22, -.48, .22), (-.3, -.45, .2))):
            out += torn_circle(cx + dx * r, cy + dy * r, rr * r, C['pearl'], T, seed=60 + k, layer=3, amp=(3, 6))
    return avoid(out, 'head')


def sleeve(x, y, rot=-30, wet=True):
    """Mum's pearl sleeve + hand reaching in from the edge."""
    g = (f'<g transform="translate({x} {y}) rotate({rot})">'
         f'<rect x="-420" y="-60" width="400" height="120" rx="20" fill="{C["pearl"]}"/>'
         f'<rect x="-40" y="-62" width="40" height="124" rx="10" fill="{C["sandLight"]}"/>'
         f'<path d="M 0 -48 Q 90 -60 120 -20 Q 130 10 100 40 Q 60 60 0 48 Z" fill="{C["sandLight"]}"/></g>')
    out = paper(g, T, 2)
    if wet:
        out += paper(f'<g transform="translate({x} {y}) rotate({rot})">'
                     + ''.join(f'<ellipse cx="{-360 + k * 70}" cy="{-10 + (k % 2) * 30}" rx="22" ry="12" fill="{C["teal"]}" fill-opacity=".55"/>' for k in range(5))
                     + '</g>', T, 3, 't')
    return avoid(out, 'sleeve')


def towel(cx, cy, w=300, h=150, rot=-6, hand=True):
    out = torn_rect(cx - w / 2, cy - h / 2, w, h, C['sandLight'], T, sides='lr', seed=31, layer=3, rot=rot,
                    inner=f'<rect x="{cx - w / 2}" y="{cy + h / 2 - 34}" width="{w}" height="14" fill="{C["gold"]}" transform="rotate({rot} {cx} {cy})"/>')
    if hand:
        out += paper(f'<g transform="translate({cx + w / 2 - 20} {cy + 10}) rotate({rot})"><path d="M 0 -40 Q 70 -50 80 0 Q 70 50 0 40 Z" fill="{C["sandLight"]}"/>'
                     f'<path d="M 0 -40 Q 70 -50 80 0 Q 70 50 0 40" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="3"/></g>', T, 3)
    return avoid(out, 'towel')


def hand_shower(x, y, s=1.0, rot=0, stream=True, seed=5, hand=False, hose=True, n_stream=5, L=220):
    """Hand-held shower, 3/4 view. Local frame: the spray face points up (-y), the
    handle leaves the BACK of the head at an angle (never a stalk under a cap, so it
    can't read as a mushroom), a ribbed teal hose curls away from the handle end,
    and the face shows a grid of nozzles. (x, y) = centre of the spray face;
    rot = degrees clockwise: rot 0 sprays up, rot 180 sprays down."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    out = ''
    if hose:
        out += paper(f'<path d="M 128 318 C 150 420, 300 430, 330 340 C 352 270, 250 250, 260 360 C 268 460, 420 520, 520 470" '
                     f'fill="none" stroke="{C["tealDeep"]}" stroke-width="30" stroke-linecap="round"/>'
                     f'<path d="M 128 318 C 150 420, 300 430, 330 340 C 352 270, 250 250, 260 360 C 268 460, 420 520, 520 470" '
                     f'fill="none" stroke="{C["teal"]}" stroke-width="30" stroke-dasharray="6 14" stroke-opacity=".55"/>', T, 1, T=tr)
    # handle: tapered, leaves the back-bottom of the head at ~22 degrees
    out += paper(f'<path d="M -6 30 L 46 22 L 142 300 Q 146 330 120 336 L 104 340 Q 84 340 80 318 Z" fill="{C["pearl"]}"/>'
                 f'<path d="M 22 40 L 108 318" stroke="{C["tealMist"]}" stroke-width="10" stroke-linecap="round" stroke-opacity=".8"/>'
                 f'<rect x="92" y="300" width="56" height="30" rx="8" fill="{C["gold"]}" transform="rotate(-19 120 315)"/>', T, 2, T=tr)
    # head: thickness band (goldDeep) + face (gold) + pearl rim + nozzles
    holes = ''
    for r_, n_ in ((0, 1), (28, 6), (56, 11)):
        for k in range(n_):
            a = 2 * math.pi * k / n_
            holes += f'<ellipse cx="{r_ * 1.3 * math.cos(a):.1f}" cy="{-4 + r_ * .55 * math.sin(a):.1f}" rx="6.5" ry="4.5" fill="{C["goldDeep"]}"/>'
    out += paper(f'<ellipse cx="0" cy="22" rx="112" ry="52" fill="{C["goldDeep"]}"/>'
                 f'<rect x="-112" y="-4" width="224" height="26" fill="{C["goldDeep"]}"/>'
                 f'<ellipse cx="0" cy="-4" rx="112" ry="52" fill="{C["pearl"]}"/>'
                 f'<ellipse cx="0" cy="-4" rx="98" ry="44" fill="{C["gold"]}"/>' + holes, T, 3, T=tr)
    if hand:
        # a small hand wrapped round the handle, wrist + sleeve running off down the handle line
        out += paper(f'<g transform="{tr}"><path d="M 150 300 L 260 620 L 170 660 L 74 330 Z" fill="{C["tealDeep"]}"/>'
                     f'<path d="M 40 150 Q 30 120 66 112 L 120 104 Q 150 104 154 136 L 168 270 Q 172 310 130 316 L 96 320 Q 64 320 60 290 Z" fill="{C["sandLight"]}"/>'
                     + ''.join(f'<path d="M {50 + k * 4} {150 + k * 34} Q {100 + k * 4} {140 + k * 34} {150 + k * 4} {150 + k * 34}" fill="none" '
                               f'stroke="{C["goldDeep"]}" stroke-opacity=".45" stroke-width="5" stroke-linecap="round"/>' for k in range(4))
                     + f'<path d="M 40 150 Q 10 190 34 216 Q 52 226 66 206" fill="{C["sandLight"]}"/></g>', T, 3)
    if stream:
        a0 = math.radians(rot - 90)
        for k in range(n_stream):
            off = (k - (n_stream - 1) / 2) * 34 * s
            sx = x + off * math.cos(a0 + math.pi / 2) + 40 * s * math.cos(a0)
            sy = y + off * math.sin(a0 + math.pi / 2) + 40 * s * math.sin(a0)
            spread = (k - (n_stream - 1) / 2) * .07
            ll = L * s * (0.85 + 0.25 * ((k * 3) % 4) / 3)
            out += torn_strip([(sx, sy), (sx + ll * math.cos(a0 + spread), sy + ll * math.sin(a0 + spread))], 12 * min(s, 1.2),
                              C['teal'] if k % 2 else C['tealMist'], T, seed=seed + k, layer=2)
    return avoid(out, 'shower')


def counting(x, y, n=10, lit=10, r=26, gap=70):
    """Ten gold paper discs in two rows (counting one to ten), the lit ones gold."""
    out = ''
    for k in range(n):
        cx = x - (k % 5) * gap
        cy = y + (k // 5) * gap
        col = C['gold'] if k < lit else C['tealDeep']
        out += paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/>', T, 2 if k < lit else 1)
    return avoid(out, 'count')


def towel_eyes(cx, cy, r):
    """s4: a dry sandLight face towel held over the eyes. Seen from behind, so the
    head hides the middle of the towel; its two ends stick out at eye height on
    both sides, each pinched by a small hand."""
    y = cy + r * .05
    out = torn_rect(cx - r * 1.75, y - r * .32, r * 3.5, r * .62, C['sandLight'], T, sides='lr', seed=33, layer=1, rot=-3,
                    inner=f'<rect x="{cx - r * 1.75}" y="{y + r * .14}" width="{r * 3.5}" height="{r * .1}" fill="{C["gold"]}" transform="rotate(-3 {cx} {y})"/>')
    for side in (-1, 1):
        hx = cx + side * r * 1.32
        out += paper(f'<g transform="translate({hx} {y + 4}) rotate({side * 10})">'
                     f'<rect x="-{r * .2}" y="-{r * .3}" width="{r * .4}" height="{r * .62}" rx="{r * .18}" fill="{C["sandLight"]}"/>'
                     f'<path d="M -{r * .16} -{r * .08} H {r * .16} M -{r * .16} {r * .08} H {r * .16}" stroke="{C["goldDeep"]}" stroke-opacity=".45" stroke-width="5" stroke-linecap="round"/>'
                     f'<rect x="-{r * .2}" y="{r * .26}" width="{r * .4}" height="{r * .6}" fill="{C["tealDeep"]}"/></g>', T, 2)
    return avoid(out, 'towel')


def splash(cx, cy, r, seed=70):
    """s2: water bouncing off the head in every direction: short torn strips that
    radiate from the crown, plus flung drops."""
    out = ''
    for k, a in enumerate((-160, -135, -112, -68, -45, -20, 200, -5)):
        ar = math.radians(a)
        p0 = (cx + r * 1.05 * math.cos(ar), cy + r * 1.05 * math.sin(ar))
        p1 = (cx + r * (1.55 + .2 * (k % 3)) * math.cos(ar), cy + r * (1.55 + .2 * (k % 3)) * math.sin(ar))
        out += torn_strip([p0, p1], 16, C['teal'] if k % 2 else C['tealMist'], T, seed=seed + k, layer=2)
    return avoid(out, 'splash')


def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = (f'<g transform="translate(70 940) scale(.62)">{towel(260, 330, 300, 150, rot=-8, hand=False)}</g>'
                + hand_shower(250, 1010, .5, rot=-40, stream=False, hose=True))
        return cta_end(ctx, mini_art=mini, tag_y=1000, tag_x=W - MX - 520)
    art, html = '', ''
    if s == 1:
        art = (shower_head(330, 770, 1.1) + water(330, 910, n=8, length=290, angle=74, seed=3, width=26)
               + small_head(600, 1180, r=150)
               + drops([(860, 1010), (930, 1150), (800, 1250), (230, 1150), (160, 1020), (990, 900)], r=18))
        html = hook_box(ctx, G, y=MT - 20, size=90, w=920,
                        breaks=('شعره ',), keep=('وهو يصيح', 'وتطلعي من الحمام', 'وأنتي اللي مبلولة', 'أكثر منه؟'))
    elif s == 2:
        # splashing everywhere: the stream hits the head and bounces off it
        art = (shower_head(330, 715, .95) + water(330, 835, n=7, length=300, angle=73, seed=8, width=24)
               + small_head(560, 1190, r=165) + splash(560, 1190, 165)
               + drops([(150, 900), (230, 1070), (130, 1230), (870, 880), (960, 1010), (900, 1180), (770, 960), (1000, 1280)], r=19))
        html = body_box(ctx, G, y=MT)
    elif s == 3:
        # the promise: the three tools lined up big on a torn pearl shelf
        art = avoid(torn_rect(90, 1110, 900, 40, C['pearl'], T, sides='tb', seed=12, layer=1), 'shelf')
        art += towel(800, 1035, 300, 150, rot=-3, hand=False)
        art += counting(620, 950, n=10, lit=10, r=27, gap=66)
        art += hand_shower(220, 760, .95, rot=-8, stream=False, hose=False)
        html = body_box(ctx, G, y=MT + 60)
    elif s == 4:
        art = towel_eyes(400, 1170, 150) + small_head(400, 1170, r=150, foam=True)
        html = body_box(ctx, G) + soft_cta(ctx, y=670)
    elif s == 5:
        # water cut at ten: the stream stops, ten gold discs counted out
        art = (shower_head(270, 745, .9) + water(270, 860, n=6, length=330, angle=80, seed=14, gaps=True, width=24)
               + drops([(300, 1030), (250, 1110), (330, 1190)], r=16)
               + counting(900, 990, n=10, lit=10, r=38, gap=92)
               + avoid(torn_circle(900 - 4 * 92, 1082, 56, C['gold'], T, seed=91, layer=1), 'stop'))
        html = body_box(ctx, G)
    elif s == 6:
        # the small hand holds the hand shower; the stream is short and gentle
        art = (small_head(720, 1215, r=135, foam=False)
               + hand_shower(430, 860, 1.05, rot=148, stream=True, seed=21, hand=True, hose=False, n_stream=5, L=230))
        html = body_box(ctx, G)
    elif s == 7:
        # the three tools together, a little cascade from top-left, and a dry pearl sleeve
        art = (hand_shower(200, 760, .82, rot=-12, stream=False, hose=False)
               + counting(600, 900, n=10, lit=10, r=26, gap=62)
               + towel(790, 1090, 320, 160, rot=-5, hand=False)
               + sleeve(1060, 1260, rot=-165, wet=False))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
