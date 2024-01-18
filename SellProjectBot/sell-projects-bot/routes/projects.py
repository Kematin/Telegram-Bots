from dataclasses import dataclass
from typing import Any, List

import aiohttp
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types.input_file import FSInputFile

import descriptions
import keyboards
from create_bot import bot

project_router = Router()
REQUEST_URL = "http://localhost:9999/bot/"
PROJECT_INDEX_ALL = {}
PROJECT_INDEX_FULL11 = {}
PROJECT_INDEX_FULL9 = {}
PROJECT_INDEX_MINIMUM = {}
PROJECT_INDEX_EXCLUSIVE = {}


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


@dataclass
class Projects:
    projects: List[Project]


async def request_json(url) -> Any:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def request_file(url):
    pass


def get_index(user_id: int, db: dict) -> int:
    index = db.get(user_id, None)
    if index is None:
        index = 0
        db[user_id] = index
    return index


def change_index(user_id: int, set_value: int, db: dict) -> None:
    db[user_id] = set_value


async def get_project_and_size(url: str, index: int) -> (Project, int):
    data = await request_json(url)
    projects = Projects(projects=data["projects"]).projects
    project = Project(**projects[index])
    return project, len(projects)


async def handle_send_project(
    callback_query: CallbackQuery, url: str, index: int, category: str
) -> None:
    project, size = await get_project_and_size(url, index)

    await bot.send_message(
        callback_query.from_user.id,
        descriptions.get_project_description(project),
        reply_markup=keyboards.interactive_keyboard(index, size, category),
    )


async def handle_edit_project(
    callback_query: CallbackQuery, url: str, index: int, category: str
) -> None:
    project, size = await get_project_and_size(url, index)

    await bot.edit_message_text(
        descriptions.get_project_description(project),
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        reply_markup=keyboards.interactive_keyboard(index, size, category),
    )


# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------


@project_router.callback_query(lambda c: c.data == "buy_projects")
async def about_callback(callback_query: CallbackQuery):
    img_url = "./static/price_list.jpeg"

    input_photo = FSInputFile(img_url)
    await bot.send_photo(
        callback_query.from_user.id,
        photo=input_photo,
        caption=descriptions.BUY_PROJECTS,
        reply_markup=keyboards.buy_project_keyboard(),
    )


# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------


@project_router.callback_query(lambda c: c.data == "all_project")
async def get_all_projects(callback_query: CallbackQuery):
    try:
        index = get_index(callback_query.from_user.id, PROJECT_INDEX_ALL)
        url = REQUEST_URL + "projects"
        category = "all"
        await handle_send_project(callback_query, url, index, category)
    except IndexError:
        await bot.send_message(
            callback_query.from_user.id,
            "Нет доступных проектов :(",
            reply_markup=keyboards.get_return_to_start(),
        )


