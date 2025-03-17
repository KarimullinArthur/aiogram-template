from aiogram import F, Router
from aiogram.dispatcher.event.handler import CallbackType
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import markup as markup
import states as states


router = Router(name=__name__)


@router.callback_query(F.data == markup.callbacks.stats, StateFilter(states.AdminMenu.main_menu))
async def menu(callback: CallbackQuery, state: FSMContext):
    await callback.answer("There will be stats info here", reply_markup=markup.admin.main_menu())
