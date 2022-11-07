import random

RANDOM_NUMBER = random.randint(1, 100)


def check_difficulty():
    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if user_input == "easy":
        return 10
    elif user_input == "hard":
        return 5
    else:
        print("Invalid input!")
        return 0


def check_user_number():
    input_number = int(input("Choose a number: "))
    if input_number < 0:
        print("Invalid input number!")
        return 0
    elif input_number > 100:
        print("Invalid input number!")
        return 0
    else:
        return input_number


if __name__ == '__main__':
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    user_tries = 0
    while user_tries == 0:
        user_tries = check_difficulty()

    print("You have " + str(user_tries) + " tries to guess the number!")

    while user_tries > 0:
        user_number = 0
        while user_number == 0:
            user_number = check_user_number()

        if user_number > RANDOM_NUMBER:
            print("Too high!")
            user_tries -= 1
            print("You have " + str(user_tries) + " attempts remaining to guess the number!")
        elif user_number < RANDOM_NUMBER:
            print("Too low!")
            user_tries -= 1
            print("You have " + str(user_tries) + " attempts remaining to guess the number!")
        else:
            print("Good job, you found the number!")
            exit(0)

    print("You lose, Searching number is: " + str(RANDOM_NUMBER))
