from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import markup as markup
import states as states
import filters as filters


router = Router(name=__name__)


@router.callback_query(F.data == markup.callbacks.mailing, filters.AdminFilter())
async def menu(callback: CallbackQuery, state: FSMContext):
    await state.set_state(states.AdminMenu.main_menu)
    await callback.answer("You are in admin menu!", reply_markup=markup.admin.main_menu())
