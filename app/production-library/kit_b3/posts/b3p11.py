"""b3p11 Mall hand dryer. Night ground. Composition: WALL-TILE GRID MACRO.

A thin pearl-teal tile grid covers the wall; one BIG wall-mounted hand dryer
(pearl box, ink nozzle, gold button), its sound as torn gold arcs.
s1: the dryer roaring (big arcs); two wet hands cupped over the ears of a small
    head seen from behind.
s2: mum's wet hands dripping, the dryer still roaring.
s3: the dryer alone, a sudden jagged burst (soft CTA above).
s4: a door frame, the dryer small inside; a small hand pointing at it.
s5: a small hand under the dryer, arcs small; mum's hands up in mock surprise.
s6: the door, two pairs of feet waiting outside, faint arcs from inside.
s7: two dryers side by side: steady loud arcs vs one sudden burst.
End: gold, a mini dryer bottom-right.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, torn_poly, arc_pts, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'night'
T = 'd'


# ---------------------------------------------------------------- motifs
def tiles(y0=0, x0=0, x1=W, y1=H, step=135, op=.13):
    """Thin tile grid over the wall (not paper: grout lines)."""
    lines = ''.join(f'<path d="M {x} {y0} V {y1}" />' for x in range(x0 + 30, x1, step))
    lines += ''.join(f'<path d="M {x0} {y} H {x1}" />' for y in range(y0 + 50, y1, step))
    return f'<g stroke="{C["tealMist"]}" stroke-opacity="{op}" stroke-width="3" fill="none">{lines}</g>'


def dryer(cx, cy, s=1.0, on=True, name='dryer'):
    """Wall hand dryer, front view: pearl box, tealMist front panel, ink nozzle
    slot at the bottom, a gold button. (cx, cy) = box centre. on: air below."""
    tr = f'translate({cx} {cy}) scale({s})'
    box = (f'<rect x="-190" y="-150" width="380" height="300" rx="56" fill="{C["pearl"]}"/>'
           f'<rect x="-150" y="-112" width="300" height="150" rx="30" fill="{C["tealMist"]}"/>'
           + ''.join(f'<rect x="-110" y="{-84 + k * 30}" width="220" height="12" rx="6" fill="{C["tealDeep"]}" fill-opacity=".45"/>' for k in range(4))
           + f'<circle cx="120" cy="92" r="24" fill="{C["gold"]}"/>')
    nozzle = (f'<path d="M -120 140 L 90 140 L 70 200 Q 66 214 52 214 L -102 214 Q -116 214 -120 200 Z" fill="{C["ink"]}"/>'
              f'<rect x="-96" y="196" width="160" height="12" rx="6" fill="{C["night"]}"/>')
    out = paper(f'<rect x="-206" y="-166" width="412" height="332" rx="64" fill="{C["tealDeep"]}"/>', T, 1, T=tr)
    out += paper(box, T, 2, T=tr) + paper(nozzle, T, 3, T=tr)
    if on:
        for k in range(5):
            x0 = cx + (-88 + k * 34) * s
            out += torn_strip([(x0, cy + 225 * s), (x0 - 6 * s, cy + (330 + (k % 2) * 40) * s)], 12 * s,
                              C['tealMist'] if k % 2 else C['pearl'], T, seed=200 + k, layer=2)
    return avoid(out, name)


def arcs(cx, cy, r0, n=3, gap=60, width=22, sides=('l', 'r'), span=56, seed=0, col='gold'):
    """Torn gold sound arcs either side of a source."""
    out = ''
    for sd in sides:
        a0, a1 = (180 - span / 2, 180 + span / 2) if sd == 'l' else (-span / 2, span / 2)
        for k in range(n):
            out += torn_strip(arc_pts(cx, cy, r0 + k * gap, a0, a1, 16), width - k * 3,
                              C[col] if k % 2 == 0 else C['goldDeep'], T, seed=seed + k * 7 + len(sd), layer=2)
    return avoid(out, 'arcs')


def burst(cx, cy, r0=40, r1=130, n=9, seed=300):
    """A sudden jagged burst: short torn strips radiating from a point."""
    out = ''
    for k in range(n):
        a = math.radians(-90 + k * 360 / n + (k % 2) * 8)
        rr = r1 * (1 if k % 2 == 0 else .72)
        out += torn_strip([(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + rr * math.cos(a), cy + rr * math.sin(a))],
                          18, C['gold'] if k % 2 == 0 else C['goldDeep'], T, seed=seed + k, layer=2)
    return avoid(out, 'burst')


def drops(pts, r=14, col='teal'):
    return ''.join(paper(f'<path d="M {x} {y - r * 1.6} Q {x + r} {y - r * .2} {x} {y + r} Q {x - r} {y - r * .2} {x} {y - r * 1.6} Z" fill="{C[col]}"/>', T, 1)
                   for (x, y) in pts)


def small_head_ears(cx, cy, r=150):
    """Back of a small head (no face), shoulders below; two wet hands cupped over
    the ears, mum's pearl sleeves running down-out to the frame edges."""
    out = paper(f'<path d="M {cx - r * 1.6} {cy + r * 2.4} Q {cx - r * 1.5} {cy + r * 1.05} {cx} {cy + r} '
                f'Q {cx + r * 1.5} {cy + r * 1.05} {cx + r * 1.6} {cy + r * 2.4} Z" fill="{C["teal"]}"/>'
                f'<rect x="{cx - r * .3}" y="{cy + r * .55}" width="{r * .6}" height="{r * .6}" rx="{r * .2}" fill="{C["sandLight"]}"/>', T, 1)
    out += paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["goldDeep"]}"/>', T, 2)
    for sd in (-1, 1):
        hx, hy = cx + sd * r * 1.0, cy + r * .1
        g = (f'<g transform="translate({hx} {hy}) rotate({sd * -14})">'
             f'<path d="M {sd * 10} 40 L {sd * 130} 600 L {sd * 330} 600 L {sd * 110} 40 Z" fill="{C["pearl"]}"/>'
             f'<rect x="{-30 + sd * 50}" y="30" width="80" height="40" rx="12" fill="{C["tealMist"]}"/>'
             f'<rect x="-54" y="-40" width="108" height="110" rx="40" fill="{C["sandLight"]}"/>'
             + ''.join(f'<rect x="{-50 + n * 26}" y="{-118 + abs(n - 1.5) * 12:.0f}" width="22" height="110" rx="11" fill="{C["sandLight"]}" transform="rotate({(n - 1.5) * 5} {-39 + n * 26} 0)"/>' for n in range(4))
             + f'<rect x="{-sd * 70 - 17}" y="-20" width="34" height="84" rx="17" fill="{C["sandLight"]}" transform="rotate({sd * 30} {-sd * 70} 20)"/>'
             + '</g>')
        out += paper(g, T, 3)
    out += drops([(cx - r * 1.3, cy + r * .9), (cx + r * 1.35, cy + r * 1.0), (cx - r * 1.1, cy + r * 1.35)], r=12)
    return avoid(out, 'head')


