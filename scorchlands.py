"""
'Scorchlands' path for Portal Hunt.

This module contains the functions and logic to navigate the 'Scorchlands' path
in Portal Hunt.

Includes; directions, locations, items, enemies, and the corresponding
interaction logic for each based on user input.

When required, functions are named based on the 'Scorchlands' grid reference
provided in the README.md.
"""
import colorama
from colorama import Fore
import narrative as nar
import general as gen
import glade
colorama.init(autoreset=True)


def scorchlands_portal():
    """
    Runs the 'scorchlands portal' scene, end of the 'Scorchlands Path'
    """
    print(nar.SCORCHLANDS_PORTAL_TEXT)
    gen.game_over()


def scor_crossrd_1a():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-1A'
    """
    directions = ["north", "east"]

    print(nar.CROSSROAD_TEXT)
    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        staff()
    elif valid_input == "east":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        golem()


def staff():
    """
    Checks if the 'staff' item is in the inventory.
    Runs an 'existing item' scene if true, allows player to 'keep' or 'return'
    the item.
    Runs a 'new item' scene if false, allows player to 'take' or 'leave' the
    item.
    Grid ref. 'Scorchlands-1B'
    """
    directions = ["north", "east", "south"]

    # If the specified item already in the inventory
    if "staff" in gen.inventory:
        options = ["keep", "return"]

        print(nar.STAFF_EXISTING_ITEM_TEXT)
        print(Fore.GREEN + f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "keep":
            print(nar.KEEP_ITEM_TEXT)
        elif valid_input == "return":
            gen.inventory.remove("staff")
            print(nar.RETURN_ITEM_TEXT)
    else:
        options = ["take", "leave"]

        print(nar.STAFF_NEW_ITEM_TEXT)
        print(Fore.GREEN + f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "take":
            gen.inventory.append("staff")
            print(nar.TAKE_ITEM_TEXT)
        elif valid_input == "leave":
            print(nar.LEAVE_ITEM_TEXT)

    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        scor_crossrd_1c()
    elif valid_input == "east":
        gen.clear()
        scor_crossrd_2b()
    elif valid_input == "south":
        gen.clear()
        scor_crossrd_1a()


def golem():
    """
    Checks if the 'golem' is alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Scorchlands-2A'
    """
    directions = ["north", "east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["golem"]:
        options = ["fight", "flee"]

        print(nar.GOLEM_DESC_TEXT)
        print(Fore.GREEN + f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if all(item in gen.inventory for item in [
                    "sabre", "staff", "earthshaker"]):
                gen.enemies["golem"] = False

                print(nar.GOLEM_VICTORY_TEXT)
                print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    scor_crossrd_2b()
                elif valid_input == "east":
                    gen.clear()
                    scor_crossrd_3a()
                elif valid_input == "south":
                    gen.clear()
                    scorchlands_portal()
                elif valid_input == "west":
                    gen.clear()
                    scor_crossrd_1a()
            # If required items not in inventory, defeat scene
            else:
                print(nar.GOLEM_DEFEAT_TEXT)
                print(nar.ASCII_GAME_OVER)
                gen.game_over()
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                scor_crossrd_2b()
            elif gen.flee_direction == ["east"]:
                scor_crossrd_3a()
            elif gen.flee_direction == ["west"]:
                scor_crossrd_1a()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.GOLEM_CLEARED_TEXT)
        print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            scor_crossrd_2b()
        elif valid_input == "east":
            gen.clear()
            scor_crossrd_3a()
        elif valid_input == "south":
            gen.clear()
            scorchlands_portal()
        elif valid_input == "west":
            gen.clear()
            scor_crossrd_1a()


def earthshaker():
    """
    Checks if the 'earthshaker' item is in the inventory.
    Runs an 'existing item' scene if true, allows player to 'keep' or 'return'
    the item.
    Runs a 'new item' scene if false, allows player to 'take' or 'leave' the
    item.
    Grid ref. 'Scorchlands-4A'
    """
    directions = ["west"]

    # If the specified item already in the inventory
    if "earthshaker" in gen.inventory:
        options = ["keep", "return"]

        print(nar.EARTHSHAKER_EXISTING_ITEM_TEXT)
        print(Fore.GREEN + f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "keep":
            print(nar.KEEP_ITEM_TEXT)
        elif valid_input == "return":
            gen.inventory.remove("earthshaker")
            print(nar.RETURN_ITEM_TEXT)
    else:
        options = ["take", "leave"]

        print(nar.EARTHSHAKER_NEW_ITEM_TEXT)
        print(Fore.GREEN + f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "take":
            gen.inventory.append("earthshaker")
            print(nar.TAKE_ITEM_TEXT)
        elif valid_input == "leave":
            print(nar.LEAVE_ITEM_TEXT)

    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "west":
        gen.clear()
        scor_crossrd_3a()


def scor_crossrd_1c():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-1C'
    """
    directions = ["east", "south"]

    print(nar.CROSSROAD_TEXT)
    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "east":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        wolves_2c()
    elif valid_input == "south":
        gen.clear()
        staff()


