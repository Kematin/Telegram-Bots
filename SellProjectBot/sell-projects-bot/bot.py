import asyncio
import logging

from aiogram import Bot, Dispatcher, F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from config import config


def start_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="Button", callback_data="button")
    return builder.as_markup()


logging.basicConfig(level=logging.INFO)
router = Router()
md2 = ParseMode.MARKDOWN_V2


@router.message(Command("start"))
async def start(message: Message) -> None:
    await message.reply("start", reply_markup=start_keyboard())


async def main() -> None:
    bot = Bot(config.BOT_TOKEN)

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
