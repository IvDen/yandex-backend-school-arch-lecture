import typing
import dataclasses
import models


@dataclasses.dataclass
class Location:
    lat: float
    lon: float


# наследование забыл?
@dataclasses.dataclass
class Scooter_dto(models.Scooter):
    address: typing.Optional[str] = None


def from_model(scooter: models.Scooter) -> Scooter_dto:
    return Scooter_dto(id=scooter.id, location=scooter.location, user=scooter.user)
