"""p1 Night waking. Night ground. Composition: TOP-DOWN BED.

The big bed seen from straight above: a deep frame, two tealMist pillows, a
pearl duvet. His small tealDeep duvet lies diagonally across the middle and
takes half of it (the back of his head on the middle pillow, hair only); mum is
a thin lump squeezed onto the left edge, her pearl sleeve hanging off the side.
Across the slides the camera pulls away and the night plays out:
s1 the bed, half his.  s2 small footprints in the dark walking in from the door.
s3 heavy closed-eye arcs (no head, no face).  s4 a night clock disc at two.
s5 a big hand leads a small hand along a dashed path to his own bed, lamp dim.
s6 mum on a chair beside his bed (head and shoulders from above, sitting up).
s7 the day/night strip with one marked moment.  CTA: the bed small, bottom-right.
"""
import math
from kit import C, MX, MT, W, H, keep_in, paper, torn_strip, torn_rect, torn_circle, torn_poly, glow, avoid, arc_pts
from common import hook_box, body_box, soft_cta, cta_end

G = 'night'
T = 'd'


# ---------------------------------------------------------------- motifs
def big_bed(cx, cy, s=1.0, tone=T, child=True, mum=True, name='bed'):
    """The big bed from above, local coords: 760 wide, head at the top (y -470..450)."""
    tr = f'translate({cx} {cy}) scale({s})'
    frame = paper(f'<rect x="-390" y="-440" width="780" height="900" rx="26" fill="{C["deep"]}"/>'
                  f'<rect x="-410" y="-480" width="820" height="70" rx="20" fill="{C["deep"]}"/>', tone, 1, T=tr)
    sheet = paper(f'<rect x="-360" y="-420" width="720" height="860" rx="18" fill="{C["sandLight"]}"/>', tone, 1, T=tr)
    pillows = paper(f'<rect x="-340" y="-400" width="300" height="120" rx="40" fill="{C["tealMist"]}"/>'
                    f'<rect x="40" y="-400" width="300" height="120" rx="40" fill="{C["tealMist"]}"/>', tone, 2, T=tr)
    duvet = paper(f'<path d="M -372 -250 Q 0 -275 372 -250 L 372 470 L -372 470 Z" fill="{C["pearl"]}"/>'
                  f'<path d="M -372 -205 Q 0 -230 372 -205" fill="none" stroke="{C["gold"]}" stroke-width="12" stroke-opacity=".75"/>',
                  tone, 2, T=tr)
    out = frame + sheet + pillows + duvet
    if mum:
        # mum: a long narrow lump on the far left edge, back of her head on the pillow edge
        out += paper(f'<path d="M -372 -230 Q -300 -240 -282 -150 L -270 300 Q -300 380 -372 380 Z" fill="{C["pearl"]}"/>'
                     f'<path d="M -282 -150 Q -270 80 -272 300" fill="none" stroke="{C["deep"]}" stroke-opacity=".45" stroke-width="10"/>'
                     f'<path d="M -330 -180 Q -318 60 -326 330" fill="none" stroke="{C["tealMist"]}" stroke-width="8"/>', tone, 3, T=tr)
        out += paper(f'<ellipse cx="-330" cy="-300" rx="58" ry="66" fill="{C["ink"]}"/>', tone, 3, T=tr)
        out += paper(f'<g transform="rotate(8 -372 -100)"><rect x="-470" y="-130" width="110" height="64" rx="26" fill="{C["pearl"]}"/>'
                     f'<path d="M -470 -126 Q -540 -120 -540 -98 Q -540 -72 -470 -70 Z" fill="{C["sandLight"]}"/></g>', tone, 3, T=tr)
    if child:
        # his small duvet across the middle, diagonal, taking half the bed
        out += paper(f'<g transform="rotate(-18 40 60)"><path d="M -200 -170 Q 40 -210 280 -170 Q 300 60 270 300 Q 40 330 -190 300 Q -230 60 -200 -170 Z" fill="{C["tealDeep"]}"/>'
                     + ''.join(f'<circle cx="{-140 + (k % 4) * 120}" cy="{-90 + (k // 4) * 120}" r="11" fill="{C["pearl"]}" fill-opacity=".7"/>' for k in range(12))
                     + '</g>', tone, 3, T=tr)
        out += paper(f'<circle cx="40" cy="-300" r="62" fill="{C["goldDeep"]}"/>', tone, 3, T=tr)
    return avoid(out, name)


