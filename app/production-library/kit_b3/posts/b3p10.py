"""b3p10 Nails. Night ground. Composition: TORCH CONE.

A phone flash throws a pale gold cone through the dark onto a small sleeping
hand on a pillow edge, nail clippers glinting (s1). The cone stays on the hand
as three nails get done and the hand pulls away (s2). Then the story moves to
the day: mum clips her own nail while a small hand watches (s3), the closed
clippers sit in the small hand (s4), one nail done with a gold mark (s5), two
small hands, one done (s6). Nails that are done are gold.
CTA end: gold ground, mini clippers bottom-left.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_rect, torn_strip, avoid, glow
from common import hook_box, body_box, cta_end

G = 'night'
T = 'd'


def hand(x, y, s=1.0, rot=0, nails=('m',) * 5, spread=1.0, cuff=None, flip=False, curl=0.0, skin=None):
    """A hand seen from the back (nails visible). Local frame: wrist at (0,0),
    fingers point up (-y). nails: per finger (thumb last) 'm' plain, 'g' done
    (gold), None no nail. curl shortens the fingers (relaxed / sleeping)."""
    skin = skin or C['sandLight']
    fx = -1 if flip else 1
    tr = f'translate({x} {y}) rotate({rot}) scale({s * fx} {s})'
    out = ''
    if cuff:
        out += f'<rect x="-70" y="-6" width="140" height="190" rx="16" fill="{C[cuff]}"/>'
    out += f'<rect x="-62" y="-170" width="124" height="176" rx="48" fill="{skin}"/>'
    lens = [86, 104, 98, 76]
    xs = [-42, -14, 14, 42]
    angs = [-13, -4, 4, 13]
    nail_svg = ''
    for k in range(4):
        L = lens[k] * (1 - curl)
        a = angs[k] * spread
        out += (f'<rect x="{xs[k] - 14}" y="{-150 - L}" width="28" height="{L + 30}" rx="14" fill="{skin}" '
                f'transform="rotate({a} {xs[k]} -150)"/>')
        if nails[k]:
            col = C['gold'] if nails[k] == 'g' else C['pearl']
            nail_svg += (f'<rect x="{xs[k] - 9}" y="{-150 - L + 3}" width="18" height="22" rx="8" fill="{col}" '
                         f'transform="rotate({a} {xs[k]} -150)"/>')
    tl = 92 * (1 - curl * .6)
    out += f'<rect x="42" y="{-60 - tl}" width="32" height="{tl + 20}" rx="16" fill="{skin}" transform="rotate(52 58 -50)"/>'
    if nails[4]:
        col = C['gold'] if nails[4] == 'g' else C['pearl']
        nail_svg += f'<rect x="48" y="{-60 - tl + 4}" width="20" height="22" rx="8" fill="{col}" transform="rotate(52 58 -50)"/>'
    out += ''.join(f'<path d="M {xs[k] - 8} -152 Q {xs[k]} -146 {xs[k] + 8} -152" fill="none" stroke="{C["goldDeep"]}" '
                   f'stroke-opacity=".35" stroke-width="3" stroke-linecap="round"/>' for k in range(4))
    return paper(f'<g transform="{tr}">{out}{nail_svg}</g>', T, 2)


def tip(x, y, s, rot, k, spread=1.0, curl=0.0):
    """Canvas position of the centre of nail k (0-3) of hand(x, y, s, rot)."""
    lens = [86, 104, 98, 76]
    xs = [-42, -14, 14, 42]
    angs = [-13, -4, 4, 13]
    L = lens[k] * (1 - curl)
    a = math.radians(angs[k] * spread)
    lx, ly = 0, -L + 14            # nail centre relative to the finger base (xs[k], -150)
    px, py = xs[k] + lx * math.cos(a) - ly * math.sin(a), -150 + lx * math.sin(a) + ly * math.cos(a)
    r = math.radians(rot)
    return x + s * (px * math.cos(r) - py * math.sin(r)), y + s * (px * math.sin(r) + py * math.cos(r))


def clippers(x, y, s=1.0, rot=0, open_=True, glint=True):
    """Nail clippers, side view. Local frame: jaws at the left (0,0), riveted
    back end at the right with a key-ring hole. The body is one tapered piece
    with the slot between its two arms; a long paddle lever stands on a gold
    pin near the jaws and rises over the body (open) or lies flat (closed)."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    ang = -17 if open_ else -3
    body = (f'<path d="M 0 -6 Q 2 -24 22 -26 L 250 -34 Q 286 -34 286 0 Q 286 34 250 34 L 22 26 Q 2 24 0 6 Z" fill="{C["tealMist"]}"/>'
            f'<path d="M 0 0 L 196 0" stroke="{C["night"]}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M 4 -4 Q 14 -14 30 -16" fill="none" stroke="{C["pearl"]}" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="252" cy="0" r="11" fill="{C["night"]}"/>'
            f'<rect x="54" y="-50" width="18" height="28" fill="{C["gold"]}"/>')
    lever = (f'<g transform="rotate({ang} 63 -52)">'
             f'<path d="M 40 -52 Q 40 -66 56 -66 L 300 -72 Q 330 -72 330 -50 Q 330 -30 300 -30 L 56 -38 Q 40 -38 40 -52 Z" fill="{C["pearl"]}"/>'
             f'<ellipse cx="290" cy="-51" rx="24" ry="9" fill="{C["tealMist"]}"/>'
             f'<circle cx="63" cy="-52" r="12" fill="{C["gold"]}"/></g>')
    out = paper(f'<g transform="{tr}">{body}</g>', T, 2) + paper(f'<g transform="{tr}">{lever}</g>', T, 3)
    if glint:
        out += sparkle(x - 6 * s, y - 40 * s, 24 * s) + sparkle(x + 200 * s, y - 150 * s, 15 * s)
    return out


