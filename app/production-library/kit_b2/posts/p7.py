"""p7 Hair dryer. Pearl ground (the batch's only pearl post), deep type. Composition: MIRROR FRAME.

A big oval mirror on the wall (gold frame, tealMist glass with pearl glare). Mum
is only her back: long dark hair, a teal top, her own hand holding the dryer to
HER OWN hair. The dryer throws torn noise arcs. Never a face, never a reflection.
s1: mum at the mirror, dryer on, big noise arcs.
s2: the noise reaches him: a small figure (back view) on the bed edge, hands over his ears.
s3: the mirror alone, three gold tabs hanging under it (three steps), the dryer resting.
s4: close on the dryer: three level marks on the handle, only the lowest lit, one small arc.
s5: a small finger presses the button while mum's hand holds the handle.
s6: the bed corner far from the mirror, him seated with space around him; the arcs fade before him.
s7: CTA end, gold ground: mirror + dryer small, top-left; the tag low on the right.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, arc_pts, avoid, text_box, step_tab
from common import soft_cta, cta_end

G = 'pearl'
T = 'l'
TXT = 'deep'          # deep type on pearl (art direction)


# ---------------------------------------------------------------- type
def hook(ctx, y=MT, size=96, w=888, breaks=(), keep=()):
    from kit import brk, keep_in
    h = ctx.t.body()[0]
    if breaks:
        brk(h, *breaks)
    if keep:
        keep_in([h], *keep)
    return text_box([h], W - MX - w, y, w, TXT, size={'hook': size})


def body(ctx, y=None, w=888):
    out = ''
    lab = ctx.t.label()
    top = y if y is not None else (MT + 110 if lab else MT + 20)
    if lab:
        out += step_tab(lab)
    return out + text_box(ctx.t.body(), W - MX - w, top, w, TXT)


# ---------------------------------------------------------------- motifs
def mirror(cx, cy, rx, ry, seed=0, tone=T, T_='', frame='gold'):
    """Oval wall mirror: gold cut frame, deep inner rim, tealMist glass, two pearl glare bands."""
    g = paper(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{C[frame]}"/>'
              f'<ellipse cx="{cx}" cy="{cy}" rx="{rx - 10}" ry="{ry - 10}" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="4"/>',
              tone, 1, T=T_)
    glass = paper(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx * .86:.1f}" ry="{ry * .89:.1f}" fill="{C["tealMist"]}"/>'
                  f'<ellipse cx="{cx}" cy="{cy}" rx="{rx * .86:.1f}" ry="{ry * .89:.1f}" fill="none" stroke="{C["deep"]}" stroke-opacity=".25" stroke-width="6"/>',
                  tone, 2, T=T_)
    # glare: two diagonal pearl bands, kept inside the glass
    a = -35
    b1 = (f'<rect x="{cx + rx * .12:.1f}" y="{cy - ry * .62:.1f}" width="{rx * .2:.1f}" height="{ry * .9:.1f}" rx="{rx * .1:.1f}" '
          f'transform="rotate({a} {cx + rx * .22:.1f} {cy - ry * .17:.1f})" fill="{C["pearl"]}" fill-opacity=".85"/>')
    b2 = (f'<rect x="{cx + rx * .42:.1f}" y="{cy - ry * .42:.1f}" width="{rx * .08:.1f}" height="{ry * .55:.1f}" rx="{rx * .04:.1f}" '
          f'transform="rotate({a} {cx + rx * .46:.1f} {cy - ry * .15:.1f})" fill="{C["pearl"]}" fill-opacity=".85"/>')
    glare = paper(b1 + b2, tone, 2, 't', T=T_)
    return avoid(g + glass + glare, 'mirror')


def dryer(x, y, s=1.0, rot=0, tone=T, levels=None, button=False, hand=True, sleeve=True, layer=2):
    """Side-view hair dryer, nozzle pointing LEFT. (x, y) = barrel centre.
    levels = None | lit index (0 = lowest) -> three marks on the handle.
    hand = mum's hand round the handle (+ teal sleeve going down-right)."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    # handle (behind the barrel)
    handle = (f'<g transform="rotate(14 60 40)"><rect x="18" y="20" width="96" height="270" rx="40" fill="{C["deep"]}"/>'
              f'<rect x="40" y="270" width="52" height="34" rx="10" fill="{C["night"]}"/></g>')
    o = paper(handle, tone, layer, T=tr)
    # barrel + nozzle + rear vent
    barrel = (f'<path d="M -150 -78 H 120 Q 170 -78 170 0 Q 170 78 120 78 H -150 Z" fill="{C["deep"]}"/>'
              f'<rect x="-150" y="-30" width="260" height="12" rx="6" fill="{C["pearl"]}" fill-opacity=".25"/>')
    nozzle = f'<path d="M -150 -60 L -250 -46 Q -262 0 -250 46 L -150 60 Z" fill="{C["teal"]}"/>'
    o += paper(barrel + nozzle, tone, layer + 1, T=tr)
    vent = (f'<circle cx="150" cy="0" r="74" fill="{C["gold"]}"/>'
            + ''.join(f'<circle cx="150" cy="0" r="{r}" fill="none" stroke="{C["goldDeep"]}" stroke-width="6"/>' for r in (52, 32))
            + f'<circle cx="150" cy="0" r="12" fill="{C["goldDeep"]}"/>')
    o += paper(vent, tone, layer + 1, T=tr)
    if levels is not None:
        marks = ''
        for k in range(3):    # bottom = lowest level
            lit = k == levels
            cy_ = 210 - k * 52
            marks += (f'<rect x="{46 - (8 if lit else 0)}" y="{cy_ - 16}" width="{40 + (16 if lit else 0)}" height="{30 if lit else 22}" rx="10" '
                      f'fill="{C["gold"] if lit else C["pearl"]}" fill-opacity="{1 if lit else .45}"/>')
        o += paper(f'<g transform="rotate(14 60 40)">{marks}</g>', tone, layer + 1, T=tr)
    if button:
        o += paper(f'<g transform="rotate(14 60 40)"><rect x="34" y="60" width="64" height="40" rx="14" fill="{C["gold"]}"/></g>', tone, layer + 1, T=tr)
    if hand:
        # mum's fingers wrapped round the handle (four rounded bars) + teal sleeve below
        f = ''.join(f'<rect x="-6" y="{118 + n * 40}" width="128" height="36" rx="18" fill="{C["sandLight"]}"/>' for n in range(4))
        cuff = ''
        if sleeve:
            cuff = (f'<path d="M 20 280 L 150 280 L 260 760 L 40 760 Z" fill="{C["teal"]}"/>'
                    f'<rect x="10" y="270" width="150" height="34" rx="10" fill="{C["tealDeep"]}"/>')
        o = paper(f'<g transform="rotate(14 60 40)">{cuff}</g>', tone, layer, T=tr) + o
        o += paper(f'<g transform="rotate(14 60 40)">{f}<path d="M -6 118 Q -40 150 -10 200" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".3" stroke-width="4"/></g>',
                   tone, layer + 2, T=tr)
    return avoid(o, 'dryer')


