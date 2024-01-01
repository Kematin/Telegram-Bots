import asyncio
import logging

# aiogram
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from data.config import config
from data.data import FloatSettingsInfo, StickerSettingsInfo

# data
from data.telegram_data import Buttons, Descriptions, Keyboards

# db
from database.connection import initialize_database

# dotenv
from dotenv import load_dotenv
from models.floats import FloatSettings
from models.stickers import StickerSettings

# service
from service.service import SettingsWorker, UserWorker

load_dotenv()

# settings
desc = Descriptions()
buttons = Buttons()
keyboards = Keyboards()
logging.basicConfig(level=logging.INFO)

# aiogram
bot = Bot(token=config.BOT_TOKEN)
md = ParseMode.MARKDOWN_V2
dp = Dispatcher()

# workers
user_worker = UserWorker()
float_worker = SettingsWorker(model=FloatSettings, data_show=FloatSettingsInfo)
sticker_worker = SettingsWorker(model=StickerSettings, data_show=StickerSettingsInfo)


@dp.message(Command("start"))
async def start_bot(message: types.Message):
    await user_worker.create_user(message)
    await message.answer(desc.botDescription, reply_markup=keyboards.startKeyboard)


@dp.message(F.text.lower() == "💎 лучшие предложения 💎")
async def best_offers(message: types.Message):
    await message.answer("Лучшие предложения")


@dp.message(F.text.lower() == "📊 настройки float 📊")
async def float_settings(message: types.Message):
    float_settings = await float_worker.get_settings_info(message)
    print(float_settings)
    await message.answer("Настройки float")


@dp.message(F.text.lower() == "🀄️ настройки sticker 🀄️")
async def sticker_settings(message: types.Message):
    sticker_settongs = await sticker_worker.get_settings_info(message)
    print(sticker_settongs)
    await message.answer("Настройки sticker")


@dp.message(F.text.lower() == "🚹️ профиль 🚹️")
async def profile(message: types.Message):
    user_info = await user_worker.get_user_info(message)
    await message.answer(f"{user_info.user_id}: {user_info.username}")


async def main():
    await initialize_database()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
