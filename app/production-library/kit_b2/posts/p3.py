"""p3 8 to 10. Deep ground. Composition: DAY BAND.

A horizontal torn-paper strip of the day runs across the frame, read right to
left (RTL): afternoon sun on the right, evening moon on the left. Each segment is
its own torn sheet: gold (asr), sandLight (maghrib), tealDeep (evening), night (8 to 10).
s1: the whole day, sun to moon; the night stretch on the left is long.
s2: zoom on the night stretch alone, a clock disc at 8 and one at 10, a cup on it.
s3: asr to bedtime: three gold tabs stand on the band before the pyjamas.
s4: the nap segment lifted and lit, the sun low over it.
s5: the last segment before bed: screen + running shoe fade, ball + warm cup take over.
s6: a guest night: a dallah and a door on the band, the same steps squeezed shorter.
s7: three segments as notes, one ticked.
s8: CTA end, gold: the band small in the bottom-right, tag bottom-left.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, arc_pts, avoid
from common import hook_box, body_box, soft_cta, cta_end

G = 'deep'
T = 'd'

DAY = [('gold', 0.26), ('sandLight', 0.16), ('tealDeep', 0.2), ('night', 0.38)]   # right -> left


# ---------------------------------------------------------------- motifs
def band(y, x0=60, x1=1020, h=110, segs=DAY, lift=None, dim=(), seed=0, tone=T, T_=''):
    """The day strip, right (x1) to left (x0). segs = [(colour, share)].
    lift = index of a segment drawn raised (a layer up, nudged up). dim = indices drawn faint."""
    o = ''
    x = x1
    total = sum(f for _, f in segs)
    for k, (col, f) in enumerate(segs):
        w = (x1 - x0) * f / total
        dy = -18 if k == lift else 0
        g = torn_rect(x - w + 3, y + dy, w - 6, h, C[col], tone, sides='tblr', seed=seed + 7 * k + 1,
                      layer=3 if k == lift else 1, rot=(-1.2, .8, -.6, 1.0, -.8)[k % 5], amp=(4, 9), T=T_)
        if k in dim:
            g = f'<g opacity=".38">{g}</g>'
        o += g
        x -= w
    return avoid(o, 'band')


def seg_x(k, x0=60, x1=1020, segs=DAY):
    """Centre x of segment k."""
    total = sum(f for _, f in segs)
    x = x1
    for i, (_, f) in enumerate(segs):
        w = (x1 - x0) * f / total
        if i == k:
            return x - w / 2, w
        x -= w


def sun(cx, cy, r, tone=T, half=False, col='gold'):
    rays = ''.join(f'<rect x="{cx - r * .09:.1f}" y="{cy - r * 1.55:.1f}" width="{r * .18:.1f}" height="{r * .36:.1f}" rx="{r * .09:.1f}" '
                   f'fill="{C[col]}" transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 45))
    o = paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C[col]}"/>{rays}', tone, 2)
    return avoid(o, 'sun')


def moon(cx, cy, r, tone=T):
    d = (f'M {cx:.1f} {cy - r:.1f} A {r} {r} 0 1 0 {cx:.1f} {cy + r:.1f} '
         f'A {r * 1.3:.1f} {r * 1.3:.1f} 0 0 1 {cx:.1f} {cy - r:.1f} Z')
    return avoid(paper(f'<path d="{d}" fill="{C["pearl"]}"/>', tone, 2), 'moon')


def clock(cx, cy, r, hour, tone=T, seed=0):
    """Pearl clock disc, no numbers: ticks at the quarters, hands at hour:00."""
    ticks = ''.join(f'<rect x="{cx - r * .04:.1f}" y="{cy - r * .86:.1f}" width="{r * .08:.1f}" height="{r * .18:.1f}" rx="{r * .03:.1f}" '
                    f'fill="{C["deep"]}" transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 90))
    ha = math.radians(-90 + hour * 30)
    hx, hy = cx + r * .45 * math.cos(ha), cy + r * .45 * math.sin(ha)
    hands = (f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - r * .68:.1f}" stroke="{C["ink"]}" stroke-width="{r * .07:.1f}" stroke-linecap="round"/>'
             f'<line x1="{cx}" y1="{cy}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{C["ink"]}" stroke-width="{r * .11:.1f}" stroke-linecap="round"/>'
             f'<circle cx="{cx}" cy="{cy}" r="{r * .08:.1f}" fill="{C["gold"]}"/>')
    o = paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["pearl"]}"/>'
              f'<circle cx="{cx}" cy="{cy}" r="{r * .93:.1f}" fill="none" stroke="{C["gold"]}" stroke-width="{r * .06:.1f}"/>', tone, 2)
    o += paper(ticks, tone, 2, 't') + paper(hands, tone, 3)
    return avoid(o, 'clock')


def cup(cx, base, s=1.0, steam=True, tone=T):
    """A warm cup: pearl mug, teal drink line, handle on the left, two steam strips."""
    tr = f'translate({cx} {base}) scale({s})'
    g = (f'<path d="M -60 -120 H 60 L 52 -10 Q 50 0 40 0 H -40 Q -50 0 -52 -10 Z" fill="{C["pearl"]}"/>'
         f'<path d="M -58 -88 Q -100 -84 -98 -54 Q -96 -28 -55 -30" fill="none" stroke="{C["pearl"]}" stroke-width="14"/>'
         f'<rect x="-58" y="-120" width="116" height="14" rx="6" fill="{C["goldDeep"]}"/>'
         f'<rect x="-52" y="-70" width="104" height="14" fill="{C["gold"]}"/>')
    o = paper(g, tone, 3, T=tr)
    if steam:
        o += torn_strip([(cx - 18 * s, base - 140 * s), (cx - 30 * s, base - 190 * s), (cx - 14 * s, base - 240 * s)], 12 * s, C['pearl'], tone, seed=5, layer=2)
        o += torn_strip([(cx + 18 * s, base - 140 * s), (cx + 6 * s, base - 185 * s), (cx + 22 * s, base - 225 * s)], 12 * s, C['pearl'], tone, seed=9, layer=2)
    return avoid(o, 'cup')


def pyjamas(cx, cy, s=1.0, tone=T):
    """A pyjama top: tealMist tee with short sleeves, gold stripes, pearl collar."""
    tr = f'translate({cx} {cy}) scale({s})'
    tee = (f'<path d="M -50 -110 L -130 -80 L -170 0 L -110 22 L -95 -20 L -95 120 L 95 120 L 95 -20 L 110 22 L 170 0 L 130 -80 L 50 -110 Q 0 -60 -50 -110 Z" fill="{C["tealMist"]}"/>'
           + ''.join(f'<rect x="-95" y="{-40 + k * 44}" width="190" height="14" fill="{C["gold"]}" fill-opacity=".85"/>' for k in range(4))
           + f'<path d="M -50 -110 Q 0 -60 50 -110" fill="none" stroke="{C["pearl"]}" stroke-width="14"/>')
    return avoid(paper(tee, tone, 3, T=tr), 'pyjamas')


def screen(cx, cy, s=1.0, tone=T):
    tr = f'translate({cx} {cy}) scale({s})'
    g = (f'<rect x="-130" y="-90" width="260" height="180" rx="22" fill="{C["night"]}"/>'
         f'<rect x="-108" y="-70" width="216" height="140" rx="10" fill="{C["teal"]}"/>'
         f'<polygon points="-24,-34 34,0 -24,34" fill="{C["pearl"]}"/>')
    return paper(g, tone, 3, T=tr)


def shoe(cx, base, s=1.0, tone=T):
    """Running shoe, side view, toe to the left: pearl upper, gold sole, teal stripes."""
    tr = f'translate({cx} {base}) scale({s})'
    g = (f'<path d="M 110 0 L 110 -90 Q 110 -110 88 -110 L 50 -110 Q 30 -70 -20 -62 Q -110 -50 -120 -16 L -120 0 Z" fill="{C["pearl"]}"/>'
         f'<rect x="-128" y="-8" width="246" height="26" rx="12" fill="{C["gold"]}"/>'
         f'<path d="M 30 -90 L 0 -20 M 60 -96 L 40 -20" stroke="{C["teal"]}" stroke-width="14" stroke-linecap="round"/>')
    return paper(g, tone, 3, T=tr)


def ball(cx, cy, r, tone=T):
    g = (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["gold"]}"/>'
         f'<path d="M {cx - r} {cy} Q {cx} {cy - r * .5:.1f} {cx + r} {cy}" fill="none" stroke="{C["pearl"]}" stroke-width="{r * .16:.1f}"/>'
         f'<path d="M {cx - r * .25:.1f} {cy - r * .95:.1f} Q {cx + r * .35:.1f} {cy} {cx - r * .25:.1f} {cy + r * .95:.1f}" fill="none" stroke="{C["pearl"]}" stroke-width="{r * .16:.1f}"/>')
    return paper(g, tone, 3)


def dallah(cx, base, s=1.0, tone=T):
    """Arabic coffee pot: gold pear body, long beak spout to the left, finial lid, handle right."""
    tr = f'translate({cx} {base}) scale({s})'
    body = (f'<path d="M -70 0 Q -95 -70 -50 -120 Q -36 -140 -40 -170 L 40 -170 Q 36 -140 50 -120 Q 95 -70 70 0 Z" fill="{C["gold"]}"/>'
            f'<rect x="-80" y="-12" width="160" height="16" rx="6" fill="{C["goldDeep"]}"/>'
            f'<path d="M -46 -150 Q -110 -160 -150 -230 L -138 -238 Q -96 -186 -40 -184 Z" fill="{C["gold"]}"/>')
    lid = (f'<path d="M -46 -170 Q 0 -250 46 -170 Z" fill="{C["sandLight"]}"/>'
           f'<circle cx="0" cy="-252" r="14" fill="{C["sandLight"]}"/>'
           f'<rect x="-50" y="-178" width="100" height="14" rx="6" fill="{C["goldDeep"]}"/>')
    handle = f'<path d="M 46 -150 Q 120 -140 100 -60 Q 90 -30 70 -24" fill="none" stroke="{C["goldDeep"]}" stroke-width="16" stroke-linecap="round"/>'
    return paper(handle, tone, 2, T=tr) + paper(body + lid, tone, 3, T=tr)


def door(x, base, w=150, h=300, tone=T):
    """A front door ajar, pearl light in the gap, gold knob."""
    o = paper(f'<rect x="{x}" y="{base - h}" width="{w}" height="{h}" fill="{C["pearl"]}" fill-opacity=".9"/>', tone, 1)
    o += paper(f'<polygon points="{x},{base - h} {x + w * .62:.1f},{base - h + 24} {x + w * .62:.1f},{base + 14} {x},{base}" fill="{C["night"]}"/>'
               f'<circle cx="{x + w * .5:.1f}" cy="{base - h / 2}" r="9" fill="{C["gold"]}"/>', tone, 2)
    o += paper(f'<path d="M {x - 10} {base} V {base - h - 10} H {x + w + 10} V {base}" fill="none" stroke="{C["tealDeep"]}" stroke-width="16"/>', tone, 2)
    return o


def tab(cx, y, w=70, h=110, seed=1, inner='', tone=T, rot=0):
    return torn_rect(cx - w / 2, y, w, h, C['gold'], tone, 'tblr', seed=seed, layer=3, rot=rot, amp=(3, 6), inner=inner)


def arrow_left(x0, x1, y, tone=T, seed=0):
    """Torn pearl arrow pointing LEFT (later in the day), x0 > x1."""
    o = torn_strip([(x0, y), (x1 + 30, y)], 16, C['pearl'], tone, seed=seed, layer=2)
    o += paper(f'<polygon points="{x1},{y} {x1 + 44},{y - 28} {x1 + 44},{y + 28}" fill="{C["pearl"]}"/>', tone, 2)
    return o


def note(cx, cy, w, h, inner_fn, seed, rot, tick=False, tone=T):
    """A torn sandLight note standing on the band, with a small icon."""
    o = torn_rect(cx - w / 2, cy - h / 2, w, h, C['sandLight'], tone, 'tblr', seed=seed, layer=2, rot=rot, amp=(4, 8))
    o += inner_fn(cx, cy)
    if tick:
        o += torn_strip([(cx + 10, cy - 96), (cx + 54, cy - 50), (cx + 140, cy - 160)], 32, C['gold'], tone, seed=seed + 3, layer=4)
    return o


# ---------------------------------------------------------------- slides
def slide(ctx):
    s = ctx.s
    if ctx.last:
        k = .5
        mini = (f'<g transform="translate({W - 60 - 1000 * k:.0f} 1000) scale({k})">'
                + band(260, 60, 1000, h=120, tone='l')
                + sun(880, 120, 70, tone='l', col='deep') + moon(150, 120, 74, tone='l') + '</g>')
        r = cta_end(ctx, mini_art=mini, tag_y=880, tag_x=MX - 10)
        return r

    art, html = '', ''
    if s == 1:
        # the whole day: sun right, moon left, the night stretch long
        art = (band(1000, h=160)
               + sun(880, 790, 92) + moon(170, 800, 96)
               + clock(seg_x(3)[0] + 100, 1230, 66, 8) + clock(seg_x(3)[0] - 100, 1230, 66, 10))
        html = hook_box(ctx, G, y=MT - 10, size=96, keep=('تبدئي تنوميه', 'الساعة ثمانيه', 'وما تطلعي من غرفته', 'إلا الساعة عشره؟'))
    elif s == 2:
        # zoom on 8 -> 10: one long night band, a clock at each end, a water cup on it
        art = (band(1000, 70, 1010, h=130, segs=[('night', 1)], seed=21)
               + clock(880, 900, 110, 8) + clock(200, 900, 110, 10)
               + cup(540, 1000, .8, steam=False)
               + ''.join(f'<g>{paper(f"<ellipse cx=\"{x}\" cy=\"{1065 + (i % 2) * 26}\" rx=\"14\" ry=\"9\" fill=\"{C["tealMist"]}\" fill-opacity=\".7\"/>", T, 1)}</g>'
                         for i, x in enumerate(range(380, 720, 48))))
        html = body_box(ctx, G, y=MT)
    elif s == 3:
        # asr -> bedtime: three gold tabs stand on the band before the pyjamas
        segs = [('gold', .3), ('sandLight', .2), ('tealDeep', .3), ('night', .2)]
        xs = [740, 580, 420]
        art = (band(900, h=100, segs=segs, seed=31)
               + sun(940, 820, 46)
               + ''.join(tab(x, 760, seed=40 + i, rot=(-4, 2, -2)[i],
                             inner=''.join(f'<circle cx="{x}" cy="{790 + j * 26}" r="8" fill="{C["ink"]}"/>' for j in range(i + 1)))
                         for i, x in enumerate(xs))
               + pyjamas(170, 800, .6))
        html = body_box(ctx, G, y=MT) + soft_cta(ctx, y=1080, w=860)
    elif s == 4:
        # the nap: the first segment lifted and lit, the sun low over it
        x, w = seg_x(0)
        art = (band(1040, h=120, lift=0, dim=(1, 2, 3), seed=41)
               + sun(x, 880, 70)
               + paper(f'<path d="M {x - 100} {1052} Q {x - 108} {990} {x - 40} {994} Q {x} {1004} {x + 40} {994} Q {x + 108} {990} {x + 100} {1052} Z" fill="{C["pearl"]}"/>', T, 4)
               + moon(170, 900, 60))
        html = body_box(ctx, G)
    elif s == 5:
        # the last stretch before bed: screen + shoe fade out, ball + warm cup take over
        art = (band(1150, h=90, dim=(0, 1), seed=51)
               + f'<g opacity=".45">{screen(870, 1010, .72)}{shoe(690, 1100, .72)}</g>'
               + arrow_left(590, 500, 1040, seed=3)
               + ball(400, 1060, 56) + cup(270, 1120, .75)
               + moon(130, 1010, 50))
        from kit import keep_in
        keep_in(ctx.t.body(), 'أو يشرب شي دافي.')
        html = body_box(ctx, G)
    elif s == 6:
        # a guest night: dallah + door on the band; the same bedtime steps, squeezed shorter
        art = (band(1100, h=110, seed=61)
               + door(820, 1090, 140, 280)
               + dallah(600, 1092, .8)
               + ''.join(tab(x, 960, w=44, h=74, seed=70 + i, rot=(-4, 2, -2)[i]) for i, x in enumerate((330, 270, 210)))
               + pyjamas(110, 1010, .38))
        html = body_box(ctx, G)
    elif s == 7:
        # three segments as notes on the band, one ticked
        def i_nap(cx, cy):
            return sun(cx, cy + 10, 50)

        def i_act(cx, cy):
            return ball(cx, cy, 62)

        def i_guest(cx, cy):
            return dallah(cx + 10, cy + 85, .62)
        art = (band(1100, h=110, seed=71)
               + note(800, 860, 220, 220, i_nap, 81, -4, tick=True)
               + note(540, 880, 220, 220, i_act, 82, 3)
               + note(280, 860, 220, 220, i_guest, 83, -2))
        html = body_box(ctx, G, y=MT + 20)
    return {'ground': G, 'art': art, 'html': html}
