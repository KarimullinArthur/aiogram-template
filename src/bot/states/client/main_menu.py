from aiogram.fsm.state import StatesGroup, State


class ClientMenu(StatesGroup):
    main_menu = State()
