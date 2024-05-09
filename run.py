import narrative as nar

def lst_to_str(lst):
    return ", ".join(lst)

def main_menu():
    """
    Runs the main menu to start the program, includes the menu_text narrative
    """
    print(nar.menu_text)
    user_input = input("Enter 'start' to begin your quest: ")

    while user_input.lower() != "start":
        print("Invalid input. Please enter 'start' to begin your quest.\n")
        user_input = input("Enter 'start' to begin your quest: ")

    glade()

def glade():
    """
    Runs the Glade scene
    """
    directions = ["north", "east", "south", "west"]
    print(nar.glade_text)
    print(f"Directions: {lst_to_str(directions)}")
    user_input = input("Where would you like to go?: ")

    if user_input.lower() == "north":
        print("Call Mountains desc. function.")
    elif user_input.lower() == "east":
        print("Call Caves desc. function.")
    elif user_input.lower() == "south":
        print("Call Scorchlands desc. function.")
    elif user_input.lower() == "west":
        print("Call Wetlands desc. function.")
    else:
        print(f"Invalid direction. Please enter a valid direction: {lst_to_str(directions)}\n")
        user_input = input("Where would you like to go?: ")

run_game = main_menu()
run_game