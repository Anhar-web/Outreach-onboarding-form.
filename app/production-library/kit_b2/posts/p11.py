"""p11 Kids' salon. SandLight ground (ink text). Composition: THE CHAIR AS A STAGE.

The salon chair stands centred under a gold spotlight cone, a tall oval mirror
behind it (empty glass, no reflection). Everything is cut paper: a deep chair
with a tealDeep seat, pearl arms, footrest and pedestal.
Across the slides: s1 the chair on its stage.  s2 the chair empty and turned,
the cape thrown over it, hair clippings scattered (the half haircut).
s3 the chair with the clipper buzzing at the headrest, held by a strange hand
(ink sleeve).  s4 morning: the salon window with a gold sun, the waiting chairs
empty, the stage chair small.  s5 from behind: mum's lap with his back, watching
another child (back of the head) on the chair.  s6 the clipper in his small hand,
buzz strips.  s7 his small hand holding his toy car.  CTA: the chair small,
bottom-right, still under its cone.
"""
import math
from kit import C, MX, MT, W, H, keep_in, paper, torn_strip, torn_rect, torn_circle, torn_poly, glow, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'sandLight'
T = 'l'


def cone(cx, top, bottom, w_top=90, w_bot=520, op=.32, tone=T):
    """The gold spotlight: a lamp shade, a translucent cone, a pool of light on the floor."""
    out = paper(f'<polygon points="{cx - w_top / 2},{top} {cx + w_top / 2},{top} {cx + w_bot / 2},{bottom} {cx - w_bot / 2},{bottom}" '
                f'fill="{C["gold"]}" fill-opacity="{op}"/>', tone, 1, 't')
    out += paper(f'<ellipse cx="{cx}" cy="{bottom}" rx="{w_bot / 2 + 30}" ry="{w_bot * .12}" fill="{C["gold"]}" fill-opacity="{op + .15}"/>', tone, 1, 't')
    out += paper(f'<rect x="{cx - 4}" y="{top - 80}" width="8" height="50" fill="{C["ink"]}"/>'
                 f'<path d="M {cx - w_top / 2 - 20} {top + 4} L {cx - 30} {top - 40} L {cx + 30} {top - 40} L {cx + w_top / 2 + 20} {top + 4} Z" fill="{C["deep"]}"/>', tone, 2)
    return avoid(out, 'lamp')


def mirror(cx, cy, rx=230, ry=330, tone=T):
    """Tall oval mirror: gold frame, tealMist glass, pearl glare (no reflection)."""
    out = paper(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx + 26}" ry="{ry + 26}" fill="{C["gold"]}"/>'
                f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{C["tealMist"]}"/>', tone, 1)
    out += paper(f'<path d="M {cx + rx * .35} {cy - ry * .75} L {cx + rx * .7} {cy - ry * .3}" stroke="{C["pearl"]}" stroke-width="26" stroke-linecap="round"/>'
                 f'<path d="M {cx + rx * .2} {cy - ry * .55} L {cx + rx * .62} {cy + ry * .05}" stroke="{C["pearl"]}" stroke-width="12" stroke-linecap="round"/>', tone, 1, 't')
    return avoid(out, 'mirror')


