"""b4p12: Batch 4 Paper & Light. See app/b4/art_direction_b4.md."""
import scenes as S
from looks import make

CONF = dict(look=3, ground='night', scene=S.shoe_door, prop=S.shoes_prop, hook_maxh=660)


def slide(ctx):
    return make(ctx, CONF)
