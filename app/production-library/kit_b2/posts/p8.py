"""p8 Blender. Deep ground. Composition: MACRO CROP THROUGH THE JAR.

The blender jar is huge and cut off by the frame (left and bottom): a tealMist
glass jar with pearl measuring marks, milk and sandLight banana slices inside,
a gold blade, a pearl base with a gold dial. Light from the top-right puts the
glass highlight on the right.
Across the slides: s1 the macro jar.  s2 pulled back: the full jar on the
counter, the lit doorway beyond (his toy blocks in the light).  s3 the jar back
on the shelf, the bananas still in it, a crescent moon (later tonight).
s4 big torn noise strips burst from it.  s5 the blender on a folded striped
towel.  s6 short pulse marks: dash, gap, dash, a finger on the dial.
s7 macro again from above the open jar: a small hand drops a banana slice in.
CTA: the blender small in the bottom-left corner, tilted.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, torn_poly, glow, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'deep'
T = 'd'


def slice_(x, y, r=46, tilt=1.0):
    """A banana slice: a pale disc with a thin gold peel rim and a small star of
    tiny goldDeep seeds in the middle. tilt < 1 squashes it (seen at an angle)."""
    seeds = ''.join(f'<ellipse cx="{r * .22 * math.cos(k * 1.047):.1f}" cy="{r * .22 * math.sin(k * 1.047):.1f}" rx="{r * .07:.1f}" ry="{r * .035:.1f}" '
                    f'transform="rotate({k * 60} {r * .22 * math.cos(k * 1.047):.1f} {r * .22 * math.sin(k * 1.047):.1f})" fill="{C["goldDeep"]}" fill-opacity=".75"/>' for k in range(6))
    return (f'<g transform="translate({x} {y}) scale(1 {tilt})">'
            f'<circle r="{r}" fill="{C["gold"]}"/>'
            f'<circle r="{r * .86:.1f}" fill="#F3E3B8"/>'
            f'<circle r="{r * .42:.1f}" fill="{C["sandLight"]}"/>{seeds}</g>')


SLICES = [(-110, -120, 52), (40, -170, 50), (120, -60, 46), (-40, -40, 48), (-140, -260, 44), (90, -300, 46), (-20, -360, 42)]


def blender(cx, cy, s=1.0, tone=T, milk=.55, slices=7, lid=True, base=True, name='blender', rot=0, lift=0):
    """Local coords: jar bottom at y=0, jar top at y=-600, base below (0..230).
    Jar 440 wide at the top, 300 at the bottom; handle on the left."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    out = ''
    if base:
        out += paper(f'<path d="M -190 0 L 190 0 L 220 230 L -220 230 Z" fill="{C["pearl"]}"/>'
                     f'<rect x="-230" y="200" width="460" height="40" rx="14" fill="{C["tealMist"]}"/>'
                     f'<circle cx="0" cy="110" r="56" fill="{C["gold"]}"/>'
                     f'<rect x="-8" y="62" width="16" height="44" rx="8" fill="{C["goldDeep"]}"/>', tone, 1, T=tr)
    # handle (left), cut paper
    out += paper(f'<path d="M -200 -520 Q -330 -520 -330 -380 L -330 -240 Q -330 -110 -180 -110" fill="none" stroke="{C["tealMist"]}" stroke-width="48" stroke-linecap="round"/>', tone, 1, T=tr)
    jar_d = 'M -220 -600 L 220 -600 L 150 0 L -150 0 Z'
    inner = f'<path d="{jar_d}" fill="{C["tealMist"]}" fill-opacity=".38"/>'
    if milk:
        ty = -600 * milk
        w_at = 150 + 70 * milk
        inner += f'<path d="M {-w_at:.0f} {ty:.0f} L {w_at:.0f} {ty:.0f} L 150 0 L -150 0 Z" fill="{C["pearl"]}" fill-opacity=".9"/>'
    for (x, y, r) in SLICES[:slices]:
        inner += slice_(x, y + lift, r, .8 + .2 * ((x * 7) % 3) / 2)
    # blade
    inner += (f'<path d="M -110 -40 L 110 -70 M -100 -80 L 100 -30" stroke="{C["gold"]}" stroke-width="16" stroke-linecap="round"/>'
              f'<circle cx="0" cy="-55" r="18" fill="{C["goldDeep"]}"/>')
    jar = paper(inner, tone, 2, T=tr)
    # glass: outline, marks on the left, highlight on the right (light from the top-right)
    glass = (f'<path d="{jar_d}" fill="none" stroke="{C["tealMist"]}" stroke-width="14" stroke-linejoin="round"/>'
             + ''.join(f'<rect x="{-196 + k * 8.2:.0f}" y="{-520 + k * 70}" width="{60 if k % 2 == 0 else 34}" height="10" rx="5" fill="{C["pearl"]}"/>' for k in range(6))
             + f'<path d="M 170 -560 L 112 -60" stroke="{C["pearl"]}" stroke-width="22" stroke-linecap="round" stroke-opacity=".85"/>'
             f'<path d="M 128 -560 L 104 -360" stroke="{C["pearl"]}" stroke-width="10" stroke-linecap="round" stroke-opacity=".7"/>')
    out += jar + paper(glass, tone, 2, 't', T=tr)
    if lid:
        out += paper(f'<rect x="-240" y="-650" width="480" height="64" rx="18" fill="{C["teal"]}"/>'
                     f'<rect x="-70" y="-700" width="140" height="60" rx="16" fill="{C["teal"]}"/>', tone, 3, T=tr)
    return avoid(out, name)


