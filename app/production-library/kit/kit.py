"""Home Orbit carousel kit: shared helpers for post modules.

Everything a post module needs lives here:
  * torn-paper geometry (torn_rect / torn_circle / torn_ring / torn_poly)
  * paper wrappers that apply the grain + shadow filters from paper.svg
  * the TEXT MODEL: slide text is never typed by hand. build.py cuts each
    slides_ar string into Segments and the module only *places* them.
  * components: step tab, progress dots, text blocks, conversion end, quiet end

Coordinates are px on the 1080x1350 canvas. Light comes from the top-right,
so shadows fall to the bottom-left (handled inside the filters).
"""
import html
import json
import math
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.abspath(os.path.join(HERE, '..', '..'))
TOKENS = json.load(open(os.path.join(APP, 'art_tokens.json'), encoding='utf-8'))

C = {**TOKENS['colors']['brand'], **TOKENS['colors']['derived']}
W, H = TOKENS['canvas']['w'], TOKENS['canvas']['h']
MX, MT, MB = TOKENS['spacing']['marginX'], TOKENS['spacing']['marginTop'], TOKENS['spacing']['marginBottom']

DARK_GROUNDS = set(TOKENS['colors']['grounds']['dark'])
# text colour allowed on each ground (first option = default)
TEXT_ON = {k: v.split('|')[0] for k, v in TOKENS['colors']['textOn'].items()}


def tone_of(ground):
    """'d' for dark grounds (deep/night), 'l' otherwise. Picks the shadow set."""
    return 'd' if ground in DARK_GROUNDS else 'l'


# --------------------------------------------------------------------------
# geometry
# --------------------------------------------------------------------------

def P(points):
    return ' '.join(f'{x:.1f},{y:.1f}' for x, y in points)


def _edge(rng, a, b, inward, torn, amp, step):
    """Points from a to b (a included, b excluded). inward = unit normal."""
    (ax, ay), (bx, by) = a, b
    L = math.hypot(bx - ax, by - ay)
    out = [a]
    if L < 1:
        return out
    ux, uy = (bx - ax) / L, (by - ay) / L
    t = 0.0
    flip = rng.random() < .5
    while True:
        t += rng.uniform(*step) if torn else rng.uniform(40, 80)
        if t >= L - 4:
            break
        if torn:
            # mostly alternate deep/shallow, but not always: real tears are irregular
            flip = (not flip) if rng.random() < .7 else flip
            d = rng.uniform(*amp) if flip else rng.uniform(0, amp[0] * .5)
        else:
            d = rng.uniform(-0.8, 0.8)
        out.append((ax + ux * t + inward[0] * d, ay + uy * t + inward[1] * d))
    return out


def torn_rect_pts(x, y, w, h, sides='tblr', seed=1, amp=None, step=None, grow=0):
    """Jagged rectangle. sides: which edges are torn (t,b,l,r); others are clean cuts.
    grow expands the rect (used for the pearl core underneath)."""
    te = TOKENS['paper']['tornEdge']
    amp = amp or tuple(te['amplitudePx'])
    step = step or tuple(te['stepPx'])
    rng = random.Random(seed)
    x, y, w, h = x - grow, y - grow, w + 2 * grow, h + 2 * grow
    tl, tr, br, bl = (x, y), (x + w, y), (x + w, y + h), (x, y + h)
    pts = []
    pts += _edge(rng, tl, tr, (0, 1), 't' in sides, amp, step)
    pts += _edge(rng, tr, br, (-1, 0), 'r' in sides, amp, step)
    pts += _edge(rng, br, bl, (0, -1), 'b' in sides, amp, step)
    pts += _edge(rng, bl, tl, (1, 0), 'l' in sides, amp, step)
    return pts


def torn_poly_pts(vertices, torn=None, seed=1, amp=None, step=None):
    """Jagged version of any polygon. torn = indices of edges to tear (edge i runs
    from vertex i to vertex i+1); None = all edges. Others get a clean cut."""
    te = TOKENS['paper']['tornEdge']
    amp = amp or tuple(te['amplitudePx'])
    step = step or tuple(te['stepPx'])
    rng = random.Random(seed)
    n = len(vertices)
    area = sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n))
    sgn = 1 if area > 0 else -1
    pts = []
    for i in range(n):
        a, b = vertices[i], vertices[(i + 1) % n]
        L = math.hypot(b[0] - a[0], b[1] - a[1]) or 1
        ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
        pts += _edge(rng, a, b, (-uy * sgn, ux * sgn), torn is None or i in torn, amp, step)
    return pts


