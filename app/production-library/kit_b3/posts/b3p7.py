"""b3p7 Losing a game (F5 walk-through). Deep ground. Composition: FANNED CARDS, TOP-DOWN TABLE.

Plain paper cards (no numbers, only one simple gold/teal shape each) on a
tealDeep felt table seen from above. Across the slides: s1 cards tossed
mid-air, the sister's hand still holding her neat fan; s2 the cards scattered
all over the table; s3 one neat fan laid on the table (the promise); s4 mum's
hand laying her cards down face up; s5 a short game: three cards only and a
small hand; s6 the cards stacked into their box by a small hand; s7 a neat
stack and a little sand timer. End: gold, a mini fan.
"""
import math
from kit import C, MX, MT, W, H, keep_in, brk, paper, torn_strip, torn_rect, torn_circle, torn_poly, glow, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'deep'
T = 'd'
CW, CH = 150, 210
FACES = ('circle', 'diamond', 'square', 'drop')


def card_svg(cx, cy, rot=0, face='circle', s=1.0, top=False):
    """One card as raw SVG (no filter). face=None draws the back."""
    w, h = CW * s, CH * s
    g = f'<g transform="translate({cx:.1f} {cy:.1f}) rotate({rot:.1f})">'
    if face is None:
        return (g + f'<rect x="{-w / 2:.1f}" y="{-h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{14 * s:.1f}" fill="{C["teal"]}"/>'
                f'<rect x="{-w / 2 + 14 * s:.1f}" y="{-h / 2 + 14 * s:.1f}" width="{w - 28 * s:.1f}" height="{h - 28 * s:.1f}" rx="{8 * s:.1f}" fill="none" stroke="{C["pearl"]}" stroke-width="{5 * s:.1f}"/>'
                f'<rect x="{-16 * s:.1f}" y="{-16 * s:.1f}" width="{32 * s:.1f}" height="{32 * s:.1f}" fill="{C["gold"]}" transform="rotate(45)"/></g>')
    r = 34 * s
    shape = {
        'circle': f'<circle r="{r:.1f}" fill="{C["gold"]}"/>',
        'diamond': f'<rect x="{-r * .8:.1f}" y="{-r * .8:.1f}" width="{r * 1.6:.1f}" height="{r * 1.6:.1f}" fill="{C["teal"]}" transform="rotate(45)"/>',
        'square': f'<rect x="{-r * .85:.1f}" y="{-r * .85:.1f}" width="{r * 1.7:.1f}" height="{r * 1.7:.1f}" rx="{4 * s:.1f}" fill="{C["tealDeep"]}"/>',
        'drop': f'<path d="M 0 {-r * 1.2:.1f} Q {r:.1f} {-r * .1:.1f} 0 {r:.1f} Q {-r:.1f} {-r * .1:.1f} 0 {-r * 1.2:.1f} Z" fill="{C["goldDeep"]}"/>',
    }[face]
    if top:  # in a fan only the top of each card shows: lift the shape and shrink it
        shape = f'<g transform="translate({-w * .24:.1f} {-h * .3:.1f}) scale(.62)">{shape}</g>'
    return (g + f'<rect x="{-w / 2:.1f}" y="{-h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{14 * s:.1f}" fill="{C["pearl"]}" stroke="{C["tealMist"]}" stroke-width="{3 * s:.1f}"/>' + shape + '</g>')


def card(cx, cy, rot=0, face='circle', s=1.0, layer=2):
    return paper(card_svg(cx, cy, rot, face, s), T, layer)


def table(y, seed=5, x0=60, x1=W - 60):
    """The felt table top seen from above: a big torn tealDeep sheet with a
    goldDeep wood rim, running off the bottom of the frame."""
    out = torn_rect(x0 - 26, y - 26, x1 - x0 + 52, H - y + 80, C['goldDeep'], T, sides='tlr', seed=seed, layer=1)
    out += torn_rect(x0, y, x1 - x0, H - y + 60, C['night'], T, sides='tlr', seed=seed + 1, layer=1, core=False)
    return out


def fan(px, py, n=5, spread=60, s=1.0, rot=0, faces=None, back=False):
    """Cards fanned about a pivot (px, py) at their bottom centre."""
    out = ''
    faces = faces or [FACES[k % 4] for k in range(n)]
    for k in range(n):
        a = rot + (k - (n - 1) / 2) * spread / max(n - 1, 1)
        ar = math.radians(a)
        d = CH * s * .38
        cx, cy = px + d * math.sin(ar), py - d * math.cos(ar)
        out += card_svg(cx, cy, a, None if back else faces[k], s, top=True)
    return paper(out, T, 3)


