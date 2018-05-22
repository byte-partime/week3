import sqlite3

conn = sqlite3.connect('databasename.db')
print "Opened database successfully";

cursor = conn.execute("SELECT id, movie, character, year FROM movie")
for row in cursor:
   print "ID = ", row[0]
   print "MOVIE = ", row[1]
   print "CHARACTER = ", row[2]
   print "YEAR = ", row[3], "\n"

print "Operation done successfully";
conn.close()