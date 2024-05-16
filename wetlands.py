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


def wtl_crossrd_3a():
    """
    Runs a 'crossroad' scene. Grid ref. 'Wetlands-3A'
    """
    directions = ["north", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        leeches_3b()
    elif valid_input == "west":
        gen.clear()
        print("Call trident() function")  # TO BE DEFINED


def leeches_3d():
    """
    Checks if 'leeches-3d' are alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Wetlands-3D'
    """
    directions = ["east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["leeches-3d"]:
        options = ["fight", "flee"]

        print(nar.LEECHES_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if "elixir" in gen.inventory:
                gen.enemies["leeches-3d"] = False

                print(nar.ENEMY_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "east":
                    gen.clear()
                    wtl_crossrd_4d()
                elif valid_input == "south":
                    gen.clear()
                    wtl_crossrd_3c()
                elif valid_input == "west":
                    gen.clear()
                    print("Call wtl_crossrd_2d() function")  # TO BE DEFINED
            # If required items not in inventory, defeat scene
            else:
                print(nar.LEECHES_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["east"]:
                wtl_crossrd_4d()
            elif gen.flee_direction == ["south"]:
                wtl_crossrd_3c()
            elif gen.flee_direction == ["west"]:
                print("Call wtl_crossrd_2d() function")  # TO BE DEFINED

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.LEECHES_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "east":
            gen.clear()
            wtl_crossrd_4d()
        elif valid_input == "south":
            gen.clear()
            wtl_crossrd_3c()
        elif valid_input == "west":
            gen.clear()
            print("Call wtl_crossrd_2d() function")  # TO BE DEFINED


def crocodile():
    """
    Checks if the 'crocodile' is alive (True) or dead (False), runs a 'fight'
    or 'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Wetlands-2C'
    """
    directions = ["north", "east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["crocodile"]:
        options = ["fight", "flee"]

        print(nar.CROCODILE_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if all(item in gen.inventory for item in [
                    "elixir", "trident"]):
                gen.enemies["crocodile"] = False

                print(nar.CROCODILE_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    print("Call wtl_crossrd_2d() function")  # TO BE DEFINED
                elif valid_input == "east":
                    gen.clear()
                    wtl_crossrd_3c()
                elif valid_input == "south":
                    gen.clear()
                    print("Call wtl_crossrd_2b() function")  # TO BE DEFINED
                elif valid_input == "west":
                    gen.clear()
                    print("Call wtl_crossrd_1c() function")  # TO BE DEFINED
            # If required items not in inventory, defeat scene
            else:
                print(nar.CROCODILE_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                print("Call wtl_crossrd_2d() function")  # TO BE DEFINED
            elif gen.flee_direction == ["east"]:
                wtl_crossrd_3c()
            elif gen.flee_direction == ["south"]:
                print("Call wtl_crossrd_2b() function")  # TO BE DEFINED
            elif gen.flee_direction == ["west"]:
                print("Call wtl_crossrd_1c() function")  # TO BE DEFINED

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.CROCODILE_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            print("Call wtl_crossrd_2d() function")  # TO BE DEFINED
        elif valid_input == "east":
            gen.clear()
            wtl_crossrd_3c()
        elif valid_input == "south":
            gen.clear()
            print("Call wtl_crossrd_2b() function")  # TO BE DEFINED
        elif valid_input == "west":
            gen.clear()
            print("Call wtl_crossrd_1c() function")  # TO BE DEFINED


def leeches_3b():
    """
    Checks if 'leeches-3b' are alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Wetlands-3B'
    """
    directions = ["north", "east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["leeches-3b"]:
        options = ["fight", "flee"]

        print(nar.LEECHES_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if "elixir" in gen.inventory:
                gen.enemies["leeches-3b"] = False

                print(nar.LEECHES_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    wtl_crossrd_3c()
                elif valid_input == "east":
                    gen.clear()
                    wtl_crossrd_4b()
                elif valid_input == "south":
                    gen.clear()
                    wtl_crossrd_3a()
                elif valid_input == "west":
                    gen.clear()
                    print("Call wtl_crossrd_2b() function")  # TO BE DEFINED
            # If required items not in inventory, defeat scene
            else:
                print(nar.LEECHES_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                wtl_crossrd_3c()
            elif gen.flee_direction == ["east"]:
                wtl_crossrd_4b()
            elif gen.flee_direction == ["south"]:
                wtl_crossrd_3a()
            elif gen.flee_direction == ["west"]:
                print("Call wtl_crossrd_2b() function")  # TO BE DEFINED

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.LEECHES_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            wtl_crossrd_3c()
        elif valid_input == "east":
            gen.clear()
            wtl_crossrd_4b()
        elif valid_input == "south":
            gen.clear()
            wtl_crossrd_3a()
        elif valid_input == "west":
            gen.clear()
            print("Call wtl_crossrd_2b() function")  # TO BE DEFINED


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
        leeches_3d()


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
        leeches_3d()
    elif valid_input == "east":
        gen.clear()
        wetlands_desc()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        leeches_3b()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        crocodile()


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
        leeches_3b()


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
