import random

if __name__ == '__main__':
    lifes = 6
    flag = bool(1)
    print("Welcome to the Hangman!")
    words_list = ("apple", "orange", "purple", "acknowledge", "biological", "celebrity", "consumption", "development",
                  "enforcement", "fundamental")
    chosen_word = random.choice(words_list)
    length = len(chosen_word)
    word_print = str()
    word_print_list = list()
    check_words = 0
    check_input_user = 0
    words_add_list = list()
    counter = 0

    for x in range(length):
        word_print += "_"
        word_print_list.append("_")

    while flag:
        counter = 0
        check_words = 0
        check_input_user = 0
        print(word_print)
        word_print = ""
        print("You have " + str(lifes) + " lifes remain")
        print("Choose a letter")
        user_input = str(input())
        if words_add_list:
            for x in words_add_list:
                if x == user_input:
                    check_input_user = 1

        words_add_list.append(user_input)

        if check_input_user == 0:
            for x in chosen_word:
                if x == user_input:
                    check_words = 1
                    length -= 1
                    word_print_list[counter] = user_input
                counter = counter+1

            for x in word_print_list:
                word_print += x

            if check_words == 0:
                print("Wrong letter!")
                print("*******************************")
                lifes -= 1

            if lifes == 0:
                flag = bool(0)
                print("The word was " + chosen_word)
                print("Game over!")

            if length == 0:
                flag = bool(0)
                print(word_print)
                print("Congratz, You win!!")

        else:
            for x in word_print_list:
                word_print += x

            print("Letter already entered!")
            print("Choose other letter!")
            print("********************************")
