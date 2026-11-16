"""Batch 2 shared slide helpers (hook, body, soft CTA, CTA end).

Every post module can use these so the batch shares one type system:
    from common import hook_box, body_box, soft_cta, cta_end, ink_or_pearl
"""
from kit import C, MX, MT, W, H, text_box, step_tab, soft_tag, conversion_tag, brk, keep_in, TEXT_ON

DARK = {'deep', 'night'}


def ink_or_pearl(ground):
    return 'pearl' if ground in DARK else 'ink'


def hook_box(ctx, ground, y=MT, size=96, w=888, x=None, align='right', breaks=(), keep=()):
    """Slide-1 hook: El Messiri, top-right. breaks = substrings to break after
    (e.g. '؟ '); commas are handled by the kit (no line ends with a comma)."""
    h = ctx.t.body()[0]
    if breaks:
        brk(h, *breaks)
    if keep:
        keep_in([h], *keep)
    x = (W - MX - w) if x is None else x
    return text_box([h], x, y, w, ink_or_pearl(ground), align=align, size={'hook': size})


def body_box(ctx, ground, y=None, w=888, x=None, align='right', size=None):
    """Step tab (if the slide has a label) + body text. Long (amber) slides are
    already set at 50px by base.css."""
    out = ''
    lab = ctx.t.label()
    top = y if y is not None else (MT + 110 if lab else MT + 20)
    if lab:
        out += step_tab(lab)
    x = (W - MX - w) if x is None else x
    out += text_box(ctx.t.body(), x, top, w, ink_or_pearl(ground), align=align, size=size)
    return out


def soft_cta(ctx, y=None, x=None, w=None):
    """The early soft CTA line, on a small torn gold strip (ink text)."""
    s = ctx.t.soft()
    if not s:
        return ''
    return soft_tag(s, y=y, x=x, w=w, color='ink', fill=C['gold'])


def cta_end(ctx, mini_art='', y=MT + 20, tag_y=None, tag_x=None, w=888):
    """Last slide: gold ground, ink text, the final «الرابط في البايو.» line on the
    pearl torn tag. mini_art = the post's motif drawn small in a corner (SVG)."""
    segs = ctx.t.body()
    last = segs[-1]
    want = ctx.cta_text()
    if last.text != want:
        # the CTA sentence sits at the end of the last line: cut it off
        for sep in ('. ', '، '):
            if last.text.endswith(sep + want):
                a, b = ctx.t.rsplit_seg(last, sep)
                last = b
                break
    assert last.text == want, (last.text, want)
    body = [s for s in ctx.t.body() if s is not last]
    html = text_box(body, W - MX - w, y, w, 'ink')
    tx = tag_x if tag_x is not None else W - MX - 520
    ty = tag_y if tag_y is not None else 900
    html += conversion_tag(last, tx, ty)
    return {'ground': 'gold', 'art': mini_art, 'html': html}
