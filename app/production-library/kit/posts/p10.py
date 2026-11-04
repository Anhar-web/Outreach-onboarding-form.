"""p10 crying. SandLight ground, light. Clue board (a symbolic board, no scene).

Motif: a cut deep teardrop (~300px) centre-low; three blank pearl torn notes with
gold pins sit round it in a triangle, tied to the drop by deep threads.
s1: question 96px ink top-right, clause 54px under it; the board fills the lower half.
s2: the drop swells; the three guesses (water, a plate, a toy) circle it, unpinned.
s3-s5: each «شي» enlarges one note, which gains a flat deep icon:
       an iPad with an off-dot, then a puzzle piece, then a blender.
s6: the whole board again, every note now filled in; one thread turns gold
    («تبدئي من وحدة منهم»).
s7: conversion end: gold ground, ink text, the board at 25% bottom-left, pearl tag.
"""
from kit import (C, MX, MT, W, H, paper, torn_rect, torn_strip, glow,
                 text_box, step_tab, avoid, keep_in, conversion_tag)

TONE = 'l'


# ---------------------------------------------------------------- motifs
def drop(cx, cy, s=1.0, tone=TONE, layer=2):
    """Cut deep teardrop, 300px tall at s=1, point up. Pearl sheen top-right."""
    T = f'translate({cx} {cy}) scale({s})'
    body = (f'<path d="M 0 -170 C 30 -110, 118 -40, 118 40 A 118 118 0 0 1 -118 40 '
            f'C -118 -40, -30 -110, 0 -170 Z" fill="{C["deep"]}"/>')
    sheen = (f'<path d="M 46 -14 C 70 6, 82 30, 80 58 C 70 46, 58 22, 36 2 Z" fill="{C["pearl"]}" fill-opacity=".55"/>')
    inner = (f'<path d="M 0 -120 C 18 -80, 76 -30, 80 30 A 80 80 0 0 1 -40 100 '
             f'A 100 100 0 0 0 60 30 C 58 -20, 20 -70, 0 -120 Z" fill="{C["night"]}" fill-opacity=".35"/>')
    return avoid(paper(body + inner + sheen, tone, layer, T=T), 'drop')


def pin(x, y, tone=TONE):
    return paper(f'<circle cx="{x}" cy="{y}" r="17" fill="{C["gold"]}"/>'
                 f'<circle cx="{x + 4}" cy="{y - 4}" r="6" fill="{C["pearl"]}" fill-opacity=".55"/>'
                 f'<circle cx="{x}" cy="{y}" r="17" fill="none" stroke="{C["goldDeep"]}" stroke-width="3" stroke-opacity=".6"/>',
                 tone, 3)


def note(x, y, w, h, rot=0, seed=1, icon='', tone=TONE):
    """Pearl torn note with a gold pin at the top centre. icon = SVG drawn on the
    note in its own (unrotated) coordinates. Returns (svg, pin_xy)."""
    sheet = torn_rect(x, y, w, h, C['pearl'], tone, 'tblr', seed=seed, layer=1, rot=rot, amp=(4, 9), inner=icon)
    px, py = x + w / 2, y + 30
    import math
    a = math.radians(rot)
    cx, cy = x + w / 2, y + h / 2
    rx = cx + (px - cx) * math.cos(a) - (py - cy) * math.sin(a)
    ry = cy + (px - cx) * math.sin(a) + (py - cy) * math.cos(a)
    return avoid(sheet + pin(rx, ry, tone), 'note'), (rx, ry)


def thread(a, b, color=None, width=5, tone=TONE, sag=40, layer=1):
    color = color or C['deep']
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + sag
    return paper(f'<path d="M {a[0]:.1f} {a[1]:.1f} Q {mx:.1f} {my:.1f} {b[0]:.1f} {b[1]:.1f}" fill="none" '
                 f'stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>', tone, layer, 't')


