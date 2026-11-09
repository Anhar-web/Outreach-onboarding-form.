"""p9 Shower: knocking and crying. Deep ground. Composition: DOOR AS THE DIVIDER.

A tall pearl-framed bathroom door stands on the floor line and splits the frame:
INSIDE (the bathroom: tiles, shower head, water, steam) on the left, OUTSIDE
(the hallway: a small fist knocking, tears, the gold light under the door) on the
right, where the RTL eye lands first. The camera slides with the story:
s1 both sides, s2 the door pushed left (outside fills the frame), s3 pushed right
(inside fills the frame, mum's hand on the handle), s4 centred, the voice bubble
stopped by the door. s5 a snack bowl outside, the fist gone. s6 gold sound arcs
pass straight through the door. s7 a small chair with mum's folded towel by the
door. CTA end: gold, the door + chair small in the bottom-left.
No faces anywhere: the child is a fist, a sleeve and small hands.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, torn_poly, glow, avoid, arc_pts, keep_in
from common import hook_box, body_box, soft_cta, cta_end

G = 'deep'
T = 'd'
FL = 1215          # floor line
DH = 640           # door leaf height (local units)
DW = 300           # door leaf width


# ------------------------------------------------------------------ the room
def floor(dx, tone=T):
    """Night floor band; the bathroom half (left of the door) gets tealDeep tiles."""
    band = torn_poly([(-20, FL), (W + 20, FL), (W + 20, H + 20), (-20, H + 20)], C['night'], tone, torn=[0], seed=91, amp=(3, 7))
    tiles = ''.join(f'<rect x="{x}" y="{FL + 14}" width="66" height="40" rx="3" fill="{C["tealDeep"]}" fill-opacity=".45"/>'
                    for x in range(-40, int(dx) - 150, 76))
    return band + (paper(tiles, tone, 1, 't') if tiles else '')


def wall_tiles(dx, top, tone=T):
    """Bathroom wall tiles, left of the door, from `top` down to the floor."""
    out = ''
    for row, y in enumerate(range(int(top), FL - 40, 92)):
        off = 0 if row % 2 == 0 else 46
        for x in range(-60 + off, int(dx) - 175, 92):
            out += f'<rect x="{x}" y="{y}" width="84" height="84" rx="6" fill="{C["tealDeep"]}" fill-opacity=".28"/>'
    return paper(out, tone, 1, 't') if out else ''


def door(dx, s=1.0, light=True, tone=T):
    """Closed door, front view, standing on the floor at x = dx. s scales it."""
    tr = f'translate({dx} {FL}) scale({s})'
    hw = DW / 2
    out = ''
    if light:
        # warm light leaking from the bathroom under the door, onto the hallway floor
        out += glow(f'<ellipse cx="{dx + 40 * s}" cy="{FL + 14}" rx="{230 * s}" ry="22" fill="{C["gold"]}" fill-opacity=".55"/>', 's')
    leaf = paper(f'<rect x="{-hw}" y="{-DH}" width="{DW}" height="{DH}" fill="{C["sandLight"]}"/>'
                 f'<rect x="{-hw + 40}" y="{-DH + 48}" width="{DW - 80}" height="230" rx="8" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="7"/>'
                 f'<rect x="{-hw + 40}" y="{-DH + 320}" width="{DW - 80}" height="260" rx="8" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="7"/>'
                 f'<rect x="{-hw}" y="-10" width="{DW}" height="10" fill="{C["gold"]}" fill-opacity=".9"/>', tone, 1, T=tr)
    handle = paper(f'<rect x="{hw - 62}" y="{-DH / 2 - 52}" width="26" height="104" rx="12" fill="{C["goldDeep"]}"/>'
                   f'<rect x="{hw - 92}" y="{-DH / 2 - 14}" width="72" height="26" rx="12" fill="{C["gold"]}"/>', tone, 3, T=tr)
    frame = paper(f'<path d="M {-hw - 14} 0 V {-DH - 14} H {hw + 14} V 0" fill="none" stroke="{C["pearl"]}" stroke-width="28" stroke-linejoin="round"/>',
                  tone, 2, T=tr)
    return out + avoid(leaf + frame + handle, 'door')


def shower_head(x, y, s=1.0, tone=T):
    """Wall pipe from the left edge, bending down into a big gold rose."""
    tr = f'translate({x} {y}) scale({s})'
    pipe = paper(f'<path d="M -400 -60 H -40 Q 0 -60 0 -20 V 20" fill="none" stroke="{C["pearl"]}" stroke-width="30" stroke-linecap="round"/>', tone, 1, T=tr)
    head = paper(f'<path d="M -95 20 H 95 Q 108 20 98 52 L 80 92 H -80 L -98 52 Q -108 20 -95 20 Z" fill="{C["gold"]}"/>'
                 + ''.join(f'<circle cx="{-52 + k * 26}" cy="78" r="6" fill="{C["goldDeep"]}"/>' for k in range(5)), tone, 2, T=tr)
    return pipe + head


def water(x, y, length=380, n=5, spread=26, seed=1, tone=T):
    out = ''
    for k in range(n):
        sx = x + (k - (n - 1) / 2) * spread
        L = length * (0.82 + 0.3 * ((k * 37) % 7) / 7)
        ex = sx + (k - (n - 1) / 2) * 22
        out += torn_strip([(sx, y), (ex, y + L)], 18, C['teal' if k % 2 == 0 else 'pearl'], tone, seed=seed + k, layer=2)
    return out


def steam(x, y, n=3, h=260, seed=7, tone=T):
    """Pearl wavy strips rising (soft: semi-transparent)."""
    out = ''
    for k in range(n):
        x0 = x + k * 70
        pts = [(x0 + 22 * math.sin(i / 3.0 + k), y - i * h / 14) for i in range(15)]
        out += torn_strip(pts, 20, C['pearl'], tone, seed=seed + k, layer=1, core=False)
    return f'<g opacity=".45">{out}</g>'


def drops(pts, r=14, col='teal', tone=T):
    out = ''
    for (x, y) in pts:
        out += f'<path d="M {x} {y - r * 1.6} Q {x + r} {y - r * .2} {x} {y + r} Q {x - r} {y - r * .2} {x} {y - r * 1.6} Z" fill="{C[col]}"/>'
    return paper(out, tone, 1)


def fist(x, y, s=1.0, tone=T):
    """A small fist knocking leftwards (on the door), teal sleeve from the right."""
    tr = f'translate({x} {y}) scale({s})'
    sleeve = paper(f'<path d="M 40 -38 L 330 -60 L 330 60 L 40 38 Z" fill="{C["teal"]}"/>'
                   f'<rect x="34" y="-42" width="30" height="84" rx="10" fill="{C["tealDeep"]}"/>', tone, 2, T=tr)
    hand = paper(f'<rect x="-46" y="-44" width="96" height="88" rx="34" fill="{C["sandLight"]}"/>'
                 + ''.join(f'<path d="M -46 {-22 + k * 22} H -20" stroke="{C["goldDeep"]}" stroke-opacity=".45" stroke-width="4" stroke-linecap="round"/>' for k in range(3))
                 + f'<path d="M -10 -44 Q 20 -66 44 -40 Q 30 -24 -6 -30 Z" fill="{C["sandLight"]}" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="3"/>',
                 tone, 3, T=tr)
    return avoid(sleeve + hand, 'fist')


def knocks(x, y, s=1.0, tone=T):
    """Gold impact marks fanning out from the knock point (x, y)."""
    out = ''
    for k, a in enumerate((-62, -34, 34, 62)):
        r = math.radians(a)
        p0 = (x + 70 * s * math.cos(r), y + 70 * s * math.sin(r))
        p1 = (x + 150 * s * math.cos(r), y + 150 * s * math.sin(r))
        out += torn_strip([p0, p1], 16 * s, C['gold'], tone, seed=70 + k, layer=2)
    return out


def bubble(x, y, w=230, h=140, tail='right', seed=5, words=2, tone=T):
    """Wordless pearl speech bubble: short ink strips stand for the words."""
    if tail == 'right':
        tl = f'<polygon points="{x + w - 70},{y + h - 4} {x + w + 10},{y + h + 50} {x + w - 20},{y + h - 4}" fill="{C["pearl"]}"/>'
    else:
        tl = f'<polygon points="{x + 70},{y + h - 4} {x - 10},{y + h + 50} {x + 20},{y + h - 4}" fill="{C["pearl"]}"/>'
    bars = ''
    bw = (w - 70 - (words - 1) * 22) / words
    for k in range(words):
        bars += f'<rect x="{x + 35 + k * (bw + 22)}" y="{y + h / 2 - 9}" width="{bw}" height="18" rx="9" fill="{C["deep"]}" fill-opacity=".75"/>'
    return avoid(torn_rect(x, y, w, h, C['pearl'], tone, 'tblr', seed=seed, layer=3, inner=tl + bars), 'bubble')


def mum_hand(x, y, s=1.0, length=380, tone=T):
    """Mum's wet pearl sleeve + hand reaching right, to the inside of the handle."""
    tr = f'translate({x} {y}) scale({s})'
    L = -40 - length
    out = paper(f'<path d="M {L} -56 L -40 -48 L -40 48 L {L} 56 Z" fill="{C["pearl"]}"/>'
                f'<path d="M -40 -40 Q 40 -54 74 -24 Q 88 4 64 30 Q 30 50 -40 40 Z" fill="{C["sandLight"]}"/>', tone, 2, T=tr)
    out += paper(''.join(f'<ellipse cx="{L + 50 + k * 72}" cy="{-12 + (k % 2) * 28}" rx="20" ry="11" fill="{C["teal"]}" fill-opacity=".6"/>' for k in range(int(length / 80))),
                 tone, 3, 't', T=tr)
    return avoid(out, 'sleeve')


