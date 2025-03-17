from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import database as database
import states as states
import markup as markup


router = Router(name=__name__)


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(states.client.ClientMenu.main_menu)

    if await database.users.get_user(message.chat.id) == None:
        await database.users.create_user(message.chat.id)

    await message.answer("welcome1000-10", reply_markup=markup.client.main_menu())
