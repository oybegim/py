import sqlite3 as sql
a = sql.connect("O'quvchilar.db")
b = a.cursor()
b.execute(""" 
CREATE TABLE IF NOT EXISTS Talabalar(
    ism TEXT
    familiya TEXT
    ochestva TEXT
    yosh INTEGER
)
""")

b.execute("""
CREATE TABLE IF NOT EXISTS Abituriyentlar(
    ism TEXT
    familiya TEXT
    yosh INTEGER
)
""")