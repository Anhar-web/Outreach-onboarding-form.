"""b3p1 Sister's ملكة. Deep ground. Composition: DOORWAY GLOW.

A tall majlis doorway in the right half, warm gold light pouring out of it
across a dark corridor floor. People only from behind.
s1: mum's abaya from behind at the corridor end, a small child on her shoulder
    (back of the head), the glowing doorway behind.
s2: inside the glow: many abaya shapes, cups on a low table, noise arcs.
s3: the corridor: the door far right, the exit at the far left with a car
    outline, the pair standing by the car.
s4: the pair at the edge of the light (soft CTA above).
s5: two hands (big + small) holding, two small gold squeeze marks.
s6: the pair walking back toward the light, hand in hand.
s7: inside the glow: the pair seated at the dinner table.
End: gold, a mini doorway bottom-left.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, torn_poly, arc_pts, glow, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'deep'
T = 'd'
FY = 1150   # corridor floor line


# ---------------------------------------------------------------- motifs
def floor(y=FY):
    return torn_rect(-30, y, W + 60, H - y + 40, C['night'], T, sides='t', seed=5, layer=1)


def guests_in(x, w, base, n=2):
    """A few seated guests from behind at the bottom of a doorway (it is a room, not a panel)."""
    out = ''
    for k in range(n):
        gx = x + w * (k + .5) / n
        out += guest(gx, base, min(150, w * .55) * (1 if k % 2 == 0 else .88))
    return out


def doorway(x, y, w, h, spill=True, inside='', name='door', spill_to=None):
    """A tall doorway: warm gold light inside, a goldDeep frame, a flat pale-gold
    light spill thrown across the floor toward the lower-left."""
    out = ''
    if spill:
        bx0, bx1, by = x, x + w, y + h
        tx = spill_to if spill_to is not None else x - w * 1.6
        out += (f'<polygon points="{bx0},{by} {bx1},{by} {bx1 - w * .3:.0f},{H + 20} {tx:.0f},{H + 20}" '
                f'fill="{C["gold"]}" fill-opacity=".4"/>')
    out += glow(f'<rect x="{x - 30}" y="{y - 30}" width="{w + 60}" height="{h + 30}" fill="{C["gold"]}" fill-opacity=".8"/>', 'l')
    out += torn_rect(x, y, w, h, C['gold'], T, sides='', seed=61, layer=1,
                     inner=f'<rect x="{x + w * .12:.0f}" y="{y + h * .06:.0f}" width="{w * .76:.0f}" height="{h * .94:.0f}" fill="{C["sandLight"]}" fill-opacity=".45"/>' + inside)
    out += paper(f'<path d="M {x - 22} {y + h} V {y - 22} H {x + w + 22} V {y + h}" fill="none" stroke="{C["goldDeep"]}" stroke-width="30"/>', T, 3)
    return avoid(out, name)


def mum_back(cx, foot, h=600, carry=False, hand_to=None):
    """Mum from behind: scarf, shoulders, long abaya. carry: a small child on her
    right shoulder (back of a small head, a teal back, a small hand on her shoulder).
    hand_to=(x, y): her arm hangs down to a hand at that point."""
    r = h * .085
    top = foot - h
    d = (f'M {cx - h * .1} {top + r * 2.3} Q {cx - h * .2} {top + r * 2.6} {cx - h * .2} {top + h * .3} '
         f'L {cx - h * .27} {foot} L {cx + h * .27} {foot} L {cx + h * .2} {top + h * .3} '
         f'Q {cx + h * .2} {top + r * 2.6} {cx + h * .1} {top + r * 2.3} Z')
    out = paper(f'<path d="{d}" fill="{C["ink"]}"/><ellipse cx="{cx}" cy="{top + r * 1.25}" rx="{r * 1.1}" ry="{r * 1.3}" fill="{C["ink"]}"/>'
                f'<path d="M {cx} {top + r * 2.7} V {foot}" stroke="{C["tealDeep"]}" stroke-opacity=".45" stroke-width="6"/>', T, 2)
    if carry:
        kx, ky = cx + h * .19, top + r * 1.9
        kid = (f'<path d="M {kx - h * .12} {ky + h * .08} Q {kx - h * .13} {ky + h * .02} {kx - h * .04} {ky} L {kx + h * .06} {ky} '
               f'Q {kx + h * .15} {ky + h * .02} {kx + h * .14} {ky + h * .1} L {kx + h * .12} {ky + h * .3} L {kx - h * .1} {ky + h * .3} Z" fill="{C["teal"]}"/>'
               f'<path d="M {kx - h * .09} {ky + h * .06} Q {kx - h * .2} {ky + h * .1} {kx - h * .2} {ky + h * .18}" fill="none" stroke="{C["teal"]}" stroke-width="{h * .055:.0f}" stroke-linecap="round"/>'
               f'<circle cx="{kx - h * .2}" cy="{ky + h * .2}" r="{h * .032:.0f}" fill="{C["sandLight"]}"/>')
        head = (f'<circle cx="{kx}" cy="{ky - h * .04}" r="{h * .085:.0f}" fill="{C["goldDeep"]}"/>'
                f'<ellipse cx="{kx - h * .085}" cy="{ky - h * .03}" rx="{h * .014:.0f}" ry="{h * .025:.0f}" fill="{C["sandLight"]}"/>'
                f'<ellipse cx="{kx + h * .085}" cy="{ky - h * .03}" rx="{h * .014:.0f}" ry="{h * .025:.0f}" fill="{C["sandLight"]}"/>')
        arm = (f'<path d="M {cx + h * .2} {top + h * .3} Q {cx + h * .26} {ky + h * .33} {kx} {ky + h * .3} L {kx - h * .06} {ky + h * .29}" '
               f'fill="none" stroke="{C["ink"]}" stroke-width="{h * .075:.0f}" stroke-linecap="round"/>'
               f'<ellipse cx="{kx - h * .09}" cy="{ky + h * .28}" rx="{h * .05:.0f}" ry="{h * .035:.0f}" fill="{C["sandLight"]}"/>')
        out += paper(kid, T, 3) + paper(head, T, 3) + paper(arm, T, 3)
    if hand_to:
        hx, hy = hand_to
        out += paper(f'<path d="M {cx + h * .15} {top + h * .2} Q {cx + h * .24} {top + h * .32} {hx} {hy - 30}" fill="none" '
                     f'stroke="{C["ink"]}" stroke-width="{h * .085:.0f}" stroke-linecap="round"/>'
                     f'<circle cx="{hx}" cy="{hy}" r="{h * .05:.0f}" fill="{C["sandLight"]}"/>', T, 3)
    return out


def kid_back(cx, foot, s=1.0, arm_up='left'):
    """A small child standing, from behind: back of the head, teal top, one arm up."""
    tr = f'translate({cx} {foot}) scale({s})'
    up_x = -98 if arm_up == 'left' else 64
    rot = 28 if arm_up == 'left' else -28
    other_x = 64 if arm_up == 'left' else -98
    g = (f'<rect x="-36" y="-150" width="30" height="130" rx="12" fill="{C["tealDeep"]}"/>'
         f'<rect x="6" y="-150" width="30" height="130" rx="12" fill="{C["tealDeep"]}"/>'
         f'<rect x="-50" y="-30" width="48" height="30" rx="14" fill="{C["pearl"]}"/>'
         f'<rect x="2" y="-30" width="48" height="30" rx="14" fill="{C["pearl"]}"/>'
         f'<path d="M -70 -150 L -60 -320 Q -55 -350 -20 -352 L 20 -352 Q 55 -350 60 -320 L 70 -150 Z" fill="{C["teal"]}"/>'
         f'<rect x="{up_x}" y="-440" width="34" height="130" rx="16" fill="{C["teal"]}" transform="rotate({rot} {up_x + 17} -320)"/>'
         f'<rect x="{other_x}" y="-340" width="34" height="160" rx="16" fill="{C["teal"]}" transform="rotate({-8 if arm_up == "left" else 8} {other_x + 17} -340)"/>'
         f'<rect x="-18" y="-370" width="36" height="30" fill="{C["sandLight"]}"/>')
    head = (f'<circle cx="0" cy="-420" r="62" fill="{C["goldDeep"]}"/><ellipse cx="-62" cy="-410" rx="10" ry="16" fill="{C["sandLight"]}"/>'
            f'<ellipse cx="62" cy="-410" rx="10" ry="16" fill="{C["sandLight"]}"/>')
    return paper(g, T, 2, T=tr) + paper(head, T, 3, T=tr)


def guest(cx, base, h, seed=0):
    """A seated guest from behind inside the glow: ink head-scarf + shoulders."""
    r = h * .2
    return paper(f'<path d="M {cx - h * .42} {base} Q {cx - h * .42} {base - h * .55} {cx} {base - h * .6} Q {cx + h * .42} {base - h * .55} {cx + h * .42} {base} Z" fill="{C["ink"]}"/>'
                 f'<ellipse cx="{cx}" cy="{base - h * .72}" rx="{r}" ry="{r * 1.15}" fill="{C["ink"]}"/>', T, 2)


def cup(cx, base, s=1.0):
    """A small finjan: a pearl trapezoid on a tiny saucer."""
    return paper(f'<path d="M {cx - 22 * s} {base - 40 * s} L {cx + 22 * s} {base - 40 * s} L {cx + 15 * s} {base - 6 * s} L {cx - 15 * s} {base - 6 * s} Z" fill="{C["pearl"]}"/>'
                 f'<rect x="{cx - 30 * s}" y="{base - 8 * s}" width="{60 * s}" height="{8 * s}" rx="4" fill="{C["tealMist"]}"/>', T, 3)


def noise(cx, cy, r0, n=3, seed=0, span=60):
    out = ''
    for k in range(n):
        for a0 in (-90 - span - 20, -90 + 20):
            out += torn_strip(arc_pts(cx, cy, r0 + k * 46, a0, a0 + span, 14), 16 - k * 2,
                              C['pearl'] if k % 2 == 0 else C['teal'], T, seed=seed + k * 5 + int(a0), layer=3)
    return out


def car_outline(cx, base, s=1.0):
    """A car in side view as a pearl torn-strip outline + two wheels."""
    pts = [(-190, -40), (-190, -80), (-120, -90), (-70, -150), (70, -150), (120, -90), (190, -80), (190, -40)]
    pts = [(cx + x * s, base + y * s) for x, y in pts]
    out = torn_strip(pts + [pts[0]], 14 * s, C['pearl'], T, seed=91, layer=2, core=False)
    out += torn_strip([(cx - 10 * s, base - 148 * s), (cx - 10 * s, base - 92 * s)], 10 * s, C['pearl'], T, seed=92, layer=2, core=False)
    out += torn_strip([(cx - 120 * s, base - 92 * s), (cx + 120 * s, base - 92 * s)], 10 * s, C['pearl'], T, seed=93, layer=2, core=False)
    out += ''.join(torn_circle(cx + wx * s, base - 30 * s, 36 * s, C['ink'], T, seed=94 + k, layer=3,
                               inner=f'<circle cx="{cx + wx * s}" cy="{base - 30 * s}" r="{12 * s}" fill="{C["pearl"]}"/>')
                   for k, wx in enumerate((-110, 110)))
    return out


def clasp(cx, cy, s=1.0):
    """Mum's big hand (pearl sleeve, from the right) closed round a small hand
    (teal sleeve, from the left). Two small gold squeeze marks over the grip."""
    tr = f'translate({cx} {cy}) scale({s})'
    small = (f'<path d="M -900 -40 L -120 -44 L -110 46 L -900 54 Z" fill="{C["teal"]}"/>'
             f'<rect x="-140" y="-48" width="30" height="100" rx="10" fill="{C["tealDeep"]}"/>'
             f'<rect x="-116" y="-40" width="120" height="84" rx="34" fill="{C["sandLight"]}"/>')
    big_back = (f'<path d="M 900 -90 L 170 -78 L 170 90 L 900 104 Z" fill="{C["pearl"]}"/>'
                f'<rect x="150" y="-84" width="40" height="176" rx="12" fill="{C["tealMist"]}"/>'
                f'<path d="M 170 -70 Q 40 -90 -20 -40 L -10 70 Q 60 96 170 80 Z" fill="{C["sandLight"]}"/>')
    big_fingers = (''.join(f'<rect x="{-70 + n * 6}" y="{-30 + n * 26}" width="{120 - n * 8}" height="26" rx="13" fill="{C["sandLight"]}" />' for n in range(4))
                   + f'<path d="M -20 -60 Q -90 -70 -100 -30" fill="none" stroke="{C["sandLight"]}" stroke-width="34" stroke-linecap="round"/>'
                   + ''.join(f'<path d="M {-60 + n * 6} {-4 + n * 26} H {40 - n * 2}" stroke="{C["goldDeep"]}" stroke-opacity=".3" stroke-width="4"/>' for n in range(3)))
    small_tips = (''.join(f'<rect x="{-52 + n * 24}" y="80" width="22" height="44" rx="11" fill="{C["sandLight"]}"/>' for n in range(4))
                  + f'<rect x="-64" y="-86" width="70" height="30" rx="15" fill="{C["sandLight"]}" transform="rotate(-12 -30 -70)"/>'
                  + ''.join(f'<path d="M {-46 + n * 24} 116 V 100" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="4"/>' for n in range(4)))
    out = paper(small, T, 2, T=tr) + paper(big_back, T, 2, T=tr) + paper(small_tips, T, 2, T=tr) + paper(big_fingers, T, 3, T=tr)
    # two squeeze marks: short gold arcs over the grip
    for k, (a0, a1) in enumerate(((-128, -104), (-76, -52))):
        out += torn_strip(arc_pts(cx - 10 * s, cy, 170 * s, a0, a1, 10), 20 * s, C['gold'], T, seed=120 + k, layer=3)
        out += torn_strip(arc_pts(cx - 10 * s, cy, 220 * s, a0 + 4, a1 - 4, 10), 14 * s, C['gold'], T, seed=130 + k, layer=3)
    return avoid(out, 'hands')


def table(x0, x1, y, plates=4):
    out = torn_rect(x0, y, x1 - x0, 30, C['tealDeep'], T, sides='tb', seed=71, layer=2)
    for k in range(plates):
        px = x0 + (k + .5) * (x1 - x0) / plates
        out += paper(f'<ellipse cx="{px}" cy="{y - 6}" rx="56" ry="16" fill="{C["pearl"]}"/>'
                     f'<ellipse cx="{px}" cy="{y - 12}" rx="34" ry="9" fill="{C["sandLight"]}"/>', T, 3)
    return out


# ---------------------------------------------------------------- slides
def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = (f'<g transform="translate(70 900) scale(.42)">'
                f'{doorway(160, 300, 300, 560, spill=False, name="mini")}</g>')
        return cta_end(ctx, mini_art=mini, tag_y=1050, tag_x=W - MX - 500)
    art, html = '', ''
    if s == 1:
        art = (floor() + doorway(680, 770, 240, FY - 770, spill_to=250, inside=guests_in(680, 240, FY, 2))
               + avoid(mum_back(330, 1360, 640, carry=True), 'mum'))
        html = hook_box(ctx, G, y=MT - 20, size=88, w=888,
                        breaks=('ساعتين ', 'أختك، ', 'طلعتي ', 'العشا '))
    elif s == 2:
        inside = ''
        for k, (gx, gh) in enumerate(((200, 240), (330, 270), (470, 230), (610, 280), (760, 250), (890, 230))):
            inside += guest(gx, 1150, gh, seed=k)
        inside += torn_rect(110, 1120, 860, 30, C['tealDeep'], T, sides='tb', seed=72, layer=3)
        inside += ''.join(cup(cx, 1120, 1.1) for cx in (190, 300, 420, 560, 700, 840))
        art = avoid(torn_rect(90, 720, 900, 520, C['gold'], T, sides='', seed=70, layer=1)
                    + paper(f'<path d="M 68 1240 V 698 H 1012 V 1240" fill="none" stroke="{C["goldDeep"]}" stroke-width="30"/>', T, 3)
                    + inside + noise(330, 900, 70, 2, seed=1) + noise(760, 890, 70, 2, seed=9), 'room')
        html = body_box(ctx, G)
    elif s == 3:
        exit_ = (torn_rect(110, 800, 380, FY - 800, C['night'], T, sides='', seed=81, layer=1,
                           inner=f'<rect x="110" y="{FY - 120}" width="380" height="120" fill="{C["ink"]}" fill-opacity=".5"/>')
                 + paper(f'<path d="M 92 {FY} V 782 H 508 V {FY}" fill="none" stroke="{C["tealMist"]}" stroke-opacity=".7" stroke-width="18"/>', T, 2))
        art = (floor() + doorway(760, 760, 200, FY - 760, spill_to=520, inside=guests_in(760, 200, FY, 2))
               + avoid(exit_ + car_outline(240, FY - 10, .75) + mum_back(410, FY + 10, 330, carry=True), 'exit'))
        html = body_box(ctx, G)
    elif s == 4:
        art = (floor(1180) + doorway(730, 850, 210, 1180 - 850, spill_to=300, inside=guests_in(730, 210, 1180, 2))
               + avoid(mum_back(380, 1330, 470, carry=True), 'mum'))
        html = body_box(ctx, G) + soft_cta(ctx, y=640)
    elif s == 5:
        lead = ctx.t.body()[0]
        lab, _ = ctx.t.split_seg(lead, 'الضغطة السرية: ')
        lab.role = 'label'
        art = clasp(560, 1020, 1.25)
        html = body_box(ctx, G)
    elif s == 6:
        art = (floor() + doorway(700, 700, 260, FY - 700, spill_to=60, inside=guests_in(700, 260, FY, 2))
               + avoid(mum_back(250, 1300, 560, hand_to=(395, 1010)) + kid_back(450, 1300, .82, arm_up='left'), 'pair'))
        html = body_box(ctx, G)
    elif s == 7:
        inside = (guest(250, 1180, 230) + guest(800, 1180, 250)
                  + mum_back(470, 1200, 330) + kid_back(620, 1200, .55, arm_up='left')
                  + table(140, 940, 1210, 4))
        art = (floor(1200) + doorway(120, 700, 840, 1200 - 700, spill=False, inside=inside, name='room'))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
