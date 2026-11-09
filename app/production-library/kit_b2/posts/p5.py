"""p5 Cooking. sandLight ground, ink text. Composition: CHILD'S-EYE LOW ANGLE.

The kitchen counter is a tealDeep band across the frame, seen from below: the
pot sits on it with pearl steam rising above, and mum is only her night-blue
hem (with a gold trim) falling to the floor. A small hand grips the hem.
Across the slides: s1 the grip; s2 a pearl sleeve stirring above while the hand
pulls the hem; s3 the hand lets go; s4 a gold chair pulled up, the child (from
behind) now at the counter at mum's height, far from the pot; s5 a zabdiya bowl
of cucumbers in water; s6 two wordless pearl bubbles (an onion, rice); s7 the
method on three torn notes. CTA end: gold, the steaming pot small bottom-right,
the tag on the left.
"""
import math
from kit import C, MX, MT, W, H, keep_in, brk, paper, torn_strip, torn_rect, torn_circle, torn_poly, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'sandLight'
T = 'l'


# ---------------------------------------------------------------- pieces
def counter(y, h=96, x0=-20, x1=W + 20, seed=5):
    """The counter edge seen from below: a pearl lip on a tealDeep slab, a darker
    underside strip."""
    out = paper(f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{h}" fill="{C["tealDeep"]}"/>'
                f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="18" fill="{C["pearl"]}"/>'
                f'<rect x="{x0}" y="{y + h - 16}" width="{x1 - x0}" height="16" fill="{C["deep"]}"/>', T, 1)
    return avoid(out, 'counter')


def pot(cx, base, s=1.0, steam=True, seed=3, lid=True, sn=7):
    """A pearl enamel pot with a deep band, gold handles and a deep lid. base = y of
    its bottom (sits on the counter)."""
    tr = f'translate({cx} {base}) scale({s})'
    body = paper(f'<rect x="-190" y="-80" width="30" height="34" rx="10" fill="{C["gold"]}"/>'
                 f'<rect x="160" y="-80" width="30" height="34" rx="10" fill="{C["gold"]}"/>'
                 f'<path d="M -165 -210 H 165 L 150 -12 Q 148 0 130 0 H -130 Q -148 0 -150 -12 Z" fill="{C["pearl"]}"/>'
                 f'<rect x="-160" y="-150" width="320" height="26" fill="{C["deep"]}"/>', T, 2, T=tr)
    top = ''
    if not lid:
        top = paper('<ellipse cx="0" cy="-210" rx="165" ry="26" fill="{0}"/>'.format(C['night']), T, 2, T=tr)
    if lid:
        top = paper(f'<path d="M -176 -206 Q 0 -290 176 -206 Z" fill="{C["deep"]}"/>'
                    f'<rect x="-26" y="-284" width="52" height="30" rx="12" fill="{C["gold"]}"/>', T, 3, T=tr)
    out = body + top
    if steam:
        for k, dx in enumerate((-90, 0, 90)):
            pts = [(cx + (dx + 22 * math.sin(i * .9 + k)) * s, base - (300 + i * 40) * s) for i in range(sn)]
            out += torn_strip(pts, 26 * s, C['pearl'], T, seed=seed + k, layer=2)
    return avoid(out, 'pot')


def hem(x0, x1, top, bottom=1228, flare=60):
    """Mum: just the lower part of a night-blue abaya, flaring a little, gold trim."""
    pts = f'{x0 + flare},{top} {x1 - flare},{top} {x1},{bottom} {x0},{bottom}'
    out = paper(f'<polygon points="{pts}" fill="{C["night"]}"/>'
                f'<path d="M {(x0 + x1) / 2 + 30} {top} L {(x0 + x1) / 2 + 50} {bottom}" stroke="{C["deep"]}" stroke-width="10"/>'
                f'<rect x="{x0}" y="{bottom - 34}" width="{x1 - x0}" height="16" fill="{C["gold"]}"/>', T, 2)
    return avoid(out, 'hem')


