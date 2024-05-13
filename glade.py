"""
'Glade' scene for Portal Hunt

This module contains the function and logic to navigate from 'The Glade' path
in Portal Hunt.

Separate file required to hold this function to allow users to return to 'The
Glade' from each separate file without caused a circular import error.
"""
import general as gen
import narrative as nar
from mountains import mountains_desc


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
        mountains_desc()
    elif valid_input == "east":
        gen.clear()
        print("Call Caves desc. function.")
    elif valid_input == "south":
        gen.clear()
        print("Call Scorchlands desc. function.")
    elif valid_input == "west":
        gen.clear()
        print("Call Wetlands desc. function.")