def counter(y, x0=-40, x1=1120, col='tealDeep', seed=5):
    return torn_rect(x0, y, x1 - x0, 1500 - y, C[col], T, sides='t', seed=seed, layer=1)


def doorway(x, y, w, h):
    """The lit doorway beyond: a pearl opening, a wedge of light, his toy blocks in it."""
    out = glow(f'<rect x="{x - 30}" y="{y - 30}" width="{w + 60}" height="{h + 60}" fill="{C["pearl"]}" fill-opacity=".22"/>', 'l')
    out += paper(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C["pearl"]}"/>', T, 1)
    out += paper(f'<path d="M {x - 26} {y + h} V {y - 26} H {x + w + 26} V {y + h}" fill="none" stroke="{C["night"]}" stroke-width="30"/>', T, 2)
    bx, by = x + w * .25, y + h - 10
    blocks = (f'<rect x="{bx}" y="{by - 70}" width="70" height="70" rx="6" fill="{C["gold"]}"/>'
              f'<rect x="{bx + 80}" y="{by - 70}" width="70" height="70" rx="6" fill="{C["teal"]}"/>'
              f'<rect x="{bx + 40}" y="{by - 140}" width="70" height="70" rx="6" fill="{C["deep"]}"/>')
    out += paper(blocks, T, 2)
    return avoid(out, 'door')


def crescent(cx, cy, r, layer=2):
    return paper(f'<path d="M {cx} {cy - r} A {r} {r} 0 1 0 {cx} {cy + r} A {r * .62} {r} 0 1 1 {cx} {cy - r} Z" fill="{C["pearl"]}"/>', T, layer)


def noise(cx, cy, scale=1.0):
    """Big torn noise strips bursting out to the right: jagged zigzags."""
    out = ''
    cols = ['gold', 'pearl', 'teal', 'gold', 'pearl']
    for k in range(5):
        a = math.radians(-50 + k * 25)
        L0, L1 = 60 * scale, (330 + 60 * (k % 2)) * scale
        pts = []
        n = 7
        for j in range(n + 1):
            t = L0 + (L1 - L0) * j / n
            off = (24 * scale) * (1 if j % 2 else -1)
            pts.append((cx + t * math.cos(a) - off * math.sin(a), cy + t * math.sin(a) + off * math.cos(a)))
        out += torn_strip(pts, 26 * scale, C[cols[k]], T, seed=30 + k, layer=2)
    return avoid(out, 'noise')


def towel(cx, top, w=560, layers=3):
    """A folded striped towel: stacked sandLight folds with gold stripes."""
    out = ''
    for k in range(layers):
        y = top + k * 46
        ww = w - (layers - 1 - k) * 0
        out += torn_rect(cx - ww / 2, y, ww, 50, C['sandLight'], T, sides='lr', seed=60 + k, layer=1 + (layers - 1 - k) % 3,
                         inner=f'<rect x="{cx - ww / 2}" y="{y + 18}" width="{ww}" height="10" fill="{C["gold"]}"/>')
    return avoid(out, 'towel')


def pulses(x0, y, n=3, dash=120, gap=80):
    """Short pulse marks right of the blender: dash, gap, dash (torn gold strips)."""
    out = ''
    for k in range(n):
        x = x0 + k * (dash + gap)
        out += torn_rect(x, y - 24, dash, 48, C['gold'], T, sides='tblr', seed=70 + k, layer=2, rot=-2 + k * 2)
    # the gaps: small pearl dots of silence
    for k in range(n - 1):
        x = x0 + k * (dash + gap) + dash + gap / 2
        out += paper(f'<circle cx="{x}" cy="{y}" r="8" fill="{C["pearl"]}" fill-opacity=".5"/>', T, 1)
    return avoid(out, 'pulses')