def bowl(x, y, s=1.0, hand=True, tone=T):
    """A gold snack bowl heaped with sandLight/pearl pieces; a small hand dips in."""
    tr = f'translate({x} {y}) scale({s})'
    heap = ''.join(f'<ellipse cx="{dx}" cy="{dy}" rx="{rx}" ry="{ry}" transform="rotate({rt} {dx} {dy})" fill="{C[c]}"/>'
                   for dx, dy, rx, ry, rt, c in ((-90, -18, 34, 20, -20, 'sandLight'), (-40, -40, 30, 22, 15, 'pearl'),
                                                  (14, -46, 34, 20, -8, 'sandLight'), (66, -30, 30, 20, 25, 'pearl'),
                                                  (110, -12, 28, 18, -12, 'sandLight'), (-20, -10, 30, 18, 30, 'pearl'),
                                                  (40, -4, 32, 18, -25, 'pearl')))
    out = paper(heap, tone, 1, T=tr)
    out += paper(f'<path d="M -170 0 H 170 Q 160 120 0 130 Q -160 120 -170 0 Z" fill="{C["gold"]}"/>'
                 f'<path d="M -170 0 H 170" stroke="{C["goldDeep"]}" stroke-width="10"/>'
                 f'<path d="M -120 46 H 120" stroke="{C["goldDeep"]}" stroke-opacity=".3" stroke-width="8"/>', tone, 2, T=tr)
    if hand:
        out += paper(f'<g transform="rotate(-28 120 -70)"><path d="M 60 -110 L 260 -120 L 260 -40 L 60 -50 Z" fill="{C["teal"]}"/>'
                     f'<rect x="10" y="-112" width="70" height="64" rx="26" fill="{C["sandLight"]}"/></g>', tone, 3, T=tr)
    return avoid(out, 'bowl')


