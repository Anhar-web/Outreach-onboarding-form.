from common import hook_box, body_box, soft_cta, cta_end
def slide(ctx):
    g='night'
    if ctx.last: return cta_end(ctx)
    if ctx.first: return {'ground':g,'html':hook_box(ctx,g)}
    return {'ground':g,'html':body_box(ctx,g)+soft_cta(ctx,y=1050)}
