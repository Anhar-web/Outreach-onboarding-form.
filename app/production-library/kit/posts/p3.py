"""p3 bedtime. Night ground, dark. Panorama: one long strip (the bedroom, bed on
the right, door on the far left), seen through a camera that pans along it.

The room is drawn ONCE in world coordinates (WORLD_W wide); every slide shows a
window onto that same strip (camera x, scale), so the floor line, the bed, the
window and the door never move: only Mum's gold chair does (bed -> mid-room ->
door across s4-s8). No figures: the child is a pearl blanket lump, no head.
s1: hook centred in the upper third over the bed, lamp glow and moon.
s2: closer on the bed: two lumps under one blanket (she is still lying there).
s3: the whole strip pulled back: four torn gold floor marks from bed to door.
s4: the chair beside the bed.  s5: her hand on his back, then only her voice.
s6: the strip again, the chair now mid-room, ghosts of where it was and will be.
s7 (red flag) is split at its "\\n": s7a the gold route back to bed;
     s7b the bed with only his lump, the chair waiting at the door.
s8: attention end: the door ajar with a pearl light wedge; quiet line centred.
"""
from kit import (C, MX, MT, W, H, paper, torn_poly, torn_strip, torn_rect, glow,
                 text_box, step_tab, avoid, keep_in, P)

TONE = 'd'
FLOOR = 1130            # floor line (world y)
WORLD_W = 3260

BED = (2000, 2800)      # footboard x .. headboard x
DOOR = (820, 1100)      # door opening x0 .. x1
WIN = (2170, 2490, 640, 880)
STAND = 2850            # nightstand left x
CHAIR_BED, CHAIR_MID, CHAIR_DOOR = 1780, 1480, 1150


# ---------------------------------------------------------------- world pieces
def floor():
    pts = [(-400, FLOOR), (WORLD_W + 400, FLOOR), (WORLD_W + 400, 2200), (-400, 2200)]
    band = torn_poly(pts, C['deep'], TONE, torn=[0], seed=301, amp=(4, 9))
    # skirting: a thin pearl-ish line just above the floor, the strip's through-line
    skirt = paper(f'<rect x="-400" y="{FLOOR - 26}" width="{WORLD_W + 800}" height="10" fill="{C["pearl"]}" fill-opacity=".14"/>', TONE, 1, 't')
    return skirt + band


def window_moon():
    x0, x1, y0, y1 = WIN
    frame = paper(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="{C["night"]}" stroke="{C["deep"]}" stroke-width="22"/>'
                  f'<line x1="{(x0 + x1) / 2}" y1="{y0}" x2="{(x0 + x1) / 2}" y2="{y1}" stroke="{C["deep"]}" stroke-width="12"/>'
                  f'<line x1="{x0}" y1="{(y0 + y1) / 2}" x2="{x1}" y2="{(y0 + y1) / 2}" stroke="{C["deep"]}" stroke-width="12"/>', TONE, 1)
    cx, cy, r = x0 + 90, y0 + 85, 48
    moon = paper(f'<path d="M {cx} {cy - r} A {r} {r} 0 1 0 {cx} {cy + r} A {r * .6} {r} 0 1 1 {cx} {cy - r} Z" fill="{C["pearl"]}"/>', TONE, 2)
    sill = paper(f'<rect x="{x0 - 26}" y="{y1 + 6}" width="{x1 - x0 + 52}" height="20" rx="4" fill="{C["deep"]}"/>', TONE, 2)
    return avoid(frame + moon + sill, 'window')


