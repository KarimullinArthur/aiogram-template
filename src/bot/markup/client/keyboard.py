from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


text_button = "Кнопка"

callback_data_button = "button"


def main_menu():
    mailing = InlineKeyboardButton(text=text_button, callback_data=callback_data_button)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[mailing, ]], resize_keyboard=True)

    return keyboard