def grip(x, y, rot=0, s=1.0, sleeve=420, open_=False):
    """A small hand. Closed: a fist with four curled fingers (grips the hem edge).
    Open: palm with four straight fingers. A teal sleeve runs back along local -x."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    sl = (f'<rect x="{-sleeve}" y="-46" width="{sleeve - 40}" height="92" rx="16" fill="{C["teal"]}"/>'
          f'<rect x="-70" y="-50" width="34" height="100" rx="10" fill="{C["tealDeep"]}"/>')
    if open_:
        fingers = ''.join(f'<rect x="20" y="{-40 + n * 21}" width="{74 - abs(n - 1.5) * 12:.0f}" height="18" rx="9" '
                          f'transform="rotate({(n - 1.5) * 9:.0f} 20 {-31 + n * 21})"/>' for n in range(4))
        hand = (f'<g fill="{C["sandLight"]}"><rect x="-44" y="-44" width="82" height="86" rx="32"/>{fingers}'
                f'<rect x="-14" y="-74" width="58" height="20" rx="10" transform="rotate(-30 0 -60)"/></g>')
    else:
        knuckles = ''.join(f'<path d="M {6 + n * 2} {-38 + n * 24} q 38 -6 40 12" fill="none" stroke="{C["goldDeep"]}" '
                           f'stroke-opacity=".5" stroke-width="5" stroke-linecap="round"/>' for n in range(4))
        hand = (f'<path d="M -44 -48 Q -10 -60 40 -50 Q 70 -40 70 0 Q 72 48 36 56 Q -10 62 -44 50 Z" fill="{C["sandLight"]}"/>'
                + knuckles)
    return avoid(paper(f'<g transform="{tr}">{sl}{hand}</g>', T, 3), 'hand')


def mum_sleeve(x, y, rot=150, spoon=True):
    """Mum's pearl sleeve from the right edge, her hand on a wooden spoon in the pot."""
    tr = f'translate({x} {y}) rotate({rot})'
    sp = f'<rect x="40" y="-12" width="190" height="24" rx="10" fill="{C["goldDeep"]}"/>' if spoon else ''
    g = (f'<g transform="{tr}">{sp}'
         f'<rect x="-330" y="-70" width="310" height="140" rx="24" fill="{C["pearl"]}"/>'
         f'<rect x="-40" y="-74" width="44" height="148" rx="12" fill="{C["deep"]}"/>'
         f'<path d="M 0 -52 Q 90 -64 120 -16 Q 128 20 96 44 Q 50 62 0 50 Z" fill="{C["sandLight"]}"/></g>')
    return avoid(paper(g, T, 3), 'sleeve')


def chair(x, top, w=260, legs_to=1290):
    """A gold kitchen chair seen low, under the counter: seat edge + four legs."""
    out = paper(f'<rect x="{x}" y="{top}" width="{w}" height="40" rx="10" fill="{C["gold"]}"/>'
                f'<rect x="{x + 14}" y="{top + 30}" width="26" height="{legs_to - top - 30}" rx="8" fill="{C["goldDeep"]}"/>'
                f'<rect x="{x + w - 40}" y="{top + 30}" width="26" height="{legs_to - top - 30}" rx="8" fill="{C["goldDeep"]}"/>'
                f'<rect x="{x + 20}" y="{legs_to - 70}" width="{w - 40}" height="18" rx="6" fill="{C["goldDeep"]}"/>', T, 2)
    return avoid(out, 'chair')


