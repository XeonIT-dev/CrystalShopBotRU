from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import sqlite3
from main_config.reviews import reviews
from aiogram.filters.callback_data import CallbackData


class NumbersCallbackFactory(CallbackData, prefix="good"):
    number: int
    name: str
    price: int


def list_goods():
    db = sqlite3.connect('Database.db')
    cur = db.cursor()
    cur.execute(f'''SELECT name, price, more, number FROM Goods''')
    data = cur.fetchall()
    builder = InlineKeyboardBuilder()
    for i in data:
        builder.button(
            text=f'{i[0]} {i[1]}₽', callback_data=NumbersCallbackFactory(number=int(i[3]), name=str(i[0]), price=int(i[1])))
    builder.adjust(1)
    db.commit()
    db.close
    return builder.as_markup()


class InvoiceCallbackFactory(CallbackData, prefix="invoice"):
    number_invoice: int

class CardCallbackFactory(CallbackData, prefix='card'):
    number_answer: int

def make_invoice(num, rew = reviews):
             
    builder = InlineKeyboardBuilder()
    builder.button(
                            text=f'Оплата Криптовалютой ₿', callback_data=InvoiceCallbackFactory(number_invoice=int(num)))
    builder.button(
                            text=f'Отзывы', url=rew)
    builder.adjust(1)
    return builder.as_markup() 


class CryptocheckCallbackFactory(CallbackData, prefix='cryptocheck'):
    number_check: int
    id_deal: str

def Cryptocheck(link, num, id):
                
                builder = InlineKeyboardBuilder()
                builder.button(
                        text=f'Оплатить 💸', url=link)
                builder.button(
                        text=f'Проверить платеж ❓', callback_data=CryptocheckCallbackFactory(number_check=int(num), id_deal=str(id)))

                builder.adjust(1)
                return builder.as_markup() 


escape_to_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Вернуться в меню', callback_data='back')]])

