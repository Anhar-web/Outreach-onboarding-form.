"""b3p5 Broken biscuit. Night ground. Composition: SPLIT PAIR, BISCUIT / PHONE.

A big round biscuit (sandLight paper, scalloped rim, goldDeep docking holes)
and, in the metaphor slides, a phone with the very same crack line.
s1: an open packet spilling biscuits, the top one cracked; a small pile of
    halves by mum's pearl-sleeved hand.
s2: one biscuit snapping in a small hand (halves apart, crumbs).
s3: a phone with a hairline crack (pearl line on a dark screen), held.
s4: biscuit and phone side by side, the same crack (soft CTA above).
s5: two small hands breaking it into two halves.
s6: the two halves held out on mum's open palm.
s7: two identical biscuits, different crack placements.
End: gold, a mini biscuit bottom-right.
"""
import math
import random
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'night'
T = 'd'


# ---------------------------------------------------------------- geometry
def zig(p0, p1, n=7, amp=18, seed=3):
    """A crack: a zigzag from p0 to p1 (ends on the line)."""
    rng = random.Random(seed)
    (x0, y0), (x1, y1) = p0, p1
    L = math.hypot(x1 - x0, y1 - y0) or 1
    nx, ny = -(y1 - y0) / L, (x1 - x0) / L
    pts = [p0]
    for k in range(1, n):
        t = k / n
        a = amp * (1 if k % 2 else -1) * rng.uniform(.6, 1.1)
        pts.append((x0 + (x1 - x0) * t + nx * a, y0 + (y1 - y0) * t + ny * a))
    pts.append(p1)
    return pts


def rim_pts(cx, cy, r, a0, a1, n=None, sc=24, amp=.025):
    """Scalloped biscuit rim from angle a0 to a1 (degrees)."""
    n = n or max(24, int(abs(a1 - a0) / 1.5))
    out = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        rr = r * (1 + amp * math.cos(sc * a))
        out.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return out


def P(pts):
    return ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)


def holes(cx, cy, r, keep=lambda x, y: True):
    out = ''
    for k in range(-3, 4):
        for j in range(-3, 4):
            x, y = cx + k * r * .24, cy + j * r * .24
            if math.hypot(x - cx, y - cy) < r * .72 and keep(x, y):
                out += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r * .035:.1f}" fill="{C["goldDeep"]}"/>'
    return out


def biscuit(cx, cy, r, crack=None, split=0, seed=3, rot=0, name='biscuit', crack_len=1.0, tilt=8):
    """crack = angle (deg) of the crack line through the centre (None = whole).
    split = gap between the two halves (px) when broken. crack_len < 1: a
    partial hairline crack from the rim inward."""
    ring = (f'<circle cx="{cx}" cy="{cy}" r="{r * .86:.1f}" fill="none" stroke="{C["gold"]}" stroke-opacity=".55" stroke-width="{r * .03:.1f}"/>')
    if crack is None:
        body = f'<polygon points="{P(rim_pts(cx, cy, r, 0, 360))}" fill="{C["sandLight"]}"/>'
        return avoid(paper(f'<g transform="rotate({rot} {cx} {cy})">' + body + ring + holes(cx, cy, r) + '</g>', T, 2), name)
    a = math.radians(crack)
    e1 = (cx + r * math.cos(a), cy + r * math.sin(a))
    e2 = (cx - r * math.cos(a), cy - r * math.sin(a))
    z = zig(e1, e2, 7, r * .09, seed)
    if not split:
        body = f'<polygon points="{P(rim_pts(cx, cy, r, 0, 360))}" fill="{C["sandLight"]}"/>'
        m = max(2, int(len(z) * crack_len + .5))
        line = (f'<polyline points="{P(z[:m])}" fill="none" stroke="{C["night"]}" stroke-width="{max(5, r * .035):.1f}" '
                f'stroke-linejoin="round" stroke-linecap="round"/>')
        return avoid(paper(f'<g transform="rotate({rot} {cx} {cy})">' + body + ring + holes(cx, cy, r) + line + '</g>', T, 2), name)
    nx, ny = -math.sin(a), math.cos(a)
    half_a = rim_pts(cx, cy, r, crack, crack + 180, amp=0) + z[::-1]
    half_b = rim_pts(cx, cy, r, crack + 180, crack + 360, amp=0) + z
    out = ''
    arcs = {1: rim_pts(cx, cy, r * .86, crack + 14, crack + 166, amp=0), -1: rim_pts(cx, cy, r * .86, crack + 194, crack + 346, amp=0)}
    for sgn, pts in ((1, half_a), (-1, half_b)):
        dx, dy = nx * split / 2 * sgn, ny * split / 2 * sgn
        rg = f'<polyline points="{P(arcs[sgn])}" fill="none" stroke="{C["gold"]}" stroke-opacity=".55" stroke-width="{r * .03:.1f}"/>'
        keep = (lambda sg: (lambda x, y: sg * ((x - cx) * nx + (y - cy) * ny) > r * .1))(sgn)
        hl = holes(cx, cy, r, keep)
        out += paper(f'<g transform="translate({dx:.1f} {dy:.1f}) rotate({sgn * tilt} {cx} {cy}) rotate({rot} {cx} {cy})">'
                     f'<polygon points="{P(pts)}" fill="{C["sandLight"]}"/>'
                     f'{rg}{hl}</g>', T, 2)
    return avoid(out, name)


