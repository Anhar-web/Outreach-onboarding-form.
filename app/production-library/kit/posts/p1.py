"""p1 park. Deep ground, dark. Top-down route map (replaces the photo hybrid).

Motif: a torn teal lawn island over the lower ~55% of the frame with tealDeep tree
crowns seen from above; a gold picnic blanket with pearl stripes at the
bottom-right; a dashed pearl paper path winding from it to a small night car with
pearl windows, parked in a pearl-lined bay on the deep "road" at the top-left.
s1: hook question on a torn pearl strip (-1.5deg) across the top third, ink 88px;
    the clause below it in pearl at 54px.
Inner slides: things travel the path. s2 four empty waypoints on the path; s3 the
    camera drops onto the car: a gold map pin; s4 bag > ball > blanket lift off in
    order along the path; s5 the ball, carried, mid-path; s6 the car with its roof
    off: a gold juice box on the back seat. s7 attention end: quiet line, the car.
"""
import math
from kit import (torn_circle_pts, C, MX, MT, W, H, paper, torn_rect, torn_poly, torn_circle, torn_ring, glow,
                 text_box, step_tab, avoid, keep_in, torn_line_pts, P)

TONE = 'd'
CAR = (205, 705)        # car centre (map coords); nose up
BLANKET = (800, 1060)


# ---------------------------------------------------------------- path geometry
def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return (u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
            u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1])


PATH = [(650, 1060), (430, 1150), (230, 1040), (210, 850)]     # blanket -> car (map coords)
_S = [bez(*PATH, k / 400) for k in range(401)]
_L = [0.0]
for a, b in zip(_S, _S[1:]):
    _L.append(_L[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))


def at(f):
    """Point and tangent angle (deg) at fraction f of the path's length (0 = blanket, 1 = car)."""
    target = f * _L[-1]
    k = next(i for i, l in enumerate(_L) if l >= target) if f < 1 else 400
    k = max(1, k)
    (ax, ay), (bx, by) = _S[k - 1], _S[k]
    return (bx, by), math.degrees(math.atan2(by - ay, bx - ax))


def dashes(dash=34, gap=22, width=17, f0=0.0, f1=1.0, seed=0):
    """The dashed pearl path: small torn pearl strips along the curve, one sheet."""
    out, pos, k = '', f0 * _L[-1], 0
    while pos + dash <= f1 * _L[-1]:
        a, _ = at(pos / _L[-1])
        b, _ = at((pos + dash) / _L[-1])
        m, _ = at((pos + dash / 2) / _L[-1])
        out += f'<polygon points="{P(torn_line_pts([a, m, b], width, seed + k, amp=(1.5, 3.5)))}" fill="{C["pearl"]}"/>'
        pos += dash + gap
        k += 1
    return out


# ---------------------------------------------------------------- motifs (map coords)
LAWN = [(-40, 880), (110, 852), (300, 800), (470, 735), (640, 690), (820, 650), (980, 632), (1120, 640),
        (1120, 1400), (-40, 1400)]
TREES = [(470, 880, 50, 1), (110, 1150, 72, 2), (350, 1290, 52, 3), (1000, 760, 62, 4), (1040, 1250, 58, 5)]


def tree(x, y, r, seed, T):
    """Tree crown from above: three overlapping tealDeep lobes, lit from the top-right."""
    lobes = ''.join(f'<polygon points="{P(torn_circle_pts(x + dx * r, y + dy * r, r * rr, seed + 40 + k, (3, 7)))}" fill="{C["tealDeep"]}"/>'
                    for k, (dx, dy, rr) in enumerate(((-.28, .18, .72), (.3, .12, .66), (0, -.26, .7))))
    lit = ''.join(f'<circle cx="{x + dx * r:.1f}" cy="{y + dy * r:.1f}" r="{r * rr:.1f}" fill="{C["teal"]}" fill-opacity=".55"/>'
                  for dx, dy, rr in ((.38, -.1, .26), (.12, -.4, .24)))
    return paper(lobes + lit, TONE, 2, 't', T=T)


