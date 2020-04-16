import sqlite3


# Open database
conn = sqlite3.connect('database.db')

# Create table

conn.execute('''DROP TABLE IF EXISTS user''')
conn.execute('''DROP TABLE IF EXISTS votes''')


conn.execute('''CREATE TABLE user(id INTEGER  PRIMARY KEY, username VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL, name VARCHAR(100) NOT NULL  )''')
conn.execute(
    '''CREATE TABLE votes(id INTEGER PRIMARY KEY, username VARCHAR(100) NOT NULL, vote VARCHAR(100) NOT NULL)''')


# Create an admin user
conn.execute(
    '''INSERT INTO user(username, password, name) VALUES("admin", "admin", "admin")''')
conn.commit()

# Close database cursor
conn.close()