def sparkle(x, y, r):
    d = (f'M {x} {y - r} Q {x + r * .18} {y - r * .18} {x + r} {y} Q {x + r * .18} {y + r * .18} {x} {y + r} '
         f'Q {x - r * .18} {y + r * .18} {x - r} {y} Q {x - r * .18} {y - r * .18} {x} {y - r} Z')
    return paper(f'<path d="{d}" fill="{C["gold"]}"/>', T, 3)


def phone(x, y, s=1.0, rot=0):
    """A phone seen from the back, flash at the top end, held at its lower half by
    a hand in a pearl sleeve that runs off to local +x. Returns (svg, flash_xy)."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    ph = (f'<rect x="-70" y="-140" width="140" height="280" rx="26" fill="{C["tealDeep"]}"/>'
          f'<rect x="-50" y="-122" width="62" height="62" rx="16" fill="{C["ink"]}"/>'
          f'<circle cx="-34" cy="-106" r="10" fill="{C["night"]}"/><circle cx="-4" cy="-76" r="10" fill="{C["night"]}"/>'
          f'<circle cx="34" cy="-104" r="12" fill="{C["pearl"]}"/>')
    grip = (f'<rect x="60" y="40" width="300" height="124" rx="24" fill="{C["pearl"]}"/>'
            f'<path d="M -40 30 Q 20 10 80 36 L 80 160 Q 20 170 -30 140 Z" fill="{C["sandLight"]}"/>'
            + ''.join(f'<rect x="-92" y="{18 + k * 36}" width="70" height="30" rx="15" fill="{C["sandLight"]}"/>' for k in range(4)))
    a = math.radians(rot)
    fx, fy = 34 * s, -104 * s
    flash = (x + fx * math.cos(a) - fy * math.sin(a), y + fx * math.sin(a) + fy * math.cos(a))
    return paper(f'<g transform="{tr}">{ph}</g>', T, 3) + paper(f'<g transform="{tr}">{grip}</g>', T, 3), flash


def cone(x0, y0, x1, y1, w1):
    """The flash beam: a pale gold translucent paper cone from (x0,y0) widening to w1 at (x1,y1)."""
    a = math.atan2(y1 - y0, x1 - x0)
    nx, ny = -math.sin(a), math.cos(a)
    pts = [(x0 + nx * 10, y0 + ny * 10), (x0 - nx * 10, y0 - ny * 10),
           (x1 - nx * w1 / 2, y1 - ny * w1 / 2), (x1 + nx * w1 / 2, y1 + ny * w1 / 2)]
    p = ' '.join(f'{px:.0f},{py:.0f}' for px, py in pts)
    out = glow(f'<polygon points="{p}" fill="{C["gold"]}" fill-opacity=".22"/>', 'l')
    out += paper(f'<polygon points="{p}" fill="{C["gold"]}" fill-opacity=".26"/>', T, 1, 't')
    out += glow(f'<ellipse cx="{x1}" cy="{y1}" rx="{w1 * .55}" ry="{w1 * .3}" fill="{C["gold"]}" fill-opacity=".35"/>', 'l')
    return out


def pillow(x, y, w=720, h=300, rot=-4):
    return avoid(torn_rect(x, y, w, h, C['tealMist'], T, sides='l', seed=21, layer=1, rot=rot,
                           inner=f'<rect x="{x}" y="{y + 26}" width="{w}" height="10" fill="{C["pearl"]}" transform="rotate({rot} {x + w / 2} {y + h / 2})"/>'),
                 'pillow')


def motion(x, y, n=3, L=90, ang=200, seed=50):
    out = ''
    a = math.radians(ang)
    for k in range(n):
        sx, sy = x + k * 26 * math.sin(a), y - k * 26 * math.cos(a)
        out += torn_strip([(sx, sy), (sx + L * math.cos(a), sy + L * math.sin(a))], 9, C['pearl'], T, seed=seed + k, layer=1)
    return out


def arcs(x, y, r0=40, n=3, a0=-40, a1=40, col='gold'):
    out = ''
    for k in range(n):
        r = r0 + k * 30
        p0 = (x + r * math.cos(math.radians(a0)), y + r * math.sin(math.radians(a0)))
        p1 = (x + r * math.cos(math.radians(a1)), y + r * math.sin(math.radians(a1)))
        out += paper(f'<path d="M {p0[0]:.0f} {p0[1]:.0f} A {r} {r} 0 0 1 {p1[0]:.0f} {p1[1]:.0f}" fill="none" '
                     f'stroke="{C[col]}" stroke-width="10" stroke-linecap="round"/>', T, 1)
    return out


def big_sleeve(x, y, rot, length=420, col='ink'):
    """Mum's abaya sleeve (ink, gold cuff band) running off-canvas from (x,y)."""
    return paper(f'<g transform="translate({x} {y}) rotate({rot})"><rect x="-80" y="0" width="160" height="{length}" rx="24" fill="{C[col]}"/>'
                 f'<rect x="-80" y="0" width="160" height="22" fill="{C["gold"]}"/></g>', T, 1)


