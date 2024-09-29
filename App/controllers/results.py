from App.models import Results
from App.controllers import get_competition_by_name

from App.database import db
from sqlalchemy.exc import IntegrityError

# def create_result(username, competition_name, results): # Create a new result for a user in a competition
#     new_result = Results(username=username, competition_name=competition_name, results=results) # Creating new result 
#     db.session.add(new_result)
#     db.session.commit()
#     return new_result

# def get_result(id): # Return result with specified id
#     return Results.query.get(id)

# def get_all_results(): # Return list of results
#     return Results.query.all()

# def get_all_results_json():
#     results = Results.query.all()
#     return [result.get_json() for result in results]

# def update_result(id, username, competition_name, results): # Update existing result through id
#     result = get_result(id) # Get result by id
#     if result: # Update attributes
#         result.username = username
#         result.competition_name = competition_name
#         result.results = results
#         db.session.add(result)
#         db.session.commit()
#         return result
#     return None

# def view_results(identifier=None): # View results based on competition name or username
#     if identifier:
#         # Check if it's a competition name
#         results_query = Results.query.filter(
#             (Results.competition_name == identifier) |
#             (Results.username == identifier)
#         )
#         results = results_query.all()

#         if results: # Print results if they exist
#             print("=" * 80)
#             print(f"{'Username':<20} {'Competition':<30} {'Results':<20}")
#             print("=" * 80)
#             for result in results:
#                 print(f"{result.username:<20} {result.competition_name:<30} {result.results:<20}")
#             print("=" * 80)
#         else:
#             print("No results found for this competition or username.")
#     else:
#         # If no identifier is provided, list unique competitions
#         competitions = {result.competition_name for result in Results.query.all()}
#         print("=" * 50)
#         print("Available Competitions:")
#         print("=" * 50)
#         for index, comp in enumerate(sorted(competitions), start=1):
#             print(f"{index}. {comp}")
#         print("=" * 50)
#         print("Please enter the command again with a specific competition name or username to view results.")

def create_result(username, competition_name, results, user):  # Create a new result with user role check
    if user.is_admin():  # Only admins can create results
        new_result = Results(username=username, competition_name=competition_name, results=results)
        db.session.add(new_result)
        db.session.commit()
        print(f"Result created successfully for '{username}' in competition '{competition_name}'.")
        return new_result
    else:
        print("Error: Only admins can create results.")
        return None
    
def add_result_for_user(username, result, competition_name, admin_user): 
    """Add a result for a specified username and competition name, ensuring that only admins can add results."""
    if admin_user.is_admin():  # Check if the user is an admin
        if not username or not competition_name or not result:
            print("Error: Username, competition name, and result must all be specified.")
            return

        try:
            competition = get_competition_by_name(competition_name)  # Get the competition by name
            if not competition:
                print(f"Error: Competition '{competition_name}' does not exist.")
                return
            
            # Create and add the result
            new_result = Results(
                username=username,  # Use the specified username
                competition_name=competition_name,
                results=result
            )
            db.session.add(new_result)
            db.session.commit()
            print(f"Result '{result}' added successfully for user '{username}' in competition '{competition_name}'.")
        except Exception as e:
            db.session.rollback()
            print(f"An unexpected error occurred while adding the result: {e}")
    else:
        print("Error: Only admins can add results.")

def get_result(id):
    """Return result with specified id."""
    return Results.query.get(id)

def get_all_results():
    """Return list of results."""
    return Results.query.all()

def get_all_results_json():
    """Return all results in JSON format."""
    results = Results.query.all()
    return [result.get_json() for result in results]

def update_result(id, username, competition_name, results, user):  # Update existing result with user role check
    if user.is_admin():  # Only admins can update results
        result = get_result(id)
        if result:
            result.username = username
            result.competition_name = competition_name
            result.results = results
            db.session.add(result)
            db.session.commit()
            print(f"Result updated successfully for '{username}' in competition '{competition_name}'.")
            return result
        else:
            print("Error: Result not found.")
    else:
        print("Error: Only admins can update results.")
    return None

def view_results(identifier=None):  # View results with optional identifier
    if identifier:
        results_query = Results.query.filter(
            (Results.competition_name == identifier) |
            (Results.username == identifier)
        )
        results = results_query.all()

        if results:
            print("=" * 80)
            print(f"{'Username':<20} {'Competition':<30} {'Results':<20}")
            print("=" * 80)
            for result in results:
                print(f"{result.username:<20} {result.competition_name:<30} {result.results:<20}")
            print("=" * 80)
        else:
            print("No results found for this competition or username.")
    else:
        competitions = {result.competition_name for result in Results.query.all()}
        if competitions:
            print("=" * 50)
            print("Available Competitions:")
            print("=" * 50)
            for index, comp in enumerate(sorted(competitions), start=1):
                print(f"{index}. {comp}")
            print("=" * 50)
            print("Please enter the command again with a specific competition name or username to view results.")
        else:
            print("No competitions available to display.")


