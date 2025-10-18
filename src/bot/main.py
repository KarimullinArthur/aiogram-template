import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from routers.all_routers import list_routers
from config import settings


dp = Dispatcher()
bot = Bot(settings.bot_token)


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    for router in list_routers:
        dp.include_routers(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
