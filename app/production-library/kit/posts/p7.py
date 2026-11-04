"""p7 iPad. Split frame with a torn seam: deep (plate side, left) + tealMist (iPad side, right).
Conversion post.

s1: diagonal torn seam. Question over the iPad (ink, 96px, on tealMist); the
    clause «جهزي...» over the plate (pearl, 54px, on deep).
Inner slides: the seam turns horizontal and the tealMist side shrinks to a band at
    the bottom while the plate side (deep) grows. s4 (split in two, red flag): a deep
    shower-head crossed by a torn gold strip, in the band.
s6 (red flag) is split at its middle "\\n": s6a widens to the bigger picture
    (four tiles), s6b is the conversion end (gold, pearl tag = «الرابط في البايو.»).
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


def plate(cx, cy, r, tone=D, biscuits=4, crumbs=False, layer=1, seed=0):
    """Gold concentric plate with sandLight biscuits."""
    p = (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["gold"]}"/>'
         f'<circle cx="{cx}" cy="{cy}" r="{r * .74}" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".55" stroke-width="{max(3, r * .025):.1f}"/>'
         f'<circle cx="{cx}" cy="{cy}" r="{r * .9}" fill="none" stroke="{C["pearl"]}" stroke-opacity=".28" stroke-width="{max(2, r * .015):.1f}"/>')
    out = paper(p, tone, layer)
    spots = [(-.3, -.26), (.3, -.22), (-.24, .3), (.32, .28)][:biscuits]
    br = r * .25
    for k, (dx, dy) in enumerate(spots):
        bx, by = cx + dx * r, cy + dy * r
        dots = ''.join(f'<circle cx="{bx + ox * br * .42:.1f}" cy="{by + oy * br * .42:.1f}" r="{br * .08:.1f}" fill="{C["goldDeep"]}"/>'
                       for ox, oy in ((-1, -1), (1, -1), (-1, 1), (1, 1), (0, 0)))
        out += paper(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="{br:.1f}" fill="{C["sandLight"]}"/>{dots}', tone, layer + 1)
    if crumbs:
        cr = ''.join(f'<circle cx="{cx + r * dx:.1f}" cy="{cy + r * dy:.1f}" r="{r * .035:.1f}" fill="{C["sandLight"]}"/>'
                     for dx, dy in ((-.2, .1), (.15, -.3), (.32, .18), (-.05, .38), (-.4, -.12)))
        out += paper(cr, tone, layer + 1, 't')
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
    cx, cy = x + s / 2, y + s / 2
    return (f'<circle cx="{cx}" cy="{cy}" r="{s * .3}" fill="{C["deep"]}"/><circle cx="{cx}" cy="{cy}" r="{s * .18}" fill="{C["tealMist"]}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{s * .1}" fill="{C["gold"]}"/>')


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
        art = (band(800) + shower(770, 1060, .95, L, seed=5)
               + ipad(260, 1060, 230, 300, -14, L, on=False, layer=1))
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
        mini = (torn_poly([(150, 1010), (330, 1010), (330, 1240), (110, 1240)], C['tealMist'], L, torn=[3], seed=71)
                + ipad(250, 1125, 95, 130, -7, L, on=True) + plate(130, 1175, 58, L))
        art = mini
        html = (text_box(segs[:-1], MX, 260, W - 2 * MX, 'ink')
                + conversion_tag(cta, 300, 700, rot=-3))
        r.update(ground='gold', art=art, html=html, dots_theme='gold')
    return r
