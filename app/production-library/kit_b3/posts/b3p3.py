"""b3p3 Checkout. Deep ground. Composition: LOW CONVEYOR BAND.

The checkout belt is a long dark strip running across the lower third, side-on,
on a night counter. A side-view shopping trolley (wire = torn pearl strips).
s1: the full trolley abandoned at the belt end; mum's abaya walks off right,
    a small pair of feet and the back of a small head on her hip.
s2: the sweets rack (round torn discs) and a small hand reaching for one.
s3: the trolley alone, items heaped high (soft CTA above it).
s4: a small figure from behind, standing idle by the belt.
s5: the race: a small hand and mum's hand both putting boxes on the belt.
s6: the small row is ahead; a gold disc over it.
s7: a light trolley rolling out, a small hand on the handle.
End: gold, a mini trolley bottom-left.
"""
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'deep'
T = 'd'
BY = 1040   # belt top


# ---------------------------------------------------------------- motifs
def belt(y=BY, x0=-30, x1=1110, seed=1):
    """Counter (night block) with the belt (ink torn strip) on top, a pearl edge and roller studs."""
    out = torn_rect(x0, y + 40, x1 - x0, H - y, C['night'], T, sides='t', seed=seed, layer=1)
    out += torn_rect(x0, y, x1 - x0, 48, C['ink'], T, sides='tb', seed=seed + 4, layer=2,
                     inner=''.join(f'<rect x="{x}" y="{y + 20}" width="34" height="6" rx="3" fill="{C["deep"]}" fill-opacity=".6"/>'
                                   for x in range(int(x0) + 40, int(x1), 90)))
    out += torn_strip([(x0, y + 54), (x1, y + 54)], 10, C['pearl'], T, seed=seed + 9, layer=2)
    return avoid(out, 'belt')


def items_svg(kind):
    """Groceries inside the basket (local trolley frame, basket floor y=-110)."""
    if kind == 'none':
        return ''
    full = [(-215, -260, 120, 150, 'gold'), (-95, -300, 115, 190, 'teal'), (20, -250, 120, 140, 'sandLight'),
            (-190, -395, 95, 140, 'tealMist'), (-80, -405, 80, 110, 'pearl'), (10, -380, 140, 135, 'gold'),
            (110, -230, 70, 120, 'tealMist')]
    heap = full + [(-150, -500, 120, 110, 'sandLight'), (-30, -490, 110, 95, 'teal'), (70, -470, 90, 100, 'pearl'),
                   (-230, -470, 80, 85, 'gold')]
    if kind == 'light':
        return (f'<path d="M -60 -110 L -80 -270 L 70 -270 L 50 -110 Z" fill="{C["pearl"]}"/>'
                f'<path d="M -40 -270 Q -5 -330 30 -270" fill="none" stroke="{C["pearl"]}" stroke-width="12"/>'
                f'<rect x="-50" y="-215" width="90" height="16" fill="{C["gold"]}"/>')
    boxes = heap if kind == 'heap' else full
    out = ''
    for (x, y, w, h, col) in boxes:
        out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{C[col]}"/>'
        out += f'<rect x="{x + 12}" y="{y + h * .3:.0f}" width="{w - 24}" height="{max(10, h * .12):.0f}" fill="{C["goldDeep"] if col in ("pearl", "tealMist", "sandLight") else C["pearl"]}" fill-opacity=".6"/>'
    return out


def trolley(x, gy, s=1.0, items='full', flip=False, seed=10, name='trolley'):
    """Side-view trolley. (x, gy) = centre on the floor. Wire = torn pearl strips;
    handle on the right (flip=True puts it on the left)."""
    fx = -1 if flip else 1
    tr = f'translate({x} {gy}) scale({s * fx} {s})'
    out = paper(items_svg(items), T, 1, T=tr)
    rimL, rimR, botL, botR = (-250, -340), (210, -340), (-185, -110), (175, -110)
    strips = [[rimL, rimR], [botL, botR], [rimL, botL], [rimR, botR],
              [(-232, -225), (195, -225)]]
    for k in range(1, 8):
        t = k / 8
        strips.append([(rimL[0] + (rimR[0] - rimL[0]) * t, -340), (botL[0] + (botR[0] - botL[0]) * t, -110)])
    strips += [[(-165, -110), (-150, -64)], [(155, -110), (140, -64)], [(-200, -64), (190, -64)],
               [rimR, (275, -430)]]
    for k, st in enumerate(strips):
        wd = 18 if k < 4 or k >= 12 else 9
        out += torn_strip(st, wd, C['pearl'], T, seed=seed + k, layer=2, core=False, T=tr)
    out += paper(f'<rect x="250" y="-452" width="64" height="40" rx="18" fill="{C["gold"]}" transform="rotate(-30 282 -432)"/>'
                 + ''.join(f'<circle cx="{wx}" cy="-30" r="32" fill="{C["ink"]}"/><circle cx="{wx}" cy="-30" r="12" fill="{C["pearl"]}"/>'
                           for wx in (-160, 150)), T, 3, T=tr)
    return avoid(out, name)


