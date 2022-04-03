# onsflix.py
# Richie Moon, 29/3/2022
from datetime import timedelta
movies = {"test": 30}


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
    print("    " + "-" * 17)
    print("    ➕ ADD MOVIE")
    print("    " + "-" * 17)
    title = input("    > Title: ")
    while True:
        try:
            length = int(input("    > Length (Minutes): "))
            break
        except ValueError:
            print("    Please enter an integer for the length")
    print("    " + "-" * 17)
    # Stole Code from
    # https://stackoverflow.com/questions/1784952/how-get-hoursminutes/33964397
    formatted_time = str(timedelta(minutes=length))[:-3]
    movies.update({title: formatted_time})


def main():
    """The main function. Will be using this one to call all the other
    functions and ask the user for their choices. """

    while True:
        print_menu()
        user_choice = input("> Enter a choice: ")
        valid_answer = valid_choice(user_choice)

        while valid_answer is False:
            print("Sorry, that's not a valid choice. ")
            print_menu()

            user_choice = input("> Enter a choice: ")
            valid_answer = valid_choice(user_choice)

        menu_choice = [['a', 'd', 'e', 'l', 'q'], [add_movie]]

        index = menu_choice[0].index(user_choice)
        menu_choice[1][index]()


main()