def chair(cx, cy, s=1.0, tone=T, back=False, rot=0, cape=False, kid=False, name='chair'):
    """Salon chair, front view (or from behind with back=True). Local: seat at y=0,
    headrest top at y=-430, pedestal disc at y=+300."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    out = paper(f'<ellipse cx="0" cy="300" rx="190" ry="40" fill="{C["ink"]}"/>'
                f'<rect x="-34" y="150" width="68" height="150" fill="{C["pearl"]}"/>'
                f'<rect x="-60" y="230" width="120" height="20" rx="8" fill="{C["tealMist"]}"/>', tone, 1, T=tr)
    if back:
        out += paper(f'<rect x="-200" y="-330" width="400" height="420" rx="60" fill="{C["deep"]}"/>'
                     f'<rect x="-100" y="-420" width="200" height="80" rx="30" fill="{C["deep"]}"/>'
                     f'<rect x="-240" y="40" width="480" height="110" rx="30" fill="{C["deep"]}"/>', tone, 2, T=tr)
        out += paper(f'<line x1="-150" y1="-200" x2="150" y2="-200" stroke="{C["night"]}" stroke-width="10"/>'
                     f'<line x1="-150" y1="-60" x2="150" y2="-60" stroke="{C["night"]}" stroke-width="10"/>', tone, 2, 't', T=tr)
        if kid:
            # another child, back of the head only, above the backrest, a tealMist cape round the neck
            out += paper(f'<path d="M -170 -300 Q 0 -360 170 -300 L 180 -250 L -180 -250 Z" fill="{C["tealMist"]}"/>', tone, 3, T=tr)
            out += paper(f'<circle cx="0" cy="-400" r="110" fill="{C["goldDeep"]}"/>'
                         f'<ellipse cx="-108" cy="-390" rx="18" ry="30" fill="{C["sand"] if "sand" in C else C["pearl"]}"/>'
                         f'<ellipse cx="108" cy="-390" rx="18" ry="30" fill="{C["pearl"]}"/>', tone, 3, T=tr)
        return avoid(out, name)
    # backrest + headrest
    out += paper(f'<rect x="-170" y="-340" width="340" height="400" rx="56" fill="{C["deep"]}"/>'
                 f'<rect x="-90" y="-430" width="180" height="76" rx="30" fill="{C["deep"]}"/>'
                 f'<rect x="-14" y="-370" width="28" height="40" fill="{C["ink"]}"/>', tone, 1, T=tr)
    # tufting lines on the back
    out += paper(f'<path d="M -110 -260 H 110 M -110 -150 H 110 M -110 -40 H 110" stroke="{C["night"]}" stroke-width="10" stroke-linecap="round" stroke-opacity=".7"/>', tone, 1, 't', T=tr)
    # arms + seat + footrest
    out += paper(f'<rect x="-250" y="-40" width="80" height="44" rx="20" fill="{C["pearl"]}"/>'
                 f'<rect x="170" y="-40" width="80" height="44" rx="20" fill="{C["pearl"]}"/>'
                 f'<rect x="-226" y="0" width="30" height="110" fill="{C["pearl"]}"/>'
                 f'<rect x="196" y="0" width="30" height="110" fill="{C["pearl"]}"/>', tone, 2, T=tr)
    out += paper(f'<path d="M -200 40 L 200 40 L 220 150 L -220 150 Z" fill="{C["tealDeep"]}"/>', tone, 3, T=tr)
    out += paper(f'<rect x="-150" y="200" width="300" height="26" rx="12" fill="{C["gold"]}"/>', tone, 2, T=tr)
    if cape:
        out += paper(f'<path d="M -120 -330 Q 40 -360 160 -300 L 240 120 Q 120 190 -20 150 Q -140 120 -150 40 Z" fill="{C["teal"]}"/>'
                     f'<path d="M -40 -300 L 60 120 M 80 -300 L 160 100" stroke="{C["tealMist"]}" stroke-width="8" stroke-opacity=".7"/>', tone, 3, T=tr)
    return avoid(out, name)


def clippings(pts, seed=0):
    """Hair clippings on the floor: short goldDeep and ink torn snips."""
    out = ''
    for k, (x, y) in enumerate(pts):
        a = math.radians((k * 67 + seed * 13) % 180)
        L = 30 + (k * 17) % 26
        col = C['goldDeep'] if k % 3 else C['ink']
        out += f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x + L * math.cos(a):.0f}" y2="{y + L * math.sin(a):.0f}" stroke="{col}" stroke-width="7" stroke-linecap="round"/>'
    return paper(out, T, 1, 't')


def clipper(x, y, s=1.0, rot=0, tone=T):
    """Hair clipper: pearl body, gold blade head with ink teeth, ink cord tail."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    out = paper(f'<path d="M 0 140 Q 10 260 -60 330" fill="none" stroke="{C["ink"]}" stroke-width="12" stroke-linecap="round"/>', tone, 1, T=tr)
    out += paper(f'<path d="M -56 -120 L 56 -120 L 44 150 Q 0 170 -44 150 Z" fill="{C["pearl"]}"/>'
                 f'<rect x="-14" y="-40" width="28" height="60" rx="12" fill="{C["teal"]}"/>', tone, 2, T=tr)
    out += paper(f'<rect x="-70" y="-170" width="140" height="54" rx="10" fill="{C["gold"]}"/>'
                 + ''.join(f'<rect x="{-62 + k * 16}" y="-196" width="9" height="30" rx="3" fill="{C["ink"]}"/>' for k in range(9)), tone, 3, T=tr)
    return out