def lamp(on=True):
    x = STAND
    stand = paper(f'<rect x="{x}" y="{FLOOR - 190}" width="150" height="190" rx="6" fill="{C["deep"]}"/>'
                  f'<rect x="{x + 18}" y="{FLOOR - 160}" width="114" height="60" rx="4" fill="{C["night"]}"/>'
                  f'<circle cx="{x + 75}" cy="{FLOOR - 130}" r="7" fill="{C["gold"]}"/>', TONE, 1)
    lx, ly = x + 75, FLOOR - 190
    g = ''
    if on:
        g = (glow(f'<circle cx="{lx}" cy="{ly - 110}" r="150" fill="{C["gold"]}" fill-opacity=".38"/>', 'l')
             + glow(f'<circle cx="{lx}" cy="{ly - 110}" r="80" fill="{C["gold"]}" fill-opacity=".55"/>', 's'))
    body = paper(f'<rect x="{lx - 8}" y="{ly - 110}" width="16" height="110" fill="{C["goldDeep"]}"/>'
                 f'<rect x="{lx - 40}" y="{ly - 10}" width="80" height="14" rx="6" fill="{C["goldDeep"]}"/>'
                 f'<path d="M {lx - 70} {ly - 100} L {lx + 70} {ly - 100} L {lx + 44} {ly - 190} L {lx - 44} {ly - 190} Z" fill="{C["gold"]}"/>', TONE, 2)
    return avoid(g + stand + body, 'lamp')


def bed(lumps=1):
    x0, x1 = BED
    frame = paper(
        f'<rect x="{x1 - 60}" y="{FLOOR - 370}" width="60" height="370" rx="14" fill="{C["deep"]}"/>'      # headboard (right)
        f'<rect x="{x0}" y="{FLOOR - 240}" width="48" height="240" rx="12" fill="{C["deep"]}"/>'          # footboard (left)
        f'<rect x="{x0 + 30}" y="{FLOOR - 120}" width="{x1 - x0 - 60}" height="56" rx="6" fill="{C["deep"]}"/>', TONE, 1)
    mattress = paper(f'<rect x="{x0 + 40}" y="{FLOOR - 200}" width="{x1 - x0 - 90}" height="84" rx="16" fill="{C["sandLight"]}"/>', TONE, 2)
    pillow = paper(f'<path d="M {x1 - 210} {FLOOR - 196} Q {x1 - 205} {FLOOR - 262} {x1 - 130} {FLOOR - 258} '
                   f'Q {x1 - 66} {FLOOR - 254} {x1 - 66} {FLOOR - 196} Z" fill="{C["tealMist"]}"/>', TONE, 2)
    # pearl blanket with lump(s); no head anywhere
    bx0, bx1, by = x0 + 30, x1 - 150, FLOOR - 196
    if lumps == 2:
        d = (f'M {bx0} {by + 70} L {bx0} {by} Q {bx0 + 60} {by - 6} {bx0 + 110} {by - 70} '
             f'Q {bx0 + 250} {by - 190} {bx0 + 400} {by - 90} Q {bx0 + 450} {by - 50} {bx0 + 480} {by - 64} '
             f'Q {bx0 + 580} {by - 150} {bx0 + 680} {by - 60} L {bx1} {by - 40} L {bx1} {by + 70} Z')
    else:
        d = (f'M {bx0} {by + 70} L {bx0} {by} Q {bx0 + 200} {by - 4} {bx0 + 420} {by - 20} '
             f'Q {bx0 + 520} {by - 150} {bx0 + 640} {by - 70} L {bx1} {by - 40} L {bx1} {by + 70} Z')
    stripe = f'<path d="M {bx0} {by + 40} L {bx1} {by + 40}" stroke="{C["gold"]}" stroke-width="10" stroke-opacity=".7"/>'
    blanket = paper(f'<path d="{d}" fill="{C["pearl"]}"/>{stripe}', TONE, 3)
    slipper = paper(f'<path d="M {x0 - 150} {FLOOR - 2} L {x0 - 150} {FLOOR - 34} Q {x0 - 140} {FLOOR - 50} {x0 - 96} {FLOOR - 44} '
                    f'Q {x0 - 46} {FLOOR - 38} {x0 - 40} {FLOOR - 10} L {x0 - 40} {FLOOR - 2} Z" fill="{C["gold"]}"/>'
                    f'<rect x="{x0 - 156}" y="{FLOOR - 8}" width="122" height="10" rx="4" fill="{C["goldDeep"]}"/>', TONE, 2)
    return avoid(frame + mattress + pillow + blanket, 'bed') + slipper


