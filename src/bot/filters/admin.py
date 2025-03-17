from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message

import database as database


class AdminFilter(Filter):
    async def __call__(self, message: Message | CallbackQuery) -> bool:
        admins = await database.admins.get_admins_tg_ids()

        # if callaback
        if hasattr(message, "message"):
            return message.message.chat.id in admins

        return message.chat.id in admins
