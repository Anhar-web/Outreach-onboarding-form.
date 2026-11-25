"""b4p2: Batch 4 Paper & Light. See app/b4/art_direction_b4.md."""
import scenes as S
from looks import make

CONF = dict(look=3, ground='deep', scene=S.majlis_tray, prop=S.tray_prop)


def slide(ctx):
    return make(ctx, CONF)
