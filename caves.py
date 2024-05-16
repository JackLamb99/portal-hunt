"""
'Caves' path for Portal Hunt.

This module contains the functions and logic to navigate the 'Caves' path
in Portal Hunt.

Includes; directions, locations, items, enemies, and the corresponding
interaction logic for each based on user input.

When required, functions are named based on the 'Caves' grid reference
provided in the README.md.
"""
import narrative as nar
import general as gen
import glade


def cave_crossrd_1d():
    """
    Runs a 'crossroad' scene, grid ref. 'Caves-1D'
    """
    directions = ["east", "south"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "east":
        gen.clear()
        print("Call everflame() function")  # TO BE DEFINED
    elif valid_input == "south":
        gen.clear()
        caves_desc()


def caves_desc():
    """
    Runs the 'Caves Desc.' scene, start of the 'Caves Path'.
    Grid ref. 'Caves-1C'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.CAVES_DESC_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        cave_crossrd_1d()
    elif valid_input == "east":
        gen.clear()
        print("Call cave_crossrd_2c() function")  # TO BE DEFINED
    elif valid_input == "south":
        gen.clear()
        print("Call cave_crossrd_1b() function")  # TO BE DEFINED
    elif valid_input == "west":
        gen.clear()
        glade.glade()
