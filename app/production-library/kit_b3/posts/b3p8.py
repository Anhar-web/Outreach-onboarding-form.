"""b3p8 Ride ends (F7 mistakes). Night ground. Composition: KIDDIE RIDE ON THE MALL FLOOR.

One coin-ride car (side view, no face, no lights) on a spring and a gold coin
box, standing on a perspective tile floor. Across the slides: s1 the child
clings to the wheel, a glowing exit door far left; s2 a queue of small backs
waits; s3 a small hand waves bye-bye at the empty ride; s4 one finger raised
("one more time"); s5 a timeline with a gold mark one beat before the cry;
s6 mum's hand holds the small hand, the ride slowing. End: a mini ride.
"""
import math
from kit import C, MX, MT, W, H, keep_in, brk, paper, torn_strip, torn_rect, torn_circle, torn_poly, glow, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'night'
T = 'd'


def floor(yh, seed=1, x0=0, x1=W):
    """Mall floor: a deep paper plane from the horizon yh down, tile seams
    converging to a vanishing point above the middle."""
    vx, vy = 540, yh - 700
    lines = ''
    for k in range(-9, 10):
        bx = 540 + k * 170
        t = (yh - vy) / (1350 - vy)
        tx = vx + (bx - vx) * t
        lines += f'<line x1="{tx:.1f}" y1="{yh + 4}" x2="{bx:.1f}" y2="1350" stroke="{C["night"]}" stroke-opacity=".5" stroke-width="3"/>'
    y, step = yh, 26
    while y < 1350:
        y += step
        step *= 1.38
        lines += f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{C["night"]}" stroke-opacity=".5" stroke-width="3"/>'
    return torn_rect(x0 - 20, yh, x1 - x0 + 40, 1400 - yh, C['deep'], T, sides='t', seed=seed, layer=1, inner=lines)


def exit_door(x, yb, w=190, h=300):
    """A far exit: a pearl frame, the doorway glowing gold (no arrow, no sign)."""
    out = glow(f'<rect x="{x - 40}" y="{yb - h - 40}" width="{w + 80}" height="{h + 40}" fill="{C["gold"]}" fill-opacity=".8"/>', 'l')
    out += f'<polygon points="{x},{yb} {x + w},{yb} {x + w + 220},{yb + 200} {x - 80},{yb + 200}" fill="{C["gold"]}" fill-opacity=".3"/>'
    out += paper(f'<rect x="{x - 18}" y="{yb - h - 18}" width="{w + 36}" height="{h + 18}" fill="{C["ink"]}"/>'
                 f'<rect x="{x}" y="{yb - h}" width="{w}" height="{h}" fill="{C["gold"]}"/>'
                 f'<path d="M {x} {yb - h} L {x + w * .34} {yb - h + 26} L {x + w * .34} {yb + 4} L {x} {yb} Z" fill="{C["goldDeep"]}"/>', T, 1)
    return avoid(out, 'door')


