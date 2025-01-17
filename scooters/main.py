import asyncio
import argparse
import os
import sys

import aiohttp

from app.context import AppContext
from app import routes


# TODO what about psycopg3 in req.txt?
# TODO rework from asyncpg to psycopg3
# TODO SQLAlch for query building?
# TODO SQLAlch for ORM

async def create_app(args):
    app = aiohttp.web.Application()
    ctx = AppContext(secrets_dir=args.secrets_dir)

    app.on_startup.append(ctx.on_startup)
    app.on_shutdown.append(ctx.on_shutdown)

    routes.setup_routes(app, ctx)

    return app


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--secrets_dir', type=str, required=True)

    return parser.parse_args()


def main():
    args = parse_args()

    app = asyncio.get_event_loop().run_until_complete(create_app(args))
    aiohttp.web.run_app(app)
    # asyncio.run(create_app(args))


if __name__ == '__main__':
    main()
