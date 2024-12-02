# myframework.py

import argparse
from aiohttp import web

async def handle(request):
    return web.Response(text="Hello, from custom aiohttp server!")

def runserver():
    parser = argparse.ArgumentParser(description="Start custom server")
    parser.add_argument(
        '--host', type=str, default='127.0.0.1', help="Host address"
    )
    parser.add_argument(
        '--port', type=int, default=8080, help="Port to listen on"
    )

    args = parser.parse_args()

    app = web.Application()
    app.router.add_get('/', handle)
    
    # Aiohttp serverini ishga tushurish
    web.run_app(app, host=args.host, port=args.port)

if __name__ == "__main__":
    runserver()
