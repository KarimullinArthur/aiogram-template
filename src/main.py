import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from routers import router_manager
from config import settings


dp = Dispatcher()
bot = Bot(settings.bot_token)


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    dp.include_routers(*list(router_manager._routers.values()))

#     dp.include_routers(*router_manager.get_all_except(
#             (
#             router_manager.click, 
#             )
#         )
#     )
#     dp.include_routers(*router_manager.get_only(router_manager.click))

#     dp.include_router(routers["admin_panel.menu"])
# 
#     try: dp.include_routers(*list(routers.values()))
#     except: pass
# 
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