def scor_crossrd_2b():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-2B'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        wolves_2c()
    elif valid_input == "east":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        crawler()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        golem()
    elif valid_input == "west":
        gen.clear()
        staff()


def scor_crossrd_3a():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-3A'
    """
    directions = ["north", "east", "west"]

    print(nar.CROSSROAD_TEXT)
    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        crawler()
    elif valid_input == "east":
        gen.clear()
        earthshaker()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        golem()


def scor_crossrd_4b():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-4B'
    """
    directions = ["north", "west"]

    print(nar.CROSSROAD_TEXT)
    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        wolves_4c()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        crawler()


def sabre():
    """
    Checks if the 'sabre' item is in the inventory.
    Runs an 'existing item' scene if true, allows player to 'keep' or 'return'
    the item.
    Runs a 'new item' scene if false, allows player to 'take' or 'leave' the
    item.
    Grid ref. 'Scorchlands-1D'
    """
    directions = ["east"]

    # If the specified item already in the inventory
    if "sabre" in gen.inventory:
        options = ["keep", "return"]

        print(nar.SABRE_EXISTING_ITEM_TEXT)
        print(Fore.GREEN + f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "keep":
            print(nar.KEEP_ITEM_TEXT)
        elif valid_input == "return":
            gen.inventory.remove("sabre")
            print(nar.RETURN_ITEM_TEXT)
    else:
        options = ["take", "leave"]

        print(nar.SABRE_NEW_ITEM_TEXT)
        print(Fore.GREEN + f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input(
            "What would you like to do with this item?: ", options)
        if valid_input == "take":
            gen.inventory.append("sabre")
            print(nar.TAKE_ITEM_TEXT)
        elif valid_input == "leave":
            print(nar.LEAVE_ITEM_TEXT)

    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "east":
        gen.clear()
        scor_crossrd_2d()


def wolves_2c():
    """
    Checks if 'wolves-2c' are alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Scorchlands-2C'
    """
    directions = ["north", "east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["wolves-2c"]:
        options = ["fight", "flee"]

        print(nar.WOLVES_DESC_TEXT)
        print(Fore.GREEN + f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if "sabre" in gen.inventory:
                gen.enemies["wolves-2c"] = False

                print(nar.WOLVES_VICTORY_TEXT)
                print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    scor_crossrd_2d()
                elif valid_input == "east":
                    gen.clear()
                    scor_crossrd_3c()
                elif valid_input == "south":
                    gen.clear()
                    scor_crossrd_2b()
                elif valid_input == "west":
                    gen.clear()
                    scor_crossrd_1c()
            # If required items not in inventory, defeat scene
            else:
                print(nar.WOLVES_DEFEAT_TEXT)
                print(nar.ASCII_GAME_OVER)
                gen.game_over()
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                scor_crossrd_2d()
            elif gen.flee_direction == ["east"]:
                scor_crossrd_3c()
            elif gen.flee_direction == ["south"]:
                scor_crossrd_2b()
            elif gen.flee_direction == ["west"]:
                scor_crossrd_1c()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.WOLVES_CLEARED_TEXT)
        print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            scor_crossrd_2d()
        elif valid_input == "east":
            gen.clear()
            scor_crossrd_3c()
        elif valid_input == "south":
            gen.clear()
            scor_crossrd_2b()
        elif valid_input == "west":
            gen.clear()
            scor_crossrd_1c()


def crawler():
    """
    Checks if the 'crawler' is alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Scorchlands-3B'
    """
    directions = ["north", "east", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["crawler"]:
        options = ["fight", "flee"]

        print(nar.CRAWLER_DESC_TEXT)
        print(Fore.GREEN + f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if all(item in gen.inventory for item in [
                    "sabre", "staff"]):
                gen.enemies["crawler"] = False

                print(nar.CRAWLER_VICTORY_TEXT)
                print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    scor_crossrd_3c()
                elif valid_input == "east":
                    gen.clear()
                    scor_crossrd_4b()
                elif valid_input == "south":
                    gen.clear()
                    scor_crossrd_3a()
                elif valid_input == "west":
                    gen.clear()
                    scor_crossrd_2b()
            # If required items not in inventory, defeat scene
            else:
                print(nar.CRAWLER_DEFEAT_TEXT)
                print(nar.ASCII_GAME_OVER)
                gen.game_over()
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                scor_crossrd_3c()
            elif gen.flee_direction == ["east"]:
                scor_crossrd_4b()
            elif gen.flee_direction == ["south"]:
                scor_crossrd_3a()
            elif gen.flee_direction == ["west"]:
                scor_crossrd_2b()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.CRAWLER_CLEARED_TEXT)
        print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            scor_crossrd_3c()
        elif valid_input == "east":
            gen.clear()
            scor_crossrd_4b()
        elif valid_input == "south":
            gen.clear()
            scor_crossrd_3a()
        elif valid_input == "west":
            gen.clear()
            scor_crossrd_2b()


def wolves_4c():
    """
    Checks if 'wolves-4c' are alive (True) or dead (False), runs a 'fight' or
    'flee' scene if alive, runs a 'enemy cleared' scene if dead.
    Checks if the required item/s are in the 'Inventory' to determine the
    outcome of the 'fight'.
    Grid ref. 'Scorchlands-4C'
    """
    directions = ["north", "south", "west"]

    # If the specified enemy is 'alive'
    if gen.enemies["wolves-4c"]:
        options = ["fight", "flee"]

        print(nar.WOLVES_DESC_TEXT)
        print(Fore.GREEN + f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if "sabre" in gen.inventory:
                gen.enemies["wolves-4c"] = False

                print(nar.WOLVES_VICTORY_TEXT)
                print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    scor_crossrd_4d()
                elif valid_input == "south":
                    gen.clear()
                    scor_crossrd_4b()
                elif valid_input == "west":
                    gen.clear()
                    scor_crossrd_3c()
            # If required items not in inventory, defeat scene
            else:
                print(nar.WOLVES_DEFEAT_TEXT)
                print(nar.ASCII_GAME_OVER)
                gen.game_over()
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                scor_crossrd_4d()
            elif gen.flee_direction == ["south"]:
                scor_crossrd_4b()
            elif gen.flee_direction == ["west"]:
                scor_crossrd_3c()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.WOLVES_CLEARED_TEXT)
        print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            scor_crossrd_4d()
        elif valid_input == "south":
            gen.clear()
            scor_crossrd_4b()
        elif valid_input == "west":
            gen.clear()
            scor_crossrd_3c()


def scor_crossrd_2d():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-2D'
    """
    directions = ["east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "east":
        gen.clear()
        scorchlands_desc()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        wolves_2c()
    elif valid_input == "west":
        gen.clear()
        sabre()


def scor_crossrd_3c():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-3C'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        scorchlands_desc()
    elif valid_input == "east":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        wolves_4c()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        crawler()
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        wolves_2c()


def scor_crossrd_4d():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-4D'
    """
    directions = ["south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        wolves_4c()
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
    print(Fore.GREEN + f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "north":
        gen.clear()
        glade.glade()
    elif valid_input == "east":
        gen.clear()
        scor_crossrd_4d()
    elif valid_input == "south":
        gen.clear()
        scor_crossrd_3c()
    elif valid_input == "west":
        gen.clear()
        scor_crossrd_2d()
