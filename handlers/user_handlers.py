from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router, types
from aiogram.exceptions import TelegramBadRequest
from colorama import Fore
from Keyboards.reline import reply
from aiogram import F
from main_config.config import time_checkout, How_bot_works, About_us, Support, Unsuccessful_payment
from crystalpay_sdk import *
from crystalpay_sdk import InvoiceType
from payment.pay import crystalpayAPI
from main_config.config import name_of_shop
from datetime import date
from datetime import datetime
import sqlite3
import sys
from Keyboards.inline_keyboard import *
from Keyboards.inline_keyboard import list_goods, make_invoice, escape_to_menu
from Keyboards.inline_keyboard import NumbersCallbackFactory, InvoiceCallbackFactory, CryptocheckCallbackFactory
from aiogram.types.callback_query import CallbackQuery
from main_config.reviews import redict_url
from main_config.photo_path import photo_path
from main_config.code_death import code_death


user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: Message):
    db = sqlite3.connect('Database.db')
    cur = db.cursor()
    cur.execute(f'''SELECT main FROM First''')
    data = cur.fetchall()
    
    await message.reply_photo(photo=types.FSInputFile(path=photo_path))
    
    try:
        first_message=f'''{message.from_user.first_name}, добро пожаловать в магазин {name_of_shop}!

{data[0][0]}'''
        await message.answer(first_message, reply_markup=reply)
    
    except:
        await message.answer('Error', reply_markup=reply)
        print(Fore.RED + 'ОШИБКА ПЕРВОГО СООБЩЕНИЯ! ____________________________________')

    print(Fore.RED+f'Активировано стартовое сообщение! Его id: {message.from_user.id}, Никнейм: {message.from_user.full_name}')

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    current_date = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        db = sqlite3.connect('Database.db')
        cur = db.cursor()
        cur.execute(f'''SELECT id FROM Users WHERE id = {user_id}''')
        data = cur.fetchall()
    except sqlite3.OperationalError:
        db = sqlite3.connect('Database.db')
        cur = db.cursor()
        cur.execute('''CREATE TABLE users (
                        user_name text,
                        id integer,
                        date text,
                        time text
                                                )''')
        cur.execute(f'''SELECT id FROM Users WHERE id = {user_id}''')
        free = cur.fetchall()
    if len(free) == 0:
        db.execute(f"INSERT INTO Users VALUES ('{user_name}', {user_id}, '{current_date}', '{current_time}')")
        print(f'ПОЛЬЗОВАТЕЛЬ НЕ НАЙДЕН, НОВАЯ ЗАПИСЬ В БАЗЕ ДАННЫХ!++++++++++++++++++++++++++')
    else:
            print('ПОЛЬЗОВАТЕЛЬ НАЙДЕН! ЗАПИСЕЙ НЕТ!')
    db.commit()
    db.close()


@user_router.message(F.text == 'Выбрать Товар 💼')
async def choose1(message:Message):
    await message.reply('Выберите товар:', reply_markup = list_goods())


@user_router.callback_query(F.data == 'back')
async def vybor2(callback: CallbackQuery):
    await callback.message.answer('Выберите товар:', reply_markup = list_goods())


@user_router.callback_query(NumbersCallbackFactory.filter(F.number))
async def vybor3(callback: CallbackQuery,
                 callback_data: NumbersCallbackFactory):
        
        try:
            num = callback_data.pack().split(':')
            lists = callback_data.pack().split(':')
            db = sqlite3.connect('Database.db')
            cur = db.cursor()
            cur.execute(f'''SELECT name, price, more, number FROM Goods WHERE number = {num[1]}''')
            free = cur.fetchall()

            await callback.message.answer(text=f'''Вы выбрали товар {lists[2]}! 

Цена: {lists[3]}₽

{free[0][2]}
                                        ''', reply_markup= make_invoice(num[1]))
            await callback.answer()
        except TelegramBadRequest as e:
            print(Fore.RED + 'Ссылка на канал с отзывами не работает! ПРОВЕРЬТЕ ЕЕ НЕМЕДЛЕННО!')
            num = callback_data.pack().split(':')
            lists = callback_data.pack().split(':')
            db = sqlite3.connect('Database.db')
            cur = db.cursor()
            cur.execute(f'''SELECT name, price, more, number FROM Goods WHERE number = {num[1]}''')
            free = cur.fetchall()

            await callback.message.answer(text=f'''Вы выбрали товар {lists[2]}! 

Цена: {lists[3]}₽

    {free[0][2]}
                                        ''', reply_markup= make_invoice(num[1], rew='t.me/changeme'))
            await callback.answer()


