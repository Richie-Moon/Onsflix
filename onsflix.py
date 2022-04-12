# onsflix.py
# Richie Moon, 29/3/2022

# Imports
from datetime import timedelta

# Variables
movies = {}


def valid_time(time):
    SHORTEST_LENGTH = 2
    LONGEST_LENGTH = 5100
    if SHORTEST_LENGTH <= time <= LONGEST_LENGTH:
        return True
    else:
        return False


def format_time(time):
    """Takes in an input 'time' in minutes and returns the formatted time as
    HH:MM. """
    # Stole Code from
    # https://stackoverflow.com/questions/1784952/how-get-hoursminutes/33964397
    return str(timedelta(minutes=time))[:-3]


def print_menu():
    """Prints the main menu with the different options. """
    print("=" * 11)
    print("  Onsflix")
    print("=" * 11)
    menu_items = {"A": "Add a movie",
                  "D": "Delete a movie",
                  "E": "Edit the length if a movie",
                  "L": "List all the movies and their times.",
                  "Q": "Quit"}
    for key, value in menu_items.items():
        print(f"{key}: {value}")
    print("=" * 11)


def valid_choice(user_input) -> bool:
    """Checks if the user has entered a valid input. Returns True if it is,
    False if it isn't."""
    valid_answers = ['a', 'd', 'e', 'l', 'q']
    try:
        user_input = user_input.lower().strip()
        if user_input in valid_answers:
            return True
        else:
            return False
    except Exception:
        return False


def add_movie():
    """Asks the user for the title and length of the movie. Format length to
    HH:MM and return a dict with the kay as the title and the value as the
    length"""

    print("\n    " + "-" * 17)
    print("      ➕ ADD MOVIE")
    print("    " + "-" * 17)

    while True:
        title = input("    > Title: ")
        if title in movies:
            print("    That movie already exists. "
                  "Please enter a unique movie name. \n")
        elif title.isspace() is True or title == "":
            print("    Please enter a valid title. \n")
        else:
            break

    while True:
        try:
            length = int(input("    > Length (Minutes): "))
            if valid_time(length) is True:
                break
            else:
                print("    Please enter a valid movie length. \n")

        except ValueError:
            print("    Please enter an integer for the length.\n")
    print("    " + "-" * 17)

    formatted_time = format_time(length)
    movies.update({title: formatted_time})
    print(f"    Added '{title}' ({formatted_time})\n")


def delete_movie():
    """Asks the user for the title of the movie, checks if it is in movies
    and then asks for a confirmation. Deletes the movie after confirmation."""
    print("\n    " + "-" * 18)
    print("      🗑 DELETE MOVIE")
    print("    " + "-" * 18)

    while True:
        title = input("    > Title: ")
        if title not in movies:
            print("    That movie doesn't exist.\n")
        else:
            break

    print(f"\n    Are you sure you want to delete {title}?"
          "\n    Once deleted, this movie cannot be recovered."
          "\n    Type 'yes' to confirm. ")
    confirm = input("\n    > Confirm: ").lower().strip()

    if confirm == 'yes':
        del movies[title]
        print("    " + "-" * 18)
        print(f"\n   Deleted '{title}'\n")
    else:
        print("\n    Confirmation Failed. No movies were deleted. \n")


def list_movies():
    """Lists all the current movies in the movies dictionary. """
    print('\n    ' + '-' * 18)
    print("        🎬 MOVIES")
    print('    ' + '-' * 18)

    if len(movies) == 0:
        print("    No movies to show. \n")
    else:
        list_of_keys = []
        for key in movies.keys():
            list_of_keys.append(key)

        for key, value in movies.items():
            print(f"    {list_of_keys.index(key) + 1}. {key} ({value})")
        print()


def edit_length():
    """Asks the user for the name of the movie they want to edit and checks if
    it is in movies. If it is, ask the user for the new length, check that it
    is valid, and format the time. Update the dictionary with the new value."""

    print("\n    " + "-" * 18)
    print("      ✂ EDIT LENGTH")
    print("    " + "-" * 18)
    movie = input("    > Title of Movie you want to edit: ")

    while True:
        if movie not in movies:
            print("    That movie was not found. \n")
            movie = input("    > Title of Movie you want to edit: ")
        else:
            break

    print(f"    '{movie}' is currently {movies[movie]}. ")

    while True:
        try:
            while True:
                length = int(input("\n    > New Length (Minutes): "))
                if valid_time(length) is True:
                    break
                else:
                    print("    Please enter a valid time. ")
            formatted_time = format_time(length)
            old_length = movies[movie]
            movies[movie] = formatted_time
            print("    " + "-" * 18)
            print(f"\n    Edited '{movie}' ({old_length} -> {formatted_time})")
            break
        except ValueError:
            print("    Please provide an integer. \n")


def exit_program():
    print("Thank you for using Onsflix!")
    quit()


def main():
    """The main function. Will be using this one to call all the other
    functions and ask the user for their choices. """

    while True:
        print_menu()
        user_choice = input("> Enter a choice: ")
        valid_answer = valid_choice(user_choice)
        while valid_answer is False:
            print("Sorry, that's not a valid choice. \n")
            print_menu()

            user_choice = input("> Enter a choice: ")
            valid_answer = valid_choice(user_choice)

        menu_choice = [['a', 'd', 'l', 'e', 'q'],
                       [add_movie, delete_movie, list_movies, edit_length,
                        exit_program]]

        index = menu_choice[0].index(user_choice)
        menu_choice[1][index]()


main()
