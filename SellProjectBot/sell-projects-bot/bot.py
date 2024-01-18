import asyncio
import logging

from create_bot import bot, dp
from routes.main import main_router
from routes.projects import project_router


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    dp.include_router(main_router)
    dp.include_router(project_router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
