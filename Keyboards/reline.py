from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Как работает бот❓')],
                                      [KeyboardButton(text='Выбрать Товар 💼')],
                                      [KeyboardButton(text='Поддержка ☎️'),
                                       KeyboardButton(text='О нас 🌐')]],
                                       resize_keyboard=True,
                                       input_field_placeholder='Выберите пункт меню...')
