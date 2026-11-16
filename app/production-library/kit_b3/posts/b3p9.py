"""b3p9 Hearing "no" (F6 checklist). Deep ground. Composition: HIGH SHELF.

A tall wood wardrobe edge stands on the right, a teal biscuit packet on top of
it, out of reach; small hands live at the bottom of the frame. Across the
slides: s1 the packet high, a small hand far below already holding a biscuit
(the cost landed); s2 the fridge ajar and a small figure flat on the floor;
s3 the packet high, a small hand reaching; s4 a ball and blocks laid out on a
mat (prepared before he asks); s5 a pearl hand putting the packet back on top;
s6 big + small hand walking toward the blocks; s7 the shelf, the packet, calm.
End: gold, a mini packet.
"""
import math
from kit import C, MX, MT, W, H, keep_in, brk, paper, torn_strip, torn_rect, torn_circle, torn_poly, glow, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'deep'
T = 'd'


def wardrobe(x0, top, seed=3):
    """A tall wood wardrobe edge running off the right and bottom of the frame."""
    w = W + 40 - x0
    out = paper(f'<rect x="{x0}" y="{top}" width="{w}" height="{H + 40 - top}" fill="{C["goldDeep"]}"/>'
                f'<rect x="{x0 - 22}" y="{top - 4}" width="{w + 22}" height="34" fill="{C["gold"]}"/>'
                f'<rect x="{x0 + 34}" y="{top + 70}" width="{w - 34}" height="{H - top}" rx="8" fill="{C["gold"]}" fill-opacity=".18"/>'
                f'<rect x="{x0 + 70}" y="{top + 300}" width="16" height="110" rx="8" fill="{C["sandLight"]}"/>', T, 1)
    return avoid(out, 'wardrobe')


def biscuit(cx, cy, r, seed=1, layer=2, bite=True):
    """A chocolate-chip biscuit: sand disc, a bite out of the top-right edge,
    a few scattered dark chips (irregular, so nothing reads as a face)."""
    chips = ''.join(f'<ellipse cx="{cx + r * dx:.1f}" cy="{cy + r * dy:.1f}" rx="{r * .11:.1f}" ry="{r * .08:.1f}" fill="{C["goldDeep"]}" transform="rotate({a} {cx + r * dx:.1f} {cy + r * dy:.1f})"/>'
                    for dx, dy, a in ((-.55, -.35, 20), (-.2, -.6, -30), (.15, -.3, 60), (-.35, 0, 10), (.3, .05, -40), (.6, .3, 30), (-.6, .4, 70), (-.1, .35, 15), (.25, .62, -20), (-.3, .7, 45), (.05, -.02, 80)))
    out = torn_circle(cx, cy, r, C['sandLight'], T, seed=seed, layer=layer, core=False, inner=chips, amp=(1, 3))
    if bite:
        mid = f'bite{seed}'
        out = (f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="#fff"/>'
               f'<circle cx="{cx + r * .86:.1f}" cy="{cy - r * .62:.1f}" r="{r * .3:.1f}" fill="#000"/>'
               f'<circle cx="{cx + r * .5:.1f}" cy="{cy - r * .94:.1f}" r="{r * .22:.1f}" fill="#000"/></mask>'
               f'<g mask="url(#{mid})">{out}</g>')
    return out


def packet(cx, by, s=1.0, rot=0, open_=True, seed=5):
    """A biscuit roll packet lying on its side: a teal pack with crimped ends,
    a gold band, a clear window showing the biscuits standing edge-on. When
    open, the left end is torn off and two biscuits slide out."""
    tr = f'translate({cx} {by}) rotate({rot}) scale({s})'
    L, R, Hh = -170, 170, 130
    crimp_r = ' '.join(f'{R + (18 if k % 2 else 0)},{-Hh + k * Hh / 8:.1f}' for k in range(9))
    crimp_l = ' '.join(f'{L - (18 if k % 2 else 0)},{-k * Hh / 8:.1f}' for k in range(9))
    left = (f'{L},0 {crimp_l} {L},{-Hh}' if not open_ else f'{L},0 {L + 10},{-30} {L - 6},{-64} {L + 8},{-96} {L},{-Hh}')
    edges = ''.join(f'<rect x="{-110 + k * 34}" y="{-Hh + 34}" width="22" height="{Hh - 68}" rx="11" fill="{C["sandLight"]}"/>' for k in range(7))
    out = paper(f'<polygon points="{left} {R},{-Hh} {crimp_r} {R},0" fill="{C["teal"]}"/>'
                f'<rect x="-130" y="{-Hh + 24}" width="260" height="{Hh - 48}" rx="14" fill="{C["tealMist"]}"/>' + edges +
                f'<rect x="{L}" y="-26" width="{R - L}" height="14" fill="{C["gold"]}"/>'
                f'<rect x="{L}" y="{-Hh + 10}" width="{R - L}" height="10" fill="{C["gold"]}"/>', T, 2, T=tr)
    if open_:
        out += paper(f'<g transform="{tr}"><ellipse cx="{L - 22}" cy="-62" rx="18" ry="54" fill="{C["sandLight"]}" transform="rotate(-12 {L - 22} -62)"/>'
                     f'<ellipse cx="{L - 70}" cy="-12" rx="56" ry="13" fill="{C["sandLight"]}"/></g>', T, 2)
    return avoid(out, 'packet')


