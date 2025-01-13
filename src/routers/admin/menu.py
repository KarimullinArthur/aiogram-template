from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name=__name__)

@router.message(Command("admin"))
async def menu(message: Message):
    await message.answer("You are in admin menu!")