def door(ajar=False):
    x0, x1 = DOOR
    top = FLOOR - 560
    o = ''
    if ajar:
        # light from the hall: in the gap and a pearl wedge across the floor
        o += paper(f'<rect x="{x0 + 14}" y="{top + 14}" width="{x1 - x0 - 28}" height="{560 - 14}" fill="{C["pearl"]}" fill-opacity=".92"/>', TONE, 1)
        o += paper(f'<polygon points="{x0 + 14},{FLOOR} {x1 - 14},{FLOOR} {x1 + 520},{FLOOR + 210} {x0 + 120},{FLOOR + 210}" '
                   f'fill="{C["pearl"]}" fill-opacity=".30"/>', TONE, 1, 't')
        o += paper(f'<polygon points="{x0 + 14},{top + 14} {x0 + 120},{top + 60} {x0 + 120},{FLOOR + 26} {x0 + 14},{FLOOR}" fill="{C["deep"]}"/>'
                   f'<circle cx="{x0 + 98}" cy="{FLOOR - 270}" r="9" fill="{C["gold"]}"/>', TONE, 2)
    else:
        o += paper(f'<rect x="{x0 + 14}" y="{top + 14}" width="{x1 - x0 - 28}" height="{560 - 14}" fill="{C["deep"]}"/>'
                   f'<rect x="{x0 + 50}" y="{top + 60}" width="{x1 - x0 - 100}" height="190" rx="6" fill="none" stroke="{C["night"]}" stroke-width="8"/>'
                   f'<rect x="{x0 + 50}" y="{top + 300}" width="{x1 - x0 - 100}" height="190" rx="6" fill="none" stroke="{C["night"]}" stroke-width="8"/>'
                   f'<circle cx="{x1 - 50}" cy="{FLOOR - 270}" r="10" fill="{C["gold"]}"/>', TONE, 1)
        o += paper(f'<rect x="{x0 + 20}" y="{FLOOR - 6}" width="{x1 - x0 - 40}" height="6" fill="{C["pearl"]}" fill-opacity=".7"/>', TONE, 1, 't')
    frame = paper(f'<path d="M {x0} {FLOOR} V {top} H {x1} V {FLOOR}" fill="none" stroke="{C["pearl"]}" stroke-width="22" stroke-linejoin="round"/>', TONE, 2)
    return avoid(o + frame, 'door')


def chair(x, ghost=False):
    """Mum's chair, side view, facing right (towards the bed). x = left edge."""
    if ghost:
        d = (f'M {x + 13} {FLOOR} V {FLOOR - 370} M {x} {FLOOR - 180} H {x + 170} M {x + 160} {FLOOR - 180} V {FLOOR}')
        return paper(f'<path d="{d}" fill="none" stroke="{C["gold"]}" stroke-opacity=".55" stroke-width="10" '
                     f'stroke-dasharray="4 18" stroke-linecap="round"/>', TONE, 1, 't')
    legs = paper(f'<rect x="{x + 4}" y="{FLOOR - 170}" width="18" height="170" rx="4" fill="{C["goldDeep"]}"/>'
                 f'<rect x="{x + 148}" y="{FLOOR - 170}" width="18" height="170" rx="4" fill="{C["goldDeep"]}"/>', TONE, 1)
    seat = paper(f'<rect x="{x}" y="{FLOOR - 196}" width="172" height="34" rx="8" fill="{C["gold"]}"/>'
                 f'<rect x="{x}" y="{FLOOR - 380}" width="30" height="200" rx="10" fill="{C["gold"]}"/>'
                 f'<rect x="{x + 22}" y="{FLOOR - 226}" width="140" height="30" rx="12" fill="{C["sandLight"]}"/>', TONE, 2)
    return avoid(legs + seat, 'chair')


