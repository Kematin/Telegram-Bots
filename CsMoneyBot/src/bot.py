import asyncio
import logging

# aiogram
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from data.config import config

# data
from data.telegram_data import Buttons, Descriptions, Keyboards

# db
from database.connection import initialize_database

# dotenv
from dotenv import load_dotenv

# service
from service.service import FloatWorker, StickerWorker, UserWorker

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
float_worker = FloatWorker()
sticker_worker = StickerWorker()


@dp.message(Command("start"))
async def start_bot(message: types.Message):
    await user_worker.create_user(message)
    await message.answer(desc.botDescription, reply_markup=keyboards.startKeyboard)


@dp.message(F.text.lower() == "💎 лучшие предложения 💎")
async def best_offers(message: types.Message):
    await message.answer("Лучшие предложения")


@dp.message(F.text.lower() == "📊 настройки float")
async def float_settings(message: types.Message):
    keyboard = keyboards.get_setting_keyboard("floats")
    float_string = await Descriptions.get_settings_description(message, "floats")
    await message.answer(float_string, reply_markup=keyboard)


@dp.message(F.text.lower() == "настройки sticker 🀄️")
async def sticker_settings(message: types.Message):
    keyboard = keyboards.get_setting_keyboard("sticker")
    sticker_string = await Descriptions.get_settings_description(message, "sticker")
    await message.answer(sticker_string, reply_markup=keyboard)


@dp.message(F.text.lower() == "🚹️ профиль 🚹️")
async def profile(message: types.Message):
    keyboard = keyboards.profileKeyboard
    profile_string = await Descriptions.get_user_description(message)
    await message.answer(profile_string, reply_markup=keyboard)


async def main():
    await initialize_database()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
