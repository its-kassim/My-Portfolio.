import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEES(
ID INTEGER PRIMARY KEY NOT NULL ,
NAME TEXT NOT NULL,
AGE INTEGER NOT NULL,
SALARY REAL NOT NULL);
''')

print("Table created successfully")
conn.close()
