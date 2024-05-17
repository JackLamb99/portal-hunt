"""
'Glade' scene for Portal Hunt

This module contains the function and logic to navigate from 'The Glade' path
in Portal Hunt.

Separate file required to hold this function to allow users to return to 'The
Glade' from each separate file without caused a circular import error.
"""
import colorama
from colorama import Fore
import general as gen
import narrative as nar
from mountains import mountains_desc
from caves import caves_desc
from scorchlands import scorchlands_desc
from wetlands import wetlands_desc
colorama.init(autoreset=True)


def glade():
    """
    Runs the Glade scene
    """
    directions = ["north", "east", "south", "west"]

    if not gen.inventory and all(not value for value in gen.enemies.values()):
        print(nar.SECRET_ENDING_TEXT)
        gen.game_over()
    else:
        print(nar.GLADE_TEXT)
        print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            mountains_desc()
        elif valid_input == "east":
            gen.clear()
            caves_desc()
        elif valid_input == "south":
            gen.clear()
            scorchlands_desc()
        elif valid_input == "west":
            gen.clear()
            wetlands_desc()