def crumbs(pts, s=1.0):
    return ''.join(paper(f'<polygon points="{x - 9 * s:.0f},{y:.0f} {x + 2 * s:.0f},{y - 10 * s:.0f} {x + 10 * s:.0f},{y + 4 * s:.0f} {x - 2 * s:.0f},{y + 9 * s:.0f}" fill="{C["sandLight"]}"/>', T, 1)
                   for (x, y) in pts)


def stack(cx, base, n=5, w=230, h=34):
    """Biscuits seen edge-on, stacked (thin rounded bars)."""
    out = ''
    for k in range(n):
        y = base - (k + 1) * (h + 2)
        out += f'<rect x="{cx - w / 2 + (k % 2) * 6}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" fill="{C["sandLight"]}"/>'
        out += ''.join(f'<rect x="{cx - w / 2 + 14 + q * 18}" y="{y + h / 2 - 2}" width="8" height="4" rx="2" fill="{C["goldDeep"]}" fill-opacity=".5"/>' for q in range(int((w - 28) / 18)))
    return out


def packet(cx, cy, rot=-14):
    """An open biscuit packet: teal wrapper with a gold band, torn-open top, a
    stack of biscuits sliding out of it."""
    w, h = 300, 520
    x, y = cx - w / 2, cy - h / 2
    inner = (f'<rect x="{x}" y="{y + h * .42}" width="{w}" height="{h * .18}" fill="{C["gold"]}"/>'
             f'<rect x="{x}" y="{y + h * .64}" width="{w}" height="14" fill="{C["pearl"]}" fill-opacity=".7"/>')
    body = torn_rect(x, y, w, h, C['teal'], T, sides='t', seed=41, layer=2, amp=(8, 16), inner=inner)
    spill = paper(stack(cx, y + 40, 4, w - 50, 32), T, 1)
    return f'<g transform="rotate({rot} {cx} {cy})">{spill}{body}</g>'


