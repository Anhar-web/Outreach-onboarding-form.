#!/usr/bin/env python3
"""Build carousel slide HTML from posts_draft.json + a per-post module.

    python3 build.py p5 p7 p2        # build these posts
    python3 build.py --all           # every post that has a module in posts/

Output: app/output/<postId>/slide-N.html + manifest.json. Then run render.js.

The slide text is NEVER typed in a module. build.py cuts each slides_ar string
into Segments (kit.SlideText) and hands them to the module, which only places
them. After the module returns, build.py asserts every segment of the slide was
placed exactly once, so nothing can be dropped or duplicated.

Long-slide rule (art_tokens.anharOverrides.longSlides): slides listed in
fitFlags.red are split into two output slides at the "\n" nearest the middle
(or, with no "\n", the full stop nearest the middle). Same words, in order.
Amber slides stay single; ctx.amber is True so the module sets body at
bodySupport size (base.css .amber).
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit  # noqa: E402

APP = kit.APP
OUT = os.path.join(APP, 'output')
POSTS_DIR = os.path.join(HERE, 'posts')
PAPER_DEFS = open(os.path.join(HERE, 'paper.svg'), encoding='utf-8').read()
REL_KIT = '../../production-library/kit'


def load_posts():
    return {p['id']: p for p in json.load(open(os.path.join(APP, 'posts_draft.json'), encoding='utf-8'))}


def split_point(s):
    """Return (index, sep) where the slide string should be cut in two."""
    mid = len(s) / 2
    nl = [m.start() for m in re.finditer('\n', s)]
    if nl:
        i = min(nl, key=lambda k: abs(k - mid))
        return i, '\n'
    stops = [m.start() + 1 for m in re.finditer(r'[.؟?!] ', s)]
    if not stops:
        raise ValueError(f'cannot split slide (no "\\n" and no full stop): {s!r}')
    i = min(stops, key=lambda k: abs(k - mid))
    return i, ' '


class Ctx:
    """What a module's slide() receives."""

    def __init__(self, post, meta, text, i, n):
        self.post, self.post_id = post, post['id']
        self.t = text                    # kit.SlideText
        self.i, self.n = i, n            # 1-based output index, total output slides
        self.src, self.part = text.src, text.part   # 0-based source slide, 0 = not split, 1/2 = halves
        self.s = text.src + 1            # 1-based SOURCE slide number (matches the spec's s1..sN)
        self.amber = meta['amber']
        self.red = meta['red']
        self.first, self.last = i == 1, i == n
        self.tokens = kit.TOKENS
        self.spec = kit.TOKENS['posts'].get(post['id'], {})

    def cta_text(self):
        return kit.TOKENS['components']['conversionEnd']['tagText'].get(self.post_id)


def plan_slides(post):
    pid = post['id']
    red = {int(k.split('.s')[1]) - 1 for k in kit.TOKENS['fitFlags']['red'] if k.startswith(pid + '.')}
    amber = {int(k.split('.s')[1]) - 1 for k in kit.TOKENS['fitFlags']['amber'] if k.startswith(pid + '.')}
    out, order = [], 0
    for si, s in enumerate(post['slides_ar']):
        kind = 'hook' if si == 0 else 'body'
        if si in red:
            k, sep = split_point(s)
            a = kit.SlideText(si, 1, s[:k], '', order, kind); order = a.next_order
            b = kit.SlideText(si, 2, s[k + len(sep):], sep, order, kind); order = b.next_order
            out += [(a, {'amber': False, 'red': True}), (b, {'amber': False, 'red': True})]
        else:
            t = kit.SlideText(si, 0, s, '', order, kind); order = t.next_order
            out.append((t, {'amber': si in amber, 'red': False}))
    return out


PAGE = '''<!doctype html>
<html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=1080">
<title>{pid} slide {i}</title>
<link rel="stylesheet" href="{kit}/base.css">
{css}
</head><body>
<div class="slide g-{ground}{amber}" data-post="{pid}" data-slide="{i}" data-src="{src}" data-part="{part}" data-tone="{tone}">
{defs}
<svg class="art" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
{ground_rect}
{art}
</svg>
{html}
{dots}
</div>
<script src="{kit}/kit.js"></script>
</body></html>
'''


def build_post(post, mod):
    pid = post['id']
    slides = plan_slides(post)
    n = len(slides)
    d = os.path.join(OUT, pid)
    os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        if re.match(r'slide-\d+\.(html|png)$', f):
            os.remove(os.path.join(d, f))
    manifest = {'post': pid, 'slides': []}
    for i, (text, meta) in enumerate(slides, 1):
        ctx = Ctx(post, meta, text, i, n)
        r = mod.slide(ctx)
        ground = r['ground']
        tone = kit.tone_of(ground)
        theme = r.get('dots_theme') or ('gold' if ground == 'gold' else 'dark' if tone == 'd' else 'light')
        body = r['html']
        # every segment placed exactly once
        for sg in text.segs:
            cnt = body.count(f'data-ord="{sg.order}"')
            if cnt != 1:
                raise SystemExit(f'{pid} slide {i}: segment {sg!r} placed {cnt} times (must be 1)')
        page = PAGE.format(
            pid=pid, i=i, kit=REL_KIT, ground=ground, tone=tone,
            amber=' amber' if meta['amber'] else '',
            src=text.src, part=text.part, defs=PAPER_DEFS,
            ground_rect=r.get('ground_svg', kit.ground_rect(ground)),
            art=r.get('art', ''), html=body,
            dots='' if r.get('dots') is False else kit.dots(n, i, theme),
            css=f'<style>{r["css"]}</style>' if r.get('css') else '')
        fn = f'slide-{i}.html'
        open(os.path.join(d, fn), 'w', encoding='utf-8').write(page)
        manifest['slides'].append({'file': fn, 'src': text.src, 'part': text.part,
                                   'amber': meta['amber'], 'red': meta['red'], 'ground': ground})
    json.dump(manifest, open(os.path.join(d, 'manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{pid}: {n} slides -> {d}')


def load_module(pid):
    path = os.path.join(POSTS_DIR, f'{pid}.py')
    spec = importlib.util.spec_from_file_location(f'post_{pid}', path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(argv):
    posts = load_posts()
    if not argv or argv == ['--all']:
        ids = sorted(f[:-3] for f in os.listdir(POSTS_DIR) if re.match(r'p\d+\.py$', f))
    else:
        ids = argv
    for pid in ids:
        if pid not in posts:
            raise SystemExit(f'unknown post {pid}')
        build_post(posts[pid], load_module(pid))


if __name__ == '__main__':
    main(sys.argv[1:])
