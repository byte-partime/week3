import sqlite3

conn = sqlite3.connect('databasename.db')

conn.execute(
    """
    CREATE TABLE movie (
        id INTEGER PRIMARY KEY, 
        character TEXT,
        movie TEXT,
        year INTEGER
    );
    """
)

conn.commit() # must commit when manipulating the database
conn.close()

print("Your database was created")