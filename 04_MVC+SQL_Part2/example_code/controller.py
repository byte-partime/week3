from models import Models
from views import Views

class Controller:

	def __init__(self):
		self.views = Views()
		self.models = Models()
		self.start()

	def start(self):
		user_info = self.views.get_user_info() # returns a tuple or an list
		check_user = self.models.check_user(user_info[0], user_info[1])
		if check_user == True:
			self.views.show_menu()
		else:
			self.views.get_user_info()
