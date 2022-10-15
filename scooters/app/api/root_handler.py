from aiohttp import web as aiohttp_web
from app.context import AppContext
from app import storage
from app.models import Scooter


async def handle(request: aiohttp_web.Request, context: AppContext) -> aiohttp_web.Response:
    print("______root_handle")
    result = await storage.get_data(context)
    return aiohttp_web.json_response({'items': [
        to_responce(item) for item in result
    ]})


def to_responce(item: int) -> dict:
    return {
        'int': item
    }