def small_bed(cx, cy, s=1.0, tone=T, child=True, rot=0, name='smallbed'):
    """His own bed from above, local 340 x 560, head at the top."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    out = paper(f'<rect x="-170" y="-280" width="340" height="560" rx="22" fill="{C["deep"]}"/>'
                f'<rect x="-185" y="-310" width="370" height="56" rx="18" fill="{C["deep"]}"/>', tone, 1, T=tr)
    out += paper(f'<rect x="-145" y="-262" width="290" height="522" rx="14" fill="{C["sandLight"]}"/>', tone, 1, T=tr)
    out += paper(f'<rect x="-110" y="-248" width="220" height="96" rx="34" fill="{C["tealMist"]}"/>', tone, 2, T=tr)
    if child:
        out += paper(f'<path d="M -158 -120 Q 0 -140 158 -120 L 158 272 L -158 272 Z" fill="{C["tealDeep"]}"/>'
                     + ''.join(f'<circle cx="{-90 + (k % 3) * 90}" cy="{-50 + (k // 3) * 100}" r="10" fill="{C["pearl"]}" fill-opacity=".7"/>' for k in range(9)),
                     tone, 3, T=tr)
        out += paper(f'<circle cx="0" cy="-180" r="52" fill="{C["goldDeep"]}"/>', tone, 3, T=tr)
    else:
        out += paper(f'<path d="M -158 -120 Q 0 -140 158 -120 L 158 272 L -158 272 Z" fill="{C["tealDeep"]}"/>'
                     f'<path d="M -158 -120 Q 0 -60 158 -120 L 158 -60 Q 0 -10 -158 -60 Z" fill="{C["pearl"]}" fill-opacity=".85"/>', tone, 3, T=tr)
    return avoid(out, name)


def footprint(x, y, rot, s=1.0, right=True, col=None, op=.9):
    """A small bare footprint from above: a sole and a row of five toes (big toe inside)."""
    col = col or C['pearl']
    m = 1 if right else -1
    toes = ''.join(f'<circle cx="{m * (-13 + k * 10.5):.1f}" cy="{-40 + k * k * 1.1:.1f}" r="{7.5 - k * .8:.1f}"/>' for k in range(5))
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" fill="{col}" fill-opacity="{op}">'
            f'<path d="M {m * -14} -24 Q {m * 4} -34 {m * 20} -22 Q {m * 24} 0 {m * 12} 20 Q {m * 14} 40 {m * 0} 42 Q {m * -16} 40 {m * -14} 18 Q {m * -22} -6 {m * -14} -24 Z"/>'
            f'{toes}</g>')


def footsteps(pts, s=1.0):
    """pts: list of (x, y, heading deg). Alternating left/right small feet."""
    out = ''
    for k, (x, y, h) in enumerate(pts):
        a = math.radians(h)
        off = 30 * (1 if k % 2 else -1)
        out += footprint(x - off * math.sin(a), y + off * math.cos(a), h + 90, s, right=bool(k % 2))
    return avoid(paper(out, T, 1, 't'), 'steps')


def door_light(x=0, y=880, w=46, h=470):
    """A sliver of hall light at the left edge: the door ajar."""
    return (glow(f'<rect x="{x}" y="{y}" width="{w + 30}" height="{h}" fill="{C["pearl"]}" fill-opacity=".18"/>', 'l')
            + torn_rect(x - 20, y, w + 20, h, C['pearl'], T, sides='r', seed=77, layer=1))


def crescent(cx, cy, r, col=None, tone=T, layer=2):
    col = col or C['pearl']
    return paper(f'<path d="M {cx} {cy - r} A {r} {r} 0 1 0 {cx} {cy + r} A {r * .62} {r} 0 1 1 {cx} {cy - r} Z" fill="{col}"/>', tone, layer)


def sleepy_eyes(cx, cy, w=230, gap=130):
    """Two heavy closed-eye arcs with lashes: torn pearl strips. No head shape around them."""
    out = ''
    for side in (-1, 1):
        ex = cx + side * (w / 2 + gap / 2)
        pts = arc_pts(ex, cy - w * .55, w * .62, 125, 55, 24)
        out += torn_strip(pts, 22, C['pearl'], T, seed=40 + side, layer=2)
        for k in range(5):
            a = math.radians(115 - k * 12.5)
            r0 = w * .62
            x0, y0 = ex + r0 * math.cos(a), cy - w * .55 + r0 * math.sin(a)
            x1, y1 = ex + (r0 + 46) * math.cos(a), cy - w * .55 + (r0 + 46) * math.sin(a)
            out += torn_strip([(x0, y0), (x1, y1)], 10, C['pearl'], T, seed=50 + k + side * 7, layer=2, core=False)
    return avoid(out, 'eyes')


def night_clock(cx, cy, r=170, tone=T):
    """Clock disc at two o'clock: no numerals, twelve pearl ticks, gold hub."""
    out = torn_circle(cx, cy, r + 18, C['pearl'], tone, seed=21, layer=1)
    ticks = ''
    for k in range(12):
        a = math.radians(k * 30 - 90)
        L = 26 if k % 3 == 0 else 14
        ticks += (f'<line x1="{cx + (r - 22) * math.cos(a):.1f}" y1="{cy + (r - 22) * math.sin(a):.1f}" '
                  f'x2="{cx + (r - 22 - L) * math.cos(a):.1f}" y2="{cy + (r - 22 - L) * math.sin(a):.1f}" '
                  f'stroke="{C["pearl"]}" stroke-width="{9 if k % 3 == 0 else 6}" stroke-linecap="round"/>')
    out += paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["deep"]}"/>{ticks}', tone, 2)
    ah = math.radians(60 - 90)
    out += paper(f'<line x1="{cx}" y1="{cy}" x2="{cx + r * .5 * math.cos(ah):.1f}" y2="{cy + r * .5 * math.sin(ah):.1f}" stroke="{C["pearl"]}" stroke-width="22" stroke-linecap="round"/>'
                 f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - r * .74:.1f}" stroke="{C["pearl"]}" stroke-width="14" stroke-linecap="round"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="20" fill="{C["gold"]}"/>', tone, 3)
    return avoid(out, 'clock')