def blanket(cx, cy, w=300, h=220, rot=-8, T='', layer=1, seed=0):
    stripes = ''.join(f'<rect x="{cx - w / 2 + w * f:.1f}" y="{cy - h / 2}" width="{w * .07:.1f}" height="{h}" fill="{C["pearl"]}"/>'
                      for f in (.16, .3, .64, .78))
    fringe = ''.join(f'<rect x="{cx - w / 2 + 8 + k * (w - 16) / 11:.1f}" y="{cy + h / 2 - 2}" width="6" height="18" fill="{C["goldDeep"]}"/>'
                     for k in range(12))
    g = (f'<g transform="rotate({rot} {cx} {cy})"><rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="6" fill="{C["gold"]}"/>'
         f'{stripes}{fringe}</g>')
    return avoid(paper(g, TONE, layer, T=T), 'blanket')


def car(cx, cy, s=1.0, T='', roof=True, juice=False, layer=2):
    """Small top-down car, nose up: night body, pearl windows, ink wheels.
    roof=False shows the inside: sandLight seats (and a gold juice box)."""
    w, h = 130 * s, 230 * s
    x, y = cx - w / 2, cy - h / 2
    wheels = ''.join(f'<rect x="{wx:.1f}" y="{wy:.1f}" width="{18 * s:.1f}" height="{44 * s:.1f}" rx="{6 * s:.1f}" fill="{C["ink"]}"/>'
                     for wx in (x - 8 * s, x + w - 10 * s) for wy in (y + 30 * s, y + h - 74 * s))
    body = f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{38 * s:.1f}" fill="{C["night"]}"/>'
    lights = (f'<rect x="{x + 14 * s:.1f}" y="{y + 6 * s:.1f}" width="{22 * s:.1f}" height="{10 * s:.1f}" rx="{4 * s:.1f}" fill="{C["gold"]}"/>'
              f'<rect x="{x + w - 36 * s:.1f}" y="{y + 6 * s:.1f}" width="{22 * s:.1f}" height="{10 * s:.1f}" rx="{4 * s:.1f}" fill="{C["gold"]}"/>')
    if roof:
        top = (f'<polygon points="{x + 16 * s:.1f},{y + 78 * s:.1f} {x + w - 16 * s:.1f},{y + 78 * s:.1f} {x + w - 26 * s:.1f},{y + 46 * s:.1f} {x + 26 * s:.1f},{y + 46 * s:.1f}" fill="{C["pearl"]}"/>'
               f'<rect x="{x + 20 * s:.1f}" y="{y + 86 * s:.1f}" width="{w - 40 * s:.1f}" height="{90 * s:.1f}" rx="{14 * s:.1f}" fill="{C["deep"]}"/>'
               f'<polygon points="{x + 22 * s:.1f},{y + 184 * s:.1f} {x + w - 22 * s:.1f},{y + 184 * s:.1f} {x + w - 30 * s:.1f},{y + 206 * s:.1f} {x + 30 * s:.1f},{y + 206 * s:.1f}" fill="{C["pearl"]}"/>')
        return avoid(paper(wheels + body + lights + top, TONE, layer, T=T), 'car')
    # roof off: windscreen, two front seats, back bench
    inside = (f'<polygon points="{x + 16 * s:.1f},{y + 70 * s:.1f} {x + w - 16 * s:.1f},{y + 70 * s:.1f} {x + w - 26 * s:.1f},{y + 40 * s:.1f} {x + 26 * s:.1f},{y + 40 * s:.1f}" fill="{C["pearl"]}"/>'
              f'<rect x="{x + 14 * s:.1f}" y="{y + 66 * s:.1f}" width="{w - 28 * s:.1f}" height="{h - 84 * s:.1f}" rx="{20 * s:.1f}" fill="{C["deep"]}"/>'
              f'<rect x="{x + 22 * s:.1f}" y="{y + 86 * s:.1f}" width="{40 * s:.1f}" height="{50 * s:.1f}" rx="{10 * s:.1f}" fill="{C["sandLight"]}"/>'
              f'<rect x="{x + w - 62 * s:.1f}" y="{y + 86 * s:.1f}" width="{40 * s:.1f}" height="{50 * s:.1f}" rx="{10 * s:.1f}" fill="{C["sandLight"]}"/>'
              f'<rect x="{x + 22 * s:.1f}" y="{y + 156 * s:.1f}" width="{w - 44 * s:.1f}" height="{52 * s:.1f}" rx="{12 * s:.1f}" fill="{C["sandLight"]}"/>')
    out = paper(wheels + body + lights + inside, TONE, layer, T=T)
    if juice:   # gold juice box on the back bench, pearl straw
        jx, jy = cx + 4 * s, y + 160 * s
        hT = f' transform="{T}"' if T else ''
        out += glow(f'<circle cx="{jx + 13 * s:.1f}" cy="{jy + 17 * s:.1f}" r="{34 * s:.1f}" fill="{C["gold"]}" fill-opacity=".7"{hT}/>', 's')
        out += paper(f'<rect x="{jx:.1f}" y="{jy:.1f}" width="{26 * s:.1f}" height="{34 * s:.1f}" rx="{3 * s:.1f}" fill="{C["gold"]}"/>'
                     f'<rect x="{jx + 4 * s:.1f}" y="{jy + 12 * s:.1f}" width="{18 * s:.1f}" height="{12 * s:.1f}" fill="{C["pearl"]}" fill-opacity=".85"/>'
                     f'<path d="M {jx + 19 * s:.1f} {jy + 2 * s:.1f} L {jx + 25 * s:.1f} {jy - 14 * s:.1f} L {jx + 32 * s:.1f} {jy - 18 * s:.1f}" fill="none" stroke="{C["pearl"]}" stroke-width="{3.4 * s:.1f}" stroke-linecap="round"/>',
                     TONE, layer + 1, T=T)
    return avoid(out, 'car')


