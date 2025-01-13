from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name=__name__)

@router.message(Command("subAdmin"))
async def subAdmin(message: Message):
    await message.answer("Sub ADMIN")
