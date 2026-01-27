import sqlite3
from colorama import Fore

try:
    db = sqlite3.connect('Database.db')
    cur = db.cursor()
    cur.execute(f'''SELECT link FROM Link_change''')
    data = cur.fetchall()
    db.commit()
    db.close()
    photo_path1 = str(data[0][0])
except:
    print(Fore.RED + 'Ошибка импорта фотографии! Сейчас используется стандартная! Проверьте путь на картинку, введенный раннее...')
    photo_path = 'logo.jpg'
