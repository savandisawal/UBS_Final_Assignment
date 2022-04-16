# Assignment:

Create a RESTful Web Service for with 5 URL mappings.<br/> 
•	Return a list of Employees<br/>
•	Create a new Employee<br/>
•	Return all the Roles<br/>
•	Create a new Role for a User<br/>
•	Associate a Role to a User<br/>

Integration tests<br/>
As an API User,<br/>
Given the User Service<br/>
When I call the first URL mapping, and pass a new User JSON, it’s created on the Service<br/>
<br/>
As an API User,<br/>
Given the User Service<br/>
When I call the third URL mapping, I get a list of Roles<br/>
<br/>
As an API User,<br/>
Given the User Service<br/>
When I call the third URL mapping, I get a list of Users<br/>
<br/>
As an API User,<br/>
Given the User Service<br/>
When I call the fourth URL mapping, and pass a new Role  JSON, it’s created on the Service<br/>
<br/>

As an API User,<br/>
Given the User Service<br/>
When I call the fifth URL mapping, and pass a User-Role association JSON, the concerned role is applied to the User<br/>

## There can be multiple solution to create RESTful Web Servce with different technologies. 
### 1. Using Java and Spring Boot 
### 2. Using Python and Flask framework

## Flowchart:
![Assignment_Flowchart](https://user-images.githubusercontent.com/49858330/163679498-118090e7-be57-4755-b910-d6aaccdbd878.JPG)


## Technologies used
I have used the Python and Flask framework<br/>

* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly.
* **[Flask](https://flask-restful.readthedocs.io/en/latest/)** - A microframework for Python based.
* Pycharm is used as IDE
* Minor dependencies can be found in the requirements.txt file on the root folder.

## Installation / Usage

* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).

* Git clone this repo

    ```bash
    git clone git@github.com:savandisawal/Assignment.git
    ```

* ### Python Modules used:

    Following python modules are used in this assignment:<br/>
	requests<br/>
	flask<br/>
	json<br/>
	unittest<br/>

* ### Install your requirements
  
    ```bash
    $ pip install -r requirements.txt
    ```

* ### Running the Server

    On your terminal, run the server using this one simple command:

    ```bash
    $ main.py
    ```

    You can now access the app on your local browser by using

    ```bash
    http://localhost:5000
    ```

    Following are the endpoints
	```bash
    http://localhost:5000/employees
	http://localhost:5000/roles
    ```
    # How To Execute:
    
    ## Run below file 
    ```bash
    main.py
    ```
    This will start server:-
    ```bash
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```
    ## To execute Tests:
    Open new terminal or new sesion and run below command.
    
    ```bash
    python test.py
    ```
