"""p7 iPad. Split frame with a torn seam: deep (plate side, left) + tealMist (iPad side, right).
Conversion post.

s1: diagonal torn seam. Question over the iPad (ink, 96px, on tealMist); the
    clause «جهزي...» over the plate (pearl, 54px, on deep).
Inner slides: the seam turns horizontal and the tealMist side shrinks to a band at
    the bottom while the plate side (deep) grows. The "plate" is p7's own motif: a
    rectangular tealDeep tray with square scalloped tea biscuits, set at an angle
    (p4 owns the round pearl plate). s4 (split in two, red flag): s4a the rule: tray
    yes, shower crossed by a torn gold strip; s4b the scene: iPad off, then straight
    to the shower (not crossed): two gold protest bursts = a second reason to object.
s6 (red flag) is split at its middle "\\n": s6a widens to the bigger picture
    (four tiles), s6b is the conversion end (gold, pearl tag = «الرابط في البايو.»), mini motif = the tray only.
"""
import math
from kit import (C, MX, MT, W, H, paper, torn_rect, torn_poly, torn_strip, torn_circle, glow,
                 text_box, step_tab, avoid, keep_in, conversion_tag, P)

D, L = 'd', 'l'   # shadow sets: on deep vs on tealMist / gold


# ---------------------------------------------------------------- motifs
def ipad(cx, cy, w, h, rot, tone=L, on=True, layer=1):
    tf = f'rotate({rot} {cx} {cy})'
    x, y = cx - w / 2, cy - h / 2
    g = ''
    if on:  # two-layer teal glow
        g = (glow(f'<rect x="{x - 40}" y="{y - 40}" width="{w + 80}" height="{h + 80}" rx="60" fill="{C["teal"]}" fill-opacity=".55" transform="{tf}"/>', 'l')
             + glow(f'<rect x="{x - 8}" y="{y - 8}" width="{w + 16}" height="{h + 16}" rx="36" fill="{C["teal"]}" fill-opacity=".8" transform="{tf}"/>', 's'))
    screen = C['teal'] if on else C['night']
    shine = (f'<polygon points="{x + 24},{y + h * .55} {x + w * .55},{y + 24} {x + w * .78},{y + 24} {x + 24},{y + h * .78}" fill="{C["pearl"]}" fill-opacity=".14"/>'
             if on else '')
    body = (f'<g transform="{tf}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="28" fill="{C["deep"]}"/>'
            f'<rect x="{x + 22}" y="{y + 22}" width="{w - 44}" height="{h - 44}" rx="12" fill="{screen}"/>{shine}'
            f'<circle cx="{cx}" cy="{y + 11}" r="4" fill="{C["pearl"]}" fill-opacity=".6"/></g>')
    return avoid(g + paper(body, tone, layer), 'ipad')


def biscuit(bx, by, b, rot=0):
    """Square tea biscuit: sandLight with a scalloped edge and a 3x3 grid of goldDeep docker holes."""
    k = 5                                   # scallops per side
    step = b / k
    sc = ''.join(f'<circle cx="{bx - b / 2 + step * (i + .5):.1f}" cy="{by + sy * b / 2:.1f}" r="{step * .55:.1f}"/>'
                 f'<circle cx="{bx + sy * b / 2:.1f}" cy="{by - b / 2 + step * (i + .5):.1f}" r="{step * .55:.1f}"/>'
                 for i in range(k) for sy in (-1, 1))
    holes = ''.join(f'<circle cx="{bx + ox * b * .26:.1f}" cy="{by + oy * b * .26:.1f}" r="{max(1.6, b * .035):.1f}" fill="{C["goldDeep"]}"/>'
                    for ox in (-1, 0, 1) for oy in (-1, 0, 1))
    return (f'<g transform="rotate({rot} {bx:.1f} {by:.1f})"><g fill="{C["sandLight"]}">'
            f'<rect x="{bx - b / 2:.1f}" y="{by - b / 2:.1f}" width="{b:.1f}" height="{b:.1f}"/>{sc}</g>{holes}</g>')