def bay(cx, cy, T):
    """Parking bay: three pearl lines on the deep road."""
    w = 190
    lines = ''.join(f'<rect x="{cx + dx - 4}" y="{cy - 140}" width="8" height="260" fill="{C["pearl"]}" fill-opacity=".55"/>' for dx in (-w / 2 - 10, w / 2 + 10))
    lines += f'<rect x="{cx - w / 2 - 14}" y="{cy - 140}" width="{w + 28}" height="8" fill="{C["pearl"]}" fill-opacity=".55"/>'
    return paper(lines, TONE, 1, 't', T=T)


def pin(x, y, s=1.0, T=''):
    """Gold map pin, tip at (x, y)."""
    r = 34 * s
    d = (f'M {x} {y} C {x - r * .5:.1f} {y - r * 1.2:.1f} {x - r * 1.05:.1f} {y - r * 1.6:.1f} {x - r * 1.05:.1f} {y - r * 2.3:.1f} '
         f'A {r * 1.05:.1f} {r * 1.05:.1f} 0 1 1 {x + r * 1.05:.1f} {y - r * 2.3:.1f} '
         f'C {x + r * 1.05:.1f} {y - r * 1.6:.1f} {x + r * .5:.1f} {y - r * 1.2:.1f} {x} {y} Z')
    return avoid(paper(f'<path d="{d}" fill="{C["gold"]}"/><circle cx="{x}" cy="{y - r * 2.3:.1f}" r="{r * .42:.1f}" fill="{C["pearl"]}"/>',
                       TONE, 3, T=T), 'pin')


