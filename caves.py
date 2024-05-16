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


def everflame():
    """
    Checks if the 'everflame' item is in the inventory.
    Runs an 'existing item' scene if true, allows player to 'keep' or 'return'
    the item.
    Runs a 'new item' scene if false, allows player to 'take' or 'leave' the
    item.
    Grid ref. 'Caves-2D'
    """
    directions = ["east", "south", "west"]

    # If the specified item already in the inventory
    if "everflame" in gen.inventory:
        options = ["keep", "return"]

        print(nar.EVERFLAME_EXISTING_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "keep":
            print(nar.KEEP_ITEM_TEXT)
        elif valid_input == "return":
            gen.inventory.remove("everflame")
            print(nar.RETURN_ITEM_TEXT)
    else:
        options = ["take", "leave"]

        print(nar.EVERFLAME_NEW_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "take":
            gen.inventory.append("everflame")
            print(nar.TAKE_ITEM_TEXT)
        elif valid_input == "leave":
            print(nar.LEAVE_ITEM_TEXT)

    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "east":
        gen.clear()
        print("Call cave_crossrd_3d() function")  # TO BE DEFINED
    elif valid_input == "south":
        gen.clear()
        cave_crossrd_2c()
    elif valid_input == "west":
        gen.clear()
        cave_crossrd_1d()


def cave_crossrd_1b():
    """
    Runs a 'crossroad' scene. Grid ref. 'Caves-1B'
    """
    directions = ["north", "east", "south"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        caves_desc()
    elif valid_input == "east":
        gen.clear()
        print("Call spider_2b() function")  # TO BE DEFINED
    elif valid_input == "south":
        gen.clear()
        print("Call spider_1a() function")  # TO BE DEFINED


def cave_crossrd_2c():
    """
    Runs a 'crossroad' scene. Grid ref. 'Caves-2C'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        everflame()
    elif valid_input == "east":
        gen.clear()
        print("Call skeletons() function")  # TO BE DEFINED
    elif valid_input == "south":
        gen.clear()
        print("Call spider_2b() function")  # TO BE DEFINED
    elif valid_input == "west":
        gen.clear()
        caves_desc()


def cave_crossrd_1d():
    """
    Runs a 'crossroad' scene. Grid ref. 'Caves-1D'
    """
    directions = ["east", "south"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "east":
        gen.clear()
        everflame()
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
        cave_crossrd_2c()
    elif valid_input == "south":
        gen.clear()
        cave_crossrd_1b()
    elif valid_input == "west":
        gen.clear()
        glade.glade()
