"""p2 Sneaking out. Night ground, pearl text. Composition: THRESHOLD.

A dark bedroom seen side-on: the door on the left with a vertical sliver of
pearl hall light, the bed on the right with a small shape under the duvet
(never a face). Across the slides the door is the story:
s1 the door ajar, a thin sliver of light; s2 gold tiptoe prints step toward the
light and a wordless pearl bubble rises from the bed to the door; s3 back
beside the bed (mum's sleeve, her hand on the duvet), the door shut again;
s4 the door half open, mum's silhouette in the light, leaving while he watches;
s5 three torn gold tags on the door frame carrying 1, 2 and 5 dots;
s6 the door open and the door shut joined by a loop of torn strips.
CTA end: gold, a small door with its light sliver in the bottom-left.
"""
import math
from kit import C, MX, MT, W, H, keep_in, paper, torn_strip, torn_rect, torn_circle, torn_poly, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'night'
T = 'd'
FLOOR = 1190


# ---------------------------------------------------------------- pieces
def floor(y=FLOOR):
    return torn_poly([(-40, y), (W + 40, y), (W + 40, H + 40), (-40, H + 40)], C['deep'], T, torn=[0], seed=301, amp=(4, 9))


def door(x, top, w=290, bottom=FLOOR, gap=34, wedge=True, sill=True):
    """A door in the wall. gap = how far it is open (px of hall light showing,
    on the latch side, the right). The leaf is drawn foreshortened as it swings
    in, so a wider gap also narrows the leaf a little."""
    h = bottom - top
    out, light = '', ''
    if wedge and gap > 0:
        spread = 120 + gap * 2.2
        light += paper(f'<polygon points="{x + w - gap},{bottom} {x + w},{bottom} {x + w + spread * 1.6},{bottom + 160} {x + w - gap + spread * .5},{bottom + 160}" '
                     f'fill="{C["pearl"]}" fill-opacity=".22"/>', T, 1, 't')
    # opening: hall light
    out += paper(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" fill="{C["pearl"]}"/>', T, 1)
    # leaf: hinged on the left, swings into the room (its free edge comes towards us)
    lw = w - gap
    if lw > 0:
        k = gap / w
        out += paper(f'<polygon points="{x},{top} {x + lw},{top - 30 * k} {x + lw},{bottom + 30 * k} {x},{bottom}" fill="{C["deep"]}"/>'
                     f'<rect x="{x + lw * .16}" y="{top + h * .08}" width="{lw * .68}" height="{h * .34}" rx="6" fill="none" stroke="{C["night"]}" stroke-width="8"/>'
                     f'<rect x="{x + lw * .16}" y="{top + h * .52}" width="{lw * .68}" height="{h * .4}" rx="6" fill="none" stroke="{C["night"]}" stroke-width="8"/>'
                     f'<circle cx="{x + lw - 30}" cy="{top + h * .5}" r="11" fill="{C["gold"]}"/>', T, 2)
    frame = paper(f'<path d="M {x - 14} {bottom} V {top - 14} H {x + w + 14} V {bottom}" fill="none" stroke="{C["tealDeep"]}" stroke-width="26" stroke-linejoin="round"/>', T, 2)
    return light + avoid(out + frame, 'door')


def bed(x0, x1, lump=True, y=FLOOR):
    """Side view, headboard on the right. The child is only a lump under the
    pearl duvet: no head, no face."""
    fr = paper(f'<rect x="{x1 - 50}" y="{y - 340}" width="50" height="340" rx="14" fill="{C["deep"]}"/>'
               f'<rect x="{x0}" y="{y - 220}" width="44" height="220" rx="12" fill="{C["deep"]}"/>'
               f'<rect x="{x0 + 30}" y="{y - 110}" width="{x1 - x0 - 60}" height="50" rx="6" fill="{C["deep"]}"/>', T, 1)
    mat = paper(f'<rect x="{x0 + 36}" y="{y - 186}" width="{x1 - x0 - 80}" height="80" rx="16" fill="{C["sandLight"]}"/>', T, 2)
    pil = paper(f'<path d="M {x1 - 200} {y - 182} Q {x1 - 196} {y - 246} {x1 - 124} {y - 242} Q {x1 - 60} {y - 238} {x1 - 60} {y - 182} Z" fill="{C["tealMist"]}"/>', T, 2)
    bx0, bx1, by = x0 + 26, x1 - 130, y - 182
    if lump:
        L = bx1 - bx0
        d = (f'M {bx0} {by + 70} L {bx0} {by} Q {bx0 + L * .3} {by - 8} {bx0 + L * .42} {by - 50} '
             f'Q {bx0 + L * .62} {by - 140} {bx0 + L * .8} {by - 80} Q {bx0 + L * .9} {by - 46} {bx1} {by - 30} L {bx1} {by + 70} Z')
    else:
        d = f'M {bx0} {by + 70} L {bx0} {by} L {bx1} {by - 20} L {bx1} {by + 70} Z'
    duv = paper(f'<path d="{d}" fill="{C["pearl"]}"/>'
                f'<path d="M {bx0} {by + 40} L {bx1} {by + 40}" stroke="{C["gold"]}" stroke-width="10" stroke-opacity=".7"/>', T, 3)
    return avoid(fr + mat + pil + duv, 'bed')


def prints(pts, s=1.0, col='gold'):
    """Tiptoe prints: only the ball of the foot and the toes touch the floor."""
    out = ''
    for k, (x, y) in enumerate(pts):
        sx = -1 if k % 2 else 1
        out += (f'<g transform="translate({x} {y}) rotate(-90) scale({s * sx} {s})">'
                f'<ellipse cx="0" cy="0" rx="20" ry="26" fill="{C[col]}"/>'
                + ''.join(f'<circle cx="{-12 + t * 9}" cy="{-36 + abs(t - 1.5) * 4}" r="{6 - abs(t - 1.5) * 1.2:.1f}" fill="{C[col]}"/>' for t in range(4))
                + '</g>')
    return avoid(paper(out, T, 2), 'prints')


def bubble(cx, cy, w, tail_to):
    """A wordless pearl speech bubble; the tail points at tail_to (x, y)."""
    rx, ry = w / 2, w * .36
    tx, ty = tail_to
    a = math.atan2(ty - cy, tx - cx)
    bx, by = cx + rx * .7 * math.cos(a), cy + ry * .7 * math.sin(a)
    n = (-math.sin(a) * 26, math.cos(a) * 26)
    t = f'<polygon points="{bx + n[0]:.1f},{by + n[1]:.1f} {tx},{ty} {bx - n[0]:.1f},{by - n[1]:.1f}" fill="{C["pearl"]}"/>'
    return avoid(paper(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{C["pearl"]}"/>' + t, T, 3), 'bubble')


def mum_back(cx, foot, h=560, col='ink'):
    """Mum's silhouette from behind: head with a scarf, shoulders, a long abaya."""
    r = h * .085
    top = foot - h
    d = (f'M {cx - h * .1} {top + r * 2.3} Q {cx - h * .2} {top + r * 2.6} {cx - h * .2} {top + h * .3} '
         f'L {cx - h * .26} {foot} L {cx + h * .26} {foot} L {cx + h * .2} {top + h * .3} '
         f'Q {cx + h * .2} {top + r * 2.6} {cx + h * .1} {top + r * 2.3} Z')
    out = paper(f'<path d="{d}" fill="{C[col]}"/><ellipse cx="{cx}" cy="{top + r * 1.25}" rx="{r * 1.1}" ry="{r * 1.3}" fill="{C[col]}"/>', T, 3)
    return avoid(out, 'mum')


def mum_hand(x, y, rot=-160, s=1.0):
    """Mum's pearl sleeve reaching in from the left edge, her hand on the duvet."""
    g = (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
         f'<rect x="20" y="-56" width="460" height="112" rx="20" fill="{C["tealMist"]}"/>'
         f'<rect x="0" y="-58" width="40" height="116" rx="10" fill="{C["tealDeep"]}"/>'
         f'<g fill="{C["sandLight"]}"><rect x="-70" y="-44" width="84" height="88" rx="30"/>'
         + ''.join(f'<rect x="{-150 + abs(n - 1.5) * 10:.0f}" y="{-40 + n * 21}" width="{96 - abs(n - 1.5) * 10:.0f}" height="18" rx="9"/>' for n in range(4))
         + '<rect x="-40" y="34" width="60" height="20" rx="10" transform="rotate(20 -10 44)"/></g></g>')
    return avoid(paper(g, T, 3), 'hand')


def tag(x, y, n, rot, seed):
    """A torn gold tag hanging from the frame on a short string, with n deep dots."""
    w, h = 110, 150
    string = paper(f'<path d="M {x + w / 2} {y - 60} L {x + w / 2} {y + 14}" stroke="{C["pearl"]}" stroke-width="4"/>', T, 1, 't')
    pos = {1: [(0, 0)], 2: [(0, -.22), (0, .22)], 5: [(-.24, -.26), (.24, -.26), (0, 0), (-.24, .26), (.24, .26)]}[n]
    dots = ''.join(f'<circle cx="{x + w / 2 + dx * w}" cy="{y + h / 2 + 10 + dy * h}" r="13" fill="{C["deep"]}"/>' for dx, dy in pos)
    return string + torn_rect(x, y, w, h, C['gold'], T, seed=seed, layer=3, rot=rot, inner=dots)


def loop(cx, cy, r, seed=50):
    """Two torn arcs chasing each other round: out through the door and back."""
    out = ''
    for k, (a0, a1) in enumerate(((-150, -30), (30, 150))):
        pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / 24)), cy + r * .62 * math.sin(math.radians(a0 + (a1 - a0) * i / 24))) for i in range(25)]
        out += torn_strip(pts, 26, C['gold'], T, seed=seed + k, layer=2)
        (ex, ey), (px, py) = pts[-1], pts[-3]
        a = math.atan2(ey - py, ex - px)
        tip = (ex + 40 * math.cos(a), ey + 40 * math.sin(a))
        l = (ex + 28 * math.cos(a + 1.6), ey + 28 * math.sin(a + 1.6))
        rr = (ex + 28 * math.cos(a - 1.6), ey + 28 * math.sin(a - 1.6))
        out += paper(f'<polygon points="{tip[0]:.1f},{tip[1]:.1f} {l[0]:.1f},{l[1]:.1f} {rr[0]:.1f},{rr[1]:.1f}" fill="{C["gold"]}"/>', T, 2)
    return avoid(out, 'loop')