def lamp_top(cx, cy, r=60, on=.35, tone=T):
    """Bedside lamp from above: a gold shade disc on a deep stand, with a dim glow."""
    g = ''
    if on:
        g = glow(f'<circle cx="{cx}" cy="{cy}" r="{r * 2.6}" fill="{C["gold"]}" fill-opacity="{on}"/>', 'l')
    stand = paper(f'<rect x="{cx - r * 1.6}" y="{cy - r * 1.6}" width="{r * 3.2}" height="{r * 3.2}" rx="12" fill="{C["deep"]}"/>', tone, 1)
    shade = paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["gold"]}"/><circle cx="{cx}" cy="{cy}" r="{r * .35}" fill="{C["sandLight"]}"/>', tone, 2)
    return g + avoid(stand + shade, 'lamp')


def led_hands(x, y):
    """Mum's pearl sleeve from the right edge, her big hand closed round his small
    hand; his teal pajama sleeve trails ahead, towards his own bed (left)."""
    kid = torn_strip([(x - 330, y - 50), (x - 60, y + 6)], 64, C['tealDeep'], T, seed=91, layer=2)
    arm = torn_strip([(1110, y + 250), (x + 70, y + 30)], 96, C['pearl'], T, seed=92, layer=3)
    palm = paper(f'<g transform="translate({x + 30} {y + 18}) rotate(22)">'
                 f'<rect x="-30" y="-50" width="110" height="100" rx="40" fill="{C["sandLight"]}"/>'
                 + ''.join(f'<rect x="-92" y="{-44 + n * 23}" width="{86 - abs(n - 1.5) * 10:.0f}" height="20" rx="10" fill="{C["sandLight"]}"/>' for n in range(4))
                 + f'<path d="M -84 -44 Q -60 -60 -30 -50" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".4" stroke-width="3"/>'
                 '</g>', T, 3)
    cuff = paper(f'<g transform="translate({x + 112} {y + 46}) rotate(22)"><rect x="-14" y="-56" width="34" height="112" rx="12" fill="{C["pearl"]}"/></g>', T, 3)
    small = paper(f'<g transform="translate({x - 64} {y + 4}) rotate(14)">'
                  f'<ellipse cx="0" cy="0" rx="40" ry="32" fill="{C["sandLight"]}"/>'
                  + ''.join(f'<rect x="10" y="{-26 + n * 15}" width="44" height="13" rx="6.5" fill="{C["sandLight"]}"/>' for n in range(4))
                  + f'<path d="M -30 -10 Q 0 -30 30 -14" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="3"/></g>', T, 3)
    return avoid(kid + arm + palm + cuff + small, 'hands')


