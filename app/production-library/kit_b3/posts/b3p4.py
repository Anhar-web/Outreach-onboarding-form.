"""b3p4 Fast-food wait (F7 benefits). Night ground. Composition: ORDER SCREEN + RECEIPT RIBBON.

A big order screen built from blank paper tiles (no numbers), one tile glowing
gold, and a long pearl receipt strip with one matching gold block. Across the
slides: s1 a takeaway bag and cup on a car seat, the restaurant screen tiny in
the car window; s2 a tray lands on the next table while a small figure slides
off his chair; s3 three torn cards in a row (order, sit, collect); s4 a small
hand holds the receipt up to the screen, the matching tile glowing; s5 the
screen big, tiles lighting one by one, the back of a small head watching;
s6 a short card game laid on a tray. End: gold, a mini receipt + cup.
"""
import math
from kit import C, MX, MT, W, H, keep_in, brk, paper, torn_strip, torn_rect, torn_circle, torn_poly, glow, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'night'
T = 'd'


def screen(x, y, w, h, cols=4, rows=3, lit=(), dim=(), hang=True, layer=2):
    """Order screen: ink frame, pearl bezel, blank deep tiles; lit tiles are
    gold with a glow, dim tiles half-lit. No numbers, no words."""
    out = ''
    if hang:
        out += paper(f'<rect x="{x + w * .25 - 5}" y="{y - 400}" width="10" height="400" fill="{C["pearl"]}" fill-opacity=".7"/>'
                     f'<rect x="{x + w * .75 - 5}" y="{y - 400}" width="10" height="400" fill="{C["pearl"]}" fill-opacity=".7"/>', T, 1)
    pad, gap = w * .06, w * .03
    tw = (w - 2 * pad - (cols - 1) * gap) / cols
    th = (h - 2 * pad - (rows - 1) * gap) / rows
    tiles, glows = '', ''
    for r in range(rows):
        for c in range(cols):
            k = r * cols + c
            tx, ty = x + pad + c * (tw + gap), y + pad + r * (th + gap)
            if k in lit:
                glows += f'<rect x="{tx - 14:.1f}" y="{ty - 14:.1f}" width="{tw + 28:.1f}" height="{th + 28:.1f}" rx="16" fill="{C["gold"]}"/>'
                col, op = C['gold'], 1
            elif k in dim:
                col, op = C['gold'], .45
            else:
                col, op = C['deep'], 1
            tiles += f'<rect x="{tx:.1f}" y="{ty:.1f}" width="{tw:.1f}" height="{th:.1f}" rx="{min(tw, th) * .12:.1f}" fill="{col}" fill-opacity="{op}"/>'
            tiles += f'<rect x="{tx + tw * .18:.1f}" y="{ty + th * .62:.1f}" width="{tw * .64:.1f}" height="{th * .1:.1f}" rx="4" fill="{C["night"]}" fill-opacity=".35"/>'
    out += paper(f'<rect x="{x - 14}" y="{y - 14}" width="{w + 28}" height="{h + 28}" rx="22" fill="{C["pearl"]}"/>'
                 f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{C["ink"]}"/>', T, layer)
    if glows:
        out += glow(glows, 's')
    out += paper(tiles, T, layer)
    return avoid(out, 'screen')


def receipt(x, y, L=420, w=150, rot=0, curl=True, seed=4, layer=3):
    """A long pearl receipt strip, torn at the bottom, curling at the end; thin
    printed bars (no numbers) and one bold gold block that matches the lit tile."""
    bars = ''
    yy = y + 40
    k = 0
    while yy < y + L - 40:
        ww = w * (.7 if k % 3 else .45)
        if k == 2:
            bars += f'<rect x="{x + w * .15:.1f}" y="{yy:.1f}" width="{w * .7:.1f}" height="54" rx="8" fill="{C["gold"]}"/>'
            yy += 76
        else:
            bars += f'<rect x="{x + w - 18 - ww:.1f}" y="{yy:.1f}" width="{ww:.1f}" height="10" rx="5" fill="{C["tealDeep"]}" fill-opacity=".55"/>'
            yy += 30
        k += 1
    out = torn_rect(x, y, w, L, C['pearl'], T, sides='b', seed=seed, layer=layer, rot=rot, inner=bars)
    if curl:
        cx, cy = x + w / 2, y + L
        out += paper(f'<g transform="rotate({rot} {x + w / 2} {y + L / 2})"><path d="M {x} {y + L - 6} Q {cx} {cy + 90} {x + w} {y + L - 6} L {x + w} {y + L + 30} Q {cx} {cy + 130} {x} {y + L + 30} Z" fill="{C["tealMist"]}"/></g>', T, layer)
    return avoid(out, 'receipt')


def bag(cx, by, s=1.0, rot=0):
    """A paper takeaway bag: folded top, a gold sticker seal."""
    tr = f'translate({cx} {by}) rotate({rot}) scale({s})'
    return avoid(paper(f'<path d="M -120 0 L -106 -280 L 106 -280 L 120 0 Z" fill="{C["sandLight"]}"/>'
                       f'<path d="M -106 -280 L -100 -330 L 100 -330 L 106 -280 Z" fill="{C["gold"]}"/>'
                       f'<path d="M -100 -330 L -80 -350 L -60 -330 L -40 -350 L -20 -330 L 0 -350 L 20 -330 L 40 -350 L 60 -330 L 80 -350 L 100 -330 Z" fill="{C["gold"]}"/>'
                       f'<rect x="-34" y="-306" width="68" height="40" rx="6" fill="{C["teal"]}"/>'
                       f'<path d="M -106 -280 L -60 -40 M 106 -280 L 60 -40" stroke="{C["goldDeep"]}" stroke-opacity=".18" stroke-width="5"/>', T, 2, T=tr), 'bag')


def cup(cx, by, s=1.0, rot=0):
    """A takeaway cup: tapered teal body, pearl lid, gold straw."""
    tr = f'translate({cx} {by}) rotate({rot}) scale({s})'
    return avoid(paper(f'<rect x="12" y="-330" width="18" height="120" rx="6" fill="{C["gold"]}" transform="rotate(12 21 -270)"/>'
                       f'<path d="M -70 0 L -86 -220 L 86 -220 L 70 0 Z" fill="{C["teal"]}"/>'
                       f'<rect x="-98" y="-246" width="196" height="34" rx="14" fill="{C["pearl"]}"/>'
                       f'<rect x="-80" y="-140" width="160" height="40" fill="{C["tealDeep"]}"/>', T, 2, T=tr), 'cup')


def car_window(x, y, w, h):
    """A car side window (ink frame), the restaurant's lit screen tiny inside it."""
    out = paper(f'<path d="M {x} {y + h} L {x + w * .12} {y} L {x + w} {y} L {x + w} {y + h} Z" fill="{C["ink"]}"/>'
                f'<path d="M {x + 26} {y + h - 20} L {x + w * .12 + 18} {y + 22} L {x + w - 22} {y + 22} L {x + w - 22} {y + h - 20} Z" fill="{C["deep"]}"/>', T, 1)
    out += screen(x + w * .5, y + h * .3, w * .28, h * .32, cols=3, rows=2, lit=(4,), hang=False, layer=1)
    return avoid(out, 'window')


def car_seat(x, y, w=760):
    """A car back seat, side-on: a tall tealDeep back and a long cushion."""
    return avoid(paper(f'<path d="M {x} {y} Q {x - 30} {y - 260} {x + 20} {y - 300} L {x + 90} {y - 300} Q {x + 120} {y - 200} {x + 110} {y} Z" fill="{C["tealDeep"]}"/>'
                       f'<rect x="{x}" y="{y - 30}" width="{w}" height="120" rx="40" fill="{C["tealDeep"]}"/>'
                       f'<rect x="{x + 110}" y="{y - 30}" width="{w - 140}" height="24" rx="12" fill="{C["teal"]}" fill-opacity=".5"/>', T, 1)
                 + paper(f'<path d="M {x + 60} {y - 290} L {x + 70} {y - 40} L {x + 300} {y - 20}" fill="none" stroke="{C["ink"]}" stroke-width="26" stroke-linejoin="round"/>'
                         f'<rect x="{x + 290}" y="{y - 44}" width="70" height="44" rx="8" fill="{C["pearl"]}"/>'
                         f'<rect x="{x + 304}" y="{y - 32}" width="40" height="18" rx="4" fill="{C["gold"]}"/>', T, 2), 'seat')


def table(x, y, w):
    return avoid(paper(f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="10" fill="{C["goldDeep"]}"/>'
                       f'<rect x="{x + w / 2 - 18}" y="{y + 30}" width="36" height="{H - y}" fill="{C["goldDeep"]}"/>', T, 1), 'table')


def burger(cx, by, s=1.0):
    tr = f'translate({cx} {by}) scale({s})'
    return paper(f'<rect x="-90" y="-40" width="180" height="40" rx="18" fill="{C["gold"]}"/>'
                 f'<rect x="-98" y="-70" width="196" height="34" rx="14" fill="{C["goldDeep"]}"/>'
                 f'<path d="M -104 -66 Q -80 -88 -56 -70 Q -30 -90 -4 -70 Q 22 -90 48 -70 Q 74 -90 104 -66 Z" fill="{C["teal"]}"/>'
                 f'<path d="M -96 -80 Q -96 -170 0 -170 Q 96 -170 96 -80 Z" fill="{C["gold"]}"/>'
                 + ''.join(f'<ellipse cx="{dx}" cy="{dy}" rx="7" ry="4" fill="{C["sandLight"]}"/>' for dx, dy in ((-40, -140), (-6, -152), (30, -138), (56, -120), (-60, -112), (10, -118))),
                 T, 3, T=tr)


def fries(cx, by, s=1.0):
    tr = f'translate({cx} {by}) scale({s})'
    sticks = ''.join(f'<rect x="{-50 + k * 18}" y="{-170 + (k % 3) * 16}" width="14" height="120" rx="4" fill="{C["gold"]}" transform="rotate({(k - 3) * 4} {-43 + k * 18} -60)"/>' for k in range(6))
    return paper(sticks + f'<path d="M -64 0 L -76 -110 L 76 -110 L 64 0 Z" fill="{C["teal"]}"/>'
                 f'<path d="M -76 -110 Q 0 -70 76 -110" fill="none" stroke="{C["tealDeep"]}" stroke-width="10"/>', T, 3, T=tr)


def tray(x, y, w, h=40, food=True):
    out = paper(f'<path d="M {x} {y} L {x + w} {y} L {x + w - 24} {y + h} L {x + 24} {y + h} Z" fill="{C["teal"]}"/>', T, 2)
    if food:
        out = burger(x + w * .33, y + 4, .9) + fries(x + w * .74, y + 4, .8) + out
    return avoid(out, 'tray')


def chair_slide(cx, by, s=1.0):
    """A cafe chair side-on and a small child sliding off it (back of the head,
    no face): the torso slumps forward-down, the legs reach the floor."""
    tr = f'translate({cx} {by}) scale({s})'
    chair = (f'<rect x="-120" y="-250" width="200" height="26" rx="10" fill="{C["gold"]}"/>'
             f'<rect x="60" y="-500" width="26" height="276" rx="10" fill="{C["gold"]}"/>'
             f'<rect x="-110" y="-230" width="22" height="230" fill="{C["gold"]}"/>'
             f'<rect x="50" y="-230" width="22" height="230" fill="{C["gold"]}"/>')
    kid = (f'<path d="M -150 -40 Q -110 -10 -40 -60 L 10 -100 L -30 -150 L -90 -110 Q -160 -90 -170 -40 Z" fill="{C["ink"]}"/>'
           f'<ellipse cx="-180" cy="-26" rx="44" ry="22" fill="{C["pearl"]}"/>'
           f'<path d="M -40 -250 Q 20 -330 50 -360 L 90 -300 Q 60 -200 10 -120 L -60 -120 Z" fill="{C["tealMist"]}"/>'
           f'<path d="M 10 -300 Q -60 -260 -110 -240" stroke="{C["sandLight"]}" stroke-width="30" stroke-linecap="round" fill="none"/>'
           f'<circle cx="64" cy="-410" r="70" fill="{C["goldDeep"]}"/>')
    return avoid(paper(chair, T, 1, T=tr) + paper(kid, T, 2, T=tr), 'kid')


def order_card(cx, cy, w, h, icon, rot=0, seed=1):
    """A torn pearl card with a wordless icon: 'order' (a tiny screen),
    'sit' (a chair) or 'collect' (a tray with a burger)."""
    out = torn_rect(cx - w / 2, cy - h / 2, w, h, C['pearl'], T, seed=seed, layer=2, rot=rot)
    g = f'translate({cx} {cy + 10}) rotate({rot})'
    if icon == 'order':
        out += paper(f'<g transform="{g}"><rect x="-80" y="-80" width="160" height="110" rx="12" fill="{C["ink"]}"/>'
                     + ''.join(f'<rect x="{-66 + c * 46}" y="{-66 + r * 44}" width="38" height="36" rx="5" fill="{C["gold"] if (r, c) == (1, 2) else C["deep"]}"/>' for r in range(2) for c in range(3))
                     + f'<rect x="-6" y="30" width="12" height="40" fill="{C["ink"]}"/><rect x="-46" y="66" width="92" height="12" rx="6" fill="{C["ink"]}"/></g>', T, 3)
    elif icon == 'sit':
        out += paper(f'<g transform="{g}"><rect x="-60" y="0" width="120" height="20" rx="8" fill="{C["gold"]}"/>'
                     f'<rect x="38" y="-110" width="22" height="120" rx="8" fill="{C["gold"]}"/>'
                     f'<rect x="-56" y="16" width="16" height="70" fill="{C["gold"]}"/><rect x="40" y="16" width="16" height="70" fill="{C["gold"]}"/></g>', T, 3)
    else:
        out += paper(f'<g transform="{g}"><path d="M -86 40 L 86 40 L 74 60 L -74 60 Z" fill="{C["teal"]}"/></g>', T, 3)
        out += burger(cx, cy + 50, .55)
    return avoid(out, 'card')


def path_dots(pts, r=9):
    return ''.join(paper(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{C["gold"]}"/>', T, 1) for x, y in pts)


def small_hand_up(cx, cy, s=1.0, rot=-6):
    """A small hand from the bottom edge, pinching the top of something it holds up."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    return avoid(paper(f'<path d="M -54 60 L 54 60 L 70 520 L -70 520 Z" fill="{C["tealDeep"]}"/>'
                       f'<rect x="-58" y="50" width="116" height="24" rx="8" fill="{C["teal"]}"/>'
                       f'<rect x="-66" y="-60" width="132" height="124" rx="46" fill="{C["sandLight"]}"/>'
                       f'<rect x="-92" y="-94" width="36" height="96" rx="18" fill="{C["sandLight"]}" transform="rotate(-20 -74 -46)"/>'
                       + ''.join(f'<rect x="{-50 + k * 32}" y="-84" width="30" height="60" rx="15" fill="{C["sandLight"]}" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="3"/>' for k in range(4)),
                       T, 3, T=tr), 'hand')


def small_head(cx, cy, r=110):
    """Back of a small head (hair, two ears), shoulders below. No face."""
    return avoid(paper(f'<path d="M {cx - r * 1.7} {cy + r * 2.4} Q {cx - r * 1.6} {cy + r * 1.05} {cx} {cy + r} Q {cx + r * 1.6} {cy + r * 1.05} {cx + r * 1.7} {cy + r * 2.4} Z" fill="{C["tealDeep"]}"/>'
                       f'<ellipse cx="{cx - r * .98}" cy="{cy + r * .1}" rx="{r * .16}" ry="{r * .26}" fill="{C["sandLight"]}"/>'
                       f'<ellipse cx="{cx + r * .98}" cy="{cy + r * .1}" rx="{r * .16}" ry="{r * .26}" fill="{C["sandLight"]}"/>'
                       f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["goldDeep"]}"/>', T, 2), 'head')


def game_card(cx, cy, w=120, h=160, rot=0, face=None, seed=1, layer=3):
    """A plain paper card: back = teal with a pearl border; face = pearl with one gold shape."""
    if face:
        inner = (f'<circle cx="{cx}" cy="{cy}" r="{w * .24}" fill="{C["gold"]}"/>' if face == 'circle' else
                 f'<rect x="{cx - w * .2}" y="{cy - w * .2}" width="{w * .4}" height="{w * .4}" fill="{C["teal"]}" transform="rotate(45 {cx} {cy})"/>')
        return paper(f'<g transform="rotate({rot} {cx} {cy})"><rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="12" fill="{C["pearl"]}"/>{inner}</g>', T, layer)
    return paper(f'<g transform="rotate({rot} {cx} {cy})"><rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="12" fill="{C["teal"]}"/>'
                 f'<rect x="{cx - w / 2 + 12}" y="{cy - h / 2 + 12}" width="{w - 24}" height="{h - 24}" rx="8" fill="none" stroke="{C["pearl"]}" stroke-width="5"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{w * .14}" fill="{C["gold"]}"/></g>', T, layer)


def slide(ctx):
    s = ctx.s
    if s == 6:
        keep_in(ctx.t.segs, 'يوصل لها.')
    if ctx.last:
        mini = receipt(80, 990, 230, 96, rot=-10, curl=False, seed=8) + cup(300, 1250, .62, rot=6)
        return cta_end(ctx, mini_art=mini, tag_y=1010, tag_x=W - MX - 500)
    art, html = '', ''
    if s == 1:
        art = (car_window(90, 700, 600, 270) + car_seat(80, 1190, 940)
               + bag(600, 1160, .92, rot=-3) + cup(850, 1160, .95, rot=4))
        html = hook_box(ctx, G, y=MT - 20, size=90, w=920,
                        keep=('قبل ما يوصل الأكل', 'قلتي لهم', 'خلوه سفري،', 'وأكلتيه بارد', 'في السيارة؟'))
    elif s == 2:
        art = (table(90, 960, 470) + tray(110, 920, 430)
               + chair_slide(800, 1250, 1.0))
        html = body_box(ctx, G)
    elif s == 3:
        y = 870
        art = (order_card(830, y, 230, 270, 'order', rot=3, seed=11)
               + order_card(540, y + 50, 230, 270, 'sit', rot=-2, seed=12)
               + order_card(250, y + 100, 230, 270, 'collect', rot=2, seed=13)
               + path_dots([(700, y + 190), (670, y + 200), (410, y + 240), (380, y + 250)], r=8))
        html = body_box(ctx, G)
    elif s == 4:
        art = (screen(110, 900, 470, 300, lit=(6,), hang=False)
               + receipt(720, 870, 330, 160, rot=6, curl=False, seed=5)
               + small_hand_up(800, 1170, .9, rot=6))
        html = body_box(ctx, G)
    elif s == 5:
        art = (screen(150, 560, 780, 440, cols=4, rows=3, lit=(5,), dim=(1, 2), hang=False)
               + small_head(540, 1160, 115))
        html = body_box(ctx, G)
    elif s == 6:
        art = (avoid(paper(f'<path d="M 120 880 L 960 880 L 920 1230 L 160 1230 Z" fill="{C["teal"]}"/>'
                           f'<path d="M 150 900 L 930 900 L 896 1208 L 184 1208 Z" fill="{C["tealDeep"]}"/>', T, 1), 'tray')
               + game_card(300, 1050, rot=-8, face='circle', seed=1) + game_card(450, 1040, rot=4, seed=2)
               + game_card(600, 1055, rot=-3, seed=3) + game_card(760, 1040, rot=7, face='circle', seed=4)
               + small_hand_up(760, 1150, .7, rot=-4))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
