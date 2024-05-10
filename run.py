"""
Main Game File for Portal Hunt

This module initializes and runs Portal Hunt. It loads the necessary resources,
defines the general functions, and runs the initial menu function.

Usage:
- Run this file to start the game.
- Example command: 'python run.py'
- See README.md for additional information.
"""

from os import system, name
import narrative as nar
import mountains as mnt


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


def main_menu():
    """
    Runs the main menu to start the program, includes the menu_text narrative
    """
    print(nar.MENU_TEXT)

    user_input = input("Enter 'start' to begin your quest: ")
    while user_input.lower() != "start":
        print("Invalid input. Please enter 'start' to begin your quest.\n")
        user_input = input("Enter 'start' to begin your quest: ")

    clear()
    glade()


def glade():
    """
    Runs the Glade scene
    """
    directions = ["north", "east", "south", "west"]

    print(nar.GLADE_TEXT)
    print(f"Directions: {lst_to_str(directions)}")

    user_input = input("Where would you like to go?: ")
    if user_input.lower() == "north":
        clear()
        mnt.mountains_desc()
    elif user_input.lower() == "east":
        clear()
        print("Call Caves desc. function.")
    elif user_input.lower() == "south":
        clear()
        print("Call Scorchlands desc. function.")
    elif user_input.lower() == "west":
        clear()
        print("Call Wetlands desc. function.")
    else:
        print(f"Invalid direction. Please enter a valid direction:\
            {lst_to_str(directions)}\n")
        user_input = input("Where would you like to go?: ")


main_menu()