def small_hand_biscuit(cx, cy, s=1.0, rot=-8):
    """A small hand (tealDeep sleeve, from the bottom) clutching a biscuit."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    out = paper(f'<path d="M -66 40 L 66 40 L 84 400 L -84 400 Z" fill="{C["tealDeep"]}"/>'
                f'<rect x="-70" y="24" width="140" height="28" rx="10" fill="{C["teal"]}"/>', T, 2, T=tr)
    out += biscuit(cx + 0 * s, cy - 110 * s, 82 * s, seed=11, layer=2)
    out += paper(f'<rect x="-74" y="-90" width="148" height="126" rx="50" fill="{C["sandLight"]}"/>'
                 + ''.join(f'<path d="M {-66 + k * 34} -86 Q {-49 + k * 34} -112 {-32 + k * 34} -86" fill="{C["sandLight"]}" stroke="{C["goldDeep"]}" stroke-opacity=".4" stroke-width="4"/>' for k in range(4))
                 + f'<rect x="-104" y="-76" width="40" height="92" rx="20" fill="{C["sandLight"]}" transform="rotate(-24 -84 -30)"/>', T, 3, T=tr)
    return avoid(out, 'hand')


def reach_hand(cx, cy, s=1.0, rot=10):
    """A small open hand reaching straight up from the bottom edge."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    fingers = ''.join(f'<rect x="{x}" y="{y}" width="28" height="{h}" rx="14" fill="{C["sandLight"]}" transform="rotate({a} {x + 14} {y + h})"/>'
                      for x, y, h, a in ((-58, -136, 100, -10), (-26, -160, 124, -3), (6, -156, 120, 3), (38, -132, 96, 10)))
    out = paper(f'<path d="M -50 50 L 50 50 L 64 520 L -64 520 Z" fill="{C["tealDeep"]}"/>'
                f'{fingers}<rect x="-66" y="-60" width="132" height="128" rx="48" fill="{C["sandLight"]}"/>'
                f'<rect x="-108" y="-40" width="32" height="88" rx="16" fill="{C["sandLight"]}" transform="rotate(-36 -92 40)"/>'
                f'<rect x="-52" y="46" width="104" height="22" rx="8" fill="{C["teal"]}"/>', T, 3, T=tr)
    return avoid(out, 'hand')


def fridge(x, y, w=300, h=640, ajar=True):
    """A pearl fridge, its door ajar: a gold slice of light along the opening."""
    out = ''
    if ajar:
        out += glow(f'<rect x="{x + w - 6}" y="{y + 30}" width="40" height="{h - 60}" fill="{C["gold"]}" fill-opacity=".9"/>', 's')
    out += paper(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="{C["tealMist"]}"/>'
                 f'<rect x="{x}" y="{y + h * .36}" width="{w}" height="8" fill="{C["tealDeep"]}" fill-opacity=".45"/>'
                 f'<rect x="{x + w - 46}" y="{y + 60}" width="16" height="110" rx="8" fill="{C["tealDeep"]}"/>'
                 f'<rect x="{x + w - 46}" y="{y + h * .36 + 50}" width="16" height="150" rx="8" fill="{C["tealDeep"]}"/>', T, 2)
    if ajar:
        # the lower door swung a little open towards us: a narrow pearl wedge on the right
        out += paper(f'<polygon points="{x + w},{y + h * .36 + 10} {x + w + 46},{y + h * .36 - 6} {x + w + 46},{y + h + 14} {x + w},{y + h}" fill="{C["pearl"]}"/>', T, 3)
        out += f'<polygon points="{x + w + 46},{y + h} {x + w + 46},{y + h + 14} {x + w + 300},{y + h + 90} {x + w + 220},{y + h + 30}" fill="{C["gold"]}" fill-opacity=".25"/>'
    return avoid(out, 'fridge')


