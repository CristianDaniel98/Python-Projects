def check_user_input(user_input_ls, input_list):
    check = 0
    user_list = input_list
    return_input = user_input_ls
    create_list = create_user_list(user_input_ls)
    input_list_length = len(create_list)
    for i in range(input_list_length):
        for j in range(len(input_list)):
            if user_input_ls[i] == input_list[j]:
                check += 1

    if check != input_list_length:
        print("Invalid input word!")
        print("Enter other word!")
        return_input = input()
        check_user_input(return_input, user_list)

    return str(return_input)


def check_shifting_count(shifting_count_fc):
    if shifting_count_fc > 26:
        print("Invalid shifting count")
        print("Enter other shifting count")
        shifting_count_fc = int(input())
        print("*********************************")
        check_shifting_count(shifting_count_fc)

    if shifting_count_fc < 0:
        print("Invalid shifting count")
        print("Enter other shifting count")
        shifting_count_fc = int(input())
        print("*********************************")
        check_shifting_count(shifting_count_fc)

    return shifting_count_fc


def create_user_list(user_input_fc):
    user_input_list_fc = ()
    for x in user_input_fc:
        user_input_list_fc += tuple(x)
    return user_input_list_fc


def caesarcipher_encode(length, user_input_fc, shifting_count_fc, input_list):
    length_while = int(length)
    length_list = len(input_list)
    cipher_code = str()

    while length_while > 0:
        for i in range(length):
            for j in range(len(input_list)):
                if user_input_fc[i] == input_list[j]:
                    index_list = j + int(shifting_count_fc)
                    if index_list >= length_list:
                        index_list = abs(index_list - len(input_list))
                    cipher_code += input_list[index_list]
                    length_while -= 1
    print("The encoded word is: " + cipher_code)
    print("*****************************************")


def caesarcipher_decode(length, user_input_fc, shifting_count_fc, input_list):
    length_while = int(length)
    cipher_code = str()

    while length_while > 0:
        for i in range(length):
            for j in range(len(input_list)):
                if user_input_fc[i] == input_list[j]:
                    index_list = j - int(shifting_count_fc)
                    if index_list < 0:
                        index_list = abs(index_list + len(input_list))
                    cipher_code += input_list[index_list]
                    length_while -= 1
    print("The decoded word is: " + cipher_code)
    print("*****************************************")


if __name__ == '__main__':
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

    flag = bool(1)

    while flag:
        print("Welcome to Caesar Cipher!")
        print("You want to encode or decode a word!")
        user_input_choose = str(input())

        if user_input_choose == "encode":
            print("Choose a word to encode: ")
            user_input = str(input())
            user_input = check_user_input(user_input, alphabet)
            user_input_list = create_user_list(user_input)
            input_length = len(user_input_list)
            print("Choose shifting number: ")
            shifting_count = int(input())
            shifting_count = check_shifting_count(shifting_count)
            caesarcipher_encode(input_length, user_input_list, shifting_count, alphabet)
            print("Do you want to continue, yes or no?")
            flag_inner = bool(1)
            while flag_inner:
                input_continue = str(input())
                if input_continue == "no":
                    flag = bool(0)
                    flag_inner = bool(0)
                elif input_continue == "yes":
                    flag_inner = bool(0)
                else:
                    print("Invalid input")
                    print("Choose a valid input")

        elif user_input_choose == "decode":
            print("Choose a word to decode: ")
            user_input = str(input())
            user_input = check_user_input(user_input, alphabet)
            user_input_list = create_user_list(user_input)
            input_length = len(user_input_list)
            print("Choose shifting number: ")
            shifting_count = int(input())
            shifting_count = check_shifting_count(shifting_count)
            caesarcipher_decode(input_length, user_input_list, shifting_count, alphabet)
            print("Do you want to continue, yes or no?")
            flag_inner = bool(1)
            while flag_inner:
                input_continue = str(input())
                if input_continue == "no":
                    flag = bool(0)
                    flag_inner = bool(0)
                elif input_continue == "yes":
                    flag_inner = bool(0)
                else:
                    print("Invalid input")
                    print("Choose a valid input")

        else:
            print("Invalid option!")
            print("********************************")
