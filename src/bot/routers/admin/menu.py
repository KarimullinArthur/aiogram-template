from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import bot.markup as markup
import bot.states as states
import bot.filters as filters


router = Router(name=__name__)


@router.message(Command("admin"), filters.AdminFilter())
async def menu(message: Message, state: FSMContext):
    await state.set_state(states.AdminMenu.main_menu)

    await message.answer("You are in admin menu!", reply_markup=markup.admin.main_menu())
