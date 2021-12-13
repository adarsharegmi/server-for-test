 
from typing import Text
from aiohttp import web

routes = web.RouteTableDef()

async def html_response(document='a.txt'):
    s = open(document, "r")
    return web.Response(text=s.read(), content_type='text/html')

@routes.get('/')
async def hello(request):
    return await html_response()

app = web.Application()
app.add_routes(routes)

web.run_app(app)

