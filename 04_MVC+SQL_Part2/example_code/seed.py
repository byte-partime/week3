"""
Seed your database with admins
"""

import sqlite3

db = 'databasename.db'

MOVIES = [
    ["Anna Kendrick", "Soulmate", 2013],
    ["Peter Parker", "Spiderman", 2012],
    ["Peter Parker", "Spiderman", "HELLO"]
]

conn = sqlite3.connect(db)
c = conn.cursor()

print("Destroying old data")
c.execute("DELETE FROM movie")

for movie in MOVIES:
    c.execute("""
        INSERT INTO movie 
        ("character", "movie", "year") 
        VALUES (?, ?, ?)
        """,(movie[0], movie[1], movie[2]))

conn.commit()

c.close()

print("Looks like we're all good")