def finger(x, y):
    """Mum's finger pressing the dial, from the right: pearl sleeve, sandLight hand."""
    out = paper(f'<path d="M {x + 60} {y - 30} L 1120 {y - 60} L 1120 {y + 70} L {x + 60} {y + 40} Z" fill="{C["pearl"]}"/>', T, 3)
    out += paper(f'<rect x="{x - 10}" y="{y - 36}" width="90" height="80" rx="30" fill="{C["sandLight"]}"/>'
                 f'<rect x="{x - 70}" y="{y - 22}" width="90" height="26" rx="13" fill="{C["sandLight"]}"/>', T, 3)
    return avoid(out, 'finger')


def jar_top(cx, cy, s=1.0):
    """The open jar from above-front: a wide pearl rim ellipse, milk and slices inside."""
    tr = f'translate({cx} {cy}) scale({s})'
    out = paper(f'<path d="M -300 0 L -220 900 L 220 900 L 300 0 Z" fill="{C["tealMist"]}" fill-opacity=".38"/>'
                f'<path d="M -280 180 L -228 900 L 228 900 L 280 180 Z" fill="{C["pearl"]}" fill-opacity=".9"/>'
                + slice_(-90, 260, 66) + slice_(80, 330, 62) + slice_(-20, 430, 60) + slice_(120, 500, 56) + slice_(-120, 520, 58),
                T, 2, T=tr)
    out += paper(f'<ellipse cx="0" cy="0" rx="300" ry="70" fill="none" stroke="{C["tealMist"]}" stroke-width="18"/>'
                 f'<path d="M -300 0 L -220 900 M 300 0 L 220 900" stroke="{C["tealMist"]}" stroke-width="14"/>'
                 f'<path d="M 250 60 L 196 800" stroke="{C["pearl"]}" stroke-width="22" stroke-linecap="round" stroke-opacity=".85"/>', T, 2, 't', T=tr)
    return avoid(out, 'jar')


def small_hand_drop(x, y):
    """A small hand from the top-right (teal sleeve), fingers open, a slice falling below."""
    out = torn_strip([(1120, y - 170), (x + 100, y - 40)], 90, C['tealDeep'], T, seed=81, layer=3)
    out += paper(f'<g transform="translate({x} {y}) rotate(-30) scale(1.5)">'
                 f'<rect x="-40" y="-40" width="90" height="80" rx="32" fill="{C["sandLight"]}"/>'
                 + ''.join(f'<rect x="{-38 + n * 22}" y="20" width="18" height="{48 - abs(n - 1.5) * 8:.0f}" rx="9" fill="{C["sandLight"]}"/>' for n in range(4))
                 + '</g>', T, 3)
    return avoid(out, 'hand')


def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = blender(250, 1050, .34, tone='l', milk=.5, slices=5, name='mini', rot=-8)
        return cta_end(ctx, mini_art=mini, tag_x=W - MX - 470, tag_y=1100)
    art, html = '', ''
    if s == 1:
        art = blender(250, 1840, 1.7, milk=.8, lift=-200)
        html = hook_box(ctx, G, y=MT - 10, size=96, keep=('تشغلي الخلاط', 'إن طفلك بعيد؟', 'لازم تتأكدي'))
    elif s == 2:
        art = (doorway(700, 700, 260, 520) + counter(1180)
               + blender(330, 960, .62, milk=.75))
        html = body_box(ctx, G)
    elif s == 3:
        shelf = torn_rect(80, 1030, 620, 40, C['pearl'], T, sides='tb', seed=12, layer=1)
        art = (crescent(840, 760, 56) + avoid(shelf, 'shelf')
               + blender(380, 860, .4, milk=.75, slices=7))
        html = body_box(ctx, G, y=MT + 40)
    elif s == 4:
        art = blender(330, 1000, .62, milk=.55) + noise(560, 880, 1.3)
        html = body_box(ctx, G)
    elif s == 5:
        art = towel(280, 1104, 400) + blender(280, 1016, .4, milk=.55)
        html = body_box(ctx, G) + soft_cta(ctx, y=450, w=640)
    elif s == 6:
        art = (blender(250, 990, .5, milk=.55) + pulses(480, 870)
               + finger(260, 1045))
        html = body_box(ctx, G)
    elif s == 7:
        art = (jar_top(420, 1090, .9)
               + paper(slice_(520, 960, 52, .85), T, 3)
               + small_hand_drop(600, 820))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
