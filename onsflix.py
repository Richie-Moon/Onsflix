# onsflix.py
# Richie Moon, 29/3/2022

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


def valid_choice(user_input):
    valid_answers = ['a', 'd', 'e', 'l', 'q']
    try:
        user_input.lower().strip()
        if user_input in valid_answers:
            return True
        else:
            return False
    except Exception:
        return False


def main():
    """The main function. Will be using this one to call all the other
    functions and ask the user for their choices. """
    while True:
        print_menu()
        user_choice = input("Enter a choice: ")
        valid_answer = valid_choice(user_choice)

        while valid_answer is False:
            print("Sorry, that's not a valid choice. ")
            print_menu()

            user_choice = input("Enter a choice: ")
            valid_answer = valid_choice(user_choice)


