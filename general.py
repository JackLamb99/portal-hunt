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
    "dragon": True
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
