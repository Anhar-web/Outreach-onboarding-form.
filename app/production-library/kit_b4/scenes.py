"""Batch 4 stage sets (look 3), people groups (looks 1, 4, 5) and small objects (look 2).
Round 2 (Anhar's grid review): every figure is rim-lit from behind (figures.lit) and
the poses vary per post; 2-3 figures each, at the edges and bottom only."""
from looks import (C, W, H, glow, car, lift_panel, rice_plate, tray, dallah, gift_bag, toy_car, blocks,
                   shoe_row, doorway, floor, cushions, shelf, avoid)
from kit import torn_rect
import figures as F


def _corner(svg_fn, pos, y=1200):
    x = 210 if pos == 'corner_l' else 870
    return avoid(svg_fn(x, y), 'prop')


# ---------------------------------------------------------------- p2: the host passes the sweets tray
def majlis_tray(g, tone, full=True):
    back = C['night'] if g == 'deep' else C['ink']
    out = floor(1080, C['tealDeep'], tone, seed=21) + cushions(1010, back, tone, n=4, x0=70, w=230)
    host, plate = F.woman_tray(720, 1300, 330, facing=-1)
    kid, hand = F.child_pull(420, 1300, 140, facing=-1)
    figs = F.lit(F.seated(180, 1110, 200) + host + kid, tone, halo=(560, 1120, 330))
    out += figs + f'<g>{plate}</g>' + dallah(930, 1260, 110, tone)
    return avoid(out, 'scene')


def tray_prop(g, tone, pos):
    return _corner(lambda x, y: tray(x, y, 170, tone, n=5), pos)


# ---------------------------------------------------------------- p6: the aunt holds out the gift bag
def majlis_gift(g, tone, full=True):
    out = floor(1080, C['tealDeep'], tone, seed=22) + cushions(1010, C['deep'], tone, n=3, x0=560, w=170)
    aunt, bag = F.woman_tray(330, 1300, 330, facing=1, item='bag')
    kid, hand = F.child_pull(690, 1300, 145, facing=1)
    out += F.lit(aunt + kid + F.seated(950, 1110, 180), tone, halo=(560, 1110, 320)) + bag
    return avoid(out, 'scene')


def gift_prop(g, tone, pos):
    return _corner(lambda x, y: gift_bag(x, y + 60, 150, tone), pos)


# ---------------------------------------------------------------- p8: grandma's room, the toy car
def toy_room(g, tone, full=True):
    out = floor(1070, C['night'] if g == 'deep' else C['ink'], tone, seed=23)
    out += torn_rect(250, 1150, 600, 110, C['tealDeep'], tone, sides='tblr', seed=24, layer=1)
    kid2, hand = F.child_pull(760, 1300, 135, facing=1)
    out += F.lit(F.seated(150, 1160, 170) + F.child(450, 1300, 135, arm='up') + kid2, tone, halo=(560, 1120, 320))
    out += blocks(300, 1235, 48, tone) + toy_car(600, 1235, 62, tone)
    return avoid(out, 'scene')


def car_prop(g, tone, pos):
    return _corner(lambda x, y: toy_car(x, y + 40, 110, tone), pos)


# ---------------------------------------------------------------- p12: the shoe guard at the door
def shoe_door(g, tone, full=True):
    out = doorway(820, 900, 180, 320, tone)
    out += floor(1210, C['ink'] if g == 'night' else C['night'], tone, seed=25)
    out += F.lit(F.man(700, 1250, 320) + F.woman(560, 1250, 300, lean=26, facing=-1, arm=(470, 1205)) +
                 F.child(400, 1290, 120, arm='none'), tone, halo=(620, 1150, 300))
    out += shoe_row(100, 1285, 4, 74, tone)
    return avoid(out, 'scene')


def shoes_prop(g, tone, pos):
    x0 = 110 if pos == 'corner_l' else 700
    return avoid(shoe_row(x0, 1250, 3, 82, tone), 'prop')


# ---------------------------------------------------------------- look 5 people
def toy_aisle_people(g, tone):
    out = shelf(1335, tone)
    kid, hand = F.child_pull(560, 1310, 125, facing=1)
    out += F.lit(F.woman(380, 1310, 290, lean=18, facing=1, arm=hand) + kid + F.man(920, 1310, 260), tone, halo=(560, 1180, 320))
    return avoid(out, 'people')


def door_people(g, tone):
    out = doorway(80, 1010, 150, 300, tone)
    kid, hand = F.child_pull(560, 1310, 115, facing=1)
    out += F.lit(F.grandma(300, 1310, 270, facing=1) + F.woman(800, 1310, 280, lean=22, facing=-1, arm=hand) + kid,
                 tone, halo=(560, 1180, 320))
    return avoid(out, 'people')


# ---------------------------------------------------------------- look 1 / look 4 slide-1 people
def grandma_child(g, tone):
    kid, hand = F.child_pull(620, 1190, 140, facing=-1)
    return F.lit(F.grandma(860, 1190, 270, facing=-1) + kid + F.woman(330, 1190, 275, facing=1), tone, halo=(620, 1060, 300))


def advice_people(g, tone):
    kid, hand = F.child_pull(470, 1190, 130, facing=-1)
    return F.lit(F.seated(830, 1190, 210) + F.man(640, 1190, 270) + kid, tone, halo=(640, 1060, 300))


def bedtime_people(g, tone):
    kid, hand = F.child_pull(560, 1265, 160, facing=1)
    return F.lit(F.woman(400, 1265, 380, lean=40, facing=1, arm=hand) + kid, tone, halo=(470, 1080, 320))


# ---------------------------------------------------------------- look 2 objects  obj(x, y, scale, tone)
def obj_car(x, y, sc, tone):
    return car(x, y, 120 * sc, tone)


def obj_lift(x, y, sc, tone):
    return lift_panel(x, y - 60 * sc, 95 * sc, tone)


def obj_rice(x, y, sc, tone):
    return rice_plate(x, y, 150 * sc, tone)
