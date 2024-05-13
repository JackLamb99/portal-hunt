"""
'Mountains' path for Portal Hunt

This module contains the functions and logic to navigate the 'Mountains' path
in Portal Hunt.

Includes; directions, locations, items, enemies, and the corresponding
interaction logic for each based on user input.

When required, functions are named based on the 'Mountains' grid reference
provided in the README.md.
"""
import narrative as nar
import general as gen
import glade


def mnt_crossrd_4a():
    """
    Runs a 'crossroad' scene, grid ref. 'Mountains-4A'
    """
    directions = ["north", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        print("Call frostfire() function")
    elif valid_input == "west":
        gen.clear()
        mountains_desc()


def mnt_crossrd_3b():
    """
    Runs a 'crossroad' scene, grid ref. 'Mountains-3B'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        print("Call tiger() function")
    elif valid_input == "east":
        gen.clear()
        print("Call frostfire() function")
    elif valid_input == "south":
        gen.clear()
        mountains_desc()
    elif valid_input == "west":
        gen.clear()
        print("Call goblins_2b() function")


def mnt_crossrd_2a():
    """
    Runs a 'crossroad' scene, grid ref. 'Mountains-2A'
    """
    directions = ["north", "east", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        print("Call goblins_2b() function")
    elif valid_input == "east":
        gen.clear()
        mountains_desc()
    elif valid_input == "west":
        gen.clear()
        print("Call goblins_1a() function")


def mountains_desc():
    """
    Runs the 'Mountains Desc.' scene, grid ref. 'Mountains-3A'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.MOUNTAINS_DESC_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        mnt_crossrd_3b()
    elif valid_input == "east":
        gen.clear()
        mnt_crossrd_4a()
    elif valid_input == "south":
        gen.clear()
        glade.glade()
    elif valid_input == "west":
        gen.clear()
        mnt_crossrd_2a()
