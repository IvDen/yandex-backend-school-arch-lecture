from aiohttp import web as aiohttp_web
from app.context import AppContext
from app.utils import scooters
from app.dto import Scooter_dto


async def handle(request: aiohttp_web.Request, context: AppContext) -> aiohttp_web.Response:
    sctrs = await scooters.get_scooters(context)
    return aiohttp_web.json_response({'items': [
        to_responce(sctr) for sctr in sctrs
    ]})


def to_responce(sctr: Scooter_dto) -> dict:
    # print('________debug scooter.address: ', sctr.address)
    return {
        'id': sctr.id,
        'location': [sctr.location.lon, sctr.location.lat],
        'address': sctr.address,
        'user': sctr.user.id if sctr.user else None
    }