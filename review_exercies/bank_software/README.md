## Your Own Private Bank

* Welcome back! In this challenge you'll be creating a rich Python terminal app emulating bank software. 
* Make sure to READ EVERYTHING in this markdown before you start coding

#### USER STORIES!!!

* Users can have many accounts
* All users should have to log in with a username and password
* There will be two types of users. Client and Banker
* Banker
	* Will have a higher permission level
	* They will be able to see all accounts
	* They will be able to transfer money between multiple accounts and multiple clients
	* You can create some bankers in a seed file
	* Bankers can make new client accounts
* Clients
	* Will have a lower permission level
	* They should only be able to see accounts in their name
	* They should only be able to transer funds between accounts in their name
	* Clients should be able to register for a login/account


#### Objective 1 - Database

* Draw out your ERD!
* We will have two tables: Users and Accounts
* A user can have many accounts
* Users should have
	* A username to log in
	* A password to log in
	* When they were initially created
	* A permission level
* Accounts should have
	* A number - You can keep this as the primary key since those will be unique
	* A balance
* Use a createdb file and a seed file to help yourself get started

#### Objective 2 - Models

* PLAN THIS OUT.
* Will you have one Models Class or two separate classes? Users as clients and Users and a banker
* A client should be able to:
	* view all their accounts
	* deposit and withdraw from their own account
	* transfer money from one account to another user account
* A banker should be able to:
	* create accounts
	* deposit and withdraw from any user account
	* transfer money between two accounts
* Note
	* A client cannot see the options a banker has
	* A banker cannot have any account associated with them
* Extra
	* Think about organizing it further and having an extra class that will handle only the reading and writing to the database

#### Objective 3 - The Rest of the MVC

* Make sure to follow the MVC pattern to organize your code. 
	
#### Resources

* [Blog about Inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