def small_hand(x, y, s=1.0, rot=0, grab=False, sleeve='teal', cuff='tealDeep', name='small'):
    """A small hand reaching UP, fingertips at (x, y), sleeve running down."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    if grab:
        hand = (f'<rect x="-56" y="0" width="112" height="110" rx="40" fill="{C["sandLight"]}"/>'
                + ''.join(f'<rect x="{-54 + n * 28}" y="-6" width="26" height="40" rx="13" fill="{C["sandLight"]}"/>' for n in range(4)))
    else:
        lens = (80, 96, 90, 74)
        hand = ''.join(f'<rect x="{-50 + n * 26}" y="{100 - lens[n]}" width="22" height="{lens[n] + 20}" rx="11" fill="{C["sandLight"]}" '
                       f'transform="rotate({(n - 1.5) * 6} {-39 + n * 26} 110)"/>' for n in range(4))
        hand += f'<rect x="-58" y="96" width="112" height="110" rx="40" fill="{C["sandLight"]}"/>'
        hand += f'<rect x="-96" y="120" width="34" height="80" rx="17" fill="{C["sandLight"]}" transform="rotate(-38 -79 160)"/>'
    sl = (f'<path d="M -66 190 L 64 190 L 74 900 L -76 900 Z" fill="{C[sleeve]}"/>'
          f'<rect x="-70" y="184" width="140" height="34" rx="10" fill="{C[cuff]}"/>')
    return avoid(paper(sl, T, 2, T=tr) + paper(hand, T, 3, T=tr), name)


def side_hand(x, y, side='left', s=1.0, sleeve='teal', cuff='tealDeep', name='hand', box=None):
    """A hand coming in from the left/right edge, gripping the near side of a box
    at (x, y). box = (w, h, colour) draws the held box."""
    sx = 1 if side == 'left' else -1
    tr = f'translate({x} {y}) scale({sx * s} {s})'
    out = ''
    if box:
        bw, bh, col = box
        out += paper(f'<rect x="20" y="{-bh / 2}" width="{bw}" height="{bh}" rx="8" fill="{C[col]}"/>'
                     f'<rect x="32" y="{-bh * .1:.0f}" width="{bw - 24}" height="{bh * .14:.0f}" fill="{C["pearl"] if col not in ("pearl", "tealMist", "sandLight") else C["goldDeep"]}" fill-opacity=".6"/>',
                     T, 2, T=tr)
    sl = (f'<path d="M -900 -62 L -60 -58 L -60 62 L -900 70 Z" fill="{C[sleeve]}"/>'
          f'<rect x="-84" y="-64" width="34" height="128" rx="10" fill="{C[cuff]}"/>')
    hand = (f'<rect x="-60" y="-50" width="90" height="100" rx="34" fill="{C["sandLight"]}"/>'
            + ''.join(f'<rect x="8" y="{-48 + n * 25}" width="44" height="22" rx="11" fill="{C["sandLight"]}"/>' for n in range(4))
            + f'<rect x="-30" y="-74" width="80" height="28" rx="14" fill="{C["sandLight"]}" transform="rotate(-8 10 -60)"/>')
    out += paper(sl, T, 2, T=tr) + paper(hand, T, 3, T=tr)
    return avoid(out, name)


def lolly(cx, cy, r, col, seed):
    stick = f'<rect x="{cx - 5}" y="{cy}" width="10" height="{r * 2.2:.0f}" rx="4" fill="{C["pearl"]}"/>'
    swirl = f'<circle cx="{cx}" cy="{cy}" r="{r * .55:.0f}" fill="none" stroke="{C["pearl"] if col != "pearl" else C["gold"]}" stroke-opacity=".7" stroke-width="7"/>'
    sw = (f'<path d="M {cx - r * .55:.0f} {cy} A {r * .55:.0f} {r * .55:.0f} 0 0 1 {cx + r * .55:.0f} {cy} A {r * .3:.0f} {r * .3:.0f} 0 0 1 {cx - r * .05:.0f} {cy}" '
          f'fill="none" stroke="{C["pearl"] if col != "pearl" else C["gold"]}" stroke-width="8" stroke-linecap="round"/>')
    return paper(stick, T, 1) + paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C[col]}"/>' + sw, T, 2)


def sweets_rack(x0, y0, w=330, h=520):
    """A tall sweets rack: goldDeep frame, three pearl shelves, round lollipop discs."""
    out = torn_rect(x0, y0, w, h, C['night'], T, sides='tblr', seed=21, layer=1)
    out += paper(f'<rect x="{x0 - 14}" y="{y0 - 10}" width="22" height="{h + 30}" rx="6" fill="{C["goldDeep"]}"/>'
                 f'<rect x="{x0 + w - 8}" y="{y0 - 10}" width="22" height="{h + 30}" rx="6" fill="{C["goldDeep"]}"/>', T, 2)
    cols = ('gold', 'teal', 'pearl', 'sandLight')
    for row in range(3):
        sy = y0 + 160 + row * 165
        for k in range(3):
            cx = x0 + 62 + k * 103
            out += lolly(cx, sy - 96, 40, cols[(row + k) % 4], seed=30 + row * 3 + k)
        out += torn_strip([(x0 - 10, sy), (x0 + w + 10, sy)], 18, C['pearl'], T, seed=50 + row, layer=2)
    return avoid(out, 'rack')


def mum_walking(cx, top, h=760):
    """Mum's abaya from behind, walking off right; a small child on her left hip:
    back of a small head over her shoulder, a small back, two small feet dangling."""
    r = h * .075
    foot = top + h
    abaya = (f'M {cx - h * .09} {top + r * 2.2} Q {cx - h * .2} {top + r * 2.5} {cx - h * .21} {top + h * .3} '
             f'L {cx - h * .3} {foot} L {cx + h * .32} {foot} L {cx + h * .22} {top + h * .3} '
             f'Q {cx + h * .2} {top + r * 2.5} {cx + h * .09} {top + r * 2.2} Z')
    out = paper(f'<path d="{abaya}" fill="{C["ink"]}"/>'
                f'<ellipse cx="{cx}" cy="{top + r * 1.2}" rx="{r * 1.1}" ry="{r * 1.3}" fill="{C["ink"]}"/>', T, 2)
    kx, ky = cx - h * .19, top + h * .2
    kid = (f'<ellipse cx="{kx}" cy="{ky + 90}" rx="62" ry="95" fill="{C["teal"]}"/>'
           f'<path d="M {kx - 40} {ky + 160} L {kx - 120} {ky + 240} L {kx - 92} {ky + 268} L {kx - 10} {ky + 190} Z" fill="{C["tealDeep"]}"/>'
           f'<path d="M {kx + 10} {ky + 170} L {kx - 40} {ky + 290} L {kx - 6} {ky + 304} L {kx + 46} {ky + 190} Z" fill="{C["tealDeep"]}"/>')
    shoes = (f'<rect x="{kx - 150}" y="{ky + 248}" width="64" height="38" rx="18" fill="{C["gold"]}" transform="rotate(40 {kx - 118} {ky + 267})"/>'
             f'<rect x="{kx - 62}" y="{ky + 286}" width="64" height="38" rx="18" fill="{C["gold"]}" transform="rotate(20 {kx - 30} {ky + 305})"/>')
    head = f'<circle cx="{kx + 4}" cy="{ky}" r="52" fill="{C["goldDeep"]}"/>'
    arm = f'<path d="M {cx + h * .02} {top + r * 2.7} Q {cx - h * .1} {top + h * .32} {kx + 20} {ky + 150}" fill="none" stroke="{C["ink"]}" stroke-width="46" stroke-linecap="round"/>'
    out += paper(kid + shoes, T, 3) + paper(head, T, 3) + paper(arm, T, 3)
    return avoid(out, 'mum')


def small_back(cx, foot, s=1.0):
    """A small child standing, from behind: back of the head, shirt, arms hanging, legs, shoes."""
    tr = f'translate({cx} {foot}) scale({s})'
    g = (f'<rect x="-36" y="-150" width="30" height="130" rx="12" fill="{C["ink"]}"/>'
         f'<rect x="6" y="-150" width="30" height="130" rx="12" fill="{C["ink"]}"/>'
         f'<rect x="-50" y="-30" width="48" height="30" rx="14" fill="{C["gold"]}"/>'
         f'<rect x="2" y="-30" width="48" height="30" rx="14" fill="{C["gold"]}"/>'
         f'<path d="M -70 -150 L -60 -320 Q -55 -350 -20 -352 L 20 -352 Q 55 -350 60 -320 L 70 -150 Z" fill="{C["teal"]}"/>'
         f'<rect x="-98" y="-340" width="34" height="160" rx="16" fill="{C["teal"]}" transform="rotate(8 -81 -340)"/>'
         f'<rect x="64" y="-340" width="34" height="160" rx="16" fill="{C["teal"]}" transform="rotate(-8 81 -340)"/>'
         f'<circle cx="-92" cy="-176" r="20" fill="{C["sandLight"]}"/><circle cx="92" cy="-176" r="20" fill="{C["sandLight"]}"/>'
         f'<rect x="-18" y="-370" width="36" height="30" fill="{C["sandLight"]}"/>')
    head = (f'<circle cx="0" cy="-420" r="62" fill="{C["goldDeep"]}"/><ellipse cx="-62" cy="-410" rx="10" ry="16" fill="{C["sandLight"]}"/>'
            f'<ellipse cx="62" cy="-410" rx="10" ry="16" fill="{C["sandLight"]}"/>')
    return avoid(paper(g, T, 2, T=tr) + paper(head, T, 3, T=tr), 'kid')


def box_row(x0, n, y=BY, gap=8, cols=('gold', 'teal', 'sandLight', 'tealMist'), sizes=None, dirn=1, seed=0):
    """Boxes standing on the belt, from x0 going right (dirn=1) or left (dirn=-1)."""
    out, x = '', x0
    sizes = sizes or [(96, 110), (80, 140), (104, 90), (86, 120), (92, 100)]
    for k in range(n):
        w, h = sizes[(k + seed) % len(sizes)]
        col = cols[(k + seed) % len(cols)]
        bx = x if dirn > 0 else x - w
        out += paper(f'<rect x="{bx}" y="{y - h + 4}" width="{w}" height="{h}" rx="8" fill="{C[col]}"/>'
                     f'<rect x="{bx + 10}" y="{y - h * .62:.0f}" width="{w - 20}" height="{h * .14:.0f}" fill="{C["goldDeep"] if col in ("pearl", "tealMist", "sandLight") else C["pearl"]}" fill-opacity=".6"/>', T, 2)
        x += dirn * (w + gap)
    return avoid(out, 'boxes')


def medal(cx, cy, r=46):
    """A gold paper star: the small row wins."""
    import math
    pts = []
    for k in range(10):
        a = math.radians(-90 + k * 36)
        rr = r if k % 2 == 0 else r * .45
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    from kit import torn_poly
    return avoid(torn_poly(pts, C['gold'], T, seed=77, layer=3, amp=(2, 4)), 'medal')


def motion(x, y, n=3, L=180, gap=46, seed=90):
    return ''.join(torn_strip([(x - L - k * 30, y + k * gap), (x - k * 30, y + k * gap)], 12, C['tealMist'], T, seed=seed + k, layer=1)
                   for k in range(n))


# ---------------------------------------------------------------- slides
def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = f'<g transform="translate(250 1250) scale(.48)">{trolley(0, 0, 1.0, "full", name="mini")}</g>'
        return cta_end(ctx, mini_art=mini, tag_y=1010, tag_x=W - MX - 470)
    art, html = '', ''
    if s == 1:
        art = belt(BY) + trolley(330, 1300, 1.0, 'full') + mum_walking(930, 735, 760)
        html = hook_box(ctx, G, y=MT - 20, size=90, w=900,
                        breaks=('مليانة ', 'الكاشير، ', 'طفلك ', 'الطابور '))
    elif s == 2:
        art = belt(BY) + sweets_rack(600, 700, 330, 520) + small_hand(470, 760, 1.0, rot=20, name='small')
        html = body_box(ctx, G)
    elif s == 3:
        art = belt(BY) + trolley(520, 1310, .92, 'heap')
        html = body_box(ctx, G) + soft_cta(ctx, y=640)
    elif s == 4:
        art = belt(BY) + box_row(120, 2, seed=1) + trolley(800, 1310, .78, 'full', flip=True) + small_back(420, 1300, 1.1)
        html = body_box(ctx, G)
    elif s == 5:
        lead = ctx.t.body()[0]
        lab, _ = ctx.t.split_seg(lead, 'قبل الكاشير: ')
        lab.role = 'label'
        art = (belt(BY) + box_row(150, 2, seed=1) + box_row(930, 2, dirn=-1, seed=2)
               + side_hand(345, 930, 'left', 1.0, sleeve='teal', box=(96, 120, 'gold'), name='small')
               + side_hand(735, 930, 'right', 1.15, sleeve='pearl', cuff='tealMist', box=(100, 110, 'teal'), name='mum'))
        html = body_box(ctx, G)
    elif s == 6:
        art = (belt(BY) + box_row(90, 5, seed=0) + box_row(990, 2, dirn=-1, seed=2) + medal(330, 800, 70)
               + small_hand(560, 900, .8, rot=8, name='small'))
        html = body_box(ctx, G)
    elif s == 7:
        art = (motion(220, 980, 3, 170) + trolley(560, 1300, .95, 'light')
               + small_hand(835, 880, .7, rot=-24, grab=True, name='small'))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