def floor_kid(cx, cy, s=1.0):
    """A small child flat on the floor, seen from behind: head (hair only) to the
    left, arms out, shoes kicking up to the right."""
    tr = f'translate({cx} {cy}) scale({s})'
    return avoid(paper(
        f'<path d="M 120 -10 Q 210 -90 250 -150" stroke="{C["ink"]}" stroke-width="40" stroke-linecap="round" fill="none"/>'
        f'<path d="M 120 20 Q 230 10 300 -40" stroke="{C["ink"]}" stroke-width="40" stroke-linecap="round" fill="none"/>'
        f'<ellipse cx="262" cy="-160" rx="36" ry="24" fill="{C["gold"]}" transform="rotate(-50 262 -160)"/>'
        f'<ellipse cx="312" cy="-48" rx="36" ry="24" fill="{C["gold"]}" transform="rotate(-30 312 -48)"/>'
        f'<path d="M -160 -60 Q -40 -90 140 -50 Q 170 0 140 46 Q -40 70 -160 40 Z" fill="{C["teal"]}"/>'
        f'<path d="M -130 -50 Q -170 -140 -120 -170" stroke="{C["sandLight"]}" stroke-width="30" stroke-linecap="round" fill="none"/>'
        f'<path d="M -120 40 Q -170 110 -130 140" stroke="{C["sandLight"]}" stroke-width="30" stroke-linecap="round" fill="none"/>'
        f'<circle cx="-226" cy="-4" r="78" fill="{C["goldDeep"]}"/>', T, 2, T=tr), 'kid')


def ground_line(y, seed=7):
    return torn_rect(-30, y, W + 60, H - y + 40, C['night'], T, sides='t', seed=seed, layer=1)


def ball(cx, cy, r, seed=21):
    """A beach ball: wedges of teal, pearl and gold meeting at a pole."""
    wedges = ''
    cols = ('teal', 'pearl', 'gold', 'teal', 'pearl', 'gold')
    px, py = cx + r * .25, cy - r * .45
    for k in range(6):
        a0, a1 = math.radians(k * 60 - 90), math.radians(k * 60 - 30)
        wedges += (f'<path d="M {px:.1f} {py:.1f} L {cx + r * 1.2 * math.cos(a0):.1f} {cy + r * 1.2 * math.sin(a0):.1f} '
                   f'L {cx + r * 1.2 * math.cos(a1):.1f} {cy + r * 1.2 * math.sin(a1):.1f} Z" fill="{C[cols[k]]}"/>')
    return paper(f'<clipPath id="bb{seed}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
                 f'<g clip-path="url(#bb{seed})">{wedges}</g>', T, 2)


def block(x, y, sz, col, seed, rot=0, layer=2):
    return torn_rect(x, y, sz, sz, C[col], T, seed=seed, layer=layer, rot=rot, amp=(2, 4),
                     inner=f'<rect x="{x + sz * .2}" y="{y + sz * .2}" width="{sz * .6}" height="{sz * .6}" rx="{sz * .1}" fill="none" stroke="{C["pearl"]}" stroke-opacity=".5" stroke-width="5"/>')


def blocks(x, by, sz=96, tidy=True, seed=30):
    """Three blocks stacked (tidy) or laid out in a row; x = left, by = bottom."""
    if tidy:
        return avoid(block(x, by - sz, sz, 'gold', seed) + block(x + sz + 10, by - sz, sz, 'teal', seed + 1)
                     + block(x + sz * .55, by - sz * 2 - 6, sz, 'pearl', seed + 2, rot=-4), 'blocks')
    return avoid(block(x, by - sz, sz, 'gold', seed, rot=-6) + block(x + sz + 34, by - sz, sz, 'teal', seed + 1, rot=4)
                 + block(x + 2 * sz + 70, by - sz, sz, 'pearl', seed + 2, rot=-3), 'blocks')


def mat(x, y, w, h, seed=40):
    return torn_rect(x, y, w, h, C['tealDeep'], T, seed=seed, layer=1, amp=(3, 6))


