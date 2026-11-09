"""p9 name. TealMist ground, light. Scale contrast.

Motif: a giant deep fridge with its lower door ajar on the left: a lit pearl
interior with shelves, a night inner door face with tealMist bins, and a pearl
glow wedge spilling across a sandLight kitchen floor. Against it, a tiny empty
pearl speech bubble on the right: the mother's voice.
s1 (red flag) is split at «يلتفت؟»: s1a the question at 92px in ink with the
    fridge cropped huge (it does not fit in the frame) and the bubble tiny;
    s1b the second sentence; the fridge steps back, the bubble grows.
Inner slides: the bubble grows 120 > 420px while the fridge recedes into the
    corner. s4 a gold biscuit sits in the bubble; s5 the bubble comes down to
    floor level; s6 four marks in the bubble, one lifted in gold; s7 (hearing
    check) plain teal sound arcs, nothing medical.
s8 conversion end: gold ground, pearl tag = «التقييم المجاني في البايو يمر عليها كلها.»
"""
from kit import (C, MX, MT, W, H, paper, torn_rect, torn_poly, glow, text_box, step_tab,
                 avoid, keep, keep_in, conversion_tag)

GROUND = 'tealMist'
TONE = 'l'
FLOOR_Y = 1196          # top of the sandLight floor band


# ---------------------------------------------------------------- motifs
def fridge(tx, ty, s, glow_on=True, seed=0, wedge_op=.5, magnets=False):
    """Fridge in local coords: cabinet 520 x 1000 with its top-left at (0,0); the
    lower door is swung open towards the viewer on the right (to x = 700).
    Drawn at translate(tx,ty) scale(s); filters stay outside the transform."""
    T = f'translate({tx} {ty}) scale({s})'
    o, g = [], ''
    if glow_on:
        # pearl light wedge spilling from the open door across the floor
        wedge = (f'<polygon points="470,600 700,560 1250,1240 260,1240" fill="{C["pearl"]}" fill-opacity="{wedge_op}" '
                 f'transform="{T}"/>')
        g += glow(wedge, 'l')
        g += (glow(f'<rect x="40" y="380" width="440" height="590" rx="10" fill="{C["pearl"]}" fill-opacity=".9" transform="{T}"/>', 's'))
    # cabinet (night shell)
    o.append(paper(f'<rect x="0" y="0" width="520" height="1000" rx="34" fill="{C["night"]}"/>', TONE, 1, T=T))
    # freezer door, closed: deep, with a gold bar handle
    o.append(paper(f'<rect x="14" y="14" width="492" height="338" rx="24" fill="{C["deep"]}"/>'
                   f'<rect x="420" y="190" width="30" height="132" rx="15" fill="{C["gold"]}"/>', TONE, 2, T=T))
    if magnets:
        # fridge magnets on the freezer door: a pinned pearl note, a teal disc, a gold star
        star = ' '.join(f'{300 + (34 if k % 2 == 0 else 15) * __import__("math").cos(__import__("math").pi * k / 5 - 1.5708):.1f},'
                        f'{250 + (34 if k % 2 == 0 else 15) * __import__("math").sin(__import__("math").pi * k / 5 - 1.5708):.1f}' for k in range(10))
        o.append(paper(f'<rect x="70" y="80" width="150" height="120" rx="4" fill="{C["pearl"]}" transform="rotate(-6 145 140)"/>'
                       f'<path d="M 92 160 q 26 -36 52 0 t 52 0" fill="none" stroke="{C["teal"]}" stroke-width="8" stroke-linecap="round" transform="rotate(-6 145 140)"/>'
                       f'<circle cx="140" cy="88" r="16" fill="{C["gold"]}"/>'
                       f'<circle cx="300" cy="120" r="28" fill="{C["teal"]}"/>'
                       f'<polygon points="{star}" fill="{C["gold"]}"/>', TONE, 3, T=T))
    # lit interior with three shelves and a few flat paper things on them
    shelves = ''.join(f'<rect x="40" y="{y}" width="440" height="14" fill="{C["tealMist"]}"/>' for y in (540, 700, 850))
    items = (f'<rect x="80" y="440" width="70" height="100" rx="12" fill="{C["gold"]}"/>'
             f'<rect x="92" y="426" width="46" height="22" rx="6" fill="{C["goldDeep"]}"/>'
             f'<rect x="190" y="470" width="120" height="70" rx="8" fill="{C["sandLight"]}"/>'
             f'<rect x="360" y="410" width="44" height="130" rx="16" fill="{C["teal"]}"/>'
             f'<circle cx="130" cy="660" r="40" fill="{C["teal"]}"/>'
             f'<circle cx="230" cy="666" r="34" fill="{C["gold"]}"/>'
             f'<rect x="300" y="610" width="140" height="90" rx="10" fill="{C["deep"]}"/>'
             f'<rect x="100" y="790" width="160" height="60" rx="30" fill="{C["sandLight"]}"/>'
             f'<rect x="330" y="760" width="56" height="90" rx="10" fill="{C["gold"]}"/>')
    o.append(paper(f'<rect x="40" y="380" width="440" height="590" rx="10" fill="{C["pearl"]}"/>' + shelves + items, TONE, 1, T=T))
    # open door leaf seen from inside (night) with tealMist bins and a deep rim
    leaf = (f'<polygon points="520,372 720,318 720,1048 520,1000" fill="{C["deep"]}"/>'
            f'<polygon points="540,392 700,350 700,1022 540,982" fill="{C["night"]}"/>')
    bins = ''.join(f'<polygon points="548,{y} 692,{y - 34} 692,{y + 16} 548,{y + 46}" fill="{C["tealMist"]}"/>'
                   for y in (560, 740, 910))
    bottles = (f'<rect x="572" y="470" width="30" height="92" rx="10" fill="{C["gold"]}" transform="skewY(-13) translate(0 140)"/>'
               f'<rect x="630" y="660" width="40" height="64" rx="8" fill="{C["teal"]}" transform="skewY(-13) translate(0 150)"/>')
    door = paper(leaf + bins + bottles, TONE, 2, T=T)
    # two avoid zones (cabinet, door leaf) so an L-shaped layout is checked honestly
    return g + avoid(''.join(o), 'fridge') + avoid(door, 'fridge door')


