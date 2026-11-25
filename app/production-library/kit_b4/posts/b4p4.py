"""b4p4: Batch 4 Paper & Light. See app/b4/art_direction_b4.md."""
import scenes as S
from looks import make

CONF = dict(look=1, ground='night', light='moon', people_x=760)


def slide(ctx):
    return make(ctx, CONF)
