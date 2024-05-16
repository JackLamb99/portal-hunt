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


def spider_1a():
    """
    Checks if 'spider-1a' is alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Caves-1A'
    """
    directions = ["north", "east"]

    # If the specified enemy is 'alive'
    if gen.enemies["spider-1a"]:
        options = ["fight", "flee"]

        print(nar.SPIDER_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if "everflame" in gen.inventory:
                gen.enemies["spider-1a"] = False

                print(nar.SPIDER_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    cave_crossrd_1b()
                elif valid_input == "east":
                    gen.clear()
                    print("Call cave_crossrd_2a() function")  # TO BE DEFINED
            # If required items not in inventory, defeat scene
            else:
                print(nar.SPIDER_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                cave_crossrd_1b()
            elif gen.flee_direction == ["east"]:
                print("Call cave_crossrd_2a() function")  # TO BE DEFINED

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.SPIDER_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            cave_crossrd_1b()
        elif valid_input == "east":
            gen.clear()
            print("Call cave_crossrd_2a() function")  # TO BE DEFINED


def spider_2b():
    """
    Checks if 'spider-2b' is alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Caves-2B'
    """
    directions = ["north", "east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["spider-2b"]:
        options = ["fight", "flee"]

        print(nar.SPIDER_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if "everflame" in gen.inventory:
                gen.enemies["spider-2b"] = False

                print(nar.SPIDER_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    cave_crossrd_2c()
                elif valid_input == "east":
                    gen.clear()
                    print("Call cave_crossrd_3b() function")  # TO BE DEFINED
                elif valid_input == "south":
                    gen.clear()
                    print("Call cave_crossrd_2a() function")  # TO BE DEFINED
                elif valid_input == "west":
                    gen.clear()
                    cave_crossrd_1b()
            # If required items not in inventory, defeat scene
            else:
                print(nar.SPIDER_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                cave_crossrd_2c()
            elif gen.flee_direction == ["east"]:
                print("Call cave_crossrd_3b() function")  # TO BE DEFINED
            elif gen.flee_direction == ["south"]:
                print("Call cave_crossrd_2a() function")  # TO BE DEFINED
            elif gen.flee_direction == ["west"]:
                cave_crossrd_1b()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.SPIDER_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            cave_crossrd_2c()
        elif valid_input == "east":
            gen.clear()
            print("Call cave_crossrd_3b() function")  # TO BE DEFINED
        elif valid_input == "south":
            gen.clear()
            print("Call cave_crossrd_2a() function")  # TO BE DEFINED
        elif valid_input == "west":
            gen.clear()
            cave_crossrd_1b()


def skeletons():
    """
    Checks if the 'skeletons' are alive (True) or dead (False), runs a 'fight'
    or 'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Caves-3C'
    """
    directions = ["north", "east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["skeletons"]:
        options = ["fight", "flee"]

        print(nar.SKELETONS_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if all(item in gen.inventory for item in [
                    "everflame", "mace"]):
                gen.enemies["skeletons"] = False

                print(nar.SKELETONS_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    print("Call cave_crossrd_3d() function")  # TO BE DEFINED
                elif valid_input == "east":
                    gen.clear()
                    print("Call cave_crossrd_4c() function")  # TO BE DEFINED
                elif valid_input == "south":
                    gen.clear()
                    print("Call cave_crossrd_3b() function")  # TO BE DEFINED
                elif valid_input == "west":
                    gen.clear()
                    cave_crossrd_2c()
            # If required items not in inventory, defeat scene
            else:
                print(nar.SKELETONS_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                print("Call cave_crossrd_3d() function")  # TO BE DEFINED
            elif gen.flee_direction == ["east"]:
                print("Call cave_crossrd_4c() function")  # TO BE DEFINED
            elif gen.flee_direction == ["south"]:
                print("Call cave_crossrd_3b() function")  # TO BE DEFINED
            elif gen.flee_direction == ["west"]:
                cave_crossrd_2c()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.SKELETONS_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            print("Call cave_crossrd_3d() function")  # TO BE DEFINED
        elif valid_input == "east":
            gen.clear()
            print("Call cave_crossrd_4c() function")  # TO BE DEFINED
        elif valid_input == "south":
            gen.clear()
            print("Call cave_crossrd_3b() function")  # TO BE DEFINED
        elif valid_input == "west":
            gen.clear()
            cave_crossrd_2c()


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
        gen.amend_flee_direction(valid_input)
        gen.clear()
        spider_2b()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        spider_1a()


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
        gen.amend_flee_direction(valid_input)
        gen.clear()
        skeletons()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        spider_2b()
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
