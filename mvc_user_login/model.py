import sqlite3
connection = sqlite3.connect('cable.db')
cursor = connection.cursor()


class User:
	def __init__(self,user_id=None,username = None, password=None, first_name=None,last_name=None,dob=None,phone_num=None,address=None):
		self.user_id = user_id
		self.username = username
		self.password = password
		self.first_name = first_name
		self.last_name = last_name
		self.dob = dob
		self.phone_num = phone_num
		self.address = address
	#create
	#read
	#update
	#delete.


class Model:
	def __init__(self):
		self.userwrapper = UserWrapper()

	def validate(self, username, password): 
		validation = self.userwrapper.db_validate(username,password)
		print("in model", validation)
		# print("len of validation:", len(validation))
		if len(validation) == 0: #do with ITEMS
		# if validation == None: #do with ITEM
			print("INVALID")
			return(validation)
		else:
			print("VALID")
			print(validation)
			print(validation[0])
			return validation[0]

	def create_user(self, username, password, permission_level):
		print("in models")
		# print(username, password, permission_level)
		db_user_info = self.userwrapper.db_create_user(username, password, permission_level)
		print("in model", db_user_info[0][0], db_user_info[0][1])
		user_id = db_user_info[0][0]
		username = db_user_info[0][1]
		password = db_user_info[0][2]
		return user_id, username, password

	def fill_in_profile(self, user):
		# print("username",user.username)
		# print("password",user.password)
		# print("first_name",user.first_name)
		# print("first_name",user.last_name)
		# print("dob",user.dob)
		# print("phone_num",user.phone_num)
		# print("address",user.address)
		self.userwrapper.db_fill_in_profile(user)
		self.userwrapper.db_fill_phone_address(user)
		#how can I access method in other class without using self
		#and still being able to access the different attribs


# class Profile:
	#create
	#read
	#update
	#delete


class UserWrapper:

	@staticmethod #doesnt take self
	def db_validate(username, password):
		cursor.execute('''

			SELECT id, username, password from cb_user WHERE username = (?) AND password = (?);
			''',(username, password))

		# db_validation = cursor.fetchone() # DO w/ONE ITEM
		db_validation = cursor.fetchall() #DO w/ITEMSSS
		print("username we in wrapper", db_validation)
		return db_validation

	@staticmethod
	def db_create_user(username, password, permission_level):
		print("in wrapper")
		print(username, password, permission_level)
		cursor.execute('''
			INSERT INTO cb_user (username, password, permission_level) VALUES (?,?,?);
			''',(username, password,permission_level))
		connection.commit() 
		print("user created!")

		cursor.execute('''
			SELECT * FROM cb_user WHERE username = (?);
			''',(username,))
		
		# print(cursor.fetchall())
		db_user_info = cursor.fetchall()
		connection.commit()
		return db_user_info 

	def db_fill_in_profile(self, user):
		print("in model wrapper")
		print("username",user.username)
		print("password",user.password)
		print("first_name",user.first_name)
		print("first_name",user.last_name)
		print("dob",user.dob)
		print("phone_num",user.phone_num)
		print("address",user.address)

		cursor.execute('''
			UPDATE cb_user SET first_name = (?),last_name = (?), date_of_birth = (?) WHERE username = (?);
			''', (user.first_name, user.last_name, user.dob, user.username)
			)
		# print(cursor.fetchall())
		connection.commit()

	def db_fill_phone_address(self,user):
		cursor.execute('''
			INSERT INTO user_info (user_id, phone_number, address) VALUES (?,?,?);
			''', (user.user_id, user.phone_num, user.address))
		connection.commit()



	#SELF GIVES YOU ABILITY TO ACCESS ALL ATTRIBUTES OF AN OBJECT THAT IS PASSED








