import sqlite3


try:
    db = sqlite3.connect('Database.db')
    cur = db.cursor()
    cur.execute(f'''SELECT * FROM Reviews''')
    data = cur.fetchall()
    db.commit()
    db.close()
    reviews = str(data[0][0])  
    account_link = str(data[0][1])  
    conntact_support = str(data[0][2])  
    redict_url = str(data[0][3])   
except:
    reviews = 'reviews.url/CHANGEME'
    account_link = 't.me/CHANGEME'
    conntact_support = 't.me/CHANGEME' 
    redict_url = 't.me/CHANGEME' 