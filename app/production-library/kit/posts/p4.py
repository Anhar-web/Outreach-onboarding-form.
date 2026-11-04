"""p4 plate. Deep ground, dark. Top-down flat-lay, geometric only (no realistic food).

Motif: a 640px pearl plate seen from straight above. On it: four gold nugget
blobs with sandLight dots, seven gold fry bars, a gold toast square with a
goldDeep crust. An empty 200px pearl dish waits beside it.
s1: hook 92px pearl top-right; the plate is cropped low, the empty dish beside.
s2: the whole plate; three deep dashed threads join the three foods (what joins them?).
s3: close in, a torn teal ring round the gold food (crunchy, golden).
s4: the food turns deep with one pearl brand band each; pearl frost flakes round it (brand / cold).
s5: the small dish moves to centre stage with a goldDeep falafel disc in it.
s6: plate and dish side by side, a clear gap between them.
s7: attention end: quiet line centred; one accent, the dish with the falafel.
"""
import math
import random
from kit import (C, MX, MT, W, H, paper, torn_ring, torn_strip, text_box, avoid, keep_in)

TONE = 'd'


# ---------------------------------------------------------------- geometry
def blob_path(cx, cy, rx, ry, seed, n=9, jit=.16):
    """Smooth irregular closed blob (Catmull-Rom -> cubic Bezier)."""
    rng = random.Random(seed)
    pts = []
    for k in range(n):
        a = 2 * math.pi * k / n
        f = 1 + rng.uniform(-jit, jit)
        pts.append((cx + rx * f * math.cos(a), cy + ry * f * math.sin(a)))
    d = f'M {pts[0][0]:.1f} {pts[0][1]:.1f} '
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f'C {c1[0]:.1f} {c1[1]:.1f}, {c2[0]:.1f} {c2[1]:.1f}, {p2[0]:.1f} {p2[1]:.1f} '
    return d + 'Z'


# food positions on a plate of radius 320 (local, centre = 0,0)
NUGGETS = [(-150, -80, 62, 50, 3), (-60, -150, 58, 48, 4), (-170, 40, 56, 46, 5), (-70, -40, 60, 50, 6)]
FRIES = [(70 + k * 30, -175 + (k % 3) * 14, 130 + (k % 2) * 22, -14 + k * 4) for k in range(7)]
TOAST = (40, 95, 170, 9)


def food(scheme='gold', T=''):
    """The three foods in local coords. scheme: gold (as he eats them) or brand
    (deep wrappers with one identical pearl band = the brand that never changes)."""
    main = C['gold'] if scheme == 'gold' else C['deep']
    dark = C['goldDeep'] if scheme == 'gold' else C['night']
    dotc = C['sandLight'] if scheme == 'gold' else C['pearl']
    out = ''
    # fries: rounded bars, slightly fanned
    fr = ''
    for k, (x, y, h, rot) in enumerate(FRIES):
        fr += (f'<rect x="{x}" y="{y}" width="26" height="{h}" rx="8" fill="{main}" transform="rotate({rot} {x + 13} {y + h / 2})"/>'
               f'<rect x="{x + 3}" y="{y + 8}" width="5" height="{h - 16}" rx="2" fill="{dark}" fill-opacity=".35" transform="rotate({rot} {x + 13} {y + h / 2})"/>')
    if scheme != 'gold':
        fr += f'<rect x="60" y="-110" width="250" height="36" rx="6" fill="{C["pearl"]}" transform="rotate(4 185 -92)"/>'
    out += paper(fr, TONE, 2, T=T)
    # toast: goldDeep crust square, gold crumb inset
    tx, ty, ts, tr = TOAST
    t = (f'<g transform="rotate({tr} {tx} {ty})"><rect x="{tx - ts / 2}" y="{ty - ts / 2}" width="{ts}" height="{ts}" rx="26" fill="{dark}"/>'
         f'<rect x="{tx - ts / 2 + 16}" y="{ty - ts / 2 + 16}" width="{ts - 32}" height="{ts - 32}" rx="16" fill="{main}"/>')
    if scheme != 'gold':
        t += f'<rect x="{tx - ts / 2}" y="{ty - 18}" width="{ts}" height="36" fill="{C["pearl"]}"/>'
    else:
        t += ''.join(f'<circle cx="{tx + dx}" cy="{ty + dy}" r="4" fill="{C["goldDeep"]}" fill-opacity=".5"/>'
                     for dx, dy in ((-30, -25), (20, -30), (-10, 10), (30, 25), (-35, 30)))
    out += paper(t + '</g>', TONE, 2, T=T)
    # nuggets: blobs with dots
    for k, (x, y, rx, ry, seed) in enumerate(NUGGETS):
        dots = ''.join(f'<circle cx="{x + dx * rx:.1f}" cy="{y + dy * ry:.1f}" r="4.5" fill="{dotc}"/>'
                       for dx, dy in ((-.4, -.3), (.2, -.45), (.45, .1), (-.1, .35), (-.5, .2), (.1, -.05)))
        band = (f'<rect x="{x - rx * .95:.1f}" y="{y - 9:.1f}" width="{rx * 1.9:.1f}" height="18" fill="{C["pearl"]}"/>'
                if scheme != 'gold' else '')
        out += paper(f'<path d="{blob_path(x, y, rx, ry, seed)}" fill="{main}"/>' + (dots if scheme == 'gold' else band), TONE, 3, T=T)
    return out


