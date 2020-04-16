"""
    Whenever we insert data, we have to tell the connection
    to actually save all of our changes into the disc, into 
    the data.db file, by doing connection.commit(), and than
    closing the connection to make sure it is not going to 
    receive any more data.
"""

import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_urs_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
create_items_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_urs_table)
cursor.execute(create_items_table)

connection.commit()

connection.close()
