"""b3p2 Weekly جمعة, three mistakes. Night ground. Composition: CUT-AWAY HOUSE.

A dollhouse section: a flat-roofed house with a gold Najdi parapet, the big
majlis on the right (floor cushions, seated guests from behind, a dallah and
cups) and a small side room on the left (one gold lamp, mum and a small child
from behind). s1 the full section. s2 the house again, three gold marks above
the roof (the three things). s3 a close-up at the majlis edge: mum's sleeve
holding a cup toward the guests, a small hand pulling the sleeve. s4 two torn
panels: the small figure flat on the floor (right) vs the pair stepping out of
a door (left). s5 a thin torn timeline (time runs right to left) with one gold
mark the minute before the cry burst. s6 three torn notes pinned on a board,
one picked out in gold. CTA end: gold, a mini dallah bottom-left.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_rect, torn_strip, torn_poly, torn_circle, avoid, glow
from common import hook_box, body_box, soft_cta, cta_end

G = 'night'
T = 'd'


def dallah(x, y, s=1.0, rot=0):
    """Arabic coffee pot, gold paper. Local frame: base centre at (0,0), ~300 tall,
    spout to the right, handle to the left."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    g = (f'<path d="M 46 -118 Q 120 -150 150 -258 L 170 -268 Q 150 -150 64 -92 Z" fill="{C["gold"]}"/>'
         f'<path d="M -46 -214 Q -130 -196 -84 -64" fill="none" stroke="{C["goldDeep"]}" stroke-width="16" stroke-linecap="round"/>'
         f'<rect x="-64" y="-22" width="128" height="22" rx="8" fill="{C["goldDeep"]}"/>'
         f'<path d="M -70 -22 Q -104 -110 -50 -152 L 50 -152 Q 104 -110 70 -22 Z" fill="{C["gold"]}"/>'
         f'<rect x="-52" y="-170" width="104" height="18" rx="5" fill="{C["sandLight"]}"/>'
         f'<path d="M -44 -170 L -30 -230 L 30 -230 L 44 -170 Z" fill="{C["gold"]}"/>'
         f'<path d="M -42 -228 Q 0 -286 42 -228 Z" fill="{C["goldDeep"]}"/>'
         f'<path d="M -8 -270 L 0 -312 L 8 -270 Z" fill="{C["gold"]}"/>'
         f'<path d="M -40 -80 Q 0 -70 40 -80" fill="none" stroke="{C["goldDeep"]}" stroke-width="5" stroke-opacity=".6"/>')
    return paper(f'<g transform="{tr}">{g}</g>', T, 2)


def cup(x, y, s=1.0):
    return paper(f'<g transform="translate({x} {y}) scale({s})"><path d="M -24 -40 L 24 -40 L 16 0 L -16 0 Z" fill="{C["pearl"]}"/>'
                 f'<rect x="-24" y="-40" width="48" height="8" fill="{C["gold"]}"/></g>', T, 2)


def seated(cx, base, s=1.0, kind='woman'):
    """An adult sitting on the floor, seen from behind (no face). woman: ink
    abaya + shayla; man: pearl ghutra over a pearl thobe."""
    body = C['ink'] if kind == 'woman' else C['pearl']
    head = C['ink'] if kind == 'woman' else C['pearl']
    g = (f'<g transform="translate({cx} {base}) scale({s})">'
         f'<path d="M -95 0 Q -100 -150 -50 -190 L 50 -190 Q 100 -150 95 0 Z" fill="{body}"/>'
         f'<circle cx="0" cy="-232" r="52" fill="{head}"/>')
    if kind == 'woman':
        g += f'<path d="M -52 -232 Q -60 -170 -70 -150 L 70 -150 Q 60 -170 52 -232 Z" fill="{C["ink"]}"/>'
    else:
        g += (f'<path d="M -54 -236 L -76 -130 L 76 -130 L 54 -236 Z" fill="{C["pearl"]}"/>'
              f'<path d="M -50 -258 Q 0 -280 50 -258" fill="none" stroke="{C["ink"]}" stroke-width="12"/>'
              f'<path d="M -50 -242 Q 0 -262 50 -242" fill="none" stroke="{C["ink"]}" stroke-width="12"/>')
    if kind == 'woman':
        g += f'<rect x="-95" y="-10" width="190" height="10" fill="{C["gold"]}"/>'
    g += '</g>'
    return paper(g, T, 2)


