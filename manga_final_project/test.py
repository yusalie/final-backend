import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('SELECT * FROM manga')
y = cur.fetchall()

for i in y:

    print(y)