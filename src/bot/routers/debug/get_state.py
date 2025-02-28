from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


router = Router(name=__name__)


@router.message(Command("state"))
async def start(message: Message, state: FSMContext):
    current_state = await state.get_state()
    await message.answer(str(current_state))
