import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from dotenv import load_dotenv

import form
from routers import routers, router_manager


load_dotenv()

token = str(os.getenv("BOT_TOKEN"))

dp = Dispatcher()
bot = Bot(token)


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(form.Registartion.name)
    await message.answer(message.text)
    await message.answer(message.chat.username)
    await bot.send_message(message.chat.id, "Hello, world!")
    await bot.send_message(message.chat.id, "What is your name?!")


@dp.message(Command("click"))
async def click(message: Message):
    await message.answer("click!")


async def main():
    bot2 = Bot("1317966174:AAE-bU8nkK19APV1Yoq_Cfcf1-QRJHq6MRI")
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)


    routers = router_manager._routers

    print(router_manager.click)
    print(router_manager.get_only(("click", ), as_list=False))
    print(router_manager.get_all_except((router_manager.click)))

    dp.include_routers(*router_manager.get_all_except(
            (
            router_manager.click, 
            )
        )
    )
    dp.include_routers(*router_manager.get_only(router_manager.click))

#     dp.include_router(routers["admin_panel.menu"])
# 
#     try: dp.include_routers(*list(routers.values()))
#     except: pass
# 
    await dp.start_polling(bot, bot2)


if __name__ == "__main__":
    asyncio.run(main())
