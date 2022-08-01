import aiohttp

from scooters.app.api.v1 import get_scooters
from scooters.app.api.v1 import get_scooters_admin
from scooters.app.context import AppContext


def wrap_handler(handler, context):
    async def _wrapper(request):
        return await handler(request, context)

    return _wrapper


def setup_routes(app: aiohttp.web.Application, ctx: AppContext) -> None:
    app.router.add_get(
        '/v1/scooters',
        wrap_handler(
            get_scooters.handle,
            ctx,
        ),
    )
    app.router.add_get(
        '/v1/admin/scooters',
        wrap_handler(
            get_scooters_admin.handle,
            ctx,
        ),
    )
