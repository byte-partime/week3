import sqlite3

conn = sqlite3.connect("rpg.db")

conn.execute(
    """
    CREATE TABLE players (
        id INTEGER PRIMARY KEY, 
        username TEXT,
        password TEXT,
        name TEXT,
        race TEXT,
        hp INTEGER,
        exp INTEGER,
        attack INTEGER,
        weapon TEXT,
        map_index INTEGER
    )
    """
)

conn.commit()
conn.close()

print("Your database was created")
