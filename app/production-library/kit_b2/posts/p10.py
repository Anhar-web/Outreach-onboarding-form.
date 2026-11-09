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


def hand_shower(x, y, s=1.0, rot=-35, stream=True, seed=5):
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    body = paper(f'<rect x="-30" y="-20" width="60" height="230" rx="28" fill="{C["pearl"]}"/>'
                 f'<ellipse cx="0" cy="-40" rx="70" ry="50" fill="{C["gold"]}"/>'
                 + ''.join(f'<circle cx="{-36 + k * 18}" cy="-62" r="5" fill="{C["goldDeep"]}"/>' for k in range(5)), T, 2, T=tr)
    hand = paper(f'<g transform="{tr}"><path d="M -48 90 Q -60 160 -30 200 L 40 200 Q 60 150 48 90 Z" fill="{C["sandLight"]}"/></g>', T, 3)
    out = body + hand
    if stream:
        a = math.radians(rot - 90)
        for k in range(4):
            sx, sy = x + 70 * math.cos(a) + (k - 1.5) * 16, y + 70 * math.sin(a)
            ex, ey = sx + 160 * math.cos(a + .1 * (k - 1.5)), sy + 160 * math.sin(a + .1 * (k - 1.5))
            out += torn_strip([(sx, sy), (ex, ey)], 12, C['teal'], T, seed=seed + k, layer=2)
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


def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = (f'<g transform="translate(120 990) scale(.42)">{towel(300, 300, hand=False)}</g>'
                f'<g transform="translate(330 960) scale(.42)">{hand_shower(300, 300, rot=-20, stream=False)}</g>')
        return cta_end(ctx, mini_art=mini, tag_y=1020, tag_x=W - MX - 560)
    art, html = '', ''
    if s == 1:
        art = (shower_head(330, 740, 1.1) + water(330, 880, n=8, length=300, angle=74, seed=3, width=26)
               + small_head(600, 1170, r=150)
               + drops([(860, 1010, ), (930, 1150), (800, 1250), (230, 1150), (160, 1020), (990, 900)], r=18))
        html = hook_box(ctx, G, y=MT - 20, size=90, w=920,
                        breaks=('شعره ',), keep=('وهو يصيح', 'وتطلعي من الحمام', 'وأنتي اللي مبلولة', 'أكثر منه؟'))
    elif s == 2:
        # splashing everywhere: the water scatters
        art = (shower_head(240, 560, .8) + water(240, 660, n=6, length=330, angle=70, seed=8)
               + small_head(560, 1200, r=140)
               + drops([(160, 900), (280, 1030), (760, 960), (880, 1080), (680, 1250), (420, 900), (940, 900)], r=16))
        html = body_box(ctx, G, y=MT)
    elif s == 3:
        # the promise: three objects lined up on a shelf of torn pearl
        art = avoid(torn_rect(140, 1020, 800, 34, C['pearl'], T, sides='tb', seed=12, layer=1)
                    + towel(760, 940, 220, 110, rot=-3, hand=False)
                    + counting(560, 900, n=10, lit=10, r=16, gap=36)
                    + hand_shower(260, 900, .7, rot=-10, stream=False), 'shelf')
        html = body_box(ctx, G, y=MT + 60)
    elif s == 4:
        art = small_head(420, 1190, r=120, foam=True) + towel(420, 1110, 280, 100, rot=-4)
        html = body_box(ctx, G) + soft_cta(ctx, y=690)
    elif s == 5:
        art = (shower_head(260, 760, .7) + water(260, 850, n=6, length=330, angle=80, seed=14, gaps=True)
               + counting(880, 960, n=10, lit=10, r=30, gap=78))
        html = body_box(ctx, G)
    elif s == 6:
        art = small_head(650, 1200, r=130, foam=False) + hand_shower(330, 1000, 1.0, rot=-30, seed=21)
        html = body_box(ctx, G)
    elif s == 7:
        # the three tools together, and a dry pearl sleeve
        art = (towel(780, 1000, 240, 110, rot=-5, hand=False) + counting(560, 960, n=10, lit=10, r=18, gap=40)
               + hand_shower(250, 1010, .75, rot=-15, stream=False) + sleeve(1040, 1240, rot=-170, wet=False))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
