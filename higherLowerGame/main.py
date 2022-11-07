import random


def check_user_input():
    usr_input = input("Choose A or B: ")
    if usr_input == "A":
        return usr_input
    elif usr_input == "B":
        return usr_input
    else:
        print("Invalid input!")
        return "0"


if __name__ == '__main__':
    celebrity = {
        1: {"Rihanna": 514000},
        2: {"Elon Musk": 60000},
        3: {"Neyman": 181000000},
        4: {"Ronaldo": 494000000},
        5: {"Messi": 371000000},
        6: {"Angelina Jolie": 14000000}
    }

    first = random.randint(1, 6)
    second = random.randint(1, 6)

    while first == second:
        second = random.randint(1, 6)

    score = 0
    flag = bool(1)
    while flag:
        input_user = "0"

        if score == 0:
            first_celebrity = celebrity[first]
        second_celebrity = celebrity[second]

        first = second

        for key in first_celebrity:
            first_name = key
        for key in second_celebrity:
            second_name = key

        print(first_name)
        print("VS")
        print(second_name)

        while input_user == "0":
            input_user = check_user_input()

        if input_user == "A":
            if first_celebrity[first_name] > second_celebrity[second_name]:
                score += 1
                first_celebrity = second_celebrity
                second = random.randint(1, 6)
                while first == second:
                    second = random.randint(1, 6)
            else:
                print("Your score is:" + str(score))
                flag = bool(0)

        if input_user == "B":
            if first_celebrity[first_name] < second_celebrity[second_name]:
                score += 1
                first_celebrity = second_celebrity
                second = random.randint(1, 6)
                while first == second:
                    second = random.randint(1, 6)
            else:
                print("Your score is:" + str(score))
                flag = bool(0)