def flat_hand(x, y, s=1.0, side='right', sleeve='pearl', cuff='tealMist', rot=0, name='hand'):
    """A flat hand coming in from the side edge, fingers pointing inward (palm down)."""
    sx = -1 if side == 'right' else 1
    tr = f'translate({x} {y}) scale({sx * s} {s}) rotate({rot})'
    g = (f'<path d="M -900 -60 L -90 -54 L -90 54 L -900 64 Z" fill="{C[sleeve]}"/>'
         f'<rect x="-112" y="-60" width="36" height="120" rx="10" fill="{C[cuff]}"/>')
    hand = (f'<path d="M -90 -46 L 20 -50 Q 40 -50 40 -30 L 40 40 Q 40 50 20 50 L -90 46 Z" fill="{C["sandLight"]}"/>'
            + ''.join(f'<rect x="20" y="{-48 + n * 24}" width="{110 - abs(n - 1.3) * 16:.0f}" height="22" rx="11" fill="{C["sandLight"]}"/>' for n in range(4))
            + f'<rect x="-40" y="34" width="90" height="26" rx="13" fill="{C["sandLight"]}" transform="rotate(16 -40 47)"/>')
    return avoid(paper(g, T, 2, T=tr) + paper(hand, T, 3, T=tr), name)


def hand_up(x, y, s=1.0, rot=0, sleeve='teal', cuff='tealDeep', point=False, spread=False, name='small'):
    """A hand reaching UP, fingertips at (x, y), sleeve running down out of frame.
    point: index finger only. spread: fingers fanned (mock surprise)."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    if point:
        hand = (f'<rect x="-14" y="0" width="26" height="120" rx="13" fill="{C["sandLight"]}"/>'
                f'<rect x="-56" y="86" width="112" height="120" rx="40" fill="{C["sandLight"]}"/>'
                f'<rect x="-92" y="116" width="34" height="76" rx="17" fill="{C["sandLight"]}" transform="rotate(-38 -75 154)"/>')
    else:
        lens = (80, 96, 90, 74)
        fan = 16 if spread else 6
        hand = ''.join(f'<rect x="{-50 + n * 26}" y="{100 - lens[n]}" width="22" height="{lens[n] + 20}" rx="11" fill="{C["sandLight"]}" '
                       f'transform="rotate({(n - 1.5) * fan} {-39 + n * 26} 110)"/>' for n in range(4))
        hand += f'<rect x="-58" y="96" width="112" height="110" rx="40" fill="{C["sandLight"]}"/>'
        hand += f'<rect x="-96" y="120" width="34" height="80" rx="17" fill="{C["sandLight"]}" transform="rotate({-50 if spread else -38} -79 160)"/>'
    sl = (f'<path d="M -66 190 L 64 190 L 74 900 L -76 900 Z" fill="{C[sleeve]}"/>'
          f'<rect x="-70" y="184" width="140" height="34" rx="10" fill="{C[cuff]}"/>')
    return avoid(paper(sl, T, 2, T=tr) + paper(hand, T, 3, T=tr), name)


def doorway(x, y, w, h, inside=''):
    """A door frame (goldDeep strips) on the wall; inside a deep tiled room."""
    room = torn_rect(x, y, w, h, C['deep'], T, sides='', seed=60, layer=1,
                     inner=f'<g clip-path="none">{tiles(int(y), int(x), int(x + w), int(y + h), step=70, op=.18)}</g>')
    frame = paper(f'<path d="M {x - 26} {y + h + 40} V {y - 26} H {x + w + 26} V {y + h + 40}" fill="none" stroke="{C["goldDeep"]}" stroke-width="34"/>', T, 3)
    return avoid(room + inside + frame, 'door')


def mum_back(cx, foot, h=600):
    """Mum from behind: head with a scarf, shoulders, a long abaya, gold shoe heels;
    her left arm hangs down toward the small hand."""
    r = h * .085
    top = foot - h
    d = (f'M {cx - h * .1} {top + r * 2.3} Q {cx - h * .2} {top + r * 2.6} {cx - h * .2} {top + h * .3} '
         f'L {cx - h * .27} {foot - 20} L {cx + h * .27} {foot - 20} L {cx + h * .2} {top + h * .3} '
         f'Q {cx + h * .2} {top + r * 2.6} {cx + h * .1} {top + r * 2.3} Z')
    shoes = ''.join(f'<rect x="{cx + dx - 34}" y="{foot - 34}" width="68" height="34" rx="14" fill="{C["gold"]}"/>' for dx in (-60, 60))
    body = (f'<path d="{d}" fill="{C["ink"]}"/><ellipse cx="{cx}" cy="{top + r * 1.25}" rx="{r * 1.1}" ry="{r * 1.3}" fill="{C["ink"]}"/>'
            f'<path d="M {cx} {top + r * 2.6} V {foot - 30}" stroke="{C["tealDeep"]}" stroke-opacity=".5" stroke-width="6"/>')
    arm = (f'<path d="M {cx + h * .14} {top + h * .2} Q {cx + h * .24} {top + h * .3} {cx + h * .2} {top + h * .42}" fill="none" '
           f'stroke="{C["ink"]}" stroke-width="54" stroke-linecap="round"/>'
           f'<circle cx="{cx + h * .2}" cy="{top + h * .47}" r="30" fill="{C["sandLight"]}"/>')
    return paper(shoes, T, 1) + paper(body, T, 2) + paper(arm, T, 3)


def small_back(cx, foot, s=1.0):
    """A small child standing, from behind: back of the head, shirt, one arm up to mum."""
    tr = f'translate({cx} {foot}) scale({s})'
    g = (f'<rect x="-36" y="-150" width="30" height="130" rx="12" fill="{C["tealDeep"]}"/>'
         f'<rect x="6" y="-150" width="30" height="130" rx="12" fill="{C["tealDeep"]}"/>'
         f'<rect x="-50" y="-30" width="48" height="30" rx="14" fill="{C["pearl"]}"/>'
         f'<rect x="2" y="-30" width="48" height="30" rx="14" fill="{C["pearl"]}"/>'
         f'<path d="M -70 -150 L -60 -320 Q -55 -350 -20 -352 L 20 -352 Q 55 -350 60 -320 L 70 -150 Z" fill="{C["teal"]}"/>'
         f'<rect x="-98" y="-420" width="34" height="120" rx="16" fill="{C["teal"]}" transform="rotate(-28 -81 -300)"/>'
         f'<rect x="64" y="-340" width="34" height="160" rx="16" fill="{C["teal"]}" transform="rotate(-8 81 -340)"/>'
         f'<circle cx="92" cy="-176" r="20" fill="{C["sandLight"]}"/>'
         f'<rect x="-18" y="-370" width="36" height="30" fill="{C["sandLight"]}"/>')
    head = (f'<circle cx="0" cy="-420" r="62" fill="{C["goldDeep"]}"/><ellipse cx="-62" cy="-410" rx="10" ry="16" fill="{C["sandLight"]}"/>'
            f'<ellipse cx="62" cy="-410" rx="10" ry="16" fill="{C["sandLight"]}"/>')
    return paper(g, T, 2, T=tr) + paper(head, T, 3, T=tr)


def floor(y=1180):
    return avoid(torn_rect(-30, y, W + 60, H - y + 40, C['deep'], T, sides='t', seed=81, layer=1), 'floor')


# ---------------------------------------------------------------- slides
def slide(ctx):
    s = ctx.s
    ground = tiles()
    if ctx.last:
        mini = f'<g transform="translate(860 1110) scale(.42)">{dryer(0, 0, 1.0, on=True, name="mini")}{arcs(0, 0, 260, 2, 60, 26, seed=5)}</g>'
        out = cta_end(ctx, mini_art=mini, tag_y=1030, tag_x=MX + 10)
        return out
    art, html = '', ''
    if s == 1:
        art = (dryer(300, 930, .9) + arcs(300, 930, 225, 3, 54, 24, seed=1, span=50)
               + small_head_ears(770, 1200, 145))
        html = hook_box(ctx, G, y=MT - 20, size=88, w=920,
                        breaks=('طفل ', 'اشتغلت ', 'المول ', 'الحمام '))
    elif s == 2:
        art = (dryer(290, 860, .85) + arcs(290, 860, 225, 3, 52, 22, seed=11)
               + flat_hand(700, 1010, 1.0, side='right', rot=8, name='hand1')
               + flat_hand(740, 1170, 1.0, side='right', rot=-6, name='hand2')
               + drops([(600, 1090), (640, 1140), (560, 1240), (660, 1260), (610, 1300)], r=13))
        html = body_box(ctx, G)
    elif s == 3:
        art = dryer(540, 1060, .9, on=False) + burst(870, 1000, 45, 120, seed=300) + burst(210, 1000, 45, 120, seed=320)
        html = body_box(ctx, G) + soft_cta(ctx, y=660)
    elif s == 4:
        inside = dryer(760, 900, .36, on=False, name='dryer_in')
        art = doorway(600, 760, 330, 600, inside) + hand_up(330, 900, 1.05, rot=24, point=True)
        html = body_box(ctx, G)
    elif s == 5:
        art = (dryer(330, 830, .85, on=True) + arcs(330, 830, 215, 1, 50, 20, seed=40)
               + hand_up(320, 1110, .85, rot=-4)
               + hand_up(700, 930, 1.25, rot=-16, sleeve='pearl', cuff='tealMist', spread=True, name='mum1')
               + hand_up(910, 960, 1.25, rot=14, sleeve='pearl', cuff='tealMist', spread=True, name='mum2'))
        html = body_box(ctx, G)
    elif s == 6:
        inside = dryer(760, 900, .36, on=True, name='dryer_in') + arcs(760, 900, 100, 2, 30, 12, seed=60)
        art = (floor(1200) + doorway(600, 760, 330, 470, inside)
               + avoid(mum_back(230, 1216, 560) + small_back(445, 1216, .78), 'pair'))
        html = body_box(ctx, G)
    elif s == 7:
        art = (dryer(290, 1000, .62) + arcs(290, 1000, 165, 3, 40, 18, seed=70)
               + dryer(790, 1000, .62, on=False, name='dryer2') + burst(790, 1000 - 150, 30, 110, seed=340))
        html = body_box(ctx, G)
    return {'ground': G, 'art': ground + art, 'html': html}
