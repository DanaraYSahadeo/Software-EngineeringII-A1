import click
import pytest
import sys
import csv
from sqlalchemy.exc import IntegrityError
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from App.database import db, get_migrate
from App.models import User, Competition, Results
from App.main import create_app
from App.controllers import (
    create_user, get_user_by_username, get_user, get_all_users, get_all_users_json, list_users, update_user,
    add_competition, get_competition_by_name, get_competition, get_all_competitions, get_all_competitions_json, 
    update_competition, list_competitions, create_result, get_result, get_all_results, get_all_results_json, update_result, view_results
)

app = create_app()
migrate = get_migrate(app)

@app.cli.command("import_data", help="Imports data from data.csv into the database")
def import_data():
    try:
        with open('data.csv', encoding='unicode_escape') as csvfile:
            reader = csv.DictReader(csvfile)
            success_count = 0  # To track successful imports

            for row in reader:
                # Ensure all necessary fields are present
                if not all(k in row for k in ['username', 'competition_name', 'results']):
                    continue  # Skip rows with missing fields
                
                try:
                    # Create or get user
                    user = get_user_by_username(row['username'])
                    if not user:
                        create_user(row['username'], row.get('password', 'default_password'))

                    # Create or get competition
                    competition = get_competition_by_name(row['competition_name'])
                    if not competition:
                        add_competition(row['competition_name'])

                    # Create and add result
                    result = Results(
                        username=row['username'],
                        competition_name=row['competition_name'],
                        results=row['results']
                    )
                    db.session.add(result)
                    success_count += 1  # Increment count for each successful import

                except Exception:
                    db.session.rollback()
                    continue  # Skip to the next row in case of error

            db.session.commit()
            if success_count > 0:
                print(f'Data imported successfully: {success_count} entries added.')
            else:
                print('No valid data to import.')

    except FileNotFoundError:
        print("data.csv file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

@app.cli.command("init", help="Creates and initializes the database")
def init():
    db.drop_all()
    db.create_all()
    print('Database initialized')

user_cli = AppGroup('user', help='User object commands')

@user_cli.command("create", help="Creates a user")
@click.argument("username")
@click.argument("password")
def create_user_command(username, password):
    try:
        create_user(username, password)
        print(f"User '{username}' added successfully.")
    except IntegrityError:
        print(f"Error: Username '{username}' is already in use. Please choose a different username.")

@user_cli.command("list", help="Lists usernames in the database")
@click.argument("format", default="string")
def list_user_command(format):
    user_list_output = list_users()  
    print(user_list_output)  

@user_cli.command("create_competition", help="Creates a competition")
@click.argument("competition_name")
def create_competition_command(competition_name):  
    add_competition(competition_name)  

@user_cli.command("list_competitions", help="Lists all competitions")
def list_competitions_command():
    list_competitions()

@user_cli.command("view_results", help="View competition results")
@click.argument('identifier', required=False)
def view_results_command(identifier):
    view_results(identifier)

app.cli.add_command(user_cli)

if __name__ == "__main__":
    app.run()

test = AppGroup('test', help='Testing commands')

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

app.cli.add_command(test)


