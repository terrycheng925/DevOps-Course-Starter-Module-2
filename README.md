

# DevOps Apprenticeship: Project Exercise





## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.



## Prerequisite to run the app

1. Registrated Trello account and created a board_ID,
2. Gengerated API Key and Token.
   
   #### To get a board id, use post man or curl command, e.g. https://api.trello.com/1/members/me/boards?fields=name,url&key={{APIKey}}&token={{APIToken}}
3. Update the .env file with this entries, example as : 

    `TRELLO_API_KEY=`xxxxxxxx1234

    `TRELLO_API_TOKEN=`xxxxxxx123456789xxxx

    `TRELLO_BOARD_ID=`xxxxxx123456


4. Trello end point spec here : https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-put





## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.


New for Dockerfile
========
- add the dockerfile ( however currently it can only be run with flask in Docker )
- ensure the machines instill docker desktop which and run docker command.

to build docker image : ( in the same folder : e.g. DevOps-Course-Starter-Moudule-2)

to build development and production, run the following command 

Develpment :
$ docker build --target development --tag todo-app:dev . 
$ docker run -d -p 5000:5000 --env-file .env todo-app:dev

Production : 
$ docker build --target production --tag todo-app:prod .
$ docker run -d -p 5000:5000 --env-file .env todo-app:dev

and then in borswer : localhost:5000