def marks(xs, y=FLOOR + 50, w=120):
    """Torn gold floor marks (the steps), one per x."""
    return avoid(''.join(torn_rect(x - w / 2, y - 16, w, 34, C['gold'], TONE, 'tblr', seed=60 + k, layer=2, rot=-4 + 3 * k, amp=(3, 6))
                         for k, x in enumerate(xs)), 'marks')


def hand(x, y, k=1.0):
    """An open hand, palm down, fingers towards the pillow: palm + four fingers + thumb,
    sandLight cut paper resting on the blanket. No arm, no figure."""
    fingers = ''.join(f'<rect x="40" y="{-34 + n * 17}" width="{62 - abs(n - 1.5) * 10:.0f}" height="15" rx="7.5" '
                      f'transform="rotate({(n - 1.5) * -6:.0f} 40 {-27 + n * 17})"/>' for n in range(4))
    thumb = '<rect x="-4" y="-50" width="50" height="17" rx="8.5" transform="rotate(-16 10 -42)"/>'
    palm = '<rect x="-34" y="-40" width="86" height="76" rx="30"/>'
    return avoid(paper(f'<g transform="translate({x} {y}) rotate(-10) scale({k})" fill="{C["sandLight"]}">{palm}{fingers}{thumb}</g>',
                       TONE, 3), 'hand')


def voice(x, y, n=3):
    out = ''
    for k in range(n):
        r = 46 + k * 34
        out += f'<path d="M {x + r * .5:.1f} {y - r * .87:.1f} A {r} {r} 0 0 1 {x + r * .5:.1f} {y + r * .87:.1f}" fill="none" stroke="{C["gold"]}" stroke-width="12" stroke-linecap="round"/>'
    return avoid(paper(out, TONE, 2, 't'), 'voice')


def route_back(x0, x1):
    """Gold dashed route on the floor: up from the floor, round, and back into bed."""
    d = f'M {x0} {FLOOR + 40} C {x0 + 160} {FLOOR + 110}, {x1 - 260} {FLOOR + 110}, {x1 - 120} {FLOOR + 30}'
    arrow = f'<polygon points="{x1 - 140},{FLOOR + 6} {x1 - 76},{FLOOR + 30} {x1 - 128},{FLOOR + 74}" fill="{C["gold"]}"/>'
    return avoid(paper(f'<path d="{d}" fill="none" stroke="{C["gold"]}" stroke-width="16" stroke-linecap="round" stroke-dasharray="2 34"/>{arrow}',
                       TONE, 2, 't'), 'route')


def world(chair_x=None, lumps=1, ajar=False, extra='', ghosts=(), lamp_on=True):
    o = floor() + window_moon() + door(ajar) + lamp(lamp_on) + bed(lumps)
    for gx in ghosts:
        o += chair(gx, ghost=True)
    if chair_x is not None:
        o += chair(chair_x)
    return o + extra


def cam(svg, x, k=1.0, y=0):
    """Show world x..x+1080/k at scale k. y shifts the strip vertically (screen px)."""
    return f'<g transform="translate({-x * k:.1f} {y + (1 - k) * FLOOR:.1f}) scale({k})">{svg}</g>'


