"""p12 Phone calls. TealMist ground, ink text. Composition: TUG OF WAR.

A big phone across the middle, held high in mum's hand (a sandLight hand and a
deep sleeve from the right edge); a small hand (gold sleeve) reaches up from the
bottom-left for THE PHONE itself. Never a face.
s1: the tug: the small fingertips touch the phone's corner.
s2: the small hand tugs mum's sleeve; the phone tips; a wordless bubble from the call.
s3: metaphor: a toy car held high, the small hand far below it.
s4: the phone glowing with sound waves, right in front of him.
s5: an open box of crayons and stickers (only for calls).
s6: the phone flat on the table on speaker, far right; the small hand far left at the box.
s7: a sticker sheet and paper; the small hand presses a sticker on.
s8: CTA end, gold: the phone resting on the box, small, bottom-left.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, arc_pts, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'tealMist'
T = 'l'


# ---------------------------------------------------------------- motifs
def phone(cx, cy, s=1.0, rot=0, lit=True, tone=T, layer=2):
    """Smartphone, portrait: deep body, teal screen, three pearl voice bars, a gold call pill."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    body = (f'<rect x="-120" y="-220" width="240" height="440" rx="40" fill="{C["deep"]}"/>'
            f'<rect x="-40" y="-202" width="80" height="12" rx="6" fill="{C["night"]}"/>')
    scr = f'<rect x="-100" y="-176" width="200" height="360" rx="18" fill="{C["teal"] if lit else C["night"]}"/>'
    ui = ''
    if lit:
        ui = (''.join(f'<rect x="{-60 + k * 44}" y="{-60 - h_ / 2}" width="26" height="{h_}" rx="13" fill="{C["pearl"]}"/>'
                      for k, h_ in enumerate((50, 100, 70)))
              + f'<rect x="-56" y="110" width="112" height="44" rx="22" fill="{C["gold"]}"/>')
    return paper(body, tone, layer, T=tr) + paper(scr + ui, tone, layer, 't', T=tr)


def mum_hand(cx, cy, s=1.0, rot=0, tone=T):
    """Mum's hand gripping the phone's lower half from behind + deep sleeve going down-right.
    (cx, cy) = the phone centre it holds."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    sleeve = f'<path d="M -40 150 L 120 130 L 520 560 L 260 760 Z" fill="{C["deep"]}"/><path d="M -46 150 L 126 128 L 140 176 L -30 196 Z" fill="{C["night"]}"/>'
    palm = f'<path d="M -110 60 Q -120 190 -40 200 L 110 180 Q 150 120 120 50 Z" fill="{C["sandLight"]}"/>'
    thumb = f'<rect x="90" y="-10" width="46" height="120" rx="23" fill="{C["sandLight"]}" transform="rotate(-18 113 50)"/>'
    fingers = ''.join(f'<rect x="-150" y="{30 + n * 38}" width="70" height="34" rx="17" fill="{C["sandLight"]}"/>' for n in range(4))
    return (paper(sleeve, tone, 1, T=tr) + paper(palm + thumb, tone, 1, T=tr), paper(fingers, tone, 4, T=tr))


def held_phone(cx, cy, s=1.0, rot=0, lit=True, tone=T):
    back, front = mum_hand(cx, cy, s, rot, tone)
    return avoid(back + phone(cx, cy, s, rot, lit, tone) + front, 'phone')


def small_hand(x, y, s=1.0, rot=0, grab=False, tone=T):
    """A small open hand reaching UP (fingertips at (x, y)), gold sleeve below.
    rot tilts it (positive = leaning right). grab: fingers curled (a fist round something)."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    if grab:
        hand = (f'<rect x="-56" y="0" width="112" height="110" rx="40" fill="{C["sandLight"]}"/>'
                + ''.join(f'<rect x="{-54 + n * 28}" y="-6" width="26" height="40" rx="13" fill="{C["sandLight"]}"/>' for n in range(4))
                + f'<path d="M -50 40 H 50" stroke="{C["goldDeep"]}" stroke-opacity=".3" stroke-width="4"/>')
    else:
        lens = (80, 96, 90, 74)
        hand = ''.join(f'<rect x="{-50 + n * 26}" y="{100 - lens[n]}" width="22" height="{lens[n] + 20}" rx="11" fill="{C["sandLight"]}" '
                       f'transform="rotate({(n - 1.5) * 6} {-39 + n * 26} 110)"/>' for n in range(4))
        hand += f'<rect x="-58" y="96" width="112" height="110" rx="40" fill="{C["sandLight"]}"/>'
        hand += f'<rect x="-96" y="120" width="34" height="80" rx="17" fill="{C["sandLight"]}" transform="rotate(-38 -79 160)"/>'
    sleeve = f'<path d="M -66 190 L 64 190 L 74 900 L -76 900 Z" fill="{C["gold"]}"/><rect x="-70" y="184" width="140" height="34" rx="10" fill="{C["goldDeep"]}"/>'
    return avoid(paper(sleeve, tone, 3, T=tr) + paper(hand, tone, 4, T=tr), 'small')


