"""
'Scorchlands' path for Portal Hunt.

This module contains the functions and logic to navigate the 'Scorchlands' path
in Portal Hunt.

Includes; directions, locations, items, enemies, and the corresponding
interaction logic for each based on user input.

When required, functions are named based on the 'Scorchlands' grid reference
provided in the README.md.
"""
import narrative as nar
import general as gen
import glade


def scor_crossrd_4d():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-4D'
    """
    directions = ["south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        print("Call wolves_4c() function")  # TO BE DEFINED
    elif valid_input == "west":
        gen.clear()
        scorchlands_desc()


def scorchlands_desc():
    """
    Runs the 'Scorchlands Desc.' scene, start of the 'Scorchlands Path'.
    Grid ref. 'Scorchlands-3D'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.SCORCHLANDS_DESC_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        glade.glade()
    elif valid_input == "east":
        gen.clear()
        print("Call scor_crossrd_4d() function")  # TO BE DEFINED
    elif valid_input == "south":
        gen.clear()
        print("Call scor_crossrd_3c() function")  # TO BE DEFINED
    elif valid_input == "west":
        gen.clear()
        print("Call scor_crossrd_2d() function")  # TO BE DEFINED