def child_back(cx, cy, r=110):
    """The child from behind: a round goldDeep head (hair), two ears, teal shoulders.
    No face."""
    out = paper(f'<path d="M {cx - r * 1.7} {cy + r * 1.9} Q {cx - r * 1.6} {cy + r * 1.05} {cx} {cy + r} '
                f'Q {cx + r * 1.6} {cy + r * 1.05} {cx + r * 1.7} {cy + r * 1.9} Z" fill="{C["teal"]}"/>', T, 2)
    out += paper(f'<ellipse cx="{cx - r * .98}" cy="{cy + r * .1}" rx="{r * .16}" ry="{r * .26}" fill="{C["sandLight"]}" stroke="{C["goldDeep"]}" stroke-opacity=".3" stroke-width="3"/>'
                 f'<ellipse cx="{cx + r * .98}" cy="{cy + r * .1}" rx="{r * .16}" ry="{r * .26}" fill="{C["sandLight"]}" stroke="{C["goldDeep"]}" stroke-opacity=".3" stroke-width="3"/>', T, 2)
    out += paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["goldDeep"]}"/>', T, 3)
    return avoid(out, 'child')


def zabdiya(cx, cy, w=520):
    """A wide zabdiya (clay bowl): deep outside, pearl rim, teal water with
    cucumbers floating."""
    rx, ry = w / 2, w * .16
    body = paper(f'<path d="M {cx - rx} {cy} Q {cx - rx * .9} {cy + w * .42} {cx} {cy + w * .44} '
                 f'Q {cx + rx * .9} {cy + w * .42} {cx + rx} {cy} Z" fill="{C["deep"]}"/>'
                 f'<rect x="{cx - rx * .3}" y="{cy + w * .4}" width="{rx * .6}" height="{w * .07}" rx="8" fill="{C["night"]}"/>'
                 f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{C["pearl"]}"/>'
                 f'<ellipse cx="{cx}" cy="{cy + 6}" rx="{rx * .9}" ry="{ry * .76}" fill="{C["teal"]}"/>'
                 + ''.join(f'<path d="M {cx - rx * .7 + k * rx * .35} {cy + 4} q {rx * .08} -8 {rx * .16} 0" fill="none" stroke="{C["tealMist"]}" stroke-width="5" stroke-linecap="round"/>' for k in range(5)),
                 T, 2)
    cukes = ''
    for k, (dx, dy, a) in enumerate(((-.45, -.05, -12), (-.05, .1, 8), (.38, -.04, -20))):
        cukes += cucumber(cx + dx * rx, cy + dy * ry, a, .9)
    return avoid(body + cukes, 'bowl')


def cucumber(x, y, rot=0, s=1.0):
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    return paper(f'<rect x="-84" y="-24" width="168" height="48" rx="24" fill="{C["tealDeep"]}"/>'
                 f'<rect x="-70" y="-14" width="140" height="8" rx="4" fill="{C["teal"]}" fill-opacity=".8"/>'
                 + ''.join(f'<circle cx="{-50 + k * 25}" cy="10" r="3.5" fill="{C["tealMist"]}"/>' for k in range(5))
                 + f'<rect x="78" y="-8" width="16" height="16" rx="4" fill="{C["goldDeep"]}"/>', T, 3, T=tr)


