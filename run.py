import narrative as nar

def main_menu():
    """
    Runs the main menu to start the program, includes the menu_text narrative
    """
    print(nar.menu_text)
    user_input = input("Enter 'start' to begin your quest: ")

    while user_input.lower() != "start":
        print("Invalid input. Please enter 'start' to begin your quest.\n")
        user_input = input("Enter 'start' to begin your quest: ")

    print("Call glade function here")

main_menu()