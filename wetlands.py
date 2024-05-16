"""
'Wetlands' path for Portal Hunt.

This module contains the functions and logic to navigate the 'Wetlands' path
in Portal Hunt.

Includes; directions, locations, items, enemies, and the corresponding
interaction logic for each based on user input.

When required, functions are named based on the 'Wetlands' grid reference
provided in the README.md.
"""
import narrative as nar
import general as gen
import glade


def wetlands_desc():
    """
    Runs the 'Wetlands Desc.' scene, start of the 'Wetlands Path'.
    Grid ref. 'Wetlands-4C'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.WETLANDS_DESC_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        print("Call wtl_crossrd_4d() function")  # TO BE DEFINED
    elif valid_input == "east":
        gen.clear()
        glade.glade()
    elif valid_input == "south":
        gen.clear()
        print("Call wtl_crossrd_4b() function")  # TO BE DEFINED
    elif valid_input == "west":
        gen.clear()
        print("Call wtl_crossrd_3c() function")  # TO BE DEFINED