def torn_poly(vertices, fill, tone, torn=None, seed=1, layer=1, core=True, amp=None, inner='', T='', extra=''):
    """A torn sheet of any shape (panels, seams, islands) with the pearl core."""
    core_svg = ''
    if core:
        # core: same outline pushed ~3px outward on torn edges (different seed = different teeth)
        cx = sum(v[0] for v in vertices) / len(vertices)
        cy = sum(v[1] for v in vertices) / len(vertices)
        grown = []
        for (x, y) in vertices:
            d = math.hypot(x - cx, y - cy) or 1
            grown.append((x + (x - cx) / d * 3, y + (y - cy) / d * 3))
        core_svg = f'<polygon points="{P(torn_poly_pts(grown, torn, seed + 101, amp))}" fill="{C["pearl"]}" fill-opacity="0.7"/>'
    body = f'<polygon points="{P(torn_poly_pts(vertices, torn, seed, amp))}" fill="{fill}"/>'
    return paper(core_svg + body + inner, tone, layer, 't', extra, T)


def torn_circle_pts(cx, cy, r, seed=1, amp=None, step=None):
    te = TOKENS['paper']['tornEdge']
    amp = amp or tuple(te['amplitudePx'])
    step = step or tuple(te['stepPx'])
    rng = random.Random(seed)
    pts, a, flip = [], 0.0, False
    circ = 2 * math.pi * r
    while a < 2 * math.pi - 1e-6:
        flip = (not flip) if rng.random() < .7 else flip
        d = rng.uniform(*amp) if flip else rng.uniform(0, amp[0] * .5)
        rr = r - d
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
        a += rng.uniform(*step) / circ * 2 * math.pi
    return pts


def torn_line_pts(points, width, seed=1, amp=(3, 7), step=(10, 18)):
    """A torn strip of paper following a polyline (e.g. a path or seam)."""
    rng = random.Random(seed)
    left, right = [], []
    for i, (x, y) in enumerate(points):
        if i < len(points) - 1:
            nx, ny = points[i + 1]
        else:
            nx, ny = x + (x - points[i - 1][0]), y + (y - points[i - 1][1])
        L = math.hypot(nx - x, ny - y) or 1
        ox, oy = -(ny - y) / L, (nx - x) / L
        # irregular teeth: mostly small bites, now and then a deep one
        a1 = rng.uniform(*amp) if rng.random() < .45 else rng.uniform(0, amp[0])
        a2 = rng.uniform(*amp) if rng.random() < .45 else rng.uniform(0, amp[0])
        left.append((x + ox * (width / 2 - a1), y + oy * (width / 2 - a1)))
        right.append((x - ox * (width / 2 - a2), y - oy * (width / 2 - a2)))
    return left + right[::-1]


def resample(points, step=14):
    """Densify a polyline so torn strips have teeth every ~step px."""
    out = []
    for (ax, ay), (bx, by) in zip(points, points[1:]):
        L = math.hypot(bx - ax, by - ay)
        n = max(1, int(L / step))
        for k in range(n):
            out.append((ax + (bx - ax) * k / n, ay + (by - ay) * k / n))
    out.append(points[-1])
    return out


def arc_pts(cx, cy, r, a0, a1, n=40):
    """Points along a circular arc, angles in degrees (0 = east, 90 = south)."""
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


# --------------------------------------------------------------------------
# paper wrappers (filters live in paper.svg)
# --------------------------------------------------------------------------

def paper(inner, tone, layer=1, kind='c', extra='', T=''):
    """Wrap SVG shapes as one sheet of paper. kind: c = cut edge, t = torn (no displacement).
    T = an SVG transform applied to the shapes *inside* the filter, so a scaled-down
    motif keeps full-size grain, edges and shadows."""
    if T:
        inner = f'<g transform="{T}">{inner}</g>'
    return f'<g filter="url(#p{kind}-{tone}{layer})" {extra}>{inner}</g>'


