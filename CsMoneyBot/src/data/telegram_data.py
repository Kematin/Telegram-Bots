from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class Descriptions:
    botDescription = "MarketCSGO skin helper"
    profileDescription = ""


class Buttons:
    _bestOffers = KeyboardButton(text="💎 Лучшие предложения 💎")
    _floatSettings = KeyboardButton(text="📊 Настройки float 📊")
    _stickerSettings = KeyboardButton(text="🀄️ Настройки sticker 🀄️")
    _profile = KeyboardButton(text="🚹️ Профиль 🚹️")
    startButtons = [[_bestOffers], [_floatSettings, _stickerSettings], [_profile]]


class Keyboards:
    startKeyboard = ReplyKeyboardMarkup(
        keyboard=Buttons().startButtons,
        resize_keyboard=True,
        input_field_placeholder="Выберите функционал",
    )
