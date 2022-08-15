from aiohttp import web as aiohttp_web
from app.context import AppContext
from app import storage
from app.models import Scooter


async def handle(request: aiohttp_web.Request, context: AppContext) -> aiohttp_web.Response:
    scooters = await storage.get_scooters(context)
    return aiohttp_web.json_response({'items': [
        to_responce(scooter) for scooter in scooters
    ]})


def to_responce(scooter: Scooter) -> dict:
    return {
        'id': scooter.id,
        'location': {
            'lon': scooter.location.lon,
            'lat':  scooter.location.lat
        },
        'user': scooter.user.id if scooter.user else None
    }