"""p5 vacuum. Night ground, dark. One Big Object (macro).

Motif: canister vacuum ~70% of the frame bleeding off the bottom-left (pearl body,
deep hose arc, gold wheels); five torn teal/gold "noise" strips fan from the
nozzle; two small pearl mittens cover an ear at the top-left.
Inner slides: the vacuum shrinks (70 > 45 > 25%) and drifts left; s6 a pearl
doorway stands open on the right. Attention end (quiet line, one accent).
"""
import math
from kit import keep, keep_in, C, MX, MT, W, H, paper, torn_rect, torn_strip, torn_circle, text_box, step_tab, avoid

GROUND = 'night'
TONE = 'd'


def vacuum(tx, ty, s, strips=5, strip_len=1.0, strip_cols=None, hose=True, nozzle=True, seed=0):
    """Canister vacuum in local coords (body centre = 0,0), drawn at translate(tx,ty) scale(s).
    Each piece is its own sheet of paper; the filter sits outside the transform so
    shadows stay full size."""
    T = f'translate({tx} {ty}) scale({s})'
    out = []
    # small front castor (behind the body)
    out.append(paper(f'<circle cx="250" cy="215" r="58" fill="{C["gold"]}"/><circle cx="250" cy="215" r="20" fill="{C["goldDeep"]}"/>', TONE, 1, T=T))
    # hose (deep, with faint pearl ribbing): from the body up, round, and back left to the nozzle
    if hose:
        d = 'M 300 -110 C 600 -190, 640 -480, 330 -470'
        out.append(paper(f'<path d="{d}" fill="none" stroke="{C["deep"]}" stroke-width="64" stroke-linecap="round"/>'
                         f'<path d="{d}" fill="none" stroke="{C["pearl"]}" stroke-opacity=".22" stroke-width="64" stroke-dasharray="7 30"/>',
                         TONE, 2, T=T))
    # body
    out.append(paper(f'<ellipse cx="0" cy="0" rx="390" ry="245" fill="{C["pearl"]}"/>', TONE, 1, T=T))
    # lid band along the top, hose port at the front
    out.append(paper(f'<path d="M -268 -178 A 390 245 0 0 1 268 -178 Q 0 -150 -268 -178 Z" fill="{C["deep"]}"/>', TONE, 2, T=T))
    out.append(paper(f'<circle cx="330" cy="-70" r="56" fill="{C["deep"]}"/>', TONE, 2, T=T))
    # big rear wheel on the side (the canister's tell), gold with a goldDeep hub
    out.append(paper(f'<circle cx="-150" cy="70" r="150" fill="{C["gold"]}"/>'
                     f'<circle cx="-150" cy="70" r="104" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".45" stroke-width="6"/>'
                     f'<circle cx="-150" cy="70" r="46" fill="{C["goldDeep"]}"/>', TONE, 2, T=T))
    # power button + vents on the front half
    out.append(paper(f'<circle cx="150" cy="-70" r="34" fill="{C["gold"]}"/>', TONE, 3, T=T))
    vents = ''.join(f'<rect x="{90 + k * 44}" y="10" width="22" height="110" rx="11" fill="{C["sandLight"]}"/>' for k in range(4))
    out.append(paper(vents, TONE, 2, 't', T=T))
    # nozzle at the hose end, pointing left (towards the ear)
    if nozzle:
        out.append(paper(f'<g transform="rotate(-8 330 -470)"><rect x="150" y="-508" width="200" height="76" rx="16" fill="{C["pearl"]}"/>'
                         f'<rect x="300" y="-508" width="50" height="76" rx="10" fill="{C["gold"]}"/>'
                         f'<rect x="138" y="-520" width="34" height="100" rx="8" fill="{C["deep"]}"/></g>', TONE, 3, T=T))
    # noise strips fanning left from the nozzle mouth
    ox, oy = 120, -462
    angles = [214, 196, 180, 164, 146]
    lens = [120, 150, 170, 150, 120]
    cols = strip_cols or ['teal', 'gold', 'teal', 'gold', 'teal']
    pick = {5: [0, 1, 2, 3, 4], 3: [1, 2, 3], 2: [1, 3]}.get(strips, list(range(strips)))
    for k in pick:
        a = math.radians(angles[k])
        r0, r1 = 40, 40 + lens[k] * strip_len
        p0 = (ox + r0 * math.cos(a), oy + r0 * math.sin(a))
        p1 = (ox + r1 * math.cos(a), oy + r1 * math.sin(a))
        out.append(torn_strip([p0, p1], 34, C[cols[k]], TONE, seed=seed + 20 + k, layer=2, T=T))
    return avoid(''.join(out), 'vacuum')


