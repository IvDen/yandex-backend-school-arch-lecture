import asyncpg
import typing
from app.utils import secrets

class AppContext:
    def __init__(self, *, secrets_dir: str):
        self.secrets: secrets.SecretsReader = secrets.SecretsReader(secrets_dir)
        self.db: typing.Optional[asyncpg.pool] = None
    async def on_startup(self, app=None):
        self.db = await asyncpg.create_pool(self.secrets.get('postgres_dsn'))

    async def on_shutdown(self, app=None):
        if self.db:
            await self.db.close()
