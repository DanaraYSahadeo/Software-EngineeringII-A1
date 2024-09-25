# from App.models import Results
# from App.database import db

# def create_result(username, competition_name, results):
#     new_result = Results(username=username, competition_name=competition_name, results=results)
#     db.session.add(new_result)
#     db.session.commit()
#     return new_result

# def get_result(id):
#     return Results.query.get(id)

# def get_all_results():
#     return Results.query.all()

# def get_all_results_json():
#     results = Results.query.all()
#     if not results:
#         return []
#     results = [result.get_json() for result in results]
#     return results

# def update_result(id, username, competition_name, results):
#     result = get_result(id)
#     if result:
#         result.username = username
#         result.competition_name = competition_name
#         result.results = results
#         db.session.add(result)
#         db.session.commit()
#         return result
#     return None


# def view_results(competition_name=None):
#     try:
#         with open('data.csv', encoding='unicode_escape') as csvfile:
#             reader = csv.DictReader(csvfile)
#             competitions = set(row['competition_name'] for row in reader)
                
#             if not competition_name:
#                 print("Available competitions:")
#                 for i, competition in enumerate(competitions, 1):
#                     print(f"{i}. {competition}")
#                 print("\nPlease enter the command again with a competition name to view results.")
#             else:
#                 csvfile.seek(0)  # Reset reader to the beginning of the file
#                 next(reader)  # Skip header row after seek
#                 print(f"{'Username':<20} {'Competition Name':<30} {'Results':<20}")
#                 for row in reader:
#                     if row['competition_name'] == competition_name:
#                         print(f"{row['username']:<20} {row['competition_name']:<30} {row['results']:<20}")
#     except FileNotFoundError:
#         print("data.csv file not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# import csv
# from App.models import Results
# from App.database import db

# def create_result(username, competition_name, results):
#     new_result = Results(username=username, competition_name=competition_name, results=results)
#     db.session.add(new_result)
#     db.session.commit()
#     return new_result

# def get_result(id):
#     return Results.query.get(id)

# def get_all_results():
#     return Results.query.all()

# def get_all_results_json():
#     results = Results.query.all()
#     results = [result.get_json() for result in results]
#     return results

# def update_result(id, username, competition_name, results):
#     result = get_result(id)
#     if result:
#         result.username = username
#         result.competition_name = competition_name
#         result.results = results
#         db.session.add(result)
#         db.session.commit()
#         return result
#     return None

# def view_results(competition_name=None):
#     try:
#         with open('data.csv', encoding='unicode_escape') as csvfile:
#             reader = csv.DictReader(csvfile)
#             competitions = set(row['competition_name'] for row in reader)
                
#             if not competition_name:
#                 print("Available competitions:")
#                 for i, competition in enumerate(competitions, 1):
#                     print(f"{i}. {competition}")
#                 print("\nPlease enter the command again with a competition name to view results.")
#             else:
#                 csvfile.seek(0)  # Reset reader to the beginning of the file
#                 next(reader)  # Skip header row after seek
#                 print(f"{'Username':<20} {'Competition Name':<30} {'Results':<20}")
#                 for row in reader:
#                     if row['competition_name'] == competition_name:
#                         print(f"{row['username']:<20} {row['competition_name']:<30} {row['results']:<20}")
#     except FileNotFoundError:
#         print("data.csv file not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# Test
# import csv
# from App.models import Results
# from App.database import db

# def create_result(username, competition_name, results):
#     new_result = Results(username=username, competition_name=competition_name, results=results)
#     db.session.add(new_result)
#     db.session.commit()
#     return new_result

# def get_result(id):
#     return Results.query.get(id)

# def get_all_results():
#     return Results.query.all()

# def get_all_results_json():
#     results = Results.query.all()
#     results = [result.get_json() for result in results]
#     return results

# def update_result(id, username, competition_name, results):
#     result = get_result(id)
#     if result:
#         result.username = username
#         result.competition_name = competition_name
#         result.results = results
#         db.session.add(result)
#         db.session.commit()
#         return result
#     return None

# def view_results(competition_name=None):
#     try:
#         with open('data2.csv', encoding='unicode_escape') as csvfile:
#             reader = csv.DictReader(csvfile)
#             competitions = set(row['competition_name'] for row in reader)
                
#             if not competition_name:
#                 print("Available competitions:")
#                 for i, competition in enumerate(competitions, 1):
#                     print(f"{i}. {competition}")
#                 print("\nPlease enter the command again with a competition name to view results.")
#             else:
#                 csvfile.seek(0)  # Reset reader to the beginning of the file
#                 next(reader)  # Skip header row after seek
#                 print(f"{'Username':<20} {'Competition Name':<30} {'Results':<20}")
#                 for row in reader:
#                     if row['competition_name'] == competition_name:
#                         print(f"{row['username']:<20} {row['competition_name']:<30} {row['results']:<20}")
#     except FileNotFoundError:
#         print("data2.csv file not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
           
# def view_results_command(competition_name):
#     view_results(competition_name)

# Test2
from App.models import Results
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_result(username, competition_name, results):
    new_result = Results(username=username, competition_name=competition_name, results=results)
    db.session.add(new_result)
    db.session.commit()
    return new_result

def get_result(id):
    return Results.query.get(id)

def get_all_results():
    return Results.query.all()

def get_all_results_json():
    results = Results.query.all()
    return [result.get_json() for result in results]

def update_result(id, username, competition_name, results):
    result = get_result(id)
    if result:
        result.username = username
        result.competition_name = competition_name
        result.results = results
        db.session.add(result)
        db.session.commit()
        return result
    return None

def view_results(competition_name=None):
    if competition_name:
        results_query = Results.query.filter_by(competition_name=competition_name)
        results = results_query.all()

        # Print results if they exist
        if results:
            print("=" * 80)
            print(f"{'Username':<20} {'Competition':<30} {'Results':<20}")
            print("=" * 80)
            for result in results:
                print(f"{result.username:<20} {result.competition_name:<30} {result.results:<20}")
            print("=" * 80)
        else:
            print("No results found for this competition.")
    else:
        # If no competition name is provided, list unique competitions
        competitions = {result.competition_name for result in Results.query.all()}
        print("=" * 50)
        print("Available Competitions:")
        print("=" * 50)
        for index, comp in enumerate(sorted(competitions), start=1):
            print(f"{index}. {comp}")
        print("=" * 50)
        print("Please enter the command again with a specific competition name to view results.")



