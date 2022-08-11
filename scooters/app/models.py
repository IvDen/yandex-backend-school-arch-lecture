# from __future__ import annotations
import dataclasses
import asyncpg
import typing

@dataclasses.dataclass
class User:
    id: str


@dataclasses.dataclass
class Location:
    lat: float
    lon: float


@dataclasses.dataclass
class Scooter:
    id: str
    location: Location
    user: typing.Optional[User] = None

    # @classmethod #убрал чтобы без модуля __future__
    # def from_db(cls, row: asyncpg.Record) -> Scooter:
    #     pass


def from_db(row: asyncpg.Record) -> Scooter:
    id_str: str = None
    if row:
        id_str = row['user']
    return Scooter(id=row['id'], location=Location(lat=row['location'][0], lon=row['location'][1]), user=User(id=id_str))


