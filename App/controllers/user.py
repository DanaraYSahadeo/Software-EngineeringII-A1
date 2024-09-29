from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_user(username, password, role='student'): # Create a new user with the given username, password, and role.
    if role not in ['admin', 'student']:
        print("Error: Role must be either 'admin' or 'student'.")
        return None
    new_user = User(username=username, password=password, role=role)
    db.session.add(new_user)
    try:
        db.session.commit()
        print(f"User '{username}' created successfully with role '{role}'.")
        return new_user
    except IntegrityError: # If username is taken- error message
        db.session.rollback()
        print(f"Error: Username '{username}' is already in use. Please choose a different username.")
        return None
    except Exception as e: 
        db.session.rollback()
        print(f"An unexpected error occurred while creating the user: {e}")
        return None

def get_user_by_username(username): # Return the first user that matches the username.
    return User.query.filter_by(username=username).first()

def get_user(id): # Return user with specified id.
    return User.query.get(id)

def get_all_users(): # Return list of users.
    return User.query.all()

def get_all_users_json(): # Return all users in JSON format without role.
    users = User.query.all()
    return [{'id': user.id, 'username': user.username} for user in users]  

def list_users(): # Fetch all users from the database.
    users = User.query.all()
    user_list = []

    header = f"{'User ID':<10} {'Username':<20} {'Role':<10}"
    separator = "=" * 50
    user_list.append(separator)
    user_list.append(header)
    user_list.append(separator)

    # Add each user's details to the list
    for user in users:
        user_list.append(f"{user.id:<10} {user.username:<20} {user.role:<10}")

    user_list.append(separator)
    return "\n".join(user_list)

def update_user(id, username, role=None): # Update username and optionally role by id.
    user = get_user(id)
    if user:
        user.username = username
        if role in ['admin', 'student']:
            user.role = role  # Update role if specified
        db.session.add(user)
        try:
            db.session.commit()
            print(f"User '{username}' updated successfully.")
        except IntegrityError:
            db.session.rollback()
            print("Username already exists. Please choose a different username.")
        return user
    return None



