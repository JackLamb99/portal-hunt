"""
'Scorchlands' path for Portal Hunt.

This module contains the functions and logic to navigate the 'Scorchlands' path
in Portal Hunt.

Includes; directions, locations, items, enemies, and the corresponding
interaction logic for each based on user input.

When required, functions are named based on the 'Scorchlands' grid reference
provided in the README.md.
"""
import narrative as nar
import general as gen
import glade


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
        print(f"Options: {gen.lst_to_str(options)}")

        valid_input = gen.get_valid_input("What would you like to do?: ",
                                          options)
        # Fight scene
        if valid_input == "fight":
            gen.clear()
            # If all required items in inventory, victory scene
            if "sabre" in gen.inventory:
                gen.enemies["wolves-4c"] = False

                print(nar.WOLVES_VICTORY_TEXT)
                print(f"Directions: {gen.lst_to_str(directions)}")

                valid_input = gen.get_valid_input(
                    "Where would you like to go?: ", directions)
                if valid_input == "north":
                    gen.clear()
                    scor_crossrd_4d()
                elif valid_input == "south":
                    gen.clear()
                    print("Call scor_crossrd_4b() function")  # TO BE DEFINED
                elif valid_input == "west":
                    gen.clear()
                    scor_crossrd_3c()
            # If required items not in inventory, defeat scene
            else:
                print(nar.WOLVES_DEFEAT_TEXT)
                print("Call end game function")  # TO BE DEFINED
        # Flee scene
        elif valid_input == "flee":
            gen.clear()
            print(f"You flee back to the {gen.lst_to_str(gen.flee_direction)}")

            if gen.flee_direction == ["north"]:
                scor_crossrd_4d()
            elif gen.flee_direction == ["south"]:
                print("Call scor_crossrd_4b() function")  # TO BE DEFINED
            elif gen.flee_direction == ["west"]:
                scor_crossrd_3c()

    # Else if the enemy is already defeated, 'cleared' scene
    else:
        print(nar.WOLVES_CLEARED_TEXT)
        print(f"Directions: {gen.lst_to_str(directions)}")

        valid_input = gen.get_valid_input("Where would you like to go?: ",
                                          directions)
        if valid_input == "north":
            gen.clear()
            scor_crossrd_4d()
        elif valid_input == "south":
            gen.clear()
            print("Call scor_crossrd_4b() function")  # TO BE DEFINED
        elif valid_input == "west":
            gen.clear()
            scor_crossrd_3c()


def scor_crossrd_2d():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-2D'
    """
    directions = ["east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

    valid_input = gen.get_valid_input("Where would you like to go?: ",
                                      directions)
    if valid_input == "east":
        gen.clear()
        scorchlands_desc()
    elif valid_input == "south":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        print("Call wolves_2c() function")  # TO BE DEFINED
    elif valid_input == "west":
        gen.clear()
        print("Call sabre() function")  # TO BE DEFINED


def scor_crossrd_3c():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-3C'
    """
    directions = ["north", "east", "south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

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
        print("Call crawler() function")  # TO BE DEFINED
    elif valid_input == "west":
        gen.amend_flee_direction(valid_input)
        gen.clear()
        print("Call wolves_2c() function")  # TO BE DEFINED


def scor_crossrd_4d():
    """
    Runs a 'crossroad' scene. Grid ref. 'Scorchlands-4D'
    """
    directions = ["south", "west"]

    print(nar.CROSSROAD_TEXT)
    print(f"Directions: {gen.lst_to_str(directions)}")

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
    print(f"Directions: {gen.lst_to_str(directions)}")

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
