import random

def print_dice(x):
    match x:
        case 1:
            print("===========")
            print("|         |")
            print("|    O    |")
            print("|         |")
            print("===========")
        case 2:
            print("===========")
            print("|         |")
            print("| O     O |")
            print("|         |")
            print("===========")
        case 3:
            print("===========")
            print("|    O    |")
            print("|    O    |")
            print("|    O    |")
            print("===========")
        case 4:
            print("===========")
            print("| O     O |")
            print("|         |")
            print("| O     O |")
            print("===========")
        case 5:
            print("===========")
            print("| O     O |")
            print("|    O    |")
            print("| O     O |")
            print("===========")
        case 6:
            print("===========")
            print("| O     O |")
            print("| O     O |")
            print("| O     O |")
            print("===========")
        case _:
            print("Error occurred")

def roll_random():
    return random.randint(1, 6)

def roll_dice_simulation():
    print_dice(roll_random())

def roll_dice_game():
    x = 'y'
    while x == 'y':
        roll_dice_simulation()
        x =  input("Press y to roll again\n")

roll_dice_game()