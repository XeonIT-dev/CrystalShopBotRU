import os
import asyncio
from aiogram import Bot, Dispatcher
import logging
from main_config.Token_conf import Token
from colorama import Fore
from handlers.user_handlers import user_router
import sqlite3
import time
import aiogram
from initializer.initializer_db import initialize, reload


try:
    from service import main_def
except:
    print(Fore.RED + "СРОЧНО ПОМЕНЯЙТЕ API ТОКЕН БОТА!")


name_of_creator = 'XeonIT-dev'
support_link = 'https://github.com/XeonIT-dev'


initialize()


print(Fore.GREEN + f'''╭━━━╮╱╱╱╱╱╱╱╱╭╮╱╱╱╭╮╭━━━┳╮╱╭┳━━━┳━━━┳━━╮╭━━━┳━━━━╮
┃╭━╮┃╱╱╱╱╱╱╱╭╯╰╮╱╱┃┃┃╭━╮┃┃╱┃┃╭━╮┃╭━╮┃╭╮┃┃╭━╮┃╭╮╭╮┃
┃┃╱╰╋━┳╮╱╭┳━┻╮╭╋━━┫┃┃╰━━┫╰━╯┃┃╱┃┃╰━╯┃╰╯╰┫┃╱┃┣╯┃┃┣┻┳╮╭╮
┃┃╱╭┫╭┫┃╱┃┃━━┫┃┃╭╮┃┃╰━━╮┃╭━╮┃┃╱┃┃╭━━┫╭━╮┃┃╱┃┃╱┃┃┃╭┫┃┃┃
┃╰━╯┃┃┃╰━╯┣━━┃╰┫╭╮┃╰┫╰━╯┃┃╱┃┃╰━╯┃┃╱╱┃╰━╯┃╰━╯┃╱┃┃┃┃┃╰╯┃
╰━━━┻╯╰━╮╭┻━━┻━┻╯╰┻━┻━━━┻╯╱╰┻━━━┻╯╱╱╰━━━┻━━━╯╱╰╯╰╯╰━━╯
╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╰━━╯ made buy {name_of_creator} 

Здесь ты можешь создать свой Telegram магазин!

Перед тем, как запустить бота, пожалуйста, заполните корректно все данные!
''')

print(hello_msg := '''
Choose an option:
      
      [1] Запустить бота
      [2] Просмотреть базу данных пользователей
      [3] Поменять API TOKEN бота!
      [4] Поменять платежную информацию!
      [5] Просмотреть расположение бота!
      [6] Поменять прочие ссылки!
      [7] Создать карточки товаров!
      [8] Создать результаты покупок товаров!
      [9] Поменять прочую информацию
      [10] Поменять приветственное сообщение!
      [11] Поменять приветственную фотографию!
      [12] Технические работы
      [13] Очистить терминал
      [14] Выход
      ''')

a = input('Введите ответ:   ')