def hand_fan(px, py, s=1.0, sleeve='gold', rot=0, n=5, spread=56, back=False):
    """A small hand holding a fan of cards: the thumb over the pivot, the sleeve
    running off the bottom edge."""
    out = fan(px, py, n, spread, s, rot=rot, back=back)
    tr = f'translate({px} {py}) rotate({rot}) scale({s})'
    out += paper(f'<path d="M -50 40 L 50 40 L 80 420 L -60 420 Z" fill="{C[sleeve]}"/>'
                 f'<rect x="-62" y="-40" width="124" height="110" rx="44" fill="{C["sandLight"]}"/>'
                 f'<rect x="-50" y="-70" width="88" height="40" rx="20" fill="{C["sandLight"]}" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="4" transform="rotate(-20 -6 -50)"/>'
                 f'<rect x="-54" y="34" width="108" height="20" rx="8" fill="{C["tealMist"]}"/>', T, 3, T=tr)
    return avoid(out, 'fan')


def mum_hand(cx, cy, s=1.0, rot=0, holding=True):
    """Mum's hand from above (pearl sleeve from the right edge), palm down,
    fingers pressing a row of cards onto the table."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    return avoid(paper(f'<path d="M 120 -70 L 620 -110 L 620 110 L 120 70 Z" fill="{C["pearl"]}"/>'
                       f'<rect x="96" y="-74" width="34" height="148" rx="10" fill="{C["tealMist"]}"/>'
                       f'<path d="M 110 -64 Q 20 -76 -20 -50 L -20 50 Q 20 76 110 64 Z" fill="{C["sandLight"]}"/>'
                       + ''.join(f'<rect x="-120" y="{-56 + k * 30}" width="130" height="26" rx="13" fill="{C["sandLight"]}" stroke="{C["goldDeep"]}" stroke-opacity=".3" stroke-width="3"/>' for k in range(4))
                       + f'<rect x="20" y="-104" width="90" height="34" rx="17" fill="{C["sandLight"]}" transform="rotate(-30 65 -87)"/>', T, 3, T=tr), 'hand')


def small_hand(cx, cy, s=1.0, rot=0, sleeve='tealDeep', reach=True):
    """A small hand from the bottom edge, fingers together reaching up."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    return avoid(paper(f'<path d="M -48 40 L 48 40 L 64 460 L -64 460 Z" fill="{C[sleeve]}"/>'
                       f'<rect x="-52" y="30" width="104" height="22" rx="8" fill="{C["teal"]}"/>'
                       f'<rect x="-58" y="-56" width="116" height="104" rx="42" fill="{C["sandLight"]}"/>'
                       + ''.join(f'<rect x="{-50 + k * 26}" y="{-130 + abs(k - 1.5) * 10:.0f}" width="24" height="96" rx="12" fill="{C["sandLight"]}"/>' for k in range(4))
                       + f'<rect x="-96" y="-44" width="30" height="80" rx="15" fill="{C["sandLight"]}" transform="rotate(-38 -81 -4)"/>', T, 3, T=tr), 'hand')


def box(cx, cy, w=300, h=230, cards_in=True, lid=True):
    """An open card box from above: tealDeep tray, pearl inner wall, the lid
    leaning beside it; a neat stack of backs inside."""
    out = ''
    if lid:
        lx, ly = cx + w / 2 + 40 + w * .42, cy + 10
        out += paper(f'<g transform="rotate(8 {lx} {ly})"><rect x="{lx - w * .42}" y="{ly - h / 2}" width="{w * .84}" height="{h}" rx="16" fill="{C["gold"]}"/>'
                     f'<rect x="{lx - w * .42 + 16}" y="{ly - h / 2 + 16}" width="{w * .84 - 32}" height="{h - 32}" rx="10" fill="none" stroke="{C["pearl"]}" stroke-width="5"/>'
                     f'<rect x="{lx - 28}" y="{ly - 28}" width="56" height="56" fill="{C["teal"]}" transform="rotate(45 {lx} {ly})"/></g>', T, 2)
    out += paper(f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="16" fill="{C["ink"]}"/>'
                 f'<rect x="{cx - w / 2 + 18}" y="{cy - h / 2 + 18}" width="{w - 36}" height="{h - 36}" rx="10" fill="{C["night"]}"/>', T, 2)
    if cards_in:
        out += paper(card_svg(cx, cy + 4, 90, None, .92) + card_svg(cx - 4, cy, 90, None, .92), T, 3)
    return avoid(out, 'box')


def stack(cx, cy, n=6, s=1.0, rot=-4):
    out = ''.join(card_svg(cx - k * 3, cy - k * 12, rot + ((k * 7) % 5 - 2), None, s) for k in range(n))
    return avoid(paper(out, T, 3), 'stack')


