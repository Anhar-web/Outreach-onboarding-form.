"""b4p4: Batch 4 Paper & Light. See app/b4/art_direction_b4.md."""
import scenes as S
from looks import make

CONF = dict(look=1, ground='night', light='moon', figs=S.grandma_child)


def slide(ctx):
    return make(ctx, CONF)
