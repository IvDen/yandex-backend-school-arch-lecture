import typing
import dataclasses
from app.models import Scooter


@dataclasses.dataclass
class Scooter_dto(Scooter):
    address: typing.Optional[str] = None


def from_model(scooter: Scooter) -> Scooter_dto:
    return Scooter_dto(id=scooter.id, location=scooter.location, user=scooter.user)