# flat deep icons, drawn in a box (x, y, size)
def icon_ipad(x, y, s):
    w, h = s * .56, s * .74
    ix, iy = x + (s - w) / 2, y + (s - h) / 2
    cx, cy, r = x + s / 2, y + s / 2, s * .14
    return (f'<rect x="{ix:.1f}" y="{iy:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{s * .07:.1f}" fill="{C["deep"]}"/>'
            f'<rect x="{ix + s * .05:.1f}" y="{iy + s * .07:.1f}" width="{w - s * .1:.1f}" height="{h - s * .14:.1f}" rx="{s * .02:.1f}" fill="{C["night"]}"/>'
            # power symbol: an open ring and a bar (the "off" sign)
            f'<path d="M {cx - r * .62:.1f} {cy - r * .78:.1f} A {r:.1f} {r:.1f} 0 1 0 {cx + r * .62:.1f} {cy - r * .78:.1f}" '
            f'fill="none" stroke="{C["pearl"]}" stroke-width="{s * .028:.1f}" stroke-linecap="round"/>'
            f'<line x1="{cx:.1f}" y1="{cy - r * 1.25:.1f}" x2="{cx:.1f}" y2="{cy - r * .2:.1f}" stroke="{C["pearl"]}" '
            f'stroke-width="{s * .028:.1f}" stroke-linecap="round"/>'
            f'<circle cx="{cx:.1f}" cy="{iy + h - s * .035:.1f}" r="{s * .016:.1f}" fill="{C["pearl"]}" fill-opacity=".6"/>')


def _piece_path(x, y, u):
    """Jigsaw piece: body u x u at (x,y), knob on the top and the right, socket on the left."""
    k = u * .17
    return (f'M {x} {y} L {x + u * .36} {y} '
            f'C {x + u * .36} {y - k * 1.6}, {x + u * .64} {y - k * 1.6}, {x + u * .64} {y} '
            f'L {x + u} {y} L {x + u} {y + u * .36} '
            f'C {x + u + k * 1.6} {y + u * .36}, {x + u + k * 1.6} {y + u * .64}, {x + u} {y + u * .64} '
            f'L {x + u} {y + u} L {x} {y + u} L {x} {y + u * .64} '
            f'C {x + k * 1.6} {y + u * .64}, {x + k * 1.6} {y + u * .36}, {x} {y + u * .36} Z')


def icon_puzzle(x, y, s):
    u = s * .44
    a = f'<path d="{_piece_path(x + s * .14, y + s * .34, u)}" fill="{C["deep"]}"/>'
    # the second piece hovers off, tilted: it would not go in
    b = (f'<g transform="rotate(-18 {x + s * .7} {y + s * .3})">'
         f'<path d="{_piece_path(x + s * .56, y + s * .12, u * .62)}" fill="none" stroke="{C["deep"]}" '
         f'stroke-width="{s * .03:.1f}" stroke-linejoin="round"/></g>')
    return a + b


def icon_blender(x, y, s):
    cx = x + s / 2
    jug = (f'<path d="M {cx - s * .2} {y + s * .14} L {cx + s * .2} {y + s * .14} L {cx + s * .15} {y + s * .62} '
           f'L {cx - s * .15} {y + s * .62} Z" fill="{C["tealMist"]}" stroke="{C["deep"]}" stroke-width="{s * .03:.1f}" stroke-linejoin="round"/>')
    lid = f'<rect x="{cx - s * .23:.1f}" y="{y + s * .08:.1f}" width="{s * .46:.1f}" height="{s * .07:.1f}" rx="{s * .02:.1f}" fill="{C["deep"]}"/>'
    blade = (f'<path d="M {cx - s * .1} {y + s * .5} L {cx + s * .1} {y + s * .46} M {cx - s * .1} {y + s * .44} L {cx + s * .1} {y + s * .52}" '
             f'stroke="{C["deep"]}" stroke-width="{s * .025:.1f}" stroke-linecap="round"/>')
    base = (f'<path d="M {cx - s * .2} {y + s * .62} L {cx + s * .2} {y + s * .62} L {cx + s * .25} {y + s * .86} '
            f'L {cx - s * .25} {y + s * .86} Z" fill="{C["deep"]}"/>'
            f'<circle cx="{cx:.1f}" cy="{y + s * .74:.1f}" r="{s * .045:.1f}" fill="{C["gold"]}"/>')
    # noise: three short arcs each side
    arcs = ''
    for k in range(2):
        r = s * (.3 + k * .09)
        arcs += (f'<path d="M {cx + r * .78:.1f} {y + s * .2:.1f} Q {cx + r:.1f} {y + s * .38:.1f} {cx + r * .78:.1f} {y + s * .56:.1f}" '
                 f'fill="none" stroke="{C["deep"]}" stroke-width="{s * .022:.1f}" stroke-linecap="round"/>'
                 f'<path d="M {cx - r * .78:.1f} {y + s * .2:.1f} Q {cx - r:.1f} {y + s * .38:.1f} {cx - r * .78:.1f} {y + s * .56:.1f}" '
                 f'fill="none" stroke="{C["deep"]}" stroke-width="{s * .022:.1f}" stroke-linecap="round"/>')
    return jug + lid + blade + base + arcs


