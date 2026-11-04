"""p6 shoes. Sunrise Gold ground (art_tokens override), ink text. One Big Object, centred radial.

Motif: a big clock: deep cut rim, sandLight face, deep ticks, ink hands. The
quarter-hour before 12 is a torn gold wedge (9 -> 12); small deep shoes sit at 12.
Time stands in for place: there is no room.
s1: question 88px ink top-right, clause 54px; the clock fills the lower 60%.
s2: no wedge yet: both hands snap to 12, shoes arrive, his play blocks scattered.
s3: the wedge tears into three (three things).
s4: close on the wedge: a deep iPad crossed by two torn gold strips.
s5: a cup of juice and a biscuit sit in the wedge.
s6: the shoes leave 12 and move down into the wedge (dashed path).
s7: conversion end: ink text, pearl tag, the clock at 25% bottom-left.
"""
import math
from kit import (C, MX, MT, W, H, paper, torn_poly, torn_strip, torn_rect, arc_pts,
                 text_box, avoid, keep_in, conversion_tag)

TONE = 'l'
GROUND = 'gold'


# ---------------------------------------------------------------- motifs
def polar(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def shoe(x, y, s=1.0, flip=False, rot=0):
    """Small side-view shoe (deep upper, pearl sole, gold strap). Toe points left
    unless flip. (x, y) = heel bottom."""
    sx = -1 if not flip else 1
    T = f'translate({x} {y}) rotate({rot}) scale({sx * s} {s})'
    return paper(f'<g transform="{T}">'
                 f'<path d="M 0 0 L 0 -62 Q 0 -78 18 -78 L 50 -78 Q 62 -50 92 -42 Q 150 -34 158 -8 L 158 0 Z" fill="{C["deep"]}"/>'
                 f'<rect x="-4" y="-6" width="166" height="18" rx="8" fill="{C["pearl"]}"/>'
                 f'<rect x="58" y="-60" width="16" height="44" rx="4" transform="rotate(28 66 -38)" fill="{C["gold"]}"/>'
                 f'</g>', TONE, 3)


def shoes(cx, cy, s=1.0, rot=0):
    """A pair, toes left, one slightly behind the other. (cx, cy) = centre of the soles."""
    return avoid(shoe(cx - 10 * s, cy - 6 * s, s * .92, rot=rot) + shoe(cx + 70 * s, cy + 6 * s, s, rot=rot), 'shoes')


def wedge(cx, cy, r, a0=180, a1=270, seed=1, fill=None, layer=2):
    n = max(6, int(abs(a1 - a0) / 6))
    pts = [(cx, cy)] + arc_pts(cx, cy, r, a0, a1, n=n)
    # the arc is torn, the two radii are clean cuts along the hands
    return torn_poly(pts, fill or C['gold'], TONE, torn=list(range(1, n + 1)), seed=seed, layer=layer)


def clock(cx, cy, R, wedge_parts=1, hands=(180, -97.5), ticks=True, seed=0, shoes_at=True, inside=''):
    """Deep rim, sandLight face, ticks, gold wedge(s) 9->12, ink hands.
    hands = (minute_deg, hour_deg) in SVG degrees (-90 = 12 o'clock)."""
    o = []
    o.append(paper(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{C["deep"]}"/>'
                   f'<circle cx="{cx}" cy="{cy}" r="{R * .97:.1f}" fill="none" stroke="{C["pearl"]}" stroke-opacity=".18" stroke-width="{R * .012:.1f}"/>',
                   TONE, 1))
    o.append(paper(f'<circle cx="{cx}" cy="{cy}" r="{R * .89:.1f}" fill="{C["sandLight"]}"/>', TONE, 2))
    rw = R * .82
    if wedge_parts == 1:
        o.append(wedge(cx, cy, rw, seed=seed + 5))
    elif wedge_parts == 3:
        for k, (a0, a1) in enumerate(((181, 208), (211, 239), (242, 269))):
            # each piece pulled a little out along its bisector: three separate torn sheets
            m = math.radians((a0 + a1) / 2)
            o.append(wedge(cx + 14 * math.cos(m), cy + 14 * math.sin(m), rw, a0, a1, seed=seed + 11 + k, layer=2 + (k == 1)))
    if ticks:
        t = ''
        for k in range(12):
            a = -90 + k * 30
            big = k % 3 == 0
            r0, r1 = R * (.72 if big else .77), R * .84
            x0, y0 = polar(cx, cy, r0, a)
            x1, y1 = polar(cx, cy, r1, a)
            t += (f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{C["deep"]}" '
                  f'stroke-width="{R * (.035 if big else .02):.1f}" stroke-linecap="round"/>')
        o.append(paper(t, TONE, 2, 't'))
    if shoes_at:
        # small pair parked just right of the 12
        k = R / 400 * .7
        o.append(shoes(cx + 30 + 168 * k, cy - R * .56, k))
    o.append(inside)
    if hands:
        mdeg, hdeg = hands
        mx, my = polar(cx, cy, R * .66, mdeg)
        hx, hy = polar(cx, cy, R * .44, hdeg)
        bx, by = polar(cx, cy, R * .12, mdeg + 180)
        o.append(paper(f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{mx:.1f}" y2="{my:.1f}" stroke="{C["ink"]}" stroke-width="{R * .04:.1f}" stroke-linecap="round"/>'
                       f'<line x1="{cx}" y1="{cy}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{C["ink"]}" stroke-width="{R * .065:.1f}" stroke-linecap="round"/>',
                       TONE, 3))
        o.append(paper(f'<circle cx="{cx}" cy="{cy}" r="{R * .06:.1f}" fill="{C["gold"]}"/>'
                       f'<circle cx="{cx}" cy="{cy}" r="{R * .022:.1f}" fill="{C["goldDeep"]}"/>', TONE, 3))
    return avoid(''.join(o), 'clock')


def ipad_crossed(cx, cy, s=1.0, rot=-8, seed=0):
    w, h = 230 * s, 300 * s
    x, y = cx - w / 2, cy - h / 2
    body = paper(f'<g transform="rotate({rot} {cx} {cy})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{24 * s}" fill="{C["deep"]}"/>'
                 f'<rect x="{x + 18 * s}" y="{y + 20 * s}" width="{w - 36 * s}" height="{h - 40 * s}" rx="{8 * s}" fill="{C["teal"]}"/>'
                 f'<polygon points="{x + 18 * s},{y + h * .5} {x + w * .55},{y + 20 * s} {x + w * .75},{y + 20 * s} {x + 18 * s},{y + h * .75}" fill="{C["pearl"]}" fill-opacity=".16"/></g>',
                 TONE, 3)
    d = 190 * s
    cross = (torn_strip([(cx - d, cy - d), (cx + d, cy + d)], 46 * s, C['gold'], TONE, seed=seed + 61, layer=3)
             + torn_strip([(cx + d, cy - d), (cx - d, cy + d)], 46 * s, C['gold'], TONE, seed=seed + 62, layer=3))
    return avoid(body + cross, 'ipad')


def cup(cx, cy, s=1.0):
    return paper(f'<g transform="translate({cx} {cy}) scale({s})">'
                 f'<path d="M -62 -80 L 62 -80 L 48 82 L -48 82 Z" fill="{C["pearl"]}"/>'
                 f'<path d="M -55 -18 L 55 -18 L 48 82 L -48 82 Z" fill="{C["teal"]}"/>'
                 f'<rect x="18" y="-140" width="16" height="130" rx="6" transform="rotate(14 26 -75)" fill="{C["deep"]}"/>'
                 f'</g>', TONE, 3)


def biscuit(cx, cy, r):
    dots = ''.join(f'<circle cx="{cx + dx * r:.1f}" cy="{cy + dy * r:.1f}" r="{r * .09:.1f}" fill="{C["goldDeep"]}"/>'
                   for dx, dy in ((-.4, -.3), (.35, -.35), (0, 0), (-.35, .38), (.4, .3)))
    return paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["sandLight"]}"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{r * .82:.1f}" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="3"/>{dots}',
                 TONE, 3)


