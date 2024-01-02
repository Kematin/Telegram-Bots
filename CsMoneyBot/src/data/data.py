from dataclasses import dataclass
from typing import List


@dataclass
class UserInfo:
    user_id: int
    username: str
    send_stickers: bool
    send_float: bool


@dataclass
class FloatSettingsInfo:
    user_id: int
    min_price: int
    max_price: int
    weapons: List[str]
    max_steam_overpayment: List[str]


@dataclass
class StickerSettingsInfo:
    user_id: int
    min_price: int
    max_price: int
    weapons: List[str]
    max_steam_overpayment: List[str]