ICONS = [icon_ipad, icon_puzzle, icon_blender]


def board(notes, drop_xy, drop_s, gold_thread=None, tone=TONE, case=None):
    """notes: list of (x, y, w, h, rot, seed, icon_index or None). Deep threads run
    from each note's pin to a gold pin pushed into the drop (clue-board style)."""
    dx, dy = drop_xy
    hub = (dx, dy - 30 * drop_s)
    threads, sheets = '', ''
    for k, (x, y, w, h, rot, seed, ic) in enumerate(notes):
        icon = ''
        if ic is not None:
            pad = min(w, h) * .12
            sz = min(w, h) - 2 * pad
            icon = ICONS[ic](x + (w - sz) / 2, y + (h - sz) / 2 + h * .04, sz)
        sv, p = note(x, y, w, h, rot, seed, icon, tone)
        sheets += sv
        if gold_thread == k:
            if case:   # on a gold ground: a deep casing under the gold thread so it still shows
                threads += thread(p, hub, case, 30, tone, sag=24, layer=2)
            threads += thread(p, hub, C['gold'], 14 if case else 12, tone, sag=24, layer=2)
        else:
            threads += thread(p, hub, None, 4, tone, sag=36)
    return drop(dx, dy, drop_s, tone) + threads + sheets + pin(hub[0], hub[1], tone)


# small guessed objects for s2
def cup(cx, cy, s, rot):
    return paper(f'<g transform="translate({cx} {cy}) rotate({rot}) scale({s})">'
                 f'<path d="M -46 -60 L 46 -60 L 36 60 L -36 60 Z" fill="{C["tealMist"]}"/>'
                 f'<path d="M -40 -10 L 40 -10 L 36 60 L -36 60 Z" fill="{C["teal"]}"/>'
                 f'<rect x="-50" y="-68" width="100" height="14" rx="6" fill="{C["pearl"]}"/></g>', TONE, 2)


def dish(cx, cy, s, rot):
    return paper(f'<g transform="translate({cx} {cy}) rotate({rot}) scale({s})">'
                 f'<ellipse cx="0" cy="0" rx="92" ry="92" fill="{C["pearl"]}"/>'
                 f'<circle cx="0" cy="0" r="64" fill="none" stroke="{C["sandLight"]}" stroke-width="6"/>'
                 f'<circle cx="-20" cy="-12" r="24" fill="{C["gold"]}"/><rect x="2" y="4" width="44" height="30" rx="8" fill="{C["goldDeep"]}"/>'
                 f'<circle cx="-14" cy="30" r="12" fill="{C["teal"]}"/></g>', TONE, 2)


def toy(cx, cy, s, rot):
    return paper(f'<g transform="translate({cx} {cy}) rotate({rot}) scale({s})">'
                 f'<rect x="-60" y="-60" width="120" height="120" rx="14" fill="{C["gold"]}"/>'
                 f'<rect x="-34" y="-34" width="68" height="68" rx="8" fill="{C["deep"]}"/>'
                 f'<circle cx="0" cy="0" r="18" fill="{C["gold"]}"/></g>', TONE, 2)