def arcs(cx, cy, r0, n=3, a0=150, a1=210, gap=60, width=18, seed=0, cols=('gold', 'teal', 'deep'), tone=T, fade=1.0):
    """Torn noise arcs centred on (cx, cy), spreading on the angle range a0..a1 (180 = left)."""
    out = ''
    for k in range(n):
        r = r0 + k * gap
        pts = arc_pts(cx, cy, r, a0, a1, n=24)
        # make it a little jittery: noise, not a calm wave
        pts = [(px + (4 if i % 2 else -4) * (k + 1) * .6, py) for i, (px, py) in enumerate(pts)]
        strip = torn_strip(pts, width, C[cols[k % len(cols)]], tone, seed=seed + k * 7, layer=2)
        if fade < 1:
            strip = f'<g opacity="{fade ** (k + 1):.2f}">{strip}</g>'
        out += strip
    return avoid(out, 'noise')


def mum_back(cx, cy, s=1.0, wet=True, tone=T):
    """Mum from behind: teal shoulders and neck, a round head of long night-dark hair
    falling past the shoulders, a gold clip. No face, no reflection."""
    tr = f'translate({cx} {cy}) scale({s})'
    sh = paper(f'<path d="M -280 420 Q -270 200 -70 175 L 70 175 Q 270 200 280 420 Z" fill="{C["teal"]}"/>'
               f'<path d="M -70 175 Q 0 215 70 175" fill="none" stroke="{C["tealDeep"]}" stroke-width="10"/>', tone, 1, T=tr)
    hair = paper(f'<circle cx="0" cy="-30" r="150" fill="{C["night"]}"/>'
                 f'<path d="M -150 -30 Q -170 150 -205 300 Q -110 330 0 318 Q 110 330 205 300 Q 170 150 150 -30 Z" fill="{C["night"]}"/>'
                 f'<path d="M 0 -178 Q -10 60 -6 300" fill="none" stroke="{C["deep"]}" stroke-width="8" stroke-linecap="round"/>'
                 f'<path d="M -90 -110 Q -130 100 -150 290 M 90 -110 Q 130 100 150 290" fill="none" stroke="{C["deep"]}" stroke-width="8" stroke-linecap="round"/>',
                 tone, 2, T=tr)
    clip = paper(f'<rect x="-70" y="-150" width="140" height="34" rx="14" fill="{C["gold"]}" transform="rotate(-6 0 -133)"/>', tone, 3, T=tr)
    o = sh + hair + clip
    if wet:
        d = ''
        for k, (dx, dy) in enumerate(((-170, 350), (-130, 395), (165, 345), (135, 400), (-195, 440), (40, 360))):
            r = 13
            d += f'<path d="M {dx} {dy - r * 1.6} Q {dx + r} {dy - r * .2} {dx} {dy + r} Q {dx - r} {dy - r * .2} {dx} {dy - r * 1.6} Z" fill="{C["tealDeep"]}"/>'
        o += paper(d, tone, 3, T=tr)
    return avoid(o, 'mum')


