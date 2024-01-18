from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

import descriptions
import keyboards
from create_bot import bot

main_router = Router()


@main_router.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(descriptions.START, reply_markup=keyboards.start_keyboard())


@main_router.callback_query(lambda c: c.data == "start")
async def start_callback(callback_query: CallbackQuery):
    await bot.send_message(
        callback_query.from_user.id,
        descriptions.START,
        reply_markup=keyboards.start_keyboard(),
    )


@main_router.message(Command("about"))
async def about_command(message: Message) -> None:
    await message.answer(descriptions.ABOUT)


@main_router.callback_query(lambda c: c.data == "about")
async def about_callback(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, descriptions.ABOUT)


@main_router.message(Command("feedback"))
async def feedback_command(message: Message) -> None:
    await message.answer(descriptions.FEEDBACK)


@main_router.callback_query(lambda c: c.data == "feedback")
async def feedback_callback(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, descriptions.FEEDBACK)