def child_back(cx, base, s=1.0, body='teal'):
    """A small child from behind: rounded body, round back of the head (goldDeep hair), ears."""
    g = (f'<g transform="translate({cx} {base}) scale({s})">'
         f'<path d="M -60 0 Q -64 -100 -30 -120 L 30 -120 Q 64 -100 60 0 Z" fill="{C[body]}"/>'
         f'<ellipse cx="-42" cy="-158" rx="8" ry="12" fill="{C["sandLight"]}"/><ellipse cx="42" cy="-158" rx="8" ry="12" fill="{C["sandLight"]}"/>'
         f'<circle cx="0" cy="-160" r="42" fill="{C["goldDeep"]}"/></g>')
    return paper(g, T, 2)


def mum_standing(cx, base, s=1.0):
    """Mum standing, seen from behind: shayla + abaya to the floor, gold hem."""
    g = (f'<g transform="translate({cx} {base}) scale({s})">'
         f'<path d="M -80 0 L -60 -300 Q -56 -360 0 -364 Q 56 -360 60 -300 L 80 0 Z" fill="{C["ink"]}"/>'
         f'<circle cx="0" cy="-400" r="48" fill="{C["ink"]}"/>'
         f'<rect x="-80" y="-14" width="160" height="14" fill="{C["gold"]}"/></g>')
    return paper(g, T, 2)


def lamp(x, base, s=1.0):
    g = (f'<g transform="translate({x} {base}) scale({s})">'
         f'<ellipse cx="0" cy="-6" rx="40" ry="10" fill="{C["goldDeep"]}"/>'
         f'<rect x="-5" y="-260" width="10" height="256" fill="{C["goldDeep"]}"/>'
         f'<path d="M -50 -250 L 50 -250 L 32 -330 L -32 -330 Z" fill="{C["gold"]}"/></g>')
    gl = glow(f'<circle cx="{x}" cy="{base - 260 * s}" r="{150 * s}" fill="{C["gold"]}" fill-opacity=".35"/>', 'l')
    return gl + paper(g, T, 2)


