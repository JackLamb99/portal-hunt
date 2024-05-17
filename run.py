"""
Main Game File for Portal Hunt

This module initializes and runs Portal Hunt. It loads the necessary resources,
defines the general functions, and runs the initial menu function.

Usage:
- Run this file to start the game.
- Example command: 'python run.py'
- See README.md for additional information.
"""
import colorama
from colorama import Fore
import general as gen
import narrative as nar
import glade
colorama.init(autoreset=True)


def main_menu():
    """
    Runs the main menu to start the program, includes the menu_text narrative
    """
    print(nar.MENU_TEXT)

    user_input = input("Enter 'start' to begin your quest: ")
    while user_input.lower() != "start":
        print(Fore.RED + "Invalid input. Please enter 'start' to begin your"
              " quest.\n")
        user_input = input("Enter 'start' to begin your quest: ")
    gen.clear()
    glade.glade()


main_menu()
