from copy import copy
from typing import List, Union

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
)
from service.service import FloatWorker, StickerWorker, UserWorker


class Buttons:
    @classmethod
    def get_start_buttons(cls) -> List[List[KeyboardButton]]:
        bestOffers = KeyboardButton(text="💎 Лучшие предложения 💎")
        floatSettings = KeyboardButton(text="📊 Настройки float")
        stickerSettings = KeyboardButton(text="Настройки sticker 🀄️")
        profile = KeyboardButton(text="🚹️ Профиль 🚹️")
        startButtons = [[bestOffers], [floatSettings, stickerSettings], [profile]]
        return startButtons

    @classmethod
    def get_profile_buttons(cls) -> List[List[InlineKeyboardButton]]:
        changeFloatSending = InlineKeyboardButton(
            text="Отправлять float: +", callback_data="change_float_sending"
        )
        changeStickerSending = InlineKeyboardButton(
            text="Отправлять sticker: +", callback_data="change_sticker_sending"
        )
        profileButtons = [[changeStickerSending, changeFloatSending]]
        return profileButtons

    @classmethod
    def get_settings_button(
        cls, type: Union["sticker", "floats"]
    ) -> List[InlineKeyboardButton]:
        changeFloat = InlineKeyboardButton(
            text="Изменить настройки Float", callback_data="change_settings_float"
        )
        changeSticker = InlineKeyboardButton(
            text="Изменить настройки Sticker", callback_data="change_settings_sticker"
        )
        buttons = []
        added_button = {"sticker": changeSticker, "floats": changeFloat}[type]
        buttons.append([added_button])
        return buttons


class Keyboards:
    startKeyboard = ReplyKeyboardMarkup(
        keyboard=Buttons.get_start_buttons(),
        resize_keyboard=True,
        input_field_placeholder="Выберите функционал",
    )
    profileKeyboard = InlineKeyboardMarkup(
        inline_keyboard=Buttons.get_profile_buttons()
    )

    @classmethod
    def get_setting_keyboard(
        cls, type: Union["sticker", "floats"]
    ) -> InlineKeyboardMarkup:
        buttons = Buttons.get_settings_button(type)
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard


class Descriptions:
    botDescription = "MarketCSGO skin helper"
    settingsDescription = (
        "{name}"
        + "\nMin price: {min_price} ₽"
        + "\nMax price: {max_price} ₽"
        + "\nWeapons: {weapons}"
        + "\nMax Steam Overpayments: {max_steam}%"
    )
    profileDescription = (
        "ID: {user_id}"
        + "\nUsername: {username}"
        + "\nSend stickers: {sticker}"
        + "\nSend floats: {floats}"
    )

    @classmethod
    async def get_settings_description(
        cls, message: Message, type: Union["sticker", "floats"]
    ) -> str:
        worker, name = {
            "floats": (FloatWorker, "Float Settings"),
            "sticker": (StickerWorker, "Sticker Settings"),
        }[type]
        worker = worker()
        info = await worker.get_settings_info(message)
        info_string = cls.settingsDescription.format(
            name=name,
            min_price=info.min_price,
            max_price=info.max_price,
            weapons=" | ".join(info.weapons),
            max_steam=info.max_steam_overpayment,
        )
        return info_string

    @classmethod
    async def get_user_description(cls, message: Message) -> str:
        info = await UserWorker.get_user_info(message)
        emoji = {True: "✅", False: "❌"}
        info_string = cls.profileDescription.format(
            user_id=info.user_id,
            username=info.username,
            sticker=emoji[info.send_stickers],
            floats=emoji[info.send_float],
        )
        return info_string
