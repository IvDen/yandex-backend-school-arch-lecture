# from __future__ import annotations
import dataclasses
import asyncpg
import typing
from app.dto import Location

@dataclasses.dataclass
class User:
    id: str


@dataclasses.dataclass
class Scooter:
    id: str
    location: Location
    user: typing.Optional[User] = None

    # @classmethod #убрал чтобы без модуля __future__
    # def from_db(cls, row: asyncpg.Record) -> Scooter:
    #     pass


def from_db(row: asyncpg.Record) -> Scooter:
    return Scooter(id=row['id'], location=Location(lat=row['location'][0], lon=row['location'][1]),
                   user=User(id=row['user']) if row['user'] else None)