def mittens(cy=700):
    """Back/side of a head (face is off-frame left, never shown) with goldDeep hair,
    and two pearl mittens cupped over the ear."""
    head = paper(f'<circle cx="-30" cy="{cy}" r="190" fill="{C["sandLight"]}"/>', TONE, 1)
    hair = paper(f'<path d="M -220 {cy + 10} A 190 190 0 0 1 150 {cy - 60} Q 60 {cy - 110} 0 {cy - 60} Q -60 {cy - 10} -90 {cy + 70} Q -160 {cy + 60} -220 {cy + 10} Z" fill="{C["goldDeep"]}"/>', TONE, 2, 't')
    mit = lambda x, y, r: paper(
        f'<g transform="translate({x} {y}) rotate({r})">'
        f'<path d="M -48 60 L -52 -20 Q -50 -80 0 -82 Q 50 -80 50 -20 L 48 60 Z" fill="{C["pearl"]}"/>'
        f'<ellipse cx="54" cy="10" rx="20" ry="34" transform="rotate(-25 54 10)" fill="{C["pearl"]}"/>'
        f'<rect x="-54" y="52" width="108" height="30" rx="8" fill="{C["gold"]}"/></g>', TONE, 3)
    return avoid(head + hair + mit(140, cy - 10, -16) + mit(170, cy + 82, 14), 'ear')


def moon(cx, cy, r):
    return paper(f'<path d="M {cx} {cy - r} A {r} {r} 0 1 0 {cx} {cy + r} A {r * .62} {r} 0 1 1 {cx} {cy - r} Z" fill="{C["pearl"]}"/>', TONE, 1)


def speech(x, y, w, h, seed=5):
    tail = f'<polygon points="{x + 40},{y + h - 4} {x + 20},{y + h + 46} {x + 96},{y + h - 4}" fill="{C["pearl"]}"/>'
    return avoid(torn_rect(x, y, w, h, C['pearl'], TONE, 'tblr', seed=seed, layer=2, inner=tail), 'bubble')


def doorway(x, y, w, h):
    """Pearl open doorway: frame, light spilling in, door leaf swung open."""
    frame = paper(f'<path d="M {x} {y + h} V {y} H {x + w} V {y + h}" fill="none" stroke="{C["pearl"]}" stroke-width="26" stroke-linejoin="round"/>', TONE, 2)
    light = paper(f'<rect x="{x + 13}" y="{y + 13}" width="{w - 26}" height="{h - 13}" fill="{C["pearl"]}" fill-opacity=".9"/>', TONE, 1)
    spill = paper(f'<polygon points="{x + 13},{y + h} {x + w - 13},{y + h} {x + w - 120},{y + h + 120} {x - 160},{y + h + 120}" fill="{C["pearl"]}" fill-opacity=".18"/>', TONE, 1, 't')
    leaf = paper(f'<polygon points="{x + w - 13},{y + 13} {x + w + 70},{y + 50} {x + w + 70},{y + h + 30} {x + w - 13},{y + h}" fill="{C["sandLight"]}"/>'
                 f'<circle cx="{x + w + 50}" cy="{y + h * .55}" r="9" fill="{C["gold"]}"/>', TONE, 2)
    return avoid(spill + light + leaf + frame, 'door')


