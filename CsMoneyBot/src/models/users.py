from typing import Optional

from beanie import Document, Indexed


class User(Document):
    user_id: Indexed(int)
    username: Optional[str] = None
    send_stickers: Optional[bool] = True
    send_float: Optional[bool] = True

    class Settings:
        name = "users"