def plate(cx, cy, r, tone=D, biscuits=4, crumbs=False, layer=1, seed=0, rot=-10):
    """The biscuit tray (p7's own motif; p4 owns the round plate): a rectangular
    tealDeep tray with a pearl inner line and slotted handles, set at an angle,
    holding square scalloped tea biscuits in a row. r = half the tray width."""
    w, h = 2 * r, r * 1.3
    x, y = cx - w / 2, cy - h / 2
    T = f'rotate({rot} {cx} {cy})'
    hw = r * .16                            # handle depth
    tray = (f'<rect x="{x - hw:.1f}" y="{cy - h * .22:.1f}" width="{w + 2 * hw:.1f}" height="{h * .44:.1f}" rx="{hw * .7:.1f}" fill="{C["tealDeep"]}"/>'
            f'<rect x="{x - hw * .62:.1f}" y="{cy - h * .12:.1f}" width="{hw * .34:.1f}" height="{h * .24:.1f}" rx="{hw * .17:.1f}" fill="{C["night"]}"/>'
            f'<rect x="{x + w + hw * .28:.1f}" y="{cy - h * .12:.1f}" width="{hw * .34:.1f}" height="{h * .24:.1f}" rx="{hw * .17:.1f}" fill="{C["night"]}"/>'
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r * .08:.1f}" fill="{C["tealDeep"]}"/>'
            f'<rect x="{x + r * .09:.1f}" y="{y + r * .09:.1f}" width="{w - r * .18:.1f}" height="{h - r * .18:.1f}" rx="{r * .04:.1f}" '
            f'fill="none" stroke="{C["pearl"]}" stroke-opacity=".75" stroke-width="{max(2.5, r * .022):.1f}"/>')
    out = paper(tray, tone, layer, T=T)
    b = r * .36
    spots = [(-.58, -.16, -8), (-.14, .2, 6), (.28, -.2, -4), (.66, .18, 11)][:biscuits]
    bis = ''.join(biscuit(cx + dx * r, cy + dy * r, b, br) for dx, dy, br in spots)
    if bis:
        out += paper(bis, tone, layer + 1, T=T)
    if crumbs:
        cr = ''.join(f'<rect x="{cx + r * dx:.1f}" y="{cy + r * dy:.1f}" width="{r * .06:.1f}" height="{r * .05:.1f}" '
                     f'transform="rotate({a} {cx + r * dx:.1f} {cy + r * dy:.1f})" fill="{C["sandLight"]}"/>'
                     for dx, dy, a in ((-.5, .1, 20), (.15, -.3, -30), (.62, .18, 45), (-.05, .32, 10), (-.7, -.22, -15), (.4, -.05, 60)))
        out += paper(cr, tone, layer + 1, 't', T=T)
    return avoid(out, 'plate')


def toys(x, y, s=1.0, tone=D):
    a = torn_rect(x, y, 110 * s, 110 * s, C['teal'], tone, 'tblr', seed=41, layer=1, rot=-8, amp=(3, 6))
    b = torn_rect(x + 120 * s, y + 30 * s, 90 * s, 90 * s, C['pearl'], tone, 'tblr', seed=42, layer=1, rot=6, amp=(3, 6))
    c = paper(f'<circle cx="{x + 70 * s}" cy="{y - 40 * s}" r="{48 * s}" fill="{C["gold"]}"/>'
              f'<path d="M {x + 22 * s} {y - 40 * s} Q {x + 70 * s} {y - 70 * s} {x + 118 * s} {y - 40 * s}" fill="none" stroke="{C["goldDeep"]}" stroke-width="{5 * s}"/>', tone, 2)
    return avoid(a + b + c, 'toys')


def shower(cx, cy, s=1.0, tone=L, crossed=True, seed=0):
    """Deep shower-head on its arm, teal drops, crossed by a torn gold strip."""
    arm = paper(f'<path d="M {cx + 260 * s} {cy - 230 * s} L {cx + 120 * s} {cy - 230 * s} Q {cx + 40 * s} {cy - 230 * s} {cx + 22 * s} {cy - 70 * s}" '
                f'fill="none" stroke="{C["deep"]}" stroke-width="{34 * s}" stroke-linecap="round"/>', tone, 1)
    head = (f'<path d="M {cx - 120 * s} {cy} Q {cx} {cy - 170 * s} {cx + 120 * s} {cy} Z" fill="{C["deep"]}"/>'
            f'<rect x="{cx - 130 * s}" y="{cy - 6 * s}" width="{260 * s}" height="{24 * s}" rx="{10 * s}" fill="{C["deep"]}"/>')
    holes = ''.join(f'<circle cx="{cx + k * 34 * s}" cy="{cy + 6 * s}" r="{5 * s}" fill="{C["tealMist"]}"/>' for k in range(-3, 4))
    drops = ''.join(f'<path d="M {cx + dx * s} {cy + dy * s} q {-12 * s} {22 * s} 0 {30 * s} q {12 * s} {-8 * s} 0 {-30 * s} Z" fill="{C["teal"]}"/>'
                    for dx, dy in ((-90, 60), (-30, 90), (30, 55), (90, 85), (-60, 150), (60, 140)))
    out = arm + paper(head + holes, tone, 2) + paper(drops, tone, 1, 't')
    if crossed:
        out += torn_strip([(cx - 210 * s, cy - 170 * s), (cx + 210 * s, cy + 190 * s)], 54 * s, C['gold'], tone, seed=seed + 61, layer=3)
    return avoid(out, 'shower')


