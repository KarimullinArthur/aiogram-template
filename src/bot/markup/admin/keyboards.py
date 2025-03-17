from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from . import callbacks
from . import texts
from . import data


def main_menu():
#     mailing = InlineKeyboardButton(text=texts.mailing, callback_data=callback.mailing)
    mailing = InlineKeyboardButton(
        text=data.Mailing.text,
        callback_data=data.Mailing.callback
    )

    stats = InlineKeyboardButton(text=texts.stats, callback_data=callbacks.stats)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[mailing, stats]], resize_keyboard=True)

    return keyboard
