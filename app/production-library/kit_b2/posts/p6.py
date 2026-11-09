"""p6 Only after he sleeps. tealMist ground, ink text. Composition: PINNED NOTES
ON A WALL.

The chores wait on the wall: s1 the vacuum and the pot, greyed (paused) under a
gold crescent moon. s2 the moon over a heap of chores in full colour (vacuum,
pot, laundry basket). s3 three blank torn notes pinned in a row (the three things
to notice). s4-s6 the notes turn over one per slide, right to left (RTL): the
active note grows and lifts, the ones already read stay small with their icon:
  1 vacuum noise strips ending in a deep end bar, a cupped ear;
  2 a small hand holding a T-shirt on the line;
  3 a small hand on a teal cloth wiping a table edge.
CTA end: gold, the three revealed notes small in the bottom-left.
"""
import math
from kit import C, MX, MT, W, H, paper, torn_strip, torn_rect, torn_circle, avoid, arc_pts, keep_in
from common import hook_box, body_box, soft_cta, cta_end

G = 'tealMist'
T = 'l'
GREY = '#B9D2CF'      # paused: a deeper tealMist
GREY2 = '#A6C4C1'

FULL = {'body': C['pearl'], 'lid': C['deep'], 'wheel': C['gold'], 'hub': C['goldDeep'], 'vent': C['sandLight'], 'btn': C['gold']}
PAUSED = {'body': C['pearl'], 'lid': GREY2, 'wheel': GREY, 'hub': GREY2, 'vent': GREY, 'btn': GREY}


# ------------------------------------------------------------------ chores
def vacuum(tx, ty, s, pal=FULL, tone=T, hose=True):
    """Canister vacuum (from Batch 1 p5), parked, hose curling up, no noise."""
    tr = f'translate({tx} {ty}) scale({s})'
    out = paper(f'<circle cx="250" cy="215" r="58" fill="{pal["wheel"]}"/><circle cx="250" cy="215" r="20" fill="{pal["hub"]}"/>', tone, 1, T=tr)
    d = 'M 300 -110 C 600 -190, 640 -480, 330 -470'
    if hose:
        out += paper(f'<path d="{d}" fill="none" stroke="{pal["lid"]}" stroke-width="64" stroke-linecap="round"/>'
                 f'<path d="{d}" fill="none" stroke="{C["pearl"]}" stroke-opacity=".25" stroke-width="64" stroke-dasharray="7 30"/>', tone, 2, T=tr)
    out += paper(f'<ellipse cx="0" cy="0" rx="390" ry="245" fill="{pal["body"]}"/>', tone, 1, T=tr)
    out += paper(f'<path d="M -268 -178 A 390 245 0 0 1 268 -178 Q 0 -150 -268 -178 Z" fill="{pal["lid"]}"/>'
                 f'<circle cx="330" cy="-70" r="56" fill="{pal["lid"]}"/>', tone, 2, T=tr)
    out += paper(f'<circle cx="-150" cy="70" r="150" fill="{pal["wheel"]}"/>'
                 f'<circle cx="-150" cy="70" r="104" fill="none" stroke="{pal["hub"]}" stroke-opacity=".45" stroke-width="6"/>'
                 f'<circle cx="-150" cy="70" r="46" fill="{pal["hub"]}"/>', tone, 2, T=tr)
    out += paper(''.join(f'<rect x="{90 + k * 44}" y="10" width="22" height="110" rx="11" fill="{pal["vent"]}"/>' for k in range(4)), tone, 2, 't', T=tr)
    if hose:
        out += paper(f'<g transform="rotate(-8 330 -470)"><rect x="150" y="-508" width="200" height="76" rx="16" fill="{pal["body"]}"/>'
                 f'<rect x="300" y="-508" width="50" height="76" rx="10" fill="{pal["wheel"]}"/>'
                 f'<rect x="138" y="-520" width="34" height="100" rx="8" fill="{pal["lid"]}"/></g>', tone, 3, T=tr)
    return out