def torn_rect(x, y, w, h, fill, tone, sides='tblr', seed=1, layer=1, rot=0, core=True,
              amp=None, step=None, extra='', inner='', T=''):
    """A torn sheet with the pearl core showing at the torn edges (tokens: core 3px @70%).
    `inner` = extra SVG drawn on the sheet (inside the same paper filter)."""
    cx, cy = x + w / 2, y + h / 2
    tf = f'transform="rotate({rot} {cx:.1f} {cy:.1f})"' if rot else ''
    core_svg = ''
    if core:
        core_svg = (f'<polygon points="{P(torn_rect_pts(x, y, w, h, sides, seed + 101, amp, step, grow=3))}" '
                    f'fill="{C["pearl"]}" fill-opacity="0.7"/>')
    body = f'<polygon points="{P(torn_rect_pts(x, y, w, h, sides, seed, amp, step))}" fill="{fill}"/>'
    if T:
        return paper(f'<g {tf}>' + core_svg + body + inner + '</g>', tone, layer, 't', extra, T)
    return f'<g {tf} {extra}>' + paper(core_svg + body + inner, tone, layer, 't') + '</g>'


def torn_circle(cx, cy, r, fill, tone, seed=1, layer=1, core=True, amp=None, inner='', T=''):
    core_svg = (f'<polygon points="{P(torn_circle_pts(cx, cy, r + 3, seed + 101, amp))}" fill="{C["pearl"]}" fill-opacity="0.7"/>'
                if core else '')
    body = f'<polygon points="{P(torn_circle_pts(cx, cy, r, seed, amp))}" fill="{fill}"/>'
    return paper(core_svg + body + inner, tone, layer, 't', T=T)


def torn_ring(cx, cy, r_out, r_in, fill, tone, seed=1, layer=1, amp=(4, 9), T=''):
    """A torn ring (outer and inner edges torn), with the pearl core on both edges."""
    o = torn_circle_pts(cx, cy, r_out, seed, amp)
    i = torn_circle_pts(cx, cy, r_in, seed + 7, amp)[::-1]
    oc = torn_circle_pts(cx, cy, r_out + 3, seed + 31, amp)
    ic = torn_circle_pts(cx, cy, r_in - 3, seed + 37, amp)[::-1]
    d = lambda pts: 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + 'Z'
    core_svg = f'<path d="{d(oc)} {d(ic)}" fill="{C["pearl"]}" fill-opacity="0.7" fill-rule="evenodd"/>'
    body = f'<path d="{d(o)} {d(i)}" fill="{fill}" fill-rule="evenodd"/>'
    return paper(core_svg + body, tone, layer, 't', T=T)


def torn_strip(points, width, fill, tone, seed=1, layer=1, core=True, T=''):
    pts = resample(points, 14)
    core_svg = (f'<polygon points="{P(torn_line_pts(pts, width + 6, seed + 101))}" fill="{C["pearl"]}" fill-opacity="0.7"/>'
                if core else '')
    body = f'<polygon points="{P(torn_line_pts(pts, width, seed))}" fill="{fill}"/>'
    return paper(core_svg + body, tone, layer, 't', T=T)


def glow(shape, strength='l'):
    """Soft light: wrap a shape (usually teal / pearl / gold) in a blur. 's' = tight, 'l' = wide."""
    return f'<g filter="url(#glow-{strength})">{shape}</g>'


