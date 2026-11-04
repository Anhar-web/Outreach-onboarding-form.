"""p2 عزيمة. Deep ground, dark. Top-down blueprint of a majlis.

Motif: the plan in pearl outline: a U of 8 sandLight cushions, a night TV bar,
two speakers, a door gap at the bottom-right. A torn gold ring marks the seat by
the door.
s1: the camera is close: the cushion rows bleed off the frame so the 92px hook
    sits over the empty centre of the U.
Inner slides pull back to the whole plan (or a torn-edged detail crop of it); each
«الحساب» lifts one zone in gold: the arrival path, the seat ring, a gold bag with a
cup, a dish and a toy. s7 (red flag) is split at its "\\n": s7a shows all three
zones lit; s7b is the attention end (quiet line, one accent).
"""
from kit import (C, MX, MT, W, H, paper, torn_rect, torn_ring, torn_strip, torn_poly,
                 text_box, step_tab, avoid, keep_in, P)

TONE = 'd'
SEAT = (916, 845)          # centre of the cushion by the door (plan coords)
DOOR = (780, 940)          # door gap on the bottom wall, x from..to (plan coords, y = 1100)


def plan(T, hi=(), clip=None):
    """The majlis plan in local coords (room 1000 x 1100), drawn with transform T.
    hi: zones lifted in gold: 'in' (arrival path), 'out' (leaving path), 'ring'
    (seat), 'exit' (short quiet exit), 'bag' (bag with cup, dish, toy)."""
    o = []
    pe = C['pearl']
    # walls: pearl cut-paper outline with the door gap
    walls = (f'<path d="M {DOOR[1]} 1100 H 1000 V 0 H 0 V 1100 H {DOOR[0]}" fill="none" stroke="{pe}" '
             f'stroke-width="14" stroke-linejoin="miter"/>')
    door = (f'<line x1="{DOOR[0]}" y1="1100" x2="{DOOR[0]}" y2="{1100 - (DOOR[1] - DOOR[0])}" stroke="{pe}" stroke-width="8"/>'
            f'<path d="M {DOOR[0]} {1100 - (DOOR[1] - DOOR[0])} A {DOOR[1] - DOOR[0]} {DOOR[1] - DOOR[0]} 0 0 1 {DOOR[1]} 1100" '
            f'fill="none" stroke="{pe}" stroke-opacity=".55" stroke-width="5" stroke-dasharray="14 12"/>')
    o.append(paper(walls + door, TONE, 1, T=T))
    # TV bar (night with pearl outline) and two speakers
    o.append(avoid(paper(f'<rect x="360" y="1046" width="280" height="30" rx="4" fill="{C["night"]}" stroke="{pe}" stroke-width="4"/>', TONE, 1, T=T), 'tv'))
    for sx in (262, 682):
        o.append(paper(f'<rect x="{sx}" y="1020" width="56" height="56" rx="6" fill="{C["night"]}" stroke="{pe}" stroke-width="4"/>'
                       f'<circle cx="{sx + 28}" cy="1048" r="15" fill="none" stroke="{pe}" stroke-width="4"/>', TONE, 1, T=T))
    # 8 cushions in a U: 3 left, 2 top, 3 right (the last one sits by the door)
    cush = [(34, y, 100, 190) for y in (250, 460, 670)] + [(x, 34, 200, 100) for x in (290, 510)] + \
           [(866, y, 100, 190) for y in (330, 540, 750)]
    for k, (x, y, w, h) in enumerate(cush):
        pip = f'<rect x="{x + 12}" y="{y + 12}" width="{w - 24}" height="{h - 24}" rx="10" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="4"/>'
        o.append(avoid(paper(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{C["sandLight"]}"/>{pip}', TONE, 2, T=T), 'cushion'))
    # gold zones
    if 'in' in hi or 'out' in hi:
        pts = [(860, 1330), (860, 1040), (900, 975)] if 'in' in hi else [(900, 975), (860, 1040), (860, 1150)]
        o.append(avoid(torn_strip(pts, 40, C['gold'], TONE, seed=31, layer=3, T=T), 'path'))
        if 'in' in hi:   # arrowhead pointing in, at the seat end
            o.append(paper(f'<polygon points="900,940 940,1010 862,1000" fill="{C["gold"]}"/>', TONE, 3, T=T))
        else:            # arrowhead pointing out, beyond the door
            o.append(paper(f'<polygon points="860,1215 816,1140 904,1140" fill="{C["gold"]}"/>', TONE, 3, T=T))
    if 'exit' in hi:
        o.append(torn_strip([(900, 960), (880, 1050), (870, 1180)], 30, C['gold'], TONE, seed=37, layer=3, T=T))
        o.append(paper(f'<polygon points="870,1240 836,1172 904,1172" fill="{C["gold"]}"/>', TONE, 3, T=T))
    if 'ring' in hi:
        o.append(avoid(torn_ring(SEAT[0], SEAT[1], 150, 116, C['gold'], TONE, seed=13, layer=3, T=T), 'ring'))
    if 'bag' in hi:
        bx, by = 570, 790
        handle = f'<path d="M {bx + 30} {by + 10} Q {bx + 80} {by - 70} {bx + 130} {by + 10}" fill="none" stroke="{C["goldDeep"]}" stroke-width="12"/>'
        bag = torn_rect(bx, by, 160, 170, C['gold'], TONE, 'tblr', seed=17, layer=3, amp=(4, 8), T=T)
        cup = paper(f'<rect x="{bx + 18}" y="{by + 40}" width="40" height="56" rx="8" fill="{pe}"/>'
                    f'<path d="M {bx + 58} {by + 52} q 18 0 18 16 q 0 16 -18 16" fill="none" stroke="{pe}" stroke-width="7"/>', TONE, 3, T=T)
        dish = paper(f'<ellipse cx="{bx + 112}" cy="{by + 70}" rx="34" ry="22" fill="{pe}"/>'
                     f'<ellipse cx="{bx + 112}" cy="{by + 68}" rx="18" ry="10" fill="{C["sandLight"]}"/>', TONE, 3, T=T)
        toy = paper(f'<rect x="{bx + 52}" y="{by + 104}" width="50" height="50" rx="6" fill="{C["deep"]}"/>'
                    f'<circle cx="{bx + 77}" cy="{by + 129}" r="12" fill="{C["teal"]}"/>', TONE, 3, T=T)
        o.append(avoid(paper(handle, TONE, 3, T=T) + bag + cup + dish + toy, 'bag'))
    g = ''.join(o)
    if clip:
        # data-clip-y tells render.js where the crop starts (bounding boxes ignore clip-path)
        g = f'<g clip-path="url(#{clip[0]})" data-clip-y="{clip[1]}">{g}</g>'
    return g


def torn_window(cid, y0, seed=5):
    """A clip region with a torn top edge: a detail crop of the plan."""
    from kit import torn_poly_pts
    pts = torn_poly_pts([(-20, y0 + 10), (1100, y0 - 10), (1100, 1400), (-20, 1400)], torn=[0], seed=seed)
    edge = torn_poly([(-20, y0 + 10), (1100, y0 - 10), (1100, y0 + 4), (-20, y0 + 24)], C['night'], TONE, torn=[0], seed=seed, core=False)
    return f'<defs><clipPath id="{cid}"><polygon points="{P(pts)}"/></clipPath></defs>', edge


BREAKS = {
    1: ['قبل كل عزيمة', 'تحسبي لها ألف حساب؟', 'هذي الحسابات الثلاث', 'اللي فعلاً تفرق.'],
    2: ['متى توصلي ومتى تمشي.', 'حاولي توصلي بدري', 'قبل ما يمتلئ المجلس.', 'كذا يدخل', 'والمكان لسه هادي.'],
    3: ['وامشي وهو لسه مبسوط،', 'مو بعد ما يبدأ الصياح.', 'الطلعة وهو مرتاح', 'أخف عليك بكثير', 'من الطلعة وكل العيون عليكم.'],
    4: ['فين تجلسي.', 'قريب من الباب،', 'وهو جمبك،', 'وبعيد عن التلفزيون والسماعات.'],
    5: ['كذا لو احتاج يطلع شوي،', 'تطلعوا بهدوء', 'بدون ما تمروا قدام الكل.'],
    6: ['ايش يجي معاه من البيت.', 'كوبه،', 'وأكلة يعرفها،', 'وشي يمسكه بيده.'],
    7: ['هذي الثلاث تنحسب في البيت', 'قبل ما تطلعي.',
        'عشان لما توصلي،', 'تقدري تجلسي مع أهلك', 'بدل ما تقضي العزيمة كلها', 'وراه من غرفة لغرفة.'],
}


def body(ctx, y=None):
    html = ''
    if ctx.t.label():
        html += step_tab(ctx.t.label())
    top = y or (MT + 115 if ctx.t.label() else MT + 40)
    return html + text_box(ctx.t.body(), MX, top, W - 2 * MX, 'pearl')


FULL = 'translate(230 540) scale(.62)'          # whole plan, pulled back, lower half


def slide(ctx):
    s, part = ctx.s, ctx.part
    if s in BREAKS:
        keep_in(ctx.t.segs, *[p for p in BREAKS[s] if any(p in g.text for g in ctx.t.segs)])
    r = {'ground': 'deep'}
    if s == 1:
        # close-up: the U is wider than the frame; the hook sits in its empty centre
        # 88px (range 88-110): at 92 «تحسبي لها ألف حساب؟» is 942px and would have to break
        # inside the phrase. 88px in a 920px box keeps four clean phrase lines.
        art = plan('translate(-110 -60) scale(1.3)', hi=('ring',))
        r.update(art=art, html=text_box(ctx.t.body(), 80, 330, 920, 'pearl', size={'hook': 88}))
    elif s == 2:
        r.update(art=plan(FULL, hi=('in',)), html=body(ctx))
    elif s == 3:
        # detail crop at the door: the same path, now leaving
        defs, edge = torn_window('w3', 640)
        art = defs + plan('translate(-454 -390) scale(1.4)', hi=('out',), clip=('w3', 640)) + edge
        r.update(art=art, html=body(ctx))
    elif s == 4:
        r.update(art=plan(FULL, hi=('ring',)), html=body(ctx))
    elif s == 5:
        defs, edge = torn_window('w5', 600)
        art = defs + plan('translate(-431 -279) scale(1.3)', hi=('ring', 'exit'), clip=('w5', 600)) + edge
        r.update(art=art, html=body(ctx))
    elif s == 6:
        defs, edge = torn_window('w6', 560)
        art = defs + plan('translate(-400 -383) scale(1.45)', hi=('ring', 'bag'), clip=('w6', 560)) + edge
        r.update(art=art, html=body(ctx))
    elif s == 7 and part == 1:
        r.update(art=plan('translate(230 520) scale(.64)', hi=('in', 'ring', 'bag')), html=body(ctx, y=MT + 40))
    else:
        # attention end: quiet line centred, one accent (the gold ring round the seat, with its cushion)
        for g in ctx.t.body():
            g.role = 'quiet'
        accent = avoid(paper(f'<rect x="490" y="1010" width="100" height="190" rx="18" fill="{C["sandLight"]}"/>', TONE, 2)
                       + torn_ring(540, 1105, 150, 116, C['gold'], TONE, seed=13, layer=3), 'ring')
        r.update(art=accent, html=text_box(ctx.t.body(), MX, 300, W - 2 * MX, 'pearl', align='center'))
    return r