def bed_edge(x0, x1, top, tone=T):
    """The end of a bed, side view: deep base, sandLight mattress, a tealMist sheet hanging over."""
    o = paper(f'<rect x="{x0}" y="{top + 90}" width="{x1 - x0}" height="140" rx="14" fill="{C["deep"]}"/>'
              f'<rect x="{x0 + 20}" y="{top + 220}" width="26" height="70" rx="6" fill="{C["night"]}"/>'
              f'<rect x="{x1 - 46}" y="{top + 220}" width="26" height="70" rx="6" fill="{C["night"]}"/>', tone, 1)
    o += paper(f'<rect x="{x0 + 10}" y="{top}" width="{x1 - x0 - 20}" height="100" rx="20" fill="{C["sandLight"]}"/>', tone, 2)
    o += torn_rect(x0 + 20, top - 14, x1 - x0 - 40, 70, C['tealMist'], tone, sides='b', seed=44, layer=3, amp=(5, 10))
    return avoid(o, 'bed')


def child_back(cx, base, s=1.0, ears=False, tone=T):
    """A small child seated, seen from behind: gold top, goldDeep hair. ears=True:
    both small hands pressed over his ears. No face."""
    tr = f'translate({cx} {base}) scale({s})'
    body_ = paper(f'<path d="M -110 0 Q -115 -150 -50 -175 L 50 -175 Q 115 -150 110 0 Z" fill="{C["gold"]}"/>'
                  f'<rect x="-24" y="-200" width="48" height="40" rx="12" fill="{C["sandLight"]}"/>', tone, 3, T=tr)
    head = paper(f'<circle cx="0" cy="-270" r="88" fill="{C["goldDeep"]}"/>', tone, 4, T=tr)
    o = body_ + head
    if ears:
        # arms up, hands flat over the ears
        arms = (f'<path d="M -88 -150 Q -150 -190 -110 -265" fill="none" stroke="{C["gold"]}" stroke-width="44" stroke-linecap="round"/>'
                f'<path d="M 88 -150 Q 150 -190 110 -265" fill="none" stroke="{C["gold"]}" stroke-width="44" stroke-linecap="round"/>')
        hands = (f'<ellipse cx="-96" cy="-282" rx="32" ry="44" fill="{C["sandLight"]}" transform="rotate(14 -96 -282)"/>'
                 f'<ellipse cx="96" cy="-282" rx="32" ry="44" fill="{C["sandLight"]}" transform="rotate(-14 96 -282)"/>')
        o += paper(arms, tone, 3, T=tr) + paper(hands, tone, 5, T=tr)
    else:
        o += paper(f'<ellipse cx="-86" cy="-262" rx="16" ry="24" fill="{C["sandLight"]}"/>'
                   f'<ellipse cx="86" cy="-262" rx="16" ry="24" fill="{C["sandLight"]}"/>', tone, 3, T=tr)
    return avoid(o, 'child')


