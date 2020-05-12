#### Objectives
-   Solidify Routing Concepts through Drawing a Wireframe
-   Build a RESTful Web Application

## Wireframe
-   how does the user navigate through our application?
-   when the user sends a request, how to respond?

## RESTful Web App
-   "representational state transfer"
-   url corresponds to it's own object ie. task/21 looks to our 21st task
-   GET, PUT, POST, DELETE

#### Task Manager

-  DONE! /tasks/new- GET - method should return a template containing the form for adding a new TV show  
-  DONE! /tasks/create - POST - method should add the show to the database, then redirect to /tasks 
-  DONE! /task/:id - GET - method should return a template that displays the specific show's information
-  DONE! /tasks - GET - method should return a template that displays all the tasks in a table  /tasks
-  DONE! /edit/:id - GET - method should return a template that displays a form for editing the TV show with the id specified in the url  /tasks
-  DONE! /update/:id - POST - method should update the specific show in the database, then redirect to /tasks
-  DONE! /tasks/:id/complete - GET - method should delete the show with the specified id from the database, then redirect to /tasks  Have your root route redirect to /tasks