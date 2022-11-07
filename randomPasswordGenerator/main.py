import random


if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    print("How many letters would you like in your password?")
    no_letters = int(input())
    print("How many symbols would you like?")
    no_symbols = int(input())
    print("How many numbers would you like?")
    no_numbers = int(input())

    no_total = no_numbers + no_symbols + no_letters

    letters_list = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    symbols_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    password = str()
    flag = bool(1)

    while flag:

        random_var = random.randint(0, 2)

        if random_var == 0:
            if no_letters > 0:
                no_letters = no_letters - 1
                password += str(random.choice(letters_list))
        elif random_var == 1:
            if no_symbols > 0:
                no_symbols = no_symbols - 1
                password += str(random.choice(symbols_list))
        else:
            if no_numbers > 0:
                no_numbers = no_numbers - 1
                password += str(random.choice(numbers_list))

        if no_symbols == 0 and no_numbers == 0 and no_letters == 0:
            flag = bool(0)

    print("Password is: " + password)
