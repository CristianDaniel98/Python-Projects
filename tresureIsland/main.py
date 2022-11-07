
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    choice = str(input("left or right ? "))
    if choice == "right" :
        print("Fall into a hole.")
        print("Game Over.")
    elif choice == "left":
        choice = str(input("swaim or wait? "))
        if choice == "swaim":
            print("Attacked by trout.")
            print("Game Over.")
        elif choice == "wait":
            choice = str(input("Which door? red, yellow or blue? "))
            if choice == "red":
                print("Burned by fire.")
                print("Game over.")
            elif choice == "blue":
                print("Eaten by beasts.")
                print("Game Over.")
            elif choice == "yellow":
                print("You win!")
            else:
                print("Invalid choice.")
                print("Game Over.")
        else:
            print("Invalid choice.")
            print("Game Over.")
    else:
        print("Invalid choice.")
        print("Game Over.")