def ride(cx, by, s=1.0, rock=0, kid=False, motion=0, seed=3):
    """Coin ride, side view. (cx, by) = bottom centre of the coin box on the
    floor. No headlights, no grille, nothing that can read as a face: a rounded
    teal body with a gold stripe, a tall gold seat back, a pearl steering wheel
    on a post, two plain dark wheels, a coil spring, a goldDeep coin box."""
    tr = f'translate({cx} {by}) scale({s})'
    out = ''
    out += paper(f'<rect x="-150" y="-140" width="300" height="140" rx="14" fill="{C["goldDeep"]}"/>'
                 f'<rect x="-150" y="-140" width="300" height="22" rx="10" fill="{C["gold"]}"/>'
                 f'<rect x="64" y="-96" width="44" height="12" rx="6" fill="{C["night"]}"/>'
                 f'<rect x="-120" y="-60" width="200" height="8" rx="4" fill="{C["gold"]}" fill-opacity=".6"/>', T, 1, T=tr)
    zig = ' '.join(f'{(-34 if k % 2 else 34)},{-140 - k * 14}' for k in range(0, 9))
    out += paper(f'<polyline points="{zig}" fill="none" stroke="{C["pearl"]}" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>', T, 1, T=tr)
    car = ''
    # wheels (half hidden under the arches)
    for wx in (-160, 160):
        car += f'<circle cx="{wx}" cy="-232" r="56" fill="{C["ink"]}"/><circle cx="{wx}" cy="-232" r="26" fill="{C["tealDeep"]}"/>'
    # body: a chunky cartoon car, side view, round wheel arches, nose right
    car += (f'<path d="M -290 -250 Q -300 -400 -220 -410 L -60 -410 Q -30 -410 -20 -380 L 40 -376 '
            f'Q 120 -380 170 -360 L 250 -340 Q 300 -326 296 -270 L 296 -250 L 236 -250 A 76 76 0 0 0 84 -250 '
            f'L -84 -250 A 76 76 0 0 0 -236 -250 Z" fill="{C["teal"]}"/>'
            f'<path d="M -284 -316 L 286 -310" stroke="{C["gold"]}" stroke-width="22" stroke-linecap="round"/>')
    # windscreen (pale, clearly glass on a frame), in front of the driver
    car += f'<path d="M 40 -378 L 70 -470 L 92 -470 L 70 -374 Z" fill="{C["tealMist"]}"/>'
    # seat back
    car += f'<path d="M -236 -404 L -240 -540 Q -240 -568 -212 -568 L -166 -568 Q -140 -568 -142 -540 L -136 -404 Z" fill="{C["tealDeep"]}"/>'
    # steering post + wheel (seen nearly edge-on)
    car += (f'<path d="M 30 -380 L 0 -460" stroke="{C["pearl"]}" stroke-width="16" stroke-linecap="round"/>'
            f'<ellipse cx="-4" cy="-470" rx="54" ry="15" transform="rotate(-24 -4 -470)" fill="none" stroke="{C["pearl"]}" stroke-width="14"/>')
    rot = f'rotate({rock} 0 -224)'
    out += paper(f'<g transform="{rot}">{car}</g>', T, 2, T=tr)
    if kid:
        k = (f'<path d="M -170 -404 Q -190 -520 -120 -548 Q -60 -566 -20 -520 L 0 -470 Q -20 -420 -60 -404 Z" fill="{C["gold"]}"/>'
             f'<path d="M -100 -520 Q -40 -530 10 -486" stroke="{C["sandLight"]}" stroke-width="30" stroke-linecap="round" fill="none"/>'
             f'<path d="M -110 -486 Q -50 -470 0 -470" stroke="{C["sandLight"]}" stroke-width="30" stroke-linecap="round" fill="none"/>'
             f'<circle cx="-50" cy="-590" r="60" fill="{C["goldDeep"]}"/>')
        out += paper(f'<g transform="{rot}">{k}</g>', T, 3, T=tr)
    for m in range(motion):
        r_ = 330 + m * 40
        out += torn_strip([(cx + s * r_ * math.cos(math.radians(a)), by - 330 * s + s * r_ * math.sin(math.radians(a)))
                           for a in range(-30, 5, 5)], 9, C['gold'], T, seed=seed + m, layer=1)
        out += torn_strip([(cx - s * r_ * math.cos(math.radians(a)), by - 330 * s + s * r_ * math.sin(math.radians(a)))
                           for a in range(-30, 5, 5)], 9, C['gold'], T, seed=seed + 10 + m, layer=1)
    return avoid(out, 'ride')


