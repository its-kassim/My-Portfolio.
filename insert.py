import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute("INSERT INTO EMPLOYEES VALUES (14,'PAUL',34,45000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (12,'FAITH ',35,55000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (23,' KARIMI',36,65000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (42,' KARIEMI',37,75000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (52,' KAMI',38,75000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()