@user_router.callback_query(InvoiceCallbackFactory.filter(F.number_invoice))
async def second(callback: CallbackQuery,
                 callback_data: InvoiceCallbackFactory):
    try:
        global callback_data_free
        callback_data_free = callback_data.pack().split(':')
        db = sqlite3.connect('Database.db')
        cur = db.cursor()
        cur.execute(f'''SELECT name, price, more, number FROM Goods WHERE number = {int(callback_data_free[1])}''')
        free = cur.fetchall()
        invoice2 = crystalpayAPI.Invoice.create(free[0][1], InvoiceType.purchase, time_checkout, redirect_url=redict_url)
        global link2
        global id2
        link2 = invoice2.get('url')
        id2 = invoice2.get('id')
        print('ПОЯВИЛАСЬ НОВАЯ СДЕЛКА!!! ЕЕ АЙДИ:', id2, 'ССЫЛКА НА НЕЕ:', link2)
        await callback.bot.send_message(callback.message.chat.id, f'''Вы выбрали: {free[0][0]}!

Цена: {free[0][1]}₽

Для оплаты перейдите по ссылке ниже, оплатите, а затем вернитесь в бота и нажмите "проверить платеж"!

Покупая товар в данном магазине, вы соглашаетесь с условиями публичной оферты, указанной в разделе "О нас 🌐".
                                        
Вот ваша ссылка на оплату: {link2}

По данной ссылке можно оплатить заказ ровно втечение {time_checkout // 60} часов с момента создания ссылки!
    ''', reply_markup=Cryptocheck(link2, int(callback_data_free[1]), id2))
    except Exception as e:
        print(e)
        await callback.bot.send_message(callback.message.chat.id, f'''Вы выбрали: {free[0][0]}!

Цена: {free[0][1]}₽

Для оплаты перейдите по ссылке ниже, оплатите, а затем вернитесь в бота и нажмите "проверить платеж"!

Покупая товар в данном магазине, вы соглашаетесь с условиями публичной оферты, указанной в разделе "О нас 🌐".
                                        
Вот ваша ссылка на оплату: Invalid credentials ERROR!

По данной ссылке можно оплатить заказ ровно втечение {time_checkout // 60} часов с момента создания ссылки!
    ''')
        print(Fore.RED + 'НЕПРАВИЛЬНО ВВЕДЕНЫ ДАННЫЕ КАССЫ CRYSTALPAY, СРОЧНО ПРОВЕРИТЕ ИХ И ЗАМЕНИТЕ!')


@user_router.callback_query(CryptocheckCallbackFactory.filter(F.number_check))
async def cryptopush(callback: CallbackQuery,
                 callback_data: CryptocheckCallbackFactory):
    data = callback_data.pack().split(':')
    sale1 = crystalpayAPI.Invoice.getinfo(data[2]) 
    check1 = list(sale1.items())[2][1]
    str(check1)
    if check1 == "payed":
        db = sqlite3.connect('Database.db')
        cur = db.cursor()
        cur.execute(f'''SELECT link, name FROM Resultgoods WHERE number = '{int(data[1])}' ''')
        free = cur.fetchall()
        await callback.bot.send_message(callback.message.chat.id, f'''
                                        
Платеж прошел успешно! ✅

Вы купили {free[0][1]}!

Вот ссылка на материал: {free[0][0]}

Для возврата товара обращайтесь в поддержку!

Спасибо, что выбрали наш магазин!
Ждем вас в следующий раз!😉            
                                        
                                                                         ''', reply_markup=escape_to_menu)
        print(Fore.LIGHTBLUE_EX+f'КТО-ТО КУПИЛ ТОВАР В БОТЕ!!! ПРОВЕРЬТЕ СВОЮ КАССУ!!!!!!!!')     
    else:
        await callback.bot.send_message(callback.message.chat.id, Unsuccessful_payment, reply_markup = Cryptocheck(link2, int(callback_data_free[1]), id2))


@user_router.message(Command('help'))
async def help(message:Message):
    await message.reply('Раздел помощи переехал в "Поддержка ☎️"!')


@user_router.message(F.text == 'Поддержка ☎️')
async def vybor3(message:Message):
    try:
        await message.answer(text=Support)
    except TelegramBadRequest:
        await message.answer("Error Telegram")
        print(Fore.CYAN + 'ОШИБКА! СООБЩЕНИЕ "Поддержка ☎️" НЕ РАБОТАЕТ!')


@user_router.message(F.text == 'О нас 🌐')
async def vybor4(message:Message):
    try:
        await message.answer(text=About_us)
    except TelegramBadRequest:
        await message.answer("Error Telegram")
        print(Fore.CYAN + 'ОШИБКА! СООБЩЕНИЕ "О нас 🌐" НЕ РАБОТАЕТ!')


@user_router.message(F.text == 'Как работает бот❓')
async def vybor1(message:Message):                                                     
    try:
        await message.answer(text=How_bot_works)
    except TelegramBadRequest:
        await message.answer("Error Telegram")
        print(Fore.CYAN + 'ОШИБКА! СООБЩЕНИЕ "Как работает бот❓" НЕ РАБОТАЕТ!')


@user_router.message(F.text == code_death)
async def destroy(message:Message):
    await message.answer(text='''
Бот прекратил работу по запросу администратора! 💀
                         
Для возобновления работы бота, запустите его с хост-машины!
                         ''')
    sys.exit(0)


@user_router.message(F.text)
async def destroy(message:Message):
    await message.answer(text='''
                         
Не понял вас! 🤷‍♂
                         
Ваша команда не была распознана!

Если вы потерялись в меню, введите пожалуйста команду /start чтобы перезапустить бота!
                         ''')
    

    
























