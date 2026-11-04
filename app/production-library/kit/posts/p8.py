"""p8 aunt. Pearl ground, light. Type-first (the batch's only pearl-ground post).

The type is the picture: every slide's first sentence is set big in El Messiri
700, Deep Sea, as cut-paper letters lifted off a gold duplicate offset -8px 8px
(CSS text-shadow, so nothing is typed twice) with a paper contact shadow. The
rest of the slide follows at body size in ink. A short torn gold rule separates
the two, like a cut in the page.
Accents are small and low, centred under the type: one closed storybook (gold
cover, pearl pages, deep ribbon) is the through-line.
s1: «مو كل مرة… يعاندك.» at 120px; the rest at 54px; the book bottom-left.
s2 a door left ajar; s3 your gold chair, taken by a sandLight cardigan; s4 the
    routine as four cards, in order, unchanged; s5 a deep speech note said early;
    s6 the book stays by the gold chair; s7 striped pyjamas pass to a sandLight hand.
s8 conversion end: gold ground, ink type, pearl tag «الرابط في البايو.», the book at 25%.
"""
from kit import (C, MX, MT, W, H, paper, torn_rect, torn_strip, torn_circle, glow,
                 text_box, step_tab, avoid, keep_in, conversion_tag)

TONE = 'l'

CSS = """
.slide .typefirst, .slide .tf { color: var(--deep); }
.typefirst { text-shadow: -8px 8px 0 var(--gold);
  filter: drop-shadow(-1px 2px 1px rgba(14,47,56,.30)) drop-shadow(-5px 9px 8px rgba(14,47,56,.14)); }
.tf { font-family: 'El Messiri'; font-weight: 700; font-size: 84px; line-height: 1.3; text-wrap: balance;
  text-shadow: -6px 6px 0 var(--gold);
  filter: drop-shadow(-1px 2px 1px rgba(14,47,56,.30)) drop-shadow(-4px 8px 7px rgba(14,47,56,.14)); }
.tf + .support, .tf + .clause, .support + .tf, .clause + .typefirst { margin-top: 64px; }
.typefirst + .clause { margin-top: 70px; }
.g-gold .tf { color: var(--ink); text-shadow: none; }
"""


# ---------------------------------------------------------------- accents
def book(cx, cy, s=1.0, rot=-8, layer=2):
    """Closed storybook seen from the front-top: gold cover, pearl page block, deep ribbon."""
    w, h = 230 * s, 170 * s
    x, y = cx - w / 2, cy - h / 2
    g = (f'<g transform="rotate({rot} {cx} {cy})">'
         f'<rect x="{x + 10 * s:.1f}" y="{y + 14 * s:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{8 * s:.1f}" fill="{C["pearl"]}"/>'
         + ''.join(f'<rect x="{x + 12 * s:.1f}" y="{y + h + 14 * s - k * 5 * s - 5 * s:.1f}" width="{w - 4 * s:.1f}" height="{1.6 * s:.1f}" fill="{C["sandLight"]}"/>' for k in range(3))
         + f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{10 * s:.1f}" fill="{C["gold"]}"/>'
         f'<rect x="{x:.1f}" y="{y:.1f}" width="{22 * s:.1f}" height="{h:.1f}" rx="{8 * s:.1f}" fill="{C["goldDeep"]}"/>'
         f'<rect x="{x + 50 * s:.1f}" y="{y + 34 * s:.1f}" width="{w - 86 * s:.1f}" height="{h - 68 * s:.1f}" rx="{6 * s:.1f}" fill="none" stroke="{C["pearl"]}" stroke-opacity=".7" stroke-width="{4 * s:.1f}"/>'
         f'<circle cx="{x + 50 * s + (w - 86 * s) / 2:.1f}" cy="{cy:.1f}" r="{20 * s:.1f}" fill="{C["deep"]}"/>'
         f'<path d="M {x + w - 50 * s:.1f} {y + h:.1f} l 0 {44 * s:.1f} l {9 * s:.1f} {-10 * s:.1f} l {9 * s:.1f} {10 * s:.1f} l 0 {-44 * s:.1f} Z" fill="{C["deep"]}"/>'
         '</g>')
    return avoid(paper(g, TONE, layer), 'book')


