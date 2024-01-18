from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def buy_project_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Все", callback_data="all_project"),
            ],
            [
                InlineKeyboardButton(text="Full 11", callback_data="full11_project"),
                InlineKeyboardButton(text="Full 9", callback_data="full9_project"),
                InlineKeyboardButton(text="Minimum", callback_data="min_project"),
            ],
            [
                InlineKeyboardButton(
                    text="Exclusive", callback_data="exclusive_project"
                ),
            ],
        ]
    )

    return keyboard


def start_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="Купить", callback_data="buy_projects"),
        ],
        [
            InlineKeyboardButton(text="О нас", callback_data="about"),
            InlineKeyboardButton(text="Отзывы", callback_data="feedback"),
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


def interactive_keyboard(
    index: int, project_size: int, category: str
) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    if index > 0:
        keyboard.add(
            InlineKeyboardButton(text="️⬅⬅⬅", callback_data=f"prev_project_{category}")
        )

    if index < project_size - 1:
        keyboard.add(
            InlineKeyboardButton(text="️➡➡➡", callback_data=f"next_project_{category}")
        )

    return keyboard.as_markup()


def get_return_to_start() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="Вернуться", callback_data="buy_projects"),
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard
