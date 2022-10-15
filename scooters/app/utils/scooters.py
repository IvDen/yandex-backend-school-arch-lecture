import typing

import time
import asyncio

from app.context import AppContext
from app import storage
from app import dto
from app.utils import geocode


async def _enrich_address(scooters: typing.List[dto.Scooter_dto], client: geocode.GeocoderClient) -> None:
    futures = [client.get_address(scooter.location) for scooter in scooters]
    result = await asyncio.gather(*futures)

    for scooter, address in zip(scooters, result):
        scooter.address = address


async def get_scooters(context: AppContext) -> typing.List[dto.Scooter_dto]:
    scooters_dto = [
        dto.from_model(scooter)
        for scooter in await storage.get_scooters(context)
    ]
    start = time.time()
    await _enrich_address(scooters_dto, context.geocoder)
    finish = time.time()
    print(f'Time get_scooters: {finish - start}')
    return scooters_dto
