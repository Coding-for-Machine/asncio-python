from aiohttp import web
from tortoise.contrib.aiohttp import register_tortoise
from app.routes import setup_routes
from config import DATABASE_CONFIG
import logging

app = web.Application()
setup_routes(app)

# Tortoise ORM ro'yxatdan o'tkazish
register_tortoise(
    app,
    config=DATABASE_CONFIG,
    generate_schemas=True,  # Migratsiyalarni ishlatish uchun bu `False` bo'lishi kerak
)

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)
    logging.basicConfig(level=logging.DEBUG)  # Barcha loglarni ko'rsatadi
