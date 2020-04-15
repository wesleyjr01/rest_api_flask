import sqlite3

"""
    The cursor is reponsable for actually executing the queries,
    and also storing the result. So the cursor is going to run a
    query and then store the result, so we can acess the result.
"""

# URI - Unifier Resource Identifier
connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "joe", "asdf")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, "rolf", "asdf"),
    (3, "anne", "xyz"),
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

"""
    Whenever we insert data, we have to tell the connection
    to actually save all of our changes into the disc, into 
    the data.db file, by doing connection.commit(), and than
    closing the connection to make sure it is not going to 
    receive any more data.
"""
connection.commit()

connection.close()
