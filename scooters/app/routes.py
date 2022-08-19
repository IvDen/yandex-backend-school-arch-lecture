from aiohttp import web as aiohttp_web

from app.api.v1 import get_scooters as v1_get_scooters
from app.api.v1 import get_scooters_admin as v1_get_scooters_admin
from app.api.v2 import get_scooters as v2_get_scooters
from app.api.v2 import get_scooters_admin as v2_get_scooters_admin
from app.api import root_handler

from app.context import AppContext


def wrap_handler(handler, context):
    async def _wrapper(request):
        return await handler(request, context)

    return _wrapper


def setup_routes(appl: aiohttp_web.Application, ctx: AppContext) -> None:
    appl.router.add_get(
        '/',
        wrap_handler(
            root_handler.handle,
            ctx,
        ),
    )

    appl.router.add_get(
        '/v1/scooters',
        wrap_handler(
            v1_get_scooters.handle,
            ctx,
        ),
    )

    appl.router.add_get(
        '/v1/admin/scooters',
        wrap_handler(
            v1_get_scooters_admin.handle,
            ctx,
        ),
    )

    appl.router.add_get(
        '/v2/scooters',
        wrap_handler(
            v2_get_scooters.handle,
            ctx,
        ),
    )

    appl.router.add_get(
        '/v2/admin/scooters',
        wrap_handler(
            v2_get_scooters_admin.handle,
            ctx,
        ),
    )