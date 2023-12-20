from aiogram.types import Message, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = 'Тренер'
cart = 'корзина'
delivery_status = 'статус заказа'

settings = 'Тренер'
orders = 'заказы'
questions = 'вопросы'

@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    
    await message.answer("Меню", reply_markup=markup)

@dp.message_handler(IsUser(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)

    await message.answer("Меню", reply_markup=markup)