def burst(cx, cy, r, tone=L, seed=0):
    """A jagged gold 'protest' burst (torn star), one per objection."""
    import random
    rng = random.Random(seed + 90)
    n = 11
    pts = []
    for k in range(2 * n):
        a = math.pi * k / n + rng.uniform(-.08, .08)
        rr = r * (1 if k % 2 == 0 else .52) * rng.uniform(.88, 1.08)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return torn_poly(pts, C['gold'], tone, seed=seed + 7, layer=3, amp=(2, 4))


def band(y0, tilt=18, seed=7):
    """The tealMist (iPad) side as a bottom band with a torn top edge."""
    return torn_poly([(-30, y0 + tilt), (1110, y0 - tilt), (1110, 1380), (-30, 1380)], C['tealMist'], D, torn=[0], seed=seed)


def tile(x, y, s, icon, seed):
    return torn_rect(x, y, s, s, C['tealMist'], D, 'tblr', seed=seed, layer=1, amp=(4, 8), inner=icon)


def icon_ipad(x, y, s):
    return (f'<rect x="{x + s * .27}" y="{y + s * .18}" width="{s * .46}" height="{s * .64}" rx="{s * .06}" fill="{C["deep"]}"/>'
            f'<rect x="{x + s * .31}" y="{y + s * .23}" width="{s * .38}" height="{s * .54}" rx="{s * .03}" fill="{C["teal"]}"/>')


def icon_moon(x, y, s):
    cx, cy, r = x + s / 2, y + s / 2, s * .28
    return f'<path d="M {cx} {cy - r} A {r} {r} 0 1 0 {cx} {cy + r} A {r * .62} {r} 0 1 1 {cx} {cy - r} Z" fill="{C["deep"]}"/>'


def icon_plate(x, y, s):
    """The tray, as a flat icon: deep tray, two sandLight square biscuits."""
    cx, cy = x + s / 2, y + s / 2
    return (f'<g transform="rotate(-10 {cx} {cy})"><rect x="{cx - s * .34}" y="{cy - s * .22}" width="{s * .68}" height="{s * .44}" rx="{s * .04}" fill="{C["deep"]}"/>'
            f'<rect x="{cx - s * .4}" y="{cy - s * .08}" width="{s * .8}" height="{s * .16}" rx="{s * .05}" fill="{C["deep"]}"/>'
            f'<rect x="{cx - s * .24}" y="{cy - s * .1}" width="{s * .2}" height="{s * .2}" fill="{C["sandLight"]}"/>'
            f'<rect x="{cx + s * .04}" y="{cy - s * .1}" width="{s * .2}" height="{s * .2}" fill="{C["sandLight"]}"/></g>')


def icon_door(x, y, s):
    return (f'<rect x="{x + s * .3}" y="{y + s * .18}" width="{s * .4}" height="{s * .66}" fill="{C["deep"]}"/>'
            f'<polygon points="{x + s * .3},{y + s * .18} {x + s * .5},{y + s * .26} {x + s * .5},{y + s * .9} {x + s * .3},{y + s * .84}" fill="{C["gold"]}"/>')


# ---------------------------------------------------------------- slides
BREAKS = {
    1: ['تسحبي الآيباد', 'ويبدأ الصراخ؟', 'جهزي اللي بعده', 'قبل ما تسحبيه.'],
    2: ['تسحبيه، فيصرخ', 'ويحاول ياخذه،', 'وكل شي تعطيه بعدها', 'يقابله بـ لا.'],
    3: ['قبل ما تسحبيه،', 'جهزي له شي ينتقل له على طول.', 'صحن بسكوت على الطاولة،', 'أو العاب جاهزة على الأرض جنبه.'],
    4: ['بس لا تخلي اللي بعده', 'شي دايما يرفضه.', 'تسحبي الآيباد،', 'وعلى طول تقولي يلا شاور؟', 'كذا صار قدامه', 'سبب ثاني يعترض عليه.'],
    5: ['وبعد ما تخلصوا،', 'رجعي الآيباد مكانه.', 'لا تتركيه قدامه', 'على الطاولة.'],
    6: ['والموضوع مو بس الآيباد.', 'فيه مواقف تتكرر', 'وقت النوم والأكل والطلعات وغيرها.',
        'التقييم المجاني يساعدك', 'تشوفي الصورة الأكبر', 'وتحددي أول خطوة.'],
}