def buzz(cx, cy, r=170, n=3, col='deep', seed=0, a0=-150, a1=-30):
    """Buzz strips: short torn zigzag arcs around a point."""
    out = ''
    for k in range(n):
        rr = r + k * 50
        pts = []
        m = 10
        for j in range(m + 1):
            a = math.radians(a0 + (a1 - a0) * j / m)
            d = rr + (12 if j % 2 else -12)
            pts.append((cx + d * math.cos(a), cy + d * math.sin(a)))
        out += torn_strip(pts, 14, C[col], T, seed=seed + k, layer=2, core=False)
    return avoid(out, 'buzz')


def strange_hand(x, y):
    """A grown-up's hand from the right in an ink sleeve (the barber), holding the clipper."""
    out = torn_strip([(1120, y + 140), (x + 80, y + 20)], 110, C['ink'], T, seed=41, layer=3)
    out += paper(f'<g transform="translate({x} {y}) rotate(-12)"><rect x="-70" y="-50" width="140" height="110" rx="44" fill="{C["sandLight"]}"/>'
                 f'<path d="M -70 -50 Q -40 -70 10 -60" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".5" stroke-width="4"/></g>', T, 3)
    return out


def small_hand(x, y, s=1.0, rot=0, sleeve_to=(1120, 1400)):
    """His small hand (fist round something), teal sleeve back to the frame edge."""
    out = torn_strip([sleeve_to, (x + 40 * s, y + 70 * s)], 92 * s, C['teal'], T, seed=51, layer=3)
    out += paper(f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
                 f'<rect x="-60" y="-50" width="120" height="110" rx="46" fill="#E9C9A0"/>'
                 + ''.join(f'<rect x="-66" y="{-40 + n * 24}" width="40" height="22" rx="11" fill="#E9C9A0"/>' for n in range(4))
                 + f'<path d="M -30 -50 Q 0 -70 40 -46" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".45" stroke-width="4"/></g>', T, 3)
    return out


def toy_car(x, y, s=1.0, rot=0):
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    out = paper(f'<path d="M -150 20 L -150 -30 Q -140 -50 -100 -54 L -60 -110 Q -40 -126 20 -126 L 70 -126 Q 100 -124 120 -60 L 150 -50 Q 166 -40 166 0 L 166 20 Z" fill="{C["deep"]}"/>'
                f'<path d="M -46 -100 L -20 -112 L 30 -112 L 30 -62 L -70 -62 Z" fill="{C["tealMist"]}"/>'
                f'<path d="M 46 -112 L 66 -112 Q 88 -110 100 -62 L 46 -62 Z" fill="{C["tealMist"]}"/>'
                f'<rect x="140" y="-34" width="22" height="14" rx="5" fill="{C["gold"]}"/>', T, 2, T=tr)
    out += paper(f'<circle cx="-90" cy="22" r="40" fill="{C["ink"]}"/><circle cx="-90" cy="22" r="16" fill="{C["pearl"]}"/>'
                 f'<circle cx="100" cy="22" r="40" fill="{C["ink"]}"/><circle cx="100" cy="22" r="16" fill="{C["pearl"]}"/>', T, 3, T=tr)
    return out