def sand_timer(cx, cy, s=1.0, rot=0):
    """A little sand timer: gold caps, pearl glass, gold sand mostly at the bottom."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    return avoid(paper(f'<path d="M -70 -150 L 70 -150 Q 70 -60 12 0 Q 70 60 70 150 L -70 150 Q -70 60 -12 0 Q -70 -60 -70 -150 Z" fill="{C["tealMist"]}"/>'
                       f'<path d="M -30 -80 L 30 -80 Q 22 -40 0 -10 Q -22 -40 -30 -80 Z" fill="{C["gold"]}"/>'
                       f'<rect x="-3" y="-10" width="6" height="90" fill="{C["gold"]}"/>'
                       f'<path d="M -62 146 Q -50 70 0 64 Q 50 70 62 146 Z" fill="{C["gold"]}"/>'
                       f'<rect x="-96" y="-180" width="192" height="34" rx="12" fill="{C["goldDeep"]}"/>'
                       f'<rect x="-96" y="146" width="192" height="34" rx="12" fill="{C["goldDeep"]}"/>'
                       f'<rect x="-86" y="-150" width="16" height="296" fill="{C["goldDeep"]}"/><rect x="70" y="-150" width="16" height="296" fill="{C["goldDeep"]}"/>', T, 3, T=tr), 'timer')


def scattered(seed, pts, layer=2, s=1.0):
    out = ''
    for k, (x, y, r) in enumerate(pts):
        face = None if (k + seed) % 3 == 0 else FACES[(k + seed) % 4]
        out += card_svg(x, y, r, face, s)
    return paper(out, T, layer)


def slide(ctx):
    s = ctx.s
    if s == 3:
        keep_in(ctx.t.segs, 'خطوة بخطوة.')
    if s == 5:
        keep_in(ctx.t.segs, 'أكثر من مرة،', 'من جديد.')
    if ctx.last:
        mini = hand_fan(250, 1180, .62, sleeve='pearl', rot=-6, spread=70)
        return cta_end(ctx, mini_art=mini, tag_y=1010, tag_x=W - MX - 500)
    art, html = '', ''
    if s == 1:
        art = (table(1080)
               + scattered(2, [(170, 1210, 8), (450, 1190, -20)], layer=1, s=.9)
               + avoid(scattered(1, [(170, 930, -30), (360, 850, 18), (560, 960, -12), (330, 1060, 40), (690, 870, 28)], layer=3, s=.85), 'cards')
               + ''.join(torn_strip([(x, y), (x + dx, y + dy)], 8, C['gold'], T, seed=90 + k, layer=1)
                         for k, (x, y, dx, dy) in enumerate(((520, 800, 40, -50), (250, 780, -30, -50), (800, 760, 50, -30), (110, 860, -40, -20))))
               + hand_fan(860, 1190, 1.0, sleeve='gold', rot=-8, spread=70))
        html = hook_box(ctx, G, y=MT - 20, size=90, w=920,
                        keep=('صار لك شهور', 'تخسري لطفلك بعمد،', 'ودحين أخته تسألك', 'ليش دايما', 'هو اللي يفوز؟'))
    elif s == 2:
        art = (table(620)
               + avoid(scattered(3, [(200, 760, -24), (420, 720, 12), (660, 780, -40), (870, 740, 22), (300, 960, 50), (560, 1000, -8),
                                     (820, 980, 34), (180, 1180, 14), (450, 1200, -30), (720, 1190, 6), (930, 1160, -18)], layer=2, s=1.0), 'cards'))
        html = body_box(ctx, G)
    elif s == 3:
        art = table(780) + avoid(fan(540, 1150, 7, 110, 1.5), 'fan')
        html = body_box(ctx, G) + soft_cta(ctx, y=520)
    elif s == 4:
        art = (table(760)
               + paper(card_svg(220, 1000, -4, 'circle') + card_svg(390, 1000, 2, 'diamond') + card_svg(560, 1000, -2, 'square'), T, 2)
               + mum_hand(700, 1000, 1.0, rot=0)
               + scattered(0, [(250, 1220, 80), (520, 1230, 96)], layer=1, s=.85))
        html = body_box(ctx, G)
    elif s == 5:
        art = (table(820)
               + avoid(paper(card_svg(280, 990, -3, 'circle', 1.05) + card_svg(540, 980, 2, None, 1.05) + card_svg(800, 990, -2, 'drop', 1.05), T, 2), 'cards')
               + small_hand(560, 1210, .85, rot=-4))
        html = body_box(ctx, G)
    elif s == 6:
        art = (table(720) + box(420, 960, 320, 250, cards_in=True)
               + stack(420, 1190, 1, 1.0, rot=88) + small_hand(470, 1260, .8, rot=-2))
        html = body_box(ctx, G)
    elif s == 7:
        art = table(760) + stack(380, 1110, 7, 1.15, rot=-6) + sand_timer(760, 1040, .95, rot=4)
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
