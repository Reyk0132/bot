from filters import IsUser
from aiogram.types import Message, CallbackQuery
from keyboards.inline.categories import categories_markup, category_cb
from .menu import catalog
from loader import dp, bot, db
from aiogram.types.chat import ChatActions
from keyboards.inline.products_from_catalog import product_markup, product_cb

@dp.message_handler(IsUser(), text=catalog)
async def process_catalog(message: Message):
    await message.answer('Найди себя:',
                          reply_markup=categories_markup())
    
@dp.callback_query_handler(IsUser(), category_cb.filter(action='view'))
async def category_callback_handler(query: CallbackQuery, callback_data: dict):
    products = db.fetchall('''SELECT * FROM products product
                           WHERE product.tag = (SELECT title FROM categories WHERE idx=?)
                           AND product.idx NOT IN (SELECT idx FROM cart WHERE cid = ?)''',
                           (callback_data['id'], query.message.chat.id))
    
    await query.answer('Качкозавры.')
    await show_products(query.message, products)

async def show_products(m, products):

    if len(products) == 0:

        await m.answer('Здесь ничего нет')

    else:

        await bot.send_chat_action(m.chat.id, ChatActions.TYPING)

        for idx, title, body, video, price, _ in products:

            markup = product_markup(idx, price)
            text = f'<b>{title}</b>\n\n{body}'
            
            await m.answer_photo(photo=video,caption=text,reply_markup=markup)
