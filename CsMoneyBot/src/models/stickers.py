from typing import List, Optional

from beanie import Document, Indexed


class StickerSettings(Document):
    user_id: Indexed(int)
    min_price: Optional[int] = 0
    max_price: Optional[int] = 999999999
    weapons: Optional[List[str]] = [
        "Pistol",
        "Rifle",
        "Sniper Rifle",
        "SMG",
        "Machinegum",
        "Shotgun",
    ]
    max_steam_overpayment: Optional[int] = 15

    class Settings:
        name = "stickers_settings"