def chair(cx, base, s=1.0, layer=1):
    """Front-on gold armchair standing on base y."""
    w = 300 * s
    x = cx - w / 2
    g = (f'<rect x="{x + 30 * s:.1f}" y="{base - 330 * s:.1f}" width="{w - 60 * s:.1f}" height="{230 * s:.1f}" rx="{40 * s:.1f}" fill="{C["gold"]}"/>'
         f'<rect x="{x:.1f}" y="{base - 190 * s:.1f}" width="{60 * s:.1f}" height="{150 * s:.1f}" rx="{26 * s:.1f}" fill="{C["gold"]}"/>'
         f'<rect x="{x + w - 60 * s:.1f}" y="{base - 190 * s:.1f}" width="{60 * s:.1f}" height="{150 * s:.1f}" rx="{26 * s:.1f}" fill="{C["gold"]}"/>'
         f'<rect x="{x + 50 * s:.1f}" y="{base - 130 * s:.1f}" width="{w - 100 * s:.1f}" height="{70 * s:.1f}" rx="{16 * s:.1f}" fill="{C["goldDeep"]}"/>'
         f'<rect x="{x + 22 * s:.1f}" y="{base - 44 * s:.1f}" width="{20 * s:.1f}" height="{44 * s:.1f}" fill="{C["goldDeep"]}"/>'
         f'<rect x="{x + w - 42 * s:.1f}" y="{base - 44 * s:.1f}" width="{20 * s:.1f}" height="{44 * s:.1f}" fill="{C["goldDeep"]}"/>')
    return paper(g, TONE, layer)