def waves(cx, cy, r0, n=3, side='both', gap=44, width=14, tone=T, seed=0):
    """Plain paper sound arcs (deep/teal), on the left, right or both sides."""
    out = ''
    sides = {'both': ((150, 210), (-30, 30)), 'left': ((150, 210),), 'right': ((-30, 30),), 'up': ((-120, -60),)}[side]
    for a0, a1 in sides:
        for k in range(n):
            r = r0 + k * gap
            out += torn_strip(arc_pts(cx, cy, r, a0, a1, 16), width, C['deep'] if k % 2 else C['teal'], tone, seed=seed + k * 5 + a0, layer=2)
    return avoid(out, 'waves')


def bubble(cx, cy, w=230, h=130, tone=T, seed=7):
    """A wordless pearl speech bubble with three deep dots, tail down-left."""
    tail = f'<polygon points="{cx - w * .2:.1f},{cy + h / 2 - 8:.1f} {cx - w * .36:.1f},{cy + h / 2 + 50:.1f} {cx - w * .02:.1f},{cy + h / 2 - 8:.1f}" fill="{C["pearl"]}"/>'
    dots_ = ''.join(f'<circle cx="{cx + dx}" cy="{cy}" r="13" fill="{C["deep"]}"/>' for dx in (-50, 0, 50))
    return avoid(torn_rect(cx - w / 2, cy - h / 2, w, h, C['pearl'], tone, 'tblr', seed=seed, layer=3, amp=(4, 8), inner=tail + dots_), 'bubble')


