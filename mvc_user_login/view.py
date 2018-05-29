class View:

#NO INIT 
	def v_login(self):
		username = input("username:")
		password = input("password:")
		return username, password

	def tell_user_status(self,validation, user):
		if len(validation) == 0:
			print("I am sorry " + str(user.username) + " but you are not in the Database")
			return int(input("would you like to register yes[1] or no[3] "))
		else:
			print("welcome back " + str(user.username) +"!!")
			return int(input("do you want to add info to profile yes[2] or sign out[3] "))

	def logged_in(self, user):
		print("you have successfully made a username and password " + str(user.username))
		profile_info = int(input("you want to add info to profile[1] or sign out[2] "))
		if profile_info == 1:
			self.get_profile_info(user)
		else:
			self.goodbye(user.username)

	def get_profile_info(self, user):
		print("hello "+ str(user.username) + "!!!")
		print("WOW" + str(user.password) + "!!!")
		user.first_name = input("what is your first name? ")
		user.last_name = input("what is your last name? ")
		user.dob = input("what is your date of birth (ie 12-03-2004? ")
		user.phone_num = input("what is your phone number ")
		user.address = input("do you have an address to add ")
		return user

	def goodbye(self, user):
		print("ok come back again " + user.username)







		# def ask_phone_address()
	# 	phone = input("do you have a phone number you would like to include?")
	# 	address = input("do you have an address you would like to include?")
	# 	return phone, address