def bubble(cx, cy, w, inner='', seed=0, tail='left'):
    """Empty pearl speech bubble (cut paper), width w; tail drops to the bottom-left."""
    rx, ry = w / 2, w * .38
    if tail == 'left':
        t = (f'<polygon points="{cx - rx * .42:.1f},{cy + ry * .7:.1f} {cx - rx * .78:.1f},{cy + ry * 1.38:.1f} '
             f'{cx - rx * .05:.1f},{cy + ry * .92:.1f}" fill="{C["pearl"]}"/>')
    else:   # straight down (s5: at his level)
        t = (f'<polygon points="{cx - rx * .3:.1f},{cy + ry * .8:.1f} {cx - rx * .2:.1f},{cy + ry * 1.42:.1f} '
             f'{cx + rx * .12:.1f},{cy + ry * .9:.1f}" fill="{C["pearl"]}"/>')
    body = f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{C["pearl"]}"/>' + t
    return avoid(paper(body, TONE, 2) + inner, 'bubble')


def biscuit(cx, cy, r):
    dots = ''.join(f'<circle cx="{cx + dx * r:.1f}" cy="{cy + dy * r:.1f}" r="{r * .09:.1f}" fill="{C["goldDeep"]}"/>'
                   for dx, dy in ((-.42, -.4), (.4, -.38), (-.44, .38), (.42, .4), (0, 0), (0, -.62), (0, .62), (-.62, 0), (.62, 0)))
    rim = f'<circle cx="{cx}" cy="{cy}" r="{r * .82:.1f}" fill="none" stroke="{C["goldDeep"]}" stroke-opacity=".4" stroke-width="{r * .05:.1f}" stroke-dasharray="{r * .1:.1f} {r * .12:.1f}"/>'
    return paper(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["gold"]}"/>{rim}{dots}', TONE, 3)


def sound_arcs(cx, cy, r0, n=3):
    """Plain teal paper arcs, opening to the left: a voice travelling. Nothing medical."""
    out = ''
    for k in range(n):
        r = r0 + k * r0 * .62
        sw = r0 * .2
        out += (f'<path d="M {cx - r * .5:.1f} {cy - r * .866:.1f} A {r:.1f} {r:.1f} 0 0 0 {cx - r * .5:.1f} {cy + r * .866:.1f}" '
                f'fill="none" stroke="{C["teal"] if k != 1 else C["deep"]}" stroke-width="{sw:.1f}" stroke-linecap="round"/>')
    return paper(out, TONE, 3)


def four_marks(cx, cy, w):
    """Four small deep paper dots in the bubble; the one he turned to is lifted, bigger, in gold."""
    out = ''
    gap = w * .17
    xs = [cx + gap * 1.5, cx + gap * .5, cx - gap * .5, cx - gap * 1.5]    # RTL: first on the right
    for k, x in enumerate(xs):
        if k == 2:
            continue
        out += paper(f'<circle cx="{x:.1f}" cy="{cy}" r="{w * .045:.1f}" fill="{C["deep"]}"/>', TONE, 3)
    out += paper(f'<circle cx="{xs[2]:.1f}" cy="{cy - w * .02:.1f}" r="{w * .075:.1f}" fill="{C["gold"]}"/>', TONE, 3)
    return out


def floor():
    return torn_poly([(-30, FLOOR_Y + 8), (1110, FLOOR_Y - 8), (1110, 1380), (-30, 1380)],
                     C['sandLight'], TONE, torn=[0], seed=29)


