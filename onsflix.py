# egg_shop.py
# Richie Moon
# 9/5/2022
# A program to keep track of egg inventory, adding stock, dividing stock into
# different size cartons and selling eggs to customers.

# The list of stock. They are in the format {size: quantity}.
stock = {4: 80,
         5: 0,
         6: 0,
         7: 0,
         8: 0}


def print_line():
    """Prints 17 = signs. """
    print("=" * 17)


def enter_size() -> int:
    """Asks the user for the size and checks that it is valid. Will return a
    valid size, as an int. """
    while True:
        try:
            size = int(input("    > Enter Size (4-8): "))
            MAX_SIZE = 8
            MIN_SIZE = 4
            if MIN_SIZE <= size <= MAX_SIZE:
                return size
            else:
                print("    Please enter a valid size. \n")
        except ValueError:
            print("    Please enter an integer. \n")


def enter_quantity(input_message: str = None) -> int:
    """Asks the user for the quantity and checks that it is valid. Will return
    the quantity as an int. """
    while True:
        try:
            if input_message is None:
                quantity = int(input("    > Enter quantity: "))
            else:
                quantity = int(input(f"   > {input_message}: "))

            MIN_SIZE = 1
            if quantity >= MIN_SIZE:
                return quantity
            else:
                print("\n    Please enter a valid quantity. ")
        except ValueError:
            print("    Please enter an integer. \n")


def print_menu():
    """Will print the main menu and menu items when called. """
    print_line()
    print("   🥚 EGGSHOP")
    print_line()
    menu_items = {"A": "Add Eggs to Stock.",
                  "E": "Edit egg stock and possible combinations. ",
                  "L": "List stock. ",
                  "S": "Sell Eggs. ",
                  "R": "View receipts. ",
                  "Q": "Quit. "}
    for key, value in menu_items.items():
        print(f"{key}: {value}")
    print_line()


def is_valid_choice(choice: str) -> bool:
    """Takes an input 'choice' and checks if it in the list of valid_choices.
    Return True if it is, False if it isn't. """

    valid_choices = ["a", "e", "l", "s", "r", "q"]
    if choice in valid_choices:
        return True
    else:
        return False


def add_stock():
    """Will ask the user for the size and quantity to increase stock by."""
    print("\n    " + "-" * 17)
    print("       ➕ ADD EGGS")
    print("    " + "-" * 17)

    # Call the enter_size and enter_quantity functions to ask the user for the
    # size and quantity.
    size = enter_size()
    quantity = enter_quantity()

    # Adds the quantity provided by the user to the quantity in the stocks
    # dictionary.
    stock[size] += quantity
    print("    " + "-" * 17)
    print(f"    Added {quantity}x size {size} eggs. \n")


def edit_stock():
    """Will edit the number of eggs in the stock by the amount that the user
    enters. """
    print("    " + "-" * 17)
    print("      ✂️ EDIT STOCK")
    print('    ' + '-' * 17)

    size = enter_size()
    print(f"    There are currently {stock[size]}x size {size} eggs. \n")

    quantity = enter_quantity("Enter new quantity")
    print('    ' + '-' * 17)

    stock[size] = quantity

    print(f"    In Stock: {stock[size]}x size {size} eggs. \n")


def list_stock():
    """Prints the number of eggs are in stock for each size and also displays
     how many cartons of 6, 12 and 24 can be made using the number on hand. """
    print("    " + '-' * 17)
    print("      🍳 COMBINATIONS")
    print("    " + '-' * 17)

    # For every size in stock, print the size and the total number of eggs in 
    # that size. Then, for every carton/tray size, check if it is 24. If it is, 
    # print Trays of 24, and then how many we can make. Do the same with 6 and
    # 12 except print 'Cartons' instead of 'Trays'. 
    cartons = [6, 12, 24]
    for size in stock:
        print(f"    Size {size}: {stock[size]}x")
        for i in cartons:
            if i == 24:
                print(f"        - Trays of {i}: {int(stock[size] / i)}x")
            else:
                print(f"        - Cartons of {i}: {int(stock[size] / i)}x")
    print()


def main():
    """This function will ask the user for their choice and check that it's
    valid. It will then call the other functions that the user asked for. """
    while True:
        print_menu()
        user_choice = input("> Enter a choice: ").strip().lower()
        valid_answer = is_valid_choice(user_choice)

        # While loop, which says sorry if the user answer is not valid,
        # and then asks the user for another choice, which gets checked.
        while valid_answer is False:
            print("Sorry, that's not a valid choice. \n")
            print_menu()

            user_choice = input("> Enter a choice: ").lower().strip()
            valid_answer = is_valid_choice(user_choice)

        menu_choices = [["a", "e", "l", "s", "r", "q"],
                        [add_stock, edit_stock, list_stock]]

        # The index of the letters and the function names in the menu_choices
        # list. Find the index of the letter that the user entered, and use
        # that to call the actual function.
        LETTERS = 0
        FUNCTION_NAMES = 1

        index = menu_choices[LETTERS].index(user_choice)
        menu_choices[FUNCTION_NAMES][index]()


main()
