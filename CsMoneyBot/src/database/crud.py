from typing import Any

from beanie import Document


class Database:
    def __init__(self, model: Document):
        self.model = model

    async def save(self, document) -> None:
        await document.create()

    async def get(self, user_id: int) -> Any:
        doc = await self.model.find_one(self.model.user_id == user_id)
        if doc:
            return doc
        else:
            return False

    async def update(self, id: int, body: dict) -> Any:
        doc = await self.get(id)
        if not doc:
            return False

        body = {key: value for key, value in body.items() if value is not None}

        update_query = {"$set": {field: value for field, value in body.items()}}

        await doc.update(update_query)
        return doc
