from typing import Optional

from beanie import Document, Indexed


class User(Document):
    user_id: Indexed(int)
    username: Optional[str] = None

    class Settings:
        name = "users"
