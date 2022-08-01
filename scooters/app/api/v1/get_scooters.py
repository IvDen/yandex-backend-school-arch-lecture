from aiohttp import web

from scooters.app.context import AppContext


async def handle(request: web.Request, context: AppContext) -> web.Response:
    return web.json_respomce({'Hello': 'world'})