def pot(cx, cy, s=1.0, paused=False, tone=T):
    """Cooking pot, side view: body, rim, two handles, lid and knob."""
    tr = f'translate({cx} {cy}) scale({s})'
    body = GREY if paused else C['deep']
    rim = GREY2 if paused else C['night']
    lid = C['pearl'] if paused else C['gold']
    knob = GREY2 if paused else C['goldDeep']
    out = paper(f'<rect x="-250" y="-40" width="60" height="34" rx="14" fill="{rim}"/>'
                f'<rect x="190" y="-40" width="60" height="34" rx="14" fill="{rim}"/>', tone, 1, T=tr)
    out += paper(f'<path d="M -200 -60 H 200 V 120 Q 200 180 140 180 H -140 Q -200 180 -200 120 Z" fill="{body}"/>'
                 f'<rect x="-214" y="-74" width="428" height="30" rx="12" fill="{rim}"/>', tone, 2, T=tr)
    out += paper(f'<path d="M -206 -78 Q 0 -190 206 -78 Z" fill="{lid}"/>'
                 f'<rect x="-34" y="-176" width="68" height="40" rx="16" fill="{knob}"/>', tone, 3, T=tr)
    return out


def basket(cx, cy, s=1.0, tone=T):
    """Laundry basket with clothes heaped over the rim."""
    tr = f'translate({cx} {cy}) scale({s})'
    clothes = paper(f'<path d="M -170 -40 Q -150 -150 -60 -120 Q -10 -190 60 -130 Q 140 -160 170 -40 Z" fill="{C["teal"]}"/>'
                    f'<path d="M -120 -40 Q -90 -110 -20 -90 Q 30 -120 80 -60 L 90 -40 Z" fill="{C["pearl"]}"/>'
                    f'<path d="M 40 -40 Q 80 -120 150 -80 L 160 -40 Z" fill="{C["gold"]}"/>', tone, 1, T=tr)
    weave = ''.join(f'<rect x="-150" y="{-10 + k * 42}" width="300" height="12" rx="6" fill="{C["goldDeep"]}" fill-opacity=".35"/>' for k in range(4))
    body = paper(f'<path d="M -190 -50 H 190 L 160 170 H -160 Z" fill="{C["sandLight"]}"/>{weave}'
                 f'<rect x="-204" y="-62" width="408" height="30" rx="12" fill="{C["gold"]}"/>', tone, 2, T=tr)
    return clothes + body


def moon(cx, cy, r, col=None, tone=T):
    col = col or C['gold']
    return paper(f'<path d="M {cx} {cy - r} A {r} {r} 0 1 0 {cx} {cy + r} A {r * .6} {r} 0 1 1 {cx} {cy - r} Z" fill="{col}"/>', tone, 2)


