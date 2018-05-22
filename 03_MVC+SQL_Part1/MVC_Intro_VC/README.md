# Models Views Controllers(Mini Lesson)

### Learning Objectives
***Students Will Be Able To...***

* Diagram the MVC concept taking input from a browser and passing it through a url router. 

---

### Context

* The MVC concept is a design pattern found throughout many frameworks on the front and back end. 

---

### Lesson

#### Part 1 - What is MVC?

* The MVC concept is a popular design pattern meant to help programmers keep their code organized.
* There are three parts to this pattern
	* Models - Interact with your database
	* Views - Presents information to the end user
	* Controllers - Application Logic

***Why is this helpful? How is this more organized?***

* By following this pattern you will be able to search through, read, and edit your code much easier. 
* An added benefit to this patterns popularity is that collaboration between programmers will also be easier. 
* If you found an error in your code you will be able to locate it and debug it much faster. For example if the user sees something they are not supposed to see, you will check the "views" file first
* For the purposes of todays exercises we will be focusing strictly on the interaction between the Views and the Controllers. 

![](https://s3.amazonaws.com/nettuts/613_mvc/diagram.jpg)

#### Part 2 - Views

* Your views class/classes represent the information the user sees
* This is where your `input` and `print` methods will go
* The goal of your views methods will be to take arguments from the database to show to the user. `(Remember we can pass information between methods by invoking them with arguments)`
* Little to no logic should go in the views. It's main goal is to show the end user data and take in user input

#### Part 3 - Controllers

* This is where your main logic will go
* In the example of your RPG terminal game you may put your `class Game` or `class Quest` inside this file. 

#### Part 4 - Models 

* Models will be a python file where we will make our SQL calls
* Connecting our Models to SQL is something we will touch upon tomorrow

***Note***

* All these files will be able to access each other by using Python `imports`

#### Required Reading
[https://study.cs50.net/mvc](https://study.cs50.net/mvc)