def blocks(cx, cy, s=1.0):
    out = ''
    for k, (dx, dy, rot, col) in enumerate(((0, 0, -12, 'teal'), (110, 40, 18, 'deep'), (40, 120, 6, 'pearl'), (-70, 90, 30, 'goldDeep'))):
        out += torn_rect(cx + dx * s, cy + dy * s, 76 * s, 76 * s, C[col], TONE, 'tblr', seed=70 + k, layer=3, rot=rot, amp=(3, 6))
    return avoid(out, 'blocks')


def path_dashes(pts, tone=TONE):
    d = 'M ' + ' L '.join(f'{x:.1f} {y:.1f}' for x, y in pts)
    return paper(f'<path d="{d}" fill="none" stroke="{C["deep"]}" stroke-width="9" stroke-linecap="round" stroke-dasharray="4 26"/>', tone, 2, 't')


# ---------------------------------------------------------------- slides
BREAKS = {
    1: ['يبدأ الصراخ', 'أول ما تجيبي الجزمة', 'عشان تطلعوا؟', 'الفرق كله في الربع ساعة', 'اللي قبلها.'],
    2: ['لما تجي الجزمة', 'وهو لسه مستمتع باللعب،', 'طبيعي ما يبغى يوقف.'],
    3: ['هذي ثلاث أشياء تسويها', 'في الربع ساعة', 'اللي قبل الطلعة.'],
    4: ['قبل الطلعة بربع ساعة،', 'لا تبدئي معاه شي جديد', 'يحتاج وقت.', 'لا آيباد ولا غيره.'],
    5: ['وخلي آخر شي قبل الطلعة', 'حاجة بسيطة يخلصها على راحته.', 'عصير يشربه،', 'أو بسكوتة ياكلها.',
        'يخلص منها، وبعدها تطلعوا.'],
    6: ['لا تناديه يجي للباب', 'عشان يلبس الجزمة.', 'خذيها له مكانه،', 'ولبّسيه وهو جالس،', 'وبعدها اطلعوا.'],
    7: ['الطلعة موقف واحد بس.', 'التقييم المجاني يساعدك', 'تشوفي الصورة الأكبر،', 'وتعرفي من فين تبدئي.'],
}