def small_back(cx, by, s=1.0, shirt='tealDeep', seed=1):
    """A small child seen from behind: legs, torso, back of the head with both ears."""
    tr = f'translate({cx} {by}) scale({s})'
    return avoid(paper(f'<rect x="-34" y="-110" width="28" height="110" rx="12" fill="{C["ink"]}"/>'
                       f'<rect x="6" y="-110" width="28" height="110" rx="12" fill="{C["ink"]}"/>'
                       f'<path d="M -62 -100 Q -66 -230 0 -236 Q 66 -230 62 -100 Z" fill="{C[shirt]}"/>'
                       f'<ellipse cx="-58" cy="-282" rx="11" ry="17" fill="{C["sandLight"]}"/>'
                       f'<ellipse cx="58" cy="-282" rx="11" ry="17" fill="{C["sandLight"]}"/>'
                       f'<circle cx="0" cy="-286" r="56" fill="{C["goldDeep"]}"/>', T, 2, T=tr), 'kid')


def wave_hand(cx, cy, s=1.0, rot=-12):
    """A small open hand waving (palm out), tealDeep sleeve, gold wave arcs."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    fingers = ''.join(f'<rect x="{x}" y="{y}" width="30" height="{h}" rx="15" fill="{C["sandLight"]}" transform="rotate({a} {x + 15} {y + h})"/>'
                      for x, y, h, a in ((-62, -150, 110, -14), (-28, -176, 136, -4), (6, -172, 132, 4), (40, -146, 106, 14)))
    out = paper(f'<path d="M -50 60 L 50 60 L 60 330 L -60 330 Z" fill="{C["tealDeep"]}"/>'
                f'{fingers}<rect x="-70" y="-70" width="140" height="140" rx="52" fill="{C["sandLight"]}"/>'
                f'<rect x="-120" y="-30" width="34" height="96" rx="17" fill="{C["sandLight"]}" transform="rotate(-48 -86 50)"/>'
                f'<rect x="-50" y="56" width="100" height="22" rx="8" fill="{C["teal"]}"/>', T, 3, T=tr)
    for k in range(2):
        r = 190 + k * 50
        out += torn_strip([(cx + r * math.cos(math.radians(a)), cy - 40 + r * math.sin(math.radians(a))) for a in range(-150, -110, 5)],
                          10, C['gold'], T, seed=40 + k, layer=2)
        out += torn_strip([(cx + r * math.cos(math.radians(a)), cy - 40 + r * math.sin(math.radians(a))) for a in range(-70, -30, 5)],
                          10, C['gold'], T, seed=50 + k, layer=2)
    return avoid(out, 'hand')


def one_finger(cx, cy, s=1.0, rot=6):
    """Mum's hand, palm towards us, index finger raised ('just one more'):
    the thumb folds across the three curled fingers, the index rises from the
    thumb side, so it can only read as 'one'. Pearl sleeve."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    out = paper(f'<path d="M -86 70 L 86 70 L 110 420 L -110 420 Z" fill="{C["pearl"]}"/>'
                f'<rect x="54" y="-250" width="50" height="250" rx="25" fill="{C["sandLight"]}"/>'
                f'<rect x="-90" y="-90" width="196" height="170" rx="56" fill="{C["sandLight"]}"/>'
                + ''.join(f'<path d="M {x} -88 Q {x + 22} -112 {x + 44} -88" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".45" stroke-width="5" stroke-linecap="round"/>'
                          for x in (-84, -40, 4))
                + f'<rect x="-80" y="-30" width="150" height="46" rx="23" fill="{C["sandLight"]}" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="4"/>'
                f'<rect x="-92" y="66" width="200" height="26" rx="10" fill="{C["tealMist"]}"/>', T, 3, T=tr)
    return avoid(out, 'hand')