def sound_arcs(x, y, n=4, r0=90, gap=70, a=48, tone=T):
    """Gold arcs of the voice, centred at (x, y), opening to the right."""
    out = ''
    for k in range(n):
        out += torn_strip(arc_pts(x, y, r0 + k * gap, -a, a, 18), 24, C['teal' if k % 2 == 0 else 'gold'], tone, seed=110 + k, layer=3)
    return avoid(out, 'voice')


def chair(x, s=1.0, towel=True, hands=True, tone=T):
    """Small gold chair, side view facing the door (left), on the floor; mum's folded
    towel on the seat, held by two small hands."""
    tr = f'translate({x} {FL}) scale({s})'
    legs = paper(f'<rect x="-80" y="-150" width="18" height="150" rx="5" fill="{C["goldDeep"]}"/>'
                 f'<rect x="62" y="-150" width="18" height="150" rx="5" fill="{C["goldDeep"]}"/>', tone, 1, T=tr)
    seat = paper(f'<rect x="-92" y="-176" width="184" height="32" rx="8" fill="{C["gold"]}"/>'
                 f'<rect x="58" y="-400" width="40" height="234" rx="14" fill="{C["gold"]}"/>'
                 f'<path d="M 64 -330 H 92" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="6"/>', tone, 2, T=tr)
    out = legs + seat
    if towel:
        out += paper(f'<rect x="-80" y="-222" width="150" height="46" rx="10" fill="{C["pearl"]}"/>'
                     f'<rect x="-80" y="-206" width="150" height="12" fill="{C["teal"]}"/>', tone, 3, T=tr)
        out += paper(f'<rect x="-70" y="-262" width="134" height="44" rx="10" fill="{C["pearl"]}"/>'
                     f'<rect x="-70" y="-248" width="134" height="12" fill="{C["teal"]}"/>', tone, 3, T=tr)
        if hands:
            out += paper(f'<rect x="-108" y="-252" width="44" height="58" rx="20" fill="{C["sandLight"]}"/>'
                         f'<rect x="56" y="-252" width="44" height="58" rx="20" fill="{C["sandLight"]}"/>', tone, 3, T=tr)
    return avoid(out, 'chair')


