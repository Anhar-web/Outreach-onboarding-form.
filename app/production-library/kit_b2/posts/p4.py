"""p4 "Just today" became every night. Night ground. Composition: MOONS MULTIPLY.

The room is two beds on one floor line: the big bed (right) and his small bed
(left). The sky above them counts the nights:
s1 two shapes under one duvet in the big bed, the small bed empty beside it.
s2 one pearl crescent (that one night).  s3 the crescent becomes a row of moons
(every night).  s4 a single gold sun (the day: a new start).  s5 the sun over
the small bed, now with a small lump in it (the nap).  s6 a pearl speech bubble
holding two short strips (the same two words).  s7 a gold dashed path from the
big bed back to the small bed.  CTA end: gold, a row of small moons over the
small bed with its lump, bottom-left.
No faces: people are lumps under a duvet.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, torn_poly, glow, avoid, keep_in, arc_pts
from common import hook_box, body_box, soft_cta, cta_end

G = 'night'
T = 'd'
FL = 1195


def floor(tone=T):
    return torn_poly([(-20, FL), (W + 20, FL), (W + 20, H + 20), (-20, H + 20)], C['deep'], tone, torn=[0], seed=41, amp=(3, 7))


def bed(x, w, lumps=(), head=330, foot=210, s=1.0, fl=FL, tone=T, name='bed'):
    """Side view, headboard on the right. x = footboard left edge (canvas px), w = length.
    lumps = list of (pos 0..1 along the duvet, height, width) shapes under ONE duvet."""
    tr = f'translate({x} {fl}) scale({s})'
    frame = paper(f'<rect x="{w - 50}" y="{-head}" width="50" height="{head}" rx="14" fill="{C["deep"]}"/>'
                  f'<rect x="0" y="{-foot}" width="42" height="{foot}" rx="12" fill="{C["deep"]}"/>'
                  f'<rect x="24" y="-104" width="{w - 50}" height="46" rx="6" fill="{C["deep"]}"/>', tone, 1, T=tr)
    mattress = paper(f'<rect x="34" y="-180" width="{w - 76}" height="78" rx="16" fill="{C["sandLight"]}"/>', tone, 2, T=tr)
    pillow = paper(f'<path d="M {w - 200} -176 Q {w - 196} -236 {w - 128} -234 Q {w - 64} -232 {w - 60} -176 Z" fill="{C["tealMist"]}"/>', tone, 2, T=tr)
    # one pearl duvet over every lump; no heads anywhere
    bx0, bx1, by = 24, w - 150, -176
    d = f'M {bx0} {by + 70} L {bx0} {by}'
    cur = bx0
    for (pos, hgt, wid) in sorted(lumps):
        cx = bx0 + (bx1 - bx0) * pos
        a, b = cx - wid / 2, cx + wid / 2
        d += f' L {a} {by - 6} Q {a + wid * .12} {by - hgt} {cx} {by - hgt} Q {b - wid * .12} {by - hgt} {b} {by - 6}'
    d += f' L {bx1} {by - 18} L {bx1} {by + 70} Z'
    stripe = f'<path d="M {bx0} {by + 40} L {bx1} {by + 40}" stroke="{C["gold"]}" stroke-width="10" stroke-opacity=".7"/>'
    duvet = paper(f'<path d="{d}" fill="{C["pearl"]}"/>{stripe}', tone, 3, T=tr)
    return avoid(frame + mattress + pillow + duvet, name)


def big_bed(lumps=((.3, 120, 230), (.8, 80, 130)), s=1.0, x=470, fl=FL, tone=T):
    return bed(x, 540, lumps, 330, 210, s, fl, tone, 'bigbed')


def small_bed(lump=False, s=1.0, x=90, fl=FL, tone=T):
    return bed(x, 310, [(.45, 70, 130)] if lump else [], 230, 150, s, fl, tone, 'smallbed')


def moon(cx, cy, r, glow_on=True, col=None, seed=1, tone=T):
    col = col or C['pearl']
    g = glow(f'<circle cx="{cx}" cy="{cy}" r="{r * 1.25}" fill="{C["pearl"]}" fill-opacity=".16"/>', 'l') if glow_on else ''
    return g + paper(f'<path d="M {cx} {cy - r} A {r} {r} 0 1 0 {cx} {cy + r} A {r * .6} {r} 0 1 1 {cx} {cy - r} Z" fill="{col}"/>', tone, 2)


def moons(n, x0, x1, y, r, glow_on=False, wave=0, tone=T):
    out = ''
    for k in range(n):
        cx = x1 - (x1 - x0) * k / max(1, n - 1)      # first moon on the right (RTL)
        out += moon(cx, y + wave * math.sin(k * 1.3), r, glow_on, seed=k, tone=tone)
    return avoid(out, 'moons')


def sun(cx, cy, r, rays=10, tone=T):
    out = glow(f'<circle cx="{cx}" cy="{cy}" r="{r * 1.5}" fill="{C["gold"]}" fill-opacity=".28"/>', 'l')
    for k in range(rays):
        a = math.radians(k * 360 / rays + 8)
        p0 = (cx + (r + 26) * math.cos(a), cy + (r + 26) * math.sin(a))
        p1 = (cx + (r + 26 + r * .55) * math.cos(a), cy + (r + 26 + r * .55) * math.sin(a))
        out += torn_strip([p0, p1], max(12, r * .16), C['gold'], tone, seed=60 + k, layer=2)
    out += torn_circle(cx, cy, r, C['gold'], tone, seed=77, layer=2)
    return avoid(out, 'sun')


def bubble(x, y, w, h, seed=5, tone=T):
    """Pearl speech bubble with two short deep strips: the same two words."""
    tl = f'<polygon points="{x + w - 110},{y + h - 4} {x + w - 30},{y + h + 70} {x + w - 50},{y + h - 4}" fill="{C["pearl"]}"/>'
    b1 = f'<rect x="{x + w * .14}" y="{y + h / 2 - 16}" width="{w * .4}" height="32" rx="16" fill="{C["deep"]}"/>'
    b2 = f'<rect x="{x + w * .6}" y="{y + h / 2 - 16}" width="{w * .26}" height="32" rx="16" fill="{C["deep"]}"/>'
    return avoid(torn_rect(x, y, w, h, C['pearl'], tone, 'tblr', seed=seed, layer=3, inner=tl + b1 + b2), 'bubble')


def path_back(x0, y0, x1, y1, lift=220, tone=T):
    """Gold dashed path arching from (x0,y0) on the big bed back down into the small bed."""
    pts = []
    for i in range(41):
        t = i / 40
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t - lift * 4 * t * (1 - t)
        pts.append((x, y))
    out = ''
    for k in range(0, 38, 3):
        out += torn_strip(pts[k:k + 2], 16, C['gold'], tone, seed=90 + k, layer=2)
    # arrow head at the end, pointing down-left into the small bed
    (ax, ay), (bx, by) = pts[-3], pts[-1]
    a = math.atan2(by - ay, bx - ax)
    tip = (bx + 22 * math.cos(a), by + 22 * math.sin(a))
    l = (bx + 30 * math.cos(a + 2.5), by + 30 * math.sin(a + 2.5))
    r = (bx + 30 * math.cos(a - 2.5), by + 30 * math.sin(a - 2.5))
    out += paper(f'<polygon points="{tip[0]:.1f},{tip[1]:.1f} {l[0]:.1f},{l[1]:.1f} {r[0]:.1f},{r[1]:.1f}" fill="{C["gold"]}"/>', tone, 2)
    return avoid(out, 'path')


def slide(ctx):
    s = ctx.s
    if ctx.last:
        keep_in(ctx.t.segs, '"اليوم بس" صارت كل ليلة', 'بالتدريج، مو فجأة.', 'والرجوع منها يبدأ', 'بخطوة وحدة تناسبه هو.',
                'ابدئي بالتقييم المجاني،', 'واعرفي فين تركزي أول شي.')
        mini = (moons(3, 110, 330, 990, 26, tone='l')
                + small_bed(True, .78, x=96, fl=1235, tone='l'))
        return cta_end(ctx, mini_art=mini, tag_y=1080, tag_x=W - MX - 500)

    art, html = '', ''
    if s == 1:
        art = floor() + small_bed(False) + big_bed()
        html = hook_box(ctx, G, y=MT - 10, size=96, w=900,
                        keep=('قلتي له اليوم بس', 'تنام جنبي،', 'ودحين ما يرضى', 'ينام لحاله؟'))
    elif s == 2:
        # that one night: one moon
        art = floor() + moon(250, 760, 115) + small_bed(False, .82, x=110) + big_bed(s=.82, x=500)
        keep_in(ctx.t.segs, 'ذيك الليلة كنتي تعبانة،', 'وهو يبكي ويمد يدينه لك.', 'قلتي في نفسك', '"اليوم بس.', 'بكرة يرجع لسريره".')
        html = body_box(ctx, G, y=MT + 20)
    elif s == 3:
        # every night: the crescent becomes a row of moons
        art = (floor() + moons(7, 140, 940, 790, 44, wave=14)
               + small_bed(False, .7, x=110) + big_bed(s=.7, x=540))
        keep_in(ctx.t.segs, 'دحين كل ليلة تقولي', '"متى آخر مرة نام لحاله؟"', 'تنسدحي جنبه،', 'وتسمعي أصوات البيت برا،', 'وأنتي مو قادرة تقومي.')
        html = body_box(ctx, G, y=MT + 20)
    elif s == 4:
        # the day: a single gold sun, the beds made and quiet
        art = floor() + sun(540, 860, 140) + small_bed(False, .62, x=120) + big_bed((), s=.62, x=610)
        keep_in(ctx.t.segs, 'ذيك الليلة', 'ما سويتي شي غلط.', 'وهذي ثلاث خطوات تبدئي فيها', 'عشان يرجع ينام في سريره.')
        html = body_box(ctx, G, y=MT + 20)
    elif s == 5:
        # step 1: the nap, the sun over the small bed, now with him in it
        art = floor() + sun(310, 850, 90, rays=9) + small_bed(True, 1.05, x=150) + big_bed((), s=.6, x=700)
        keep_in(ctx.t.segs, 'ابدئي بنومة الظهر في سريره،', 'مو بنوم الليل.', 'النهار أهون عليكي وعليه.')
        html = body_box(ctx, G, y=MT + 115) + soft_cta(ctx, y=530)
    elif s == 6:
        # step 2: the same two words, every time
        art = floor() + moon(170, 720, 60) + bubble(430, 700, 440, 190, seed=7) + small_bed(True, .95, x=110) + big_bed(((.3, 120, 230),), s=.62, x=700)
        keep_in(ctx.t.segs, 'في الليل،', 'نفس الكلمتين كل مرة،', 'زي "يلا سريرك".', 'قوليها بهدوء،', 'وما تزيدي عليها.')
        html = body_box(ctx, G, y=MT + 115)
    elif s == 7:
        # step 3: the way back, from the big bed to the small one
        art = (floor() + moon(170, 790, 50)
               + small_bed(True, .9, x=90) + big_bed(((.3, 120, 230),), s=.9, x=540)
               + path_back(820, 960, 250, 1000, lift=200))
        keep_in(ctx.t.segs, 'إذا قام وجاك،', 'رجعيه لسريره،', 'ولا ترجعي تنسدحي جنبه.', 'كذا يكون الجواب واحد', 'كل ليلة،', 'ويعرف ايش يتوقع.')
        html = body_box(ctx, G, y=MT + 115)
    return {'ground': G, 'art': art, 'html': html}