def body(ctx, y=MT + 40, w=888):
    return text_box(ctx.t.body(), W - MX - w, y, w, 'ink')


def slide(ctx):
    s = ctx.s
    if s == 1:
        q, clause = ctx.t.split_seg(ctx.t.body()[0], '؟ ')
        clause.role = 'clause'
    if s in BREAKS:
        keep_in(ctx.t.segs, *[p for p in BREAKS[s] if any(p in g.text for g in ctx.t.segs)])
    r = {'ground': GROUND, 'dots_theme': 'gold'}

    if s == 1:
        art = clock(540, 1010, 370)
        html = (text_box([q], MX, MT - 10, W - 2 * MX, 'ink', size={'hook': 88})
                + text_box([clause], MX, MT + 370, W - 2 * MX, 'ink'))
        r.update(art=art, html=html)

    elif s == 2:
        # the shoes arrive at 12 sharp while he is still mid-play: no wedge yet
        art = clock(600, 1180, 560, wedge_parts=0, hands=(-90, -90), seed=2, inside=blocks(200, 860, 1.0))
        r.update(art=art, html=body(ctx))

    elif s == 3:
        art = clock(540, 990, 400, wedge_parts=3, seed=3)
        r.update(art=art, html=body(ctx))

    elif s == 4:
        # close on the wedge: no new thing that takes time
        R = 600
        cx, cy = 800, 1220
        wx, wy = polar(cx, cy, R * .5, 225)
        art = clock(cx, cy, R, seed=4, shoes_at=True, inside=ipad_crossed(wx, wy, .95, -8, seed=4))
        r.update(art=art, html=body(ctx))

    elif s == 5:
        # pushed in close and to the right: the wedge is the stage for the last small thing
        R = 520
        cx, cy = 700, 1120
        wx, wy = polar(cx, cy, R * .5, 225)
        art = clock(cx, cy, R, seed=5, shoes_at=False,
                    inside=avoid(cup(wx + 20, wy - 40, .8) + biscuit(wx - 120, wy + 80, 58), 'snack'))
        r.update(art=art, html=body(ctx, y=MT + 20))

    elif s == 6:
        # the shoes leave 12 and travel down into the wedge, to where he sits
        R = 470
        cx, cy = 520, 1080
        sx, sy = polar(cx, cy, R * .5, 225)
        trail = path_dashes(arc_pts(cx, cy, R * .7, -62, -128, 14))
        hx, hy = polar(cx, cy, R * .7, -136)
        head = paper(f'<polygon points="{hx - 18:.1f},{hy - 22:.1f} {hx + 22:.1f},{hy - 8:.1f} {hx - 12:.1f},{hy + 22:.1f}" fill="{C["deep"]}"/>', TONE, 2)
        art = clock(cx, cy, R, seed=6, shoes_at=False,
                    inside=trail + head + shoes(sx + 5, sy + 70, R / 400 * .8, rot=-4))
        r.update(art=art, html=body(ctx))

    else:
        segs = ctx.t.body()
        cta = segs[-1]
        assert cta.text == ctx.cta_text(), (cta.text, ctx.cta_text())
        art = clock(205, 1105, 120, seed=7)
        html = (text_box(segs[:-1], MX, 240, W - 2 * MX, 'ink')
                + conversion_tag(cta, 450, 660, rot=-3))
        r.update(art=art, html=html)
    return r
