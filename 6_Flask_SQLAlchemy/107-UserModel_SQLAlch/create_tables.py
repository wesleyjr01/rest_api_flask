import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

u = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(u)

i = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(i)

connection.commit()

connection.close()
