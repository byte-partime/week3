import sqlite3

conn = sqlite3.connect('databasename.db')

class Models:

	def __init__(self):
		pass

	def check_user(self, username, password):
		username = username
		password = password

		c = conn.execute("""
				SELECT * FROM Users
				WHERE username = ?
				AND password = ?;
			"""(username, password))
		user = c.fetchone()
		if user == True:
			pass
		else:
			reject

# conn = sqlite3.connect('databasename.db')
# print("Opened database successfully")

# cursor = conn.execute("""
# 	SELECT * FROM movie;
# 	""")

# print(cursor.fetchall())

# # for row in cursor:
# #    print("ID = ", row[0])
# #    print("NAME = ", row[1])
# #    print("ADDRESS = ", row[2])
# #    print("SALARY = ", row[3], "\n")

# print("Operation done successfully")
# conn.close()