def rooms(x, y):
    """Three receding door frames: the farthest room is the smallest."""
    out = ''
    for k, (w, h) in enumerate(((560, 520), (400, 380), (250, 240))):
        cx = x
        out += paper(f'<rect x="{cx - w / 2}" y="{y - h}" width="{w}" height="{h}" fill="none" stroke="{C["pearl"]}" '
                     f'stroke-opacity="{.35 + k * .25}" stroke-width="{18 - k * 4}"/>', TONE, 1 + (k > 0))
    return out


def body(ctx, y=None, w=888):
    """Tab (if the slide has a label) + body text block."""
    html = ''
    top = y or (MT + 120 if ctx.t.label() else MT + 40)
    if ctx.t.label():
        html += step_tab(ctx.t.label())
    html += text_box(ctx.t.body(), W - MX - w, top, w, 'pearl')
    return html


BREAKS = {  # phrase groups that must stay on one line (break only between them)
    3: ['هذي ثلاث أشياء', 'ما تاخذ إلا ثواني،', 'وأنتي ماسكة المكنسة.'],
    4: ['قبل ما تشغليها،', 'قولي له "بشغل المكنسة".', 'نفس الجملة كل مرة،', 'عشان يعرف إن الصوت جاي.'],
    5: ['ابدئي من أبعد غرفة عنه،', 'مو من الغرفة اللي هو فيها.', 'كذا الصوت يقرب شوي شوي،', 'بدل ما يبدأ جمبه.'],
    6: ['لا توقفي بالمكنسة', 'بينه وبين الباب.', 'إذا بغى يبعد،', 'طريقه مفتوح.'],
    7: ['والهدف إنك تكنسي', 'العصر وهو صاحي،', 'بدل ما تستني', 'إلين ما ينام.'],
}


def slide(ctx):
    s = ctx.s
    art, html = '', ''
    if s in BREAKS:
        keep_in(ctx.t.segs, *BREAKS[s])
    if s == 1:
        hook = ctx.t.body()[0]
        keep(hook, 'يغطي أذنه', 'أول ما تشغلي المكنسة،', 'فصرتي تكنسي', 'وهو نايم؟')
        art = mittens(660) + vacuum(330, 1185, 1.0)
        # 88px (hook range 88-110): at 96 the phrase "أول ما تشغلي المكنسة،" is 1003px and
        # cannot sit on one line; 88px in a 920px box keeps every break at a phrase boundary.
        html = text_box([hook], 80, MT, 920, 'pearl', size={'hook': 88})
    elif s == 2:
        # "when he sleeps you have no strength": vacuum parked, silent, under a moon
        art = moon(890, 640, 90) + vacuum(360, 1075, .7, strips=0, nozzle=True)
        html = body(ctx, y=MT + 60)
    elif s == 3:
        # three things: three gold strips only, vacuum held ready
        art = vacuum(380, 1090, .62, strips=3, strip_len=1.3, strip_cols=['gold'] * 5, seed=3)
        html = body(ctx, y=MT + 60)
    elif s == 4:
        # say it first: vacuum off, an empty pearl speech note
        art = speech(640, 690, 300, 170) + vacuum(320, 1110, .52, strips=0)
        html = body(ctx)
    elif s == 5:
        # start from the farthest room: vacuum small inside the farthest frame
        art = avoid(rooms(540, 1230) + vacuum(530, 1160, .2, strips=3, strip_len=.7, seed=9), 'rooms')
        html = body(ctx)
    elif s == 6:
        # don't block the door: open pearl doorway on the right, vacuum to the left
        art = doorway(720, 760, 200, 420) + vacuum(210, 1150, .27, strips=2, strip_len=.8, strip_cols=['gold'] * 5, seed=11)
        html = body(ctx)
    else:
        # attention end: quiet line centred, one accent (the vacuum, parked, silent)
        art = vacuum(540, 1120, .3, strips=0, nozzle=True)
        segs = ctx.t.body()
        for g in segs:
            g.role = 'quiet'
        html = text_box(segs, MX, 400, W - 2 * MX, 'pearl', align='center')
    return {'ground': GROUND, 'art': art, 'html': html}
