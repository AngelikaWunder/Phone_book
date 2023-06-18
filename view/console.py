rom .text import *
def menu()-> int:
    print (main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice)< 9:
            return int(choice)
        print (input_error)