def bubble(cx, cy, w, inner='', tail=(1, 1), seed=0):
    """Wordless pearl speech bubble; tail points along tail=(dx, dy)."""
    rx, ry = w / 2, w * .38
    tx, ty = tail
    bx, by = cx + tx * rx * .35, cy + ry * .75
    t = (f'<polygon points="{bx - 30},{by} {bx + tx * rx * .5},{cy + ry * 1.45} {bx + 40},{by - 6}" fill="{C["pearl"]}"/>')
    return avoid(paper(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{C["pearl"]}"/>' + t, T, 2) + inner, 'bubble')


def onion(cx, cy, r):
    out = paper(f'<path d="M {cx} {cy - r * 1.25} Q {cx + r * .2} {cy - r * .9} {cx + r} {cy - r * .1} '
                f'Q {cx + r * 1.05} {cy + r * .9} {cx} {cy + r} Q {cx - r * 1.05} {cy + r * .9} {cx - r} {cy - r * .1} '
                f'Q {cx - r * .2} {cy - r * .9} {cx} {cy - r * 1.25} Z" fill="{C["gold"]}"/>'
                + ''.join(f'<path d="M {cx} {cy - r * 1.1} Q {cx + k * r * .32} {cy} {cx} {cy + r * .95}" fill="none" '
                          f'stroke="{C["goldDeep"]}" stroke-opacity=".55" stroke-width="5"/>' for k in (-2, -1, 1, 2))
                + f'<path d="M {cx - r * .25} {cy + r * .98} l -6 18 M {cx} {cy + r} v 20 M {cx + r * .25} {cy + r * .98} l 6 18" '
                  f'stroke="{C["goldDeep"]}" stroke-width="5" stroke-linecap="round"/>', T, 3)
    return out


def rice(cx, cy, r):
    """A small deep bowl heaped with pearl rice grains."""
    grains = ''
    k = 0
    for row in range(4):
        for col in range(-3 + row // 2, 4 - row // 2):
            gx = cx + col * r * .26 + (row % 2) * r * .13
            gy = cy - r * .05 - row * r * .17
            grains += f'<ellipse cx="{gx:.1f}" cy="{gy:.1f}" rx="{r * .12:.1f}" ry="{r * .06:.1f}" transform="rotate({(k * 47) % 60 - 30} {gx:.1f} {gy:.1f})" fill="{C["pearl"]}" stroke="{C["goldDeep"]}" stroke-opacity=".5" stroke-width="2.5"/>'
            k += 1
    heap = f'<path d="M {cx - r * .95} {cy} Q {cx} {cy - r * 1.05} {cx + r * .95} {cy} Z" fill="{C["sandLight"]}"/>'
    bowl = (f'<path d="M {cx - r} {cy} Q {cx - r * .9} {cy + r * .8} {cx} {cy + r * .8} Q {cx + r * .9} {cy + r * .8} {cx + r} {cy} Z" fill="{C["deep"]}"/>'
            f'<rect x="{cx - r}" y="{cy - 6}" width="{2 * r}" height="12" rx="6" fill="{C["tealDeep"]}"/>')
    return paper(heap + grains + bowl, T, 3)


def note(x, y, w, h, rot, seed, icon=''):
    """A torn pearl note with a strip of gold tape, carrying an icon."""
    tape = torn_rect(x + w / 2 - 60, y - 22, 120, 44, C['gold'], T, sides='lr', seed=seed + 50, layer=3, rot=rot - 4, amp=(2, 5))
    return avoid(torn_rect(x, y, w, h, C['pearl'], T, seed=seed, layer=2, rot=rot) + icon + tape, f'note{seed}')


def day_strip(cx, cy, w):
    """A day strip: a gold sun at the right end (RTL start), a deep moon at the left."""
    out = torn_rect(cx - w / 2, cy - 14, w, 28, C['tealMist'], T, sides='tb', seed=81, layer=2, amp=(2, 4))
    out += paper(f'<circle cx="{cx + w / 2 - 6}" cy="{cy}" r="34" fill="{C["gold"]}"/>'
                 f'<path d="M {cx - w / 2 + 10} {cy - 34} A 34 34 0 1 0 {cx - w / 2 + 10} {cy + 34} A 22 34 0 1 1 {cx - w / 2 + 10} {cy - 34} Z" fill="{C["deep"]}"/>', T, 3)
    return out


def one_spot(cx, cy, r):
    """One situation picked out: one gold disc, the others small and dim."""
    out = ''
    for k in range(6):
        a = math.radians(k * 60 + 20)
        out += f'<circle cx="{cx + r * 1.3 * math.cos(a):.1f}" cy="{cy + r * 1.3 * math.sin(a):.1f}" r="{r * .22:.1f}" fill="{C["tealMist"]}" stroke="{C["tealDeep"]}" stroke-opacity=".5" stroke-width="3"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="{r * .62}" fill="{C["gold"]}"/>'
    return paper(out, T, 3)


def loop_two(cx, cy, r):
    """Adjust every two weeks: a loop arrow of deep paper with two gold stops ON the
    ring (never inside it: two dots in a circle would read as a face)."""
    a0, a1 = -60, 230
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / 30)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / 30))) for i in range(31)]
    out = torn_strip(pts, 22, C['deep'], T, seed=91, layer=2)
    ex, ey = pts[-1]
    out += paper(f'<polygon points="{ex - 30},{ey - 6} {ex + 30},{ey - 14} {ex + 4},{ey + 34}" fill="{C["deep"]}"/>'
                 + ''.join(f'<circle cx="{cx + r * math.cos(math.radians(g)):.1f}" cy="{cy + r * math.sin(math.radians(g)):.1f}" r="{r * .2}" fill="{C["gold"]}"/>'
                           for g in (20, 140)), T, 3)
    return out