def timeline(x0, x1, y, n=9, gold_at=6, cry_at=7, seed=60):
    """A thin torn pearl strip with beats; one gold mark one beat before the cry
    (a jagged teal burst). No words, no numbers."""
    out = torn_strip([(x0, y), (x1, y)], 16, C['pearl'], T, seed=seed, layer=1)
    step = (x1 - x0) / (n - 1)
    for k in range(n):
        x = x0 + k * step
        if k == cry_at:
            pts = [(x + (64 if j % 2 == 0 else 32) * math.cos(math.radians(j * 30 - 90)),
                    y + (64 if j % 2 == 0 else 32) * math.sin(math.radians(j * 30 - 90))) for j in range(12)]
            out += torn_poly(pts, C['teal'], T, seed=seed + 5, layer=2)
        elif k == gold_at:
            out += torn_circle(x, y, 40, C['gold'], T, seed=seed + 7, layer=3)
        else:
            out += paper(f'<circle cx="{x:.1f}" cy="{y}" r="15" fill="{C["tealDeep"]}"/>', T, 2)
    return avoid(out, 'timeline')


def hands_pair(cx, cy, s=1.0):
    """Mum's big hand (pearl sleeve, from the right) wrapped round the small
    hand (tealDeep sleeve, from the left)."""
    tr = f'translate({cx} {cy}) scale({s})'
    return avoid(paper(
        f'<path d="M 140 -60 L 330 -120 L 360 -20 L 170 40 Z" fill="{C["pearl"]}"/>'
        f'<rect x="150" y="-62" width="30" height="104" rx="10" fill="{C["tealMist"]}" transform="rotate(-18 165 -10)"/>'
        f'<path d="M -110 50 L -300 110 L -320 40 L -130 -16 Z" fill="{C["tealDeep"]}"/>'
        f'<rect x="-120" y="-30" width="140" height="80" rx="34" fill="{C["sandLight"]}" transform="rotate(-14 -50 10)"/>'
        f'<path d="M 160 -40 Q 40 -90 -40 -40 Q -80 -10 -50 30 Q 40 60 170 30 Z" fill="{C["sandLight"]}"/>'
        + ''.join(f'<path d="M {-30 + k * 26} -44 Q {-50 + k * 26} 0 {-26 + k * 26} 34" stroke="{C["goldDeep"]}" stroke-opacity=".4" stroke-width="5" fill="none" stroke-linecap="round"/>' for k in range(4)),
        T, 3, T=tr), 'hands')


def slide(ctx):
    s = ctx.s
    if s == 4:
        keep_in(ctx.t.segs, '"طيب مرة وحده بس"', '"لا خلاص، تأخرنا"', '"مرة وحده بس"')
    if ctx.last:
        mini = ride(260, 1230, .42, rock=-6)
        return cta_end(ctx, mini_art=mini, tag_y=1010, tag_x=W - MX - 500)
    art, html = '', ''
    if s == 1:
        art = (floor(990, seed=2) + exit_door(110, 1000, 150, 250)
               + ride(680, 1290, .94, rock=-4, kid=True, motion=0))
        html = hook_box(ctx, G, y=MT - 20, size=88, w=920,
                        breaks=('اللعبة ', 'تطلعي '), keep=('وهو يبكي،', 'من المول', 'من باب ثاني؟'))
    elif s == 2:
        art = (floor(960, seed=4) + ride(330, 1240, .82, rock=-3, kid=True)
               + small_back(700, 1240, .78, 'teal') + small_back(840, 1236, .72, 'gold') + small_back(965, 1232, .66, 'tealDeep'))
        html = body_box(ctx, G)
    elif s == 3:
        art = floor(1010, seed=6) + ride(730, 1260, .8, rock=0) + wave_hand(250, 1110, .85)
        html = body_box(ctx, G) + soft_cta(ctx, y=650)
    elif s == 4:
        art = floor(1040, seed=8) + ride(740, 1255, .66, rock=3, kid=True, motion=1) + one_finger(260, 960, .9)
        html = body_box(ctx, G)
    elif s == 5:
        art = (floor(1000, seed=10) + ride(540, 1040, .62, rock=0, kid=True)
               + timeline(170, 910, 1150))
        html = body_box(ctx, G)
    elif s == 6:
        art = (floor(900, seed=12) + ride(700, 1150, .82, rock=-1, kid=True, motion=1)
               + hands_pair(300, 1210, 1.0))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
