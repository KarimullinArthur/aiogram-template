from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


text_back = "Назад"

callback_data_back = "back"


def url(title: str, url: str):
    link_button = InlineKeyboardButton(text=title, url=url)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[link_button,]], resize_keyboard=True)

    return keyboard
