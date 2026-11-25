"""b4p5: Batch 4 Paper & Light. See app/b4/art_direction_b4.md."""
import scenes as S
from looks import make

CONF = dict(look=2, ground='sandLight', object=S.obj_lift, hook_maxh=800)


def slide(ctx):
    return make(ctx, CONF)
