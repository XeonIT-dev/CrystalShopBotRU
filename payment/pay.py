from crystalpay_sdk import CrystalPAY
import sqlite3


try:
    db = sqlite3.connect('Database.db')
    cur = db.cursor()
    cur.execute(f'''SELECT * FROM Payment''')
    data = cur.fetchall()
    db.commit()
    db.close()
    Name_kassa = str(data[0][0])
    Private_key = str(data[0][1])
    Salty_key = str(data[0][2])
except:
    Name_kassa = 'CHANGEME' 
    Private_key = 'CHANGEME' 
    Salty_key = 'CHANGEME' 


crystalpayAPI = CrystalPAY(Name_kassa, Private_key, Salty_key)
    