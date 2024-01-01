from aiogram import types
from beanie import Document
from data.data import FloatSettingsInfo, StickerSettingsInfo, UserInfo
from database.crud import Database
from models.floats import FloatSettings
from models.stickers import StickerSettings
from models.users import User


class UserWorker:
    user_crud = Database(User)

    async def create_user(self, message: types.Message) -> None:
        user = User(user_id=message.from_user.id, username=message.from_user.username)
        await self._create_float_settings(user.user_id)
        await self._create_sticker_settings(user.user_id)
        await self.user_crud.save(user)

    async def get_user_info(self, message: types.Message) -> UserInfo:
        user_id = message.from_user.id
        user_info = await self.user_crud.get(user_id)
        user_info = UserInfo(user_id=user_info.user_id, username=user_info.username)
        return user_info

    async def _create_float_settings(self, user_id: int):
        await SettingsWorker(FloatSettings, FloatSettingsInfo).create_settings_document(
            user_id
        )

    async def _create_sticker_settings(self, user_id: int) -> None:
        await SettingsWorker(
            StickerSettings, StickerSettingsInfo
        ).create_settings_document(user_id)


class SettingsWorker:
    def __init__(
        self, model: Document, data_show: FloatSettingsInfo | StickerSettingsInfo
    ) -> None:
        self.model = model
        self.crud = Database(model)
        self.data_show = data_show

    async def get_settings_info(
        self, message: types.Message
    ) -> FloatSettingsInfo | StickerSettingsInfo:
        info = await self.crud.get(message.from_user.id)
        info = info.dict()
        del info["id"]
        info = self.data_show(**info)
        return info

    async def create_settings_document(self, user_id: int) -> None:
        settings = self.model(user_id=user_id)
        await self.crud.save(settings)