# ------------------------------------------------------------------ slides
def scene(dx, s=1.0, tiles_top=None, light=True):
    top = tiles_top if tiles_top is not None else FL - DH * s
    return floor(dx) + wall_tiles(dx, top) + door(dx, s, light)


def slide(ctx):
    s = ctx.s
    if ctx.last:
        keep_in(ctx.t.segs, 'فكري في الأشياء', 'اللي صرتي تسويها', 'قبل ما يصحى', 'أو بعد ما ينام.')
        mini = (f'<g transform="translate(60 {1350 - 500}) scale(.42)">'
                + f'<g transform="translate(0 {-FL + 1100})">{door(330, 1.0, light=False, tone="l")}{chair(640, 1.0, hands=False, tone="l")}</g></g>')
        return cta_end(ctx, mini_art=mini, tag_y=1030, tag_x=W - MX - 520)

    art, html = '', ''
    if s == 1:
        dx, ds = 540, .66
        art = (scene(dx, ds)
               + shower_head(130, 880, .72) + water(130, 945, length=230, n=4, spread=22, seed=3)
               + steam(190, 1180, n=3, h=200)
               + knocks(dx + DW * ds / 2 + 6, 1020, .8)
               + fist(dx + DW * ds / 2 + 46, 1020, .8)
               + drops([(860, 1110), (910, 1170), (830, 1180)], r=12))
        html = hook_box(ctx, G, y=MT - 20, size=92, w=900,
                        keep=('يدق باب الحمام', 'ويبكي  أول ما تسكريه،', 'فصرتي تتروشي', 'بعد ما ينام', 'أو قبل ما يصحى؟'))
    elif s == 2:
        # OUTSIDE: the door pushed left; the hallway fills the frame
        dx = 250
        art = (scene(dx, 1.0)
               + knocks(dx + DW / 2 + 6, 860, 1.15)
               + fist(dx + DW / 2 + 62, 860, 1.25)
               + drops([(640, 1010), (700, 1090), (600, 1120), (760, 1160), (560, 1040)], r=17))
        keep_in(ctx.t.segs, 'يوقف شويه،', 'يسمع،', 'وما يسمع شي،', 'فيرجع يدق.')
        html = body_box(ctx, G, y=MT + 115)
    elif s == 3:
        # INSIDE: the door pushed right; the bathroom fills the frame
        dx = 840
        art = (scene(dx, 1.0, tiles_top=560)
               + shower_head(200, 640, 1.0) + water(200, 735, length=400, n=5, spread=24, seed=11)
               + steam(60, 1190, n=2, h=260, seed=21)
               + bubble(390, 610, 230, 130, tail='left', seed=8)
               + mum_hand(dx - DW / 2 - 50, FL - DH / 2 + 4, 1.0, length=280))
        keep_in(ctx.t.segs, 'الموية شغالة', 'وأنتي تقولي "جيت، جيت"', 'وتستعجلي.', 'تطلعي له', 'وما خلصتي.')
        html = body_box(ctx, G, y=MT + 115)
    elif s == 4:
        # HIS SIDE: both sides; her voice bubble stops at the door, he knocks again
        dx, ds = 540, .78
        art = (scene(dx, ds)
               + shower_head(110, 800, .7) + water(110, 865, length=260, n=4, spread=22, seed=41)
               + steam(160, 1170, n=2, h=200, seed=51)
               + bubble(250, 900, 190, 112, tail='left', seed=12)
               + knocks(dx + DW * ds / 2 + 6, 1000, .85)
               + fist(dx + DW * ds / 2 + 50, 1000, .85)
               + drops([(860, 1110), (910, 1170)], r=13))
        keep_in(ctx.t.segs, 'الباب اتسكر،', 'وصوتك اختفى.', 'فيدق ويبكي.', 'وهذي ثلاث خطوات', 'تخلي الباب المسكر', 'أخف عليه.')
        html = body_box(ctx, G, y=MT + 115)
    elif s == 5:
        # step 1: the snack bowl outside, a calm small hand in it; the door small and low
        dx, ds = 330, .48
        art = (scene(dx, ds) + steam(70, 1190, n=2, h=150, seed=61)
               + bowl(720, 1130, .92))
        keep_in(ctx.t.segs, 'لا تدخلي الحمام', 'وطفلك فاضي يدور عليك.', 'ادخلي أول ما يبدأ شي يحبه،', 'ياكل سناكه', 'أو يلعب بألعابه.')
        html = body_box(ctx, G, y=MT + 115) + soft_cta(ctx, y=600, w=888)
    elif s == 6:
        # step 2: her voice passes through the closed door as gold arcs
        dx = 540
        art = (scene(dx, .92)
               + shower_head(130, 690, .78) + water(130, 760, length=300, n=4, spread=22, seed=71)
               + bubble(110, 1000, 200, 120, tail='right', seed=14)
               + sound_arcs(300, 960, n=5, r0=110, gap=92, a=30))
        keep_in(ctx.t.segs, 'خلي صوتك يوصله', 'طول الوقت.', 'كذا يسمع إنك موجودة،', 'حتى والباب مسكّر.')
        html = body_box(ctx, G, y=MT + 115)
    elif s == 7:
        # step 3: a small chair by the door, mum's folded towel held in small hands
        dx, ds = 420, .8
        art = (scene(dx, ds) + steam(80, 1190, n=2, h=180, seed=81)
               + chair(dx + DW * ds / 2 + 190, 1.1, hands=False))
        keep_in(ctx.t.segs, 'اعطيه شغلة برا.', 'يمسك منشفتك جنب الباب،', 'ويعطيك إياها', 'أول ما تطلعي.', 'كذا يستنى', 'عشان يعطيك شي،', 'مو بس يستناك.')
        html = body_box(ctx, G, y=MT + 115)
    return {'ground': G, 'art': art, 'html': html}
