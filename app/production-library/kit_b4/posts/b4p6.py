"""b4p6: Batch 4 Paper & Light. See app/b4/art_direction_b4.md."""
import scenes as S
from looks import make

CONF = dict(look=3, ground='night', scene=S.majlis_gift, prop=S.gift_prop)


def slide(ctx):
    return make(ctx, CONF)
