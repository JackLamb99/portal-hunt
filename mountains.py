"""
'Mountains' path for Portal Hunt

This module contains the functions and logic to navigate the 'Mountains' path
in Portal Hunt.

Includes; directions, locations, items, enemies, and the corresponding
interaction logic for each based on user input.

When required, functions are named based on the 'Mountains' grid reference
provided in the README.md.
"""

from os import system, name

import narrative as nar


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


def mountains_desc():
    """
    Runs the 'Mountains' description scene
    """
    directions = ["north", "east", "west"]
    print(nar.MOUNTAINS_DESC_TEXT)
    print(f"Directions: {lst_to_str(directions)}")
    user_input = input("Where would you like to go?: ")

    if user_input.lower() == "north":
        clear()
        print("Call crossroad_mnt_3b function.")
    elif user_input.lower() == "east":
        clear()
        print("Call crossroad_mnt_4a function.")
    elif user_input.lower() == "west":
        clear()
        print("Call crossroad_mnt_2a function.")
    else:
        print(f"Invalid direction. Please enter a valid direction:\
            {lst_to_str(directions)}\n")
        user_input = input("Where would you like to go?: ")
