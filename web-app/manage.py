import asyncio
from tortoise import Tortoise
from config import DATABASE_CONFIG

async def init():
    await Tortoise.init(config=DATABASE_CONFIG)
    await Tortoise.generate_schemas()
    print("Schemas generated.")
    await Tortoise.close_connections()

if __name__ == "__main__":
    asyncio.run(init())
