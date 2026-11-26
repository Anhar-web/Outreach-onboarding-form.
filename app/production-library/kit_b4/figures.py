"""Batch 4 people, round 2 (Anhar's grid review): visible and varied.

Every figure is a flat paper silhouette with NO face, lit from behind: a warm
gold rim (the same shapes, stroked gold, drawn just behind the figure) plus a
soft glow, so it separates from the night/deep ground at feed size.
Poses: standing mother, mother bending at a door, woman holding a plate/tray,
seated woman, grandmother with a cane, standing man, child, child pulling away.
2-3 figures per post, at the edges and bottom only.
"""
from looks import C, glow
from kit import paper

FIG = C['ink']
RIM = C['gold']


def lit(shapes, tone='d', halo=(0, 0, 0)):
    """shapes: SVG elements filled/stroked with FIG. Adds a gold rim behind them
    (light from behind) and an optional soft glow centred at halo=(x, y, r)."""
    rim = shapes.replace(f'fill="{FIG}"', f'fill="{RIM}" stroke="{RIM}" stroke-width="9" stroke-linejoin="round"')
    rim = rim.replace(f'stroke="{FIG}"', f'stroke="{RIM}"')
    out = glow(*halo, .42) if halo[2] else ''
    out += f'<g opacity=".85" transform="translate(4 -3)">{rim}</g>'
    return out + paper(shapes, tone, 2)


def _head(x, y, r):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{FIG}"/>'


def woman(cx, foot, h, lean=0, arm=None, facing=1):
    """Standing woman in hijab + abaya. lean: forward bend in px at the shoulders
    (bending at a door / toward a child). arm=(x, y): her hand reaches there."""
    f, r = facing, h * .085
    hx, hy = cx + f * (h * .025 + lean), foot - h + r * 1.05 + abs(lean) * .35
    sh = hy + r * 2.0
    scx = cx + f * lean * .55
    body = (f'M {hx - r * .95} {hy + r * .35} Q {hx - r * 1.05} {sh - r * .55} {scx - h * .15} {sh} '
            f'Q {cx - h * .19} {sh + h * .25} {cx - h * .22} {foot} L {cx + h * .21} {foot} '
            f'Q {cx + h * .18} {sh + h * .25} {scx + h * .14} {sh} Q {hx + r * 1.05} {sh - r * .55} {hx + r * .95} {hy + r * .35} Z')
    out = f'<path d="{body}" fill="{FIG}"/>' + _head(hx, hy, r * 1.08)
    if arm:
        ax, ay = arm
        out += (f'<path d="M {scx + f * h * .07} {sh + r * .6} Q {scx + f * h * .14} {(sh + ay) / 2 + h * .05} {ax} {ay}" '
                f'fill="none" stroke="{FIG}" stroke-width="{h * .055:.0f}" stroke-linecap="round"/>')
    return out


def woman_tray(cx, foot, h, facing=1, item='tray'):
    """Woman holding a plate/tray (or a gift bag) out in front of her."""
    f = facing
    r = h * .085
    sh = foot - h + r * 1.05 + r * 2.0
    hand = (cx + f * h * .3, sh + h * .16)
    out = woman(cx, foot, h, facing=f, arm=hand)
    hx, hy = hand
    if item == 'tray':
        obj = (f'<ellipse cx="{hx + f * h * .05}" cy="{hy - h * .01}" rx="{h * .16}" ry="{h * .035}" fill="{C["gold"]}"/>'
               + ''.join(f'<rect x="{hx + f * h * .05 + dx * h - h * .02}" y="{hy - h * .05}" width="{h * .04}" height="{h * .03}" rx="{h * .01}" fill="{c}"/>'
                         for dx, c in [(-.09, C['pearl']), (-.03, C['tealMist']), (.03, C['sand']), (.09, C['pearl'])]))
    else:   # gift bag hanging from the hand
        obj = (f'<rect x="{hx - h * .07}" y="{hy + h * .03}" width="{h * .14}" height="{h * .15}" fill="{C["sand"]}"/>'
               f'<path d="M {hx - h * .035} {hy + h * .03} Q {hx} {hy - h * .04} {hx + h * .035} {hy + h * .03}" fill="none" stroke="{C["goldDeep"]}" stroke-width="{h * .012}"/>'
               f'<rect x="{hx - h * .07}" y="{hy + h * .09}" width="{h * .14}" height="{h * .018}" fill="{C["gold"]}"/>')
    return out, obj