def window_sun(x, y, w=380, h=440):
    out = paper(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{C["tealMist"]}"/>', T, 1)
    sx, sy = x + w * .62, y + h * .36
    rays = ''.join(f'<rect x="{sx - 8}" y="{sy - 110}" width="16" height="36" rx="7" transform="rotate({k * 45} {sx} {sy})" fill="{C["gold"]}"/>' for k in range(8))
    out += paper(f'<circle cx="{sx}" cy="{sy}" r="58" fill="{C["gold"]}"/>{rays}', T, 2)
    out += paper(f'<path d="M {x} {y} H {x + w} V {y + h} H {x} Z M {x + w / 2} {y} V {y + h} M {x} {y + h / 2} H {x + w}" fill="none" stroke="{C["pearl"]}" stroke-width="22"/>', T, 2)
    return avoid(out, 'window')


def waiting_chair(x, y, s=1.0):
    tr = f'translate({x} {y}) scale({s})'
    return paper(f'<rect x="-60" y="-130" width="120" height="110" rx="20" fill="{C["tealDeep"]}"/>'
                 f'<rect x="-70" y="-30" width="140" height="34" rx="12" fill="{C["tealDeep"]}"/>'
                 f'<rect x="-60" y="0" width="14" height="80" fill="{C["ink"]}"/><rect x="46" y="0" width="14" height="80" fill="{C["ink"]}"/>', T, 2, T=tr)


def mum_lap(cx, cy):
    """From behind: mum's lap (deep abaya, pearl hands round him) and his back:
    small shoulders in a teal tee, the back of his head (hair only)."""
    out = paper(f'<path d="M {cx - 420} 1400 Q {cx - 400} {cy - 40} {cx - 220} {cy - 80} L {cx + 220} {cy - 80} Q {cx + 400} {cy - 40} {cx + 420} 1400 Z" fill="{C["deep"]}"/>', T, 1)
    out += paper(f'<path d="M {cx - 170} 1400 Q {cx - 180} {cy - 150} {cx} {cy - 170} Q {cx + 180} {cy - 150} {cx + 170} 1400 Z" fill="{C["teal"]}"/>', T, 2)
    out += paper(f'<circle cx="{cx}" cy="{cy - 250}" r="118" fill="{C["goldDeep"]}"/>'
                 f'<ellipse cx="{cx - 116}" cy="{cy - 240}" rx="18" ry="30" fill="#E9C9A0"/>'
                 f'<ellipse cx="{cx + 116}" cy="{cy - 240}" rx="18" ry="30" fill="#E9C9A0"/>', T, 3)
    out += paper(f'<ellipse cx="{cx - 190}" cy="{cy + 40}" rx="56" ry="40" fill="#E9C9A0"/>'
                 f'<ellipse cx="{cx + 190}" cy="{cy + 40}" rx="56" ry="40" fill="#E9C9A0"/>', T, 3)
    return avoid(out, 'lap')


def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = cone(830, 860, 1230, 40, 300, .3) + chair(830, 1100, .34, name='mini', rot=4)
        return cta_end(ctx, mini_art=mini, tag_x=MX + 10, tag_y=1100)
    art, html = '', ''
    if s == 1:
        art = (mirror(540, 1000, 200, 250)
               + cone(540, 745, 1280, 90, 560, .4)
               + chair(540, 1070, .6))
        html = hook_box(ctx, G, y=MT - 10, size=96, keep=('كل ما وديتيه', 'صالون الاطفال', 'يبدأ الصراخ', 'ويحاول يهرب؟'))
    elif s == 2:
        pts = [(170 + (k * 137) % 740, 1110 + (k * 53) % 110) for k in range(22)]
        art = (mirror(620, 880, 170, 240)
               + clippings(pts, 2)
               + chair(560, 960, .62, rot=-8, cape=True))
        html = body_box(ctx, G)
    elif s == 3:
        art = (mirror(420, 960, 170, 230)
               + chair(420, 1045, .58)
               + buzz(560, 880, 80, 3, 'deep', 11, -110, 10)
               + avoid(clipper(620, 900, .65, rot=-60) + strange_hand(700, 950), 'hand'))
        html = body_box(ctx, G)
    elif s == 4:
        keep_in(ctx.t.segs, 'قبل ما يزحم الصالون')
        art = (window_sun(600, 620, 320, 270)
               + avoid(waiting_chair(680, 960, .55) + waiting_chair(840, 960, .55), 'waiting')
               + chair(280, 870, .4))
        html = body_box(ctx, G) + soft_cta(ctx, y=1030)
    elif s == 5:
        art = (cone(780, 720, 1060, 56, 300, .3)
               + chair(780, 930, .34, back=True, kid=True)
               + mum_lap(380, 1260))
        html = body_box(ctx, G)
    elif s == 6:
        art = (buzz(560, 840, 170, 3, 'deep', 21, -160, -20)
               + avoid(clipper(560, 900, 1.0, rot=-8) + small_hand(600, 1020, 1.1, rot=-8), 'clipper'))
        html = body_box(ctx, G)
    elif s == 7:
        art = avoid(toy_car(520, 950, 1.35, rot=-6) + small_hand(600, 1060, 1.25, rot=-4), 'car')
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