while a != '1':
    try:
        if a == '1':
            pass
        
        elif a == '2':
            
            try:
                db = sqlite3.connect('Database.db')
                cur = db.cursor()
                cur.execute('''SELECT * from users''')
                data = cur.fetchall()
                for el in data:
                    print(el)
                db.commit()
                db.close()
                print('Запустить магазин --> 1')
                a = input('Enter answer:  ')
            except sqlite3.OperationalError:
                print('В бота еще никто не заходил! База данных Users пуста!')
                print('Запустить магазин --> 1')
                a = input('Введите ответ:  ')
        
        elif a == '3':
            print('''Если вы не хотите менять API TOKEN бота, введите 0:  ''')
            start_loop = input('Для продолжения изменений, напечатайте 1, для отмены - 0:  ')
            if start_loop == '1':
                db = sqlite3.connect('Database.db')
                db.execute(f'DELETE FROM Token')
                d = input(f'Введите новый API TOKEN бота:  ')    
                db.execute(f"INSERT INTO TOKEN VALUES ('{d}')")
                db.commit()
                db.close()
                print('Ваши новые данные успешно сохранены!')
                reload()

            elif start_loop == '0':
                print('Запустить магазин --> 1')
                a = input('Введите ответ:  ')

        elif a == '4':
            print('''Если вы не хотите менять прочие ссылки бота, введите 0:  ''')
            start_loop = input('Для продолжения изменений, напечатайте 1, для отмены - 0:  ')
            if start_loop == '1':
                db = sqlite3.connect('Database.db')
                db.execute(f'DELETE FROM Payment')
                d = input(f'Введите имя кассы CrystalPAY:  ')  
                d1 = input(f'Введите Private Key (приватный ключ) кассы:  ')   
                d2 = input(f'Введите Salt Key (соленный ключ) кассы:  ')
                db.execute(f"INSERT INTO Payment VALUES ('{d}', '{d1}', '{d2}')")
                db.commit()
                db.close()
                print('Ваши новые данные успешно сохранены!')
                reload()

            elif start_loop == '0':
                print('Запустить магазин --> 1')
                a = input('Введите ответ:  ')
        
        elif a == "5":
            
            print(f'Бот работает из директории:  {os.path.dirname(__file__)}')
            print('Запустить магазин --> 1')
            a = input('Введите ответ:  ')

        elif a == "6":
            print('''Если вы не хотите менять прочие ссылки бота, введите 0:  ''')
            start_loop = input('Для продолжения изменений, напечатайте 1, для отмены - 0:  ')
            if start_loop == '1':
                db = sqlite3.connect('Database.db')
                db.execute(f'DELETE FROM Reviews')
                d = input(f'Введите ссылку на канал с отзывами:  ')  
                d1 = input(f'Введите ссылку на аккаунт администратора бота:  ')   
                d2 = input(f'Введите ссылку на аккаунт поддержки бота:  ')
                print('Введите ссылку на redirect ссылку, на которую будет кидать после оплаты.')
                d3 = input(f'Советуем поставить ссылку на самого бота магазин:  ')   
                db.execute(f"INSERT INTO Reviews VALUES ('{d}', '{d1}', '{d2}', '{d3}')")
                db.commit()
                db.close()
                print('Ваши новые данные успешно сохранены!')
                reload()

            elif start_loop == '0':
                print('Запустить магазин --> 1')
                a = input('Введите ответ:  ')
            
        elif a == '7':
            
            print('Вы точно хотите продолжить изменения товаров и услуг? Предыдущие данные будет невозможно восстановить!')
            start_loop = input('Для продолжения изменений, напечатайте 1, для отмены - 0:  ')
            if start_loop == '1':
                db = sqlite3.connect('Database.db')
                db.execute(f'DELETE FROM Goods')
                db.commit()
                db.close()
                n = int(input('Введите количество новых товаров для добавления (Только число!):  '))
                for i in range(1, n + 1):
                    c = ''    
                    b = input(f'Введите имя товара № {i} (Не более 20 символов!):  ')
                    numoflines = int(input('Введите количество строк в описании файла (Только число!):  '))

                    for k in range(1, numoflines + 1):
                        log = input(f'Введите строку № {k} в товаре № {k}:  ') + '\n'
                        c += log

                    d = int(input(f'Введите цену товара № {k}:  '))
                    db = sqlite3.connect('Database.db')     
                    db.execute(f"INSERT INTO Goods VALUES ('{k}', '{b}', '{c}', '{d}')")
                    db.commit()
                    db.close()
                
                print('Ваши новые данные успешно сохранены!')
                reload()

            elif start_loop == '0':
                print('Запустить магазин --> 1')
                a = input('Введите ответ:  ')
            else:
                continue

        elif a == '8':
            
            print('Вы точно хотите продолжить изменения результатов покупок товаров и услуг? Предыдущие данные будет невозможно восстановить!')
            start_loop = input('Для продолжения изменений, напечатайте 1, для отмены - 0:  ')
            if start_loop == '1':
                db = sqlite3.connect('Database.db')
                cur = db.cursor()
                cur.execute('''SELECT * from Goods''')
                data = len(cur.fetchall())
                db.close()
                db = sqlite3.connect('Database.db')
                db.execute(f'DELETE FROM Resultgoods')
                db.commit()
                db.close()
                for i in range(1, data + 1):
                    login = input(f'Введите название результата успешной покупки № {i}:  ')
                    result_link = input(f'Введите ссылку на ресурс, которая будет даваться при успешной покупке товара № {i}:  ')
                    db = sqlite3.connect('Database.db')     
                    db.execute(f"INSERT INTO Resultgoods VALUES ('{i}', '{login}', '{result_link}')")
                    db.commit()
                    db.close()
                print('Ваши новые данные успешно сохранены!')
                reload()
            elif start_loop == '0':
                print('Запустить магазин --> 1')
                a = input('Введите ответ:   ')
            else:
                continue
        
        elif a == '9':
            
            print('Вы точно хотите изменить прочую информацию? Восстановить ее будет невозможно!')
            start_loop = input('Для продолжения изменений, напечатайте 1, для отмены - 0:  ')
            if start_loop == '1':
                db = sqlite3.connect('Database.db')
                db.execute(f'DELETE FROM Other_data')
                db.commit()
                db.close()

                name_of_shop = input(f'Введите название магазина:  ')
                    
                time_checkout = int(input(f'Введите время жизни чека (в минутах):  '))
                
                print('Напишите раздел "О нас". В данном разделе обязательно должна быть ссылка на публичную оферту магазина!')  
                numoflines = int(input('Введите количество строк в "О нас" бота:  '))
                text_about_us = ''
                for k in range(1, numoflines + 1):
                    log = input(f'Введите строку № {k} в описании бота:  ') + '\n'
                    text_about_us += log
                    
                hours = int(input('Введите время, в течение которого поддержка отвечает на запросы:  '))
                    
                print('Введите код, при вводе которого в чат в телеграмме бот будет сразу останавливаться...')
                code_death = input('Сделайте данный код сложным, чтобы его нельзя было подобрать:  ')
                    
                How_bot_works = ''
                numoflines1 = int(input('Введите количество строк в "Как работает бот" бота:  '))
                for n in range(1, numoflines1 + 1):
                    log1 = input(f'Введите строку № {n} в описании бота:  ') + '\n'
                    How_bot_works += log1

                support_link_bot = input('Введите ссылку на поддержку магазина:  ')


                db = sqlite3.connect('Database.db')     
                db.execute(f"INSERT INTO Other_data VALUES ('{name_of_shop}', '{time_checkout}', '{text_about_us}', '{How_bot_works}', '{hours}', '{support_link_bot}', '{code_death}')")
                db.commit()
                db.close()
                print('Ваши новые данные успешно сохранены!')
                reload()

                    
            elif start_loop == '0':
                print('Запустить магазин --> 1')
                a = input('Введите ответ:  ')
            else:
                continue

        elif a == '10':
            
            print('Вы точно хотите изменить первое сообщение? Восстановить его будет невозможно!')
            start_loop9 = input('Для продолжения изменений, напечатайте 1, для отмены - 0:  ')
            if start_loop9 == '1':
                db = sqlite3.connect('Database.db')
                db.execute(f'DELETE FROM First')
                db.commit()
                db.close()
                numoflines = int(input('Введите количество строк в первом сообщении бота:  '))
                lol = 1
                command1 = ''
                for k in range(numoflines):
                    vvod = input(f'Введите строку № {lol} в описании бота:  ') + '\n'
                    command1 += vvod
                    lol += 1
                db = sqlite3.connect('Database.db')
                cur = db.cursor()
                db.execute(f"INSERT INTO First VALUES ('{command1}')")
                db.commit()
                db.close()
                print('Ваши новые данные успешно сохранены!')
                reload()
            elif start_loop == '0':
                print('Запустить магазин --> 1')
                a = input('Enter answer:  ')
            else:
                continue

        elif a == '11':
            
            print('''Вы точно хотите изменить начальное фото? Восстановить начальное фото будет возможно, выбрав в данным пункте расположение 'logo.jpg'!''')
            start_loop10 = input('Для продолжения изменений, напечатайте 1, для отмены - 0:  ')

            if start_loop10 == '1':
                db = sqlite3.connect('Database.db')
                db.execute(f'DELETE FROM Link_change')
                data = input(f'Введите путь к картинке в форме png, jpg, jpeg:  ')  
                db.execute(f"INSERT INTO Link_change VALUES ('{data}')")
                db.commit()
                db.close()
                print('Ваши новые данные успешно сохранены!')
                reload()

            elif start_loop10 == '0':
                print('Запустить магазин --> 1')
                a = input('Введите ответ:  ')
            else: 
                print('Запустить магазин --> 1')
                a = input('Введите ответ:  ')

        elif a == '12':
            if __name__ == '__main__':
                logging.basicConfig(level=logging.INFO)
                try:
                    asyncio.run(main_def())
                except KeyboardInterrupt:
                    print('You have killed script!')
                    time.sleep(10)
                    exit()
                except RuntimeError:
                    print('You have killed script!')
                    time.sleep(10)
                    exit()
                except aiogram.exceptions.TelegramNetworkError:
                    print('Бот не начал свою работу! Проверьте подключение к интернету и перезапустите программу!')
                    time.sleep(100)
                    exit()
                except:
                    print('Возникла проблема! Проверьте, ввели ли Вы все данные в бот по инструкции верно и перезапустите программу! ')
                    print(f'Если проблема не устраняется, обратитесь в поддержку по ссылке:  {support_link}')
                    time.sleep(100)
                    exit()

        elif a == '13':
            if os.name == 'nt':
                os.system('cls')
                print(hello_msg)
                a = input('Введите ответ:   ')
            elif os.name == 'posix':
                os.system('clear')
                print(hello_msg)
                a = input('Введите ответ:   ')
            

        elif a == '14':
            
            print('Вы вышли из программы!')
            time.sleep(3)
            exit()

        else:
            print('Программа Вас не поняла, повторите попытку.')
            a = input('Введите ответ:  ')
    except ValueError as e:
        print('Произошла ошибка ввода данных! Пожалуйста, введите данные согласно инструкции!')
        time.sleep(5)
        print(hello_msg)
        a = input('Введите ответ:   ')

try:
    bot = Bot(token=Token)
    dp = Dispatcher()
    async def main():
        bot = Bot(token=Token)
        dp = Dispatcher()
        dp.include_router(user_router)
        await dp.start_polling(bot)
except:
    print('Что-то пошло не так! Скорее всего, проблема с API TOKEN! Пожалуйста, перепроверьте его!')
    time.sleep(20)
    exit()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('You have killed script!')
        time.sleep(10)
    except aiogram.exceptions.TelegramNetworkError:
        print('Бот не начал свою работу! Проверьте подключение к интернету и перезапустите программу!')
        time.sleep(100)
        exit()
    except RuntimeError:
                print('You have killed script!')
                time.sleep(10)
                exit()
    except:
        print('Возникла проблема! Проверьте, ввели ли Вы все данные в бот по инструкции верно и перезапустите программу! ')
        print(f'Если проблема не устраняется, обратитесь в поддержку по ссылке:  {support_link}')
        time.sleep(100)
        exit()