def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = (f'<g transform="translate(150 1150) rotate(-14) scale(.85)">{clippers(0, 0, 1.0, 0, open_=True, glint=False)}</g>'
                + sparkle(200, 1060, 20) + sparkle(470, 1010, 13))
        return cta_end(ctx, mini_art=mini, tag_y=990, tag_x=W - MX - 500)
    art, html = '', ''
    if s == 1:
        ph, (fx, fy) = phone(250, 690, .8, rot=128)
        art = pillow(300, 1010, 900, 400, rot=-5)
        art += cone(fx, fy, 690, 1110, 520)
        art += avoid(hand(760, 1250, 1.05, rot=-62, spread=.6, curl=.25, cuff='tealDeep'), 'hand')
        art += avoid(clippers(250, 1230, .9, rot=-6, open_=True), 'clip')
        art += avoid(ph, 'phone')
        html = hook_box(ctx, G, y=MT - 10, size=96)
    elif s == 2:
        ph, (fx, fy) = phone(190, 760, .65, rot=128)
        art = pillow(300, 1060, 900, 360, rot=-5)
        art += cone(fx, fy, 600, 1150, 440)
        art += avoid(hand(880, 1160, .95, rot=-80, nails=('g', 'g', 'g', 'm', 'm'), spread=.6, curl=.2, cuff='tealDeep'), 'hand')
        art += motion(620, 1000, n=3, L=120, ang=180, seed=50)
        art += avoid(clippers(380, 1250, .7, rot=-6, open_=True), 'clip')
        art += avoid(ph, 'phone')
        html = body_box(ctx, G)
    elif s == 3:
        # mum clips her own nail (hand from the left, fingers to the right), the click
        # heard as gold arcs, a nail crescent falling; a small hand watches from below right
        mx, my, ms, mr = 170, 1030, 1.3, 70
        art = paper(f'<g transform="translate({mx} {my}) rotate({mr})"><rect x="-90" y="0" width="180" height="400" rx="24" fill="{C["ink"]}"/>'
                    f'<rect x="-90" y="0" width="180" height="24" fill="{C["gold"]}"/></g>', T, 1)
        art += avoid(hand(mx, my, ms, rot=mr, nails=('m', 'm', 'm', 'm', 'm'), spread=.7), 'mum')
        nx, ny = tip(mx, my, ms, mr, 1, .7)
        art += avoid(clippers(nx + 4, ny - 6, 1.1, rot=-4, open_=True, glint=False), 'clip')
        art += arcs(nx + 40, ny - 40, r0=60, n=3, a0=-150, a1=-80)
        art += paper(f'<path d="M {nx + 10} {ny + 70} q 18 14 36 0 q -18 6 -36 0 Z" fill="{C["gold"]}" stroke="{C["gold"]}" stroke-width="6" stroke-linejoin="round"/>', T, 2)
        art += avoid(hand(850, 1340, 1.1, rot=-22, spread=.9, cuff='tealDeep'), 'small')
        html = body_box(ctx, G)
    elif s == 4:
        # the small hand holds the CLOSED clippers and tries the jaw on a nail of the other hand
        art = avoid(hand(300, 1370, 1.3, rot=22, cuff='tealDeep'), 'hand')
        art += avoid(hand(790, 1390, 1.4, rot=-8, nails=(None,) * 5, cuff='tealDeep', curl=.35), 'grip')
        art += avoid(clippers(405, 1040, 1.35, rot=4, open_=False, glint=True), 'clip')
        art += paper(''.join(f'<rect x="{610 + k * 60}" y="1000" width="50" height="132" rx="25" fill="{C["sandLight"]}" transform="rotate(-8 {635 + k * 60} 1066)"/>'
                             for k in range(4)), T, 3)
        html = body_box(ctx, G)
    elif s == 5:
        # one nail done: a big small-hand, one gold nail ringed in gold, the clippers set down
        hx, hy, hs = 600, 1400, 2.1
        art = avoid(hand(hx, hy, hs, rot=0, nails=('m', 'g', 'm', 'm', 'm'), spread=1.1, cuff='tealDeep'), 'hand')
        nx, ny = tip(hx, hy, hs, 0, 1, 1.1)
        art += paper(f'<circle cx="{nx:.0f}" cy="{ny:.0f}" r="52" fill="none" stroke="{C["gold"]}" stroke-width="9"/>', T, 3)
        art += avoid(clippers(110, 1180, .8, rot=-6, open_=False, glint=False), 'clip')
        html = body_box(ctx, G)
    elif s == 6:
        # two small hands held out, one done (all gold), one still to go
        art = avoid(hand(290, 1400, 1.7, rot=-8, nails=('g',) * 5, cuff='tealDeep', flip=True), 'left')
        art += avoid(hand(790, 1400, 1.7, rot=8, cuff='tealDeep'), 'right')
        art += sparkle(120, 760, 22) + sparkle(530, 720, 15)
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