def plate(cx, cy, R=320, scheme='gold', ring=False, links=False, empty=False, seed=0):
    s = R / 320
    T = f'translate({cx} {cy}) scale({s})'
    o = paper(f'<circle cx="0" cy="0" r="320" fill="{C["pearl"]}"/>'
              f'<circle cx="0" cy="0" r="262" fill="none" stroke="{C["sandLight"]}" stroke-width="6"/>'
              f'<circle cx="0" cy="0" r="300" fill="none" stroke="{C["tealMist"]}" stroke-opacity=".8" stroke-width="3"/>', TONE, 1, T=T)
    if not empty:
        o += food(scheme, T)
    if links:
        # deep dashed threads joining the three foods: what do they have in common?
        a, b, c = (-115, -75), (170, -95), (40, 95)
        d = f'M {a[0]} {a[1]} L {b[0]} {b[1]} L {c[0]} {c[1]} Z'
        o += paper(f'<path d="{d}" fill="none" stroke="{C["deep"]}" stroke-width="7" stroke-linecap="round" stroke-dasharray="2 20"/>'
                   + ''.join(f'<circle cx="{x}" cy="{y}" r="16" fill="{C["deep"]}"/><circle cx="{x}" cy="{y}" r="7" fill="{C["gold"]}"/>' for x, y in (a, b, c)),
                   TONE, 3, 't', T=T)
    if ring:
        o += torn_ring(0, 0, 286, 252, C['teal'], TONE, seed=seed + 41, layer=3, amp=(4, 9), T=T)
    return avoid(o, 'plate')


def dish(cx, cy, r=100, falafel=False, seed=0):
    s = r / 100
    T = f'translate({cx} {cy}) scale({s})'
    o = paper(f'<circle cx="0" cy="0" r="100" fill="{C["pearl"]}"/>'
              f'<circle cx="0" cy="0" r="74" fill="none" stroke="{C["sandLight"]}" stroke-width="5"/>', TONE, 1, T=T)
    if falafel:
        rng = random.Random(seed + 7)
        specks = ''
        for _ in range(16):
            a, rr = rng.uniform(0, 2 * math.pi), rng.uniform(8, 38)
            specks += (f'<ellipse cx="{rr * math.cos(a):.1f}" cy="{rr * math.sin(a):.1f}" rx="3.2" ry="1.8" '
                       f'transform="rotate({rng.uniform(0, 180):.0f} {rr * math.cos(a):.1f} {rr * math.sin(a):.1f})" fill="{C["sandLight"]}"/>')
        o += paper(f'<path d="{blob_path(0, 0, 50, 48, seed + 3, n=10, jit=.06)}" fill="{C["goldDeep"]}"/>'
                   f'<path d="{blob_path(-4, -4, 34, 32, seed + 5, n=8, jit=.1)}" fill="{C["ink"]}" fill-opacity=".18"/>{specks}',
                   TONE, 2, T=T)
    return avoid(o, 'dish')


