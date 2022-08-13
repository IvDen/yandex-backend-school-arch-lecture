import typing

from app import models
from app.context import AppContext


async def get_scooters(context: AppContext) -> typing.List[models.Scooter]:
    sql = '''
    SELECT id, location, "user" FROM scooters
    '''
    rows = await context.db.fetch(sql)
    return [models.from_db(row) for row in rows]
