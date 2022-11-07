# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill? "))
    tip_percent = float(input("What parcentage tip would you like to give? 10, 12, or 15? "))
    no_people = int(input("How many people to split the bill? "))
    each_pay = str((total_bill + (total_bill*tip_percent)/100)/no_people)
    print("Each person should pay: " + each_pay)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
