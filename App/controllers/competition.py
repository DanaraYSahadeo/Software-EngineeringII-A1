from App.models import Competition
from App.database import db
from sqlalchemy.exc import IntegrityError

def add_competition(competition_name): # Add a new competition
    try:
        new_competition = Competition(competition_name=competition_name) # Create a competition
        db.session.add(new_competition)
        db.session.commit()
        print(f"Competition '{competition_name}' created successfully.") # Success message
    except IntegrityError: # If integrity error
        db.session.rollback()
        print(f"Error: Competition '{competition_name}' already exists. Please choose a different name.")
    except Exception as e: # If unexpected error
        db.session.rollback()
        print(f"An unexpected error occurred while creating the competition: {e}")


def get_competition_by_name(competition_name): # Return first matching competition
    return Competition.query.filter_by(competition_name=competition_name).first()

def get_competition(id): # Return competition with specified id
    return Competition.query.get(id)

def get_all_competitions(): # Return list of competitions
    return Competition.query.all()

def get_all_competitions_json():
    competitions = Competition.query.all()
    return [competition.get_json() for competition in competitions]

def update_competition(id, competition_name): # Update competition by id
    competition = get_competition(id) # Get competition by id
    if competition: # Update info
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

    print("=" * 40)
    print(f"{'No.':<5} {'Competition Name':<30}")
    print("=" * 40)

    # Enumerate over unique sorted competition names and print them
    for index, competition_name in enumerate(sorted_competitions, start=1):
        print(f"{index:<5} {competition_name:<30}")

    print("=" * 40)  