def seated(cx, base, s):
    hr = s * .11
    hy = base - s * .9
    sy = hy + hr * 1.5
    return (f'<circle cx="{cx}" cy="{hy}" r="{hr * 1.12}" fill="{FIG}"/>'
            f'<path d="M {cx - hr * 1.12} {hy + hr * .1} Q {cx - hr * 1.2} {sy} {cx - s * .2} {sy + s * .08} '
            f'Q {cx - s * .34} {sy + s * .2} {cx - s * .38} {base} L {cx + s * .38} {base} '
            f'Q {cx + s * .34} {sy + s * .2} {cx + s * .2} {sy + s * .08} Q {cx + hr * 1.2} {sy} {cx + hr * 1.12} {hy + hr * .1} Z" fill="{FIG}"/>')


def grandma(cx, foot, h, facing=1):
    """Grandmother, stooped, with a cane in her front hand."""
    f = facing
    out = woman(cx, foot, h, lean=h * .09, facing=f)
    cx2 = cx + f * h * .27
    out += (f'<path d="M {cx + f * h * .1} {foot - h * .55} Q {cx + f * h * .2} {foot - h * .5} {cx2} {foot - h * .47}" fill="none" '
            f'stroke="{FIG}" stroke-width="{h * .05:.0f}" stroke-linecap="round"/>'
            f'<path d="M {cx2} {foot - h * .5} L {cx2 + f * h * .02} {foot}" stroke="{FIG}" stroke-width="{h * .03:.0f}" stroke-linecap="round"/>'
            f'<path d="M {cx2 - f * h * .05} {foot - h * .5} Q {cx2} {foot - h * .56} {cx2 + f * h * .03} {foot - h * .5}" fill="none" stroke="{FIG}" stroke-width="{h * .03:.0f}"/>')
    return out


def man(cx, foot, h):
    hr = h * .07
    hy = foot - h + hr * 1.2
    return (f'<path d="M {cx - hr * 1.3} {hy + hr * .2} Q {cx} {hy - hr * 2.1} {cx + hr * 1.3} {hy + hr * .2} '
            f'L {cx + h * .13} {hy + h * .2} L {cx - h * .13} {hy + h * .2} Z" fill="{FIG}"/>'
            f'<path d="M {cx - h * .13} {hy + h * .12} L {cx + h * .13} {hy + h * .12} L {cx + h * .15} {foot} L {cx - h * .15} {foot} Z" fill="{FIG}"/>')


def child(cx, foot, h, arm='up', facing=1):
    f = facing
    hr = h * .17
    hy = foot - h + hr
    by0, by1 = hy + hr * .9, foot - h * .3
    out = (_head(cx, hy, hr) +
           f'<rect x="{cx - h * .17}" y="{by0}" width="{h * .34}" height="{by1 - by0}" rx="{h * .1}" fill="{FIG}"/>'
           f'<rect x="{cx - h * .14}" y="{by1 - 4}" width="{h * .11}" height="{foot - by1 + 4}" rx="{h * .04}" fill="{FIG}"/>'
           f'<rect x="{cx + h * .03}" y="{by1 - 4}" width="{h * .11}" height="{foot - by1 + 4}" rx="{h * .04}" fill="{FIG}"/>')
    if arm == 'up':
        out += (f'<path d="M {cx + f * h * .12} {by0 + h * .08} Q {cx + f * h * .3} {by0} {cx + f * h * .34} {by0 - h * .16}" '
                f'fill="none" stroke="{FIG}" stroke-width="{h * .09:.0f}" stroke-linecap="round"/>')
    return out


def child_pull(cx, foot, h, facing=1):
    """A child leaning away (toward `facing`), one arm stretched back behind him:
    pulling his hand away. Returns (svg, hand_xy) so an adult can hold the hand."""
    f = facing
    hr = h * .17
    lean = h * .16
    hx, hy = cx + f * lean, foot - h + hr
    by0 = hy + hr * .9
    out = (_head(hx, hy, hr) +
           f'<path d="M {hx - h * .16} {by0} L {hx + h * .16} {by0} L {cx + f * h * .05 + h * .15} {foot - h * .28} L {cx + f * h * .05 - h * .15} {foot - h * .28} Z" fill="{FIG}"/>'
           f'<path d="M {cx + f * h * .05} {foot - h * .3} L {cx + f * h * .22} {foot}" stroke="{FIG}" stroke-width="{h * .11:.0f}" stroke-linecap="round"/>'
           f'<path d="M {cx + f * h * .02} {foot - h * .3} L {cx - f * h * .12} {foot}" stroke="{FIG}" stroke-width="{h * .11:.0f}" stroke-linecap="round"/>')
    hand = (hx - f * h * .5, by0 + h * .02)
    out += (f'<path d="M {hx - f * h * .08} {by0 + h * .1} Q {hx - f * h * .3} {by0 + h * .02} {hand[0]} {hand[1]}" '
            f'fill="none" stroke="{FIG}" stroke-width="{h * .085:.0f}" stroke-linecap="round"/>')
    return out, hand
