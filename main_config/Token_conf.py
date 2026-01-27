import sqlite3

try:
    db = sqlite3.connect('Database.db')
    cur = db.cursor()
    cur.execute(f'''SELECT Token FROM TOKEN''')
    data = cur.fetchall()
    db.commit()
    db.close()
    Token = f'{str(data[0][0])}'
except:
    Token = 'CHANGEME'