# ---------------------------------------------------------------- slides
def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = (door(110, 930, w=170, bottom=1240, gap=26, wedge=False)
                + paper(f'<rect x="60" y="1240" width="330" height="14" rx="6" fill="{C["deep"]}"/>', T, 1))
        return cta_end(ctx, mini_art=mini, tag_x=W - MX - 500, tag_y=1080)
    art, html = '', ''
    if s == 1:
        art = floor() + door(90, 560, gap=30) + bed(470, 1040)
        html = hook_box(ctx, G, y=MT - 10, size=96, w=920,
                        keep=('وأول ما قُمتي', 'من جمبه', 'فتح عيونه؟'))
    elif s == 2:
        art = (floor() + door(90, 750, w=260, gap=44) + bed(560, 1040)
               + prints([(780, 1206), (660, 1220), (540, 1204), (420, 1218)], .8)
               + bubble(470, 800, 230, (600, 900)))
        html = body_box(ctx, G)
    elif s == 3:
        art = floor() + door(90, 760, w=240, gap=0, wedge=False) + bed(430, 1040) + mum_hand(720, 985, rot=-158, s=.7)
        html = body_box(ctx, G) + soft_cta(ctx, y=520)
    elif s == 4:
        art = (floor() + door(150, 600, w=330, gap=200) + mum_back(395, FLOOR + 10, 560)
               + bed(640, 1060))
        html = body_box(ctx, G)
    elif s == 5:
        art = (floor() + door(290, 850, w=500, gap=44)
               + tag(330, 905, 1, -4, 61) + tag(480, 920, 2, 3, 62) + tag(630, 905, 5, -2, 63))
        html = body_box(ctx, G)
    elif s == 6:
        art = (floor()
               + door(110, 620, w=280, gap=170) + door(690, 620, w=280, gap=0, wedge=False)
               + loop(540, 880, 330))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