def mum_hand_packet(cx, by, s=1.0):
    """A pearl sleeve from the left, mum's hand gripping the packet's side,
    lowering it onto the wardrobe top."""
    tr = f'translate({cx} {by}) scale({s})'
    out = packet(cx, by, s, rot=0, open_=False)
    out += avoid(paper(f'<path d="M -560 -40 L -150 -150 L -120 -40 L -540 80 Z" fill="{C["pearl"]}"/>'
                       f'<rect x="-170" y="-160" width="34" height="130" rx="10" fill="{C["tealMist"]}" transform="rotate(-14 -153 -95)"/>'
                       f'<path d="M -140 -170 Q -100 -190 -60 -180 L -60 -60 Q -100 -40 -130 -60 Z" fill="{C["sandLight"]}"/>'
                       f'<rect x="-104" y="-210" width="110" height="34" rx="17" fill="{C["sandLight"]}"/>'
                       + ''.join(f'<rect x="-80" y="{-160 + k * 34}" width="96" height="30" rx="15" fill="{C["sandLight"]}" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="3"/>' for k in range(3)),
                       T, 3, T=tr), 'hand')
    return out


def hands_pair(cx, cy, s=1.0):
    """Mum's hand (pearl sleeve, from the left) holding the small hand
    (tealDeep sleeve), walking right toward the blocks."""
    tr = f'translate({cx} {cy}) scale({s}) scale(-1 1)'
    return avoid(paper(
        f'<path d="M 140 -60 L 330 -120 L 360 -20 L 170 40 Z" fill="{C["pearl"]}"/>'
        f'<rect x="150" y="-62" width="30" height="104" rx="10" fill="{C["tealMist"]}" transform="rotate(-18 165 -10)"/>'
        f'<path d="M -110 50 L -300 110 L -320 40 L -130 -16 Z" fill="{C["tealDeep"]}"/>'
        f'<rect x="-120" y="-30" width="140" height="80" rx="34" fill="{C["sandLight"]}" transform="rotate(-14 -50 10)"/>'
        f'<path d="M 160 -40 Q 40 -90 -40 -40 Q -80 -10 -50 30 Q 40 60 170 30 Z" fill="{C["sandLight"]}"/>'
        + ''.join(f'<path d="M {-30 + k * 26} -44 Q {-50 + k * 26} 0 {-26 + k * 26} 34" stroke="{C["goldDeep"]}" stroke-opacity=".4" stroke-width="5" fill="none" stroke-linecap="round"/>' for k in range(4)),
        T, 3, T=tr), 'hands')


def crumbs(pts, r=9):
    return ''.join(paper(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["sandLight"]}"/>', T, 1) for x, y in pts)


def slide(ctx):
    s = ctx.s
    if s == 7:
        keep_in(ctx.t.segs, 'كل مرة.')
    if ctx.last:
        mini = packet(250, 1240, .7, rot=-6) + biscuit(110, 1210, 46, seed=9, bite=False)
        return cta_end(ctx, mini_art=mini, tag_y=1040, tag_x=W - MX - 480)
    art, html = '', ''
    if s == 1:
        art = (wardrobe(660, 770) + packet(880, 770, 1.15)
               + small_hand_biscuit(330, 1170, 1.1) + crumbs([(470, 1250), (500, 1200), (200, 1260), (540, 1290)]))
        html = hook_box(ctx, G, y=MT - 10, size=96, keep=('آخر مرة', 'قلتي له "لا"،', 'انتهى الموضوع', 'ببكاء', 'وبسكوتة في يده؟'))
    elif s == 2:
        art = ground_line(1190) + fridge(110, 700, 280, 560) + floor_kid(740, 1150, .95)
        html = body_box(ctx, G)
    elif s == 3:
        art = wardrobe(700, 860) + packet(900, 860, 1.05) + reach_hand(330, 1110, .95)
        html = body_box(ctx, G) + soft_cta(ctx, y=520)
    elif s == 4:
        art = (wardrobe(760, 780) + packet(935, 780, .8, open_=False)
               + mat(80, 1060, 620, 170) + ball(200, 1120, 78) + blocks(330, 1190, 88, tidy=False))
        html = body_box(ctx, G)
    elif s == 5:
        art = wardrobe(660, 960) + mum_hand_packet(870, 900, 1.1)
        html = body_box(ctx, G)
    elif s == 6:
        art = (ground_line(1200, seed=9) + hands_pair(360, 1000, 1.0) + blocks(720, 1220, 96, tidy=True))
        html = body_box(ctx, G)
    elif s == 7:
        art = wardrobe(660, 820) + packet(880, 820, 1.15, open_=False) + blocks(150, 1240, 100, tidy=True) + ball(500, 1170, 70)
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
