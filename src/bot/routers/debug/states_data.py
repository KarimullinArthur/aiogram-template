from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


router = Router(name=__name__)


@router.message(Command("fsm"))
async def start(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(str(data))
