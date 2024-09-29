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
    update_competition, list_competitions, create_result, get_result, get_all_results, get_all_results_json, update_result, view_results, add_result_for_user
)

app = create_app()
migrate = get_migrate(app)

# Command to import data from CSV :- flask import_data "username"
@app.cli.command("import_data", help="Imports data from data.csv into the database")
@click.argument("admin_username")  # Admin username as an argument for authentication
def import_data(admin_username):
    # Check if the user is an admin
    admin_user = get_user_by_username(admin_username)
    if not admin_user or not admin_user.is_admin():
        print("Error: You do not have permission to import data. Only admins can perform this action.")
        return

    try:
        with open('data.csv', encoding='unicode_escape') as csvfile:
            reader = csv.DictReader(csvfile)
            success_count = 0  # Track successful imports

            for row in reader:
                print(f"Processing row: {row}")  # Debugging output
                if not all(k in row for k in ['username', 'competition_name', 'results']):
                    print(f"Skipping row due to missing fields: {row}")  
                    continue
                
                try:
                    # Create or get user (assuming all users are students)
                    user = get_user_by_username(row['username'])
                    if not user:
                        create_user(row['username'], row.get('password', 'default_password'))  # Default role is student

                    # Create or get competition
                    competition = get_competition_by_name(row['competition_name'])
                    if not competition:
                        add_competition(row['competition_name'], admin_user)  # Admin context for adding competitions

                    # Create and add result
                    result = Results(
                        username=row['username'],
                        competition_name=row['competition_name'],
                        results=row['results']
                    )
                    db.session.add(result)
                    success_count += 1  

                except Exception as e:
                    db.session.rollback()
                    print(f"Error processing row: {row}, error: {e}")  
                    continue

            db.session.commit()
            if success_count > 0:
                print(f'Data imported successfully: {success_count} entries added.')
            else:
                print('No valid data to import.')

    except FileNotFoundError:
        print("data.csv file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Command to initialize the database :- flask init
@app.cli.command("init", help="Creates and initializes the database")
def init():
    db.drop_all()
    db.create_all()
    print('Database initialized')

user_cli = AppGroup('user', help='User object commands')

# Command to create a user :- flask user create "username" "password" "role(admin/student)"
@user_cli.command("create", help="Creates a user")
@click.argument("username")
@click.argument("password")
@click.argument("role", default="student")
def create_user_command(username, password, role):
    """Creates a user with specified username, password, and role."""
    user = create_user(username, password, role)
    if user:
        print(f"User '{username}' added successfully with role '{role}'.")

# Command to list usernames :- flask user list
@user_cli.command("list", help="Lists usernames in the database")
@click.argument("format", default="string")
def list_user_command(format):
    user_list_output = list_users()  
    print(user_list_output)  

# Command to create a competition :- flask user create_competition "competition_name"
@user_cli.command("create_competition", help="Creates a competition")
@click.argument("competition_name")
@click.argument("user_username")
def create_competition_command(competition_name, user_username):
    user = get_user_by_username(user_username)
    if user and user.is_admin():
        add_competition(competition_name, user)
    else:
        print("Error: Only admins can create competitions.")

# Command to list competitions :- flask user list_competitions
@user_cli.command("list_competitions", help="Lists all competitions")
def list_competitions_command():
    list_competitions()

# Command to add a result :- flask user add_result "admin_username" "username" "result" "competition_name"
@user_cli.command("add_result", help="Adds a result for a specified user and competition")
@click.argument("admin_username")  
@click.argument("username")  
@click.argument("result")  
@click.argument("competition_name") 
def add_result_command(admin_username, username, result, competition_name):
    """Command to add a result for a specified user and competition, checking for admin permissions."""
    # Check if the user is an admin
    admin_user = get_user_by_username(admin_username)
    if not admin_user or not admin_user.is_admin():
        print("Error: You do not have permission to add results. Only admins can perform this action.")
        return

    if not username or not competition_name or not result:
        print("Username, competition name, and result must all be specified.")
        return

    # Add the result using the updated function
    add_result_for_user(username, result, competition_name, admin_user)


# Command to view results (specified by username or competition name) :- flask user view_results "competition_name" OR "username"
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