def ground_rect(ground, x=0, y=0, w=W, h=H, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C[ground]}" filter="url(#pg)" {extra}/>'


def avoid(inner, name='motif'):
    """Mark an art group as 'text must not cross this'. render.js checks it."""
    return f'<g data-avoid="{name}">{inner}</g>'


# --------------------------------------------------------------------------
# TEXT MODEL
# --------------------------------------------------------------------------
# A Segment is one run of the original slide string. sep = the exact characters
# of the original that sit *before* it and are not drawn (a "\n", a space, or "").
# Concatenating sep+text over every segment of every output slide that came from
# slide i gives slides_ar[i] back, character for character. render.js checks that
# from the rendered DOM.

class Seg:
    def __init__(self, text, role, sep, order):
        self.text, self.role, self.sep, self.order = text, role, sep, order
        self.keep = []      # substrings that must not break across lines (see keep())

    def __repr__(self):
        return f'Seg({self.role}:{self.text!r} sep={self.sep!r})'


SEP_CODE = {'': 'none', ' ': 'sp', '\n': 'nl'}

LABEL_RE = re.compile(r'^([^:.\n؟،"«]{2,24}:) ')


class SlideText:
    """Text for one OUTPUT slide. Built by build.py, consumed by post modules."""

    def __init__(self, src, part, raw, first_sep, order0, kind):
        self.src, self.part, self.raw, self.kind = src, part, raw, kind
        self.segs = []
        o = order0
        lines = raw.split('\n')
        sep = first_sep
        for li, line in enumerate(lines):
            if li == 0 and kind == 'body':
                m = LABEL_RE.match(line)
                if m:
                    self.segs.append(Seg(m.group(1), 'label', sep, o)); o += 1
                    line, sep = line[m.end():], ' '
            role = ('hook' if kind == 'hook' else
                    'lead' if (li == 0 and part in (0, 1)) else 'support')
            self.segs.append(Seg(line, role, sep, o)); o += 1
            sep = '\n'
        self.next_order = o

    # convenience accessors -------------------------------------------------
    def label(self):
        return next((s for s in self.segs if s.role == 'label'), None)

    def body(self):
        return [s for s in self.segs if s.role != 'label']

    def split_seg(self, seg, at):
        """Cut one segment in two at the first occurrence of `at` (e.g. '؟ ').
        The characters of `at` that are spaces become the separator; the rest
        stay on the first piece. Returns (first, second)."""
        i = seg.text.index(at)
        keep = at.rstrip(' ')
        sep = at[len(keep):]
        a = Seg(seg.text[:i] + keep, seg.role, seg.sep, seg.order)
        b = Seg(seg.text[i + len(at):], seg.role, sep, seg.order + 0.5)
        k = self.segs.index(seg)
        self.segs[k:k + 1] = [a, b]
        return a, b

    def take_last(self):
        """Pop the last segment (used to move the CTA line onto the tag)."""
        return self.segs.pop()


def keep(seg, *phrases):
    """Line-break control without touching the words: each phrase (an exact
    substring of the segment) is wrapped in a no-wrap span, so lines can only
    break between phrases. Use it to break at commas / phrase boundaries and to
    keep construct pairs, a preposition with its noun, or a quote together."""
    for p in phrases:
        if p not in seg.text:
            raise ValueError(f'keep(): {p!r} is not in {seg.text!r}')
    seg.keep = list(phrases)
    return seg


def keep_in(segs, *phrases):
    """keep() for a whole slide: each phrase is attached to the segment that contains it."""
    for p in phrases:
        for s in segs:
            if p in s.text:
                s.keep.append(p)
                break
        else:
            raise ValueError(f'keep_in(): {p!r} not found in this slide')
    return segs


def seg_html(seg, cls=None, tag='div'):
    cls = cls or seg.role
    body = html.escape(seg.text, quote=False)
    for p in seg.keep:
        e = html.escape(p, quote=False)
        body = body.replace(e, f'<span class="nb">{e}</span>', 1)
    return (f'<{tag} class="{cls}" data-seg data-ord="{seg.order}" data-sep="{SEP_CODE[seg.sep]}">'
            f'{body}</{tag}>')


def text_box(segs, x, y, w, color='pearl', align='right', cls='', style='', size=None, h=None):
    """Absolute text box. x,y = top-left in canvas px; text is right-aligned in RTL.
    size: dict role->px to override token sizes (e.g. amber slides)."""
    inner = ''
    for s in segs:
        st = f' style="font-size:{size[s.role]}px"' if size and s.role in size else ''
        inner += seg_html(s).replace(' data-seg', st + ' data-seg', 1)
    hh = f'height:{h}px;' if h else ''
    return (f'<div class="tx c-{color} {cls}" style="left:{x}px;top:{y}px;width:{w}px;{hh}'
            f'text-align:{align};{style}">{inner}</div>')


# --------------------------------------------------------------------------
# components
# --------------------------------------------------------------------------

def step_tab(seg, top=MT, right=MX, seed=3):
    """Torn gold strip, top-right, -2deg, ink label. Label = the slide's own prefix."""
    return (f'<div class="step-tab torn" data-fill="{C["gold"]}" data-seed="{seed}" data-sides="lr" '
            f'style="top:{top}px;right:{right}px">{seg_html(seg, "label", "span")}</div>')


def dots(n, i, theme):
    """Progress dots, RTL (first slide = rightmost). i is 1-based. None on slide 1."""
    if i == 1:
        return ''
    ds = ''.join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(1, n + 1))
    return f'<div class="dots dots-{theme}">{ds}</div>'


def conversion_tag(seg, x, y, rot=-3, seed=9):
    """Pearl torn tag with a punched hole and a deep string, holding the CTA line."""
    return (f'<div class="cta-tag torn" data-fill="{C["pearl"]}" data-seed="{seed}" data-sides="tblr" '
            f'data-hole="1" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)">'
            f'{seg_html(seg, "tag", "span")}</div>')


def mini(svg_inner, scale=0.25, x=0, y=0):
    """Re-use a full-canvas motif at small scale (conversion end: 25% bottom-left)."""
    return f'<g transform="translate({x} {y}) scale({scale})">{svg_inner}</g>'
