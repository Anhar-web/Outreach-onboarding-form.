"""b4p10: Batch 4 Paper & Light. See app/b4/art_direction_b4.md."""
import scenes as S
from looks import make

CONF = dict(look=1, ground='deep', light='lantern', people_x=780)


def slide(ctx):
    return make(ctx, CONF)
