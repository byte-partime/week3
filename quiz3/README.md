# Quiz Week3

## Part I

The first part of the quiz will focus on SQL queries.
We will be using the 'sitemetrics.db' file.This is the same database used in our exercices, you will be asked to answer somewhat more nuanced questions.
You may want to make sure you are familiar with operators such as 
'NOT' 'NOT IN' 'DISTINCT'
and subqueries. A subquery, is essentially a temporary table that is nested inside a larger query. The syntax would be:
```SELECT ...
.... FROM (SELECT ...
..);
```
The parenthesis enclose the subquery that is used by the outer query.
Here is a link with some subquery examples:
https://www.tutorialspoint.com/sql/sql-sub-queries.htm

To inspect the database,
open sqlite3 in the terminal, and use the commands (use .help if necessary).

You will create a 'query.sql' file, which will be a script of SQL queries.
You can execute the queries by running:
```
sqlite3 sitemetrics.db < query.sql
```

How many users are there in the database?

How many unique search_term-user pairs are there in the database?

How many users have not searched a single search_term?

How many users have searched for at least one term?

(The answers to the last two questions can be deduced from each other. Try writing a query that answers each question directly)

Who are the top 5 users with the most searches?

Write a query that will return a table with two columns - one displaying a number of searches per user (1, 2, 3 etc.) and the second displaying the corresponding number of users whose total number of searches is the amount in the first column.
(Hint: think how the previous query can be applicable to this query)

## Part II

In the 'real world' one would usually be required to register an API key 
in order to use most web APIs. For the sake of simplicity and to avoid 
possible complications with registration, we will be using a website that
doesn't require registration;
https://pokeapi.co/

The API is:
http://pokeapi.co/api/v2/
or more precisely
http://pokeapi.co/api/v2/ {endpoint}

So for example, to get all the 'berry' items,
we hit the API:
`requests.get("http://pokeapi.co/api/v2/berry").json()`
And so on. Documentation is available at
https://pokeapi.co/docsv2/

We will be working with 3 endpoints:
http://pokeapi.co/api/v2/pokemon/ {id or name}

http://pokeapi.co/api/v2/pokemon-species/ {id or name}

http://pokeapi.co/api/v2/pokemon-habitat/ {id or name}

look these up in the docs.

Your assignment is to create a database with (at least) 4 tables
'user' 'pokemon' 'species' 'habitat'

create a seed.db file seeding at least one user,

The MVC should allow one to add users, add/delete pokemon belonging to a user,
and look up how many pokemon a user/users have, how many by species, and how many by habitat.
Read the docs carefully for the 3 endpoints, in addition to a foreign key
in the pokemon tabe pointing to user, you should think about how to configure
the other two tables in relation to pokemon table.
Is there a many-to-many relationship between any of the tables? If so, how to implement it.
The habitat endpoint includes a list of species that inhabit this habitat.
Does the species endpoint have the corresponding habitat data. What can you
say about the relationship between these two?
When a user adds a pokemon to their account, what other information needs to be updated so that the database contains all the relevant information.
In your logic, think of how to handle requests for non existent data
(trying to add a pokemon that doesn't exist). 