# ---------------------------------------------------------------- slides
BREAKS = {
    1: ['يبكي وما تعرفي', 'ايش يبغى؟', 'هذي ثلاث أشياء تلاحظيها', 'قبل ما تبدئي تخمني.'],
    2: ['تجيبي له موية،', 'وبعدها أكل،', 'وبعدها لعبته،', 'وهو يبكي أكثر.'],
    3: ['ايش اللي صار', 'قبل البكا بشوي.', 'الآيباد طفى', 'أو رجعتوا من طلعه', 'أو خلص الاكل اللي في صحنه.'],
    4: ['ايش كان يسوي', 'لما بدأ.', 'يحاول يركب قطعة وما ركبت،', 'أو يدور على لعبة وما لقاها.'],
    5: ['فين كان.', 'في المطبخ والخلاط شغال،', 'أو في الصالة والتلفزيون عالي،', 'أو في غرفة نورها قوي.'],
    6: ['هذي الثلاث تلاحظيها في ثواني،', 'وهو لسه يبكي.', 'كذا بدل ما تجربي كل شي،', 'تبدئي من وحدة منهم.'],
    7: ['إذا البكا يتكرر كل يوم،', 'التقييم المجاني يساعدك', 'تشوفي يومه كامل', 'بدل ما تخمني.'],
}


def body(ctx, y=None, w=888):
    html = ''
    if ctx.t.label():
        html += step_tab(ctx.t.label())
    top = y or (MT + 115 if ctx.t.label() else MT + 40)
    return html + text_box(ctx.t.body(), W - MX - w, top, w, 'ink')


def slide(ctx):
    s = ctx.s
    if s == 1:
        q, clause = ctx.t.split_seg(ctx.t.body()[0], '؟ ')
        clause.role = 'clause'
    if s in BREAKS:
        keep_in(ctx.t.segs, *[p for p in BREAKS[s] if any(p in g.text for g in ctx.t.segs)])
    r = {'ground': 'sandLight'}

    if s == 1:
        # triangle of blank notes round the drop: two up, one down to the right
        art = board([(96, 640, 250, 220, -6, 11, None),
                     (720, 610, 250, 220, 5, 12, None),
                     (700, 1000, 250, 220, -3, 13, None)],
                    (430, 1010), 1.0)
        html = (text_box([q], MX, MT, W - 2 * MX, 'ink')
                + text_box([clause], MX, MT + 290, W - 2 * MX, 'ink'))
        r.update(art=art, html=html)

    elif s == 2:
        # everything she tries: the guesses circle a bigger drop, none of them pinned
        art = (drop(540, 960, 1.3)
               + avoid(cup(230, 760, 1.35, -14) + dish(850, 800, 1.25, 10) + toy(260, 1120, 1.25, 16), 'guesses'))
        r.update(art=art, html=body(ctx))

    elif s in (3, 4, 5):
        k = s - 3          # which note grows
        big = {0: (470, 590, 470, 460, 3, 21),
               1: (150, 600, 470, 460, -3, 22),
               2: (315, 600, 450, 430, 2, 23)}[k]
        small = {0: [(110, 640, 170, 150, -7, 31), (150, 860, 170, 150, 6, 32)],
                 1: [(780, 640, 170, 150, 6, 33), (770, 860, 170, 150, -5, 34)],
                 2: [(110, 650, 170, 150, -6, 35), (800, 660, 170, 150, 7, 36)]}[k]
        drop_xy = {0: (250, 1130), 1: (850, 1130), 2: (540, 1125)}[k]
        notes = [big + (k,)] + [n + (None,) for n in small]
        art = board(notes, drop_xy, .45 if k == 2 else .5)
        r.update(art=art, html=body(ctx))

    elif s == 6:
        art = board([(730, 590, 250, 240, 5, 41, 0),
                     (100, 600, 250, 240, -5, 42, 1),
                     (415, 680, 250, 240, -2, 43, 2)],
                    (540, 1110), .62, gold_thread=0)
        r.update(art=art, html=body(ctx, y=MT + 20))

    else:
        # conversion end: gold ground, ink text, the board at 25% bottom-left, pearl tag
        segs = ctx.t.body()
        cta = segs[-1]
        assert cta.text == ctx.cta_text(), (cta.text, ctx.cta_text())
        mini = (f'<g transform="translate(60 975) scale(.36)">'
                + board([(620, 30, 260, 240, 5, 51, 0), (40, 40, 260, 240, -6, 52, 1), (330, 110, 260, 240, -2, 53, 2)],
                        (460, 560), .72, gold_thread=0, case=C['deep']) + '</g>')
        html = (text_box(segs[:-1], MX, 260, W - 2 * MX, 'ink')
                + conversion_tag(cta, 430, 640, rot=-3))
        r.update(ground='gold', art=mini, html=html, dots_theme='gold')
    return r
