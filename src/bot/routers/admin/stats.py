from aiogram import F, Router
from aiogram.dispatcher.event.handler import CallbackType
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import bot.markup as markup
import bot.states as states


router = Router(name=__name__)


@router.callback_query(F.data == markup.callback_data_stats, StateFilter(states.AdminMenu.main_menu))
async def menu(callback: CallbackQuery, state: FSMContext):
    await callback.answer("There will be stats info here", reply_markup=markup.admin.main_menu())
