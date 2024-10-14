print(r'''
 _                                       _      _                 _ 
| |                                     (_)    | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___   _ ___ | | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ | |/ __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | |\__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___| |_||___/_|\__,_|_| |_|\__,_|
''')

def choose_action():
    answer = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\": ").lower()
    if answer == "left":
        print("You've come to a lake. There is an island in the middle of the lake.")
        lake_scenario()
    elif answer == "right":
        print("You fell into a hole. Game over.")
    else:
        print("Please write \"left\" or \"right\".")
        choose_action()

def lake_scenario():
    answer = input("Type \"wait\" to wait for a boat or type \"swim\" to swim across.\n").lower()

    if answer == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        house_scenario()
    elif answer == "swim":
        print("You get attacked by an angry trout. Game over.")
    else:
        print("Please write \"wait\" or \"swim\".")
        lake_scenario()

def house_scenario():
    answer = input("Which color do you choose?\n").lower()

    if answer == "red":
        print("It's a room full of fire. Game over.")
    elif answer == "yellow":
        print("You found the treasure! You win!")
    elif answer == "blue":
        print("You enter a room full of beasts. Game over.")
    else:
        print("Please enter one of the colors mentioned above (red, yellow, blue).")
        house_scenario()

def continue_game():
    choice = input("Do you want to play again? Type \"yes\" or \"no\".").lower()

    if choice == "yes":
        return True
    elif choice == "no":
        print("Thank you for playing Treasure Island.")
        return False
    else:
        print("Please type either \"yes\" or \"no\".")
        continue_game()

game_is_on = True
while game_is_on:
    print("Welcome to the Treasure Island.\nYour mission is to find the treasure.\n")
    choose_action()

    if continue_game():
        game_is_on = True
    else:
        game_is_on = False

