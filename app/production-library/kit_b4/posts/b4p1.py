"""b4p1: Batch 4 Paper & Light. See app/b4/art_direction_b4.md."""
import scenes as S
from looks import make

CONF = dict(look=2, ground='pearl', object=S.obj_car)


def slide(ctx):
    return make(ctx, CONF)