def flakes(pts, s=1.0):
    """Pearl frost flakes: six-armed cut stars."""
    out = ''
    for k, (x, y, r) in enumerate(pts):
        r *= s
        w = max(8, r * .2)
        arm = (f'<rect x="{-w / 2:.1f}" y="{-r:.1f}" width="{w:.1f}" height="{2 * r:.1f}" rx="{w / 2:.1f}"/>'
               # a short V twig near each tip
               + ''.join(f'<rect x="{-w * .4:.1f}" y="{sgn * r * .62 - r * .2:.1f}" width="{w * .8:.1f}" height="{r * .4:.1f}" rx="{w * .4:.1f}" '
                         f'transform="rotate({tw} 0 {sgn * r * .55:.1f})"/>' for sgn in (-1, 1) for tw in (40, -40)))
        star = ''.join(f'<g transform="rotate({a})">{arm}</g>' for a in (0, 60, 120))
        out += paper(f'<g transform="translate({x} {y}) rotate({k * 13})" fill="{C["pearl"]}">{star}'
                     f'<circle r="{w * .9:.1f}" fill="{C["tealMist"]}"/></g>', TONE, 2)
    return avoid(out, 'flakes')


# ---------------------------------------------------------------- slides
BREAKS = {
    1: ['تطبخي للبيت كله،', 'وهو له صحن لحاله', 'فيه نفس الثلاث أكلات', 'كل يوم؟'],
    2: ['قبل ما تجربي أكل جديد،', 'لاحظي ايش يجمع', 'الأكلات الثلاث اللي ياكلها.'],
    3: ['إذا صحنه نقت وبطاطس وتوست،', 'كلها مقرمشة ولونها ذهبي.'],
    4: ['ومرات اللي يجمعها', 'ماركة وحدة ما تتغير،', 'أو إنها لازم تكون باردة.'],
    5: ['ولما تلاحظي الشي المشترك،', 'اختاري أكلة وحدة من السفرة', 'فيها نفس الشي.', 'حبة فلافل،', 'أو قطعة تميس.'],
    6: ['لا تحطيها داخل صحنه،', 'ولا تطلبي منه يذوقها.', 'حطيها في صحن صغير جمب صحنه،', 'وخليها بدون ما تقولي شي.'],
    7: ['إذا لمسها أو شمها،', 'هذا يكفي اليوم.', 'وبكرة حطي نفس الأكلة،', 'في نفس الصحن الصغير،', 'جمب صحنه.'],
}


def body(ctx, y=MT + 40, w=888):
    return text_box(ctx.t.body(), W - MX - w, y, w, 'pearl')


def slide(ctx):
    s = ctx.s
    if s in BREAKS:
        keep_in(ctx.t.segs, *[p for p in BREAKS[s] if any(p in g.text for g in ctx.t.segs)])
    r = {'ground': 'deep'}

    if s == 1:
        # cropped low: only the top of his plate shows; the empty dish waits beside it
        art = plate(600, 1190, 320) + dish(185, 975, 100)
        r.update(art=art, html=text_box(ctx.t.body(), MX, MT, W - 2 * MX, 'pearl', size={'hook': 92}))

    elif s == 2:
        r.update(art=plate(540, 930, 320, links=True), html=body(ctx))

    elif s == 3:
        # close in, plate bleeding off the right: crunchy and golden, ringed in teal
        r.update(art=plate(640, 960, 400, ring=True, seed=3), html=body(ctx), dots_theme='light')

    elif s == 4:
        art = (plate(460, 900, 320, scheme='brand')
               + flakes([(895, 690, 52), (955, 940, 36), (860, 1150, 44), (150, 1250, 30)]))
        r.update(art=art, html=body(ctx))

    elif s == 5:
        # the dish is the star now: one food from the family table, same thing in common
        art = plate(1010, 960, 320) + dish(420, 900, 200, falafel=True, seed=5)
        r.update(art=art, html=body(ctx))

    elif s == 6:
        # beside his plate, not on it: a clear gap between the two
        art = plate(690, 960, 300) + dish(190, 1000, 110, falafel=True, seed=6)
        r.update(art=art, html=body(ctx, y=MT + 20))

    else:
        for g in ctx.t.body():
            g.role = 'quiet'
        art = dish(540, 1100, 120, falafel=True, seed=7)
        r.update(art=art, html=text_box(ctx.t.body(), MX, 250, W - 2 * MX, 'pearl', align='center'))
    return r
