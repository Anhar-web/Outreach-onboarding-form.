"""Batch 4 stage sets (look 3), people groups (look 5) and small objects (look 2).

Look 3 scene(g, tone, full) draws the bottom ~40% of slide 1; prop(g, tone, pos)
draws one small prop in a corner for the inner and last slides.
Silhouettes are flat paper, one step darker than the ground, no faces.
"""
from looks import (C, W, H, glow, star, stars, mother, child, child_hand, seated, standing_man, car,
                   lift_panel, rice_plate, tray, dallah, gift_bag, toy_car, blocks, shoe_row, doorway,
                   floor, cushions, shelf, avoid)
from kit import paper, torn_rect


def _corner(svg_fn, pos, y=1200):
    """Place a small prop: corner_l = bottom-left, corner_r = bottom-right."""
    x = 210 if pos == 'corner_l' else 870
    return avoid(svg_fn(x, y), 'prop')


# ---------------------------------------------------------------- p2: majlis + sweets tray
def majlis_tray(g, tone, full=True):
    back = C['night'] if g == 'deep' else C['ink']
    lit = glow(860, 960, 380, .42)
    out = floor(1060, C['tealDeep'], tone, seed=21)
    out += cushions(990, back, tone, n=4, x0=70, w=230)
    out += seated(180, 1080, 190, C['ink'], tone) + seated(390, 1080, 175, C['ink'], tone) + seated(940, 1080, 185, C['ink'], tone)
    out += tray(600, 1210, 190, tone, n=6)
    out += dallah(830, 1240, 120, tone)
    out += child(470, 1290, 120, C['ink'], tone, facing=1)
    return lit + avoid(out, 'scene')


def tray_prop(g, tone, pos):
    return _corner(lambda x, y: tray(x, y, 170, tone, n=5), pos)


# ---------------------------------------------------------------- p6: the gift in a bag
def majlis_gift(g, tone, full=True):
    lit = glow(250, 980, 360, .4)
    out = floor(1080, C['tealDeep'], tone, seed=22)
    out += cushions(1010, C['deep'], tone, n=3, x0=520, w=180)
    out += seated(980, 1100, 170, C['ink'], tone)
    out += standing_man(780, 1290, 300, C['ink'], tone) if False else ''
    out += mother(330, 1290, 300, C['ink'], tone, facing=1)           # the aunt
    out += gift_bag(470, 1250, 110, tone)
    out += child(640, 1290, 125, C['ink'], tone, facing=-1, arm_up=False)
    return lit + avoid(out, 'scene')


def gift_prop(g, tone, pos):
    return _corner(lambda x, y: gift_bag(x, y + 60, 150, tone), pos)


# ---------------------------------------------------------------- p8: grandma's room, the toy car
def toy_room(g, tone, full=True):
    lit = glow(900, 1000, 340, .38)
    out = floor(1070, C['night'] if g == 'deep' else C['ink'], tone, seed=23)
    out += torn_rect(250, 1140, 600, 120, C['tealDeep'], tone, sides='tblr', seed=24, layer=1)   # the rug
    out += seated(930, 1100, 180, C['ink'], tone)                                                 # grandma at the back
    out += blocks(300, 1225, 52, tone)
    out += toy_car(560, 1225, 70, tone)
    out += child(420, 1300, 125, C['ink'], tone, facing=1, arm_up=True)
    out += child(720, 1300, 118, C['ink'], tone, facing=-1, arm_up=False)
    return lit + avoid(out, 'scene')


def car_prop(g, tone, pos):
    return _corner(lambda x, y: toy_car(x, y + 40, 110, tone), pos)


# ---------------------------------------------------------------- p12: the shoe guard at the door
def shoe_door(g, tone, full=True):
    out = doorway(800, 900, 190, 320, tone)
    out += floor(1210, C['ink'] if g == 'night' else C['night'], tone, seed=25)
    out += standing_man(690, 1250, 330, C['ink'], tone)
    out += mother(560, 1250, 300, C['ink'], tone, facing=1)
    out += shoe_row(100, 1275, 5, 74, tone)
    out += child(470, 1290, 120, C['ink'], tone, facing=-1, arm_up=False)
    return avoid(out, 'scene')


def shoes_prop(g, tone, pos):
    x0 = 110 if pos == 'corner_l' else 700
    return avoid(shoe_row(x0, 1250, 3, 82, tone), 'prop')


# ---------------------------------------------------------------- look 5 people
def toy_aisle_people(g, tone):
    lit = glow(540, 1200, 330, .3)
    out = shelf(1330, tone)
    out += standing_man(150, 1300, 250, C['ink'], tone) + mother(290, 1300, 240, C['ink'], tone, facing=1)
    out += mother(880, 1300, 260, C['ink'], tone, facing=-1)
    out += child(700, 1312, 90, C['ink'], tone, arm_up=False)
    return lit + avoid(out, 'people')


def door_people(g, tone):
    lit = glow(940, 1180, 300, .35)
    out = seated(130, 1300, 170, C['ink'], tone) + standing_man(300, 1300, 250, C['ink'], tone)
    out += mother(860, 1300, 260, C['ink'], tone, facing=-1)
    out += child(950, 1300, 105, C['ink'], tone, facing=-1, arm_up=False)
    return lit + avoid(out, 'people')


# ---------------------------------------------------------------- look 2 objects  obj(x, y, scale, tone)
def obj_car(x, y, sc, tone):
    return car(x, y, 120 * sc, tone)


def obj_lift(x, y, sc, tone):
    return lift_panel(x, y - 60 * sc, 95 * sc, tone)


def obj_rice(x, y, sc, tone):
    return rice_plate(x, y, 150 * sc, tone)
