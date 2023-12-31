from aiogram.dispatcher.filters.state import StatesGroup, State

class CategoryState(StatesGroup):
    title = State()

class ProductState(StatesGroup):
    title = State()
    body = State()
    video = State()
    price = State()
    confirm = State()