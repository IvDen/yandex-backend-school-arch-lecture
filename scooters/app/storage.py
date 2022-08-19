import typing

from app import models
from app.context import AppContext


async def get_scooters(context: AppContext) -> typing.List[models.Scooter]:
    async with context.db.acquire() as conn:
        sql = '''
        SELECT id, location, "user" FROM scooters
        '''
        rows = await conn.fetch(sql)
        # rows = await context.db.fetch(sql)
        return [models.from_db(row) for row in rows]


async def get_data(context: AppContext) -> typing.List[int]:
    async with context.db.acquire() as conn:
        sql = '''
        SELECT 1 as "test"
        '''
        rows = await conn.fetch(sql)
        return [models.from_db_raw_test(row) for row in rows]
