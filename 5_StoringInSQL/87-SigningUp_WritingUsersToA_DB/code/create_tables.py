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

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

connection.commit()

connection.close()
