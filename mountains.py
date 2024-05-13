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


def dragon():
    """
    Checks if the 'dragon' is alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Mountains-GRID'
    """
    directions = ["north", "east", "south"]

    # If the specified enemy is 'alive'
    if gen.enemies["dragon"]:
        options = ["fight", "flee"]

        print(nar.DRAGON_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if all(item in gen.inventory for item in [
                    "frostfire", "voltcrusher", "bow"]):
                gen.enemies["dragon"] = False

                print(nar.DRAGON_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    print("Call mountains_portal() function")  # TO BE DEFINED
                elif valid_input == "east":
                    gen.clear()
                    mnt_crossrd_3d()
                elif valid_input == "south":
                    gen.clear()
                    mnt_crossrd_2c()
            # If required items not in inventory, defeat scene
            else:
                print(nar.DRAGON_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["east"]:
                mnt_crossrd_3d()
            elif gen.flee_direction == ["south"]:
                mnt_crossrd_2c()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.DRAGON_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            print("Call mountains_portal() function")  # TO BE DEFINED
        elif valid_input == "east":
            gen.clear()
            mnt_crossrd_3d()
        elif valid_input == "south":
            gen.clear()
            mnt_crossrd_2c()


def voltcrusher():
    """
    Checks if the 'voltcrusher' item is in the inventory.
    Runs an 'existing item' scene if true, allows player to 'keep' or 'return'
    the item.
    Runs a 'new item' scene if false, allows player to 'take' or 'leave' the
    item.
    Grid ref. 'Mountains-1C'
    """
    directions = ["north", "east", "south"]

    # If the specified item already in the inventory
    if "voltcrusher" in gen.inventory:
        options = ["keep", "return"]

        print(nar.VOLTCRUSHER_EXISTING_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "keep":
            print(nar.KEEP_ITEM_TEXT)
        elif valid_input == "return":
            gen.inventory.remove("ITEM")
            print(nar.RETURN_ITEM_TEXT)
    else:
        options = ["take", "leave"]

        print(nar.VOLTCRUSHER_NEW_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "take":
            gen.inventory.append("ITEM")
            print(nar.TAKE_ITEM_TEXT)
        elif valid_input == "leave":
            print(nar.LEAVE_ITEM_TEXT)

    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        print("Call dead_end_1d() function")  # TO BE DEFINED
    elif valid_input == "east":
        gen.clear()
        mnt_crossrd_2c()
    elif valid_input == "south":
        gen.clear()
        mnt_crossrd_1b()


def mnt_crossrd_4c():
    """
    Runs a 'crossroad' scene, grid ref. 'Mountains-4C'
    """
    directions = ["south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "south":
        gen.clear()
        frostfire()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        tiger()


def mnt_crossrd_3d():
    """
    Runs a 'crossroad' scene, grid ref. 'Mountains-3D'
    """
    directions = ["east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "east":
        gen.clear()
        print("Call bow() function")  # TO BE DEFINED
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        tiger()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        print("Call dragon() function")  # TO BE DEFINED


def mnt_crossrd_2c():
    """
    Runs a 'crossroad' scene, grid ref. 'Mountains-2C'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        print("Call dragon() function")  # TO BE DEFINED
    elif valid_input == "east":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        tiger()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        goblins_2b()
    elif valid_input == "west":
        gen.clear()
        voltcrusher()


def mnt_crossrd_1b():
    """
    Runs a 'crossroad' scene. Grid ref. 'Mountains-1B'
    """
    directions = ["north", "east", "south"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        voltcrusher()
    elif valid_input == "east":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        goblins_2b()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        goblins_1a()


def frostfire():
    """
    Checks if the 'frostfire' item is in the inventory.
    Runs an 'existing item' scene if true, allows player to 'keep' or 'return'
    the item.
    Runs a 'new item' scene if false, allows player to 'take' or 'leave' the
    item.
    Grid ref. 'Mountains-4B'
    """
    directions = ["north", "south", "west"]

    # If the specified item already in the inventory
    if "frostfire" in gen.inventory:
        options = ["keep", "return"]

        print(nar.FROSTFIRE_EXISTING_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "keep":
            print(nar.KEEP_ITEM_TEXT)
        elif valid_input == "return":
            gen.inventory.remove("frostfire")
            print(nar.RETURN_ITEM_TEXT)
    else:
        options = ["take", "leave"]

        print(nar.FROSTFIRE_NEW_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "take":
            gen.inventory.append("frostfire")
            print(nar.TAKE_ITEM_TEXT)
        elif valid_input == "leave":
            print(nar.LEAVE_ITEM_TEXT)

    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        mnt_crossrd_4c()
    elif valid_input == "south":
        gen.clear()
        mnt_crossrd_4a()
    elif valid_input == "west":
        gen.clear()
        mnt_crossrd_3b()


def tiger():
    """
    Checks if the 'tiger' is alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Mountains-3C'
    """
    directions = ["north", "east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["tiger"]:
        options = ["fight", "flee"]

        print(nar.TIGER_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if all(item in gen.inventory for item in [
                    "frostfire", "voltcrusher"]):
                gen.enemies["tiger"] = False

                print(nar.TIGER_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    mnt_crossrd_3d()
                elif valid_input == "east":
                    gen.clear()
                    mnt_crossrd_4c()
                elif valid_input == "south":
                    gen.clear()
                    mnt_crossrd_3b()
                elif valid_input == "west":
                    gen.clear()
                    mnt_crossrd_2c()
            # If required items not in inventory, defeat scene
            else:
                print(nar.TIGER_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                mnt_crossrd_3d()
            elif gen.flee_direction == ["east"]:
                mnt_crossrd_4c()
            elif gen.flee_direction == ["south"]:
                mnt_crossrd_3b()
            elif gen.flee_direction == ["west"]:
                mnt_crossrd_2c()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.TIGER_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            mnt_crossrd_3d()
        elif valid_input == "east":
            gen.clear()
            mnt_crossrd_4c()
        elif valid_input == "south":
            gen.clear()
            mnt_crossrd_3b()
        elif valid_input == "west":
            gen.clear()
            mnt_crossrd_2c()


def goblins_2b():
    """
    Checks if goblins-2b are alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Mountains-2B'
    """
    directions = ["north", "east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["goblins-2b"]:
        options = ["fight", "flee"]

        print(nar.GOBLINS_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If required item in inventory, victory scene
            if "frostfire" in gen.inventory:
                gen.enemies["goblins-2b"] = False

                print(nar.GOBLINS_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    mnt_crossrd_2c()
                elif valid_input == "east":
                    gen.clear()
                    mnt_crossrd_3b()
                elif valid_input == "south":
                    gen.clear()
                    mnt_crossrd_2a()
                elif valid_input == "west":
                    gen.clear()
                    mnt_crossrd_1b()
            # If required item not in inventory, defeat scene
            else:
                print(nar.GOBLINS_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                mnt_crossrd_2c()
            elif gen.flee_direction == ["east"]:
                mnt_crossrd_3b()
            elif gen.flee_direction == ["south"]:
                mnt_crossrd_2a()
            elif gen.flee_direction == ["west"]:
                mnt_crossrd_1b()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.GOBLINS_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            mnt_crossrd_2c()
        elif valid_input == "east":
            gen.clear()
            mnt_crossrd_3b()
        elif valid_input == "south":
            gen.clear()
            mnt_crossrd_2a()
        elif valid_input == "west":
            gen.clear()
            mnt_crossrd_1b()


def goblins_1a():
    """
    Checks if 'goblins-1a' are alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Mountains-1A'
    """
    directions = ["north", "east"]

    # If the specified enemy is 'alive'
    if gen.enemies["goblins-1a"]:
        options = ["fight", "flee"]

        print(nar.GOBLINS_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If required item in inventory, victory scene
            if "frostfire" in gen.inventory:
                gen.enemies["goblins-1a"] = False

                print(nar.GOBLINS_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    mnt_crossrd_1b()
                elif valid_input == "east":
                    gen.clear()
                    mnt_crossrd_2a()
            # If required item not in inventory, defeat scene
            else:
                print(nar.GOBLINS_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                mnt_crossrd_1b()
            elif gen.flee_direction == ["east"]:
                mnt_crossrd_2a()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.GOBLINS_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            mnt_crossrd_1b()
        elif valid_input == "east":
            gen.clear()
            mnt_crossrd_2a()


def mnt_crossrd_4a():
    """
    Runs a 'crossroad' scene. Grid ref. 'Mountains-4A'
    """
    directions = ["north", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        frostfire()
    elif valid_input == "west":
        gen.clear()
        mountains_desc()


def mnt_crossrd_3b():
    """
    Runs a 'crossroad' scene. Grid ref. 'Mountains-3B'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        tiger()
    elif valid_input == "east":
        gen.clear()
        frostfire()
    elif valid_input == "south":
        gen.clear()
        mountains_desc()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        goblins_2b()


def mnt_crossrd_2a():
    """
    Runs a 'crossroad' scene. Grid ref. 'Mountains-2A'
    """
    directions = ["north", "east", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        goblins_2b()
    elif valid_input == "east":
        gen.clear()
        mountains_desc()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        goblins_1a()


def mountains_desc():
    """
    Runs the 'Mountains Desc.' scene. Grid ref. 'Mountains-3A'
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