def cushions(x0, x1, base, h=90):
    """A row of floor cushions against the back wall: gold seat strip + teal back cushions."""
    out = paper(f'<rect x="{x0}" y="{base - 40}" width="{x1 - x0}" height="40" rx="10" fill="{C["gold"]}"/>', T, 1)
    n = max(2, int((x1 - x0) // 110))
    cw = (x1 - x0) / n
    out += paper(''.join(f'<rect x="{x0 + k * cw + 6:.0f}" y="{base - 40 - h}" width="{cw - 12:.0f}" height="{h}" rx="22" fill="{C["teal"] if k % 2 else C["tealDeep"]}"/>'
                         for k in range(n)), T, 1)
    return out


def house(x0, y0, x1, y1, split, inner_l='', inner_r=''):
    """The cut-away section: roof slab with a gold Najdi (triangle) parapet,
    two rooms (deep) divided by a wall with a doorway, floor slab."""
    wall = C['tealDeep']
    out = paper(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="{C["deep"]}"/>', T, 1)
    out += glow(f'<circle cx="{(x0 + split) / 2}" cy="{y0 + (y1 - y0) * .35}" r="{(split - x0) * .55}" fill="{C["gold"]}" fill-opacity=".18"/>', 'l')
    out += inner_l + inner_r
    tri = ''.join(f'<path d="M {x0 + 10 + k * 56} {y0 - 26} l 28 -40 l 28 40 Z" fill="{C["gold"]}"/>' for k in range(int((x1 - x0 - 20) // 56)))
    out += paper(f'<rect x="{x0 - 20}" y="{y0 - 30}" width="{x1 - x0 + 40}" height="34" fill="{wall}"/>' + tri
                 + f'<rect x="{x0 - 20}" y="{y0}" width="22" height="{y1 - y0}" fill="{wall}"/>'
                   f'<rect x="{x1 - 2}" y="{y0}" width="22" height="{y1 - y0}" fill="{wall}"/>'
                   f'<rect x="{split - 11}" y="{y0}" width="22" height="{(y1 - y0) * .38}" fill="{wall}"/>'
                   f'<rect x="{x0 - 20}" y="{y1}" width="{x1 - x0 + 40}" height="34" fill="{wall}"/>', T, 2)
    return out


def full_house(y0, y1, x0=70, x1=1010, split=380, s=1.0, guests=True):
    base = y1
    inner_r = cushions(split + 30, x1 - 20, base - 4)
    if guests:
        inner_r += seated(split + 140, base, .62 * s, 'woman') + seated(split + 330, base, .62 * s, 'man') + seated(x1 - 110, base, .62 * s, 'woman')
    inner_r += dallah(split + 235, base - 6, .42) + cup(split + 430, base - 6, .8) + cup(split + 470, base - 6, .8)
    inner_l = lamp(x0 + 60, base, .9) + mum_standing(x0 + 190, base, .72) + child_back(split - 70, base, .85)
    return house(x0, y0, x1, y1, split, inner_l, inner_r)


def cry_burst(x, y, r=70, col='pearl'):
    pts = []
    for k in range(16):
        a = math.radians(k * 22.5)
        rr = r if k % 2 == 0 else r * .5
        pts.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    return torn_poly(pts, C[col], T, seed=7, layer=2)


def note(x, y, w, h, rot, seed, icon='', fill='pearl'):
    out = torn_rect(x, y, w, h, C[fill], T, seed=seed, layer=2, rot=rot,
                    inner=f'<g transform="rotate({rot} {x + w / 2} {y + h / 2})">{icon}</g>')
    out += paper(f'<circle cx="{x + w / 2}" cy="{y + 20}" r="13" fill="{C["gold"]}"/>', T, 3)
    return out


def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = dallah(230, 1220, .8, rot=-6) + cup(400, 1218, 1.1) + cup(460, 1218, 1.1)
        return cta_end(ctx, mini_art=mini, tag_y=1050)
    art, html = '', ''
    if s == 1:
        art = avoid(full_house(805, 1225), 'house')
        html = hook_box(ctx, G, y=MT - 10, size=88, keep=('مع طفلك',))
    elif s == 2:
        art = avoid(full_house(720, 1220, guests=True), 'house')
        art += ''.join(torn_circle(380 + k * 160, 590, 34, C['gold'], T, seed=20 + k, layer=2) for k in range(3))
        html = body_box(ctx, G)
    elif s == 3:
        # majlis edge: cushions + dallah on the right; mum's sleeve offering a cup; a small hand pulls the sleeve
        art = cushions(620, 1100, 1250, h=110)
        art += dallah(760, 1250, .55)
        art += paper(f'<g transform="translate(140 1110) rotate(-10)"><rect x="-300" y="-55" width="560" height="110" rx="30" fill="{C["ink"]}"/>'
                     f'<rect x="236" y="-55" width="24" height="110" fill="{C["gold"]}"/>'
                     f'<path d="M 262 -44 Q 330 -56 372 -30 Q 392 -10 380 12 Q 366 30 330 26 L 262 44 Z" fill="{C["sandLight"]}"/></g>', T, 3)
        art += cup(495, 1050, 1.4)
        art += paper(f'<g transform="translate(318 1222) rotate(14)"><rect x="-40" y="0" width="80" height="200" rx="14" fill="{C["teal"]}"/>'
                     f'<rect x="-36" y="-80" width="72" height="86" rx="28" fill="{C["sandLight"]}"/>'
                     + ''.join(f'<rect x="{-30 + k * 16}" y="-118" width="14" height="60" rx="7" fill="{C["sandLight"]}"/>' for k in range(4))
                     + '</g>', T, 3)
        art = avoid(art, 'majlis')
        html = body_box(ctx, G) + soft_cta(ctx, y=760)
    elif s == 4:
        # right panel: the small figure flat on the floor; left panel: mum and child stepping out of a door
        art = torn_rect(560, 790, 440, 450, C['deep'], T, seed=31, layer=1)
        art += paper(f'<rect x="590" y="1150" width="380" height="40" rx="10" fill="{C["tealDeep"]}"/>'
                     f'<rect x="600" y="1160" width="360" height="6" fill="{C["gold"]}"/>', T, 1)
        art += paper(f'<g transform="translate(780 1150)"><path d="M -150 0 Q -150 -60 -80 -64 L 90 -60 Q 130 -56 130 0 Z" fill="{C["teal"]}"/>'
                     f'<circle cx="-170" cy="-40" r="40" fill="{C["goldDeep"]}"/>'
                     f'<rect x="130" y="-40" width="60" height="34" rx="16" fill="{C["sandLight"]}"/></g>', T, 2)
        art += cry_burst(870, 960, 50)
        art += torn_rect(80, 790, 440, 450, C['deep'], T, seed=32, layer=1)
        art += paper(f'<rect x="180" y="840" width="240" height="380" fill="{C["night"]}"/>'
                     f'<rect x="168" y="830" width="264" height="22" fill="{C["tealDeep"]}"/>'
                     f'<rect x="168" y="830" width="20" height="392" fill="{C["tealDeep"]}"/><rect x="412" y="830" width="20" height="392" fill="{C["tealDeep"]}"/>', T, 1)
        art += glow(f'<rect x="200" y="860" width="200" height="360" fill="{C["gold"]}" fill-opacity=".3"/>', 's')
        art += mum_standing(330, 1220, .72) + child_back(240, 1220, .7)
        art = avoid(art, 'panels')
        html = body_box(ctx, G)
    elif s == 5:
        # a thin torn timeline; time runs right to left; gold minute marked just before the cry
        y = 1030
        art = torn_strip([(1010, y), (90, y)], 38, C['pearl'], T, seed=5, layer=1)
        art += ''.join(paper(f'<circle cx="{x}" cy="{y}" r="17" fill="{C["teal"]}"/>', T, 2) for x in range(950, 420, -105))
        art += torn_rect(250, y - 42, 190, 84, C['gold'], T, seed=9, layer=3)
        art += cry_burst(160, y, 95)
        art += paper(f'<path d="M 250 {y - 80} V {y - 140} H 440 V {y - 80}" fill="none" stroke="{C["gold"]}" stroke-width="10" stroke-linejoin="round"/>', T, 2)
        art = avoid(art, 'timeline')
        html = body_box(ctx, G)
    elif s == 6:
        # three torn notes pinned on a board; one picked out in gold (one step)
        art = torn_rect(80, 560, 920, 620, C['tealDeep'], T, seed=40, layer=1)
        ic1 = (f'<g transform="translate(830 860) scale(.36)"><path d="M 46 -118 Q 120 -150 150 -258 L 170 -268 Q 150 -150 64 -92 Z" fill="{C["gold"]}"/>'
               f'<path d="M -70 -22 Q -104 -110 -50 -152 L 50 -152 Q 104 -110 70 -22 Z" fill="{C["gold"]}"/>'
               f'<path d="M -44 -170 L -30 -230 L 30 -230 L 44 -170 Z" fill="{C["gold"]}"/></g>')
        ic2 = (f'<rect x="500" y="700" width="80" height="140" fill="{C["night"]}"/><rect x="510" y="712" width="60" height="128" fill="{C["gold"]}" fill-opacity=".6"/>')
        ic3 = (f'<rect x="200" y="780" width="180" height="10" fill="{C["teal"]}"/><rect x="250" y="772" width="50" height="26" fill="{C["goldDeep"]}"/>')
        art += note(720, 640, 230, 280, 4, 41, ic1)
        art += note(420, 620, 240, 300, -3, 42, ic2, fill='gold')
        art += note(140, 650, 230, 270, 5, 43, ic3)
        art += paper(f'<ellipse cx="540" cy="770" rx="170" ry="200" fill="none" stroke="{C["gold"]}" stroke-width="8"/>', T, 3)
        art = avoid(art, 'board')
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