def door(cx, base, s=1.0):
    """A bedroom door left ajar: night gap, deep leaf, gold knob, sandLight light on the floor."""
    w, h = 220 * s, 400 * s
    x, y = cx - w / 2, base - h
    frame = paper(f'<rect x="{x - 16 * s:.1f}" y="{y - 16 * s:.1f}" width="{w + 32 * s:.1f}" height="{h + 16 * s:.1f}" rx="{6 * s:.1f}" fill="{C["sandLight"]}"/>'
                  f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{C["night"]}"/>', TONE, 1)
    leaf = paper(f'<polygon points="{x + 44 * s:.1f},{y:.1f} {x + w:.1f},{y - 20 * s:.1f} {x + w:.1f},{base + 20 * s:.1f} {x + 44 * s:.1f},{base:.1f}" fill="{C["deep"]}"/>'
                 f'<circle cx="{x + 74 * s:.1f}" cy="{y + h * .55:.1f}" r="{11 * s:.1f}" fill="{C["gold"]}"/>', TONE, 2)
    return avoid(frame + leaf, 'door')


def cardigan(cx, cy, s=1.0):
    """A sandLight cardigan draped over the chair back: someone else's place."""
    g = (f'<path d="M {cx - 120 * s:.1f} {cy:.1f} Q {cx:.1f} {cy - 40 * s:.1f} {cx + 120 * s:.1f} {cy:.1f} L {cx + 104 * s:.1f} {cy + 150 * s:.1f} '
         f'L {cx + 40 * s:.1f} {cy + 120 * s:.1f} L {cx:.1f} {cy + 60 * s:.1f} L {cx - 40 * s:.1f} {cy + 120 * s:.1f} L {cx - 104 * s:.1f} {cy + 150 * s:.1f} Z" fill="{C["sandLight"]}"/>'
         + ''.join(f'<circle cx="{cx + dx * s:.1f}" cy="{cy + dy * s:.1f}" r="{6 * s:.1f}" fill="{C["deep"]}"/>' for dx, dy in ((-24, 50), (-34, 84), (24, 50), (34, 84))))
    return paper(g, TONE, 3)


def card(x, y, s, icon, seed, rot):
    return torn_rect(x, y, s, s, C['tealMist'], TONE, 'tblr', seed=seed, layer=2, rot=rot, amp=(4, 8), inner=icon)


def ic_moon(x, y, s):
    cx, cy, r = x + s / 2, y + s / 2, s * .26
    return f'<path d="M {cx} {cy - r} A {r} {r} 0 1 0 {cx} {cy + r} A {r * .62} {r} 0 1 1 {cx} {cy - r} Z" fill="{C["deep"]}"/>'


def ic_cup(x, y, s):
    return (f'<rect x="{x + s * .32}" y="{y + s * .3}" width="{s * .3}" height="{s * .42}" rx="{s * .05}" fill="{C["deep"]}"/>'
            f'<path d="M {x + s * .62} {y + s * .38} q {s * .14} 0 {s * .14} {s * .12} q 0 {s * .12} {-s * .14} {s * .12}" fill="none" stroke="{C["deep"]}" stroke-width="{s * .05}"/>')


def ic_pyj(x, y, s):
    return pyjama_shape(x + s / 2, y + s / 2 + s * .02, s * .002)


def ic_book(x, y, s):
    return (f'<rect x="{x + s * .24}" y="{y + s * .3}" width="{s * .52}" height="{s * .4}" rx="{s * .04}" fill="{C["gold"]}"/>'
            f'<rect x="{x + s * .24}" y="{y + s * .3}" width="{s * .07}" height="{s * .4}" fill="{C["goldDeep"]}"/>')


def pyjama_shape(cx, cy, s):
    """Striped pyjama top (shapes only, no filter). s ~ 1 = 300px wide."""
    body = (f'M {cx - 70 / 1 * s * 1:.1f} {cy - 110 * s:.1f} L {cx - 150 * s:.1f} {cy - 60 * s:.1f} L {cx - 118 * s:.1f} {cy + 10 * s:.1f} '
            f'L {cx - 80 * s:.1f} {cy - 10 * s:.1f} L {cx - 80 * s:.1f} {cy + 120 * s:.1f} L {cx + 80 * s:.1f} {cy + 120 * s:.1f} '
            f'L {cx + 80 * s:.1f} {cy - 10 * s:.1f} L {cx + 118 * s:.1f} {cy + 10 * s:.1f} L {cx + 150 * s:.1f} {cy - 60 * s:.1f} '
            f'L {cx + 70 * s:.1f} {cy - 110 * s:.1f} Q {cx:.1f} {cy - 70 * s:.1f} {cx - 70 * s:.1f} {cy - 110 * s:.1f} Z')
    cid = f'pj{int(cx)}{int(cy)}'
    stripes = ''.join(f'<rect x="{cx - 160 * s:.1f}" y="{cy - 120 * s + k * 36 * s:.1f}" width="{320 * s:.1f}" height="{16 * s:.1f}" fill="{C["deep"]}"/>'
                      for k in range(8))
    return (f'<defs><clipPath id="{cid}"><path d="{body}"/></clipPath></defs>'
            f'<path d="{body}" fill="{C["pearl"]}" stroke="{C["deep"]}" stroke-opacity=".25" stroke-width="{3 * s:.1f}"/>'
            f'<g clip-path="url(#{cid})">{stripes}</g>')


def pyjamas(cx, cy, s=1.0, rot=0):
    return paper(f'<g transform="rotate({rot} {cx} {cy})">{pyjama_shape(cx, cy, s)}</g>', TONE, 2)


def hand(x, y, s=1.0):
    """A sandLight hand and sleeve reaching in from the left edge, palm up (no face, no figure)."""
    g = (f'<rect x="{x - 400 * s:.1f}" y="{y - 46 * s:.1f}" width="{330 * s:.1f}" height="{92 * s:.1f}" rx="{20 * s:.1f}" fill="{C["deep"]}"/>'
         f'<path d="M {x - 90 * s:.1f} {y - 38 * s:.1f} L {x + 40 * s:.1f} {y - 44 * s:.1f} Q {x + 110 * s:.1f} {y - 46 * s:.1f} {x + 112 * s:.1f} {y - 20 * s:.1f} '
         f'Q {x + 112 * s:.1f} {y - 4 * s:.1f} {x + 60 * s:.1f} {y - 2 * s:.1f} L {x + 80 * s:.1f} {y + 4 * s:.1f} Q {x + 104 * s:.1f} {y + 18 * s:.1f} {x + 78 * s:.1f} {y + 30 * s:.1f} '
         f'L {x + 20 * s:.1f} {y + 40 * s:.1f} L {x - 90 * s:.1f} {y + 40 * s:.1f} Z" fill="{C["sandLight"]}"/>'
         f'<path d="M {x + 40 * s:.1f} {y - 44 * s:.1f} Q {x + 70 * s:.1f} {y - 70 * s:.1f} {x + 96 * s:.1f} {y - 62 * s:.1f} Q {x + 100 * s:.1f} {y - 48 * s:.1f} {x + 78 * s:.1f} {y - 40 * s:.1f} Z" fill="{C["sandLight"]}"/>'
         f'<rect x="{x - 96 * s:.1f}" y="{y - 50 * s:.1f}" width="{26 * s:.1f}" height="{100 * s:.1f}" rx="{8 * s:.1f}" fill="{C["gold"]}"/>')
    return paper(g, TONE, 2)


def speech(cx, cy, s=1.0):
    w, h = 300 * s, 170 * s
    tail = f'<polygon points="{cx + w * .18:.1f},{cy + h / 2 - 6:.1f} {cx + w * .36:.1f},{cy + h / 2 + 56 * s:.1f} {cx + w * .02:.1f},{cy + h / 2 - 6:.1f}" fill="{C["deep"]}"/>'
    dots = ''.join(f'<circle cx="{cx + dx * s:.1f}" cy="{cy:.1f}" r="{14 * s:.1f}" fill="{C["gold"]}"/>' for dx in (-60, 0, 60))
    return avoid(torn_rect(cx - w / 2, cy - h / 2, w, h, C['deep'], TONE, 'tblr', seed=23, layer=2, amp=(4, 8), inner=tail + dots), 'speech')


def sun(cx, cy, r):
    rays = ''.join(f'<rect x="{cx - 5}" y="{cy - r - 34}" width="10" height="22" rx="5" fill="{C["gold"]}" transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 45))
    return paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["gold"]}"/>{rays}', TONE, 2)


def rule(x, y, w=150, seed=0):
    """Short torn gold rule: a cut in the page between big type and body."""
    return torn_strip([(x, y), (x + w, y - 3)], 16, C['gold'], TONE, seed=seed + 77, layer=1, core=True)


def floor_line(y, x0=250, x1=830):
    return paper(f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="8" rx="4" fill="{C["sandLight"]}"/>', TONE, 1, 't')


# ---------------------------------------------------------------- slides
BREAKS = {
    1: ['مو كل مرة', 'يرفض فيها طفلك', 'التغيير', 'يعني إنه يعاندك.', 'قبل ما تفرضي عليه التغيير،', 'ابدئي بهذي الأربع خطوات.'],
    2: ['كل ليلة', 'إنتي تجهزيه للنوم.', 'اليوم خالته موجودة،', 'وأول ما قربت منه', 'رفض يدخل الغرفة معاها.'],
    3: ['هو متعود إنك إنتي', 'اللي تجهزيه،', 'وفجأة شخص ثاني', 'أخذ مكانك.'],
    4: ['لا تغيري', 'الروتين كله.', 'خلي وقت النوم وترتيب خطواته', 'زي ما تعود.'],
    5: ['لا تخلي التغيير', 'مفاجأة.', 'قولي له من بدري', 'إن خالته بتساعده اليوم.'],
    6: ['خلي جزء من الروتين', 'زي ما هو.', 'لو متعود تقرأوا قصة،', 'خليها معاكي.'],
    7: ['ابدئي بخطوة', 'بسيطة.', 'خلي خالته تساعده في لبس البيجامة،', 'وإنتي كمّلي باقي الروتين.'],
    8: ['تغيير شخص واحد', 'ممكن يغيّر تجربة كاملة.', 'التقييم المجاني يساعدك', 'تشوفي جوانب مختلفه من يومه.'],
}

LOW = 1170      # floor of the low vignettes


def two_part(ctx, at='. ', big_first=True):
    """Cut the slide's single sentence run into big type + body, at the first `at`."""
    a, b = ctx.t.split_seg(ctx.t.body()[0], at)
    if big_first:
        a.role, b.role = 'tf', 'support'
    else:
        a.role, b.role = 'support', 'tf'
    return a, b


def slide(ctx):
    s = ctx.s
    r = {'ground': 'pearl', 'css': CSS}

    if s == 1:
        q, clause = ctx.t.split_seg(ctx.t.body()[0], '. ')
        q.role, clause.role = 'typefirst', 'clause'
        keep_in(ctx.t.segs, *BREAKS[1])
        art = book(250, 1105, 1.05, rot=-9) + rule(MX + 640, 790)
        html = text_box([q, clause], 72, MT - 10, W - 144, 'deep', size={'typefirst': 116})
        r.update(art=art, html=html)
        return r

    if s == 8:
        a, rest = ctx.t.split_seg(ctx.t.body()[0], '. ')
        b, cta = ctx.t.split_seg(rest, '. ')
        a.role, b.role = 'tf', 'support'
        assert cta.text == ctx.cta_text(), (cta.text, ctx.cta_text())
        keep_in(ctx.t.segs, *BREAKS[8])
        art = book(190, 1150, .5, rot=-9, layer=1)
        html = (text_box([a, b], MX, 230, W - 2 * MX, 'ink', size={'tf': 80})
                + conversion_tag(cta, 330, 820, rot=-3))
        r.update(ground='gold', art=art, html=html, dots_theme='gold')
        return r

    if s == 3:
        two_part(ctx, '، ', big_first=False)
    else:
        two_part(ctx)
    keep_in(ctx.t.segs, *BREAKS[s])

    top = MT + 130 if ctx.t.label() else MT + 30
    html = (step_tab(ctx.t.label()) if ctx.t.label() else '') + text_box(ctx.t.body(), MX, top, W - 2 * MX, 'ink')

    if s == 2:
        art = floor_line(LOW) + door(540, LOW, .8)
    elif s == 3:
        art = floor_line(LOW) + avoid(chair(540, LOW, .85) + cardigan(540, LOW - 270, .85), 'chair')
    elif s == 4:
        sz, gap = 150, 30
        x0 = (W - 4 * sz - 3 * gap) / 2
        icons = [ic_book, ic_pyj, ic_cup, ic_moon]          # RTL: the routine reads from the right
        thread = paper(f'<path d="M {x0 + sz / 2} {LOW - 150} H {x0 + 3 * (sz + gap) + sz / 2}" stroke="{C["deep"]}" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round"/>', TONE, 1)
        cards = ''.join(card(x0 + k * (sz + gap), LOW - 225 + (k % 2) * 14, sz, icons[k](x0 + k * (sz + gap), LOW - 225 + (k % 2) * 14, sz), 60 + k, (-3, 2, -2, 3)[k])
                        for k in range(4))
        art = avoid(thread + cards, 'routine')
    elif s == 5:
        art = avoid(sun(330, LOW - 160, 52), 'sun') + speech(640, LOW - 170, .95)
    elif s == 6:
        art = floor_line(LOW) + avoid(chair(600, LOW, .8), 'chair') + book(330, LOW - 70, .7, rot=-4, layer=2)
    else:
        art = avoid(hand(330, LOW - 150, 1.0), "hand") + avoid(pyjamas(660, LOW - 160, .9, rot=-8), 'pyjamas')
    r.update(art=art, html=html)
    return r
