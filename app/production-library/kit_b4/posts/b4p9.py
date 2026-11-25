"""b4p9: Batch 4 Paper & Light. See app/b4/art_direction_b4.md."""
import scenes as S
from looks import make

CONF = dict(look=4, ground='night')


def slide(ctx):
    return make(ctx, CONF)
