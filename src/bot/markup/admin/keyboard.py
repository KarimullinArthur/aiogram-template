from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


text_mailing = "📢Рассылка"
callback_data_mailing = "mailing"

text_stats = "📊Статистика"
callback_data_stats = "stats"


def main_menu():
    mailing = InlineKeyboardButton(text=text_mailing, callback_data=callback_data_mailing)
    stats = InlineKeyboardButton(text=text_stats, callback_data=callback_data_stats)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[mailing, stats]], resize_keyboard=True)

    return keyboard