def body_text(ctx, y, w=888, color='pearl'):
    return text_box(ctx.t.body(), W - MX - w, y, w, color)


def slide(ctx):
    s, part = ctx.s, ctx.part
    if s == 1:   # the hook is two sentences: question (big) + clause (small)
        q, clause = ctx.t.split_seg(ctx.t.body()[0], '؟ ')
        clause.role = 'clause'
    if s in BREAKS:
        keep_in(ctx.t.segs, *[p for p in BREAKS[s] if any(p in g.text for g in ctx.t.segs)])
    r = {'ground': 'deep', 'dots_theme': 'light'}

    if s == 1:
        seam = torn_poly([(340, -30), (1110, -30), (1110, 1380), (640, 1380)], C['tealMist'], D, torn=[3], seed=3)
        art = seam + ipad(820, 900, 380, 520, -7, L) + plate(250, 1110, 205, D)
        html = (text_box([q], 384, MT, 1080 - MX - 384, 'ink')
                + text_box([clause], MX, 590, 372, 'pearl'))
        r.update(art=art, html=html)

    elif s == 2:
        # he grabs, everything after meets "no": the iPad is yanked out of the band, plate pushed aside
        art = (band(1030) + ipad(860, 1150, 260, 340, 24, L, on=True)
               + plate(220, 860, 120, D, biscuits=0, seed=2))
        r.update(art=art, html=body_text(ctx, MT + 60))

    elif s == 3:
        # get the next thing ready: plate of biscuits grows, toys on the floor, iPad still on
        art = (band(1080) + ipad(880, 1220, 200, 260, -10, L, on=True)
               + plate(330, 800, 200, D) + toys(640, 820, 1.0, D))
        r.update(art=art, html=body_text(ctx, MT + 40))

    elif s == 4 and part == 1:
        art = band(860) + shower(770, 1100, .85, L, seed=4) + plate(210, 640, 130, D, biscuits=4)
        r.update(art=art, html=body_text(ctx, 300, w=620))

    elif s == 4 and part == 2:
        ctx.t.body()[0].role = 'lead'      # stands alone after the split: set it as the slide's lead
        # the scene, not the rule again: iPad off, then straight to the shower (not crossed
        # this time): two objects, two gold protest bursts = «سبب ثاني يعترض عليه»
        art = (band(800) + shower(780, 1070, .85, L, crossed=False, seed=5)
               + ipad(270, 1080, 230, 300, -14, L, on=False, layer=1)
               + avoid(burst(395, 905, 80, L, seed=1) + burst(935, 860, 80, L, seed=2), 'bursts'))
        r.update(art=art, html=body_text(ctx, MT + 40))

    elif s == 5:
        # put it back in its place: iPad upright in a gold stand in the band; plate eaten
        stand = paper(f'<path d="M 700 1250 L 920 1250 L 900 1200 L 720 1200 Z" fill="{C["gold"]}"/>', L, 2)
        art = (band(1000) + ipad(810, 1060, 190, 260, 0, L, on=False) + stand
               + plate(300, 800, 190, D, biscuits=0, crumbs=True))
        r.update(art=art, html=body_text(ctx, MT + 40))

    elif s == 6 and part == 1:
        # the bigger picture: four torn tiles, the iPad is only one of them
        sz, gap = 196, 34
        x0 = MX
        icons = [icon_door, icon_plate, icon_moon, icon_ipad]   # RTL: iPad first on the right
        art = avoid(''.join(tile(x0 + k * (sz + gap), 780 + (k % 2) * 40, sz, icons[k](x0 + k * (sz + gap), 780 + (k % 2) * 40, sz), 50 + k)
                            for k in range(4)), 'tiles')
        r.update(art=art, html=body_text(ctx, MT + 140), dots_theme='dark')

    else:
        # conversion end: gold ground, ink text, pearl torn tag with the CTA, mini motif bottom-left
        segs = ctx.t.body()
        cta = segs[-1]
        assert cta.text == ctx.cta_text(), (cta.text, ctx.cta_text())
        segs[0].role = 'lead'
        # one focal motif only: the biscuit tray (the iPad stays out of the end)
        mini = plate(215, 1130, 120, L, biscuits=4, rot=-8)
        art = mini
        html = (text_box(segs[:-1], MX, 260, W - 2 * MX, 'ink')
                + conversion_tag(cta, 300, 700, rot=-3))
        r.update(ground='gold', art=art, html=html, dots_theme='gold')
    return r
