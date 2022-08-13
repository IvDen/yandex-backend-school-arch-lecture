import typing
from app.context import AppContext
from app import storage
from app import dto
from app.utils import geocode


async def _enrich_address(scooters: typing.List[dto.Scooter_dto], client: geocode.GeocoderClient) -> None:
    for scooter in scooters:
        scooter.address = client.get_address(scooter.location)


async def get_vehicles(context: AppContext) -> typing.List[dto.Scooter_dto]:
    scooters = await storage.get_scooters(context)

    scooters_dto = [
        dto.from_model(scooter)
        for scooter in scooters
    ]
    await _enrich_address(scooters_dto, context.geocoder)
    return scooters_dto
