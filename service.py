from aiogram import Bot, Dispatcher, types, F
from main_config.Token_conf import Token
import time

msg = '''В боте проводятся технические работы! 🛠 
Просим прощения за предоставленные неудобства!'''

bot = Bot(token=Token)
dp = Dispatcher()

@dp.message(F.text)
async def start(message: types.Message):
    await bot.send_message(message.chat.id, msg)

async def main_def():
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print('You have killed script!')
        time.sleep(10)
        exit()

