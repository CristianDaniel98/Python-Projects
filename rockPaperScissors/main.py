import random
import rps_module

if __name__ == '__main__':
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    user_input = int(input())

    if user_input == 0:
        print(rps_module.rock)
    elif user_input == 1:
        print(rps_module.paper)
    elif user_input == 2:
        print(rps_module.scissors)
    else:
        print("Invalid input!")
        exit(-1)

    computer_input = random.randint(0,2)
    print("Computer chose: ")

    if computer_input == 0:
        print(rps_module.rock)
    elif computer_input == 1:
        print(rps_module.paper)
    elif computer_input == 2:
        print(rps_module.scissors)

    if user_input == computer_input:
        print("Tie! ")
    elif user_input == 0 and computer_input == 1:
        print("Computer wins!")
    elif user_input == 1 and computer_input == 2:
        print("Computer wins!")
    elif user_input == 2 and computer_input == 0:
        print("Computer wins!")
    else:
        print("You win!")
