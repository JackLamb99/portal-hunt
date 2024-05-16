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


def elixir():
    """
    Checks if the 'elixir' item is in the inventory.
    Runs an 'existing item' scene if true, allows player to 'keep' or 'return'
    the item.
    Runs a 'new item' scene if false, allows player to 'take' or 'leave' the
    item.
    Grid ref. 'Wetlands-4A'
    """
    directions = ["north"]

    # If the specified item already in the inventory
    if "elixir" in gen.inventory:
        options = ["keep", "return"]

        print(nar.ELIXIR_EXISTING_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "keep":
            print(nar.KEEP_ITEM_TEXT)
        elif valid_input == "return":
            gen.inventory.remove("elixir")
            print(nar.RETURN_ITEM_TEXT)
    else:
        options = ["take", "leave"]

        print(nar.ELIXIR_NEW_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "take":
            gen.inventory.append("elixir")
            print(nar.TAKE_ITEM_TEXT)
        elif valid_input == "leave":
            print(nar.LEAVE_ITEM_TEXT)

    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        wtl_crossrd_4b()


def wtl_crossrd_4d():
    """
    Runs a 'crossroad' scene. Grid ref. 'Wetlands-4D'
    """
    directions = ["south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "south":
        gen.clear()
        wetlands_desc()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        print("Call leeches_3d() function")  # TO BE DEFINED


def wtl_crossrd_3c():
    """
    Runs a 'crossroad' scene. Grid ref. 'Wetlands-3C'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        print("Call leeches_3d() function")  # TO BE DEFINED
    elif valid_input == "east":
        gen.clear()
        wetlands_desc()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        print("Call leeches_3b() function")  # TO BE DEFINED
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        print("Call crocodile() function")  # TO BE DEFINED


def wtl_crossrd_4b():
    """
    Runs a 'crossroad' scene. Grid ref. 'Wetlands-4B'
    """
    directions = ["north", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        wetlands_desc()
    elif valid_input == "south":
        gen.clear()
        elixir()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        print("Call leeches_3b() function")  # TO BE DEFINED


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
        wtl_crossrd_4d()
    elif valid_input == "east":
        gen.clear()
        glade.glade()
    elif valid_input == "south":
        gen.clear()
        wtl_crossrd_4b()
    elif valid_input == "west":
        gen.clear()
        wtl_crossrd_3c()
