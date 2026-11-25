"""b4p3: Batch 4 Paper & Light. See app/b4/art_direction_b4.md."""
import scenes as S
from looks import make

CONF = dict(look=5, ground='night', people=S.toy_aisle_people)


def slide(ctx):
    return make(ctx, CONF)
