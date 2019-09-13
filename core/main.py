from aiohttp import web

from common.utils import Db, get_html

db = Db()


async def get_rates(request):
    rates = db.get_rates()
    return web.Response(text=get_html(rates), content_type='text/html')


async def add_pair(request):
    data = await request.post()
    pair = data.get("pair", "").strip().lower()
    if pair and '-' in pair:
        db.add_pair(pair)
    raise web.HTTPFound('/')


app = web.Application()
app.add_routes([
    web.get('/', get_rates),
    web.post('/add', add_pair)
])

web.run_app(app)
