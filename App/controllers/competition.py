# from App.models import Competition
# from App.database import db

# def create_competition(name, location, description=None):
#     new_competition = Competition(name=name, location=location, description=description)
#     db.session.add(new_competition)
#     db.session.commit()
#     return new_competition

# def get_competition_by_name(name):
#     return Competition.query.filter_by(name=name).first()

# def get_competition(id):
#     return Competition.query.get(id)

# def get_all_competitions():
#     return Competition.query.all()

# def get_all_competitions_json():
#     competitions = Competition.query.all()
#     if not competitions:
#         return []
#     competitions = [competition.get_json() for competition in competitions]
#     return competitions

# def update_competition(id, name, location, description=None):
#     competition = get_competition(id)
#     if competition:
#         competition.name = name
#         competition.location = location
#         competition.description = description
#         db.session.add(competition)
#         db.session.commit()
#         return competition
#     return None

# def list_competitions():
#     try:
#         with open('data.csv', encoding='unicode_escape') as csvfile:
#             reader = csv.DictReader(csvfile)
#             competitions = set()
#             for row in reader:
#                 competitions.add(row['competition_name'])
#             print(f"{'Competition Name':<30}")
#             for i, competition in enumerate(competitions, 1):
#                 print(f"{i:<5} {competition:<30}")
#     except FileNotFoundError:
#         print("data.csv file not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# import csv
# from App.models import Competition
# from App.database import db

# def create_competition(name, location, description=None):
#     new_competition = Competition(name=name, location=location, description=description)
#     db.session.add(new_competition)
#     db.session.commit()
#     return new_competition

# def get_competition_by_name(name):
#     return Competition.query.filter_by(name=name).first()

# def get_competition(id):
#     return Competition.query.get(id)

# def get_all_competitions():
#     return Competition.query.all()

# def get_all_competitions_json():
#     competitions = Competition.query.all()
#     competitions = [competition.get_json() for competition in competitions]
#     return competitions

# def update_competition(id, name, location, description=None):
#     competition = get_competition(id)
#     if competition:
#         competition.name = name
#         competition.location = location
#         competition.description = description
#         db.session.add(competition)
#         db.session.commit()
#         return competition
#     return None

# def list_competitions():
#     try:
#         with open('data.csv', encoding='unicode_escape') as csvfile:
#             reader = csv.DictReader(csvfile)
#             competitions = set()
#             for row in reader:
#                 competitions.add(row['competition_name'])
#             print(f"{'Competition Name':<30}")
#             for i, competition in enumerate(competitions, 1):
#                 print(f"{i:<5} {competition:<30}")
#     except FileNotFoundError:
#         print("data.csv file not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# Test
# import csv
# from App.models import Competition
# from App.database import db

# def create_competition(competition_name):
#     new_competition = Competition(competition_name=competition_name)
#     db.session.add(new_competition)
#     db.session.commit()
#     return new_competition

# def get_competition_by_name(competition_name):
#     return Competition.query.filter_by(competition_name=competition_name).first()

# def get_competition(id):
#     return Competition.query.get(id)

# def get_all_competitions():
#     return Competition.query.all()

# def get_all_competitions_json():
#     competitions = Competition.query.all()
#     competitions = [competition.get_json() for competition in competitions]
#     return competitions

# def update_competition(id, competition_name):
#     competition = get_competition(id)
#     if competition:
#         competition.competition_name = competition_name
#         db.session.add(competition)
#         db.session.commit()
#         return competition
#     return None

# def list_competitions():
#     try:
#         with open('data2.csv', encoding='unicode_escape') as csvfile:
#             reader = csv.DictReader(csvfile)
#             competitions = set()
#             for row in reader:
#                 competitions.add(row['competition_name'])
#             print(f"{'Competition Name':<30}")
#             for i, competition in enumerate(competitions, 1):
#                 print(f"{i:<5} {competition:<30}")
#     except FileNotFoundError:
#         print("data.csv file not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# Test2
from App.models import Competition
from App.database import db
from sqlalchemy.exc import IntegrityError

def add_competition(competition_name):  
    try:
        new_competition = Competition(competition_name=competition_name)
        db.session.add(new_competition)
        db.session.commit()
        print(f"Competition '{competition_name}' created successfully.")
    except IntegrityError:
        db.session.rollback()
        print(f"Error: Competition '{competition_name}' already exists. Please choose a different name.")
    except Exception as e:
        db.session.rollback()
        print(f"An unexpected error occurred while creating the competition: {e}")


def get_competition_by_name(competition_name):
    return Competition.query.filter_by(competition_name=competition_name).first()

def get_competition(id):
    return Competition.query.get(id)

def get_all_competitions():
    return Competition.query.all()

def get_all_competitions_json():
    competitions = Competition.query.all()
    return [competition.get_json() for competition in competitions]

def update_competition(id, competition_name):
    competition = get_competition(id)
    if competition:
        competition.competition_name = competition_name
        db.session.add(competition)
        db.session.commit()
        return competition
    return None

def list_competitions():
    # Retrieve all competitions and create a set for unique names
    competitions = {comp.competition_name for comp in get_all_competitions()}

    # Sort the competition names for better readability
    sorted_competitions = sorted(competitions)

    # Print header with a decorative line
    print("=" * 40)
    print(f"{'No.':<5} {'Competition Name':<30}")
    print("=" * 40)

    # Enumerate over unique sorted competition names and print them
    for index, competition_name in enumerate(sorted_competitions, start=1):
        print(f"{index:<5} {competition_name:<30}")

    print("=" * 40)  # Decorative line at the end
