### RPG Refactor

* We learned a lot about SQL CRUD today but for tonights exercise we will be staying away from SQL
* Instead we will be focusing on using Object Oriented Programming alongside the MVC design pattern to build an app.
* We will be specifically focused on the Views and Controllers in this assignment and not so much the Models (since they talk to the DB)

#### Objectives

* Refactor your RPG game from the weekend
* You will be making a new python file for views
* You will be making a new python file for controllers
* Remember you will need to import the `class View` from the view.py while
* Make sure all your print and input statements that are intended for the User will be in the `Views`
* Your controller will hold the game logic

***Importing Example***

```
from view import (className)

class controllerClassName:
	
	def __init__(self):
		self.view = className()
```
* After you are done think about how you will build out your game further
* Write out User Stories and Pseudo Code how you will save user data. `("THIS IS JUST PLANNING FOR TOMORROW")`
	* What will the table look like? 
	* What will the columns be? 
	* What will the queries look like for the interaction? 
	* Can a user login? Will they have a username and password?
	
***Notes***

* **DO NOT** copy and paste your old code. If you would like to bring over things that you did have your old code up for reference but please make sure to type everything out. It will not only help you memorize your process but it acts as a review of what everything is doing and how they are all connected