# Bank Your Market Cash!

In this exercise you will be building an application that is the combination of the Terminal Trader app and the Banking Software app from earlier this week. 

##### Prompts

* A user should be able to link their bank credentials to the terminal trader
* A user should be able to withdraw their liquid cash from the terminal trader into their bank accounts
* If a user tries to connect with an account that's not theirs or does not exist they should get an error
* If they try to withdraw more than what they have in the bank they should get an error

##### Notes

* Keep your database files separate
* PSEUDO CODE, USER STORIES, ERDS!!!!
* Do NOT copy and paste your code from your previous assignments
* Try to add as much object oriented organization as possible. It will save you time, frustration, and lower your `technical debt`. 


##### Additional Features and Luxury Goals

* These are luxury goals you might think about incorporating should you finish the above assignment and feeling sassy
* Add [Options](http://en.wikipedia.org/wiki/Option_(finance)) to the type of equity assets a user can buy. The most common types of options are [put options](http://en.wikipedia.org/wiki/Put_option) and [call options](http://en.wikipedia.org/wiki/Call_option).
* Allow the user to place a [stop-loss order](http://www.investopedia.com/terms/s/stop-lossorder.asp) on any stock they hold in their portfolio
* Save the user's total portfolio value minimum every time they log in, maximum once a day. Graph this data in terminal using something like Blessings or even better, generate a SVG using Python's super intuitive plotting library [Matplotlib](http://matplotlib.org/)
* Add Crypto-currency, ie. Bitcoin, to the type of assets a user can buy. Use the [Coinmarketcap api](http://coinmarketcap-nexuist.rhcloud.com/) to get this data. See also [Coinmarketcap.com](http://www.coinmarketcap.com)