import sqlite3

conn = sqlite3.connect("sql1.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS ece(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
def data_entry():
    c.execute("INSERT INTO ece VALUES(1452549219,'2019-01-11 10:30:00','Python',6)")

    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