@project_router.callback_query(lambda c: c.data == "prev_project_all")
async def get_prev_all_project(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    index = get_index(user_id, PROJECT_INDEX_ALL) - 1
    url = REQUEST_URL + "projects"
    category = "all"
    change_index(user_id, index, PROJECT_INDEX_ALL)
    await handle_edit_project(callback_query, url, index, category)


@project_router.callback_query(lambda c: c.data == "next_project_all")
async def get_next_all_project(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    index = get_index(user_id, PROJECT_INDEX_ALL) + 1
    url = REQUEST_URL + "projects"
    category = "all"
    change_index(user_id, index, PROJECT_INDEX_ALL)
    await handle_edit_project(callback_query, url, index, category)


# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------


@project_router.callback_query(lambda c: c.data == "full11_project")
async def get_full_11_projects(callback_query: CallbackQuery):
    try:
        index = get_index(callback_query.from_user.id, PROJECT_INDEX_FULL11)
        url = REQUEST_URL + "projects?category=full11"
        category = "full11"
        await handle_send_project(callback_query, url, index, category)
    except IndexError:
        await bot.send_message(
            callback_query.from_user.id,
            "Нет доступных проектов :(",
            reply_markup=keyboards.get_return_to_start(),
        )


@project_router.callback_query(lambda c: c.data == "prev_project_full11")
async def get_prev_full11_project(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    index = get_index(user_id, PROJECT_INDEX_FULL11) - 1
    url = REQUEST_URL + "projects?category=full11"
    category = "full11"
    change_index(user_id, index, PROJECT_INDEX_FULL11)
    await handle_edit_project(callback_query, url, index, category)


@project_router.callback_query(lambda c: c.data == "next_project_full11")
async def get_next_full11_project(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    index = get_index(user_id, PROJECT_INDEX_FULL11) + 1
    url = REQUEST_URL + "projects?category=full11"
    category = "full11"
    change_index(user_id, index, PROJECT_INDEX_FULL11)
    await handle_edit_project(callback_query, url, index, category)


# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------


@project_router.callback_query(lambda c: c.data == "full9_project")
async def get_full9_project(callback_query: CallbackQuery):
    try:
        index = get_index(callback_query.from_user.id, PROJECT_INDEX_FULL9)
        url = REQUEST_URL + "projects?category=full9"
        category = "full9"
        await handle_send_project(callback_query, url, index, category)
    except IndexError:
        await bot.send_message(
            callback_query.from_user.id,
            "Нет доступных проектов :(",
            reply_markup=keyboards.get_return_to_start(),
        )


@project_router.callback_query(lambda c: c.data == "prev_project_full9")
async def get_prev_full9_project(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    index = get_index(user_id, PROJECT_INDEX_FULL9) - 1
    url = REQUEST_URL + "projects?category=full9"
    category = "full9"
    change_index(user_id, index, PROJECT_INDEX_FULL9)
    await handle_edit_project(callback_query, url, index, category)


@project_router.callback_query(lambda c: c.data == "next_project_full9")
async def get_next_full9_project(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    index = get_index(user_id, PROJECT_INDEX_FULL9) + 1
    url = REQUEST_URL + "projects?category=full9"
    category = "full9"
    change_index(user_id, index, PROJECT_INDEX_FULL9)
    await handle_edit_project(callback_query, url, index, category)


# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------


@project_router.callback_query(lambda c: c.data == "min_project")
async def get_min_project(callback_query: CallbackQuery):
    try:
        index = get_index(callback_query.from_user.id, PROJECT_INDEX_MINIMUM)
        url = REQUEST_URL + "projects?category=minimum"
        category = "min"
        await handle_send_project(callback_query, url, index, category)
    except IndexError:
        await bot.send_message(
            callback_query.from_user.id,
            "Нет доступных проектов :(",
            reply_markup=keyboards.get_return_to_start(),
        )


@project_router.callback_query(lambda c: c.data == "prev_project_min")
async def get_prev_min_project(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    index = get_index(user_id, PROJECT_INDEX_MINIMUM) - 1
    url = REQUEST_URL + "projects?category=minimum"
    category = "min"
    change_index(user_id, index, PROJECT_INDEX_MINIMUM)
    await handle_edit_project(callback_query, url, index, category)


@project_router.callback_query(lambda c: c.data == "next_project_min")
async def get_next_min_project(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    index = get_index(user_id, PROJECT_INDEX_MINIMUM) + 1
    url = REQUEST_URL + "projects?category=minimum"
    category = "min"
    change_index(user_id, index, PROJECT_INDEX_MINIMUM)
    await handle_edit_project(callback_query, url, index, category)


# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------


@project_router.callback_query(lambda c: c.data == "exclusive_project")
async def get_exclusive_project(callback_query: CallbackQuery):
    try:
        index = get_index(callback_query.from_user.id, PROJECT_INDEX_EXCLUSIVE)
        url = REQUEST_URL + "projects?category=exclusive"
        category = "exclusive"
        await handle_send_project(callback_query, url, index, category)
    except IndexError:
        await bot.send_message(
            callback_query.from_user.id,
            "Нет доступных проектов :(",
            reply_markup=keyboards.get_return_to_start(),
        )


@project_router.callback_query(lambda c: c.data == "prev_project_exclusive")
async def get_prev_exclusive_project(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    index = get_index(user_id, PROJECT_INDEX_EXCLUSIVE) - 1
    url = REQUEST_URL + "projects?category=exclusive"
    category = "exclusive"
    change_index(user_id, index, PROJECT_INDEX_EXCLUSIVE)
    await handle_edit_project(callback_query, url, index, category)


@project_router.callback_query(lambda c: c.data == "next_project_exclusive")
async def get_next_exclusive_project(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    index = get_index(user_id, PROJECT_INDEX_EXCLUSIVE) + 1
    url = REQUEST_URL + "projects?category=exclusive"
    category = "exclusive"
    change_index(user_id, index, PROJECT_INDEX_EXCLUSIVE)
    await handle_edit_project(callback_query, url, index, category)
