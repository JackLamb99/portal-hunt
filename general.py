"""
general.py

This module contains a collection of generic functions that are used across
multiple other Python files within this project.
"""
from os import system, name


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
