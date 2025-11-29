# Raidan George
# MO4 Programming Assignment - Modules and Databases
# Exercise 16.8

from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///books.db', echo=True)

conn = engine.connect()

rows = conn.execute(text('SELECT title FROM book ORDER BY title ASC'))

for row in rows:
        print(row[0])

conn.commit()

conn.close()
