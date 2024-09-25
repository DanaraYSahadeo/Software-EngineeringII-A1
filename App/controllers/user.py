from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_user(username, password):
    new_user = User(username=username, password=password) # Create a new user 
    db.session.add(new_user)
    try:
        db.session.commit()
        print(f"User '{username}' created successfully.") # Success message
    except IntegrityError: # Integrity error handling
        db.session.rollback()
        print(f"Error: Username '{username}' is already in use. Please choose a different username.")
        raise  
    except Exception as e: # Unexpected error handling
        db.session.rollback()
        print(f"An unexpected error occurred while creating the user: {e}")
        raise  
    
def get_user_by_username(username): # Return first user that matches the username
    return User.query.filter_by(username=username).first()

def get_user(id): # Return user with specified id
    return User.query.get(id)

def get_all_users(): # Return list of users
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    return [user.get_json() for user in users]

def list_users(): # Fetch all users from the database
    users = User.query.all() 
    user_list = []
    
    header = f"{'User ID':<10} {'Username':<20}"
    separator = "=" * 30
    user_list.append(separator)
    user_list.append(header)
    user_list.append(separator)

    # Add each user's details to the list
    for user in users:
        user_list.append(f"{user.id:<10} {user.username:<20}")

    user_list.append(separator)  
    return "\n".join(user_list)  

def update_user(id, username): # Update username by id
    user = get_user(id) # Fetch the user through their id
    if user:
        user.username = username # Update username
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print("Username already exists. Please choose a different username.")
        return user
    return None