def car(cx, cy, s=1.0, rot=0, tone=T):
    """Toy car, side view: gold body, deep windows, deep wheels with pearl hubs."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    body = (f'<path d="M -170 40 L -170 -10 Q -165 -40 -120 -44 L -70 -46 L -30 -110 L 80 -110 L 120 -46 L 160 -40 Q 180 -30 180 10 L 180 40 Z" fill="{C["gold"]}"/>'
            f'<path d="M -16 -96 L 26 -96 L 26 -50 L -46 -50 Z" fill="{C["deep"]}"/>'
            f'<path d="M 40 -96 L 74 -96 L 104 -50 L 40 -50 Z" fill="{C["deep"]}"/>'
            f'<rect x="150" y="-28" width="26" height="16" rx="6" fill="{C["pearl"]}"/>')
    wheels = ''.join(f'<circle cx="{x}" cy="44" r="44" fill="{C["ink"]}"/><circle cx="{x}" cy="44" r="18" fill="{C["pearl"]}"/>' for x in (-100, 110))
    return paper(body, tone, 2, T=tr) + paper(wheels, tone, 3, T=tr)


def big_hand_up(cx, cy, s=1.0, tone=T):
    """An adult hand from above-right holding something at (cx, cy) by its top."""
    tr = f'translate({cx} {cy}) scale({s})'
    g = (f'<path d="M 60 -150 L 600 -420 L 700 -260 L 160 -60 Z" fill="{C["deep"]}"/>'
         f'<path d="M -60 -150 Q -80 -230 20 -240 L 110 -230 Q 170 -190 150 -120 L 120 -90 Z" fill="{C["sandLight"]}"/>'
         + ''.join(f'<rect x="{-70 + n * 36}" y="-140" width="32" height="70" rx="16" fill="{C["sandLight"]}"/>' for n in range(4)))
    return paper(g, tone, 3, T=tr)


def crayon(x, y, L, col, rot, tone=T, w=36):
    """One crayon: coloured stick, pointed tip at the top, a paper wrapper band."""
    g = (f'<g transform="translate({x} {y}) rotate({rot})">'
         f'<rect x="{-w / 2}" y="0" width="{w}" height="{L}" rx="6" fill="{C[col]}"/>'
         f'<polygon points="{-w / 2},2 {w / 2},2 0,{-w * 1.1:.0f}" fill="{C[col]}"/>'
         f'<rect x="{-w / 2}" y="{L * .35:.0f}" width="{w}" height="{L * .3:.0f}" fill="{C["pearl"]}" fill-opacity=".55"/></g>')
    return g


def star(cx, cy, r, col):
    pts = []
    for k in range(10):
        a = math.radians(-90 + k * 36)
        rr = r if k % 2 == 0 else r * .45
        pts.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{C[col]}"/>'


def box(cx, base, s=1.0, tone=T, stickers=True):
    """The calls-only box, open: deep box, gold lid flipped back, crayons standing up, star stickers."""
    tr = f'translate({cx} {base}) scale({s})'
    lid = f'<path d="M -210 -230 L 210 -230 L 250 -400 L -170 -400 Z" fill="{C["gold"]}"/><path d="M -150 -380 L 220 -380" stroke="{C["goldDeep"]}" stroke-width="8" stroke-opacity=".5"/>'
    cr = ''.join(crayon(-150 + k * 60, -330 + (k % 2) * 30, 200, col, (k - 2.5) * 5)
                 for k, col in enumerate(('teal', 'gold', 'deep', 'goldDeep', 'tealDeep', 'gold')))
    front = (f'<path d="M -230 -230 L 230 -230 L 210 0 L -210 0 Z" fill="{C["deep"]}"/>'
             f'<rect x="-120" y="-150" width="240" height="64" rx="32" fill="{C["pearl"]}" fill-opacity=".9"/>'
             + star(-60, -118, 22, 'gold') + star(0, -118, 22, 'teal') + star(60, -118, 22, 'gold'))
    o = paper(lid, tone, 1, T=tr) + paper(cr, tone, 2, T=tr) + paper(front, tone, 3, T=tr)
    if stickers:
        st = (f'<rect x="250" y="-150" width="170" height="130" rx="10" fill="{C["pearl"]}" transform="rotate(8 335 -85)"/>'
              + star(300, -110, 26, 'gold') + star(370, -70, 26, 'teal') + f'<circle cx="300" cy="-50" r="20" fill="{C["deep"]}"/>')
        o += paper(st, tone, 3, T=tr)
    return avoid(o, 'box')


def table(y, x0=-20, x1=1100, tone=T):
    return avoid(paper(f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="60" fill="{C["sandLight"]}"/>'
                       f'<rect x="{x0}" y="{y + 52}" width="{x1 - x0}" height="14" fill="{C["goldDeep"]}" fill-opacity=".45"/>', tone, 1), 'table')


def phone_flat(cx, cy, s=1.0, tone=T):
    """The phone lying on the table, seen at a low angle: a flat slab, screen up and lit."""
    tr = f'translate({cx} {cy}) scale({s})'
    g = (f'<path d="M -200 0 L 160 0 L 200 -40 L -160 -40 Z" fill="{C["teal"]}"/>'
         f'<path d="M -200 0 L 160 0 L 160 22 L -200 22 Z" fill="{C["deep"]}"/>'
         f'<path d="M 160 0 L 200 -40 L 200 -18 L 160 22 Z" fill="{C["night"]}"/>')
    return paper(g, tone, 2, T=tr)


def sheet(cx, cy, s=1.0, tone=T):
    """A sheet of paper with stickers already stuck on, and a sticker sheet beside it."""
    tr = f'translate({cx} {cy}) scale({s})'
    paper_ = (f'<rect x="-230" y="-170" width="380" height="300" fill="{C["pearl"]}" transform="rotate(-5 -40 -20)"/>')
    stuck = star(-150, -90, 34, 'gold') + star(-40, -40, 30, 'teal') + f'<circle cx="60" cy="-100" r="28" fill="{C["deep"]}"/>' + star(-120, 50, 30, 'deep')
    ss = (f'<rect x="180" y="-120" width="170" height="230" rx="12" fill="{C["sandLight"]}" transform="rotate(7 265 -5)"/>'
          + ''.join(star(225 + (k % 2) * 80, -70 + (k // 2) * 70, 24, ('gold', 'teal', 'deep', 'gold', 'teal', 'gold')[k]) for k in range(5)))
    return avoid(paper(paper_, tone, 1, T=tr) + paper(stuck, tone, 2, T=tr) + paper(ss, tone, 2, T=tr), 'sheet')


# ---------------------------------------------------------------- slides
def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = (f'<g transform="translate(270 1250) scale(.5)">{box(0, 0)}</g>'
                + phone(330, 960, .5, rot=-14) + waves(330, 940, 140, n=2, side='left', gap=34, width=12, seed=3))
        return cta_end(ctx, mini_art=mini, tag_y=1090, tag_x=500)

    art, html = '', ''
    if s == 1:
        # the tug: phone high in mum's hand, small fingertips touching its corner
        art = (held_phone(720, 930, .95, rot=10)
               + small_hand(520, 1075, 1.0, rot=30))
        html = hook_box(ctx, G, y=MT - 10, size=92,
                        keep=('مع أمك', 'إلا لما', 'تدخلي الحمام', 'وتقفلي الباب؟'))
    elif s == 2:
        # he pulls her hand: the small fist on the sleeve, the phone tipping, a wordless bubble
        art = (held_phone(760, 960, .8, rot=24)
               + bubble(470, 820)
               + small_hand(690, 1130, .9, rot=-30, grab=True))
        html = body_box(ctx, G, y=MT)
    elif s == 3:
        # metaphor: a toy car held high out of reach, the small hand far below
        art = (big_hand_up(700, 640, 1.0) + car(700, 700, 1.05, rot=-6)
               + small_hand(330, 1080, 1.0, rot=12))
        html = body_box(ctx, G, y=MT)
    elif s == 4:
        # the phone right in front of him: lit, sound waves on both sides
        art = (held_phone(600, 820, 1.0, rot=0)
               + waves(600, 760, 190, n=3, side='both', gap=46, width=16, seed=11)
               + small_hand(250, 1120, .85, rot=18))
        html = body_box(ctx, G, y=MT)
    elif s == 5:
        # the calls-only box, open
        art = box(470, 1200, 1.0)
        html = body_box(ctx, G)
    elif s == 6:
        # the phone on speaker, on the table, far right; the small hand far left at the box
        art = (table(1080)
               + phone_flat(800, 1080, 1.0)
               + waves(800, 1020, 80, n=3, side='up', gap=40, width=14, seed=21)
               + f'<g transform="translate(250 1080) scale(.5)">{box(0, 0, stickers=False)}</g>'
               + small_hand(130, 980, .7, rot=10))
        html = body_box(ctx, G)
    elif s == 7:
        # stickers on paper, the small hand pressing one on
        art = (sheet(520, 1000, 1.1)
               + small_hand(380, 930, .8, rot=-14))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
