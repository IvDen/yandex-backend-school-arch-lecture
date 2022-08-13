from aiohttp import web
from app.context import AppContext
from app.utils.vehicles import get_vehicles
from app.utils import vehicles
#TODO dto v2 handle scooters to vehicle
async def handle(request: web.Request, context: AppContext) -> web.Response:
    vehicles_handled = await vehicles.get_vehicles(context)
    return web.json_response({'items': [
        to_responce(scooter) for scooter in scooters
    ]})


def to_responce(scooter: Scooter) -> dict:
    return {
        'id': scooter.id,
        'location': [scooter.location.lon, scooter.location.lat],
        'user': scooter.user.id if scooter.user else None
    }