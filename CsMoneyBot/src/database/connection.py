from beanie import init_beanie
from data.config import config
from models.floats import FloatSettings
from models.stickers import StickerSettings
from models.users import User
from motor.motor_asyncio import AsyncIOMotorClient


async def initialize_database():
    client = AsyncIOMotorClient(config.DATABASE_URL)
    await init_beanie(
        database=client.get_database(),
        document_models=[User, FloatSettings, StickerSettings],
    )
