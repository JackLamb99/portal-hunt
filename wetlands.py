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


def wetlands_portal():
    """
    Runs the 'wetlands portal' scene, end of the 'Wetlands Path'
    """
    print(nar.WETLANDS_PORTAL_TEXT)
    gen.game_over()


def wtl_crossrd_1a():
    """
    Runs a 'crossroad' scene. Grid ref. 'Wetlands-1A'
    """
    directions = ["north", "east"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        serpent()
    elif valid_input == "east":
        gen.clear()
        trident()


def harpoon():
    """
    Checks if the 'harpoon' item is in the inventory.
    Runs an 'existing item' scene if true, allows player to 'keep' or 'return'
    the item.
    Runs a 'new item' scene if false, allows player to 'take' or 'leave' the
    item.
    Grid ref. 'Wetlands-1D'
    """
    directions = ["south"]

    # If the specified item already in the inventory
    if "harpoon" in gen.inventory:
        options = ["keep", "return"]

        print(nar.HARPOON_EXISTING_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "keep":
            print(nar.KEEP_ITEM_TEXT)
        elif valid_input == "return":
            gen.inventory.remove("harpoon")
            print(nar.RETURN_ITEM_TEXT)
    else:
        options = ["take", "leave"]

        print(nar.HARPOON_NEW_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "take":
            gen.inventory.append("harpoon")
            print(nar.TAKE_ITEM_TEXT)
        elif valid_input == "leave":
            print(nar.LEAVE_ITEM_TEXT)

    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "south":
        gen.clear()
        wtl_crossrd_1c()


def serpent():
    """
    Checks if the 'serpent' is alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Wetlands-1B'
    """
    directions = ["north", "east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["serpent"]:
        options = ["fight", "flee"]

        print(nar.SERPENT_DESC_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if all(item in gen.inventory for item in [
                    "elixir", "trident", "harpoon"]):
                gen.enemies["serpent"] = False

                print(nar.SERPENT_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    wtl_crossrd_1c()
                elif valid_input == "east":
                    gen.clear()
                    wtl_crossrd_2b()
                elif valid_input == "south":
                    gen.clear()
                    wtl_crossrd_1a()
                elif valid_input == "west":
                    gen.clear()
                    wetlands_portal()
            # If required items not in inventory, defeat scene
            else:
                print(nar.SERPENT_DEFEAT_TEXT)
                print("Game over! Your quest has ended in defeat.\n")
                gen.game_over()
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                wtl_crossrd_1c()
            elif gen.flee_direction == ["east"]:
                wtl_crossrd_2b()
            elif gen.flee_direction == ["south"]:
                wtl_crossrd_1a()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.SERPENT_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            wtl_crossrd_1c()
        elif valid_input == "east":
            gen.clear()
            wtl_crossrd_2b()
        elif valid_input == "south":
            gen.clear()
            wtl_crossrd_1a()
        elif valid_input == "west":
            gen.clear()
            wetlands_portal()


def trident():
    """
    Checks if the 'trident' item is in the inventory.
    Runs an 'existing item' scene if true, allows player to 'keep' or 'return'
    the item.
    Runs a 'new item' scene if false, allows player to 'take' or 'leave' the
    item.
    Grid ref. 'Wetlands-2A'
    """
    directions = ["north", "east", "west"]

    # If the specified item already in the inventory
    if "trident" in gen.inventory:
        options = ["keep", "return"]

        print(nar.TRIDENT_EXISTING_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "keep":
            print(nar.KEEP_ITEM_TEXT)
        elif valid_input == "return":
            gen.inventory.remove("trident")
            print(nar.RETURN_ITEM_TEXT)
    else:
        options = ["take", "leave"]

        print(nar.TRIDENT_NEW_ITEM_TEXT)
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "take":
            gen.inventory.append("trident")
            print(nar.TAKE_ITEM_TEXT)
        elif valid_input == "leave":
            print(nar.LEAVE_ITEM_TEXT)

    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        wtl_crossrd_2b()
    elif valid_input == "east":
        gen.clear()
        wtl_crossrd_3a()
    elif valid_input == "west":
        gen.clear()
        wtl_crossrd_1a()


def wtl_crossrd_2d():
    """
    Runs a 'crossroad' scene. Grid ref. 'Wetlands-2D'
    """
    directions = ["east", "south"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "east":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        leeches_3d()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        crocodile()


def wtl_crossrd_1c():
    """
    Runs a 'crossroad' scene. Grid ref. 'Wetlands-1C'
    """
    directions = ["north", "east", "south"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        harpoon()
    elif valid_input == "east":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        crocodile()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        serpent()


def wtl_crossrd_2b():
    """
    Runs a 'crossroad' scene. Grid ref. 'Wetlands-2B'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        crocodile()
    elif valid_input == "east":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        leeches_3b()
    elif valid_input == "south":
        gen.clear()
        trident()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        serpent()


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
        trident()


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

                print(nar.LEECHES_VICTORY_TEXT)
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
                    wtl_crossrd_2d()
            # If required items not in inventory, defeat scene
            else:
                print(nar.LEECHES_DEFEAT_TEXT)
                print("Game over! Your quest has ended in defeat.\n")
                gen.game_over()
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["east"]:
                wtl_crossrd_4d()
            elif gen.flee_direction == ["south"]:
                wtl_crossrd_3c()
            elif gen.flee_direction == ["west"]:
                wtl_crossrd_2d()

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
            wtl_crossrd_2d()


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
                    wtl_crossrd_2d()
                elif valid_input == "east":
                    gen.clear()
                    wtl_crossrd_3c()
                elif valid_input == "south":
                    gen.clear()
                    wtl_crossrd_2b()
                elif valid_input == "west":
                    gen.clear()
                    wtl_crossrd_1c()
            # If required items not in inventory, defeat scene
            else:
                print(nar.CROCODILE_DEFEAT_TEXT)
                print("Game over! Your quest has ended in defeat.\n")
                gen.game_over()
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                wtl_crossrd_2d()
            elif gen.flee_direction == ["east"]:
                wtl_crossrd_3c()
            elif gen.flee_direction == ["south"]:
                wtl_crossrd_2b()
            elif gen.flee_direction == ["west"]:
                wtl_crossrd_1c()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.CROCODILE_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            wtl_crossrd_2d()
        elif valid_input == "east":
            gen.clear()
            wtl_crossrd_3c()
        elif valid_input == "south":
            gen.clear()
            wtl_crossrd_2b()
        elif valid_input == "west":
            gen.clear()
            wtl_crossrd_1c()


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
                    wtl_crossrd_2b()
            # If required items not in inventory, defeat scene
            else:
                print(nar.LEECHES_DEFEAT_TEXT)
                print("Game over! Your quest has ended in defeat.\n")
                gen.game_over()
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
                wtl_crossrd_2b()

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
            wtl_crossrd_2b()


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
