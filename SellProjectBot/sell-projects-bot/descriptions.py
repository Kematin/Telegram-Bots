from dataclasses import dataclass

from config import config


@dataclass
class Project:
    id: str
    name: str
    summary: str
    price: int
    category: str
    have_presentation: bool
    have_product: bool
    have_unique: bool
    is_blocked: bool
    created_at: str


ABOUT = "О НАС"
START = "СТАРТ"
FEEDBACK = "ОТЗЫВЫ"

BUY_PROJECTS = "КУПИТЬ ПРОЕКТЫ"


def get_project_description(project: Project):
    have = {1: "✔️", 0: "✖️"}

    desc = (
        f"НАЗВАНИЕ: {project.name}"
        + f"\nКРАТКОЕ СОДЕРЖАНИЕ: {project.summary}"
        + f"\nЦЕНА: {project.price}"
        + f"\nКАТЕГОРИЯ: {config.CATEGORIES[project.category]}"
        + f"\nПРЕЗЕНТАЦИЯ: {have[project.have_presentation]}"
        + f"\nПРОДУКТ: {have[project.have_product]}"
        + f"\nУНИКАЛЬНОСТЬ: {have[project.have_unique]}"
    )
    return desc
