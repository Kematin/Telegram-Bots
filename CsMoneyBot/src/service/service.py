from abc import ABC

from aiogram.types import Message
from beanie import Document
from data.data import FloatSettingsInfo, StickerSettingsInfo, UserInfo
from database.crud import Database
from models.floats import FloatSettings
from models.stickers import StickerSettings
from models.users import User


# TODO
class UserWorker:
    user_crud = Database(User)

    @classmethod
    async def create_user(cls, message: Message) -> None:
        user = User(user_id=message.from_user.id, username=message.from_user.username)
        await cls._create_float_settings(user.user_id)
        await cls._create_sticker_settings(user.user_id)
        await cls.user_crud.save(user)

    @classmethod
    async def get_user_info(cls, message: Message) -> UserInfo:
        user_id = message.from_user.id
        user_info = await cls.user_crud.get(user_id)
        user_info = user_info.dict()
        del user_info["id"]
        user_info = UserInfo(**user_info)
        return user_info

    @staticmethod
    async def _create_float_settings(user_id: int) -> None:
        await SettingsWorker(FloatSettings, FloatSettingsInfo).create_settings_document(
            user_id=user_id
        )

    @staticmethod
    async def _create_sticker_settings(user_id: int) -> None:
        await SettingsWorker(
            StickerSettings, StickerSettingsInfo
        ).create_settings_document(user_id=user_id)


class SettingsWorker(ABC):
    def __init__(
        self, model: Document, data_show: FloatSettingsInfo | StickerSettingsInfo
    ) -> None:
        self.model = model
        self.crud = Database(model)
        self.data_show = data_show

    async def get_settings_info(
        self, message: Message
    ) -> FloatSettingsInfo | StickerSettingsInfo:
        info = await self.crud.get(message.from_user.id)
        info = info.dict()
        del info["id"]
        info = self.data_show(**info)
        return info

    async def create_settings_document(self, user_id: int) -> None:
        settings = self.model(user_id=user_id)
        await self.crud.save(settings)


class FloatWorker(SettingsWorker):
    def __init__(self) -> None:
        super().__init__(FloatSettings, FloatSettingsInfo)


class StickerWorker(SettingsWorker):
    def __init__(self) -> None:
        super().__init__(StickerSettings, StickerSettingsInfo)