def bag(cx, cy, s=1.0, T='', layer=3):
    """Food bag from above: sandLight sack with goldDeep handles."""
    w, h = 96 * s, 80 * s
    return avoid(paper(f'<rect x="{cx - w / 2:.1f}" y="{cy - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{10 * s:.1f}" fill="{C["sandLight"]}"/>'
                       f'<path d="M {cx - w * .3:.1f} {cy - h * .2:.1f} Q {cx:.1f} {cy - h * .9:.1f} {cx + w * .3:.1f} {cy - h * .2:.1f}" fill="none" stroke="{C["goldDeep"]}" stroke-width="{7 * s:.1f}" stroke-linecap="round"/>'
                       f'<rect x="{cx - w / 2:.1f}" y="{cy + h * .18:.1f}" width="{w:.1f}" height="{h * .14:.1f}" fill="{C["gold"]}"/>',
                       TONE, layer, T=T), 'bag')


def ball(cx, cy, r=34, T='', layer=3):
    return avoid(paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["pearl"]}"/>'
                       f'<path d="M {cx - r} {cy} Q {cx} {cy - r * .55} {cx + r} {cy}" fill="none" stroke="{C["deep"]}" stroke-width="{r * .18:.1f}"/>'
                       f'<path d="M {cx - r * .7:.1f} {cy + r * .7:.1f} Q {cx} {cy + r * .1:.1f} {cx + r * .7:.1f} {cy + r * .7:.1f}" fill="none" stroke="{C["gold"]}" stroke-width="{r * .18:.1f}"/>'
                       f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C["deep"]}" stroke-opacity=".25" stroke-width="2"/>',
                       TONE, layer, T=T), 'ball')


def waypoint(x, y, T, lit=False):
    if lit:
        return avoid(paper(f'<circle cx="{x}" cy="{y}" r="26" fill="{C["gold"]}"/><circle cx="{x}" cy="{y}" r="10" fill="{C["pearl"]}"/>', TONE, 3, T=T), 'waypoint')
    return avoid(paper(f'<circle cx="{x}" cy="{y}" r="24" fill="{C["deep"]}" stroke="{C["pearl"]}" stroke-width="7"/>', TONE, 3, T=T), 'waypoint')


def park(T='', items=(), roof=True, juice=False, blanket_on=True, path=(0.0, 1.0)):
    """The whole map in map coords, drawn through transform T."""
    o = [torn_poly(LAWN, C['teal'], TONE, torn=list(range(8)), seed=19, T=T, amp=(5, 11))]
    for (x, y, r, sd) in TREES:
        o.append(avoid(tree(x, y, r, sd, T), 'tree'))
    o.append(bay(CAR[0], CAR[1], T))
    o.append(paper(dashes(f0=path[0], f1=path[1]), TONE, 1, 't', T=T))
    if blanket_on:
        o.append(blanket(*BLANKET, T=T))
    o.append(car(CAR[0], CAR[1], 1.0, T=T, roof=roof, juice=juice))
    o += [f(T) for f in items]
    return ''.join(o)


# ---------------------------------------------------------------- slides
BREAKS = {
    1: ['كل رجعه من الحديقة', 'نفس المعركة؟', 'جهزيه للخروج من اول ما توصلوا،', 'مو آخر خمس دقايق.'],
    2: ['هذي أربع أشياء تبدأ', 'من أول ما تفرشوا الفرشه،', 'عشان ما يحس إنكم', 'فجأة قررتوا تمشوا.'],
    3: ['أول ما تنزلوا من السيارة،', 'وريه فين وقفتوا.', '"هذي سيارتنا،', 'نرجع لها بعدين."'],
    4: ['ولما يقرب وقت الرجعة،', 'لمّي الأغراض قدامه شوي شوي.', 'كيس الأكل أول،', 'بعدين الألعاب،', 'والفرشة آخر شي.'],
    5: ['وخلي له شي يشيله بنفسه.', 'الكورة، أو شنطته الصغيرة،', 'هو اللي يوديها للسيارة.'],
    6: ['وخلي في السيارة شي يحبه،', 'يلقاه أول ما يركب.', 'عصير، أو لعبة', 'ما تطلع إلا في طريق الرجعة.'],
    7: ['كذا لما تقولي يلا نمشي،', 'يكون عارف', 'إن وقت الخرجة خلص.'],
}