def dotted_path(d, col=None, width=14):
    col = col or C['pearl']
    return paper(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{width}" stroke-linecap="round" stroke-dasharray="26 30" stroke-opacity=".8"/>', T, 1, 't')


def chair_top(cx, cy, s=1.0, mum=True):
    """A chair from above with mum sitting UP on it: seat, back bar, her shoulders
    and the back of her head (hair only), her hand on his bed edge."""
    tr = f'translate({cx} {cy}) scale({s})'
    out = paper(f'<rect x="-110" y="-110" width="220" height="220" rx="22" fill="{C["gold"]}"/>'
                f'<rect x="96" y="-120" width="40" height="240" rx="14" fill="{C["goldDeep"]}"/>', T, 1, T=tr)
    if mum:
        out += paper(f'<path d="M 120 -130 Q 20 -150 -10 -70 Q -30 0 -10 70 Q 20 150 120 130 Z" fill="{C["pearl"]}"/>', T, 2, T=tr)
        out += paper(f'<path d="M 10 -96 L -150 -70 L -150 -36 L 0 -50 Z" fill="{C["pearl"]}"/>'
                     f'<ellipse cx="-160" cy="-54" rx="34" ry="24" fill="{C["sandLight"]}"/>', T, 2, T=tr)
        out += paper(f'<ellipse cx="50" cy="0" rx="62" ry="70" fill="{C["ink"]}"/>', T, 3, T=tr)
    return avoid(out, 'chair')


def day_night(y=960, x0=110, x1=970, mark=0.22):
    """Torn horizontal strip: day on the right (sandLight, sun), night on the left
    (deep, moon). Small pearl moments along it, one marked with a gold tag."""
    xm = (x0 + x1) / 2
    out = torn_rect(xm, y, x1 - xm, 120, C['sandLight'], T, sides='tbr', seed=81, layer=1)
    out += torn_rect(x0, y, xm - x0, 120, C['deep'], T, sides='tbl', seed=82, layer=1)
    sx, sy = x1 - 90, y + 60
    rays = ''.join(f'<rect x="{sx - 6}" y="{sy - 66}" width="12" height="22" rx="5" transform="rotate({k * 45} {sx} {sy})" fill="{C["gold"]}"/>' for k in range(8))
    out += paper(f'<circle cx="{sx}" cy="{sy}" r="32" fill="{C["gold"]}"/>{rays}', T, 2)
    out += crescent(x0 + 80, y + 60, 36)
    mx = []
    for k in range(7):
        px = x1 - 190 - k * ((x1 - x0 - 320) / 6)
        mx.append(px)
        col = C['goldDeep'] if px > xm else C['pearl']
        out += paper(f'<circle cx="{px:.0f}" cy="{y + 60}" r="13" fill="{col}"/>', T, 2)
    tx = mx[5]
    out += torn_rect(tx - 40, y - 120, 80, 96, C['gold'], T, sides='tblr', seed=88, layer=3, rot=-4)
    out += paper(f'<rect x="{tx - 4}" y="{y - 30}" width="8" height="78" fill="{C["gold"]}"/>', T, 2)
    return avoid(out, 'strip')


# ---------------------------------------------------------------- slides
def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = big_bed(850, 1130, .3, tone='l', name='mini')
        return cta_end(ctx, mini_art=mini, tag_x=MX + 10, tag_y=1080)
    art, html = '', ''
    if s == 1:
        art = (crescent(170, 640, 56, layer=1)
               + lamp_top(980, 760, 46, on=.3)
               + big_bed(540, 1110, .86))
        html = hook_box(ctx, G, y=MT - 10, size=88, w=920, breaks=('؟ ',), keep=('سريرك صار نصه لطفلك؟', 'الساعة اثنين', 'ينام جنبك؟'))
    elif s == 2:
        steps = [(110 + k * 92, 1230 - k * 53, -30) for k in range(6)]
        art = (door_light(0, 900, 40, 450)
               + big_bed(810, 990, .5)
               + footsteps(steps, 1.15))
        html = body_box(ctx, G)
    elif s == 3:
        art = (crescent(880, 900, 50, layer=1) + sleepy_eyes(520, 1080, w=300, gap=150))
        html = body_box(ctx, G)
    elif s == 4:
        keep_in(ctx.t.segs, 'في وسط الليل')
        art = crescent(470, 660, 40, layer=1) + night_clock(260, 790, 120)
        html = body_box(ctx, G) + soft_cta(ctx, y=940)
    elif s == 5:
        art = (lamp_top(120, 700, 40, on=.18)
               + small_bed(230, 1060, .62, child=False)
               + dotted_path('M 1060 1250 C 860 1200, 640 1200, 400 1130')
               + led_hands(690, 1000))
        html = body_box(ctx, G)
    elif s == 6:
        art = (lamp_top(110, 640, 36, on=.15)
               + small_bed(330, 1020, .95)
               + chair_top(720, 1000, 1.0))
        html = body_box(ctx, G)
    elif s == 7:
        keep_in(ctx.t.segs, 'في الخطة الحية:')
        art = day_night(y=1000)
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
