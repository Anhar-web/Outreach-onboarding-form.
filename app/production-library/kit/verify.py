#!/usr/bin/env python3
"""Browser-free verbatim check: parse app/output/<id>/slide-N.html, pull every
[data-seg] element's text, re-join (with each segment's recorded separator, across
split slides) and compare with posts_draft.json slides_ar character for character.

    python3 verify.py p5 p7 p2     (no args = every built post)

render.js runs the same check on the rendered DOM; this one needs no Chromium.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(APP, 'output')
SEP = {'none': '', 'sp': ' ', 'nl': '\n'}


class Segs(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.segs = [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'data-seg' in a:
            self.segs.append({'ord': float(a['data-ord']), 'sep': SEP[a['data-sep']], 'text': ''})
            self.stack.append(len(self.segs) - 1)
        else:
            self.stack.append(None)

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        for i in reversed(self.stack):
            if i is not None:
                self.segs[i]['text'] += data
                break


def check(pid, posts):
    d = os.path.join(OUT, pid)
    man = json.load(open(os.path.join(d, 'manifest.json'), encoding='utf-8'))
    by_src = {}
    for s in man['slides']:
        p = Segs()
        p.feed(open(os.path.join(d, s['file']), encoding='utf-8').read())
        by_src.setdefault(s['src'], []).append((s['part'], sorted(p.segs, key=lambda g: g['ord'])))
    bad = 0
    for i, want in enumerate(posts[pid]['slides_ar']):
        parts = sorted(by_src.get(i, []), key=lambda x: x[0])
        got = ''.join(g['sep'] + g['text'] for _, segs in parts for g in segs)
        if got != want:
            bad += 1
            print(f'  {pid} s{i + 1} MISMATCH\n    want {want!r}\n    got  {got!r}')
    print(f'{pid}: {len(posts[pid]["slides_ar"])} source slides, {len(man["slides"])} output slides, verbatim {"PASS" if not bad else "FAIL"}')
    return bad


def main(ids):
    posts = {p['id']: p for p in json.load(open(os.path.join(APP, 'posts_draft.json'), encoding='utf-8'))}
    ids = ids or sorted(x for x in os.listdir(OUT) if os.path.exists(os.path.join(OUT, x, 'manifest.json')))
    sys.exit(1 if sum(check(i, posts) for i in ids) else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
