import sqlite3
from colorama import Fore


try:
    db = sqlite3.connect('Database.db')
    cur = db.cursor()
    cur.execute(f'''SELECT code_death FROM Other_data''')
    free = cur.fetchall()
    code_death = str(free[0][0])
    db.commit()
    db.close()
except:
    code_death = 'usWJGw7Rdy!pmqg!OhGjYhme9XIMimCj1KIkN4#K1CfhJ!4erzqSkSiCwX$'
    print(Fore.RED + f'Вы используете обычный, пакетный код "смерти"! Пожалуйста, поменяйте его...')
