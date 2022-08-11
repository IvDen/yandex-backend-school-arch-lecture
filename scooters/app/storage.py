import asyncpg

from app.context import AppContext
import typing
from app import models


async def get_scooters(context: AppContext) -> typing.List[models.Scooter]:
    sql = '''
    select id, location, user from scooters
    '''
    rows = await context.db.fetch(sql)
    return [models.from_db(row) for row in rows]