# ---------------------------------------------------------------- slides
BREAKS = {
    1: ['تنسدحي جمبه', 'إلين ما ينام،', 'وتصحي بعد ساعتين', 'وأنتي اللي نمتي؟'],
    2: ['كل ليلة نفس القصة.', 'هو ما ينام إلا وأنتي جمبه،', 'وأنتي تبغيه ينام لحاله.'],
    3: ['هذي أربع خطوات', 'تبعدي فيها عنه شوي شوي،', 'بدون ما تختفي', 'من الغرفة فجأة.'],
    4: ['بدل ما تنسدحي جمبه،', 'اجلسي جمب سريره.', 'نفس القرب،', 'بس أنتي جالسة،', 'وما راح تنامي قبله.'],
    5: ['يدك على ظهره', 'في البداية.', 'وبعد كم ليلة،', 'صوتك بس،', 'بدون يدك.'],
    6: ['كل كم ليلة،', 'مكانك يبعد شوي.', 'من جمب السرير،', 'لنص الغرفة،', 'لعند الباب.'],
    7: ['إذا قام من سريره،', 'رجعيه بهدوء', 'وبنفس الكلمتين كل مرة،', 'زي "يلا نوم".',
        'بدون نقاش،', 'وبدون ما تنسدحي جمبه من جديد.'],
    8: ['تاخذ وقت،', 'بس كل كم ليلة', 'أنتي أبعد بخطوة.', 'والهدف ليلة تطلعي فيها', 'من الغرفة وهو لسه صاحي.'],
}


def body(ctx, y=None, align='right'):
    html = ''
    if ctx.t.label():
        html += step_tab(ctx.t.label())
    top = y or (MT + 115 if ctx.t.label() else MT + 40)
    return html + text_box(ctx.t.body(), MX, top, W - 2 * MX, 'pearl', align=align)


def slide(ctx):
    s, part = ctx.s, ctx.part
    if s in BREAKS:
        keep_in(ctx.t.segs, *[p for p in BREAKS[s] if any(p in g.text for g in ctx.t.segs)])
    r = {'ground': 'night'}

    if s == 1:
        art = cam(world(lumps=2), 1880)
        html = text_box(ctx.t.body(), MX, MT - 10, W - 2 * MX, 'pearl', align='center', size={'hook': 92})
        r.update(art=art, html=html)
    elif s == 2:
        art = cam(world(lumps=2), 2030, 1.25, y=20)
        r.update(art=art, html=body(ctx))
    elif s == 3:
        # the whole strip, pulled back: bed on the right, door on the left, four steps between
        # marks drawn at screen scale under their world positions, so they read at this distance
        k, cx, yo = .49, 790, -190
        xs = [(wx - cx) * k for wx in (1880, 1640, 1400, 1160)]
        art = cam(world(), cx, k, y=yo) + marks(xs, FLOOR + yo + 70, w=78)
        r.update(art=art, html=body(ctx))
    elif s == 4:
        art = cam(world(chair_x=CHAIR_BED), 1660)
        r.update(art=art, html=body(ctx))
    elif s == 5:
        extra = hand(2500, FLOOR - 296, 1.0) + voice(1970, FLOOR - 330)
        art = cam(world(chair_x=CHAIR_BED, extra=extra), 1720, 1.1, y=10)
        r.update(art=art, html=body(ctx))
    elif s == 6:
        art = cam(world(chair_x=CHAIR_MID, ghosts=(CHAIR_BED, CHAIR_DOOR)), 790, .49, y=-150)
        r.update(art=art, html=body(ctx))
    elif s == 7 and part == 1:
        art = cam(world(chair_x=CHAIR_DOOR, extra=route_back(1540, BED[0] + 240)), 1420)
        r.update(art=art, html=body(ctx))
    elif s == 7:
        ctx.t.body()[0].role = 'lead'
        # pulled back: his lump alone in bed on the right, her chair already by the door
        art = cam(world(chair_x=CHAIR_DOOR), 960, .58)
        r.update(art=art, html=body(ctx))
    else:
        for g in ctx.t.body():
            g.role = 'quiet'
        art = cam(world(chair_x=CHAIR_DOOR, ajar=True), 600, y=60)
        r.update(art=art, html=text_box(ctx.t.body(), MX, MT, W - 2 * MX, 'pearl', align='center'))
    return r