# ---------------------------------------------------------------- slides
KEEP = {
    2: ('تفتحي الثلاجة، ويمسك رجلك.', 'تقطعي البصل، ويسحب بلوزتك.'),
    7: ('طريقتنا في الخطة الحية:', 'نشوف يومه كامل'),
    8: ('ولا لما تبدئي تطبخي.',),
}


def slide(ctx):
    s = ctx.s
    if s in KEEP:
        keep_in(ctx.t.segs, *KEEP[s])
    if s == 2:
        ctx.t.body()[0].comma = 'glue'
    if s == 7:
        brk(ctx.t.body()[0], 'الحية: ')
    if ctx.last:
        mini = pot(860, 1250, .55, steam=True, seed=41) + counter(1250, 50, 560, 1100)
        return cta_end(ctx, mini_art=mini, tag_x=MX + 10, tag_y=1040)
    art, html = '', ''
    if s == 1:
        cy = 960
        art = (pot(205, cy, .85, seed=3, sn=5) + counter(cy) + hem(560, 1000, cy - 40)
               + grip(640, 1130, rot=-8, s=1.1, sleeve=700))
        html = hook_box(ctx, G, y=MT - 10, size=96, w=920, keep=('غدا بكرة',))
    elif s == 2:
        cy = 990
        art = (pot(700, cy, .85, seed=7, lid=False, steam=False) + mum_sleeve(880, 795, rot=168) + counter(cy)
               + hem(560, 1000, cy - 30) + grip(620, 1140, rot=-16, s=1.0, sleeve=700))
        html = body_box(ctx, G)
    elif s == 3:
        cy = 860
        art = (pot(290, cy, .9, seed=11, sn=5) + counter(cy) + hem(600, 1020, cy - 40)
               + grip(400, 1130, rot=8, s=1.1, sleeve=520, open_=True))
        html = body_box(ctx, G, y=MT + 40)
    elif s == 4:
        cy = 1070
        art = (pot(230, cy, .7, seed=15, sn=6) + child_back(760, 1000, 95) + counter(cy) + chair(600, cy + 96, w=280, legs_to=1250))
        html = body_box(ctx, G) + soft_cta(ctx, y=652, w=620)
    elif s == 5:
        cy = 1060
        art = (counter(cy) + zabdiya(480, 930, 620) + cucumber(760, 800, 75, .95)
               + grip(780, 740, rot=160, s=.9, sleeve=420)
               + ''.join(paper(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="14" fill="{C["teal"]}"/>', T, 1) for x, y in ((735, 905), (770, 880))))
        html = body_box(ctx, G)
    elif s == 6:
        cy = 1080
        art = (pot(240, cy, .6, seed=19) + child_back(820, 980, 90) + counter(cy)
               + bubble(330, 770, 300, onion(330, 760, 70), tail=(1, 1))
               + bubble(700, 790, 280, rice(700, 810, 90), tail=(-1, 1)))
        html = body_box(ctx, G)
    elif s == 7:
        art = (note(680, 710, 310, 270, 3, 1, day_strip(835, 845, 220))
               + note(380, 830, 290, 280, -4, 2, one_spot(525, 970, 95))
               + note(90, 950, 290, 280, 5, 3, loop_two(235, 1090, 85)))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