# ------------------------------------------------------------------ notes
def small_hand(x, y, s=1.0, rot=0, tone=T, layer=3):
    """A small open hand, palm down, fingers pointing right (rot turns it)."""
    fingers = ''.join(f'<rect x="40" y="{-34 + n * 17}" width="{62 - abs(n - 1.5) * 10:.0f}" height="15" rx="7.5" '
                      f'transform="rotate({(n - 1.5) * -6:.0f} 40 {-27 + n * 17})"/>' for n in range(4))
    thumb = '<rect x="-4" y="-50" width="50" height="17" rx="8.5" transform="rotate(-16 10 -42)"/>'
    palm = '<rect x="-34" y="-40" width="86" height="76" rx="30"/>'
    cuff = f'<rect x="-120" y="-36" width="96" height="68" rx="10" fill="{C["teal"]}"/>'
    return paper(f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">{cuff}<g fill="{C["sandLight"]}">{palm}{fingers}{thumb}</g></g>', tone, layer)


def icon_vacuum(tone=T):
    """Note 1: a small vacuum, noise strips that stop at a deep end bar, an ear."""
    out = vacuum(-50, 50, .2, tone=tone, hose=False)
    for k, (y, L) in enumerate(((-2, 54), (28, 70), (58, 54))):
        out += torn_strip([(34, y), (34 + L, y)], 12, C['teal'], tone, seed=200 + k, layer=2)
    out += paper(f'<rect x="114" y="-24" width="16" height="104" rx="6" fill="{C["deep"]}"/>', tone, 3)
    # an ear (filled, no face anywhere), top-right
    out += paper(f'<path d="M 72 -112 C 118 -112 122 -64 100 -50 C 88 -42 92 -24 76 -18 C 60 -12 50 -28 58 -40 '
                 f'C 34 -54 30 -112 72 -112 Z" fill="{C["sandLight"]}"/>'
                 f'<path d="M 70 -92 C 96 -92 98 -66 84 -58 C 76 -54 76 -44 70 -40" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".6" stroke-width="7" stroke-linecap="round"/>', tone, 2)
    return out


def icon_laundry(tone=T):
    """Note 2: a T-shirt pinned on a line; a small hand holds its hem."""
    out = paper(f'<path d="M -130 -88 Q 0 -66 130 -88" fill="none" stroke="{C["deep"]}" stroke-width="5"/>', tone, 1)
    shirt = (f'<path d="M -36 -80 L -82 -62 L -104 -18 L -70 -6 L -60 -28 L -60 66 L 60 66 L 60 -28 L 70 -6 L 104 -18 L 82 -62 L 36 -80 '
             f'Q 0 -56 -36 -80 Z" fill="{C["teal"]}"/>')
    out += paper(shirt, tone, 2)
    out += paper(f'<rect x="-48" y="-96" width="13" height="32" rx="4" fill="{C["gold"]}"/><rect x="35" y="-96" width="13" height="32" rx="4" fill="{C["gold"]}"/>', tone, 3)
    out += small_hand(6, 82, .55, rot=-90, tone=tone)
    return out


def icon_cloth(tone=T):
    """Note 3: a small hand on a teal cloth, wiping a gold table top."""
    out = paper(f'<rect x="-120" y="56" width="240" height="30" rx="6" fill="{C["gold"]}"/>'
                f'<rect x="-100" y="86" width="18" height="42" fill="{C["goldDeep"]}"/><rect x="82" y="86" width="18" height="42" fill="{C["goldDeep"]}"/>', tone, 1)
    for k, (y, x0, L) in enumerate(((22, -128, 42), (40, -118, 32))):
        out += torn_strip([(x0, y), (x0 + L, y)], 8, C['tealDeep'], tone, seed=230 + k, layer=1, core=False)
    out += paper(f'<path d="M -74 56 L -66 18 Q 0 6 64 18 L 72 56 Z" fill="{C["teal"]}"/>'
                 f'<path d="M -66 36 H 66" stroke="{C["tealDeep"]}" stroke-width="5"/>', tone, 2)
    out += small_hand(14, 14, .55, rot=180, tone=tone)
    return out


ICONS = [icon_vacuum, icon_laundry, icon_cloth]
ICON_T = ['translate(-6 0) scale(1.08)', 'translate(0 6) scale(1.1)', 'translate(0 -40) scale(1.22)']
SLOTS = [820, 540, 260]       # note 1 sits on the right (RTL), then the middle, then the left
ROTS = [3, -2, 4]
FILLS = ['pearl', 'sandLight', 'pearl']


def note(i, cx, cy, s=1.0, shown=False, tone=T):
    """Torn note pinned with a gold pin. Local note size 300x300; s scales it."""
    tr = f'translate({cx} {cy}) rotate({ROTS[i]}) scale({s})'
    lines = ''
    if not shown:   # blank: faint ruled lines only
        lines = ''.join(f'<rect x="-100" y="{-40 + k * 44}" width="{200 - (k == 2) * 70}" height="10" rx="5" fill="{C["tealDeep"]}" fill-opacity=".14"/>' for k in range(3))
    sheet = torn_rect(-150, -150, 300, 300, C[FILLS[i]], tone, 'tblr', seed=300 + i * 7, layer=2, inner=lines, T=tr)
    icon = ''
    if shown:
        icon = f'<g transform="{tr}"><g transform="{ICON_T[i]}">{ICONS[i](tone)}</g></g>'
    pin = paper(f'<circle cx="0" cy="-122" r="17" fill="{C["gold"]}"/><circle cx="-5" cy="-127" r="5" fill="{C["pearl"]}" fill-opacity=".7"/>', tone, 3, T=tr)
    return avoid(sheet + icon + pin, f'note{i + 1}')


def board(active=None, shown=(), big=1.6, ax=420, ay=900, sx=880, sys=(780, 1020), small=.55):
    """No active note: the three blank notes in a row. Otherwise the active note is
    big on the left and the other two wait small in a column on the right."""
    if active is None:
        return ''.join(note(k, SLOTS[k], ay, .9, k in shown) for k in range(3))
    out = ''
    others = [k for k in range(3) if k != active]
    for k, yy in zip(others, sys):
        out += note(k, sx, yy, small, k in shown)
    return out + note(active, ax, ay, big, True)


# ------------------------------------------------------------------ slides
def slide(ctx):
    s = ctx.s
    if ctx.last:
        keep_in(ctx.t.segs, 'فكري ايش اللي يصير معاه أكثر', 'وأنتي تشتغلي في البيت.', 'هذي التفاصيل', 'تساعدك تبني خطة تناسبه.')
        mini = ''.join(note(k, 640 + (2 - k) * 150, 1140 + (k % 2) * 34, .48, True) for k in (2, 1, 0))
        return cta_end(ctx, mini_art=mini, tag_y=900, tag_x=MX + 20)

    art, html = '', ''
    if s == 1:
        # everything paused: vacuum and pot greyed under the moon
        art = (moon(240, 730, 120)
               + avoid(vacuum(330, 1130, .52, pal=PAUSED), 'vacuum')
               + avoid(pot(790, 1110, .9, paused=True), 'pot'))
        html = hook_box(ctx, G, y=MT - 10, size=96, w=900,
                        keep=('ما تقدري تكنسي', 'وهو صاحي،', 'ولا تطبخي', 'إلا بعد ما ينام؟'))
    elif s == 2:
        # the moon over the heap of chores, now in full colour: all waiting
        art = (moon(880, 760, 80)
               + avoid(vacuum(300, 1120, .44) + basket(790, 1110, .78) + pot(560, 1040, .62), 'pile'))
        keep_in(ctx.t.segs, 'كل شي عندك صار', '"بسويه لما ينام".', 'ولما ينام،', 'تلقي كل شي ينتظرك،', 'وتحتاري تخلصيه', 'ولا ترتاحي.')
        html = body_box(ctx, G, y=MT + 20)
    elif s == 3:
        art = board(None, (), ay=960)
        keep_in(ctx.t.segs, 'قبل ما تدوري حل،', 'لاحظي ايش يصير معاه', 'أول ما تبدئي شغل البيت.', 'هذي ثلاث أشياء', 'ممكن تلاحظيها،', 'وكل وحدة لها خطوة.')
        html = body_box(ctx, G, y=MT + 20)
    elif s == 4:
        art = board(0, (0,), big=.95, ax=420, ay=1095, sys=(1010, 1170), small=.4)
        keep_in(ctx.t.segs, 'يغطي أذنه', 'أو يطلع من الغرفة', 'أول ما تشغلي المكنسة.', 'قولي له قبل ما تبدئي', '"بكنس غرفتين بس"،',
                'وكل ما خلصتي غرفة', 'قولي "خلصت وحدة".', 'عشان يعرف', 'إن الصوت له آخر.')
        html = body_box(ctx, G, y=MT + 115) + soft_cta(ctx, y=758)
    elif s == 5:
        art = board(1, (0, 1))
        keep_in(ctx.t.segs, 'يتعلق فيكي', 'ويسحبك من يدك.', 'خليه معاكي في نفس الشغلة.', 'يمسك الكيس وأنتي تكنسي،', 'أو يناولك الملابس', 'وأنتي تنشريها.')
        html = body_box(ctx, G, y=MT + 115)
    elif s == 6:
        art = board(2, (0, 1, 2))
        keep_in(ctx.t.segs, 'يبغى ياخذ المكنسة منك', 'ويكنس بنفسه.', 'اعطيه منشفه', 'يمسح فيها الطاوله جمبك،', 'هو له شغلته', 'وأنتي لك شغلتك.')
        html = body_box(ctx, G, y=MT + 115)
    return {'ground': G, 'art': art, 'html': html}