def small_hand(x, y, s=1.0, rot=0, tone=T):
    """A small hand with the index finger pointing (pressing). (x, y) = fingertip."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    g = (f'<rect x="-15" y="0" width="30" height="100" rx="15" fill="{C["sandLight"]}"/>'
         f'<path d="M -40 80 Q -44 70 -20 66 L 50 66 Q 66 70 62 100 L 58 170 Q 50 196 10 196 L -26 196 Q -48 190 -46 160 Z" fill="{C["sandLight"]}"/>'
         f'<path d="M -14 110 H 50 M -14 138 H 52" stroke="{C["goldDeep"]}" stroke-opacity=".3" stroke-width="4"/>'
         f'<rect x="-46" y="190" width="104" height="160" rx="18" fill="{C["gold"]}"/>')
    return avoid(paper(g, tone, 4, T=tr), 'finger')


def tabs3(cx, y, w=110, gap=40, seed=80, tone=T):
    """Three small torn gold tabs hanging from a string under the mirror (three steps)."""
    o = ''
    xs = [cx + (w + gap), cx, cx - (w + gap)]     # RTL: first on the right
    o += paper(f'<path d="M {xs[0]} {y - 70} Q {cx} {y - 30} {xs[2]} {y - 70}" fill="none" stroke="{C["deep"]}" stroke-width="5"/>', tone, 1, 't')
    for k, x in enumerate(xs):
        o += paper(f'<line x1="{x}" y1="{y - 60 + (10 if k == 1 else 0)}" x2="{x}" y2="{y}" stroke="{C["deep"]}" stroke-width="4"/>', tone, 1, 't')
        dots_ = ''.join(f'<circle cx="{x - (k * 16) + j * 32}" cy="{y + 50}" r="10" fill="{C["deep"]}"/>' for j in range(k + 1))
        o += torn_rect(x - w / 2, y, w, 100, C['gold'], tone, 'tblr', seed=seed + k, layer=2, rot=(-4, 3, -2)[k], amp=(3, 6), inner=dots_)
    return avoid(o, 'tabs')


# ---------------------------------------------------------------- slides
def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = (mirror(250, 330, 150, 190, tone='l', frame='deep')
                + dryer(400, 430, .45, rot=-8, hand=False, sleeve=False, tone='l')
                + arcs(250, 430, 70, n=2, a0=150, a1=210, gap=34, width=10, seed=9, tone='l'))
        # text sits under the mini? no: text keeps its top-right place, mini goes top-left
        r = cta_end(ctx, mini_art='', y=560, tag_y=1050, tag_x=W - MX - 470)
        r['art'] = mini
        return r

    art, html = '', ''
    if s == 1:
        # mum at the mirror, drying her own hair, noise arcs everywhere
        art = (mirror(360, 990, 270, 330)
               + mum_back(660, 1080, .85, wet=True)
               + arcs(520, 1000, 130, n=3, a0=140, a1=220, gap=58, width=20, seed=3)
               + dryer(915, 960, .7, rot=-12))
        html = hook(ctx, y=MT - 10, size=96, keep=('إلا لما يكون', 'طفلك بعيد عنك؟'))
    elif s == 2:
        # the noise reaches him: bed edge on the left, the dryer on the right
        art = (bed_edge(60, 560, 1080)
               + child_back(300, 1100, .85, ears=True)
               + arcs(820, 990, 150, n=4, a0=150, a1=215, gap=58, width=18, seed=11, cols=('gold', 'teal', 'gold', 'deep'))
               + dryer(980, 990, .62, rot=-6, sleeve=True))
        html = body(ctx, y=MT)
    elif s == 3:
        # the mirror alone, three steps hanging under it; the dryer resting, off
        art = (mirror(540, 800, 330, 330)
               + tabs3(540, 1150)
               + dryer(230, 1080, .5, rot=0, hand=False, sleeve=False))
        html = body(ctx, y=MT + 20)
    elif s == 4:
        # close on the dryer: three level marks, only the lowest lit, one small arc
        art = (dryer(620, 640, 1.0, rot=-4, levels=0, sleeve=False)
               + arcs(320, 640, 70, n=1, a0=150, a1=210, width=16, seed=21, cols=('gold',)))
        html = body(ctx) + soft_cta(ctx, y=1060, w=860)
    elif s == 5:
        # his small finger on the button while mum holds the handle
        art = (dryer(560, 830, 1.05, rot=-4, button=True, sleeve=True)
               + small_hand(600, 925, .8, rot=90))
        html = body(ctx)
    elif s == 6:
        # far from the mirror: the bed corner left, him seated, space around; arcs fade before him
        art = (mirror(940, 900, 120, 165)
               + dryer(980, 1080, .32, rot=-8, hand=False, sleeve=False)
               + arcs(870, 1080, 60, n=3, a0=160, a1=200, gap=36, width=10, seed=31, fade=.6)
               + bed_edge(60, 470, 1110)
               + child_back(250, 1130, .55))
        html = body(ctx)
    return {'ground': G, 'art': art, 'html': html}