def phone(cx, cy, s=1.0, rot=0, crack=True, crack_angle=-58, seed=3, name='phone'):
    """A phone, portrait: pearl body, ink screen, a hairline pearl crack running
    across the screen, the same zigzag as the biscuit."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    body = (f'<rect x="-150" y="-280" width="300" height="560" rx="46" fill="{C["pearl"]}"/>'
            f'<rect x="-130" y="-256" width="260" height="512" rx="30" fill="{C["ink"]}"/>'
            f'<rect x="-34" y="-244" width="68" height="16" rx="8" fill="{C["night"]}"/>')
    out = paper(body, T, 2, T=tr)
    if crack:
        a = math.radians(crack_angle)
        r = 200
        z = zig((r * math.cos(a), r * math.sin(a)), (-r * math.cos(a), -r * math.sin(a)), 7, 18, seed)
        out += paper(f'<polyline points="{P(z)}" fill="none" stroke="{C["pearl"]}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>'
                     f'<polyline points="{P(z[2:4])}" fill="none" stroke="{C["tealMist"]}" stroke-width="3" transform="translate(14 -8)"/>', T, 3, 't', T=tr)
    return avoid(out, name)


def small_hand(x, y, s=1.0, rot=0, grab=True, sleeve='teal', cuff='tealDeep', name='small'):
    """A small hand reaching UP, fingertips at (x, y), sleeve running down out of frame."""
    tr = f'translate({x} {y}) rotate({rot}) scale({s})'
    if grab:
        hand = (f'<rect x="-56" y="0" width="112" height="110" rx="40" fill="{C["sandLight"]}"/>'
                + ''.join(f'<rect x="{-54 + n * 28}" y="-6" width="26" height="40" rx="13" fill="{C["sandLight"]}"/>' for n in range(4))
                + f'<path d="M -50 40 H 50" stroke="{C["goldDeep"]}" stroke-opacity=".35" stroke-width="4"/>')
    else:
        lens = (80, 96, 90, 74)
        hand = ''.join(f'<rect x="{-50 + n * 26}" y="{100 - lens[n]}" width="22" height="{lens[n] + 20}" rx="11" fill="{C["sandLight"]}" '
                       f'transform="rotate({(n - 1.5) * 6} {-39 + n * 26} 110)"/>' for n in range(4))
        hand += f'<rect x="-58" y="96" width="112" height="110" rx="40" fill="{C["sandLight"]}"/>'
    hand += f'<rect x="-96" y="40" width="34" height="80" rx="17" fill="{C["sandLight"]}" transform="rotate(-30 -79 80)"/>'
    sl = (f'<path d="M -66 100 L 64 100 L 74 900 L -76 900 Z" fill="{C[sleeve]}"/>'
          f'<rect x="-70" y="96" width="140" height="34" rx="10" fill="{C[cuff]}"/>')
    return avoid(paper(sl, T, 1, T=tr) + paper(hand, T, 3, T=tr), name)


def pinch(x, y, side='left', s=1.0, sleeve='teal', cuff='tealDeep', name='pinch'):
    """A hand from the side edge pinching a biscuit edge at (x, y): thumb on top,
    fingers below (drawn above the biscuit)."""
    sx = 1 if side == 'left' else -1
    tr = f'translate({x} {y}) scale({sx * s} {s})'
    sl = (f'<path d="M -900 20 L -110 4 L -96 124 L -900 150 Z" fill="{C[sleeve]}"/>'
          f'<rect x="-128" y="0" width="34" height="128" rx="10" fill="{C[cuff]}" transform="rotate(-6 -110 64)"/>')
    hand = (f'<path d="M -110 10 Q -40 -20 10 10 L 30 90 Q 0 130 -100 120 Z" fill="{C["sandLight"]}"/>'
            f'<rect x="-30" y="-36" width="90" height="34" rx="17" fill="{C["sandLight"]}" transform="rotate(-10 0 -20)"/>'
            + ''.join(f'<rect x="{-20 + n * 4}" y="{40 + n * 24}" width="{72 - n * 8}" height="24" rx="12" fill="{C["sandLight"]}"/>' for n in range(3)))
    return avoid(paper(sl, T, 2, T=tr) + paper(hand, T, 3, T=tr), name)


def open_palm(cx, cy, s=1.0, rot=-8, name='palm'):
    """Mum's open hand, palm up, from the lower right (pearl sleeve): a flat
    cupped palm with the fingers to the left."""
    tr = f'translate({cx} {cy}) rotate({rot}) scale({s})'
    sl = (f'<path d="M 200 -40 L 900 -60 L 900 160 L 200 110 Z" fill="{C["pearl"]}"/>'
          f'<rect x="180" y="-44" width="40" height="160" rx="12" fill="{C["tealMist"]}"/>')
    hand = (f'<path d="M 200 -30 Q 60 -50 -120 -20 Q -200 0 -190 40 Q -150 90 0 100 L 200 100 Z" fill="{C["sandLight"]}"/>'
            + ''.join(f'<path d="M {-190 + n * 4} {-6 + n * 22} H {-60}" stroke="{C["goldDeep"]}" stroke-opacity=".25" stroke-width="4"/>' for n in range(3))
            + f'<rect x="40" y="-90" width="110" height="40" rx="20" fill="{C["sandLight"]}" transform="rotate(-24 95 -70)"/>')
    return avoid(paper(sl, T, 1, T=tr) + paper(hand, T, 2, T=tr), name)


# ---------------------------------------------------------------- slides
def slide(ctx):
    s = ctx.s
    if ctx.last:
        mini = biscuit(860, 1120, 120, crack=-30, split=26, name='mini')
        return cta_end(ctx, mini_art=mini, tag_y=1040, tag_x=MX + 20)
    art, html = '', ''
    if s == 1:
        art = (avoid(packet(240, 980, -16), 'packet')
               + biscuit(560, 930, 150, crack=-60, crack_len=1.0, seed=5, name='top')
               + biscuit(470, 1150, 120, seed=6, name='b2')
               + open_palm(900, 1210, .9, rot=-6)
               + biscuit(860, 1100, 80, crack=20, split=22, seed=7, name='h1')
               + biscuit(780, 1040, 66, crack=-40, split=18, seed=8, name='h2'))
        html = hook_box(ctx, G, y=MT - 20, size=88, w=888,
                        breaks=('كله ', 'بسكوتة ', 'مكسوره، '), keep=('تدوري له على بسكوتة', 'وأكلتي أنتي المكسور؟'))
    elif s == 2:
        art = (small_hand(540, 1060, 1.15, rot=0, grab=True)
               + biscuit(540, 920, 200, crack=-75, split=34, seed=11, tilt=10)
               + crumbs([(330, 1010), (370, 1090), (760, 1000), (720, 1120), (800, 1180)], 1.2))
        html = body_box(ctx, G)
    elif s == 3:
        art = phone(560, 1010, .95, rot=8, crack_angle=-58, seed=21) + open_palm(780, 1250, .8, rot=-14)
        html = body_box(ctx, G)
    elif s == 4:
        art = (biscuit(300, 1060, 170, crack=-58, crack_len=1.0, seed=21, name='b')
               + phone(760, 1050, .62, rot=0, crack_angle=-58, seed=21))
        html = body_box(ctx, G) + soft_cta(ctx, y=640)
    elif s == 5:
        from kit import keep_in
        keep_in(ctx.t.segs, 'وحده لك ووحده لي".')
        art = (biscuit(540, 1000, 200, crack=-90, split=40, seed=31, tilt=6)
               + pinch(300, 960, 'left', 1.0) + pinch(780, 960, 'right', 1.0, sleeve='teal'))
        html = body_box(ctx, G)
    elif s == 6:
        art = (open_palm(640, 1140, 1.25, rot=-6, name='palm')
               + biscuit(500, 1010, 120, crack=-90, split=40, seed=41, tilt=12))
        html = body_box(ctx, G)
    elif s == 7:
        art = (biscuit(300, 1040, 175, crack=-90, seed=51, name='left')
               + biscuit(780, 1040, 175, crack=-30, crack_len=.35, seed=52, name='right'))
        html = body_box(ctx, G)
    return {'ground': G, 'art': art, 'html': html}