def body(ctx, top=None):
    html = ''
    if ctx.t.label():
        html += step_tab(ctx.t.label())
    top = top or (MT + 118 if ctx.t.label() else MT + 20)
    return html + text_box(ctx.t.body(), MX, top, W - 2 * MX, 'pearl')


def slide(ctx):
    s = ctx.s
    r = {'ground': 'deep'}
    if s == 1:
        q, clause = ctx.t.split_seg(ctx.t.body()[0], '؟ ')
        clause.role = 'clause'
    keep_in(ctx.t.segs, *BREAKS[s])

    if s == 1:
        # hook on a torn pearl strip across the top third; the map below
        strip = torn_rect(-30, 112, 1140, 300, C['pearl'], TONE, 'tb', seed=11, layer=2, rot=-1.5)
        art = strip + park('translate(0 40)')
        html = (text_box([q], MX + 14, 140, W - 2 * MX - 28, 'ink', size={'hook': 88}, style='transform:rotate(-1.5deg)')
                + text_box([clause], MX, 452, W - 2 * MX, 'pearl'))
        r.update(art=art, html=html)

    elif s == 2:
        # four empty waypoints on the path: four things, starting at the blanket
        T = 'translate(0 40)'
        wps = [lambda T, f=f: waypoint(*at(f)[0], T) for f in (.14, .38, .62, .86)]
        r.update(art=park(T, items=wps), html=body(ctx))

    elif s == 3:
        # the camera drops onto the car: gold pin, "this is our car"
        T = 'translate(-60 -470) scale(1.85)'
        r.update(art=park(T, items=[lambda T: pin(CAR[0] + 6, CAR[1] - 40, 1.0, T)]), html=body(ctx))

    elif s == 4:
        # pack up in order, in front of him: bag (first, nearly at the car), ball, then the blanket lifts off
        T = 'translate(0 30)'
        bx, by = BLANKET
        ghost = lambda T: paper(f'<rect x="{bx - 150}" y="{by - 110}" width="300" height="220" rx="6" fill="none" stroke="{C["pearl"]}" '
                                f'stroke-opacity=".45" stroke-width="6" stroke-dasharray="20 14" transform="rotate(-8 {bx} {by})"/>', TONE, 1, 't', T=T)
        items = [ghost,
                 lambda T: bag(*at(.84)[0], 1.0, T),
                 lambda T: ball(*at(.5)[0], 34, T),
                 lambda T: blanket(bx - 40, by - 20, 150, 84, 10, T, layer=3, seed=3)]
        r.update(art=park(T, items=items, blanket_on=False), html=body(ctx))

    elif s == 5:
        # he carries the ball himself: the ball on the path, the walked part of the path in gold
        T = 'translate(-90 -60) scale(1.18)'
        (bx, by), _ = at(.55)
        walked = lambda T: paper(dashes(f0=0.0, f1=.52, seed=40).replace(C['pearl'], C['gold']), TONE, 2, 't', T=T)
        items = [walked, lambda T: ball(bx, by, 44, T)]
        r.update(art=park(T, items=items), html=body(ctx, top=MT + 40))

    elif s == 6:
        # something he loves waits in the car: roof off, a gold juice box on the back seat
        T = 'translate(-60 -540) scale(2.1)'
        r.update(art=park(T, roof=False, juice=True), html=body(ctx))

    else:
        # attention end: quiet line centred, one accent (the car in its bay, the path arriving)
        for g in ctx.t.body():
            g.role = 'quiet'
        T = 'translate(330 260)'
        accent = (bay(CAR[0], CAR[1], T)
                  + paper(dashes(f0=.72, f1=1.0, seed=70), TONE, 1, 't', T=T)
                  + car(CAR[0], CAR[1], 1.0, T=T))
        r.update(art=accent, html=text_box(ctx.t.body(), MX, 330, W - 2 * MX, 'pearl', align='center'))
    return r
