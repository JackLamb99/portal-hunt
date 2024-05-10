"""
Main Game File for Portal Hunt

This module initializes and runs Portal Hunt. It loads the necessary resources,
defines the general functions, and runs the initial menu function.

Usage:
- Run this file to start the game.
- Example command: 'python run.py'
- See README.md for additional information.
"""
import general as gen
import narrative as nar
import mountains as mnt


def main_menu():
    """
    Runs the main menu to start the program, includes the menu_text narrative
    """
    print(nar.MENU_TEXT)

    user_input = input("Enter 'start' to begin your quest: ")
    while user_input.lower() != "start":
        print("Invalid input. Please enter 'start' to begin your quest.\n")
        user_input = input("Enter 'start' to begin your quest: ")
    gen.clear()
    glade()


def glade():
    """
    Runs the Glade scene
    """
    directions = ["north", "east", "south", "west"]

    print(nar.GLADE_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        mnt.mountains_desc()
    elif valid_input == "east":
        gen.clear()
        print("Call Caves desc. function.")
    elif valid_input == "south":
        gen.clear()
        print("Call Scorchlands desc. function.")
    elif valid_input == "west":
        gen.clear()
        print("Call Wetlands desc. function.")


main_menu()