# ---------------------------------------------------------------- slides
BREAKS = {
    (1, 1): ['يسمع باب الثلاجة', 'من آخر البيت،', 'ولما تناديه باسمه', 'ما يلتفت؟'],
    (1, 2): ['جربي هذي الأربع خطوات،', 'وراح تبدئي تكتشفي', 'ايش اللي يخليه يلتفت لك.'],
    2: ['ناديه من قدامه،', 'مو من وراه.', 'خليه يشوفك', 'وأنتي تقولي اسمه.'],
    3: ['ناديه وهو فاضي.', 'لما يكون مندمج في لعبة', 'أو قدام الشاشة،', 'طبيعي ما ينتبه.'],
    4: ['قولي اسمه،', 'وبعده على طول شي يحبه.', '"فهد، بسكوت!"', 'والبسكوتة في يدك يشوفها.'],
    5: ['لا تناديه من آخر الصالة.', 'قربي منه،', 'وانزلي لطوله،', 'وعينك في عينه.'],
    6: ['ولاحظي مع أي وحدة فيهم', 'يلتفت لك أكثر.', 'هذي اللي تبدئي منها.'],
    7: ['وإذا ما فحصتوا سمعه قبل،', 'فحص السمع', 'خطوة بسيطة وتستاهل.'],
    8: ['الاسم جزء من تواصله،', 'والتواصل واحد من ستة جوانب في يومه.',
        'التقييم المجاني في البايو', 'يمر عليها كلها.'],
}

# fridge scale / bubble width per source slide (the bubble grows, the fridge recedes)
STEP = {2: (.66, 190), 3: (.58, 240), 4: (.5, 290), 5: (.44, 310), 6: (.38, 380), 7: (.32, 420)}


def body(ctx, top=None, w=W - 2 * MX):
    html = ''
    if ctx.t.label():
        html += step_tab(ctx.t.label())
    top = top or (MT + 118 if ctx.t.label() else MT + 30)
    return html + text_box(ctx.t.body(), W - MX - w, top, w, 'ink')


def scene(fs, bw, by=840, inner_fn=None, tail='left'):
    """Fridge at scale fs standing on the floor at the left; bubble of width bw on the right."""
    fx = 40 - (1 - fs) * 30
    art = floor() + fridge(fx, FLOOR_Y + 8 - 1000 * fs, fs)
    bx = W - MX - bw / 2 - 10
    inner = inner_fn(bx, by, bw) if inner_fn else ''
    return art + bubble(bx, by, bw, inner, tail=tail)


def slide(ctx):
    s, part = ctx.s, ctx.part
    key = (s, part) if (s, part) in BREAKS else s
    if key in BREAKS:
        keep_in(ctx.t.segs, *BREAKS[key])
    r = {'ground': GROUND}

    if s == 1 and part == 1:
        # the question, 92px ink; the fridge is too big for the frame, the bubble is tiny
        # the fridge towers from the top of the frame to past the floor in a left column
        # widened crop (QA): the whole fridge face, freezer handle, magnets, open door with
        # lit shelves and bins and the light spill, too big to fit: it runs off the bottom
        art = (fridge(150, 668, .92, wedge_op=.6, magnets=True)
               + bubble(960, 1170, 112))
        r.update(art=art, html=text_box(ctx.t.body(), MX, MT, W - 2 * MX, 'ink', size={'hook': 92}))

    elif s == 1 and part == 2:
        # the second sentence on its own slide: the fridge steps back, the bubble is noticed
        for g in ctx.t.body():
            g.role = 'quiet'
        art = floor() + fridge(30, FLOOR_Y + 8 - 1000 * .7, .7) + bubble(W - MX - 85, 960, 150)
        r.update(art=art, html=text_box(ctx.t.body(), MX, MT + 10, W - 2 * MX, 'ink'))

    elif s in STEP:
        fs, bw = STEP[s]
        if s == 4:
            r.update(art=scene(fs, bw, 830, lambda x, y, w: biscuit(x + w * .02, y - w * .02, w * .2)), html=body(ctx))
        elif s == 5:
            # get down to his level: the bubble comes down close to the floor
            r.update(art=scene(fs, bw, FLOOR_Y - 190, tail='down'), html=body(ctx))
        elif s == 6:
            r.update(art=scene(fs, bw, 820, four_marks), html=body(ctx, top=MT + 30))
        elif s == 7:
            r.update(art=scene(fs, bw, 820, lambda x, y, w: sound_arcs(x + w * .2, y, w * .14)), html=body(ctx, top=MT + 40))
        else:
            r.update(art=scene(fs, bw), html=body(ctx))

    else:
        # conversion end: gold ground, ink text, pearl tag with the CTA, mini motif bottom-left
        segs = ctx.t.body()
        cta = segs[-1]
        assert cta.text == ctx.cta_text(), (cta.text, ctx.cta_text())
        mini = (fridge(120, 1240 - 250, .25, glow_on=True)
                + bubble(330, 1080, 110))
        tag_css = ('.cta-tag{width:600px}.cta-tag .tag{white-space:normal;display:block}')
        html = (text_box(segs[:-1], MX, 250, W - 2 * MX, 'ink')
                + conversion_tag(cta, 330, 640, rot=-3))
        r.update(ground='gold', art=mini, html=html, dots_theme='gold', css=tag_css)
    return r
