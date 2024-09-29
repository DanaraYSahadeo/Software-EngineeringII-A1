# Introduction

Hi, my name is Danara Sahadeo and this is my interpretation of a Competitions Platform for COMP 3616: Software Engineering II.

# Flask Commands

1. flask init
2. flask import_data "username"

After initializing and importing the database, you the user can enter any of these commands in the CLI:

1. flask user create "username" "password" "role(admin/student)":- to create a user
2. flask user list :- to list the users
3. flask user create_competition "Competition Name" "admin_username":- to create a competition
4. flask user add_result "admin_username" "username" "result" "competition_name"
5. flask user list_competitions :- to list all competitions
6. flask user view_results :- to view results based on a username or a competition name

# Features Implemented 

1. Create Competition
2. Import competition results from file (data.csv)
3. View competitions list
4. View competition results
5. Add results 

# Running the Project

_For development run the serve command (what you execute):_
```bash
$ flask run
```

_For production using gunicorn (what the production server executes):_
```bash
$ gunicorn wsgi:app
```

# Deploying
You can deploy your version of this app to render by clicking on the "Deploy to Render" link above.

# Initializing the Database
When connecting the project to a fresh empty database ensure the appropriate configuration is set then file then run the following command. This must also be executed once when running the app on heroku by opening the heroku console, executing bash and running the command in the dyno.

```bash
$ flask init
```

# Database Migrations
If changes to the models are made, the database must be'migrated' so that it can be synced with the new models.
Then execute following commands using manage.py. More info [here](https://flask-migrate.readthedocs.io/en/latest/)

```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
$ flask db --help
```

# Testing 

## Unit & Integration
Unit and Integration tests are created in the App/test. You can then create commands to run them. Look at the unit test command in wsgi.py for example

```python
@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "User"]))
```

You can then execute all user tests as follows

```bash
$ flask test user
```

You can also supply "unit" or "int" at the end of the comand to execute only unit or integration tests.

You can run all application tests with the following command

```bash
$ pytest
```

## Test Coverage

You can generate a report on your test coverage via the following command

```bash
$ coverage report
```

You can also generate a detailed html report in a directory named htmlcov with the following comand

```bash
$ coverage html
```

