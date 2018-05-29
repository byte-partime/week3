import model
import view

class Controller:
	def __init__(self):
		

		self.view = view.View()
		self.model = model.Model()
		self.user = model.User()

	def start(self):
		self.login()

	def login(self): 
		login_tupple = self.view.v_login()
		# print(login_tupple)
		username = login_tupple[0]
		password = login_tupple[1]
		print(username, password)
		validation = self.model.validate(username,password)
		
		self.user.user_id = validation[0]
		print("this that user ID in controller",self.user.user_id)
		self.user.username = validation[1]
		self.user.password = validation[2]		

		register_decision = self.view.tell_user_status(validation, self.user)
		if register_decision == 1:
			login_tupple = self.view.v_login()
			username = login_tupple[0]
			password = login_tupple[1]
			print("login tupple", username, password)
			user_id, username, password = self.model.create_user(username, password, "customer")
			print("controller user_id", user_id)
			print("controller username:", username)
			print("controller password:", password)
			self.user.user_id
			self.user.username = username 
			self.user.password = password 
			print("self.user.user_id: ",self.user.user_id)
			print("self.user.username: ",self.user.username)
			print("self.user.password: ",self.user.password)
			print("this is entire self.user: ", self.user)

			self.view.logged_in(self.user)
	
		elif register_decision == 2:
			user = self.view.get_profile_info(self.user)
			print("the entire user profile:", user)
			print("user.address!!!", user.address)
			self.model.fill_in_profile(user)

		else:
			self.view.goodbye(self.user)

		
			
		
#ONLY CALL SELF.USER ONCE TO CREATE THE USER OBJ W/ALL THE ATTRIBUTES that can be changed/manipulated

	# def ask_more(self, username)
	# 		self.view.ask_phone_address(username)

		# else:
			# self.views.goodbye()





controlla = Controller()
controlla.start()