# from App.models import User
# from App.database import db
# from sqlalchemy.exc import IntegrityError

# def create_user(username, password):
#     new_user = User(username=username, password=password)
#     db.session.add(new_user)
#     try:
#         db.session.commit()
#     except IntegrityError:
#         db.session.rollback()
#         print("Username already exists. Please choose a different username.")

# def get_user_by_username(username):
#     return User.query.filter_by(username=username).first()

# def get_user(id):
#     return User.query.get(id)

# def get_all_users():
#     return User.query.all()

# def get_all_users_json():
#     users = User.query.all()
#     if not users:
#         return []
#     users = [user.get_json() for user in users]
#     return users

# def update_user(id, username):
#     user = get_user(id)
#     if user:
#         user.username = username
#         db.session.add(user)
#         try:
#             db.session.commit()
#         except IntegrityError:
#             db.session.rollback()
#             print("Username already exists. Please choose a different username.")
#         return user
#     return None


#Test
# from App.models import User
# from App.database import db
# from sqlalchemy.exc import IntegrityError

# def create_user(username, password):
#     new_user = User(username=username, password=password)
#     db.session.add(new_user)
#     try:
#         db.session.commit()
#     except IntegrityError:
#         db.session.rollback()
#         print("Username already exists. Please choose a different username.")

# def get_user_by_username(username):
#     return User.query.filter_by(username=username).first()

# def get_user(id):
#     return User.query.get(id)

# def get_all_users():
#     return User.query.all()

# def get_all_users_json():
#     users = User.query.all()
#     if not users:
#         return []
#     users = [user.get_json() for user in users]
#     return users

# def update_user(id, username):
#     user = get_user(id)
#     if user:
#         user.username = username
#         db.session.add(user)
#         try:
#             db.session.commit()
#         except IntegrityError:
#             db.session.rollback()
#             print("Username already exists. Please choose a different username.")
#         return user
#     return None

# Test2
from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_user(username, password):
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    try:
        db.session.commit()
        print(f"User '{username}' created successfully.")
    except IntegrityError:
        db.session.rollback()
        print(f"Error: Username '{username}' is already in use. Please choose a different username.")
        raise  # Raise exception to be handled in the CLI command
    except Exception as e:
        db.session.rollback()
        print(f"An unexpected error occurred while creating the user: {e}")
        raise  # Raise exception for unexpected errors
    
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    return [user.get_json() for user in users]

from App.models import User

def list_users():
    users = User.query.all()  # Fetch all users from the database
    user_list = []
    
    # Prepare the header and user details
    header = f"{'User ID':<10} {'Username':<20}"
    separator = "=" * 30
    user_list.append(separator)
    user_list.append(header)
    user_list.append(separator)

    # Add each user's details to the list
    for user in users:
        user_list.append(f"{user.id:<10} {user.username:<20}")

    user_list.append(separator)  # Decorative line at the end
    return "\n".join(user_list)  # Join all lines into a single string

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print("Username already exists. Please choose a different username.")
        return user
    return None



