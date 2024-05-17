"""
general.py

This module contains a collection of generic functions that are used across
multiple other Python files within this project.

This module also contains the 'Inventory' list and 'Enemy' dictionary that are
used across multiple other Python files within this project.
"""
from os import system, name


flee_direction = []
inventory = []
enemies = {
    "goblins-1a": True,
    "goblins-2b": True,
    "tiger": True,
    "dragon": True,
    "spider-2b": True,
    "spider-1a": True,
    "skeletons": True,
    "troll": True,
    "wolves-4c": True,
    "wolves-2c": True,
    "crawler": True,
    "golem": True,
    "leeches-3b": True,
    "leeches-3d": True,
    "crocodile": True,
    "serpent": True
}


# Reference: "Clear screen in Python", GeeksforGeeks
# Source: https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    """
    Clears the content from the screen
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def lst_to_str(lst):
    """
    Returns a list as a string of the values separated by commas
    """
    return ", ".join(lst)


def get_valid_input(prompt, lst):
    """
    Prompts the user for input until a valid response is received.
    Repeats loop to request valid input until a valid input is entered.
    Breaks when a valid input is entered.
    """
    # Keep asking until valid input is entered
    while True:
        user_input = input(prompt).lower()
        if user_input in lst:
            # If the input is valid, break out of the loop
            return user_input
        else:
            print("Invalid direction, please choose from the "
                  "available options")


def amend_flee_direction(direction):
    """
    Clears the flee_direction list and amends the value with the opposite of
    the given direction.
    Used to return the player to their previous direction if they 'flee' from
    an enemy.
    """
    if direction == "north":
        flee_direction.clear()
        flee_direction.append("south")
    elif direction == "east":
        flee_direction.clear()
        flee_direction.append("west")
    elif direction == "south":
        flee_direction.clear()
        flee_direction.append("north")
    elif direction == "west":
        flee_direction.clear()
        flee_direction.append("east")


def reset_game():
    """
    Clears the 'inventory' list and resets the 'enemies' dictionary values to
    True.
    """
    inventory.clear()

    for enemy in enemies:
        enemies[enemy] = True


def game_over():
    """
    Allows the user to return the the main menu or restart the game.
    """
    options = ["menu", "again"]

    print(f"Options: {lst_to_str(options)}")

    valid_input = get_valid_input("Would you like to return to the main menu"
                                  " or play again?: ", options)
    if valid_input == "menu":
        reset_game()
        clear()
        # Imports function locally to avoid circular import error
        from run import main_menu
        main_menu()
    elif valid_input == "again":
        reset_game()
        clear()
        # Imports function locally to avoid circular import error
        from glade import glade
        glade()
